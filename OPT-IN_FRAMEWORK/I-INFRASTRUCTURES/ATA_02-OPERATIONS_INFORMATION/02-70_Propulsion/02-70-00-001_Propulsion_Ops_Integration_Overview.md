# 02-70-00-001 — Propulsion Operations Integration Overview

## Document Information

- **Document ID**: 02-70-00-001
- **Title**: Propulsion Operations Integration Overview
- **Subsystem**: ATA 02-70 Propulsion
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-21

## Table of Contents

1. [Introduction](#1-introduction)
2. [Integration Architecture](#2-integration-architecture)
3. [H₂ Hybrid-Electric Propulsion System](#3-h₂-hybrid-electric-propulsion-system)
4. [Data Flows](#4-data-flows)
5. [Main Interfaces](#5-main-interfaces)
6. [Stakeholders](#6-stakeholders)
7. [References](#7-references)

## 1. Introduction

### 1.1 Purpose

This document provides a high-level overview of how the AMPEL360 BWB H₂ Hybrid-Electric propulsion systems integrate with Operations Information (ATA 02), establishing the foundation for data flows, interfaces, and operational monitoring across all phases of flight operations.

### 1.2 Scope

This overview covers:
- Propulsion system components and their operational data interfaces
- Integration points with flight operations, OCC, and maintenance
- Data exchange patterns between propulsion and operational systems
- Key stakeholders and their information needs

### 1.3 Propulsion System Overview

The AMPEL360 propulsion architecture combines:
- **Cryogenic H₂ Fuel System** ([ATA 28](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_28-FUEL_SAF_CRYOGENIC_H2/)): Storage, distribution, boiloff management
- **Fuel Cell Stacks** ([ATA 73](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/P-PROPULSION/ATA_73-ENGINE_FUEL_CONTROL/)): Electrochemical power generation
- **Electric Motors** ([ATA 72](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/P-PROPULSION/ATA_72-ENGINE/)): Propulsive power units
- **Thermal Management** ([ATA 21](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E1-ENVIRONMENT/ATA_21-AIR_CONDITIONING_PRESSURIZATION/)): Cooling and heat rejection
- **Power Electronics** ([ATA 24](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E2-ENERGY/ATA_24-ELECTRICAL_POWER/)): Power conditioning and distribution
- **Control Systems** ([ATA 76](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/P-PROPULSION/ATA_76-ENGINE_CONTROLS/)): Propulsion control logic

## 2. Integration Architecture

### 2.1 Architectural Layers

```
┌─────────────────────────────────────────────────────────────┐
│          Flight Operations / Crew Interface (EFB)           │
│              (Performance, Alerts, Procedures)              │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────┴────────────────────────────────┐
│             Operations Information Layer (ATA 02)           │
│  • Flight Planning    • Performance Monitoring              │
│  • Range Calculation  • Health Management                   │
│  • Alerting & Limits  • Digital Twin Integration            │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────┴────────────────────────────────┐
│         Data Acquisition & Processing Layer                 │
│  • Onboard TSDB       • Data Concentrator                   │
│  • Telemetry Gateway  • Ground Data Links                   │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────┴────────────────────────────────┐
│              Propulsion Systems (ATA 70/72/73)              │
│  • H₂ Fuel System     • Fuel Cells      • Motors            │
│  • Thermal Mgmt       • Power Electronics                   │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Integration Principles

- **Real-Time Data Availability**: Critical propulsion parameters available with <100ms latency for crew displays
- **Historical Trending**: All performance data archived for post-flight analysis and prognostics
- **Bidirectional Communication**: Ground systems can request specific data or simulations from digital twin
- **Graceful Degradation**: System continues operation with reduced functionality if data links fail
- **Data Quality Monitoring**: Automated validation of sensor data quality and consistency

## 3. H₂ Hybrid-Electric Propulsion System

### 3.1 Fuel Cell Power Generation

**Primary Function**: Convert H₂ and O₂ into electrical power

**Key Operational Data**:
- Stack voltage and current (per cell and aggregate)
- Operating temperature profile
- H₂ and air flow rates
- Membrane hydration level
- Stack degradation indicators
- Efficiency (electrical output vs. H₂ consumption)

**Operational Interfaces**:
- Real-time power output to performance management
- Fuel consumption to range calculation
- Health indicators to predictive maintenance
- Temperature/thermal load to thermal management

### 3.2 Electric Motor Propulsion

**Primary Function**: Convert electrical power to mechanical thrust

**Key Operational Data**:
- Motor speed (RPM)
- Torque output
- Phase currents and voltages
- Winding and bearing temperatures
- Vibration signatures
- Efficiency (mechanical output vs. electrical input)

**Operational Interfaces**:
- Thrust output to performance models
- Power demand to energy management
- Health parameters to HUMS
- Temperature to thermal management

### 3.3 Cryogenic H₂ Fuel System

**Primary Function**: Store and supply hydrogen fuel

**Key Operational Data**:
- Tank quantity (mass and volume)
- Tank pressure and temperature
- Boiloff rate
- Fill level and distribution
- Valve positions and flow rates
- Thermal insulation performance

**Operational Interfaces**:
- Fuel quantity to range calculation
- Boiloff predictions to flight planning
- System health to maintenance
- Refueling data to ground operations

### 3.4 Thermal Management

**Primary Function**: Manage heat rejection from propulsion components

**Key Operational Data**:
- Coolant temperatures (inlet/outlet)
- Coolant flow rates
- Heat exchanger performance
- Pump speeds and pressures
- Ambient conditions
- Thermal load distribution

**Operational Interfaces**:
- Thermal capacity to performance limits
- Cooling effectiveness to efficiency models
- Degradation trends to maintenance

## 4. Data Flows

### 4.1 Pre-Flight Data Flow

```
Ground Planning Systems → Flight Planning Tools
  ├─ Aircraft Performance Model
  ├─ H₂ Fuel Load Planning
  ├─ Route Optimization
  ├─ Weather Impact Assessment
  └─ Reserve Calculation
         ↓
Flight Plan → Electronic Flight Bag (EFB)
  └─ Performance Tables, Limits, Procedures
```

**Data Elements**:
- Expected fuel cell efficiency by flight phase
- H₂ fuel requirements (including boiloff reserves)
- Thrust available vs. altitude/temperature
- Performance limitations and restrictions
- Alternate airport requirements

### 4.2 In-Flight Data Flow

```
Propulsion Sensors → Data Concentrator → Onboard Systems
  ├─ Performance Management Computer
  ├─ Flight Management System (FMS)
  ├─ Electronic Flight Bag (EFB)
  ├─ EICAS/ECAM Displays
  └─ Onboard Maintenance System (OMS)
         ↓
Real-Time Monitoring → Aircraft Communications Addressing and Reporting System (ACARS)
         ↓
Operations Control Center (OCC) / AOC
  ├─ Fleet Monitoring
  ├─ Performance Tracking
  └─ Maintenance Coordination
```

**Data Elements**:
- Real-time fuel cell performance
- H₂ consumption rate
- Motor thrust output
- System health status
- Performance deviations
- Alert and caution messages

### 4.3 Post-Flight Data Flow

```
Flight Data Recorder (FDR) → Ground Download
         ↓
Data Processing & Analytics Platform
  ├─ Performance Analysis
  ├─ Fuel Efficiency Review
  ├─ Component Health Trending
  ├─ Model Validation
  └─ Fleet Comparison
         ↓
Reports → Stakeholders
  ├─ Flight Operations: Performance review
  ├─ Maintenance: Health trends, prognostics
  ├─ Engineering: Model updates, certification data
  └─ Management: Fleet efficiency, optimization opportunities
```

**Data Elements**:
- Flight profile vs. planned performance
- Actual vs. predicted fuel consumption
- Component performance trends
- Anomalies and events
- Efficiency metrics

## 5. Main Interfaces

### 5.1 Interface to ATA 28 (Fuel System)

**Interface Type**: Real-time sensor data and control signals

**Data Exchange**:
- **From ATA 28**: Fuel quantity, pressure, temperature, valve states, flow rates
- **To ATA 28**: Fuel demand forecasts, refueling requirements

**Protocol**: ARINC 429 / AFDX
**Update Rate**: 1-10 Hz (depending on parameter)

See: [02-70-01_Fuel_Performance_Interfaces](./02-70-01_Fuel_Performance_Interfaces/)

### 5.2 Interface to ATA 70/72/73 (Propulsion Systems)

**Interface Type**: Telemetry and control

**Data Exchange**:
- **From ATA 70/72/73**: Performance parameters, health indicators, status
- **To ATA 70/72/73**: Power commands, mode selections

**Protocol**: AFDX / CAN
**Update Rate**: 10-100 Hz (critical parameters)

See: [02-70-02_Engine_Performance_Data](./02-70-02_Engine_Performance_Data/)

### 5.3 Interface to ATA 31 (Indicating/Recording)

**Interface Type**: Data recording and display

**Data Exchange**:
- **To ATA 31**: All propulsion parameters for FDR recording
- **From ATA 31**: Historical data retrieval for analysis

**Protocol**: ARINC 717 (FDR), AFDX (displays)
**Recording Rate**: Per certification requirements (typically 1-8 Hz)

### 5.4 Interface to ATA 45 (Onboard Maintenance System)

**Interface Type**: Health monitoring and diagnostics

**Data Exchange**:
- **To ATA 45**: Fault codes, health metrics, HUMS data
- **From ATA 45**: Diagnostic requests, maintenance status

**Protocol**: AFDX
**Update Rate**: Event-driven + 0.1 Hz periodic health

See: [02-70-04_Propulsion_System_Health](./02-70-04_Propulsion_System_Health/)

### 5.5 Interface to ATA 95 (Digital Product Passport / AI Systems)

**Interface Type**: Model training and inference

**Data Exchange**:
- **To ATA 95**: Operational data for model training, real-time inputs for inference
- **From ATA 95**: Predictions (RUL, anomalies), optimized control strategies

**Protocol**: Ethernet / Time-Series Database (TSDB)
**Update Rate**: Variable (training: batch; inference: 1-10 Hz)

See: [02-70-10_Digital_Twin_Integration](./02-70-10_Digital_Twin_Integration/)

## 6. Stakeholders

### 6.1 Flight Crew

**Information Needs**:
- Current propulsion system status and performance
- Available thrust/power
- Fuel quantity and range
- System health and alerts
- Performance limitations
- Emergency and abnormal procedure guidance

**Interface**: Electronic Flight Bag (EFB), primary flight displays, EICAS/ECAM

### 6.2 Operations Control Center (OCC)

**Information Needs**:
- Real-time fleet propulsion status
- Fuel consumption trends
- System health across fleet
- Performance deviations
- Maintenance alerts

**Interface**: Ground-based monitoring dashboards, ACARS data

### 6.3 Maintenance Planning

**Information Needs**:
- Component health trends
- Predictive maintenance recommendations
- Fault history and diagnostics
- Performance degradation indicators
- RUL (Remaining Useful Life) estimates

**Interface**: Maintenance management system, health monitoring dashboards

### 6.4 Flight Planning / Dispatch

**Information Needs**:
- Aircraft performance capabilities
- Fuel planning data
- Performance limitations
- Alternate airport viability
- Weather impact on performance

**Interface**: Flight planning tools, performance databases

### 6.5 Performance Engineering

**Information Needs**:
- Model validation data
- Performance trends vs. predictions
- Component efficiency over life
- Certification compliance data
- Design improvement feedback

**Interface**: Analytics platforms, data warehouses

## 7. References

### Internal Documents
- [02-70-00-002 Cross-ATA Propulsion Data Map](./02-70-00-002_Cross_ATA_Propulsion_Data_Map.md)
- [02-70-00-003 Propulsion Performance Monitoring](./02-70-00-003_Propulsion_Performance_Monitoring.md)
- [ATA 02-00 Operations Information Overview](../02-00_GENERAL/02-00-01_Overview/README.md)

### External Standards
- **[CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)**: Certification Specifications for Large Aeroplanes
- **[CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)**: Equipment, Systems, and Installations
- **[ARINC 429](https://www.arinc.com/cf/store/catalog_detail.cfm?item_id=77)**: Digital Information Transfer System
- **[ARINC 717](https://www.arinc.com/cf/store/catalog_detail.cfm?item_id=85)**: Flight Data Recorder
- **[DO-178C](https://www.rtca.org/document/do-178c-ed-3/)**: Software Considerations in Airborne Systems and Equipment Certification

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---
