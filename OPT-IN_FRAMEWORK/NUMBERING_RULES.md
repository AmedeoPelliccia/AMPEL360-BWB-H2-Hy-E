# AMPEL360 ATA Numbering System Rules
## Law of Origin - Systematic Code Assignment

**Version:** 1.0.0  
**Date:** 2025-11-12  
**Status:** Active

---

## 1. Introduction

This document defines the **Law of Origin** numbering system for AMPEL360 framework. This rule establishes how ATA codes are assigned based on the functional origin and nature of systems, structures, engines, and meta-information.

The numbering system applies to:
- Classic ATA chapters (20, 50, 70, 80, 90)
- Derived domain codes (e.g., 03-20-xx, 03-50-xx, 03-80-xx, 03-90-xx in I-Infrastructures)

---

## 2. Core Numbering Rules

### 2.1 Rule 1: Systems → 20-xx Block

**Origin:** All **functional systems** use **20** as their root block.

**Definition:** Any operational system, handling procedure, fleet maintenance program, or service system.

**Examples:**
- **ATA 20:** Standard Practices - Airframe
- **03-20-00:** General Handling (GSE)
- **03-20-01:** Storage & Shipping
- **03-20-10:** Fleet Maintenance Program
- **03-20-11:** LH₂ Cryo Refueler Maintenance

**Application:** Use 20-xx when the element is primarily a **system** that performs operational or maintenance functions.

---

### 2.2 Rule 2: Structures → 50-xx Block

**Origin:** All **physical structures** use **50** as their root block.

**Definition:** Any airframe component, structural support, physical platform, dock, or structural GSE.

**Examples:**
- **ATA 50:** Cargo and Accessory Compartments
- **ATA 51:** Standard Practices and Structures - General
- **ATA 52:** Doors
- **ATA 53:** Fuselage
- **ATA 57:** Wings
- **03-50-00:** General Structural GSE
- **03-50-01:** LH₂ Support Frames
- **03-50-02:** Docking Platforms
- **03-50-03:** Maintenance Stands

**Application:** Use 50-xx when the element is primarily a **structure**, frame, support, or physical component.

---

### 2.3 Rule 3: Engines / Propulsion / Energy → 70-xx / 80-xx Block

**Origin:** All **propulsion and energy systems** use **70-xx** or **80-xx** as their root blocks.

**Definition:**
- **70-xx:** Powerplant, main engines, H₂ propulsion systems
- **80-xx:** Auxiliary power, ground energy, GPUs, electrical conversion, starting systems

**Examples - 70-xx (Main Propulsion):**
- **ATA 70:** Standard Practices - Engine
- **ATA 71:** Power Plant
- **ATA 72:** Engine
- **ATA 73:** Engine Fuel and Control
- **ATA 74:** Ignition
- **ATA 75:** Air
- **ATA 76:** Engine Controls
- **ATA 78:** Exhaust
- **ATA 79:** Oil

**Examples - 80-xx (Auxiliary Energy):**
- **ATA 80:** Starting
- **03-80-00:** General Energy GSE
- **03-80-01:** LH₂ Cryogenic Refueler
- **03-80-02:** HV Ground Power Unit
- **03-80-03:** Battery Charging Station

**Application:** 
- Use **70-xx** for on-board propulsion and powerplant systems
- Use **80-xx** for auxiliary power, ground energy equipment, and starting systems

---

### 2.4 Rule 4: Schemas / Meta / Catalogues → 90-xx Block

**Origin:** All **meta-information, schemas, catalogues, and documentation** use **90** as their root block.

**Definition:** Any schema definition, catalogue (IPL/IPC), in-service registry, training material, safety data sheet (SDS), or governance documentation.

**Examples:**
- **ATA 90:** (Reserved for infrastructure interface standards in some taxonomies)
- **ATA 91:** Charts - Flight Operations
- **ATA 92:** Model-Based Maintenance
- **ATA 93:** Onboard Data Load
- **ATA 95:** Digital Product Passport and Traceability
- **03-90-00:** In-Service Registry
- **03-90-01:** Training Materials
- **03-90-02:** Safety Data Sheets (SDS)
- **03-90-10:** Fleet Spares Program (IPL)
- **03-90-11:** LH₂ Cryo Refueler Parts Catalogue

**Application:** Use 90-xx when the element is primarily **documentation, metadata, training content, or catalogue information**.

---

## 3. Application to ATA 03 - Support Information GSE

The **ATA 03** chapter in I-Infrastructures uses this Law of Origin to organize Ground Support Equipment (GSE) by function:

### 3.1 Structure Overview

```
ATA_03-SUPPORT_INFORMATION_GSE/
├── 03-00-00_GENERAL
│   └── [14 lifecycle folders]
│
├── 03-20_SYSTEMS_SUPPORT (Origin: 20 = Systems)
│   ├── 03-20-00_GENERAL_HANDLING
│   ├── 03-20-01_STORAGE_SHIPPING
│   ├── 03-20-10_FLEET_MAINTENANCE_PROGRAM
│   └── 03-20-11_LH2_CRYO_REFUELER_MAINT
│
├── 03-50_STRUCTURAL_GSE (Origin: 50 = Structures)
│   ├── 03-50-00_GENERAL_STRUCTURAL_GSE
│   └── 03-50-01_LH2_SUPPORT_FRAMES
│
├── 03-80_ENERGY_GSE (Origin: 80 = Engines/Energy)
│   ├── 03-80-00_GENERAL_ENERGY_GSE
│   ├── 03-80-01_LH2_CRYOGENIC_REFUELER
│   └── 03-80-02_HV_GROUND_POWER_UNIT
│
└── 03-90_SCHEMAS_AND_REGISTRIES (Origin: 90 = Schemas/Meta)
    ├── 03-90-00_IN_SERVICE_REGISTRY
    ├── 03-90-01_TRAINING_MATERIALS
    ├── 03-90-02_SAFETY_DATA_SHEETS
    ├── 03-90-10_FLEET_SPARES_PROGRAM
    └── 03-90-11_LH2_CRYO_REFUELER_PARTS
```

### 3.2 Mapping Old to New Codes

| Old Code | Old Name | New Code | New Name | Reason |
|----------|----------|----------|----------|--------|
| 03-10-xx | (Undefined) | 03-20-xx | Systems Support | Functional systems |
| 03-40-xx | Fleet Spares | 03-90-10 | Fleet Spares Program | Catalogue/IPL = Meta |
| 03-40-01 | Refueler Parts | 03-90-11 | LH₂ Refueler Parts | Catalogue/IPC = Meta |

---

## 4. Decision Tree for Code Assignment

When assigning a new ATA code, follow this decision tree:

```
START: What is the primary nature of this element?

├─ Is it a FUNCTIONAL SYSTEM (operations, handling, maintenance)?
│  └─ YES → Use 20-xx block
│
├─ Is it a PHYSICAL STRUCTURE (frame, support, dock, stand)?
│  └─ YES → Use 50-xx block
│
├─ Is it ENGINE/PROPULSION/ENERGY related?
│  ├─ Main propulsion or powerplant? → Use 70-xx block
│  └─ Auxiliary power or ground energy? → Use 80-xx block
│
└─ Is it META-INFORMATION (schema, catalogue, training, registry)?
   └─ YES → Use 90-xx block
```

---

## 5. Examples by Domain

### 5.1 On-Board Aircraft Systems (T-Technology)

| Code | Name | Origin Rule |
|------|------|-------------|
| ATA 20 | Standard Practices - Airframe | 20 = Systems |
| ATA 50-57 | Airframe Structures | 50 = Structures |
| ATA 70-79 | Propulsion Systems | 70 = Engines |
| ATA 80 | Starting Systems | 80 = Auxiliary Energy |
| ATA 91-95 | Information Systems | 90 = Meta/Schemas |

### 5.2 Infrastructure GSE (I-Infrastructures, ATA 03)

| Code | Name | Origin Rule |
|------|------|-------------|
| 03-20-xx | Systems Support (handling, maintenance) | 20 = Systems |
| 03-50-xx | Structural GSE (frames, stands) | 50 = Structures |
| 03-80-xx | Energy GSE (refuelers, power units) | 80 = Auxiliary Energy |
| 03-90-xx | Registries, Training, Catalogues | 90 = Meta/Schemas |

---

## 6. Agent Implementation Rules

### 6.1 For Code Generation Agents

When generating a new ATA code:

1. **Identify the functional nature** of the element (System, Structure, Engine/Energy, or Meta)
2. **Apply the Law of Origin** rule to select the root block (20, 50, 70/80, or 90)
3. **Use consistent sub-codes** within that block
4. **Document the reasoning** in the element's metadata

### 6.2 For Code Validation Agents

When validating an existing code:

1. **Check the element's primary function** against its assigned code block
2. **Flag misalignments** where:
   - A functional system is not in 20-xx
   - A structure is not in 50-xx
   - An energy system is not in 70/80-xx
   - Meta-information is not in 90-xx
3. **Suggest corrections** based on the Law of Origin

### 6.3 For Migration Agents

When migrating legacy codes:

1. **Analyze each element's** true functional nature
2. **Map to the correct block** using the Law of Origin
3. **Preserve traceability** by documenting old → new mappings
4. **Update all references** in related documents

---

## 7. Governance

### 7.1 Authority

This numbering system is maintained by the **AMPEL360 Program Office** and applies to all OPT-IN Framework documentation.

### 7.2 Change Control

Changes to the Law of Origin require:
1. Technical review by domain experts
2. Impact analysis on existing codes
3. Approval by Program Office
4. Version update of this document

### 7.3 Exceptions

Exceptions to the Law of Origin may be granted when:
- An element has dual nature (e.g., structural system with equal emphasis)
- Legacy compatibility requires preservation of specific codes
- Regulatory requirements mandate specific numbering

All exceptions must be documented in the element's 14_META_GOVERNANCE folder.

---

## 8. References

- **ATA iSpec 2200** - Air Transport Association Specification for electronic data interchange
- **S1000D** - International specification for technical publications
- **AMPEL360 OPT-IN Framework** - 14-folder lifecycle skeleton methodology
- **Problem Statement** - "LOS SISTEMAS salen del 20, estructuras del 50, engines del 70 y 80, schemas y demás del 90"

---

## 9. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-11-12 | AMPEL360 Program Office | Initial release - Law of Origin established |

---

**© 2024-2025 AMPEL360 Project | All Rights Reserved**
