# 03-90-03-03A - Wiring Diagrams

## 1. Purpose

This document establishes standards for electrical wiring diagrams for Ground Support Equipment, providing detailed point-to-point wiring information for installation, maintenance, and troubleshooting.

## 2. Scope

This specification covers wiring diagrams for:
- Control panel internal wiring
- Field device connections
- Motor connections and terminations
- Instrument loop wiring
- Grounding and shield connections
- Cable and wire identification

## 3. Applicable Documents

- [IEEE 315](https://standards.ieee.org/standard/315-1975.html) - Graphic Symbols for Electrical Diagrams
- [NFPA 79](https://www.nfpa.org/) - Electrical Standard for Industrial Machinery
- [IEC 60204-1](https://www.iec.ch/) - Safety of Machinery - Electrical Equipment
- [IEC 60445](https://www.iec.ch/) - Identification of Equipment Terminals and Conductor Terminations
- [UL 508A](https://www.ul.com/) - Industrial Control Panels

## 4. Documentation Description

### 4.1 Overview

Wiring diagrams show the physical connections between components, enabling accurate installation and efficient troubleshooting.

### 4.2 Format and Structure

| Element | Format | Standard |
|---------|--------|----------|
| Wire Numbers | Alphanumeric tags | Sequential or functional |
| Terminal Designations | Equipment tag + terminal | e.g., PLC-01:I001 |
| Cable Schedules | Tabular format | From-To with wire details |
| Color Coding | Per standard or custom | Document in legend |

### 4.3 Content Requirements

#### 4.3.1 Wire and Cable Identification

**Wire Numbering System:**
- Format: `XXX-NNN` where XXX = circuit/function, NNN = sequence
- Example: `PMP-001` = Pump circuit, wire 001
- Consistent numbering across all diagrams

**Cable Identification:**
- Format: `CBL-XXX-YYY` where XXX = source, YYY = destination
- Example: `CBL-PLC-MCC` = Cable from PLC panel to MCC

**Cable Schedule Table:**

| Cable Tag | From | To | Cores | Size | Length | Type | Route |
|-----------|------|----|-------|------|--------|------|-------|
| CBL-001 | MDP | CP-01 | 4 | 6mm² | 50m | Armored | Underground |
| CBL-002 | CP-01 | M-101 | 4 | 10mm² | 25m | Armored | Tray |

#### 4.3.2 Terminal Block Layouts

**Terminal Strip Designation:**
- Each panel has numbered terminal strips
- Left-to-right, top-to-bottom numbering
- Document terminal type (screw, spring, feed-through)

#### 4.3.3 Instrument Loop Wiring

**Loop Diagram:**
- Shows sensor, transmitter, PLC input, power supply
- Cable shield grounding (one-end or both-ends)
- Junction box locations
- Wire color codes

**Example: Pressure Transmitter Loop**
- PT-101 (field) → JB-05 → PLC AI-001 (panel)
- 4-20mA, 2-wire, shielded pair
- Shield grounded at PLC end only

## 5. Cross-References

- Parent Document: [03-90_Tables_Schemas_Diagrams](../README.md)
- Related Documents:
  - [03-90-03-01A Power Distribution Diagrams](./03-90-03-01A_Power_Distribution_Diagrams.md)
  - [03-90-03-02A Control Circuit Schematics](./03-90-03-02A_Control_Circuit_Schematics.md)

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
