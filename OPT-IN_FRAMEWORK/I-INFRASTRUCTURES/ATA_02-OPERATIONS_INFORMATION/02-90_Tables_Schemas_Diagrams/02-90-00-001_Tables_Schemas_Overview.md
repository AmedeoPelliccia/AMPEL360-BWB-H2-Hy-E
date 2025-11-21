# 02-90-00-001: Tables, Schemas, and Diagrams Overview

## 1. Purpose

This document provides a high-level overview of how tables, schemas, and diagrams are organized, governed, and consumed by ATA 02 Operations Information systems and cross-ATA integrations.

## 2. Organization Principles

### 2.1 Separation of Concerns

The 02-90 structure separates different types of data artifacts:

1. **Database Schemas** (02-90-01): Physical data storage definitions
2. **API Specifications** (02-90-02): Service contracts and interfaces
3. **Data Exchange Formats** (02-90-03): Avionics and ground system protocols
4. **Architecture Diagrams** (02-90-04): Visual representations of systems and flows
5. **Reference Tables** (02-90-05): Static operational data
6. **ML Training Datasets** (02-90-06): AI/ML data catalogs with provenance
7. **Configuration Manifests** (02-90-07): Infrastructure as code
8. **Code Lists** (02-90-08): Standardized enumerations
9. **Network Diagrams** (02-90-09): Physical and logical network topology

### 2.2 Governance Model

All schemas and tables in ATA 02-90 follow a three-tier governance model:

#### Tier 1: Strategic Governance
- **Data Governance Board**: Reviews breaking changes, deprecation policies
- **Architecture Review**: Ensures alignment with system architecture
- **Security Review**: Validates no sensitive data exposure

#### Tier 2: Tactical Governance
- **Schema Owners**: Domain experts responsible for specific schema areas
- **Change Control**: Versioning, compatibility, migration strategies
- **Quality Assurance**: Validation rules, data quality checks

#### Tier 3: Operational Governance
- **Version Control**: Git-based schema version management
- **CI/CD Integration**: Automated schema validation and deployment
- **Documentation**: Mandatory documentation for all schemas

### 2.3 Consumption Patterns

Schemas and tables are consumed by:

1. **Operations Systems** ([02-20 Subsystems](../02-20_Subsystems/README.md))
   - Flight operations databases
   - Performance monitoring systems
   - Energy management systems

2. **Software Applications** ([02-40 Software](../02-40_Software/README.md))
   - EFB applications ([02-40-11](../02-40_Software/02-40-11_EFB_Software/README.md))
   - Backend services ([02-40-12](../02-40_Software/02-40-12_Backend_Services/README.md))
   - Performance calculators ([02-40-13](../02-40_Software/02-40-13_Performance_Calculator/README.md))
   - Flight planning ([02-40-15](../02-40_Software/02-40-15_Flight_Planning_Software/README.md))
   - Analytics engines ([02-40-19](../02-40_Software/02-40-19_Analytics_Engine/README.md))

3. **Propulsion Systems** ([02-70 Propulsion](../02-70_Propulsion/README.md))
   - Propulsion telemetry data models
   - Performance data schemas

4. **Energy Systems** ([02-80 Energy](../02-80_Energy/README.md))
   - Energy monitoring schemas
   - Power distribution data models

5. **Cross-ATA Integrations**
   - [ATA 95 Digital Product Passport](../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md)
   - External systems (AOC, ANSP, airports)

## 3. Schema Types and Technologies

### 3.1 Database Technologies

| Technology | Use Case | Location |
|------------|----------|----------|
| PostgreSQL | Relational operational data | [02-90-01-001](./02-90-01_Database_Schemas/02-90-01-001_PostgreSQL_Schemas.sql) |
| TimescaleDB | Time-series telemetry | [02-90-01-002](./02-90-01_Database_Schemas/02-90-01-002_TimescaleDB_Hypertables.sql) |
| MongoDB | Semi-structured documents | [02-90-01-003](./02-90-01_Database_Schemas/02-90-01-003_MongoDB_Collections.json) |
| Redis | Caching and session state | [02-90-01-004](./02-90-01_Database_Schemas/02-90-01-004_Redis_Data_Structures.yaml) |

### 3.2 API Technologies

| Technology | Use Case | Location |
|------------|----------|----------|
| OpenAPI 3.0+ | REST APIs | [02-90-02 OpenAPI](./02-90-02_API_Specifications/ASSETS/OpenAPI/) |
| GraphQL | Flexible query interfaces | [02-90-02 GraphQL](./02-90-02_API_Specifications/ASSETS/GraphQL/) |
| AsyncAPI | Event streaming (Kafka, MQTT) | [02-90-02 AsyncAPI](./02-90-02_API_Specifications/ASSETS/AsyncAPI/) |

### 3.3 Data Exchange Formats

| Format | Use Case | Location |
|--------|----------|----------|
| AFDX Virtual Links | Avionics data bus | [02-90-03 AFDX](./02-90-03_Data_Exchange_Formats/ASSETS/AFDX/) |
| ARINC 429 | Legacy avionics interfaces | [02-90-03 ARINC](./02-90-03_Data_Exchange_Formats/ASSETS/ARINC_429/) |
| Protocol Buffers | High-performance telemetry | [02-90-03 Protobuf](./02-90-03_Data_Exchange_Formats/ASSETS/Protobuf/) |
| JSON Schema | Web and application data | [02-90-03 JSON](./02-90-03_Data_Exchange_Formats/ASSETS/JSON_Schema/) |

## 4. Version Control Strategy

All schemas follow semantic versioning (SemVer):

- **Major version** (X.0.0): Breaking changes requiring migration
- **Minor version** (x.Y.0): Backward-compatible additions
- **Patch version** (x.y.Z): Bug fixes and clarifications

See [02-90-00-004 Schema Version Control](./02-90-00-004_Schema_Version_Control.md) for detailed policies.

## 5. Data Quality and Validation

### 5.1 Quality Dimensions

All schemas must address:

1. **Completeness**: All required fields documented
2. **Consistency**: Naming conventions followed
3. **Accuracy**: Data types and constraints correct
4. **Validity**: Conformance to standards (SQL-92, OpenAPI 3.1, etc.)
5. **Timeliness**: Schemas updated with system changes

### 5.2 Validation Methods

- **Schema Linters**: Automated checks in CI/CD
- **Data Dictionary Alignment**: Cross-reference with [02-90-00-002](./02-90-00-002_Data_Dictionary_Master.md)
- **Integration Tests**: Schema compatibility validation
- **Documentation Reviews**: Human review of documentation completeness

## 6. Cross-ATA Integration Points

### 6.1 Integration with ATA 95 Digital Product Passport

ML training datasets ([02-90-06](./02-90-06_ML_Training_Datasets/README.md)) include:

- **Dataset provenance**: Source systems and transformations
- **Blockchain anchors**: Immutable references to [DPP](../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md)
- **Training lineage**: Tracking from raw data to trained models

### 6.2 Integration with Other ATAs

- **ATA 70/72 Propulsion**: Engine telemetry schemas align with [02-70](../02-70_Propulsion/README.md)
- **ATA 24 Electrical Power**: Energy schemas reference [02-80](../02-80_Energy/README.md)
- **ATA 34 Navigation**: Flight planning schemas compatible with navigation systems
- **ATA 46 Information Systems**: API contracts support cockpit displays and datalink

## 7. Security and Compliance

### 7.1 Data Sensitivity

All data in 02-90 must be:

- **Non-proprietary**: No OEM-confidential information
- **Non-operational**: No real airline operational data
- **Synthetic or anonymized**: Example data for testing only
- **Publicly safe**: Suitable for open collaboration

### 7.2 Regulatory Alignment

Schemas align with:

- [CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27) certification requirements
- [DO-178C](https://en.wikipedia.org/wiki/DO-178C) software development standards
- [DO-254](https://en.wikipedia.org/wiki/DO-254) hardware design standards
- [EU AI Act](https://artificialintelligenceact.eu/) transparency requirements for ML datasets

## 8. Usage Guidelines

### 8.1 For Schema Consumers

1. **Check version compatibility** before integration
2. **Review data dictionary** ([02-90-00-002](./02-90-00-002_Data_Dictionary_Master.md)) for field definitions
3. **Validate against schemas** using provided validation tools
4. **Subscribe to change notifications** for schema updates

### 8.2 For Schema Producers

1. **Follow naming conventions** defined in data dictionary
2. **Document all changes** with rationale and impact analysis
3. **Version schemas appropriately** using SemVer
4. **Provide migration guides** for breaking changes
5. **Update diagrams** ([02-90-00-003](./02-90-00-003_Diagram_Index.md)) when structures change

## 9. References

- [02-90 Main README](./README.md)
- [02-90-00-002 Data Dictionary Master](./02-90-00-002_Data_Dictionary_Master.md)
- [02-90-00-003 Diagram Index](./02-90-00-003_Diagram_Index.md)
- [02-90-00-004 Schema Version Control](./02-90-00-004_Schema_Version_Control.md)
- [ATA 02 Operations Information](../README.md)
- [AMPEL360 Documentation Standard](../../../../AMPEL360_DOCUMENTATION_STANDARD.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
