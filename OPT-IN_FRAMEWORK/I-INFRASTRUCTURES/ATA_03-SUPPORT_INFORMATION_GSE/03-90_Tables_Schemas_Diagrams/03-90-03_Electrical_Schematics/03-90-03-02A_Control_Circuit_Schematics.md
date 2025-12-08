# 03-90-03-02A - Control Circuit Schematics

## 1. Purpose

This document establishes standards for control circuit schematics for Ground Support Equipment, covering control logic, interlocks, and automation systems for safe and efficient hydrogen GSE operations.

## 2. Scope

This specification covers control circuit schematics for:
- Programmable Logic Controller (PLC) based control systems
- Relay logic and hardwired interlocks
- Safety instrumented systems (SIS)
- Human-Machine Interface (HMI) integration
- Sequence of operations diagrams
- Interlock matrices

## 3. Applicable Documents

- [IEC 61131-3](https://www.iec.ch/) - Programmable Controllers Programming Languages
- [ISA 5.1](https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa5-1) - Instrumentation Symbols and Identification
- [IEC 61508](https://www.iec.ch/) - Functional Safety of Electrical/Electronic Systems
- [ISA 84](https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa84) - Safety Instrumented Systems
- [NEMA ICS](https://www.nema.org/) - Industrial Control and Systems Standards
- [IEEE 315](https://standards.ieee.org/standard/315-1975.html) - Graphic Symbols for Electrical Diagrams

## 4. Documentation Description

### 4.1 Overview

Control circuit schematics define the logic and sequence for automated and manual control of GSE systems, ensuring safe and repeatable operations.

### 4.2 Format and Structure

| Element | Format | Standard |
|---------|--------|----------|
| Ladder Logic | IEC 61131-3 LD | PLC programming standard |
| Function Block Diagrams | IEC 61131-3 FBD | Graphical programming |
| Relay Logic | Ladder diagram format | NEMA/IEEE convention |
| State Machines | State transition diagrams | UML or ISA |
| Interlock Matrix | Tabular format | Permissive/inhibit table |

### 4.3 Content Requirements

#### 4.3.1 Control System Architecture

**PLC-Based Control:**

| Component | Specification | Notes |
|-----------|---------------|-------|
| PLC Type | Modular rack-based or compact | Suitable for industrial environment |
| CPU | TBD model with required I/O capacity | Redundant for critical applications |
| I/O Modules | Digital input, Digital output, Analog input, Analog output | Isolated, explosion-proof if required |
| Communication | Ethernet/IP, Profibus, Modbus TCP | Industry-standard protocols |
| Power Supply | Redundant 24 VDC supplies | N+1 redundancy |
| Programming Software | Manufacturer-specific (e.g., TIA Portal, RSLogix) | Version controlled |

**Safety PLC (if SIL-rated):**
- Dedicated safety controller separate from process PLC
- Certified to IEC 61508 SIL 2 or SIL 3
- Hardwired E-stop and critical interlocks

#### 4.3.2 Input/Output (I/O) List

**Digital Inputs (DI):**

| Tag | Description | Device | Location | Normal State |
|-----|-------------|--------|----------|--------------|
| DI-001 | LH2 Tank High Level | Level Switch | GSE-LH2-0001 | Open |
| DI-002 | Transfer Pump Running | Aux Contact | M-101 | Open |
| DI-003 | ESV-001 Closed Position | Limit Switch | VXV-001 | Closed |
| ... | ... | ... | ... | ... |

**Digital Outputs (DO):**

| Tag | Description | Device | Location | Normal State |
|-----|-------------|--------|----------|--------------|
| DO-001 | Start LH2 Pump | Motor Starter | MCC-01 | De-energized |
| DO-002 | Open ESV-001 | Solenoid Valve | VXV-001 | De-energized (closed) |
| DO-003 | High H2 Alarm Horn | Horn | Control Room | De-energized |
| ... | ... | ... | ... | ... |

**Analog Inputs (AI):**

| Tag | Description | Sensor Type | Range | Alarm Setpoints |
|-----|-------------|-------------|-------|-----------------|
| AI-001 | LH2 Tank Pressure | 4-20mA | 0-10 bar | High: 8 bar, High-High: 9 bar |
| AI-002 | LH2 Tank Level | 4-20mA | 0-100% | Low: 10%, High: 90% |
| AI-003 | H2 Concentration | 4-20mA | 0-100% LEL | High: 25% LEL, High-High: 40% LEL |
| ... | ... | ... | ... | ... |

**Analog Outputs (AO):**

| Tag | Description | Actuator Type | Range | Control Mode |
|-----|-------------|---------------|-------|--------------|
| AO-001 | LH2 Flow Control Valve | 4-20mA | 0-100% open | PID control |
| AO-002 | VFD Pump Speed | 4-20mA | 0-60 Hz | PID or manual |
| ... | ... | ... | ... | ... |

#### 4.3.3 Control Sequences

**LH2 Transfer Sequence Example:**

**Pre-Transfer Checks (Permissives):**
1. Source tank level > 20%
2. Receiver tank level < 80%
3. All H2 detectors operational and < 10% LEL
4. Fire detection system operational
5. ESVs in correct positions
6. Personnel authorized and ready

**Transfer Start Sequence:**
1. Open isolation valves (VBV-101, VBV-102)
2. Wait 5 seconds
3. Start transfer pump (M-101)
4. Ramp pump speed to setpoint (VFD control)
5. Monitor flow rate and adjust valve position (AO-001)
6. Monitor levels in source and receiver tanks

**Normal Shutdown Sequence:**
1. Ramp down pump speed to minimum
2. Stop pump (M-101)
3. Close isolation valves (VBV-101, VBV-102)
4. Log transfer quantity and time

**Emergency Shutdown Sequence:**
1. Stop pump immediately (M-101)
2. Close all ESVs (VXV-001, VXV-002, VXV-003)
3. Activate alarms and beacons
4. Vent system to safe pressure

#### 4.3.4 Interlock Matrix

**Interlock Table Example:**

| Equipment | Start Permissives | Running Interlocks (Trip Conditions) |
|-----------|-------------------|--------------------------------------|
| LH2 Pump M-101 | • Tank level > 20%<br>• ESV-001 open<br>• No high H2 alarm<br>• VFD ready | • Tank level < 5% (low-low)<br>• High H2 > 25% LEL<br>• Fire detected<br>• E-stop pressed<br>• ESV closed |
| GH2 Compressor M-102 | • Suction pressure > 2 bar<br>• Discharge pressure < 200 bar<br>• Oil level OK<br>• Cooling water flow OK | • Suction pressure < 1 bar<br>• Discharge pressure > 220 bar<br>• High vibration<br>• High bearing temperature<br>• Fire or high H2 |

#### 4.3.5 Alarm Management

**Alarm Priority Levels:**

| Priority | Description | Response Time | Typical Causes |
|----------|-------------|---------------|----------------|
| Critical | Immediate action required | < 1 minute | Fire, high H2, ESD activation |
| High | Prompt action required | < 5 minutes | Process deviation, equipment fault |
| Medium | Action required | < 15 minutes | Approaching limit, maintenance due |
| Low | Information only | When convenient | Normal events, status changes |

**Alarm Philosophy:**
- Alarms must be actionable (operator can respond)
- Avoid alarm floods (cascading alarms from single root cause)
- Shelving/acknowledgment: Critical alarms cannot be shelved
- Alarm log: All alarms logged with timestamp

#### 4.3.6 HMI (Human-Machine Interface) Integration

**HMI Screens:**
1. **Overview Screen**: System status, key parameters
2. **LH2 Storage Screen**: Tank levels, pressures, temperatures
3. **Transfer Operations Screen**: Flow control, pump status
4. **Safety Systems Screen**: H2 detection, fire detection, ESD status
5. **Alarm Summary Screen**: Active alarms, alarm history
6. **Trends Screen**: Historical data plots

**HMI Navigation:**
- Hierarchical structure (overview → detail)
- Consistent layout and color coding
- Context-sensitive help
- Operator authentication for control actions

#### 4.3.7 Communication Networks

**Control Network Architecture:**

| Network | Protocol | Purpose | Devices |
|---------|----------|---------|---------|
| Process Control | Ethernet/IP or Profibus | PLC to I/O modules | PLC, Remote I/O, VFDs |
| HMI/SCADA | Ethernet TCP/IP | HMI to PLC | HMI servers, workstations |
| Safety | Dedicated safety bus | Safety PLC to safety I/O | Safety PLC, E-stops, safety sensors |
| Enterprise | Ethernet TCP/IP | Data to MES/ERP | Historians, databases |

**Cybersecurity:**
- Firewalls between control and enterprise networks
- VLANs for segmentation
- Access control (authentication, authorization)
- Antivirus on HMI/SCADA servers
- Regular security audits

#### 4.3.8 Control Logic Documentation

**Ladder Logic Example (Simplified):**

```
---| |---[ ]---( )---    Start LH2 Pump
   DI-Start  Interlocks  DO-Pump

Where Interlocks =
   Tank Level > 20% AND
   No High H2 Alarm AND
   ESV Open AND
   NOT (E-Stop)
```

**Function Block Diagram (FBD) Example:**

```
[AI-001]-->[Scale]-->[PID]-->[AO-001]
 Tank       0-10bar   Flow     Flow
 Pressure   to 0-100% Controller Valve
                      SP=Setpoint
```

#### 4.3.9 Control Panel Layout

**Typical Control Panel Contents:**
- PLC rack with CPU and I/O modules
- Power supplies (redundant)
- Circuit breakers/fuses for I/O protection
- Terminal blocks for field wiring
- Ethernet switches
- UPS (for critical panels)
- Cooling fan or A/C (if required)
- Panel lights and status indicators

**Panel Enclosure:**
- NEMA 4X (outdoor, corrosive) or NEMA 1/12 (indoor)
- Pressurized (Ex p) if in hazardous area
- Adequate ventilation/cooling
- Cable glands for incoming/outgoing cables

### 4.4 Testing and Commissioning

**Factory Acceptance Test (FAT):**
- Control logic simulation
- I/O verification
- HMI functionality
- Alarm testing
- Sequence testing (dry run)

**Site Acceptance Test (SAT):**
- End-to-end testing with actual field devices
- Interlock verification
- Safety system testing (ESD, E-stops)
- Performance verification

**Loop Checks:**
- Each I/O point tested individually
- Sensor calibration verified
- Actuator stroke testing
- Signal integrity (4-20mA, Modbus communication)

## 5. Cross-References

- Related ATA Chapters: ATA 24 (Electrical Power), ATA 31 (Instruments)
- Parent Document: [03-90_Tables_Schemas_Diagrams](../README.md)
- Related Documents:
  - [03-90-03-01A Power Distribution Diagrams](./03-90-03-01A_Power_Distribution_Diagrams.md)
  - [03-90-03-03A Wiring Diagrams](./03-90-03-03A_Wiring_Diagrams.md)
  - [03-90-02-04A H2 Safety Schematics](../03-90-02_H2_GSE_Schematics/03-90-02-04A_H2_Safety_Schematics.md)

## 6. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Controls Engineering | Initial release |

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-08.

---
