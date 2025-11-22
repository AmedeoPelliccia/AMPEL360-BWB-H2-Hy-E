# 85-70-01-001: Battery Electric Tugs

## Document Information

- **Document ID**: 85-70-01-001
- **Title**: Battery Electric Tugs
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

---

## 1. Purpose

This document defines the specifications, requirements, and operational guidelines for battery-electric tugs used in ground handling operations for the AMPEL360 BWB-H2-Hy-E aircraft.

---

## 2. Scope

### 2.1 In Scope

- Battery-electric pushback tractors
- Electric towbarless aircraft tugs
- Towing capacity requirements for BWB configuration
- Battery system specifications for tug operations
- Charging requirements and operational constraints
- Performance criteria for airport operations

### 2.2 Out of Scope

- Diesel or hybrid tug systems (see [85-70-03](../85-70-03_Hybrid_Propulsion_Systems/))
- Maintenance procedures (see [85-70-06](../85-70-06_Maintenance_and_Diagnostics/))
- Charging infrastructure design (see [85-70-04](../85-70-04_Charging_Infrastructure/))

---

## 3. Technical Requirements

### 3.1 Towing Capacity

- **Maximum Towing Weight**: 650 metric tons (BWB-H2-Hy-E MTOW)
- **Pushback Force**: Minimum 150 kN
- **Operating Speed**: 0-25 km/h
- **Slope Capability**: Up to 3% gradient fully loaded

### 3.2 Battery System

- **Battery Type**: Lithium-ion (LFP or NMC chemistry)
- **Energy Capacity**: Minimum 400 kWh for towbarless tugs
- **Operating Voltage**: 600-800 VDC nominal
- **Charging Time**: 
  - Fast charging: 80% in 60 minutes
  - Opportunity charging: Compatible with 15-minute charge cycles
- **Battery Life**: Minimum 3,000 charge cycles at 80% DoD

### 3.3 Electric Drivetrain

- **Motor Type**: Permanent magnet synchronous motor (PMSM)
- **Motor Power**: 200-300 kW continuous, 400-500 kW peak
- **Torque Output**: 15,000-20,000 Nm at wheels
- **Efficiency**: >90% at rated load
- **Regenerative Braking**: Minimum 60% energy recovery

### 3.4 Environmental Requirements

- **Operating Temperature**: -30°C to +50°C
- **Humidity**: 0-95% non-condensing
- **Ingress Protection**: IP54 minimum for electrical components
- **Altitude**: Operation up to 2,500m AMSL

---

## 4. Operational Requirements

### 4.1 Performance Metrics

- **Daily Operations**: Minimum 10 pushbacks per charge
- **Availability**: >95% during operational hours
- **Reliability**: MTBF >2,000 hours
- **Maintainability**: MTTR <4 hours for critical failures

### 4.2 Safety Features

- **Emergency Stop**: Dual-circuit emergency stop system
- **Dead Man Switch**: Operator presence detection
- **Anti-collision**: 360° proximity sensors
- **Towing Pin Monitor**: Automatic connection verification
- **Battery Management**: Thermal runaway prevention and detection

### 4.3 Operator Interface

- **Control System**: Wireless remote control with line-of-sight requirement
- **Display**: Real-time SOC, range, and operational status
- **Alerts**: Visual and audible warnings for safety conditions
- **Ergonomics**: Compliance with [ISO 11228-1](https://www.iso.org/standard/76820.html) (Manual handling)

---

## 5. Integration Requirements

### 5.1 Aircraft Interface

- **Towbar Compatibility**: NATO standard and custom BWB nose gear
- **Towbarless Interface**: Automated lifting and securing system
- **Ground Connection**: Anti-static grounding during operations
- **Communication**: Integration with aircraft systems via [ATA 85-40](../../85-40_Software/)

### 5.2 Airport Infrastructure

- **Charging Points**: Compatible with airport charging infrastructure (see [85-70-04](../85-70-04_Charging_Infrastructure/))
- **Fleet Management**: Integration with airport GSE management systems
- **Weather Protection**: Outdoor storage capability with IP-rated enclosures
- **Maintenance Facilities**: Access to airport GSE maintenance hangars

---

## 6. Standards and Compliance

### 6.1 Aviation Standards

- [EASA CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes) – Equipment, systems, and installations
- [FAA AC 150/5210-5D](https://www.faa.gov/airports/resources/advisory_circulars) – Aircraft rescue and firefighting

### 6.2 Electric Vehicle Standards

- [ISO 8855](https://www.iso.org/standard/51180.html) – Road vehicles – Vehicle dynamics and road-holding ability
- [SAE J1772](https://www.sae.org/standards/content/j1772_201710/) – Electric vehicle conductive charge coupler
- [IEC 61851](https://webstore.iec.ch/publication/6035) – Electric vehicle conductive charging system

### 6.3 Battery Safety Standards

- [UN 38.3](https://unece.org/transportdangerous-goods/un-manual-tests-and-criteria-rev6-2015) – Lithium battery testing
- [UL 2580](https://www.ul.com/resources/ul-2580-standard-safety) – Batteries for use in electric vehicles
- [IEC 62619](https://webstore.iec.ch/publication/7299) – Secondary batteries for industrial applications

---

## 7. Performance Monitoring

### 7.1 Key Performance Indicators

- **Energy Efficiency**: kWh per tow operation
- **Battery Health**: State of Health (SOH) tracking
- **Operational Uptime**: Hours available vs. hours scheduled
- **Maintenance Costs**: Cost per operational hour
- **Carbon Footprint**: CO₂ equivalent emissions (lifecycle)

### 7.2 Data Collection

- **Telematics**: Real-time position, status, and diagnostics
- **Energy Logging**: Charge/discharge cycles and consumption
- **Maintenance Records**: Integrated with CMMS systems
- **Incident Reporting**: Automated safety event logging

---

## 8. Cross-References

### 8.1 Internal (ATA 85)

- [85-70-01-A-001_Equipment_Specifications.csv](./ASSETS/85-70-01-A-001_Equipment_Specifications.csv) – Detailed equipment specs
- [85-70-01-A-002_Performance_Requirements.csv](./ASSETS/85-70-01-A-002_Performance_Requirements.csv) – Performance data
- [85-70-01-A-003_Battery_Systems.md](./ASSETS/85-70-01-A-003_Battery_Systems.md) – Battery design details
- [85-70-04](../85-70-04_Charging_Infrastructure/) – Charging infrastructure
- [85-70-06](../85-70-06_Maintenance_and_Diagnostics/) – Maintenance procedures

### 8.2 External (Other ATAs)

- [ATA 03 – Support Information GSE](../../../ATA_03-SUPPORT_INFORMATION_GSE/)
- [ATA 09 – Towing and Taxiing](../../../../P-PROGRAM/ATA_09-TOWING_AND_TAXIING/)

---

## 9. Status and Next Steps

- **Current Phase**: Requirements definition
- **Next Phase**: Vendor selection and procurement specifications
- **Dependencies**: BWB nose gear interface design, airport charging infrastructure deployment

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22.

---

**End of Document**
