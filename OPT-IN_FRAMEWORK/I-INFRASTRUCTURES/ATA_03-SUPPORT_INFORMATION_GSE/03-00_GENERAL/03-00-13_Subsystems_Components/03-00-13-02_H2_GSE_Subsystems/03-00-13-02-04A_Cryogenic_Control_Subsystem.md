---
Title: "Cryogenic Control Subsystem — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-13-02-04A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Detailed specifications for the Cryogenic Control Subsystem managing temperature, pressure, and boil-off gas in LH₂ GSE for the AMPEL360 BWB H₂ Hy-E aircraft."
Keywords: ["ATA 03","GSE","Cryogenic Control","LH2","Temperature Control","Pressure Control"]
Compliance:
  - "ATA iSpec 2200"
  - "SAE AS6968"
  - "ISO 19880-8"
  - "ASME B31.12"
Links:
  Parent: "../"
  Siblings:
    - "03-00-13-02-01A_LH2_Storage_Subsystem.md"
    - "03-00-13-02-02A_LH2_Transfer_Subsystem.md"
    - "03-00-13-02-03A_H2_Safety_Subsystem.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial cryogenic control subsystem specification" }
---

# Cryogenic Control Subsystem — ATA 03 Support Information GSE

## 1. Purpose

This document specifies the **Cryogenic Control Subsystem** for ground support equipment serving the AMPEL360 BWB H₂ Hy-E aircraft. The subsystem maintains optimal cryogenic conditions for liquid hydrogen storage and transfer by controlling temperature (20-22 K), pressure (1-5 bar), managing boil-off gas, and preventing excessive heat ingress.

## 2. Scope

### 2.1 Coverage

The Cryogenic Control Subsystem encompasses:

1. **Temperature Control Unit**
   - Cryocooler for active cooling (if required)
   - Temperature monitoring and control
   - Heat load management
   - Setpoint: -253°C ± 2°C (20 K ± 2 K)

2. **Pressure Control Unit**
   - Pressure regulation valves
   - Pressure relief and venting
   - Pressure monitoring and alarms
   - Operating range: 1-5 bar absolute

3. **Boil-Off Gas (BOG) Recovery**
   - BOG collection and compression
   - Optional reliquefaction
   - Vent stack discharge (if not recovered)
   - Minimize hydrogen losses

4. **Cryogenic Sensors Array**
   - RTD temperature sensors (Pt-100, 20-300 K)
   - Cryogenic pressure transmitters (0-10 bar)
   - Level sensors (capacitance, differential pressure)
   - Data acquisition system

5. **Control System PLC**
   - Programmable Logic Controller
   - PID control loops for temperature and pressure
   - Data logging and trending
   - Integration with HMI and SCADA

### 2.2 Out of Scope

- LH₂ storage tank structure (see [03-00-13-02-01A](./03-00-13-02-01A_LH2_Storage_Subsystem.md))
- LH₂ transfer equipment (see [03-00-13-02-02A](./03-00-13-02-02A_LH2_Transfer_Subsystem.md))
- Safety interlocks (see [03-00-13-02-03A](./03-00-13-02-03A_H2_Safety_Subsystem.md))

## 3. Applicable Documents

| Standard | Application | Link |
|----------|-------------|------|
| **[SAE AS6968](https://www.sae.org/standards/content/as6968/)** | Hydrogen Aircraft Refueling | Cryogenic control requirements |
| **[ISO 19880-8](https://www.iso.org/standard/71940.html)** | Gaseous Hydrogen Fueling Stations | Operational requirements |
| **[ASME B31.12](https://www.asme.org/codes-standards/find-codes-standards/b31-12-hydrogen-piping-pipelines)** | Hydrogen Piping and Pipelines | Cryogenic system design |
| **[IEC 61131-3](https://www.iec.ch/)** | Programmable Logic Controllers | PLC programming standards |

## 4. Subsystem Description

### 4.1 Overview

The Cryogenic Control Subsystem maintains LH₂ at the required temperature and pressure through continuous monitoring, automated control, and boil-off gas management. The system uses a PLC-based control architecture with PID loops, ensuring stable cryogenic conditions and minimizing hydrogen losses.

```
┌──────────────────────────────────────────────────────────────┐
│         Cryogenic Control Subsystem Architecture              │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌─────────────────────────────────────────────────────┐     │
│  │           LH₂ Storage Tank                           │     │
│  │  - Primary Tank: 10,000 kg, -253°C, 1-5 bar         │     │
│  │  - Backup Tank: 5,000 kg, -253°C, 1-5 bar           │     │
│  └──────────────┬──────────────────────┬────────────────┘     │
│                 │                      │                      │
│          Temperature              Pressure                    │
│           Sensors (n=6)           Sensors (n=4)              │
│                 │                      │                      │
│                 ▼                      ▼                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         Cryogenic Control PLC                         │   │
│  │  - Input: T, P, Level sensors                        │   │
│  │  - Control: PID loops for T and P                    │   │
│  │  - Output: Valve positions, alarms                   │   │
│  │  - Data Logging: 1 Hz sampling                       │   │
│  └──────────────┬──────────────────────┬────────────────┘   │
│                 │                      │                      │
│                 ▼                      ▼                      │
│  ┌─────────────────────┐   ┌─────────────────────┐          │
│  │  Temperature         │   │  Pressure            │          │
│  │  Control Unit        │   │  Control Unit        │          │
│  │  - Cryocooler       │   │  - Pressure Reg Valve│          │
│  │    (if required)     │   │  - Relief Valves     │          │
│  │  - Vacuum Monitoring │   │  - Vent Control      │          │
│  │  - Heat Load Calc    │   │  - BOG Management    │          │
│  └─────────────────────┘   └─────────────────────┘          │
│                                      │                        │
│                                      ▼                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │       Boil-Off Gas (BOG) Recovery                     │   │
│  │  - BOG Collection Manifold                           │   │
│  │  - Compression (if recovering)                       │   │
│  │  - Reliquefaction (optional)                         │   │
│  │  - Vent Stack (if not recovering)                    │   │
│  │  - Flow Metering                                     │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                                │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         HMI / SCADA Integration                       │   │
│  │  - Real-time T, P, Level display                     │   │
│  │  - Trend charts (historical data)                    │   │
│  │  - Alarm management                                  │   │
│  │  - Operator control (setpoints, manual overrides)    │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

### 4.2 Specifications

#### 4.2.1 Temperature Control Unit

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Target Temperature** | -253°C ± 2°C (20 K ± 2 K) | Liquid hydrogen saturation |
| **Control Method** | Pressure regulation (passive) + optional cryocooler (active) | Passive primary, active if needed |
| **Temperature Sensors** | RTD Pt-100, 4-wire, Class A | 6 sensors per tank |
| **Sensor Range** | 20-300 K (-253°C to +27°C) | Covers all conditions |
| **Sensor Accuracy** | ±0.5 K @ 20 K | High precision |
| **Heat Ingress (Target)** | < 0.5 W/m² | Via vacuum insulation |
| **Cryocooler Capacity** | 100 W @ 20 K (if installed) | Gifford-McMahon or Pulse Tube |
| **Cryocooler Power** | 5 kW electrical input | For 100 W cooling |

#### 4.2.2 Pressure Control Unit

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Operating Pressure** | 1-5 bar absolute | Normal range |
| **Pressure Setpoint** | 3.0 bar (adjustable) | PLC-controlled |
| **Pressure Control** | Automated pressure regulating valve | Maintain setpoint |
| **Pressure Sensors** | Cryogenic transmitters, 0-10 bar | 4 sensors (redundant) |
| **Sensor Accuracy** | ±0.1% full scale (±0.01 bar) | High accuracy |
| **Relief Valve Set Pressure** | 6.0 bar | Primary relief |
| **Burst Disc Pressure** | 8.0 bar | Secondary relief |
| **Pressure Ramp Rate Limit** | 0.5 bar/minute max | Prevent thermal shock |

#### 4.2.3 Boil-Off Gas (BOG) Recovery

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **BOG Rate (Normal)** | 0.1% per day (10 kg/day for 10,000 kg tank) | With good insulation |
| **BOG Rate (Maximum)** | 1% per day (100 kg/day) | Degraded insulation or high usage |
| **BOG Collection** | Manifold from tank vent | Before relief valve |
| **BOG Compression** | 2-stage compressor, 1 bar to 20 bar | For storage or use |
| **BOG Flow Meter** | Thermal mass flow meter, 0-10 kg/hr | Measure losses |
| **Reliquefaction** | Optional, small-scale liquefier | Reduce losses |
| **Vent Option** | Vent stack, 10m high | If not recovering BOG |

#### 4.2.4 Cryogenic Sensors Array

**Temperature Sensors** (6 per tank):

| Location | Type | Range | Accuracy | Part Number |
|----------|------|-------|----------|-------------|
| Tank liquid space | RTD Pt-100 | 20-300 K | ±0.5 K @ 20 K | GSE-H2-04-001-A |
| Tank vapor space | RTD Pt-100 | 20-300 K | ±0.5 K @ 20 K | GSE-H2-04-001-A |
| Inlet line | RTD Pt-100 | 20-300 K | ±0.5 K @ 20 K | GSE-H2-04-001-A |
| Outlet line | RTD Pt-100 | 20-300 K | ±0.5 K @ 20 K | GSE-H2-04-001-A |
| Vacuum annulus | RTD Pt-100 | 20-300 K | ±1 K | GSE-H2-04-001-A |
| Ambient (outer shell) | RTD Pt-100 | 20-300 K | ±1 K | GSE-H2-04-001-A |

**Pressure Sensors** (4 per tank):

| Location | Type | Range | Accuracy | Part Number |
|----------|------|-------|----------|-------------|
| Tank (primary) | Cryogenic transmitter | 0-10 bar | ±0.01 bar | GSE-H2-04-002-A |
| Tank (backup) | Cryogenic transmitter | 0-10 bar | ±0.01 bar | GSE-H2-04-002-A |
| Inlet line | Cryogenic transmitter | 0-10 bar | ±0.01 bar | GSE-H2-04-002-A |
| Outlet line | Cryogenic transmitter | 0-10 bar | ±0.01 bar | GSE-H2-04-002-A |

**Level Sensors** (2 per tank, redundant):

| Type | Range | Accuracy | Part Number |
|------|-------|----------|-------------|
| Capacitance probe | 0-100% | ±1% | GSE-H2-04-003-A |
| Differential pressure | 0-100% | ±2% | GSE-H2-04-004-A |

#### 4.2.5 Control System PLC

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **PLC Model** | Siemens S7-1500 or equivalent | Industrial-grade |
| **I/O Capacity** | 64 analog inputs, 32 analog outputs, 128 digital I/O | Expandable |
| **Control Loops** | 8 PID loops minimum | Temperature, pressure control |
| **Scan Rate** | 10 ms | Fast response |
| **Data Logging** | 1 Hz sampling, local + remote storage | Minimum 1 year retention |
| **Communication** | Ethernet/IP, Modbus TCP, OPC UA | Standard protocols |
| **Redundancy** | Hot-standby option (optional) | High availability |
| **Programming** | IEC 61131-3 (Ladder, ST, FBD) | Standardized |

### 4.3 Part Number Information

| Component | Part Number | Description | Supplier | Interchangeability |
|-----------|-------------|-------------|----------|-------------------|
| Temperature Sensor (RTD) | GSE-H2-04-001-A | Pt-100, 4-wire, 20-300 K | Lake Shore Cryotronics | PT-103 series |
| Pressure Transmitter | GSE-H2-04-002-A | Cryogenic, 0-10 bar, 4-20 mA | Rosemount | 3051C |
| Level Sensor (Capacitance) | GSE-H2-04-003-A | 0-100%, cryogenic | Endress+Hauser | FMI51 |
| Level Sensor (ΔP) | GSE-H2-04-004-A | 0-100%, differential pressure | Rosemount | 3051CD |
| Pressure Regulating Valve | GSE-H2-04-005-A | DN 50, cryogenic, pneumatic | Samson AG | Type 3241 |
| BOG Compressor | GSE-H2-04-006-A | 2-stage, 0-20 bar, 10 kg/hr | Howden | Custom |
| Cryocooler (optional) | GSE-H2-04-007-A | 100 W @ 20 K, Gifford-McMahon | Sumitomo | RDK-101D |
| PLC System | GSE-H2-04-008-A | Siemens S7-1500, I/O modules | Siemens | S7-1500 series |
| BOG Flow Meter | GSE-H2-04-009-A | Thermal mass, 0-10 kg/hr | Sierra Instruments | QuadraTherm 640i |

See [03-00-13-03_GSE_Part_Number_Registry](../03-00-13-03_GSE_Part_Number_Registry/) for complete PNR.

## 5. Spare Parts Information

### 5.1 Critical Spare Parts

| Part Number | Description | Criticality | Lead Time | Min Stock |
|-------------|-------------|-------------|-----------|-----------|
| GSE-H2-04-001-A | Temperature Sensor (RTD) | **Essential** | 4 weeks | 3 units |
| GSE-H2-04-002-A | Pressure Transmitter | **Essential** | 4 weeks | 2 units |
| GSE-H2-04-003-A | Level Sensor (Capacitance) | **Essential** | 6 weeks | 1 unit |
| GSE-H2-04-005-A | Pressure Regulating Valve | **Critical** | 10 weeks | 1 unit |
| GSE-H2-04-008-A | PLC System | **Critical** | 12 weeks | 1 unit (or modules) |
| GSE-H2-04-010-A | Sensor Cable Assemblies | **Standard** | 2 weeks | 5 assemblies |

See [03-00-13-04_GSE_Spare_Parts_Management](../03-00-13-04_GSE_Spare_Parts_Management/) for complete spare parts strategy.

## 6. Control Algorithms

### 6.1 Temperature Control

**PID Control Loop**:

- **Setpoint**: -253°C (20 K)
- **Process Variable**: Average of 2 liquid space RTDs
- **Control Output**: Cryocooler power (if installed) or BOG vent rate
- **PID Tuning**: Kp = 5, Ki = 0.1, Kd = 1 (initial, tune on-site)
- **Control Range**: ±5 K
- **Alarm**: Temperature > -248°C (25 K) or < -258°C (15 K)

### 6.2 Pressure Control

**PID Control Loop**:

- **Setpoint**: 3.0 bar (adjustable 1-5 bar)
- **Process Variable**: Tank pressure (primary transmitter)
- **Control Output**: Pressure regulating valve position (0-100%)
- **PID Tuning**: Kp = 2, Ki = 0.5, Kd = 0.5 (initial, tune on-site)
- **Deadband**: ±0.1 bar (prevent hunting)
- **Alarm**: Pressure < 1.2 bar or > 4.5 bar
- **Trip**: Pressure < 1.0 bar or > 5.5 bar

### 6.3 BOG Management

**Logic**:

1. **Normal BOG Rate (< 0.5% per day)**:
   - Route BOG to recovery compressor
   - Compress to 20 bar for storage or use
   - Monitor BOG flow rate
2. **High BOG Rate (0.5-1% per day)**:
   - Alarm to operator
   - Investigate heat ingress source (vacuum loss?)
   - Continue recovery if compressor capacity allows
3. **Excessive BOG Rate (> 1% per day)**:
   - Alarm (high priority)
   - Vent to atmosphere via vent stack if compressor capacity exceeded
   - Emergency shutdown of refueling operations if BOG rate continues to rise

## 7. Operational Parameters

### 7.1 Normal Operation

| Parameter | Operating Range | Alarm Threshold | Trip Threshold |
|-----------|-----------------|-----------------|----------------|
| Tank Temperature (Liquid) | -255°C to -251°C (18-22 K) | < -258°C or > -248°C | < -260°C or > -245°C |
| Tank Pressure | 1.5-4.0 bar | < 1.2 or > 4.5 bar | < 1.0 or > 5.5 bar |
| BOG Rate | < 0.5% per day | > 0.5% per day | > 1% per day |
| Vacuum Pressure (MLI) | < 10⁻⁵ mbar | > 10⁻³ mbar | > 10⁻² mbar |

## 8. Maintenance Requirements

### 8.1 Routine Inspections

| Inspection | Frequency | Procedure |
|------------|-----------|-----------|
| Sensor reading verification | Daily | Compare multiple sensors, check for drift |
| PLC status check | Daily | Check for alarms, communication faults |
| BOG rate calculation | Daily | Compare to baseline, trend over time |
| Vacuum pressure check | Weekly | Record vacuum level, compare to baseline |
| Cryocooler performance (if installed) | Weekly | Check cooling power, vibration, temperature |

### 8.2 Preventive Maintenance

| Task | Frequency | Estimated Duration |
|------|-----------|-------------------|
| Sensor calibration (T, P) | Annually | 2 hours per sensor (in-situ or send to lab) |
| PLC backup and software update | Annually | 4 hours |
| Cryocooler maintenance (if installed) | Annually or 8000 hours | Per manufacturer (e.g., compressor overhaul) |
| Pressure regulating valve overhaul | 3 years | 8 hours |
| Vacuum pump-down (if needed) | 5 years or if vacuum degraded | 24-48 hours |

## 9. Cross-References

### 9.1 Related ATA Chapters

- [ATA 02 — Operations Information](../../../../../ATA_02-OPERATIONS_INFORMATION/) — Ground operations
- [ATA 85 — Infrastructure Interface Standards](../../../../../ATA_85-INFRASTRUCTURE_INTERFACE_STANDARDS/) — Infrastructure integration

### 9.2 Related Documents

- [03-00-13-01-01A_GSE_Subsystem_Overview](../03-00-13-01_GSE_Subsystem_Architecture/03-00-13-01-01A_GSE_Subsystem_Overview.md)
- [03-00-13-02-01A_LH2_Storage_Subsystem](./03-00-13-02-01A_LH2_Storage_Subsystem.md)
- [03-00-13-02-02A_LH2_Transfer_Subsystem](./03-00-13-02-02A_LH2_Transfer_Subsystem.md)
- [03-00-13-02-03A_H2_Safety_Subsystem](./03-00-13-02-03A_H2_Safety_Subsystem.md)
- [03-00-13-06_GSE_Control_Subsystems](../03-00-13-06_GSE_Control_Subsystems/) — General control subsystems
- [03-00-06_Engineering](../../03-00-06_Engineering/) — Engineering standards

### 9.3 Parent Document

- [03-00-13_Subsystems_Components](../) — Top-level subsystems directory

## 10. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-13-02-04A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 Ground Support Equipment WG

---
