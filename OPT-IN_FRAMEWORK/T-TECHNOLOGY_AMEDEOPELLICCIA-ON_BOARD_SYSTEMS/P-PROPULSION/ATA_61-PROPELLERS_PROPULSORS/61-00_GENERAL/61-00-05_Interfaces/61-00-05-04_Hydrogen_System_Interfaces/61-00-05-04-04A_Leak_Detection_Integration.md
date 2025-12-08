# 61-00-05-04-04A - Leak Detection Integration Interface

**Document ID:** 61-00-05-04-04A  
**Title:** H₂ Leak Detection Integration Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the hydrogen leak detection system interface for the propulsor installation, including sensor placement, signal interfaces, and integration with safety systems.

---

## 2. Scope

This specification covers:
- H₂ leak detector sensor types and locations
- Electrical and data interfaces
- Alert and warning logic
- Integration with ventilation and safety systems
- Ground and flight leak detection modes

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements |
| 61-00-05-04-02A | Safety Interlocks | Related interface |
| [SAE AIR7928](https://www.sae.org/standards/content/air7928/) | Hydrogen Aircraft — Safety Considerations | H₂ safety |

---

## 4. Interface Description

### 4.1 Leak Detector Locations

| Location ID | Description | Sensor Type | Quantity |
|-------------|-------------|-------------|----------|
| LD-61-01 | H₂ supply line (propulsor inlet) | Electrochemical | 2 (redundant) |
| LD-61-02 | Nacelle interior (ventilated zone) | Electrochemical | 2 |
| LD-61-03 | Motor housing (potential accumulation zone) | Catalytic bead | 2 |
| LD-61-04 | Fuel cell/generator enclosure | Electrochemical | 2 |

### 4.2 Sensor Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Sensor Type | Electrochemical (primary) | — | High sensitivity |
| Detection Range | 0-4% H₂ by volume | — | 0-100% LEL (Lower Explosive Limit) |
| Alarm Threshold (Level 1) | 0.4% (10% LEL) | % vol | Caution |
| Alarm Threshold (Level 2) | 1.0% (25% LEL) | % vol | Warning + action |
| Response Time (T90) | <5 | seconds | To 90% of final reading |
| Accuracy | ±0.1% vol at 1% H₂ | — | — |
| Operating Temperature | -20 to +50 | °C | — |
| Output Signal | 4-20 mA | — | Analog, proportional to H₂ concentration |

### 4.3 Functional Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| H2L-61-001 | Detection threshold (Level 1) | 0.4% H₂ (10% LEL) | Test |
| H2L-61-002 | Detection threshold (Level 2) | 1.0% H₂ (25% LEL) | Test |
| H2L-61-003 | Response time | <5 seconds (T90) | Test |
| H2L-61-004 | False alarm rate | <1 per 1,000 flight hours | Operational data |
| H2L-61-005 | Sensor self-test | Daily automatic BIT | Design feature |
| H2L-61-006 | Redundancy | 2-out-of-2 for safety-critical zones | Design, FMEA |

---

## 5. Interface Control

### 5.1 Electrical Interface

| Parameter | Specification |
|-----------|---------------|
| Power Supply | 28 VDC ±4V |
| Current Consumption | <50 mA per sensor |
| Output Signal | 4-20 mA (isolated) |
| Wiring | Shielded twisted pair, 22 AWG |
| Connector | M12 A-coded, 5-pin |

### 5.2 Data Interface

Leak detection data transmitted via:
- AFDX VL-6121 (health monitoring)
- ARINC 429 Label 103 (maintenance/diagnostics)
- Hardwired discrete alarm signals (Level 2 alarms)

### 5.3 Alarm Logic

```
IF (Any sensor ≥ 0.4% H₂) THEN
  Alert Level 1 (Caution)
  Log event
  Increase ventilation

IF (Any sensor ≥ 1.0% H₂ OR 2 sensors ≥ 0.4% H₂) THEN
  Alert Level 2 (Warning)
  Close H₂ supply valves (via safety interlock)
  Activate purge system
  Alert flight crew
  Inhibit propulsor restart
```

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| H2L-T-001 | Detection threshold verification | Alarm at 0.4% and 1.0% H₂ | Calibration gas test |
| H2L-T-002 | Response time | T90 < 5 seconds | Step input test |
| H2L-T-003 | False alarm immunity | No alarm from humidity, hydrocarbons | Cross-sensitivity test |
| H2L-T-004 | Redundancy verification | Correct operation with 1 sensor failure | Fault injection |
| H2L-T-005 | Self-test function | BIT detects sensor faults | Functional test |

### 6.2 Production Verification

| Inspection | Frequency | Method |
|------------|-----------|--------|
| Sensor calibration | 100% | Calibration gas (1.0% H₂) |
| Electrical continuity | 100% | Multimeter |
| Self-test function | 100% | Automated test fixture |
| Alarm output verification | 100% | Simulated leak test |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 28](../../../../F-FUEL/ATA_28-FUEL/README.md) — Fuel System (H₂ leak management)
- [ATA 26](../../../../ATA_26-FIRE_PROTECTION/README.md) — Fire Protection
- [ATA 21](../../../../ATA_21-AIR_CONDITIONING/README.md) — Air Conditioning (ventilation)

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

### 7.3 Related Documents
- 61-00-05-04-02A — Safety Interlocks

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Previous: 61-00-05-04-03A_Pressure_Regulation](61-00-05-04-03A_Pressure_Regulation.md) · [Parent: 61-00-05_Interfaces](../README.md) →

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
