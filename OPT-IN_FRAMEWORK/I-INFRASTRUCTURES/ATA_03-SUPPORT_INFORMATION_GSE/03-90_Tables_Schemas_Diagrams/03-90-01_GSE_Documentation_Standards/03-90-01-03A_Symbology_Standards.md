# 03-90-01-03A - GSE Symbology Standards

## 1. Purpose

This document defines the standard symbols, icons, and graphical representations to be used in all Ground Support Equipment (GSE) documentation, ensuring universal understanding and compliance with international symbology standards.

## 2. Scope

This standard covers symbology for:
- Piping and instrumentation diagrams (P&ID)
- Electrical schematics
- Safety signage and markings
- Process flow diagrams
- Hydraulic and pneumatic systems
- Hydrogen and cryogenic systems
- Control and monitoring systems

## 3. Applicable Documents

- [ISA-5.1](https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa5-1) - Instrumentation Symbols and Identification
- [IEEE 315](https://standards.ieee.org/standard/315-1975.html) - Graphic Symbols for Electrical and Electronics Diagrams
- [ISO 14617](https://www.iso.org/standard/44433.html) - Graphical Symbols for Diagrams
- [ISO 7010](https://www.iso.org/standard/72424.html) - Graphical Symbols - Safety Colors and Safety Signs
- [ASME Y32.2](https://www.asme.org/) - Graphic Symbols for Fluid Power Diagrams
- [EN ISO 80416](https://www.iso.org/standard/66675.html) - Basic Principles for Graphical Symbols
- [CGA P-1](https://www.cganet.com/) - Commodity Specification for Hydrogen (symbology aspects)

## 4. Documentation Description

### 4.1 Overview

Standardized symbology ensures:
- Immediate recognition of equipment and systems
- Consistency across all GSE documentation
- Compliance with international standards
- Safety through clear hazard identification
- Effective training and operation
- Reduced risk of misinterpretation

### 4.2 Format and Structure

| Element | Format | Standard |
|---------|--------|----------|
| Symbol Size | Scalable vector graphics | SVG format |
| Line Weight | 0.25mm - 0.5mm standard | ISO 128 |
| Color Coding | As per safety standards | ISO 7010, ANSI Z535 |
| Text Height | Minimum 2.5mm when printed | ISO 3098 |
| Symbol Libraries | Centralized repository | Internal Standard |

### 4.3 Content Requirements

#### 4.3.1 Piping and Instrumentation Symbols (P&ID)

Following ISA-5.1 standard:

**Line Symbols:**
| Symbol Description | Standard | Notes |
|-------------------|----------|-------|
| Process Line | ISA-5.1 | Solid line, weight varies by line size |
| Instrument Signal | ISA-5.1 | Dashed line |
| Electrical Connection | ISA-5.1 | Long dash-short dash |
| Capillary Tube | ISA-5.1 | Line with filled circles |
| Software Link | ISA-5.1 | Dashed line with S |

**Instrument Identification:**
- First letter: Measured/initiating variable (P=Pressure, T=Temperature, F=Flow, L=Level)
- Subsequent letters: Function (I=Indicate, R=Record, C=Control, A=Alarm)
- Example: `PT-101` = Pressure Transmitter #101
- Example: `TIC-205` = Temperature Indicating Controller #205

**Special H2/Cryogenic Symbols:**
| Symbol | Description | Application |
|--------|-------------|-------------|
| LH2 Line | Liquid Hydrogen piping | Double line with LH2 label |
| GH2 Line | Gaseous Hydrogen piping | Single line with GH2 label |
| Vacuum Jacket | Insulated piping | Double line with hatching |
| Vent Stack | Hydrogen venting | Triangle with vent arrow |
| Relief Valve | Pressure relief | PRV symbol per ISA-5.1 |

#### 4.3.2 Electrical Symbols

Following IEEE 315 standard:

**Power Distribution:**
| Symbol | Description | Application |
|--------|-------------|-------------|
| Circuit Breaker | Protection device | Main and branch circuits |
| Disconnect Switch | Isolation | Maintenance isolation points |
| Transformer | Voltage conversion | Step-down/step-up |
| Ground/Earth | Safety ground | All electrical systems |
| Motor | Electric motor | Pump, compressor, fan drives |

**Control Circuits:**
| Symbol | Description | Application |
|--------|-------------|-------------|
| Relay | Control relay | Interlock logic |
| Timer | Time delay | Sequence control |
| Push Button | Manual control | Start/stop stations |
| Indicator Light | Status indication | System status |
| Emergency Stop | E-stop button | Safety circuits |

**H2 System Specific:**
- Explosion-proof enclosures: Ex symbol per IECEx
- Intrinsically safe circuits: [ia] designation
- Hazardous area classification markers: Zone 0, 1, 2

#### 4.3.3 Safety Symbols

Following ISO 7010 and ANSI Z535:

**Mandatory Action Signs:**
| Symbol | Meaning | Color |
|--------|---------|-------|
| Eye Protection | Wear safety glasses | Blue circle |
| Hand Protection | Wear gloves | Blue circle |
| Protective Clothing | Wear PPE | Blue circle |
| Read Instructions | Consult manual | Blue circle |

**Warning Signs:**
| Symbol | Meaning | Color |
|--------|---------|-------|
| Flammable Gas | H2 present | Yellow triangle |
| Cryogenic Hazard | Cold burns | Yellow triangle |
| High Pressure | Pressure hazard | Yellow triangle |
| Electrical Hazard | Shock risk | Yellow triangle |
| No Open Flames | Fire risk | Red circle with slash |

**H2-Specific Safety Symbols:**
- Hydrogen Gas: H2 in yellow triangle with flame
- No Smoking: ISO 7010 P002
- Authorized Personnel Only: Restricted area
- Emergency Shutdown: Red emergency stop symbol
- Assembly Point: Evacuation gathering point

#### 4.3.4 Process Flow Diagram Symbols

| Symbol | Description | Standard |
|--------|-------------|----------|
| Process Vessel | Tank, container | ISO 14617 |
| Pump | Fluid mover | ISO 14617 |
| Compressor | Gas compressor | ISO 14617 |
| Heat Exchanger | Thermal transfer | ISO 14617 |
| Valve (generic) | Flow control | ISO 14617 |
| Filter | Contamination removal | ISO 14617 |

**H2 Equipment Symbols:**
- LH2 Storage Tank: Cylinder with LH2 label
- Vaporizer: Heat exchanger symbol with GH2 out
- Pressure Build Unit: Coil with pump symbol
- Defueling Unit: Pump with reverse flow arrow

#### 4.3.5 Hydraulic and Pneumatic Symbols

Following ASME Y32.2:

| Symbol | Description | Application |
|--------|-------------|-------------|
| Hydraulic Pump | Fluid power | Fixed/variable displacement |
| Pneumatic Cylinder | Linear actuator | Extend/retract operations |
| Directional Valve | Flow control | Position control |
| Pressure Regulator | Pressure control | System pressure management |
| Accumulator | Energy storage | Pressure buffering |

### 4.4 Symbol Creation Guidelines

When creating new symbols:

1. **Simplicity**: Use simple geometric shapes
2. **Scalability**: Ensure clarity at all sizes
3. **Consistency**: Follow established patterns
4. **Standards**: Reference applicable international standards
5. **Documentation**: Document new symbols in library
6. **Approval**: Require engineering approval for new symbols

### 4.5 Color Standards

| Application | Color | RGB | Use Case |
|-------------|-------|-----|----------|
| LH2 Systems | Light Blue | 173,216,230 | Cryogenic hydrogen |
| GH2 Systems | Blue | 0,102,204 | Gaseous hydrogen |
| Electrical | Black | 0,0,0 | Wiring, circuits |
| Safety/Warning | Yellow | 255,255,0 | Hazard warnings |
| Prohibition | Red | 255,0,0 | Do not, stop |
| Mandatory | Blue | 0,51,153 | Must do |
| Emergency | Green | 0,153,51 | Emergency exit, first aid |

### 4.6 Symbol Library Management

**Repository Structure:**
```
ASSETS/SYMBOLS/
├── electrical/
├── instrumentation/
├── piping/
├── mechanical/
├── safety/
├── h2_specific/
└── README.md
```

**Symbol File Naming:**
- Format: `[category]_[description]_[standard].svg`
- Example: `inst_pressure_transmitter_isa51.svg`
- Example: `safety_h2_flammable_iso7010.svg`

## 5. Cross-References

- Related ATA Chapters: ATA 02 (Operations Information), ATA 12 (Servicing)
- Parent Document: [03-90_Tables_Schemas_Diagrams](../README.md)
- Related Documents:
  - [03-90-01-02A Drawing Standards](./03-90-01-02A_Drawing_Standards.md)
  - [03-90-02 H2 GSE Schematics](../03-90-02_H2_GSE_Schematics/README.md)
  - [03-90-03 Electrical Schematics](../03-90-03_Electrical_Schematics/README.md)

## 6. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-08.

---
