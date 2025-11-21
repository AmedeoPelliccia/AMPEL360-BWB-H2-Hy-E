# 02-70-00-002 — Cross-ATA Propulsion Data Map

## Document Information

- **Document ID**: 02-70-00-002
- **Title**: Cross-ATA Propulsion Data Mapping
- **Subsystem**: ATA 02-70 Propulsion
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-21

## Table of Contents

1. [Introduction](#1-introduction)
2. [Data Mapping Overview](#2-data-mapping-overview)
3. [ATA Chapter Interfaces](#3-ata-chapter-interfaces)
4. [Data Governance](#4-data-governance)
5. [References](#5-references)

## 1. Introduction

### 1.1 Purpose

This document maps propulsion-related data objects across ATA chapters, indicating where each data type originates, where it is consumed, and how it is governed within the AMPEL360 Operations Information framework.

### 1.2 Scope

This mapping covers all propulsion data that flows between ATA 02 Operations Information and other ATA chapters, including:
- Physical system data from propulsion ATAs (70, 71, 72, 73, 76, 79)
- Fuel system data from ATA 28
- Energy system data from ATA 24, 49
- Recording and indication data from ATA 31
- AI/ML and digital twin data from ATA 95

## 2. Data Mapping Overview

### 2.1 Data Flow Patterns

```
┌──────────────────────────────────────────────────────────────┐
│                    Data Origin (Physical Systems)            │
├──────────────────────────────────────────────────────────────┤
│ ATA 28  │ H₂ Fuel: Quantity, Pressure, Temperature, Flow    │
│ ATA 72  │ Motors: Speed, Torque, Current, Temperature       │
│ ATA 73  │ Fuel Cells: Voltage, Current, Temp, Efficiency    │
│ ATA 24  │ Power Electronics: Efficiency, Status, Thermal    │
│ ATA 21  │ Thermal: Coolant Temp, Flow, Heat Load           │
└──────────────────────────────────────────────────────────────┘
                             │
                             ↓
┌──────────────────────────────────────────────────────────────┐
│               Data Processing & Management (ATA 02)          │
├──────────────────────────────────────────────────────────────┤
│ • Aggregation  • Validation  • Storage  • Distribution      │
│ • Analytics    • Trending    • Alerting • Archiving         │
└──────────────────────────────────────────────────────────────┘
                             │
                             ↓
┌──────────────────────────────────────────────────────────────┐
│                  Data Consumers                               │
├──────────────────────────────────────────────────────────────┤
│ ATA 31  │ FDR Recording, Cockpit Displays                   │
│ ATA 45  │ Onboard Maintenance System, Health Monitoring     │
│ ATA 95  │ AI/ML Models, Digital Twin, Predictive Analytics │
│ Flight Ops │ Performance Management, Range Calculation    │
│ Ground Ops │ Fleet Monitoring, Maintenance Planning        │
└──────────────────────────────────────────────────────────────┘
```

## 3. ATA Chapter Interfaces

### 3.1 ATA 28 — Fuel (H₂ Cryogenic)

**Data Originator**: Yes (Primary)
**Data Consumer**: Yes (for boiloff predictions)

| Data Object | Origin | Frequency | Consumer(s) | Purpose |
|-------------|--------|-----------|-------------|---------|
| H₂ Tank Quantity (kg) | ATA 28 Sensors | 1 Hz | ATA 02, 31, 45 | Range calculation, FDR, maintenance |
| Tank Pressure (bar) | ATA 28 Sensors | 1 Hz | ATA 02, 31 | Performance monitoring, recording |
| Tank Temperature (K) | ATA 28 Sensors | 1 Hz | ATA 02, 31, 95 | Boiloff prediction, digital twin |
| Boiloff Rate (kg/h) | ATA 02 Calculation | 0.1 Hz | Flight Planning | Fuel reserve planning |
| Fill Level (%) | ATA 28 Sensors | 1 Hz | ATA 02, 31 | Operations monitoring |
| Valve Positions | ATA 28 Control | Event | ATA 31, 45 | Diagnostics, maintenance |

**Governance**: 
- Master data managed by ATA 28 control system
- ATA 02 responsible for derived calculations (boiloff, range)
- Refer to [02-70-01_Fuel_Performance_Interfaces](./02-70-01_Fuel_Performance_Interfaces/)

### 3.2 ATA 70 — Standard Practices Engine

**Data Originator**: No (conceptual framework)
**Data Consumer**: Yes (maintenance procedures)

| Data Object | Origin | Frequency | Consumer(s) | Purpose |
|-------------|--------|-----------|-------------|---------|
| Maintenance Procedures | ATA 70 Documentation | Static | ATA 02, 45 | Ops procedures reference |
| Performance Standards | ATA 70 Certification | Static | ATA 02 | Performance validation |

**Governance**: 
- ATA 70 defines standards and procedures
- ATA 02 implements operational data flows compliant with ATA 70
- No real-time data interface

### 3.3 ATA 72 — Engine (Electric Motors)

**Data Originator**: Yes (Primary)
**Data Consumer**: No

| Data Object | Origin | Frequency | Consumer(s) | Purpose |
|-------------|--------|-----------|-------------|---------|
| Motor Speed (RPM) | ATA 72 Sensors | 100 Hz | ATA 02, 31, 95 | Performance, recording, twin |
| Motor Torque (Nm) | ATA 72 Calculation | 100 Hz | ATA 02, 31 | Thrust calculation, recording |
| Phase Currents (A) | ATA 72 Sensors | 100 Hz | ATA 02, 45, 95 | Efficiency, health, analytics |
| Winding Temperature (°C) | ATA 72 Sensors | 1 Hz | ATA 02, 21, 45 | Thermal mgmt, health |
| Bearing Temperature (°C) | ATA 72 Sensors | 1 Hz | ATA 45, 95 | Predictive maintenance |
| Vibration Proxy | ATA 72 Processing | 1 Hz | ATA 45, 95 | Condition monitoring |

**Governance**: 
- Raw sensor data owned by ATA 72 control system
- ATA 02 performs performance aggregation and derived metrics
- Refer to [02-70-02_Engine_Performance_Data](./02-70-02_Engine_Performance_Data/)

### 3.4 ATA 73 — Engine Fuel Control (Fuel Cells)

**Data Originator**: Yes (Primary)
**Data Consumer**: Yes (for control optimization)

| Data Object | Origin | Frequency | Consumer(s) | Purpose |
|-------------|--------|-----------|-------------|---------|
| Stack Voltage (V) | ATA 73 Sensors | 10 Hz | ATA 02, 31, 45, 95 | Performance, recording, health, twin |
| Stack Current (A) | ATA 73 Sensors | 10 Hz | ATA 02, 31, 95 | Efficiency, recording, twin |
| Cell Temperatures (°C) | ATA 73 Sensors | 1 Hz | ATA 02, 21, 45 | Thermal management, health |
| H₂ Flow Rate (kg/h) | ATA 73 Sensors | 1 Hz | ATA 02, 28, 31 | Consumption, range, recording |
| Air Flow Rate (kg/h) | ATA 73 Sensors | 1 Hz | ATA 02, 31 | Stoichiometry monitoring |
| Membrane Hydration | ATA 73 Estimation | 0.1 Hz | ATA 45, 95 | Health monitoring, predictive |
| Efficiency (%) | ATA 02 Calculation | 0.1 Hz | Flight Ops, 95 | Performance, optimization |
| Degradation Index | ATA 95 ML Model | 0.01 Hz | ATA 02, 45 | Maintenance planning |

**Governance**: 
- ATA 73 owns raw sensor data and control
- ATA 02 calculates derived performance metrics
- ATA 95 generates prognostic indicators
- Refer to [02-70-02_Engine_Performance_Data](./02-70-02_Engine_Performance_Data/)

### 3.5 ATA 24 — Electrical Power

**Data Originator**: Yes (Power electronics)
**Data Consumer**: Yes (for load management)

| Data Object | Origin | Frequency | Consumer(s) | Purpose |
|-------------|--------|-----------|-------------|---------|
| Inverter Efficiency (%) | ATA 24 Calculation | 1 Hz | ATA 02, 95 | Performance, optimization |
| Power Electronics Temp (°C) | ATA 24 Sensors | 1 Hz | ATA 02, 21, 45 | Thermal mgmt, health |
| DC Bus Voltage (V) | ATA 24 Sensors | 100 Hz | ATA 02, 31 | Performance, recording |
| Power Distribution | ATA 24 Metering | 1 Hz | ATA 02, 95 | Energy management |

**Governance**: 
- ATA 24 manages power distribution and conversion
- ATA 02 aggregates for propulsion system efficiency
- Bidirectional: ATA 02 may request load shedding

### 3.6 ATA 31 — Indicating/Recording

**Data Originator**: No
**Data Consumer**: Yes (Primary)

| Data Object | Origin | Frequency | Consumer(s) | Purpose |
|-------------|--------|-----------|-------------|---------|
| All Propulsion Parameters | Multiple ATA | Per FDR req | ATA 31 FDR | Certification recording |
| Cockpit Display Data | ATA 02 Processing | 1-10 Hz | ATA 31 Displays | Crew information |

**Governance**: 
- ATA 31 is pure consumer of propulsion data
- ATA 02 formats data per [ARINC 717](https://www.arinc.com/cf/store/catalog_detail.cfm?item_id=85) for FDR
- Display refresh rate per human factors requirements

### 3.7 ATA 45 — Onboard Maintenance System

**Data Originator**: No
**Data Consumer**: Yes (Primary)

| Data Object | Origin | Frequency | Consumer(s) | Purpose |
|-------------|--------|-----------|-------------|---------|
| Propulsion Health Metrics | Multiple ATA | 0.1-1 Hz | ATA 45 | HUMS, prognostics |
| Fault Codes | Multiple ATA | Event | ATA 45 | Diagnostics |
| Maintenance Predictions | ATA 95 | 0.01 Hz | ATA 45 | Planning |

**Governance**: 
- ATA 45 aggregates health data from all propulsion subsystems
- ATA 02 provides health KPIs and trends
- Refer to [02-70-04_Propulsion_System_Health](./02-70-04_Propulsion_System_Health/)

### 3.8 ATA 49 — Airborne Auxiliary Power

**Data Originator**: Yes (if APU provides propulsion assist)
**Data Consumer**: Yes (for total system energy)

| Data Object | Origin | Frequency | Consumer(s) | Purpose |
|-------------|--------|-----------|-------------|---------|
| APU Power Output (kW) | ATA 49 | 1 Hz | ATA 02, 24 | Energy management |
| APU Fuel Consumption | ATA 49 | 0.1 Hz | ATA 02 | Total fuel accounting |

**Governance**: 
- ATA 49 manages APU operation
- ATA 02 aggregates for total propulsion energy accounting

### 3.9 ATA 95 — Digital Product Passport / Neural Networks

**Data Originator**: Yes (Predictions, optimizations)
**Data Consumer**: Yes (Training data)

| Data Object | Origin | Frequency | Consumer(s) | Purpose |
|-------------|--------|-----------|-------------|---------|
| Historical Operations Data | ATA 02 Archive | Batch | ATA 95 | Model training |
| Real-Time Inputs | Multiple ATA | 1-10 Hz | ATA 95 | Inference |
| RUL Predictions | ATA 95 ML Models | 0.01 Hz | ATA 02, 45 | Maintenance planning |
| Anomaly Scores | ATA 95 ML Models | 1 Hz | ATA 02, 45 | Health monitoring |
| Optimized Strategies | ATA 95 Optimization | 0.1 Hz | ATA 02 | Performance improvement |
| Digital Twin State | ATA 95 Simulation | 1 Hz | ATA 02, Engineering | What-if analysis |

**Governance**: 
- Bidirectional data flow
- ATA 02 provides operational data to ATA 95 for training and inference
- ATA 95 provides predictions and optimizations back to ATA 02
- Data quality and provenance critical for [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206) compliance
- Refer to [02-70-10_Digital_Twin_Integration](./02-70-10_Digital_Twin_Integration/)

## 4. Data Governance

### 4.1 Data Ownership

| ATA Chapter | Ownership Scope | Responsibility |
|-------------|----------------|----------------|
| ATA 28 | H₂ fuel quantity, state | Sensor accuracy, safety |
| ATA 72 | Motor parameters | Control, health |
| ATA 73 | Fuel cell parameters | Control, efficiency |
| ATA 24 | Power electronics | Conversion, distribution |
| ATA 02 | Derived metrics, aggregations | Performance calculation, monitoring |
| ATA 95 | Predictions, optimizations | Model accuracy, explainability |

### 4.2 Data Quality Requirements

| Data Type | Accuracy | Latency | Availability | Integrity |
|-----------|----------|---------|--------------|-----------|
| Safety-critical (thrust, fuel) | ±1% | <100ms | 99.999% | Checksums, redundancy |
| Performance (efficiency) | ±2% | <1s | 99.9% | Validation |
| Health monitoring | ±5% | <10s | 99% | Trend analysis |
| Post-flight analytics | ±1% | N/A | 100% archive | Audit trail |

### 4.3 Data Retention

- **Real-time operational**: 24 hours onboard, continuous to ground
- **Health trending**: 1 year onboard, 10 years ground
- **Performance analytics**: Full flight lifetime ground
- **Certification data**: Per regulatory requirements (typically lifetime + 5 years)

### 4.4 Data Security

- **Onboard**: Encrypted AFDX, access control per [DO-326A](https://www.rtca.org/document/do-326a-ed-1/)
- **Air-ground link**: Encrypted ACARS or satellite link
- **Ground storage**: Encrypted at rest, role-based access control
- **Audit**: All data access logged per [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) and aviation regulations

## 5. References

### Internal Documents
- [02-70-00-001 Propulsion Ops Integration Overview](./02-70-00-001_Propulsion_Ops_Integration_Overview.md)
- [02-70-01_Fuel_Performance_Interfaces](./02-70-01_Fuel_Performance_Interfaces/)
- [02-70-02_Engine_Performance_Data](./02-70-02_Engine_Performance_Data/)
- [02-70-04_Propulsion_System_Health](./02-70-04_Propulsion_System_Health/)
- [02-70-10_Digital_Twin_Integration](./02-70-10_Digital_Twin_Integration/)

### External Standards
- **[CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)**: Equipment, Systems, and Installations
- **[ARINC 717](https://www.arinc.com/cf/store/catalog_detail.cfm?item_id=85)**: Flight Data Recorder
- **[DO-326A](https://www.rtca.org/document/do-326a-ed-1/)**: Airworthiness Security Process Specification
- **[EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206)**: Regulation on Artificial Intelligence
- **[GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)**: General Data Protection Regulation

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---
