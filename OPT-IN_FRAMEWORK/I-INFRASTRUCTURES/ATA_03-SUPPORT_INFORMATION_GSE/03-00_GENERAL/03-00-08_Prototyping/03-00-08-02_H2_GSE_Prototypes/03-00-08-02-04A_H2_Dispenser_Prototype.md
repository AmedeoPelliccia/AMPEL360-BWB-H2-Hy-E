# 03-00-08-02-04A - H2 Dispenser Prototype

## 1. Purpose
This document defines the prototype development for the Hydrogen Dispenser system, which serves as the primary interface between ground storage and aircraft fueling operations, providing controlled and metered delivery of liquid hydrogen to the AMPEL360 aircraft.

## 2. Scope
This prototype covers the complete dispenser system including metering equipment, flow control valves, nozzle and coupling systems, user interface, safety interlocks, and integration with both ground storage and aircraft fueling systems.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- SAE ARP1796 (GSE Design Requirements)
- SAE AS6968 (Hydrogen Aircraft Refueling)
- ISO 19880-1 (Gaseous Hydrogen Fueling Stations - General Requirements)
- ISO 19880-5 (Dispenser Safety Requirements)
- NFPA 2 (Hydrogen Technologies Code)
- [Reference to 03-00-02_Safety]
- [Reference to 03-00-08-02-01A_LH2_Fueling_GSE_Prototype]
- [Reference to 03-00-08-02-03A_H2_Safety_GSE_Prototype]

## 4. Prototype Description

### 4.1 Overview
The H2 Dispenser Prototype is the critical control point for aircraft refueling operations. It must accurately meter hydrogen flow, maintain precise temperature and pressure control, provide intuitive operator interface, ensure safety through multiple interlocks, and log all fueling transactions for traceability.

### 4.2 Design Specifications

| Parameter | Specification | Target |
|-----------|---------------|--------|
| Flow Rate Range | Controllable flow rate | 50-500 kg/hr |
| Metering Accuracy | Flow measurement precision | ±0.5% of reading |
| Operating Pressure | Dispenser pressure range | 1-8 bar |
| Temperature Control | LH2 temperature maintenance | -253°C ±2°C |
| Response Time | Flow adjustment response | < 1 second |
| User Interface | Touchscreen HMI | 10-12 inch display |
| Safety Interlocks | Number of safety systems | 8+ independent interlocks |
| Data Logging | Transaction recording | 100% of fueling events |
| Hose Length | Reach to aircraft | 10-15 meters |
| Coupling Type | Aircraft interface standard | AS6968-compliant |

### 4.3 Materials and Components

#### 4.3.1 Flow Control Components
- **Mass Flow Meters**: Coriolis-type meters for accuracy
- **Control Valves**: Cryogenic ball and butterfly valves
- **Pressure Regulators**: Precision pressure control
- **Temperature Sensors**: RTD sensors for temperature monitoring
- **Pressure Transducers**: High-accuracy pressure measurement

#### 4.3.2 Dispenser Structure
- **Cabinet**: Weatherproof stainless steel enclosure
- **Mounting System**: Mobile or fixed installation options
- **Service Hose**: Vacuum-insulated flexible hose
- **Nozzle Assembly**: Quick-disconnect coupling with break-away
- **Hose Management**: Retraction system and supports

#### 4.3.3 Control and Safety Systems
- **PLC Controller**: Programmable logic controller
- **HMI Display**: Operator interface and status display
- **Emergency Stop**: Multiple E-stop locations
- **Grounding System**: Static discharge protection
- **Leak Detection**: H2 sensors around dispenser
- **Interlock System**: Pre-fueling checklist verification

#### 4.3.4 Communication and Data Systems
- **Data Logger**: Transaction and event recording
- **Network Interface**: Connection to facility management
- **Payment System**: Authorization and billing interface
- **Diagnostic Tools**: Maintenance and troubleshooting
- **Remote Monitoring**: Cloud-based status reporting

## 5. Prototype Build Plan

| Phase | Activities | Duration | Deliverables |
|-------|------------|----------|--------------|
| Requirements | System specification, interface definitions | 1 month | Requirements document |
| Design | Mechanical, electrical, and software design | 3 months | Design package |
| Component Procurement | Long-lead items, specialized equipment | 2 months | Components inventory |
| Assembly | Integration of subsystems | 2 months | Assembled dispenser |
| Software Development | Control logic, HMI, diagnostics | 2 months | Software package |
| Testing | Factory and field testing | 2 months | Test reports |

## 6. Testing Requirements

### 6.1 Functional Testing

#### 6.1.1 Flow Control Testing
- **Flow Rate Accuracy**: Verify across full operating range
- **Pressure Control**: Maintain target pressure ±0.1 bar
- **Temperature Control**: LH2 temperature stability
- **Response Time**: Flow adjustment speed verification
- **Repeatability**: Multiple fueling cycle consistency

#### 6.1.2 Metering Accuracy Testing
- **Calibration**: Traceable flow calibration
- **Linearity**: Accuracy across flow range
- **Temperature Compensation**: Density correction
- **Long-term Stability**: Meter drift over time
- **Comparison**: Cross-check with reference meter

#### 6.1.3 User Interface Testing
- **HMI Functionality**: All screens and controls operational
- **Display Visibility**: Readable in sunlight and darkness
- **Response Time**: Touch response and screen updates
- **Error Messages**: Clear and actionable alerts
- **Language Support**: Multi-language interface

### 6.2 Safety Testing

#### 6.2.1 Interlock System Testing
- **Pre-fueling Checks**: Verify all interlocks functional
- **Ground Continuity**: Static discharge system testing
- **Emergency Stop**: E-stop response time < 1 second
- **Leak Detection**: Sensor activation and response
- **Break-away Coupling**: Separation force and sealing
- **Pressure Relief**: Safety valve activation

#### 6.2.2 Fail-safe Testing
- **Power Loss**: Safe shutdown on power failure
- **Control System Failure**: Default to safe state
- **Sensor Failures**: Redundancy and fault detection
- **Communication Loss**: Standalone operation capability

### 6.3 Environmental Testing
- **Temperature Range**: Operation from -30°C to +60°C
- **Humidity**: Performance in high humidity
- **Precipitation**: Rain and snow operation
- **Wind Loading**: Structural stability in wind
- **Vibration**: Transport and operational vibration
- **EMI/EMC**: Electromagnetic interference immunity

### 6.4 Durability Testing
- **Thermal Cycling**: 500 cooldown/warmup cycles
- **Coupling Cycles**: 10,000 connect/disconnect cycles
- **Valve Cycles**: 50,000 open/close cycles
- **Hose Flexing**: Fatigue testing of service hose
- **Long-term Operation**: 1000-hour endurance test

### 6.5 Integration Testing
- **Aircraft Interface**: Compatibility with aircraft receptacle
- **Facility Connection**: Integration with storage systems
- **Data Systems**: Network and database integration
- **Safety Systems**: Integration with facility safety systems
- **User Training**: Operator training effectiveness

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 03-00-02 (Safety)
  - ATA 03-00-05 (Interfaces)
  - ATA 03-00-06 (Engineering)
  - ATA 03-00-07 (V&V)
  - ATA 28 (Fuel)
- Parent Document: 03-00-08_Prototyping
- Related LH2 Fueling: 03-00-08-02-01A_LH2_Fueling_GSE_Prototype
- Related Cryogenic GSE: 03-00-08-02-02A_Cryogenic_GSE_Prototype
- Related H2 Safety: 03-00-08-02-03A_H2_Safety_GSE_Prototype

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation WG | Initial release |
