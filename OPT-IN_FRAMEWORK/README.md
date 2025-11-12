# OPT-IN_FRAMEWORK

**AMPEL360 BWB H₂ Hy-E Documentation Framework**  
**Version:** 2.0.0  
**Date:** 2025-11-12  
**Status:** Active

---

## Overview

The OPT-IN_FRAMEWORK provides the complete documentation structure for the AMPEL360 Blended-Wing-Body hydrogen-hybrid aircraft program. This framework ensures consistent, certifiable documentation across all domains following the **AMPEL360_DOCUMENTATION_STANDARD.md v1.3**.

---

## Framework Architecture

```
OPT-IN_FRAMEWORK/
├── O-ORGANIZATION/              # Governance, certification, airworthiness (4 chapters)
├── P-PROGRAM/                   # Configuration, geometry, ground handling (5 chapters)
├── T-TECHNOLOGY/                # On-board systems (67 chapters across 15 subsystems)
├── I-INFRASTRUCTURES/           # Ground support, airports, training (7 chapters)
└── N-NEURAL_NETWORKS.../        # AI/ML, Digital Product Passport (1 chapter)
```

**Total:** 84 ATA chapters organized across 5 main axes

---

## Documentation Standard

All ATA chapters follow the mandatory structure defined in **AMPEL360_DOCUMENTATION_STANDARD.md**:

### Each ATA Chapter Contains:

#### 1. XX-00-00_GENERAL (Mandatory)
14 numbered lifecycle folders defining **how** the chapter is documented:
- `XX-00-01_Overview` - Domain description and architecture
- `XX-00-02_Safety` - Safety framework and methods
- `XX-00-03_Requirements` - Requirements and traceability
- `XX-00-04_Design` - Reference architectures
- `XX-00-05_Interfaces` - Interface rules and ICDs
- `XX-00-06_Engineering` - Analysis and simulation
- `XX-00-07_V_AND_V` - Verification & validation strategy
- `XX-00-08_Prototyping` - Prototyping policy
- `XX-00-09_Production_Planning` - Industrialization
- `XX-00-10_Certification` - Certification strategy
- `XX-00-11_EIS_Versions_Tags` - EIS, versions, CM
- `XX-00-12_Services` - In-service MRO
- `XX-00-13_Subsystems_Components` - Component management
- `XX-00-14_Ops_Std_Sustain` - Standards and governance

#### 2. Subsystem Blocks (Law of Origin)
- `XX-20-00_Systems` - Functional systems
- `XX-40-00_Programming_Algorithms` - SW, logic, NN, algorithms
- `XX-50-00_Structures` - Physical structures
- `XX-70-00_Propulsion` - Propulsion/energy systems
- `XX-90-00_Tables_Schemas_Diagrams` - Tables, catalogs, schemas

---

## Law of Origin Numbering

The **Law of Origin** defines systematic code assignment:

| Block | Origin | Description |
|-------|--------|-------------|
| **20-xx** | Systems | Functional/operational systems |
| **40-xx** | Programming | SW, logic, NN, algorithms |
| **50-xx** | Structures | Physical structures, airframe |
| **70-xx** | Propulsion | Main propulsion, powerplant |
| **80-xx** | Energy | Auxiliary energy, ground power |
| **90-xx** | Schemas/Meta | Catalogs, training, documentation |

Blocks **10, 30, 60** are reserved for special cases only.

---

## Quick Navigation

### [O - ORGANIZATION](./O-ORGANIZATION/)
4 chapters covering governance, maintenance policy, airworthiness limitations, and time limits.

- [ATA 00 - GENERAL](./O-ORGANIZATION/ATA_00-GENERAL/)
- [ATA 01 - MAINTENANCE_POLICY_INFORMATION](./O-ORGANIZATION/ATA_01-MAINTENANCE_POLICY_INFORMATION/)
- [ATA 04 - AIRWORTHINESS_LIMITATIONS](./O-ORGANIZATION/ATA_04-AIRWORTHINESS_LIMITATIONS/)
- [ATA 05 - TIME_LIMITS_MAINTENANCE_CHECKS](./O-ORGANIZATION/ATA_05-TIME_LIMITS_MAINTENANCE_CHECKS/)

### [P - PROGRAM](./P-PROGRAM/)
5 chapters covering dimensions, lifting, leveling, towing, and servicing.

- [ATA 06 - DIMENSIONS_AND_AREAS](./P-PROGRAM/ATA_06-DIMENSIONS_AND_AREAS/)
- [ATA 07 - LIFTING_AND_SHORING](./P-PROGRAM/ATA_07-LIFTING_AND_SHORING/)
- [ATA 08 - LEVELING_AND_WEIGHING](./P-PROGRAM/ATA_08-LEVELING_AND_WEIGHING/)
- [ATA 09 - TOWING_AND_TAXIING](./P-PROGRAM/ATA_09-TOWING_AND_TAXIING/)
- [ATA 12 - SERVICING](./P-PROGRAM/ATA_12-SERVICING/)

### [T - TECHNOLOGY (On-Board Systems)](./T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/)
67 chapters organized into 15 subsystems following the A-M-E-D-E-O-P-E-L-L-I-C-C-I-A taxonomy.

#### Major Subsystems:
- **A-AIRFRAME** (9 chapters) - Structures, doors, wings, fuselage
- **M-MECHANICS** (6 chapters) - Flight controls, hydraulics, landing gear
- **E1-ENVIRONMENT** (5 chapters) - Air conditioning, fire protection
- **E2-ENERGY** (4 chapters) - Electrical power, APU, starting
- **P-PROPULSION** (11 chapters) - Engines, fuel cells, controls
- **C2-CIRCULAR_CRYOGENIC_SYSTEMS** (2 chapters) - H₂ fuel, CO₂ capture
- **I2-I_PLUS_D** (5 chapters) - AI integration, quantum scheduler
- And 8 additional subsystems

### [I - INFRASTRUCTURES](./I-INFRASTRUCTURES/)
7 chapters covering operations, GSE, parking, tools, simulators, and interface standards.

- [ATA 02 - OPERATIONS_INFORMATION](./I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/)
- [ATA 03 - SUPPORT_INFORMATION_GSE](./I-INFRASTRUCTURES/ATA_03-SUPPORT_INFORMATION_GSE/)
- [ATA 10 - PARKING_MOORING_STORAGE_RTS](./I-INFRASTRUCTURES/ATA_10-PARKING_MOORING_STORAGE_RTS/)
- [ATA 13 - HARDWARE_AND_GENERAL_TOOLS](./I-INFRASTRUCTURES/ATA_13-HARDWARE_AND_GENERAL_TOOLS/)
- [ATA 85 - INFRASTRUCTURE_INTERFACE_STANDARDS](./I-INFRASTRUCTURES/ATA_85-INFRASTRUCTURE_INTERFACE_STANDARDS/)
- [ATA 115 - FLIGHT_SIMULATOR_SYSTEMS](./I-INFRASTRUCTURES/ATA_115-FLIGHT_SIMULATOR_SYSTEMS/)
- [ATA 116 - FLIGHT_SIMULATOR_CUING_SYSTEM](./I-INFRASTRUCTURES/ATA_116-FLIGHT_SIMULATOR_CUING_SYSTEM/)

### [N - NEURAL NETWORKS, USERS, TRACEABILITY](./N-NEURAL_NETWORKS_USERS_TRACEABILITY/)
1 chapter for AI/ML systems, digital product passport, and traceability.

- [ATA 95 - NEURAL_NETWORKS](./N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-NEURAL_NETWORKS/)

---

## Statistics

- **Total ATA Chapters:** 84
- **Main Axes:** 5 (O-P-T-I-N)
- **T-Technology Subsystems:** 15
- **Total Directories:** ~1,660
- **README Files:** 1,176 (14 per chapter × 84 chapters)

---

## Usage Guidelines

### For New Systems

1. Identify the appropriate ATA chapter
2. Navigate to the relevant subsystem block (20/40/50/70/90)
3. Create system-specific structure as needed
4. Tag all artifacts with `ata_code` and `lifecycle_area` metadata

### For Documentation

1. Start with the `XX-00-00_GENERAL` layer to understand chapter approach
2. Reference the 14 lifecycle areas as "lenses" for coverage
3. Use metadata to maintain lifecycle traceability
4. Follow S1000D and ATA iSpec 2200 standards

### For Integration

Each ATA chapter:
- Maps to one or more OPT-IN axes (O, P, T, I, N)
- Integrates with CAOS (Computer Aided Operations & Services)
- Supports Digital Product Passport (DPP) requirements
- Enables certification readiness and traceability

---

## Compliance

This framework complies with:
- **AMPEL360_DOCUMENTATION_STANDARD.md** v1.3
- **ATA iSpec 2200** - Electronic data interchange standard
- **S1000D v6.0** - International specification for technical publications
- **DO-178C / DO-254** - Software/hardware certification
- **EASA / FAA** - Regulatory requirements

---

## Canonical Reference

The structure defined in:
```
/OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/
    ATA_95_NEURAL_NETWORKS/95-00-00_GENERAL/
```

serves as the canonical reference for all ATA chapters.

---

## Document Control

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2025-11-12 | Complete framework restructure per new standard |
| 1.0.0 | 2025-10-31 | Initial framework creation |

---

## Contact

**Responsible Team:** AMPEL360 Program Documentation Team  
**Channel:** GitHub Issues (label `documentation-standard`)

---

**This framework is mandatory for all documentation in the AMPEL360-BWB-H₂-Hy-E program.**

**© 2024-2025 AMPEL360 Project | All Rights Reserved**
