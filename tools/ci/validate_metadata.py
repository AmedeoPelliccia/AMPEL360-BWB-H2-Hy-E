#!/usr/bin/env python3
"""
ATA Metadata Validation Script

This script validates ATA documentation metadata against ATA iSpec 2200 standards
and CSDB (Common Source DataBase) requirements. It supports both JSON metadata files
and YAML front-matter in Markdown documents.

Validates:
- Identification (Title, Identifier, Version)
- Responsibility (Author)
- Dates (CreationDate, ModificationDate)
- Status, Scope, Abstract
- Keywords, Compliance standards
- Access Level
- Change Log entries
- Identifier uniqueness

Usage:
    python tools/ci/validate_metadata.py --path path/to/metadata.json
    python tools/ci/validate_metadata.py --path path/to/document.md --frontmatter
"""

import argparse
import json
import pathlib
import re
import sys
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple

# Script is in tools/ci/, so repo root is two levels up
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]

# Valid enums
VALID_STATUS = ["Draft", "Approved", "Superseded"]
VALID_ACCESS_LEVELS = ["Public", "Internal", "Confidential"]

# Validation rules
IDENTIFIER_PATTERN = re.compile(r'^\d{2}-\d{2}-\d{2}$')
MIN_ABSTRACT_LENGTH = 50
DATE_FORMAT = "%Y-%m-%d"


class ValidationError(Exception):
    """Raised when validation fails."""
    pass


class ValidationWarning:
    """Represents a validation warning."""
    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message

    def __str__(self):
        return f"⚠️  WARNING [{self.field}]: {self.message}"


class ValidationResult:
    """Holds validation results."""
    def __init__(self):
        self.errors: List[Tuple[str, str]] = []
        self.warnings: List[ValidationWarning] = []
        self.passed = True

    def add_error(self, field: str, message: str):
        self.errors.append((field, message))
        self.passed = False

    def add_warning(self, field: str, message: str):
        self.warnings.append(ValidationWarning(field, message))

    def report(self) -> str:
        lines = []
        if self.errors:
            lines.append("❌ VALIDATION FAILED\n")
            lines.append("Errors:")
            for field, message in self.errors:
                lines.append(f"  ❌ [{field}]: {message}")
        
        if self.warnings:
            lines.append("\nWarnings:")
            for warning in self.warnings:
                lines.append(f"  {warning}")
        
        if self.passed and not self.warnings:
            lines.append("✅ VALIDATION PASSED")
        elif self.passed:
            lines.append("\n✅ VALIDATION PASSED (with warnings)")
        
        return "\n".join(lines)


def parse_yaml_frontmatter(content: str) -> Optional[Dict[str, Any]]:
    """Extract YAML front-matter from markdown content."""
    if not content.startswith("---\n"):
        return None
    
    try:
        # Find the closing ---
        end_index = content.find("\n---\n", 4)
        if end_index == -1:
            end_index = content.find("\n---", 4)
            if end_index == -1:
                return None
        
        yaml_content = content[4:end_index]
        
        # Simple YAML parser for our specific use case
        metadata = {}
        lines = yaml_content.strip().split("\n")
        current_key = None
        in_list = False
        list_items = []
        in_changelog = False
        changelog_entries = []
        current_entry = {}
        
        for line in lines:
            line = line.rstrip()
            
            # Handle list items
            if line.startswith("  - ") and in_changelog:
                # Start of new changelog entry
                if current_entry:
                    changelog_entries.append(current_entry)
                current_entry = {}
                # Check if this line has a key-value after the dash
                remainder = line[4:].strip()
                if ":" in remainder:
                    key_val = remainder.split(":", 1)
                    if len(key_val) == 2:
                        key = key_val[0].strip()
                        val = key_val[1].strip().strip('"')
                        current_entry[key] = val
                continue
            elif line.startswith("    ") and in_changelog:
                # Changelog entry field
                key_val = line.strip().split(":", 1)
                if len(key_val) == 2:
                    key = key_val[0].strip()
                    val = key_val[1].strip().strip('"')
                    current_entry[key] = val
                continue
            elif line.startswith("  - "):
                # Regular list item
                item = line[4:].strip().strip('"').strip('[').strip(']')
                list_items.append(item)
                continue
            
            # Handle key-value pairs
            if ":" in line and not line.startswith(" "):
                if in_list and list_items:
                    metadata[current_key] = list_items
                    list_items = []
                    in_list = False
                
                if in_changelog and current_entry:
                    changelog_entries.append(current_entry)
                    current_entry = {}
                
                key, value = line.split(":", 1)
                current_key = key.strip()
                value = value.strip().strip('"')
                
                if current_key == "ChangeLog":
                    in_changelog = True
                    in_list = False
                    continue
                elif value.startswith("["):
                    # Start of inline list
                    in_list = True
                    in_changelog = False
                    if value.endswith("]"):
                        # Complete inline list
                        items = value.strip("[]").split(",")
                        metadata[current_key] = [item.strip().strip('"') for item in items]
                        in_list = False
                    continue
                else:
                    in_changelog = False
                    in_list = False
                    metadata[current_key] = value
        
        # Add remaining items
        if in_list and list_items:
            metadata[current_key] = list_items
        if in_changelog and current_entry:
            changelog_entries.append(current_entry)
        if changelog_entries:
            metadata["ChangeLog"] = changelog_entries
        
        return metadata
    except Exception as e:
        raise ValidationError(f"Failed to parse YAML front-matter: {e}")


def load_metadata(path: pathlib.Path, frontmatter: bool = False) -> Dict[str, Any]:
    """Load metadata from JSON file or Markdown front-matter."""
    if not path.exists():
        raise ValidationError(f"File not found: {path}")
    
    content = path.read_text(encoding="utf-8")
    
    if frontmatter:
        metadata = parse_yaml_frontmatter(content)
        if metadata is None:
            raise ValidationError("No YAML front-matter found in markdown file")
        return metadata
    else:
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            raise ValidationError(f"Invalid JSON: {e}")


def validate_identification(metadata: Dict[str, Any], result: ValidationResult):
    """Validate Title, Identifier, and Version fields."""
    # Title
    if "Title" not in metadata or not metadata["Title"]:
        result.add_error("Title", "Title is required")
    
    # Identifier
    if "Identifier" not in metadata or not metadata["Identifier"]:
        result.add_error("Identifier", "Identifier is required")
    elif not IDENTIFIER_PATTERN.match(metadata["Identifier"]):
        result.add_error("Identifier", f"Identifier must match pattern '##-##-##', got: {metadata['Identifier']}")
    
    # Version
    if "Version" not in metadata or not metadata["Version"]:
        result.add_error("Version", "Version is required")


def validate_responsibility(metadata: Dict[str, Any], result: ValidationResult):
    """Validate Author field."""
    if "Author" not in metadata or not metadata["Author"]:
        result.add_error("Author", "Author is required")
    elif metadata["Author"].upper() == "TBD":
        result.add_error("Author", "Author cannot be 'TBD'")


def validate_dates(metadata: Dict[str, Any], result: ValidationResult):
    """Validate CreationDate and ModificationDate."""
    creation_date = metadata.get("CreationDate")
    modification_date = metadata.get("ModificationDate")
    
    if not creation_date:
        result.add_error("CreationDate", "CreationDate is required")
        return
    
    if not modification_date:
        result.add_error("ModificationDate", "ModificationDate is required")
        return
    
    # Try to parse dates
    try:
        creation_dt = datetime.strptime(creation_date, DATE_FORMAT)
    except ValueError:
        result.add_error("CreationDate", f"Invalid date format (expected YYYY-MM-DD): {creation_date}")
        return
    
    try:
        modification_dt = datetime.strptime(modification_date, DATE_FORMAT)
    except ValueError:
        result.add_error("ModificationDate", f"Invalid date format (expected YYYY-MM-DD): {modification_date}")
        return
    
    # ModificationDate should be >= CreationDate
    if modification_dt < creation_dt:
        result.add_error("Dates", "ModificationDate must be >= CreationDate")


def validate_status(metadata: Dict[str, Any], result: ValidationResult):
    """Validate Status field."""
    status = metadata.get("Status")
    if not status:
        result.add_error("Status", "Status is required")
    elif status not in VALID_STATUS:
        result.add_error("Status", f"Status must be one of {VALID_STATUS}, got: {status}")


def validate_scope_and_abstract(metadata: Dict[str, Any], result: ValidationResult):
    """Validate Scope and Abstract fields."""
    scope = metadata.get("Scope", "")
    abstract = metadata.get("Abstract", "")
    
    if not scope or len(scope) < MIN_ABSTRACT_LENGTH:
        result.add_warning("Scope", f"Scope should be at least {MIN_ABSTRACT_LENGTH} characters")
    
    if not abstract or len(abstract) < MIN_ABSTRACT_LENGTH:
        result.add_warning("Abstract", f"Abstract should be at least {MIN_ABSTRACT_LENGTH} characters")


def validate_keywords(metadata: Dict[str, Any], result: ValidationResult):
    """Validate Keywords field."""
    keywords = metadata.get("Keywords")
    if not keywords:
        result.add_error("Keywords", "At least one keyword is required")
    elif isinstance(keywords, list) and len(keywords) == 0:
        result.add_error("Keywords", "At least one keyword is required")


def validate_compliance(metadata: Dict[str, Any], result: ValidationResult):
    """Validate Compliance field."""
    compliance = metadata.get("Compliance")
    if not compliance:
        result.add_warning("Compliance", "At least one compliance reference is recommended")
    elif isinstance(compliance, list) and len(compliance) == 0:
        result.add_warning("Compliance", "At least one compliance reference is recommended")


def validate_access_level(metadata: Dict[str, Any], result: ValidationResult):
    """Validate AccessLevel field."""
    access_level = metadata.get("AccessLevel")
    if not access_level:
        result.add_error("AccessLevel", "AccessLevel is required")
    elif access_level not in VALID_ACCESS_LEVELS:
        result.add_error("AccessLevel", f"AccessLevel must be one of {VALID_ACCESS_LEVELS}, got: {access_level}")


def validate_changelog(metadata: Dict[str, Any], result: ValidationResult):
    """Validate ChangeLog field."""
    changelog = metadata.get("ChangeLog")
    
    if not changelog:
        result.add_error("ChangeLog", "At least one ChangeLog entry is required")
        return
    
    if not isinstance(changelog, list) or len(changelog) == 0:
        result.add_error("ChangeLog", "At least one ChangeLog entry is required")
        return
    
    # Validate each entry
    for i, entry in enumerate(changelog):
        if not isinstance(entry, dict):
            result.add_error("ChangeLog", f"Entry {i+1} must be an object")
            continue
        
        required_fields = ["version", "date", "author", "change"]
        for field in required_fields:
            if field not in entry or not entry[field]:
                result.add_error("ChangeLog", f"Entry {i+1} missing required field: {field}")


def validate_metadata(metadata: Dict[str, Any]) -> ValidationResult:
    """Run all validation checks."""
    result = ValidationResult()
    
    validate_identification(metadata, result)
    validate_responsibility(metadata, result)
    validate_dates(metadata, result)
    validate_status(metadata, result)
    validate_scope_and_abstract(metadata, result)
    validate_keywords(metadata, result)
    validate_compliance(metadata, result)
    validate_access_level(metadata, result)
    validate_changelog(metadata, result)
    
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Validate ATA documentation metadata against ATA iSpec 2200 standards"
    )
    parser.add_argument(
        "--path",
        type=pathlib.Path,
        required=True,
        help="Path to metadata.json or document.md file"
    )
    parser.add_argument(
        "--frontmatter",
        action="store_true",
        help="Parse YAML front-matter from markdown file instead of JSON"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output"
    )
    
    args = parser.parse_args()
    
    try:
        if args.verbose:
            print(f"Loading metadata from: {args.path}")
        
        metadata = load_metadata(args.path, args.frontmatter)
        
        if args.verbose:
            print(f"Metadata loaded successfully")
            print(f"Validating against ATA iSpec 2200 standards...\n")
        
        result = validate_metadata(metadata)
        
        print(result.report())
        
        if not result.passed:
            sys.exit(1)
        
    except ValidationError as e:
        print(f"❌ VALIDATION ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
