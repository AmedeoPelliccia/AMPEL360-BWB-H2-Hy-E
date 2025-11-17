# DPP APIs and Interfaces

**Assembly ID**: 95-00-04-A060  
**Version**: 1.0
**Status**: WORKING

## Purpose

Defines external and internal API interfaces for the DPP+NN system.

## External APIs

### DPP Query API (RESTful)
```yaml
Base URL: https://api.ampel360.aero/dpp/v1
Authentication: OAuth 2.0 + JWT
Rate Limit: 1000 requests/hour

Endpoints:
  GET /models/{modelId}:
    description: Retrieve model metadata
    response: ModelInfo JSON
  
  GET /models/{modelId}/provenance:
    description: Full blockchain provenance chain
    response: ProvenanceChain JSON
  
  GET /aircraft/{aircraftId}/dpp:
    description: Complete digital product passport
    response: AircraftDPP JSON
  
  POST /compliance/verify:
    description: Verify regulatory compliance
    request: ComplianceQuery JSON
    response: ComplianceReport JSON
```

### Ground Operations API
```yaml
Base URL: https://ground-ops.ampel360.aero/v1
Authentication: mTLS + API Key

Endpoints:
  POST /deploy/model:
    description: Initiate model deployment
    request: DeploymentRequest JSON
  
  GET /fleet/status:
    description: Fleet-wide deployment status
    response: FleetStatus JSON
  
  POST /telemetry/upload:
    description: Upload aircraft telemetry
    request: TelemetryData (multipart)
```

## Internal Interfaces

### ARINC 653 Partition Interface
```
Protocol: ARINC 653 APEX (Application Executive)
Data Format: Binary structs with CRC32 checksums
Scheduling: Time-partitioned (10ms slots)
Safety Level: DAL B
```

### ARINC 665 Data Loader
```
Protocol: ARINC 665 (Aircraft Data Loader)
Security: Cryptographic signatures (ECDSA)
Transfer Rate: Up to 10 Mbps
Use Case: Model artifact deployment
```

## Cross-ATA Interfaces

- [ATA 02 Operations Interface](95-00-04-A061_ATA_02_Operations_Interface.md)
- [ATA 28 Fuel System Interface](95-00-04-A062_ATA_28_Fuel_System_Interface.md)
- [ATA 42 IMA Interface](95-00-04-A063_ATA_42_IMA_Interface.md)
- [ATA 45 Maintenance Interface](95-00-04-A064_ATA_45_Maintenance_Interface.md)

## Traceability

- **Requirements**: RQ-95-03-050, RQ-95-03-051
- **Parent Assembly**: 95-00-04-A001

---

**Document Control**: AI prompted by Amedeo Pelliccia | Status: WORKING
