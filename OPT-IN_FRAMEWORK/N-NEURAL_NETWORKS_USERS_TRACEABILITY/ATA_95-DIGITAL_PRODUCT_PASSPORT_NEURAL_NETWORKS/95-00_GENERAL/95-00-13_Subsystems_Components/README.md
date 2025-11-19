# 95-00-13_Subsystems_Components

## Purpose

This folder contains comprehensive documentation for the decomposition of the AMPEL360 BWB H₂ Hy-E aircraft system into subsystems and components, including hardware, software, data, models, safety monitors, and integration elements.

## Scope

This folder is part of the **95-00_GENERAL** layer, which provides governance and lifecycle management for ATA Chapter 95.

## Contents

### Strategy and Principles
- **[95-00-13-00-001_Subsystems_Components_Strategy](95-00-13-00-001_Subsystems_Components_Strategy.md).md**: Overall strategy for system decomposition
- **[95-00-13-00-002_Decomposition_Principles_and_Rules](95-00-13-00-002_Decomposition_Principles_and_Rules.md).md**: Rules and principles for decomposition

### 00_META/ - Taxonomy and Traceability
- **[95-00-13-00-003_Subsystems_Taxonomy](95-00-13-00-003_Subsystems_Taxonomy.md).md**: Hierarchical classification system
- **[95-00-13-00-004_Components_Taxonomy](95-00-13-00-004_Components_Taxonomy.md).md**: Component classification framework
- **[95-00-13-00-005_Subsys_Comp_Traceability_Matrix](00_META/95-00-13-00-005_Subsys_Comp_Traceability_Matrix.csv)**: Traceability matrix
- **[95-00-13-00-006_Subsys_Registry](00_META/95-00-13-00-006_Subsys_Registry.json)**: Component registry in JSON format
- **[95-00-13-00-007_CAOS_Subsystems_Hooks](00_META/95-00-13-00-007_CAOS_Subsystems_Hooks.md)**: CAOS AI integration points

### 01_FUNCTIONAL_SUBSYSTEMS/
Mission-capability based functional decomposition:
- Overview and decomposition rules
- Functional subsystems list (15 primary subsystems)
- Operational modes and contexts
- Requirements traceability
- ASSETS: Block diagrams, allocation tables, mode matrices

### 02_HW_COMPONENTS/
Physical hardware components and interfaces:
- Compute boards and modules (flight computers, IMA, AI accelerators)
- Sensors and actuators (IMUs, GNSS, servos)
- Power and thermal management interfaces
- ATA chapter mapping
- ASSETS: Component lists, architecture diagrams, I/O mapping

### 03_SW_COMPONENTS/
Software architecture and components:
- Services and microservices
- Libraries and runtime modules
- Inter-component interfaces
- Engineering mapping
- ASSETS: Component lists, architecture diagrams, API index

### 04_DATA_SUBSYSTEMS/
Data management and storage:
- Data stores and lakes
- Feature stores and caches
- Logs, metrics, and telemetry stores
- Interface mapping
- ASSETS: Block diagrams, catalogs, retention policies

### 05_MODEL_COMPONENTS/
AI/ML model components:
- Submodels and heads
- Ensembles and composite models
- Feature extractors and embeddings
- Model engineering links
- ASSETS: Taxonomy, index, configuration templates

### 06_SAFETY_MONITORS_AND_FALLBACKS/
Safety-critical monitoring and fallback systems:
- Runtime checkers and guards
- Fallback control paths
- Safety monitor interfaces
- Safety and V&V links
- ASSETS: Block diagrams, fallback maps, catalogs

### 07_DPP_BLOCKS_AND_REGISTERS/
Digital Product Passport integration:
- On-chain components and anchors
- Off-chain components and manifests
- DPP records per subsystem
- Certification links
- ASSETS: DPP structure, registry, subsystem mapping

### 08_INTEGRATION_KITS_AND_ADAPTERS/
Integration infrastructure:
- ATA chapter adapters (02, 28, 31, 42, 45)
- Test harnesses and shim modules
- Development vs production kits
- Interface mapping
- ASSETS: Block diagrams, adapter catalogs, templates

### 09_TEST_RIG_SUBSYSTEMS/
Testing infrastructure:
- Lab racks and simulators
- HIL/SIL rig subsystems
- V&V and prototyping mapping
- Configuration and reuse principles
- ASSETS: Architecture diagrams, subsystem lists, configurations

### 10_FIELD_REPLACEABLE_UNITS_FRU/
Field-replaceable unit management:
- FRU concept for NN and DPP
- FRU list and classification
- Replacement rules and constraints
- Spare parts management
- ASSETS: FRU catalog, flowcharts, maintenance mapping

### 11_CONFIGURATION_SETS/
Configuration management:
- Fleet and operator configurations
- Simulation, lab, and production configs
- Approval and control processes
- EIS version links
- ASSETS: Config tables, templates, workflows

### 12_DIAGNOSTICS_AND_HEALTH_COMPONENTS/
Health monitoring and diagnostics:
- Health indicators and probes
- Self-test and BIST components
- ATA 31 recording integration
- Maintenance and V&V mapping
- ASSETS: Diagrams, health indicators, test sequences

### 13_SECURITY_AND_PRIVACY_COMPONENTS/
Security and privacy infrastructure:
- Crypto engines and key stores
- Access control and authentication
- Privacy-preserving components
- Security interface links
- ASSETS: Security diagrams, key management, catalogs

### 14_SUBSYSTEMS_REQUIREMENTS_VV_MAP/
Traceability and verification:
- Requirements mapping strategy
- Subsystems to requirements map
- V&V cases mapping
- Certification evidence mapping
- Subsystem criticality levels
- ASSETS: Traceability matrices, evidence tables

## Structure Summary

```
95-00-13_Subsystems_Components/
├── README.md (this file)
├── [95-00-13-00-001_Subsystems_Components_Strategy](95-00-13-00-001_Subsystems_Components_Strategy.md).md
├── [95-00-13-00-002_Decomposition_Principles_and_Rules](95-00-13-00-002_Decomposition_Principles_and_Rules.md).md
│
├── 00_META/ (7 files)
├── 01_FUNCTIONAL_SUBSYSTEMS/ (5 docs + 4 assets)
├── 02_HW_COMPONENTS/ (5 docs + 4 assets)
├── 03_SW_COMPONENTS/ (5 docs + 4 assets)
├── 04_DATA_SUBSYSTEMS/ (5 docs + 4 assets)
├── 05_MODEL_COMPONENTS/ (5 docs + 4 assets)
├── 06_SAFETY_MONITORS_AND_FALLBACKS/ (5 docs + 4 assets)
├── 07_DPP_BLOCKS_AND_REGISTERS/ (5 docs + 4 assets)
├── 08_INTEGRATION_KITS_AND_ADAPTERS/ (5 docs + 4 assets)
├── 09_TEST_RIG_SUBSYSTEMS/ (5 docs + 4 assets)
├── 10_FIELD_REPLACEABLE_UNITS_FRU/ (5 docs + 4 assets)
├── 11_CONFIGURATION_SETS/ (5 docs + 4 assets)
├── 12_DIAGNOSTICS_AND_HEALTH_COMPONENTS/ (5 docs + 4 assets)
├── 13_SECURITY_AND_PRIVACY_COMPONENTS/ (5 docs + 4 assets)
└── 14_SUBSYSTEMS_REQUIREMENTS_VV_MAP/ (5 docs + 4 assets)

Total: 134 files across 15 directories
```

## Key Features

1. **Comprehensive Coverage**: Complete system decomposition across all aspects
2. **Multi-Dimensional Organization**: Functional, hardware, software, data, and model views
3. **Traceability**: Full traceability to requirements, V&V, and certification
4. **CAOS Integration**: AI-powered operations hooks and interfaces
5. **DPP Support**: Digital Product Passport integration at component level
6. **Safety-Focused**: Dedicated safety monitors and fallback systems
7. **Test Infrastructure**: Complete test rig and integration kit documentation
8. **Lifecycle Support**: FRU management and configuration control

## Usage Guidelines

1. **Start with Strategy**: Read [Subsystems Components Strategy](95-00-13-00-001_Subsystems_Components_Strategy.md) and [Decomposition Principles and Rules](95-00-13-00-002_Decomposition_Principles_and_Rules.md) first
2. **Understand Taxonomy**: Review 00_META/ for classification systems
3. **Navigate by Domain**: Use appropriate subfolder for your domain (HW, SW, Data, etc.)
4. **Follow Traceability**: Use 14_SUBSYSTEMS_REQUIREMENTS_VV_MAP for verification
5. **Reference ASSETS**: Each subfolder contains supporting diagrams and tables

## Status

- **Phase**: Subsystems Components
- **Lifecycle Position**: 13 of 14
- **Status**: Active - Complete structure implemented
- **Last Updated**: 2025-11-17
- **Files**: 134 files in 15 directories

## Related Folders

Part of the canonical 14-folder lifecycle:
1. Overview → 2. Safety → 3. Requirements → 4. Design → 5. Interfaces → 6. Engineering → 7. V&V → 8. Prototyping → 9. Production Planning → 10. Certification → 11. EIS/Versions/Tags → 12. Services → **13. Subsystems/Components** → 14. Ops/Std/Sustain

## Document Control

- **Standard**: OPT-IN Framework v1.1 (ATA 95 canonical template)
- **Owner**: AMPEL360 Documentation WG
- **Change Control**: Follow standard change management process
- **Review Cycle**: Quarterly or as needed for major changes
