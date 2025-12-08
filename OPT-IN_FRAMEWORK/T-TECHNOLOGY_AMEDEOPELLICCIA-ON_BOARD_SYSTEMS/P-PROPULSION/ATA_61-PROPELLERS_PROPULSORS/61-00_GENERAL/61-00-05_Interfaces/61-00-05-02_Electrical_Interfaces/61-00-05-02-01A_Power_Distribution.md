# 61-00-05-02-01A - Power Distribution Interface

**Document ID:** 61-00-05-02-01A  
**Title:** Power Distribution Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the high-voltage DC power distribution interface between the aircraft electrical system (ATA 24) and the Q100 propulsor units. This interface provides up to 4.5 MW of electrical power per propulsor for electric motor operation.

---

## 2. Scope

This specification covers:
- 800 VDC power bus interface
- Power connector specifications
- Cable routing and segregation requirements
- Power quality and transient protection
- Emergency disconnect provisions

### 2.1 Applicable Units
- All four Q100 propulsor units
- Primary and redundant power feeds

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements document |
| ICD-24-61 | Electrical Power Interface Control Document | ATA 24 interface |
| [SAE AS6968](https://www.sae.org/standards/content/as6968/) | High-Voltage Aerospace Applications | High-voltage standards |
| [MIL-STD-1399](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35823) | Interface Standard for Shipboard Systems | Power quality |
| [DO-160G Section 16](https://www.rtca.org/content/standards-guidance-materials) | Power Input | Environmental standards |

---

## 4. Interface Description

### 4.1 Physical Characteristics

| Parameter | Value | Tolerance | Unit | Notes |
|-----------|-------|-----------|------|-------|
| Nominal Bus Voltage | 800 | ±10% | VDC | Operating range: 720-880 VDC |
| Maximum Continuous Power | 4.5 | — | MW | Per propulsor |
| Peak Power (30 sec) | 5.5 | — | MW | Transient capability |
| Connector Type | MIL-DTL-38999 Series III | — | — | High-current circular |
| Connector Shell Size | 25 | — | — | — |
| Number of Power Contacts | 4 | — | — | 2× positive, 2× negative |
| Contact Current Rating | 150 | — | A | Per contact |
| Cable Type | MIL-DTL-27500 shielded | — | — | High-voltage rated |
| Cable Gauge | 2 AWG | — | — | Per conductor |
| Cable Shielding | Braided shield >85% coverage | — | — | EMI protection |

### 4.2 Functional Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| PWR-61-001 | Steady-state voltage | 800 ±10% VDC | Test |
| PWR-61-002 | Maximum voltage ripple | <5% RMS | Test |
| PWR-61-003 | Maximum continuous current | 5,625 A (at 800V) | Test |
| PWR-61-004 | Peak current (30 sec) | 6,875 A | Test |
| PWR-61-005 | Voltage transient (surge) | <1,200 V for <50 μs | Test |
| PWR-61-006 | Inrush current limiting | <200 A/ms | Test, Design |
| PWR-61-007 | Ground fault detection | <100 ms detection time | Test |
| PWR-61-008 | Isolation resistance | >10 MΩ to ground | Test |
| PWR-61-009 | Emergency disconnect time | <20 ms | Test |
| PWR-61-010 | Power factor | >0.95 | Test |
| PWR-61-011 | Contact resistance | <1 mΩ per contact | Inspection |

### 4.3 Environmental Constraints

| Parameter | Operating Range | Survival Range | Unit | Notes |
|-----------|----------------|----------------|------|-------|
| Temperature (connector) | -40 to +125 | -55 to +150 | °C | Per MIL-DTL-38999 |
| Altitude | 0 to 45,000 | 0 to 50,000 | ft | Altitude derating |
| Vibration | 10g RMS | 20g peak | g | Per DO-160G Category T |
| Humidity | 0 to 95% | — | % RH | Non-condensing |
| Voltage Withstand | 2,400 | — | VDC | 3× nominal for 1 minute |

---

## 5. Interface Control

### 5.1 Electrical Interface Parameters

| Parameter | Specification | Test Method |
|-----------|---------------|-------------|
| DC resistance (cable + connectors) | <10 mΩ total | 4-wire measurement |
| Inductance (cable loop) | <5 μH | LCR meter |
| Capacitance (line-to-ground) | <1,000 pF/m | LCR meter |
| Shield effectiveness | >40 dB at 1 MHz | Transfer impedance |

### 5.2 Connector Pinout

| Pin | Function | Wire Gauge | Notes |
|-----|----------|------------|-------|
| A, B | Positive (+800V) | 2 AWG × 2 | Paralleled for current capacity |
| C, D | Negative (0V/Return) | 2 AWG × 2 | Paralleled for current capacity |
| E | Protective Earth (PE) | 6 AWG | Safety ground |
| F, G | Shield/Chassis Ground | 10 AWG | EMI shield continuity |
| H | Power Good Signal | 22 AWG | Logic-level status |
| J | Emergency Disconnect | 22 AWG | Discrete command |

### 5.3 Cable Routing Requirements

| Requirement | Specification |
|-------------|---------------|
| Separation from fuel lines | ≥50 mm minimum |
| Separation from flight control cables | ≥100 mm minimum |
| Shielding continuity | <10 mΩ end-to-end |
| Bend radius | ≥10× cable diameter |
| Support spacing | ≤300 mm between clamps |
| Chafe protection | Required at all bulkheads and pass-throughs |
| Identification | Per MIL-STD-130N marking |

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| PWR-T-001 | Voltage drop test | <10 mΩ total resistance | 4-wire measurement at max current |
| PWR-T-002 | Power quality measurement | Ripple <5% RMS | Oscilloscope, FFT analysis |
| PWR-T-003 | Transient immunity | No malfunction with 1200V/50μs pulse | Surge generator per DO-160G |
| PWR-T-004 | Ground fault detection | Detection <100 ms | Fault injection test |
| PWR-T-005 | Emergency disconnect | <20 ms from command to power off | High-speed data acquisition |
| PWR-T-006 | Thermal test (connectors) | Temperature rise <50°C at max current | Thermal imaging |
| PWR-T-007 | Dielectric withstand | 2,400 VDC for 60 seconds, no breakdown | Hipot tester |
| PWR-T-008 | Insulation resistance | >10 MΩ at 500 VDC | Megohmmeter |

### 6.2 Production Verification

| Inspection | Frequency | Method |
|------------|-----------|--------|
| Continuity test (all conductors) | 100% | Multimeter |
| Insulation resistance | 100% | Megohmmeter (500 VDC) |
| Contact resistance | 100% | Micro-ohmmeter |
| Pin retention force | 10% (sampling) | Pull test per MIL-DTL-38999 |
| Shield continuity | 100% | Multimeter |
| Dielectric withstand | 100% | Hipot test (1,600 VDC, 1 sec) |
| Visual inspection | 100% | Workmanship, damage, contamination |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 24](../../../../E-ELECTRICAL/ATA_24-ELECTRICAL_POWER/README.md) — Electrical Power (power source)
- [ATA 92](../../../../ATA_92-ELECTRICAL_INSTALLATION/README.md) — Electrical Installation (wiring practices)
- [ATA 20](../../../../ATA_20-STANDARD_PRACTICES/README.md) — Standard Practices (connector installation)

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

### 7.3 Related Documents
- 61-00-05-02-04A — Grounding and Bonding
- 61-00-05-06-02A — ICD Propulsion to Avionics

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Parent: 61-00-05_Interfaces](../README.md) · [Next: 61-00-05-02-02A_Control_Signals](61-00-05-02-02A_Control_Signals.md) →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Electrical Interfaces  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
