# 10-00-13-43A — H2 Emergency Shutdown Subsystem

## 1. Document Information

| Field | Value |
|-------|-------|
| **Document ID** | 10-00-13-43A |
| **Document Number** | 10-00-13-43A_H2_Emergency_Shutdown_Subsystem |
| **Title** | H2 Emergency Shutdown (ESD) Subsystem |
| **Revision** | A |
| **Status** | DRAFT |
| **Date** | 2025-12-11 |
| **Subsystem Type** | h2-safety |
| **Subsystem ID** | H2-ESD-001 |
| **Parent System** | H2 Safety System (10-00-13-05A) |
| **Safety Critical** | Yes |
| **DAL Level** | B |

## 2. Purpose

The H2 Emergency Shutdown (ESD) Subsystem provides rapid, automatic, and manual isolation of hydrogen sources and pathways in response to detected hazards. This **safety-critical subsystem** ensures that in emergency conditions (leak detection, fire, personnel safety threat), all H2 flows can be stopped and systems can be isolated to prevent escalation.

## 3. Scope

### 3.1 In Scope

- Emergency shutdown logic and activation triggers
- Automatic valve closure sequences
- Manual ESD activation (pushbuttons, pull stations)
- Integration with H2 Detection Subsystem (10-00-13-40A)
- Integration with H2 Alarm Subsystem (10-00-13-42A)
- Interface to aircraft H2 fuel system (ATA 28)
- Interface to ground H2 supply systems
- Fail-safe valve design and power-off closure
- ESD reset and system recovery procedures

### 3.2 Out of Scope

- Normal H2 flow control (covered by ATA 28 Fuel System)
- Fire suppression systems (covered by ATA 26 Fire Protection)
- Facility-level ESD (covered by ground infrastructure)
- Personnel evacuation procedures (covered by HSE documentation)

## 4. Functional Description

### 4.1 Primary Functions

1. **Rapid Isolation** - Close all H2 valves within 5 seconds of ESD activation
2. **Multi-Channel Activation** - Automatic (from detection/alarm) and manual triggers
3. **Fail-Safe Operation** - De-energize to close (spring-return or gravity-close valves)
4. **Positive Feedback** - Valve position confirmation for all critical valves
5. **Interlock Management** - Prevent H2 operations until ESD is reset and system verified
6. **Event Logging** - Record all ESD activations with timestamp and trigger source

### 4.2 ESD Activation Triggers

| Trigger Source | Trigger Condition | Response Time | Auto/Manual |
|----------------|------------------|---------------|-------------|
| H2 Detection Level 3 | ≥ 75% LEL in any zone | < 1 second | Automatic |
| H2 Alarm Level 3 | Evacuation alarm active | < 1 second | Automatic |
| Manual ESD Button | Operator press (any location) | Immediate | Manual |
| Fire Detection | Fire alarm in H2 area | < 2 seconds | Automatic |
| System Fault | Critical safety system failure | < 5 seconds | Automatic |
| Remote Command | Ground control station | < 2 seconds | Manual |

## 5. Architecture

### 5.1 System Components

```
H2 Emergency Shutdown Subsystem
├── ESD Logic Controller
│   ├── Primary PLC (safety-rated)
│   ├── Backup PLC (hot standby)
│   └── Voting Logic (2-of-3 for automatic triggers)
│
├── ESD Valves
│   ├── EV-H2-001: Ground Supply Isolation
│   ├── EV-H2-002: Aircraft Fill Line Isolation
│   ├── EV-H2-003: Vent Line Isolation
│   └── EV-H2-004: Drain Line Isolation
│
├── Activation Devices
│   ├── Manual ESD Pushbuttons (6 locations)
│   ├── Emergency Pull Stations (2 locations)
│   └── Remote Command Interface (Control Room)
│
├── Feedback & Indication
│   ├── Valve Position Sensors (limit switches)
│   ├── ESD Active Indicator (lights + sirens)
│   └── Event Recorder (non-volatile memory)
│
└── Interfaces
    ├── H2 Detection (10-00-13-40A) - Trigger input
    ├── H2 Alarm (10-00-13-42A) - Trigger input & status output
    ├── ATA 28 Fuel System - Valve commands
    └── Ground H2 Supply - Isolation commands
```

### 5.2 ESD Valves

| Valve ID | Location | Type | Size | Actuation | Close Time | Fail Mode |
|----------|----------|------|------|-----------|------------|-----------|
| EV-H2-001 | Ground supply header | Ball valve | DN50 (2") | Pneumatic spring-return | < 3 sec | Closed |
| EV-H2-002 | Aircraft fill coupling | Ball valve | DN25 (1") | Pneumatic spring-return | < 2 sec | Closed |
| EV-H2-003 | Vent system isolation | Butterfly valve | DN100 (4") | Electric actuator w/ battery | < 4 sec | Open* |
| EV-H2-004 | Drain line isolation | Ball valve | DN25 (1") | Pneumatic spring-return | < 2 sec | Closed |

*EV-H2-003 fails OPEN to ensure vent path remains available

## 6. ESD Logic and Sequence

### 6.1 ESD Activation Logic

```
IF (H2_Detection_Level_3 = TRUE) OR
   (H2_Alarm_Level_3 = TRUE) OR
   (Manual_ESD_Button = PRESSED) OR
   (Fire_Detected_H2_Zone = TRUE) OR
   (Safety_System_Critical_Fault = TRUE) OR
   (Remote_ESD_Command = TRUE)
THEN
   Activate_ESD_Sequence()
END IF
```

### 6.2 ESD Valve Closure Sequence

| Step | Action | Timing | Verification |
|------|--------|--------|--------------|
| 1 | De-energize all ESD valve solenoids | T+0 sec | Solenoid current = 0 |
| 2 | Spring/actuator drives valves closed | T+0 to T+3 sec | Position sensors |
| 3 | Verify all valves closed (except vent) | T+5 sec | Limit switches |
| 4 | Activate ESD active indication | T+5 sec | Lights/sirens active |
| 5 | Lock out H2 operations | T+5 sec | Interlock engaged |
| 6 | Log ESD event | T+5 sec | Event recorded |

### 6.3 Fail-Safe Design

- **Power Loss:** All ESD valves driven to safe state (closed) by spring energy or battery backup
- **Pneumatic Loss:** Springs drive valves closed mechanically
- **Control Signal Loss:** Watchdog timer triggers ESD if no heartbeat from PLC
- **Communication Loss:** Local hardwired relays activate ESD independently

## 7. Component List

| Component ID | Component Name | Part Number | Qty | Criticality |
|--------------|----------------|-------------|-----|-------------|
| H2-ESD-PLC-01 | Safety PLC (primary) | PLC-SAFE-H2-01 | 1 | Critical |
| H2-ESD-PLC-02 | Safety PLC (backup) | PLC-SAFE-H2-01 | 1 | Critical |
| H2-ESD-VLV-001 | Ground Supply Isolation Valve | VLV-BALL-DN50-NC | 1 | Critical |
| H2-ESD-VLV-002 | Fill Line Isolation Valve | VLV-BALL-DN25-NC | 1 | Critical |
| H2-ESD-VLV-003 | Vent Isolation Valve (NO) | VLV-BFLY-DN100-NO | 1 | Critical |
| H2-ESD-VLV-004 | Drain Isolation Valve | VLV-BALL-DN25-NC | 1 | Critical |
| H2-ESD-BTN-01 | Manual ESD Pushbutton (red) | BTN-ESD-ATEX-RED | 6 | Critical |
| H2-ESD-PULL-01 | Emergency Pull Station | PULL-ESD-ATEX | 2 | Critical |
| H2-ESD-LS-01 | Valve Limit Switch | LS-ATEX-2NC2NO | 4 | Important |
| H2-ESD-SOL-01 | Pneumatic Solenoid Valve | SOL-3WAY-24VDC-NC | 3 | Critical |
| H2-ESD-IND-01 | ESD Active Beacon (red) | BEACON-LED-RED-ATEX | 4 | Essential |
| H2-ESD-SIREN-01 | ESD Siren | SIREN-ATEX-110DB | 2 | Essential |

## 8. Manual ESD Activation Points

| Location ID | Location Description | Device Type | Coverage Radius |
|-------------|---------------------|-------------|-----------------|
| ESD-LOC-01 | Fueling station control panel | Pushbutton | Central control |
| ESD-LOC-02 | Aircraft fueling interface (port side) | Pushbutton | Fueling area |
| ESD-LOC-03 | Aircraft fueling interface (starboard) | Pushbutton | Fueling area |
| ESD-LOC-04 | Ground H2 supply manifold | Pushbutton | Supply area |
| ESD-LOC-05 | Maintenance access platform (aft) | Pushbutton | Maintenance area |
| ESD-LOC-06 | Ground control station | Pushbutton | Control room |
| ESD-LOC-07 | North perimeter gate | Pull station | Facility exit |
| ESD-LOC-08 | South perimeter gate | Pull station | Facility exit |

**Note:** All manual activation points are ATEX-certified and weatherproof (IP67).

## 9. Interfaces

### 9.1 Input Interfaces

| Interface ID | Source | Type | Description |
|--------------|--------|------|-------------|
| IF-ESD-001 | H2 Detection (10-00-13-40A) | Digital | Level 3 alarm trigger (relay) |
| IF-ESD-002 | H2 Alarm (10-00-13-42A) | Digital | Evacuation alarm status (relay) |
| IF-ESD-003 | Fire Detection (ATA 26) | Digital | Fire alarm in H2 zone (relay) |
| IF-ESD-004 | Manual ESD Buttons | Digital | Hardwired pushbutton contacts |
| IF-ESD-005 | Pull Stations | Digital | Hardwired pull station contacts |
| IF-ESD-006 | Remote Command | Data | Ethernet command from control room |

### 9.2 Output Interfaces

| Interface ID | Destination | Type | Description |
|--------------|-------------|------|-------------|
| IF-ESD-101 | ESD Valve Solenoids | Electrical | 24 VDC valve control signals |
| IF-ESD-102 | H2 Alarm (10-00-13-42A) | Digital | ESD active status (relay) |
| IF-ESD-103 | H2 Monitoring (10-00-13-44A) | Data | ESD event data (Modbus TCP) |
| IF-ESD-104 | Fuel System (ATA 28) | Digital | H2 operations interlock (relay) |
| IF-ESD-105 | ESD Indication (lights/sirens) | Electrical | 24 VDC indicator control |

## 10. Safety Features

### 10.1 Redundancy

- **Controller Redundancy:** Dual PLCs with automatic failover (< 100 ms)
- **Power Redundancy:** Dual 24 VDC supplies with battery backup (UPS)
- **Activation Redundancy:** Multiple manual activation points
- **Communication Redundancy:** Hardwired + networked triggers

### 10.2 Diagnostics and Testing

- **Weekly:** Automatic PLC self-test (watchdog, I/O check)
- **Monthly:** Manual activation test (one valve at a time, controlled conditions)
- **Quarterly:** Full ESD sequence test (all valves, simulated emergency)
- **Annually:** Emergency drill with actual H2 operations

### 10.3 Interlock Functions

The ESD system enforces the following interlocks:

1. **ESD Active Interlock:** Prevents any H2 operations while ESD is active
2. **Reset Authorization:** Requires supervisor authorization to reset ESD
3. **System Verification:** Requires leak check before H2 operations resume
4. **Valve Position Interlock:** Confirms all valves in correct position before reset

## 11. ESD Reset Procedure

ESD reset is a controlled, multi-step process:

| Step | Action | Responsible Party | Verification |
|------|--------|------------------|--------------|
| 1 | Confirm emergency condition resolved | Operations Supervisor | Visual + detector readings |
| 2 | Inspect H2 system for leaks/damage | Maintenance Technician | Leak check with sniffer |
| 3 | Verify valve positions and integrity | Maintenance Technician | Visual + position sensors |
| 4 | Enter reset authorization code | Operations Supervisor | Keypad entry |
| 5 | Press ESD Reset button | Operator | Button press |
| 6 | Verify ESD indicators cleared | Operator | Lights/sirens off |
| 7 | Perform system functional test | Operator | Controlled H2 flow test |
| 8 | Log ESD event and reset | Supervisor | Entry in logbook |

## 12. Requirements Traceability

| Requirement ID | Requirement Description | Verification Method |
|---------------|-------------------------|---------------------|
| REQ-10-ESD-001 | Close all H2 valves within 5 seconds | Timing test during commissioning |
| REQ-10-ESD-002 | Fail-safe valve closure on power loss | Power interruption test |
| REQ-10-ESD-003 | Manual activation from ≥ 6 locations | Inspection + functional test |
| REQ-10-ESD-004 | Automatic activation on Level 3 alarm | Integration test with detection system |
| REQ-10-ESD-005 | ESD active indication visible/audible | Functional test of beacons/sirens |
| REQ-10-ESD-006 | Event logging of all ESD activations | Log review after test activation |

## 13. Hazard Mitigation

| Hazard ID | Hazard Description | Mitigation by this Subsystem |
|-----------|-------------------|------------------------------|
| H-10-001 | Uncontrolled H2 release during fueling | ESD isolates ground supply + fill line |
| H-10-003 | Fire in H2 area | ESD stops H2 flow, limits fuel to fire |
| H-10-005 | Personnel exposure to high H2 concentration | ESD triggered by detection, stops source |
| H-10-011 | Failure to isolate H2 on leak detection | Redundant valves + fail-safe design |

## 14. Operational Domain

| Parameter | Min | Typical | Max | Unit |
|-----------|-----|---------|-----|------|
| Ambient Temperature | -40 | +20 | +60 | °C |
| Valve Operating Pressure | 0 | 10 | 50 | bar |
| Valve Close Time (required) | - | 3 | 5 | seconds |
| ESD Logic Response Time | - | 0.5 | 1.0 | seconds |

## 15. Applicable Standards

- **NFPA 2** - Hydrogen Technologies Code (Section 7.3.6 Emergency Shutdown)
- **IEC 61508** - Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems (SIL 2)
- **IEC 61511** - Functional safety - Safety instrumented systems for the process industry sector
- **SAE AS6968** - Hydrogen Aircraft GSE (Section 5.7 Emergency Controls)
- **API RP 14C** - Analysis, Design, Installation, and Testing of Safety Systems (offshore, adapted for H2)
- **ATEX 2014/34/EU** - Equipment for potentially explosive atmospheres

## 16. Related Documentation

- [10-00-13-05A - H2 Safety System Architecture](../system-architecture/10-00-13-05A_H2_Safety_System_Architecture.md)
- [10-00-13-40A - H2 Detection Subsystem](10-00-13-40A_H2_Detection_Subsystem.md)
- [10-00-13-41A - H2 Venting Subsystem](10-00-13-41A_H2_Venting_Subsystem.md)
- [10-00-13-42A - H2 Alarm Subsystem](10-00-13-42A_H2_Alarm_Subsystem.md)
- [10-00-13-44A - H2 Monitoring Subsystem](10-00-13-44A_H2_Monitoring_Subsystem.md)
- ATA 28 - Fuel System (H2 valves and interfaces)

## 17. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-11 | AI/Copilot (Amedeo Pelliccia) | Initial ESD subsystem specification |

## 18. Document Control

| Field | Value |
|-------|-------|
| **Status** | DRAFT |
| **Owner** | AMPEL360 H2 Safety Engineering WG |
| **Approver** | _[to be completed]_ |
| **Classification** | Internal Use |
| **Next Review** | 2026-03-11 |

---

**AI Generation Note:**

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-11

---

*End of Document*
