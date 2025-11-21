# 02-70-00-003 — Propulsion Performance Monitoring

## Document Information

- **Document ID**: 02-70-00-003
- **Title**: Propulsion Performance Monitoring
- **Subsystem**: ATA 02-70 Propulsion
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-21

## Table of Contents

1. [Introduction](#1-introduction)
2. [Monitoring Concept](#2-monitoring-concept)
3. [Key Performance Indicators](#3-key-performance-indicators)
4. [Data Sources](#4-data-sources)
5. [Dashboards and Visualization](#5-dashboards-and-visualization)
6. [Alerting](#6-alerting)
7. [Integration with Predictive Maintenance](#7-integration-with-predictive-maintenance)
8. [Digital Twin Linkage](#8-digital-twin-linkage)
9. [References](#9-references)

## 1. Introduction

### 1.1 Purpose

This document describes the overall propulsion performance monitoring concept for the AMPEL360 BWB H₂ Hybrid-Electric aircraft, including KPIs, data sources, visualization, alerting mechanisms, and integration with predictive maintenance and digital twin systems.

### 1.2 Scope

This monitoring concept covers:
- Real-time performance monitoring during flight
- Post-flight performance analysis
- Long-term trending and fleet comparison
- Integration with health monitoring systems
- Linkage to predictive maintenance and digital twin

### 1.3 Objectives

- **Operational Efficiency**: Maximize propulsion system efficiency across all flight phases
- **Safety Assurance**: Detect and alert on performance deviations that may indicate safety issues
- **Maintenance Optimization**: Enable condition-based and predictive maintenance
- **Continuous Improvement**: Provide data for performance model refinement and design improvements

## 2. Monitoring Concept

### 2.1 Monitoring Layers

```
┌────────────────────────────────────────────────────────────┐
│         Layer 1: Real-Time Crew Monitoring                 │
│  • Primary Flight Displays  • EICAS/ECAM  • EFB Pages     │
│  Purpose: Immediate crew situational awareness             │
└────────────────────────────────────────────────────────────┘
                           │
                           ↓
┌────────────────────────────────────────────────────────────┐
│         Layer 2: Ground Real-Time Monitoring               │
│  • OCC Dashboards  • Fleet Overview  • Alert Management   │
│  Purpose: Operations center fleet monitoring               │
└────────────────────────────────────────────────────────────┘
                           │
                           ↓
┌────────────────────────────────────────────────────────────┐
│         Layer 3: Post-Flight Analysis                      │
│  • Performance Reports  • Efficiency Analysis  • Trending  │
│  Purpose: Continuous improvement and optimization          │
└────────────────────────────────────────────────────────────┘
                           │
                           ↓
┌────────────────────────────────────────────────────────────┐
│         Layer 4: Long-Term Analytics                       │
│  • Fleet Comparison  • Model Validation  • Certification   │
│  Purpose: Strategic insights and regulatory compliance     │
└────────────────────────────────────────────────────────────┘
```

### 2.2 Monitoring Philosophy

- **Hierarchical Alerting**: Information → Caution → Warning based on severity and time criticality
- **Contextual Display**: Different information shown based on flight phase and operational mode
- **Trend Awareness**: Not just current values, but rate of change and historical context
- **Predictive**: Where possible, predict future state to enable proactive intervention
- **Integrated**: Correlate propulsion performance with other systems (flight controls, weather, etc.)

## 3. Key Performance Indicators

### 3.1 Fuel Cell System KPIs

| KPI | Definition | Target | Alert Threshold | Purpose |
|-----|------------|--------|-----------------|---------|
| Stack Efficiency | (Electrical Power Out) / (H₂ LHV Energy In) | >55% | <50% | Energy optimization |
| Voltage per Cell | Individual cell voltage | 0.6-0.8 V | <0.5 V | Health, degradation |
| Current Density | Current per unit membrane area | <1.5 A/cm² | >2.0 A/cm² | Degradation prevention |
| Operating Temperature | Stack temperature | 60-80°C | <50°C or >90°C | Performance, safety |
| Degradation Rate | Voltage drop per hour | <1 µV/h | >5 µV/h | RUL estimation |
| H₂ Utilization | % of supplied H₂ consumed | >95% | <90% | Efficiency |

### 3.2 Electric Motor KPIs

| KPI | Definition | Target | Alert Threshold | Purpose |
|-----|------------|--------|-----------------|---------|
| Motor Efficiency | (Mechanical Power Out) / (Electrical Power In) | >94% | <90% | Energy optimization |
| Thrust Output | Net thrust delivered | Per flight phase | <Required | Performance assurance |
| Winding Temperature | Hotspot temperature | <120°C | >140°C | Thermal protection |
| Bearing Temperature | Bearing hotspot | <80°C | >100°C | Health monitoring |
| Vibration Level | RMS vibration | <2 mm/s | >5 mm/s | Condition monitoring |
| Speed Regulation | Error vs. commanded | <±1% | >±3% | Control performance |

### 3.3 H₂ Fuel System KPIs

| KPI | Definition | Target | Alert Threshold | Purpose |
|-----|------------|--------|-----------------|---------|
| Fuel Consumption Rate | kg/h H₂ consumed | Per flight profile | >110% predicted | Range management |
| Boiloff Rate | kg/h H₂ vented | <0.5% tank capacity/day | >1% tank capacity/day | Efficiency, planning |
| Tank Pressure | H₂ storage pressure | 5-8 bar | <4 bar or >10 bar | Safety, performance |
| System Efficiency | Energy delivered vs. fuel energy | >50% total | <45% total | Overall performance |
| Range Available | Calculated range from fuel | Per mission | <Reserve requirement | Safety, planning |

### 3.4 Thermal Management KPIs

| KPI | Definition | Target | Alert Threshold | Purpose |
|-----|------------|--------|-----------------|---------|
| Cooling Capacity Margin | Available vs. utilized cooling | >20% | <10% | Thermal protection |
| Coolant Temperature | Coolant supply temperature | 20-40°C | >50°C | Component protection |
| Heat Exchanger Effectiveness | Actual vs. ideal heat transfer | >80% | <70% | System health |
| Pump Efficiency | Hydraulic power vs. electrical | >70% | <60% | Energy optimization |

### 3.5 Integrated System KPIs

| KPI | Definition | Target | Alert Threshold | Purpose |
|-----|------------|--------|-----------------|---------|
| Total Propulsion Efficiency | (Thrust Power) / (H₂ Energy In) | >45% | <40% | Overall performance |
| Specific Fuel Consumption | kg H₂ per kN thrust per hour | <0.15 | >0.18 | Economics, emissions |
| Power-to-Weight Ratio | kW per kg propulsion system | >5 kW/kg | <4 kW/kg | Performance benchmark |
| Availability | % time propulsion at full capability | >99.5% | <98% | Dispatch reliability |

## 4. Data Sources

### 4.1 Sensor Data

**Primary Sources**:
- Fuel cell voltage/current sensors (ATA 73)
- Motor speed/torque sensors (ATA 72)
- H₂ fuel quantity/flow sensors (ATA 28)
- Temperature sensors (all subsystems)
- Pressure sensors (fuel, cooling, ambient)

**Data Rate**: 1-100 Hz depending on parameter criticality

**Quality**: Hardware redundancy, cross-validation, outlier detection

### 4.2 Time-Series Database (TSDB)

**Purpose**: High-frequency data storage for trend analysis

**Technology**: InfluxDB, TimescaleDB, or similar

**Data Retention**: 
- Raw data: 7 days onboard, 90 days ground
- 1-minute averages: 1 year
- 1-hour averages: 10 years

**Access**: Real-time query API for dashboards and analytics

### 4.3 Derived Metrics

**Source**: ATA 02 performance calculators

**Examples**:
- Efficiencies (calculated from sensor inputs)
- Thrust (from motor torque, propeller curves, flight conditions)
- Range (from fuel quantity, consumption rate, performance model)
- Degradation indices (from historical trending)

**Update Rate**: 0.1-1 Hz

### 4.4 Digital Twin Inputs

**Source**: [ATA 95 Digital Twin](../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/)

**Data**:
- Predicted performance under current conditions
- Optimal operating points
- Remaining useful life estimates
- What-if scenario results

**Update Rate**: 0.01-0.1 Hz

See: [02-70-10_Digital_Twin_Integration](./02-70-10_Digital_Twin_Integration/)

## 5. Dashboards and Visualization

### 5.1 Cockpit Displays (EFB)

**Purpose**: Immediate crew situational awareness

**Content**:
- Current thrust available (graphical gauge)
- H₂ fuel quantity and range (numeric + trend)
- Fuel cell and motor status (health icons)
- Performance efficiency vs. optimal (bar chart)
- Active alerts and cautions (prioritized list)

**Update Rate**: 1 Hz visual refresh

**Interaction**: Touch interface for detailed views

### 5.2 OCC Real-Time Dashboard

**Purpose**: Ground-based fleet monitoring

**Content**:
- Fleet map with aircraft status markers
- Per-aircraft propulsion summary (health, performance, fuel)
- Alert feed with filtering and acknowledgment
- Fleet-wide efficiency comparison
- Predictive maintenance queue

**Update Rate**: 1 Hz via ACARS/satellite link

**Technology**: Web-based (React/Vue), backend Python/Node.js

**Access Control**: Role-based (dispatcher, maintenance coordinator, management)

### 5.3 Post-Flight Analysis Dashboard

**Purpose**: Detailed performance review

**Content**:
- Flight profile with performance overlay (altitude, speed, thrust, fuel flow)
- Efficiency by flight phase
- Comparison vs. planned performance
- Component health trends
- Anomaly detection results

**Update Rate**: Generated within 1 hour of landing

**Distribution**: Email report + web portal access

### 5.4 Long-Term Analytics Dashboard

**Purpose**: Fleet-wide insights and optimization

**Content**:
- Fleet efficiency trends over time
- Aircraft-to-aircraft comparison
- Route-specific performance patterns
- Seasonal/environmental correlations
- Maintenance cost vs. performance degradation

**Update Rate**: Daily/weekly refresh

**Users**: Performance engineering, management, certification

## 6. Alerting

### 6.1 Alert Categories

**Information (Blue)**:
- Non-time-critical status changes
- Scheduled maintenance approaching
- Performance slightly below optimal

**Caution (Amber)**:
- Approaching operational limits
- Degraded but safe performance
- Single system redundancy loss

**Warning (Red)**:
- Operational limits exceeded
- Safety-critical system malfunction
- Immediate crew action required

### 6.2 Alert Logic

Alerts generated based on:
- **Absolute Thresholds**: Fixed limits (e.g., temperature >140°C)
- **Relative Thresholds**: Deviation from expected (e.g., >10% efficiency drop)
- **Rate of Change**: Rapid changes (e.g., pressure drop >1 bar/min)
- **Pattern Recognition**: AI/ML detection of anomalous patterns
- **Predictive**: Forecasted limit exceedance within next 5-30 minutes

### 6.3 Alert Routing

- **Cockpit**: EICAS/ECAM + EFB
- **OCC**: Real-time dashboard + automated notification (email/SMS)
- **Maintenance**: OMS message + maintenance planning system
- **Engineering**: If pattern indicates design issue or certification impact

### 6.4 Alert Suppression

- Phase-of-flight filtering (some alerts inhibited during takeoff/landing)
- Transient suppression (require persistence for >5 seconds)
- Acknowledged alert tracking (prevent alert fatigue)
- Intelligent grouping (related alerts consolidated)

## 7. Integration with Predictive Maintenance

### 7.1 Data Pipeline

```
Performance Monitoring → Health Indicators → Prognostic Models → Maintenance Actions
      (ATA 02)              (ATA 45)           (ATA 95)             (MRO Systems)
```

### 7.2 Health Indicators

Derived from performance monitoring:
- **Degradation Trends**: Efficiency decline over flight hours
- **Vibration Signatures**: Motor/bearing wear patterns
- **Thermal Patterns**: Hot spots, cooling ineffectiveness
- **Operational Exceedances**: Frequency and severity of limit approaches

See: [02-70-04_Propulsion_System_Health](./02-70-04_Propulsion_System_Health/)

### 7.3 Prognostic Models

[ATA 95 ML models](../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/) use performance data to predict:
- **Remaining Useful Life (RUL)**: Time/cycles until component reaches failure threshold
- **Probability of Failure (POF)**: Risk of failure within next mission/week/month
- **Optimal Maintenance Timing**: Balance reliability vs. cost

### 7.4 Maintenance Recommendations

Automated generation of:
- **Inspection recommendations**: "Inspect fuel cell stack manifold within 50 flight hours"
- **Deferral guidance**: "Current performance allows safe deferral of motor bearing replacement to next scheduled check"
- **Spare parts alerts**: "Order replacement heat exchanger, predicted need in 200 flight hours"

## 8. Digital Twin Linkage

### 8.1 Model Synchronization

Performance monitoring data feeds [Digital Twin](./02-70-10_Digital_Twin_Integration/) to:
- Update model state to match actual aircraft
- Calibrate model parameters (component efficiencies, degradation rates)
- Validate model predictions against actual performance

**Sync Frequency**: Real-time (1 Hz) during flight, batch post-flight for calibration

### 8.2 Predictive Simulation

Digital twin uses current state and planned flight to predict:
- Expected performance metrics for next flight phase
- Fuel consumption for route planning
- Impact of weather or operational changes

### 8.3 What-If Analysis

Enables ground planning queries:
- "Can we fly this longer route with current aircraft state?"
- "What is the efficiency impact of deferring this maintenance?"
- "How does fuel cell degradation affect our dispatch reliability?"

### 8.4 Model Cards

All digital twin models documented per [ATA 95 Model Card standard](../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/) including:
- Training data provenance
- Model accuracy and limitations
- Intended use cases
- Ethical considerations

## 9. References

### Internal Documents
- [02-70-00-001 Propulsion Ops Integration Overview](./02-70-00-001_Propulsion_Ops_Integration_Overview.md)
- [02-70-00-002 Cross-ATA Propulsion Data Map](./02-70-00-002_Cross_ATA_Propulsion_Data_Map.md)
- [02-70-04_Propulsion_System_Health](./02-70-04_Propulsion_System_Health/)
- [02-70-08_Real_Time_Performance_Monitoring](./02-70-08_Real_Time_Performance_Monitoring/)
- [02-70-10_Digital_Twin_Integration](./02-70-10_Digital_Twin_Integration/)

### External Standards
- **[CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)**: Equipment, Systems, and Installations
- **[DO-178C](https://www.rtca.org/document/do-178c-ed-3/)**: Software Considerations in Airborne Systems
- **[EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206)**: AI system transparency and monitoring requirements

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---
