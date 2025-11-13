#!/usr/bin/env python3
"""
create_optin_structure.py

Creates the complete OPT-IN Framework directory structure with:
- 5 main axes (O, P, T, I, N)
- ATA chapters under each axis
- XX-00_GENERAL with 14 lifecycle folders
- 9 cross-ATA root buckets (10/20/30/40/50/60/70/80/90)
- README.md files explaining each component

Usage:
    python tools/ci/create_optin_structure.py [--dry-run]
"""

import argparse
import pathlib
import sys
from typing import List, Dict

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
FRAMEWORK_ROOT = REPO_ROOT / "OPT-IN_FRAMEWORK"

# OPT-IN Framework Axes and their ATA chapters
FRAMEWORK_STRUCTURE = {
    "O-ORGANIZATION": {
        "description": "Policies, limitations, and maintenance frameworks",
        "chapters": [
            ("00", "GENERAL"),
            ("01", "MAINTENANCE_POLICY_INFORMATION"),
            ("04", "AIRWORTHINESS_LIMITATIONS"),
            ("05", "TIME_LIMITS_MAINTENANCE_CHECKS"),
        ]
    },
    "P-PROGRAM": {
        "description": "Geometry, handling, servicing, and physical operations",
        "chapters": [
            ("06", "DIMENSIONS_AND_AREAS"),
            ("07", "LIFTING_AND_SHORING"),
            ("08", "LEVELING_AND_WEIGHING"),
            ("09", "TOWING_AND_TAXIING"),
            ("12", "SERVICING"),
        ]
    },
    "T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS": {
        "description": "On-board systems organized by AMEDEOPELLICCIA taxonomy",
        "subsystems": {
            "A-AIRFRAME": [
                ("20", "STANDARD_PRACTICES_AIRFRAME"),
                ("50", "CARGO_ACCESSORY_COMPARTMENTS"),
                ("51", "STANDARD_PRACTICES_STRUCTURES"),
                ("52", "DOORS"),
                ("53", "FUSELAGE"),
                ("54", "NACELLES_PYLONS"),
                ("55", "STABILIZERS"),
                ("56", "WINDOWS"),
                ("57", "WINGS"),
            ],
            "M-MECHANICS": [
                ("27", "FLIGHT_CONTROLS_ACTUATION"),
                ("29", "HYDRAULIC_POWER"),
                ("32", "LANDING_GEAR"),
                ("36", "PNEUMATIC"),
                ("37", "VACUUM_WASTE_DISPOSAL"),
                ("41", "WATER_BALLAST"),
            ],
            "E1-ENVIRONMENT": [
                ("21", "AIR_CONDITIONING_PRESSURIZATION"),
                ("26", "FIRE_PROTECTION"),
                ("30", "ICE_RAIN_PROTECTION"),
                ("38", "WATER_WASTE"),
            ],
            "D-DATA": [
                ("31", "INDICATING_RECORDING"),
            ],
            "E2-ENERGY": [
                ("24", "ELECTRICAL_POWER"),
                ("47", "INERTING_SYSTEM"),
                ("49", "AIRBORNE_AUXILIARY_POWER"),
                ("80", "STARTING"),
            ],
            "O-OPERATING_SYSTEMS": [
                ("42", "IMA_GOVERNANCE"),
            ],
            "P-PROPULSION": [
                ("60", "STANDARD_PRACTICES_PROPULSION"),
                ("61", "PROPELLERS_PROPULSORS"),
                ("70", "STANDARD_PRACTICES_ENGINE"),
                ("71", "POWER_PLANT"),
                ("72", "ENGINE"),
                ("73", "ENGINE_FUEL_CONTROL"),
                ("74", "IGNITION"),
                ("75", "AIR"),
                ("76", "ENGINE_CONTROLS"),
                ("78", "EXHAUST"),
                ("79", "OIL"),
            ],
            "E3-ELECTRONICS": [
                ("34", "NAVIGATION"),
                ("39", "ELECTRICAL_ELECTRONIC_PANELS"),
            ],
            "L1-LOGICS": [
                ("22", "AUTOFLIGHT"),
            ],
            "L2-LINKS": [
                ("23", "COMMUNICATIONS"),
                ("91", "CHARTS_FLIGHT_OPERATIONS"),
            ],
            "I-INFORMATION_INTELLIGENCE_INTERFACES": [
                ("45", "ONBOARD_MAINTENANCE_SYSTEMS"),
                ("46", "INFORMATION_SYSTEMS_DATALINK"),
                ("77", "ENGINE_INDICATING"),
                ("93", "ONBOARD_DATA_LOAD_CONFIGURATION"),
            ],
            "C1-COCKPIT_CABIN_CARGO": [
                ("11", "PLACARDS_MARKINGS"),
                ("15", "AIRCREW_INFORMATION"),
                ("16", "CHANGE_OF_ROLE"),
                ("25", "EQUIPMENT_FURNISHINGS"),
                ("33", "LIGHTS"),
                ("35", "OXYGEN"),
                ("44", "CABIN_SYSTEMS"),
            ],
            "C2-CIRCULAR_CRYOGENICS_SYSTEMS": [
                ("28", "FUEL_SAF_CRYOGENIC_H2"),
                ("99", "CARBON_ACCOUNTING"),
                ("100", "CIRCULAR_METRICS"),
            ],
            "I2-R_AND_D": [
                ("40", "MULTISYSTEM_AI_INTEGRATION"),
                ("48", "IN_FLIGHT_MAINTENANCE_AI_ENABLED"),
                ("92", "MODEL_BASED_MAINTENANCE"),
            ],
            "A2-AERODYNAMICS": [
                ("27", "FLIGHT_CONTROLS_AERODYNAMIC_MANIPULATION"),
            ],
        }
    },
    "I-INFRASTRUCTURES": {
        "description": "Airports, hydrogen value chains, supply chains, facilities",
        "chapters": [
            ("02", "OPERATIONS_INFORMATION"),
            ("03", "SUPPORT_INFORMATION_GSE"),
            ("10", "PARKING_MOORING_STORAGE_RTS"),
            ("13", "HARDWARE_AND_GENERAL_TOOLS"),
            ("85", "INFRASTRUCTURE_INTERFACE_STANDARDS"),
            ("115", "FLIGHT_SIMULATOR_SYSTEMS"),
            ("116", "FLIGHT_SIMULATOR_CUING_SYSTEM"),
        ]
    },
    "N-NEURAL_NETWORKS_USERS_TRACEABILITY": {
        "description": "Digital intelligence and Digital Product Passport",
        "chapters": [
            ("95", "DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS"),
            ("96", "NEURAL_NETWORK_TRAINING_DATA"),
            ("97", "NEURAL_NETWORK_MODELS"),
            ("98", "NEURAL_NETWORK_RUNTIME_MONITORING"),
        ]
    },
}

# 14 Lifecycle folders for XX-00_GENERAL
GENERAL_LIFECYCLE_FOLDERS = [
    ("01", "Overview", "ATA domain description and global architecture"),
    ("02", "Safety", "Safety framework and analysis methods"),
    ("03", "Requirements", "Requirements framework and traceability"),
    ("04", "Design", "Reference architectures and design patterns"),
    ("05", "Interfaces", "General interface rules and ICD templates"),
    ("06", "Engineering", "Approach to analysis, models and simulation"),
    ("07", "V_AND_V", "Global verification & validation strategy"),
    ("08", "Prototyping", "Prototyping and experimentation policy"),
    ("09", "Production_Planning", "Industrialization / deployment strategy"),
    ("10", "Certification", "Certification strategy and MoC catalog"),
    ("11", "EIS_Versions_Tags", "EIS, versions, CM and change control"),
    ("12", "Services", "In-service MRO and service models"),
    ("13", "Subsystems_Components", "Subsystems, components and PNR/source management"),
    ("14", "Ops_Std_Sustain", "Operational standards, governance, circularity"),
]

# 9 Cross-ATA Root Buckets
CROSS_ATA_BUCKETS = [
    ("10", "Operations", "Ops use, turnarounds, procedures"),
    ("20", "Subsystems", "Functional subsystems (design-driven)"),
    ("30", "Circularity", "Sustainability, LCA, reuse/recycle, DPP links"),
    ("40", "Software", "SW, control logic, diagnostics, ML/NN"),
    ("50", "Structures", "Frames, housings, mounts, structural routes"),
    ("60", "Storages", "Tanks, reservoirs, accumulators, cryo vessels"),
    ("70", "Propulsion", "Propulsive interfaces/couplings (if any)"),
    ("80", "Energy", "Electrical/thermal energy interactions"),
    ("90", "Tables_Schemas_Diagrams", "Tables, data dicts, catalogs, SDS/training"),
]


def create_axis_readme(axis_name: str, description: str) -> str:
    """Generate README content for an axis."""
    return f"""# {axis_name.replace('-', ' — ').replace('_', ' ')}

## Description

{description}

## Purpose

This axis of the OPT-IN Framework contains ATA chapters related to {description.lower()}.

## Structure

Each ATA chapter within this axis follows the mandatory structure:

- **XX-00_GENERAL/**: 14 lifecycle folders (canonical template from ATA 95)
- **XX-10_Operations/**: Operational use and procedures
- **XX-20_Subsystems/**: Functional subsystems
- **XX-30_Circularity/**: Sustainability and life cycle
- **XX-40_Software/**: Software and control logic
- **XX-50_Structures/**: Physical structures
- **XX-60_Storages/**: Storage systems
- **XX-70_Propulsion/**: Propulsion interfaces
- **XX-80_Energy/**: Energy interactions
- **XX-90_Tables_Schemas_Diagrams/**: Documentation and data

## Compliance

All chapters in this axis comply with:
- ATA iSpec 2200 documentation standards
- EASA CS-25 / FAA 14 CFR Part 25 requirements
- AMPEL360 OPT-IN Framework Standard v1.1

## Document Control

- **Status**: Active
- **Owner**: AMPEL360 Documentation WG
- **Last Updated**: 2025-11-13
"""


def create_ata_chapter_readme(ata_num: str, ata_name: str, axis_name: str) -> str:
    """Generate README content for an ATA chapter."""
    return f"""# ATA {ata_num} — {ata_name.replace('_', ' ')}

## Overview

This is ATA Chapter {ata_num}: {ata_name.replace('_', ' ')}, part of the {axis_name.replace('-', ' — ').replace('_', ' ')} axis.

## Structure

This chapter follows the mandatory OPT-IN Framework structure:

### {ata_num}-00_GENERAL (Lifecycle Folders)

The GENERAL layer contains 14 mandatory lifecycle folders covering the complete development cycle:

1. **{ata_num}-00-01_Overview**: System overview and global architecture
2. **{ata_num}-00-02_Safety**: Safety framework and analysis
3. **{ata_num}-00-03_Requirements**: Requirements and traceability
4. **{ata_num}-00-04_Design**: Design specifications and patterns
5. **{ata_num}-00-05_Interfaces**: Interface control documents
6. **{ata_num}-00-06_Engineering**: Analysis, models, and simulation
7. **{ata_num}-00-07_V_AND_V**: Verification and validation
8. **{ata_num}-00-08_Prototyping**: Prototype development
9. **{ata_num}-00-09_Production_Planning**: Manufacturing planning
10. **{ata_num}-00-10_Certification**: Certification evidence
11. **{ata_num}-00-11_EIS_Versions_Tags**: Configuration management
12. **{ata_num}-00-12_Services**: Maintenance and service
13. **{ata_num}-00-13_Subsystems_Components**: Component breakdown
14. **{ata_num}-00-14_Ops_Std_Sustain**: Operational standards

### Cross-ATA Root Buckets

The following buckets are mandatory in every ATA chapter:

- **{ata_num}-10_Operations**: Operational procedures and use cases
- **{ata_num}-20_Subsystems**: Functional subsystems (design-driven internal structure)
- **{ata_num}-30_Circularity**: Sustainability, LCA, and circular economy
- **{ata_num}-40_Software**: Software, control logic, and AI/ML
- **{ata_num}-50_Structures**: Physical structures and frames
- **{ata_num}-60_Storages**: Tanks, reservoirs, and storage
- **{ata_num}-70_Propulsion**: Propulsion interfaces (if applicable)
- **{ata_num}-80_Energy**: Energy management and distribution
- **{ata_num}-90_Tables_Schemas_Diagrams**: Data tables and documentation

## Document Control

- **ATA Chapter**: {ata_num}
- **Status**: Active
- **Owner**: AMPEL360 Documentation WG
- **Standard**: OPT-IN Framework v1.1
- **Last Updated**: 2025-11-13
"""


def create_general_folder_readme(ata_num: str, folder_num: str, folder_name: str, description: str) -> str:
    """Generate README content for a GENERAL lifecycle folder."""
    return f"""# {ata_num}-00-{folder_num}_{folder_name}

## Purpose

{description}

## Scope

This folder is part of the **{ata_num}-00_GENERAL** layer, which provides governance and lifecycle management for ATA Chapter {ata_num}.

## Contents

This folder should contain:
- Documentation related to {description.lower()}
- Traceability matrices linking to other lifecycle stages
- Evidence and artifacts supporting this lifecycle phase

## Status

- **Phase**: {folder_name.replace('_', ' ')}
- **Lifecycle Position**: {folder_num} of 14
- **Status**: Active
- **Last Updated**: 2025-11-13

## Related Folders

Part of the canonical 14-folder lifecycle:
1. Overview → 2. Safety → 3. Requirements → 4. Design → 5. Interfaces → 6. Engineering → 7. V&V → 8. Prototyping → 9. Production Planning → 10. Certification → 11. EIS/Versions/Tags → 12. Services → 13. Subsystems/Components → 14. Ops/Std/Sustain

## Document Control

- **Standard**: OPT-IN Framework v1.1 (ATA 95 canonical template)
- **Owner**: AMPEL360 Documentation WG
"""


def create_bucket_readme(ata_num: str, bucket_num: str, bucket_name: str, description: str) -> str:
    """Generate README content for a cross-ATA bucket."""
    return f"""# {ata_num}-{bucket_num}_{bucket_name}

## Purpose

{description}

## Scope

This is a **cross-ATA root bucket** present in every ATA chapter. It provides a consistent location for {description.lower()}.

## Internal Structure

The internal structure of this bucket is **design-driven** and flexible:
- Organize contents based on how systems are conceived, designed, and implemented
- No mandatory 01-14 lifecycle duplication within buckets
- Maintain traceability to lifecycle phases via metadata or index files

## Naming Convention

Items within this bucket follow the pattern:
- **{ata_num}-{bucket_num}-XX_DESCRIPTION**
  - {ata_num} = ATA chapter
  - {bucket_num} = Bucket number
  - XX = Sequential number (00, 01, 02, etc.)
  - DESCRIPTION = Descriptive name

## Status

- **Bucket**: {bucket_num}_{bucket_name}
- **Status**: Active
- **Applicability**: {"Universal (all ATA chapters)" if bucket_num != "70" else "Conditional (applicable chapters only)"}
- **Last Updated**: 2025-11-13

## Document Control

- **Standard**: OPT-IN Framework v1.1
- **Owner**: AMPEL360 Documentation WG

---

**Note**: If this bucket is not applicable to ATA {ata_num}, document the reason here. Do not remove the bucket.
"""


def create_structure(dry_run: bool = False) -> int:
    """Create the complete OPT-IN Framework structure."""
    print("[create-optin] Creating OPT-IN Framework structure...")
    if dry_run:
        print("[create-optin] DRY RUN MODE - no files will be created")
    
    created_dirs = 0
    created_files = 0
    
    # Create framework root
    if not dry_run:
        FRAMEWORK_ROOT.mkdir(parents=True, exist_ok=True)
    created_dirs += 1
    
    # Process each axis
    for axis_name, axis_data in FRAMEWORK_STRUCTURE.items():
        axis_path = FRAMEWORK_ROOT / axis_name
        print(f"\n[create-optin] Processing axis: {axis_name}")
        
        if not dry_run:
            axis_path.mkdir(parents=True, exist_ok=True)
            readme_path = axis_path / "README.md"
            if not readme_path.exists():
                readme_path.write_text(
                    create_axis_readme(axis_name, axis_data["description"]),
                    encoding="utf-8"
                )
                created_files += 1
        created_dirs += 1
        
        # Handle Technology axis with subsystems
        if "subsystems" in axis_data:
            for subsystem_name, chapters in axis_data["subsystems"].items():
                subsystem_path = axis_path / subsystem_name
                print(f"  [create-optin] Creating subsystem: {subsystem_name}")
                
                if not dry_run:
                    subsystem_path.mkdir(parents=True, exist_ok=True)
                created_dirs += 1
                
                for ata_num, ata_name in chapters:
                    dirs, files = create_ata_chapter(
                        subsystem_path, ata_num, ata_name, axis_name, dry_run
                    )
                    created_dirs += dirs
                    created_files += files
        
        # Handle regular chapters
        elif "chapters" in axis_data:
            for ata_num, ata_name in axis_data["chapters"]:
                dirs, files = create_ata_chapter(
                    axis_path, ata_num, ata_name, axis_name, dry_run
                )
                created_dirs += dirs
                created_files += files
    
    print(f"\n[create-optin] Summary:")
    print(f"  Directories: {created_dirs}")
    print(f"  Files: {created_files}")
    
    if dry_run:
        print("\n[create-optin] DRY RUN completed - no actual changes made")
    else:
        print("\n[create-optin] OPT-IN Framework structure created successfully!")
    
    return 0


def create_ata_chapter(
    parent_path: pathlib.Path,
    ata_num: str,
    ata_name: str,
    axis_name: str,
    dry_run: bool
) -> tuple:
    """Create a single ATA chapter with all required structure."""
    chapter_name = f"ATA_{ata_num}-{ata_name}"
    chapter_path = parent_path / chapter_name
    
    dirs_created = 0
    files_created = 0
    
    print(f"    [create-optin] Creating chapter: {chapter_name}")
    
    if not dry_run:
        chapter_path.mkdir(parents=True, exist_ok=True)
        readme_path = chapter_path / "README.md"
        if not readme_path.exists():
            readme_path.write_text(
                create_ata_chapter_readme(ata_num, ata_name, axis_name),
                encoding="utf-8"
            )
            files_created += 1
    dirs_created += 1
    
    # Create XX-00_GENERAL with 14 lifecycle folders
    general_path = chapter_path / f"{ata_num}-00_GENERAL"
    if not dry_run:
        general_path.mkdir(parents=True, exist_ok=True)
    dirs_created += 1
    
    for folder_num, folder_name, description in GENERAL_LIFECYCLE_FOLDERS:
        folder_path = general_path / f"{ata_num}-00-{folder_num}_{folder_name}"
        if not dry_run:
            folder_path.mkdir(parents=True, exist_ok=True)
            readme_path = folder_path / "README.md"
            if not readme_path.exists():
                readme_path.write_text(
                    create_general_folder_readme(ata_num, folder_num, folder_name, description),
                    encoding="utf-8"
                )
                files_created += 1
        dirs_created += 1
    
    # Create 9 cross-ATA buckets
    for bucket_num, bucket_name, description in CROSS_ATA_BUCKETS:
        bucket_path = chapter_path / f"{ata_num}-{bucket_num}_{bucket_name}"
        if not dry_run:
            bucket_path.mkdir(parents=True, exist_ok=True)
            readme_path = bucket_path / "README.md"
            if not readme_path.exists():
                readme_path.write_text(
                    create_bucket_readme(ata_num, bucket_num, bucket_name, description),
                    encoding="utf-8"
                )
                files_created += 1
        dirs_created += 1
    
    return dirs_created, files_created


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create the complete OPT-IN Framework directory structure"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without actually creating files",
    )
    args = parser.parse_args()
    
    return create_structure(dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
