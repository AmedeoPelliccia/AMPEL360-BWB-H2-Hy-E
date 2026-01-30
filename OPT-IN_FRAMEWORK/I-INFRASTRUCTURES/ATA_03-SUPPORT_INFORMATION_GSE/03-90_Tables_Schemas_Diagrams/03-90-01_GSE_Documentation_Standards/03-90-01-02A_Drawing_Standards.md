# 03-90-01-02A - GSE Drawing Standards

## 1. Purpose

This document establishes the technical drawing standards for Ground Support Equipment (GSE) documentation, ensuring consistency, clarity, and compliance with international engineering drawing standards.

## 2. Scope

This standard applies to all GSE technical drawings including:
- Mechanical assembly drawings
- Electrical schematics
- Piping and instrumentation diagrams (P&ID)
- Layout and installation drawings
- Hydrogen system diagrams
- Cryogenic equipment drawings

## 3. Applicable Documents

- [ASME Y14.5](https://www.asme.org/codes-standards/find-codes-standards/y14-5-dimensioning-tolerancing) - Dimensioning and Tolerancing
- [ASME Y14.1](https://www.asme.org/codes-standards/find-codes-standards/y14-1-decimal-inch-drawing-sheet-size-format) - Decimal Inch Drawing Sheet Size and Format
- [ISO 128](https://www.iso.org/standard/46582.html) - Technical Drawings - General Principles of Presentation
- [ISO 5457](https://www.iso.org/standard/11588.html) - Technical Product Documentation - Sizes and Layout of Drawing Sheets
- [ISO 7200](https://www.iso.org/standard/13736.html) - Technical Product Documentation - Data Fields in Title Blocks
- [IEEE 315](https://standards.ieee.org/standard/315-1975.html) - Graphic Symbols for Electrical and Electronics Diagrams
- [ISA-5.1](https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa5-1) - Instrumentation Symbols and Identification

## 4. Documentation Description

### 4.1 Overview

Technical drawings for GSE must communicate design intent clearly and unambiguously to:
- Design engineers
- Manufacturing personnel
- Maintenance technicians
- Quality assurance inspectors
- Installation crews

All drawings must be created and maintained in formats that ensure long-term accessibility and compatibility.

### 4.2 Format and Structure

| Element | Format | Standard |
|---------|--------|----------|
| Drawing Size | A4, A3, A2, A1, A0 (metric) | ISO 5457 |
| File Format | SVG (primary), PDF (distribution) | Internal Standard |
| Scale | 1:1, 1:2, 1:5, 1:10, 1:20, 1:50, 1:100 | ISO 128 |
| Line Weights | 0.13, 0.18, 0.25, 0.35, 0.5, 0.7, 1.0 mm | ISO 128 |
| Units | Millimeters (primary), inches (parenthetical) | ISO 129 |

### 4.3 Content Requirements

#### 4.3.1 Title Block (Mandatory)

Every drawing must include a title block containing:

| Field | Content | Location |
|-------|---------|----------|
| Drawing Number | 03-90-XX-YY format | Lower right |
| Drawing Title | Descriptive name | Title block |
| Revision | Letter (A, B, C...) | Title block |
| Date | ISO 8601 (YYYY-MM-DD) | Title block |
| Drawn By | Author name/initials | Title block |
| Checked By | Reviewer name/initials | Title block |
| Approved By | Approver name/initials | Title block |
| Scale | Drawing scale | Title block |
| Sheet | X of Y | Title block |
| Project | AMPEL360 BWB-H2-Hy-E | Title block |

#### 4.3.2 Drawing Types

**Mechanical Drawings:**
- Assembly drawings showing component relationships
- Detail drawings with full dimensioning
- Installation drawings with mounting specifications
- Exploded views for maintenance

**Electrical Drawings:**
- Single-line diagrams for power distribution
- Schematic diagrams showing circuit details
- Wiring diagrams with wire numbers and colors
- Panel layouts with component locations

**Piping Drawings:**
- P&ID (Piping and Instrumentation Diagrams)
- Isometric piping drawings
- Flow diagrams with valve positions
- Cryogenic system details for LH2 equipment

#### 4.3.3 Dimensioning Standards

Follow ASME Y14.5 principles:
- Dimension to functional datums
- Use geometric dimensioning and tolerancing (GD&T) where appropriate
- Specify tolerances based on function
- Include surface finish requirements where critical
- Note critical dimensions for safety systems

#### 4.3.4 Special Requirements for H2 GSE Drawings

Hydrogen-related drawings must include:
- **Pressure ratings** clearly marked (design and operating)
- **Material specifications** (hydrogen-compatible materials)
- **Weld symbols** per AWS standards
- **Leak test requirements** and acceptance criteria
- **Hazardous area classifications** (ATEX/IECEx zones)
- **Safety distances** and clearances
- **Vent locations** and sizing
- **Emergency shutdown** locations

### 4.4 Symbol Libraries

Standard symbol libraries must be used:

| System | Symbol Standard | Library Location |
|--------|----------------|------------------|
| Electrical | IEEE 315 | ASSETS/SYMBOLS/electrical/ |
| Instrumentation | ISA-5.1 | ASSETS/SYMBOLS/instrumentation/ |
| Piping | ISO 14617 | ASSETS/SYMBOLS/piping/ |
| Mechanical | ISO 7000 | ASSETS/SYMBOLS/mechanical/ |
| Safety | ISO 7010 | ASSETS/SYMBOLS/safety/ |

### 4.5 Revision Control

Drawing revisions must be tracked:

- **Revision Clouds**: Mark changed areas
- **Revision Block**: Document changes in title block
- **Revision History**: Maintain separate revision table for complex drawings
- **Superseded Drawings**: Mark obsolete drawings clearly

### 4.6 Digital File Management

| Aspect | Requirement |
|--------|-------------|
| Primary Format | SVG (vector graphics) |
| Distribution Format | PDF (read-only) |
| Backup | Version control in Git repository |
| Naming Convention | 03-90-XX-YY_Description.svg |
| Metadata | Include in file properties |

## 5. Cross-References

- Related ATA Chapters: 
  - ATA 02 (Operations Information)
  - ATA 20 (Standard Practices - Airframe)
- Parent Document: [03-90_Tables_Schemas_Diagrams](../README.md)
- Related Documents:
  - [03-90-01-03A Symbology Standards](./03-90-01-03A_Symbology_Standards.md)
  - [03-90-01-04A Numbering Conventions](./03-90-01-04A_Numbering_Conventions.md)
  - [03-90-02 H2 GSE Schematics](../03-90-02_H2_GSE_Schematics/README.md)

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
