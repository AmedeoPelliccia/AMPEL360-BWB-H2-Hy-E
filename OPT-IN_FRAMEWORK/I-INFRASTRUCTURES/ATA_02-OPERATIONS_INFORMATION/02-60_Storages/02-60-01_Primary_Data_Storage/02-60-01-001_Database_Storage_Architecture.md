# 02-60-01-001 – Database Storage Architecture

## Purpose

This document describes the logical and physical architecture of database storage for AMPEL360 primary operational databases, including tablespace design, storage allocation, replication topology, and availability zone distribution.

---

## 1. Logical Architecture

### 1.1 Database Cluster Organization

```
┌─────────────────────────────────────────────────────────────┐
│                  AMPEL360 Database Cluster                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────┐  ┌────────────────┐  ┌──────────────┐  │
│  │   Production    │  │  Data Warehouse │  │   Reference  │  │
│  │      OLTP       │  │    (Analytics)  │  │     Data     │  │
│  │                 │  │                 │  │              │  │
│  │  - Operations   │  │  - Historical   │  │  - Aircraft  │  │
│  │  - Performance  │  │  - Reporting    │  │  - Airports  │  │
│  │  - W&B          │  │  - ML Training  │  │  - Weather   │  │
│  │  - Crew         │  │  - Compliance   │  │  - Regs      │  │
│  └────────────────┘  └────────────────┘  └──────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Tablespace Design

**Production OLTP Tablespaces**:
- `pg_default`: System and small tables
- `ops_hot`: Hot operational data (current flights, active operations)
- `ops_warm`: Recent historical data (last 90 days)
- `ops_indexes`: Indexes for operational tables
- `ops_temp`: Temporary data and sorts

**Data Warehouse Tablespaces**:
- `dw_fact`: Fact tables (flight events, metrics)
- `dw_dim`: Dimension tables (aircraft, airports, time)
- `dw_staging`: ETL staging area
- `dw_archive`: Cold historical data (> 2 years)

**Reference Data Tablespaces**:
- `ref_master`: Master reference data
- `ref_cache`: Frequently accessed reference data (in-memory)

---

## 2. Physical Storage Architecture

### 2.1 Storage Array Topology

**Primary Site (Main Data Center)**:

```
┌──────────────────────────────────────────────────────────────┐
│                    Primary Storage Array                      │
│                    (Dell PowerStore 9000)                     │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │   SSD Pool 1    │  │   SSD Pool 2    │  │  SSD Pool 3  │ │
│  │   (NVMe Fast)   │  │  (SSD Balanced) │  │ (SSD Capacity)│ │
│  │                 │  │                 │  │              │ │
│  │  - OLTP Hot     │  │  - DW Fact      │  │  - DW Archive│ │
│  │  - Indexes      │  │  - DW Dim       │  │  - Old Data  │ │
│  │  - Temp         │  │  - Ref Master   │  │              │ │
│  │                 │  │                 │  │              │ │
│  │  Tier: Hot      │  │  Tier: Warm     │  │  Tier: Cold  │ │
│  │  Latency: <1ms  │  │  Latency: <5ms  │  │  Latency:<20ms│ │
│  └─────────────────┘  └─────────────────┘  └──────────────┘ │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

**Secondary Site (DR Data Center)**:

```
┌──────────────────────────────────────────────────────────────┐
│                   Secondary Storage Array                     │
│                    (NetApp AFF A700)                          │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │           Synchronous Replica (Metro Cluster)            │ │
│  │                                                           │ │
│  │  - Full copy of production OLTP                          │ │
│  │  - Active-passive configuration                          │ │
│  │  - Zero data loss (RPO = 0)                              │ │
│  │  - Automatic failover (RTO < 60s)                        │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

### 2.2 Storage Allocation

| Database Cluster | Tablespace | Storage Pool | RAID | Capacity | Growth/Year |
|------------------|------------|--------------|------|----------|-------------|
| Production OLTP | ops_hot | SSD Pool 1 | RAID-10 | 15 TB | +30% |
| Production OLTP | ops_warm | SSD Pool 2 | RAID-6 | 10 TB | +25% |
| Production OLTP | ops_indexes | SSD Pool 1 | RAID-10 | 5 TB | +20% |
| Data Warehouse | dw_fact | SSD Pool 2 | RAID-6 | 12 TB | +35% |
| Data Warehouse | dw_dim | SSD Pool 2 | RAID-6 | 3 TB | +15% |
| Data Warehouse | dw_archive | SSD Pool 3 | RAID-6 | 5 TB | +40% |
| Reference Data | ref_master | SSD Pool 2 | RAID-6 | 2 TB | +10% |

---

## 3. Availability Zones and Replication

### 3.1 AZ Distribution

**Zone 1 (Primary)**:
- Primary database cluster
- Active serving all reads and writes
- Located in Main Data Center, Building A

**Zone 2 (Synchronous Replica)**:
- Synchronous replica within same region (< 5ms latency)
- Hot standby for automatic failover
- Located in Main Data Center, Building B (separate power/cooling)

**Zone 3 (Asynchronous Replica)**:
- Asynchronous replica in secondary region (> 50km distance)
- Disaster recovery site
- RPO: 15 minutes, RTO: 4 hours

### 3.2 Replication Topology

**Synchronous Replication** (Primary → Zone 2):
```
Primary DB (Zone 1)  ──[Sync WAL]──>  Standby DB (Zone 2)
  │                                        │
  │  Commits wait for replica ACK          │  Auto-promote on primary failure
  │  RPO: 0 (no data loss)                 │  RTO: < 60 seconds
  └────────[Heartbeat & Monitoring]────────┘
```

**Asynchronous Replication** (Primary → Zone 3):
```
Primary DB (Zone 1)  ──[Async WAL]──>  DR DB (Zone 3)
  │                                        │
  │  Commits don't wait                    │  Manual promotion
  │  RPO: 15 minutes                       │  RTO: 4 hours
  └────────[Replication Monitoring]────────┘
```

### 3.3 Quorum Configuration

For PostgreSQL high availability using Patroni:

```yaml
# Etcd quorum configuration
quorum:
  minimum_nodes: 3
  nodes:
    - etcd1.zone1.ampel360.local
    - etcd2.zone2.ampel360.local
    - etcd3.zone3.ampel360.local
  
  # Leader election
  leader_election:
    ttl: 30
    loop_wait: 10
    retry_timeout: 30
```

---

## 4. Storage Performance Characteristics

### 4.1 I/O Patterns by Workload

**OLTP Workload**:
- Read/Write Ratio: 70% read, 30% write
- Random I/O: 95%
- Block Size: 8 KB
- Concurrency: High (100-500 connections)
- Latency Sensitivity: Critical (< 5ms target)

**Data Warehouse Workload**:
- Read/Write Ratio: 95% read, 5% write
- Sequential I/O: 60%
- Block Size: 64 KB - 1 MB
- Concurrency: Medium (10-50 queries)
- Latency Sensitivity: Moderate (< 50ms acceptable)

**Reference Data Workload**:
- Read/Write Ratio: 99% read, 1% write
- Random I/O: 80%
- Block Size: 8 KB
- Concurrency: Very high (many small queries)
- Latency Sensitivity: Low (< 100ms acceptable with caching)

### 4.2 IOPS Requirements

| Workload | Peak IOPS | Avg IOPS | IOPS Type |
|----------|-----------|----------|-----------|
| OLTP Production | 80,000 | 40,000 | Random R/W |
| Data Warehouse | 20,000 | 8,000 | Mixed |
| Reference Data | 15,000 | 5,000 | Random Read |
| **Total** | **115,000** | **53,000** | Mixed |

### 4.3 Throughput Requirements

| Workload | Peak Throughput | Avg Throughput |
|----------|-----------------|----------------|
| OLTP Production | 1.5 GB/s | 600 MB/s |
| Data Warehouse | 3.0 GB/s | 1.2 GB/s |
| Reference Data | 500 MB/s | 200 MB/s |
| **Total** | **5.0 GB/s** | **2.0 GB/s** |

---

## 5. Filesystem and Volume Management

### 5.1 Filesystem Selection

**XFS** (Recommended for PostgreSQL):
- Better performance for large files
- Efficient for write-heavy workloads
- Good scalability to multi-TB volumes
- Delayed allocation improves throughput

**ext4** (Alternative):
- More mature, widely tested
- Suitable for smaller volumes
- Lower metadata overhead

### 5.2 Mount Options

**Production Volumes** (XFS):
```bash
/dev/mapper/vg_db01-lv_oltp_hot  /var/lib/pgsql/14/oltp_hot  xfs  \
  noatime,nodiratime,logbufs=8,logbsize=256k,largeio,inode64,swalloc  0 0
```

**Key Options**:
- `noatime,nodiratime`: Disable access time updates (performance)
- `logbufs=8,logbsize=256k`: Larger log buffers for write performance
- `largeio`: Optimize for large I/O operations
- `inode64`: Support for large filesystems
- `swalloc`: Stripe-width allocation for better RAID performance

### 5.3 Volume Layout

**Logical Volume Manager (LVM)**:

```
Physical Volumes (PVs)
  ├── /dev/sda  (SSD Pool 1 - 8 TB)
  ├── /dev/sdb  (SSD Pool 1 - 8 TB)
  ├── /dev/sdc  (SSD Pool 2 - 12 TB)
  └── /dev/sdd  (SSD Pool 3 - 16 TB)
        │
        ▼
Volume Groups (VGs)
  ├── vg_db_hot     (PVs: sda, sdb)
  ├── vg_db_warm    (PVs: sdc)
  └── vg_db_cold    (PVs: sdd)
        │
        ▼
Logical Volumes (LVs)
  ├── lv_oltp_hot       (10 TB, RAID-10 via storage array)
  ├── lv_oltp_indexes   (4 TB, RAID-10)
  ├── lv_dw_fact        (10 TB, RAID-6)
  └── lv_dw_archive     (5 TB, RAID-6)
```

---

## 6. Backup Integration

### 6.1 Storage-Level Snapshots

**Snapshot Strategy**:
- Hourly snapshots (retained 24 hours)
- Daily snapshots (retained 7 days)
- Weekly snapshots (retained 4 weeks)

**Snapshot Configuration**:
```yaml
snapshot_policy:
  name: db_production_snapshots
  schedule:
    - interval: hourly
      retention: 24
    - interval: daily
      retention: 7
      time: "02:00"
    - interval: weekly
      retention: 4
      day: Sunday
      time: "03:00"
  
  consistency_group: true  # Ensure consistency across volumes
```

### 6.2 Database-Level Backups

**PostgreSQL Continuous Archiving**:
- WAL segments shipped to [02-60-05 Backup Storage](../02-60-05_Backup_Storage/)
- Point-in-time recovery capability
- Integrated with pgBackRest for efficient incremental backups

---

## 7. Monitoring and Alerting

### 7.1 Storage Metrics

**Capacity Monitoring**:
- Used vs. allocated space per tablespace
- Growth rate trends
- Time to exhaustion

**Performance Monitoring**:
- IOPS (read/write)
- Latency (p50, p95, p99)
- Throughput (MB/s)
- Queue depth

**Health Monitoring**:
- Disk failures
- RAID degradation
- Replication lag
- Filesystem errors

### 7.2 Integration with Metrics Dashboard

See [02-60-00-004 Storage Metrics Dashboard](../02-60-00-004_Storage_Metrics_Dashboard.yaml) for complete metric definitions and alerting rules.

---

## 8. Maintenance and Operations

### 8.1 Planned Maintenance

**Monthly Tasks**:
- Tablespace usage review
- Index maintenance (REINDEX if needed)
- Vacuum full on large tables (off-peak)
- Performance baseline validation

**Quarterly Tasks**:
- Storage array firmware updates
- Capacity planning review
- DR failover test
- Performance tuning review

### 8.2 Emergency Procedures

**Disk Failure**:
1. RAID automatically rebuilds
2. Monitor rebuild progress
3. Replace failed disk (hot-swap)
4. Validate RAID health post-rebuild

**Primary Site Failure**:
1. Automatic failover to Zone 2 (< 60 seconds)
2. Notify operations team
3. Investigate primary site issue
4. Plan failback when primary restored

---

## 9. References

### Internal Documents
- [02-60-01 README](./README.md)
- [02-60-01-002 SSD Array Configuration](./02-60-01-002_SSD_Array_Configuration.md)
- [02-60-01-003 RAID Strategy](./02-60-01-003_RAID_Strategy.md)
- [02-60-01-005 High Availability Setup](./02-60-01-005_High_Availability_Setup.md)
- [02-60-00-001 Storage Architecture Overview](../02-60-00-001_Storage_Architecture_Overview.md)

### External References
- [PostgreSQL High Availability](https://www.postgresql.org/docs/current/high-availability.html)
- [Patroni Documentation](https://patroni.readthedocs.io/)
- [Dell PowerStore](https://www.dell.com/en-us/dt/storage/powerstore-storage-appliance.htm)
- [NetApp AFF](https://www.netapp.com/data-storage/all-flash-san-storage-arrays/)

---

## Document Control

- **Document ID**: 02-60-01-001
- **Version**: 1.0
- **Status**: DRAFT
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.
