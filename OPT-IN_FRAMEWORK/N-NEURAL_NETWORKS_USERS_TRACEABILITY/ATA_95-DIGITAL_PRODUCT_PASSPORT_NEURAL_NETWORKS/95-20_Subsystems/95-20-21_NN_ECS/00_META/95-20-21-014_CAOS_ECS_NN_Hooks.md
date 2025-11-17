# 95-20-21-014 — CAOS ECS NN Hooks

**Document ID**: 95-20-21-014  
**Parent**: 95-20-21 ECS Neural Networks  
**Type**: META - CAOS Integration  
**Status**: WORKING

## Overview

This document defines the CAOS (Cognitive Aerospace Operations System) integration points for the ECS Neural Network subsystem. It enables automatic discovery, monitoring, and management of the ECS NN capabilities within the AMPEL360 AI ecosystem.

## CAOS Discovery

### Service Registration

The ECS NN subsystem registers with CAOS using the following well-known endpoint:

**Base URL**: `/.well-known/mcp/ecs-nn/`

### Capability Manifest

```json
{
  "service": {
    "id": "95-20-21",
    "name": "NN_ECS",
    "version": "1.0",
    "type": "neural_network_subsystem",
    "parent_ata": "21",
    "description": "Environmental Control System Neural Networks"
  },
  "capabilities": [
    {
      "id": "temp_prediction",
      "name": "Cabin Temperature Prediction",
      "type": "time_series_forecasting",
      "model_id": "95-20-21-A-101",
      "endpoint": "/v1/predict/temperature",
      "input_schema": "95-20-21-A-403",
      "output_schema": "95-20-21-A-404",
      "latency_ms": 8,
      "rate_hz": 10,
      "dal_level": "C"
    },
    {
      "id": "air_quality",
      "name": "Air Quality Monitoring",
      "type": "classification",
      "model_id": "95-20-21-A-102",
      "endpoint": "/v1/monitor/air_quality",
      "input_schema": "95-20-21-A-403",
      "output_schema": "95-20-21-A-404",
      "latency_ms": 15,
      "rate_hz": 5,
      "dal_level": "C"
    },
    {
      "id": "hvac_optimization",
      "name": "HVAC Optimization",
      "type": "reinforcement_learning",
      "model_id": "95-20-21-A-103",
      "endpoint": "/v1/optimize/hvac",
      "input_schema": "95-20-21-A-403",
      "output_schema": "95-20-21-A-404",
      "latency_ms": 12,
      "rate_hz": 1,
      "dal_level": "C"
    },
    {
      "id": "pressure_control",
      "name": "Pressure Control",
      "type": "hybrid_controller",
      "model_id": "95-20-21-A-104",
      "endpoint": "/v1/control/pressure",
      "input_schema": "95-20-21-A-403",
      "output_schema": "95-20-21-A-404",
      "latency_ms": 5,
      "rate_hz": 10,
      "dal_level": "C"
    },
    {
      "id": "humidity_management",
      "name": "Humidity Management",
      "type": "regression",
      "model_id": "95-20-21-A-105",
      "endpoint": "/v1/manage/humidity",
      "input_schema": "95-20-21-A-403",
      "output_schema": "95-20-21-A-404",
      "latency_ms": 3,
      "rate_hz": 5,
      "dal_level": "D"
    },
    {
      "id": "co2_scrubbing",
      "name": "CO₂ Scrubbing Optimization",
      "type": "reinforcement_learning",
      "model_id": "95-20-21-A-106",
      "endpoint": "/v1/optimize/co2_scrubber",
      "input_schema": "95-20-21-A-403",
      "output_schema": "95-20-21-A-404",
      "latency_ms": 10,
      "rate_hz": 0.5,
      "dal_level": "D"
    }
  ],
  "health_check": {
    "endpoint": "/health",
    "interval_sec": 10,
    "timeout_ms": 500
  },
  "metrics": {
    "endpoint": "/metrics",
    "format": "prometheus",
    "includes": [
      "inference_latency",
      "prediction_accuracy",
      "energy_savings",
      "passenger_comfort_score",
      "model_health",
      "fallback_activations"
    ]
  }
}
```

### Discovery Endpoints

#### Capability Query
**GET** `/.well-known/mcp/ecs-nn/capability.json`

Returns the capability manifest described above.

#### Health Status
**GET** `/.well-known/mcp/ecs-nn/health`

Returns:
```json
{
  "status": "healthy|degraded|unhealthy",
  "timestamp": "2025-11-17T22:21:14Z",
  "models": [
    {
      "model_id": "95-20-21-A-101",
      "status": "active",
      "inference_count": 123456,
      "error_rate": 0.0001
    },
    ...
  ],
  "system": {
    "memory_usage_mb": 256,
    "cpu_usage_percent": 15,
    "gpu_usage_percent": 20
  }
}
```

#### Metrics Export
**GET** `/.well-known/mcp/ecs-nn/metrics`

Prometheus-format metrics for monitoring.

## MCP Endpoints

### Inference Endpoints

#### Temperature Prediction
**POST** `/v1/predict/temperature`

Request:
```json
{
  "zones": [
    {"zone_id": 1, "current_temp": 22.5, "target_temp": 23.0},
    ...
  ],
  "external_temp": 15.2,
  "passenger_count": 180,
  "flight_phase": "cruise",
  "hvac_power": 12.5,
  "airflow_rate": 450.0,
  "timestamp": "2025-11-17T22:21:14Z"
}
```

Response:
```json
{
  "predictions": [
    {"zone_id": 1, "predicted_temp": 22.8, "confidence": 0.95},
    ...
  ],
  "horizon_minutes": 5,
  "inference_time_ms": 8,
  "model_version": "v1.2"
}
```

#### Air Quality Monitoring
**POST** `/v1/monitor/air_quality`

Request:
```json
{
  "co2_ppm": 850,
  "humidity_rh": 45,
  "voc_ppb": 120,
  "pm25_ugm3": 8,
  "pm10_ugm3": 12,
  "temperature": 22.5,
  "timestamp": "2025-11-17T22:21:14Z"
}
```

Response:
```json
{
  "aqi_class": 2,
  "aqi_label": "Good",
  "co2_estimate": 855,
  "contaminant_alert": false,
  "confidence": 0.98,
  "inference_time_ms": 15,
  "model_version": "v1.0"
}
```

#### HVAC Optimization
**POST** `/v1/optimize/hvac`

Request:
```json
{
  "current_state": {
    "zone_temps": [22.1, 22.5, 22.3, 22.8, 22.4, 22.6],
    "target_temps": [22.5, 22.5, 22.5, 22.5, 22.5, 22.5],
    "predicted_temps": [22.2, 22.6, 22.4, 22.9, 22.5, 22.7],
    "aqi": 2,
    "external_temp": 15.2,
    "power_budget": 15.0
  },
  "timestamp": "2025-11-17T22:21:14Z"
}
```

Response:
```json
{
  "actions": {
    "fan_speeds": [75, 80, 78, 82, 76, 79],
    "heating_valve": 0.3,
    "cooling_valve": 0.1,
    "compressor_power": 60,
    "fresh_air_damper": 0.5
  },
  "expected_energy_savings": 12.5,
  "comfort_score": 0.96,
  "inference_time_ms": 12,
  "model_version": "v2.1"
}
```

### Management Endpoints

#### Model Status
**GET** `/v1/models/{model_id}/status`

Returns model-specific health and performance metrics.

#### Model Update
**POST** `/v1/models/{model_id}/update`

Triggers model update/reload (requires authorization).

#### Configuration
**GET** `/v1/config`

Returns current configuration.

**POST** `/v1/config`

Updates configuration (requires authorization).

## Event Streaming

### Real-Time Events

The ECS NN subsystem publishes events to CAOS event bus:

**Topics**:
- `ecs-nn/inference/temperature`
- `ecs-nn/inference/air_quality`
- `ecs-nn/inference/hvac`
- `ecs-nn/alerts/degradation`
- `ecs-nn/alerts/failure`
- `ecs-nn/metrics/performance`

**Event Format**:
```json
{
  "source": "95-20-21",
  "type": "inference.complete",
  "timestamp": "2025-11-17T22:21:14Z",
  "capability_id": "temp_prediction",
  "model_id": "95-20-21-A-101",
  "data": {
    "inference_time_ms": 8,
    "confidence": 0.95
  }
}
```

## Integration with Other Subsystems

### Dependencies

#### 95-20-01 (NN Core Platform)
- **Purpose**: Model deployment and inference runtime
- **Interface**: Core Platform API
- **Data Flow**: Bidirectional (model loading, inference requests)

#### 95-20-02 (NN DPP Blockchain)
- **Purpose**: Model provenance and certification tracking
- **Interface**: Blockchain API
- **Data Flow**: Write (provenance events, certification hashes)

#### 95-20-42 (NN IMA Integration)
- **Purpose**: Compute resources and partitioning
- **Interface**: IMA Partition API
- **Data Flow**: Resource allocation requests

### Data Sharing

#### Inputs from CAOS
- Flight phase information
- Weather data
- Aircraft configuration
- Maintenance status

#### Outputs to CAOS
- Environmental performance metrics
- Energy efficiency data
- Passenger comfort scores
- Anomaly alerts
- Model health status

## Security and Authentication

### API Authentication
- **Method**: JWT tokens
- **Authorization**: Role-based access control (RBAC)
- **Roles**: 
  - `ecs-nn-read`: Read-only access to data and metrics
  - `ecs-nn-operate`: Inference requests
  - `ecs-nn-admin`: Configuration and model updates

### Data Encryption
- **In Transit**: TLS 1.3
- **At Rest**: AES-256
- **Model Files**: Cryptographically signed

## Monitoring and Alerting

### Health Checks
- **Frequency**: Every 10 seconds
- **Timeout**: 500ms
- **Failure Threshold**: 3 consecutive failures trigger alert

### Performance Monitoring
- Inference latency (per model)
- Prediction accuracy (online validation)
- Energy savings (real-time calculation)
- Passenger comfort score (aggregated)
- Model health (internal metrics)
- Fallback activation rate

### Alert Conditions

| Alert Level | Condition | Action |
|-------------|-----------|--------|
| INFO | Model inference success | Log only |
| WARNING | Inference latency > 2x target | Log + metric |
| ERROR | Single model failure | Alert + fallback activation |
| CRITICAL | Multiple model failures | Alert + system degradation |
| EMERGENCY | Complete system failure | Alert + classical control |

## Lifecycle Management

### Startup Sequence
1. Load configuration from CAOS config service
2. Initialize models via 95-20-01 Core Platform
3. Register capabilities with CAOS discovery
4. Start health check heartbeat
5. Begin accepting inference requests

### Shutdown Sequence
1. Stop accepting new inference requests
2. Complete in-flight inferences
3. Deregister from CAOS discovery
4. Save state and logs
5. Release compute resources

### Update Procedure
1. Receive update notification from CAOS
2. Validate update package signature
3. Load new model version
4. Run validation tests
5. Switch to new model (hot swap)
6. Archive old model version

## Documentation Links

- Service API Documentation: `Documentation/95-20-21-801_Operations_Manual.md`
- Interface Specifications: `ASSETS/Interface_Specs/`
- Model Cards: `ASSETS/Model_Cards/`
- Traceability: `00_META/95-20-21-012_ECS_NN_Traceability_Map.csv`

## Document Control

- **Version**: 1.0
- **Status**: WORKING
- **Last Updated**: 2025-11-17
- **Maintainer**: AMPEL360 Integration Team
- **Related**: 95-20-01 (Core Platform), 95-20-02 (DPP Blockchain)
