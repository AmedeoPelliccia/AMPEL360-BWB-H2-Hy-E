# 03-00-05-01-02A - Ground Power Receptacles

## 1. Purpose
This document specifies the design, installation, and maintenance requirements for ground power receptacles on the AMPEL360 BWB H₂ Hy-E aircraft.

## 2. Scope
This specification covers all ground power receptacle installations, including AC and DC power interfaces, protective covers, and associated hardware.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- ARP4754A (Guidelines for Development of Civil Aircraft and Systems)
- MIL-DTL-38999 (Connectors, Electrical, Circular, Threaded)
- SAE AS50881 (Wiring Aerospace Vehicle)
- RTCA DO-160G (Environmental Conditions and Test Procedures)

## 4. Interface Description

### 4.1 Overview
Ground power receptacles provide the physical and electrical interface between external ground power units and the aircraft's electrical distribution system. Multiple receptacles are strategically located for operational flexibility.

### 4.2 Physical Characteristics
| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| AC Receptacle Type | MS3106F 28-21P | - |
| DC Receptacle Type | MS3106F 24-22P | - |
| Receptacle Material | Aluminum alloy, anodized | MIL-A-8625 Type II |
| Protective Cover | Stainless steel, spring-loaded | - |
| Mounting Flange | 3-bolt pattern, M8 | - |
| Sealing | EPDM gasket, IP65 rated | - |
| Contact Plating | Gold over nickel | 50 micro-inch minimum |

### 4.3 Connection Procedure
1. **Access Preparation**
   - Open protective cover using release latch
   - Inspect receptacle contacts for corrosion or damage
   - Verify O-ring seal integrity
   - Check for moisture or contamination

2. **Post-Use Inspection**
   - Inspect contacts after each use
   - Clean with approved contact cleaner if necessary
   - Verify protective cover closes and latches properly
   - Document any anomalies in aircraft maintenance log

## 5. GSE Equipment Requirements
| Equipment | Specification | Notes |
|-----------|---------------|-------|
| Inspection Tools | Borescope, LED light | For internal contact inspection |
| Cleaning Supplies | MIL-PRF-680 Type II cleaner | For contact maintenance |
| Torque Wrench | 0-20 Nm calibrated | For mounting bolt verification |
| Continuity Tester | Digital multimeter | For electrical verification |

## 6. Safety Requirements
- **Installation Safety**
  - Verify aircraft power OFF before any receptacle maintenance
  - Use lockout/tagout procedures during installation work
  - Torque mounting bolts to specified values (15 Nm ±2 Nm)
  - Verify proper bonding to aircraft structure

- **H2 Aircraft Specific**
  - Receptacles must be explosion-proof rated for Zone 2 areas
  - Materials must be compatible with hydrogen environment
  - No exposed spark-producing surfaces
  - Integrated static discharge path verification required

- **Maintenance Safety**
  - Perform functional tests after any maintenance
  - Verify seal integrity with pressure test (if applicable)
  - Check grounding continuity < 0.1Ω to structure
  - Replace protective covers showing wear or damage

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 24 (Electrical Power)
  - ATA 20 (Standard Practices - Airframe)
  - ATA 05 (Time Limits/Maintenance Checks)
- Parent Document: [03-00-05_Interfaces](../README.md)
- Related GSE Operations: 03-10_Operations
- Related Interface: [03-00-05-01-01A_GPU_Aircraft_Connection](./03-00-05-01-01A_GPU_Aircraft_Connection.md)
- Related Interface: [03-00-05-01-04A_Electrical_Grounding](./03-00-05-01-04A_Electrical_Grounding.md)

## 8. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 GSE Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
