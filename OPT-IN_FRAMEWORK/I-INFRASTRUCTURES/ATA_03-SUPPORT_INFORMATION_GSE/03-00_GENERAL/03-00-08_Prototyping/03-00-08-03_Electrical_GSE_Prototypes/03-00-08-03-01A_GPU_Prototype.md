# 03-00-08-03-01A - GPU Prototype

## 1. Purpose
This document defines the prototype development for Ground Power Unit (GPU) equipment designed to provide electrical power to the AMPEL360 aircraft during ground operations, supporting both conventional and hydrogen-electric hybrid propulsion system requirements.

## 2. Scope
This prototype covers the complete GPU system including power generation, voltage regulation, frequency control, distribution panels, cable management, protection systems, and monitoring interfaces for safe and reliable aircraft ground power supply.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- SAE ARP1796 (GSE Design Requirements)
- SAE AS50881 (Wiring Aerospace Vehicle)
- MIL-STD-704 (Aircraft Electrical Power Characteristics)
- IEEE 519 (Harmonic Control in Electrical Power Systems)
- [Reference to 03-00-02_Safety]
- [Reference to 03-00-05_Interfaces]

## 4. Prototype Description

### 4.1 Overview
The GPU Prototype is designed to provide stable, clean electrical power to aircraft during ground operations, including pre-flight checks, maintenance, and turnaround operations. It must meet strict power quality requirements while being mobile, efficient, and safe for airport ramp operations.

### 4.2 Design Specifications

| Parameter | Specification | Target |
|-----------|---------------|--------|
| Output Power | Three-phase AC power | 90 kVA (expandable to 120 kVA) |
| Voltage | Aircraft standard | 115/200 VAC, 400 Hz |
| DC Output | Auxiliary DC power | 28 VDC, 300 A |
| Frequency Stability | Frequency regulation | 400 Hz ±0.5 Hz |
| Voltage Regulation | Voltage stability | ±1% under all loads |
| THD (Total Harmonic Distortion) | Power quality | < 3% |
| Power Factor | Efficiency | > 0.95 |
| Noise Level | Acoustic emissions | < 75 dB at 7m |
| Mobility | Transport capability | Towed, self-propelled option |

### 4.3 Materials and Components
- **Power Source**: Diesel generator or battery-electric system
- **Generator**: 3-phase synchronous alternator
- **Inverter**: High-efficiency power electronics (for battery version)
- **Control System**: Digital power management controller
- **Protection**: Circuit breakers, ground fault protection
- **Distribution**: Heavy-duty connectors and cable sets
- **Monitoring**: Power quality analyzer and display
- **Cooling**: Forced air or liquid cooling system
- **Enclosure**: Weatherproof, noise-dampened housing

## 5. Prototype Build Plan

| Phase | Activities | Duration | Deliverables |
|-------|------------|----------|--------------|
| Design | Electrical system design, power calculations | 2 months | Design specifications |
| Procurement | Generator, inverter, control components | 2 months | Component inventory |
| Assembly | Integration, wiring, panel construction | 2 months | Assembled GPU unit |
| Software | Control logic, protection systems | 1 month | Control software |
| Testing | Load testing, power quality verification | 2 months | Test reports |

## 6. Testing Requirements

### 6.1 Electrical Performance Testing
- **No-load Testing**: Voltage and frequency at no load
- **Load Testing**: Performance at 25%, 50%, 75%, 100% load
- **Transient Response**: Step load changes
- **Power Quality**: THD, voltage regulation, frequency stability
- **Efficiency**: Power conversion efficiency across load range
- **Power Factor**: Measurement under various loads

### 6.2 Protection System Testing
- **Overcurrent Protection**: Circuit breaker operation
- **Ground Fault**: Ground fault detection and isolation
- **Over/Under Voltage**: Voltage limit protection
- **Over/Under Frequency**: Frequency limit protection
- **Phase Loss**: Single-phase loss detection
- **Emergency Shutdown**: E-stop functionality

### 6.3 Interface Testing
- **Aircraft Connection**: Compatibility with aircraft receptacle
- **Cable Testing**: Insulation, continuity, voltage drop
- **Connector Testing**: Insertion/extraction force, retention
- **Grounding**: Earth continuity verification
- **Polarity**: Phase sequence verification

### 6.4 Environmental Testing
- **Temperature Range**: Operation from -30°C to +50°C
- **Humidity**: Performance in 95% relative humidity
- **Vibration**: Transport vibration testing
- **Noise**: Acoustic emission measurement
- **EMI/EMC**: Electromagnetic compatibility testing

### 6.5 Durability Testing
- **Continuous Operation**: 8-hour run test at full load
- **Start/Stop Cycles**: 1000 start/stop cycles
- **Thermal Cycling**: Temperature cycling tests
- **Component Life**: Accelerated life testing

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 03-00-05 (Interfaces)
  - ATA 03-00-06 (Engineering)
  - ATA 24 (Electrical Power - Aircraft)
- Parent Document: 03-00-08_Prototyping
- Related Electrical GSE: 03-00-08-03-02A_Power_Cart_Prototype
- Related Charging: 03-00-08-03-04A_Charging_Station_Prototype
- Related Testing: 03-00-08-06_GSE_Prototype_Testing

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation WG | Initial release |
