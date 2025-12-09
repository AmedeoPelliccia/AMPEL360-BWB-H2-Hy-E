# 03-00-08-03-02A - Power Cart Prototype

## 1. Purpose
This document defines the prototype development for mobile Power Cart equipment designed to provide portable electrical power distribution for various ground support operations, maintenance activities, and auxiliary systems supporting the AMPEL360 aircraft.

## 2. Scope
This prototype covers portable power distribution carts including battery banks, inverters, charging systems, multiple output configurations, cable management, and portable power solutions for field operations and maintenance activities.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- SAE ARP1796 (GSE Design Requirements)
- UL 2202 (Electric Vehicle Charging Equipment)
- NEC Article 625 (Electric Vehicle Charging)
- IEEE 1625 (Rechargeable Batteries for Multi-Cell Mobile Computing)
- [Reference to 03-00-02_Safety]
- [Reference to 03-00-08-03-01A_GPU_Prototype]

## 4. Prototype Description

### 4.1 Overview
The Power Cart Prototype provides flexible, mobile electrical power for various ground support needs. Unlike the main GPU, power carts are designed for portability, multiple output types, and distributed operations around the aircraft during maintenance and servicing.

### 4.2 Design Specifications

| Parameter | Specification | Target |
|-----------|---------------|--------|
| Battery Capacity | Energy storage | 20-40 kWh lithium-ion |
| AC Output | Standard power | 120/240 VAC, 60 Hz, 10 kVA |
| DC Outputs | Multiple DC voltages | 12V, 24V, 48V, various currents |
| USB/Charging | Device charging | USB-A, USB-C, wireless charging |
| Runtime | Continuous operation | 4-8 hours at 50% load |
| Recharge Time | Full charge time | < 4 hours |
| Weight | Portable weight | < 200 kg (440 lbs) |
| Mobility | Transport method | Wheeled cart, towable |
| Output Protection | Circuit protection | Individual circuit breakers |

### 4.3 Materials and Components
- **Battery System**: Lithium-ion battery pack with BMS
- **Inverter**: Pure sine wave inverter, 10 kVA
- **DC Converters**: Buck/boost converters for multiple outputs
- **Charge Controller**: Smart charging with temperature management
- **Distribution Panel**: Multiple outlet types and protection
- **Cable Management**: Retractable cord reels
- **Monitoring System**: Battery status, output monitoring
- **Housing**: Rugged, weatherproof enclosure
- **Wheels/Mobility**: Heavy-duty casters or tow bar

## 5. Prototype Build Plan

| Phase | Activities | Duration | Deliverables |
|-------|------------|----------|--------------|
| Requirements | User needs assessment, specifications | 1 month | Requirements document |
| Design | Electrical and mechanical design | 2 months | Design package |
| Procurement | Battery, inverter, components | 1 month | Components inventory |
| Assembly | Integration, wiring, testing | 1 month | Assembled power cart |
| Validation | Performance and safety testing | 1 month | Test reports |

## 6. Testing Requirements

### 6.1 Battery System Testing
- **Capacity Testing**: Discharge/charge cycling
- **BMS Functionality**: Battery management system validation
- **Temperature Management**: Thermal performance under load
- **Safety Testing**: Overcharge, overdischarge, short circuit protection
- **Cycle Life**: Accelerated aging testing
- **State of Charge**: SOC accuracy verification

### 6.2 Electrical Output Testing
- **AC Output Quality**: Voltage, frequency, waveform
- **DC Output Regulation**: Voltage stability under load
- **Load Testing**: Multiple outputs simultaneously
- **Efficiency**: Input/output power efficiency
- **Protection**: Overcurrent, short circuit protection
- **Parallel Operation**: Multiple carts operating together

### 6.3 Charging System Testing
- **Charge Rate**: Verification of charge time
- **Charge Algorithm**: Proper CC-CV charging
- **Temperature Compensation**: Charge adjustment for temperature
- **Input Compatibility**: Various input sources (grid, solar, generator)
- **Safety**: Charge fault detection and shutdown

### 6.4 Mobility and Ergonomics Testing
- **Maneuverability**: Ease of movement and positioning
- **Stability**: Tip-over resistance
- **Handle Design**: Ergonomic towing/pushing
- **Wheel Performance**: Various surface testing
- **Storage**: Compact storage configuration

### 6.5 Environmental Testing
- **Temperature Range**: Operation and storage limits
- **Humidity**: Sealed electronics testing
- **Vibration**: Transport vibration testing
- **Drop/Impact**: Ruggedness testing
- **Weather**: Rain and dust ingress testing

### 6.6 User Interface Testing
- **Display Readability**: Status information clarity
- **Control Accessibility**: Easy operation
- **Alarm/Warning**: Clear indication of faults
- **Documentation**: User manual effectiveness

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 03-00-06 (Engineering)
  - ATA 03-00-07 (V&V)
  - ATA 24 (Electrical Power)
- Parent Document: 03-00-08_Prototyping
- Related GPU: 03-00-08-03-01A_GPU_Prototype
- Related Cable Systems: 03-00-08-03-03A_Cable_System_Prototype
- Related Charging: 03-00-08-03-04A_Charging_Station_Prototype

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation WG | Initial release |
