#!/usr/bin/env python3
"""
pub_brex_guard.py

Validates S1000D Data Module (DM) files in PUB directories:
- Checks DMC filename patterns conform to project standards
- Verifies BREX references are present in DM files
- Ensures DM files comply with BREX validation rules

Usage:
    python tools/ci/pub_brex_guard.py
    python tools/ci/pub_brex_guard.py --path OPT-IN_FRAMEWORK/
"""

import argparse
import pathlib
import re
import sys
import xml.etree.ElementTree as ET
from typing import List, Tuple

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]

# DMC pattern for AMPEL360AT project
# Format: DMC-AMPEL360AT-X-XX-XX-XX-XXX-XXXX-X_XXX-XX_XX-XX.XML
# Where:
#   - ModelIdentCode: AMPEL360AT
#   - SystemDiffCode: A-Z
#   - SystemCode: 00-99 (ATA chapter)
#   - SubSystemCode: 00-99
#   - SubSubSystemCode: 00-99
#   - AssyCode: 0000-9999
#   - DisassyCode: 00-99
#   - DisassyCodeVariant: A-Z
#   - InfoCode: 000A-999Z
#   - InfoCodeVariant: A-Z
#   - ItemLocationCode: A-ZZZ
#   - LearnCode: 000-999 (sequence)
#   - LearnEventCode: 00-99 (indenture)
#   - LanguageIsoCode: EN-US, etc.
#   - IssueNumber: 001-00 to 999-99

DMC_PATTERN = re.compile(
    r'^DMC-AMPEL360AT-'  # Model ident code
    r'[A-Z]-'  # System diff code
    r'\d{2}-'  # System code (ATA chapter)
    r'\d{2}-'  # SubSystem code
    r'\d{2}-'  # SubSubSystem code
    r'\d{2,4}[A-Z0-9]-'  # Assy code
    r'[0-9A-Z]{3,4}[A-Z]-'  # Disassy code + variant OR Info code
    r'[A-Z]_'  # Info code variant or item location start
    r'\d{3}-'  # Learn code (sequence)
    r'\d{2}_'  # Learn event code (indenture)
    r'[A-Z]{2}-[A-Z]{2}'  # Language ISO code
    r'(?:_\d{3}-\d{2})?'  # Optional issue number
    r'\.XML$',
    re.IGNORECASE
)

# Simplified pattern that matches the expected format more closely
DMC_PATTERN_SIMPLIFIED = re.compile(
    r'^DMC-AMPEL360AT-[A-Z]-\d{2}-\d{2}-\d{2}-\d{2,4}[A-Z0-9]?-[0-9A-Z]{3,4}[A-Z]?-[A-Z]_\d{3}-\d{2}_[A-Z]{2}-[A-Z]{2}(?:_\d{3}-\d{2})?\.XML$',
    re.IGNORECASE
)


class ValidationError:
    """Represents a validation error found in a DM file."""
    
    def __init__(self, file_path: pathlib.Path, message: str):
        self.file_path = file_path
        self.message = message
    
    def __str__(self) -> str:
        rel_path = self.file_path.relative_to(REPO_ROOT) if self.file_path.is_relative_to(REPO_ROOT) else self.file_path
        return f"ERROR: {rel_path}: {self.message}"


def find_dm_files(search_path: pathlib.Path) -> List[pathlib.Path]:
    """Find all Data Module XML files in PUB/*/CSDB/DM directories."""
    dm_files = []
    
    # Search for DM directories under PUB
    for dm_dir in search_path.rglob("PUB/*/CSDB/DM"):
        if dm_dir.is_dir():
            # Find all XML files starting with DMC-
            for xml_file in dm_dir.glob("DMC-*.XML"):
                if xml_file.is_file():
                    dm_files.append(xml_file)
    
    return sorted(dm_files)


def validate_dmc_filename(file_path: pathlib.Path) -> Tuple[bool, str]:
    """
    Validate that the filename follows the DMC pattern.
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    filename = file_path.name
    
    if not DMC_PATTERN_SIMPLIFIED.match(filename):
        return False, "Filename is not a valid DMC pattern for this repo."
    
    return True, ""


def validate_brex_reference(file_path: pathlib.Path) -> Tuple[bool, str]:
    """
    Validate that the DM file includes a BREX reference.
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Look for BREX reference in identAndStatusSection
        # Standard S1000D structure: //identAndStatusSection//brexDmRef
        namespaces = {
            '': 'http://www.s1000d.org/S1000D_5-0/xml/schema/dmodule',
            's1000d': 'http://www.s1000d.org/S1000D_5-0/xml/schema/dmodule'
        }
        
        # Try with namespace
        brex_refs = root.findall('.//brexDmRef', namespaces)
        if not brex_refs:
            # Try without namespace (for documents without proper namespace declaration)
            brex_refs = root.findall('.//brexDmRef')
        
        if not brex_refs:
            return False, "DM must include a BREX reference (e.g., <brexDmRef> element in identAndStatusSection)."
        
        return True, ""
    
    except ET.ParseError as e:
        return False, f"XML parse error: {e}"
    except Exception as e:
        return False, f"Error reading file: {e}"


def validate_dm_files(search_path: pathlib.Path) -> List[ValidationError]:
    """
    Validate all DM files found under the search path.
    
    Returns:
        List of validation errors
    """
    errors = []
    
    dm_files = find_dm_files(search_path)
    
    if not dm_files:
        print("[pub-brex-guard] No Data Module XML files found to validate.")
        return errors
    
    print(f"[pub-brex-guard] Found {len(dm_files)} Data Module file(s) to validate...")
    
    for dm_file in dm_files:
        # Validate filename pattern
        is_valid_name, name_error = validate_dmc_filename(dm_file)
        if not is_valid_name:
            errors.append(ValidationError(dm_file, name_error))
        
        # Validate BREX reference
        is_valid_brex, brex_error = validate_brex_reference(dm_file)
        if not is_valid_brex:
            errors.append(ValidationError(dm_file, brex_error))
    
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate S1000D Data Module files against project standards"
    )
    parser.add_argument(
        "--path",
        type=pathlib.Path,
        default=REPO_ROOT / "OPT-IN_FRAMEWORK",
        help="Path to search for DM files (default: OPT-IN_FRAMEWORK/)",
    )
    args = parser.parse_args()
    
    search_path = args.path
    if not search_path.exists():
        print(f"ERROR: Search path does not exist: {search_path}")
        return 1
    
    print("[pub-brex-guard] Starting Data Module validation...")
    print(f"[pub-brex-guard] Search path: {search_path}")
    
    errors = validate_dm_files(search_path)
    
    if errors:
        print(f"\n[pub-brex-guard] ✗ Validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"  {error}")
        print("\nPlease fix the errors and re-run validation.")
        return 1
    
    print("[pub-brex-guard] ✓ All Data Module files passed validation!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
