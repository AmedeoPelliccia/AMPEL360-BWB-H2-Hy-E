# 03-90 - Schemas and Registries

**Origin Rule:** 90 = Schemas/Meta/Catalogues  
**Category:** Documentation - Registries, Training, SDS, IPL/IPC  
**Status:** Active  

---

## Overview

This block contains all **meta-information, documentation, catalogues, registries, and training materials** related to GSE. This includes schemas, illustrated parts lists, safety data sheets, in-service registries, and training programs.

**Law of Origin:** Per the AMPEL360 numbering rules, code block **90-xx** is reserved for schemas, catalogues, meta-information, and documentation, as opposed to functional systems (20-xx), structures (50-xx), or energy equipment (80-xx).

---

## Subsystems

### 03-90-00 - In-Service Registry
Registry of all GSE in service, including certification status, maintenance history, and traceability.

**Scope:**
- GSE asset register (unique identification)
- Certification and approval status
- Configuration management
- Maintenance history tracking
- Location and assignment tracking
- Utilization statistics
- Lifecycle status (active, maintenance, retired)
- Modification and upgrade tracking

**Data Elements:**
- Equipment serial number
- Manufacturer and model
- Date of manufacture
- Certification expiry dates
- Maintenance due dates
- Current location
- Assigned operator/organization
- Service hours/cycles

**Status:** Structure created, documentation pending

---

### 03-90-01 - Training Materials
Training courses, procedures, and certification requirements for GSE operators and maintainers.

**Scope:**
- Operator training programs
  - LH₂ refueler operation
  - Ground power unit operation
  - General GSE handling
- Maintainer training programs
  - Cryogenic system maintenance
  - Electrical system maintenance
  - Safety system testing
- Certification requirements
- Competency assessment procedures
- Refresher training schedules
- Training records management

**Training Courses:**
- 🎓 GSE-001: General GSE Safety (4 hours)
- 🎓 GSE-080: Hydrogen Safety Awareness (8 hours)
- 🎓 GSE-081: LH₂ Refueler Operation (16 hours)
- 🎓 GSE-082: Ground Power Unit Operation (8 hours)
- 🎓 GSE-083: Emergency Response Procedures (4 hours)
- 🎓 GSE-090: GSE Maintenance Fundamentals (24 hours)

**Links to:**
- **03-80-01** - LH₂ Refueler (equipment being trained on)
- **03-80-02** - Ground Power Unit (equipment being trained on)
- **03-90-02** - Safety Data Sheets (safety training content)

**Status:** Structure created, documentation pending

---

### 03-90-02 - Safety Data Sheets
Safety Data Sheets (SDS) for all hazardous materials and substances used in GSE operations.

**Scope:**
- Liquid Hydrogen (LH₂) SDS
  - Physical and chemical properties
  - Hazards identification
  - First aid measures
  - Fire-fighting measures
  - Accidental release measures
  - Handling and storage
  - Exposure controls / PPE
  - Regulatory information
- Cryogenic fluids SDS
- Electrical safety information
- Hydraulic fluids SDS
- Lubricants and greases SDS
- Cleaning agents SDS

**Key SDS Documents:**
- 📄 SDS-001: Liquid Hydrogen (LH₂)
- 📄 SDS-002: Gaseous Hydrogen (GH₂)
- 📄 SDS-003: Liquid Nitrogen (LN₂)
- 📄 SDS-004: Helium (He)
- 📄 SDS-005: Hydraulic Fluid (Skydrol)

**Emergency Procedures:**
- LH₂ spill response
- Hydrogen fire response
- Cryogenic exposure treatment
- Evacuation procedures

**Status:** Structure created, documentation pending

---

### 03-90-10 - Fleet Spares Program
Illustrated Parts List (IPL) and spare parts management program for fleet-wide GSE support.

**Migration Note:** Formerly coded as 03-40-00. Migrated to 03-90-10 per Law of Origin (catalogues → 90-xx).

**Scope:**
- Fleet-wide spare parts catalogue
- Minimum stock levels
- Reorder points and quantities
- Supplier information
- Parts obsolescence management
- Alternative parts identification
- Parts pricing and procurement
- Inventory management system
- Distribution network

**Coverage:**
- Common components across all GSE
- High-wear items
- Safety-critical components
- Long lead-time items
- Consumables and expendables

**Status:** Structure created, documentation pending

---

### 03-90-11 - LH₂ Cryo Refueler Parts
Illustrated Parts Catalogue (IPC) specifically for LH₂ cryogenic refueler components and assemblies.

**Migration Note:** Formerly coded as 03-40-01. Migrated to 03-90-11 per Law of Origin (catalogues → 90-xx).

**Scope:**
- Complete parts breakdown of refueler
- Assembly and subassembly illustrations
- Part numbers and nomenclature
- Applicability (by refueler serial number)
- Quantities per assembly
- Supplier part numbers
- Maintenance level (organizational/depot)
- Special tooling requirements

**Major Assemblies:**
- 📦 Storage Tank Assembly
  - Inner vessel
  - Outer vessel
  - Vacuum insulation
  - Support structure
- 📦 Transfer System Assembly
  - Cryogenic pumps
  - Valves and fittings
  - Transfer hoses
  - Couplings
- 📦 Control System Assembly
  - Sensors (T, P, flow)
  - Controllers
  - Control panels
  - Wiring harnesses
- 📦 Safety System Assembly
  - Leak detectors
  - Emergency shutdown valves
  - Fire suppression
  - Pressure relief valves

**Links to:**
- **03-80-01** - LH₂ Cryogenic Refueler (equipment specification)
- **03-20-11** - LH₂ Refueler Maintenance (maintenance procedures)
- **03-90-10** - Fleet Spares Program (fleet-wide parts management)

**Status:** Structure created, documentation pending

---

## 14-Folder Lifecycle Structure

Each subsystem follows the standard AMPEL360 lifecycle:

```
XX-XX-XX_SUBSYSTEM_NAME/
├── 01_OVERVIEW/
├── 02_SAFETY/
├── 03_REQUIREMENTS/
├── 04_DESIGN/
├── 05_INTERFACES/
├── 06_ENGINEERING/
├── 07_V_AND_V/
├── 08_PROTOTYPING/
├── 09_PRODUCTION_PLANNING/
├── 10_CERTIFICATION/
├── 11_OPERATIONS_MAINTENANCE/
├── 12_ASSETS_MANAGEMENT/
├── 13_SUBSYSTEMS_COMPONENTS/
└── 14_META_GOVERNANCE/
```

---

## Documentation Standards

### Technical Publications
- **S1000D** - International specification for technical publications
  - Common Source Database (CSDB)
  - Data Modules (DM)
  - Publication Modules (PM)
  - Interactive Electronic Technical Publications (IETP)

### Parts Catalogues
- **ATA iSpec 2200** - Electronic data interchange standard
- **S1000D** - Illustrated Parts Data (IPD)
- **ISO 15926** - Industrial automation systems and integration

### Training Materials
- **SCORM** - Sharable Content Object Reference Model
- **xAPI** - Experience API (Learning Management Systems)
- **ISD** - Instructional Systems Design methodology

---

## Related Systems

### Other GSE Categories
- **03-20-xx:** Systems Support (procedures using these materials)
- **03-50-xx:** Structural GSE (equipment being documented)
- **03-80-xx:** Energy GSE (equipment being documented)

### Equipment Being Documented
- **03-80-01:** LH₂ Cryogenic Refueler
- **03-80-02:** HV Ground Power Unit
- **03-50-01:** LH₂ Support Frames
- All GSE systems

### Aircraft Systems
- **ATA 91:** Charts (operational documentation)
- **ATA 92:** Model-Based Maintenance
- **ATA 95:** Digital Product Passport

---

## Migration from Legacy Codes

| Legacy Code | Legacy Name | New Code | New Name | Reason |
|-------------|-------------|----------|----------|--------|
| 03-40-00 | Fleet Spares | 03-90-10 | Fleet Spares Program | Catalogue → 90-xx |
| 03-40-01 | Refueler Parts | 03-90-11 | LH₂ Refueler Parts | Catalogue → 90-xx |

All references to legacy codes should be updated to new codes per Law of Origin.

---

## Next Steps

1. Develop in-service registry database schema (03-90-00)
2. Create operator training curriculum (03-90-01)
3. Compile safety data sheets (03-90-02)
4. Build fleet spares catalogue (03-90-10)
5. Detail LH₂ refueler IPC (03-90-11)

---

**© 2024-2025 AMPEL360 Project | All Rights Reserved**
