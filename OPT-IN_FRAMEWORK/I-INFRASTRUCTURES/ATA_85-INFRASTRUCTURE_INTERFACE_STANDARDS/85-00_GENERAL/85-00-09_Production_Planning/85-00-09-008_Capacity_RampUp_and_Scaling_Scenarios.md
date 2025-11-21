# 85-00-09-008 Capacity RampUp and Scaling Scenarios

## Document Information

- **Document ID**: 85-00-09-008
- **Title**: Capacity RampUp and Scaling Scenarios
- **Version**: 1.0
- **Date**: 2025-11-21
- **Status**: Draft
- **Category**: Production Planning
- **ATA Chapter**: 85 - Infrastructure Interface Standards

## Purpose

This document defines capacity planning and scaling scenarios for ATA 85 infrastructure interfaces. It analyzes fleet growth projections, airport adoption rates, infrastructure capacity requirements, throughput planning, and the strategies to scale infrastructure deployment in alignment with aircraft production and market demand.

## Scope

This plan addresses:

- Fleet growth projections and demand scenarios
- Airport network expansion scenarios
- Infrastructure capacity requirements by phase
- Throughput and turnaround time analysis
- Scaling strategies for each infrastructure domain
- Bottleneck identification and mitigation
- Capacity investment planning and optimization

## Fleet Growth Projections

### BWB Fleet Forecast Scenarios

**Conservative Scenario**:
- EIS: 5-10 aircraft delivered
- EIS+5 years: 80-120 aircraft in service
- EIS+10 years: 200-300 aircraft in service
- EIS+15 years: 400-500 aircraft in service

**Base Case Scenario** (planning baseline):
- EIS: 10-15 aircraft delivered
- EIS+5 years: 150-200 aircraft in service
- EIS+10 years: 400-500 aircraft in service
- EIS+15 years: 750-1000 aircraft in service

**Optimistic Scenario**:
- EIS: 15-20 aircraft delivered
- EIS+5 years: 250-300 aircraft in service
- EIS+10 years: 600-800 aircraft in service
- EIS+15 years: 1200-1500 aircraft in service

### Fleet Distribution Assumptions

**Geographic Distribution** (Base Case, EIS+10):
- Europe: 30-35% (120-175 aircraft)
- North America: 25-30% (100-150 aircraft)
- Asia-Pacific: 25-30% (100-150 aircraft)
- Middle East: 10-12% (40-60 aircraft)
- Other regions: 3-5% (15-25 aircraft)

**Operator Type Distribution**:
- Network carriers: 60-70%
- Low-cost carriers: 20-25%
- Cargo operators: 5-10%
- Other (government, private): 3-5%

**Utilization Assumptions**:
- Average daily utilization: 10-12 flight hours
- Average cycles per day: 3-4
- Average turnaround time: 45-60 minutes (target)

## Airport Network Expansion Scenarios

### Airport Adoption Rate Scenarios

**Conservative Adoption**:
- EIS: 3-5 pilot airports
- EIS+2: 15-20 airports
- EIS+5: 40-60 airports
- EIS+10: 100-120 airports

**Base Case Adoption** (planning baseline):
- EIS: 3-5 pilot airports
- EIS+2: 20-30 airports
- EIS+5: 60-80 airports
- EIS+10: 150-200 airports

**Optimistic Adoption**:
- EIS: 5-8 pilot airports
- EIS+2: 30-40 airports
- EIS+5: 80-120 airports
- EIS+10: 250-300 airports

### Airport Selection and Prioritization

**Tier 1 Airports** (large international hubs):
- Expected daily BWB movements: 8-15+ at maturity
- Infrastructure priority: High
- Deployment timing: EIS to EIS+2
- Example count: 20-30 airports globally

**Tier 2 Airports** (major regional hubs):
- Expected daily BWB movements: 3-8 at maturity
- Infrastructure priority: Medium
- Deployment timing: EIS+1 to EIS+4
- Example count: 60-100 airports globally

**Tier 3 Airports** (secondary and regional):
- Expected daily BWB movements: 1-3 at maturity
- Infrastructure priority: Demand-driven
- Deployment timing: EIS+3 to EIS+8
- Example count: 100-200 airports globally

## Infrastructure Capacity Requirements

### H₂ Infrastructure Capacity

**Refueling Capacity per Airport** (Base Case):

**Tier 1 Airports** (at maturity, EIS+10):
- Daily BWB movements: 10-15
- H₂ consumption per movement: ~200-300 kg (average)
- Daily H₂ demand: 2,000-4,500 kg/day
- Storage capacity: 5,000-10,000 kg (2-3 days buffer)
- Refueling points: 8-12 gates

**Tier 2 Airports** (at maturity, EIS+10):
- Daily BWB movements: 4-8
- Daily H₂ demand: 800-2,400 kg/day
- Storage capacity: 2,000-5,000 kg
- Refueling points: 4-8 gates

**Tier 3 Airports** (at maturity, EIS+10):
- Daily BWB movements: 1-3
- Daily H₂ demand: 200-900 kg/day
- Storage capacity: 500-1,500 kg
- Refueling points: 2-4 gates

**Global H₂ Supply Requirement** (Base Case, EIS+10):
- Fleet size: 400-500 aircraft
- Average daily consumption per aircraft: 200-300 kg
- Total daily demand: 80,000-150,000 kg/day (~80-150 tonnes/day)
- Annual demand: 30,000-55,000 tonnes/year

**H₂ Production Scaling**:
- EIS: 3,000-5,000 tonnes/year (pilot airports)
- EIS+5: 15,000-25,000 tonnes/year
- EIS+10: 30,000-55,000 tonnes/year
- EIS+15: 60,000-100,000 tonnes/year (optimistic scenario)

### CO₂ Battery Infrastructure Capacity

**Battery Inventory per Airport** (Base Case):

**Tier 1 Airports** (at maturity):
- Daily BWB movements: 10-15
- Batteries per aircraft: 6 (average)
- Battery swap operations: 50-60% of movements (others charged in place)
- Daily battery swaps: 60-90 batteries
- Inventory requirement: 100-150 batteries (charged + in rotation)
- Charging bays: 30-50

**Tier 2 Airports** (at maturity):
- Daily BWB movements: 4-8
- Daily battery swaps: 24-48 batteries
- Inventory requirement: 40-80 batteries
- Charging bays: 15-30

**Tier 3 Airports** (at maturity):
- Daily BWB movements: 1-3
- Daily battery swaps: 6-18 batteries (or charging-only operations)
- Inventory requirement: 10-30 batteries
- Charging bays: 5-15

**Global Battery Fleet Requirement** (Base Case, EIS+10):
- Aircraft fleet: 400-500 aircraft
- Batteries per aircraft: 6 (installed)
- Airport buffer inventory: 1.5x installed base
- Total battery population: ~3,600-4,500 (installed) + 1,800-2,250 (ground) = 5,400-6,750 batteries

**Battery Production Scaling**:
- EIS: 300-500 batteries (pilot operations)
- EIS+5: 2,000-3,000 batteries
- EIS+10: 5,400-6,750 batteries
- EIS+15: 10,000-15,000 batteries (optimistic scenario)

### GSE and Ground Operations Capacity

**GSE Equipment per Airport** (Base Case):

**Tier 1 Airports**:
- BWB-compatible GPU units: 6-10
- Battery swap/charge equipment: 2-3 swap bays, 30-50 charge points
- eGSE units: 20-30 (tugs, loaders, service vehicles)
- Data interface units: 10-15 (GODI carts or fixed installations)

**Tier 2 Airports**:
- BWB-compatible GPU units: 3-6
- Battery charge equipment: 15-30 charge points
- eGSE units: 10-20
- Data interface units: 5-10

**Tier 3 Airports**:
- BWB-compatible GPU units: 1-3
- Battery charge equipment: 5-15 charge points
- eGSE units: 5-10
- Data interface units: 2-5

**Global GSE Scaling** (Base Case, EIS+10):
- BWB-compatible GPU units: 1,200-1,800 units globally
- Battery handling equipment: 200-300 swap systems, 5,000-8,000 charge points
- eGSE units: 4,000-6,000 units
- Data interface units: 1,500-2,500 units

### Passenger Boarding and Terminal Capacity

**Terminal Infrastructure per Airport**:

**Tier 1 Airports**:
- BWB-capable gates: 8-12
- Dual jetway gates: 60-80% of BWB gates
- Single jetway or ground boarding: 20-40%
- Passenger throughput: 3,000-5,000 passengers/day (BWB-related)

**Tier 2 Airports**:
- BWB-capable gates: 4-8
- Dual jetway gates: 30-50%
- Passenger throughput: 1,200-2,500 passengers/day

**Tier 3 Airports**:
- BWB-capable gates: 2-4
- Ground boarding primary: 50-80%
- Passenger throughput: 300-1,000 passengers/day

**Global Terminal Investment** (Base Case, EIS+10):
- BWB-capable gates: 1,200-1,600 gates worldwide
- Jetway upgrades/new installations: 800-1,200 jetways
- Passenger boarding bridges: Investment of $1-2 billion globally

## Throughput and Turnaround Time Analysis

### Turnaround Time Targets

**Target Turnaround Times** (Base Case):
- Short turnaround (quick stop): 45-60 minutes
- Standard turnaround: 60-90 minutes
- Extended turnaround (with maintenance): 90-180 minutes

**Turnaround Components and Timing**:

**Critical Path Activities**:
1. Passenger deplaning: 10-15 minutes (dual jetway)
2. Cabin cleaning and servicing: 15-25 minutes (parallel with other activities)
3. Cargo/baggage unload: 15-25 minutes (parallel)
4. Refueling (H₂): 20-30 minutes
5. Battery swap (if required): 20-30 minutes (or charging: 90+ minutes)
6. Cargo/baggage load: 15-25 minutes (parallel)
7. Passenger boarding: 15-20 minutes (dual jetway)
8. Final checks and pushback prep: 5-10 minutes

**Bottleneck Analysis**:
- H₂ refueling and battery swap are critical path items
- Parallel execution of passenger and cargo operations essential
- Dual jetway critical for competitive turnaround times
- Battery charging turnaround requires longer ground time (overnight or extended stop)

### Capacity Optimization Strategies

**Infrastructure Strategies**:
- Prioritize H₂ refueling speed (flow rate, connector efficiency)
- Battery swap capability at high-frequency airports
- Dual jetway deployment where turnaround time critical
- Parallel ground service vehicle operations

**Operational Strategies**:
- Advanced turnaround planning and coordination
- Predictive maintenance to avoid ground delays
- Pre-positioned equipment and resources
- Real-time monitoring and optimization

**Technology Strategies**:
- Automated or semi-automated battery swap
- High-speed data interfaces for reduced connection time
- Intelligent ground power management
- Turnaround optimization software and analytics

## Scaling Strategies by Infrastructure Domain

### H₂ Infrastructure Scaling Strategy

**Phase 1: Pilot and Validation** (EIS-18 to EIS+12 months):
- Focus on proving infrastructure designs and operations
- Limited airports (3-5) with full capability
- Tube trailer delivery primary method
- Establish supply chain and operational procedures

**Phase 2: Initial Scale** (EIS to EIS+36 months):
- Expand to 20-30 key airports
- Begin pipeline infrastructure at major hubs
- Regional H₂ production coordination
- Standardized deployment approach

**Phase 3: Network Expansion** (EIS+24 to EIS+60 months):
- Expand to 60-100 airports
- Pipeline infrastructure at 30-50% of locations
- Mature supply chain and operations
- Regional production and distribution networks

**Phase 4: Global Coverage** (EIS+48 months onward):
- Complete network coverage (150-200+ airports)
- Mature H₂ economy integration
- Technology refresh and optimization
- Next-generation infrastructure

**Capacity Scaling Challenges**:
- H₂ production capacity growth
- Pipeline infrastructure investment and lead times
- Regulatory approvals and permitting
- Supply chain and logistics

**Mitigation Strategies**:
- Long-term supply agreements with producers
- Multi-source supply strategies
- Early infrastructure investment incentives
- Regulatory streamlining and coordination

### CO₂ Battery Infrastructure Scaling Strategy

**Phase 1: Pilot and Validation**:
- Validate battery interface and operations
- Limited battery inventory (300-500 batteries)
- Charging-primary operations with swap validation
- Refine handling and logistics

**Phase 2: Initial Scale**:
- Expand battery production (2,000-3,000 batteries)
- Selective swap capability deployment
- Regional battery pooling
- Logistics network establishment

**Phase 3: Network Expansion**:
- Major battery production scale-up (5,000-7,000 batteries)
- Swap capability at high-frequency airports
- Regional service and refurbishment centers
- Battery lifecycle management programs

**Phase 4: Global Coverage**:
- Complete battery fleet (10,000-15,000 batteries at optimistic scenario)
- Mature swap and charging network
- Second-life battery applications
- Circular economy integration

**Capacity Scaling Challenges**:
- Battery production ramp-up and quality
- Electrical grid capacity at airports
- Battery logistics and distribution
- Battery health and lifecycle management

**Mitigation Strategies**:
- Early engagement with battery manufacturers
- Grid capacity planning and investment
- Regional battery service networks
- Predictive maintenance and health monitoring

### GSE and Ground Operations Scaling Strategy

**Phase 1: Pilot and Validation**:
- Adapter solutions for legacy GSE
- Prototype BWB-specific GSE
- Initial ground handler training
- Procedure validation and refinement

**Phase 2: Initial Scale**:
- Production orders for standardized GSE
- Expansion of training programs
- Regional GSE equipment distribution
- eGSE integration begins

**Phase 3: Network Expansion**:
- Full-scale GSE production and distribution
- Mature ground handler capabilities
- eGSE transition acceleration
- Technology integration and optimization

**Phase 4: Global Coverage**:
- Complete global GSE fleet
- Technology refresh cycles
- Next-generation eGSE
- Fully integrated ground operations

**Capacity Scaling Challenges**:
- GSE manufacturer engagement and capacity
- Ground handler investment and readiness
- Legacy GSE compatibility and phase-out
- Training and certification scale-up

**Mitigation Strategies**:
- Early GSE manufacturer partnerships
- Standardized equipment specifications
- Modular adapter solutions
- Centralized and regional training programs

### Terminal and Passenger Infrastructure Scaling Strategy

**Phase 1: Pilot and Validation**:
- Jetway adapter solutions at pilot airports
- Evacuation infrastructure validation
- Passenger flow optimization studies
- Emergency response training and drills

**Phase 2: Initial Scale**:
- Jetway upgrades/new installations (20-40 gates)
- Standardized adapter and equipment packages
- Regional fire/rescue coordination
- Ground boarding capability expansion

**Phase 3: Network Expansion**:
- Major jetway investment program (100-150 gates)
- Mix of dual and single jetway
- Mature emergency response capabilities
- Terminal flow optimization

**Phase 4: Global Coverage**:
- Complete gate network (200-300+ gates)
- Technology refresh and improvements
- Next-generation boarding solutions
- Continuous passenger experience enhancement

**Capacity Scaling Challenges**:
- Airport capital investment cycles
- Terminal modification complexity and cost
- Regulatory approvals for terminal changes
- Passenger flow and capacity constraints

**Mitigation Strategies**:
- Early airport engagement and planning
- Cost-effective adapter solutions
- Phased gate conversion approach
- Framework agreements with airports

## Bottleneck Identification and Mitigation

### Potential System Bottlenecks

**Bottleneck 1: H₂ Production and Supply**
- **Impact**: Limits fleet deployment and operations
- **Indicators**: H₂ availability <95%, price volatility
- **Mitigation**:
  - Diversified supply sources
  - Early production capacity commitments
  - Alternative airport selection if supply limited
  - Strategic H₂ reserves at key locations

**Bottleneck 2: Battery Production Capacity**
- **Impact**: Limits aircraft production and operational flexibility
- **Indicators**: Battery lead times >6 months, quality issues
- **Mitigation**:
  - Multiple battery suppliers
  - Early production ramp-up
  - Battery health and lifecycle management (extend usable life)
  - Alternative configurations (more charging, less swap)

**Bottleneck 3: Airport Infrastructure Investment**
- **Impact**: Limits route network and operational airports
- **Indicators**: Airport commitments lag fleet deployment
- **Mitigation**:
  - Framework agreements and incentives
  - Phased investment approaches
  - Cost-sharing models
  - Simplified deployments for lower-volume airports

**Bottleneck 4: Ground Handler Readiness**
- **Impact**: Operational delays and inefficiencies
- **Indicators**: Training gaps, equipment shortages, turnaround time issues
- **Mitigation**:
  - Comprehensive training programs
  - Equipment leasing and rental options
  - Centralized support and helpdesk
  - Performance monitoring and improvement

**Bottleneck 5: Regulatory Approvals**
- **Impact**: Delays in airport deployments and operations
- **Indicators**: Approval timelines exceed plans
- **Mitigation**:
  - Early regulatory engagement
  - Standardized approval packages
  - Mutual recognition among authorities
  - Dedicated regulatory coordination resources

## Capacity Investment Planning

### Investment Requirements by Phase (Base Case)

**Phase 1: Pilot** (EIS-18 to EIS+12 months):
- H₂ infrastructure: $20-40M (3-5 airports)
- Battery infrastructure: $30-50M (batteries + charging)
- GSE and ground ops: $10-20M
- Terminal infrastructure: $15-30M
- **Total: $75-140M**

**Phase 2: Initial Scale** (EIS to EIS+36 months):
- H₂ infrastructure: $100-200M (20-30 airports)
- Battery infrastructure: $150-250M (batteries + charging/swap)
- GSE and ground ops: $50-100M
- Terminal infrastructure: $100-200M
- **Total: $400-750M**

**Phase 3: Network Expansion** (EIS+24 to EIS+60 months):
- H₂ infrastructure: $300-600M (60-100 airports)
- Battery infrastructure: $400-700M (batteries + infrastructure)
- GSE and ground ops: $150-300M
- Terminal infrastructure: $300-600M
- **Total: $1,150-2,200M**

**Phase 4: Global Coverage** (EIS+48 months onward):
- H₂ infrastructure: $500-1,000M (150-200+ airports)
- Battery infrastructure: $600-1,200M (full fleet + infrastructure)
- GSE and ground ops: $300-600M
- Terminal infrastructure: $500-1,000M
- **Total: $1,900-3,800M**

**Cumulative Investment** (through EIS+10):
- **Base Case: $3.5-6.9 billion**
- Conservative Scenario: $2.5-5.0 billion
- Optimistic Scenario: $5.0-10.0 billion

### Investment Allocation by Stakeholder

**Infrastructure Providers** (H₂, energy): 30-40%
**Airports**: 30-40%
**Operators/Airlines**: 15-25%
**Government/Public**: 5-15% (subsidies, incentives)

### Return on Investment and Business Case

**Value Drivers**:
- Reduced emissions and environmental compliance
- Operational cost savings (fuel, maintenance)
- Route network expansion opportunities
- Competitive differentiation
- Regulatory and market positioning

**Payback Period** (typical):
- Large hub airports: 5-8 years
- Medium hub airports: 7-10 years
- Infrastructure providers: 8-12 years (through supply contracts)

## Risk Management

### Capacity Scaling Risks

**Risk**: Fleet deployment exceeds infrastructure capacity
**Mitigation**: 
- Conservative infrastructure planning (headroom)
- Flexible deployment sequencing
- Rapid response capability for bottlenecks
- Real-time monitoring and alerting

**Risk**: Infrastructure investment precedes demand (stranded assets)
**Mitigation**:
- Phased investment aligned with commitments
- Modular and scalable designs
- Multi-use infrastructure where possible
- Risk-sharing agreements with stakeholders

**Risk**: Supply chain constraints (H₂, batteries, equipment)
**Mitigation**:
- Early supplier engagement and commitments
- Multi-source strategies
- Buffer inventories and reserves
- Contingency plans and alternatives

**Reference**: [ASSETS/Risk_Assessments/85-00-09-A-301_Production_RampUp_Risk_Register.xlsx](ASSETS/Risk_Assessments/85-00-09-A-301_Production_RampUp_Risk_Register.xlsx)

## Key Performance Indicators

**Capacity Utilization**:
- Infrastructure utilization rate (target: 60-80% at maturity)
- Spare capacity margin (target: 20-30%)
- Peak vs. average utilization

**Scaling Performance**:
- Deployment rate vs. plan (airports, gates, equipment)
- Lead time from commitment to operational
- Cost per unit vs. plan

**Operational Performance**:
- Throughput vs. design capacity
- Turnaround time performance
- Bottleneck frequency and severity

**Investment Efficiency**:
- Cost per aircraft supported
- Capacity ROI and payback period
- Asset utilization and productivity

## Related Documentation

### Internal References
- [85-00-09-001_Production_Planning_Overview.md](85-00-09-001_Production_Planning_Overview.md)
- [85-00-09-002_Airport_Interface_RampUp_Plan.md](85-00-09-002_Airport_Interface_RampUp_Plan.md)
- [ASSETS/Plans/85-00-09-A-001_Master_Production_Schedule.xlsx](ASSETS/Plans/85-00-09-A-001_Master_Production_Schedule.xlsx)
- [ASSETS/Plans/85-00-09-A-002_RampUp_Curve_Scenarios.xlsx](ASSETS/Plans/85-00-09-A-002_RampUp_Curve_Scenarios.xlsx)

### External References
- IATA 20-Year Air Passenger Forecast
- Airbus Global Market Forecast
- Boeing Commercial Market Outlook

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21

---

**End of Document**
