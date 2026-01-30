---
Title: "H₂ Defueling Operations"
Identifier: "AMPEL360-03-10-02-03A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES GSE Operations"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
ReviewDue: "2026-06-07"
Effectivity: "Q100 INTEGRA H₂ GSE Operations"
Abstract: "Operational procedures for safe removal of liquid hydrogen from aircraft fuel tanks for maintenance, emergencies, or fuel quality issues."
Keywords: ["Defueling","H₂ Removal","LH₂","GSE Operations","Maintenance","ATA 03"]
Compliance:
  - "ATA iSpec 2200"
  - "SAE AS6968"
  - "NFPA 2"
Links:
  ParentDoc: "./03-10-02-01A_LH2_Fueling_Operations.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial release" }
---

# 03-10-02-03A — H₂ Defueling Operations

## 1. Purpose

This document establishes procedures for safe removal of liquid hydrogen from AMPEL360 BWB aircraft fuel tanks, including planned defueling for maintenance and emergency defueling scenarios.

## 2. Scope

This document covers:
- Planned defueling procedures for maintenance
- Emergency defueling operations
- Fuel transfer to ground storage or disposal
- Tank purging and inerting post-defueling
- Safety protocols for defueling operations

## 3. Applicable Documents

- SAE AS6968 (Hydrogen Aircraft Refueling Ground Support Equipment)
- NFPA 2 (Hydrogen Technologies Code)
- `03-10-02-01A_LH2_Fueling_Operations.md`
- `03-10-05-03A_Emergency_Response_Ops.md`

## 4. Operations Description

### 4.1 Overview

Defueling operations remove LH₂ from aircraft fuel tanks when required for maintenance, fuel system repairs, emergency situations, or fuel quality concerns. Defueling follows similar safety protocols as refueling but with additional considerations for tank venting and purging.

### 4.2 Operating Procedures

#### 4.2.1 Planned Defueling Procedure

| Step | Action | Responsible | Notes |
|------|--------|-------------|-------|
| 1 | Position aircraft in designated defueling area | Ramp Operations | Away from buildings, other aircraft |
| 2 | Establish safety zone (10m radius minimum) | H₂ Safety Officer | Larger than refueling zone |
| 3 | Configure aircraft fuel system for defueling | Flight Crew / Maintenance | Open appropriate valves |
| 4 | Connect defueling equipment to aircraft | H₂ Operator | Similar to refueling connection |
| 5 | Ground bonding aircraft and GSE | H₂ Operator | Verify continuity <10 Ω |
| 6 | Verify receiving tank has adequate capacity | H₂ Operator | Check available volume |
| 7 | Open defueling valves slowly | H₂ Operator | Control initial flow |
| 8 | Transfer LH₂ to storage or bowser | H₂ Operator | Monitor quantity, rate, pressure |
| 9 | Continue until maximum practical removal | H₂ Operator | Some residual will remain |
| 10 | Close valves and disconnect equipment | H₂ Operator | Follow safe disconnect procedures |
| 11 | Purge aircraft fuel tanks with inert gas | Maintenance Technician | Remove H₂ vapor residue |
| 12 | Verify tank atmosphere safe (<5% H₂) | H₂ Safety Officer | Test before any maintenance |

#### 4.2.2 Emergency Defueling Procedure

**Indications for Emergency Defueling:**
- Fuel system leak detected
- Fire in fuel system area
- Crash/hard landing with fuel system damage
- Fuel contamination detected
- Extreme weather conditions threatening aircraft

**Emergency Procedure (Abbreviated):**
1. Alert airport emergency services immediately
2. Evacuate non-essential personnel from area
3. Position fire suppression equipment
4. If time permits, connect defueling equipment
5. Transfer fuel as quickly as safety allows
6. If immediate danger exists, allow controlled venting/boil-off
7. Monitor H₂ concentrations continuously
8. Do not enter fuel tanks or confined spaces until verified safe

### 4.3 Safety Considerations

- **Extended Safety Zone**: Larger than refueling due to increased venting
- **Ventilation**: Ensure adequate air movement to disperse H₂ vapors
- **Tank Entry**: Never enter tank until purged and tested (<5% H₂, >19.5% O₂)
- **Ignition Sources**: Strictly controlled throughout operation
- **Monitoring**: Continuous H₂ detection during and after defueling
- **Documentation**: Record fuel removed, destination, and tank condition

## 5. Equipment Requirements

| Equipment | Specification | Quantity |
|-----------|---------------|----------|
| Defueling Adapter | Compatible with aircraft fuel receptacle | 1 set |
| LH₂ Receiving Tank | Mobile bowser or fixed storage | Adequate capacity |
| Inert Gas Supply | GN₂ or GHe for tank purging | Sufficient for tank volume |
| H₂ Monitors | Portable, real-time reading | 4 minimum |
| Tank Atmosphere Tester | H₂ and O₂ measurement | 1 unit |

## 6. Cross-References

- Related ATA Chapters: ATA 28 (Fuel System), ATA 05 (Periodic Inspection)
- Parent Document: 03-10-02_H2_GSE_Operations
- Related Fueling: 03-10-02-01A_LH2_Fueling_Operations
- Emergency Response: 03-10-05-03A_Emergency_Response_Ops

## 7. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.
