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
Generate complete OPT-IN Framework Neural Network Subsystem structure
Location: tools/scripts/generate_nn_subsystem.py
"""

import sys
from pathlib import Path
from typing import Dict
import yaml
from datetime import datetime

SUBSYSTEM_TEMPLATE = {
    'docs': [
        '{id}-001_{name}_Overview.md',
        '{id}-002_{component1}.md',
        '{id}-003_{component2}.md',
        '{id}-004_{component3}.md',
        '{id}-005_{component4}.md',
        '{id}-008_Integration_with_ATA_{ata}.md',
        '{id}-009_Safety_and_Certification.md',
        '{id}-010_Operational_Procedures.md'
    ],
    'meta': [
        '{id}-011_{name}_Taxonomy.md',
        '{id}-012_{name}_Traceability_Map.csv',
        '{id}-013_{name}_Assets_Registry.json',
        '{id}-014_CAOS_{name}_Hooks.md'
    ],
    'folders': [
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
}

DOC_TEMPLATES = {
    'overview': """# {full_name} - Overview

**Subsystem ID**: {subsystem_id}  
**Parent ATA**: ATA {ata} - {ata_name}  
**Version**: 1.0  
**Status**: WORKING

## Executive Summary

[TODO: Describe the neural network subsystem purpose and key capabilities]

## System Architecture

[TODO: Add system architecture diagram]

## Neural Network Models Summary

| Model | Purpose | Architecture | Inference Rate | DAL |
|-------|---------|--------------|----------------|-----|
| Model 1 | [Purpose] | [Type] | [Rate] | [Level] |

## Integration Points

### Inputs from ATA {ata}
- [List sensor inputs]

### Outputs to ATA {ata}
- [List control outputs]

## Traceability

### Requirements
- [Link to requirements]

### Design
- [Link to design documents]

---

## Document Control
- **Originator**: AI prompted by Amedeo Pelliccia
- **Toolchain**: GitHub Copilot + MCP Doc Control Server
- **Related file**: `{filename}`
- **Status**: `WORKING`
- **Parent ATA**: [ATA {ata}](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA/...)
- **Version**: 1.0
- **Last Updated**: {date}
"""
}

def generate_subsystem(
    subsystem_num: str,
    subsystem_name: str,
    ata_chapter: str,
    ata_name: str,
    output_dir: Path
):
    """Generate complete subsystem structure"""
    
    subsystem_id = f"95-20-{subsystem_num}"
    full_name = f"NN_{subsystem_name}"
    subsystem_dir = output_dir / f"{subsystem_id}_{full_name}"
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    print(f"\n{'='*80}")
    print(f"Generating Neural Network Subsystem: {subsystem_id}_{full_name}")
    print(f"{'='*80}\n")
    
    # Create folder structure
    print("Creating folder structure...")
    for folder in SUBSYSTEM_TEMPLATE['folders']:
        folder_path = subsystem_dir / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {folder}")
    
    # Create root documents
    print("\nCreating root documents...")
    for doc_template in SUBSYSTEM_TEMPLATE['docs']:
        doc_name = doc_template.format(
            id=subsystem_id,
            name=full_name,
            component1='Component_1',
            component2='Component_2',
            component3='Component_3',
            component4='Component_4',
            ata=ata_chapter
        )
        doc_path = subsystem_dir / doc_name
        
        # Create with template content
        if '001' in doc_name:  # Overview doc
            content = DOC_TEMPLATES['overview'].format(
                full_name=full_name,
                subsystem_id=subsystem_id,
                ata=ata_chapter,
                ata_name=ata_name,
                filename=doc_name,
                date=current_date
            )
            doc_path.write_text(content)
        else:
            # Placeholder for other docs
            doc_path.write_text(f"# {doc_name}\n\n[TODO: Add content]\n\n## Document Control\n- **Status**: PLACEHOLDER\n- **Last Updated**: {current_date}\n")
        
        print(f"  ✓ {doc_name}")
    
    # Create META documents
    print("\nCreating META documents...")
    meta_dir = subsystem_dir / '00_META'
    for doc_template in SUBSYSTEM_TEMPLATE['meta']:
        doc_name = doc_template.format(
            id=subsystem_id,
            name=full_name,
            ata=ata_chapter
        )
        doc_path = meta_dir / doc_name
        
        if doc_name.endswith('.csv'):
            # Traceability matrix template
            content = "Requirement,Design,Interface,Engineering,Verification,Notes\n"
            content += f"RQ-95-03-XXX,95-00-04-AXXX,{subsystem_id}-XXX,95-00-06-XX-XXX,95-00-07-XX-XXX,TODO\n"
            doc_path.write_text(content)
        elif doc_name.endswith('.json'):
            # Assets registry template
            registry = {
                "subsystem_id": subsystem_id,
                "subsystem_name": full_name,
                "version": "1.0",
                "last_updated": current_date,
                "assets": [],
                "metadata": {
                    "total_assets": 0,
                    "assets_complete": 0,
                    "assets_placeholder": 0,
                    "last_audit": current_date,
                    "audit_status": "Initial creation"
                }
            }
            doc_path.write_text(json.dumps(registry, indent=2))
        else:
            doc_path.write_text(f"# {doc_name}\n\n[TODO: Add content]\n\n## Document Control\n- **Status**: PLACEHOLDER\n- **Last Updated**: {current_date}\n")
        
        print(f"  ✓ {doc_name}")
    
    # Create README
    print("\nCreating README...")
    readme_content = f"""# {subsystem_id}_{full_name}

Neural Network subsystem for ATA {ata_chapter} - {ata_name}

## Structure

- **Root**: Core subsystem documentation
- **00_META/**: Taxonomy, traceability, asset registry
- **ASSETS/**: Architecture diagrams, model cards, test data, certification
- **Models/**: Source code, trained models, configs
- **Data/**: Training, validation, synthetic datasets
- **Tests/**: Unit, integration, HIL tests
- **Documentation/**: Operations manual, maintenance, training

## Quick Start

1. Review `{subsystem_id}-001_{full_name}_Overview.md`
2. Check model cards in `ASSETS/Model_Cards/`
3. Review integration doc `{subsystem_id}-008_Integration_with_ATA_{ata_chapter}.md`

## Status

**Version**: 1.0  
**Status**: WORKING  
**Last Updated**: {current_date}
"""
    (subsystem_dir / 'README.md').write_text(readme_content)
    print(f"  ✓ README.md")
    
    print(f"\n{'='*80}")
    print(f"✅ Subsystem structure generated successfully!")
    print(f"   Location: {subsystem_dir}")
    print(f"{'='*80}\n")
    
    return subsystem_dir

def main():
    """Main generation routine"""
    
    if len(sys.argv) < 5:
        print("Usage: generate_nn_subsystem.py <subsystem_num> <name> <ata_chapter> <ata_name>")
        print("\nExample:")
        print("  generate_nn_subsystem.py 27 Flight_Controls 27 'Flight Controls'")
        sys.exit(1)
    
    subsystem_num = sys.argv[1]
    subsystem_name = sys.argv[2]
    ata_chapter = sys.argv[3]
    ata_name = sys.argv[4]
    
    # Determine output directory
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent.parent
    output_dir = repo_root / 'OPT-IN_FRAMEWORK' / 'N-NEURAL_NETWORKS_USERS_TRACEABILITY' / 'ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS' / '95-20_Subsystems'
    
    # Make sure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    generate_subsystem(subsystem_num, subsystem_name, ata_chapter, ata_name, output_dir)

if __name__ == '__main__':
    # Need json module
    import json
    main()
