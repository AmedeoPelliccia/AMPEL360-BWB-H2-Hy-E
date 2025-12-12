#!/usr/bin/env python3
"""
Validate DPP Export v0.1 JSON files against their schemas.

This script validates example JSON documents against the JSON Schema draft-07
definitions for the Aircraft Baseline DPP Export v0.1 package.
"""

import json
import logging
import sys
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import jsonschema
    from jsonschema import Draft7Validator
except ImportError:
    logging.error("jsonschema module not found. Install with: pip install jsonschema>=4.20.0")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)


def load_json_file(filepath: Path) -> Dict:
    """Load and parse a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON in {filepath}: {e}")
        sys.exit(1)
    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
        sys.exit(1)


def validate_json_against_schema(
    data: Dict,
    schema: Dict,
    data_name: str,
    schema_name: str
) -> Tuple[bool, List[str]]:
    """
    Validate JSON data against a schema.
    
    Args:
        data: The JSON data to validate
        schema: The JSON Schema to validate against
        data_name: Human-readable name of the data file (for error messages)
        schema_name: Human-readable name of the schema file (for error messages)
    
    Returns:
        Tuple of (is_valid, errors_list)
    """
    errors = []
    
    # Create validator
    try:
        validator = Draft7Validator(schema)
    except jsonschema.exceptions.SchemaError as e:
        errors.append(f"Invalid schema {schema_name}: {e}")
        return False, errors
    
    # Validate
    try:
        validation_errors = list(validator.iter_errors(data))
    except (AttributeError, TypeError) as e:
        # Catch errors that occur during validation due to malformed schema
        errors.append(f"Error validating against schema {schema_name}: {str(e)}")
        return False, errors
    
    if validation_errors:
        for error in validation_errors:
            path = " -> ".join(str(p) for p in error.path) if error.path else "root"
            errors.append(f"  At '{path}': {error.message}")
        return False, errors
    
    return True, []


def main():
    """Main validation function."""
    # Define paths relative to repository root
    repo_root = Path(__file__).parent.parent
    schemas_dir = repo_root / "schemas" / "dpp_export" / "v0.1"
    examples_dir = repo_root / "examples" / "dpp_export" / "v0.1"
    
    # Define schema and example pairs to validate
    validation_pairs = [
        ("manifest.schema.json", "manifest.json"),
        ("baseline.schema.json", "baseline.json"),
        ("effectivity.schema.json", "effectivity.json"),
        ("software_bom.schema.json", "software_bom.json"),
    ]
    
    logging.info("=" * 70)
    logging.info("DPP Export v0.1 Validation")
    logging.info("=" * 70)
    logging.info("")
    
    # Check directories exist
    if not schemas_dir.exists():
        logging.error(f"Schemas directory not found: {schemas_dir}")
        sys.exit(1)
    
    if not examples_dir.exists():
        logging.error(f"Examples directory not found: {examples_dir}")
        sys.exit(1)
    
    all_valid = True
    results = []
    
    # Validate each pair
    for schema_file, example_file in validation_pairs:
        schema_path = schemas_dir / schema_file
        example_path = examples_dir / example_file
        
        logging.info(f"Validating: {example_file}")
        logging.info(f"Against:    {schema_file}")
        
        # Load files
        schema = load_json_file(schema_path)
        data = load_json_file(example_path)
        
        # Validate
        is_valid, errors = validate_json_against_schema(
            data, schema, example_file, schema_file
        )
        
        if is_valid:
            logging.info("✓ VALID")
            results.append((example_file, True, []))
        else:
            logging.warning("✗ INVALID")
            for error in errors:
                logging.warning(error)
            results.append((example_file, False, errors))
            all_valid = False
        
        logging.info("")
    
    # Print summary
    logging.info("=" * 70)
    logging.info("Validation Summary")
    logging.info("=" * 70)
    
    valid_count = sum(1 for _, is_valid, _ in results if is_valid)
    total_count = len(results)
    
    logging.info(f"Total files validated: {total_count}")
    logging.info(f"Valid: {valid_count}")
    logging.info(f"Invalid: {total_count - valid_count}")
    logging.info("")
    
    if all_valid:
        logging.info("✓ All DPP Export v0.1 examples are valid!")
        return 0
    else:
        logging.warning("✗ Some DPP Export v0.1 examples have validation errors.")
        logging.warning("")
        logging.warning("Failed validations:")
        for name, is_valid, errors in results:
            if not is_valid:
                logging.warning(f"  - {name}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
