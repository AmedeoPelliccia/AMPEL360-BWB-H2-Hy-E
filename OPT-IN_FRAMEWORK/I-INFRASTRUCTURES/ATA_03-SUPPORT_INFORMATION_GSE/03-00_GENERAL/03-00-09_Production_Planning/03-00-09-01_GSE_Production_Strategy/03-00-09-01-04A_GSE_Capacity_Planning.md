# 03-00-09-01-04A - GSE Capacity Planning

**Version:** A  
**Date:** 2025-12-07  
**Status:** DRAFT  
**Document ID:** 03-00-09-01-04A

---

## 1. Purpose

This document defines the capacity planning approach for Ground Support Equipment (GSE) production to support the AMPEL360 BWB H2 Hy-E aircraft program. It establishes production capacity requirements, resource allocation strategies, and scalability plans to meet program demand.

---

## 2. Scope

This capacity planning document covers:
- Production capacity requirements by GSE category
- Resource requirements (facilities, equipment, workforce)
- Capacity utilization and optimization
- Scalability and flexibility planning
- Bottleneck identification and mitigation
- Long-term capacity strategy

---

## 3. Applicable Documents

- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- SAE ARP1796 (GSE Design Requirements)
- ISO 9001 (Quality Management Systems)
- AMPEL360 Aircraft Production Plan
- Reference: 03-00-09-01-03A (GSE Production Roadmap)

---

## 4. Capacity Planning Requirements

### 4.1 GSE Demand Forecast

#### 4.1.1 Aircraft Production Alignment

| Year | Aircraft Deliveries | GSE Sets Required | Cumulative GSE Sets |
|------|---------------------|-------------------|---------------------|
| 2026 | 2 | 5 | 5 |
| 2027 | 8 | 20 | 25 |
| 2028 | 20 | 30 | 55 |
| 2029 | 35 | 45 | 100 |
| 2030 | 50 | 60 | 160 |

**Notes:**
- GSE sets include both customer-specific and common pool equipment
- Assumes 2.5x GSE set multiplier for initial fleet establishment
- Aftermarket and replacement demand not included

#### 4.1.2 GSE Set Composition

One complete GSE set includes:
- 1x LH2 Fueling Unit (primary criticality)
- 1x LH2 Storage/Transport Unit
- 1x Ground Power Unit (H2 fuel cell)
- 2x H2 Safety Equipment Sets
- 1x Nitrogen Purge Unit
- Standard GSE: tow tractor, stairs, cargo loader, etc.
- BWB-specific: custom access platforms and stands

---

## 5. Production Capacity Analysis

### 5.1 Current and Target Capacity

| GSE Category | Current | 2026 | 2027 | 2028 | 2030 |
|--------------|---------|------|------|------|------|
| Complete GSE Sets/month | 0 | 0.5 | 2 | 3 | 5 |
| LH2 Fueling Units/month | 0 | 1 | 3 | 5 | 8 |
| Ground Power Units/month | 0 | 1 | 3 | 5 | 8 |
| Standard GSE/month | 0 | 5 | 15 | 25 | 40 |

### 5.2 Capacity by Production Stage

#### 5.2.1 Fabrication Capacity

| Process | Current | Target 2028 | Utilization | Constraint |
|---------|---------|-------------|-------------|-----------|
| Welding (H2 qualified) | 0 | 10 stations | 75% | Skilled labor |
| Machining | 0 | 8 machines | 70% | Equipment |
| Assembly | 0 | 6 lines | 80% | Space |
| Testing (cryogenic) | 0 | 4 cells | 85% | Equipment |
| Inspection/QC | 0 | 15 stations | 60% | Personnel |

#### 5.2.2 Bottleneck Analysis

**Critical Bottlenecks:**
1. **Cryogenic Testing** - Longest cycle time, specialized equipment
2. **H2-Qualified Welding** - Limited workforce, certification requirements
3. **LH2 Component Supply** - Limited supplier base

**Mitigation Actions:**
- Cryogenic testing: Add 2nd shift, external test facility partnership
- Welding: Accelerated training program, recruit experienced welders
- Supply: Qualify additional suppliers, maintain strategic inventory

---

## 6. Resource Requirements

### 6.1 Facility Requirements

#### 6.1.1 Production Floor Space

| Area | 2026 | 2027 | 2028 | 2030 | Notes |
|------|------|------|------|------|-------|
| Assembly (m²) | 800 | 1,500 | 2,500 | 3,500 | Climate controlled |
| Welding (m²) | 400 | 700 | 1,000 | 1,200 | H2-safe ventilation |
| Testing (m²) | 600 | 1,000 | 1,500 | 2,000 | Cryogenic capable |
| Storage (m²) | 300 | 600 | 1,000 | 1,500 | Secure/climate controlled |
| Quality Lab (m²) | 200 | 300 | 400 | 500 | Metrology equipment |
| **Total (m²)** | **2,300** | **4,100** | **6,400** | **8,700** | |

#### 6.1.2 Facility Capabilities

Required capabilities:
- Hydrogen-safe production areas (ventilation, monitoring)
- Cryogenic test facilities (-253°C capability)
- Clean room areas for critical component assembly
- Pressure test cells (up to 700 bar for H2 systems)
- NDT (Non-Destructive Testing) capabilities
- Environmental test chambers

### 6.2 Equipment and Tooling

#### 6.2.1 Major Equipment Investment

| Equipment Category | Quantity 2028 | Unit Cost | Total Investment |
|-------------------|---------------|-----------|------------------|
| CNC Machines | 8 | $200k | $1.6M |
| Welding Stations (H2 certified) | 12 | $80k | $960k |
| Cryogenic Test Cells | 4 | $500k | $2.0M |
| Leak Test Systems | 6 | $150k | $900k |
| Assembly Tooling | Sets | $100k | $600k |
| NDT Equipment | Suite | $400k | $400k |
| Metrology Equipment | Suite | $300k | $300k |
| **Total** | | | **$6.76M** |

#### 6.2.2 Tooling Strategy

- Modular tooling for flexibility
- Quick-change fixtures for product variants
- Digital work instructions and MES integration
- Tool life management and preventive maintenance

### 6.3 Workforce Planning

#### 6.3.1 Headcount by Function

| Role | 2026 | 2027 | 2028 | 2030 | Key Skills |
|------|------|------|------|------|------------|
| Production Engineers | 8 | 15 | 25 | 30 | GSE design, H2 systems |
| Welders (H2 certified) | 6 | 15 | 25 | 30 | Cryogenic welding, ASME |
| Machinists | 4 | 10 | 18 | 22 | CNC, precision machining |
| Assembly Technicians | 15 | 30 | 60 | 80 | Mechanical assembly |
| Test Technicians | 8 | 15 | 25 | 30 | Cryogenic systems, H2 safety |
| Quality Inspectors | 10 | 18 | 30 | 35 | NDT, metrology, FAI |
| Planners/Schedulers | 3 | 6 | 10 | 12 | Production planning |
| Supply Chain | 4 | 8 | 12 | 15 | Procurement, logistics |
| **Total** | **58** | **117** | **205** | **254** | |

#### 6.3.2 Training Requirements

**H2 Safety Training:**
- All personnel: H2 awareness (8 hours)
- Production staff: H2 handling (40 hours)
- Welders: H2 welding certification (80 hours + qualification)

**Specialized Training:**
- Cryogenic systems handling
- Pressure system assembly and testing
- Quality inspection techniques (NDT)
- Lean manufacturing and continuous improvement

---

## 7. Capacity Utilization Strategy

### 7.1 Utilization Targets

| Resource Type | Target Utilization | Rationale |
|---------------|-------------------|-----------|
| Production Equipment | 75-85% | Allows for maintenance, flexibility |
| Test Equipment | 80-90% | Critical path, maximize throughput |
| Workforce | 85-95% | Efficient but sustainable |
| Facility Space | 70-80% | Growth capacity, staging area |

### 7.2 Shift Strategy

| Phase | Shift Pattern | Rationale |
|-------|---------------|-----------|
| Pilot Production | 1 shift (8h) | Learning curve, process validation |
| Production Ramp | 1.5 shifts (12h) | Capacity increase, critical operations 2nd shift |
| Full Production | 2 shifts (16h) | Maximize equipment utilization |
| Sustaining | 1.5-2 shifts | Demand-driven |

### 7.3 Flexibility and Surge Capacity

**Flexibility Mechanisms:**
- Overtime availability (up to 20% capacity increase)
- Weekend production for critical items
- Contract manufacturing for non-critical GSE
- Supplier capacity agreements with surge provisions

**Surge Capacity:**
- 30% above baseline with existing resources (overtime)
- 50% with temporary workforce and equipment rental
- 100% with contract manufacturing activation

---

## 8. Scalability Planning

### 8.1 Expansion Phases

#### Phase 1: Core Capacity (2025-2026)
- Establish initial production capability
- 1,000 m² facility
- Single shift operation
- Capacity: 0.5 GSE sets/month

#### Phase 2: Scale-Up (2027-2028)
- Expand to 3,000 m² facility
- Two-shift operation
- Capacity: 3 GSE sets/month

#### Phase 3: Full-Scale (2028-2030)
- Expand to 6,000+ m² facility
- Two-shift operation
- Capacity: 5 GSE sets/month

### 8.2 Modular Expansion Strategy

- Design production lines for modular expansion
- Add capacity in 25% increments
- Minimize disruption to ongoing production
- Reuse tooling and equipment where possible

---

## 9. Capacity Optimization

### 9.1 Lean Manufacturing Principles

- Value stream mapping to identify waste
- Single-piece flow where feasible
- Pull systems for material management
- Continuous improvement (Kaizen)

### 9.2 Production Efficiency Targets

| Metric | Baseline | Target 2028 | Improvement |
|--------|----------|-------------|-------------|
| Cycle Time (GSE set) | TBD | 30 days | -30% |
| First-Pass Yield | TBD | 95% | +15% |
| Equipment OEE | TBD | 85% | +20% |
| Inventory Turns | TBD | 12x/year | +100% |

### 9.3 Digital Manufacturing

- Manufacturing Execution System (MES)
- Real-time production tracking
- Digital work instructions
- Predictive maintenance
- Data analytics for optimization

---

## 10. Supply Chain Capacity

### 10.1 Supplier Capacity Assessment

| Supplier Category | Current Capacity | Required 2028 | Gap | Mitigation |
|------------------|------------------|---------------|-----|-----------|
| Cryogenic Components | Limited | High | High | Qualify additional suppliers |
| H2 Valves/Fittings | Moderate | High | Medium | Capacity agreements |
| Standard Hardware | High | High | None | Multiple sources |
| Electronics | High | High | Low | Contract extensions |

### 10.2 Inventory Strategy

- Strategic inventory for long-lead items (3-6 months)
- Just-in-time for standard components
- Consignment inventory with key suppliers
- Safety stock for critical H2 components

---

## 11. Risk Management

### 11.1 Capacity Risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Demand spike | Medium | High | Flexible capacity, surge plans |
| Supplier constraints | High | High | Multiple sources, inventory |
| Skilled labor shortage | High | Medium | Training programs, retention |
| Equipment breakdown | Medium | High | Preventive maintenance, spares |
| Quality issues | Low | High | Robust QMS, early detection |

### 11.2 Contingency Plans

- Contract manufacturing agreements (activated on demand)
- Equipment rental arrangements
- Temporary workforce agencies
- Alternative supplier qualification

---

## 12. Cross-References

- Related ATA Chapters:
  - ATA 03-00-06 (GSE Engineering)
  - ATA 03-00-07 (GSE V&V)
- Parent Document: 03-00-09-01_GSE_Production_Strategy
- Related Documents:
  - 03-00-09-01-03A (Production Roadmap)
  - 03-00-09-06-01A (Master Schedule)
  - 03-00-09-06-03A (Resource Allocation)

---

## 13. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Production Planning | Initial release |

---

**Document Control Information:**
- **Status**: DRAFT
- **Classification**: Internal - Production
- **Distribution**: Production Planning Team, Operations Management
