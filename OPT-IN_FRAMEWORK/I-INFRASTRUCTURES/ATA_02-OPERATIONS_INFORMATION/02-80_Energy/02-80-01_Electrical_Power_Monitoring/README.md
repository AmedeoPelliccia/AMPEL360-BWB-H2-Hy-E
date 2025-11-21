# 02-80-01: Electrical Power Monitoring

## Purpose

This section covers monitoring of the electrical power system in operation, including generation, distribution, power quality, and load management for the AMPEL360 BWB-H2-Hy-E aircraft.

## Scope

Electrical power monitoring encompasses:

- **Power Distribution Monitoring**: Real-time bus voltages, currents, and loads
- **Generator Performance**: Output tracking for engine-driven, APU, fuel cell, and GPU sources
- **Battery Status Integration**: SOC, SOH, and operational limits
- **Power Quality**: Voltage regulation, frequency stability, harmonics
- **Load Management Interface**: Data exchange between monitoring and control functions

## Content

### Documentation

- [02-80-01-001_Power_Distribution_Monitoring.md](./02-80-01-001_Power_Distribution_Monitoring.md) – Real-time power distribution tracking
- [02-80-01-002_Generator_Performance_Data.md](./02-80-01-002_Generator_Performance_Data.md) – Generator telemetry and health
- [02-80-01-003_Battery_Status_Integration.md](./02-80-01-003_Battery_Status_Integration.md) – Battery monitoring integration
- [02-80-01-004_Power_Quality_Monitoring.md](./02-80-01-004_Power_Quality_Monitoring.md) – Voltage, frequency, THD metrics
- [02-80-01-005_Load_Management_Interface.md](./02-80-01-005_Load_Management_Interface.md) – Monitoring-to-control interface

### Assets

#### Data Models (`ASSETS/Data_Models/`)

- `02-80-01-A-001_Power_System_Schema.json` – JSON schema for power system data
- `02-80-01-A-002_Generator_Data_Model.json` – Generator telemetry schema
- `02-80-01-A-003_Battery_Telemetry_Schema.json` – Battery monitoring data schema

#### Dashboards (`ASSETS/Dashboards/`)

- `02-80-01-A-101_Electrical_System_Dashboard.json` – Overall system status visualization
- `02-80-01-A-102_Power_Quality_Dashboard.json` – Power quality metrics display
- `02-80-01-A-103_Load_Distribution_View.json` – Load distribution across buses

#### Integration (`ASSETS/Integration/`)

- `02-80-01-A-201_ATA_24_Interface_Spec.yaml` – Interface to [ATA 24 Electrical Power](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes)
- `02-80-01-A-202_Data_Flow_Diagram.svg` – Data flow from sensors to dashboards

## Main Data Sources

Electrical power monitoring integrates data from:

- **Power Distribution Units (PDU)**: Bus voltages, currents, breaker status
- **Generator ECUs**: Output power, efficiency, temperature, faults
- **Battery Management Systems (BMS)**: SOC, SOH, cell voltages, temperatures
- **Fuel Cell Controllers**: Stack output, efficiency (see [ATA 28](#))
- **Ground Power Interface**: GPU connection status, power supplied

## Primary Consumers

Monitored data supports:

- **Flight Crew**: Real-time electrical system synoptic on MFD/ECAM
- **OCC**: Fleet-wide power system monitoring and alerting
- **Maintenance**: Fault diagnostics and trend analysis
- **Energy Optimization**: AI/ML inputs for load prediction and allocation ([02-80-05](../02-80-05_Energy_Optimization/))

## Related Sections

- [02-80-00-002_Cross_ATA_Energy_Data_Map.md](../02-80-00-002_Cross_ATA_Energy_Data_Map.md) – Data governance and lineage
- [02-80-02_Energy_Budget_Management](../02-80-02_Energy_Budget_Management/) – Budget tracking using monitored data
- [02-80-07_Real_Time_Energy_Monitoring](../02-80-07_Real_Time_Energy_Monitoring/) – Real-time analytics and anomaly detection
- [ATA 24 – Electrical Power](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes) – Source systems

## Compliance

Monitoring functions support:

- [CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes) – System integrity and safety
- [DO-178C](https://www.rtca.org/) – Software assurance for monitoring software
- [DO-254](https://www.rtca.org/) – Hardware assurance for PDU and sensor interfaces

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-11-21*.

---
