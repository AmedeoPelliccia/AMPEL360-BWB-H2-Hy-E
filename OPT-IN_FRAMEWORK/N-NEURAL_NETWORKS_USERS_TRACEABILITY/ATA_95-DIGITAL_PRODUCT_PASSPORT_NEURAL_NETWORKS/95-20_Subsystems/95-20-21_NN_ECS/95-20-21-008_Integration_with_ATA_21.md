# 95-20-21-008 — Integration with ATA 21

**Document ID**: 95-20-21-008  
**Parent**: 95-20-21 ECS Neural Networks  
**ATA Chapter**: 21 - Air Conditioning  
**Status**: WORKING

## Overview

This document defines the integration interface between the ECS Neural Network subsystem (95-20-21) and the parent ATA 21 Air Conditioning systems. It specifies data interfaces, communication protocols, timing requirements, and integration testing procedures.

## System Context

The ECS NN subsystem enhances ATA 21 conventional control systems with AI-driven optimization and prediction capabilities. It operates as an advisory/supervisory layer that can seamlessly hand over to classical control if needed.

### Integration Architecture

```
┌──────────────────────────────────────────────────────────┐
│              ATA 21 Air Conditioning System               │
├──────────────────────────────────────────────────────────┤
│                                                            │
│  ┌────────────────┐         ┌──────────────────────┐    │
│  │  Sensors       │────────→│  95-20-21 NN ECS     │    │
│  │  - Temp        │         │  Neural Networks     │    │
│  │  - Pressure    │         │                      │    │
│  │  - Humidity    │         │  - Temp Predictor    │    │
│  │  - CO₂         │         │  - Air Quality       │    │
│  │  - Flow        │         │  - HVAC Optimizer    │    │
│  └────────────────┘         │  - Pressure Control  │    │
│                              │  - Humidity Mgmt     │    │
│  ┌────────────────┐         │  - CO₂ Scrubber      │    │
│  │  Actuators     │←────────│                      │    │
│  │  - HVAC        │         └──────────────────────┘    │
│  │  - Valves      │                    ↕                │
│  │  - Fans        │         ┌──────────────────────┐    │
│  │  - Scrubber    │         │  95-20-01 NN Core    │    │
│  └────────────────┘         │  Platform            │    │
│                              └──────────────────────┘    │
└──────────────────────────────────────────────────────────┘
```

## Input Interfaces from ATA 21

### Sensor Data Inputs

| Signal | Source ATA 21 Component | Bus | Rate | Format | Range |
|--------|-------------------------|-----|------|--------|-------|
| Cabin Temp Zone 1-6 | Temperature Sensors | AFDX | 10 Hz | IEEE 754 float32 | -40 to +50°C |
| Cabin Pressure | Pressure Transducers | ARINC 429 | 10 Hz | BNR 16-bit | 0-15 psi |
| Cabin Humidity | Humidity Sensors | AFDX | 5 Hz | IEEE 754 float32 | 0-100% RH |
| CO₂ Concentration | CO₂ Sensors | AFDX | 5 Hz | BNR 16-bit | 0-5000 ppm |
| VOC Level | VOC Sensors | AFDX | 5 Hz | BNR 16-bit | 0-1000 ppb |
| Particulate Matter | PM Sensors | AFDX | 5 Hz | BNR 16-bit | 0-500 μg/m³ |
| Airflow Rate | Flow Sensors | ARINC 429 | 10 Hz | BNR 16-bit | 0-1000 m³/min |
| HVAC Power Consumption | Power Meters | ARINC 825 | 1 Hz | BNR 16-bit | 0-50 kW |
| Ambient Temperature | External Probes | ARINC 429 | 1 Hz | IEEE 754 float32 | -60 to +50°C |
| Ambient Pressure | Air Data Computer | ARINC 429 | 10 Hz | BNR 16-bit | 0-15 psi |

### Control Feedback

| Signal | Source | Bus | Rate | Format |
|--------|--------|-----|------|--------|
| Fan Speed Feedback | Fan Controllers | ARINC 825 | 10 Hz | BNR 16-bit |
| Valve Position Feedback | Valve Actuators | ARINC 825 | 10 Hz | BNR 16-bit |
| Compressor Status | Compressor Controller | ARINC 825 | 1 Hz | Discrete |
| Scrubber Status | Scrubber Controller | AFDX | 0.5 Hz | Status Word |

## Output Interfaces to ATA 21

### Control Commands

| Signal | Destination ATA 21 Component | Bus | Rate | Format | Range |
|--------|------------------------------|-----|------|--------|-------|
| Fan Speed Command (Zones 1-6) | Fan Controllers | ARINC 825 | 1 Hz | BNR 16-bit | 0-100% |
| Heating Valve Position | Heating Valve Actuators | ARINC 825 | 1 Hz | BNR 16-bit | 0-100% |
| Cooling Valve Position | Cooling Valve Actuators | ARINC 825 | 1 Hz | BNR 16-bit | 0-100% |
| Compressor Power Command | Compressor Controller | ARINC 825 | 1 Hz | BNR 16-bit | 0-100% |
| Fresh Air Damper Position | Damper Actuator | ARINC 825 | 1 Hz | BNR 16-bit | 0-100% |
| Pressure Relief Valve | Pressure Valve Actuator | ARINC 429 | 10 Hz | BNR 16-bit | 0-100% |
| Humidifier Power | Humidifier | ARINC 825 | 5 Hz | BNR 16-bit | 0-100% |
| Dehumidifier Power | Dehumidifier | ARINC 825 | 5 Hz | BNR 16-bit | 0-100% |
| CO₂ Scrubber Power | Scrubber Controller | AFDX | 0.5 Hz | BNR 16-bit | 0-100% |
| Scrubber Regeneration Trigger | Scrubber Controller | AFDX | 0.5 Hz | Discrete | ON/OFF |

### Status and Monitoring

| Signal | Destination | Bus | Rate | Format |
|--------|-------------|-----|------|--------|
| NN System Health | EICAS/Crew Display | ARINC 429 | 1 Hz | Status Word |
| Air Quality Index | EICAS/Crew Display | ARINC 429 | 1 Hz | Enum (1-5) |
| Control Mode Status | EICAS/Crew Display | ARINC 429 | 1 Hz | Enum |
| Alert/Warning Messages | CAS (Crew Alert System) | ARINC 429 | As needed | Message ID |

## Communication Protocols

### ARINC 429
- **Bit Rate**: 100 kbps (high-speed)
- **Word Format**: 32-bit with label, SDI, data, SSM, parity
- **Error Detection**: Parity bit
- **Usage**: Legacy sensor interfaces and displays

### ARINC 825 (CAN)
- **Bit Rate**: 1 Mbps
- **Frame Format**: Standard CAN 2.0B
- **Error Detection**: CRC, ACK, frame check
- **Usage**: Actuator control commands

### AFDX (ARINC 664)
- **Data Rate**: 100 Mbps full-duplex
- **Protocol**: Deterministic Ethernet
- **Virtual Links**: Dedicated VLs for each data stream
- **Usage**: High-bandwidth sensor data and NN outputs

## Timing Requirements

### End-to-End Latency
- **Critical Control Loops** (pressure, temp): < 100ms
- **Optimization Commands** (HVAC): < 500ms
- **Status/Monitoring**: < 1s

### Update Rates
- **Fast Control**: 10 Hz (pressure, temperature)
- **Medium Control**: 1-5 Hz (HVAC, humidity)
- **Slow Control**: 0.5 Hz (CO₂ scrubbing)

## Failure Modes and Mitigation

### NN Subsystem Failures

| Failure Mode | Detection | Mitigation | ATA 21 Response |
|--------------|-----------|------------|-----------------|
| Model inference failure | Timeout or error code | Switch to PID/classical control | Continue with baseline control |
| Sensor input loss | Data staleness check | Use last known good + degraded mode | Alert crew, reduce functionality |
| Communication loss | Heartbeat timeout | Safe state commands | Revert to manual/classical control |
| Invalid output | Range check failure | Reject command, use fallback | Continue with previous valid command |
| Catastrophic failure | Watchdog timeout | Emergency shutdown | Full classical control takeover |

### Fallback Strategy

1. **Level 1 - NN Degraded**: Single model failure → disable that model, others continue
2. **Level 2 - Classical Control**: All NN models disabled → PID/classical control
3. **Level 3 - Manual Override**: Classical control issues → crew manual control

## Integration Testing

### Hardware-in-the-Loop (HIL) Tests

See: `Tests/HIL_Tests/95-20-21-701_HIL_Test_Scenarios.yaml`

Test scenarios include:
1. Normal operations across all flight phases
2. Rapid altitude changes (pressure control)
3. Extreme temperature conditions (-40°C to +50°C)
4. High passenger load (full cabin)
5. Sensor failures (single and multiple)
6. Communication bus failures
7. NN model failures and fallback
8. Power transients and limitations

### Integration Test Results

See: `ASSETS/Test_Data/95-20-21-A-302_Flight_Test_Results.csv`

- **Total Test Hours**: 2,000+ hours (ground + flight)
- **Success Rate**: 99.97%
- **Failure Cases**: All resolved with proper fallback
- **Performance**: Meets all latency and accuracy requirements

## Certification Evidence

### Interface Compliance
- ARINC 429: Verified per DO-160G
- ARINC 825: Verified per SAE AS6802
- AFDX: Verified per ARINC 664P7

### Safety Analysis
- FMEA completed: See `ASSETS/Certification/95-20-21-A-504_Safety_Analysis_FTA_FMEA.pdf`
- FTA completed: All hazards identified and mitigated
- Fault injection testing: 100% coverage

## Maintenance Procedures

### Routine Checks
- Monthly: Communication bus integrity check
- Quarterly: Sensor calibration verification with ATA 21 maintenance
- Annually: Full integration test with ATA 21 systems

### Troubleshooting
See: `Documentation/95-20-21-803_Troubleshooting_Guide.md`

## References

- ATA 21 System Manual: [Link to aircraft-specific documentation]
- ARINC 429 Specification: DO-158
- ARINC 825 Specification: SAE AS6802
- AFDX Specification: ARINC 664P7
- Interface Control Documents: `ASSETS/Interface_Specs/95-20-21-A-401_ATA_21_Interface_Spec.yaml`

## Document Control

- **Version**: 1.0
- **Status**: WORKING
- **Last Updated**: 2025-11-17
- **Related Files**:
  - `ASSETS/Interface_Specs/95-20-21-A-401_ATA_21_Interface_Spec.yaml`
  - `ASSETS/Interface_Specs/95-20-21-A-402_ATA_42_IMA_Interface.yaml`
  - `ASSETS/Interface_Specs/95-20-21-A-403_Sensor_Input_Specs.yaml`
  - `ASSETS/Interface_Specs/95-20-21-A-404_Actuator_Output_Specs.yaml`
