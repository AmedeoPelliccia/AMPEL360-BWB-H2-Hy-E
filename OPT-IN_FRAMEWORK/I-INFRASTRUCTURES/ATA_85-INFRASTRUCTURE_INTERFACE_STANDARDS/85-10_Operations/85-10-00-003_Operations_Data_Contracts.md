# 85-10-00-003: Operations Data Contracts

## Document Information

- **Document ID**: 85-10-00-003  
- **Title**: Operations Data Contracts  
- **Version**: 1.0  
- **Status**: DRAFT  
- **Date**: 2025-11-21  

---

## 1. Purpose

This document defines the **operational data contracts** between:

- **Aircraft systems** (ATA 85 infrastructure interfaces)
- **Ground infrastructure** (airports, H₂/CO₂ providers)
- **GSE (Ground Support Equipment)**
- **Airline operations systems** (AOC, dispatch, maintenance)

These contracts ensure:
- **Interoperability** across diverse systems
- **Real-time coordination** during operations
- **Traceability** for compliance and continuous improvement
- **Consistency** in data formats, protocols, and semantics

---

## 2. Scope

### 2.1 In Scope

- Data structures and schemas for all ATA 85 operational interfaces
- Communication protocols and message formats
- Real-time data streaming and event-driven architectures
- Integration with ATA 02, 95, and 99 data systems
- Security, authentication, and data integrity requirements

### 2.2 Out of Scope

- Internal aircraft system data buses (covered in ATA 28, 31, etc.)
- Detailed maintenance data schemas (covered in ATA 01/03)
- Certification data requirements (covered in `85-00-10_Certification`)

---

## 3. Data Contract Principles

### 3.1 Design Principles

1. **Technology Agnostic**: Contracts are defined semantically; implementation can use JSON, XML, Protobuf, etc.
2. **Versioned**: All contracts include version identifiers for evolution
3. **Backward Compatible**: New versions maintain compatibility where feasible
4. **Self-Describing**: Include metadata for discoverability and validation
5. **Secure by Default**: Authentication, authorization, and encryption required

### 3.2 Contract Lifecycle

| **Stage** | **Activity** | **Owner** |
|-----------|------------|----------|
| **Define** | Contract specification | ATA 85 Ops + IT Leads |
| **Review** | Cross-ATA alignment | ATA 02, 95, 99 Leads |
| **Implement** | Integration development | System vendors |
| **Test** | Contract conformance testing | Certification Team |
| **Deploy** | Production rollout | Airline Ops |
| **Evolve** | Versioning and updates | ATA 85 Ops + IT Leads |

---

## 4. Core Data Entities

### 4.1 Interface Connection Status

**Purpose**: Report status of infrastructure interface connections.

**Schema**:
```json
{
  "interface_id": "string",           // Unique interface identifier (e.g., "H2-REFUEL-001")
  "interface_type": "enum",           // H2_REFUEL, CO2_BUFFER, GROUND_POWER, DATA_LINK, etc.
  "aircraft_id": "string",            // Aircraft tail number or registration
  "location_id": "string",            // Gate/stand identifier
  "status": "enum",                   // DISCONNECTED, CONNECTING, CONNECTED, ACTIVE, DISCONNECTING, FAULT
  "timestamp": "ISO8601",             // Event timestamp
  "metadata": {
    "connection_time": "ISO8601",     // When connection was established
    "last_activity": "ISO8601",       // Last data/activity on interface
    "health_score": "float"           // 0.0-1.0, overall interface health
  }
}
```

**Status Values**:
- `DISCONNECTED`: Interface not connected
- `CONNECTING`: Connection in progress
- `CONNECTED`: Physical/logical connection established, idle
- `ACTIVE`: Data/energy transfer in progress
- `DISCONNECTING`: Disconnect sequence in progress
- `FAULT`: Error condition detected

**Update Frequency**: On change (event-driven), heartbeat every 10 seconds

**Consumers**: ATA 02 Ops Systems, AOC, Digital Twin (ATA 95)

---

### 4.2 H₂ Refuelling Data

**Purpose**: Real-time H₂ refuelling operation data.

**Schema**:
```json
{
  "refuel_session_id": "string",      // Unique session identifier
  "aircraft_id": "string",
  "h2_source_id": "string",           // Ground H2 system identifier
  "start_time": "ISO8601",
  "end_time": "ISO8601",              // null if in progress
  "status": "enum",                   // PREPARING, FILLING, COMPLETING, COMPLETED, ABORTED, FAULT
  "tanks": [
    {
      "tank_id": "string",            // ATA 28 tank identifier
      "capacity_kg": "float",
      "initial_quantity_kg": "float",
      "current_quantity_kg": "float",
      "target_quantity_kg": "float",
      "pressure_bar": "float",
      "temperature_k": "float"
    }
  ],
  "flow_rate_kg_per_min": "float",
  "total_filled_kg": "float",
  "safety_checks": {
    "grounding_verified": "boolean",
    "leak_check_passed": "boolean",
    "pressure_within_limits": "boolean",
    "temperature_within_limits": "boolean"
  },
  "alerts": [
    {
      "alert_id": "string",
      "severity": "enum",             // INFO, WARNING, CRITICAL
      "message": "string",
      "timestamp": "ISO8601"
    }
  ]
}
```

**Update Frequency**: 1 Hz during active refuelling

**Consumers**: ATA 02 Turnaround System, ATA 28 Fuel Management, ATA 99 Carbon Accounting

**Cross-Reference**: `85-10-02_H2_Ground_Operations/85-10-02-002_H2_Interface_Sequence_and_Timing.md`

---

### 4.3 CO₂ Buffer Status

**Purpose**: CO₂ battery buffer state and logistics tracking.

**Schema**:
```json
{
  "buffer_id": "string",              // Unique buffer identifier (serial number)
  "aircraft_id": "string",            // Currently installed on (or null if in logistics)
  "status": "enum",                   // INSTALLED, IN_USE, DEPLETED, IN_TRANSIT, RECHARGING, CHARGED, FAULT
  "charge_level_percent": "float",    // 0.0-100.0
  "charge_capacity_kg_co2": "float",
  "current_charge_kg_co2": "float",
  "cycles_count": "integer",          // Lifecycle tracking
  "last_exchange_time": "ISO8601",
  "next_exchange_due": "ISO8601",     // Predicted based on usage
  "location": {
    "type": "enum",                   // AIRCRAFT, AIRPORT, RECHARGE_FACILITY
    "location_id": "string"
  },
  "carbon_credits_kg": "float",       // Associated carbon capture credits
  "health_metrics": {
    "temperature_k": "float",
    "pressure_bar": "float",
    "health_score": "float"           // 0.0-1.0
  }
}
```

**Update Frequency**: On change (event-driven), hourly status report

**Consumers**: ATA 02 Ops Planning, ATA 99 Carbon/Circularity System, Logistics Providers

**Cross-Reference**: `85-10-03_CO2_Battery_Ground_Operations/85-10-03-002_CO2_Buffer_Exchange_and_Recharge_Procedures.md`

---

### 4.4 Gate Connection Summary

**Purpose**: Aggregate status of all interfaces at gate/stand.

**Schema**:
```json
{
  "aircraft_id": "string",
  "gate_id": "string",
  "arrival_time": "ISO8601",
  "departure_time": "ISO8601",        // Scheduled
  "interfaces": [
    {
      "interface_type": "enum",
      "status": "enum",               // See 4.1
      "connected_time": "ISO8601",
      "last_update": "ISO8601"
    }
  ],
  "turnaround_status": "enum",        // ON_TIME, DELAYED, AHEAD
  "critical_path_interface": "string", // Interface currently delaying turnaround (if any)
  "estimated_ready_time": "ISO8601"   // When all interfaces will be disconnected
}
```

**Update Frequency**: 10 Hz during turnaround

**Consumers**: ATA 02 Turnaround Orchestration, AOC, Airport Control

**Cross-Reference**: `85-10-01_Turnaround_Interface_Management/85-10-01-002_Turnaround_Interface_Timelines_and_Milestones.md`

---

## 5. Event Streams

### 5.1 Interface Alert Stream

**Purpose**: Real-time alerting for interface anomalies.

**Message Format**:
```json
{
  "event_id": "string",               // UUID
  "event_type": "INTERFACE_ALERT",
  "timestamp": "ISO8601",
  "aircraft_id": "string",
  "interface_id": "string",
  "severity": "enum",                 // INFO, WARNING, CRITICAL
  "alert_code": "string",             // Standardized alert code (e.g., "H2-LEAK-001")
  "message": "string",
  "recommended_action": "string",
  "context": {
    // Additional diagnostic data
  }
}
```

**Delivery**: Pub/Sub or Kafka-style event stream

**Subscribers**: ATA 02 Ops Systems, AOC, Maintenance Systems, Digital Twin (ATA 95)

---

### 5.2 Interface Performance Metrics Stream

**Purpose**: Continuous performance monitoring for analytics and digital twin.

**Message Format**:
```json
{
  "event_id": "string",
  "event_type": "INTERFACE_METRICS",
  "timestamp": "ISO8601",
  "aircraft_id": "string",
  "interface_id": "string",
  "metrics": {
    "connection_duration_sec": "float",
    "data_transfer_bytes": "integer",
    "energy_transfer_kwh": "float",   // For power/H2 interfaces
    "errors_count": "integer",
    "latency_ms": "float",            // For data interfaces
    "throughput": "float"             // Units depend on interface type
  }
}
```

**Delivery**: Batch (every 60 seconds) or streaming

**Subscribers**: ATA 95 Digital Twin, ATA 99 Carbon Accounting, Performance Analytics

---

## 6. Communication Protocols

### 6.1 Real-Time Interfaces (Critical Operations)

**Use Cases**: H₂ refuelling control, safety interlocks, critical alerts

**Protocol**: **OPC UA** (Open Platform Communications Unified Architecture)
- **Rationale**: Industrial standard, real-time, security built-in, semantic modeling
- **Security**: TLS 1.3+, certificate-based authentication
- **Latency Target**: <100ms for critical safety signals

**Alternative**: **MQTT with QoS 2** for event-driven alerts
- **Security**: TLS 1.3+, token-based authentication

---

### 6.2 Bulk Data Transfer (Logs, Historical Data)

**Use Cases**: Post-flight data download, maintenance logs, performance history

**Protocol**: **HTTPS REST APIs**
- **Security**: OAuth 2.0 / API keys, TLS 1.3+
- **Format**: JSON (primary), Parquet/Avro for large datasets

**Alternative**: **SFTP** for large file transfers (compatibility with legacy systems)

---

### 6.3 Event Streaming (Analytics, Monitoring)

**Use Cases**: Real-time metrics, alerting, digital twin updates

**Protocol**: **Apache Kafka** or **Azure Event Hubs / AWS Kinesis**
- **Security**: SASL/SCRAM, TLS 1.3+
- **Retention**: 7-30 days (configurable)
- **Partitioning**: By aircraft_id for parallel processing

---

## 7. Data Security and Privacy

### 7.1 Authentication and Authorization

- **Aircraft ↔ Ground Infrastructure**: Mutual TLS (mTLS) with certificate pinning
- **Ground Systems ↔ Airline Systems**: OAuth 2.0 with JWT tokens
- **Human Operators**: Multi-factor authentication (MFA)

**Authorization Model**: Role-Based Access Control (RBAC)
- Roles: Operator, Supervisor, Maintenance, Analytics, Admin
- Permissions: Read, Write, Control (interface actuation)

### 7.2 Data Encryption

- **In Transit**: TLS 1.3 minimum for all communications
- **At Rest**: AES-256 encryption for stored operational data
- **Sensitive Data**: H₂ quantities, CO₂ credits, predictive maintenance insights

### 7.3 Data Retention and Privacy

- **Real-Time Data**: Retained for 7-30 days for operational needs
- **Aggregated Metrics**: Retained for 5 years for trend analysis
- **Personally Identifiable Information (PII)**: Not included in ATA 85 data contracts
- **Compliance**: GDPR, aviation data protection regulations

---

## 8. Data Validation and Quality

### 8.1 Schema Validation

All data exchanges must conform to published JSON Schema or Protobuf definitions.

**Validation Points**:
- **Producer**: Validate before publishing
- **Broker/Gateway**: Optional validation at API gateway
- **Consumer**: Validate on receipt, reject malformed data

### 8.2 Data Quality Metrics

| **Metric** | **Target** | **Action if Below Target** |
|-----------|-----------|---------------------------|
| **Completeness** | >99% | Alert data quality team |
| **Timeliness** | <10s latency for critical data | Escalate to operations |
| **Accuracy** | No out-of-range values | Reject and log error |
| **Consistency** | Cross-field validation passes | Flag for manual review |

### 8.3 Anomaly Detection

ATA 95 Digital Twin continuously monitors data for anomalies:
- Out-of-range values (e.g., negative H₂ quantity)
- Unexpected state transitions (e.g., CONNECTED → FAULT without intermediate states)
- Missing heartbeats (timeout detection)

**Action**: Generate alert, fallback to manual procedures if critical

---

## 9. Integration Patterns

### 9.1 Synchronous Request-Response

**Use Case**: Query current interface status before initiating operation

**Pattern**: REST API GET request
```http
GET /api/v1/interfaces/{interface_id}/status
Authorization: Bearer {token}
```

**Response**:
```json
{
  "interface_id": "H2-REFUEL-001",
  "status": "CONNECTED",
  ...
}
```

**SLA**: <500ms response time

---

### 9.2 Asynchronous Command-Response

**Use Case**: Initiate H₂ refuelling operation

**Pattern**: REST API POST request with async job
```http
POST /api/v1/interfaces/H2-REFUEL-001/start_refuel
Authorization: Bearer {token}
Content-Type: application/json

{
  "target_quantity_kg": 500.0,
  "max_flow_rate_kg_per_min": 10.0
}
```

**Response**:
```json
{
  "job_id": "refuel-job-12345",
  "status": "ACCEPTED",
  "status_url": "/api/v1/jobs/refuel-job-12345"
}
```

**Follow-up**: Poll status URL or subscribe to event stream for completion

---

### 9.3 Event-Driven Pub/Sub

**Use Case**: Real-time alert distribution

**Pattern**: Kafka topic subscription
```
Topic: interface-alerts
Partition: by aircraft_id
Consumer Group: aoc-monitoring
```

**Message**: See 5.1 Interface Alert Stream

**Acknowledgment**: At-least-once delivery, consumers must deduplicate if needed

---

## 10. Versioning Strategy

### 10.1 Contract Versioning

- **Format**: Semantic versioning (MAJOR.MINOR.PATCH)
  - **MAJOR**: Breaking changes (not backward compatible)
  - **MINOR**: New fields or enums (backward compatible)
  - **PATCH**: Bug fixes, clarifications

- **Example**: 
  - v1.0.0: Initial release
  - v1.1.0: Add new optional field `health_score`
  - v2.0.0: Rename field `status` → `connection_state` (breaking)

### 10.2 Transition Period

When introducing breaking changes (MAJOR version):
- **Announcement**: 6 months in advance
- **Parallel Support**: Both versions supported for 12 months
- **Deprecation**: Old version marked deprecated
- **Sunset**: Old version retired after transition period

### 10.3 Version Negotiation

Systems include version in API requests:
```http
GET /api/v2/interfaces/{interface_id}/status
Accept: application/vnd.ampel360.interface+json;version=2.0
```

---

## 11. Testing and Compliance

### 11.1 Contract Testing

- **Unit Tests**: Validate schema compliance in producer/consumer code
- **Integration Tests**: End-to-end data flow verification
- **Contract Tests**: Consumer-driven contract testing (e.g., Pact framework)

### 11.2 Conformance Testing

Before deployment, systems must pass conformance testing:
1. Schema validation (100% pass rate)
2. Protocol compliance (security, latency, throughput)
3. Error handling (graceful degradation)
4. Interoperability with reference implementation

### 11.3 Compliance Reporting

All data exchanges logged for compliance:
- Interface usage logs (retained 5 years)
- Audit trail for critical operations (H₂ refuel, safety interlocks)
- Traceability to certification requirements via GenCCC

---

## 12. Cross-References

### 12.1 Internal (ATA 85)

- `85-10-00-001_Operations_Interface_Overview.md` – Operational ConOps
- `85-10-00-002_Cross_ATA_Operations_Interface_Map.md` – ATA integration
- `85-10-01_Turnaround_Interface_Management/` – Turnaround data flows
- `85-10-02_H2_Ground_Operations/` – H₂ refuelling data
- `85-10-06_Real_Time_Monitoring_and_Alerts/` – Monitoring and alerting

### 12.2 External (Other ATAs)

- [ATA 02 – Operations Information](../../ATA_02-OPERATIONS_INFORMATION/) – Ops system integration
- [ATA 95 – Digital Product Passport & Neural Networks](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/) – Digital twin data
- [ATA 99 – Circularity & Carbon](../ATA_99-CIRCULARITY_CARBON/) – Carbon accounting data

### 12.3 Standards

- **OPC UA**: [IEC 62541](https://opcfoundation.org/about/opc-technologies/opc-ua/)
- **MQTT**: [ISO/IEC 20922](https://www.iso.org/standard/69466.html)
- **JSON Schema**: [Draft 2020-12](https://json-schema.org/)
- **OAuth 2.0**: [RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)

---

## 13. Status and Next Steps

### 13.1 Current Status

- **Phase**: Data contract definition (SKELETON)
- **Next Phase**: 
  - Detailed schema development (JSON Schema / Protobuf)
  - Reference implementation creation
  - Integration testing with ATA 02/95/99 systems

### 13.2 Planned Deliverables

1. Complete JSON Schema and Protobuf definitions
2. API specification (OpenAPI 3.0)
3. Reference implementation (Python/Java client libraries)
4. Contract testing framework
5. Conformance test suite

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-21.

---

**End of Document**
