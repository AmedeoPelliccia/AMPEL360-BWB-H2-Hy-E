# Spare Parts Provisioning Data
## Door L1 Forward

### Overview
This document provides guidance for operators on spare parts provisioning for Door L1 Forward. Recommendations are based on reliability data, usage patterns, and lead times.

### Provisioning Strategy

#### Initial Provisioning (per aircraft)
Recommended spare parts for the first 5 years of operation:

| Category | Investment | Parts Count |
|----------|-----------|-------------|
| Critical LRUs | €15,200 | 8 items |
| Essential LRUs | €8,400 | 12 items |
| Consumables | €1,800 | Stock items |
| **Total** | **€25,400** | |

#### Fleet Provisioning (10 aircraft)
Pooled spares to achieve 95% availability:

| Category | Investment | Parts Count |
|----------|-----------|-------------|
| Critical LRUs | €89,500 | 28 items |
| Essential LRUs | €42,000 | 52 items |
| Consumables | €12,000 | Stock items |
| **Total** | **€143,500** | |

### Critical LRUs

Parts requiring immediate availability:

| Part Number | Description | Price | Qty per Aircraft | Fleet Pool (10 AC) | Lead Time |
|-------------|-------------|-------|------------------|-------------------|-----------|
| PN-52-10-01-302001 | Door Controller | €3,250 | 0.5 | 2 | 60 days |
| PN-52-10-01-203001 | Motor Assembly | €1,850 | 0.5 | 2 | 90 days |
| PN-52-10-01-203002 | Gearbox | €1,420 | 0.5 | 2 | 90 days |
| PN-52-10-01-202001 | Hinge Arm | €520 | 0.3 | 1 | 60 days |
| PN-52-10-01-303001 | Position Sensor | €420 | 1.0 | 4 | 45 days |

### Essential LRUs

Parts with moderate criticality:

| Part Number | Description | Price | Qty per Aircraft | Fleet Pool (10 AC) | Lead Time |
|-------------|-------------|-------|------------------|-------------------|-----------|
| PN-52-10-01-204001 | Primary Seal | €285 | 2.0 | 8 | 30 days |
| PN-52-10-01-201001 | Latch Hook | €185 | 1.0 | 4 | 45 days |
| PN-52-10-01-204002 | Secondary Seal | €145 | 2.0 | 8 | 30 days |
| PN-52-10-01-202002 | Hinge Pin | €125 | 1.0 | 4 | 60 days |
| PN-52-10-01-301002 | Circuit Breakers | €95 | 1.0 | 4 | 45 days |

### Consumables

Regular replacement items:

| Part Number | Description | Price | Annual Usage per AC | Stock Level (10 AC) |
|-------------|-------------|-------|---------------------|---------------------|
| PN-52-10-01-501001 | Seal Lubricant | €12 | 12 units | 120 units |
| PN-52-10-01-501002 | IPA Cleaner | €8 | 18 units | 180 units |
| PN-52-10-01-501003 | Epoxy Adhesive | €45 | 6 units | 60 units |

### Provisioning Models

#### Model 1: Single Aircraft Operator
- Stock critical LRUs (1 each)
- Expedite remaining parts as needed
- Total investment: €25,400
- Target availability: 98%

#### Model 2: Small Fleet (3-5 aircraft)
- Pool critical LRUs (1-2 each)
- Stock consumables (2-year supply)
- Repair exchange program
- Total investment: €65,000
- Target availability: 99%

#### Model 3: Large Fleet (10+ aircraft)
- Full pooled spares strategy
- Regional distribution centers
- Remanufacturing capability
- Total investment: €143,500
- Target availability: 99.5%

### Stock Location Strategy

#### Base Stock
- Critical LRUs at main base
- Consumables at all stations
- Rotable repair pool

#### Regional Distribution
- Hubs serve 3-4 aircraft
- 24-hour courier service
- AOG emergency stock

#### Vendor Consignment
- High-value, low-usage items
- Pay on consumption
- Vendor maintains inventory

### Economic Analysis

#### Cost per Flight Hour
Based on 3,000 flight hours per aircraft per year:

| Category | Annual Cost per AC | Cost per FH |
|----------|-------------------|-------------|
| Consumables | €800 | €0.27 |
| LRU replacements | €1,200 | €0.40 |
| Remanufacturing | €600 | €0.20 |
| **Total** | **€2,600** | **€0.87** |

#### Total Cost of Ownership (10 years)

| Item | Single Aircraft | Fleet (10 AC) |
|------|----------------|---------------|
| Initial provisioning | €25,400 | €143,500 |
| Annual replenishment | €2,600 | €26,000 |
| 10-year total | €51,400 | €403,500 |
| Cost per FH (30k FH) | €1.71 | €1.35 |

**Fleet savings:** 21% reduction in per-FH costs

### Reliability Data

#### MTBF (Mean Time Between Failures)

| Component | MTBF (hours) | Annual Failures (3000 FH) |
|-----------|--------------|---------------------------|
| Door Controller | 50,000 | 0.06 |
| Motor Assembly | 30,000 | 0.10 |
| Position Sensor | 70,000 | 0.04 |
| Primary Seal | 10,000 | 0.30 |
| Latch Hook | 50,000 | 0.06 |

### Optimization Tools

#### CAOS Predictive Provisioning
- Usage pattern analysis
- Failure prediction
- Optimal stock levels
- Automated reordering
- Dynamic pooling

#### Benefits
- 15% reduction in inventory
- 20% reduction in AOG events
- Improved cash flow
- Better availability

### Supplier Programs

#### Repair Exchange
- Submit failed unit
- Receive serviceable unit
- Pay differential if needed
- Typical turnaround: 14 days

#### Pooling Agreements
- Share spares with other operators
- Coordinated by AMPEL360
- Usage tracking via blockchain
- Fair cost allocation

#### Consignment
- Supplier maintains inventory
- Located at operator site
- Pay on installation
- Automatic replenishment

### Documentation

Maintain records of:
- Inventory levels
- Usage rates
- Stockouts
- Excess inventory
- Turn rates
- Carrying costs

### Review Schedule

- **Monthly:** Consumption vs. forecast
- **Quarterly:** Stock levels optimization
- **Annually:** Provisioning model review
- **Continuous:** CAOS predictive updates

---

*Part of AMPEL360 OPT-IN Framework*
*Document: Provisioning_Data.md*
*Version: 1.0*
*Last Updated: 2025-11-03*
