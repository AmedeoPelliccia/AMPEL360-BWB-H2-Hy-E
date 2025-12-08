# Index: ATA 61-00-05 Interfaces Documentation

> **Document ID:** 61-00-05-INDEX  
> **Last Update:** 2025-12-07  
> **Status:** Active

---

## 📂 Directory Overview

This directory contains comprehensive interface specifications for the AMPEL360 Q100 Propellers and Propulsors system (ATA 61). All interface documents follow the ATA nomenclature standard: `61-00-05-XX-XXA_Description.md`.

---

## 📑 Table of Contents

### 1. Mechanical Interfaces (`61-00-05-01`)
Structural and mechanical interface specifications for propulsor mounting, shaft couplings, and vibration isolation.

| Document ID | Title | Description |
|-------------|-------|-------------|
| [61-00-05-01-01A](61-00-05-01_Mechanical_Interfaces/61-00-05-01-01A_Shaft_Coupling.md) | Shaft Coupling Interface | Motor-to-fan torque transmission interface |
| [61-00-05-01-02A](61-00-05-01_Mechanical_Interfaces/61-00-05-01-02A_Mounting_Flanges.md) | Mounting Flanges Interface | Propulsor-to-nacelle structural mounting |
| [61-00-05-01-03A](61-00-05-01_Mechanical_Interfaces/61-00-05-01-03A_Vibration_Dampers.md) | Vibration Dampers Interface | Vibration isolation system specification |
| [61-00-05-01-04A](61-00-05-01_Mechanical_Interfaces/61-00-05-01-04A_Thrust_Bearings.md) | Thrust Bearings Interface | Axial load bearing system specification |

### 2. Electrical Interfaces (`61-00-05-02`)
Electrical power, control signals, sensors, and grounding interfaces.

| Document ID | Title | Description |
|-------------|-------|-------------|
| [61-00-05-02-01A](61-00-05-02_Electrical_Interfaces/61-00-05-02-01A_Power_Distribution.md) | Power Distribution Interface | 800 VDC power supply (up to 4.5 MW per propulsor) |
| [61-00-05-02-02A](61-00-05-02_Electrical_Interfaces/61-00-05-02-02A_Control_Signals.md) | Control Signals Interface | Discrete and analog control signals |
| [61-00-05-02-03A](61-00-05-02_Electrical_Interfaces/61-00-05-02-03A_Sensor_Connections.md) | Sensor Connections Interface | Temperature, vibration, speed, and current sensors |
| [61-00-05-02-04A](61-00-05-02_Electrical_Interfaces/61-00-05-02-04A_Grounding_Bonding.md) | Grounding and Bonding Interface | Protective earth, EMI shielding, lightning protection |

### 3. Data Interfaces (`61-00-05-03`)
Digital communication buses and data exchange protocols.

| Document ID | Title | Description |
|-------------|-------|-------------|
| [61-00-05-03-01A](61-00-05-03_Data_Interfaces/61-00-05-03-01A_ARINC_429_Buses.md) | ARINC 429 Buses Interface | Health monitoring and maintenance data (100 kbps) |
| [61-00-05-03-02A](61-00-05-03_Data_Interfaces/61-00-05-03-02A_AFDX_Networks.md) | AFDX Networks Interface | High-speed deterministic control data (100 Mbps) |
| [61-00-05-03-03A](61-00-05-03_Data_Interfaces/61-00-05-03-03A_Discrete_Signals.md) | Discrete Signals Interface | Safety-critical discrete signal encoding |
| [61-00-05-03-04A](61-00-05-03_Data_Interfaces/61-00-05-03-04A_CAN_Bus_Links.md) | CAN Bus Links Interface | Internal propulsor and ground support (500 kbps) |

### 4. Hydrogen System Interfaces (`61-00-05-04`)
Hydrogen fuel supply, safety interlocks, and leak detection systems.

| Document ID | Title | Description |
|-------------|-------|-------------|
| [61-00-05-04-01A](61-00-05-04_Hydrogen_System_Interfaces/61-00-05-04-01A_H2_Fuel_Supply_Connections.md) | H₂ Fuel Supply Connections | Gaseous H₂ supply lines and fittings |
| [61-00-05-04-02A](61-00-05-04_Hydrogen_System_Interfaces/61-00-05-04-02A_Safety_Interlocks.md) | Safety Interlocks Interface | H₂ leak detection and emergency shutdown interlocks |
| [61-00-05-04-03A](61-00-05-04_Hydrogen_System_Interfaces/61-00-05-04-03A_Pressure_Regulation.md) | Pressure Regulation Interface | H₂ pressure control (5-10 bar) |
| [61-00-05-04-04A](61-00-05-04_Hydrogen_System_Interfaces/61-00-05-04-04A_Leak_Detection_Integration.md) | Leak Detection Integration | H₂ leak detector sensors and alarm logic |

### 5. Thermal Interfaces (`61-00-05-05`)
Cooling system connections and thermal management.

| Document ID | Title | Description |
|-------------|-------|-------------|
| [61-00-05-05-01A](61-00-05-05_Thermal_Interfaces/61-00-05-05-01A_Cooling_System_Connections.md) | Cooling System Connections | Coolant supply/return (10 L/min, 200 kW heat rejection) |
| [61-00-05-05-02A](61-00-05-05_Thermal_Interfaces/61-00-05-05-02A_Heat_Exchanger_Mounts.md) | Heat Exchanger Mounts Interface | Structural mounting for heat exchangers |
| [61-00-05-05-03A](61-00-05-05_Thermal_Interfaces/61-00-05-05-03A_Thermal_Insulation_Boundaries.md) | Thermal Insulation Boundaries | Insulation requirements for hot/cold zones |

### 6. Interface Control Documents (`61-00-05-06`)
System-level interface control documents coordinating multiple interfaces.

| Document ID | Title | Description |
|-------------|-------|-------------|
| [61-00-05-06-01A](61-00-05-06_Interface_Control_Documents/61-00-05-06-01A_ICD_Template.md) | ICD Template | Standard template for all interface control documents |
| [61-00-05-06-02A](61-00-05-06_Interface_Control_Documents/61-00-05-06-02A_ICD_Propulsion_to_Avionics.md) | ICD Propulsion to Avionics | Propulsion ↔ ATA 24/27/42 (power, control, data) |
| [61-00-05-06-03A](61-00-05-06_Interface_Control_Documents/61-00-05-06-03A_ICD_Propulsion_to_Fuel_System.md) | ICD Propulsion to Fuel System | Propulsion ↔ ATA 28 (H₂ supply, safety) |
| [61-00-05-06-04A](61-00-05-06_Interface_Control_Documents/61-00-05-06-04A_ICD_Propulsion_to_Structure.md) | ICD Propulsion to Structure | Propulsion ↔ ATA 54 (mounting, loads) |

---

## 🔗 Cross-References to Related ATA Chapters

### ATA 24 — Electrical Power
- Power distribution (800 VDC)
- Ground fault detection
- Power quality management

### ATA 27 — Flight Controls
- Thrust command and feedback
- Differential thrust for yaw/roll control
- Emergency shutdown commands

### ATA 28 — Fuel
- Hydrogen fuel supply
- Pressure regulation
- Safety interlocks

### ATA 54 — Nacelles and Pylons
- Structural mounting interfaces
- Load transfer paths
- Access for maintenance

### ATA 21 — Air Conditioning
- Thermal management system
- Coolant supply and return
- Heat rejection

### ATA 73 — Engine Fuel and Control
- Fuel control systems (for H₂ systems)

### ATA 91 — Charts
- Interface diagrams and schematics

---

## 📊 Document Status Summary

| Category | Documents | Status |
|----------|-----------|--------|
| Mechanical Interfaces | 4 | Draft (Rev A) |
| Electrical Interfaces | 4 | Draft (Rev A) |
| Data Interfaces | 4 | Draft (Rev A) |
| Hydrogen System Interfaces | 4 | Draft (Rev A) |
| Thermal Interfaces | 3 | Draft (Rev A) |
| Interface Control Documents | 4 | Draft (Rev A) |
| **Total** | **23** | **All Draft (Rev A)** |

---

## 📝 Nomenclature Guide

### Document Numbering Convention
```
61-00-05-XX-XXA_Description.md
│  │  │  │  │ │
│  │  │  │  │ └─ Revision (A=Initial, B=1st update, etc.)
│  │  │  │  └─── Topic number (01, 02, 03, ...)
│  │  │  └────── Subsection (01=Mechanical, 02=Electrical, etc.)
│  │  └───────── Subject (05=Interfaces)
│  └──────────── Section (00=General)
└─────────────── ATA Chapter (61=Propellers/Propulsors)
```

### Subsection Codes
- `01` — Mechanical Interfaces
- `02` — Electrical Interfaces
- `03` — Data Interfaces
- `04` — Hydrogen System Interfaces
- `05` — Thermal Interfaces
- `06` — Interface Control Documents

---

## 📚 Related Documentation

- [61-00-03-004](../61-00-03_Requirements/61-00-03-004_Interface_Requirements.md) — Interface Requirements (parent document)
- [61-00-04_Design](../61-00-04_Design/README.md) — Design specifications
- [61-00-07_V_AND_V](../61-00-07_V_AND_V/README.md) — Verification and validation

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: Active documentation set, all documents at Draft (Rev A)
- **Approval**: Subject to human review and technical approval
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last Update**: 2025-12-07

---
