# 03-40-02-03A - H2 Safety Monitoring Software

**Document ID:** 03-40-02-03A  
**Title:** Hydrogen Safety Monitoring Software  
**ATA Chapter:** 03 — Support Information/GSE  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the safety monitoring software for detecting and responding to hydrogen hazards in ground support equipment operations, including leak detection, fire detection, and personnel safety monitoring.

---

## 2. Scope

This specification covers:
- Hydrogen concentration monitoring
- Fire and flame detection
- Oxygen deficiency monitoring
- Personnel proximity detection in hazard zones
- Automated safety response algorithms
- Real-time alert and alarm management

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| [IEC 61508](https://www.iec.ch/functional-safety) | Functional Safety | SIL 3 requirement |
| [IEC 60079-29-1](https://webstore.iec.ch/publication/638) | Gas Detectors - Performance Requirements | Detector standards |
| [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) | Hydrogen Technologies Code | Safety requirements |
| [ISO 26142](https://www.iso.org/standard/74601.html) | Hydrogen Detection Apparatus - Stationary Applications | Detection systems |

---

## 4. Software Description

### 4.1 Overview

The H2 Safety Monitoring Software provides continuous surveillance of hydrogen operations areas, detecting hazardous conditions and automatically initiating protective actions to prevent incidents.

**Safety Integrity Level:** SIL 3 (IEC 61508)

### 4.2 Software Specifications

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| H2 Detection Range | 0 to 4% volume (0-100% LEL) | LEL = 4% vol |
| Detection Response Time | <1 second | Per IEC 60079-29-1 |
| Alarm Response Time | <2 seconds | From detection to action |
| Sensor Polling Rate | 1 Hz minimum | Continuous monitoring |
| Data Logging | All events logged | 10-year retention |
| Redundancy | 2oo3 voting for safety actions | Triple modular redundancy |

### 4.3 Monitoring Zones

| Zone Type | H2 Sensors | Fire Detectors | O2 Monitors | Personnel Detection |
|-----------|-----------|----------------|-------------|-------------------|
| Fueling Area | 6-10 | 4-6 | 2-4 | Yes |
| Storage Area | 4-6 | 2-4 | 2 | Yes |
| Transfer Paths | 8-12 | 4-6 | As needed | Yes |
| Equipment Rooms | 2-4 | 2 | 2 | No |
| Control Room | 1 | 2 | Optional | No |

### 4.4 Safety Thresholds

| Parameter | Warning Level | Alarm Level | Emergency Shutdown |
|-----------|---------------|-------------|-------------------|
| H2 Concentration | >10% LEL (0.4% vol) | >25% LEL (1.0% vol) | >40% LEL (1.6% vol) |
| O2 Deficiency | <19.5% vol | <18% vol | <17% vol |
| Fire Detection | Pre-alarm | Confirmed fire | Multiple zones |
| Temperature (abnormal) | >5°C above ambient | >10°C above ambient | Rapid rise detected |

### 4.5 Interfaces

- Gas detection system (Modbus, 4-20mA)
- Fire alarm system
- Emergency shutdown system
- Personnel tracking system
- SCADA/HMI

---

## 5. Safety and Security Requirements

### 5.1 Safety Requirements

| Requirement ID | Requirement | Verification |
|----------------|-------------|--------------|
| H2-MON-SAF-001 | Detect H2 at >10% LEL with 95% confidence | Calibration testing |
| H2-MON-SAF-002 | Activate ESD at >40% LEL within 2 seconds | System testing |
| H2-MON-SAF-003 | Provide 3-level alarm escalation | Logic verification |
| H2-MON-SAF-004 | Continue operation on single sensor failure | Redundancy testing |
| H2-MON-SAF-005 | Log all safety events with timestamp | Audit trail review |

---

## 6. Cross-References

- 03-40-02-01A — LH2 Fueling Control SW
- 03-40-02-04A — H2 Leak Detection SW
- 03-40-06-02A — Emergency Shutdown SW

---

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

---
