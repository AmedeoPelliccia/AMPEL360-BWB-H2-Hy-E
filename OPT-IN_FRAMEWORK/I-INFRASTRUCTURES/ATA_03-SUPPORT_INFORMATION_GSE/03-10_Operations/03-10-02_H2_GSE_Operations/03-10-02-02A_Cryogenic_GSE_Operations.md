---
Title: "Cryogenic GSE Operations"
Identifier: "AMPEL360-03-10-02-02A"
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
Abstract: "Operational procedures for cryogenic ground support equipment used in LH₂ handling, storage, and transfer at -253°C."
Keywords: ["Cryogenic","GSE","LH₂","Operations","Cold Operations","ATA 03"]
Compliance:
  - "ATA iSpec 2200"
  - "SAE AS6968"
  - "CGA H-3 - Cryogenic Hydrogen Storage"
  - "NFPA 2"
Links:
  ParentDoc: "./03-10-02-01A_LH2_Fueling_Operations.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial release" }
---

# 03-10-02-02A — Cryogenic GSE Operations

## 1. Purpose

This document defines operational procedures for cryogenic ground support equipment (GSE) used in liquid hydrogen handling operations, including equipment pre-cooling, operation at -253°C, and maintenance considerations for cryogenic systems.

## 2. Scope

This document covers:
- Cryogenic GSE equipment types and specifications
- Pre-cooling and thermal management procedures
- Vacuum-insulated system operations
- Boil-off management and venting
- Equipment cooldown and warmup procedures
- Cryogenic safety protocols

## 3. Applicable Documents

- SAE AS6968 (Hydrogen Aircraft Refueling Ground Support Equipment)
- CGA H-3 (Cryogenic Hydrogen Storage)
- NFPA 2 (Hydrogen Technologies Code)
- CGA P-12 (Safe Handling of Cryogenic Liquids)
- `03-10-02-01A_LH2_Fueling_Operations.md`

## 4. Operations Description

### 4.1 Overview

Cryogenic GSE for LH₂ operations must maintain hydrogen at -253°C throughout storage and transfer processes. These systems utilize vacuum insulation, specialized materials, and thermal management strategies to minimize heat ingress and boil-off losses.

### 4.2 Operating Procedures

#### 4.2.1 Cryogenic Equipment Startup

| Step | Action | Responsible | Notes |
|------|--------|-------------|-------|
| 1 | Inspect vacuum insulation integrity | Cryogenic Technician | Check for frost patterns indicating vacuum loss |
| 2 | Verify pressure relief devices functional | Cryogenic Technician | Test PRV operation, check set pressures |
| 3 | Check boil-off vent system clear | Cryogenic Technician | Ensure no blockages in vent lines |
| 4 | Monitor vacuum jacket pressure | Cryogenic Technician | Should be <10⁻⁴ mbar for effective insulation |
| 5 | Begin equipment pre-cooling (if warm) | Cryogenic Operator | Introduce LH₂ slowly, vent boil-off |
| 6 | Monitor cooldown temperatures | Cryogenic Operator | Allow gradual thermal equilibration |
| 7 | Verify all valves and controls operational | Cryogenic Operator | Test before committing to operations |
| 8 | Complete pre-use inspection checklist | Cryogenic Technician | Document equipment readiness |

#### 4.2.2 Boil-off Management

**Boil-off Rate Factors:**
- Vacuum insulation effectiveness (heat leak)
- Ambient temperature
- Fill level (surface area to volume ratio)
- Transfer line cool-down losses
- Equipment age and condition

**Typical Boil-off Rates:**
- LH₂ Storage Dewars: 0.2-0.5% per day
- Transfer Operations: 2-5% during connection/disconnection
- Fueling Bowsers: 1-2% per day (well-maintained)

**Boil-off Handling Procedures:**
1. Vent boil-off to safe upward direction (minimum 4m above grade)
2. Monitor H₂ concentration in vent plume (<25% LEL at 1m from vent)
3. Keep ignition sources away from vent discharge (minimum 7.5m)
4. Record boil-off losses for inventory management
5. Investigate if boil-off rates exceed normal parameters

### 4.3 Safety Considerations

- **Cryogenic Burns**: Prevent skin/eye contact with cryogenic fluids or cold surfaces
- **Trapped Cryogen**: Never fully enclose cryogenic liquid (pressure hazard)
- **Material Selection**: Use only materials rated for cryogenic service
- **Vacuum Loss**: Monitor insulation performance; loss creates rapid boil-off
- **Oxygen Enrichment**: Air liquefaction near LH₂ leaks creates fire hazard
- **Ice Formation**: Manage ice buildup on external surfaces (slip/trip hazard)

## 5. Equipment Requirements

| Equipment | Specification | Quantity |
|-----------|---------------|----------|
| LH₂ Storage Dewar | 10,000-50,000 L capacity, vacuum-insulated | Per site |
| Cryogenic Transfer Pumps | LH₂ rated, 100-500 kg/min flow capacity | 1 per bowser |
| Vacuum-Insulated Transfer Lines | -253°C rated, flexible or rigid | As required |
| Temperature Sensors | Cryogenic RTDs, -270°C to +50°C range | Multiple locations |
| Pressure Sensors | 0-10 bar absolute, cryogenic rated | Per vessel |
| Vacuum Monitoring | Pirani/Penning gauges for insulation vacuum | Per insulated component |

## 6. Cross-References

- Related ATA Chapters: ATA 28 (Fuel System)
- Parent Document: 03-10-02_H2_GSE_Operations
- Related Fueling Ops: 03-10-02-01A_LH2_Fueling_Operations
- Related Safety: 03-10-05-02A_H2_Safety_Operations

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
