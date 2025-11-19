# 95-70-00-008: CAOS Propulsion Hooks

## 1. Introduction

This document describes how the CAOS (Computer Aided Operations & Services) system discovers, monitors, and optimizes propulsion assets within the AMPEL360 BWB H₂ Hy-E Q100 aircraft. It defines the integration points, data flows, and neural network models that enable AI-powered propulsion management.

## 2. CAOS Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                      CAOS Core Platform                          │
│  (ATA 40, 92, 95-20, 95-30, 95-40, 95-50, 95-60)               │
└────────────────────────┬────────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
   ┌──────────┐   ┌──────────┐   ┌──────────┐
   │ Discovery│   │ Monitoring│   │Optimization│
   │  Hooks   │   │   Hooks   │   │   Hooks   │
   └────┬─────┘   └────┬──────┘   └────┬──────┘
        │              │               │
        └──────────────┼───────────────┘
                       │
         ┌─────────────┴─────────────┐
         │  Propulsion Assets       │
         │  (ATA 70-79)             │
         │  • Engines/Propulsors     │
         │  • FADEC Controllers      │
         │  • Health Monitoring      │
         │  • Fuel Systems           │
         └───────────────────────────┘
```

## 3. Asset Discovery Hooks

### 3.1 Discovery Mechanism

CAOS discovers propulsion assets through:

1. **Static Registry**: Reads `95-70-00-006_Propulsion_Assets_Registry.json` at system initialization
2. **Dynamic Discovery**: Queries ARINC 429 / MIL-STD-1553 bus for active propulsion components
3. **Configuration Files**: Loads aircraft-specific propulsion configuration (tail number specific)
4. **Health Checks**: Validates each discovered asset is responsive

### 3.2 Asset Registration Schema

Each propulsion asset registers with CAOS using the following schema:

```json
{
  "asset_id": "PROP-76-001",
  "asset_type": "FADEC",
  "ata_chapter": "76",
  "location": {
    "station": "FS 240",
    "side": "Left"
  },
  "capabilities": [
    "thrust_control",
    "health_monitoring",
    "fuel_metering",
    "nn_optimization"
  ],
  "data_endpoints": {
    "health_data": "arinc429://channel2/label270",
    "performance_data": "arinc429://channel2/label271",
    "control_input": "can://engine_can1/id0x100"
  },
  "nn_models": [
    {
      "model_id": "fadec_health_v1.0",
      "input_channels": 32,
      "inference_rate_hz": 10,
      "output": "health_score"
    }
  ],
  "metadata": {
    "manufacturer": "TBD",
    "serial_number": "SN-12345",
    "software_version": "v2.0.0"
  }
}
```

### 3.3 Discovery API

**Endpoint**: `caos://discovery/propulsion`

**Methods**:
- `discover_all()`: Returns list of all propulsion assets
- `discover_by_ata(chapter)`: Returns assets for specific ATA chapter
- `get_asset(asset_id)`: Returns detailed info for specific asset
- `register_asset(asset_info)`: Manually register a new asset
- `unregister_asset(asset_id)`: Remove asset from registry

**Example**:
```python
import caos

# Discover all propulsion assets
propulsion_assets = caos.discovery.propulsion.discover_all()

# Filter by ATA chapter
fadec_units = caos.discovery.propulsion.discover_by_ata(76)

# Get specific asset
left_engine_fadec = caos.discovery.propulsion.get_asset("PROP-76-001")
```

---

## 4. Monitoring Hooks

### 4.1 Real-Time Data Streams

CAOS monitors propulsion systems through continuous data streams:

| Data Stream | Source | Sample Rate | Protocol | Data Volume |
|-------------|--------|-------------|----------|-------------|
| **Thrust Command** | FADEC | 10 Hz | ARINC 429 | 0.1 KB/s |
| **Engine Performance** | FADEC | 10 Hz | ARINC 429 | 1 KB/s |
| **Health Parameters** | Sensors via FADEC | 100 Hz | ARINC 429 | 10 KB/s |
| **Fuel Flow** | FMU | 1 Hz | CAN Bus | 0.05 KB/s |
| **Vibration Data** | Accelerometers | 1000 Hz | Analog (digitized) | 100 KB/s |
| **Temperature Map** | Thermocouples | 10 Hz | ARINC 429 | 2 KB/s |

**Total Data Volume**: ~113 KB/s per engine → ~226 KB/s for two engines

### 4.2 Monitoring API

**Endpoint**: `caos://monitoring/propulsion`

**Methods**:
- `subscribe_to_stream(asset_id, data_type, callback)`: Subscribe to real-time data
- `get_latest_value(asset_id, parameter)`: Get most recent value
- `get_history(asset_id, parameter, time_range)`: Retrieve historical data
- `get_health_score(asset_id)`: Get current health score (0.0-1.0)
- `get_anomalies(asset_id, since_time)`: Retrieve detected anomalies

**Example**:
```python
import caos

# Subscribe to engine health data
def health_callback(data):
    print(f"Health Score: {data['health_score']}")
    if data['health_score'] < 0.85:
        print("WARNING: Engine health degraded")

caos.monitoring.propulsion.subscribe_to_stream(
    asset_id="PROP-72-001",
    data_type="health_score",
    callback=health_callback
)

# Get current EGT
egt = caos.monitoring.propulsion.get_latest_value(
    asset_id="PROP-77-001",
    parameter="exhaust_gas_temperature"
)
print(f"Current EGT: {egt}°C")
```

### 4.3 Alerting Hooks

CAOS generates alerts for propulsion anomalies:

| Alert Level | Trigger Condition | Action |
|-------------|------------------|--------|
| **Advisory** | Minor deviation from normal | Log to maintenance system |
| **Caution** | Parameter approaching limit | Alert flight crew, log event |
| **Warning** | Parameter exceeds limit | Alert flight crew, limit engine operation |
| **Emergency** | Critical failure detected | Auto-shutdown if safe, emergency procedures |

**Alert API**:
```python
caos.monitoring.propulsion.register_alert_handler(
    alert_level="warning",
    callback=my_alert_handler
)
```

---

## 5. Optimization Hooks

### 5.1 Neural Network Optimization Models

CAOS uses multiple NN models to optimize propulsion performance:

#### 5.1.1 Thrust Optimization Model

**Model ID**: `thrust_optimizer_v1.2`

**Purpose**: Real-time thrust command optimization for fuel efficiency

**Inputs** (32 channels):
- Current thrust setting (%)
- Airspeed (KTAS)
- Altitude (ft)
- Temperature (°C)
- Fuel flow rate (kg/min)
- H₂ tank pressure (bar)
- Battery state of charge (%)
- Requested thrust from FCC

**Outputs** (4 channels):
- Optimized thrust command (%)
- Fuel cell power split (%)
- Battery power split (%)
- Predicted fuel efficiency gain (%)

**Inference Rate**: 10 Hz

**Model Location**: `caos://models/propulsion/thrust_optimizer_v1.2.onnx`

**Safety**: Advisory only; FADEC can override if outside safe envelope

#### 5.1.2 Health Prediction Model

**Model ID**: `propulsion_health_predictor_v1.0`

**Purpose**: Predict remaining useful life (RUL) and upcoming maintenance needs

**Inputs** (64 channels):
- Historical health scores (last 100 flights)
- Vibration spectrum (FFT features)
- Temperature trends
- Oil quality metrics
- Flight hours and cycles
- Operating envelope statistics

**Outputs** (8 channels):
- Health score (0.0-1.0)
- RUL estimate (flight hours)
- Probability of failure in next 100/500/1000 hours
- Recommended maintenance actions (encoded)
- Component-level degradation scores

**Inference Rate**: 0.1 Hz (once per 10 seconds)

**Model Location**: `caos://models/propulsion/health_predictor_v1.0.onnx`

**Training**: Continuously updated with fleet data

#### 5.1.3 Thermal Management Model

**Model ID**: `thermal_optimizer_v1.0`

**Purpose**: Optimize cooling and heat recovery for efficiency and component life

**Inputs** (24 channels):
- Engine temperatures (EGT, oil, fuel)
- Ambient conditions
- Cooling airflow rates
- Heat exchanger effectiveness
- CO₂ capture thermal demand

**Outputs** (8 channels):
- Optimal cooling airflow
- Heat exchanger valve positions
- Predicted component life impact
- CO₂ capture heat allocation

**Inference Rate**: 1 Hz

**Model Location**: `caos://models/propulsion/thermal_optimizer_v1.0.onnx`

### 5.2 Optimization API

**Endpoint**: `caos://optimization/propulsion`

**Methods**:
- `get_optimized_thrust(current_state)`: Get optimized thrust command
- `get_maintenance_schedule(asset_id)`: Get predicted maintenance needs
- `simulate_scenario(scenario_params)`: Run "what-if" simulation
- `get_efficiency_metrics()`: Retrieve current efficiency KPIs

**Example**:
```python
import caos

# Get optimized thrust command
current_state = {
    "thrust_setting": 0.85,
    "airspeed_ktas": 250,
    "altitude_ft": 35000,
    "temperature_c": -55,
    "fuel_flow_kg_min": 4.5
}

optimized = caos.optimization.propulsion.get_optimized_thrust(current_state)
print(f"Recommended Thrust: {optimized['thrust_command']}%")
print(f"Efficiency Gain: {optimized['efficiency_gain']}%")

# Get maintenance prediction
maint = caos.optimization.propulsion.get_maintenance_schedule("PROP-72-001")
print(f"Next Inspection Due: {maint['next_inspection_hours']} hours")
print(f"Predicted RUL: {maint['rul_hours']} hours")
```

---

## 6. Data Flow Architecture

### 6.1 Data Pipeline

```
Propulsion Sensors → FADEC → ARINC 429 Bus → Avionics Gateway → 
CAOS Data Ingestion → NN Inference Engines → 
Optimization Outputs → FADEC (advisory) → Actuators
```

### 6.2 Latency Requirements

| Path | Max Latency | Typical |
|------|-------------|---------|
| **Sensor → FADEC** | 10 ms | 5 ms |
| **FADEC → CAOS** | 50 ms | 20 ms |
| **CAOS NN Inference** | 100 ms | 30 ms |
| **CAOS → FADEC Advisory** | 50 ms | 20 ms |
| **End-to-End** | 210 ms | 75 ms |

### 6.3 Data Storage

- **Real-Time Buffer**: 10-second rolling buffer (in-memory)
- **Flight Data**: Full-resolution data stored for entire flight
- **Post-Flight Archive**: Compressed and stored for 10 years
- **Training Dataset**: Anonymized and aggregated for NN model training

**Storage Volume**:
- Per Flight (5 hours): ~4 GB
- Per Aircraft Per Year: ~8 TB
- Fleet (10 aircraft) Per Year: ~80 TB

---

## 7. Security and Safety

### 7.1 Safety Architecture

- **Independence**: CAOS optimization is advisory; FADEC has full authority
- **Validation**: All CAOS commands validated by FADEC before execution
- **Fallback**: If CAOS fails, FADEC operates in standalone mode
- **Monitoring**: CAOS self-monitors for erroneous outputs

### 7.2 Cybersecurity

- **Authentication**: All CAOS-propulsion communication authenticated (TLS 1.3)
- **Authorization**: Role-based access control (RBAC)
- **Encryption**: All data encrypted in transit and at rest
- **Intrusion Detection**: Network monitoring for anomalous traffic
- **Air Gap**: Critical control loops (FADEC) isolated from CAOS network

**Compliance**: DO-326A / DO-356A (Airworthiness Security Process)

---

## 8. Model Management

### 8.1 Model Versioning

- **Version Format**: `model_name_vMAJOR.MINOR.PATCH`
- **Rollback**: Previous 3 model versions retained for rollback
- **A/B Testing**: New models validated in shadow mode before deployment
- **Fleet Rollout**: Gradual rollout to 10% → 50% → 100% of fleet

### 8.2 Model Training and Updates

| Update Type | Frequency | Approval Required |
|-------------|-----------|-------------------|
| **Patch** (bug fix) | As needed | Automated (post-validation) |
| **Minor** (improvement) | Quarterly | Engineering review |
| **Major** (architecture change) | Annually | Full certification review |

**Training Data**: Fleet data from all AMPEL360 aircraft, anonymized and aggregated

**Training Infrastructure**: Cloud-based (AWS, Azure, or on-prem)

**Validation**: Test on holdout dataset (20% of fleet data)

---

## 9. Integration Testing

### 9.1 Test Scenarios

| Test ID | Scenario | Pass Criteria |
|---------|----------|---------------|
| **CAOS-PROP-001** | Asset discovery on startup | All propulsion assets discovered in <10s |
| **CAOS-PROP-002** | Real-time monitoring | Data latency <100ms, 99.9% uptime |
| **CAOS-PROP-003** | NN thrust optimization | Efficiency gain >5%, no safety violations |
| **CAOS-PROP-004** | Health prediction accuracy | >90% accuracy on test dataset |
| **CAOS-PROP-005** | FADEC override | CAOS advisory rejected if outside envelope |
| **CAOS-PROP-006** | Failover to standalone | FADEC operates normally if CAOS fails |

### 9.2 Ground Testing

- **HIL (Hardware-in-the-Loop)**: FADEC + CAOS integration rig
- **Flight Simulator**: Full mission simulation with CAOS active
- **Dry Run**: On-ground engine runs with CAOS monitoring

### 9.3 Flight Testing

- **Phase 1**: CAOS monitoring only (no optimization)
- **Phase 2**: CAOS optimization in shadow mode (logged but not executed)
- **Phase 3**: CAOS optimization active (human-monitored)
- **Phase 4**: Full autonomous operation

---

## 10. Documentation and Training

### 10.1 Technical Documentation

- **API Reference**: `CAOS_Propulsion_API_v1.0.pdf`
- **Integration Guide**: `CAOS_Propulsion_Integration_Guide_v1.0.pdf`
- **Model Specifications**: `95-20-70-NN-Models/` (per model)

### 10.2 Training Materials

- **Flight Crew**: CAOS propulsion indications and advisories
- **Maintenance**: CAOS health predictions and maintenance planning
- **Engineering**: CAOS integration, troubleshooting, model updates

---

## 11. Related Documents

- [95-70-00-001: Propulsion DPP Overview](../95-70-00-001_Propulsion_DPP_Overview.md)
- [95-70-76-004: NN Propulsion Control Interfaces](../95-70-76_Propulsion_Control_Systems/95-70-76-004_Interfaces_to_NN_Propulsion_95-20-70_and_ATA_42_IMA.md)
- [95-20-70: Neural Network Propulsion Optimization](../../95-20_Systems/95-20-70_NN_Propulsion/)
- [ATA 40: AI Integration](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/I2-R_AND_D/ATA_40-AI_INTEGRATION/)

---

## 12. Version History

| Version | Date       | Author               | Changes                    |
|---------|------------|----------------------|----------------------------|
| 1.0     | 2025-11-17 | AMPEL360 Doc Team    | Initial creation           |

---

**Document ID**: 95-70-00-008  
**Status**: Active  
**Classification**: Internal Use  
**Next Review**: 2026-02-17
