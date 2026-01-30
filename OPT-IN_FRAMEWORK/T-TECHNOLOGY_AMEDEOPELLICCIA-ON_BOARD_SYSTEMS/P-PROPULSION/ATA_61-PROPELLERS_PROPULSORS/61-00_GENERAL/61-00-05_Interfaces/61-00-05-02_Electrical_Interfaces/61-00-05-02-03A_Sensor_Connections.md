# 61-00-05-02-03A - Sensor Connections Interface

**Document ID:** 61-00-05-02-03A  
**Title:** Sensor Connections Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the electrical interface for propulsor health monitoring sensors including temperature, vibration, speed, position, and current sensors. These interfaces provide real-time data for condition monitoring and diagnostics.

---

## 2. Scope

This specification covers:
- Temperature sensor interfaces (thermocouples, RTDs)
- Vibration sensor interfaces (accelerometers)
- Speed sensor interfaces (tachometers, encoders)
- Current and voltage sensor interfaces
- Signal conditioning requirements

### 2.1 Applicable Units
- All four Q100 propulsor units
- Multiple sensors per propulsor

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements document |
| [IEC 60751](https://webstore.iec.ch/publication/3426) | Industrial Platinum Resistance Thermometers | RTD standard |
| [ANSI MC96.1](https://webstore.ansi.org/) | Temperature Measurement Thermocouples | Thermocouple standard |
| [ISO 10816](https://www.iso.org/standard/63180.html) | Mechanical Vibration — Evaluation of Machine Vibration | Vibration monitoring |

---

## 4. Interface Description

### 4.1 Temperature Sensors

#### 4.1.1 RTD Sensors (Motor Windings)

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Sensor Type | Pt100 (Class A) | — | 3-wire configuration |
| Temperature Range | -50 to +200 | °C | Extended range |
| Accuracy | ±(0.15 + 0.002×|t|) | °C | Per IEC 60751 |
| Excitation Current | 1 | mA | Constant current source |
| Wire Gauge | 24 AWG | — | Shielded, twisted triplet |
| Number per Propulsor | 6 | — | Phase windings + bearings |

#### 4.1.2 Thermocouples (Gas Path, if applicable)

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Sensor Type | Type K | — | Chromel-Alumel |
| Temperature Range | 0 to +1,200 | °C | High-temp measurement |
| Accuracy | ±2.2°C or ±0.75% | — | Whichever is greater |
| Wire Gauge | 24 AWG | — | Thermocouple extension wire |
| Number per Propulsor | 4 | — | Duct exit temperature |

### 4.2 Vibration Sensors

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Sensor Type | Piezoelectric accelerometer | — | IEPE (ICP) type |
| Sensitivity | 100 | mV/g | Nominal |
| Frequency Range | 1 to 10,000 | Hz | Broadband |
| Measurement Range | ±50 | g peak | Wide dynamic range |
| Supply Voltage | 18-30 | VDC | Constant current (4 mA) |
| Output Impedance | <100 | Ω | Low impedance |
| Cable Type | Low-noise coaxial | — | BNC or M12 connector |
| Number per Propulsor | 3 | — | Axial, radial ×2 |

### 4.3 Speed Sensors

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Sensor Type | Variable reluctance (VR) | — | Magnetic pickup |
| Target | 60-tooth gear | — | On motor shaft |
| Air Gap | 0.5-1.5 | mm | Nominal |
| Output Voltage | 5-30 | VAC RMS | At rated speed |
| Frequency Range | 0 to 3,600 | Hz | 0-3,600 rpm |
| Wire Gauge | 22 AWG | — | Twisted, shielded pair |
| Number per Propulsor | 2 | — | Redundant channels |

### 4.4 Current/Voltage Sensors

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Current Sensor Type | Hall-effect | — | Closed-loop |
| Current Range | 0 to ±7,500 | A | Per phase |
| Accuracy | ±0.5 | % FS | At 25°C |
| Bandwidth | DC to 100 | kHz | High-frequency capable |
| Output | 0-10 | V | Analog output |
| Isolation Voltage | 2,500 | VDC | Primary-secondary |
| Number per Propulsor | 3 | — | One per motor phase |

### 4.5 Position Sensors (Brake, Future Variable Pitch)

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Sensor Type | LVDT (Linear Variable Differential Transformer) | — | — |
| Stroke Range | ±25 | mm | Brake position |
| Linearity | ±0.5 | % FS | — |
| Excitation | 5 V, 5 kHz | — | AC excitation |
| Output | ±10 | VDC | Proportional to position |
| Number per Propulsor | 2 | — | Brake + future use |

---

## 5. Interface Control

### 5.1 Signal Conditioning Requirements

| Sensor Type | Conditioning | ADC Resolution | Sampling Rate |
|-------------|--------------|----------------|---------------|
| RTD (Pt100) | 3-wire bridge, cold junction compensation | 16-bit | 10 Hz |
| Thermocouple | Cold junction compensation, linearization | 16-bit | 10 Hz |
| Accelerometer | AC coupling, anti-aliasing filter | 16-bit | 25.6 kHz |
| Tachometer | Schmitt trigger, frequency-to-voltage | 16-bit | 10 kHz |
| Current sensor | Differential input, isolation amplifier | 16-bit | 100 kHz |
| LVDT | Demodulator, low-pass filter | 16-bit | 1 kHz |

### 5.2 Connector Specifications

| Sensor Type | Connector Type | Shell Size | Number of Pins |
|-------------|----------------|------------|----------------|
| RTD | MIL-DTL-38999 Series III | 11 | 18 (6 sensors × 3 wires) |
| Thermocouple | MIL-DTL-38999 Series III | 9 | 8 (4 sensors × 2 wires) |
| Accelerometer | M12 × 1 circular | 4-pin | 4 (per sensor) |
| Tachometer | MIL-DTL-38999 Series III | 9 | 4 (2 sensors × 2 wires) |
| Current sensor | Integral to sensor | — | — |
| LVDT | MIL-DTL-38999 Series III | 9 | 12 (2 sensors × 6 wires) |

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| SEN-T-001 | RTD accuracy verification | ±0.15°C at reference temps | Calibration bath |
| SEN-T-002 | Thermocouple accuracy | ±2.2°C or ±0.75% | Calibration furnace |
| SEN-T-003 | Accelerometer calibration | ±5% sensitivity | Vibration calibrator |
| SEN-T-004 | Tachometer accuracy | ±0.1% of reading | Reference tachometer |
| SEN-T-005 | Current sensor accuracy | ±0.5% FS | Precision current source |
| SEN-T-006 | LVDT linearity | ±0.5% FS | Position reference |
| SEN-T-007 | Signal-to-noise ratio | >60 dB | Spectrum analyzer |

### 6.2 Production Verification

| Inspection | Frequency | Method |
|------------|-----------|--------|
| Sensor calibration certificate | 100% | Review calibration data |
| Wiring continuity | 100% | Multimeter |
| Insulation resistance | 100% | Megohmmeter (500 VDC) |
| Shield continuity | 100% | Multimeter |
| Functional test (sensor output) | 100% | Automated test fixture |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 45](../../../../ATA_45-CENTRAL_MAINTENANCE_SYSTEM/README.md) — Central Maintenance System (data consumers)
- [ATA 31](../../../../ATA_31-INDICATING_RECORDING/README.md) — Indicating and Recording
- [ATA 77](../../../../ATA_77-ENGINE_INDICATING/README.md) — Engine Indicating

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

### 7.3 Related Documents
- 61-00-05-03-01A — ARINC 429 Buses (data transmission)
- 61-00-05-02-04A — Grounding and Bonding

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Previous: 61-00-05-02-02A_Control_Signals](61-00-05-02-02A_Control_Signals.md) · [Next: 61-00-05-02-04A_Grounding_Bonding](61-00-05-02-04A_Grounding_Bonding.md) →

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
