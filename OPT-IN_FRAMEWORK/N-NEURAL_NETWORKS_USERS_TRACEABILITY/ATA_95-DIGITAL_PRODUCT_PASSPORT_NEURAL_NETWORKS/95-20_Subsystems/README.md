# 95-20_Subsystems — Neural Network Fleet of Subsystems Mapped to ATA

## Purpose

This directory contains the **"NN fleet of subsystems"** — a comprehensive mapping of Neural Network-based subsystems to their corresponding ATA chapters. Each subsystem represents how AI/ML capabilities enhance specific aircraft systems while maintaining full traceability to lifecycle phases and cross-ATA dependencies.

## Overview

The 95-20_Subsystems structure provides:

1. **Core Platform Infrastructure** (95-20-01, 95-20-02): Foundation for all NN operations
2. **ATA-Specific NN Subsystems** (95-20-21 through 95-20-80): Neural networks serving specific aircraft systems
3. **Cross-ATA Integration**: Clear traceability between NN subsystems and their parent ATA chapters
4. **Digital Product Passport Integration**: Blockchain-based provenance for all NN models

## Architecture

### Core Platform Subsystems

- **95-20-01_NN_Core_Platform**: Central NN infrastructure (model registry, inference runtime, monitoring)
- **95-20-02_NN_DPP_Blockchain**: Digital Product Passport with blockchain-based provenance chain

### ATA-Mapped NN Subsystems

Each subsystem follows the pattern `95-20-XX_NN_[System]` where XX mirrors the ATA chapter it serves:

| Subsystem | ATA | Purpose | Key Capabilities |
|-----------|-----|---------|------------------|
| 95-20-21 | ATA 21 | Environmental Control | Cabin temp prediction, air quality, HVAC optimization |
| 95-20-27 | ATA 27 | Flight Controls | Aerodynamic prediction, gust alleviation, CFD surrogate |
| 95-20-28 | ATA 28 | Fuel System (H₂) | Level prediction, boiloff estimation, fuel optimization |
| 95-20-31 | ATA 31 | Recording Systems | Anomaly detection, event classification, data compression |
| 95-20-42 | ATA 42 | IMA/Avionics | Neural partition manager, AFDX traffic prediction |
| 95-20-45 | ATA 45 | Maintenance | Predictive maintenance, RUL estimation, fault diagnosis |
| 95-20-49 | ATA 49 | APU | Performance prediction, health monitoring |
| 95-20-53 | ATA 53 | Structures (Fuselage) | Structural health (GNN), load distribution, fatigue |
| 95-20-57 | ATA 57 | Wings | Flutter prediction (LSTM), ice detection, load alleviation |
| 95-20-70 | ATA 70-79 | Propulsion | Engine performance, fuel cell optimization, thrust prediction |
| 95-20-80 | ATA 80 | Energy/Electrical | Power load prediction, battery SOH, energy management |

## Naming Conventions

### Documents
- `95-20-SS-XXX_Description.md` where:
  - `95` = ATA chapter
  - `20` = Subsystems bucket
  - `SS` = Subsystem code (01, 02, 21, 27, etc.)
  - `XXX` = Sequential number (001-999)

### Assets
- `95-20-SS-A-XXX_Description.ext` where:
  - `A` = Asset indicator
  - Extension: `.drawio`, `.svg`, `.json`, `.yaml`, `.sol`, etc.

### Model Cards
- `95-20-SS-A-2XX_ModelName_vX.Y.yaml` where:
  - `2XX` = Model card number range (200-299)
  - Version follows semantic versioning (vX.Y)

## Directory Structure

```
95-20_Subsystems/
├── README.md                                    # This file
├── 95-20-00-001_Subsystems_Overview.md         # High-level architecture
├── 95-20-00-002_Subsystems_Integration_Map.md  # Integration matrix
├── 95-20-00-003_Cross_ATA_Dependencies.csv     # Dependency tracking
│
├── 00_META/                                     # Metadata and governance
│   ├── 95-20-00-004_Subsystems_Taxonomy.md
│   ├── 95-20-00-005_Subsystems_Traceability_Matrix.csv
│   ├── 95-20-00-006_Subsystem_Registry.json
│   └── 95-20-00-007_CAOS_Subsystems_Hooks.md
│
├── 95-20-01_NN_Core_Platform/                  # Core infrastructure
├── 95-20-02_NN_DPP_Blockchain/                 # Digital passport
├── 95-20-21_NN_ECS/                            # Environmental Control
├── 95-20-27_NN_Flight_Controls/                # Flight Controls
├── 95-20-28_NN_Fuel_System/                    # H₂ Fuel
├── 95-20-31_NN_Recording_Systems/              # Recording
├── 95-20-42_NN_IMA_Integration/                # IMA/Avionics
├── 95-20-45_NN_Maintenance/                    # Maintenance
├── 95-20-49_NN_APU/                            # APU
├── 95-20-53_NN_Structures/                     # Structures
├── 95-20-57_NN_Wing_Systems/                   # Wings
├── 95-20-70_NN_Propulsion/                     # Propulsion
└── 95-20-80_NN_Energy_Systems/                 # Energy
```

## Traceability

### To 95-00-13_Subsystems_Components
Each NN subsystem maintains bidirectional traceability to:
- Component registry in 95-00-13
- Lifecycle phases (01-14 folders)
- Parent ATA chapters

### To 95-10_Operations
NN subsystems surface operational capabilities through:
- Operational procedures
- Performance monitoring
- Runtime orchestration

### To 95-00-11_EIS_Versions_Tags
Version control linkage:
- Model versions tied to EIS releases
- Certification baselines
- Configuration management

## CAOS/MCP Discovery Rules

### How CAOS Discovers Subsystems

1. **Entry Point**: CAOS starts at `95-20_Subsystems/00_META/95-20-00-007_CAOS_Subsystems_Hooks.md`
2. **Registry Scan**: Reads `95-20-00-006_Subsystem_Registry.json` for active subsystems
3. **Capability Discovery**: Each subsystem's README.md declares:
   - Model endpoints
   - API interfaces
   - Monitoring hooks
   - Integration requirements
4. **Dependency Resolution**: Uses `95-20-00-003_Cross_ATA_Dependencies.csv` to understand relationships
5. **Runtime Registration**: Each subsystem registers with CAOS core platform (95-20-01)

### MCP Server Integration

MCP (Model Context Protocol) servers can crawl this tree via:

```json
{
  "discovery_path": "95-20_Subsystems/",
  "registry_file": "00_META/95-20-00-006_Subsystem_Registry.json",
  "hooks_file": "00_META/95-20-00-007_CAOS_Subsystems_Hooks.md",
  "subsystem_pattern": "95-20-{code}_NN_{name}/"
}
```

## Internal Organization

Each subsystem folder follows this design-driven pattern:

```
95-20-XX_NN_System/
├── README.md                          # Subsystem overview
├── 95-20-XX-001_Overview.md          # Architecture
├── 95-20-XX-002_Component1.md        # Individual components
├── 95-20-XX-003_Component2.md
├── 95-20-XX-00Y_Integration.md       # Integration with ATA XX
└── ASSETS/
    ├── 95-20-XX-A-001_Architecture.drawio
    ├── 95-20-XX-A-002_Diagram.svg
    ├── 95-20-XX-A-003_Config.json
    └── Model_Cards/
        ├── 95-20-XX-A-201_Model1_vX.Y.yaml
        └── 95-20-XX-A-202_Model2_vX.Y.yaml
```

## Status

- **Bucket**: 20_Subsystems
- **Status**: Active — Automation-Ready Structure
- **Applicability**: ATA 95 (Neural Networks & Digital Product Passport)
- **Standard**: OPT-IN Framework v1.4
- **Last Updated**: 2025-11-17

## References

- [95-00-13_Subsystems_Components](../95-00_GENERAL/95-00-13_Subsystems_Components/) — Component registry
- [95-10_Operations](../95-10_Operations/) — Operational procedures
- [95-00-11_EIS_Versions_Tags](../95-00_GENERAL/95-00-11_EIS_Versions_Tags/) — Version control
- [OPT-IN_FRAMEWORK_STANDARD](../../../../../OPT-IN_FRAMEWORK_STANDARD.md) — Framework specification

## Document Control

- **Standard**: OPT-IN Framework v1.4 + AMPEL360_DOCUMENTATION_STANDARD
- **Owner**: AMPEL360 Neural Networks WG
- **Classification**: Technical Reference
- **Change Control**: CCB approval required for structural changes

---

**Note**: This structure is OPT-IN compliant and automation-ready. All naming follows the established `95-20-XX-YYY` convention to enable programmatic discovery and integration.
