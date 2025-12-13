#!/usr/bin/env python3
# Copyright 2025 AMPEL360 Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# SPDX-License-Identifier: Apache-2.0

"""
Gate 1 — Cross-Reference Validator

Validates cross-references within documents, checking:
- Internal links (within same document)
- External links (to other documents in repo)
- Reference existence and accessibility
- Broken or malformed references

Usage:
    python tools/genccc/gate1_xref_validator.py \
        --artifact path/to/file.md \
        --chain .genccc/chain_state.json \
        --issues .genccc/issues/<id>.xref.json \
        --log .genccc/logs/<id>.xref.log \
        --repo-root /path/to/repo

Exit codes:
    0: Passed (no errors)
    1: Failed (errors found)
    2: Skipped (no references)
"""

import argparse
import json
import logging
import pathlib
import re
import sys
from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Tuple

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# ============================================================================
# CROSS-REFERENCE DETECTION
# ============================================================================

def extract_markdown_links(content: str) -> List[Tuple[str, str]]:
    """Extract markdown links [text](url) from content."""
    # Pattern: [text](url)
    pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    matches = re.findall(pattern, content)
    return matches


def extract_reference_style_links(content: str) -> List[Tuple[str, str]]:
    """Extract reference-style links [text]: url from content."""
    # Pattern: [ref]: url
    pattern = r"\[([^\]]+)\]:\s*(\S+)"
    matches = re.findall(pattern, content)
    return matches


def extract_internal_anchors(content: str) -> Set[str]:
    """Extract internal anchor targets from markdown headings."""
    anchors = set()
    
    # Markdown headings become anchors
    heading_pattern = r"^#+\s+(.+)$"
    for match in re.finditer(heading_pattern, content, re.MULTILINE):
        heading_text = match.group(1)
        # Convert to anchor: lowercase, spaces to hyphens, remove special chars
        anchor = re.sub(r"[^\w\s-]", "", heading_text.lower())
        anchor = re.sub(r"\s+", "-", anchor)
        anchors.add(anchor)
    
    # Explicit HTML anchors
    anchor_pattern = r'<a\s+(?:name|id)=["\']([^"\']+)["\']'
    for match in re.finditer(anchor_pattern, content, re.IGNORECASE):
        anchors.add(match.group(1))
    
    return anchors


def extract_document_references(content: str) -> List[str]:
    """Extract document ID references (e.g., REQ-XX-YY-ZZZ, DOC-XXX)."""
    patterns = [
        r"\bREQ-\d{2}-\d{2}-[A-Z]+-\d{3,6}\b",
        r"\bDOC-\d{2}-\d{2}-\d{3,6}\b",
        r"\b\d{2}-\d{2}-\d{2}-[A-Z]+-\d{3}\b",
        r"\bH-\d{2}-\d{2}-\d{2}\b",  # Hazard IDs
        r"\bTEST-\d{2}-\d{2}-\d{3}\b",  # Test IDs
    ]
    
    refs = []
    for pattern in patterns:
        refs.extend(re.findall(pattern, content))
    
    return refs


# ============================================================================
# VALIDATION CHECKS
# ============================================================================

class XRefIssue:
    """Represents a cross-reference validation issue."""
    
    SEVERITY_ERROR = "ERROR"
    SEVERITY_WARN = "WARN"
    SEVERITY_INFO = "INFO"
    
    def __init__(self, severity: str, code: str, message: str, 
                 link_text: Optional[str] = None, link_url: Optional[str] = None):
        self.severity = severity
        self.code = code
        self.message = message
        self.link_text = link_text
        self.link_url = link_url
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "severity": self.severity,
            "code": self.code,
            "message": self.message,
            "link_text": self.link_text,
            "link_url": self.link_url,
        }


def is_external_url(url: str) -> bool:
    """Check if URL is external (http/https/ftp)."""
    return url.startswith(("http://", "https://", "ftp://"))


def is_internal_anchor(url: str) -> bool:
    """Check if URL is internal anchor (#section)."""
    return url.startswith("#")


def resolve_relative_path(base_path: pathlib.Path, relative_url: str) -> pathlib.Path:
    """Resolve relative URL to absolute path."""
    # Remove anchor if present
    url_without_anchor = relative_url.split("#")[0]
    
    if not url_without_anchor:
        return base_path
    
    # Resolve relative to base file's directory
    base_dir = base_path.parent
    resolved = (base_dir / url_without_anchor).resolve()
    
    return resolved


def check_internal_anchors(
    content: str,
    internal_links: List[Tuple[str, str]]
) -> List[XRefIssue]:
    """Check internal anchor links."""
    issues = []
    
    # Extract available anchors
    available_anchors = extract_internal_anchors(content)
    
    for text, url in internal_links:
        if is_internal_anchor(url):
            anchor = url.lstrip("#")
            if anchor not in available_anchors:
                issues.append(XRefIssue(
                    XRefIssue.SEVERITY_ERROR,
                    "BROKEN_INTERNAL_ANCHOR",
                    f"Internal anchor not found: {anchor}",
                    link_text=text,
                    link_url=url
                ))
    
    return issues


def check_file_references(
    base_path: pathlib.Path,
    repo_root: pathlib.Path,
    file_links: List[Tuple[str, str]]
) -> List[XRefIssue]:
    """Check file reference links."""
    issues = []
    
    # Cache for parsed target file anchors to avoid re-reading
    anchor_cache: Dict[str, Set[str]] = {}
    
    # Size limit for target files (prevent reading huge files)
    MAX_TARGET_SIZE = 10 * 1024 * 1024  # 10MB
    
    for text, url in file_links:
        if is_external_url(url) or is_internal_anchor(url):
            continue
        
        # Remove anchor for file existence check
        url_parts = url.split("#")
        file_url = url_parts[0]
        anchor = url_parts[1] if len(url_parts) > 1 else None
        
        # Resolve path
        try:
            resolved_path = resolve_relative_path(base_path, file_url)
            
            # Check if path is within repo
            try:
                resolved_path.relative_to(repo_root)
            except ValueError:
                issues.append(XRefIssue(
                    XRefIssue.SEVERITY_WARN,
                    "EXTERNAL_REPO_REFERENCE",
                    f"Reference points outside repository: {file_url}",
                    link_text=text,
                    link_url=url
                ))
                continue
            
            # Check file existence
            if not resolved_path.exists():
                issues.append(XRefIssue(
                    XRefIssue.SEVERITY_ERROR,
                    "BROKEN_FILE_REFERENCE",
                    f"Referenced file not found: {file_url} (resolved to: {resolved_path})",
                    link_text=text,
                    link_url=url
                ))
            elif anchor:
                # If anchor specified, validate it exists in target (with caching and size limits)
                try:
                    # Check file size first
                    file_size = resolved_path.stat().st_size
                    if file_size > MAX_TARGET_SIZE:
                        issues.append(XRefIssue(
                            XRefIssue.SEVERITY_WARN,
                            "TARGET_FILE_TOO_LARGE",
                            f"Target file too large to validate anchor: {file_url} ({file_size} bytes)",
                            link_text=text,
                            link_url=url
                        ))
                        continue
                    
                    # Check cache first
                    target_path_str = str(resolved_path)
                    if target_path_str not in anchor_cache:
                        target_content = resolved_path.read_text(encoding="utf-8")
                        anchor_cache[target_path_str] = extract_internal_anchors(target_content)
                    
                    target_anchors = anchor_cache[target_path_str]
                    if anchor not in target_anchors:
                        issues.append(XRefIssue(
                            XRefIssue.SEVERITY_WARN,
                            "BROKEN_ANCHOR_IN_TARGET",
                            f"Anchor not found in target file: {anchor}",
                            link_text=text,
                            link_url=url
                        ))
                except Exception as e:
                    logger.debug(f"Could not check anchor in target: {e}")
        
        except Exception as e:
            issues.append(XRefIssue(
                XRefIssue.SEVERITY_ERROR,
                "INVALID_FILE_REFERENCE",
                f"Could not resolve file reference: {file_url} ({e})",
                link_text=text,
                link_url=url
            ))
    
    return issues


def check_document_references(
    repo_root: pathlib.Path,
    doc_refs: List[str]
) -> List[XRefIssue]:
    """Check document ID references."""
    issues = []
    
    # For now, just report the references found (INFO level)
    # In a full implementation, we would search for these IDs in a database
    # or throughout the repository
    
    if doc_refs:
        unique_refs = sorted(set(doc_refs))
        issues.append(XRefIssue(
            XRefIssue.SEVERITY_INFO,
            "DOCUMENT_REFERENCES_FOUND",
            f"Found {len(unique_refs)} document references: {', '.join(unique_refs[:10])}{'...' if len(unique_refs) > 10 else ''}",
        ))
    
    return issues


# ============================================================================
# MAIN GATE 1 VALIDATION LOGIC
# ============================================================================

def validate_cross_references(
    file_path: pathlib.Path,
    repo_root: pathlib.Path
) -> Dict[str, Any]:
    """
    Run Gate 1 cross-reference validation on artifact.
    
    Returns:
        Result dictionary with status, issues, and statistics
    """
    logger.info(f"Validating cross-references: {file_path}")
    
    # Read file content
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return {
            "status": "error",
            "error": f"Failed to read file: {e}",
            "links_found": 0,
            "references_found": 0,
        }
    
    # Extract all links and references
    markdown_links = extract_markdown_links(content)
    reference_links = extract_reference_style_links(content)
    doc_refs = extract_document_references(content)
    
    all_links = markdown_links + reference_links
    
    if not all_links and not doc_refs:
        logger.info(f"No cross-references found in {file_path}")
        return {
            "status": "skipped",
            "links_found": 0,
            "references_found": 0,
            "issues": [],
        }
    
    logger.info(f"Found {len(all_links)} links and {len(doc_refs)} document references")
    
    # Run validation checks
    issues = []
    
    # Separate internal and file links
    internal_links = [(t, u) for t, u in all_links if is_internal_anchor(u)]
    file_links = [(t, u) for t, u in all_links if not is_external_url(u)]
    
    # 1. Check internal anchors
    if internal_links:
        issues.extend(check_internal_anchors(content, internal_links))
    
    # 2. Check file references
    if file_links:
        issues.extend(check_file_references(file_path, repo_root, file_links))
    
    # 3. Check document references
    if doc_refs:
        issues.extend(check_document_references(repo_root, doc_refs))
    
    # Determine overall status
    has_errors = any(i.severity == XRefIssue.SEVERITY_ERROR for i in issues)
    
    if has_errors:
        status = "failed"
    elif issues:
        status = "passed_with_warnings"
    else:
        status = "passed"
    
    return {
        "status": status,
        "links_found": len(all_links),
        "references_found": len(doc_refs),
        "issues": [i.to_dict() for i in issues],
    }


# ============================================================================
# CHAIN STATE & REPORTING
# ============================================================================

def update_chain_state(
    chain_file: pathlib.Path,
    artifact_path: pathlib.Path,
    result: Dict[str, Any]
) -> None:
    """Update chain state JSON file with Gate 1 result."""
    chain_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Load existing chain state
    if chain_file.exists():
        try:
            with open(chain_file, "r", encoding="utf-8") as f:
                chain_state = json.load(f)
        except json.JSONDecodeError:
            chain_state = {"artifacts": []}
    else:
        chain_state = {"artifacts": []}
    
    # Find or create artifact entry
    artifact_id = str(artifact_path)
    artifact_entry = None
    for entry in chain_state["artifacts"]:
        if entry.get("path") == artifact_id:
            artifact_entry = entry
            break
    
    if artifact_entry is None:
        artifact_entry = {"path": artifact_id}
        chain_state["artifacts"].append(artifact_entry)
    
    # Update with Gate 1 result
    artifact_entry["gate1_xref"] = {
        "status": result["status"],
        "links_found": result["links_found"],
        "references_found": result["references_found"],
        "error_count": sum(1 for i in result.get("issues", []) if i["severity"] == "ERROR"),
        "warning_count": sum(1 for i in result.get("issues", []) if i["severity"] == "WARN"),
    }
    
    # Write chain state
    with open(chain_file, "w", encoding="utf-8") as f:
        json.dump(chain_state, f, indent=2, ensure_ascii=False)
    
    logger.info(f"Updated chain state: {chain_file}")


def write_issues_file(issues_file: pathlib.Path, result: Dict[str, Any]) -> None:
    """Write detailed issues to JSON file."""
    issues_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(issues_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    logger.info(f"Wrote issues file: {issues_file}")


def write_log_file(log_file: pathlib.Path, result: Dict[str, Any]) -> None:
    """Write human-readable log file."""
    log_file.parent.mkdir(parents=True, exist_ok=True)
    
    lines = [
        f"Gate 1 — Cross-Reference Validator",
        f"{'=' * 60}",
        f"",
        f"Status: {result['status'].upper()}",
        f"Links Found: {result['links_found']}",
        f"Document References Found: {result['references_found']}",
        f"",
    ]
    
    if result.get("error"):
        lines.append(f"Error: {result['error']}")
        lines.append("")
    
    issues = result.get("issues", [])
    if issues:
        lines.append(f"Issues Found: {len(issues)}")
        lines.append("")
        
        # Group by severity
        for severity in ["ERROR", "WARN", "INFO"]:
            severity_issues = [i for i in issues if i["severity"] == severity]
            if severity_issues:
                lines.append(f"{severity}S ({len(severity_issues)}):")
                lines.append("-" * 60)
                for issue in severity_issues:
                    link_info = ""
                    if issue.get("link_text"):
                        link_info = f" [{issue['link_text']}]"
                    if issue.get("link_url"):
                        link_info += f" ({issue['link_url']})"
                    
                    lines.append(f"  [{issue['code']}]{link_info}")
                    lines.append(f"    {issue['message']}")
                    lines.append("")
    else:
        lines.append("No issues found.")
        lines.append("")
    
    lines.append(f"{'=' * 60}")
    lines.append(f"Generated: {datetime.now().isoformat()}")
    
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    logger.info(f"Wrote log file: {log_file}")


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Gate 1 — Cross-Reference Validator"
    )
    parser.add_argument(
        "--artifact",
        type=pathlib.Path,
        required=True,
        help="Path to artifact to validate"
    )
    parser.add_argument(
        "--repo-root",
        type=pathlib.Path,
        default=pathlib.Path.cwd(),
        help="Repository root path"
    )
    parser.add_argument(
        "--chain",
        type=pathlib.Path,
        default=pathlib.Path(".genccc/chain_state.json"),
        help="Path to chain state JSON file"
    )
    parser.add_argument(
        "--issues",
        type=pathlib.Path,
        help="Path to issues JSON file"
    )
    parser.add_argument(
        "--log",
        type=pathlib.Path,
        help="Path to log file"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Resolve paths
    artifact_path = args.artifact.resolve()
    repo_root = args.repo_root.resolve()
    
    if not artifact_path.exists():
        logger.error(f"Artifact not found: {artifact_path}")
        sys.exit(2)
    
    # Auto-generate issues and log paths if not provided
    artifact_id = artifact_path.stem
    if args.issues is None:
        args.issues = pathlib.Path(f".genccc/issues/{artifact_id}.xref.json")
    if args.log is None:
        args.log = pathlib.Path(f".genccc/logs/{artifact_id}.xref.log")
    
    # Run validation
    result = validate_cross_references(artifact_path, repo_root)
    
    # Update chain state
    update_chain_state(args.chain, artifact_path, result)
    
    # Write issues and log files
    write_issues_file(args.issues, result)
    write_log_file(args.log, result)
    
    # Print summary
    print(f"\nGate 1 — Cross-Reference Validator")
    print(f"{'=' * 60}")
    print(f"Artifact: {artifact_path}")
    print(f"Status: {result['status'].upper()}")
    print(f"Links Found: {result['links_found']}")
    print(f"Document References: {result['references_found']}")
    
    if result.get("issues"):
        error_count = sum(1 for i in result["issues"] if i["severity"] == "ERROR")
        warn_count = sum(1 for i in result["issues"] if i["severity"] == "WARN")
        print(f"Errors: {error_count}")
        print(f"Warnings: {warn_count}")
    
    print(f"\nDetails:")
    print(f"  Chain state: {args.chain}")
    print(f"  Issues: {args.issues}")
    print(f"  Log: {args.log}")
    
    # Exit with appropriate code
    if result["status"] == "skipped":
        sys.exit(2)
    elif result["status"] == "failed":
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
