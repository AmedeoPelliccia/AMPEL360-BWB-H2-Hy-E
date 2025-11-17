# 95-00-01-007 — DPP Data Model and Identifiers

**Document ID**: 95-00-01-007  
**Version**: 1.0  
**Date**: 2025-11-17  
**Status**: Active

---

## 1. Introduction

This document specifies the data model and identification scheme for Digital Product Passports (DPPs) of neural networks in the AMPEL360 program. A consistent data model ensures interoperability, machine-readability, and long-term sustainability of DPP records.

---

## 2. DPP Identifier Scheme

### 2.1 Universally Unique Identifier (UUID)

Each neural network DPP is assigned a **UUID** (RFC 4122) for unambiguous global identification:

**Format**: 8-4-4-4-12 hexadecimal characters
**Example**: `550e8400-e29b-41d4-a716-446655440000`

**Generation**: UUIDv4 (random) for new models; UUIDv5 (name-based, SHA-1) for deterministic generation from model name and namespace.

**Usage**:
- Primary key in DPP database
- Referenced in aircraft configuration files
- Embedded in model metadata (ONNX models, TensorFlow SavedModel)

### 2.2 Human-Readable Model Name

In addition to UUID, each model has a **human-readable name**:

**Format**: `[System]_[Function]_[Architecture]_NN`

**Examples**:
- `FlightControl_PitchStability_LSTM_NN`
- `PredictiveMaint_BearingFault_CNN_NN`
- `EnergyOrch_BatterySOC_MLP_NN`

**Constraints**:
- Alphanumeric + underscore only
- Maximum 64 characters
- Unique within AMPEL360 program

### 2.3 Semantic Version Number

Each model version follows **Semantic Versioning 2.0.0** (semver.org):

**Format**: `MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]`

**Examples**:
- `1.0.0` — Initial certified release
- `1.1.0` — Minor update (retraining with expanded dataset)
- `2.0.0` — Major update (architecture change, breaking interface)
- `1.0.1-beta` — Pre-release version (testing phase)
- `1.2.3+20250601` — Build metadata (date: 2025-06-01)

**Versioning Rules**:
- **MAJOR**: Breaking changes (interface incompatibility, architecture redesign)
- **MINOR**: Backward-compatible enhancements (retraining, hyperparameter tuning)
- **PATCH**: Backward-compatible bug fixes (numerical stability, error handling)

### 2.4 Composite Identifier

The complete identifier combines UUID, name, and version:

**Full Identifier**: `UUID:Name:Version`

**Example**: `550e8400-e29b-41d4-a716-446655440000:FlightControl_PitchStability_LSTM_NN:1.2.0`

**Short Identifier (for human use)**: `Name:Version` (e.g., `FlightControl_PitchStability_LSTM_NN:1.2.0`)

---

## 3. DPP Data Model Schema

### 3.1 Core Metadata

```json
{
  "dpp_schema_version": "1.0",
  "uuid": "550e8400-e29b-41d4-a716-446655440000",
  "model_name": "FlightControl_PitchStability_LSTM_NN",
  "semantic_version": "1.2.0",
  "creation_date": "2025-06-15T14:30:00Z",
  "last_updated": "2025-11-17T09:15:00Z",
  "status": "Certified",
  "lifecycle_stage": "In-Service",
  "design_assurance_level": "B",
  "ata_chapter": "95",
  "related_ata_chapters": ["22", "27", "42"],
  "owner": {
    "name": "Jane Doe",
    "role": "Lead AI Engineer",
    "email": "jane.doe@ampel360.aero"
  }
}
```

### 3.2 Purpose & Scope

```json
{
  "purpose": {
    "description": "Adaptive pitch stability control for BWB aircraft",
    "use_cases": ["Normal flight envelope", "Turbulence mitigation"],
    "success_criteria": {
      "accuracy": "> 95%",
      "latency": "< 10 ms",
      "robustness": "< 5% degradation under perturbations"
    }
  },
  "operational_design_domain": {
    "altitude_range": {"min": 0, "max": 45000, "unit": "ft"},
    "airspeed_range": {"min": 120, "max": 450, "unit": "knots"},
    "temperature_range": {"min": -55, "max": 50, "unit": "°C"},
    "weather_conditions": ["VMC", "IMC"],
    "aircraft_configurations": ["clean", "takeoff", "landing"]
  }
}
```

### 3.3 Architecture & Design

```json
{
  "architecture": {
    "type": "LSTM",
    "layers": [
      {"type": "input", "shape": [10, 32]},
      {"type": "lstm", "units": 128, "activation": "tanh"},
      {"type": "dropout", "rate": 0.2},
      {"type": "dense", "units": 64, "activation": "relu"},
      {"type": "output", "units": 3, "activation": "linear"}
    ],
    "total_parameters": 123456,
    "trainable_parameters": 120000,
    "framework": "TensorFlow",
    "framework_version": "2.14.0"
  },
  "hardware_platform": {
    "inference_device": "NVIDIA Jetson AGX Xavier",
    "memory_footprint_mb": 512,
    "inference_latency_ms": 8.5,
    "power_consumption_w": 15
  }
}
```

### 3.4 Training Data

```json
{
  "training_data": {
    "dataset_name": "FlightSim_Pitch_v3.2",
    "dataset_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "dataset_version": "3.2",
    "dataset_checksum_sha256": "d2d2d2d2e5e5e5e5a1a1a1a1b3b3b3b3c4c4c4c4...",
    "size_samples": 500000,
    "size_gb": 12.3,
    "collection_date_range": {"start": "2024-01-01", "end": "2025-05-31"},
    "data_sources": ["Flight simulator", "Wind tunnel", "Flight test"],
    "labeling_method": "Automated from control laws",
    "split_ratios": {"train": 0.7, "validation": 0.15, "test": 0.15}
  }
}
```

### 3.5 Training Procedure

```json
{
  "training": {
    "training_date": "2025-06-10",
    "training_duration_hours": 18.5,
    "hyperparameters": {
      "optimizer": "Adam",
      "learning_rate": 0.001,
      "batch_size": 64,
      "epochs": 100,
      "early_stopping_patience": 10,
      "loss_function": "mean_squared_error"
    },
    "compute_infrastructure": {
      "gpu_type": "NVIDIA A100",
      "gpu_count": 4,
      "cpu_cores": 64,
      "memory_gb": 512,
      "data_center": "AWS us-east-1"
    },
    "carbon_footprint": {
      "energy_kwh": 120,
      "carbon_intensity_g_per_kwh": 350,
      "total_co2e_kg": 42
    }
  }
}
```

### 3.6 Validation Results

```json
{
  "validation": {
    "validation_date": "2025-06-12",
    "test_dataset": "FlightSim_Pitch_v3.2_test",
    "metrics": {
      "accuracy": 0.972,
      "rmse": 0.023,
      "mae": 0.015,
      "r2_score": 0.985
    },
    "robustness_testing": {
      "adversarial_perturbation_epsilon": 0.01,
      "accuracy_degradation": 0.03,
      "corner_cases_tested": 1500,
      "corner_cases_passed": 1485
    }
  }
}
```

### 3.7 Certification Status

```json
{
  "certification": {
    "authority": "EASA",
    "certificate_type": "Type Certificate",
    "certificate_number": "EASA.A.123",
    "issue_date": "2025-09-15",
    "expiry_date": null,
    "design_assurance_level": "B",
    "means_of_compliance": [
      {"id": "MoC-001", "standard": "CS 25.1309", "method": "Analysis + Test"},
      {"id": "MoC-002", "standard": "DO-178C (adapted)", "method": "V&V Campaign"}
    ],
    "certification_artifacts": [
      {"doc_id": "CERT-001", "title": "Safety Assessment Report", "path": "95-00-10/"},
      {"doc_id": "CERT-002", "title": "V&V Report", "path": "95-00-07/"}
    ]
  }
}
```

### 3.8 Operational History

```json
{
  "operational_history": {
    "entry_into_service": "2025-10-01",
    "fleet_deployment": {
      "aircraft_count": 25,
      "flight_hours": 15000,
      "flight_cycles": 7500
    },
    "performance_metrics": {
      "average_latency_ms": 8.2,
      "uptime_percent": 99.97,
      "false_alarm_rate": 0.008,
      "detected_out_of_odd_events": 3
    },
    "incidents": [
      {
        "date": "2025-11-05",
        "description": "ODD exceedance due to icing conditions",
        "severity": "Minor",
        "resolution": "Fallback to conventional control laws, no safety impact"
      }
    ]
  }
}
```

### 3.9 Dependencies

```json
{
  "dependencies": {
    "software_libraries": [
      {"name": "TensorFlow", "version": "2.14.0", "license": "Apache 2.0"},
      {"name": "NumPy", "version": "1.24.3", "license": "BSD"},
      {"name": "ONNX Runtime", "version": "1.15.1", "license": "MIT"}
    ],
    "hardware_dependencies": [
      {"component": "NVIDIA Jetson AGX Xavier", "part_number": "945-82972-0000-000"}
    ],
    "system_interfaces": [
      {"system": "Flight Control Computer", "protocol": "AFDX", "ata_chapter": "27"},
      {"system": "Air Data System", "protocol": "ARINC 429", "ata_chapter": "34"}
    ]
  }
}
```

### 3.10 Traceability Links

```json
{
  "traceability": {
    "requirements": [
      {"req_id": "REQ-FC-001", "description": "Pitch control accuracy", "doc_ref": "95-00-03/RTM.xlsx"},
      {"req_id": "REQ-FC-002", "description": "Latency constraint", "doc_ref": "95-00-03/RTM.xlsx"}
    ],
    "test_cases": [
      {"test_id": "TC-FC-101", "requirement": "REQ-FC-001", "status": "Passed", "doc_ref": "95-00-07/"},
      {"test_id": "TC-FC-102", "requirement": "REQ-FC-002", "status": "Passed", "doc_ref": "95-00-07/"}
    ],
    "design_artifacts": [
      {"artifact_id": "DES-001", "type": "Architecture Diagram", "path": "95-00-04/ASSETS/"}
    ]
  }
}
```

### 3.11 Sustainability Metrics

```json
{
  "sustainability": {
    "carbon_footprint": {
      "training_co2e_kg": 42,
      "inference_co2e_per_flight_g": 0.5,
      "lifecycle_co2e_kg": 55
    },
    "circular_economy": {
      "transfer_learning_parent": "BaseFlightControlNN:1.0.0",
      "reuse_percentage": 60,
      "planned_retirement_date": "2030-10-01",
      "archival_plan": "Long-term storage per 95-00-14 retention policy"
    }
  }
}
```

---

## 4. Data Formats & Serialization

### 4.1 Primary Format: JSON

DPPs are stored as **JSON** files for human-readability and wide tool support.

**File Naming**: `{UUID}_DPP_v{version}.json`

**Example**: `550e8400-e29b-41d4-a716-446655440000_DPP_v1.2.0.json`

### 4.2 Alternative Formats

**XML**: For integration with legacy systems (S1000D tools)
**YAML**: For version control (more human-friendly diffs)
**Protobuf**: For high-performance applications (runtime monitoring)

**Conversion**: Lossless conversion between JSON ↔ XML ↔ YAML ↔ Protobuf

### 4.3 Schema Validation

DPP JSON files validated against **JSON Schema**:

**Schema Location**: `OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/95-90_Tables_Schemas_Diagrams/DPP_Schema_v1.0.json`

**Validation Tool**: `ajv` (Another JSON Schema Validator) integrated into CI/CD pipeline

---

## 5. Database Storage

### 5.1 Relational Database Schema (PostgreSQL)

**Tables**:

```sql
CREATE TABLE dpp_models (
  uuid UUID PRIMARY KEY,
  model_name VARCHAR(64) UNIQUE NOT NULL,
  semantic_version VARCHAR(32) NOT NULL,
  status VARCHAR(32),
  lifecycle_stage VARCHAR(32),
  ata_chapter VARCHAR(10),
  owner_name VARCHAR(128),
  creation_date TIMESTAMP,
  last_updated TIMESTAMP,
  dpp_json JSONB  -- Full DPP as JSONB for querying
);

CREATE TABLE dpp_versions (
  id SERIAL PRIMARY KEY,
  model_uuid UUID REFERENCES dpp_models(uuid),
  version VARCHAR(32),
  version_date TIMESTAMP,
  changelog TEXT,
  dpp_json JSONB
);

CREATE TABLE dpp_traceability (
  id SERIAL PRIMARY KEY,
  model_uuid UUID REFERENCES dpp_models(uuid),
  requirement_id VARCHAR(32),
  test_case_id VARCHAR(32),
  certification_artifact VARCHAR(128)
);
```

### 5.2 Graph Database (Neo4j)

For complex traceability queries (e.g., "Find all models affected by a requirement change"):

**Nodes**: Model, Requirement, TestCase, CertificationArtifact, Dataset
**Relationships**: SATISFIES, TESTS, CERTIFIES, USES_DATA, DERIVED_FROM

**Example Query** (Cypher):
```cypher
MATCH (m:Model)-[:SATISFIES]->(r:Requirement)
WHERE r.id = 'REQ-FC-001'
RETURN m.name, m.version
```

---

## 6. Data Access & APIs

### 6.1 RESTful API

**Base URL**: `https://dpp.ampel360.aero/api/v1/`

**Endpoints**:

- `GET /models` — List all models
- `GET /models/{uuid}` — Retrieve specific model DPP
- `GET /models/{uuid}/versions` — List all versions of a model
- `POST /models` — Create new DPP (requires auth)
- `PUT /models/{uuid}` — Update DPP (requires auth + CCB approval)
- `DELETE /models/{uuid}` — Retire model (soft delete, requires auth)

**Authentication**: OAuth 2.0 (role-based access control)

**Response Format**: JSON (with `Content-Type: application/json`)

### 6.2 GraphQL API

For flexible querying:

```graphql
query {
  model(uuid: "550e8400-e29b-41d4-a716-446655440000") {
    name
    version
    status
    certification {
      authority
      certificateNumber
    }
    traceability {
      requirements {
        id
        description
      }
    }
  }
}
```

### 6.3 Access Control

**Roles**:
- **Public**: Read-only access to non-proprietary metadata (name, purpose, certification status)
- **Partner**: Read access to interface specifications, operational guidance
- **Internal**: Full read/write access
- **Admin**: Database administration, user management

**Implementation**: Role-based access control (RBAC) via Keycloak

---

## 7. Data Integrity & Security

### 7.1 Checksums

All DPP JSON files include SHA-256 checksum for integrity verification:

```json
{
  "dpp_checksum": {
    "algorithm": "SHA-256",
    "value": "d5d5d5d5e6e6e6e6a2a2a2a2b4b4b4b4c5c5c5c5..."
  }
}
```

### 7.2 Digital Signatures

High-risk models (DAL A/B) digitally signed by Configuration Manager:

**Signing Standard**: XML Signature (XMLDsig) or JWS (JSON Web Signature)

**Public Key Infrastructure (PKI)**: AMPEL360 internal CA

### 7.3 Encryption

DPPs containing proprietary information encrypted at rest (AES-256) and in transit (TLS 1.3).

---

## 8. Version Control Integration

### 8.1 Git Repository

DPP JSON files stored in Git for version history:

**Repository**: `<internal-repository-url>` (private)

**Branch Strategy**:
- `main` — Certified models (production)
- `develop` — Models in development
- `feature/*` — Experimental models

**Commit Message Format**: `[DPP] {model_name}:{version} - {description}`

**Example**: `[DPP] FlightControl_PitchStability_LSTM_NN:1.2.0 - Updated training data to v3.2`

### 8.2 Tagging

Each certified model version tagged:

**Tag Format**: `{model_name}-v{version}`

**Example**: `FlightControl_PitchStability_LSTM_NN-v1.2.0`

---

## 9. Data Retention & Archival

### 9.1 Retention Policy

- **Active Models**: Indefinite retention in production database
- **Retired Models**: 10 years minimum (regulatory requirement)
- **Historical Versions**: All versions retained for traceability

### 9.2 Archival Format

Long-term archival uses **open standards** to ensure future accessibility:

- JSON (human-readable)
- PDF/A-3 (ISO 19005-3) — Includes embedded JSON
- XML (with XSD schema)

**Storage**: Cold storage (AWS S3 Glacier) with 99.999999999% durability

---

## 10. Data Quality Assurance

### 10.1 Completeness Checks

Automated validation ensures all mandatory fields populated:

**Mandatory Fields**: UUID, model_name, version, status, lifecycle_stage, owner, architecture, training_data, validation

**Tool**: Custom Python script + JSON Schema validation

### 10.2 Consistency Checks

Cross-references validated:

- All referenced requirements exist in requirements database
- All test case IDs match test case repository
- All traceability links bidirectional

**Tool**: Graph database queries (Neo4j)

### 10.3 Audit Trail

All DPP modifications logged:

```json
{
  "audit_log": [
    {
      "timestamp": "2025-11-17T10:00:00Z",
      "user": "john.smith@ampel360.aero",
      "action": "UPDATE",
      "fields_changed": ["validation.metrics.accuracy"],
      "old_value": 0.970,
      "new_value": 0.972,
      "reason": "Updated with latest test results"
    }
  ]
}
```

---

## 11. Document Control

| Version | Date       | Author                 | Changes                                |
| ------- | ---------- | ---------------------- | -------------------------------------- |
| 1.0     | 2025-11-17 | AMPEL360 Documentation | Initial release — Data Model & IDs     |

---

### Document Metadata

- **Originator**: AI prompted by Amedeo Pelliccia
- **Toolchain**: GitHub Copilot + AMPEL360 Documentation Standards
- **Status**: `WORKING`
- **Notes**: This document was generated with AI assistance and must be reviewed and approved by a designated human checker/approver before being used as an official baseline.

---

**Previous Document**: [95-00-01-006_DPP_Roles_and_Responsibilities.md](95-00-01-006_DPP_Roles_and_Responsibilities.md)

**Next Document**: [95-00-01-008_DPP_Scope_Limitations_and_Exclusions.md](95-00-01-008_DPP_Scope_Limitations_and_Exclusions.md)

**Parent**: [95-00-01_Overview README](README.md)
