#!/usr/bin/env python3
"""
Loop Packet Status Checker

This script checks the status of Loop Packets and validates consistency
between the CSV register and actual Loop Packet files.

Usage:
    python check_loop_status.py [--bb-id BB_ID] [--summary] [--validate]
"""

import argparse
import csv
import sys
from pathlib import Path


def load_register(register_path):
    """Load the BB Identity Register CSV."""
    artifacts = []
    with open(register_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            artifacts.append(row)
    return artifacts


def check_artifact_status(artifact, loops_base):
    """Check the status of a single artifact's Loop Packet."""
    bb_id = artifact['bb_id']
    loop_path = loops_base / bb_id
    
    status = {
        'bb_id': bb_id,
        'name': artifact['artifact_name'],
        'exists': loop_path.exists(),
        'files': {},
        'next_action': '',
        'issues': []
    }
    
    if not loop_path.exists():
        status['issues'].append(f"Loop Packet directory does not exist: {loop_path}")
        return status
    
    # Check for required files
    required_files = [
        f"LOOP_{bb_id}.md",
        f"AM_{bb_id}.md",
        f"DV_{bb_id}.md",
        f"DPP_{bb_id}.md",
        f"OM_{bb_id}.md",
        f"OAV_{bb_id}.md",
        f"DT_{bb_id}.md"
    ]
    
    for filename in required_files:
        file_path = loop_path / filename
        status['files'][filename] = file_path.exists()
        if not file_path.exists():
            status['issues'].append(f"Missing file: {filename}")
    
    # Compute next action based on statuses
    am_status = artifact.get('am_status', 'NOT_STARTED')
    dv_status = artifact.get('dv_status', 'NOT_STARTED')
    dpp_status = artifact.get('dpp_status', 'NOT_ISSUED')
    om_status = artifact.get('om_status', 'NOT_DEFINED')
    oav_status = artifact.get('oav_status', 'NOT_STARTED')
    
    if am_status == 'NOT_STARTED':
        status['next_action'] = "Write AM (At-Rest Model) first"
        status['next_gate'] = "DV"
    elif dv_status not in ['PASSED', 'APPROVED']:
        status['next_action'] = "Complete DV and mark DV gate"
        status['next_gate'] = "DV"
    elif dpp_status == 'NOT_ISSUED' and dv_status in ['PASSED', 'APPROVED']:
        status['next_action'] = "Issue DPP (locked identity + claims)"
        status['next_gate'] = "OAV"
    elif om_status == 'NOT_DEFINED':
        status['next_action'] = "Author OM (what DPP predicts operationally)"
        status['next_gate'] = "OAV"
    elif oav_status not in ['PASSED', 'APPROVED']:
        status['next_action'] = "Define/Execute OAV (asset context truth validation)"
        status['next_gate'] = "OAV"
    else:
        status['next_action'] = "Append DT snapshot and propose AM′ (change-controlled update)"
        status['next_gate'] = "COMPLETE"
    
    # Validate next_gate consistency
    register_next_gate = artifact.get('next_gate', '')
    if register_next_gate and register_next_gate != status['next_gate']:
        status['issues'].append(
            f"next_gate mismatch: CSV has '{register_next_gate}', computed '{status['next_gate']}'"
        )
    
    return status


def print_artifact_status(status, verbose=False):
    """Print the status of a single artifact."""
    print(f"\n{'='*80}")
    print(f"BB ID: {status['bb_id']}")
    print(f"Name:  {status['name']}")
    print(f"{'='*80}")
    
    if not status['exists']:
        print("❌ Loop Packet directory does NOT exist")
        return
    
    print("✅ Loop Packet directory exists")
    
    if verbose:
        print(f"\nFiles:")
        for filename, exists in status['files'].items():
            icon = "✅" if exists else "❌"
            print(f"  {icon} {filename}")
    
    missing_count = sum(1 for exists in status['files'].values() if not exists)
    if missing_count > 0:
        print(f"\n⚠️  {missing_count} file(s) missing")
    else:
        print(f"\n✅ All 7 files present")
    
    print(f"\nNext Gate: {status['next_gate']}")
    print(f"Next Action: {status['next_action']}")
    
    if status['issues']:
        print(f"\n⚠️  Issues ({len(status['issues'])}):")
        for issue in status['issues']:
            print(f"  - {issue}")


def print_summary(all_statuses):
    """Print a summary of all artifacts."""
    print(f"\n{'='*80}")
    print(f"LOOP PACKET STATUS SUMMARY")
    print(f"{'='*80}")
    
    total = len(all_statuses)
    with_loops = sum(1 for s in all_statuses if s['exists'])
    complete = sum(1 for s in all_statuses if all(s['files'].values()))
    with_issues = sum(1 for s in all_statuses if s['issues'])
    
    print(f"\nTotal Artifacts: {total}")
    print(f"With Loop Packets: {with_loops} ({with_loops/total*100:.1f}%)")
    print(f"Complete (7 files): {complete} ({complete/total*100:.1f}%)")
    print(f"With Issues: {with_issues}")
    
    print(f"\nNext Gates:")
    gate_counts = {}
    for status in all_statuses:
        gate = status['next_gate']
        gate_counts[gate] = gate_counts.get(gate, 0) + 1
    
    for gate, count in sorted(gate_counts.items()):
        print(f"  {gate}: {count}")
    
    if with_issues > 0:
        print(f"\n⚠️  Artifacts with Issues:")
        for status in all_statuses:
            if status['issues']:
                print(f"  - {status['bb_id']}: {len(status['issues'])} issue(s)")


def main():
    parser = argparse.ArgumentParser(
        description="Check the status of Loop Packets",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Check status of a specific artifact
    python check_loop_status.py --bb-id 27-BB-008

    # Show summary of all artifacts
    python check_loop_status.py --summary

    # Validate consistency and show detailed issues
    python check_loop_status.py --validate --verbose
        """
    )
    
    parser.add_argument('--bb-id', help='Check specific BB ID')
    parser.add_argument('--summary', action='store_true', help='Show summary of all artifacts')
    parser.add_argument('--validate', action='store_true', help='Validate consistency')
    parser.add_argument('--verbose', action='store_true', help='Show detailed file status')
    
    args = parser.parse_args()
    
    # Determine paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    register_base = repo_root / "OPT-IN_FRAMEWORK" / "N-NEURAL_NETWORKS_USERS_TRACEABILITY" / \
                    "ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS" / "95-00_GENERAL" / \
                    "95-00-01_Registers" / "95-00-01-010_BB_Identity_Register"
    
    register_path = register_base / "ASSETS" / "95-00-01-010-A-001_BodyBrain_Identity_Register.csv"
    loops_base = register_base / "LOOPS"
    
    # Check if register exists
    if not register_path.exists():
        print(f"ERROR: Register CSV not found: {register_path}")
        return 1
    
    # Load register
    artifacts = load_register(register_path)
    
    if not artifacts:
        print("No artifacts found in register")
        return 0
    
    # Process artifacts
    all_statuses = []
    
    if args.bb_id:
        # Check specific artifact
        artifact = next((a for a in artifacts if a['bb_id'] == args.bb_id), None)
        if not artifact:
            print(f"ERROR: BB ID '{args.bb_id}' not found in register")
            return 1
        
        status = check_artifact_status(artifact, loops_base)
        all_statuses.append(status)
        print_artifact_status(status, verbose=True)
    
    else:
        # Check all artifacts
        for artifact in artifacts:
            status = check_artifact_status(artifact, loops_base)
            all_statuses.append(status)
            
            if args.validate and not args.summary:
                print_artifact_status(status, verbose=args.verbose)
    
    # Print summary if requested
    if args.summary or (not args.bb_id and not args.validate):
        print_summary(all_statuses)
    
    # Exit with error code if issues found
    has_issues = any(s['issues'] for s in all_statuses)
    return 1 if has_issues else 0


if __name__ == '__main__':
    sys.exit(main())
