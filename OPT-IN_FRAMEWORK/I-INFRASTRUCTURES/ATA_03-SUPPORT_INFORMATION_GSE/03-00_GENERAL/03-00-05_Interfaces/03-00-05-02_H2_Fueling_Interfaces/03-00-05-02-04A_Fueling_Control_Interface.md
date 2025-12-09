# 03-00-05-02-04A - Fueling Control Interface

## 1. Purpose
This document specifies the control and monitoring interface requirements for hydrogen fueling operations on the AMPEL360 BWB H₂ Hy-E aircraft.

## 2. Scope
This specification covers the communication protocol, control signals, monitoring data, and safety interlocks between the aircraft systems and ground-based H2 fueling equipment.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- SAE AS6968 (Hydrogen Aircraft Refueling)
- ISO 19880-1 (Gaseous Hydrogen Fueling Stations - General Requirements)
- SAE J2601 (Fueling Protocols for Light Duty Gaseous Hydrogen Surface Vehicles)
- ARINC 429 (Digital Information Transfer System)
- IEC 61508 (Functional Safety of Electrical/Electronic Systems)
- DO-178C (Software Considerations in Airborne Systems)
- ISO 26262 (Road Vehicles - Functional Safety)

## 4. Interface Description

### 4.1 Overview
The fueling control interface provides bidirectional communication between the aircraft fuel management system and the ground-based hydrogen fueling equipment. This interface enables automated fueling control, real-time monitoring, safety interlock management, and emergency shutdown capability.

### 4.2 Physical Characteristics
| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| Communication Protocol | ARINC 429 + Ethernet backup | - |
| Data Rate | 100 kbit/s (ARINC 429) | High-speed mode |
| Connector Type | D-sub 25-pin + RJ45 | Sealed, IP67 rated |
| Cable Type | Shielded twisted pair | 10m maximum length |
| Signal Voltage | RS-422 differential, ±5V | ARINC 429 standard |
| Update Rate | 10 Hz minimum | For critical parameters |
| Latency | < 100ms | End-to-end |
| Safety Interlock Signals | 24V DC discrete | Fail-safe logic |
| Emergency Stop | Hardware discrete + software | Dual-redundant |
| Power Supply | 28V DC from aircraft | 2A maximum |

### 4.3 Connection Procedure
1. **Pre-Connection Interface Setup**
   - Verify fueling control panel is in STANDBY mode
   - Connect communication cable (ARINC 429 + Ethernet)
   - Verify indicator lights show LINK ESTABLISHED
   - Perform communication handshake test
   - Verify safety interlock signals functional
   - Test emergency stop function (button check only)
   - Confirm all monitoring parameters reading correctly

2. **Fueling Session Initialization**
   - Aircraft sends READY FOR FUELING status
   - GSE acknowledges and sends pre-fueling checklist status
   - Aircraft verifies fuel tank status (pressure, temperature, level)
   - GSE confirms supply parameters (temperature, pressure, purity)
   - Both systems verify safety interlocks ENABLED
   - Exchange authentication tokens if required
   - Establish secure communication session

3. **Active Fueling Control Loop**
   - Aircraft sends target fuel quantity and flow rate limits
   - GSE acknowledges and begins fueling sequence
   - Continuous monitoring data exchange at 10 Hz:
     - Fuel flow rate (L/min)
     - Tank pressure (bar)
     - Tank temperature (°C)
     - Accumulated volume (L)
     - Bonding resistance (Ω)
     - H2 concentration (ppm)
   - Aircraft controls fueling rate based on tank conditions
   - GSE responds to flow rate commands within 1 second
   - Both systems continuously verify safety parameters

4. **Fueling Completion and Shutdown**
   - Aircraft sends STOP FUELING command when target reached
   - GSE acknowledges and closes supply valve
   - Systems verify pressure stabilization
   - Exchange final fueling data summary
   - Document total fuel transferred, time, anomalies
   - Disconnect communication link
   - Store session data for records

## 5. GSE Equipment Requirements
| Equipment | Specification | Notes |
|-----------|---------------|-------|
| Fueling Control Panel | Touch screen, 15-inch display | Intrinsically safe rated |
| ARINC 429 Interface | Dual-channel, certified | DO-178C Level C software |
| Emergency Stop Button | Hardwired, redundant circuits | Large red mushroom type |
| Data Logger | 1 GB storage minimum | Records all fueling sessions |
| UPS Backup Power | 30 minutes runtime | For safe shutdown |
| Interlock Relay Module | Safety-rated SIL 3 | Fail-safe design |
| Communication Cable | Shielded, 10m length | Quick-connect both ends |

## 6. Safety Requirements
- **Communication Safety**
  - Watchdog timer: 5-second timeout triggers alarm
  - CRC validation on all data packets
  - Automatic fueling stop if communication lost
  - Redundant emergency stop circuits
  - Authentication required for critical commands
  - Encryption for wireless links (if used)

- **Interlock Safety Features**
  - Grounding verification < 0.1 Ω required before fueling enable
  - Door/hatch position verification
  - Personnel proximity detection in exclusion zone
  - Fire detection system armed
  - Lightning proximity interlock (> 10 km clear)
  - Wind speed interlock (< 15 knots)
  - All safety interlocks must be ACTIVE before fueling permit

- **Monitoring and Limits**
  - Tank pressure limit: 12 bar absolute maximum
  - Tank temperature limit: -240°C to -250°C operating range
  - Flow rate limit: 200 L/min maximum
  - H2 concentration: automatic stop at 25% LEL
  - Bonding resistance: continuous monitoring, alarm if > 0.1 Ω
  - Operator must acknowledge all alarms within 10 seconds

- **Emergency Shutdown Hierarchy**
  - Level 1 (Automatic): safety parameter exceeded, immediate stop
  - Level 2 (Operator): emergency stop button pressed
  - Level 3 (Aircraft): flight deck emergency stop command
  - Level 4 (External): fire alarm or evacuation signal
  - All levels result in valve closure < 1 second
  - System enters SAFE MODE requiring reset before resuming

- **Data Recording Requirements**
  - Log all fueling sessions with timestamp
  - Record all parameter data at 1 Hz minimum
  - Store all alarms and operator actions
  - Maintain logs for minimum 5 years
  - Data available for post-fueling analysis
  - Export capability for incident investigation

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 28 (Fuel - H2 Management System)
  - ATA 31 (Indicating/Recording Systems)
  - ATA 42 (Integrated Modular Avionics)
  - ATA 46 (Information Systems - Data Management)
- Parent Document: [03-00-05_Interfaces](../README.md)
- Related GSE Operations: 03-10_Operations
- Related GSE Subsystems: 03-20_Subsystems
- Related Interface: [03-00-05-02-01A_LH2_Coupling_Standards](./03-00-05-02-01A_LH2_Coupling_Standards.md)
- Related Interface: [03-00-05-02-02A_Fueling_Port_Specifications](./03-00-05-02-02A_Fueling_Port_Specifications.md)
- Related Interface: [03-00-05-02-03A_Cryogenic_Connections](./03-00-05-02-03A_Cryogenic_Connections.md)
- Related Interface: [03-00-05-05-01A_ARINC_429_Ground_Interface](../03-00-05-05_Data_Communication_Interfaces/03-00-05-05-01A_ARINC_429_Ground_Interface.md)
- Related Interface: [03-00-05-01-04A_Electrical_Grounding](../03-00-05-01_Electrical_Interfaces/03-00-05-01-04A_Electrical_Grounding.md)
- Safety Reference: [03-00-02_Safety](../../03-00-02_Safety/)

## 8. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 GSE Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
