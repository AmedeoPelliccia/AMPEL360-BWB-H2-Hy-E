# 61-00-05-03-04A - CAN Bus Links Interface

**Document ID:** 61-00-05-03-04A  
**Title:** CAN Bus Links Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the Controller Area Network (CAN) bus interface for internal propulsor subsystem communication and ground support equipment (GSE) interfaces.

---

## 2. Scope

This specification covers:
- CAN bus physical layer (CAN 2.0B / CAN-FD)
- Message identifiers and data formats
- Intra-propulsor communication (motor controller, sensors, actuators)
- Ground maintenance and diagnostic interfaces

### 2.1 Applicable Units
- All four Q100 propulsor units
- Internal subsystems per propulsor

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements |
| [ISO 11898](https://www.iso.org/standard/63648.html) | Road Vehicles — CAN | CAN standard |
| [SAE J1939](https://www.sae.org/standards/content/j1939/) | Serial Control and Communications | Heavy-duty vehicle CAN |

---

## 4. Interface Description

### 4.1 Physical Characteristics

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Bus Type | CAN 2.0B (Extended Frame) | — | 29-bit identifier |
| Optional High-Speed | CAN-FD | — | For future use |
| Baud Rate (Flight) | 500 | kbps | Standard CAN |
| Baud Rate (Ground) | 250 | kbps | Diagnostics |
| Cable Type | Twisted pair, shielded | — | Per ISO 11898 |
| Termination | 120 Ω at each end | — | — |
| Connector Type | M12 A-coded (5-pin) | — | — |

### 4.2 CAN Message Identifiers (Internal Propulsor)

| CAN ID (Hex) | Source | Destination | Data | Rate |
|--------------|--------|-------------|------|------|
| 0x100 | Motor Controller | Sensors/Actuators | Motor command | 100 Hz |
| 0x101 | Motor Controller | Sensors/Actuators | Current setpoint | 100 Hz |
| 0x200 | Temperature Sensors | Motor Controller | Temperature readings | 10 Hz |
| 0x201 | Vibration Sensor | Motor Controller | Vibration data | 100 Hz |
| 0x202 | Position Sensors | Motor Controller | Position feedback | 100 Hz |
| 0x300 | Propulsor Control Unit | Motor Controller | High-level command | 50 Hz |
| 0x301 | Motor Controller | Propulsor Control Unit | Status/health | 10 Hz |

### 4.3 Functional Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| CAN-61-001 | Bus utilization | <70% | Analysis |
| CAN-61-002 | Message latency | <10 ms for control messages | Test |
| CAN-61-003 | Error detection | Per ISO 11898 CRC | Design |
| CAN-61-004 | Bus-off recovery | Automatic, <1 second | Test |

---

## 5. Interface Control

### 5.1 Connector Pinout (M12 A-coded, 5-pin)

| Pin | Signal | Function |
|-----|--------|----------|
| 1 | Shield | Cable shield |
| 2 | CAN_H | CAN high |
| 3 | GND | Signal ground |
| 4 | CAN_L | CAN low |
| 5 | (Reserved) | — |

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| CAN-T-001 | Physical layer compliance | Per ISO 11898 | CAN analyzer |
| CAN-T-002 | Message latency | <10 ms | Protocol analyzer |
| CAN-T-003 | Bus loading | <70% at max traffic | Analysis, test |
| CAN-T-004 | Error handling | Automatic recovery | Fault injection |

### 6.2 Production Verification

| Inspection | Frequency | Method |
|------------|-----------|--------|
| Bus termination | 100% | Resistance measurement |
| Message transmission | 100% | Loopback test |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 45](../../../../ATA_45-CENTRAL_MAINTENANCE_SYSTEM/README.md) — Central Maintenance System

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

### 7.3 Related Documents
- 61-00-05-02-03A — Sensor Connections

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Previous: 61-00-05-03-03A_Discrete_Signals](61-00-05-03-03A_Discrete_Signals.md) · [Parent: 61-00-05_Interfaces](../README.md) →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Data Interfaces  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
