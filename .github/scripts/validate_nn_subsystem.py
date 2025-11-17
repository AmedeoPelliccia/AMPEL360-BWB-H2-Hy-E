# Copyright 2025 AMPEL360 Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python3
"""
Validate OPT-IN Framework Neural Network Subsystem Structure
Location: .github/scripts/validate_nn_subsystem.py
"""

import sys
from pathlib import Path
from typing import Dict, List, Tuple
import yaml
import json
import csv
import re

REQUIRED_SUBSYSTEM_STRUCTURE = {
    'root_docs': {
        'range': (1, 10),
        'pattern': r'95-20-\d{2}-\d{3}_.*\.md'
    },
    'meta_docs': {
        'range': (11, 20),
        'pattern': r'95-20-\d{2}-\d{3}_.*\.(md|csv|json)'
    },
    'assets': {
        'architecture': (1, 10),
        'model_cards': (101, 199),
        'performance_data': (201, 299),
        'test_data': (301, 399),
        'interface_specs': (401, 499),
        'certification': (501, 599)
    },
    'data_files': {
        'range': (601, 699),
        'pattern': r'95-20-\d{2}-\d{3}_.*\.(parquet|csv|json)'
    },
    'hil_tests': {
        'range': (701, 799),
        'pattern': r'95-20-\d{2}-\d{3}_.*\.yaml'
    },
    'documentation': {
        'range': (801, 899),
        'pattern': r'95-20-\d{2}-\d{3}_.*\.(md|pdf)'
    }
}

MANDATORY_DOCUMENTS = [
    '95-20-{subsystem}-001_*_Overview.md',
    '95-20-{subsystem}-008_Integration_with_ATA_*.md',
    '95-20-{subsystem}-009_Safety_and_Certification.md',
    '95-20-{subsystem}-010_Operational_Procedures.md'
]

MANDATORY_FOLDERS = [
    '00_META',
    'ASSETS/Architecture',
    'ASSETS/Model_Cards',
    'ASSETS/Performance_Data',
    'ASSETS/Test_Data',
    'ASSETS/Interface_Specs',
    'ASSETS/Certification',
    'Models/Source',
    'Models/Trained',
    'Models/Configs',
    'Data/Training_Datasets',
    'Data/Validation_Datasets',
    'Data/Synthetic_Data',
    'Tests/Unit_Tests',
    'Tests/Integration_Tests',
    'Tests/HIL_Tests',
    'Documentation',
    'Documentation/Training_Materials'
]

def validate_subsystem_structure(subsystem_path: Path) -> Tuple[bool, List[str]]:
    """Validate complete subsystem structure"""
    
    errors = []
    
    # Extract subsystem number (e.g., "21" from "95-20-21_NN_ECS")
    subsystem_name = subsystem_path.name
    if not subsystem_name.startswith('95-20-'):
        errors.append(f"Invalid subsystem name: {subsystem_name}")
        return False, errors
    
    subsystem_num = subsystem_name.split('_')[0].split('-')[2]
    
    # Check mandatory folders
    for folder in MANDATORY_FOLDERS:
        folder_path = subsystem_path / folder
        if not folder_path.exists():
            errors.append(f"Missing mandatory folder: {folder}")
    
    # Check mandatory documents (using glob patterns for flexibility)
    for doc_template in MANDATORY_DOCUMENTS:
        doc_pattern = doc_template.format(subsystem=subsystem_num, ata='*')
        matching_files = list(subsystem_path.glob(doc_pattern))
        if not matching_files:
            errors.append(f"Missing mandatory document matching pattern: {doc_pattern}")
    
    # Validate naming conventions
    errors.extend(validate_naming(subsystem_path, subsystem_num))
    
    # Validate model cards
    errors.extend(validate_model_cards(subsystem_path))
    
    # Validate traceability
    errors.extend(validate_traceability(subsystem_path))
    
    return len(errors) == 0, errors

def validate_naming(subsystem_path: Path, subsystem_num: str) -> List[str]:
    """Validate file naming conventions"""
    
    errors = []
    expected_pattern = f"95-20-{subsystem_num}-"
    
    # Check all markdown files in root (except README.md)
    for md_file in subsystem_path.glob('*.md'):
        if md_file.name == 'README.md':
            continue  # README.md is allowed
        if not md_file.name.startswith(expected_pattern):
            errors.append(f"Incorrect naming: {md_file.name}")
    
    # Check META folder
    meta_path = subsystem_path / '00_META'
    if meta_path.exists():
        for file in meta_path.iterdir():
            if file.is_file() and not file.name.startswith(expected_pattern):
                errors.append(f"Incorrect META naming: {file.name}")
    
    # Check ASSETS
    assets_path = subsystem_path / 'ASSETS'
    if assets_path.exists():
        for asset_file in assets_path.rglob('*'):
            if asset_file.is_file():
                name = asset_file.name
                # Should follow 95-20-XX-A-YYY pattern
                if not name.startswith(f"95-20-{subsystem_num}-A-"):
                    errors.append(f"Incorrect ASSET naming: {name}")
    
    return errors

def validate_model_cards(subsystem_path: Path) -> List[str]:
    """Validate model card completeness"""
    
    errors = []
    model_cards_path = subsystem_path / 'ASSETS' / 'Model_Cards'
    
    if not model_cards_path.exists():
        return [f"Model_Cards folder missing"]
    
    required_fields = [
        'model_card.name',
        'model_card.version',
        'model_card.model_id',
        'architecture.type',
        'performance.metrics',
        'deployment.target',
        'certification.dal_level',
        'dpp_integration.blockchain_anchor'
    ]
    
    for card_file in model_cards_path.glob('*.yaml'):
        try:
            with open(card_file, 'r') as f:
                card_data = yaml.safe_load(f)
            
            # Skip placeholder/template files
            if card_data and isinstance(card_data, dict):
                status = card_data.get('model_card', {}).get('status', '')
                if status in ['template', 'PLACEHOLDER']:
                    continue
                
                # Check required fields for non-template files
                for field in required_fields:
                    keys = field.split('.')
                    data = card_data
                    for key in keys:
                        if data is None or not isinstance(data, dict) or key not in data:
                            errors.append(f"{card_file.name}: Missing field '{field}'")
                            break
                        data = data[key]
        
        except Exception as e:
            errors.append(f"{card_file.name}: Parse error - {e}")
    
    return errors

def validate_traceability(subsystem_path: Path) -> List[str]:
    """Validate traceability matrix completeness"""
    
    errors = []
    
    trace_files = list((subsystem_path / '00_META').glob('*Traceability*.csv'))
    
    if not trace_files:
        errors.append("Missing traceability matrix CSV")
        return errors
    
    # Check that traceability file has required columns
    required_columns = ['Requirement', 'Design', 'Interface', 'Engineering', 'Verification']
    
    for trace_file in trace_files:
        try:
            with open(trace_file, 'r') as f:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames
                
                if fieldnames is None:
                    errors.append(f"{trace_file.name}: No columns found")
                    continue
                
                for col in required_columns:
                    if col not in fieldnames:
                        errors.append(f"{trace_file.name}: Missing column '{col}'")
        
        except Exception as e:
            errors.append(f"{trace_file.name}: Parse error - {e}")
    
    return errors

def main():
    """Main validation routine"""
    
    if len(sys.argv) < 2:
        print("Usage: validate_nn_subsystem.py <subsystem_path>")
        sys.exit(1)
    
    subsystem_path = Path(sys.argv[1])
    
    if not subsystem_path.exists():
        print(f"❌ Subsystem path does not exist: {subsystem_path}")
        sys.exit(1)
    
    print(f"\n{'='*80}")
    print(f"Validating Neural Network Subsystem: {subsystem_path.name}")
    print(f"{'='*80}\n")
    
    valid, errors = validate_subsystem_structure(subsystem_path)
    
    if valid:
        print("✅ Subsystem structure is valid!")
        print(f"   - All mandatory folders present")
        print(f"   - All mandatory documents present")
        print(f"   - Naming conventions compliant")
        print(f"   - Model cards complete")
        print(f"   - Traceability matrix present")
        sys.exit(0)
    else:
        print(f"❌ Validation failed with {len(errors)} errors:\n")
        for error in errors:
            print(f"   - {error}")
        sys.exit(1)

if __name__ == '__main__':
    main()
