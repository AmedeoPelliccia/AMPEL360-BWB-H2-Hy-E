# 03-40-02-04A - H2 Leak Detection Software

**Document ID:** 03-40-02-04A  
**Title:** Hydrogen Leak Detection Software  
**ATA Chapter:** 03 — Support Information/GSE  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document specifies the software for detecting hydrogen leaks in GSE systems using advanced leak detection algorithms, sensor fusion, and predictive maintenance capabilities.

---

## 2. Scope

Covers hydrogen leak detection, localization, quantification, and automated response for LH2 ground support equipment.

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| [ISO 26142](https://www.iso.org/standard/74601.html) | Hydrogen Detection Apparatus | Detection standards |
| [IEC 61508](https://www.iec.ch/functional-safety) | Functional Safety | SIL 3 |
| [NFPA 2](https://www.nfpa.org/codes-and-standards/list-of-codes-and-standards/detail?code=2) | Hydrogen Technologies Code | Safety |

---

## 4. Software Description

### 4.1 Overview

Multi-sensor leak detection with AI-based pattern recognition for early leak identification and localization.

**Safety Integrity Level:** SIL 3

### 4.2 Detection Methods

| Method | Sensitivity | Response Time | Application |
|--------|-------------|---------------|-------------|
| Point Sensors | 10-100 ppm | <1 sec | Fixed locations |
| Infrared Imaging | 100 ppm-m | <0.5 sec | Area coverage |
| Acoustic Detection | Small leaks | Real-time | High-pressure systems |
| Flow Balance | 0.1% of flow | 5-10 sec | System-wide |

### 4.3 Leak Classification

| Leak Size | H2 Rate | Action | Response Time |
|-----------|---------|--------|---------------|
| Micro | <10 g/hr | Log, investigate | 24 hours |
| Small | 10-100 g/hr | Alarm, schedule repair | 4 hours |
| Medium | 100-1000 g/hr | Alarm, controlled shutdown | 30 minutes |
| Large | >1000 g/hr | Emergency shutdown | Immediate |

### 4.4 Interfaces

- H2 sensor network
- Flow meters and pressure sensors
- SCADA system
- Emergency shutdown system
- Maintenance management system

---

## 5. Safety and Security Requirements

| Requirement ID | Requirement | Verification |
|----------------|-------------|--------------|
| H2-LEAK-001 | Detect leaks at 10% LEL | Testing |
| H2-LEAK-002 | Localize leak to ±5 m | Algorithm validation |
| H2-LEAK-003 | Quantify leak rate ±20% | Flow correlation |
| H2-LEAK-004 | Initiate ESD for large leaks <5 sec | System test |

---

## 6. Cross-References

- 03-40-02-01A — LH2 Fueling Control SW
- 03-40-02-03A — H2 Safety Monitoring SW
- 03-40-05-02A — Predictive Maintenance SW

---

## 7. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
