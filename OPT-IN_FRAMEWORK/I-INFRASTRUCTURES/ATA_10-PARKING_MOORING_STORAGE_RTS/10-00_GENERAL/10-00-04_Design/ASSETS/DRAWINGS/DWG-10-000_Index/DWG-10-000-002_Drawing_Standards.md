# DWG-10-000-002 — Drawing Standards

**Document ID:** DWG-10-000-002  
**Title:** Drawing Standards  
**ATA Chapter:** 10 – Parking, Mooring, Storage, RTS  
**Status:** DRAFT  
**Version:** A  
**Date:** 2025-12-09

---

## 1. Purpose

This document defines the drawing standards and conventions for ATA 10 drawings in the Q100 (AMPEL360) aircraft project.

---

## 2. Drawing Formats

### 2.1 File Formats

All drawings shall be provided in the following formats:

- **SVG (Scalable Vector Graphics):** Primary format for all technical drawings
- **PDF:** For distribution and review purposes
- **DWG/DXF:** Optional, for CAD interchange when required

### 2.2 Drawing Sizes

Standard drawing sizes shall follow ISO 216:

| Size | Dimensions (mm) | Use Case |
|------|----------------|----------|
| A0 | 841 × 1189 | General arrangements, large assemblies |
| A1 | 594 × 841 | System schematics, zone drawings |
| A2 | 420 × 594 | Detail drawings, installations |
| A3 | 297 × 420 | Component details, checklists |
| A4 | 210 × 297 | Labels, simple details |

---

## 3. Title Block Requirements

All drawings shall include a title block containing:

- Drawing number (Q100-10-XXXX-XXX-XXX format)
- Drawing title
- Drawing type code
- Revision level
- Date
- Created by
- Approved by
- Scale
- Drawing size
- Classification level
- H₂/HV related indicator (if applicable)
- Safety critical indicator (if applicable)

---

## 4. Line Types and Weights

### 4.1 Line Weights

| Line Type | Weight | Use |
|-----------|--------|-----|
| Thick continuous | 0.7mm | Visible edges, outlines |
| Medium continuous | 0.5mm | Secondary details |
| Thin continuous | 0.25mm | Dimension lines, hatching |
| Dashed | 0.35mm | Hidden edges |
| Chain | 0.35mm | Center lines, reference lines |

### 4.2 Color Coding

For safety-critical systems:

- **Red:** H₂ systems, hazard zones
- **Orange:** High-voltage systems (800V+)
- **Yellow:** Caution areas
- **Green:** Safe zones, ground connections
- **Blue:** Electrical systems
- **Black:** General mechanical components

---

## 5. Dimensioning Standards

- All dimensions in millimeters unless otherwise specified
- Use decimal notation (e.g., 25.4, not 25,4)
- Tolerance notation: ±0.1 unless specified
- Critical dimensions shall be highlighted
- Reference dimensions in parentheses: (100)

---

## 6. Symbols and Annotations

### 6.1 Safety Symbols

Standard ISO 7010 safety symbols shall be used for:
- H₂ hazard warnings
- High-voltage warnings
- Cryogenic warnings
- Mandatory actions
- Prohibited actions
- Emergency equipment

### 6.2 Material Symbols

Standard hatching patterns per ISO 128-50:
- Steel: Diagonal lines 45°
- Aluminum: Diagonal lines 45° + 135°
- Composite: Cross-hatch
- Insulation: Wavy lines

---

## 7. Revision Control

### 7.1 Revision Levels

- Letters A-Z for production releases
- Numbers 0-99 for preliminary/draft revisions

### 7.2 Revision Indicators

- Cloud markup around changed areas
- Revision triangle with revision letter
- Revision history table in title block

---

## 8. References

- ISO 128: Technical drawings — General principles of presentation
- ISO 7010: Graphical symbols — Safety colors and safety signs
- ISO 216: Writing paper and certain classes of printed matter — Trimmed sizes
- ATA iSpec 2200: Information Standards for Aviation Maintenance

---

## 9. Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.**
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-12-09

---
