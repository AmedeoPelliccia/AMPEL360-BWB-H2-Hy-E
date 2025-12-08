# 03-00-05-05-02A - Maintenance Data Link

## 1. Purpose
Specifies maintenance data link interface for downloading flight data and uploading software/configuration to AMPEL360 BWB H₂ Hy-E aircraft.

## 2. Scope
Covers data link protocols, security, and procedures for aircraft-GSE data exchange.

## 3. Applicable Documents
- ATA iSpec 2200, ARINC 615A (Aircraft Data Loader), ARINC 717 (Flight Data Recorder)

## 4. Interface Description

### 4.1 Overview
Secure data link for maintenance data download, software loading, and configuration management.

### 4.2 Physical Characteristics
| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| Connection Type | Ethernet 100BASE-TX + ARINC 429 | Redundant |
| Data Rate | 100 Mbit/s (Ethernet) | Full duplex |
| Connector | RJ45 + D-sub 25 | Sealed connectors |
| Security | TLS 1.3 encryption | Certificate-based |
| Protocol | ARINC 615A + custom | Software loading |

### 4.3 Connection Procedure
Secure authentication, data integrity verification, and transfer procedures.

## 5. GSE Equipment Requirements
Portable maintenance access terminal (PMAT), data loader, secure storage.

## 6. Safety Requirements
- Software version control
- Change management procedures
- Backup before updates
- H2 aircraft: intrinsically safe equipment

## 7. Cross-References
- ATA 45 (Central Maintenance System), ATA 46 (Information Systems)
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
