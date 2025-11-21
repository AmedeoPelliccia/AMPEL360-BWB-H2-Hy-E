# 02-60-01 – Primary Data Storage

## Purpose

This directory defines the primary data storage infrastructure for AMPEL360 operational databases. It covers production OLTP systems, data warehouses, and reference data stores that support flight operations, performance calculations, weight & balance, dispatch, and crew management systems.

---

## Scope

Primary data storage encompasses:

- **Production OLTP Databases**: Transactional systems for operational data (PostgreSQL, MySQL)
- **Data Warehouses**: Analytical databases for historical analysis and reporting
- **Reference Data**: Master data management (aircraft specs, airport data, regulatory data)
- **Configuration Databases**: System configuration and application settings

---

## Relationship to Backend Services

Primary data storage is consumed by [ATA 02-40 Software](../../02-40_Software/) backend services:

- **[02-40-01 Core Applications](../../02-40_Software/02-40-01_Core_Applications/)** – Flight planning, dispatch, crew management
- **[02-40-12 Backend Services](../../02-40_Software/02-40-12_Backend_Services/)** – API services and microservices
- **[02-40-13 Performance Calculator](../../02-40_Software/02-40-13_Performance_Calculator/)** – Performance calculation data
- **[02-40-14 Weight Balance System](../../02-40_Software/02-40-14_Weight_Balance_System/)** – W&B operational data

---

## Key Documents

### Architecture & Design
- **[02-60-01-001_Database_Storage_Architecture.md](./02-60-01-001_Database_Storage_Architecture.md)** – Logical and physical database storage architecture
- **[02-60-01-002_SSD_Array_Configuration.md](./02-60-01-002_SSD_Array_Configuration.md)** – SSD array design for aviation workloads
- **[02-60-01-003_RAID_Strategy.md](./02-60-01-003_RAID_Strategy.md)** – RAID configuration patterns and trade-offs

### Performance & Optimization
- **[02-60-01-004_Performance_Optimization.md](./02-60-01-004_Performance_Optimization.md)** – Tuning guidelines for IOPS, latency, throughput
- **[02-60-01-005_High_Availability_Setup.md](./02-60-01-005_High_Availability_Setup.md)** – HA patterns, replication, RPO/RTO

---

## ASSETS

### Configurations
- **[02-60-01-A-001_Storage_Array_Topology.yaml](./ASSETS/Configurations/02-60-01-A-001_Storage_Array_Topology.yaml)** – Storage array topology and connectivity
- **[02-60-01-A-002_RAID_Configuration.yaml](./ASSETS/Configurations/02-60-01-A-002_RAID_Configuration.yaml)** – RAID configuration templates
- **[02-60-01-A-003_Replication_Setup.yaml](./ASSETS/Configurations/02-60-01-A-003_Replication_Setup.yaml)** – Database replication topology

### Performance
- **02-60-01-A-101_IOPS_Benchmarks.xlsx** – IOPS benchmark data and analysis
- **02-60-01-A-102_Latency_Analysis.xlsx** – Latency analysis for workloads
- **02-60-01-A-103_Throughput_Tests.pdf** – Throughput test methodology and results

### Hardware
- **02-60-01-A-201_Dell_PowerStore_Spec.pdf** – Enterprise SSD array specifications (Dell PowerStore)
- **02-60-01-A-202_NetApp_AFF_Spec.pdf** – All-flash array specifications (NetApp AFF)

---

## Technology Stack

**Primary Databases**:
- PostgreSQL 14+ (OLTP, data warehouse with extensions)
- MySQL 8.0+ (specific legacy systems)

**Storage Hardware**:
- Dell PowerStore (all-flash arrays)
- NetApp AFF A-Series (all-flash arrays)
- Enterprise NVMe SSDs

**High Availability**:
- Synchronous replication (local)
- Asynchronous replication (cross-region)
- Automatic failover with Patroni/pgpool

**Backup Integration**:
- Linked to [02-60-05 Backup Storage](../02-60-05_Backup_Storage/)
- Continuous archiving (WAL shipping)
- Point-in-time recovery capability

---

## Performance Targets

| Metric | Target | Measurement |
|--------|--------|-------------|
| Read Latency (p95) | < 5ms | Hot data, SSD array |
| Write Latency (p95) | < 10ms | OLTP workload |
| IOPS (sustained) | > 50,000 | Mixed read/write |
| Throughput | > 2 GB/s | Sequential operations |
| Availability | 99.95% | Measured monthly |
| RPO | 15 minutes | Worst-case data loss |
| RTO | 4 hours | Primary system recovery |

---

## Capacity Planning

See [02-60-00-002 Storage Capacity Planning](../02-60-00-002_Storage_Capacity_Planning.md) for detailed projections.

**Current Capacity** (Year 0):
- Production OLTP: 30 TB usable
- Data Warehouse: 20 TB usable
- Total: 50 TB usable

**Growth Projection**:
- Year 1: 65 TB (+30%)
- Year 3: 110 TB
- Year 5: 185 TB

---

## Security and Compliance

- **Encryption at Rest**: AES-256 encryption for all data volumes
- **Encryption in Transit**: TLS 1.3 for all database connections
- **Access Control**: Role-based access control (RBAC) with audit logging
- **Compliance**: Aligned with [02-60-00-003 Data Governance Policy](../02-60-00-003_Data_Governance_Policy.md)

---

## References

### Internal Documents
- [02-60-00-001 Storage Architecture Overview](../02-60-00-001_Storage_Architecture_Overview.md)
- [02-60-00-002 Storage Capacity Planning](../02-60-00-002_Storage_Capacity_Planning.md)
- [02-60-12 Storage Security](../02-60-12_Storage_Security/)
- [ATA 02-40 Software](../../02-40_Software/)

### External Standards
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Dell PowerStore](https://www.dell.com/en-us/dt/storage/powerstore-storage-appliance.htm)
- [NetApp AFF](https://www.netapp.com/data-storage/all-flash-san-storage-arrays/)

---

## Document Control

- **Directory**: 02-60-01_Primary_Data_Storage
- **Version**: 1.0
- **Status**: DRAFT
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.
