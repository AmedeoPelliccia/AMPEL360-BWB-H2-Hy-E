# 95-20-28 NN Fuel System — Data Dictionary

**Version**: 1.0  
**Status**: WORKING  
**Last Updated**: 2025-11-18

## Overview

This document defines all data elements used in the Neural Network Fuel System subsystem, including sensor inputs, model outputs, and internal state variables.

## Sensor Inputs

### Fuel Quantity Sensors

| Field Name | Type | Unit | Range | Accuracy | Sample Rate | Source |
|------------|------|------|-------|----------|-------------|--------|
| tank_level_1 | float32 | liters | [0, 10000] | ±0.5% | 5 Hz | Capacitance sensor |
| tank_level_2 | float32 | liters | [0, 10000] | ±0.5% | 5 Hz | Capacitance sensor |
| tank_level_center | float32 | liters | [0, 15000] | ±0.5% | 5 Hz | Capacitance sensor |
| tank_level_reserve | float32 | liters | [0, 2000] | ±0.5% | 5 Hz | Capacitance sensor |

### Flow Sensors

| Field Name | Type | Unit | Range | Accuracy | Sample Rate | Source |
|------------|------|------|-------|----------|-------------|--------|
| flow_engine_1 | float32 | kg/min | [0, 200] | ±1% | 5 Hz | Turbine flow meter |
| flow_engine_2 | float32 | kg/min | [0, 200] | ±1% | 5 Hz | Turbine flow meter |
| flow_transfer_1_2 | float32 | kg/min | [-50, 50] | ±2% | 1 Hz | Transfer flow meter |
| flow_transfer_2_center | float32 | kg/min | [-50, 50] | ±2% | 1 Hz | Transfer flow meter |

### Pressure Sensors

| Field Name | Type | Unit | Range | Accuracy | Sample Rate | Source |
|------------|------|------|-------|----------|-------------|--------|
| pressure_tank_1 | float32 | psi | [0, 100] | ±0.5 psi | 5 Hz | Pressure transducer |
| pressure_tank_2 | float32 | psi | [0, 100] | ±0.5 psi | 5 Hz | Pressure transducer |
| pressure_feed_line_1 | float32 | psi | [0, 150] | ±1 psi | 5 Hz | Pressure transducer |
| pressure_feed_line_2 | float32 | psi | [0, 150] | ±1 psi | 5 Hz | Pressure transducer |

### Temperature Sensors

| Field Name | Type | Unit | Range | Accuracy | Sample Rate | Source |
|------------|------|------|-------|----------|-------------|--------|
| temp_tank_1 | float32 | celsius | [-40, 50] | ±1°C | 2 Hz | RTD probe |
| temp_tank_2 | float32 | celsius | [-40, 50] | ±1°C | 2 Hz | RTD probe |
| temp_ambient | float32 | celsius | [-60, 50] | ±2°C | 1 Hz | External probe |
| temp_fuel_feed_1 | float32 | celsius | [-40, 50] | ±1°C | 2 Hz | RTD probe |

### Valve and Pump Status

| Field Name | Type | Unit | Range | Accuracy | Sample Rate | Source |
|------------|------|------|-------|----------|-------------|--------|
| valve_xfer_1_2 | float32 | percent | [0, 100] | ±1% | 1 Hz | Position sensor |
| valve_xfer_2_center | float32 | percent | [0, 100] | ±1% | 1 Hz | Position sensor |
| pump_xfer_1 | bool | - | [0, 1] | N/A | 1 Hz | Status indicator |
| pump_xfer_2 | bool | - | [0, 1] | N/A | 1 Hz | Status indicator |
| pump_boost_1 | bool | - | [0, 1] | N/A | 1 Hz | Status indicator |
| pump_boost_2 | bool | - | [0, 1] | N/A | 1 Hz | Status indicator |

### Water Detection Sensors

| Field Name | Type | Unit | Range | Accuracy | Sample Rate | Source |
|------------|------|------|-------|----------|-------------|--------|
| capacitance_tank_1 | float32 | picofarad | [0, 1000] | ±1 pF | 0.1 Hz | Capacitance probe |
| conductivity_tank_1 | float32 | µS/cm | [0, 100] | ±1 µS/cm | 0.1 Hz | Conductivity probe |
| optical_density_tank_1 | float32 | abs | [0, 5] | ±0.01 | 0.1 Hz | Optical sensor |

### Aircraft State

| Field Name | Type | Unit | Range | Accuracy | Sample Rate | Source |
|------------|------|------|-------|----------|-------------|--------|
| pitch | float32 | degrees | [-90, 90] | ±0.1° | 10 Hz | AHRS |
| roll | float32 | degrees | [-180, 180] | ±0.1° | 10 Hz | AHRS |
| yaw_rate | float32 | deg/s | [-10, 10] | ±0.01° | 10 Hz | AHRS |
| altitude | float32 | feet | [0, 45000] | ±10 ft | 1 Hz | Air data |
| airspeed | float32 | knots | [0, 500] | ±2 kt | 1 Hz | Air data |
| aircraft_weight | float32 | kg | [50000, 120000] | ±100 kg | 0.1 Hz | FMS |
| cg_position | float32 | % MAC | [15, 35] | ±0.1% | 0.5 Hz | FMS |
| flight_phase | enum | - | [8 values] | N/A | 0.5 Hz | FMS |

## Model Outputs

### Fuel Quantity Estimation Outputs

| Field Name | Type | Unit | Range | Description |
|------------|------|------|-------|-------------|
| estimated_qty_tank_1 | float32 | liters | [0, 10000] | Corrected fuel quantity |
| estimated_qty_tank_2 | float32 | liters | [0, 10000] | Corrected fuel quantity |
| estimated_qty_center | float32 | liters | [0, 15000] | Corrected fuel quantity |
| total_fuel_remaining | float32 | liters | [0, 35000] | Total usable fuel |
| confidence_qty | float32 | - | [0, 1] | Estimation confidence |
| sensor_health_status | enum[] | - | [OK, DEGRADED, FAILED] | Individual sensor health |

### Leak Detection Outputs

| Field Name | Type | Unit | Range | Description |
|------------|------|------|-------|-------------|
| anomaly_score | float32 | - | [0, 1] | Anomaly severity score |
| leak_detected | bool | - | [0, 1] | Leak detection flag |
| leak_severity | enum | - | [NONE, MINOR, MODERATE, SEVERE] | Severity classification |
| affected_system | enum | - | [TANK_1, ...] | Location of detected leak |
| confidence_leak | float32 | - | [0, 1] | Detection confidence |

### Fuel Transfer Optimization Outputs

| Field Name | Type | Unit | Range | Description |
|------------|------|------|-------|-------------|
| pump_command_1 | bool | - | [0, 1] | Transfer pump 1 activation |
| pump_command_2 | bool | - | [0, 1] | Transfer pump 2 activation |
| valve_command_1_2 | float32 | percent | [0, 100] | Valve position command |
| valve_command_2_center | float32 | percent | [0, 100] | Valve position command |
| estimated_completion_time | float32 | minutes | [0, 60] | Transfer completion estimate |
| confidence_transfer | float32 | - | [0, 1] | Optimization confidence |

### Temperature Prediction Outputs

| Field Name | Type | Unit | Range | Description |
|------------|------|------|-------|-------------|
| predicted_temp_tank_1 | float32 | celsius | [-40, 50] | 10-min ahead prediction |
| predicted_temp_tank_2 | float32 | celsius | [-40, 50] | 10-min ahead prediction |
| temp_rate_of_change_1 | float32 | °C/min | [-5, 5] | Temperature change rate |
| cooling_requirement_1 | float32 | kW | [0, 50] | Required cooling power |
| warning_flag_temp | bool[] | - | [0, 1] | Temperature warning flags |

### Water Contamination Detection Outputs

| Field Name | Type | Unit | Range | Description |
|------------|------|------|-------|-------------|
| water_detected_tank_1 | bool | - | [0, 1] | Water detection flag |
| water_content_tank_1 | float32 | % vol | [0, 10] | Estimated water content |
| contamination_severity | enum | - | [NONE, LOW, MEDIUM, HIGH] | Severity classification |
| recommended_action | enum | - | [MONITOR, SCHEDULE_DRAIN, DRAIN_IMMEDIATELY] | Action recommendation |

## Internal State Variables

### Model State

| Field Name | Type | Unit | Range | Description |
|------------|------|------|-------|-------------|
| model_loaded | bool | - | [0, 1] | Model load status |
| inference_time_ms | float32 | milliseconds | [0, 1000] | Last inference time |
| inference_count | uint64 | - | [0, ∞] | Total inference count |
| error_count | uint32 | - | [0, ∞] | Error counter |

### System Health

| Field Name | Type | Unit | Range | Description |
|------------|------|------|-------|-------------|
| system_status | enum | - | [HEALTHY, DEGRADED, FAILED] | Overall system status |
| degradation_level | uint8 | - | [0, 3] | Degradation severity (0=none, 3=severe) |
| last_health_check | int64 | milliseconds | [0, ∞] | Timestamp of last health check |

## Enumeration Definitions

### Flight Phase

```
GROUND = 0
TAXI = 1
TAKEOFF = 2
CLIMB = 3
CRUISE = 4
DESCENT = 5
APPROACH = 6
LANDING = 7
```

### System Status

```
HEALTHY = 0
DEGRADED = 1
FAILED = 2
```

### Sensor Health

```
OK = 0
DEGRADED = 1
FAILED = 2
```

### Leak Severity

```
NONE = 0
MINOR = 1
MODERATE = 2
SEVERE = 3
```

### Contamination Severity

```
NONE = 0
LOW = 1
MEDIUM = 2
HIGH = 3
```

## Data Quality Requirements

### Completeness

- Missing data rate: <0.1%
- Imputation strategy: Linear interpolation for gaps <1 second, flag as invalid for longer gaps

### Validity

- Range checking: All values within specified ranges
- Reasonableness: Rate of change limits enforced
- Cross-validation: Redundant sensors cross-checked

### Timeliness

- Maximum latency: 200 ms from sensor to NN output
- Timeout handling: Maintain last valid state, flag as stale

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
