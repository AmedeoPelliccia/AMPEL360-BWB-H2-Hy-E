# 02-90 Tables, Schemas, and Diagrams

## Purpose

ATA 02-90 serves as the **canonical location** for tables, schemas, and diagrams that support [ATA 02 Operations Information](../README.md) and enable cross-ATA integrations. This bucket consolidates:

- **Database schemas** (SQL, NoSQL) for operational data
- **API specifications** (OpenAPI, GraphQL, AsyncAPI) for service contracts
- **Data exchange formats** (AFDX, ARINC 429, Protobuf, JSON Schema)
- **System architecture diagrams** (C4 model, data flows, deployments)
- **Reference tables** (airports, configurations, performance tables)
- **ML/AI training dataset catalogs** with [DPP linkage](../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md)
- **Configuration manifests** (Kubernetes, Helm, Docker, Terraform)
- **Code lists and enumerations** (ICAO codes, message types, status codes)
- **Network and wiring diagrams** (AFDX topology, avionics networks)

## Scope

This is a **cross-ATA root bucket** present in every ATA chapter. For ATA 02, it supports:

- **Operations systems** ([02-20 Subsystems](../02-20_Subsystems/README.md))
- **Software applications** ([02-40 Software](../02-40_Software/README.md))
- **Propulsion data models** ([02-70 Propulsion](../02-70_Propulsion/README.md))
- **Energy monitoring schemas** ([02-80 Energy](../02-80_Energy/README.md))

All tables and schemas in 02-90 are **non-proprietary, synthetic, or example data** suitable for testing, prototyping, and documentation purposes.

## Internal Structure

```
02-90_Tables_Schemas_Diagrams/
├── 02-90-00-001_Tables_Schemas_Overview.md        # Organization and governance
├── 02-90-00-002_Data_Dictionary_Master.md         # Master data dictionary
├── 02-90-00-003_Diagram_Index.md                  # Index of all diagrams
├── 02-90-00-004_Schema_Version_Control.md         # Version control strategy
├── 02-90-01_Database_Schemas/                     # SQL/NoSQL schemas
├── 02-90-02_API_Specifications/                   # OpenAPI, GraphQL, AsyncAPI
├── 02-90-03_Data_Exchange_Formats/                # AFDX, ARINC, Protobuf
├── 02-90-04_System_Architecture_Diagrams/         # C4, data flows, integrations
├── 02-90-05_Reference_Tables/                     # Operational reference data
├── 02-90-06_ML_Training_Datasets/                 # ML dataset catalogs & DPP links
├── 02-90-07_Configuration_Manifests/              # K8s, Helm, Docker, Terraform
├── 02-90-08_Code_Lists_Enumerations/              # ICAO codes, system codes
└── 02-90-09_Wiring_Data_Network_Diagrams/         # Network topology, AFDX
```

Each subfolder contains:
- **README.md** – Purpose, scope, and usage guidance
- **Markdown documentation** – Structured guidelines and policies
- **ASSETS/** – Concrete files (SQL, YAML, JSON, SVG, diagrams)

## Naming Convention

Items within this bucket follow the pattern:
- **02-90-XX_DESCRIPTION**
  - 02 = ATA chapter
  - 90 = Bucket number
  - XX = Sequential number (00, 01, 02, etc.)
  - DESCRIPTION = Descriptive name

Asset files use:
- **02-90-XX-A-NNN_Description.ext**
  - A = Asset indicator
  - NNN = Asset sequential number
  - ext = File extension (sql, yaml, json, svg, etc.)

## Key Cross-References

- [02-00-05 Interfaces](../02-00_GENERAL/02-00-05_Interfaces/README.md) – Interface Control Documents
- [02-20 Subsystems](../02-20_Subsystems/README.md) – Operational subsystems using these schemas
- [02-40 Software](../02-40_Software/README.md) – Applications consuming APIs and data models
- [ATA 95 Digital Product Passport](../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md) – DPP integration for datasets
- [CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27) – Certification Specifications for Large Aeroplanes
- [DO-178C](https://en.wikipedia.org/wiki/DO-178C) – Software Considerations in Airborne Systems
- [EU AI Act](https://artificialintelligenceact.eu/) – AI governance and transparency requirements

## Governance

- **Data Quality**: All schemas and tables must be validated against defined quality checks
- **Version Control**: See [02-90-00-004 Schema Version Control](./02-90-00-004_Schema_Version_Control.md)
- **Change Control**: Schema changes require review by data governance board
- **Security**: No real operational data, credentials, or proprietary information in this bucket
- **Compatibility**: Breaking changes must be documented and versioned appropriately

## Status

- **Bucket**: 90_Tables_Schemas_Diagrams
- **Status**: Active
- **Applicability**: Universal (all ATA chapters)
- **Last Updated**: 2025-11-21

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---