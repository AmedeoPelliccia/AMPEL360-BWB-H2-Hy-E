# 03-90-01-04A - GSE Numbering Conventions

## 1. Purpose

This document establishes the numbering and identification conventions for all Ground Support Equipment (GSE) documentation, drawings, equipment, and components to ensure consistent identification, traceability, and lifecycle management.

## 2. Scope

This standard covers numbering conventions for:
- Document identification numbers
- Drawing numbers
- Equipment identification tags
- Component part numbers
- Instrument tag numbers
- Valve and fitting identification
- Work order and maintenance tracking numbers

## 3. Applicable Documents

- [ATA iSpec 2200](https://www.ata.org/resources/specifications) - Information Standards for Aviation Maintenance
- [ISO 11179](https://www.iso.org/standard/50340.html) - Metadata Registries
- [ISA-5.1](https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa5-1) - Instrumentation Symbols and Identification
- [SAE AS9100](https://www.sae.org/standards/content/as9100d/) - Quality Management Systems for Aviation
- Internal AMPEL360 Configuration Management Plan

## 4. Documentation Description

### 4.1 Overview

A structured numbering system provides:
- Unique identification of all items
- Traceability throughout lifecycle
- Efficient data management and retrieval
- Clear hierarchical relationships
- Integration with inventory and maintenance systems

### 4.2 Format and Structure

| Element | Format | Standard |
|---------|--------|----------|
| Document Numbers | XX-YY-ZZ-NNA | ATA-based hierarchy |
| Equipment Tags | GSE-XXX-YYYY | Asset management |
| Instrument Tags | XXX-NNN | ISA-5.1 |
| Drawing Numbers | XX-YY-ZZ-NN | Document hierarchy |
| Part Numbers | PNNNNN-NNN-NN | Configuration management |

### 4.3 Content Requirements

#### 4.3.1 Document Numbering System

**Format: XX-YY-ZZ-NNA_Description**

**Structure:**
- **XX**: ATA Chapter (03 = Support Information/GSE)
- **YY**: Section within chapter (90 = Tables/Schemas/Diagrams)
- **ZZ**: Subsection (01-08 defined in 03-90 structure)
- **NN**: Sequential document number (01-99)
- **A**: Revision letter (A, B, C...)
- **Description**: Descriptive name with underscores

**Examples:**
- `03-90-01-01A_Documentation_Guidelines.md`
- `03-90-02-03A_Cryogenic_Flow_Diagrams.md`
- `03-90-06-02A_H2_Equipment_Specs.md`

**Subsection Codes:**
| Code | Subsection |
|------|------------|
| 01 | GSE Documentation Standards |
| 02 | H2 GSE Schematics |
| 03 | Electrical Schematics |
| 04 | Mechanical Drawings |
| 05 | Process Flow Diagrams |
| 06 | Specification Tables |
| 07 | System Architecture Diagrams |
| 08 | Reference Materials |

#### 4.3.2 Equipment Identification System

**Format: GSE-XXX-YYYY**

**Structure:**
- **GSE**: Ground Support Equipment prefix
- **XXX**: Equipment type code (3 characters)
- **YYYY**: Sequential unit number (4 digits)

**Equipment Type Codes:**
| Code | Equipment Type |
|------|----------------|
| LH2 | Liquid Hydrogen Systems |
| GH2 | Gaseous Hydrogen Systems |
| CRY | Cryogenic Equipment |
| PWR | Power Distribution Units |
| CTL | Control Systems |
| PMP | Pumps and Transfer Equipment |
| TRK | Hydrogen Tube Trailers |
| DSP | Dispensers/Service Carts |
| TST | Test Equipment |
| SAF | Safety Equipment |

**Examples:**
- `GSE-LH2-0001`: First LH2 storage tank
- `GSE-GH2-0015`: GH2 tube trailer #15
- `GSE-PMP-0003`: Cryogenic pump unit #3
- `GSE-CTL-0007`: Control panel #7

#### 4.3.3 Instrument Tag Numbers

Following ISA-5.1 standard:

**Format: XXX-NNN**

**Structure:**
- **X**: First letter = Measured/initiating variable
- **XX**: Subsequent letters = Function modifiers
- **NNN**: Loop number (001-999)

**First Letter Codes (Measured Variable):**
| Letter | Variable |
|--------|----------|
| P | Pressure |
| T | Temperature |
| F | Flow |
| L | Level |
| V | Vibration |
| A | Analysis (e.g., gas composition) |
| S | Speed/Frequency |
| W | Weight/Force |

**Subsequent Letter Codes (Function):**
| Letter | Function |
|--------|----------|
| I | Indicate |
| R | Record |
| C | Control |
| A | Alarm |
| T | Transmit |
| S | Switch |
| E | Element (sensor) |
| Y | Relay/Compute |

**Examples:**
- `PT-101`: Pressure Transmitter, loop 101
- `TIC-205`: Temperature Indicating Controller, loop 205
- `FT-310`: Flow Transmitter, loop 310
- `LAH-420`: Level Alarm High, loop 420
- `PICA-150`: Pressure Indicating Control Alarm, loop 150

**Loop Numbering by System:**
| Range | System |
|-------|--------|
| 001-099 | LH2 Storage System |
| 100-199 | LH2 Transfer System |
| 200-299 | GH2 Compression System |
| 300-399 | Vaporization System |
| 400-499 | Safety and Relief Systems |
| 500-599 | Electrical/Control Systems |
| 600-699 | Auxiliary Systems |
| 700-799 | Test and Calibration |
| 800-899 | Environmental Monitoring |
| 900-999 | Reserved/Future |

#### 4.3.4 Valve and Fitting Identification

**Format: VXX-NNN**

**Structure:**
- **V**: Valve prefix
- **XX**: Valve type code
- **NNN**: Sequential number by system

**Valve Type Codes:**
| Code | Valve Type |
|------|------------|
| BV | Ball Valve |
| GV | Gate Valve |
| CV | Check Valve |
| RV | Relief Valve |
| SV | Solenoid Valve |
| PV | Pressure Control Valve |
| HV | Hand Valve |
| XV | Emergency Shutoff Valve (ESV) |

**Examples:**
- `VBV-105`: Ball valve #105
- `VRV-042`: Relief valve #042
- `VXV-001`: Emergency shutoff valve #001
- `VSV-220`: Solenoid valve #220

#### 4.3.5 Drawing Numbering System

**Format: DWG-03-90-ZZ-NN-A**

**Structure:**
- **DWG**: Drawing prefix
- **03**: ATA Chapter
- **90**: Section
- **ZZ**: Subsection
- **NN**: Sequential drawing number
- **A**: Revision letter

**Examples:**
- `DWG-03-90-02-01-A`: H2 GSE Schematic #1, Rev A
- `DWG-03-90-03-05-B`: Electrical Schematic #5, Rev B
- `DWG-03-90-04-10-A`: Mechanical Drawing #10, Rev A

#### 4.3.6 Part Numbering System

**Format: PNNNNN-XXX-YY**

**Structure:**
- **P**: Part prefix
- **NNNNN**: Base part number (5 digits)
- **XXX**: Manufacturer code (3 digits)
- **YY**: Variant/revision (2 digits)

**Part Categories (First Digit):**
| Digit | Category |
|-------|----------|
| 1XXXX | Structural components |
| 2XXXX | Mechanical components |
| 3XXXX | Electrical components |
| 4XXXX | Instrumentation |
| 5XXXX | Piping and fittings |
| 6XXXX | Valves and actuators |
| 7XXXX | Seals and gaskets |
| 8XXXX | Fasteners and hardware |
| 9XXXX | Consumables and supplies |

**Examples:**
- `P50123-ABC-01`: LH2 compatible pipe fitting
- `P61045-DEF-03`: Cryogenic ball valve, variant 03
- `P40789-GHI-02`: Pressure transmitter, revision 02

#### 4.3.7 Work Order and Maintenance Tracking

**Format: WO-YYYYMMDD-NNN**

**Structure:**
- **WO**: Work Order prefix
- **YYYY**: Year
- **MM**: Month
- **DD**: Day
- **NNN**: Sequential number that day

**Examples:**
- `WO-20251208-001`: First work order on Dec 8, 2025
- `WO-20251208-042`: 42nd work order on Dec 8, 2025

**Maintenance Type Prefixes:**
- **PM**: Preventive Maintenance
- **CM**: Corrective Maintenance
- **EM**: Emergency Maintenance
- **IN**: Inspection
- **CA**: Calibration

**Examples:**
- `PM-20251208-001`: Preventive maintenance
- `EM-20251208-003`: Emergency maintenance

### 4.4 Special Numbering for H2 Systems

Hydrogen systems require additional identification due to safety criticality:

**H2 System Zones:**
| Zone | Description |
|------|-------------|
| H2-Z1 | LH2 Storage and Distribution |
| H2-Z2 | LH2-to-GH2 Vaporization |
| H2-Z3 | GH2 Compression and Storage |
| H2-Z4 | Aircraft Fueling Interface |
| H2-Z5 | Vent and Relief Systems |
| H2-Z6 | Safety and Monitoring Systems |

Incorporate zone codes into instrument and valve tags:
- `PT-Z1-101`: Pressure transmitter in Zone 1, loop 101
- `VXV-Z4-001`: Emergency shutoff in Zone 4

### 4.5 Database and Asset Management Integration

All numbering systems must integrate with:

**Systems:**
- CMMS (Computerized Maintenance Management System)
- EAM (Enterprise Asset Management)
- PLM (Product Lifecycle Management)
- Document Management System

**Database Fields:**
| Field | Format | Example |
|-------|--------|---------|
| Asset ID | GSE-XXX-YYYY | GSE-LH2-0001 |
| Location | Site-Zone-Area | APT1-H2Z1-A |
| Status | Active/Inactive/Retired | Active |
| Commission Date | YYYY-MM-DD | 2025-12-08 |
| Next Maintenance | YYYY-MM-DD | 2026-06-08 |

### 4.6 Barcode and RFID Implementation

**Barcode Format:**
- Standard: Code 128 or QR Code
- Content: Equipment ID + location + status URL
- Size: Minimum 25mm x 25mm
- Material: Weather-resistant, cryogenic-compatible

**RFID Tags:**
- Standard: ISO 15693 (HF) or ISO 18000-6C (UHF)
- Read range: 0.5m - 5m depending on application
- Data: Equipment ID + basic metadata
- Durability: Rated for -253°C to +80°C

## 5. Cross-References

- Related ATA Chapters: ATA 02 (Operations Information), ATA 45 (Maintenance Systems)
- Parent Document: [03-90_Tables_Schemas_Diagrams](../README.md)
- Related Documents:
  - [03-90-01-01A Documentation Guidelines](./03-90-01-01A_Documentation_Guidelines.md)
  - [03-90-06 Specification Tables](../03-90-06_Specification_Tables/README.md)

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
