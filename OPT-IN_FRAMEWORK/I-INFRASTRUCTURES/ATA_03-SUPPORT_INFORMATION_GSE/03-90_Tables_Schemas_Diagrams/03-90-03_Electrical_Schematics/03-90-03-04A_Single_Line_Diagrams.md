# 03-90-03-04A - Single Line Diagrams

## 1. Purpose

This document establishes standards for electrical single line diagrams (SLD) for Ground Support Equipment, providing a simplified representation of the electrical power distribution system.

## 2. Scope

This specification covers single line diagrams for:
- Main service and distribution
- Transformer connections
- Circuit breaker and protection device layout
- Load distribution and feeders
- Emergency power systems
- Grounding and bonding overview

## 3. Applicable Documents

- [IEEE 315](https://standards.ieee.org/standard/315-1975.html) - Graphic Symbols for Electrical Diagrams
- [IEEE 242](https://standards.ieee.org/) - Protection and Coordination of Industrial Power Systems
- [ANSI C37](https://www.ansi.org/) - Power Switchgear Standards
- [IEC 60617](https://www.iec.ch/) - Graphical Symbols for Diagrams

## 4. Documentation Description

### 4.1 Overview

Single line diagrams show the electrical power flow from source to loads in a simplified format, essential for system design, analysis, and fault studies.

### 4.2 Format and Structure

| Element | Format | Standard |
|---------|--------|----------|
| Power Flow | Top-to-bottom or left-to-right | Single line per phase |
| Protective Devices | Standard symbols with ratings | IEEE 315 |
| Bus Representation | Heavy horizontal line | Three-phase bus shown as one |
| Equipment Ratings | Annotated near symbols | Voltage, current, power |

### 4.3 Content Requirements

#### 4.3.1 Electrical Service

**Utility Connection:**
- Voltage: 480V, 3-phase, 4-wire, 60Hz
- Service capacity: TBD kVA
- Main circuit breaker: TBD AF, TBD AT
- Short circuit rating: TBD kA

#### 4.3.2 Distribution Overview

**Main Distribution Panel (MDP):**
- Incoming feeder from service
- Main breaker characteristics
- Outgoing feeders to sub-panels and major loads
- Protection device coordination

**Feeders Shown:**
- Motor control center (MCC)
- Control power panels (CPP)
- Lighting panels
- Emergency power panel
- Major individual loads (large motors, compressors)

#### 4.3.3 Protective Device Annotations

**Breaker Notation Example:**
- `CB-01: 400AF / 350AT / 35kA SCCR`
- AF = Ampere Frame
- AT = Ampere Trip (adjustable)
- SCCR = Short Circuit Current Rating

#### 4.3.4 Load Representation

**Motor Loads:**
- Motor symbol with HP/kW rating
- Full load amps (FLA)
- Starting method (DOL, soft start, VFD)
- Protection (OL relay, breaker)

**Other Loads:**
- Lighting and receptacle panels (total load)
- HVAC equipment
- UPS and battery systems
- Control and instrumentation loads

## 5. Cross-References

- Parent Document: [03-90_Tables_Schemas_Diagrams](../README.md)
- Related Documents:
  - [03-90-03-01A Power Distribution Diagrams](./03-90-03-01A_Power_Distribution_Diagrams.md)

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
