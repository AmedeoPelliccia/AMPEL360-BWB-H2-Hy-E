# 03-40-03-02A - HMI Software

**Document ID:** 03-40-03-02A  
**Title:** Human-Machine Interface Software for GSE  
**ATA Chapter:** 03 — Support Information/GSE  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

Defines requirements and standards for HMI software used in GSE operator interfaces.

---

## 2. Scope

Covers HMI design principles, alarm management, data visualization, and user experience for GSE control systems.

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| [ISA-101](https://www.isa.org/) | Human Machine Interfaces | HMI design standard |
| [ISA-18.2](https://www.isa.org/) | Alarm Management | Alarm standards |
| [IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) | Industrial Cybersecurity | Security |

---

## 4. Software Description

### 4.1 HMI Platforms

| Platform | Usage | Application |
|----------|-------|-------------|
| Siemens WinCC | Primary | SCADA/HMI for PLC systems |
| Rockwell FactoryTalk | Primary | For Allen-Bradley PLCs |
| Ignition by Inductive Automation | Secondary | Web-based SCADA |
| Custom Web HMI (React/Vue) | Mobile | Technician apps |

### 4.2 Screen Design Standards

| Element | Specification | Rationale |
|---------|---------------|-----------|
| Screen Update Rate | 1-2 Hz | Balance responsiveness and load |
| Alarm Banner | Always visible | Operator awareness |
| Navigation | ≤3 clicks to any screen | Efficiency |
| Color Coding | ISA-101 standard | Consistency |
| Text Size | ≥12 pt minimum | Readability |

### 4.3 Alarm Management (ISA-18.2)

| Priority | Description | Color | Audible | Response Time |
|----------|-------------|-------|---------|---------------|
| Critical | Immediate safety risk | Red | Continuous | <1 minute |
| High | Equipment damage risk | Orange | Intermittent | <5 minutes |
| Medium | Process deviation | Yellow | Single tone | <15 minutes |
| Low | Information only | Blue | None | As convenient |

### 4.4 Key HMI Screens

1. **Overview Screen**: System status at-a-glance
2. **Fueling Control**: LH2 transfer operations
3. **Safety Monitoring**: H2 detection, fire alarms
4. **Trending**: Historical data visualization
5. **Alarms**: Active and historical alarms
6. **Diagnostics**: Equipment health monitoring

### 4.5 Interfaces

- PLC communication (OPC UA, proprietary)
- Database (historian for trending)
- User authentication system
- Event logging system
- Report generation

---

## 5. Safety and Security Requirements

| Requirement ID | Requirement | Standard |
|----------------|-------------|----------|
| HMI-SAF-001 | Critical alarms shall be impossible to silence | ISA-18.2 |
| HMI-SEC-001 | Role-based access control (RBAC) required | IEC 62443 |
| HMI-SEC-002 | Operator actions shall be logged | IEC 62443 |
| HMI-UX-001 | Alarm flood rate shall not exceed 10 alarms/10 min | ISA-18.2 |

---

## 6. Cross-References

- 03-40-03-01A — PLC Programming
- 03-40-03-03A — SCADA Systems

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
