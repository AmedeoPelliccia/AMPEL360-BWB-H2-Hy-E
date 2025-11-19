# 95-20-28 NN Fuel System — API Specifications

**Version**: 1.0  
**Status**: WORKING  
**Last Updated**: 2025-11-18

## Overview

This document specifies the APIs for the Neural Network Fuel System subsystem, including input/output interfaces, data formats, and communication protocols.

## API Endpoints

### Inference API

#### Fuel Quantity Estimation

```yaml
endpoint: /v1/fuel-quantity/estimate
method: POST
rate: 5 Hz
content-type: application/json

request:
  tank_levels:
    type: array<float32>
    unit: liters
    description: Raw tank level sensor readings
  attitude:
    pitch: float32  # degrees
    roll: float32   # degrees
    yaw_rate: float32  # deg/s
  temperature:
    type: array<float32>
    unit: celsius
  pressure:
    type: array<float32>
    unit: psi
  flow_rate:
    type: array<float32>
    unit: kg/min

response:
  estimated_quantities:
    type: array<float32>
    unit: liters
    description: Corrected fuel quantities per tank
  total_fuel:
    type: float32
    unit: liters
  confidence:
    type: array<float32>
    range: [0, 1]
  sensor_health:
    type: array<enum>
    values: [OK, DEGRADED, FAILED]
  timestamp:
    type: int64
    unit: milliseconds
```

#### Leak Detection

```yaml
endpoint: /v1/fuel-leak/detect
method: POST
rate: 1 Hz
content-type: application/json

request:
  fuel_levels:
    type: array<float32>
    unit: liters
  flow_rates:
    type: array<float32>
    unit: kg/min
  pressures:
    type: array<float32>
    unit: psi
  temperatures:
    type: array<float32>
    unit: celsius
  valve_positions:
    type: array<float32>
    unit: percent
  pump_status:
    type: array<bool>
  engine_consumption:
    type: array<float32>
    unit: kg/min

response:
  anomaly_score:
    type: float32
    range: [0, 1]
  leak_detected:
    type: bool
  leak_severity:
    type: enum
    values: [NONE, MINOR, MODERATE, SEVERE]
  affected_system:
    type: enum
    values: [TANK_1, TANK_2, ... , TRANSFER_LINE, UNKNOWN]
  confidence:
    type: float32
    range: [0, 1]
  timestamp:
    type: int64
    unit: milliseconds
```

#### Fuel Transfer Optimization

```yaml
endpoint: /v1/fuel-transfer/optimize
method: POST
rate: 0.5 Hz
content-type: application/json

request:
  fuel_levels:
    type: array<float32>
    unit: liters
  current_cg:
    type: float32
    unit: percent_MAC
  target_cg:
    type: float32
    unit: percent_MAC
  aircraft_weight:
    type: float32
    unit: kg
  flight_phase:
    type: enum
    values: [GROUND, TAXI, TAKEOFF, CLIMB, CRUISE, DESCENT, APPROACH, LANDING]
  pump_status:
    type: array<bool>
  valve_positions:
    type: array<float32>
    unit: percent

response:
  pump_commands:
    type: array<bool>
    description: Activate/deactivate transfer pumps
  valve_commands:
    type: array<float32>
    unit: percent
    description: Valve position commands
  transfer_sequence:
    type: array<object>
    description: Recommended transfer operations
  estimated_completion:
    type: float32
    unit: minutes
  confidence:
    type: float32
    range: [0, 1]
  timestamp:
    type: int64
    unit: milliseconds
```

#### Temperature Prediction

```yaml
endpoint: /v1/fuel-temperature/predict
method: POST
rate: 2 Hz
content-type: application/json

request:
  fuel_temperatures:
    type: array<float32>
    unit: celsius
  ambient_temperature:
    type: float32
    unit: celsius
  flow_rates:
    type: array<float32>
    unit: kg/min
  pressures:
    type: array<float32>
    unit: psi
  solar_radiation:
    type: float32
    unit: W/m²
  altitude:
    type: float32
    unit: feet
  flight_phase:
    type: enum

response:
  predicted_temperatures:
    type: array<float32>
    unit: celsius
    description: 10-minute ahead predictions
  rate_of_change:
    type: array<float32>
    unit: celsius/min
  cooling_requirement:
    type: array<float32>
    unit: kW
  warning_flags:
    type: array<bool>
  confidence:
    type: array<float32>
    range: [0, 1]
  timestamp:
    type: int64
    unit: milliseconds
```

#### Water Contamination Detection

```yaml
endpoint: /v1/fuel-water/detect
method: POST
rate: 0.1 Hz
content-type: application/json

request:
  capacitance:
    type: array<float32>
    unit: picofarad
  conductivity:
    type: array<float32>
    unit: microsiemens/cm
  optical_density:
    type: array<float32>
    unit: absorbance
  temperature:
    type: array<float32>
    unit: celsius
  pressure:
    type: array<float32>
    unit: psi
  humidity:
    type: array<float32>
    unit: percent_RH

response:
  water_detected:
    type: array<bool>
  water_content:
    type: array<float32>
    unit: percent_volume
  contamination_severity:
    type: array<enum>
    values: [NONE, LOW, MEDIUM, HIGH]
  detection_confidence:
    type: array<float32>
    range: [0, 1]
  recommended_action:
    type: array<enum>
    values: [MONITOR, SCHEDULE_DRAIN, DRAIN_IMMEDIATELY]
  timestamp:
    type: int64
    unit: milliseconds
```

## Health and Status API

### System Health

```yaml
endpoint: /health
method: GET
rate: 1 Hz

response:
  status: enum [HEALTHY, DEGRADED, FAILED]
  models:
    - model_id: string
      status: enum [LOADED, RUNNING, DEGRADED, FAILED]
      inference_time_ms: float32
      last_inference: int64
  sensors:
    - sensor_id: string
      status: enum [OK, DEGRADED, FAILED]
  timestamp: int64
```

### Model Information

```yaml
endpoint: /v1/models
method: GET

response:
  models:
    - model_id: string
      model_name: string
      version: string
      status: enum [ACTIVE, STANDBY, DEPRECATED]
      load_time: int64
      inference_count: int64
      average_latency_ms: float32
```

## Error Handling

### Error Response Format

```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": {}
  },
  "timestamp": 1700000000000
}
```

### Error Codes

| Code | Description | Action |
|------|-------------|--------|
| 400 | Bad Request - Invalid input format | Correct request format |
| 408 | Request Timeout | Retry request |
| 500 | Internal Server Error | Check system health |
| 503 | Service Unavailable | Model not loaded or system degraded |

## Communication Protocols

### ARINC 429

- **Baud Rate**: 100 kbps (high speed)
- **Word Format**: 32-bit
- **Update Rate**: Model-dependent (0.1-5 Hz)
- **Labels**: 200-237 (fuel system data)

### ARINC 825 (CAN)

- **Baud Rate**: 1 Mbps
- **Message IDs**: 0x280-0x2BF (fuel system commands)
- **Priority**: High for alerts, normal for status
- **Error Handling**: CRC, acknowledge, retry

### AFDX

- **Virtual Links**: 10 dedicated VLs
- **Bandwidth**: 5 Mbps aggregate
- **Latency**: <10 ms guaranteed
- **Redundancy**: Dual network paths

## Performance Requirements

| Metric | Requirement | Measurement Method |
|--------|-------------|-------------------|
| Latency | <200 ms end-to-end | Hardware timer |
| Throughput | 100+ requests/sec | Load testing |
| Availability | >99.99% | Uptime monitoring |
| Error Rate | <0.01% | Error logging |

## Security

### Authentication

- Mutual TLS authentication for API access
- Certificate-based device authentication

### Authorization

- Role-based access control (RBAC)
- Read-only access for monitoring
- Write access restricted to authorized systems

### Data Protection

- Encryption in transit (TLS 1.3)
- Integrity checking (HMAC)
- Replay attack prevention (timestamp + nonce)

## Document Control

- **Version**: 1.0  
- **Status**: WORKING  
- **Last Updated**: 2025-11-18  

---

## Document Control – AI Involvement

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.  
- Status: **DRAFT** – Subject to human review and approval.  
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-18_.
