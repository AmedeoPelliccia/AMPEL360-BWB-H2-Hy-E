# 03-40-03-01A - PLC Programming

**Document ID:** 03-40-03-01A  
**Title:** Programmable Logic Controller Programming Standards  
**ATA Chapter:** 03 — Support Information/GSE  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

Defines programming standards, best practices, and requirements for PLCs used in GSE control systems.

---

## 2. Scope

Covers PLC programming languages, standards, safety programming, and code organization for GSE automation.

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| [IEC 61131-3](https://www.iec.ch/) | PLC Programming Languages | Standard |
| [IEC 61508](https://www.iec.ch/functional-safety) | Functional Safety | SIL certification |
| [IEC 61511](https://www.iec.ch/functional-safety) | Safety Instrumented Systems | Process safety |
| [MISRA C](https://misra.org.uk/) | C Coding Guidelines | If C used |

---

## 4. Software Description

### 4.1 Programming Languages (IEC 61131-3)

| Language | Usage | Pros | Typical Application |
|----------|-------|------|-------------------|
| Ladder Logic (LD) | 40% | Easy for electricians | Discrete control, interlocks |
| Structured Text (ST) | 35% | Complex algorithms | PID control, calculations |
| Function Block (FBD) | 15% | Visual, modular | Process control |
| Sequential Function Chart (SFC) | 10% | State machines | Batch processes, sequences |

### 4.2 PLC Standards

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Primary Platform | Siemens S7-1500, Allen-Bradley ControlLogix | Safety-rated |
| Programming Environment | TIA Portal, Studio 5000 | Latest versions |
| Safety Programming | SafetyPLC or dedicated safety PLC | SIL 3 capable |
| Cycle Time | 10-100 ms typical | Based on application |
| Memory | ≥2 MB program, ≥8 MB data | Adequate headroom |

### 4.3 Code Organization

```
PLC Program Structure:
├── MAIN (Organization Block)
│   ├── Initialization
│   ├── Safety_Logic (highest priority)
│   ├── Process_Control
│   ├── Sequencing
│   ├── HMI_Interface
│   └── Diagnostics
├── Function Blocks (Reusable)
│   ├── FB_Valve_Control
│   ├── FB_PID_Controller
│   ├── FB_Pump_Control
│   └── FB_Emergency_Stop
└── Data Blocks
    ├── Process_Variables
    ├── Setpoints
    ├── Alarms
    └── Historical_Data
```

### 4.4 Safety Programming

- **Safety Functions**: Separate from standard logic
- **Voting**: 2oo3 for critical sensors
- **Watchdogs**: Monitor PLC health
- **Fail-Safe Outputs**: De-energize to safe state

### 4.5 Interfaces

- Field I/O (digital, analog, RTD, thermocouple)
- HMI communication (Profinet, EtherNet/IP)
- SCADA integration (OPC UA)
- Safety I/O (PROFIsafe, CIP Safety)

---

## 5. Safety and Security Requirements

| Requirement ID | Requirement | Standard |
|----------------|-------------|----------|
| PLC-SAF-001 | Safety logic shall be certified to SIL 3 | IEC 61508 |
| PLC-SAF-002 | Emergency stop response time <50 ms | System requirement |
| PLC-SEC-001 | PLC shall have password protection | IEC 62443 |
| PLC-SEC-002 | Firmware updates require authentication | IEC 62443 |

---

## 6. Cross-References

- 03-40-03-02A — HMI Software
- 03-40-03-03A — SCADA Systems
- 03-40-03-04A — Real Time Control SW

---

## 7. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
