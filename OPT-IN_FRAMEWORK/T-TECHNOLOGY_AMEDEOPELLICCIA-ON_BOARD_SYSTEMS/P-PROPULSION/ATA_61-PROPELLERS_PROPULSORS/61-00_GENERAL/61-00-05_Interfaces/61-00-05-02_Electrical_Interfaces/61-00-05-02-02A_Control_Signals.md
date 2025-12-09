# 61-00-05-02-02A - Control Signals Interface

**Document ID:** 61-00-05-02-02A  
**Title:** Control Signals Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the discrete and analog control signal interfaces between the flight control system (ATA 27) and the Q100 propulsor control units. These signals enable thrust command, mode selection, and safety interlocks.

---

## 2. Scope

This specification covers:
- Discrete control inputs and outputs
- Analog control signals
- Signal voltage levels and timing
- Fault detection and fail-safe modes
- Redundancy management

### 2.1 Applicable Units
- All four Q100 propulsor units
- Primary and redundant control channels

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements document |
| ICD-27-61 | Flight Controls Interface Control Document | Flight control interface |
| [SAE AS5643](https://www.sae.org/standards/content/as5643/) | Discrete Signals for Avionics Systems | Discrete signal standard |
| [ARINC 429](https://www.aviation-ia.com/arinc-429/) | Mark 33 Digital Information Transfer System | Data bus (reference) |
| [DO-254](https://www.rtca.org/content/standards-guidance-materials) | Hardware Design Assurance | Development standard |

---

## 4. Interface Description

### 4.1 Physical Characteristics

| Parameter | Value | Tolerance | Unit | Notes |
|-----------|-------|-----------|------|-------|
| Connector Type | MIL-DTL-38999 Series III | — | — | Size 17 |
| Number of Discrete I/O | 24 | — | — | 16 inputs, 8 outputs |
| Number of Analog Inputs | 4 | — | — | 0-5V, 0-10V ranges |
| Discrete Logic Level | 28 VDC (nominal) | — | — | Cockpit/avionics bus |
| Discrete High Level | 22-30 | — | VDC | Logic "1" |
| Discrete Low Level | 0-5 | — | VDC | Logic "0" |
| Current Sink/Source (Discrete) | 50 | ±5 | mA | Per signal |
| Wire Gauge (Discrete) | 22 AWG | — | — | Twisted, shielded pairs |
| Wire Gauge (Analog) | 20 AWG | — | — | Shielded pairs |

### 4.2 Functional Requirements

#### 4.2.1 Discrete Input Signals (to Propulsor)

| Signal Name | Source | Function | Logic High | Logic Low |
|-------------|--------|----------|-----------|-----------|
| ENABLE_CMD | Flight Control Computer | Propulsor enable command | Enabled | Disabled |
| MODE_SELECT_1 | Flight Control Computer | Operating mode bit 1 | — | — |
| MODE_SELECT_2 | Flight Control Computer | Operating mode bit 2 | — | — |
| EMERG_SHUTDOWN | Safety System | Emergency shutdown | Shutdown | Normal |
| REVERSE_THRUST_ARM | Pilot Command | Reverse thrust arming | Armed | Disarmed |
| REVERSE_THRUST_CMD | Pilot Command | Reverse thrust command | Reverse | Forward |
| SYNC_PULSE | Flight Control Computer | Synchronization pulse | — | — |
| FAULT_RESET | Maintenance Panel | Fault latch reset | Reset | Normal |

#### 4.2.2 Discrete Output Signals (from Propulsor)

| Signal Name | Destination | Function | Logic High | Logic Low |
|-------------|-------------|----------|-----------|-----------|
| READY_STATUS | Flight Control Computer | Propulsor ready | Ready | Not ready |
| FAULT_STATUS | Flight Control Computer | Fault detected | Fault | Normal |
| OVERSPEED_ALERT | Flight Control Computer | Overspeed condition | Overspeed | Normal |
| OVERTEMP_ALERT | Flight Control Computer | Overtemperature condition | Overtemp | Normal |
| POWER_GOOD | Flight Control Computer | Power supply status | Good | Fail |
| BRAKE_ENGAGED | Flight Control Computer | Propulsor brake status | Engaged | Released |

#### 4.2.3 Analog Input Signals

| Signal Name | Range | Accuracy | Function |
|-------------|-------|----------|----------|
| THRUST_CMD_ANALOG | 0-10 V | ±0.5% FS | Backup analog thrust command |
| BLADE_PITCH_CMD | 0-5 V | ±1.0% FS | Variable pitch command (future) |
| TORQUE_LIMIT | 0-10 V | ±1.0% FS | External torque limit |
| TEMP_LIMIT | 0-5 V | ±2.0% FS | External temperature limit |

### 4.3 Timing Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| CTL-61-001 | Discrete input response time | <5 ms | Test |
| CTL-61-002 | Discrete output update rate | 100 Hz (10 ms) | Test |
| CTL-61-003 | Analog input sampling rate | ≥1 kHz | Design review |
| CTL-61-004 | Analog input conversion time | <1 ms | Test |
| CTL-61-005 | Signal debounce time | 10 ms | Design feature |
| CTL-61-006 | Emergency shutdown response | <10 ms from signal to power cutoff | Test |

### 4.4 Environmental Constraints

| Parameter | Operating Range | Survival Range | Unit | Notes |
|-----------|----------------|----------------|------|-------|
| Temperature | -40 to +85 | -55 to +125 | °C | Per DO-160G |
| Vibration | 10g RMS | 20g peak | g | Per DO-160G Category T |
| EMI Susceptibility | Per DO-160G Category M | — | — | High intensity fields |

---

## 5. Interface Control

### 5.1 Discrete Signal Electrical Specifications

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| Input High Voltage (VIH) | 11 | 28 | 30 | V | Logic "1" threshold |
| Input Low Voltage (VIL) | 0 | — | 5 | V | Logic "0" threshold |
| Output High Voltage (VOH) | 22 | 28 | 30 | V | At 50 mA sink |
| Output Low Voltage (VOL) | 0 | — | 1 | V | At 50 mA source |
| Input Impedance | 5 | 10 | — | kΩ | Per input |
| Output Current | 40 | 50 | 60 | mA | Per output |

### 5.2 Analog Signal Specifications

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| Input Voltage Range (0-10V signals) | 0 | — | 10 | V | — |
| Input Voltage Range (0-5V signals) | 0 | — | 5 | V | — |
| Input Impedance | 50 | 100 | — | kΩ | High-impedance |
| Resolution | 12 | — | — | bits | ADC resolution |
| Absolute Accuracy | — | — | ±0.5 | % FS | Including all errors |
| Linearity | — | — | ±0.2 | % FS | INL |
| Common-Mode Rejection | 60 | — | — | dB | At 50/60 Hz |

### 5.3 Connector Pinout

| Pin | Signal Name | Type | Direction | Notes |
|-----|-------------|------|-----------|-------|
| A | ENABLE_CMD | Discrete | Input | — |
| B | MODE_SELECT_1 | Discrete | Input | — |
| C | MODE_SELECT_2 | Discrete | Input | — |
| D | EMERG_SHUTDOWN | Discrete | Input | Safety-critical |
| E | REVERSE_THRUST_ARM | Discrete | Input | — |
| F | REVERSE_THRUST_CMD | Discrete | Input | — |
| G | SYNC_PULSE | Discrete | Input | — |
| H | FAULT_RESET | Discrete | Input | — |
| J | READY_STATUS | Discrete | Output | — |
| K | FAULT_STATUS | Discrete | Output | — |
| L | OVERSPEED_ALERT | Discrete | Output | — |
| M | OVERTEMP_ALERT | Discrete | Output | — |
| N | POWER_GOOD | Discrete | Output | — |
| P | BRAKE_ENGAGED | Discrete | Output | — |
| R | THRUST_CMD_ANALOG+ | Analog | Input | Differential |
| S | THRUST_CMD_ANALOG- | Analog | Input | Differential |
| T | TORQUE_LIMIT+ | Analog | Input | Differential |
| U | TORQUE_LIMIT- | Analog | Input | Differential |
| V | SIGNAL_GROUND | Ground | — | Common reference |
| W | CHASSIS_GROUND | Ground | — | Shield/chassis |

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| CTL-T-001 | Discrete input threshold | VIH > 11V, VIL < 5V | Bench test, voltage sweep |
| CTL-T-002 | Discrete output levels | VOH > 22V at 50mA, VOL < 1V at 50mA | Load test |
| CTL-T-003 | Response time (discrete) | <5 ms from input transition to output | Oscilloscope |
| CTL-T-004 | Analog input accuracy | ±0.5% FS over full range | Precision source, DMM |
| CTL-T-005 | Emergency shutdown timing | <10 ms from EMERG_SHUTDOWN to power off | High-speed DAQ |
| CTL-T-006 | EMI susceptibility | No false triggers per DO-160G Category M | EMI chamber |
| CTL-T-007 | Signal isolation | >10 MΩ between circuits | Megohmmeter |

### 6.2 Production Verification

| Inspection | Frequency | Method |
|------------|-----------|--------|
| Continuity (all signals) | 100% | Multimeter, automated test |
| Signal-to-ground resistance | 100% | Megohmmeter |
| Discrete I/O functional test | 100% | Automated test fixture |
| Analog input calibration | 100% | Precision source, readback |
| Pin retention | 10% (sampling) | Pull test |
| Visual inspection | 100% | Workmanship |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 27](../../../../F-FLIGHT_CONTROLS/ATA_27-FLIGHT_CONTROLS/README.md) — Flight Controls (signal source)
- [ATA 31](../../../../ATA_31-INDICATING_RECORDING/README.md) — Indicating and Recording Systems
- [ATA 22](../../../../F-FLIGHT_CONTROLS/ATA_22-AUTO_FLIGHT/README.md) — Auto Flight (mode commands)

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

### 7.3 Related Documents
- 61-00-05-02-03A — Sensor Connections
- 61-00-05-03-03A — Discrete Signals (data bus interface)

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Previous: 61-00-05-02-01A_Power_Distribution](61-00-05-02-01A_Power_Distribution.md) · [Next: 61-00-05-02-03A_Sensor_Connections](61-00-05-02-03A_Sensor_Connections.md) →

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
