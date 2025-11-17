# 95-20-27-014 — CAOS FCS_NN Hooks

**Document ID:** 95-20-27-014  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active

---

## 1. Purpose

This document describes how the CAOS (Computer-Aided Operations System) / MCP (Model Context Protocol) server discovers and interacts with the FCS_NN subsystem.

---

## 2. MCP Endpoint Discovery

### 2.1 Capability Descriptor

**Location**: `/.well-known/mcp/capability.json`

```json
{
  "subsystem_id": "95-20-27",
  "subsystem_name": "NN_Flight_Controls",
  "version": "1.0.0",
  "mcp_version": "1.0",
  "base_url": "https://ampel360.local/api/fcs_nn",
  
  "capabilities": [
    {
      "name": "real_time_inference",
      "description": "Real-time neural network inference for flight control",
      "endpoint": "/v1/predict",
      "methods": ["POST"],
      "rate_limit": "100 Hz per model"
    },
    {
      "name": "health_monitoring",
      "description": "Subsystem health and performance monitoring",
      "endpoint": "/health",
      "methods": ["GET"],
      "rate_limit": "1 Hz"
    },
    {
      "name": "model_registry",
      "description": "Query active models and their metadata",
      "endpoint": "/v1/models",
      "methods": ["GET"],
      "rate_limit": "10/min"
    },
    {
      "name": "performance_metrics",
      "description": "Real-time performance metrics and telemetry",
      "endpoint": "/metrics",
      "methods": ["GET"],
      "rate_limit": "10/min"
    },
    {
      "name": "configuration",
      "description": "Runtime configuration and parameters",
      "endpoint": "/v1/config",
      "methods": ["GET", "PUT"],
      "rate_limit": "1/min"
    }
  ],
  
  "authentication": {
    "type": "mTLS",
    "cert_authority": "AMPEL360_IMA_CA",
    "required_claims": ["subsystem:fcs_nn"]
  },
  
  "dependencies": [
    {
      "subsystem_id": "95-20-01",
      "subsystem_name": "NN_Core_Platform",
      "purpose": "Model deployment and inference runtime"
    },
    {
      "subsystem_id": "95-20-02",
      "subsystem_name": "NN_DPP_Blockchain",
      "purpose": "Model provenance and audit trail"
    },
    {
      "subsystem_id": "95-20-42",
      "subsystem_name": "NN_IMA_Integration",
      "purpose": "Compute resources and partitioning"
    }
  ],
  
  "metadata": {
    "parent_ata": "ATA-27",
    "criticality": "DAL-A",
    "deployment_environment": "IMA Partition",
    "documentation_base": "../Documentation/",
    "assets_base": "../ASSETS/"
  }
}
```

---

## 3. API Endpoints

### 3.1 Health Monitoring

**Endpoint**: `/health`

**Method**: `GET`

**Response**:
```json
{
  "status": "healthy",
  "timestamp": "2025-11-17T12:34:56Z",
  "uptime_seconds": 86400,
  
  "models": {
    "aero_predictor_v2.1": {
      "status": "active",
      "health_score": 98,
      "last_inference_ms": 2.8,
      "inferences_per_second": 100
    },
    "control_surface_optimizer_v1.4": {
      "status": "active",
      "health_score": 97,
      "last_inference_ms": 6.2,
      "inferences_per_second": 100
    },
    "gust_load_alleviation_v1.3": {
      "status": "active",
      "health_score": 99,
      "last_inference_ms": 4.5,
      "inferences_per_second": 100
    },
    "envelope_protection_v1.0": {
      "status": "active",
      "health_score": 100,
      "last_inference_ms": 3.1,
      "inferences_per_second": 100
    },
    "flight_path_stabilization_v1.1": {
      "status": "active",
      "health_score": 96,
      "last_inference_ms": 9.8,
      "inferences_per_second": 10
    }
  },
  
  "ima_partition": {
    "partition_id": "FCS_NN_P1",
    "cpu_usage_percent": 45,
    "memory_usage_mb": 52,
    "memory_limit_mb": 68
  },
  
  "alerts": []
}
```

### 3.2 Model Inference

**Endpoint**: `/v1/predict`

**Method**: `POST`

**Request**:
```json
{
  "model_id": "aero_predictor_v2.1",
  "inputs": {
    "alpha_deg": 5.2,
    "beta_deg": -0.3,
    "mach": 0.78,
    "delta_e_deg": -2.1,
    "delta_a_deg": 0.5,
    "delta_r_deg": 0.2,
    "delta_f_deg": 0.0,
    "pitch_rate_dps": 1.2,
    "roll_rate_dps": 0.8,
    "yaw_rate_dps": -0.1,
    "altitude_ft": 35000,
    "tas_kt": 450
  },
  "request_id": "abc123",
  "timestamp_us": 1700234567890123
}
```

**Response**:
```json
{
  "model_id": "aero_predictor_v2.1",
  "request_id": "abc123",
  "outputs": {
    "CL": 0.62,
    "CD": 0.028,
    "Cm": -0.015,
    "Cn": 0.002,
    "Cy": -0.008,
    "Cl": 0.004
  },
  "confidence": 0.98,
  "inference_time_ms": 2.7,
  "timestamp_us": 1700234567892893
}
```

### 3.3 Model Registry

**Endpoint**: `/v1/models`

**Method**: `GET`

**Response**:
```json
{
  "models": [
    {
      "model_id": "aero_predictor_v2.1",
      "name": "Aerodynamic Predictor",
      "version": "2.1.0",
      "type": "PINN",
      "status": "active",
      "deployed_date": "2025-10-15T08:00:00Z",
      "model_card_url": "/assets/model_cards/95-20-27-A-101_Aero_Predictor_v2.1.yaml",
      "input_dimensions": 12,
      "output_dimensions": 6,
      "inference_rate_hz": 100,
      "avg_latency_ms": 2.8,
      "model_size_mb": 4.2
    },
    {
      "model_id": "control_surface_optimizer_v1.4",
      "name": "Control Surface Optimizer",
      "version": "1.4.0",
      "type": "PPO/RL",
      "status": "active",
      "deployed_date": "2025-09-20T10:30:00Z",
      "model_card_url": "/assets/model_cards/95-20-27-A-102_Control_Surface_Optimizer_v1.4.yaml",
      "input_dimensions": 18,
      "output_dimensions": 8,
      "inference_rate_hz": 100,
      "avg_latency_ms": 6.2,
      "model_size_mb": 8.7
    }
  ],
  "total_models": 5
}
```

### 3.4 Performance Metrics

**Endpoint**: `/metrics`

**Method**: `GET`

**Response** (Prometheus format):
```
# HELP fcs_nn_inference_latency_ms Inference latency in milliseconds
# TYPE fcs_nn_inference_latency_ms histogram
fcs_nn_inference_latency_ms_bucket{model="aero_predictor_v2.1",le="1"} 0
fcs_nn_inference_latency_ms_bucket{model="aero_predictor_v2.1",le="2"} 1234
fcs_nn_inference_latency_ms_bucket{model="aero_predictor_v2.1",le="5"} 98765
fcs_nn_inference_latency_ms_bucket{model="aero_predictor_v2.1",le="10"} 100000
fcs_nn_inference_latency_ms_sum{model="aero_predictor_v2.1"} 280000
fcs_nn_inference_latency_ms_count{model="aero_predictor_v2.1"} 100000

# HELP fcs_nn_health_score Model health score (0-100)
# TYPE fcs_nn_health_score gauge
fcs_nn_health_score{model="aero_predictor_v2.1"} 98
fcs_nn_health_score{model="control_surface_optimizer_v1.4"} 97
fcs_nn_health_score{model="gust_load_alleviation_v1.3"} 99
fcs_nn_health_score{model="envelope_protection_v1.0"} 100
fcs_nn_health_score{model="flight_path_stabilization_v1.1"} 96

# HELP fcs_nn_inferences_total Total number of inferences
# TYPE fcs_nn_inferences_total counter
fcs_nn_inferences_total{model="aero_predictor_v2.1"} 8640000
fcs_nn_inferences_total{model="control_surface_optimizer_v1.4"} 8640000
```

---

## 4. CAOS Discovery Process

### 4.1 Automatic Discovery

CAOS discovers the FCS_NN subsystem through:

1. **Subsystem Registry**: Registered in `../00_META/95-20-00-006_Subsystem_Registry.json`
2. **Well-Known Endpoint**: Query `/.well-known/mcp/capability.json`
3. **Service Mesh**: mDNS/DNS-SD advertising on IMA network
4. **Static Configuration**: Pre-configured in CAOS deployment manifest

### 4.2 Discovery Sequence

```
1. CAOS Boot
   ↓
2. Load Subsystem Registry
   ↓
3. For each subsystem:
   - Query /.well-known/mcp/capability.json
   - Validate mTLS certificate
   - Check dependencies
   ↓
4. Build Dependency Graph
   ↓
5. Initialize API Clients
   ↓
6. Start Health Monitoring
```

---

## 5. CAOS Integration Points

### 5.1 Model Deployment

CAOS orchestrates model deployment via:

- **95-20-01 NN Core Platform**: Model registry and versioning
- **95-20-42 NN IMA Integration**: Partition allocation and resource management
- **FCS_NN Subsystem**: Model loading and inference runtime

### 5.2 Monitoring and Alerting

CAOS continuously monitors FCS_NN:

- **Health Checks**: `/health` endpoint polled at 1 Hz
- **Performance Metrics**: `/metrics` scraped at 10s intervals
- **Anomaly Detection**: Statistical analysis of metrics
- **Alert Generation**: Crew alerts via EICAS/ECAM

### 5.3 Provenance Tracking

CAOS logs all FCS_NN activity to blockchain:

- **Model Inference**: Each inference logged with inputs/outputs
- **Configuration Changes**: All runtime config changes
- **Health Events**: Degradation, failures, recoveries
- **Model Updates**: Version changes, retraining

Integration via **95-20-02 NN DPP Blockchain**.

---

## 6. Event Notifications

### 6.1 WebSocket Stream

**Endpoint**: `/v1/events`

**Protocol**: WebSocket

**Events**:
```json
{
  "event_type": "health_change",
  "timestamp": "2025-11-17T12:34:56Z",
  "model_id": "aero_predictor_v2.1",
  "old_health_score": 98,
  "new_health_score": 85,
  "reason": "Increased latency variance"
}
```

```json
{
  "event_type": "envelope_protection_activation",
  "timestamp": "2025-11-17T12:35:12Z",
  "parameter": "alpha",
  "predicted_exceedance_time_ms": 800,
  "action_taken": "pitch_correction"
}
```

```json
{
  "event_type": "model_failover",
  "timestamp": "2025-11-17T12:36:45Z",
  "model_id": "control_surface_optimizer_v1.4",
  "reason": "inference_timeout",
  "fallback_mode": "conventional_fcs"
}
```

---

## 7. Configuration Management

### 7.1 Runtime Configuration

**Endpoint**: `/v1/config`

**Method**: `GET` / `PUT`

**Configuration Parameters**:
```json
{
  "gla_enabled": true,
  "gla_activation_threshold_turbulence_intensity": 20,
  "trim_optimizer_enabled": true,
  "trim_optimizer_update_rate_hz": 0.1,
  "envelope_protection_mode": "normal",
  "envelope_protection_margins": {
    "alpha_soft_deg": 20,
    "alpha_hard_deg": 25,
    "speed_margin_kt": 10
  },
  "logging_level": "info",
  "telemetry_rate_hz": 10
}
```

### 7.2 Configuration Changes

All configuration changes:
- **Validated**: Against schema and safety limits
- **Authorized**: Require maintenance credentials
- **Logged**: To blockchain provenance
- **Audited**: Post-flight review

---

## 8. Security

### 8.1 Authentication

- **mTLS**: Mutual TLS with AMPEL360_IMA_CA
- **Client Certificates**: Required for all API calls
- **Certificate Rotation**: Automatic 30-day rotation
- **Revocation**: Real-time CRL/OCSP checking

### 8.2 Authorization

- **Role-Based Access Control (RBAC)**:
  - `subsystem:fcs_nn:read`: Read model data, health, metrics
  - `subsystem:fcs_nn:infer`: Perform inference
  - `subsystem:fcs_nn:config`: Modify configuration
  - `subsystem:fcs_nn:admin`: Full administrative access

### 8.3 Audit Logging

All API calls logged with:
- Timestamp (microsecond precision)
- Client identity (certificate CN)
- Request/response payload (sanitized)
- Execution time
- Result (success/failure)

Logs streamed to **95-20-02 blockchain** for immutable audit trail.

---

## 9. References

- [95-20-27-001_FCS_NN_Overview.md](../95-20-27-001_FCS_NN_Overview.md)
- [95-20-01 NN Core Platform](../../95-20-01_NN_Core_Platform/)
- [95-20-02 NN DPP Blockchain](../../95-20-02_NN_DPP_Blockchain/)
- [95-20-42 NN IMA Integration](../../95-20-42_NN_IMA_Integration/)
- CAOS Architecture Documentation

---

## Document Control

- **Owner**: AMPEL360 CAOS Integration Team
- **Version**: 1.0
- **Status**: Active
- **Classification**: Technical Reference
- **Last Updated**: 2025-11-17
