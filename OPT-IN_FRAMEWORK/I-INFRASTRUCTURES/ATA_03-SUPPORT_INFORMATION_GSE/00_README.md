# ATA 03 - Support Information GSE

**Version:** 2.0.0  
**Status:** Active  
**Last Updated:** 2025-11-12

---

## Overview

This chapter contains specifications, manuals, and certification documentation for all Ground Support Equipment (GSE) used with the AMPEL360 aircraft. The structure follows the **Law of Origin** numbering system, organizing GSE by functional category.

---

## Numbering System - Law of Origin

The ATA 03 structure is organized according to the **origin-based numbering rules**:

- **03-20-xx → SYSTEMS** - Functional systems (handling, maintenance, programs)
- **03-50-xx → STRUCTURES** - Physical structures (frames, stands, supports)
- **03-80-xx → ENERGY** - Energy and propulsion GSE (refuelers, power units)
- **03-90-xx → SCHEMAS/META** - Documentation, registries, training, catalogues

For complete numbering rules, see: [`/OPT-IN_FRAMEWORK/NUMBERING_RULES.md`](../../NUMBERING_RULES.md)

---

## Structure

### 03-00-00_GENERAL
General GSE policies, standards, and cross-cutting requirements applicable to all GSE categories.

**Contains:** 14 lifecycle folders (01_OVERVIEW through 14_META_GOVERNANCE)

---

### 03-20_SYSTEMS_SUPPORT (Origin: 20 = Systems)

Functional systems for handling, storage, maintenance, and operational support.

#### 03-20-00_GENERAL_HANDLING
General handling procedures and equipment for AMPEL360 aircraft operations.

#### 03-20-01_STORAGE_SHIPPING
Systems and procedures for aircraft storage, preservation, and shipping.

#### 03-20-10_FLEET_MAINTENANCE_PROGRAM
Fleet-wide maintenance program management, scheduling, and tracking systems.

#### 03-20-11_LH2_CRYO_REFUELER_MAINT
Maintenance procedures and systems for LH₂ cryogenic refueling equipment.

**Each subsystem contains:** 14 lifecycle folders

---

### 03-50_STRUCTURAL_GSE (Origin: 50 = Structures)

Physical structures, frames, platforms, and support equipment.

#### 03-50-00_GENERAL_STRUCTURAL_GSE
General structural GSE standards and design requirements.

#### 03-50-01_LH2_SUPPORT_FRAMES
Structural support frames and platforms for LH₂ system maintenance and servicing.

**Each subsystem contains:** 14 lifecycle folders

---

### 03-80_ENERGY_GSE (Origin: 80 = Engines/Energy)

Ground support equipment for energy supply, propulsion support, and auxiliary power.

#### 03-80-00_GENERAL_ENERGY_GSE
General standards for energy GSE, including safety protocols and interface specifications.

#### 03-80-01_LH2_CRYOGENIC_REFUELER
Liquid hydrogen cryogenic refueling system for AMPEL360 fuel cell propulsion.
- Capacity: 500 kg LH₂
- Operating temperature: 20K (-253°C)
- Pressure rating: 10 bar
- Transfer rate: 100 kg/hr

#### 03-80-02_HV_GROUND_POWER_UNIT
High-voltage ground power unit for aircraft electrical system ground testing and auxiliary power.
- Voltage: 270 VDC / 115-230 VAC
- Power rating: 120 kVA
- Compatibility: PEM fuel cell ground testing

**Each subsystem contains:** 14 lifecycle folders

---

### 03-90_SCHEMAS_AND_REGISTRIES (Origin: 90 = Schemas/Meta)

Documentation, catalogues, registries, training materials, and meta-information.

#### 03-90-00_IN_SERVICE_REGISTRY
Registry of all GSE in service, including certification status, maintenance history, and traceability.

#### 03-90-01_TRAINING_MATERIALS
Training courses, procedures, and certification requirements for GSE operators and maintainers.

#### 03-90-02_SAFETY_DATA_SHEETS
Safety Data Sheets (SDS) for all hazardous materials and substances used in GSE operations.
- LH₂ handling procedures
- Cryogenic safety protocols
- Emergency response procedures

#### 03-90-10_FLEET_SPARES_PROGRAM
Illustrated Parts List (IPL) and spare parts management program for fleet-wide GSE support.

#### 03-90-11_LH2_CRYO_REFUELER_PARTS
Illustrated Parts Catalogue (IPC) specifically for LH₂ cryogenic refueler components and assemblies.

**Each subsystem contains:** 14 lifecycle folders

---

## 14-Folder Lifecycle Skeleton

Each subsystem follows the standard AMPEL360 lifecycle structure:

```
01_OVERVIEW/              - Purpose, scope, and context
02_SAFETY/                - Safety analysis, FMEA, hazard identification
03_REQUIREMENTS/          - Functional and performance specifications
04_DESIGN/                - Design documentation and specifications
05_INTERFACES/            - Interface Control Documents (ICDs)
06_ENGINEERING/           - Engineering analysis, calculations, simulations
07_V_AND_V/              - Verification and validation plans/reports
08_PROTOTYPING/          - Prototype development and testing
09_PRODUCTION_PLANNING/  - Manufacturing and production processes
10_CERTIFICATION/        - Certification documentation and compliance
11_OPERATIONS_MAINTENANCE/ - Operating procedures and maintenance manuals
12_ASSETS_MANAGEMENT/    - Asset tracking and lifecycle management
13_SUBSYSTEMS_COMPONENTS/ - Detailed subsystem and component breakdown
14_META_GOVERNANCE/      - Documentation control and governance
```

---

## Key Interfaces

### Aircraft Interfaces
- **ATA 28:** Fuel System (LH₂ refueling interface)
- **ATA 24:** Electrical Power (ground power interface)
- **ATA 12:** Servicing (general servicing interfaces)

### Infrastructure Interfaces
- **ATA 02:** Operations Information (operational procedures)
- **ATA 10:** Parking, Mooring, Storage (ground handling)
- **ATA 85-90:** Infrastructure Interface Standards

---

## Hydrogen Safety Requirements

All GSE used with AMPEL360 aircraft must comply with:

- **ISO 19881:** Gaseous hydrogen — Land vehicle fuel containers
- **SAE J2601:** Fueling protocols for light duty gaseous hydrogen surface vehicles
- **NFPA 2:** Hydrogen Technologies Code
- **EASA Special Condition:** Hydrogen fuel cell systems (pending)

Special attention is required for:
- ❄️ Cryogenic temperature handling (20K / -253°C)
- 💨 Hydrogen leak detection and ventilation
- 🔥 Fire suppression and emergency response
- 🧊 Cold burn prevention
- ⚡ Static electricity control

---

## Governance

### Certification Authority
All GSE must be certified and approved for use with the AMPEL360 aircraft by:
- AMPEL360 Engineering Authority
- GSE manufacturer quality system (ISO 9001, AS9100)
- Relevant aviation authority (EASA, FAA) for critical systems

### Configuration Control
- All GSE changes subject to Configuration Control Board (CCB) review
- Traceability maintained in 03-90-00_IN_SERVICE_REGISTRY
- Drawing and document control per 14_META_GOVERNANCE requirements

### Documentation Standards
- **S1000D** for technical publications
- **ATA iSpec 2200** for data exchange
- **ISO 15926** for lifecycle data integration

---

## Quick Reference

| GSE Type | Code Block | Example |
|----------|------------|---------|
| Handling/Maintenance Systems | 03-20-xx | Fleet Maintenance Program |
| Physical Structures | 03-50-xx | Support Frames |
| Energy/Refueling Equipment | 03-80-xx | LH₂ Refueler, Ground Power |
| Documentation/Catalogues | 03-90-xx | Training, SDS, Spares IPL |

---

## Related Documents

- [`NUMBERING_RULES.md`](../../NUMBERING_RULES.md) - Complete numbering system documentation
- [`ATA_02-OPERATIONS_INFORMATION`](../ATA_02-OPERATIONS_INFORMATION/) - Operational procedures
- [`ATA_28-FUEL_SAF_AND_CRYOGENIC`](../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENIC_SYSTEMS/ATA_28-FUEL_SAF_AND_CRYOGENIC/) - On-board H₂ system

---

**© 2024-2025 AMPEL360 Project | All Rights Reserved**
