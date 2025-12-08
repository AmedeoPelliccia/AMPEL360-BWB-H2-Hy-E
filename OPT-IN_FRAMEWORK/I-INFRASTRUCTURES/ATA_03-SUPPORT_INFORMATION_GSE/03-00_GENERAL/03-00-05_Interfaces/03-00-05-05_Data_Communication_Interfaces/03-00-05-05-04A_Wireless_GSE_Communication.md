# 03-00-05-05-04A - Wireless GSE Communication

## 1. Purpose
Specifies wireless communication interfaces between AMPEL360 BWB H₂ Hy-E aircraft and ground support equipment.

## 2. Scope
Covers wireless protocols, security, and operational procedures for GSE-aircraft communication.

## 3. Applicable Documents
- ATA iSpec 2200, IEEE 802.11 (Wi-Fi), Bluetooth 5.0, RTCA DO-160G

## 4. Interface Description

### 4.1 Overview
Wireless communication enables cable-free data exchange for monitoring, diagnostics, and control.

### 4.2 Physical Characteristics
| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| Protocol | Wi-Fi 6 (802.11ax) | 2.4/5 GHz bands |
| Range | 30m typical | Line of sight |
| Security | WPA3-Enterprise | 256-bit encryption |
| Data Rate | Up to 600 Mbit/s | Actual depends on conditions |
| Backup Protocol | Bluetooth 5.0 LE | For close-range operations |

### 4.3 Connection Procedure
Secure pairing, authentication, encrypted data transfer, and session termination procedures.

## 5. GSE Equipment Requirements
Wireless access point, certified tablets/laptops, secure authentication server.

## 6. Safety Requirements
- Approved for use in aircraft environment
- RF interference monitoring
- Secure authentication mandatory
- H2 aircraft: certified for Zone 2 areas

## 7. Cross-References
- ATA 46 (Information Systems), ATA 23 (Communications)
- Related: [03-00-05-05-02A_Maintenance_Data_Link](./03-00-05-05-02A_Maintenance_Data_Link.md)

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
