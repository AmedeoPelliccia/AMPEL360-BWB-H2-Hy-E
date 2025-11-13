#!/usr/bin/env python3
# Copyright (c) 2025 AMPEL360 Project Contributors
# SPDX-License-Identifier: Apache-2.0
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
AMPEL360 Documentation Structure Validator

This script validates that all ATA chapters comply with the mandatory
XX-00-00_GENERAL documentation structure as defined in the AMPEL360
Documentation Standard.

Usage:
    python3 validate_documentation_structure.py [--fix] [--verbose]
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Optional

# Base path
BASE_PATH = Path(__file__).parent.parent

# Mandatory folders in XX-00-00_GENERAL
MANDATORY_FOLDERS = [
    "01_OVERVIEW",
    "02_SAFETY",
    "03_REQUIREMENTS",
    "04_DESIGN",
    "05_INTERFACES",
    "06_ENGINEERING",
    "07_V_AND_V",
    "08_PROTOTYPING",
    "09_PRODUCTION_PLANNING",
    "10_CERTIFICATION",
    "11_OPERATIONS_MAINTENANCE",
    "12_ASSETS_MANAGEMENT",
    "13_SUBSYSTEMS_COMPONENTS",
    "14_META_GOVERNANCE",
]


class ValidationResult:
    """Stores validation results for an ATA chapter."""

    def __init__(self, ata_path: Path, ata_num: str) -> None:
        self.ata_path: Path = ata_path
        self.ata_num: str = ata_num
        self.has_general: bool = False
        self.general_has_readme: bool = False
        self.missing_folders: List[str] = []
        self.folders_without_readme: List[str] = []
        self.passed: bool = False

    def validate(self) -> None:
        """Perform validation checks."""
        general_dir = self.ata_path / f"{self.ata_num}-00-00_GENERAL"

        # Check if XX-00-00_GENERAL exists
        if not general_dir.exists():
            self.has_general = False
            return

        self.has_general = True

        # Check for main README
        general_readme = general_dir / "README.md"
        self.general_has_readme = general_readme.exists()

        # Check for all mandatory folders with several name variants
        for folder in MANDATORY_FOLDERS:
            folder_num = folder.split("_", 1)[0]  # e.g., "01"
            folder_desc = folder.split("_", 1)[1]  # e.g., "OVERVIEW"

            # Build a set of plausible folder name variants to match existing styles
            candidates = set()

            # Standard: e.g., "02-00-01_OVERVIEW" where ata_num is "02"
            candidates.add(f"{self.ata_num}-00-{folder_num}_{folder_desc}")
            # Title-cased description: "02-00-01_Overview"
            candidates.add(f"{self.ata_num}-00-{folder_num}_{folder_desc.title()}")
            # Lower/Title variations and common stylings
            candidates.add(f"{self.ata_num}-00-{folder_num}_{folder_desc.replace('_', ' ').title().replace(' ', '_')}")
            # Alternative connector variations for V_AND_V -> V_and_V
            candidates.add(f"{self.ata_num}-00-{folder_num}_{folder_desc.replace('_AND_', '_and_')}")
            # Old style (no ATA prefix): "01_OVERVIEW"
            candidates.add(folder)
            # Also allow lowercase variants of folder
            candidates.add(folder.lower())
            candidates.add(folder.title())

            found = False
            for subfolder_name in sorted(candidates):
                subfolder = general_dir / subfolder_name
                if subfolder.exists():
                    found = True
                    readme = subfolder / "README.md"
                    if not readme.exists():
                        self.folders_without_readme.append(subfolder_name)
                    break

            if not found:
                # report using the canonical standard name
                self.missing_folders.append(f"{self.ata_num}-00-{folder_num}_{folder_desc}")

        # Determine if validation passed
        self.passed = (
            self.has_general
            and self.general_has_readme
            and len(self.missing_folders) == 0
            and len(self.folders_without_readme) == 0
        )

    def __str__(self) -> str:
        """String representation of validation result."""
        status = "✅ PASS" if self.passed else "❌ FAIL"
        try:
            rel_path = self.ata_path.relative_to(BASE_PATH)
        except Exception:
            rel_path = self.ata_path
        return f"{status} - {rel_path}"


def get_ata_number(ata_dir_name: str) -> Optional[str]:
    """Extract ATA number from directory name.

    Accepts names like:
      - ATA_02
      - ATA_02-11
      - ATA_02-11-00
      - ATA_95
    """
    match = re.match(r"ATA_([\d-]+)", ata_dir_name)
    if match:
        return match.group(1)
    return None


def find_all_ata_directories() -> List[Path]:
    """Find all ATA directories in the repository."""
    ata_dirs: List[Path] = []
    for root, dirs, files in os.walk(BASE_PATH):
        # Avoid walking into common virtual envs or hidden dirs
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("venv", "__pycache__", "node_modules")]
        for d in dirs:
            if d.startswith("ATA_") and "ATA_Standards_Training" not in d:
                full_path = Path(root) / d
                ata_dirs.append(full_path)
    return sorted(ata_dirs)


def validate_all_ata_chapters(verbose: bool = False) -> Tuple[List[ValidationResult], List[ValidationResult]]:
    """Validate all ATA chapters.

    Returns:
        Tuple of (passed_results, failed_results)
    """
    ata_dirs = find_all_ata_directories()
    passed: List[ValidationResult] = []
    failed: List[ValidationResult] = []

    for ata_dir in ata_dirs:
        ata_num = get_ata_number(ata_dir.name)
        if not ata_num:
            if verbose:
                print(f"[skip] could not extract ata number from {ata_dir.name}")
            continue

        result = ValidationResult(ata_dir, ata_num)
        result.validate()

        if result.passed:
            passed.append(result)
        else:
            failed.append(result)

    return passed, failed


def print_detailed_failures(failed: List[ValidationResult]) -> None:
    """Print detailed information about failures."""
    for result in failed:
        print(f"\n{result}")

        if not result.has_general:
            print(f"  ❌ Missing XX-00-00_GENERAL directory")
        else:
            if not result.general_has_readme:
                print(f"  ⚠️  Missing README.md in XX-00-00_GENERAL")

            if result.missing_folders:
                print(f"  ❌ Missing {len(result.missing_folders)} mandatory folder(s):")
                for folder in result.missing_folders:
                    print(f"      - {folder}")

            if result.folders_without_readme:
                print(f"  ⚠️  Missing README.md in {len(result.folders_without_readme)} folder(s):")
                for folder in result.folders_without_readme:
                    print(f"      - {folder}")


def generate_report(passed: List[ValidationResult], failed: List[ValidationResult]) -> Dict:
    """Generate validation report summary."""
    total = len(passed) + len(failed)
    pass_rate = (len(passed) / total * 100) if total > 0 else 0

    no_general = sum(1 for r in failed if not r.has_general)
    missing_readme = sum(1 for r in failed if r.has_general and not r.general_has_readme)
    incomplete_folders = sum(1 for r in failed if r.has_general and (r.missing_folders or r.folders_without_readme))

    return {
        "total": total,
        "passed": len(passed),
        "failed": len(failed),
        "pass_rate": pass_rate,
        "no_general": no_general,
        "missing_readme": missing_readme,
        "incomplete_folders": incomplete_folders,
    }


def main() -> None:
    """Main execution."""
    import argparse

    parser = argparse.ArgumentParser(description="Validate AMPEL360 documentation structure compliance")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed output for all checks")
    parser.add_argument("--fix", action="store_true", help="Attempt to fix issues (not implemented)")
    args = parser.parse_args()

    print("=" * 80)
    print("AMPEL360 Documentation Structure Validation")
    print("=" * 80)
    print()

    passed, failed = validate_all_ata_chapters(args.verbose)
    report = generate_report(passed, failed)

    print(f"Total ATA Chapters:    {report['total']}")
    print(f"✅ Passed:              {report['passed']}")
    print(f"❌ Failed:              {report['failed']}")
    print(f"Pass Rate:             {report['pass_rate']:.1f}%")
    print()

    if failed:
        print("Failure Breakdown:")
        print(f"  - Missing XX-00-00_GENERAL:     {report['no_general']}")
        print(f"  - Missing main README.md:       {report['missing_readme']}")
        print(f"  - Incomplete folder structure:  {report['incomplete_folders']}")
        print()

    if args.verbose and passed:
        print("=" * 80)
        print("PASSED VALIDATIONS")
        print("=" * 80)
        for result in passed:
            print(result)
        print()

    if failed:
        print("=" * 80)
        print("FAILED VALIDATIONS")
        print("=" * 80)
        print_detailed_failures(failed)
        print()

        print("=" * 80)
        print("❌ Validation FAILED - Issues found")
        print("=" * 80)
        print()
        print("To fix issues, ensure all ATA chapters have:")
        print("  1. XX-00-00_GENERAL directory")
        print("  2. README.md in XX-00-00_GENERAL")
        print("  3. All 14 mandatory subfolders (01-14)")
        print("  4. README.md in each subfolder")
        print()
        print("See AMPEL360_DOCUMENTATION_STANDARD.md for details.")
        sys.exit(1)
    else:
        print("=" * 80)
        print("✅ Validation PASSED - All ATA chapters comply")
        print("=" * 80)
        sys.exit(0)


if __name__ == "__main__":
    main()
