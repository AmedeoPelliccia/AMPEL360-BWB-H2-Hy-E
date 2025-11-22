# 85-70-01-002: Electric Belt Loaders

## Document Information

- **Document ID**: 85-70-01-002
- **Title**: Electric Belt Loaders
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

---

## 1. Purpose

This document defines the specifications and requirements for battery-electric belt loader systems used for baggage and cargo handling operations supporting the AMPEL360 BWB-H2-Hy-E aircraft.

---

## 2. Scope

### 2.1 In Scope

- Battery-electric belt loader vehicles
- Conveyor system specifications
- Load capacity and height requirements for BWB configuration
- Battery and charging requirements
- Safety systems and operator controls
- Integration with airport baggage handling systems

### 2.2 Out of Scope

- Cargo loader vehicles (see [85-70-01-004](./85-70-01-004_Electric_Cargo_Loaders.md))
- Maintenance procedures (see [85-70-06](../85-70-06_Maintenance_and_Diagnostics/))
- Baggage screening systems (airport security domain)

---

## 3. Technical Requirements

### 3.1 Physical Specifications

- **Platform Height Range**: 1.5m - 6.5m (adjustable for BWB cargo door heights)
- **Platform Length**: 7-9 meters
- **Load Capacity**: 3,000 kg maximum
- **Conveyor Width**: 600mm minimum
- **Overall Dimensions**: Length 12m × Width 2.5m × Height 7m (extended)

### 3.2 Conveyor System

- **Belt Speed**: Variable 0-30 m/min
- **Belt Material**: Anti-static, non-marking rubber
- **Angle Adjustment**: 0-25° elevation
- **Drive Type**: Electric motor with variable frequency drive (VFD)
- **Emergency Stop**: Belt stops within 1 second
- **Load Sensors**: Continuous weight monitoring

### 3.3 Battery System

- **Battery Type**: Lithium-ion (LFP preferred for safety)
- **Energy Capacity**: 150-200 kWh
- **Operating Voltage**: 400-600 VDC nominal
- **Operating Duration**: 8-10 hours continuous operation
- **Charging Time**:
  - Full charge: 4-6 hours
  - Opportunity charging: 80% in 2 hours
- **Battery Life**: Minimum 5,000 charge cycles at 80% DoD

### 3.4 Electric Propulsion

- **Drive System**: All-wheel electric drive (4×4)
- **Motor Power**: 50-75 kW total (drivetrain)
- **Top Speed**: 25 km/h
- **Gradeability**: 15% at full load
- **Steering**: Four-wheel steering for maneuverability
- **Braking**: Regenerative + mechanical disc brakes

### 3.5 Environmental Ratings

- **Operating Temperature**: -25°C to +50°C
- **Humidity**: 0-95% non-condensing
- **Ingress Protection**: IP65 for electrical components
- **Wind Resistance**: Operational up to 50 km/h wind speed
- **Altitude**: Up to 3,000m AMSL

---

## 4. Operational Requirements

### 4.1 Performance Metrics

- **Loading Rate**: 600 bags per hour minimum
- **Positioning Accuracy**: ±50mm to aircraft door
- **Setup Time**: <2 minutes from arrival to ready
- **Availability**: >98% during operational hours
- **Reliability**: MTBF >3,000 hours

### 4.2 Safety Features

- **Platform Safety Rails**: Automatic deployment at height
- **Anti-tip System**: Stabilizers and load sensing
- **Emergency Descent**: Manual override for platform lowering
- **Proximity Sensors**: Aircraft and obstacle detection
- **Fire Suppression**: Automatic system for battery compartment
- **Grounding**: Anti-static grounding during operations
- **Lighting**: LED work lights and safety beacons

### 4.3 Operator Controls

- **Primary Controls**: Platform-mounted control panel
- **Backup Controls**: Ground-level emergency controls
- **Display**: Digital readout for height, load, battery SOC
- **Communication**: Two-way radio integration
- **Ergonomics**: Standing operator platform with anti-fatigue matting

---

## 5. Integration Requirements

### 5.1 Aircraft Interface

- **BWB Cargo Door Compatibility**: Adjustable height for multiple door positions
- **Door Sill Protection**: Soft-contact bumpers and alignment guides
- **Aircraft Grounding**: Bonding connection to aircraft structure
- **Weather Protection**: Optional rain cover for loading operations

### 5.2 Airport Infrastructure

- **Charging Stations**: Compatible with CCS or CHAdeMO standards (see [85-70-04](../85-70-04_Charging_Infrastructure/))
- **Fleet Management**: GPS tracking and telematics integration
- **Baggage System**: Interface with airport BHS (Baggage Handling System)
- **Apron Operations**: Compliance with airport ground operations rules

### 5.3 Software Integration

- **Fleet Management System**: Real-time status and dispatch
- **Maintenance Management**: Predictive maintenance alerts (see [85-70-06](../85-70-06_Maintenance_and_Diagnostics/))
- **Energy Management**: Optimization of charging schedules
- **Safety Monitoring**: Incident logging and reporting

---

## 6. Standards and Compliance

### 6.1 Aviation Standards

- [EASA Part-145](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-13212014) – Aircraft maintenance
- [IATA Ground Operations Manual (IGOM)](https://www.iata.org/en/publications/manuals/ground-operations-manual/) – Ground handling standards (**Note: Access requires IATA membership or purchase**)
- [SAE AS6171](https://www.sae.org/standards/content/as6171/) – Ground support equipment terminology

### 6.2 Safety Standards

- [ISO 13849-1](https://www.iso.org/standard/69883.html) – Safety of machinery - Safety-related parts of control systems
- [EN 1915-1](https://standards.iteh.ai/catalog/standards/cen/1a3a0f0c-0a1e-4f5e-9e6e-5c0f5e5e5e5e/en-1915-1-2013) – Aircraft ground support equipment - General requirements
- [ANSI/ITSDF B56.1](https://webstore.ansi.org/standards/itsdf/ansiitsdfb561) – Safety standard for low lift and high lift trucks

### 6.3 Electric Vehicle Standards

- [IEC 61851-1](https://webstore.iec.ch/publication/6035) – EV conductive charging system
- [ISO 15118](https://www.iso.org/standard/55366.html) – Vehicle-to-grid communication
- [UL 2580](https://www.ul.com/resources/ul-2580-standard-safety) – Batteries for electric vehicles

---

## 7. Performance Monitoring

### 7.1 Key Performance Indicators

- **Bags Handled per Charge**: Target 3,000+ bags
- **Energy Efficiency**: kWh per 1,000 bags handled
- **Battery Health**: SOH tracking and degradation monitoring
- **Uptime**: Operational hours / scheduled hours
- **Maintenance Costs**: EUR per operational hour
- **Safety Incidents**: Zero accidents target

### 7.2 Data Collection and Analytics

- **Telematics System**: Position, status, energy use
- **Load Monitoring**: Weight and distribution data
- **Operator Behavior**: Usage patterns and efficiency metrics
- **Maintenance Logs**: Automated failure prediction and scheduling
- **Environmental Impact**: Carbon footprint tracking

---

## 8. Cross-References

### 8.1 Internal (ATA 85)

- [85-70-01-A-001_Equipment_Specifications.csv](./ASSETS/85-70-01-A-001_Equipment_Specifications.csv) – Equipment specifications
- [85-70-01-A-002_Performance_Requirements.csv](./ASSETS/85-70-01-A-002_Performance_Requirements.csv) – Performance benchmarks
- [85-70-04](../85-70-04_Charging_Infrastructure/) – Charging infrastructure
- [85-70-05](../85-70-05_Motor_and_Drivetrain/) – Motor and drivetrain design
- [85-70-06](../85-70-06_Maintenance_and_Diagnostics/) – Maintenance and diagnostics

### 8.2 External (Other ATAs)

- [ATA 03 – Support Information GSE](../../../ATA_03-SUPPORT_INFORMATION_GSE/)
- [ATA 12 – Servicing](../../../../P-PROGRAM/ATA_12-SERVICING/)

---

## 9. Status and Next Steps

- **Current Phase**: Requirements definition and vendor engagement
- **Next Phase**: Prototype testing and validation
- **Dependencies**: BWB cargo door dimensions, airport BHS integration specifications

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22.

---

**End of Document**
