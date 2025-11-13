#!/usr/bin/env python3
"""
GenCCC Baseline Management
Create and compare requirements baselines for change control.

Baselines provide snapshots of requirements at specific points in time,
enabling impact analysis and change tracking.
"""

import argparse
import csv
import datetime
import json
import pathlib
import sys
from typing import Dict, List, Optional


# Repository paths
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
REQUIREMENTS_DIR = REPO_ROOT / "OPT-IN_FRAMEWORK" / "N-NEURAL_NETWORKS_USERS_TRACEABILITY" / "ATA_95_NEURAL_NETWORKS" / "95-00-00_GENERAL" / "95-00-03_Requirements"
BASELINES_DIR = REPO_ROOT / "cd" / "baselines"
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


def create_baseline(name: Optional[str] = None) -> pathlib.Path:
    """
    Create a baseline snapshot of current requirements.
    
    Args:
        name: Optional baseline name. If None, uses timestamp.
        
    Returns:
        Path to created baseline file
    """
    BASELINES_DIR.mkdir(parents=True, exist_ok=True)
    
    requirements = load_requirements()
    
    # Generate baseline filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if name:
        filename = f"requirements_{name}_{timestamp}.json"
    else:
        filename = f"requirements_{timestamp}.json"
    
    baseline_file = BASELINES_DIR / filename
    
    # Create baseline data
    baseline_data = {
        "created_at": datetime.datetime.now().isoformat(),
        "name": name or timestamp,
        "total_requirements": len(requirements),
        "requirements": requirements
    }
    
    # Write baseline
    with open(baseline_file, 'w', encoding='utf-8') as f:
        json.dump(baseline_data, f, indent=2)
    
    print(f"✅ Created baseline: {baseline_file}")
    print(f"   Total requirements: {len(requirements)}")
    
    return baseline_file


def list_baselines() -> List[pathlib.Path]:
    """List all available baselines."""
    if not BASELINES_DIR.exists():
        return []
    
    baselines = sorted(BASELINES_DIR.glob("requirements_*.json"), reverse=True)
    return baselines


def load_baseline(baseline_file: pathlib.Path) -> Dict:
    """Load a baseline file."""
    with open(baseline_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def compare_baselines(baseline1_path: pathlib.Path, baseline2_path: pathlib.Path) -> str:
    """
    Compare two baselines and generate diff report.
    
    Args:
        baseline1_path: Path to older baseline
        baseline2_path: Path to newer baseline
        
    Returns:
        Markdown formatted diff report
    """
    baseline1 = load_baseline(baseline1_path)
    baseline2 = load_baseline(baseline2_path)
    
    reqs1 = {req["ID"]: req for req in baseline1["requirements"]}
    reqs2 = {req["ID"]: req for req in baseline2["requirements"]}
    
    ids1 = set(reqs1.keys())
    ids2 = set(reqs2.keys())
    
    # Find changes
    added = ids2 - ids1
    removed = ids1 - ids2
    common = ids1 & ids2
    modified = []
    
    for req_id in common:
        req1 = reqs1[req_id]
        req2 = reqs2[req_id]
        
        # Check for modifications
        if req1 != req2:
            modified.append((req_id, req1, req2))
    
    # Generate report
    lines = [
        "# Baseline Comparison Report",
        "",
        f"**Baseline 1:** {baseline1['name']} ({baseline1['created_at']})",
        f"**Baseline 2:** {baseline2['name']} ({baseline2['created_at']})",
        "",
        "---",
        "",
        "## Summary",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Requirements in Baseline 1 | {len(ids1)} |",
        f"| Requirements in Baseline 2 | {len(ids2)} |",
        f"| Added | {len(added)} |",
        f"| Removed | {len(removed)} |",
        f"| Modified | {len(modified)} |",
        "",
    ]
    
    # Added requirements
    if added:
        lines.append(f"## Added Requirements ({len(added)})")
        lines.append("")
        for req_id in sorted(added):
            req = reqs2[req_id]
            lines.append(f"### {req_id}: {req['Title']}")
            lines.append(f"- **Status:** {req['Status']}")
            lines.append(f"- **Safety Level:** {req.get('SafetyLevel', 'N/A')}")
            lines.append(f"- **Text:** {req['Text'][:100]}...")
            lines.append("")
    
    # Removed requirements
    if removed:
        lines.append(f"## Removed Requirements ({len(removed)})")
        lines.append("")
        for req_id in sorted(removed):
            req = reqs1[req_id]
            lines.append(f"### {req_id}: {req['Title']}")
            lines.append(f"- **Status:** {req['Status']}")
            lines.append("")
    
    # Modified requirements
    if modified:
        lines.append(f"## Modified Requirements ({len(modified)})")
        lines.append("")
        for req_id, req1, req2 in sorted(modified, key=lambda x: x[0]):
            lines.append(f"### {req_id}: {req2['Title']}")
            lines.append("")
            
            # Compare fields
            fields_changed = []
            for key in req1.keys():
                if req1.get(key) != req2.get(key):
                    fields_changed.append(key)
            
            lines.append(f"**Fields changed:** {', '.join(fields_changed)}")
            lines.append("")
            
            for field in fields_changed:
                old_val = req1.get(field, "")
                new_val = req2.get(field, "")
                lines.append(f"- **{field}:**")
                lines.append(f"  - Old: `{old_val}`")
                lines.append(f"  - New: `{new_val}`")
            lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("## Change Impact Analysis")
    lines.append("")
    
    # Safety-critical changes
    safety_changes = []
    for req_id, req1, req2 in modified:
        if req1.get("SafetyLevel") in ["DAL-A", "DAL-B"] or req2.get("SafetyLevel") in ["DAL-A", "DAL-B"]:
            safety_changes.append((req_id, req1, req2))
    
    if safety_changes:
        lines.append(f"### ⚠️ Safety-Critical Changes ({len(safety_changes)})")
        lines.append("")
        lines.append("The following safety-critical requirements have been modified:")
        lines.append("")
        for req_id, req1, req2 in safety_changes:
            lines.append(f"- **{req_id}**: {req2['Title']}")
            if req1.get("SafetyLevel") != req2.get("SafetyLevel"):
                lines.append(f"  - Safety Level: {req1.get('SafetyLevel')} → {req2.get('SafetyLevel')}")
        lines.append("")
        lines.append("**Action Required:** These changes require additional review and re-verification.")
        lines.append("")
    
    return "\n".join(lines)


def cmd_create(args: argparse.Namespace) -> int:
    """Create a new baseline."""
    create_baseline(args.name)
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    """List all baselines."""
    baselines = list_baselines()
    
    if not baselines:
        print("No baselines found.")
        print("Create one with: genccc baseline create")
        return 0
    
    print(f"📦 Baselines ({len(baselines)})")
    print("=" * 80)
    
    for baseline_path in baselines:
        baseline = load_baseline(baseline_path)
        print(f"Name: {baseline['name']}")
        print(f"  File: {baseline_path.name}")
        print(f"  Created: {baseline['created_at']}")
        print(f"  Requirements: {baseline['total_requirements']}")
        print()
    
    return 0


def cmd_diff(args: argparse.Namespace) -> int:
    """Compare two baselines."""
    baselines = list_baselines()
    
    if len(baselines) < 2:
        print("❌ Need at least 2 baselines to compare.")
        print("Create baselines with: genccc baseline create")
        return 1
    
    # Determine baselines to compare
    if args.baseline1 and args.baseline2:
        # Use specified baselines
        baseline1_path = BASELINES_DIR / args.baseline1
        baseline2_path = BASELINES_DIR / args.baseline2
        
        if not baseline1_path.exists():
            print(f"❌ Baseline not found: {args.baseline1}")
            return 1
        if not baseline2_path.exists():
            print(f"❌ Baseline not found: {args.baseline2}")
            return 1
    else:
        # Compare latest two baselines
        baseline2_path = baselines[0]  # Most recent
        baseline1_path = baselines[1]  # Second most recent
        print(f"Comparing latest two baselines:")
        print(f"  Older: {baseline1_path.name}")
        print(f"  Newer: {baseline2_path.name}")
        print()
    
    # Generate diff
    diff_report = compare_baselines(baseline1_path, baseline2_path)
    
    # Save report
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_file = REPORTS_DIR / "baseline_diff.md"
    report_file.write_text(diff_report, encoding='utf-8')
    
    print(f"✅ Generated diff report: {report_file}")
    print()
    
    # Display summary
    lines = diff_report.split('\n')
    for line in lines[:30]:  # Show first 30 lines
        print(line)
    
    if len(lines) > 30:
        print(f"\n... ({len(lines) - 30} more lines in report file)")
    
    return 0


def main():
    """Main entry point for baseline management."""
    parser = argparse.ArgumentParser(
        description="GenCCC Baseline Management",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create a new baseline
  genccc baseline create --name "Release_1.0"
  
  # List all baselines
  genccc baseline list
  
  # Compare latest two baselines
  genccc baseline diff
  
  # Compare specific baselines
  genccc baseline diff --baseline1 requirements_20250101.json \\
                        --baseline2 requirements_20250201.json
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new baseline')
    create_parser.add_argument('--name', help='Baseline name')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all baselines')
    
    # Diff command
    diff_parser = subparsers.add_parser('diff', help='Compare two baselines')
    diff_parser.add_argument('--baseline1', help='First baseline filename')
    diff_parser.add_argument('--baseline2', help='Second baseline filename')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Execute command
    if args.command == 'create':
        return cmd_create(args)
    elif args.command == 'list':
        return cmd_list(args)
    elif args.command == 'diff':
        return cmd_diff(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
