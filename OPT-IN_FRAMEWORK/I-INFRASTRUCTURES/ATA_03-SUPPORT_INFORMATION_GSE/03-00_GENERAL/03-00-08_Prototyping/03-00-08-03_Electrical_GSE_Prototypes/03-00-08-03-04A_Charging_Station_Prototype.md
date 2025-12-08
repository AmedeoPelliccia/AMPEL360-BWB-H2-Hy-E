# 03-00-08-03-04A - Charging Station Prototype

## 1. Purpose
This document defines the prototype development for Charging Station equipment designed to recharge battery-powered ground support equipment, electric ground vehicles, and auxiliary power systems supporting the AMPEL360 hydrogen aircraft operations.

## 2. Scope
This prototype covers charging infrastructure including AC and DC charging stations, battery management integration, smart charging controls, renewable energy integration, load management, and fleet charging coordination for airport GSE operations.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- SAE ARP1796 (GSE Design Requirements)
- SAE J1772 (Electric Vehicle Conductive Charge Coupler)
- IEC 61851 (Electric Vehicle Charging Systems)
- UL 2202 (Electric Vehicle Charging Equipment)
- NEC Article 625 (Electric Vehicle Charging)
- ISO 15118 (Vehicle to Grid Communication)
- [Reference to 03-00-02_Safety]
- [Reference to 03-00-08-03-02A_Power_Cart_Prototype]

## 4. Prototype Description

### 4.1 Overview
The Charging Station Prototype provides intelligent charging infrastructure for battery-powered GSE, supporting both conventional electric vehicles and specialized aviation ground equipment. It features smart charging, load management, renewable energy integration, and fleet charging coordination.

### 4.2 Design Specifications

| Parameter | Specification | Target |
|-----------|---------------|--------|
| AC Charging Power | Level 2 charging | 7.7-19.2 kW, 240 VAC |
| DC Fast Charging | Rapid charging capability | 50-150 kW, 400-800 VDC |
| Number of Ports | Simultaneous charging | 4-8 ports per station |
| Connector Types | Universal compatibility | CCS, CHAdeMO, Type 2 |
| Communication | Smart charging protocol | ISO 15118, OCPP 2.0 |
| Load Management | Dynamic power allocation | Real-time load balancing |
| Renewable Integration | Solar/wind input | Up to 50% renewable power |
| Network Connectivity | Cloud management | 4G/5G, Ethernet, Wi-Fi |
| User Interface | Payment and authentication | RFID, mobile app, credit card |
| Weather Protection | Outdoor installation | IP54 rating, -30°C to +50°C |

### 4.3 Materials and Components

#### 4.3.1 Power Electronics
- **AC Charging Module**: 7.7-19.2 kW EVSE units
- **DC Charging Module**: 50-150 kW DC fast charger
- **Power Conversion**: AC/DC converters with PFC
- **Grid Interface**: Medium voltage switchgear (if required)
- **Transformer**: Step-down transformer for distribution

#### 4.3.2 Control and Communication
- **Charge Controller**: Smart charging management system
- **Communication Gateway**: OCPP 2.0 compliant
- **Network Interface**: Cellular, Ethernet, Wi-Fi
- **Load Management**: Dynamic power allocation controller
- **Metering**: Revenue-grade energy meters

#### 4.3.3 User Interface
- **Display**: 7-10 inch touchscreen
- **Card Reader**: RFID/NFC for authentication
- **Payment Terminal**: Credit/debit card processing
- **Mobile App**: Smartphone integration
- **Status Indicators**: LED status lights

#### 4.3.4 Safety and Protection
- **Ground Fault Protection**: GFCI/RCD devices
- **Overcurrent Protection**: Circuit breakers and fuses
- **Emergency Stop**: Manual E-stop button
- **Cable Management**: Retractable cable holder
- **Collision Protection**: Bollards or barriers

#### 4.3.5 Renewable Energy Integration
- **Solar Interface**: DC input from solar panels
- **Energy Storage**: Optional battery buffer
- **Inverter**: Bidirectional for V2G capability
- **Monitoring**: Renewable generation tracking

## 5. Prototype Build Plan

| Phase | Activities | Duration | Deliverables |
|-------|------------|----------|--------------|
| Requirements | Site assessment, power requirements | 1 month | Requirements document |
| Design | Electrical design, network architecture | 2 months | Design package |
| Procurement | Charging modules, control systems | 2 months | Equipment inventory |
| Installation | Site preparation, equipment installation | 1 month | Installed station |
| Commissioning | Testing, calibration, certification | 1 month | Operational charging station |

## 6. Testing Requirements

### 6.1 Electrical Performance Testing
- **AC Charging**: Power delivery at various levels
- **DC Charging**: Fast charge performance and efficiency
- **Power Quality**: THD, power factor, voltage regulation
- **Efficiency**: Energy conversion efficiency
- **Load Management**: Dynamic power allocation testing
- **Grid Interface**: Utility interconnection testing

### 6.2 Communication and Smart Charging
- **OCPP Protocol**: Backend communication verification
- **ISO 15118**: Vehicle-to-grid communication testing
- **Load Balancing**: Multi-vehicle charging scenarios
- **Authentication**: User identification and authorization
- **Data Logging**: Charging session recording
- **Remote Management**: Cloud control and monitoring

### 6.3 Safety Testing
- **Ground Fault Protection**: GFCI response time
- **Overcurrent Protection**: Breaker operation
- **Emergency Stop**: E-stop shutdown verification
- **Electrical Safety**: Touch voltage, ground continuity
- **Arc Fault**: AFCI functionality (if equipped)
- **Cable Interlock**: Vehicle disconnect detection

### 6.4 Environmental Testing
- **Temperature Range**: Operation from -30°C to +50°C
- **Humidity**: High humidity and condensing conditions
- **Water Ingress**: IP54 rating verification
- **UV Exposure**: Outdoor weathering
- **Vibration**: Structural stability testing
- **Impact**: Collision resistance (bollards)

### 6.5 User Experience Testing
- **Ease of Use**: User interface intuitiveness
- **Charging Start**: Time from plug-in to charge start
- **Payment Processing**: Transaction speed and reliability
- **Mobile App**: App functionality and features
- **Accessibility**: ADA compliance verification
- **Signage**: Wayfinding and instruction clarity

### 6.6 Integration Testing
- **Fleet Management**: Multiple GSE charging coordination
- **Grid Integration**: Utility demand response
- **Renewable Energy**: Solar/wind integration testing
- **Energy Storage**: Battery buffer operation
- **V2G Capability**: Bidirectional power flow (if applicable)
- **Billing System**: Payment processing integration

### 6.7 Durability and Reliability
- **Connector Durability**: 10,000 plug/unplug cycles
- **Continuous Operation**: 24/7 operation testing
- **Power Cycling**: Start/stop cycle testing
- **Component Life**: MTBF assessment
- **Preventive Maintenance**: Maintenance interval validation

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 03-00-05 (Interfaces)
  - ATA 03-00-06 (Engineering)
  - ATA 03-00-07 (V&V)
  - ATA 24 (Electrical Power)
- Parent Document: 03-00-08_Prototyping
- Related Power Cart: 03-00-08-03-02A_Power_Cart_Prototype
- Related Cable Systems: 03-00-08-03-03A_Cable_System_Prototype
- Related Operations: 03-10_Operations

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation WG | Initial release |
