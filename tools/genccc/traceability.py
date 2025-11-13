#!/usr/bin/env python3
"""
GenCCC Traceability Matrix Generator
Generates Requirements Traceability Matrix (RTM) and Verification Coverage Matrix.

Integrates with req.py to provide comprehensive traceability from requirements
to verification methods and evidence artifacts.
"""

import csv
import pathlib
import sys
from typing import Dict, List, Set


# Repository paths
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
REQUIREMENTS_DIR = REPO_ROOT / "OPT-IN_FRAMEWORK" / "N-NEURAL_NETWORKS_USERS_TRACEABILITY" / "ATA_95_NEURAL_NETWORKS" / "95-00-00_GENERAL" / "95-00-03_Requirements"
EVIDENCE_DIR = REPO_ROOT / "EVIDENCE"
REPORTS_DIR = REPO_ROOT / "cd" / "reports"


def load_requirements() -> List[Dict[str, str]]:
    """Load all requirements from CSV file."""
    req_file = REQUIREMENTS_DIR / "requirements.csv"
    
    if not req_file.exists():
        return []
    
    requirements = []
    with open(req_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            requirements.append(row)
    
    return requirements


def find_evidence_files() -> Dict[str, List[str]]:
    """
    Find evidence files and map them to requirement IDs.
    
    Returns:
        Dictionary mapping requirement ID to list of evidence file paths
    """
    evidence_map = {}
    
    if not EVIDENCE_DIR.exists():
        return evidence_map
    
    # Scan evidence directory for files
    for evidence_file in EVIDENCE_DIR.rglob("*"):
        if evidence_file.is_file():
            # Extract requirement IDs from filename or content
            filename = evidence_file.name
            
            # Pattern: RQ-XX-YY-#### in filename
            import re
            matches = re.findall(r'RQ-\d{2}-\d{2}-\d{4}', filename)
            
            for req_id in matches:
                if req_id not in evidence_map:
                    evidence_map[req_id] = []
                rel_path = str(evidence_file.relative_to(REPO_ROOT))
                evidence_map[req_id].append(rel_path)
    
    return evidence_map


def generate_rtm() -> str:
    """Generate Requirements Traceability Matrix in markdown format."""
    requirements = load_requirements()
    
    if not requirements:
        return "# Requirements Traceability Matrix\n\nNo requirements found.\n"
    
    lines = [
        "# Requirements Traceability Matrix (RTM)",
        "",
        f"**Generated:** {pathlib.Path(__file__).name}",
        f"**Total Requirements:** {len(requirements)}",
        "",
        "This matrix provides traceability from requirements to their parent requirements,",
        "verification methods, and evidence artifacts.",
        "",
        "---",
        ""
    ]
    
    # Group by status
    status_groups = {}
    for req in requirements:
        status = req.get("Status", "Unknown")
        if status not in status_groups:
            status_groups[status] = []
        status_groups[status].append(req)
    
    # Summary section
    lines.append("## Summary by Status")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|--------|-------|")
    for status, reqs in sorted(status_groups.items()):
        lines.append(f"| {status} | {len(reqs)} |")
    lines.append("")
    
    # Detailed traceability table
    lines.append("## Detailed Traceability")
    lines.append("")
    lines.append("| ID | Title | Status | Parent | Verification | Evidence |")
    lines.append("|----|-------|--------|--------|--------------|----------|")
    
    evidence_map = find_evidence_files()
    
    for req in sorted(requirements, key=lambda r: r["ID"]):
        req_id = req["ID"]
        title = req["Title"][:50] + "..." if len(req["Title"]) > 50 else req["Title"]
        status = req["Status"]
        parent = req["ParentID"] or "—"
        verification = req["VerificationMethod"] or "—"
        
        # Evidence
        evidence_files = evidence_map.get(req_id, [])
        if evidence_files:
            evidence = f"{len(evidence_files)} file(s)"
        else:
            evidence = "⚠️ None"
        
        lines.append(f"| {req_id} | {title} | {status} | {parent} | {verification} | {evidence} |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Legend")
    lines.append("")
    lines.append("**Verification Methods:**")
    lines.append("- T = Test")
    lines.append("- A = Analysis")
    lines.append("- I = Inspection")
    lines.append("- D = Demonstration")
    lines.append("- N/A = Not Applicable")
    lines.append("")
    
    return "\n".join(lines)


def generate_coverage_matrix() -> str:
    """Generate Verification Coverage Matrix in markdown format."""
    requirements = load_requirements()
    evidence_map = find_evidence_files()
    
    if not requirements:
        return "# Verification Coverage Matrix\n\nNo requirements found.\n"
    
    lines = [
        "# Verification Coverage Matrix",
        "",
        f"**Generated:** {pathlib.Path(__file__).name}",
        f"**Total Requirements:** {len(requirements)}",
        "",
        "This matrix tracks verification coverage for each requirement.",
        "",
        "---",
        ""
    ]
    
    # Calculate coverage statistics
    total_reqs = len(requirements)
    reqs_with_verification = len([r for r in requirements if r.get("VerificationMethod") and r["VerificationMethod"] != "N/A"])
    reqs_with_evidence = len([r for r in requirements if r["ID"] in evidence_map])
    fully_covered = len([r for r in requirements if r.get("VerificationMethod") and r["VerificationMethod"] != "N/A" and r["ID"] in evidence_map])
    
    coverage_pct = (fully_covered / total_reqs * 100) if total_reqs > 0 else 0
    
    # Summary
    lines.append("## Coverage Summary")
    lines.append("")
    lines.append(f"| Metric | Count | Percentage |")
    lines.append(f"|--------|-------|------------|")
    lines.append(f"| Total Requirements | {total_reqs} | 100% |")
    lines.append(f"| With Verification Method | {reqs_with_verification} | {reqs_with_verification/total_reqs*100:.1f}% |")
    lines.append(f"| With Evidence | {reqs_with_evidence} | {reqs_with_evidence/total_reqs*100:.1f}% |")
    lines.append(f"| **Fully Covered** | **{fully_covered}** | **{coverage_pct:.1f}%** |")
    lines.append("")
    
    # Coverage status
    if coverage_pct >= 95:
        status_icon = "✅"
        status_text = "Excellent coverage"
    elif coverage_pct >= 80:
        status_icon = "✓"
        status_text = "Good coverage"
    elif coverage_pct >= 60:
        status_icon = "⚠️"
        status_text = "Needs improvement"
    else:
        status_icon = "❌"
        status_text = "Insufficient coverage"
    
    lines.append(f"{status_icon} **Coverage Status:** {status_text}")
    lines.append("")
    
    # Gaps analysis
    lines.append("## Coverage Gaps")
    lines.append("")
    
    missing_verification = [r for r in requirements if not r.get("VerificationMethod") or r["VerificationMethod"] == "N/A"]
    missing_evidence = [r for r in requirements if r.get("VerificationMethod") and r["VerificationMethod"] != "N/A" and r["ID"] not in evidence_map]
    
    if missing_verification:
        lines.append(f"### Requirements Missing Verification Method ({len(missing_verification)})")
        lines.append("")
        for req in missing_verification[:10]:  # Show first 10
            lines.append(f"- **{req['ID']}**: {req['Title'][:60]}")
        if len(missing_verification) > 10:
            lines.append(f"- ... and {len(missing_verification) - 10} more")
        lines.append("")
    
    if missing_evidence:
        lines.append(f"### Requirements Missing Evidence ({len(missing_evidence)})")
        lines.append("")
        for req in missing_evidence[:10]:  # Show first 10
            lines.append(f"- **{req['ID']}**: {req['Title'][:60]} (Method: {req['VerificationMethod']})")
        if len(missing_evidence) > 10:
            lines.append(f"- ... and {len(missing_evidence) - 10} more")
        lines.append("")
    
    # Detailed coverage table
    lines.append("## Detailed Coverage")
    lines.append("")
    lines.append("| ID | Title | Verification | Evidence | Status |")
    lines.append("|----|-------|--------------|----------|--------|")
    
    for req in sorted(requirements, key=lambda r: r["ID"]):
        req_id = req["ID"]
        title = req["Title"][:40] + "..." if len(req["Title"]) > 40 else req["Title"]
        verification = req["VerificationMethod"] or "—"
        evidence_files = evidence_map.get(req_id, [])
        
        if verification and verification != "N/A" and evidence_files:
            status = "✅ Covered"
        elif verification and verification != "N/A":
            status = "⚠️ No Evidence"
        elif evidence_files:
            status = "⚠️ No Method"
        else:
            status = "❌ Not Covered"
        
        evidence = f"{len(evidence_files)}" if evidence_files else "0"
        
        lines.append(f"| {req_id} | {title} | {verification} | {evidence} | {status} |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Recommendations")
    lines.append("")
    lines.append("1. Assign verification methods to all requirements")
    lines.append("2. Create evidence artifacts in `EVIDENCE/` directory")
    lines.append("3. Use requirement IDs in evidence filenames for automatic linking")
    lines.append("4. Target 100% coverage for safety-critical requirements (DAL-A, DAL-B)")
    lines.append("")
    
    return "\n".join(lines)


def generate_csv_rtm() -> None:
    """Generate RTM in CSV format for tool import."""
    requirements = load_requirements()
    evidence_map = find_evidence_files()
    
    output_file = REPORTS_DIR / "Requirements_Traceability_Matrix.csv"
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Title", "Status", "ParentID", "VerificationMethod", "EvidenceCount", "SafetyLevel"])
        
        for req in sorted(requirements, key=lambda r: r["ID"]):
            evidence_count = len(evidence_map.get(req["ID"], []))
            writer.writerow([
                req["ID"],
                req["Title"],
                req["Status"],
                req["ParentID"],
                req["VerificationMethod"],
                evidence_count,
                req["SafetyLevel"]
            ])
    
    print(f"✅ Generated CSV RTM: {output_file}")


def generate_csv_coverage() -> None:
    """Generate Coverage Matrix in CSV format."""
    requirements = load_requirements()
    evidence_map = find_evidence_files()
    
    output_file = REPORTS_DIR / "Verification_Coverage_Matrix.csv"
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Title", "VerificationMethod", "EvidenceFiles", "CoverageStatus"])
        
        for req in sorted(requirements, key=lambda r: r["ID"]):
            verification = req.get("VerificationMethod", "")
            evidence_files = evidence_map.get(req["ID"], [])
            
            if verification and verification != "N/A" and evidence_files:
                status = "Covered"
            elif verification and verification != "N/A":
                status = "No Evidence"
            elif evidence_files:
                status = "No Method"
            else:
                status = "Not Covered"
            
            evidence_str = ";".join(evidence_files) if evidence_files else ""
            
            writer.writerow([
                req["ID"],
                req["Title"],
                verification,
                evidence_str,
                status
            ])
    
    print(f"✅ Generated CSV Coverage Matrix: {output_file}")


def main():
    """Generate all traceability matrices."""
    print("🔗 GenCCC Traceability Matrix Generator")
    print("=" * 80)
    print()
    
    requirements = load_requirements()
    
    if not requirements:
        print("⚠️  No requirements found. Use 'genccc req new' to create requirements.")
        return 1
    
    print(f"📋 Found {len(requirements)} requirements")
    print()
    
    # Ensure output directory exists
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Generate markdown RTM
    rtm_md = generate_rtm()
    rtm_file = REPORTS_DIR / "requirements_traceability_matrix.md"
    rtm_file.write_text(rtm_md, encoding='utf-8')
    print(f"✅ Generated RTM: {rtm_file}")
    
    # Generate markdown coverage matrix
    coverage_md = generate_coverage_matrix()
    coverage_file = REPORTS_DIR / "verification_coverage_matrix.md"
    coverage_file.write_text(coverage_md, encoding='utf-8')
    print(f"✅ Generated Coverage Matrix: {coverage_file}")
    
    # Generate CSV versions
    generate_csv_rtm()
    generate_csv_coverage()
    
    print()
    print("=" * 80)
    print("✅ Traceability matrices generated successfully!")
    print()
    print("Next steps:")
    print("  1. Review coverage gaps in verification_coverage_matrix.md")
    print("  2. Add verification methods to requirements using 'genccc req edit'")
    print("  3. Create evidence artifacts in EVIDENCE/ directory")
    print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
