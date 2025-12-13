#!/usr/bin/env python3
# Copyright 2025 AMPEL360 Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

"""
Gate 0 — Metadata Coherence Screen

Validates metadata presence, parseability, completeness, and coherence
against path and naming conventions. Runs before any other machine validation
to provide early fail-fast behavior.

Usage:
    python tools/genccc/gate0_metadata_screen.py \
        --artifact path/to/file.md \
        --chain .genccc/chain_state.json \
        --issues .genccc/issues/<id>.metadata.json \
        --log .genccc/logs/<id>.metadata.log

Exit codes:
    0: Passed (no errors)
    1: Failed (errors found)
    2: Skipped (no metadata detected)
"""

import argparse
import json
import logging
import pathlib
import re
import sys
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

import yaml

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# ============================================================================
# METADATA DETECTION
# ============================================================================

def has_yaml_frontmatter(content: str) -> bool:
    """Check if content has YAML front-matter block (--- ... ---)."""
    return content.strip().startswith("---") and "\n---" in content


def extract_yaml_frontmatter(content: str) -> Optional[Dict[str, Any]]:
    """Extract and parse YAML front-matter from markdown content."""
    if not has_yaml_frontmatter(content):
        return None
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    
    try:
        return yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        logger.error(f"YAML parsing error: {e}")
        return None


def has_metadata_signature(content: str) -> bool:
    """Check if content contains recognized metadata signatures."""
    signatures = [
        r"document_id:",
        r"utcs_id:",
        r"ata_chapter:",
        r"optin_axis:",
        r"axis:",
        r"## Document Information",
        r"\*\*Document ID\*\*:",
    ]
    for sig in signatures:
        if re.search(sig, content, re.IGNORECASE):
            return True
    return False


def extract_inline_metadata(content: str) -> Dict[str, Any]:
    """Extract metadata from inline markdown patterns."""
    metadata = {}
    
    # Pattern: **Key**: Value or - **Key**: Value
    patterns = [
        (r"\*\*Document ID\*\*:\s*(.+?)(?:\n|$)", "document_id"),
        (r"\*\*Title\*\*:\s*(.+?)(?:\n|$)", "title"),
        (r"\*\*Version\*\*:\s*(.+?)(?:\n|$)", "version"),
        (r"\*\*Date\*\*:\s*(.+?)(?:\n|$)", "date"),
        (r"\*\*Status\*\*:\s*(.+?)(?:\n|$)", "status"),
        (r"\*\*Classification\*\*:\s*(.+?)(?:\n|$)", "classification"),
        (r"\*\*Author\*\*:\s*(.+?)(?:\n|$)", "author"),
        (r"\*\*ATA Chapter\*\*:\s*(.+?)(?:\n|$)", "ata_chapter"),
        (r"\*\*Category\*\*:\s*(.+?)(?:\n|$)", "category"),
    ]
    
    for pattern, key in patterns:
        match = re.search(pattern, content, re.MULTILINE)
        if match:
            metadata[key] = match.group(1).strip()
    
    return metadata


def is_schema_file(file_path: pathlib.Path) -> bool:
    """Check if file is a schema-bearing file."""
    return file_path.suffix.lower() in [".json", ".yaml", ".yml"]


def detect_metadata(file_path: pathlib.Path, content: str) -> Tuple[bool, Optional[Dict[str, Any]]]:
    """
    Detect and extract metadata from file.
    
    Returns:
        (metadata_detected: bool, metadata: Optional[Dict])
    """
    # Check for YAML front-matter first
    if has_yaml_frontmatter(content):
        metadata = extract_yaml_frontmatter(content)
        return True, metadata
    
    # Check for inline metadata signatures
    if has_metadata_signature(content):
        metadata = extract_inline_metadata(content)
        return True, metadata if metadata else {}
    
    # Check if schema file
    if is_schema_file(file_path):
        try:
            if file_path.suffix == ".json":
                metadata = json.loads(content)
            else:
                metadata = yaml.safe_load(content)
            return True, metadata
        except (json.JSONDecodeError, yaml.YAMLError):
            return True, None  # Detected but unparseable
    
    return False, None


# ============================================================================
# VALIDATION CHECKS
# ============================================================================

class ValidationIssue:
    """Represents a validation issue."""
    
    SEVERITY_ERROR = "ERROR"
    SEVERITY_WARN = "WARN"
    SEVERITY_INFO = "INFO"
    
    def __init__(self, severity: str, code: str, message: str, field: Optional[str] = None):
        self.severity = severity
        self.code = code
        self.message = message
        self.field = field
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "severity": self.severity,
            "code": self.code,
            "message": self.message,
            "field": self.field,
        }


def check_parseability(file_path: pathlib.Path, content: str) -> List[ValidationIssue]:
    """Check if metadata is parseable."""
    issues = []
    
    # YAML front-matter
    if has_yaml_frontmatter(content):
        try:
            extract_yaml_frontmatter(content)
        except Exception as e:
            issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_ERROR,
                "PARSE_YAML_FRONTMATTER",
                f"YAML front-matter parsing failed: {e}"
            ))
    
    # JSON/YAML files
    if is_schema_file(file_path):
        try:
            if file_path.suffix == ".json":
                json.loads(content)
            else:
                yaml.safe_load(content)
        except json.JSONDecodeError as e:
            issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_ERROR,
                "PARSE_JSON",
                f"JSON parsing failed: {e}"
            ))
        except yaml.YAMLError as e:
            issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_ERROR,
                "PARSE_YAML",
                f"YAML parsing failed: {e}"
            ))
    
    return issues


def check_required_keys(metadata: Optional[Dict[str, Any]]) -> List[ValidationIssue]:
    """Check if required metadata keys are present."""
    issues = []
    
    if metadata is None:
        issues.append(ValidationIssue(
            ValidationIssue.SEVERITY_ERROR,
            "METADATA_UNPARSEABLE",
            "Metadata detected but could not be parsed"
        ))
        return issues
    
    # Required keys (configurable based on policy)
    required_keys = [
        "document_id",
        "title",
        "version",
        "status",
    ]
    
    for key in required_keys:
        if key not in metadata or not metadata[key]:
            issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_ERROR,
                "MISSING_REQUIRED_KEY",
                f"Required metadata key missing or empty: {key}",
                field=key
            ))
    
    # Optional but recommended keys
    recommended_keys = ["date", "author", "classification"]
    for key in recommended_keys:
        if key not in metadata or not metadata[key]:
            issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_WARN,
                "MISSING_RECOMMENDED_KEY",
                f"Recommended metadata key missing: {key}",
                field=key
            ))
    
    return issues


def extract_axis_from_path(file_path: pathlib.Path) -> Optional[str]:
    """Extract OPT-IN axis from file path."""
    path_str = str(file_path)
    
    # Pattern: OPT-IN_FRAMEWORK/{AXIS}-{NAME}/...
    # Match full axis names: O, P, T, I, N
    axis_patterns = [
        r"OPT-IN_FRAMEWORK/(O|P|T|I|N)-",
        r"/(O|P|T|I|N)-[A-Z_]+/",
    ]
    
    for pattern in axis_patterns:
        match = re.search(pattern, path_str)
        if match:
            return match.group(1)
    
    return None


def extract_ata_chapter_from_path(file_path: pathlib.Path) -> Optional[str]:
    """Extract ATA chapter from file path."""
    path_str = str(file_path)
    
    # Pattern: ATA_{XX}-{NAME} or {XX}-{YY}-{ZZ}_NAME
    ata_patterns = [
        r"ATA_(\d{2})-",
        r"/(\d{2})-\d{2}-\d{2}_",
        r"/(\d{2})-\d{2}_",
    ]
    
    for pattern in ata_patterns:
        match = re.search(pattern, path_str)
        if match:
            return match.group(1)
    
    return None


def validate_version_format(version: str) -> bool:
    """Validate version format (e.g., R01, 1.0, v1.0)."""
    patterns = [
        r"^R\d{2}$",  # R01, R02, etc.
        r"^\d+\.\d+$",  # 1.0, 2.1, etc.
        r"^v?\d+\.\d+(\.\d+)?$",  # v1.0, v1.0.0, 1.0.0, etc.
    ]
    
    for pattern in patterns:
        if re.match(pattern, version):
            return True
    
    return False


def validate_date_format(date_str: str) -> bool:
    """Validate date format (ISO-8601) with semantic validation."""
    patterns = [
        (r"^(\d{4})-(\d{2})-(\d{2})$", True),  # YYYY-MM-DD with validation
        (r"^(\d{4})-(\d{2})-(\d{2})T\d{2}:\d{2}:\d{2}", False),  # ISO-8601 with time (basic check)
    ]
    
    for pattern, validate_semantic in patterns:
        match = re.match(pattern, date_str)
        if match:
            if validate_semantic:
                # Validate month and day ranges
                year, month, day = match.groups()
                year_int, month_int, day_int = int(year), int(month), int(day)
                
                # Basic range checks
                if month_int < 1 or month_int > 12:
                    return False
                if day_int < 1 or day_int > 31:
                    return False
                
                # Month-specific day validation
                if month_int in [4, 6, 9, 11] and day_int > 30:
                    return False
                if month_int == 2 and day_int > 29:
                    return False
            
            return True
    
    return False


def validate_utcs_id_format(utcs_id: str) -> bool:
    """Validate UTCS ID format."""
    # Basic pattern - adjust based on actual UTCS ID specification
    pattern = r"^[A-Z0-9]+-\d{2}-[A-Z0-9]+-\d{3,6}$"
    return re.match(pattern, utcs_id) is not None


def check_coherence(
    file_path: pathlib.Path,
    metadata: Optional[Dict[str, Any]]
) -> List[ValidationIssue]:
    """Check metadata coherence with path and naming conventions."""
    issues = []
    
    if metadata is None:
        return issues
    
    # 1. Check optin_axis vs path
    path_axis = extract_axis_from_path(file_path)
    meta_axis = metadata.get("optin_axis") or metadata.get("axis")
    
    if path_axis and meta_axis:
        if path_axis != meta_axis:
            issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_ERROR,
                "AXIS_MISMATCH",
                f"OPT-IN axis mismatch: path indicates '{path_axis}', metadata says '{meta_axis}'",
                field="optin_axis"
            ))
    elif path_axis and not meta_axis:
        issues.append(ValidationIssue(
            ValidationIssue.SEVERITY_WARN,
            "AXIS_MISSING",
            f"Path indicates OPT-IN axis '{path_axis}' but metadata missing optin_axis field",
            field="optin_axis"
        ))
    
    # 2. Check ata_chapter vs path
    path_ata = extract_ata_chapter_from_path(file_path)
    meta_ata = metadata.get("ata_chapter")
    
    if path_ata and meta_ata:
        # Normalize: "95 - Digital Product Passport" -> "95"
        meta_ata_normalized = re.match(r"(\d{2})", str(meta_ata))
        if meta_ata_normalized:
            meta_ata_normalized = meta_ata_normalized.group(1)
        else:
            meta_ata_normalized = str(meta_ata)
        
        if path_ata != meta_ata_normalized:
            issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_ERROR,
                "ATA_CHAPTER_MISMATCH",
                f"ATA chapter mismatch: path indicates '{path_ata}', metadata says '{meta_ata_normalized}'",
                field="ata_chapter"
            ))
    
    # 3. Check document_id vs filename
    doc_id = metadata.get("document_id")
    if doc_id:
        filename_stem = file_path.stem
        # Check if document_id appears in filename
        if doc_id not in filename_stem:
            issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_WARN,
                "DOCUMENT_ID_FILENAME_MISMATCH",
                f"Document ID '{doc_id}' not found in filename '{filename_stem}'",
                field="document_id"
            ))
    
    # 4. Check version format
    version = metadata.get("version")
    if version and not validate_version_format(str(version)):
        issues.append(ValidationIssue(
            ValidationIssue.SEVERITY_ERROR,
            "INVALID_VERSION_FORMAT",
            f"Invalid version format: '{version}' (expected R01, 1.0, or v1.0.0)",
            field="version"
        ))
    
    # 5. Check date format
    date = metadata.get("date")
    if date and not validate_date_format(str(date)):
        issues.append(ValidationIssue(
            ValidationIssue.SEVERITY_ERROR,
            "INVALID_DATE_FORMAT",
            f"Invalid date format: '{date}' (expected ISO-8601: YYYY-MM-DD)",
            field="date"
        ))
    
    # 6. Check UTCS ID format (if present)
    utcs_id = metadata.get("utcs_id")
    if utcs_id and not validate_utcs_id_format(str(utcs_id)):
        issues.append(ValidationIssue(
            ValidationIssue.SEVERITY_WARN,
            "INVALID_UTCS_ID_FORMAT",
            f"UTCS ID format may be invalid: '{utcs_id}'",
            field="utcs_id"
        ))
    
    return issues


# ============================================================================
# MAIN GATE 0 SCREENING LOGIC
# ============================================================================

def screen_artifact(file_path: pathlib.Path) -> Dict[str, Any]:
    """
    Run Gate 0 metadata coherence screen on artifact.
    
    Returns:
        Result dictionary with status, issues, and metadata
    """
    logger.info(f"Screening artifact: {file_path}")
    
    # Read file content
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return {
            "status": "error",
            "detected": False,
            "error": f"Failed to read file: {e}",
        }
    
    # Detect metadata
    detected, metadata = detect_metadata(file_path, content)
    
    if not detected:
        logger.info(f"No metadata detected in {file_path}")
        return {
            "status": "skipped",
            "detected": False,
            "parsed": True,
            "missing_keys": [],
            "mismatches": [],
            "issues": [],
        }
    
    logger.info(f"Metadata detected in {file_path}")
    
    # Run validation checks
    issues = []
    
    # 1. Parseability
    issues.extend(check_parseability(file_path, content))
    
    # 2. Required keys (only if metadata was parsed)
    if metadata is not None:
        issues.extend(check_required_keys(metadata))
    
    # 3. Coherence rules
    issues.extend(check_coherence(file_path, metadata))
    
    # Determine overall status
    has_errors = any(i.severity == ValidationIssue.SEVERITY_ERROR for i in issues)
    parsed = metadata is not None
    
    if has_errors:
        status = "failed"
    elif issues:
        status = "passed_with_warnings"
    else:
        status = "passed"
    
    # Collect missing keys and mismatches for summary
    missing_keys = [i.field for i in issues if i.code == "MISSING_REQUIRED_KEY"]
    mismatches = [i.field for i in issues if "MISMATCH" in i.code]
    
    return {
        "status": status,
        "detected": True,
        "parsed": parsed,
        "missing_keys": missing_keys,
        "mismatches": mismatches,
        "issues": [i.to_dict() for i in issues],
        "metadata": metadata,
    }


# ============================================================================
# CHAIN STATE & REPORTING
# ============================================================================

def update_chain_state(
    chain_file: pathlib.Path,
    artifact_path: pathlib.Path,
    result: Dict[str, Any]
) -> None:
    """Update chain state JSON file with Gate 0 result."""
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
    
    # Update with Gate 0 result (bounded summary only)
    artifact_entry["gate0_metadata"] = {
        "status": result["status"],
        "detected": result["detected"],
        "parsed": result["parsed"],
        "missing_keys": result["missing_keys"],
        "mismatches": result["mismatches"],
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
        f"Gate 0 — Metadata Coherence Screen",
        f"{'=' * 60}",
        f"",
        f"Status: {result['status'].upper()}",
        f"Metadata Detected: {result['detected']}",
        f"Metadata Parsed: {result['parsed']}",
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
                    field_info = f" [field: {issue['field']}]" if issue.get("field") else ""
                    lines.append(f"  [{issue['code']}]{field_info}")
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
        description="Gate 0 — Metadata Coherence Screen"
    )
    parser.add_argument(
        "--artifact",
        type=pathlib.Path,
        required=True,
        help="Path to artifact to screen"
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
        help="Path to issues JSON file (default: .genccc/issues/<artifact-id>.metadata.json)"
    )
    parser.add_argument(
        "--log",
        type=pathlib.Path,
        help="Path to log file (default: .genccc/logs/<artifact-id>.metadata.log)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Resolve artifact path
    artifact_path = args.artifact.resolve()
    if not artifact_path.exists():
        logger.error(f"Artifact not found: {artifact_path}")
        sys.exit(2)
    
    # Auto-generate issues and log paths if not provided
    artifact_id = artifact_path.stem
    if args.issues is None:
        args.issues = pathlib.Path(f".genccc/issues/{artifact_id}.metadata.json")
    if args.log is None:
        args.log = pathlib.Path(f".genccc/logs/{artifact_id}.metadata.log")
    
    # Run screening
    result = screen_artifact(artifact_path)
    
    # Update chain state
    update_chain_state(args.chain, artifact_path, result)
    
    # Write issues and log files
    write_issues_file(args.issues, result)
    write_log_file(args.log, result)
    
    # Print summary
    print(f"\nGate 0 — Metadata Coherence Screen")
    print(f"{'=' * 60}")
    print(f"Artifact: {artifact_path}")
    print(f"Status: {result['status'].upper()}")
    print(f"Metadata Detected: {result['detected']}")
    print(f"Metadata Parsed: {result['parsed']}")
    
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
        sys.exit(2)  # Skipped (no metadata)
    elif result["status"] == "failed":
        sys.exit(1)  # Failed (errors found)
    else:
        sys.exit(0)  # Passed


if __name__ == "__main__":
    main()
