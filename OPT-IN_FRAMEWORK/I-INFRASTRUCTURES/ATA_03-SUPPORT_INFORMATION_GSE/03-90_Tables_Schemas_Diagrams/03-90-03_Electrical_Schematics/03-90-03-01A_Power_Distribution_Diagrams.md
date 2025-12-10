# 03-90-03-01A - Power Distribution Diagrams

## 1. Purpose

This document establishes standards for electrical power distribution diagrams for Ground Support Equipment, covering primary power supply, distribution systems, and load connections for hydrogen GSE operations.

## 2. Scope

This specification covers power distribution diagrams for:
- Main electrical service and transformers
- Distribution panels and switchgear
- Motor control centers (MCC)
- Power to H2 system equipment (pumps, compressors, controls)
- Emergency and backup power systems
- Grounding and bonding systems

## 3. Applicable Documents

- [IEEE 315](https://standards.ieee.org/standard/315-1975.html) - Graphic Symbols for Electrical and Electronics Diagrams
- [NFPA 70](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=70) - National Electrical Code (NEC)
- [IEC 60617](https://www.iec.ch/) - Graphical Symbols for Diagrams
- [IEEE 242](https://standards.ieee.org/) - Protection and Coordination of Industrial Power Systems
- [IEC 60079-14](https://www.iec.ch/) - Electrical Installations in Hazardous Areas
- [NFPA 2](https://www.nfpa.org/) - Hydrogen Technologies Code (Electrical Requirements)

## 4. Documentation Description

### 4.1 Overview

Power distribution diagrams provide essential information for:
- System design and load analysis
- Equipment specification and procurement
- Installation and commissioning
- Operation and troubleshooting
- Maintenance and modifications
- Safety and compliance verification

### 4.2 Format and Structure

| Element | Format | Standard |
|---------|--------|----------|
| Single Line Diagrams | IEEE 315 symbols | One-line per phase representation |
| Three Line Diagrams | Three lines for 3-phase | Detailed phase representation |
| Load Schedule | Tabular format | Equipment list with ratings |
| Protective Device Coordination | Time-current curves | IEEE 242 |
| Hazardous Area Classification | Zone markings | IEC 60079, NEC Article 505/506 |

### 4.3 Content Requirements

#### 4.3.1 Main Service and Transformers

**Primary Service:**
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Voltage | 480V, 3-phase, 4-wire | Typical industrial |
| Frequency | 50/60 Hz | Regional standard |
| Service Capacity | TBD kVA | Based on load calculation |
| Main Breaker | TBD Ampere frame | Coordinated with utility |
| Short Circuit Rating | TBD kA | Fault current analysis |

**Step-Down Transformers (if required):**
- Primary voltage / Secondary voltage
- kVA rating
- Impedance (%)
- Vector group (Dyn11, etc.)
- Indoor/outdoor rating
- Temperature rise class

#### 4.3.2 Distribution Panel Configuration

**Main Distribution Panel (MDP):**

| Circuit | Load Description | Rating (A) | Breaker Type | Cable Size |
|---------|------------------|------------|--------------|------------|
| 1 | LH2 Transfer Pump | 100 | MCB, 3P | 3x25mm² + PE |
| 2 | GH2 Compressor | 150 | MCB, 3P | 3x50mm² + PE |
| 3 | Control Power Panel | 30 | MCB, 3P | 3x6mm² + PE |
| 4 | Lighting Panel | 20 | MCB, 1P | 1x4mm² + PE |
| 5 | HVAC for Control Room | 40 | MCB, 3P | 3x10mm² + PE |
| ... | ... | ... | ... | ... |

**Sub-Panels:**
- Control Power Panel (CPP) - 120V/240V for instrumentation
- Lighting and Small Power Panel (LSPP)
- Emergency Power Panel (EPP)
- Uninterruptible Power Supply (UPS) Panel

#### 4.3.3 Motor Loads

**Major Motors:**

| Motor Tag | Equipment | HP (kW) | Voltage | FLA (A) | Starting Method | Protection |
|-----------|-----------|---------|---------|---------|-----------------|------------|
| M-101 | LH2 Pump | 50 (37) | 480V 3φ | 52 | VFD | OL, SC, GF |
| M-102 | GH2 Compressor | 100 (75) | 480V 3φ | 104 | Soft Start | OL, SC, GF |
| M-103 | Cooling Fan | 5 (3.7) | 480V 3φ | 5.2 | DOL | OL, SC |
| ... | ... | ... | ... | ... | ... | ... |

**Motor Protection:**
- **OL**: Overload protection (thermal or electronic)
- **SC**: Short circuit protection (circuit breaker or fuses)
- **GF**: Ground fault protection (residual current)
- **UV**: Under-voltage protection
- **PH**: Phase loss protection

#### 4.3.4 Hazardous Area Electrical Design

**Zone Classification per IEC 60079-10-1:**

| Zone | Description | Equipment Rating |
|------|-------------|------------------|
| Zone 0 | H2 present continuously | Ex ia (Intrinsically Safe) |
| Zone 1 | H2 likely in normal ops | Ex d, Ex e, Ex ia |
| Zone 2 | H2 unlikely or brief | Suitable for Zone 2 or better |
| Non-Hazardous | No H2 risk | Standard industrial |

**Electrical Equipment in Hazardous Areas:**
- Motors: Explosion-proof or increased safety (Ex d, Ex e)
- Control panels: Pressurized (Ex p) or explosion-proof
- Lighting: Explosion-proof fixtures
- Instrumentation: Intrinsically safe (Ex ia/ib)
- Cable glands: Certified for zone
- Bonding: All equipment earthed

#### 4.3.5 Variable Frequency Drives (VFD)

**VFD Applications:**
- LH2 pump speed control
- Compressor capacity control
- Cooling fan speed control

**VFD Specifications:**
| Parameter | Specification |
|-----------|---------------|
| Input Voltage | 480V, 3-phase |
| Output Voltage | 0-480V variable |
| Frequency Range | 0-60 Hz |
| Control Mode | V/Hz, Vector, or Flux Vector |
| Enclosure | NEMA 4X (outdoor/corrosive) or NEMA 1 (indoor) |
| EMI/RFI Filtering | Category C3 (industrial) |
| Communication | Modbus RTU/TCP, Profibus, EtherNet/IP |

**VFD Protection Features:**
- Input: Fuses or breaker, line reactor
- Output: Motor overload, ground fault
- VFD: Overvoltage, undervoltage, overcurrent, overtemperature

#### 4.3.6 Control Power Distribution

**24 VDC Control Power:**
- Primary control voltage for instrumentation
- Redundant power supplies (N+1)
- Battery backup for critical control (UPS)
- Distribution via fused terminal blocks

**120 VAC Control Power:**
- Solenoid valves
- Indicator lights
- Panel lighting
- Small instruments
- Isolation transformer from 480V or 240V

#### 4.3.7 Emergency and Backup Power

**Emergency Power Scenarios:**
- Utility power loss
- Critical load identification
- Automatic transfer switch (ATS)
- Emergency generator or battery system

**Critical Loads (must remain powered):**
- H2 gas detection system
- Emergency shutdown (ESD) system
- Emergency lighting
- Fire detection and alarm
- Control room power
- UPS for control systems

**Backup Generator (if used):**
- Capacity: Based on critical loads
- Start time: < 10 seconds
- Fuel: Diesel (typical)
- Automatic start on power loss
- Exercised weekly

**Uninterruptible Power Supply (UPS):**
- Capacity: Control system loads + 30% margin
- Runtime: 30-60 minutes (to allow shutdown or generator start)
- Battery type: VRLA or Lithium-ion
- Topology: Online double-conversion (preferred)

#### 4.3.8 Grounding and Bonding

**Grounding System:**

| Component | Grounding Method | Notes |
|-----------|------------------|-------|
| Main Service | Ground rod(s) + ground ring | Per NEC 250 |
| Equipment | Green wire or PE conductor | All metal parts |
| LH2/GH2 Equipment | Bonded to ground | Prevent static buildup |
| Piping | Bonding jumpers across flanges | Continuous path to ground |
| Control Panels | Isolated or common ground bar | Per design |
| Instrumentation | Shielded cable grounding | One end grounded (typical) |

**Grounding Resistance:**
- Target: < 5 Ω (industrial standard)
- < 1 Ω preferred for sensitive electronics
- Testing: Annual with ground resistance tester

**Lightning Protection:**
- Lightning rods/air terminals on structures
- Down conductors to ground system
- Surge protection devices (SPD) on power distribution

### 4.4 Single Line Diagram (SLD) Requirements

**Diagram Must Show:**
1. Utility service connection point
2. Main circuit breaker/disconnect
3. Service transformer(s)
4. Main distribution panel (MDP)
5. Feeder breakers to sub-panels
6. Sub-panels and load centers
7. Major motor loads (directly shown or referenced)
8. Protective devices (breakers, fuses) with ratings
9. Cable sizes and lengths (major feeders)
10. Grounding connections
11. Emergency/backup power connections

**Annotations:**
- Voltage levels at each point
- Current ratings (breaker, cable)
- Short circuit ratings
- Protective device coordination reference
- Equipment location (Zone classification)

### 4.5 Load Calculation and Demand Factor

**Connected Load:**
- Sum of all equipment ratings (kW or kVA)

**Demand Load:**
- Connected load × Demand factor
- Demand factor: 0.6-0.8 typical (not all loads run simultaneously)

**Load Growth:**
- Spare capacity: 20-30% for future expansion
- Spare breaker positions in panels

**Power Factor:**
- Target: > 0.95
- Correction: Capacitor banks if needed (not typical in H2 GSE)

### 4.6 Protective Device Coordination

**Coordination Study:**
- Time-current curves (TCC) for all protective devices
- Ensure selective coordination (downstream trips before upstream)
- Short circuit analysis (fault current calculations)
- Arc flash hazard analysis per NFPA 70E

**Coordination Principles:**
- Overcurrent devices sized per NEC 240
- Selectivity margin: 0.2-0.4 seconds between devices
- Ground fault protection coordinated separately

## 5. Cross-References

- Related ATA Chapters: ATA 24 (Electrical Power), ATA 33 (Lights)
- Parent Document: [03-90_Tables_Schemas_Diagrams](../README.md)
- Related Documents:
  - [03-90-03-02A Control Circuit Schematics](./03-90-03-02A_Control_Circuit_Schematics.md)
  - [03-90-03-03A Wiring Diagrams](./03-90-03-03A_Wiring_Diagrams.md)
  - [03-90-02-04A H2 Safety Schematics](../03-90-02_H2_GSE_Schematics/03-90-02-04A_H2_Safety_Schematics.md)

## 6. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Electrical Engineering | Initial release |

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-08.

---
