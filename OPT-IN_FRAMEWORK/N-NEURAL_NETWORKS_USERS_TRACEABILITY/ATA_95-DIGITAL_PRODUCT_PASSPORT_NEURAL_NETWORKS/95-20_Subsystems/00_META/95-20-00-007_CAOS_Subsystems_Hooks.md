# 95-20-00-007 — CAOS Subsystems Discovery Hooks

## Document Information

- **Document ID**: 95-20-00-007
- **Title**: CAOS/MCP Subsystems Discovery Hooks
- **Version**: 1.0
- **Date**: 2025-11-17
- **Status**: Active
- **Classification**: Technical Reference

## Purpose

This document defines how CAOS (Computer Aided Operations & Services) and MCP (Model Context Protocol) servers discover, register, and orchestrate the 95-20 Neural Network subsystems.

## Discovery Entry Point

**Primary Entry**: `95-20_Subsystems/00_META/95-20-00-006_Subsystem_Registry.json`

This JSON registry is the **single source of truth** for subsystem discovery.

## CAOS Discovery Flow

### Step 1: Bootstrap Discovery

```javascript
// CAOS reads the registry on startup
const registryPath = "95-20_Subsystems/00_META/95-20-00-006_Subsystem_Registry.json";
const registry = await loadRegistry(registryPath);

// Extract all active subsystems
const activeSubsystems = registry.subsystems.filter(s => s.status === "active");
```

### Step 2: Subsystem Capability Discovery

For each subsystem, CAOS reads its README.md to extract capabilities:

```javascript
for (const subsystem of activeSubsystems) {
  const readmePath = `95-20_Subsystems/${subsystem.id}_${subsystem.name}/README.md`;
  const capabilities = await extractCapabilities(readmePath);
  
  subsystem.capabilities = capabilities;
}
```

**Capability Manifest Format** (in each README.md):

```yaml
# Embedded in README.md frontmatter or metadata section
capabilities:
  - name: "temperature_prediction"
    endpoint: "/predict/cabin_temp"
    input_schema: "95-90-001_Sensor_Data_Schema_v1.json"
    output_schema: "95-90-002_Model_Output_Schema_v1.json"
    latency: "10ms"
    criticality: "DAL-C"
  - name: "air_quality_monitoring"
    endpoint: "/monitor/air_quality"
    ...
```

### Step 3: Dependency Resolution

```javascript
// Build dependency graph
const dependencyGraph = buildDependencyGraph(activeSubsystems);

// Topological sort for initialization order
const initOrder = topologicalSort(dependencyGraph);

// Example order: [95-20-01, 95-20-02, 95-20-42, 95-20-27, ...]
```

### Step 4: Runtime Registration

```javascript
for (const subsystemId of initOrder) {
  const subsystem = registry.subsystems.find(s => s.id === subsystemId);
  
  // Verify 95-20-01 (Core Platform) has model available
  if (subsystemId !== "95-20-01") {
    await verifyModelAvailability(subsystem, corePlatform);
  }
  
  // Register with CAOS orchestrator
  await caos.register(subsystem);
  
  // Subscribe to subsystem events
  await caos.subscribe(subsystem.endpoints.mcp);
}
```

## MCP Server Integration

### MCP Discovery Protocol

MCP servers implement the following discovery pattern:

```json
{
  "mcp_version": "1.0",
  "discovery": {
    "method": "file-based",
    "entry_point": "95-20_Subsystems/00_META/95-20-00-006_Subsystem_Registry.json",
    "capability_manifests": "95-20_Subsystems/95-20-XX_*/README.md",
    "dependency_matrix": "95-20_Subsystems/95-20-00-003_Cross_ATA_Dependencies.csv"
  }
}
```

### MCP Endpoint Standard

Each subsystem exposes these standardized MCP endpoints:

#### 1. Capability Endpoint

```
GET /.well-known/mcp/capability.json

Response:
{
  "subsystem_id": "95-20-27",
  "name": "NN_Flight_Controls",
  "version": "2.1.0",
  "capabilities": [
    {
      "name": "aerodynamic_prediction",
      "type": "inference",
      "model": "CFD_Surrogate_v2.1",
      "input": {
        "schema": "95-90-027-Input-v1.json",
        "rate": "100Hz"
      },
      "output": {
        "schema": "95-90-027-Output-v1.json",
        "latency": "5ms"
      }
    }
  ]
}
```

#### 2. Health Endpoint

```
GET /health

Response:
{
  "status": "healthy",
  "subsystem_id": "95-20-27",
  "checks": {
    "model_loaded": true,
    "dependencies_available": true,
    "resource_usage": {
      "cpu": "28%",
      "memory": "230MB/256MB"
    }
  },
  "last_check": "2025-11-17T21:24:00Z"
}
```

#### 3. Metrics Endpoint

```
GET /metrics

Response (Prometheus format):
# HELP nn_inference_duration_seconds Time spent in model inference
# TYPE nn_inference_duration_seconds histogram
nn_inference_duration_seconds_bucket{subsystem="95-20-27",le="0.001"} 1024
nn_inference_duration_seconds_bucket{subsystem="95-20-27",le="0.01"} 15328
...
```

#### 4. Models Endpoint

```
GET /v1/models

Response:
{
  "models": [
    {
      "id": "CFD_Surrogate_v2.1",
      "status": "active",
      "registry_entry": "95-20-01/models/CFD_Surrogate_v2.1",
      "provenance": "95-20-02/chain/0x7a3b...9f2e",
      "deployed_at": "2025-11-15T10:30:00Z"
    }
  ]
}
```

## Hooks for Real-Time Orchestration

### Pre-Flight Hook

**Trigger**: Before each flight

```javascript
async function preFlightHook() {
  // 1. Verify all DAL-A/B subsystems are healthy
  const criticalSubsystems = registry.subsystems.filter(
    s => s.criticality === "DAL-A" || s.criticality === "DAL-B"
  );
  
  for (const subsystem of criticalSubsystems) {
    const health = await fetch(`${subsystem.endpoints.health}`);
    if (health.status !== "healthy") {
      throw new Error(`Subsystem ${subsystem.id} not healthy`);
    }
  }
  
  // 2. Verify model versions match EIS baseline
  const eisVersion = await getEISVersion(); // from 95-00-11
  await verifyModelVersions(eisVersion);
  
  // 3. Load flight-specific configuration
  await loadFlightConfig();
}
```

### In-Flight Hook

**Trigger**: Continuous during flight

```javascript
async function inFlightMonitoring() {
  // Monitor all active subsystems
  for (const subsystem of activeSubsystems) {
    // Check for model drift
    const metrics = await fetch(`${subsystem.endpoints.metrics}`);
    if (detectDrift(metrics)) {
      await alertCrew(`Model drift detected in ${subsystem.name}`);
    }
    
    // Check for anomalies
    if (subsystem.id === "95-20-31") { // NN_Recording_Systems
      const anomalies = await subsystem.getAnomalies();
      if (anomalies.length > 0) {
        await notifyMaintenance(anomalies);
      }
    }
  }
}
```

### Post-Flight Hook

**Trigger**: After each flight

```javascript
async function postFlightHook() {
  // 1. Collect performance data from all subsystems
  const performanceData = await collectPerformanceData();
  
  // 2. Run 95-20-45 (Maintenance) analysis
  const maintenanceSubsystem = registry.subsystems.find(s => s.id === "95-20-45");
  const analysis = await maintenanceSubsystem.analyze(performanceData);
  
  // 3. Log to 95-20-02 (Blockchain) for provenance
  await blockchainLog(performanceData, analysis);
  
  // 4. Check for model update triggers
  if (analysis.suggestsUpdate) {
    await scheduleMaintenance(analysis.recommendations);
  }
}
```

## Event Subscription Hooks

### Event Types

CAOS subscribes to these event types from subsystems:

```javascript
const eventTypes = {
  MODEL_LOADED: "model.loaded",
  MODEL_UNLOADED: "model.unloaded",
  INFERENCE_COMPLETED: "inference.completed",
  ANOMALY_DETECTED: "anomaly.detected",
  DRIFT_DETECTED: "drift.detected",
  HEALTH_CHANGED: "health.changed",
  DEPENDENCY_FAILED: "dependency.failed"
};
```

### Event Handler Registration

```javascript
// CAOS registers handlers for each subsystem
for (const subsystem of activeSubsystems) {
  await caos.on(subsystem.id, eventTypes.ANOMALY_DETECTED, async (event) => {
    console.log(`Anomaly in ${subsystem.id}:`, event);
    await handleAnomaly(subsystem, event);
  });
  
  await caos.on(subsystem.id, eventTypes.DRIFT_DETECTED, async (event) => {
    console.log(`Drift in ${subsystem.id}:`, event);
    await handleDrift(subsystem, event);
  });
}
```

## Integration with 95-20-01 (Core Platform)

All subsystem orchestration flows through the Core Platform:

```
CAOS
  ↓ (discovery)
95-20-00-006_Subsystem_Registry.json
  ↓ (registration)
95-20-01 (Core Platform)
  ↓ (inference requests)
95-20-XX (Application Subsystems)
  ↓ (provenance logging)
95-20-02 (Blockchain)
```

### Core Platform API

```javascript
// CAOS uses Core Platform API for orchestration
const corePlatform = await caos.getSubsystem("95-20-01");

// Register new subsystem
await corePlatform.registerSubsystem({
  id: "95-20-27",
  modelId: "CFD_Surrogate_v2.1",
  partition: "P1",
  resources: { cpu: "30%", memory: "256MB" }
});

// Request inference
const result = await corePlatform.inference({
  subsystem: "95-20-27",
  model: "CFD_Surrogate_v2.1",
  input: sensorData
});

// Query model registry
const models = await corePlatform.listModels({
  subsystem: "95-20-27",
  status: "active"
});
```

## Configuration Management

### Environment-Specific Configuration

CAOS loads environment-specific configurations:

```json
{
  "environment": "production",
  "discovery": {
    "registry_path": "95-20_Subsystems/00_META/95-20-00-006_Subsystem_Registry.json",
    "refresh_interval": "60s"
  },
  "orchestration": {
    "max_concurrent_inferences": 100,
    "timeout": "5s",
    "retry_policy": {
      "max_retries": 3,
      "backoff": "exponential"
    }
  },
  "monitoring": {
    "metrics_interval": "10s",
    "health_check_interval": "30s",
    "drift_detection_threshold": 0.1
  }
}
```

### Per-Subsystem Configuration

Each subsystem can override defaults:

```yaml
# 95-20-27_NN_Flight_Controls/config.yaml
subsystem_id: "95-20-27"
override:
  timeout: "10ms"  # Stricter for flight-critical
  health_check_interval: "1s"  # More frequent
  failover:
    enabled: true
    fallback: "conventional_control_laws"
    switch_time: "10ms"
```

## Security & Authentication

### mTLS Authentication

All MCP endpoints require mutual TLS:

```javascript
const tlsConfig = {
  cert: await loadCert("95-20_Subsystems/certs/subsystem.crt"),
  key: await loadKey("95-20_Subsystems/certs/subsystem.key"),
  ca: await loadCA("95-20_Subsystems/certs/ca.crt")
};

const client = new MCPClient(subsystem.endpoints.mcp, tlsConfig);
```

### Authorization

Role-based access control (RBAC):

```json
{
  "roles": {
    "caos_orchestrator": {
      "permissions": ["read", "execute", "monitor"],
      "subsystems": ["all"]
    },
    "maintenance_engineer": {
      "permissions": ["read", "monitor"],
      "subsystems": ["95-20-45", "95-20-31"]
    },
    "flight_crew": {
      "permissions": ["read", "monitor"],
      "subsystems": ["95-20-27", "95-20-57", "95-20-70"]
    }
  }
}
```

## Failure Handling

### Subsystem Failure Recovery

```javascript
async function handleSubsystemFailure(subsystemId, error) {
  const subsystem = registry.subsystems.find(s => s.id === subsystemId);
  
  if (subsystem.criticality === "DAL-A") {
    // Flight-critical: immediate failover
    await triggerFailover(subsystem);
    await alertCrew(`Critical subsystem ${subsystem.name} failed`);
  } else if (subsystem.criticality === "DAL-B") {
    // Safety-significant: attempt restart
    const restarted = await attemptRestart(subsystem);
    if (!restarted) {
      await triggerFailover(subsystem);
    }
  } else {
    // DAL-C/D: log and continue
    await logFailure(subsystem, error);
    await scheduleMaintenanceCheck(subsystem);
  }
}
```

## References

- [95-20-00-001_Subsystems_Overview.md](../95-20-00-001_Subsystems_Overview.md) — Architecture
- [95-20-00-002_Subsystems_Integration_Map.md](../95-20-00-002_Subsystems_Integration_Map.md) — Integration
- [95-20-00-006_Subsystem_Registry.json](./95-20-00-006_Subsystem_Registry.json) — Registry
- [CAOS_OPERATIONS_FRAMEWORK](../../../../../CAOS/CAOS_OPERATIONS_FRAMEWORK.md) — CAOS architecture
- [MCP Specification](https://github.com/modelcontextprotocol/specification) — Model Context Protocol

## Document Control

- **Author**: AMPEL360 CAOS Integration Team
- **Reviewer**: Chief AI Operations Engineer
- **Approver**: Technical Director
- **Change Log**:
  - 2025-11-17: v1.0 — Initial discovery hooks specification

---

**Classification**: Technical Reference  
**Distribution**: Internal + CAOS Development Team
