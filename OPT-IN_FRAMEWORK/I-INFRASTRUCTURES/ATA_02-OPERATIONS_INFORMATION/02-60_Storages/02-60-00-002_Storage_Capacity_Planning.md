# 02-60-00-002 – Storage Capacity Planning

## Purpose

This document defines the methods, formulas, and processes for planning storage capacity across all AMPEL360 storage tiers. It provides a systematic approach to forecasting growth, managing capacity, and ensuring adequate headroom for operational needs.

---

## 1. Capacity Planning Framework

### 1.1 Planning Objectives

- **Avoid Capacity Exhaustion**: Maintain sufficient headroom to prevent operational disruptions
- **Optimize Costs**: Right-size storage investments without over-provisioning
- **Support Growth**: Plan for projected data growth across all tiers
- **Ensure Performance**: Maintain performance levels as capacity scales
- **Enable Compliance**: Meet regulatory retention requirements

### 1.2 Planning Horizon

- **Tactical Planning**: 3-6 months (procurement lead times)
- **Operational Planning**: 6-12 months (annual budgets)
- **Strategic Planning**: 2-5 years (technology roadmap)

---

## 2. Capacity Measurement and Metrics

### 2.1 Raw vs. Usable Capacity

**Raw Capacity**: Total physical storage media capacity

**Usable Capacity**: Capacity available after:
- RAID overhead (parity, mirroring)
- Filesystem overhead (metadata, journals)
- Snapshot and replication space
- Reserved space (operating system)

**Formula**:
```
Usable_Capacity = Raw_Capacity × RAID_Efficiency × FS_Efficiency × (1 - Reserved_Percentage)
```

**Example Calculations**:

| RAID Level | Raw | RAID Eff | FS Eff | Reserved | Usable |
|------------|-----|----------|--------|----------|--------|
| RAID-10    | 100 TB | 50%   | 95%    | 10%      | 42.75 TB |
| RAID-6     | 100 TB | 67%   | 95%    | 10%      | 57.29 TB |
| RAID-0     | 100 TB | 100%  | 95%    | 10%      | 85.5 TB  |

### 2.2 Key Capacity Metrics

**Current Utilization**:
```
Utilization = (Used_Capacity / Usable_Capacity) × 100%
```

**Growth Rate**:
```
Growth_Rate = (Current_Capacity - Previous_Capacity) / Previous_Capacity / Time_Period
```

**Time to Exhaustion**:
```
TTE = (Usable_Capacity - Used_Capacity) / Average_Daily_Growth
```

**Effective Capacity**:
```
Effective = Usable_Capacity × (1 - Safety_Margin_Percentage)
```

---

## 3. Storage Tier Capacity Requirements

### 3.1 Primary Data Storage (02-60-01)

**Current Baseline** (Year 0):
- Production OLTP: 30 TB usable
- Data Warehouse: 20 TB usable
- Total: 50 TB usable

**Growth Drivers**:
- New aircraft deliveries: +15% annually
- Operational data resolution increase: +10% annually
- Historical data accumulation: +5% annually

**Growth Formula**:
```
Capacity(year) = Baseline × (1 + Aircraft_Growth + Data_Resolution + Historical)^year
Capacity(year) = 50 TB × (1.30)^year
```

**Projections**:
- Year 1: 65 TB
- Year 2: 85 TB
- Year 3: 110 TB
- Year 5: 185 TB

**Safety Margin**: 20% operational headroom
**Recommended Procurement**: 80 TB at Y0, +30 TB annually

### 3.2 Time-Series Storage (02-60-02)

**Current Baseline** (Year 0):
- Hot tier (7 days): 20 TB
- Warm tier (90 days): 80 TB
- Cold tier (2 years): 100 TB
- Total: 200 TB usable

**Growth Drivers**:
- Sensor density increase: +20% annually
- Sampling frequency increase: +15% annually
- Fleet expansion: +15% annually
- Compression improvements: -10% annually (offset)

**Growth Formula**:
```
Capacity(year) = Baseline × (1 + Sensors + Frequency + Fleet - Compression)^year
Capacity(year) = 200 TB × (1.40)^year
```

**Projections**:
- Year 1: 280 TB
- Year 2: 390 TB
- Year 3: 550 TB
- Year 5: 1,080 TB (~1.1 PB)

**Safety Margin**: 15% (time-series is more predictable)
**Recommended Procurement**: 240 TB at Y0, +100 TB annually

### 3.3 Object Storage (02-60-03)

**Current Baseline** (Year 0):
- Documents: 100 TB
- Media/Video: 200 TB
- Backups: 150 TB
- Artifacts: 50 TB
- Total: 500 TB usable

**Growth Drivers**:
- Video content: +50% annually
- Document accumulation: +20% annually
- Backup growth: +30% annually (tracks primary data)
- Artifacts: +25% annually

**Weighted Growth Formula**:
```
Capacity(year) = Σ(Baseline_i × (1 + Growth_i)^year)
Capacity(year) ≈ 500 TB × (1.35)^year (weighted average)
```

**Projections**:
- Year 1: 675 TB
- Year 2: 910 TB
- Year 3: 1,230 TB (~1.2 PB)
- Year 5: 2,245 TB (~2.2 PB)

**Safety Margin**: 25% (highly variable workload)
**Recommended Procurement**: 650 TB at Y0, +200 TB annually

### 3.4 Cache Storage (02-60-04)

**Current Baseline** (Year 0):
- Redis cluster: 200 GB
- Memcached: 100 GB
- Total: 300 GB

**Growth Drivers**:
- User base growth: +20% annually
- Session complexity: +10% annually
- Computed data caching: +15% annually

**Growth Formula**:
```
Capacity(year) = 300 GB × (1.45)^year
```

**Projections**:
- Year 1: 435 GB
- Year 2: 630 GB
- Year 3: 915 GB
- Year 5: 1,930 GB (~2 TB)

**Safety Margin**: 30% (performance-critical, cost-effective to over-provision)
**Recommended Procurement**: Upgrade to 500 GB at Y0, evaluate annually

### 3.5 Backup Storage (02-60-05)

**Current Baseline** (Year 0):
- 750 TB (1.5× primary + time-series + hot object)

**Growth Drivers**:
- Tracks primary data growth
- Retention policy: 90 days full, 1 year incremental

**Growth Formula**:
```
Capacity(year) = (Primary + TimeSeries + HotObject) × Retention_Factor × (1 + Growth)^year
```

**Projections**:
- Year 1: 1,020 TB (~1 PB)
- Year 2: 1,390 TB (~1.4 PB)
- Year 3: 1,890 TB (~1.9 PB)
- Year 5: 3,465 TB (~3.5 PB)

**Safety Margin**: 10% (backup growth is predictable)
**Recommended Procurement**: 850 TB at Y0, +300 TB annually

### 3.6 Archive Storage (02-60-06)

**Current Baseline** (Year 0):
- Compliance archives: 1,000 TB
- Operational archives: 500 TB
- Total: 1,500 TB

**Growth Drivers**:
- Continuous accumulation (minimal deletion)
- Regulatory retention: 5-25 years
- Fleet expansion: +15% annually

**Growth Formula**:
```
Capacity(year) = Baseline + (Annual_Archival_Rate × year)
Annual_Archival_Rate = 300 TB/year (increases 15% annually)
```

**Projections**:
- Year 1: 1,800 TB
- Year 2: 2,145 TB
- Year 3: 2,540 TB
- Year 5: 3,515 TB (~3.5 PB)

**Safety Margin**: 5% (low-cost storage, can over-provision)
**Recommended Procurement**: Tape library expansion, 500 TB annually

---

## 4. Capacity Planning Methodology

### 4.1 Data Collection

**Monthly Metrics Collection**:
1. Current used capacity per tier
2. Growth rate (daily, weekly, monthly)
3. I/O patterns and performance metrics
4. Cost per TB per tier
5. Decommission and cleanup opportunities

**Quarterly Review**:
1. Validate growth projections vs. actuals
2. Adjust forecasting models
3. Identify optimization opportunities
4. Plan procurement for next 6 months

### 4.2 Forecasting Process

**Step 1: Historical Analysis**
- Review 12-18 months of historical growth
- Identify trends, seasonality, anomalies
- Calculate average and peak growth rates

**Step 2: Driver-Based Modeling**
- Link growth to business drivers (fleet size, operations, etc.)
- Separate organic growth from one-time events
- Model different scenarios (conservative, expected, aggressive)

**Step 3: Constraint Application**
- Apply safety margins based on tier criticality
- Factor in cleanup and deduplication opportunities
- Consider planned data lifecycle policy changes

**Step 4: Validation**
- Cross-check with other teams (ops, dev, ML)
- Validate against industry benchmarks
- Adjust for known upcoming changes

### 4.3 Capacity Triggers

**Procurement Triggers**:
- Utilization exceeds 70% on critical tiers
- Time to exhaustion < 6 months
- Performance degradation due to capacity
- Planned project requiring additional capacity

**Optimization Triggers**:
- Utilization below 40% sustained for 6 months
- High cost per TB relative to alternatives
- Technology refresh opportunities
- Data lifecycle policy adjustments

---

## 5. Cost Optimization Strategies

### 5.1 Tiered Storage Cost Model

| Tier | $/TB/Month | Performance | Use Case |
|------|------------|-------------|----------|
| Hot SSD | $150 | < 1ms latency | Active OLTP |
| Warm SSD | $75 | < 10ms latency | Recent data |
| Cold HDD | $25 | < 100ms latency | Analytics |
| Object Hot | $20 | API access | Documents, backups |
| Object Cold | $10 | Delayed retrieval | Older backups |
| Archive Glacier | $3 | Hours to days | Compliance |
| Tape Archive | $1 | Days | Long-term |

### 5.2 Optimization Techniques

**Compression**:
- Time-series: 10:1 compression ratio
- Logs: 5:1 compression ratio
- Backups: 2:1 compression ratio
- Cost savings: 50-70% for compressed tiers

**Deduplication**:
- Backup deduplication: 10:1 ratio
- VM image deduplication: 5:1 ratio
- Cost savings: 80-90% for backup storage

**Lifecycle Policies**:
- Automatic tier transitions
- Deletion of expired data
- Snapshot management
- Cost savings: 30-50% through aggressive tiering

**Technology Refresh**:
- Moore's Law: ~2× capacity/cost every 18 months
- Technology migration every 3-4 years
- Cost savings: 40-60% on refresh cycles

---

## 6. Capacity Safety Margins

### 6.1 Tier-Specific Margins

| Storage Tier | Safety Margin | Rationale |
|--------------|---------------|-----------|
| Primary DB | 20% | Performance-critical, sudden growth |
| Time-Series | 15% | Predictable, can scale quickly |
| Object Storage | 25% | Highly variable, media bursts |
| Cache | 30% | Performance impact, cheap to over-provision |
| Backup | 10% | Predictable, tracks primary |
| Archive | 5% | Low-cost, minimal risk |
| Edge | 35% | Hard to upgrade, flight-critical |
| Distributed | 20% | Scales elastically, maintain performance |

### 6.2 Safety Margin Formula

```
Required_Capacity = Projected_Capacity / (1 - Safety_Margin)

Example (Primary DB, Year 1):
Required = 65 TB / (1 - 0.20) = 81.25 TB
```

---

## 7. Procurement Planning

### 7.1 Procurement Cycles

**Annual Strategic Procurement**:
- Major capacity additions (> 100 TB)
- Technology refresh cycles
- Long-term contracts and pricing
- Budget alignment

**Quarterly Tactical Procurement**:
- Capacity gap filling (< 100 TB)
- Opportunistic purchases
- Emergency capacity additions
- Maintenance renewals

### 7.2 Lead Times

| Item | Lead Time | Notes |
|------|-----------|-------|
| Enterprise SSDs | 4-8 weeks | Common models |
| Custom SSD arrays | 12-16 weeks | Dell, NetApp |
| LTO tape drives | 8-12 weeks | IBM TS4500 |
| Cloud storage | Immediate | API provisioning |
| Network upgrades | 8-16 weeks | For capacity scaling |

### 7.3 Vendor Management

**Preferred Vendors**:
- **Primary Storage**: Dell (PowerStore), NetApp (AFF)
- **Backup**: Veeam, Commvault
- **Archive**: IBM (tape), AWS (Glacier)
- **Object Storage**: MinIO (on-prem), AWS S3, Azure Blob
- **Distributed**: Red Hat (Ceph), Red Hat (GlusterFS)

---

## 8. Capacity Risk Management

### 8.1 Capacity Risks

**Critical Risks**:
1. **Exhaustion**: Running out of capacity on critical tiers
2. **Performance Degradation**: Over-utilization impacting operations
3. **Budget Overrun**: Unexpected capacity purchases
4. **Technology Obsolescence**: Unsupported hardware

**Mitigation Strategies**:
1. **Exhaustion**: Maintain safety margins, automated alerting
2. **Performance**: Monitor I/O patterns, proactive scaling
3. **Budget**: Reserve contingency funds, multi-year planning
4. **Obsolescence**: Regular technology refresh cycles

### 8.2 Contingency Planning

**Emergency Capacity Options**:
- Cloud burst capacity (short-term)
- Temporary storage rental
- Accelerated procurement (premium pricing)
- Data archival acceleration (aggressive cleanup)

**Emergency Thresholds**:
- Critical: < 5% free space or < 30 days TTE
- High: < 10% free space or < 60 days TTE
- Medium: < 15% free space or < 90 days TTE

---

## 9. Monitoring and Reporting

### 9.1 Capacity Dashboard

**Real-Time Metrics**:
- Current utilization per tier (percentage and absolute)
- Growth rate (daily, weekly, monthly)
- Time to exhaustion (days)
- Cost per TB per tier

**Historical Trends**:
- 12-month growth chart
- Forecast vs. actual comparison
- Cost trends
- Efficiency metrics (compression ratios, deduplication)

### 9.2 Reporting Cadence

**Daily**: Automated capacity alerts (thresholds exceeded)
**Weekly**: Capacity utilization summary to operations team
**Monthly**: Detailed capacity report to management
**Quarterly**: Capacity review and forecast update
**Annually**: Strategic capacity plan and budget proposal

---

## 10. Integration with Other Systems

### 10.1 Links to Related Documentation

- [02-60-00-001 Storage Architecture Overview](./02-60-00-001_Storage_Architecture_Overview.md)
- [02-60-00-003 Data Governance Policy](./02-60-00-003_Data_Governance_Policy.md)
- [02-60-00-004 Storage Metrics Dashboard](./02-60-00-004_Storage_Metrics_Dashboard.yaml)
- [ATA 02-30 Circularity](../02-30_Circularity/) – Data lifecycle management

### 10.2 External References

- [Storage Performance Council](https://www.storageperformance.org/) – Industry benchmarks
- [SNIA](https://www.snia.org/) – Storage Networking Industry Association standards

---

## Document Control

- **Document ID**: 02-60-00-002
- **Version**: 1.0
- **Status**: DRAFT
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.
