# 02-60_Storages – ATA 02 Operations Information Storage

## Purpose

This directory defines the comprehensive storage infrastructure architecture for AMPEL360 operations information systems. It encompasses all data storage layers from primary databases to edge storage, ensuring reliable, secure, and scalable storage for aviation operations, predictive analytics, and compliance requirements.

## Scope

The **02-60_Storages** section covers:

- **Primary Data Storage** ([02-60-01](#02-60-01_primary_data_storage)) – Production databases for operational and performance systems
- **Time-Series Storage** ([02-60-02](#02-60-02_time_series_storage)) – Telemetry and operational metrics storage
- **Object Storage** ([02-60-03](#02-60-03_object_storage)) – Documents, media, backups, and artifacts
- **Cache Storage** ([02-60-04](#02-60-04_cache_storage)) – High-speed caching layer (Redis, in-memory)
- **Backup Storage** ([02-60-05](#02-60-05_backup_storage)) – Backup and disaster recovery systems
- **Archive Storage** ([02-60-06](#02-60-06_archive_storage)) – Long-term cold storage and compliance archives
- **Document Storage** ([02-60-07](#02-60-07_document_storage)) – Technical publications and EFB documents
- **ML Model Storage** ([02-60-08](#02-60-08_ml_model_storage)) – Neural network models and training datasets
- **Edge Storage** ([02-60-09](#02-60-09_edge_storage)) – On-board and edge device storage
- **Distributed Storage** ([02-60-11](#02-60-11_distributed_storage)) – Cloud-native distributed storage clusters
- **Storage Security** ([02-60-12](#02-60-12_storage_security)) – Cross-cutting security for all storage tiers

## Relationship to Other ATA 02 Sections

- **[ATA 02-30 Circularity](../02-30_Circularity/)** – Data lifecycle management and sustainability
- **[ATA 02-40 Software](../02-40_Software/)** – Backend services that consume storage resources
- **[ATA 02-00 GENERAL](../02-00_GENERAL/)** – Overall operations information framework

## Storage Layers Overview

### Primary Storage Tiers

1. **Hot Storage** – SSD-based, low-latency access for operational data
2. **Warm Storage** – Balanced performance for recent historical data
3. **Cold Storage** – Cost-optimized for infrequent access
4. **Archive Storage** – Long-term retention for compliance

### Storage Types by Use Case

| Storage Type | Primary Use Cases | Key Technologies |
|--------------|-------------------|------------------|
| Primary DB | OLTP, configuration, reference data | PostgreSQL, SSD arrays |
| Time-Series | Telemetry, metrics, flight data | TimescaleDB, InfluxDB |
| Object | Documents, logs, backups | S3-compatible, MinIO |
| Cache | Sessions, hot keys, computed views | Redis, Memcached |
| Backup | DR, RPO/RTO compliance | Veeam, snapshots |
| Archive | Compliance, audit trails | Glacier, tape libraries |
| Document | Manuals, EFB content | Repository + search |
| ML Model | NN models, datasets, features | MLflow, DVC, registries |
| Edge | Aircraft, EFB local storage | DO-160 compliant SSDs |
| Distributed | Cloud-native clusters | Ceph, GlusterFS |

## Root-Level Documents

- **[02-60-00-001_Storage_Architecture_Overview.md](./02-60-00-001_Storage_Architecture_Overview.md)** – High-level architecture of all storage layers
- **[02-60-00-002_Storage_Capacity_Planning.md](./02-60-00-002_Storage_Capacity_Planning.md)** – Capacity planning methods and growth projections
- **[02-60-00-003_Data_Governance_Policy.md](./02-60-00-003_Data_Governance_Policy.md)** – Governance rules for data ownership and retention
- **[02-60-00-004_Storage_Metrics_Dashboard.yaml](./02-60-00-004_Storage_Metrics_Dashboard.yaml)** – Metrics and KPI definitions

## Internal Structure

Each storage subsystem (02-60-01 through 02-60-12) contains:

- **README.md** – Scope, purpose, and links to related systems
- **Architectural documents** – Logical and physical architecture
- **Configuration guides** – Setup and optimization procedures
- **ASSETS/** – Configurations, schemas, performance data, procedures

## Naming Convention

Items within this bucket follow the pattern:
- **02-60-XX-YYY_DESCRIPTION**
  - 02 = ATA chapter (Operations Information)
  - 60 = Bucket number (Storages)
  - XX = Storage subsystem (00=root, 01-12=specific types)
  - YYY = Sequential document number
  - DESCRIPTION = Descriptive name

## Compliance and Standards

Storage infrastructure adheres to:

- **[CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)** – Large Aeroplanes certification specifications
- **[DO-178C](https://www.rtca.org/content/standards-guidance-materials)** – Software considerations in airborne systems
- **[DO-254](https://www.rtca.org/content/standards-guidance-materials)** – Hardware considerations in airborne systems
- **[EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206)** – Artificial Intelligence regulatory framework
- **ISO 27001** – Information security management
- **GDPR** – Data protection and privacy

## Status

- **Bucket**: 60_Storages
- **Status**: Active
- **Applicability**: ATA 02 Operations Information
- **Last Updated**: 2025-11-21

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.