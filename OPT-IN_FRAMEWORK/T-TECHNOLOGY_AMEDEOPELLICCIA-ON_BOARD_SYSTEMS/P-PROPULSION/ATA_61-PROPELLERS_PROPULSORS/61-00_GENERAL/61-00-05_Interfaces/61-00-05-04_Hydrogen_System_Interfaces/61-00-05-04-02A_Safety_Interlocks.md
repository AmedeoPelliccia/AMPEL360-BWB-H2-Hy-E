# 61-00-05-04-02A - Safety Interlocks Interface

**Document ID:** 61-00-05-04-02A  
**Title:** H₂ System Safety Interlocks Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the safety interlock system between the propulsor and the aircraft H₂ fuel system to prevent unsafe operating conditions.

---

## 2. Scope

This specification covers:
- H₂ leak detection interlocks
- Overpressure/underpressure interlocks
- Temperature limit interlocks
- Emergency shutdown logic
- Ground safety interlocks

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements |
| 61-00-02-SFHA-001 | System Functional Hazard Assessment | Safety analysis |
| [SAE AIR7928](https://www.sae.org/standards/content/air7928/) | Hydrogen Aircraft — Safety Considerations | H₂ safety |

---

## 4. Interface Description

### 4.1 Safety Interlock Signals

| Signal Name | Source | Destination | Type | Function |
|-------------|--------|-------------|------|----------|
| H2_LEAK_DETECTED | H₂ Leak Detector | Propulsor Control + Fuel System | Discrete | Shutdown fuel supply |
| H2_OVERPRESSURE | Pressure Sensor | Propulsor Control + Fuel System | Discrete | Close supply valve |
| H2_UNDERTEMPERATURE | Temperature Sensor | Propulsor Control | Discrete | Prevent cold damage |
| GROUND_SAFETY_PIN | Ground Equipment | Propulsor Control | Discrete | Prevent H₂ flow on ground |
| EMERG_H2_SHUTOFF | Pilot Command | All H₂ Systems | Discrete | Master shutdown |
| PURGE_COMPLETE | Purge System | Propulsor Control | Discrete | Allow H₂ introduction |

### 4.2 Functional Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| H2S-61-001 | Leak detection response time | <500 ms from detection to valve closure | Test |
| H2S-61-002 | Overpressure shutoff setpoint | >1.2× max operating pressure | Test |
| H2S-61-003 | Redundant sensor voting | 2-out-of-3 for safety-critical | Design, Test |
| H2S-61-004 | Interlock failsafe | Fail-safe to closed/shutdown | FMEA, Test |
| H2S-61-005 | Ground safety pin detection | Prevent H₂ valve opening | Test |

---

## 5. Interface Control

### 5.1 Interlock Logic

```
IF (H2_LEAK_DETECTED OR H2_OVERPRESSURE OR EMERG_H2_SHUTOFF)
  THEN Close H₂ supply valves
  AND  Disable propulsor startup
  AND  Activate purge system
  AND  Alert flight crew

IF (GROUND_SAFETY_PIN_INSTALLED)
  THEN Disable H₂ supply valves
  AND  Lock out propulsor operation
```

### 5.2 Connector Pinout

Interlocks via hardwired discrete signals (see 61-00-05-02-02A) and AFDX VL-6101.

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| H2S-T-001 | Leak detection interlock | <500 ms response | Fault injection |
| H2S-T-002 | Overpressure shutoff | Valve closure at setpoint | Pressure test |
| H2S-T-003 | Redundancy verification | Correct operation with 1 sensor failure | Fault injection |
| H2S-T-004 | Ground safety pin | No H₂ flow with pin installed | Functional test |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 28](../../../../F-FUEL/ATA_28-FUEL/README.md) — Fuel System
- [ATA 26](../../../../ATA_26-FIRE_PROTECTION/README.md) — Fire Protection

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Previous: 61-00-05-04-01A_H2_Fuel_Supply_Connections](61-00-05-04-01A_H2_Fuel_Supply_Connections.md) · [Next: 61-00-05-04-03A_Pressure_Regulation](61-00-05-04-03A_Pressure_Regulation.md) →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Hydrogen System Interfaces  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
