# 95-30-00-006 Circularity KPI Definitions

**Document ID:** 95-30-00-006  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** ACTIVE

## 1. Introduction

This document defines all Key Performance Indicators (KPIs) used to measure, monitor, and optimize circularity performance across the AMPEL360 BWB H₂ Hy-E aircraft.

## 2. KPI Framework

### 2.1 KPI Categories

| Category | Code | Focus Area |
|----------|------|------------|
| Energy Recovery | **EFF-E** | Energy capture and reuse efficiency |
| Material Recovery | **EFF-M** | Material and fluid recovery rates |
| System Performance | **PRF** | Operational performance metrics |
| Lifecycle Management | **LFC** | Component and system lifecycle |
| Environmental Impact | **ENV** | Carbon and environmental metrics |
| Economic Value | **ECN** | Cost savings and value creation |

### 2.2 Measurement Frequency

- **Real-time**: Continuous monitoring during flight operations
- **Per-flight**: Aggregated per flight cycle
- **Per-maintenance**: Measured during maintenance activities
- **Annual**: Yearly aggregation and trending

## 3. Energy Recovery KPIs

### KPI-001: Overall Energy Recovery Rate
- **ID**: 95-30-00-006-KPI-001
- **Formula**: (Recovered Energy / Total Waste Energy) × 100%
- **Unit**: Percentage (%)
- **Target**: ≥85%
- **Measurement**: Real-time + Per-flight aggregation
- **Source**: Energy management system sensors across all ATA chapters
- **Owner**: Energy Circularity Lead

### KPI-002: Thermal Recovery Efficiency (Fuel Cells to ECS)
- **ID**: 95-30-00-006-KPI-002
- **Formula**: (Thermal Energy Delivered to ECS / FC Waste Heat Available) × 100%
- **Unit**: Percentage (%)
- **Target**: ≥75%
- **Measurement**: Real-time
- **Source**: ATA-21 ECS sensors, ATA-70 fuel cell thermal sensors
- **Owner**: ECS Lead

### KPI-003: Electrical Regeneration Efficiency
- **ID**: 95-30-00-006-KPI-003
- **Formula**: (Regenerated Electrical Energy / Total Braking Energy) × 100%
- **Unit**: Percentage (%)
- **Target**: ≥85%
- **Measurement**: Real-time
- **Source**: ATA-24 electrical power system, ATA-32 braking system
- **Owner**: Electrical Lead

### KPI-004: Hydraulic Energy Recovery Rate
- **ID**: 95-30-00-006-KPI-004
- **Formula**: (Accumulator Recovered Energy / Total Hydraulic Work) × 100%
- **Unit**: Percentage (%)
- **Target**: ≥80%
- **Measurement**: Real-time
- **Source**: ATA-29 hydraulic system sensors
- **Owner**: Hydraulic Lead

## 4. Material Recovery KPIs

### KPI-005: H₂ Boil-off Recovery Rate
- **ID**: 95-30-00-006-KPI-005
- **Formula**: (Recompressed H₂ / Total Boil-off) × 100%
- **Unit**: Percentage (%)
- **Target**: ≥92%
- **Measurement**: Real-time + Per-flight
- **Source**: ATA-28 fuel system sensors
- **Owner**: Fuel Systems Lead

### KPI-006: Hydraulic Fluid Loss Rate
- **ID**: 95-30-00-006-KPI-006
- **Formula**: (Fluid Lost / Total Fluid Volume) × 100%
- **Unit**: Percentage (%)
- **Target**: <1%
- **Measurement**: Per-flight + Per-maintenance
- **Source**: ATA-29 fluid level and condition monitoring
- **Owner**: Hydraulic Lead

### KPI-007: Water Recovery Rate
- **ID**: 95-30-00-006-KPI-007
- **Formula**: (Recovered Water / Total Water Input) × 100%
- **Unit**: Percentage (%)
- **Target**: ≥88%
- **Measurement**: Per-flight
- **Source**: ATA-38 water management system
- **Owner**: Water Systems Lead

### KPI-008: Air Recirculation Efficiency
- **ID**: 95-30-00-006-KPI-008
- **Formula**: (Recirculated Air / Total Cabin Air) × 100%
- **Unit**: Percentage (%)
- **Target**: ≥90%
- **Measurement**: Real-time
- **Source**: ATA-21 environmental control system
- **Owner**: ECS Lead

## 5. System Performance KPIs

### KPI-009: APU Load Optimization Factor
- **ID**: 95-30-00-006-KPI-009
- **Formula**: (Actual APU Load / Optimal APU Load) × 100%
- **Unit**: Percentage (%)
- **Target**: 90-100%
- **Measurement**: Real-time
- **Source**: ATA-49 APU monitoring, ATA-24 load management
- **Owner**: APU Lead

### KPI-010: Electrical Load Balance Factor
- **ID**: 95-30-00-006-KPI-010
- **Formula**: σ(Load Distribution) / Mean Load
- **Unit**: Dimensionless (lower is better)
- **Target**: <0.15
- **Measurement**: Real-time
- **Source**: ATA-24 electrical distribution system
- **Owner**: Electrical Lead

### KPI-011: Pneumatic Pressure Regulation Efficiency
- **ID**: 95-30-00-006-KPI-011
- **Formula**: (Useful Pneumatic Work / Input Energy) × 100%
- **Unit**: Percentage (%)
- **Target**: ≥85%
- **Measurement**: Real-time
- **Source**: ATA-36 pneumatic system
- **Owner**: Pneumatic Lead

### KPI-012: Filter Lifecycle Utilization
- **ID**: 95-30-00-006-KPI-012
- **Formula**: (Actual Filter Life / Design Filter Life) × 100%
- **Unit**: Percentage (%)
- **Target**: ≥95%
- **Measurement**: Per-maintenance
- **Source**: ATA-21 filter condition monitoring
- **Owner**: ECS Lead

## 6. Lifecycle Management KPIs

### KPI-013: Component Second-Life Rate
- **ID**: 95-30-00-006-KPI-013
- **Formula**: (Components in Second Life / Total Retired Components) × 100%
- **Unit**: Percentage (%)
- **Target**: ≥60%
- **Measurement**: Annual
- **Source**: ATA-95 Digital Product Passport system
- **Owner**: Material Circularity Lead

### KPI-014: Battery Cycle Efficiency
- **ID**: 95-30-00-006-KPI-014
- **Formula**: (Actual Cycles at 80% SOH / Design Cycles) × 100%
- **Unit**: Percentage (%)
- **Target**: ≥100%
- **Measurement**: Continuous + Annual
- **Source**: ATA-80 battery management system
- **Owner**: Energy Storage Lead

### KPI-015: Material Circularity Index (MCI)
- **ID**: 95-30-00-006-KPI-015
- **Formula**: MCI = 0.9 × LFI + 0.1 × FU (per ISO standard)
- **Unit**: Dimensionless (0-1, higher is better)
- **Target**: ≥0.7
- **Measurement**: Annual (design phase assessment)
- **Source**: Material composition database, lifecycle analysis
- **Owner**: Material Circularity Lead

### KPI-016: Component Refurbishment Success Rate
- **ID**: 95-30-00-006-KPI-016
- **Formula**: (Successfully Refurbished / Total Refurb Attempts) × 100%
- **Unit**: Percentage (%)
- **Target**: ≥85%
- **Measurement**: Per-refurbishment
- **Source**: Maintenance records, ATA-95 DPP
- **Owner**: Material Circularity Lead

## 7. Environmental Impact KPIs

### KPI-017: Net CO₂ per Flight
- **ID**: 95-30-00-006-KPI-017
- **Formula**: CO₂ Captured - CO₂ Emitted
- **Unit**: Kilograms (kg)
- **Target**: ≤-5 kg (negative = carbon removal)
- **Measurement**: Per-flight
- **Source**: ATA-80 CO₂ battery system
- **Owner**: Sustainability Lead

### KPI-018: Total Energy Efficiency
- **ID**: 95-30-00-006-KPI-018
- **Formula**: (Useful Work Output / Total Energy Input) × 100%
- **Unit**: Percentage (%)
- **Target**: ≥65%
- **Measurement**: Per-flight
- **Source**: All energy systems (ATA-24, 28, 49, 70, 80)
- **Owner**: Energy Circularity Lead

### KPI-019: Water Footprint per Flight
- **ID**: 95-30-00-006-KPI-019
- **Formula**: Fresh Water Consumed - Water Recovered
- **Unit**: Liters (L)
- **Target**: <10 L
- **Measurement**: Per-flight
- **Source**: ATA-38 water management system
- **Owner**: Water Systems Lead

### KPI-020: Waste Diversion Rate
- **ID**: 95-30-00-006-KPI-020
- **Formula**: (Recycled/Reused Waste / Total Waste) × 100%
- **Unit**: Percentage (%)
- **Target**: ≥90%
- **Measurement**: Per-maintenance + Annual
- **Source**: Maintenance waste tracking, ATA-38 waste management
- **Owner**: Operations Lead

## 8. Economic Value KPIs

### KPI-021: Energy Recovery Value
- **ID**: 95-30-00-006-KPI-021
- **Formula**: Recovered Energy × Energy Cost
- **Unit**: Euros (€) per flight
- **Target**: ≥€150 per flight
- **Measurement**: Per-flight
- **Source**: Energy management system + economic model
- **Owner**: Program Economics Team

### KPI-022: Component Reuse Value
- **ID**: 95-30-00-006-KPI-022
- **Formula**: (Refurbishment Cost - New Component Cost) × Components Reused
- **Unit**: Euros (€) per year
- **Target**: ≥€500,000 per aircraft per year
- **Measurement**: Annual
- **Source**: Maintenance cost tracking, procurement database
- **Owner**: Material Circularity Lead

### KPI-023: Circular Economy ROI
- **ID**: 95-30-00-006-KPI-023
- **Formula**: (Annual Circular Benefits - Circular Implementation Costs) / Implementation Costs
- **Unit**: Percentage (%)
- **Target**: ≥20%
- **Measurement**: Annual
- **Source**: Financial systems, operational data
- **Owner**: Program Economics Team

## 9. Composite KPIs

### KPI-024: Overall Circularity Score (OCS)
- **ID**: 95-30-00-006-KPI-024
- **Formula**: Weighted average of:
  - Energy Recovery (30%)
  - Material Recovery (25%)
  - Lifecycle Performance (20%)
  - Environmental Impact (15%)
  - Economic Value (10%)
- **Unit**: Score (0-100, higher is better)
- **Target**: ≥80
- **Measurement**: Per-flight + Annual trending
- **Source**: All KPI systems
- **Owner**: Circularity Program Manager

### KPI-025: Digital Traceability Coverage
- **ID**: 95-30-00-006-KPI-025
- **Formula**: (Monitored Circular Loops / Total Circular Loops) × 100%
- **Unit**: Percentage (%)
- **Target**: 100%
- **Measurement**: Real-time system check + Monthly audit
- **Source**: ATA-95 DPP system, CAOS monitoring
- **Owner**: DPP Lead

## 10. KPI Monitoring and Reporting

### 10.1 Real-Time Dashboard
All real-time KPIs displayed on CAOS circularity dashboard:
- Color-coded status (green/amber/red)
- Trend analysis (7-day, 30-day, annual)
- Anomaly detection and alerting

### 10.2 Reporting Schedule

| Report Type | Frequency | Audience | Content |
|-------------|-----------|----------|---------|
| Operations Report | Daily | Flight crew, maintenance | Key operational KPIs |
| Performance Report | Weekly | Engineering teams | Detailed system KPIs |
| Management Report | Monthly | Program management | Summary KPIs, trends |
| Sustainability Report | Quarterly | Stakeholders | Environmental and lifecycle KPIs |
| Annual Review | Yearly | Board, regulators | Complete KPI analysis, targets |

### 10.3 KPI Review Process
- **Quarterly**: Review KPI performance vs. targets
- **Semi-Annual**: Adjust targets based on operational data
- **Annual**: Comprehensive KPI framework review and update

## 11. Data Quality and Validation

### 11.1 Data Sources
All KPIs derived from:
- Certified aircraft sensors and systems
- Calibrated ground support equipment
- Validated maintenance records
- Audited financial systems

### 11.2 Validation Methods
- Automated data quality checks
- Cross-system validation
- Manual audit sampling (5% of records)
- Independent verification for regulatory reporting

## 12. References

### Internal Documents
- [95-30-00-001: Circularity Overview](../95-30-00-001_Circularity_Overview.md)
- [95-30-00-002: Circularity Strategy and Objectives](../95-30-00-002_Circularity_Strategy_and_Objectives.md)
- [95-30-00-004: Circularity Taxonomy](./95-30-00-004_Circularity_Taxonomy.md)
- [95-30-00-005: Circularity Traceability Matrix](./95-30-00-005_Circularity_Traceability_Matrix.csv)

### External Standards
- [ISO 14040:2006](https://www.iso.org/standard/37456.html): Life Cycle Assessment - Principles and framework
- [ISO 14044:2006](https://www.iso.org/standard/38498.html): Life Cycle Assessment - Requirements and guidelines
- [ISO 59004:2024](https://www.iso.org/standard/80647.html): Circular Economy - Terminology, principles and guidance for implementation

## 13. Document Control

| Item | Details |
|------|---------|
| **Owner** | Circularity Program Manager |
| **Approved By** | Chief Engineer - Systems Integration |
| **Next Review** | 2026-02-17 (Quarterly) |
| **Classification** | Internal |

---

*This document is part of the AMPEL360 OPT-IN Framework and follows the structure defined in [OPT-IN_FRAMEWORK_STANDARD.md](../../../../OPT-IN_FRAMEWORK_STANDARD.md)*
