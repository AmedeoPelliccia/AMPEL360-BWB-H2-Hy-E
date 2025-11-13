#!/usr/bin/env python3
"""
optin_structure_validator.py

Validates that the OPT-IN Framework structure conforms to the mandatory standard:
- XX-00_GENERAL with all 14 lifecycle folders
- 9 cross-ATA root buckets (10/20/30/40/50/60/70/80/90)
- README.md in each folder
- Proper naming conventions

Usage:
    # Check structure compliance (CI mode)
    python tools/ci/optin_structure_validator.py --check

    # Generate SARIF report for GitHub Code Scanning
    python tools/ci/optin_structure_validator.py --check --sarif structure_results.sarif

    # Validate specific ATA chapter
    python tools/ci/optin_structure_validator.py --check --chapter 95
"""

import argparse
import json
import pathlib
import re
import sys
from typing import List, Dict, Tuple

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
FRAMEWORK_ROOT = REPO_ROOT / "OPT-IN_FRAMEWORK"

# Expected 14 lifecycle folders in XX-00_GENERAL
GENERAL_LIFECYCLE_FOLDERS = [
    "01_Overview",
    "02_Safety",
    "03_Requirements",
    "04_Design",
    "05_Interfaces",
    "06_Engineering",
    "07_V_AND_V",
    "08_Prototyping",
    "09_Production_Planning",
    "10_Certification",
    "11_EIS_Versions_Tags",
    "12_Services",
    "13_Subsystems_Components",
    "14_Ops_Std_Sustain",
]

# Expected 9 cross-ATA root buckets
CROSS_ATA_BUCKETS = [
    "10_Operations",
    "20_Subsystems",
    "30_Circularity",
    "40_Software",
    "50_Structures",
    "60_Storages",
    "70_Propulsion",
    "80_Energy",
    "90_Tables_Schemas_Diagrams",
]


class ValidationIssue:
    """Represents a validation issue found in the structure."""
    
    def __init__(self, level: str, path: pathlib.Path, message: str, rule_id: str = None):
        self.level = level  # 'error', 'warning', 'note'
        self.path = path
        self.message = message
        self.rule_id = rule_id or "structure-compliance"
    
    def __str__(self) -> str:
        rel_path = self.path.relative_to(REPO_ROOT) if self.path.is_relative_to(REPO_ROOT) else self.path
        return f"[{self.level.upper()}] {rel_path}: {self.message}"


class OptinStructureValidator:
    """Validates OPT-IN Framework structure compliance."""
    
    def __init__(self):
        self.issues: List[ValidationIssue] = []
    
    def validate_framework(self, specific_chapter: str = None) -> bool:
        """Validate the entire OPT-IN Framework or a specific chapter."""
        if not FRAMEWORK_ROOT.exists():
            self.issues.append(ValidationIssue(
                "error",
                FRAMEWORK_ROOT,
                "OPT-IN_FRAMEWORK directory does not exist",
                "missing-framework-root"
            ))
            return False
        
        # Find all ATA chapters
        ata_chapters = list(FRAMEWORK_ROOT.rglob("ATA_*"))
        
        if specific_chapter:
            ata_chapters = [ch for ch in ata_chapters if ch.name.startswith(f"ATA_{specific_chapter}-")]
            if not ata_chapters:
                self.issues.append(ValidationIssue(
                    "error",
                    FRAMEWORK_ROOT,
                    f"ATA chapter {specific_chapter} not found",
                    "missing-chapter"
                ))
                return False
        
        if not ata_chapters:
            self.issues.append(ValidationIssue(
                "error",
                FRAMEWORK_ROOT,
                "No ATA chapters found in OPT-IN_FRAMEWORK",
                "no-chapters"
            ))
            return False
        
        print(f"[validator] Found {len(ata_chapters)} ATA chapter(s) to validate")
        
        for chapter_path in sorted(ata_chapters):
            if chapter_path.is_dir():
                self.validate_ata_chapter(chapter_path)
        
        return len([i for i in self.issues if i.level == "error"]) == 0
    
    def validate_ata_chapter(self, chapter_path: pathlib.Path) -> None:
        """Validate a single ATA chapter."""
        # Extract ATA number from chapter name (e.g., ATA_95-NAME -> 95)
        match = re.match(r"ATA_(\d+)-", chapter_path.name)
        if not match:
            self.issues.append(ValidationIssue(
                "error",
                chapter_path,
                f"Invalid chapter name format: {chapter_path.name}",
                "invalid-chapter-name"
            ))
            return
        
        ata_num = match.group(1)
        
        # Check for chapter README.md
        readme_path = chapter_path / "README.md"
        if not readme_path.exists():
            self.issues.append(ValidationIssue(
                "warning",
                chapter_path,
                "Missing README.md",
                "missing-readme"
            ))
        
        # Validate XX-00_GENERAL structure
        self.validate_general_layer(chapter_path, ata_num)
        
        # Validate cross-ATA buckets
        self.validate_cross_ata_buckets(chapter_path, ata_num)
    
    def validate_general_layer(self, chapter_path: pathlib.Path, ata_num: str) -> None:
        """Validate the XX-00_GENERAL layer with 14 lifecycle folders."""
        general_path = chapter_path / f"{ata_num}-00_GENERAL"
        
        if not general_path.exists():
            self.issues.append(ValidationIssue(
                "error",
                chapter_path,
                f"Missing {ata_num}-00_GENERAL directory",
                "missing-general-layer"
            ))
            return
        
        # Check for all 14 lifecycle folders
        for folder_name in GENERAL_LIFECYCLE_FOLDERS:
            folder_num = folder_name.split("_")[0]
            expected_folder = general_path / f"{ata_num}-00-{folder_name}"
            
            if not expected_folder.exists():
                self.issues.append(ValidationIssue(
                    "error",
                    general_path,
                    f"Missing lifecycle folder: {ata_num}-00-{folder_name}",
                    "missing-lifecycle-folder"
                ))
            else:
                # Check for README.md in lifecycle folder
                readme_path = expected_folder / "README.md"
                if not readme_path.exists():
                    self.issues.append(ValidationIssue(
                        "warning",
                        expected_folder,
                        "Missing README.md in lifecycle folder",
                        "missing-lifecycle-readme"
                    ))
    
    def validate_cross_ata_buckets(self, chapter_path: pathlib.Path, ata_num: str) -> None:
        """Validate the 9 cross-ATA root buckets."""
        for bucket_name in CROSS_ATA_BUCKETS:
            bucket_num = bucket_name.split("_")[0]
            expected_bucket = chapter_path / f"{ata_num}-{bucket_name}"
            
            if not expected_bucket.exists():
                self.issues.append(ValidationIssue(
                    "error",
                    chapter_path,
                    f"Missing cross-ATA bucket: {ata_num}-{bucket_name}",
                    "missing-bucket"
                ))
            else:
                # Check for README.md in bucket
                readme_path = expected_bucket / "README.md"
                if not readme_path.exists():
                    self.issues.append(ValidationIssue(
                        "warning",
                        expected_bucket,
                        "Missing README.md in bucket",
                        "missing-bucket-readme"
                    ))
    
    def to_sarif(self) -> dict:
        """Convert validation issues to SARIF format."""
        runs = [{
            "tool": {
                "driver": {
                    "name": "optin_structure_validator",
                    "version": "1.0",
                    "informationUri": "https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E/blob/main/OPT-IN_FRAMEWORK_STANDARD.md",
                    "rules": [
                        {
                            "id": "missing-framework-root",
                            "name": "Missing Framework Root",
                            "shortDescription": {"text": "OPT-IN_FRAMEWORK directory does not exist"}
                        },
                        {
                            "id": "missing-chapter",
                            "name": "Missing ATA Chapter",
                            "shortDescription": {"text": "Required ATA chapter not found"}
                        },
                        {
                            "id": "no-chapters",
                            "name": "No Chapters Found",
                            "shortDescription": {"text": "No ATA chapters found in framework"}
                        },
                        {
                            "id": "invalid-chapter-name",
                            "name": "Invalid Chapter Name",
                            "shortDescription": {"text": "ATA chapter name does not follow naming convention"}
                        },
                        {
                            "id": "missing-readme",
                            "name": "Missing README",
                            "shortDescription": {"text": "Required README.md file is missing"}
                        },
                        {
                            "id": "missing-general-layer",
                            "name": "Missing GENERAL Layer",
                            "shortDescription": {"text": "XX-00_GENERAL directory is missing"}
                        },
                        {
                            "id": "missing-lifecycle-folder",
                            "name": "Missing Lifecycle Folder",
                            "shortDescription": {"text": "One of the 14 mandatory lifecycle folders is missing"}
                        },
                        {
                            "id": "missing-lifecycle-readme",
                            "name": "Missing Lifecycle README",
                            "shortDescription": {"text": "README.md missing in lifecycle folder"}
                        },
                        {
                            "id": "missing-bucket",
                            "name": "Missing Cross-ATA Bucket",
                            "shortDescription": {"text": "One of the 9 mandatory cross-ATA buckets is missing"}
                        },
                        {
                            "id": "missing-bucket-readme",
                            "name": "Missing Bucket README",
                            "shortDescription": {"text": "README.md missing in cross-ATA bucket"}
                        },
                    ]
                }
            },
            "results": []
        }]
        
        for issue in self.issues:
            rel_path = str(issue.path.relative_to(REPO_ROOT)) if issue.path.is_relative_to(REPO_ROOT) else str(issue.path)
            
            # Map validation level to SARIF level
            sarif_level = {
                "error": "error",
                "warning": "warning",
                "note": "note"
            }.get(issue.level, "warning")
            
            runs[0]["results"].append({
                "ruleId": issue.rule_id,
                "level": sarif_level,
                "message": {"text": issue.message},
                "locations": [{
                    "physicalLocation": {
                        "artifactLocation": {"uri": rel_path},
                        "region": {
                            "startLine": 1,
                            "startColumn": 1
                        }
                    }
                }]
            })
        
        return {
            "version": "2.1.0",
            "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
            "runs": runs
        }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate OPT-IN Framework structure compliance"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check structure compliance (CI mode)",
    )
    parser.add_argument(
        "--chapter",
        type=str,
        help="Validate specific ATA chapter (e.g., '95')",
    )
    parser.add_argument(
        "--sarif",
        type=pathlib.Path,
        help="Write SARIF report to this path for GitHub Code Scanning integration",
    )
    args = parser.parse_args()
    
    validator = OptinStructureValidator()
    
    print("[validator] Validating OPT-IN Framework structure...")
    
    is_valid = validator.validate_framework(specific_chapter=args.chapter)
    
    # Print all issues
    if validator.issues:
        print(f"\n[validator] Found {len(validator.issues)} issue(s):")
        for issue in validator.issues:
            print(f"  {issue}")
    else:
        print("[validator] ✓ All structure checks passed!")
    
    # Generate SARIF report if requested
    if args.sarif:
        args.sarif.parent.mkdir(parents=True, exist_ok=True)
        sarif_data = validator.to_sarif()
        args.sarif.write_text(json.dumps(sarif_data, indent=2), encoding="utf-8")
        print(f"[validator] SARIF report written to {args.sarif}")
    
    # Return exit code
    error_count = len([i for i in validator.issues if i.level == "error"])
    if error_count > 0:
        print(f"\n[validator] ✗ Validation failed with {error_count} error(s)")
        return 1
    
    warning_count = len([i for i in validator.issues if i.level == "warning"])
    if warning_count > 0:
        print(f"\n[validator] ⚠ Validation passed with {warning_count} warning(s)")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
