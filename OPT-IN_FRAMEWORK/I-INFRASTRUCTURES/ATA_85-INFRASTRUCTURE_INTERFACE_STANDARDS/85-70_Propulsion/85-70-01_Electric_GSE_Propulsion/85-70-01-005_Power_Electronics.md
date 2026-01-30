# 85-70-01-005: Power Electronics

## Document Information

- **Document ID**: 85-70-01-005
- **Title**: Power Electronics
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

---

## 1. Purpose

This document defines the specifications and requirements for power electronics systems used in battery-electric Ground Support Equipment (GSE) for the AMPEL360 BWB-H2-Hy-E aircraft operations.

---

## 2. Scope

### 2.1 In Scope

- Power electronics architecture for electric GSE
- Inverters and motor controllers
- DC-DC converters and power distribution
- Battery management systems (BMS)
- Charging electronics and interfaces
- Thermal management for power electronics
- Safety and protection systems
- EMC and EMI considerations

### 2.2 Out of Scope

- Battery cell chemistry and design (see [85-70-01-A-003_Battery_Systems.md](./ASSETS/85-70-01-A-003_Battery_Systems.md))
- Charging infrastructure design (see [85-70-04](../85-70-04_Charging_Infrastructure/))
- Motor mechanical design (see [85-70-05](../85-70-05_Motor_and_Drivetrain/))

---

## 3. Power Electronics Architecture

### 3.1 System Overview

The power electronics system consists of:

1. **High-Voltage Battery System**: 400-800 VDC
2. **Battery Management System (BMS)**: Cell monitoring and protection
3. **DC-DC Converters**: High-voltage to low-voltage conversion
4. **Motor Controllers/Inverters**: DC to 3-phase AC conversion
5. **On-Board Charger (OBC)**: AC to DC charging electronics
6. **Auxiliary Power Supply**: 12V/24V for vehicle systems
7. **Thermal Management**: Cooling/heating for power electronics

### 3.2 Architecture Topology

```
HV Battery (400-800V)
    ↓
BMS (monitoring & protection)
    ↓
Main DC Bus (isolated)
    ├→ Traction Inverter → Motor(s)
    ├→ Auxiliary Inverter → Hydraulic Pump / Conveyor
    ├→ DC-DC Converter → 24V/12V System
    └→ On-Board Charger ← AC Input (Charging)
```

---

## 4. Technical Requirements

### 4.1 Motor Controllers / Inverters

#### 4.1.1 Traction Inverter

- **Topology**: Three-phase 2-level or 3-level IGBT/SiC inverter
- **Voltage Rating**: 450-900 VDC bus voltage
- **Current Rating**: 200-600 A continuous, 800 A peak (10s)
- **Power Rating**: 100-500 kW (depending on GSE type)
- **Switching Frequency**: 10-20 kHz
- **Efficiency**: >97% at rated load
- **Control Method**: Field-oriented control (FOC) or direct torque control (DTC)
- **Protection**: 
  - Overcurrent, overvoltage, undervoltage
  - Overtemperature shutdown
  - Short-circuit protection
  - Ground fault detection

#### 4.1.2 Auxiliary Inverter

- **Application**: Hydraulic pumps, conveyor systems, HVAC
- **Power Rating**: 20-100 kW
- **Voltage Rating**: Same as main bus (400-800 VDC)
- **Efficiency**: >95% at rated load
- **Control**: Variable frequency drive (VFD) with V/f or FOC

#### 4.1.3 Power Semiconductor Technology

- **IGBT** (Insulated Gate Bipolar Transistor):
  - Cost-effective for lower power applications (<200 kW)
  - Mature technology with proven reliability
- **SiC** (Silicon Carbide):
  - Higher efficiency (>98%)
  - Higher switching frequency → smaller passives
  - Better thermal performance
  - Recommended for high-power applications (>200 kW)
- **Compliance**: [AEC-Q101](https://www.aecouncil.com/AECDocuments.html) – Automotive electronics reliability

### 4.2 DC-DC Converters

#### 4.2.1 High-Voltage to Low-Voltage Converter

- **Input Voltage**: 400-800 VDC (HV battery)
- **Output Voltage**: 24 VDC ±5% (vehicle systems)
- **Output Power**: 3-10 kW continuous
- **Topology**: Isolated DC-DC (full bridge or LLC resonant)
- **Efficiency**: >94% at full load
- **Isolation**: Galvanic isolation per [IEC 60950-1](https://webstore.iec.ch/publication/4108)
- **Protection**: Output short-circuit, overload, thermal

#### 4.2.2 Auxiliary Low-Voltage Converter

- **Input Voltage**: 24 VDC
- **Output Voltage**: 12 VDC ±3%
- **Output Power**: 500-1000 W
- **Topology**: Buck converter (non-isolated)
- **Efficiency**: >92%

### 4.3 Battery Management System (BMS)

#### 4.3.1 Functions

- **Cell Monitoring**: Voltage, temperature, and current for each cell/module
- **State Estimation**: SOC, SOH, SOP, remaining range
- **Cell Balancing**: Active or passive balancing to equalize cells
- **Thermal Management**: Control of cooling/heating system
- **Safety**: Contactor control, fault detection, emergency shutdown
- **Communication**: CAN bus interface to vehicle controller

#### 4.3.2 Specifications

- **Voltage Measurement Accuracy**: ±5 mV per cell
- **Current Measurement Accuracy**: ±0.5% of full scale
- **Temperature Measurement Accuracy**: ±2°C
- **Balancing Current**: 100-500 mA per cell (passive) or 5-10 A (active)
- **Communication Protocol**: [CAN 2.0B](https://www.can-cia.org/) or CAN FD
- **Safety Certification**: [ISO 26262](https://www.iso.org/standard/68383.html) ASIL-C or ASIL-D

#### 4.3.3 Protection Functions

- **Overvoltage Protection**: Cell level and pack level
- **Undervoltage Protection**: Prevents deep discharge
- **Overcurrent Protection**: Charge and discharge limits
- **Overtemperature Protection**: Cell and module temperature limits
- **Short-Circuit Protection**: Fast shutdown (<10 ms)
- **Insulation Monitoring**: Continuous resistance measurement to ground

### 4.4 On-Board Charger (OBC)

#### 4.4.1 AC Input

- **Input Voltage**: 
  - Single-phase: 230 VAC ±10%
  - Three-phase: 400 VAC ±10%
- **Input Frequency**: 50/60 Hz ±5%
- **Power Factor**: >0.99 (unity power factor)
- **THD**: <5% (total harmonic distortion)

#### 4.4.2 DC Output

- **Output Voltage**: 450-850 VDC (matches battery voltage)
- **Output Power**: 
  - Level 2 (AC charging): 7-22 kW
  - Fast charging: Handled by external DC charger
- **Efficiency**: >95% at rated load
- **Charging Profile**: Constant current (CC) → Constant voltage (CV)

#### 4.4.3 Safety and Standards

- **Isolation**: Galvanic isolation per [IEC 61851-1](https://webstore.iec.ch/publication/6035)
- **Connector**: Type 2 (IEC 62196-2) or CCS Combo 2
- **Communication**: ISO 15118 for smart charging
- **Ground Fault Protection**: Residual current detection (<30 mA)

---

## 5. Thermal Management

### 5.1 Cooling Requirements

- **Inverter Cooling**: Liquid cooling with 50/50 water-glycol mixture
- **Coolant Flow Rate**: 10-30 L/min (depending on power level)
- **Coolant Temperature**: 45-65°C operating range
- **Heat Exchanger**: Air-to-liquid with electric fan
- **BMS Cooling**: Air cooling or shared liquid cooling loop
- **Ambient Operating Range**: -30°C to +50°C

### 5.2 Thermal Management Strategy

- **Temperature Sensors**: NTC thermistors on critical components
- **Fan Control**: Variable-speed fans based on coolant temperature
- **Derating**: Automatic power reduction if temperature limits approached
- **Preheating**: Battery heating in cold weather (<0°C)
- **Thermal Interface Material**: High-conductivity TIM for semiconductors

---

## 6. Control and Communication

### 6.1 Vehicle Control Unit (VCU)

- **Function**: Supervisory control of all power electronics
- **Processor**: Automotive-grade microcontroller (e.g., Infineon AURIX, NXP S32)
- **Communication**: CAN bus (primary), Ethernet (diagnostics)
- **Safety**: [ISO 26262](https://www.iso.org/standard/68383.html) ASIL-B or higher
- **Real-Time OS**: QNX, FreeRTOS, or similar

### 6.2 Communication Protocols

- **CAN Bus**: [CAN 2.0B](https://www.can-cia.org/) or CAN FD
  - Traction inverter ↔ VCU
  - BMS ↔ VCU
  - Auxiliary systems ↔ VCU
- **Ethernet**: Diagnostics, firmware updates, telematics
- **Charging Communication**: ISO 15118 (PLC over CCS)

### 6.3 Diagnostics

- **On-Board Diagnostics (OBD)**: Fault code storage and retrieval
- **Telematics**: Real-time data transmission to fleet management
- **Logging**: Event and data logging for troubleshooting
- **Remote Diagnostics**: Over-the-air diagnostics and updates

---

## 7. Safety and Protection

### 7.1 Electrical Safety

- **High-Voltage Interlock Loop (HVIL)**: Continuous monitoring of HV connections
- **Insulation Monitoring**: Resistance to ground >100 Ω/V
- **Contactor Control**: Pyro-fuse or mechanical contactors for emergency disconnect
- **Pre-charge Circuit**: Inrush current limiting during power-up
- **Discharge Resistor**: Capacitor discharge after shutdown (<60s to <60V)

### 7.2 Functional Safety

- **Redundancy**: Dual-channel safety-critical measurements
- **Watchdog Timers**: Monitor controller operation
- **Safe State**: Defined safe state on fault detection
- **Compliance**: [ISO 26262](https://www.iso.org/standard/68383.html) – Functional safety of road vehicles

### 7.3 EMC / EMI

- **Conducted Emissions**: [CISPR 25](https://webstore.iec.ch/publication/59037) Class 5
- **Radiated Emissions**: CISPR 25 Class 5
- **Immunity**: [ISO 11452](https://www.iso.org/standard/75428.html) series
- **ESD Protection**: [IEC 61000-4-2](https://webstore.iec.ch/publication/4219) Level 4
- **Shielding**: HV cables shielded and properly grounded

---

## 8. Standards and Compliance

### 8.1 Electric Vehicle Standards

- [ISO 6469](https://www.iso.org/standard/77165.html) – Electric road vehicles - Safety specifications
- [IEC 61851](https://webstore.iec.ch/publication/6035) – Electric vehicle conductive charging system
- [ISO 15118](https://www.iso.org/standard/55366.html) – Vehicle-to-grid communication

### 8.2 Functional Safety

- [ISO 26262](https://www.iso.org/standard/68383.html) – Road vehicles - Functional safety
- [IEC 61508](https://webstore.iec.ch/publication/5515) – Functional safety of electrical/electronic systems

### 8.3 EMC Standards

- [CISPR 25](https://webstore.iec.ch/publication/59037) – Radio disturbance characteristics for protection of receivers
- [ISO 11452](https://www.iso.org/standard/75428.html) – Road vehicles - Component test methods for electrical disturbances

### 8.4 Battery Standards

- [UL 2580](https://www.ul.com/resources/ul-2580-standard-safety) – Batteries for use in electric vehicles
- [IEC 62619](https://webstore.iec.ch/publication/7299) – Safety requirements for secondary lithium cells

---

## 9. Performance Monitoring

### 9.1 Key Performance Indicators

- **System Efficiency**: Overall efficiency from battery to wheel/load
- **Power Electronics Efficiency**: Inverter and converter efficiency
- **Thermal Performance**: Maximum junction temperatures
- **Reliability**: MTBF for power electronics components
- **Fault Rate**: Faults per 1,000 operating hours

### 9.2 Data Logging

- **Energy Flow**: kWh consumed by each subsystem
- **Temperature Profiles**: Thermal performance over time
- **Fault Codes**: DTC (Diagnostic Trouble Codes) logging
- **Performance Metrics**: Efficiency maps at various loads

---

## 10. Cross-References

### 10.1 Internal (ATA 85)

- [85-70-01-A-003_Battery_Systems.md](./ASSETS/85-70-01-A-003_Battery_Systems.md) – Battery system design
- [85-70-01-A-004_Charging_Integration.md](./ASSETS/85-70-01-A-004_Charging_Integration.md) – Charging integration
- [85-70-04](../85-70-04_Charging_Infrastructure/) – Charging infrastructure
- [85-70-05](../85-70-05_Motor_and_Drivetrain/) – Motor specifications
- [85-70-06-002_Battery_Health_Monitoring.md](../85-70-06_Maintenance_and_Diagnostics/85-70-06-002_Battery_Health_Monitoring.md) – BMS diagnostics

### 10.2 External (Other ATAs)

- [ATA 85-40 – Software](../../85-40_Software/) – Control software and algorithms
- [ATA 95 – Digital Product Passport](../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/) – Component traceability

---

## 11. Status and Next Steps

- **Current Phase**: Requirements specification
- **Next Phase**: Component selection and supplier qualification
- **Dependencies**: Battery pack design, motor selection, charging infrastructure standards

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22.

---

**End of Document**
