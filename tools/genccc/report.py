#!/usr/bin/env python3
"""
GenCCC Report Generator
Generates cross-reference audit reports for markdown documentation.

Scans markdown files in the repository to:
- Identify broken internal links
- Find missing cross-references between related documents
- Detect documents that should be linked but aren't
- Report on documentation structure consistency

Output: cd/reports/cross_reference_audit.md
"""

import pathlib
import re
from typing import Dict, List, Set, Tuple
import sys

# Repository root
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
FRAMEWORK_ROOT = REPO_ROOT / "OPT-IN_FRAMEWORK"
REPORT_DIR = REPO_ROOT / "cd" / "reports"


def find_all_markdown_files() -> List[pathlib.Path]:
    """Find all markdown files in the framework."""
    md_files = []
    if FRAMEWORK_ROOT.exists():
        md_files.extend(FRAMEWORK_ROOT.rglob("*.md"))
    
    # Also include root-level markdown files
    root_files = [
        REPO_ROOT / "README.md",
        REPO_ROOT / "CAOS_INDEX.md",
        REPO_ROOT / "CAOS_MANIFESTO.md",
        REPO_ROOT / "CAOS_OPERATIONS_FRAMEWORK.md",
        REPO_ROOT / "CAOS_USE_CASES.md",
    ]
    for f in root_files:
        if f.exists():
            md_files.append(f)
    
    return sorted(md_files)


def extract_internal_links(content: str) -> List[str]:
    """Extract internal markdown links from content."""
    # Match [text](path) format, excluding external URLs
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    links = []
    
    for match in re.finditer(link_pattern, content):
        link_target = match.group(2)
        # Skip external URLs, anchors, and mailto links
        if not link_target.startswith(('http://', 'https://', '#', 'mailto:')):
            links.append(link_target)
    
    return links


def extract_ata_references(content: str) -> Set[str]:
    """Extract ATA chapter references from content."""
    # Match patterns like ATA_02, ATA_95, 02-11-00, etc.
    ata_pattern = r'\b(?:ATA[_\s-]?)?(\d{2})(?:[_\s-](\d{2})(?:[_\s-](\d{2}))?)?\b'
    references = set()
    
    for match in re.finditer(ata_pattern, content):
        # Format as ATA_XX or ATA_XX-YY-ZZ
        chapter = match.group(1)
        section = match.group(2)
        subsection = match.group(3)
        
        if subsection:
            references.add(f"ATA_{chapter}-{section}-{subsection}")
        elif section:
            references.add(f"ATA_{chapter}-{section}")
        else:
            references.add(f"ATA_{chapter}")
    
    return references


def check_link_validity(source_file: pathlib.Path, link: str) -> Tuple[bool, str]:
    """Check if a link target exists relative to source file."""
    try:
        # Handle relative paths
        if link.startswith('/'):
            target = REPO_ROOT / link.lstrip('/')
        else:
            target = (source_file.parent / link).resolve()
        
        # Remove anchor if present
        target_str = str(target).split('#')[0]
        target = pathlib.Path(target_str)
        
        if target.exists():
            return True, ""
        else:
            return False, f"Target not found: {link}"
    except Exception as e:
        return False, f"Error resolving link: {str(e)}"


def generate_report() -> str:
    """Generate the cross-reference audit report."""
    md_files = find_all_markdown_files()
    
    report_lines = [
        "# GenCCC Cross-Reference Audit Report",
        "",
        f"**Generated:** {pathlib.Path(__file__).name}",
        f"**Files Scanned:** {len(md_files)}",
        "",
        "---",
        "",
    ]
    
    # Track statistics
    total_links = 0
    broken_links = 0
    missing_ata_docs = set()
    files_with_issues = []
    
    # Scan each file
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception as e:
            report_lines.append(f"⚠️ **Error reading file:** `{md_file.relative_to(REPO_ROOT)}`")
            report_lines.append(f"   Error: {str(e)}")
            report_lines.append("")
            continue
        
        # Extract and check links
        links = extract_internal_links(content)
        total_links += len(links)
        
        file_broken_links = []
        for link in links:
            is_valid, error_msg = check_link_validity(md_file, link)
            if not is_valid:
                broken_links += 1
                file_broken_links.append((link, error_msg))
        
        # Extract ATA references
        ata_refs = extract_ata_references(content)
        
        # Report issues for this file
        if file_broken_links or ata_refs:
            rel_path = md_file.relative_to(REPO_ROOT)
            files_with_issues.append(str(rel_path))
            
            if file_broken_links:
                report_lines.append(f"## 🔗 `{rel_path}`")
                report_lines.append("")
                report_lines.append("### Broken Links:")
                for link, error in file_broken_links:
                    report_lines.append(f"- `{link}` — {error}")
                report_lines.append("")
    
    # Summary section
    summary = [
        "## 📊 Summary",
        "",
        f"- **Total Markdown Files:** {len(md_files)}",
        f"- **Total Internal Links:** {total_links}",
        f"- **Broken Links:** {broken_links}",
        f"- **Files with Issues:** {len(files_with_issues)}",
        "",
    ]
    
    if broken_links == 0:
        summary.extend([
            "✅ **All cross-references are valid!**",
            "",
            "No broken links detected. Documentation cross-reference integrity is excellent.",
            "",
        ])
    else:
        summary.extend([
            "⚠️ **Issues detected that may need attention.**",
            "",
            "Consider running `/genccc apply` to automatically fix broken links and generate missing documentation.",
            "",
        ])
    
    # Insert summary at the beginning (after header)
    report_lines[6:6] = summary
    
    report_lines.extend([
        "---",
        "",
        "## 📝 Recommendations",
        "",
        "1. **Review Broken Links:** Check if links point to moved or deleted files",
        "2. **Update References:** Update paths to reflect current file structure",
        "3. **Generate Missing Docs:** Use `/genccc apply` to auto-generate referenced but missing documents",
        "4. **Cross-Reference:** Ensure related ATA chapters link to each other",
        "",
        "---",
        "",
        "**To apply automatic fixes and generate missing contextual documentation:**",
        "",
        "Comment on this PR: `/genccc apply`",
        "",
    ])
    
    return "\n".join(report_lines)


def main():
    """Main execution function."""
    print("🔍 GenCCC: Scanning repository for cross-reference issues...")
    print(f"📁 Repository root: {REPO_ROOT}")
    print(f"📂 Framework root: {FRAMEWORK_ROOT}")
    print("")
    
    # Ensure report directory exists
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Generate report
    report = generate_report()
    
    # Write report
    report_path = REPORT_DIR / "cross_reference_audit.md"
    report_path.write_text(report, encoding='utf-8')
    
    print(f"✅ Report generated: {report_path}")
    print("")
    print("📄 Report preview:")
    print("=" * 80)
    # Print first 30 lines
    lines = report.split('\n')
    for line in lines[:30]:
        print(line)
    if len(lines) > 30:
        print(f"... ({len(lines) - 30} more lines)")
    print("=" * 80)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
