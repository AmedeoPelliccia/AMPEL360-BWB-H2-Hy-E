# 95-00-05-00-003 Interface Taxonomy

**Document ID:** 95-00-05-00-003
**Title:** Interface Taxonomy and Classification
**Version:** 1.0.0
**Status:** APPROVED
**Date:** 2025-11-17

---

## 1. Overview

This document defines the classification system, naming conventions, and taxonomy for all interfaces in the AMPEL360 BWB H2-Hy-E AI/ML system.

---

## 2. Interface Categories

### 2.1 Category Hierarchy

```
Interfaces (95-00-05)
├── 00_META - Governance & Traceability
├── 01_DATA - Data Layer Interfaces
├── 02_MODEL - AI/ML Model Interfaces
├── 03_SYSTEM - Aircraft System Interfaces
├── 04_CERTIFICATION - Regulatory & Compliance Interfaces
├── 05_SECURITY - Security & Privacy Interfaces
└── 06_DPP_BLOCKCHAIN - Digital Product Passport & Blockchain Interfaces
```

### 2.2 Category Descriptions

| Category | Code | Purpose | Examples |
|----------|------|---------|----------|
| **META** | 00 | Cross-cutting governance, traceability, taxonomy | Registry, traceability matrix, CAOS hooks |
| **DATA** | 01 | Data sources, sinks, schemas, contracts, lineage | Sensor data, feature schemas, AFDX mapping |
| **MODEL** | 02 | AI/ML model I/O, APIs, inference pipelines | Input specs, ONNX runtime, model-to-model |
| **SYSTEM** | 03 | Aircraft systems, avionics, edge compute, ground | ATA 28 fuel, ARINC 825, IMA integration |
| **CERTIFICATION** | 04 | Regulatory APIs, explainability, audit, evidence | EASA/FAA interfaces, DO-178C evidence |
| **SECURITY** | 05 | Cybersecurity, privacy, access control, crypto | Zero Trust model, audit logs, key mgmt |
| **DPP_BLOCKCHAIN** | 06 | Blockchain provenance, smart contracts, supply chain | DPP data model, blockchain write/query |

---

## 3. Interface Types

### 3.1 By Communication Pattern

| Type | Description | Characteristics | Examples |
|------|-------------|-----------------|----------|
| **Synchronous** | Request-response, blocking | Real-time, tight coupling | Model inference API |
| **Asynchronous** | Message-based, non-blocking | Loose coupling, eventual consistency | Event streams, data ingestion |
| **Streaming** | Continuous data flow | High throughput, time-series | Sensor telemetry, video |
| **Batch** | Bulk data transfer | Scheduled, high volume | Training data export, logs |

### 3.2 By Protocol Layer

| Layer | Protocols | Use Cases |
|-------|-----------|-----------|
| **Application** | HTTP/REST, gRPC, GraphQL, MQTT | APIs, web services, IoT |
| **Transport** | TCP, UDP, AFDX, CAN | Reliable or fast data transfer |
| **Network** | IP, ARINC 664 | Routing, addressing |
| **Data Link** | Ethernet, ARINC 825, MIL-STD-1553 | Physical network access |

### 3.3 By Data Direction

| Direction | Description | Examples |
|-----------|-------------|----------|
| **Input** | Data flowing into AI/ML system | Sensor readings, flight phase |
| **Output** | Data produced by AI/ML system | Predictions, alerts, recommendations |
| **Bidirectional** | Request-response or duplex | Model API, query interface |
| **Broadcast** | One-to-many | System status, alarms |

### 3.4 By Criticality Level

| Level | Description | Safety Impact | Examples |
|-------|-------------|---------------|----------|
| **DAL A** | Catastrophic failure | Loss of aircraft | Flight-critical predictions |
| **DAL B** | Hazardous failure | Severe injury | Safety-critical sensor data |
| **DAL C** | Major failure | Discomfort, system degradation | Performance monitoring |
| **DAL D** | Minor failure | Nuisance | Maintenance recommendations |
| **DAL E** | No safety effect | Informational | Usage statistics |

---

## 4. Naming Convention

### 4.1 Document Naming

**Pattern:** `95-00-05-XX-ZZZ_Descriptive_Name.md`

**Components:**
- `95` - ATA Chapter (AI/ML Systems)
- `00` - Bucket (GENERAL)
- `05` - Lifecycle Phase (Interfaces)
- `XX` - Category (00-06, see Section 2.2)
- `ZZZ` - Sequence number (001-999)
- `Descriptive_Name` - Human-readable title

**Examples:**
- `95-00-05-01-001_Data_Sources_Catalog.md`
- `95-00-05-02-006_Model_API_Specification.yaml`
- `95-00-05-03-002_Avionics_Bus_Integration.md`

### 4.2 Asset Naming

**Pattern:** `95-00-05-XX-A-ZZZ_Descriptive_Name.ext`

**Additional Component:**
- `A` - Asset type designator

**Sub-sequences:**
- `001-099` - Primary assets (diagrams, specs)
- `101-199` - Secondary assets (schemas, models)
- `201-299` - Tertiary assets (samples, templates)

**Examples:**
- `95-00-05-01-A-001_Data_Flow_Diagram.svg`
- `95-00-05-02-A-101_H2_Predictor_Model_Card.yaml`
- `95-00-05-03-A-201_Sample_Input_Packet.bin`

### 4.3 Type Codes

| Code | Type | Extensions | Purpose |
|------|------|-----------|----------|
| _(none)_ | Document | .md, .yaml, .csv | Primary interface documentation |
| **A** | Asset | .svg, .png, .json, .bin, .drawio, .pdf | Supporting diagrams, schemas, samples |
| **T** | Test | .py, .js, .json | Test cases, scripts, fixtures |
| **R** | Reference | .pdf, .md | External standards, citations |
| **C** | Config | .yaml, .json, .toml | Configuration files, parameters |

---

## 5. Interface Attributes

### 5.1 Mandatory Attributes

Every interface must specify:

| Attribute | Description | Example |
|-----------|-------------|---------|
| **ID** | Unique identifier | 95-00-05-01-001 |
| **Name** | Short descriptive name | H2 Sensor Data Interface |
| **Version** | Semantic version | 1.2.3 |
| **Status** | Lifecycle status | ACTIVE, DEPRECATED, RETIRED |
| **Owner** | Responsible team/person | Data Engineering Team |
| **Stakeholders** | Affected parties | AI/ML Team, Avionics, Test |
| **Category** | Interface category | DATA (01) |
| **Type** | Communication pattern | Streaming, Synchronous |
| **Protocol** | Communication protocol | AFDX, HTTP/REST |
| **Criticality** | Safety level | DAL B |
| **Data Direction** | Input/Output/Bidirectional | Input |

### 5.2 Optional Attributes

| Attribute | Description | Example |
|-----------|-------------|---------|
| **Frequency** | Update rate | 10 Hz |
| **Latency** | Max acceptable delay | < 100 ms |
| **Throughput** | Data rate | 1 MB/s |
| **Reliability** | Delivery guarantee | At-least-once |
| **Authentication** | Auth method | mTLS, JWT |
| **Encryption** | Encryption requirement | TLS 1.3, AES-256 |

---

## 6. ICD Template Structure

### 6.1 Standard ICD Sections

```markdown
# [Document ID] [Interface Name]

**Metadata Block**

---

## 1. Introduction
  1.1 Purpose
  1.2 Scope
  1.3 Applicable Documents
  1.4 Definitions and Acronyms

## 2. Interface Overview
  2.1 System Context
  2.2 Interface Description
  2.3 Stakeholders
  2.4 Interface Attributes

## 3. Requirements
  3.1 Functional Requirements
  3.2 Performance Requirements
  3.3 Safety Requirements
  3.4 Security Requirements

## 4. Technical Specification
  4.1 Data Formats and Schemas
  4.2 Protocols and APIs
  4.3 Timing and Synchronization
  4.4 Error Handling
  4.5 State Management

## 5. Interface Behavior
  5.1 Normal Operations
  5.2 Initialization and Shutdown
  5.3 Error Conditions
  5.4 Degraded Modes

## 6. Examples
  6.1 Sample Data / Payloads
  6.2 Usage Scenarios
  6.3 Code Snippets

## 7. Verification and Validation
  7.1 Test Requirements
  7.2 Acceptance Criteria
  7.3 Verification Methods

## 8. Traceability
  8.1 Requirements Traceability
  8.2 Cross-References
  8.3 Change History

## 9. Appendices
  A. Detailed Schemas
  B. Protocol Specifications
  C. References
```

### 6.2 Metadata Block Template

```markdown
**Document ID:** 95-00-05-XX-YYY
**Title:** [Interface Name]
**Version:** X.Y.Z
**Status:** DRAFT | REVIEW | APPROVED | DEPRECATED
**Date:** YYYY-MM-DD
**Classification:** PUBLIC | INTERNAL | CONFIDENTIAL

---

## Document Control

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Prepared By** | [Name] | _Pending_ | YYYY-MM-DD |
| **Reviewed By** | [Name] | _Pending_ | YYYY-MM-DD |
| **Approved By** | [Name] | _Pending_ | YYYY-MM-DD |

### Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0.0 | YYYY-MM-DD | [Name] | Initial release |

---

## Interface Attributes

| Attribute | Value |
|-----------|-------|
| **ID** | 95-00-05-XX-YYY |
| **Name** | [Interface Name] |
| **Category** | [DATA/MODEL/SYSTEM/etc.] |
| **Type** | [Sync/Async/Streaming/Batch] |
| **Protocol** | [HTTP/AFDX/CAN/etc.] |
| **Criticality** | [DAL A/B/C/D/E] |
| **Direction** | [Input/Output/Bidirectional] |
| **Owner** | [Team/Person] |
| **Stakeholders** | [List] |
```

---

## 7. Interface States and Lifecycle

### 7.1 Status Values

| Status | Description | Allowed Changes |
|--------|-------------|-----------------|
| **DRAFT** | Under development, not reviewed | → REVIEW, CANCELLED |
| **REVIEW** | Under stakeholder review | → DRAFT, APPROVED, CANCELLED |
| **APPROVED** | ICB approved, baseline | → ACTIVE, CANCELLED |
| **ACTIVE** | In production use | → DEPRECATED |
| **DEPRECATED** | Obsolete, migration underway | → RETIRED |
| **RETIRED** | No longer in use, archived | _(terminal)_ |
| **CANCELLED** | Development stopped | _(terminal)_ |

### 7.2 Lifecycle Transitions

```
DRAFT ──review──> REVIEW ──approval──> APPROVED ──deploy──> ACTIVE
  │                  │                      │
  └─────cancel───────┴──────cancel──────────┘

ACTIVE ──supersede──> DEPRECATED ──decommission──> RETIRED
```

---

## 8. Versioning

### 8.1 Semantic Versioning

**Format:** `MAJOR.MINOR.PATCH`

- **MAJOR:** Breaking changes, incompatible with previous version
- **MINOR:** Backward-compatible additions or enhancements
- **PATCH:** Backward-compatible bug fixes

**Examples:**
- `1.0.0` → `1.0.1` - Bug fix, fully compatible
- `1.0.1` → `1.1.0` - New optional field added
- `1.1.0` → `2.0.0` - Removed field, incompatible

### 8.2 Compatibility Policy

**Backward Compatibility:**
- PATCH: 100% compatible
- MINOR: Compatible (new features optional)
- MAJOR: May be incompatible

**Support Policy:**
- Current MAJOR version: Full support
- Previous MAJOR version: 6 months maintenance
- Older versions: Best effort, migration encouraged

**Deprecation:**
- Announce deprecation 3 months before MAJOR version
- Mark deprecated interfaces with warning
- Provide migration guide

---

## 9. Quality Standards

### 9.1 ICD Quality Checklist

- ✅ Follows naming convention (95-00-05-XX-YYY)
- ✅ Includes all mandatory metadata
- ✅ Uses standard ICD template structure
- ✅ Provides clear, unambiguous specifications
- ✅ Includes diagrams (system context, sequence, state)
- ✅ Contains sample data or payloads
- ✅ Documents all error conditions
- ✅ Specifies performance requirements (latency, throughput)
- ✅ Addresses security and access control
- ✅ Traceable to requirements (95-00-03)
- ✅ Reviewed by stakeholders
- ✅ Approved by ICB
- ✅ Passes MCP validation

### 9.2 Documentation Standards

**Language:**
- Use precise, technical language
- Define all acronyms on first use
- Use consistent terminology

**Formatting:**
- Markdown for text documents
- Draw.io source (.drawio) for diagrams
- Export to SVG/PNG for viewing
- JSON Schema for data structures
- OpenAPI for REST APIs

**Diagrams:**
- System context diagrams (C4 Level 1-2)
- Sequence diagrams for interactions
- State diagrams for stateful interfaces
- Data flow diagrams

---

## 10. Cross-References

### 10.1 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| 95-00-05-00-001 | Interface Management Plan | Governance framework |
| 95-00-05-00-002 | Change Control Process | Change management |
| 95-00-05-00-004 | Cross-ATA Interface Map | System integration |
| 95-00-05-00-005 | Interface Traceability Matrix | Requirements linkage |
| 95-00-05-00-006 | Interface Registry | Master catalog |

### 10.2 External Standards

| Standard | Title | Relevance |
|----------|-------|-----------|
| **ARINC 664 Part 7** | AFDX Specification | Avionics networking |
| **ARINC 825** | CAN Bus for Airborne Use | Fuel system interface |
| **DO-178C** | Software Airworthiness | Certification requirements |
| **DO-326A** | Airworthiness Security Process | Cybersecurity |
| **ISO/IEC 15288** | System Life Cycle Processes | Systems engineering |
| **OpenAPI 3.0** | API Specification | REST API documentation |
| **JSON Schema** | Data Validation | Schema definition |

---

## 11. Appendices

### Appendix A: Naming Convention Examples

**Data Interfaces:**
- `95-00-05-01-001_Data_Sources_Catalog.md`
- `95-00-05-01-A-001_Data_Flow_Diagram.svg`
- `95-00-05-01-A-101_H2_Sensor_Schema.json`

**Model Interfaces:**
- `95-00-05-02-001_Input_Specifications.md`
- `95-00-05-02-A-001_NN_IO_Architecture.svg`
- `95-00-05-02-A-101_H2_Predictor_Model_Card.yaml`

**System Interfaces:**
- `95-00-05-03-001_Aircraft_Systems_Interfaces.md`
- `95-00-05-03-A-001_System_IF_Architecture.pdf`
- `95-00-05-03-A-101_ATA_02_Context.svg`

### Appendix B: ICD Template File

See repository: `templates/ICD_Template.md`

### Appendix C: Asset Organization

```
ASSETS/
├── [Primary Assets] 001-099
│   ├── Architecture diagrams
│   ├── Flowcharts
│   └── Specifications
├── [Secondary Assets] 101-199
│   ├── Schemas (JSON, YAML)
│   ├── Model cards
│   └── API definitions
└── [Tertiary Assets] 201-299
    ├── Sample data
    ├── Templates
    └── Code examples
```

---

**End of Document**

**Next Review:** 2025-12-17
**Owner:** Systems Engineering / Interface Control Board
