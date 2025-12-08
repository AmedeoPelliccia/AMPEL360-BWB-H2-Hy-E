# 03-00-05-05-03A - Diagnostic Ports

## 1. Purpose
Specifies diagnostic port locations and interfaces for troubleshooting AMPEL360 BWB H₂ Hy-E aircraft systems.

## 2. Scope
Covers diagnostic port types, access, and testing procedures for aircraft systems.

## 3. Applicable Documents
- ATA iSpec 2200, SAE J1939 (CAN Bus), OBD-II Standards

## 4. Interface Description

### 4.1 Overview
Multiple diagnostic ports provide access to aircraft subsystems for fault detection and analysis.

### 4.2 Physical Characteristics
| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| Port Types | CAN Bus, RS-232, Ethernet | Multiple protocols |
| Connector Locations | Throughout aircraft | Per system |
| CAN Data Rate | 250 kbit/s, 500 kbit/s | System dependent |
| Access Level | Technician, Engineer, OEM | Security tiered |

### 4.3 Connection Procedure
Standard diagnostic connection, system interrogation, and fault code retrieval.

## 5. GSE Equipment Requirements
Multi-protocol diagnostic tool, fault code reader, oscilloscope.

## 6. Safety Requirements
- Verify system state before connection
- Use authorized diagnostic equipment only
- Document all findings
- H2 aircraft: certified intrinsically safe tools

## 7. Cross-References
- ATA 45 (Central Maintenance System)
- Related: [03-00-05-05-01A_ARINC_429_Ground_Interface](./03-00-05-05-01A_ARINC_429_Ground_Interface.md)

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
