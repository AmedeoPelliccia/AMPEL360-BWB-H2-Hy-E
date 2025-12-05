# Q100-61-STD-DRAWING-REQUIREMENTS — Drawing Requirements Standard

## Purpose

This document defines the technical requirements for all ATA 61 engineering drawings in the AMPEL360-BWB-H2-Hy-E project.

## Scope

Applies to all drawing types:
- DRW (Engineering Drawings)
- SCH (Schematics)
- ICD (Interface Control Drawings)
- INST (Installation Drawings)
- DIAG (Diagrams)

---

## 1. General Requirements

### 1.1 Drawing Content

All drawings shall include:

| Element | Requirement |
|---------|-------------|
| Title Block | Mandatory, per [Q100-61-TPL-TITLE-BLOCK.svg](../TEMPLATES/Q100-61-TPL-TITLE-BLOCK.svg) |
| Revision Block | Mandatory, per [Q100-61-TPL-REVISION-BLOCK.svg](../TEMPLATES/Q100-61-TPL-REVISION-BLOCK.svg) |
| Drawing Number | Per [naming convention](./Q100-61-STD-NAMING-CONVENTION.md) |
| Sheet Size | Per template (A0–A4) |
| Scale | Stated on drawing, metric preferred |
| Units | SI units (mm, kg, N) |

### 1.2 Content Requirements

- All dimensions in millimeters (mm)
- Tolerances per ISO 2768 or as specified
- Surface finish per ISO 1302
- Material specifications per approved list
- Reference to applicable standards

---

## 2. Drawing Types

### 2.1 Engineering Drawings (DRW)

- Fully dimensioned part/assembly drawings
- Include GD&T per ASME Y14.5 / ISO 1101
- Material callout required
- Finish specification required

### 2.2 Schematics (SCH)

- Functional diagrams showing system relationships
- Use standard symbols from [SYMBOL_LIBRARIES/](../SYMBOL_LIBRARIES/)
- Include signal/flow identification
- Reference to component drawings

### 2.3 Interface Control Drawings (ICD)

- Define mechanical, electrical, and functional interfaces
- Include tolerance stack-up where applicable
- Reference controlling specifications
- Show both sides of interface

### 2.4 Installation Drawings (INST)

- Show installation context and location
- Include required clearances
- Reference installation procedures
- Show service access points

### 2.5 Diagrams (DIAG)

- Block diagrams, flow diagrams, wiring diagrams
- Use standard symbols
- Clear labeling and legend
- Reference detailed drawings

---

## 3. Drawing Quality

### 3.1 Legibility

- Minimum text height: 2.5mm (printed)
- Clear line weights per ISO 128
- Adequate spacing between elements
- No overlapping dimensions

### 3.2 Completeness

- All features fully defined
- No implied dimensions
- All referenced documents listed
- Complete parts list for assemblies

---

## 4. File Format Requirements

| Format | Use |
|--------|-----|
| `.svg` | Released vector drawings (Git-friendly) |
| `.dxf` | CAD interchange |
| `.dwg` | Native CAD (if applicable) |

See [Q100-61-STD-EXPORT-SETTINGS.md](./Q100-61-STD-EXPORT-SETTINGS.md) for export specifications.

---

## 5. References

- ASME Y14.100 — Engineering Drawing Practices
- ISO 128 — Technical Drawings — General Principles
- ASME Y14.5 — Dimensioning and Tolerancing
- ISO 1101 — Geometrical Tolerancing
- [AMPEL360_ASSETS_STANDARD.md](../../../../../../../../AMPEL360_ASSETS_STANDARD.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
