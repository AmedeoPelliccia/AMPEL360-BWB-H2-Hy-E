# 85-00-14-003 — Service Levels and KPIs

## 1. Purpose

This document defines the **Service Level Agreements (SLAs)** and **Key Performance Indicators (KPIs)** for [ATA 85 – Infrastructure Interface Standards](https://www.ata.org/resources/specifications) supporting the AMPEL360 BWB H₂ Hy-E aircraft operations.

These metrics ensure infrastructure readiness, operational efficiency, safety, and sustainability across all ground interface operations.

---

## 2. Scope

### 2.1 Applicable Interfaces

Service levels and KPIs apply to:

1. **H₂ Infrastructure** — Hydrogen refuelling and storage
2. **CO₂ Battery Interface** — CO₂ battery charging and servicing
3. **Airport Interface** — Gates, bridges, ground power, data
4. **Ground Services Interface** — GSE connections and operations
5. **Passenger Boarding & Evacuation** — Boarding and emergency interfaces

### 2.2 Stakeholders

- **Airlines/Operators** — Service availability and turnaround efficiency
- **Airport Authorities** — Infrastructure readiness and safety compliance
- **Ground Service Providers** — Equipment performance and crew efficiency
- **Regulatory Bodies** — Safety and environmental compliance

---

## 3. Infrastructure Readiness KPIs

### 3.1 Availability Metrics

#### KPI-001: Infrastructure Availability Rate
- **Definition**: Percentage of scheduled operations where infrastructure is ready at gate/stand
- **Target**: ≥ 99.5% availability
- **Measurement**: (Ready operations / Scheduled operations) × 100
- **Data source**: Airport operations management system
- **Reporting frequency**: Daily, aggregated monthly

#### KPI-002: H₂ Refuelling System Uptime
- **Definition**: Percentage of time H₂ infrastructure is operational
- **Target**: ≥ 99.0% uptime
- **Measurement**: (Operational hours / Total hours) × 100
- **Data source**: H₂ infrastructure monitoring system
- **Reporting frequency**: Continuous monitoring, daily reports

#### KPI-003: CO₂ Battery Charging Availability
- **Definition**: Percentage of planned charging operations successfully completed
- **Target**: ≥ 98.5% success rate
- **Measurement**: (Successful charges / Planned charges) × 100
- **Data source**: Battery management system logs
- **Reporting frequency**: Per operation, aggregated weekly

### 3.2 Positioning and Connection Metrics

#### KPI-004: Equipment Positioning Time
- **Definition**: Average time to position GSE at aircraft interface points
- **Target**: ≤ 5 minutes per equipment item
- **Measurement**: Time from dispatch to ready-for-connection
- **Data source**: GSE tracking system
- **Reporting frequency**: Per turnaround, aggregated daily

#### KPI-005: Interface Connection Success Rate
- **Definition**: Percentage of first-attempt successful connections
- **Target**: ≥ 95% first-attempt success
- **Measurement**: (Successful first connections / Total connection attempts) × 100
- **Data source**: Operational logs and crew reports
- **Reporting frequency**: Per operation, aggregated weekly

---

## 4. Turnaround Efficiency KPIs

### 4.1 Service Time Metrics

#### KPI-010: H₂ Refuelling Time
- **Definition**: Total time to complete hydrogen refuelling
- **Target**: ≤ 15 minutes (standard turnaround)
- **Measurement**: Time from connection to disconnection
- **Data source**: H₂ system flow meters and logs
- **Reporting frequency**: Per operation

#### KPI-011: CO₂ Battery Service Time
- **Definition**: Total time for CO₂ battery charging/servicing
- **Target**: ≤ 10 minutes (rapid turnaround), ≤ 30 minutes (full charge)
- **Measurement**: Time from connection to ready-for-flight
- **Data source**: Battery management system
- **Reporting frequency**: Per operation

#### KPI-012: Ground Power Connection Time
- **Definition**: Time to establish ground power connection
- **Target**: ≤ 3 minutes
- **Measurement**: Time from arrival at stand to power available
- **Data source**: Ground power system logs
- **Reporting frequency**: Per turnaround

#### KPI-013: Data Link Establishment Time
- **Definition**: Time to establish airport data communications
- **Target**: ≤ 2 minutes
- **Measurement**: Time from connection to successful data exchange
- **Data source**: Aircraft and airport IT systems
- **Reporting frequency**: Per turnaround

### 4.2 Overall Turnaround Impact

#### KPI-014: Infrastructure-Related Turnaround Delays
- **Definition**: Total delay minutes attributed to infrastructure interface issues
- **Target**: ≤ 1% of total turnaround time
- **Measurement**: Sum of delay minutes / Total turnaround time
- **Data source**: Operations delay reporting system
- **Reporting frequency**: Per turnaround, aggregated daily

---

## 5. Safety and Incident KPIs

### 5.1 Safety Performance

#### KPI-020: Interface-Related Safety Incidents
- **Definition**: Number of safety incidents at infrastructure interfaces
- **Target**: Zero safety incidents per 10,000 operations
- **Categories**: Personnel injury, equipment damage, aircraft damage
- **Data source**: Safety reporting system
- **Reporting frequency**: Incident-based, aggregated monthly

#### KPI-021: H₂ Leak Detection Response Time
- **Definition**: Time from leak detection to system isolation
- **Target**: ≤ 30 seconds (automated), ≤ 2 minutes (manual)
- **Measurement**: Time from alarm to safe state
- **Data source**: H₂ safety system logs
- **Reporting frequency**: Per incident

#### KPI-022: Emergency Disconnect Success Rate
- **Definition**: Percentage of successful emergency disconnections
- **Target**: 100% success rate
- **Measurement**: (Successful emergency disconnects / Total emergency disconnect attempts) × 100
- **Data source**: Incident investigation reports
- **Reporting frequency**: Per incident

### 5.2 Operational Risk Metrics

#### KPI-023: Interface Malfunction Rate
- **Definition**: Number of interface malfunctions per 1,000 operations
- **Target**: ≤ 5 malfunctions per 1,000 operations
- **Measurement**: Total malfunctions / Operations × 1,000
- **Data source**: Maintenance and operations logs
- **Reporting frequency**: Monthly

---

## 6. Energy Performance and Sustainability KPIs

### 6.1 Energy Efficiency

#### KPI-030: Ground Power Efficiency
- **Definition**: Energy losses in ground power interface
- **Target**: ≤ 5% energy loss
- **Measurement**: (Input energy - Aircraft received energy) / Input energy × 100
- **Data source**: Power monitoring systems
- **Reporting frequency**: Per operation, aggregated weekly

#### KPI-031: H₂ Transfer Efficiency
- **Definition**: Hydrogen losses during refuelling
- **Target**: ≤ 2% H₂ loss (venting, spillage)
- **Measurement**: (H₂ dispensed - H₂ stored on aircraft) / H₂ dispensed × 100
- **Data source**: H₂ flow meters and tank sensors
- **Reporting frequency**: Per refuelling operation

### 6.2 Sustainability Metrics

#### KPI-032: Carbon Footprint of Ground Operations
- **Definition**: CO₂ equivalent emissions from ground interface operations
- **Target**: Aligned with [ATA 99 (Carbon Accounting)](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_99-CARBON_ACCOUNTING) targets
- **Measurement**: Total CO₂e from GSE, ground power, and infrastructure
- **Data source**: Energy monitoring and carbon accounting systems
- **Reporting frequency**: Monthly, aligned with ATA 99 reporting

#### KPI-033: Interface Hardware Recycling Rate
- **Definition**: Percentage of end-of-life interface hardware recycled
- **Target**: ≥ 85% by weight recycled or refurbished
- **Measurement**: (Recycled mass / Total retired mass) × 100
- **Data source**: Lifecycle management database
- **Reporting frequency**: Annually

See [85-00-14-004_Sustainability_and_Circularity_Strategy.md](./85-00-14-004_Sustainability_and_Circularity_Strategy.md) for sustainability strategy.

---

## 7. Data Integration and Monitoring

### 7.1 Data Sources and Systems

KPI data is collected from:

- **Airport Operations Management System** — Gate readiness, turnaround times
- **Infrastructure Monitoring Systems** — H₂, CO₂, power, data interface status
- **Aircraft Systems** — [Digital Product Passport (DPP)](../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS) data capture
- **Safety Reporting System** — Incidents and near-misses
- **Energy Management System** — Power consumption and sustainability data

### 7.2 Dashboard and Reporting

#### Real-Time Monitoring
- **Operations dashboards** for airport control centers
- **Alert thresholds** for critical KPIs (safety, availability)
- **Predictive analytics** for infrastructure readiness

#### Periodic Reporting
- **Daily ops reports** — Availability, delays, incidents
- **Weekly performance reviews** — Turnaround efficiency, energy performance
- **Monthly executive summaries** — Strategic KPIs and trends
- **Quarterly sustainability reports** — Aligned with [ATA 99](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_99-CARBON_ACCOUNTING)

See `ASSETS/KPIs_Dashboards/` for dashboard configuration files.

---

## 8. SLA Definitions

### 8.1 Infrastructure Availability SLA

**SLA-01: H₂ Infrastructure Availability**
- **Commitment**: H₂ refuelling available ≥ 99.0% of scheduled operations
- **Service credit**: 0.5% per hour of unplanned unavailability
- **Exceptions**: Scheduled maintenance, force majeure events

**SLA-02: Airport Interface Readiness**
- **Commitment**: Gate, bridge, power ready ≥ 99.5% of scheduled arrivals
- **Service credit**: Proportional to delay caused
- **Exceptions**: Aircraft early arrival, weather delays

### 8.2 Response Time SLAs

**SLA-10: Infrastructure Issue Response**
- **Commitment**: Technical support on-site within 10 minutes of notification
- **Service credit**: Delay compensation beyond 10 minutes
- **Escalation**: Automatic escalation after 15 minutes

---

## 9. Related Documentation

### Internal References

- [85-00-14-002_Operational_Standards_and_SOPs.md](./85-00-14-002_Operational_Standards_and_SOPs.md) — SOPs supporting KPI targets
- [85-00-14-006_Incident_Problem_and_Risk_Management.md](./85-00-14-006_Incident_Problem_and_Risk_Management.md) — Incident handling aligned with KPIs
- [ASSETS/KPIs_Dashboards/](./ASSETS/KPIs_Dashboards/) — Dashboard configurations

### Cross-ATA References

- [ATA 02-80 (Energy)](../../../../I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-80_Energy) — Energy operations data
- [ATA 99 (Carbon Accounting)](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_99-CARBON_ACCOUNTING) — Sustainability metrics
- [ATA 95 (DPP)](../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS) — Data capture and traceability

---

## 10. Status

- **Phase**: Service Level Definition (A-LIVE-GP Stage 14)
- **Maturity**: `DRAFT` — KPI targets to be validated with operational data
- **Last Updated**: 2025-11-21

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---

**End of Document**
