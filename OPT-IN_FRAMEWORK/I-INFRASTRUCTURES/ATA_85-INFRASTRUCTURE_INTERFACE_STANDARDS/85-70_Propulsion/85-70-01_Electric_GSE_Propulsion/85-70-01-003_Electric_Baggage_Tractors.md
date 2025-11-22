# 85-70-01-003: Electric Baggage Tractors

## Document Information

- **Document ID**: 85-70-01-003
- **Title**: Electric Baggage Tractors
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

---

## 1. Purpose

This document defines specifications and requirements for battery-electric baggage tractors used to transport baggage carts between aircraft and terminal facilities for AMPEL360 BWB-H2-Hy-E operations.

---

## 2. Scope

### 2.1 In Scope

- Battery-electric baggage tractor specifications
- Cart towing capacity and configurations
- Battery system and charging requirements
- Operational performance criteria
- Safety systems and operator controls
- Integration with airport baggage handling operations

### 2.2 Out of Scope

- Belt loader systems (see [85-70-01-002](./85-70-01-002_Electric_Belt_Loaders.md))
- Aircraft tugs (see [85-70-01-001](./85-70-01-001_Battery_Electric_Tugs.md))
- Baggage cart design (airport equipment domain)

---

## 3. Technical Requirements

### 3.1 Towing Capacity

- **Maximum Tow Weight**: 15,000 kg (5 fully loaded baggage carts)
- **Hitch System**: NATO standard tow bar and quick-release coupling
- **Towing Speed**: 0-40 km/h (governed)
- **Cart Configuration**: Up to 5 carts in train configuration
- **Grade Capability**: 8% gradient with full load

### 3.2 Physical Specifications

- **Overall Dimensions**: Length 3.5m × Width 1.3m × Height 2.1m
- **Wheelbase**: 2.0m
- **Ground Clearance**: 150mm minimum
- **Turning Radius**: 4.5m (inside)
- **Gross Vehicle Weight**: 2,500 kg
- **Payload**: N/A (towing only)

### 3.3 Battery System

- **Battery Type**: Lithium-ion (LFP chemistry preferred)
- **Energy Capacity**: 80-120 kWh
- **Operating Voltage**: 400 VDC nominal
- **Operating Duration**: 12-16 hours per charge (typical operations)
- **Charging Time**:
  - Full charge (0-100%): 4 hours
  - Opportunity charging: 50% in 30 minutes
- **Battery Life**: Minimum 6,000 charge cycles at 80% DoD
- **Thermal Management**: Active liquid cooling system

### 3.4 Electric Drivetrain

- **Motor Type**: Permanent magnet AC motor
- **Motor Power**: 40-60 kW continuous, 80 kW peak
- **Drive Configuration**: Rear-wheel drive
- **Transmission**: Single-speed reduction gearbox
- **Regenerative Braking**: Minimum 70% energy recovery
- **Efficiency**: >85% system efficiency at rated load

### 3.5 Environmental Requirements

- **Operating Temperature**: -30°C to +50°C
- **Humidity**: 0-100% (rain and snow capable)
- **Ingress Protection**: IP66 for electrical systems
- **Wind Resistance**: Operational in 60 km/h winds
- **Altitude**: Operation up to 3,000m AMSL

---

## 4. Operational Requirements

### 4.1 Performance Metrics

- **Daily Operational Range**: 150-200 km per charge
- **Availability**: >97% during scheduled operations
- **Reliability**: MTBF >4,000 hours
- **Acceleration**: 0-40 km/h in <10 seconds (unladen)
- **Braking Distance**: <15m from 40 km/h (laden)

### 4.2 Safety Features

- **Emergency Stop**: Push-button emergency stop on dashboard
- **Dead Man Switch**: Operator seat occupancy sensor
- **Backup Alarm**: Automatic reverse warning system
- **Lights**: LED headlights, tail lights, warning beacons
- **Mirrors**: Wide-angle side and rear-view mirrors
- **Hitch Monitor**: Automatic detection of connected carts
- **Stability Control**: Electronic stability program (ESP)
- **Fire Suppression**: Automatic system for battery compartment

### 4.3 Operator Interface

- **Driver Position**: Enclosed cabin with HVAC
- **Steering**: Power-assisted rack and pinion
- **Controls**: Accelerator, brake, forward/reverse selector
- **Display**: Digital instrument cluster showing:
  - Speed, SOC, range estimate
  - Cart count and hitch status
  - Warnings and diagnostics
- **Communication**: Integrated two-way radio
- **Ergonomics**: Adjustable seat, ergonomic controls per [ISO 6682-1](https://www.iso.org/standard/45086.html)

---

## 5. Integration Requirements

### 5.1 Airport Infrastructure

- **Charging Infrastructure**: Compatible with airport charging stations (see [85-70-04](../85-70-04_Charging_Infrastructure/))
- **Fleet Management**: GPS tracking and dispatch system integration
- **Baggage Handling System**: Coordination with airport BHS schedules
- **Apron Operations**: Compliance with airport ground traffic rules
- **Weather Protection**: Indoor/outdoor parking capability

### 5.2 Software Systems

- **Telematics**: Real-time location, status, and diagnostics
- **Fleet Management**: Integration with airport GSE management
- **Maintenance System**: Predictive maintenance alerts (see [85-70-06](../85-70-06_Maintenance_and_Diagnostics/))
- **Energy Management**: Smart charging schedule optimization
- **Driver Management**: Access control and driver identification

### 5.3 Communication Systems

- **Radio System**: Airport ground frequency compatibility
- **WiFi/Cellular**: 4G/5G connectivity for data transmission
- **RFID**: Baggage cart identification and tracking
- **Emergency Communication**: Direct link to airport operations center

---

## 6. Standards and Compliance

### 6.1 Aviation Standards

- [IATA AHM](https://www.iata.org/en/publications/manuals/airport-handling-manual/) – Airport Handling Manual
- [SAE AS6171](https://www.sae.org/standards/content/as6171/) – Ground support equipment terminology
- [EASA Part-145](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-13212014) – Maintenance organization approval

### 6.2 Vehicle Safety Standards

- [ISO 3691-4](https://www.iso.org/standard/66916.html) – Industrial trucks - Safety requirements - Driverless trucks
- [ISO 6682-1](https://www.iso.org/standard/45086.html) – Earth-moving machinery - Zones of comfort and reach for controls
- [EN 1175](https://standards.iteh.ai/catalog/standards/cen/2e5e5e5e-2e5e-2e5e-2e5e-2e5e2e5e2e5e/en-1175-2020) – Safety of industrial trucks – Electrical requirements

### 6.3 Electric Vehicle Standards

- [UN ECE R100](https://unece.org/transport/vehicle-regulations-wp29/standards/addenda-1958-agreement-regulations-101-120) – Electric power trained vehicles safety
- [IEC 61851-1](https://webstore.iec.ch/publication/6035) – EV conductive charging system
- [ISO 17409](https://www.iso.org/standard/59887.html) – Electrically propelled road vehicles - Connection to external electric circuit

### 6.4 Battery Standards

- [UL 2580](https://www.ul.com/resources/ul-2580-standard-safety) – Batteries for electric vehicles
- [IEC 62619](https://webstore.iec.ch/publication/7299) – Secondary cells and batteries for industrial applications
- [SAE J2929](https://www.sae.org/standards/content/j2929_201104/) – Electric and hybrid vehicle propulsion battery system safety

---

## 7. Performance Monitoring

### 7.1 Key Performance Indicators

- **Energy Efficiency**: kWh per km traveled
- **Cart-km Hauled**: Total cart-kilometers per day
- **Battery Health**: State of Health (SOH) tracking
- **Operational Uptime**: Available hours / scheduled hours
- **Maintenance Costs**: Cost per operational kilometer
- **Carbon Footprint**: Lifecycle CO₂ equivalent emissions

### 7.2 Data Collection

- **Telematics Data**: 
  - Position tracking (GPS)
  - Speed and acceleration profiles
  - Energy consumption per trip
- **Operational Data**:
  - Number of carts towed
  - Distance traveled
  - Charging events and duration
- **Maintenance Data**:
  - Component wear and tear
  - Fault codes and diagnostics
  - Service intervals and costs
- **Safety Data**:
  - Incident reports
  - Near-miss events
  - Driver behavior analysis

---

## 8. Environmental Considerations

### 8.1 Emissions

- **Zero Tailpipe Emissions**: No local air pollution
- **Lifecycle Assessment**: Full LCA per [ISO 14040](https://www.iso.org/standard/37456.html)
- **Carbon Intensity**: Based on electricity grid mix
- **Noise Levels**: <68 dB(A) at 7m (significantly quieter than diesel)

### 8.2 Sustainability

- **Battery Recycling**: End-of-life battery recycling plan
- **Component Reuse**: Design for disassembly and reuse
- **Circular Economy**: Integration with [85-30_Circularity](../../85-30_Circularity/) framework
- **Energy Source**: Preference for renewable energy charging

---

## 9. Cross-References

### 9.1 Internal (ATA 85)

- [85-70-01-A-001_Equipment_Specifications.csv](./ASSETS/85-70-01-A-001_Equipment_Specifications.csv) – Detailed specifications
- [85-70-01-A-002_Performance_Requirements.csv](./ASSETS/85-70-01-A-002_Performance_Requirements.csv) – Performance data
- [85-70-01-A-003_Battery_Systems.md](./ASSETS/85-70-01-A-003_Battery_Systems.md) – Battery design
- [85-70-04](../85-70-04_Charging_Infrastructure/) – Charging infrastructure
- [85-70-05](../85-70-05_Motor_and_Drivetrain/) – Drivetrain specifications
- [85-70-06](../85-70-06_Maintenance_and_Diagnostics/) – Maintenance procedures

### 9.2 External (Other ATAs)

- [ATA 03 – Support Information GSE](../../../ATA_03-SUPPORT_INFORMATION_GSE/)
- [ATA 12 – Servicing](../../../../P-PROGRAM/ATA_12-SERVICING/)

---

## 10. Status and Next Steps

- **Current Phase**: Requirements specification and vendor selection
- **Next Phase**: Pilot program with selected airport partner
- **Dependencies**: Airport charging infrastructure deployment, fleet management system integration

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22.

---

**End of Document**
