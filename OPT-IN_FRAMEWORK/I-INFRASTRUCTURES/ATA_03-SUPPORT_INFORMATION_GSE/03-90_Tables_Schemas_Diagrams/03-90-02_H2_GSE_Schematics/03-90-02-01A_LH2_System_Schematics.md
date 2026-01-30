# 03-90-02-01A - LH2 System Schematics

## 1. Purpose

This document defines the schematic representation standards and requirements for Liquid Hydrogen (LH2) Ground Support Equipment systems, including storage, transfer, and distribution systems operating at cryogenic temperatures (-253°C).

## 2. Scope

This specification covers LH2 GSE system schematics including:
- LH2 storage tank systems
- Cryogenic transfer systems
- Vacuum-insulated piping networks
- Pressure build and vaporization circuits
- LH2 conditioning systems
- Defueling and recovery systems

## 3. Applicable Documents

- [ATA iSpec 2200](https://www.ata.org/resources/specifications) - Information Standards for Aviation Maintenance
- [ISO 10209](https://www.iso.org/standard/18411.html) - Technical Documentation
- [ISA-5.1](https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa5-1) - Instrumentation Symbols and Identification
- [ASME B31.3](https://www.asme.org/codes-standards/find-codes-standards/b31-3-process-piping) - Process Piping
- [CGA G-5.5](https://www.cganet.com/) - Hydrogen Vent Systems
- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) - Hydrogen Technologies Code
- [ISO/TR 15916](https://www.iso.org/standard/29316.html) - Basic Considerations for Safety of Hydrogen Systems

## 4. Documentation Description

### 4.1 Overview

LH2 system schematics provide critical information for:
- System design and engineering
- Safe operation and maintenance
- Emergency response procedures
- Training and certification
- Regulatory compliance demonstration
- Troubleshooting and diagnostics

All LH2 schematics must emphasize safety-critical elements and cryogenic handling considerations.

### 4.2 Format and Structure

| Element | Format | Standard |
|---------|--------|----------|
| Drawing Format | SVG (vector graphics) | ISO 5457 |
| Line Designation | Color-coded by fluid type | ISA-5.1 |
| Instrument Tags | XXX-NNN format | ISA-5.1 |
| Valve Numbering | VXX-NNN format | [03-90-01-04A](../03-90-01_GSE_Documentation_Standards/03-90-01-04A_Numbering_Conventions.md) |
| Symbol Library | Standardized symbols | [03-90-01-03A](../03-90-01_GSE_Documentation_Standards/03-90-01-03A_Symbology_Standards.md) |

### 4.3 Content Requirements

#### 4.3.1 LH2 Storage Tank Schematics

**Primary Components to be Shown:**

| Component | Representation | Details Required |
|-----------|----------------|------------------|
| Storage Tank | Double-wall vessel symbol | Capacity, design pressure, insulation type |
| Inner Vessel | Solid line boundary | Material specification (e.g., 316L SS) |
| Outer Jacket | Dashed line boundary | Vacuum level, pressure indication |
| Fill Connection | Inlet piping | Line size, connection type |
| Withdrawal Line | Outlet piping | Line size, connection type |
| Pressure Build Circuit | Vaporizer loop | Heat exchanger, control valves |
| Vent System | Relief and vent lines | PRV settings, vent stack height |
| Level Instrumentation | Differential pressure or capacitance | Range, accuracy, alarming |
| Pressure Gauges | Local and transmitted | Range, alarm setpoints |
| Temperature Sensors | RTDs or thermocouples | Locations, quantity |

**Safety Systems:**
- Primary relief valves (PRV) with set pressures
- Secondary/emergency relief paths
- Overfill prevention system (OFPS)
- Low temperature alarms
- Emergency shutdown valves (ESV)

**Schematic Views Required:**
1. **Overall System View**: Complete tank system with all connections
2. **Fill/Transfer Detail**: Focus on fill and withdrawal circuits
3. **Pressure Build Detail**: Vaporizer and pressure control system
4. **Vent and Relief Detail**: Safety relief and normal venting

#### 4.3.2 Cryogenic Transfer System Schematics

**Transfer Pump System:**

| Element | Details |
|---------|---------|
| Pump Type | Centrifugal, positive displacement, or jet pump |
| Drive System | Electric motor, hydraulic, or pneumatic |
| Sealing | Magnetic drive or cryogenic mechanical seal |
| Cooling/Conditioning | Pump cooldown circuit, recirculation |
| Performance | Flow rate, head pressure, NPSH required |

**Transfer Line Components:**
- Vacuum-insulated transfer hoses or hard piping
- Quick-disconnect couplings (QDC)
- Break-away safety couplings
- Flow meters and flow control valves
- Filter/strainer locations
- Drain and purge connections

**Control and Monitoring:**
- Flow rate control (manual or automatic)
- Pressure monitoring (supply and discharge)
- Temperature monitoring (fluid and ambient)
- Transfer sequence interlocks
- Emergency stop provisions

#### 4.3.3 LH2 Distribution Network

**Network Components:**
| Component | Specification |
|-----------|---------------|
| Main Distribution Header | Line size, design pressure, insulation |
| Branch Lines | Sizing per demand calculation |
| Isolation Valves | Location, type, actuation method |
| Pressure Regulators | Set points, flow capacity |
| Expansion Joints | Type, allowable movement |
| Support Systems | Cryogenic-compatible hangers/supports |

**Zone Isolation:**
- Define H2 zones per [03-90-01-04A](../03-90-01_GSE_Documentation_Standards/03-90-01-04A_Numbering_Conventions.md)
- Zone isolation valves (manual and automatic)
- Zone-specific vent systems
- Zone pressure and temperature monitoring

#### 4.3.4 Pressure Build and Vaporization

**Ambient Vaporizer System:**
- Heat exchanger type (forced air, ambient, water bath)
- Capacity (kg/hr or scfm equivalent)
- Pressure control downstream
- Temperature monitoring (inlet/outlet)
- Anti-icing provisions

**Pressure Build Circuit:**
- Internal or external vaporizer
- Control valve (pressure-actuated or electrically controlled)
- Pressure control setpoint
- Feedback control loop diagram
- Redundancy provisions

#### 4.3.5 Conditioning and Quality Control

**LH2 Quality Systems:**
| System | Purpose |
|--------|---------|
| Filters | Particulate removal (e.g., 10 micron) |
| Cold Traps | Moisture and contaminant freezing |
| Purity Monitoring | H2 purity analyzer (>99.95%) |
| Sample Points | Sample extraction for lab analysis |

**Cooldown Procedures:**
- Cooldown vent paths
- Temperature monitoring points
- Cooldown rate limitations
- Vent gas handling

#### 4.3.6 Defueling and Recovery

**Defueling System:**
- Defuel connection to aircraft
- Defuel pump or transfer method
- LH2 recovery tank
- Vent gas recovery (if applicable)
- Purge gas system (GH2 or nitrogen)

**Boil-off Gas (BOG) Management:**
- BOG collection header
- BOG compressor (if used)
- BOG reliquefaction (if applicable)
- BOG flare or vent stack

### 4.4 Schematic Detail Levels

**Level 1 - Process Flow Diagram (PFD):**
- Major equipment only
- Primary flow paths
- Critical control loops
- Suitable for overview and training

**Level 2 - Piping and Instrumentation Diagram (P&ID):**
- All equipment with tags
- All instrumentation with tags
- All piping with line numbers
- All valves with identifiers
- Suitable for detailed engineering and operations

**Level 3 - Detailed Schematics:**
- Component-level detail
- Wiring and signal paths
- Control logic diagrams
- Suitable for maintenance and troubleshooting

### 4.5 Color Coding Standards

| Fluid/System | Line Color | Standard |
|--------------|------------|----------|
| LH2 (liquid) | Light Blue | ANSI/ASME A13.1 |
| GH2 (gas) | Blue | ANSI/ASME A13.1 |
| Vent/Relief | Yellow | ANSI/ASME A13.1 |
| Nitrogen Purge | Gray | ANSI/ASME A13.1 |
| Instrument Air | Light Green | ISA-5.1 |
| Electrical | Black | IEEE 315 |

### 4.6 Safety Annotations

All LH2 schematics must include:

**Hazard Warnings:**
- Cryogenic burn hazard zones
- Flammability hazard areas
- High pressure zones
- Asphyxiation risk areas

**Safety Equipment Locations:**
- Emergency stop buttons
- Fire detection and suppression
- Gas detection sensors
- Emergency breathing apparatus
- Safety showers and eyewash stations
- Evacuation routes

**Regulatory Notes:**
- ATEX/IECEx zone classifications
- Pressure vessel code stamps
- Inspection and test requirements
- Operational limits and restrictions

### 4.7 Document Maintenance

Schematics must be updated for:
- Equipment additions or removals
- Instrument or valve replacements
- Control logic changes
- Set point modifications
- Regulatory requirement changes

Update frequency: **Annual review minimum, immediate for safety-critical changes**

## 5. Cross-References

- Related ATA Chapters: 
  - ATA 12 (Servicing - Hydrogen)
  - ATA 28 (Fuel - Hydrogen as fuel)
- Parent Document: [03-90_Tables_Schemas_Diagrams](../README.md)
- Related Documents:
  - [03-90-02-02A H2 Piping Diagrams](./03-90-02-02A_H2_Piping_Diagrams.md)
  - [03-90-02-03A Cryogenic Flow Diagrams](./03-90-02-03A_Cryogenic_Flow_Diagrams.md)
  - [03-90-02-04A H2 Safety Schematics](./03-90-02-04A_H2_Safety_Schematics.md)
  - [03-90-05-01A LH2 Fueling PFD](../03-90-05_Process_Flow_Diagrams/03-90-05-01A_LH2_Fueling_PFD.md)

## 6. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 H2 Systems Engineering | Initial release |

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-08.

---
