# OPT-IN Framework

**Version:** 1.1  
**Date:** 2025-11-13  
**Status:** Active

## Overview

The **OPT-IN Framework** is the mandatory program documentation topology for AMPEL360, providing a structured, certification-grade approach to organizing all technical documentation for the Blended-Wing-Body hydrogen-hybrid aircraft program.

## Purpose

The OPT-IN Framework unifies:

1. **The OPT-IN axes** (O, P, T, I, N) and their ATA mappings
2. **The canonical XX-00_GENERAL 14-folder lifecycle**
3. **The cross-ATA root buckets** (XX-10/20/30/40/50/60/70/80/90) present in every ATA chapter

This enforces **certification-grade traceability**, **consistent navigation**, and **CI validation**.

## Framework Structure

```
OPT-IN_FRAMEWORK/
├── O-ORGANIZATION/                  # Policies, limitations, maintenance frameworks
│   ├── ATA_00-GENERAL/
│   ├── ATA_01-MAINTENANCE_POLICY_INFORMATION/
│   ├── ATA_04-AIRWORTHINESS_LIMITATIONS/
│   └── ATA_05-TIME_LIMITS_MAINTENANCE_CHECKS/
│
├── P-PROGRAM/                       # Geometry, handling, servicing, operations
│   ├── ATA_06-DIMENSIONS_AND_AREAS/
│   ├── ATA_07-LIFTING_AND_SHORING/
│   ├── ATA_08-LEVELING_AND_WEIGHING/
│   ├── ATA_09-TOWING_AND_TAXIING/
│   └── ATA_12-SERVICING/
│
├── T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/  # On-board systems
│   ├── A-AIRFRAME/                  # ATA 20, 50-57
│   ├── M-MECHANICS/                 # ATA 27, 29, 32, 36, 37, 41
│   ├── E1-ENVIRONMENT/              # ATA 21, 26, 30, 38
│   ├── D-DATA/                      # ATA 31
│   ├── E2-ENERGY/                   # ATA 24, 47, 49, 80
│   ├── O-OPERATING_SYSTEMS/         # ATA 42
│   ├── P-PROPULSION/                # ATA 60-61, 70-79
│   ├── E3-ELECTRONICS/              # ATA 34, 39, 42
│   ├── L1-LOGICS/                   # ATA 22, 27, 42
│   ├── L2-LINKS/                    # ATA 23, 42, 91
│   ├── I-INFORMATION_INTELLIGENCE_INTERFACES/  # ATA 31, 42, 45, 46, 77, 93
│   ├── C1-COCKPIT_CABIN_CARGO/      # ATA 11, 15, 16, 25, 33, 35, 44
│   ├── C2-CIRCULAR_CRYOGENICS_SYSTEMS/  # ATA 28, 99, 100
│   ├── I2-R_AND_D/                  # ATA 40, 48, 92
│   └── A2-AERODYNAMICS/             # ATA 27
│
├── I-INFRASTRUCTURES/               # Airports, H₂ chains, facilities
│   ├── ATA_02-OPERATIONS_INFORMATION/
│   ├── ATA_03-SUPPORT_INFORMATION_GSE/
│   ├── ATA_10-PARKING_MOORING_STORAGE_RTS/
│   ├── ATA_13-HARDWARE_AND_GENERAL_TOOLS/
│   ├── ATA_85-INFRASTRUCTURE_INTERFACE_STANDARDS/
│   ├── ATA_115-FLIGHT_SIMULATOR_SYSTEMS/
│   └── ATA_116-FLIGHT_SIMULATOR_CUING_SYSTEM/
│
└── N-NEURAL_NETWORKS_USERS_TRACEABILITY/  # Digital intelligence, DPP
    ├── ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/  # Canonical template
    ├── ATA_96-NEURAL_NETWORK_TRAINING_DATA/
    ├── ATA_97-NEURAL_NETWORK_MODELS/
    └── ATA_98-NEURAL_NETWORK_RUNTIME_MONITORING/
```

## Standard ATA Chapter Structure

**Every ATA chapter** in the OPT-IN Framework follows this mandatory structure:

```
ATA_XX-DESCRIPTION/
├── XX-00_GENERAL/                   # 14 lifecycle folders (see below)
├── XX-10_Operations/                # Ops use, turnarounds, procedures
├── XX-20_Subsystems/                # Functional subsystems (design-driven)
├── XX-30_Circularity/               # Sustainability, LCA, reuse/recycle, DPP
├── XX-40_Software/                  # SW, control logic, diagnostics, ML/NN
├── XX-50_Structures/                # Frames, housings, mounts, structural routes
├── XX-60_Storages/                  # Tanks, reservoirs, accumulators, cryo vessels
├── XX-70_Propulsion/                # Propulsive interfaces/couplings (if any)
├── XX-80_Energy/                    # Electrical/thermal energy interactions
└── XX-90_Tables_Schemas_Diagrams/   # Tables, data dicts, catalogs, SDS/training
```

### XX-00_GENERAL: 14 Lifecycle Folders

The GENERAL layer contains **14 mandatory lifecycle folders** covering the complete development cycle:

```
XX-00_GENERAL/
├── XX-00-01_Overview/               # System overview and global architecture
├── XX-00-02_Safety/                 # Safety framework and analysis
├── XX-00-03_Requirements/           # Requirements and traceability
├── XX-00-04_Design/                 # Design specifications and patterns
├── XX-00-05_Interfaces/             # Interface control documents
├── XX-00-06_Engineering/            # Analysis, models, and simulation
├── XX-00-07_V_AND_V/                # Verification and validation
├── XX-00-08_Prototyping/            # Prototype development
├── XX-00-09_Production_Planning/    # Manufacturing planning
├── XX-00-10_Certification/          # Certification evidence
├── XX-00-11_EIS_Versions_Tags/      # Configuration management
├── XX-00-12_Services/               # Maintenance and service
├── XX-00-13_Subsystems_Components/  # Component breakdown
└── XX-00-14_Ops_Std_Sustain/        # Operational standards
```

**Source**: ATA 95-00-00_GENERAL serves as the canonical template.

## Key Rules

1. **All chapters include XX-00_GENERAL with all 14 lifecycle folders.**
2. **All 9 cross-ATA buckets (10/20/30/40/50/60/70/80/90) are present in every chapter.**
   - If not applicable, include a `README.md` stating "Not Applicable" and why
   - Do **not** remove the bucket
3. **No 01–14 lifecycle duplication inside buckets.**
   - Bucket internals are design-driven and flexible
4. **Naming convention**: `XX-YY-ZZ_DESCRIPTION`
   - XX = ATA chapter (e.g., 95)
   - YY = Bucket number (10, 20, 30, 40, 50, 60, 70, 80, or 90)
   - ZZ = Sequential number within bucket (00, 01, 02, etc.)

## CI Validation

The repository includes automated validation to enforce this structure:

- **Creation script**: `tools/ci/create_optin_structure.py`
- **Validation script**: `tools/ci/optin_structure_validator.py`
- **CI Workflow**: `.github/workflows/optin-structure-check.yml`

### Usage

```bash
# Create the complete structure
python tools/ci/create_optin_structure.py

# Validate structure compliance
python tools/ci/optin_structure_validator.py --check

# Validate specific chapter
python tools/ci/optin_structure_validator.py --check --chapter 95
```

## Benefits

1. **Consistency**: Same structure across all ATA chapters
2. **Traceability**: Clear lifecycle stages and cross-cutting concerns
3. **Flexibility**: Design-driven internal structure within buckets
4. **Certification-Ready**: Built-in compliance with regulatory expectations
5. **CI Enforcement**: Automated validation ensures conformance
6. **Industry Standard**: Aligned with ATA iSpec 2200, EASA CS-25, FAA 14 CFR Part 25

## Navigation

### For Engineers
1. Navigate to the relevant axis (O, P, T, I, or N)
2. Find your ATA chapter
3. Use XX-00_GENERAL for lifecycle documentation
4. Use cross-ATA buckets for cross-cutting concerns

### For Program Managers
1. Use XX-00-01_Overview for status tracking
2. Monitor progress across all 14 lifecycle folders
3. Review XX-00-10_Certification for compliance status
4. Track interfaces across subsystems

### For Certification Authorities
1. Complete audit trail in each ATA chapter
2. Requirements traceability in XX-00-03_Requirements
3. V&V evidence in XX-00-07_V_AND_V
4. Certification packages in XX-00-10_Certification

## Compliance

This framework ensures compliance with:
- **EASA CS-25**: Certification Specifications for Large Aeroplanes
- **FAA 14 CFR Part 25**: Airworthiness Standards
- **ATA iSpec 2200**: Documentation Standards
- **S1000D**: Technical Publications
- **ISO 15926**: Industrial Data Standards

## Statistics

- **Total ATA Chapters**: 79
- **Main Axes**: 5 (O-P-T-I-N)
- **T-Technology Subsystems**: 15 (A-M-E-D-E-O-P-E-L-I-C-C-I-A₂)
- **Lifecycle Folders per Chapter**: 14
- **Cross-ATA Buckets per Chapter**: 9
- **Total Directories**: ~2,000
- **Total README Files**: ~1,900

## Documentation

For complete specification, see:
- [OPT-IN_FRAMEWORK_STANDARD.md](../OPT-IN_FRAMEWORK_STANDARD.md)
- [AMPEL360_DOCUMENTATION_STANDARD.md](../AMPEL360_DOCUMENTATION_STANDARD.md)

## Document Control

- **Version**: 1.1
- **Status**: Active
- **Owner**: AMPEL360 Documentation WG
- **Standard**: OPT-IN Framework v1.1
- **Last Updated**: 2025-11-13

---

**OPT-IN Framework** © 2025 AMPEL360 Program  
*Amedeo Pelliccia's Development and Documentation Methodology*
