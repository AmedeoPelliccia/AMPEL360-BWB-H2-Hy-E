#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2025 AMPEL360 Project Contributors

"""
GenCCC Requirements Validation
Validates requirements against schema, checks for orphans, duplicates, and coverage gaps.

This script is designed to run in CI to enforce requirements quality gates.
"""

import csv
import pathlib
import re
import sys
from typing import Dict, List, Set, Tuple


# Repository paths
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
REQUIREMENTS_DIR = REPO_ROOT / "OPT-IN_FRAMEWORK" / "N-NEURAL_NETWORKS_USERS_TRACEABILITY" / "ATA_95_NEURAL_NETWORKS" / "95-00-00_GENERAL" / "95-00-03_Requirements"
EVIDENCE_DIR = REPO_ROOT / "EVIDENCE"
REPORTS_DIR = REPO_ROOT / "cd" / "reports"

# Valid values
VALID_STATUSES = ["Draft", "Review", "Approved", "Implemented", "Verified", "Closed", "Obsolete"]
VALID_VERIFICATION_METHODS = ["T", "A", "I", "D", "N/A"]
VALID_SAFETY_LEVELS = ["DAL-A", "DAL-B", "DAL-C", "DAL-D", "DAL-E", "N/A"]


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
    """Find evidence files mapped to requirement IDs."""
    evidence_map = {}
    
    if not EVIDENCE_DIR.exists():
        return evidence_map
    
    for evidence_file in EVIDENCE_DIR.rglob("*"):
        if evidence_file.is_file():
            filename = evidence_file.name
            matches = re.findall(r'RQ-\d{2}-\d{2}-\d{4}', filename)
            
            for req_id in matches:
                if req_id not in evidence_map:
                    evidence_map[req_id] = []
                evidence_map[req_id].append(str(evidence_file.relative_to(REPO_ROOT)))
    
    return evidence_map


class ValidationError:
    """Represents a validation error."""
    
    def __init__(self, severity: str, category: str, req_id: str, message: str):
        self.severity = severity  # ERROR, WARNING, INFO
        self.category = category
        self.req_id = req_id
        self.message = message
    
    def __str__(self):
        return f"[{self.severity}] {self.category}: {self.req_id} - {self.message}"


def validate_schema(requirements: List[Dict[str, str]]) -> List[ValidationError]:
    """Validate requirements against data model schema."""
    errors = []
    
    for req in requirements:
        req_id = req.get("ID", "UNKNOWN")
        
        # ID format
        if not req.get("ID"):
            errors.append(ValidationError("ERROR", "Schema", req_id, "ID is missing"))
        elif not re.match(r'^RQ-\d{2}-\d{2}-\d{4}$', req["ID"]):
            errors.append(ValidationError("ERROR", "Schema", req_id, f"ID format invalid: {req['ID']}"))
        
        # Required fields
        if not req.get("Title"):
            errors.append(ValidationError("ERROR", "Schema", req_id, "Title is missing"))
        
        if not req.get("Text"):
            errors.append(ValidationError("ERROR", "Schema", req_id, "Text is missing"))
        
        # Status
        if req.get("Status") and req["Status"] not in VALID_STATUSES:
            errors.append(ValidationError("ERROR", "Schema", req_id, f"Invalid status: {req['Status']}"))
        
        # Safety level
        if req.get("SafetyLevel") and req["SafetyLevel"] not in VALID_SAFETY_LEVELS:
            errors.append(ValidationError("WARNING", "Schema", req_id, f"Invalid safety level: {req['SafetyLevel']}"))
        
        # Verification method
        if req.get("VerificationMethod"):
            methods = [m.strip() for m in req["VerificationMethod"].split(",")]
            invalid = [m for m in methods if m and m not in VALID_VERIFICATION_METHODS]
            if invalid:
                errors.append(ValidationError("ERROR", "Schema", req_id, f"Invalid verification methods: {invalid}"))
    
    return errors


def validate_orphans(requirements: List[Dict[str, str]]) -> List[ValidationError]:
    """Check for orphaned requirements (parent doesn't exist)."""
    errors = []
    
    req_ids = {req["ID"] for req in requirements}
    
    for req in requirements:
        if req.get("ParentID"):
            if req["ParentID"] not in req_ids:
                errors.append(ValidationError(
                    "ERROR", "Orphan", req["ID"],
                    f"Parent {req['ParentID']} does not exist"
                ))
    
    return errors


def validate_duplicates(requirements: List[Dict[str, str]]) -> List[ValidationError]:
    """Check for duplicate IDs and titles."""
    errors = []
    
    # Duplicate IDs
    id_counts = {}
    for req in requirements:
        req_id = req["ID"]
        id_counts[req_id] = id_counts.get(req_id, 0) + 1
    
    for req_id, count in id_counts.items():
        if count > 1:
            errors.append(ValidationError(
                "ERROR", "Duplicate", req_id,
                f"Duplicate ID appears {count} times"
            ))
    
    # Duplicate titles (warning only)
    title_map = {}
    for req in requirements:
        title = req.get("Title", "").strip().lower()
        if title:
            if title not in title_map:
                title_map[title] = []
            title_map[title].append(req["ID"])
    
    for title, req_ids in title_map.items():
        if len(req_ids) > 1:
            errors.append(ValidationError(
                "WARNING", "Duplicate", req_ids[0],
                f"Duplicate title found in: {', '.join(req_ids)}"
            ))
    
    return errors


def validate_coverage(requirements: List[Dict[str, str]], evidence_map: Dict[str, List[str]]) -> List[ValidationError]:
    """Check verification coverage."""
    errors = []
    
    for req in requirements:
        req_id = req["ID"]
        verification = req.get("VerificationMethod", "")
        safety_level = req.get("SafetyLevel", "")
        status = req.get("Status", "")
        
        # Skip closed/obsolete requirements
        if status in ["Closed", "Obsolete"]:
            continue
        
        # Check verification method
        if not verification or verification == "N/A":
            if safety_level in ["DAL-A", "DAL-B"]:
                errors.append(ValidationError(
                    "ERROR", "Coverage", req_id,
                    f"Safety-critical requirement ({safety_level}) missing verification method"
                ))
            else:
                errors.append(ValidationError(
                    "WARNING", "Coverage", req_id,
                    "No verification method assigned"
                ))
        
        # Check evidence
        elif verification != "N/A":
            if req_id not in evidence_map or not evidence_map[req_id]:
                if safety_level in ["DAL-A", "DAL-B"]:
                    errors.append(ValidationError(
                        "ERROR", "Coverage", req_id,
                        f"Safety-critical requirement ({safety_level}) missing evidence"
                    ))
                elif status in ["Implemented", "Verified"]:
                    errors.append(ValidationError(
                        "WARNING", "Coverage", req_id,
                        f"Requirement marked {status} but no evidence found"
                    ))
    
    return errors


def validate_circular_parents(requirements: List[Dict[str, str]]) -> List[ValidationError]:
    """Check for circular parent relationships."""
    errors = []
    
    # Build parent map
    parent_map = {req["ID"]: req.get("ParentID", "") for req in requirements}
    
    def has_circular_ref(req_id: str, visited: Set[str]) -> bool:
        if req_id in visited:
            return True
        if not parent_map.get(req_id):
            return False
        visited.add(req_id)
        return has_circular_ref(parent_map[req_id], visited.copy())
    
    for req in requirements:
        if req.get("ParentID"):
            if has_circular_ref(req["ID"], set()):
                errors.append(ValidationError(
                    "ERROR", "Circular", req["ID"],
                    "Circular parent relationship detected"
                ))
    
    return errors


def generate_validation_report(all_errors: List[ValidationError], requirements: List[Dict[str, str]]) -> str:
    """Generate validation report."""
    error_count = len([e for e in all_errors if e.severity == "ERROR"])
    warning_count = len([e for e in all_errors if e.severity == "WARNING"])
    
    lines = [
        "# Requirements Validation Report",
        "",
        f"**Total Requirements:** {len(requirements)}",
        f"**Errors:** {error_count}",
        f"**Warnings:** {warning_count}",
        "",
    ]
    
    if error_count == 0 and warning_count == 0:
        lines.append("✅ **All requirements are valid!**")
        lines.append("")
        lines.append("No errors or warnings found. Requirements are ready for baseline.")
        return "\n".join(lines)
    
    lines.append("---")
    lines.append("")
    
    # Group by category
    by_category = {}
    for error in all_errors:
        if error.category not in by_category:
            by_category[error.category] = []
        by_category[error.category].append(error)
    
    # Report by category
    for category in sorted(by_category.keys()):
        errors_in_cat = by_category[category]
        errors_only = [e for e in errors_in_cat if e.severity == "ERROR"]
        warnings_only = [e for e in errors_in_cat if e.severity == "WARNING"]
        
        lines.append(f"## {category} Issues ({len(errors_only)} errors, {len(warnings_only)} warnings)")
        lines.append("")
        
        # Show errors first
        for error in errors_only:
            lines.append(f"- ❌ **{error.req_id}**: {error.message}")
        
        # Then warnings
        for warning in warnings_only:
            lines.append(f"- ⚠️ **{warning.req_id}**: {warning.message}")
        
        lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("## Recommendations")
    lines.append("")
    lines.append("1. Fix all ERROR-level issues before creating a baseline")
    lines.append("2. Review WARNING-level issues and address as appropriate")
    lines.append("3. Ensure all safety-critical requirements have verification methods and evidence")
    lines.append("4. Run validation again after making fixes")
    lines.append("")
    
    return "\n".join(lines)


def main():
    """Run validation and generate report."""
    print("🔍 GenCCC Requirements Validation")
    print("=" * 80)
    print()
    
    requirements = load_requirements()
    
    if not requirements:
        print("⚠️  No requirements found.")
        print("   This may be expected for new repositories.")
        return 0
    
    print(f"📋 Validating {len(requirements)} requirements...")
    print()
    
    # Run validations
    all_errors = []
    
    print("  • Checking schema...")
    all_errors.extend(validate_schema(requirements))
    
    print("  • Checking for orphans...")
    all_errors.extend(validate_orphans(requirements))
    
    print("  • Checking for duplicates...")
    all_errors.extend(validate_duplicates(requirements))
    
    print("  • Checking for circular references...")
    all_errors.extend(validate_circular_parents(requirements))
    
    print("  • Checking coverage...")
    evidence_map = find_evidence_files()
    all_errors.extend(validate_coverage(requirements, evidence_map))
    
    print()
    
    # Generate report
    report = generate_validation_report(all_errors, requirements)
    
    # Save report
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_file = REPORTS_DIR / "requirements_validation.md"
    report_file.write_text(report, encoding='utf-8')
    
    print(f"✅ Generated validation report: {report_file}")
    print()
    
    # Count errors
    error_count = len([e for e in all_errors if e.severity == "ERROR"])
    warning_count = len([e for e in all_errors if e.severity == "WARNING"])
    
    print("=" * 80)
    if error_count > 0:
        print(f"❌ Validation failed with {error_count} errors and {warning_count} warnings")
        print()
        print("Critical issues found:")
        for error in all_errors[:10]:
            if error.severity == "ERROR":
                print(f"  - {error}")
        if error_count > 10:
            print(f"  ... and {error_count - 10} more errors")
        print()
        return 1
    elif warning_count > 0:
        print(f"⚠️  Validation passed with {warning_count} warnings")
        print()
        print("Review warnings in the report file.")
        return 0
    else:
        print("✅ Validation passed! All requirements are valid.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
