# 95-00-05-03-006 ATA 28 Fuel System Interface

**Document ID:** 95-00-05-03-006
**Title:** ATA 28 H2 Fuel System Interface
**Version:** 1.1.0
**Status:** ACTIVE
**Date:** 2025-11-12

---

## Interface Attributes

| Attribute | Value |
|-----------|-------|
| **Category** | SYSTEM |
| **Type** | System Interface (H2 Fuel) |
| **Protocol** | ARINC 825 (CAN Bus) |
| **Criticality** | DAL B |
| **Direction** | Bidirectional |
| **Owner** | Systems Integration Team |
| **Stakeholders** | AI/ML Team, Fuel Systems, Safety Engineering |

---

## 1. Introduction

### 1.1 Purpose

This document specifies the interface between the AI/ML system and the hydrogen (H2) fuel system (ATA 28) for the AMPEL360 BWB H2-Hy-E aircraft.

### 1.2 Scope

**Input (Fuel System → AI/ML):**
- H2 pressure, temperature, flow rate, tank levels
- Valve positions and leak detection status
- Fuel system health and fault codes

**Output (AI/ML → Fuel System):**
- Leak probability predictions
- Consumption forecasts
- Anomaly alerts
- Maintenance recommendations

---

## 2. System Context

```
┌──────────────────────────────────────────────────────────┐
│            ATA 28 - H2 Fuel System                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │  Tank 1  │  │  Tank 2  │  │  Tank 3  │  │  Tank 4  │ │
│  │ Sensors  │  │ Sensors  │  │ Sensors  │  │ Sensors  │ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘ │
│       │             │              │              │       │
│  ┌────┴─────────────┴──────────────┴──────────────┴────┐ │
│  │          Fuel System Controller (FSC)                │ │
│  │               ARINC 825 (CAN)                        │ │
│  └────────────────────────┬──────────────────────────────┘│
└───────────────────────────┼───────────────────────────────┘
                            │
                            │ CAN Bus (250 kbps)
                            │
┌───────────────────────────▼───────────────────────────────┐
│              AI/ML Edge Compute Platform                   │
│  ┌──────────────────────────────────────────────────────┐ │
│  │  Data Ingestion → Feature Engineering → Inference   │ │
│  └────────────────────────┬──────────────────────────────┘│
│                           │                                │
│  ┌────────────────────────▼──────────────────────────────┐│
│  │  H2 Leak Predictor                                    ││
│  │  H2 Consumption Forecaster                             ││
│  │  Anomaly Detector                                     ││
│  └──────────────────────────────────────────────────────┘ │
└───────────────────────────┬────────────────────────────────┘
                            │
                            │ Predictions & Alerts
                            ▼
┌────────────────────────────────────────────────────────────┐
│  EICAS / Cockpit Display / Maintenance System              │
└────────────────────────────────────────────────────────────┘
```

---

## 3. Requirements

### 3.1 Functional Requirements

| Req ID | Description | Priority |
|--------|-------------|----------|
| **REQ-047** | Leak detection within 50 ms of sensor indication | CRITICAL |
| **REQ-048** | Failsafe to safe state on sensor fault | CRITICAL |
| **REQ-049** | Redundant pressure monitoring (2-out-of-4 voting) | HIGH |
| **REQ-025** | Provide real-time H2 sensor data at 10 Hz | HIGH |
| **REQ-H2-001** | Support 4 independent H2 tanks | HIGH |
| **REQ-H2-002** | Detect and report valve position changes | MEDIUM |

### 3.2 Performance Requirements

| Metric | Requirement | Rationale |
|--------|-------------|-----------|
| **Data Latency** | < 10 ms (p99) | Real-time leak detection |
| **CAN Bus Utilization** | < 60% | Leave headroom for faults/retransmissions |
| **Message Loss Rate** | < 0.01% | Safety-critical data |
| **Sensor Accuracy** | Per sensor spec (§4.2) | Model prediction quality |

### 3.3 Safety Requirements

| Req ID | Description | Mitigation |
|--------|-------------|------------|
| **SAFE-001** | Sensor failure must not cause hazardous state | Redundancy + voting logic |
| **SAFE-002** | AI prediction failure must not disable fuel system | Fallback to manual control |
| **SAFE-003** | False positive leak alerts must be < 0.1% | Model validation & thresholding |

---

## 4. Technical Specification

### 4.1 Protocol: ARINC 825 (CAN Bus)

**Bus Configuration:**
- **Standard:** ARINC 825-2 (CAN 2.0B)
- **Baud Rate:** 250 kbps
- **Bus Topology:** Dual-redundant CAN (CAN-A, CAN-B)
- **Termination:** 120Ω at each end
- **Connector:** Deutsch DT04-4P

**Message Format:**
- **Identifier:** 29-bit extended CAN ID
- **Payload:** Up to 8 bytes
- **Byte Order:** Big-endian (network order)

### 4.2 Sensor Data Messages

#### 4.2.1 H2 Pressure (CAN ID: 0x2A0 - 0x2A3)

**Frequency:** 10 Hz per tank

| Byte | Bits | Description | Units | Range |
|------|------|-------------|-------|-------|
| 0-3 | 0-31 | Pressure (float32 IEEE 754) | bar | 0-350 |
| 4-5 | 0-15 | Sensor status (uint16) | - | See §4.2.5 |
| 6-7 | 0-15 | Sequence counter (uint16) | - | 0-65535 |

**Example (Tank 1, 325.5 bar):**
```
CAN ID: 0x2A0
Data: 43 A2 B3 33 00 00 00 42
      └─ Pressure (325.5 as IEEE 754 float)
                  └─ Status (OK)
                        └─ Sequence
```

#### 4.2.2 H2 Temperature (CAN ID: 0x2B0 - 0x2B3)

**Frequency:** 10 Hz per tank

| Byte | Bits | Description | Units | Range |
|------|------|-------------|-------|-------|
| 0-3 | 0-31 | Temperature (float32 IEEE 754) | Kelvin | 20-300 |
| 4-5 | 0-15 | Sensor status (uint16) | - | See §4.2.5 |
| 6-7 | 0-15 | Sequence counter (uint16) | - | 0-65535 |

#### 4.2.3 H2 Flow Rate (CAN ID: 0x2C0 - 0x2C3)

**Frequency:** 10 Hz per tank

| Byte | Bits | Description | Units | Range |
|------|------|-------------|-------|-------|
| 0-3 | 0-31 | Flow rate (float32 IEEE 754) | kg/s | 0-50 |
| 4-5 | 0-15 | Sensor status (uint16) | - | See §4.2.5 |
| 6-7 | 0-15 | Sequence counter (uint16) | - | 0-65535 |

#### 4.2.4 H2 Tank Level (CAN ID: 0x2D0 - 0x2D3)

**Frequency:** 10 Hz per tank

| Byte | Bits | Description | Units | Range |
|------|------|-------------|-------|-------|
| 0-1 | 0-15 | Level (uint16, scaled) | 0.01% | 0-10000 (0-100%) |
| 2 | 0-7 | Valve position (uint8) | - | 0=Closed, 1=Open |
| 3 | 0 | Leak detected (bit) | - | 0=No, 1=Yes |
| 4-5 | 0-15 | Sensor status (uint16) | - | See §4.2.5 |
| 6-7 | 0-15 | Sequence counter (uint16) | - | 0-65535 |

#### 4.2.5 Sensor Status Codes

| Value | Status | Description |
|-------|--------|-------------|
| 0x0000 | GOOD | Sensor operating normally |
| 0x0001 | DEGRADED | Sensor accuracy reduced |
| 0x0002 | FAILED | Sensor fault, data invalid |
| 0x0003 | MISSING | No data received (timeout) |

---

## 5. AI/ML Output Messages

### 5.1 Leak Probability (CAN ID: 0x3A0)

**Frequency:** 1 Hz (continuous), Event-driven (alert)

| Byte | Bits | Description | Units | Range |
|------|------|-------------|-------|-------|
| 0-1 | 0-15 | Leak probability (uint16, scaled) | 0.01% | 0-10000 (0-100%) |
| 2 | 0-7 | Tank ID (uint8) | - | 1-4 |
| 3 | 0-7 | Severity (uint8) | - | 0=None, 1=Low, 2=Med, 3=High |
| 4-5 | 0-15 | Confidence (uint16, scaled) | 0.01% | 0-10000 (0-100%) |
| 6-7 | 0-15 | Reserved | - | - |

**Alert Threshold:** Leak probability > 10% with confidence > 85%

### 5.2 Anomaly Alert (CAN ID: 0x3A1)

**Frequency:** Event-driven

| Byte | Bits | Description | Units | Range |
|------|------|-------------|-------|-------|
| 0 | 0-7 | Anomaly type (uint8) | - | See §5.3 |
| 1 | 0-7 | Tank ID (uint8) | - | 1-4 |
| 2-3 | 0-15 | Anomaly score (uint16, scaled) | 0.01 | 0-10000 |
| 4-7 | 0-31 | Timestamp (uint32) | seconds | Unix epoch |

### 5.3 Anomaly Types

| Code | Type | Description |
|------|------|-------------|
| 0x01 | PRESSURE_SPIKE | Rapid pressure increase |
| 0x02 | TEMP_ANOMALY | Unexpected temperature change |
| 0x03 | FLOW_MISMATCH | Flow rate inconsistent with valves |
| 0x04 | LEVEL_DRIFT | Tank level drifting unexpectedly |

---

## 6. Error Handling

### 6.1 Sensor Fault Detection

**Voting Logic (2-out-of-4):**
```python
def get_validated_pressure():
    readings = [tank1.pressure, tank2.pressure, tank3.pressure, tank4.pressure]
    valid_readings = [r for r in readings if r.status == GOOD]

    if len(valid_readings) < 2:
        raise SensorFault("Insufficient valid sensors")

    # Median of valid readings
    return median(valid_readings)
```

### 6.2 CAN Bus Error Handling

| Error | Detection | Response |
|-------|-----------|----------|
| **Bus-Off** | CAN controller status | Switch to redundant bus (CAN-B) |
| **Message Timeout** | No message for 200 ms | Use last known good value, flag DEGRADED |
| **CRC Error** | CAN frame CRC | Discard message, request retransmit |
| **Sequence Gap** | Sequence counter discontinuity | Log warning, check for data loss |

---

## 7. Safety Assurance

### 7.1 Fail-Safe Behavior

**On AI/ML Failure:**
1. Fuel system controller falls back to direct sensor monitoring
2. Cockpit displays show "AI UNAVAILABLE" status
3. Manual leak checks via crew procedures

**On Sensor Failure:**
1. Redundant sensor voting (2-out-of-4)
2. If < 2 sensors available, disable automated leak prediction
3. Crew alerted to DEGRADED FUEL MONITORING status

### 7.2 Certification Compliance

- **DO-178C DAL B:** Software assurance for leak prediction
- **DO-254 DAL B:** Hardware assurance for CAN interface
- **ARP4754A:** System safety assessment
- **EASA AI Roadmap:** AI/ML specific certification requirements

---

## 8. Testing and Validation

### 8.1 Integration Tests

| Test ID | Description | Pass Criteria |
|---------|-------------|---------------|
| **INT-001** | CAN message reception | All sensor messages received at 10 Hz |
| **INT-002** | Leak prediction latency | Alert generated within 50 ms |
| **INT-003** | Sensor fault handling | Correct voting logic, no false alarms |
| **INT-004** | Bus redundancy | Automatic switchover < 10 ms |

### 8.2 Fault Injection Tests

| Test ID | Fault | Expected Behavior |
|---------|-------|-------------------|
| **FI-001** | Single sensor failure | System continues with 3 sensors |
| **FI-002** | Two sensor failures | System continues with 2 sensors |
| **FI-003** | Three sensor failures | DEGRADED mode, crew alert |
| **FI-004** | CAN bus failure | Switch to redundant bus |

---

## 9. Traceability

| Requirement | Interface Spec | Test Case |
|-------------|----------------|-----------|
| REQ-047 | §5.1 Leak Probability | TEST-509 |
| REQ-048 | §7.1 Fail-Safe | TEST-510 |
| REQ-049 | §6.1 Voting Logic | TEST-511 |

---

## 10. Related Documents

| Document ID | Title |
|-------------|-------|
| 95-00-05-01-001 | Data Sources Catalog |
| 95-00-05-00-004 | Cross-ATA Interface Map |
| 95-00-05-03-A-102 | ATA 28 Context Diagram (Asset) |

---

**End of Document**

**Next Review:** 2025-12-12
**Owner:** Systems Integration Team
