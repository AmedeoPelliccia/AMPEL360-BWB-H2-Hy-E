# 95-20-27-008 — Integration with ATA 27 and ATA 42 FCS

**Document ID:** 95-20-27-008  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active

---

## 1. Purpose

This document describes the integration of the FCS_NN subsystem (95-20-27) with the primary Flight Control System (ATA 27) and Integrated Modular Avionics platform (ATA 42).

---

## 2. Architecture Overview

### 2.1 Integration Layers

```
┌─────────────────────────────────────────────────────┐
│           Pilot Interface (Sticks, MCP)            │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│   Flight Management System (FMS) / Autopilot       │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│  Flight Path Stabilization NN (95-20-27-006)       │
│  • Outer Loop: Trajectory Tracking                 │
│  • Outputs: Rate Commands (p, q, r, T)             │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│  Control Surface Optimizer NN (95-20-27-003)       │
│  • Inner Loop: Rate Control + Optimization         │
│  • Inputs: Aero Predictor (95-20-27-002)           │
│  • Overlays: GLA (95-20-27-004), Trim (95-20-27-007)│
│  • Protection: Envelope (95-20-27-005)             │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│           ATA 27 Flight Control Computer           │
│  • Surface Command Distribution                    │
│  • Actuator Control Laws                           │
│  • Redundancy Management                           │
│  • Built-In Test (BIT)                             │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│        Control Surface Actuators (Hydraulic)       │
│  • Elevators, Ailerons, Rudders, Flaps, Spoilers   │
└─────────────────────────────────────────────────────┘
```

### 2.2 Data Flow

**Sensor Inputs** → **Aero Predictor** → **Control Surface Optimizer** → **ATA 27 FCC** → **Actuators**

**Pilot Commands** → **Flight Path Stabilization** → **Control Surface Optimizer**

---

## 3. ATA 27 Integration Points

### 3.1 Input Interfaces from ATA 27

| Data | Source | Bus | Rate | Encoding |
|------|--------|-----|------|----------|
| Air Data (α, β, V, M, h) | Air Data Computer | ARINC 429 | 20 Hz | BNR |
| Inertial Data (p, q, r, a_x, a_y, a_z) | IRU | ARINC 429 | 100 Hz | BNR |
| Attitude (φ, θ, ψ) | AHRS | ARINC 429 | 50 Hz | BNR |
| Control Surface Positions | LVDT Sensors | AFDX | 100 Hz | Engineering Units |
| Hydraulic Pressure | Hydraulic Sensors | AFDX | 10 Hz | Engineering Units |
| Pilot Stick Inputs | Sidestick Controllers | AFDX | 100 Hz | Engineering Units |
| Autopilot Commands | FMS/AFDS | AFDX | 20 Hz | Engineering Units |

### 3.2 Output Interfaces to ATA 27

| Data | Destination | Bus | Rate | Encoding |
|------|-------------|-----|------|----------|
| Elevator Commands (δe_L, δe_R) | FCC | AFDX | 100 Hz | Engineering Units |
| Aileron Commands (δa_L, δa_R) | FCC | AFDX | 100 Hz | Engineering Units |
| Rudder Commands (δr_L, δr_R) | FCC | AFDX | 100 Hz | Engineering Units |
| Flap Commands (δf_L, δf_R) | FCC | AFDX | 20 Hz | Engineering Units |
| Spoiler Commands | FCC | AFDX | 100 Hz | Engineering Units |
| FCS_NN Status | FCC | AFDX | 10 Hz | Discrete |
| FCS_NN Health | FCC | AFDX | 1 Hz | Discrete + BIT word |

### 3.3 Mode Coordination

| ATA 27 Mode | FCS_NN Behavior | Authority |
|-------------|-----------------|-----------|
| Direct Law | FCS_NN bypassed | 0% |
| Alternate Law | Envelope Protection only | 30% |
| Normal Law | Full NN active | 100% |
| Degraded | Reduced optimization | 50% |

---

## 4. ATA 42 Integration (IMA Platform)

### 4.1 Compute Partition Allocation

The FCS_NN models execute on dedicated IMA partitions managed by 95-20-42:

| Model | Partition | MIPS | Memory | Update Rate | Priority |
|-------|-----------|------|--------|-------------|----------|
| Aero Predictor | FCS_NN_P1 | 150 | 8 MB | 100 Hz | High |
| Control Surface Optimizer | FCS_NN_P2 | 300 | 16 MB | 100 Hz | Critical |
| Gust Load Alleviation | FCS_NN_P3 | 120 | 12 MB | 100 Hz | High |
| Envelope Protection | FCS_NN_P4 | 80 | 10 MB | 100 Hz | Critical |
| Flight Path Stabilization | FCS_NN_P5 | 200 | 14 MB | 10 Hz | Medium |
| Trim Optimizer | FCS_NN_P6 | 50 | 8 MB | 0.1 Hz | Low |

**Total Resource Allocation**: 900 MIPS, 68 MB RAM

### 4.2 Partition Communication

- **Inter-Partition Communication**: AFDX Virtual Links
- **Latency Budget**: <2ms (deterministic)
- **Bandwidth**: 100 Mbps per partition
- **Isolation**: ARINC 653 time and space partitioning

### 4.3 Partition Monitoring

Each partition implements:
- **Watchdog Timer**: 10ms timeout
- **Stack Overflow Detection**: Hardware and software guards
- **Memory Protection**: MMU enforcement
- **Health Monitoring**: Periodic BIT

---

## 5. Interface Specifications

### 5.1 ARINC 429 Interface

**Air Data (Label 206)**:
```
Word 1: α (deg) - BNR, ±180°, resolution 0.01°
Word 2: β (deg) - BNR, ±180°, resolution 0.01°
Word 3: V_TAS (kt) - BNR, 0-500 kt, resolution 0.1 kt
Word 4: M - BNR, 0-1.0, resolution 0.001
Word 5: h (ft) - BNR, -1000 to 50000 ft, resolution 1 ft
```

**Inertial Data (Label 324)**:
```
Word 1: p (deg/s) - BNR, ±180°/s, resolution 0.01°/s
Word 2: q (deg/s) - BNR, ±180°/s, resolution 0.01°/s
Word 3: r (deg/s) - BNR, ±180°/s, resolution 0.01°/s
Word 4: a_x (g) - BNR, ±4g, resolution 0.001g
Word 5: a_y (g) - BNR, ±4g, resolution 0.001g
Word 6: a_z (g) - BNR, ±4g, resolution 0.001g
```

### 5.2 AFDX Interface

**Control Surface Commands (VL_FCS_CMD)**:
```yaml
VL_ID: 0x1234
BAG: 10 ms
Payload:
  - Elevator_L: float32 (deg)
  - Elevator_R: float32 (deg)
  - Aileron_L: float32 (deg)
  - Aileron_R: float32 (deg)
  - Rudder_L: float32 (deg)
  - Rudder_R: float32 (deg)
  - Flap_L: float32 (deg)
  - Flap_R: float32 (deg)
  - Spoiler_L: float32 (deg)
  - Spoiler_R: float32 (deg)
  - Validity: uint8 (bitmask)
  - Sequence: uint16
```

**FCS_NN Status (VL_FCS_NN_STATUS)**:
```yaml
VL_ID: 0x1235
BAG: 100 ms
Payload:
  - Mode: uint8 (Normal/Degraded/Inactive)
  - Aero_Predictor_Health: uint8 (0-100%)
  - Control_Optimizer_Health: uint8 (0-100%)
  - GLA_Health: uint8 (0-100%)
  - Envelope_Protection_Health: uint8 (0-100%)
  - Flight_Path_Stab_Health: uint8 (0-100%)
  - Trim_Optimizer_Health: uint8 (0-100%)
  - BIT_Word: uint32
  - Fault_Count: uint16
```

Full specifications: `ASSETS/Interface_Specs/95-20-27-A-401_ATA_27_FCS_Interface_Spec.yaml`

---

## 6. Redundancy and Fault Tolerance

### 6.1 Redundancy Architecture

- **Primary FCS**: ATA 27 Flight Control Computer (Triplex)
- **FCS_NN Models**: Dual redundant (independent inference)
- **Voting**: 2-out-of-2 for NN outputs (if disagreement, fallback to conventional)
- **Monitoring**: Cross-channel comparison with <5% tolerance

### 6.2 Failure Modes

| Failure | Detection | Response | Crew Alert |
|---------|-----------|----------|------------|
| Model Inference Timeout | Watchdog | Fallback to conventional FCS | EICAS Caution |
| Model Output Disagreement | Cross-check | Use conventional FCS | EICAS Caution |
| Sensor Failure | BIT + Reasonableness | Reconfigure with remaining sensors | ECAM Alert |
| IMA Partition Failure | Health Monitor | Restart partition or disable NN | EICAS Warning |
| Actuator Failure | Position feedback | Reconfigure control allocation | ECAM Alert |

### 6.3 Graceful Degradation Path

```
Normal Law (Full NN)
    ↓ (NN failure)
Alternate Law (Envelope Protection only)
    ↓ (Further failure)
Direct Law (Conventional FCS)
    ↓ (FCC failure)
Mechanical Backup (if available)
```

---

## 7. Built-In Test (BIT)

### 7.1 Continuous BIT (CBIT)

Executed every cycle (10ms):
- **Inference Latency Check**: <10ms threshold
- **Output Range Check**: Within expected bounds
- **Memory Integrity**: CRC check on model weights
- **Watchdog Kick**: Confirm partition alive

### 7.2 Power-On BIT (PBIT)

Executed at startup:
- **Model Load Verification**: CRC on ONNX files
- **Test Inference**: Known input → expected output
- **Interface Check**: Loopback on AFDX/ARINC 429
- **Partition Resources**: Memory, CPU allocation

### 7.3 Maintenance BIT (MBIT)

Triggered by maintenance crew:
- **Full Model Validation**: Extended test suite
- **Actuator Sweep**: Full range check
- **Sensor Calibration Check**: Compare to reference
- **Log Download**: Event and performance logs

---

## 8. Latency Budget

### 8.1 End-to-End Latency

| Stage | Latency | Cumulative |
|-------|---------|------------|
| Sensor Sampling | 1 ms | 1 ms |
| ARINC 429 / AFDX Transmission | 2 ms | 3 ms |
| Aero Predictor Inference | 3 ms | 6 ms |
| Control Optimizer Inference | 6 ms | 12 ms |
| Envelope Protection Check | 3 ms | 15 ms |
| Command Transmission to FCC | 2 ms | 17 ms |
| Actuator Response | 20 ms | 37 ms |

**Total Latency (Pilot Input → Surface Motion)**: 37 ms

**Requirement**: <50 ms (MET)

### 8.2 Latency Monitoring

Real-time tracking:
- **Average Latency**: Rolling window (1 second)
- **Maximum Latency**: Peak over 10 seconds
- **Timeout Events**: Count of >50ms latencies
- **Performance Alerts**: If average >40ms for >5 seconds

---

## 9. Certification Considerations

### 9.1 DO-178C Compliance

- **Software Level**: Level A (DAL-A)
- **Requirements Traceability**: All requirements traced to tests
- **Code Coverage**: 100% MC/DC coverage
- **Model Verification**: ONNX model validated against training

### 9.2 DO-254 Compliance (IMA Hardware)

- **Hardware Level**: Level A
- **FPGA Verification**: Formal verification of partition isolation
- **Resource Budgets**: Proven worst-case execution time (WCET)

### 9.3 ARP-4754A (System Level)

- **Safety Assessment**: Fault Tree Analysis, FMEA
- **Functional Hazard Assessment**: All failure modes analyzed
- **Common Cause Analysis**: Independence of redundant channels

---

## 10. Testing and Validation

### 10.1 Iron Bird Testing

- **Duration**: 500 hours HIL testing
- **Scenarios**: All flight phases, failures, edge cases
- **Integration**: Real FCC, actuators, sensors
- **Results**: `ASSETS/Test_Data/95-20-27-A-303_IronBird_Validation_Results.xlsx`

### 10.2 Flight Test

- **Duration**: 100 hours in-flight validation
- **Test Aircraft**: AMPEL360 Prototype
- **Envelope**: Full flight envelope explored
- **Results**: `ASSETS/Test_Data/95-20-27-A-302_Flight_Test_Results.csv`

---

## 11. Interface Specification Files

Complete interface specifications available in:
- `ASSETS/Interface_Specs/95-20-27-A-401_ATA_27_FCS_Interface_Spec.yaml`
- `ASSETS/Interface_Specs/95-20-27-A-402_ATA_42_IMA_Interface.yaml`
- `ASSETS/Interface_Specs/95-20-27-A-403_Sensor_and_Bus_Input_Specs.yaml`
- `ASSETS/Interface_Specs/95-20-27-A-404_Actuator_Command_Output_Specs.yaml`

---

## 12. References

- [95-20-27-001_FCS_NN_Overview.md](95-20-27-001_FCS_NN_Overview.md)
- [95-20-42 NN IMA Integration](../95-20-42_NN_IMA_Integration/)
- ARINC 429 Specification
- ARINC 653 Specification (APEX)
- ARINC 664 Part 7 (AFDX)
- DO-178C: Software Considerations in Airborne Systems
- DO-254: Design Assurance Guidance for Airborne Electronic Hardware

---

## Document Control

- **Owner**: AMPEL360 FCS_NN Team
- **Version**: 1.0
- **Status**: Active
- **Classification**: Technical Reference
- **Last Updated**: 2025-11-17
