# 02-80-00-004: Power Budget Tracking

## Purpose

This document defines how power and energy budgets are planned, tracked, and reviewed across flight phases and ground operations for the AMPEL360 BWB-H2-Hy-E aircraft, including Key Performance Indicators (KPIs) and reporting structures.

## Scope

Power budget tracking encompasses:

- **Budget Planning**: Pre-flight and operational phase power allocation
- **Real-Time Tracking**: Monitoring actual vs. planned power consumption
- **Variance Analysis**: Identifying deviations and root causes
- **KPI Reporting**: Performance metrics for stakeholders
- **Continuous Improvement**: Refining budgets based on operational data

## Power Budget Framework

### Budget Hierarchy

```
┌─────────────────────────────────────────────────────────┐
│              AIRCRAFT TOTAL POWER BUDGET                 │
│              (Generation - Distribution Losses)          │
└────────────────────┬────────────────────────────────────┘
                     │
      ┌──────────────┼──────────────┬──────────────┐
      ▼              ▼              ▼              ▼
 Flight Phase   System Type   Priority Level   Reserve
   Budgets        Budgets       Budgets        Margin
```

### Budget Types

#### 1. Flight Phase Budgets

Power budgets defined for each operational phase:

- **Ground Operations** (GPU/APU powered)
- **Taxi** (APU/fuel cell powered)
- **Takeoff** (maximum generator output)
- **Climb** (high power demand)
- **Cruise** (steady-state, optimized)
- **Descent** (reduced loads)
- **Approach and Landing** (safety margins)
- **Emergency** (essential loads only)

Details in [02-80-02_Energy_Budget_Management](./02-80-02_Energy_Budget_Management/).

#### 2. System-Level Budgets

Power allocated by system type:

- **Flight-Critical** (Priority 1)
- **Essential** (Priority 2)
- **Non-Essential** (Priority 3)
- **Comfort/Convenience** (Priority 4)

See priority framework in [02-80-00-003](./02-80-00-003_Energy_Management_Strategy.md).

#### 3. Reserve Margins

**Safety Reserves**: Per [CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes), adequate power must be available for all foreseeable conditions.

Typical margins:
- **Normal Operations**: 20% margin above maximum expected load
- **Single Generator Failure**: 10% margin on remaining sources
- **Emergency**: Essential loads only, 5% margin

## Budget Planning Process

### Pre-Design Phase

**Objective**: Establish preliminary power budgets for aircraft design.

**Inputs**:
- Mission requirements (range, payload, speed)
- System architecture (avionics, cabin, propulsion)
- Regulatory requirements ([CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes))

**Outputs**:
- Generator sizing (kW capacity)
- Battery capacity (kWh)
- Fuel cell power rating (kW)
- Distribution architecture (bus structure)

**Responsibility**: Energy Systems Engineering, Aircraft Design Team

### Pre-Flight Planning

**Objective**: Validate energy readiness for specific flight.

**Checks**:
- Battery SOC ≥ minimum threshold (e.g., 80%)
- Fuel cell H₂ tanks filled
- APU available (if required by MEL)
- GPU available at origin/destination (if needed)

**Tools**: Pre-flight checklist, dispatch system, OCC dashboard

**Responsibility**: Flight Crew, Dispatch, OCC

### In-Flight Monitoring

**Objective**: Track actual power consumption vs. planned budget in real-time.

**Telemetry** (see [02-80-00-002](./02-80-00-002_Cross_ATA_Energy_Data_Map.md)):
- Generator output (kW per source)
- Battery discharge/charge (kW, SOC)
- Bus voltages and currents
- Load distribution by system

**Displays**:
- Flight deck MFD: Electrical synoptic page
- ECAM/EICAS: Power system status and alerts
- OCC dashboard: Fleet energy overview

**Automation**: Real-time comparison to budget, alerts on deviations > threshold

**Responsibility**: Flight Control Computer, Flight Crew, OCC

### Post-Flight Analysis

**Objective**: Review actual energy usage, identify variances, improve future budgets.

**Data Sources**:
- Flight Data Recorder (FDR) / Quick Access Recorder (QAR)
- Battery BMS logs
- Fuel cell controller logs
- Maintenance event logs

**Analysis** (see [02-80-08](./02-80-08_Post_Flight_Energy_Analysis/)):
- Total energy consumed vs. planned
- Peak power vs. budget
- Efficiency metrics
- Anomalies and deviations

**Responsibility**: Engineering, Data Analytics Team

## Power Budget by Flight Phase

### Example: Cruise Phase Budget

**Total Available Power**: 150 kW (from 2× generators + fuel cell)

| System Category | Planned (kW) | % of Total | Priority |
|-----------------|--------------|------------|----------|
| **Flight Controls & Actuators** | 20 | 13% | 1 |
| **Avionics & Navigation** | 10 | 7% | 1 |
| **Communication** | 5 | 3% | 1/2 |
| **Environmental Control (ECS)** | 40 | 27% | 1/2 |
| **Cabin Systems** | 15 | 10% | 2/3 |
| **Galley** | 10 | 7% | 3 |
| **In-Flight Entertainment** | 12 | 8% | 3 |
| **Lighting** | 8 | 5% | 2/3 |
| **Miscellaneous** | 5 | 3% | 3/4 |
| **Distribution Losses** | 5 | 3% | — |
| **Subtotal (Planned Load)** | 130 | 87% | — |
| **Reserve Margin** | 20 | 13% | — |
| **Total** | 150 | 100% | — |

**Load Shedding Sequence** (if power < 130 kW):
1. IFE and galley (Priority 3/4) → Reduce to 115 kW
2. Non-essential cabin systems → Reduce to 100 kW
3. Alert crew for further action

**Tracking**: Compare actual load (from PDU telemetry) to this budget every second; alert if deviation > 10%.

### Example: Takeoff Phase Budget

**Total Available Power**: 180 kW (maximum generator output + battery assist)

| System Category | Planned (kW) | % of Total | Priority |
|-----------------|--------------|------------|----------|
| **Flight Controls (Full Authority)** | 30 | 17% | 1 |
| **Avionics** | 12 | 7% | 1 |
| **ECS (Full Pressurization)** | 50 | 28% | 1 |
| **Hydraulic Pumps** | 25 | 14% | 1 |
| **Lighting (Landing, Taxi)** | 10 | 6% | 1/2 |
| **Cabin Systems (Minimum)** | 8 | 4% | 2 |
| **Communication** | 5 | 3% | 1/2 |
| **IFE (Suspended)** | 0 | 0% | 3 (shed) |
| **Galley (Suspended)** | 0 | 0% | 3 (shed) |
| **Distribution Losses** | 10 | 6% | — |
| **Subtotal (Planned Load)** | 150 | 83% | — |
| **Reserve Margin** | 30 | 17% | — |
| **Total** | 180 | 100% | — |

**Note**: IFE and galley automatically shed during takeoff; reconnected after climb.

## Key Performance Indicators (KPIs)

### Energy Efficiency KPIs

#### 1. Energy Intensity

**Definition**: Energy consumed per available seat kilometer (ASK)

**Formula**: `Energy Intensity (kWh/ASK) = Total Energy (kWh) / (Seats × Distance (km))`

**Target**: Year-over-year reduction of 3%

**Reporting**: Monthly, by aircraft and fleet average

#### 2. Battery Cycle Life

**Definition**: Average cycles to 80% SOH

**Target**: > 3000 cycles (per battery pack specification)

**Tracking**: Battery BMS logs, prognostics models ([02-80-03](./02-80-03_Battery_Energy_Management/))

**Reporting**: Quarterly, with predictive replacement alerts

#### 3. Fuel Cell Efficiency

**Definition**: Electrical output / H₂ energy input

**Target**: > 50% at rated power, > 40% at partial load

**Tracking**: Fuel cell controller telemetry, efficiency calculations

**Reporting**: Per flight, trending monthly

#### 4. Power System Availability

**Definition**: % of scheduled flights with full power system availability (no MEL deferrals)

**Target**: > 99.5%

**Tracking**: Dispatch records, MEL logs

**Reporting**: Daily dashboard, monthly summary

### Operational KPIs

#### 5. Budget Variance

**Definition**: (Actual Energy - Planned Energy) / Planned Energy

**Target**: Mean absolute error < 5%

**Tracking**: Real-time monitoring, post-flight analysis

**Reporting**: Per flight, aggregated weekly

**Action**: Variance > 10% triggers investigation and potential budget revision

#### 6. Load Shedding Events

**Definition**: Count and duration of non-essential load shedding events

**Target**: < 1 event per 100 flights (excluding routine takeoff/landing shedding)

**Tracking**: Power management system logs

**Reporting**: Real-time alert, monthly trend

#### 7. Peak Power vs. Budget

**Definition**: Maximum instantaneous power / Budgeted peak power

**Target**: < 1.0 (no budget exceedance)

**Tracking**: PDU telemetry, 10 Hz sampling

**Reporting**: Post-flight, flagged if > 1.0

#### 8. Reserve Margin Utilization

**Definition**: Minimum reserve margin reached during flight

**Target**: Reserve never < 5% except in emergency

**Tracking**: Real-time calculation from available power and load

**Reporting**: Alert if < 10%, detailed analysis if < 5%

### Cost KPIs

#### 9. Ground Energy Cost per Flight

**Definition**: Total electricity/APU fuel cost during ground operations

**Target**: Reduce by 10% via GPU preference and time-of-use optimization

**Tracking**: GPU usage logs, APU fuel burn, electricity pricing

**Reporting**: Per flight, by airport, monthly summary (see [02-80-12](./02-80-12_Energy_Cost_Optimization/))

#### 10. Battery Replacement Cost per Flight Hour

**Definition**: Amortized battery pack replacement cost / Total flight hours

**Target**: Minimize via optimized charge/discharge cycling

**Tracking**: Battery health trending, cycle count, procurement costs

**Reporting**: Quarterly, with lifecycle projections

### Sustainability KPIs

#### 11. Renewable Energy Share

**Definition**: kWh from renewable sources / Total ground energy (kWh)

**Target**: > 50% by end of Year 2, > 80% by end of Year 5

**Tracking**: GPU renewable certification, solar charging logs ([02-80-11](./02-80-11_Renewable_Energy_Integration/))

**Reporting**: Monthly, by airport and fleet-wide

#### 12. Carbon Footprint (Energy-Related)

**Definition**: CO₂e emissions from electrical energy sources (scope 2)

**Formula**: `CO₂e = Energy (kWh) × Grid Emission Factor (kg CO₂e/kWh)`

**Target**: Aligned with AMPEL360 net-zero roadmap

**Tracking**: Energy usage logs, emission factors by airport/region

**Reporting**: Quarterly, included in sustainability reports

## Reporting Structure

### Real-Time Dashboards

**Flight Deck Display**:
- Current power sources and output
- Total load and reserve margin
- Battery SOC and range estimate
- Alerts for budget deviations

**OCC Dashboard** ([02-80-07](./02-80-07_Real_Time_Energy_Monitoring/)):
- Fleet-wide energy status
- Aircraft with active alerts
- Predictive load forecasts
- Budget variance by aircraft

### Periodic Reports

#### Daily Energy Summary (OCC)

**Audience**: Operations management, dispatch

**Content**:
- Total energy consumed (fleet and per aircraft)
- Budget variance summary
- Anomalies and alerts
- GPU vs. APU usage
- Cost summary

**Delivery**: Email, dashboard, 06:00 local time

#### Weekly Energy Review (Engineering)

**Audience**: Energy systems engineers, maintenance

**Content**:
- Detailed variance analysis
- System-level consumption trends
- Battery and fuel cell health updates
- Predictive maintenance alerts
- Efficiency trending

**Delivery**: Report document, review meeting

#### Monthly Performance Report (Executive)

**Audience**: Executive management, board

**Content**:
- KPI scorecard (green/yellow/red status)
- Year-to-date trends
- Cost analysis and savings
- Sustainability metrics
- Strategic initiatives progress

**Delivery**: Executive dashboard, presentation

#### Quarterly Deep Dive (Cross-Functional)

**Audience**: Engineering, operations, maintenance, finance, sustainability

**Content**:
- Comprehensive energy analysis
- Root cause analysis of anomalies
- Budget refinement recommendations
- Technology upgrade assessments
- Circularity and lifecycle updates

**Delivery**: Workshop, detailed technical report

## Budget Refinement Process

### Trigger Conditions for Budget Review

1. **Systematic Variance**: Budget variance > 10% for 3 consecutive flights
2. **Anomalous Event**: Unexpected load shedding or power shortage
3. **Fleet-Wide Trend**: Pattern observed across multiple aircraft
4. **Configuration Change**: New software, hardware, or operational procedures
5. **Seasonal Variation**: Different energy usage in extreme weather

### Refinement Steps

1. **Data Collection**: Gather telemetry from affected flights ([02-80-08](./02-80-08_Post_Flight_Energy_Analysis/))
2. **Root Cause Analysis**: Identify why variance occurred
   - Underestimated load?
   - New operational pattern?
   - System degradation?
   - Environmental factors?
3. **Budget Adjustment Proposal**: Recommend revised power allocations
4. **Validation**: Simulate adjusted budget, assess safety and operational impact
5. **Approval**: Cross-functional review (Safety, Engineering, Operations)
6. **Deployment**: Update budget in systems and documentation
7. **Monitoring**: Track performance under new budget for 30 days

### Example: Galley Power Budget Adjustment

**Observation**: Galley power consumption 15% higher than budget during cruise on long-haul flights.

**Analysis**: 
- Root cause: Increased passenger meal service frequency
- Impact: Reserve margin reduced from 20% to 12% (still safe, but less buffer)

**Action**:
- Revise cruise galley budget from 10 kW to 12 kW
- Compensate by reducing IFE budget from 12 kW to 10 kW (lower screen brightness)
- Net change: Maintain 20% reserve

**Validation**: Pilot on 5 flights, monitor variance

**Result**: Variance reduced from 15% to 3%; approved for fleet deployment

## Integration with Other Systems

### Energy Management Strategy

Power budgets implement the strategic priorities defined in [02-80-00-003](./02-80-00-003_Energy_Management_Strategy.md):
- Safety-first allocation (essential loads prioritized)
- Efficiency optimization (minimize waste)
- Cost management (balance GPU vs. APU based on budgets)

### Real-Time Monitoring

Budgets provide the baseline for anomaly detection in [02-80-07](./02-80-07_Real_Time_Energy_Monitoring/):
- Statistical process control (SPC) uses budget as mean
- Variance alerts triggered when actual exceeds budget control limits

### Predictive Optimization

AI/ML models in [02-80-05](./02-80-05_Energy_Optimization/) use budgets as constraints:
- Optimization algorithms must meet minimum reserve margins
- Load predictions validated against historical budget adherence

### Certification Compliance

Power budgets demonstrate compliance with [CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes):
- Show adequate power available for all required systems in all phases
- Document reserve margins and failure scenarios
- Trace load shedding logic to safety assessments

## Tools and Systems

### Budget Management Software

**Capabilities**:
- Pre-flight budget validation
- Real-time tracking and alerting
- Post-flight variance analysis
- Historical trending and reporting
- Budget scenario simulation

**Integration**:
- Flight planning systems (flight plan → predicted budget)
- Aircraft telemetry (ACARS, AFDX gateway)
- Maintenance systems (ATA 05 data)
- Data lake (historical analytics)

**Access**:
- Flight crew: Read-only (current budget, actual vs. budget)
- OCC: Real-time monitoring, alerting
- Engineering: Full access (read, analyze, propose updates)
- Management: Dashboards and reports

### Telemetry Infrastructure

**Data Sources**: Power Distribution Units (PDU), Battery BMS, Generator ECUs, Fuel Cell Controllers

**Transmission**: ARINC 664 (onboard), ACARS (air-to-ground), Secure FTP (post-flight)

**Storage**: Time-series database (hot), data lake (warm/cold archival)

**Processing**: Real-time streaming (Kafka), batch analytics (Spark)

See [02-80-00-002](./02-80-00-002_Cross_ATA_Energy_Data_Map.md) for data flow details.

## Governance and Roles

| Role | Responsibility |
|------|----------------|
| **Energy Systems Engineer** | Define and maintain power budgets, approve refinements |
| **Flight Operations** | Validate pre-flight energy readiness per budget |
| **OCC Dispatcher** | Monitor real-time budget adherence, alert on deviations |
| **Data Analyst** | Perform post-flight variance analysis, identify trends |
| **Maintenance Planner** | Address recurring variances caused by system degradation |
| **Safety Manager** | Ensure budget changes do not compromise safety margins per [CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes) |

## References

### Standards and Regulations

- [CS-25 – Certification Specifications for Large Aeroplanes](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes)
- [CS-25.1309 – Equipment, Systems, and Installations](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes)
- [CS-25.1351 – Electrical Systems and Equipment](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes)

### Internal Documents

- [02-80-00-001_Energy_Operations_Overview.md](./02-80-00-001_Energy_Operations_Overview.md)
- [02-80-00-002_Cross_ATA_Energy_Data_Map.md](./02-80-00-002_Cross_ATA_Energy_Data_Map.md)
- [02-80-00-003_Energy_Management_Strategy.md](./02-80-00-003_Energy_Management_Strategy.md)
- [02-80-02_Energy_Budget_Management](./02-80-02_Energy_Budget_Management/)
- [02-80-05_Energy_Optimization](./02-80-05_Energy_Optimization/)
- [02-80-07_Real_Time_Energy_Monitoring](./02-80-07_Real_Time_Energy_Monitoring/)
- [02-80-08_Post_Flight_Energy_Analysis](./02-80-08_Post_Flight_Energy_Analysis/)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-11-21*.

---
