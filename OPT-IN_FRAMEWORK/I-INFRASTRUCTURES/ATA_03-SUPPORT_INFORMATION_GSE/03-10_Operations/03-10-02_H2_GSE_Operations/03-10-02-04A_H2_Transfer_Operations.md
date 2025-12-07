---
Title: "H₂ Transfer Operations"
Identifier: "AMPEL360-03-10-02-04A"
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
Abstract: "Procedures for transferring liquid hydrogen between ground storage systems, mobile bowsers, and fixed infrastructure."
Keywords: ["H₂ Transfer","LH₂","GSE","Ground Operations","Storage","ATA 03"]
Compliance:
  - "ATA iSpec 2200"
  - "SAE AS6968"
  - "CGA H-3"
  - "NFPA 2"
Links:
  ParentDoc: "./03-10-02-01A_LH2_Fueling_Operations.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial release" }
---

# 03-10-02-04A — H₂ Transfer Operations

## 1. Purpose

This document defines procedures for transferring liquid hydrogen between various ground support systems, including mobile bowsers, fixed storage dewars, and hydrant systems.

## 2. Scope

This document covers:
- LH₂ transfer between storage systems
- Bowser loading from fixed storage
- Hydrant system operations
- Transfer efficiency optimization
- Boil-off minimization techniques

## 3. Applicable Documents

- SAE AS6968 (Hydrogen Aircraft Refueling Ground Support Equipment)
- CGA H-3 (Cryogenic Hydrogen Storage)
- NFPA 2 (Hydrogen Technologies Code)
- `03-10-02-01A_LH2_Fueling_Operations.md`

## 4. Operations Description

### 4.1 Overview

H₂ transfer operations move cryogenic liquid hydrogen between ground storage systems to position fuel for aircraft refueling operations. Efficient transfer operations minimize boil-off losses and ensure fuel availability.

### 4.2 Operating Procedures

#### 4.2.1 Bowser Loading from Fixed Storage

| Step | Action | Responsible | Notes |
|------|--------|-------------|-------|
| 1 | Position bowser at loading station | Bowser Driver | Align transfer connections |
| 2 | Set parking brake and chocks | Bowser Driver | Prevent vehicle movement |
| 3 | Ground bonding bowser and storage system | H₂ Operator | Verify continuity <10 Ω |
| 4 | Connect transfer line to bowser | H₂ Operator | Verify proper engagement |
| 5 | Pre-cool transfer line (if warm) | H₂ Operator | Vent initial boil-off |
| 6 | Open valves and begin transfer | H₂ Operator | Monitor flow rate, pressure |
| 7 | Fill to target quantity | H₂ Operator | Leave ullage space (5-10%) |
| 8 | Close valves and depressurize line | H₂ Operator | Purge if required |
| 9 | Disconnect transfer equipment | H₂ Operator | Cap all connections |
| 10 | Record transfer quantity and boil-off | H₂ Operator | Update inventory system |
| 11 | Release bowser for service | H₂ Supervisor | Authorize for aircraft fueling |

#### 4.2.2 Transfer Efficiency Optimization

**Factors Affecting Transfer Efficiency:**
- Transfer line pre-cooling (minimize cooldown losses)
- Transfer rate (faster = less time for heat ingress, but pressure limits)
- Ambient temperature and weather conditions
- Transfer distance and line insulation quality
- Equipment pre-cooling and thermal management

**Best Practices:**
- Schedule transfers during cooler parts of day
- Use shortest practical transfer lines
- Maintain transfer equipment in top condition
- Monitor and minimize connection/disconnection time
- Pre-cool receiving vessels when possible

### 4.3 Safety Considerations

- **Transfer Area Security**: Control access during operations
- **Spill Containment**: Ensure adequate drainage away from equipment
- **Ventilation**: Outdoor operations with good natural air movement
- **Emergency Shutoff**: E-stop accessible from transfer location
- **Communication**: Maintain radio contact throughout operation

## 5. Equipment Requirements

| Equipment | Specification | Quantity |
|-----------|---------------|----------|
| Vacuum-Insulated Transfer Hoses | Rated -253°C, various lengths | As required |
| Cryogenic Transfer Pump | 200-500 kg/min capacity | 1 per system |
| Flow Meters | Cryogenic LH₂ service, ±1% accuracy | Per transfer path |
| Pressure/Temperature Monitors | Real-time monitoring | Multiple points |

## 6. Cross-References

- Related ATA Chapters: ATA 28 (Fuel System)
- Parent Document: 03-10-02_H2_GSE_Operations
- Related Operations: 03-10-02-01A_LH2_Fueling_Operations
- Related Equipment: 03-10-02-02A_Cryogenic_GSE_Operations

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
