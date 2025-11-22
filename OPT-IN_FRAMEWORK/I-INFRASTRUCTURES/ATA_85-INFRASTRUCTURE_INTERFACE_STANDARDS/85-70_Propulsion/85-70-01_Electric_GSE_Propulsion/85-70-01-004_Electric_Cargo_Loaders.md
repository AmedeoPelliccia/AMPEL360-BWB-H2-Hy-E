# 85-70-01-004: Electric Cargo Loaders

## Document Information

- **Document ID**: 85-70-01-004
- **Title**: Electric Cargo Loaders
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

---

## 1. Purpose

This document defines specifications and requirements for battery-electric cargo loader systems used for loading and unloading containerized cargo and pallets on the AMPEL360 BWB-H2-Hy-E aircraft.

---

## 2. Scope

### 2.1 In Scope

- Battery-electric main deck cargo loaders
- Lower deck cargo loader specifications
- Container and pallet handling capabilities
- Battery system and charging requirements
- Safety systems and automation
- Integration with airport cargo handling systems

### 2.2 Out of Scope

- Belt loaders for bulk baggage (see [85-70-01-002](./85-70-01-002_Electric_Belt_Loaders.md))
- Cargo handling procedures (airport operations domain)
- Warehouse and terminal cargo systems

---

## 3. Technical Requirements

### 3.1 Loading Capacity

- **Maximum Load Weight**: 32,000 kg (containerized cargo)
- **Container Types**: LD3, LD7, LD9, LD11, and BWB-specific containers
- **Pallet Dimensions**: Up to 3.17m × 2.43m (125" × 96")
- **Platform Load**: 15,000 kg per platform
- **Dual Platform**: Simultaneous loading capability
- **Height Range**: Ground level to 8 meters (BWB main deck)

### 3.2 Physical Specifications

- **Overall Length**: 15-18 meters (deployed)
- **Overall Width**: 3.5-4.0 meters
- **Overall Height**: 9-10 meters (maximum elevation)
- **Platform Width**: 3.2 meters
- **Platform Length**: 7.0 meters
- **Wheelbase**: 5.5 meters
- **Gross Vehicle Weight**: 45,000 kg

### 3.3 Lifting System

- **Lift Type**: Scissor lift mechanism with redundant hydraulic systems
- **Lift Speed**: 0.3-0.5 m/s (variable)
- **Platform Tilt**: ±5° adjustment for aircraft interface
- **Stabilizers**: Four-point hydraulic outriggers
- **Load Sensing**: Real-time weight distribution monitoring
- **Emergency Descent**: Manual and battery-powered backup

### 3.4 Battery System

- **Battery Type**: Lithium-ion (NMC or LFP chemistry)
- **Energy Capacity**: 400-500 kWh
- **Operating Voltage**: 800 VDC nominal
- **Operating Duration**: 10-12 hours continuous operation
- **Charging Time**:
  - Full charge: 6-8 hours
  - Fast charge: 80% in 2 hours
  - Opportunity charging: Compatible
- **Battery Life**: Minimum 4,000 charge cycles at 80% DoD
- **Battery Thermal Management**: Active liquid cooling/heating

### 3.5 Electric Propulsion and Hydraulics

- **Traction Motors**: 2× 50 kW permanent magnet motors
- **Hydraulic Pump**: 75 kW electric motor-driven pump
- **Drive Configuration**: All-wheel drive (4×4)
- **Top Speed**: 20 km/h
- **Gradeability**: 10% at full load
- **Steering**: Four-wheel steering
- **Braking**: Regenerative + hydraulic disc brakes

### 3.6 Environmental Requirements

- **Operating Temperature**: -25°C to +50°C
- **Humidity**: 0-100% (weatherproof operation)
- **Ingress Protection**: IP65 for electrical systems
- **Wind Resistance**: Operational up to 45 km/h wind (retracted)
- **Altitude**: Up to 3,000m AMSL

---

## 4. Operational Requirements

### 4.1 Performance Metrics

- **Loading Rate**: 20-25 ULD per hour
- **Positioning Time**: <3 minutes from arrival to aircraft interface
- **Accuracy**: ±30mm positioning at cargo door
- **Availability**: >96% during operational hours
- **Reliability**: MTBF >2,500 hours
- **Maintainability**: MTTR <6 hours for critical failures

### 4.2 Safety Features

- **Platform Safety Gates**: Automatic deployment at height
- **Anti-collision System**: 360° radar and camera coverage
- **Load Monitoring**: Overload protection and alarm
- **Stabilizer Sensors**: Automatic deployment verification
- **Emergency Stop**: Multiple E-stop buttons (platform and ground)
- **Wind Speed Sensor**: Operation lockout in high winds
- **Fire Suppression**: Automatic system for battery and hydraulic compartments
- **Aircraft Protection**: Soft-contact bumpers and proximity sensors
- **Operator Safety**:
  - Fall protection anchor points
  - Non-slip platform surfaces
  - Safety railings and gates

### 4.3 Operator Controls

- **Primary Controls**: Platform-mounted control console
- **Backup Controls**: Ground-level control panel
- **Display System**:
  - Digital readout for height, load, tilt
  - Battery SOC and range estimate
  - Camera views (aircraft interface, surroundings)
  - Diagnostics and warning messages
- **Communication**: Integrated radio and intercom systems
- **Automation**: Semi-automated positioning and height adjustment
- **Ergonomics**: Climate-controlled operator cabin

---

## 5. Integration Requirements

### 5.1 Aircraft Interface

- **BWB Cargo Door Compatibility**: Adjustable for main and lower deck doors
- **Door Sill Protection**: Compliant bumpers and roller systems
- **Aircraft Grounding**: Bonding connection during cargo operations
- **Power Assist**: Powered rollers to transfer cargo into aircraft
- **Environmental Seal**: Weather curtain for rain protection
- **Lighting**: LED work lights for night operations

### 5.2 Airport Infrastructure

- **Charging Infrastructure**: High-power DC fast charging (see [85-70-04](../85-70-04_Charging_Infrastructure/))
- **Fleet Management**: Real-time tracking and dispatch
- **Cargo System Integration**: Interface with airport cargo management system (CMS)
- **Warehouse Interface**: Coordination with cargo terminal operations
- **Weather Protection**: Indoor storage with charging capability

### 5.3 Software Systems

- **Fleet Management**: Real-time location and status
- **Load Planning**: Integration with aircraft load and balance system
- **Maintenance Management**: Predictive maintenance (see [85-70-06](../85-70-06_Maintenance_and_Diagnostics/))
- **Energy Management**: Smart charging optimization
- **Safety Monitoring**: Automated incident reporting
- **Cargo Tracking**: ULD identification and verification (RFID/barcode)

---

## 6. Standards and Compliance

### 6.1 Aviation Standards

- [IATA ULD Regulations](https://www.iata.org/en/publications/manuals/unit-load-devices-regulations/) – Unit load device standards
- [IATA AHM](https://www.iata.org/en/publications/manuals/airport-handling-manual/) – Airport handling procedures
- [SAE AS36100](https://www.sae.org/standards/content/as36100/) – Unit load devices
- [EASA Part-M](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-13212014) – Continuing airworthiness

### 6.2 Safety Standards

- [ISO 13849-1](https://www.iso.org/standard/69883.html) – Safety-related parts of control systems
- [EN 1915-2](https://standards.iteh.ai/catalog/standards/cen/1a3a0f0c-0a1e-4f5e-9e6e-5c0f5e5e5e5e/en-1915-2-2013) – Aircraft ground support equipment - Safety requirements - Loader/transporters
- [ISO 23386](https://www.iso.org/standard/75365.html) – Building construction machinery and equipment - Safety requirements

### 6.3 Electric Vehicle Standards

- [IEC 61851-1](https://webstore.iec.ch/publication/6035) – EV conductive charging
- [ISO 15118](https://www.iso.org/standard/55366.html) – Vehicle-to-grid communication
- [UN ECE R100](https://unece.org/transport/vehicle-regulations-wp29/standards/addenda-1958-agreement-regulations-101-120) – Electric vehicle safety

### 6.4 Hydraulic and Mechanical Standards

- [ISO 4413](https://www.iso.org/standard/51184.html) – Hydraulic fluid power systems - General rules
- [ISO 12100](https://www.iso.org/standard/51528.html) – Safety of machinery - General principles

---

## 7. Automation Features

### 7.1 Semi-Automated Functions

- **Auto-positioning**: GPS and visual guidance to aircraft door
- **Height Adjustment**: Automatic platform leveling to door sill
- **Load Transfer**: Powered roller system with automatic speed control
- **Stabilizer Deployment**: Automatic when platform elevated
- **Safety Monitoring**: AI-based collision avoidance

### 7.2 Future Automation Roadmap

- **Phase 1** (Current): Manual operation with safety assists
- **Phase 2** (2026-2027): Semi-automated positioning and loading
- **Phase 3** (2028+): Fully autonomous cargo loading operations
- **Integration**: Link to [ATA 85-40 Software](../../85-40_Software/) and [ATA 97 Neural Networks](../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_97-NEURAL_NETWORK_MODELS/)

---

## 8. Performance Monitoring

### 8.1 Key Performance Indicators

- **ULD Handling Rate**: ULD per hour per loader
- **Energy Efficiency**: kWh per ULD handled
- **Battery Health**: SOH tracking and predictive replacement
- **Operational Uptime**: Availability percentage
- **Maintenance Costs**: Cost per ULD handled
- **Safety Incidents**: Target zero accidents
- **Carbon Footprint**: Lifecycle emissions per ISO 14040

### 8.2 Data Collection

- **Telematics**: Real-time position, status, energy use
- **Load Data**: Weight, distribution, ULD identification
- **Operational Metrics**: Cycle times, positioning accuracy
- **Maintenance Data**: Component health, predictive alerts
- **Energy Data**: Charging events, consumption patterns
- **Safety Data**: Incident logs, near-miss events

---

## 9. Cross-References

### 9.1 Internal (ATA 85)

- [85-70-01-A-001_Equipment_Specifications.csv](./ASSETS/85-70-01-A-001_Equipment_Specifications.csv) – Equipment specs
- [85-70-01-A-002_Performance_Requirements.csv](./ASSETS/85-70-01-A-002_Performance_Requirements.csv) – Performance benchmarks
- [85-70-01-A-003_Battery_Systems.md](./ASSETS/85-70-01-A-003_Battery_Systems.md) – Battery system details
- [85-70-04](../85-70-04_Charging_Infrastructure/) – Charging infrastructure
- [85-70-05](../85-70-05_Motor_and_Drivetrain/) – Motor and drivetrain
- [85-70-06](../85-70-06_Maintenance_and_Diagnostics/) – Maintenance procedures

### 9.2 External (Other ATAs)

- [ATA 03 – Support Information GSE](../../../ATA_03-SUPPORT_INFORMATION_GSE/)
- [ATA 12 – Servicing](../../../../P-PROGRAM/ATA_12-SERVICING/)
- [ATA 85-40 – Software](../../85-40_Software/) – Control software

---

## 10. Status and Next Steps

- **Current Phase**: Requirements definition and vendor RFP preparation
- **Next Phase**: Prototype evaluation and airport trials
- **Dependencies**: BWB cargo door specifications, airport cargo system upgrades

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22.

---

**End of Document**
