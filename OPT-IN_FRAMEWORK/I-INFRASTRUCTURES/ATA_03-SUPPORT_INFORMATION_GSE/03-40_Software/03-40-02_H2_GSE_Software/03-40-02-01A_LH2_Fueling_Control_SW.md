# 03-40-02-01A - LH2 Fueling Control Software

**Document ID:** 03-40-02-01A  
**Title:** Liquid Hydrogen Fueling Control Software  
**ATA Chapter:** 03 — Support Information/GSE  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the software requirements and specifications for the automated control system managing liquid hydrogen (LH2) fueling operations for the AMPEL360 BWB H2-Hybrid Electric aircraft, operating at cryogenic temperatures of -253°C.

---

## 2. Scope

This specification covers:
- LH2 fueling sequence control algorithms
- Cryogenic temperature monitoring and control
- Pressure regulation during fueling
- Flow rate control and metering
- Safety interlocks and emergency shutdown
- Integration with aircraft fueling interface

### 2.1 Operational Phases
- Pre-cooling phase (aircraft tank conditioning)
- Fast-fill phase (bulk hydrogen transfer)
- Top-off phase (final fill to target quantity)
- Post-fueling purge and disconnect
- Emergency abort and safing

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| [SAE AS6968](https://www.sae.org/standards/content/as6968/) | Hydrogen Aircraft Refueling | Industry standard |
| [ISO 13985](https://www.iso.org/standard/69922.html) | Liquid Hydrogen - Land Vehicle Fueling System Interface | Fueling interface |
| [IEC 61508](https://www.iec.ch/functional-safety) | Functional Safety | SIL 3 requirement |
| [IEC 61511](https://www.iec.ch/functional-safety) | Safety Instrumented Systems for Process Industry | Process control |
| [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) | Hydrogen Technologies Code | Safety standards |
| 03-00-13 | GSE Subsystems & Components | Parent systems document |

---

## 4. Software Description

### 4.1 Overview

The LH2 Fueling Control Software manages the complete automated fueling process, ensuring safe and efficient transfer of liquid hydrogen from ground storage to aircraft tanks while maintaining cryogenic temperatures and preventing hazardous conditions such as leaks, over-pressure, or rapid temperature excursions.

**Safety Integrity Level:** SIL 3 (IEC 61508)  
**Control System:** PLC-based with redundant safety logic

### 4.2 Software Specifications

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Safety Integrity Level | SIL 3 | IEC 61508 certified |
| Control Cycle Time | 100 ms | Real-time control loop |
| Response Time (Emergency Shutdown) | <50 ms | Safety-critical requirement |
| Programming Language | Structured Text (IEC 61131-3) | Safety-certified PLC |
| Redundancy | 2oo3 (Two-out-of-Three) voting | For safety functions |
| Operating Temperature Range | -40°C to +50°C ambient | Control system environment |
| Cryogenic Monitoring Range | -270°C to +20°C | LH2 temperature range |

### 4.3 Functional Architecture

```
┌─────────────────────────────────────────────────┐
│         Operator Interface (HMI)                 │
│  - Process visualization                         │
│  - Manual overrides (with safety limits)         │
│  - Alarm management                              │
└─────────────────────┬───────────────────────────┘
                      ↕
┌─────────────────────────────────────────────────┐
│         Supervisory Control Layer                │
│  - Sequence management                           │
│  - Process optimization                          │
│  - Data logging and reporting                    │
└─────────────────────┬───────────────────────────┘
                      ↕
┌─────────────────────────────────────────────────┐
│         Regulatory Control Layer                 │
│  - PID controllers (temperature, pressure, flow) │
│  - Valve positioning control                     │
│  - Pump speed control                            │
└─────────────────────┬───────────────────────────┘
                      ↕
┌─────────────────────────────────────────────────┐
│         Safety Logic Layer (SIL 3)               │
│  - Safety interlocks                             │
│  - Emergency shutdown (ESD)                      │
│  - Leak detection response                       │
│  - Pressure relief activation                    │
└─────────────────────┬───────────────────────────┘
                      ↕
┌─────────────────────────────────────────────────┐
│         Field I/O Layer                          │
│  - Sensors (temp, pressure, flow, level, H2)    │
│  - Actuators (valves, pumps)                     │
│  - Safety devices (ESD valves, relief valves)    │
└─────────────────────────────────────────────────┘
```

### 4.4 Control Sequences

#### 4.4.1 Pre-Fueling Sequence
1. System integrity check (leak test, valve function)
2. Aircraft connection verification
3. Ground bonding verification
4. Initial tank temperature measurement
5. Pre-cooling initiation (if required)
6. Safety interlock verification

**Duration:** 5-15 minutes (depending on pre-cooling needs)

#### 4.4.2 Fueling Sequence
1. **Phase 1 - Slow Fill (Tank Conditioning)**
   - Flow rate: 10-50 kg/min
   - Monitor tank temperature gradient
   - Prevent thermal shock
   - Duration: Variable based on initial tank temperature

2. **Phase 2 - Fast Fill (Bulk Transfer)**
   - Flow rate: 100-500 kg/min
   - Maintain pressure differential
   - Monitor for leaks continuously
   - Duration: 10-30 minutes for typical tank size

3. **Phase 3 - Top-Off (Final Fill)**
   - Flow rate: 10-50 kg/min
   - Precise quantity control
   - Reach target fill level
   - Duration: 2-5 minutes

#### 4.4.3 Post-Fueling Sequence
1. Valve closure sequence
2. Line purge with nitrogen
3. Pressure relief verification
4. Disconnect authorization
5. System reset and logging

**Duration:** 3-5 minutes

### 4.5 Interfaces

#### 4.5.1 Aircraft Interface
- **Communication Protocol:** CAN bus, ARINC 825
- **Data Exchange:**
  - Tank temperature (multiple sensors)
  - Tank pressure
  - Fill level
  - Fueling authorization status
  - Emergency stop signal

#### 4.5.2 Ground Storage Interface
- LH2 tank level monitoring
- Storage pressure and temperature
- Pump status and control
- Vaporizer status (if applicable)

#### 4.5.3 Safety System Interface
- H2 leak detectors (multiple zones)
- Fire detection system
- Emergency shutdown system
- Gas detection system
- Personnel safety system

---

## 5. Safety and Security Requirements

### 5.1 Safety Requirements

| Requirement ID | Requirement | Target | Verification |
|----------------|-------------|--------|--------------|
| LH2-FC-SAF-001 | Emergency shutdown shall activate within 50ms of hazard detection | <50ms | Tested |
| LH2-FC-SAF-002 | All safety valves shall fail-closed on power loss | 100% | Design |
| LH2-FC-SAF-003 | H2 concentration >25% LEL shall trigger immediate shutdown | <1 sec | Tested |
| LH2-FC-SAF-004 | Overpressure condition shall activate relief within 100ms | <100ms | Tested |
| LH2-FC-SAF-005 | Redundant temperature monitoring with 2oo3 voting | N/A | Design |
| LH2-FC-SAF-006 | Leak detection coverage ≥95% of piping system | ≥95% | Analysis |
| LH2-FC-SAF-007 | Manual emergency stop shall override all automated controls | 100% | Tested |

### 5.2 Cybersecurity Requirements

| Requirement ID | Requirement | Standard |
|----------------|-------------|----------|
| LH2-FC-SEC-001 | Control system shall be isolated from corporate network | IEC 62443-3-2 |
| LH2-FC-SEC-002 | Operator authentication required for all control actions | IEC 62443-3-3 SR 1.1 |
| LH2-FC-SEC-003 | All setpoint changes shall be logged with user ID | IEC 62443-3-3 SR 2.8 |
| LH2-FC-SEC-004 | Remote access shall use VPN with MFA | IEC 62443-3-3 SR 1.13 |
| LH2-FC-SEC-005 | Firmware updates require cryptographic signature verification | IEC 62443-4-2 |

### 5.3 Operational Limits

| Parameter | Normal Range | Alarm Limit | Shutdown Limit | Unit |
|-----------|--------------|-------------|----------------|------|
| LH2 Temperature | -253 to -250 | <-255, >-248 | <-260, >-245 | °C |
| Transfer Pressure | 1.5 to 3.0 | <1.2, >3.5 | <1.0, >4.0 | bar |
| Flow Rate (Fast Fill) | 100 to 500 | >550 | >600 | kg/min |
| H2 Concentration | 0 to 5% | >10% | >25% LEL | % volume |
| Tank Fill Level | 0 to 95% | >98% | >99% | % capacity |

---

## 6. Cross-References

### 6.1 Related ATA Chapters
- [ATA 03-00-13](../../03-00_GENERAL/03-00-13_Subsystems_Components/README.md) — GSE Subsystems & Components
- [ATA 03-10](../../03-10_Operations/README.md) — GSE Operations
- [ATA 28](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/ATA_28-FUEL/README.md) — Fuel System (Aircraft side)

### 6.2 Parent Document
- [03-40-02_H2_GSE_Software](./README.md) — H2 GSE Software Overview

### 6.3 Related Software Documents
- 03-40-02-02A — Cryogenic Management SW
- 03-40-02-03A — H2 Safety Monitoring SW
- 03-40-02-04A — H2 Leak Detection SW
- 03-40-06-02A — Emergency Shutdown SW

---

## 7. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 03 — Support Information/GSE — LH2 Fueling Control Software  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
