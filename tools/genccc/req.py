#!/usr/bin/env python3
"""
GenCCC Requirements Management CLI
Provides CRUD operations for requirements with traceability support.

This tool integrates with the GenCCC workflow to provide a complete
requirements management solution including:
- Requirements CRUD (Create, Read, Update, Delete/Close)
- Unique ID generation (RQ-XX-YY-####)
- Status workflow management
- Parent/child linking
- Traceability to verification and evidence
- Baseline management
- Validation and compliance checking
"""

import argparse
import csv
import datetime
import json
import pathlib
import re
import sys
from typing import Dict, List, Optional, Tuple


# Repository paths
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
REQUIREMENTS_DIR = REPO_ROOT / "OPT-IN_FRAMEWORK" / "N-NEURAL_NETWORKS_USERS_TRACEABILITY" / "ATA_95_NEURAL_NETWORKS" / "95-00-00_GENERAL" / "95-00-03_Requirements"
BASELINES_DIR = REPO_ROOT / "cd" / "baselines"
EVIDENCE_DIR = REPO_ROOT / "EVIDENCE"
REPORTS_DIR = REPO_ROOT / "cd" / "reports"

# CSV headers for requirements data model
REQ_CSV_HEADERS = [
    "ID", "Title", "Text", "Source", "SafetyLevel", "Owner", "Status",
    "Version", "ParentID", "VerificationMethod", "EvidenceRefs",
    "Subsystem", "ChangeRationale", "ChangedBy", "ChangedAt"
]

# Valid statuses for requirements workflow
VALID_STATUSES = ["Draft", "Review", "Approved", "Implemented", "Verified", "Closed", "Obsolete"]

# Valid verification methods (DO-178C/DO-254)
VALID_VERIFICATION_METHODS = ["T", "A", "I", "D", "N/A"]  # Test, Analysis, Inspection, Demo, Not Applicable

# Valid safety levels (DO-178C)
VALID_SAFETY_LEVELS = ["DAL-A", "DAL-B", "DAL-C", "DAL-D", "DAL-E", "N/A"]


def ensure_directories() -> None:
    """Ensure required directories exist."""
    REQUIREMENTS_DIR.mkdir(parents=True, exist_ok=True)
    BASELINES_DIR.mkdir(parents=True, exist_ok=True)
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def get_requirements_file() -> pathlib.Path:
    """Get the main requirements CSV file path."""
    return REQUIREMENTS_DIR / "requirements.csv"


def load_requirements() -> List[Dict[str, str]]:
    """Load all requirements from CSV file."""
    req_file = get_requirements_file()
    
    if not req_file.exists():
        return []
    
    requirements = []
    with open(req_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            requirements.append(row)
    
    return requirements


def save_requirements(requirements: List[Dict[str, str]]) -> None:
    """Save requirements to CSV file."""
    req_file = get_requirements_file()
    
    with open(req_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=REQ_CSV_HEADERS)
        writer.writeheader()
        writer.writerows(requirements)
    
    print(f"✅ Saved {len(requirements)} requirements to {req_file}")


def generate_requirement_id(ata_chapter: str, section: str) -> str:
    """
    Generate unique requirement ID in format RQ-XX-YY-####.
    
    Args:
        ata_chapter: ATA chapter number (e.g., "95")
        section: Section number (e.g., "00")
        
    Returns:
        Unique requirement ID
    """
    requirements = load_requirements()
    
    # Find existing IDs for this ATA chapter and section
    prefix = f"RQ-{ata_chapter}-{section}-"
    existing_ids = [req["ID"] for req in requirements if req["ID"].startswith(prefix)]
    
    # Find next available sequence number
    if not existing_ids:
        seq_num = 1
    else:
        seq_nums = []
        for req_id in existing_ids:
            match = re.search(r'-(\d{4})$', req_id)
            if match:
                seq_nums.append(int(match.group(1)))
        seq_num = max(seq_nums) + 1 if seq_nums else 1
    
    return f"{prefix}{seq_num:04d}"


def validate_requirement(req: Dict[str, str]) -> List[str]:
    """
    Validate a requirement against the data model.
    
    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []
    
    # Required fields
    if not req.get("ID"):
        errors.append("ID is required")
    elif not re.match(r'^RQ-\d{2}-\d{2}-\d{4}$', req["ID"]):
        errors.append(f"ID must match format RQ-XX-YY-####, got: {req['ID']}")
    
    if not req.get("Title"):
        errors.append("Title is required")
    
    if not req.get("Text"):
        errors.append("Text is required")
    
    # Status validation
    if req.get("Status") and req["Status"] not in VALID_STATUSES:
        errors.append(f"Status must be one of {VALID_STATUSES}, got: {req['Status']}")
    
    # Safety level validation
    if req.get("SafetyLevel") and req["SafetyLevel"] not in VALID_SAFETY_LEVELS:
        errors.append(f"SafetyLevel must be one of {VALID_SAFETY_LEVELS}, got: {req['SafetyLevel']}")
    
    # Verification method validation
    if req.get("VerificationMethod"):
        methods = [m.strip() for m in req["VerificationMethod"].split(",")]
        invalid_methods = [m for m in methods if m and m not in VALID_VERIFICATION_METHODS]
        if invalid_methods:
            errors.append(f"Invalid verification methods: {invalid_methods}. Valid: {VALID_VERIFICATION_METHODS}")
    
    # Parent ID validation (if specified, must exist)
    if req.get("ParentID"):
        requirements = load_requirements()
        parent_ids = [r["ID"] for r in requirements]
        if req["ParentID"] not in parent_ids:
            errors.append(f"ParentID {req['ParentID']} does not exist")
    
    return errors


def cmd_new(args: argparse.Namespace) -> int:
    """Create a new requirement."""
    ensure_directories()
    
    # Generate ID
    req_id = generate_requirement_id(args.ata_chapter, args.section)
    
    # Create requirement
    req = {
        "ID": req_id,
        "Title": args.title,
        "Text": args.text,
        "Source": args.source or "",
        "SafetyLevel": args.safety_level or "N/A",
        "Owner": args.owner or "",
        "Status": "Draft",
        "Version": "1.0",
        "ParentID": args.parent or "",
        "VerificationMethod": args.verification or "",
        "EvidenceRefs": "",
        "Subsystem": args.subsystem or "",
        "ChangeRationale": "Initial creation",
        "ChangedBy": args.changed_by or "system",
        "ChangedAt": datetime.datetime.now().isoformat()
    }
    
    # Validate
    errors = validate_requirement(req)
    if errors:
        print(f"❌ Validation errors:")
        for error in errors:
            print(f"  - {error}")
        return 1
    
    # Add to requirements
    requirements = load_requirements()
    requirements.append(req)
    save_requirements(requirements)
    
    print(f"✅ Created requirement {req_id}")
    print(f"   Title: {req['Title']}")
    print(f"   Status: {req['Status']}")
    
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    """List requirements with optional filters."""
    requirements = load_requirements()
    
    if not requirements:
        print("No requirements found.")
        return 0
    
    # Apply filters
    if args.status:
        requirements = [r for r in requirements if r["Status"] == args.status]
    
    if args.owner:
        requirements = [r for r in requirements if r["Owner"] == args.owner]
    
    if args.subsystem:
        requirements = [r for r in requirements if r["Subsystem"] == args.subsystem]
    
    # Display
    print(f"📋 Requirements ({len(requirements)} total)")
    print("=" * 80)
    
    for req in requirements:
        print(f"ID: {req['ID']}")
        print(f"  Title: {req['Title']}")
        print(f"  Status: {req['Status']}")
        print(f"  Owner: {req['Owner']}")
        print(f"  Safety Level: {req['SafetyLevel']}")
        if req['ParentID']:
            print(f"  Parent: {req['ParentID']}")
        print()
    
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    """Show detailed information for a requirement."""
    requirements = load_requirements()
    
    req = next((r for r in requirements if r["ID"] == args.id), None)
    if not req:
        print(f"❌ Requirement {args.id} not found")
        return 1
    
    print(f"📋 Requirement: {req['ID']}")
    print("=" * 80)
    for key, value in req.items():
        if value:
            print(f"{key:20s}: {value}")
    
    # Show children
    children = [r for r in requirements if r["ParentID"] == args.id]
    if children:
        print()
        print(f"Children ({len(children)}):")
        for child in children:
            print(f"  - {child['ID']}: {child['Title']}")
    
    return 0


def cmd_edit(args: argparse.Namespace) -> int:
    """Edit an existing requirement."""
    requirements = load_requirements()
    
    req = next((r for r in requirements if r["ID"] == args.id), None)
    if not req:
        print(f"❌ Requirement {args.id} not found")
        return 1
    
    # Update fields
    changed = False
    if args.title:
        req["Title"] = args.title
        changed = True
    if args.text:
        req["Text"] = args.text
        changed = True
    if args.status:
        req["Status"] = args.status
        changed = True
    if args.owner:
        req["Owner"] = args.owner
        changed = True
    if args.verification:
        req["VerificationMethod"] = args.verification
        changed = True
    if args.rationale:
        req["ChangeRationale"] = args.rationale
        changed = True
    
    if changed:
        # Increment version
        try:
            version_parts = req["Version"].split(".")
            version_parts[-1] = str(int(version_parts[-1]) + 1)
            req["Version"] = ".".join(version_parts)
        except:
            req["Version"] = "1.1"
        
        req["ChangedBy"] = args.changed_by or "system"
        req["ChangedAt"] = datetime.datetime.now().isoformat()
        
        # Validate
        errors = validate_requirement(req)
        if errors:
            print(f"❌ Validation errors:")
            for error in errors:
                print(f"  - {error}")
            return 1
        
        save_requirements(requirements)
        print(f"✅ Updated requirement {args.id}")
        print(f"   Version: {req['Version']}")
    else:
        print("ℹ️  No changes made")
    
    return 0


def cmd_close(args: argparse.Namespace) -> int:
    """Close a requirement."""
    requirements = load_requirements()
    
    req = next((r for r in requirements if r["ID"] == args.id), None)
    if not req:
        print(f"❌ Requirement {args.id} not found")
        return 1
    
    req["Status"] = "Closed"
    req["ChangeRationale"] = args.rationale or "Requirement closed"
    req["ChangedBy"] = args.changed_by or "system"
    req["ChangedAt"] = datetime.datetime.now().isoformat()
    
    save_requirements(requirements)
    print(f"✅ Closed requirement {args.id}")
    
    return 0


def main():
    """Main entry point for requirements CLI."""
    parser = argparse.ArgumentParser(
        description="GenCCC Requirements Management CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create a new requirement
  genccc req new --ata-chapter 95 --section 00 \\
                 --title "System shall..." --text "Detailed text..." \\
                 --safety-level DAL-A --verification T,A
  
  # List all requirements
  genccc req list
  
  # List by status
  genccc req list --status Approved
  
  # Show requirement details
  genccc req show RQ-95-00-0001
  
  # Edit a requirement
  genccc req edit RQ-95-00-0001 --status Approved \\
                  --rationale "Passed review"
  
  # Close a requirement
  genccc req close RQ-95-00-0001 --rationale "Superseded by RQ-95-00-0002"
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # New command
    new_parser = subparsers.add_parser('new', help='Create a new requirement')
    new_parser.add_argument('--ata-chapter', required=True, help='ATA chapter (e.g., 95)')
    new_parser.add_argument('--section', required=True, help='Section number (e.g., 00)')
    new_parser.add_argument('--title', required=True, help='Requirement title')
    new_parser.add_argument('--text', required=True, help='Requirement text')
    new_parser.add_argument('--source', help='Source document or stakeholder')
    new_parser.add_argument('--safety-level', choices=VALID_SAFETY_LEVELS, help='Safety level')
    new_parser.add_argument('--owner', help='Requirement owner')
    new_parser.add_argument('--parent', help='Parent requirement ID')
    new_parser.add_argument('--verification', help='Verification methods (T,A,I,D)')
    new_parser.add_argument('--subsystem', help='Subsystem name')
    new_parser.add_argument('--changed-by', help='User making the change')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List requirements')
    list_parser.add_argument('--status', choices=VALID_STATUSES, help='Filter by status')
    list_parser.add_argument('--owner', help='Filter by owner')
    list_parser.add_argument('--subsystem', help='Filter by subsystem')
    
    # Show command
    show_parser = subparsers.add_parser('show', help='Show requirement details')
    show_parser.add_argument('id', help='Requirement ID')
    
    # Edit command
    edit_parser = subparsers.add_parser('edit', help='Edit a requirement')
    edit_parser.add_argument('id', help='Requirement ID')
    edit_parser.add_argument('--title', help='New title')
    edit_parser.add_argument('--text', help='New text')
    edit_parser.add_argument('--status', choices=VALID_STATUSES, help='New status')
    edit_parser.add_argument('--owner', help='New owner')
    edit_parser.add_argument('--verification', help='Verification methods (T,A,I,D)')
    edit_parser.add_argument('--rationale', help='Change rationale')
    edit_parser.add_argument('--changed-by', help='User making the change')
    
    # Close command
    close_parser = subparsers.add_parser('close', help='Close a requirement')
    close_parser.add_argument('id', help='Requirement ID')
    close_parser.add_argument('--rationale', help='Reason for closing')
    close_parser.add_argument('--changed-by', help='User making the change')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Execute command
    if args.command == 'new':
        return cmd_new(args)
    elif args.command == 'list':
        return cmd_list(args)
    elif args.command == 'show':
        return cmd_show(args)
    elif args.command == 'edit':
        return cmd_edit(args)
    elif args.command == 'close':
        return cmd_close(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
