# ATA 03 Support Information GSE - Numbering Convention Guide

**Version:** 1.0  
**Date:** 2025-11-12  
**Related:** AMPEL360_DOCUMENTATION_STANDARD.md § ATA Code Numbering Convention

---

## Overview

This guide demonstrates the application of the **ATA Code Numbering Convention (Law of Origin)** to **ATA_03-SUPPORT_INFORMATION_GSE** within the Infrastructure axis.

The numbering blocks (20, 50, 70/80, 90) serve as the foundation for organizing all GSE systems, structures, energy equipment, and documentation.

---

## Recommended Structure for ATA 03

```
/I-INFRASTRUCTURES/ATA_03-SUPPORT_INFORMATION_GSE/
│
├── 03-00-00_GENERAL/                    # Mandatory general framework
│   ├── 03-00-01_OVERVIEW/
│   ├── 03-00-02_SAFETY/
│   ├── 03-00-03_REQUIREMENTS/
│   ├── 03-00-04_DESIGN/
│   ├── 03-00-05_INTERFACES/
│   ├── 03-00-06_ENGINEERING/
│   ├── 03-00-07_V_AND_V/
│   ├── 03-00-08_PROTOTYPING/
│   ├── 03-00-09_PRODUCTION_PLANNING/
│   ├── 03-00-10_CERTIFICATION/
│   ├── 03-00-11_OPERATIONS_MAINTENANCE/
│   ├── 03-00-12_ASSETS_MANAGEMENT/
│   ├── 03-00-13_SUBSYSTEMS_COMPONENTS/
│   └── 03-00-14_META_GOVERNANCE/
│
├── 03-20_SYSTEMS_SUPPORT/               # Block 20: Functional/Operational Systems
│   ├── 03-20-00_GENERAL_HANDLING/      # General handling systems
│   │   ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
│   ├── 03-20-01_STORAGE_SHIPPING/      # Storage and shipping systems
│   │   ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
│   ├── 03-20-10_FLEET_MAINTENANCE_PROGRAM/  # Fleet-level maintenance system
│   │   ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
│   └── 03-20-11_LH2_CRYO_REFUELER_MAINT/    # LH₂ refueler maintenance system
│       ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
│
├── 03-50_STRUCTURAL_GSE/                # Block 50: Physical Structures
│   ├── 03-50-00_GENERAL_STRUCTURAL_GSE/ # General structural equipment
│   │   ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
│   ├── 03-50-01_LH2_SUPPORT_FRAMES/    # LH₂ support frames and stands
│   │   ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
│   └── 03-50-02_DOCKING_STRUCTURES/    # Aircraft docking structures
│       ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
│
├── 03-80_ENERGY_GSE/                    # Block 70/80: Engines/Propulsion/Energy
│   ├── 03-80-00_GENERAL_ENERGY_GSE/    # General energy systems
│   │   ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
│   ├── 03-80-01_LH2_CRYOGENIC_REFUELER/     # LH₂ refueling system
│   │   ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
│   ├── 03-80-02_HV_GROUND_POWER_UNIT/       # High-voltage ground power
│   │   ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
│   └── 03-80-03_H2_FUEL_CELL_CHARGER/       # H₂ fuel cell charging system
│       ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
│
└── 03-90_SCHEMAS_AND_REGISTRIES/       # Block 90: Schemas/Catalogs/Training
    ├── 03-90-00_IN_SERVICE_REGISTRY/   # In-service equipment registry
    │   ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
    ├── 03-90-01_TRAINING_MATERIALS/    # GSE training programs
    │   ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
    ├── 03-90-02_SAFETY_DATA_SHEETS/    # SDS for hazardous materials
    │   ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
    ├── 03-90-10_FLEET_SPARES_PROGRAM/  # Spares catalog and program
    │   ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
    └── 03-90-11_LH2_CRYO_REFUELER_PARTS/    # LH₂ refueler parts catalog (IPL/IPC)
        ├── 01_OVERVIEW/ … 14_META_GOVERNANCE/
```

---

## Numbering Logic Explained

### 03-20-xx: Systems Support
**Origin Block:** 20 (Systems/Operational)

All **functional systems** and **operational processes** for GSE:
- **03-20-00**: General handling procedures and systems
- **03-20-01**: Storage and shipping operations
- **03-20-10**: Fleet-wide maintenance programs
- **03-20-11**: LH₂ refueler maintenance system

**Key Principle:** If it's a **process, program, or operational system**, it belongs in 03-20-xx.

---

### 03-50-xx: Structural GSE
**Origin Block:** 50 (Structures/Physical)

All **physical structures** and **structural equipment**:
- **03-50-00**: General structural GSE (frames, stands, fixtures)
- **03-50-01**: LH₂ tank support frames
- **03-50-02**: Aircraft docking structures

**Key Principle:** If it's a **physical structure you can touch**, it belongs in 03-50-xx.

---

### 03-80-xx: Energy GSE
**Origin Block:** 70/80 (Engines/Energy)

All **energy systems**, **power equipment**, and **fuel handling**:
- **03-80-00**: General energy GSE
- **03-80-01**: LH₂ cryogenic refueler (the energy system aspect)
- **03-80-02**: High-voltage ground power unit (GPU)
- **03-80-03**: H₂ fuel cell chargers

**Key Principle:** If it **generates, stores, converts, or delivers energy/fuel**, it belongs in 03-80-xx.

---

### 03-90-xx: Schemas and Registries
**Origin Block:** 90 (Schemas/Meta/Catalogs)

All **documentation**, **catalogs**, **training**, **registries**, and **schemas**:
- **03-90-00**: In-service registry (tracking GSE assets)
- **03-90-01**: Training materials and programs
- **03-90-02**: Safety Data Sheets (SDS)
- **03-90-10**: Fleet spares program (catalog/planning)
- **03-90-11**: LH₂ refueler parts catalog (IPL/IPC)

**Key Principle:** If it's **documentation, training, or metadata about other systems**, it belongs in 03-90-xx.

---

## Mapping from Old to New Numbering

If codes were previously assigned without the Law of Origin, here's how to remap them:

| Old Code (Wrong) | New Code (Correct) | Reason |
|------------------|-------------------|---------|
| `03-10-00_HANDLING` | `03-20-00_GENERAL_HANDLING` | It's a system (20), not random 10 |
| `03-30-00_STORAGE` | `03-20-01_STORAGE_SHIPPING` | It's a system (20), not 30 |
| `03-40-00_FLEET_SPARES` | `03-90-10_FLEET_SPARES_PROGRAM` | It's a catalog (90), not 40 |
| `03-40-01_REFUELER_PARTS` | `03-90-11_LH2_CRYO_REFUELER_PARTS` | It's a parts catalog (90), not 40 |
| `03-60-01_POWER_UNIT` | `03-80-02_HV_GROUND_POWER_UNIT` | It's energy equipment (80), not 60 |

---

## Decision Tree for ATA 03

When creating a new code under ATA 03, follow this decision tree:

```
Is it for ATA 03 Support Information GSE?
├─ YES
│  │
│  ├─ Is it a functional system or operational process?
│  │  └─ YES → Use 03-20-xx (Systems Support)
│  │
│  ├─ Is it a physical structure or airframe-related GSE?
│  │  └─ YES → Use 03-50-xx (Structural GSE)
│  │
│  ├─ Is it related to energy, power, fuel, or propulsion?
│  │  └─ YES → Use 03-80-xx (Energy GSE)
│  │
│  ├─ Is it documentation, training, catalog, or metadata?
│  │  └─ YES → Use 03-90-xx (Schemas and Registries)
│  │
│  └─ Doesn't fit any category?
│     └─ Review with technical authority and AMPEL360_DOCUMENTATION_STANDARD.md
│
└─ NO
   └─ Use appropriate top-level ATA chapter
```

---

## Example: LH₂ Cryogenic Refueler

The LH₂ Cryogenic Refueler demonstrates how a single piece of equipment can span multiple numbering blocks:

### As an Energy System (Primary)
**Code:** `03-80-01_LH2_CRYOGENIC_REFUELER`
- Location: `/03-80_ENERGY_GSE/03-80-01_LH2_CRYOGENIC_REFUELER/`
- **Primary function:** Delivers cryogenic hydrogen fuel
- Contains: System design, safety analysis, interfaces, operations

### Supporting Structure
**Code:** `03-50-01_LH2_SUPPORT_FRAMES`
- Location: `/03-50_STRUCTURAL_GSE/03-50-01_LH2_SUPPORT_FRAMES/`
- **Function:** Physical frame/stand for the refueler
- Contains: Structural analysis, mounting specs, load calculations

### Maintenance System
**Code:** `03-20-11_LH2_CRYO_REFUELER_MAINT`
- Location: `/03-20_SYSTEMS_SUPPORT/03-20-11_LH2_CRYO_REFUELER_MAINT/`
- **Function:** Maintenance program and procedures
- Contains: Maintenance schedule, troubleshooting, servicing

### Parts Catalog
**Code:** `03-90-11_LH2_CRYO_REFUELER_PARTS`
- Location: `/03-90_SCHEMAS_AND_REGISTRIES/03-90-11_LH2_CRYO_REFUELER_PARTS/`
- **Function:** Illustrated Parts List (IPL/IPC)
- Contains: Parts catalog, BOMs, spares requirements

**Key Insight:** Each aspect of the refueler is documented in the appropriate numbering block based on its **primary function**.

---

## Cross-References and Traceability

Systems spanning multiple blocks should maintain clear cross-references:

### In 03-80-01_LH2_CRYOGENIC_REFUELER (Energy System)
```markdown
## Related Systems

- **Structure:** See [03-50-01_LH2_SUPPORT_FRAMES](../03-50-01_LH2_SUPPORT_FRAMES/)
- **Maintenance:** See [03-20-11_LH2_CRYO_REFUELER_MAINT](../03-20-11_LH2_CRYO_REFUELER_MAINT/)
- **Parts Catalog:** See [03-90-11_LH2_CRYO_REFUELER_PARTS](../03-90-11_LH2_CRYO_REFUELER_PARTS/)
```

### In 03-90-11_LH2_CRYO_REFUELER_PARTS (Parts Catalog)
```markdown
## Parent System

This parts catalog supports:
- **Primary System:** [03-80-01_LH2_CRYOGENIC_REFUELER](../03-80-01_LH2_CRYOGENIC_REFUELER/)
- **Maintenance Program:** [03-20-11_LH2_CRYO_REFUELER_MAINT](../03-20-11_LH2_CRYO_REFUELER_MAINT/)
```

---

## Implementation Checklist

When implementing this numbering convention for ATA 03:

- [ ] Review all existing codes against the Law of Origin
- [ ] Identify codes that don't follow 20/50/80/90 blocks
- [ ] Create migration plan for misaligned codes
- [ ] Update all cross-references in documentation
- [ ] Update any automated tools/scripts with new codes
- [ ] Update training materials with new structure
- [ ] Communicate changes to all stakeholders
- [ ] Update AMPEL360_DOCUMENTATION_STANDARD.md if needed

---

## Benefits of This Approach

### 1. Predictability
Engineers can **predict** where information lives:
- Need maintenance procedures? → Look in 20-xx
- Need structural specs? → Look in 50-xx
- Need energy system details? → Look in 80-xx
- Need parts catalog? → Look in 90-xx

### 2. Scalability
New GSE can be added systematically:
- New energy GSE → Add to 03-80-xx
- New structural equipment → Add to 03-50-xx
- No ambiguity about numbering

### 3. Consistency
Same logic applies across **all ATA domains**:
- ATA 03 (Infrastructures): 03-20, 03-50, 03-80, 03-90
- ATA 27 (Flight Controls): 27-20, 27-50, 27-80, 27-90
- ATA 95 (Neural Networks): 95-20, 95-50, 95-80, 95-90

### 4. Certification Readiness
Authorities can navigate documentation predictably:
- Safety documentation → Always in XX-00-02 or XX-YY-00/02_SAFETY
- Requirements → Always in XX-00-03 or XX-YY-00/03_REQUIREMENTS
- Clear separation between system types

---

## References

### Primary Documents
- [AMPEL360_DOCUMENTATION_STANDARD.md](./AMPEL360_DOCUMENTATION_STANDARD.md) - § ATA Code Numbering Convention
- [ATA_03-SUPPORT_INFORMATION_GSE](./OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_03-SUPPORT_INFORMATION_GSE/) - Implementation location
- [OPT-IN Framework](./OPT-IN_FRAMEWORK/README.md) - Framework overview

### Standards
- ATA iSpec 2200 - Information Standards for Aviation Maintenance
- S1000D - Technical Publications Specification
- ATA 100 - Specification for Manufacturers' Technical Data

---

## Document Control

| Version | Date       | Author                  | Changes                            |
|---------|------------|-------------------------|------------------------------------|
| 1.0     | 2025-11-12 | AMPEL360 Implementation | Initial ATA 03 numbering guide     |

---

**Contact:** AMPEL360 Program Documentation Team  
**Status:** Active  
**Applies to:** ATA_03-SUPPORT_INFORMATION_GSE and all Infrastructure GSE systems
