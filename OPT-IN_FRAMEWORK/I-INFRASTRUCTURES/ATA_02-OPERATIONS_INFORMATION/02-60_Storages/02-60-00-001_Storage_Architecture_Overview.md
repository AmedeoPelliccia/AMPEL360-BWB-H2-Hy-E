# 02-60-00-001 – Storage Architecture Overview

## Purpose

This document provides a comprehensive overview of the AMPEL360 operations storage architecture, describing the overall structure, key storage layers, architectural patterns, and design principles that govern all data storage systems supporting the BWB-H₂-Hy-E aircraft operations.

---

## 1. Architecture Vision

The AMPEL360 storage infrastructure is designed to support:

- **Safety-critical operations** with high availability and disaster recovery
- **Real-time performance** for operational databases and caching
- **Scalability** from edge devices to cloud-scale distributed systems
- **Compliance** with aviation regulations and data protection laws
- **Cost optimization** through intelligent tiering and lifecycle management
- **Sustainability** aligned with [ATA 02-30 Circularity](../02-30_Circularity/) principles

---

## 2. Storage Architecture Layers

### 2.1 Primary Data Storage Layer

**Purpose**: Operational databases for transactional systems

- **Technology**: PostgreSQL on enterprise SSD arrays
- **RAID Strategy**: RAID-10 for OLTP, RAID-6 for data warehouses
- **High Availability**: Synchronous replication across availability zones
- **Performance Target**: < 5ms latency for 95th percentile
- **Capacity**: 50-100 TB primary, 200-500 TB data warehouse

**Key Systems**:
- Flight operations database
- Performance calculation data
- Weight & balance records
- Crew and dispatch systems

**Reference**: [02-60-01_Primary_Data_Storage](./02-60-01_Primary_Data_Storage/)

### 2.2 Time-Series Storage Layer

**Purpose**: Telemetry, metrics, and operational time-series data

- **Technology**: TimescaleDB (PostgreSQL extension), InfluxDB
- **Data Model**: Hypertables with time-based partitioning
- **Retention Policy**: Hot (7 days), Warm (90 days), Cold (2 years)
- **Compression**: 10:1 average compression ratio
- **Ingestion Rate**: 100K+ metrics/second sustained

**Key Data Streams**:
- Aircraft telemetry (sensor data, ACARS)
- Operations metrics (turnaround times, fuel consumption)
- H₂ system monitoring
- Predictive analytics inputs

**Reference**: [02-60-02_Time_Series_Storage](./02-60-02_Time_Series_Storage/)

### 2.3 Object Storage Layer

**Purpose**: Unstructured data, documents, backups, artifacts

- **Technology**: S3-compatible (MinIO, AWS S3, Azure Blob)
- **Buckets Organization**: Environment-based (prod, staging, dev, archive)
- **Lifecycle Policies**: Automatic transition to cold/archive tiers
- **Versioning**: Enabled for critical buckets with retention policies
- **Capacity**: Multi-petabyte scale

**Key Content Types**:
- EFB documents and manuals
- Flight logs and reports
- Video and media assets
- Software artifacts and container images
- Database backups

**Reference**: [02-60-03_Object_Storage](./02-60-03_Object_Storage/)

### 2.4 Cache Storage Layer

**Purpose**: High-speed in-memory caching for performance optimization

- **Technology**: Redis Cluster, Memcached
- **Architecture**: Multi-master with automatic failover
- **Eviction Policy**: LRU with TTL-based expiration
- **Hit Rate Target**: > 90% for session and computed data
- **Capacity**: 100-500 GB per cluster

**Cached Data**:
- User sessions and authentication tokens
- Frequently accessed reference data
- Pre-computed performance calculations
- API response caching

**Reference**: [02-60-04_Cache_Storage](./02-60-04_Cache_Storage/)

### 2.5 Backup Storage Layer

**Purpose**: Disaster recovery and business continuity

- **Strategy**: 3-2-1 rule (3 copies, 2 media types, 1 offsite)
- **RPO**: 15 minutes for critical systems
- **RTO**: 4 hours for primary systems, 24 hours for secondary
- **Backup Types**: Full, incremental, differential
- **Validation**: Automated monthly restore tests

**Backup Scope**:
- All production databases
- Configuration management systems
- Critical application data
- Infrastructure as Code (IaC) repositories

**Reference**: [02-60-05_Backup_Storage](./02-60-05_Backup_Storage/)

### 2.6 Archive Storage Layer

**Purpose**: Long-term compliance and regulatory retention

- **Technology**: Glacier-class storage, LTO-9 tape libraries
- **Retention Periods**: 5-25 years based on regulatory requirements
- **Retrieval SLA**: 4-24 hours for standard, 48-72 hours for tape
- **Immutability**: Write-once-read-many (WORM) for compliance
- **Compliance**: [EASA Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012), [FAA Part 121](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-G/part-121)

**Archived Data**:
- Flight operational records (25 years)
- Maintenance records (aircraft lifetime + 5 years)
- Training records (as per operator requirements)
- Certification evidence (indefinite)

**Reference**: [02-60-06_Archive_Storage](./02-60-06_Archive_Storage/)

### 2.7 Document Storage Layer

**Purpose**: Technical publications and EFB content management

- **Technology**: Document repository with full-text search (Elasticsearch)
- **Standards**: [S1000D](http://www.s1000d.org/) for technical publications
- **Version Control**: Git-based with approval workflows
- **Digital Signatures**: PKI-based signing for controlled documents
- **Distribution**: Synchronized to EFB devices

**Document Types**:
- Aircraft Flight Manuals (AFM)
- Operations Manuals (OM-A, OM-B, OM-C)
- Maintenance Manuals (AMM, IPC, CMM)
- Training materials and procedures
- Regulatory documentation

**Reference**: [02-60-07_Document_Storage](./02-60-07_Document_Storage/)

### 2.8 ML Model Storage Layer

**Purpose**: Neural network models, training datasets, and ML artifacts

- **Technology**: MLflow Registry, DVC, feature stores (Feast)
- **Model Formats**: ONNX, TensorFlow SavedModel, PyTorch
- **Versioning**: Semantic versioning with lineage tracking
- **DPP Integration**: Linked to [ATA 95 Digital Product Passport](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/)
- **Compliance**: [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206) traceability requirements

**Stored Artifacts**:
- Trained neural network models
- Training and validation datasets
- Feature engineering pipelines
- Model performance metrics
- Training provenance and metadata

**Reference**: [02-60-08_ML_Model_Storage](./02-60-08_ML_Model_Storage/)

### 2.9 Edge Storage Layer

**Purpose**: On-board and edge device storage

- **Technology**: DO-160 qualified SSDs, EFB local storage
- **Architecture**: IMA partitioned storage, EFB synchronized storage
- **Sync Pattern**: Offline-first with delta synchronization
- **Environmental**: Temperature range -40°C to +85°C
- **Reliability**: MTBF > 2 million hours

**Edge Data**:
- EFB application cache
- Offline operational manuals
- Flight plans and weather data
- Local performance calculations
- Sensor buffering before ground sync

**Reference**: [02-60-09_Edge_Storage](./02-60-09_Edge_Storage/)

### 2.10 Distributed Storage Layer

**Purpose**: Cloud-native scalable storage clusters

- **Technology**: Ceph (block, object, file), GlusterFS
- **Replication**: 3-way replication across failure domains
- **Consistency**: Tunable consistency levels per use case
- **Performance**: Parallel access, load balancing
- **Capacity**: Elastic scaling to petabyte scale

**Use Cases**:
- Container persistent volumes
- Shared file systems for analytics
- Block storage for VMs
- Object storage backend

**Reference**: [02-60-11_Distributed_Storage](./02-60-11_Distributed_Storage/)

### 2.11 Storage Security Layer

**Purpose**: Cross-cutting security for all storage tiers

- **Encryption at Rest**: AES-256 for all persistent storage
- **Encryption in Transit**: TLS 1.3 for all data transfers
- **Key Management**: HSM-backed key management (PKCS#11)
- **Access Control**: Role-based and attribute-based access control
- **Audit Logging**: Comprehensive audit trails for compliance

**Security Controls**:
- Zero-trust architecture
- Least privilege access
- Continuous security scanning
- Automated vulnerability remediation

**Reference**: [02-60-12_Storage_Security](./02-60-12_Storage_Security/)

---

## 3. Storage Architecture Patterns

### 3.1 Tiered Storage Strategy

**Hot Tier** (< 24 hours)
- High-performance SSD storage
- Sub-millisecond latency
- In-memory caching
- Real-time operational data

**Warm Tier** (24 hours - 90 days)
- Balanced SSD/HDD storage
- Millisecond to second latency
- Recent historical data
- Frequent analytics queries

**Cold Tier** (90 days - 2 years)
- Cost-optimized HDD/object storage
- Minute-scale latency acceptable
- Infrequent access patterns
- Long-term analytics

**Archive Tier** (> 2 years)
- Glacier/tape storage
- Hour to day retrieval times
- Compliance and regulatory retention
- Immutable records

### 3.2 Data Lifecycle Management

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Data        │────>│ Data        │────>│ Data        │────>│ Data        │
│ Creation    │     │ Active Use  │     │ Archival    │     │ Deletion    │
│             │     │             │     │             │     │             │
│ - Ingest    │     │ - OLTP      │     │ - Compress  │     │ - Secure    │
│ - Validate  │     │ - Analytics │     │ - Migrate   │     │   erase     │
│ - Classify  │     │ - Backup    │     │ - Retain    │     │ - Audit     │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
    Hot Tier          Warm/Cold Tier       Archive Tier        End of Life
```

**Lifecycle Policies**:
- Automatic tier transitions based on age and access patterns
- Data classification drives retention periods
- Compliance requirements override cost optimization
- Regular reviews of lifecycle policies

### 3.3 Backup and Disaster Recovery

**Backup Levels**:
1. **L0 (Full)**: Weekly full backups of all systems
2. **L1 (Differential)**: Daily differential since last L0
3. **L2 (Incremental)**: Hourly incremental for critical systems
4. **L3 (Continuous)**: Transaction log shipping for databases

**Recovery Scenarios**:
- **Data Loss**: Point-in-time recovery from backups
- **Site Failure**: Failover to secondary data center
- **Regional Disaster**: Geo-redundant replication
- **Logical Corruption**: Restore from known-good backup

### 3.4 Data Replication Strategy

**Synchronous Replication** (Primary DB)
- Zero data loss (RPO = 0)
- Sub-second failover (RTO < 60s)
- Within same region/metro area
- Performance impact acceptable

**Asynchronous Replication** (Secondary systems)
- Near-zero data loss (RPO < 5 min)
- Fast failover (RTO < 15 min)
- Cross-region replication
- Minimal performance impact

**Hybrid Replication** (Multi-tier)
- Synchronous to local replica
- Asynchronous to remote sites
- Balanced performance and protection

---

## 4. Storage Capacity Planning

### 4.1 Capacity Growth Model

**Current State** (Year 0):
- Primary DB: 50 TB
- Time-Series: 200 TB
- Object Storage: 500 TB
- Total: ~750 TB

**Growth Projections**:
- **Year 1**: 40% growth → 1.05 PB
- **Year 2**: 35% growth → 1.42 PB
- **Year 3**: 30% growth → 1.85 PB
- **Year 5**: 25% annual → 2.85 PB

**Growth Drivers**:
- Increased telemetry resolution
- ML training dataset expansion
- Video/media content growth
- Compliance retention requirements

### 4.2 Capacity Safety Margins

- **Operational Headroom**: 20% free space on hot tiers
- **Growth Buffer**: 6-month projected growth pre-provisioned
- **Emergency Reserve**: 10% additional for unexpected events
- **Effective Target**: ~65-70% utilization at steady state

### 4.3 Cost Optimization

**Storage Cost Hierarchy** ($/TB/month):
- Hot SSD: $100-200
- Warm SSD/HDD: $30-50
- Cold Object: $10-20
- Archive Glacier: $1-5
- Tape: $0.50-1

**Optimization Strategies**:
- Aggressive tiering for non-critical data
- Compression for time-series and logs
- Deduplication for backups
- Intelligent caching to reduce hot storage

---

## 5. Integration with AMPEL360 Systems

### 5.1 Backend Services Integration

Storage layers are consumed by [ATA 02-40 Software](../02-40_Software/) systems:

- **Core Applications**: Primary DB, cache, object storage
- **EFB Software**: Document storage, edge storage, object storage
- **Analytics Engine**: Time-series, data warehouse, object storage
- **Predictive Ops**: ML model storage, time-series, feature stores

### 5.2 Circularity Integration

Storage lifecycle aligned with [ATA 02-30 Circularity](../02-30_Circularity/):

- Data minimization and retention policies
- Energy-efficient storage technologies
- Hardware lifecycle management
- Carbon accounting for storage infrastructure

### 5.3 Digital Product Passport

ML models and training data linked to [ATA 95 DPP](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/):

- Model provenance and lineage
- Training data versioning
- Performance metrics history
- Blockchain-anchored hashes for immutability

---

## 6. Monitoring and Observability

### 6.1 Key Storage Metrics

**Capacity Metrics**:
- Used vs. allocated capacity
- Growth rate trends
- Time to exhaustion projections
- Tier distribution

**Performance Metrics**:
- IOPS (read/write)
- Throughput (MB/s)
- Latency (p50, p95, p99)
- Queue depth

**Reliability Metrics**:
- Availability percentage (target: 99.95%)
- MTBF and MTTR
- Failed disk replacement rate
- Backup success rate

**Cost Metrics**:
- Cost per TB per tier
- Total cost of ownership
- Cost trends and forecasts
- Optimization opportunities

### 6.2 Alerting Thresholds

**Critical Alerts**:
- Capacity > 85% on hot tiers
- Backup failures
- Replication lag > 5 minutes
- Storage array errors

**Warning Alerts**:
- Capacity > 75%
- Performance degradation > 20%
- Unusual growth patterns
- Approaching warranty expiration

---

## 7. Compliance and Governance

### 7.1 Regulatory Requirements

Storage systems comply with:

- **[CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)** – Equipment, systems, and installations
- **[EASA Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012)** – Certification of aircraft and related products
- **[DO-178C](https://www.rtca.org/content/standards-guidance-materials)** – Software considerations (for storage management software)
- **GDPR** – Personal data protection (crew, passenger data)
- **[EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206)** – AI system data requirements

### 7.2 Data Governance

See [02-60-00-003_Data_Governance_Policy.md](./02-60-00-003_Data_Governance_Policy.md) for:

- Data ownership and stewardship
- Data classification levels
- Access control policies
- Retention and disposal procedures
- Audit and compliance reporting

---

## 8. Technology Standards

### 8.1 Supported Technologies

**Databases**:
- PostgreSQL 14+ (primary OLTP)
- TimescaleDB 2.x (time-series)
- MongoDB 6.x (document store)

**Object Storage**:
- S3 API compatible
- MinIO (on-premises)
- AWS S3, Azure Blob (cloud)

**Caching**:
- Redis 7.x (primary)
- Memcached 1.6+ (specific use cases)

**Distributed Storage**:
- Ceph Quincy+ (block, object, file)
- GlusterFS 10+ (file)

### 8.2 Storage Hardware

**Primary Storage**:
- Enterprise NVMe SSDs (Dell PowerStore, NetApp AFF)
- All-flash arrays for hot tier
- Hybrid arrays for warm tier

**Archive Storage**:
- LTO-9 tape libraries (IBM TS4500)
- Object storage appliances
- Cloud-based glacier storage

---

## 9. Future Enhancements

### 9.1 Short-Term (6-12 months)

- Implement automated capacity forecasting
- Deploy storage observability platform
- Enhance tiering automation
- Expand geo-replication

### 9.2 Medium-Term (1-2 years)

- Implement storage-as-a-service model
- Deploy AI-driven storage optimization
- Enhanced edge-to-cloud data sync
- Quantum-safe encryption migration

### 9.3 Long-Term (2-5 years)

- Fully automated data lifecycle management
- Self-healing storage infrastructure
- Carbon-neutral storage operations
- Next-generation storage technologies

---

## 10. References

### Internal Documents
- [02-60-00-002 Storage Capacity Planning](./02-60-00-002_Storage_Capacity_Planning.md)
- [02-60-00-003 Data Governance Policy](./02-60-00-003_Data_Governance_Policy.md)
- [02-60-00-004 Storage Metrics Dashboard](./02-60-00-004_Storage_Metrics_Dashboard.yaml)
- [ATA 02-30 Circularity](../02-30_Circularity/)
- [ATA 02-40 Software](../02-40_Software/)

### External Standards
- [CS-25 Certification Specifications](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)
- [DO-178C Software Considerations](https://www.rtca.org/content/standards-guidance-materials)
- [EASA Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012)
- [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206)

---

## Document Control

- **Document ID**: 02-60-00-001
- **Version**: 1.0
- **Status**: DRAFT
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.
