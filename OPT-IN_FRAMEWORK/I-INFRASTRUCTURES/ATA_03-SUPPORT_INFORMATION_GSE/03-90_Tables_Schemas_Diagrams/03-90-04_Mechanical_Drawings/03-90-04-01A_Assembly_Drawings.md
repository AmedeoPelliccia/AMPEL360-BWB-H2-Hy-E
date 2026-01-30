# 03-90-04-01A - Assembly Drawings

## 1. Purpose

This document establishes standards for mechanical assembly drawings for Ground Support Equipment, showing how components fit together to form complete assemblies for hydrogen GSE systems.

## 2. Scope

This specification covers assembly drawings for:
- LH2/GH2 equipment assemblies
- Structural frame assemblies
- Piping subassemblies
- Control panel assemblies
- Cart and mobile equipment assemblies
- Installation assemblies

## 3. Applicable Documents

- [ASME Y14.5](https://www.asme.org/codes-standards/find-codes-standards/y14-5-dimensioning-tolerancing) - Dimensioning and Tolerancing
- [ASME Y14.24](https://www.asme.org/) - Types and Applications of Engineering Drawings
- [ISO 128](https://www.iso.org/standard/46582.html) - Technical Drawings - General Principles
- [ISO 5456](https://www.iso.org/standard/11507.html) - Technical Drawings - Projection Methods
- [ISO 7200](https://www.iso.org/standard/13736.html) - Technical Product Documentation - Data Fields in Title Blocks

## 4. Documentation Description

### 4.1 Overview

Assembly drawings communicate how parts are assembled, their relationships, and assembly sequences for manufacturing, installation, and maintenance.

### 4.2 Format and Structure

| Element | Format | Standard |
|---------|--------|----------|
| Drawing Views | Orthographic or isometric | ISO 5456 |
| Section Views | As required for clarity | Cutting plane notation |
| Detail Views | Enlarged areas | Scale noted |
| Parts List | Bill of Materials (BOM) | Tabular format |
| Balloon Numbers | Reference to BOM | Sequential numbering |

### 4.3 Content Requirements

#### 4.3.1 Assembly Views

**Main Assembly View:**
- Overall assembly shown in assembled state
- Major components identified with balloon numbers
- Reference to detail drawings for sub-assemblies
- Assembly envelope dimensions (overall height, width, length)
- Connection points to adjacent equipment

**Exploded View:**
- Components separated to show assembly sequence
- Assembly direction indicators
- Fastener types and locations
- Special tools required (if any)

#### 4.3.2 Bill of Materials (BOM)

**BOM Table Format:**

| Item | Part Number | Description | Qty | Material | Remarks |
|------|-------------|-------------|-----|----------|---------|
| 1 | P50123-ABC-01 | LH2 Ball Valve 3" | 1 | 316L SS | Cryogenic service |
| 2 | P20456-DEF-02 | Mounting Bracket | 2 | 304 SS | Painted |
| 3 | P80789-GHI-01 | Hex Bolt M12x50 | 8 | Grade 8.8 | With lockwasher |
| ... | ... | ... | ... | ... | ... |

**BOM Organization:**
- Grouped by sub-assembly (if complex)
- Standard hardware listed separately or at end
- Revision level of each part noted

#### 4.3.3 Assembly Instructions

**Key Information:**
- Assembly sequence (numbered steps if critical)
- Torque specifications for bolts
- Clearances required during assembly
- Alignment requirements
- Special handling (fragile, heavy lift, cryogenic precautions)
- Testing after assembly (pressure test, leak test)

#### 4.3.4 Welded Assemblies

For welded assemblies:
- Weld symbols per AWS A2.4
- Weld procedure specification (WPS) reference
- Non-destructive testing (NDT) requirements (RT, UT, PT)
- Post-weld heat treatment (PWHT) if required
- Distortion control measures

#### 4.3.5 Interface Dimensions

**Critical Interface Dimensions:**
- Mounting hole patterns
- Flange bolt circles
- Pipe connection locations and orientations
- Electrical conduit entry points
- Lifting points and center of gravity

**Mating Parts:**
- Reference to mating equipment drawings
- Clearance and tolerance stackup analysis
- Assembly fit checks

### 4.4 H2-Specific Considerations

**LH2 Equipment:**
- Material compatibility (austenitic stainless steels, aluminum alloys)
- Cleanliness requirements (oxygen-clean per CGA G-4.1)
- Vacuum jacket details (if applicable)
- Thermal contraction allowances
- Support system design (minimize heat leak)

**GH2 High Pressure:**
- Pressure boundary identification
- Hydrostatic test markings
- Code stamp locations (ASME Section VIII)
- Pressure relief device installation

## 5. Cross-References

- Related ATA Chapters: ATA 20 (Standard Practices - Airframe)
- Parent Document: [03-90_Tables_Schemas_Diagrams](../README.md)
- Related Documents:
  - [03-90-04-02A Component Drawings](./03-90-04-02A_Component_Drawings.md)
  - [03-90-04-03A Installation Drawings](./03-90-04-03A_Installation_Drawings.md)
  - [03-90-01-02A Drawing Standards](../03-90-01_GSE_Documentation_Standards/03-90-01-02A_Drawing_Standards.md)

## 6. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Mechanical Engineering | Initial release |

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-08.

---
