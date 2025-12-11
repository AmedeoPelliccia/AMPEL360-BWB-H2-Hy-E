# DWG-10-000-004 — Drawing Templates

**Document ID:** DWG-10-000-004  
**Title:** Drawing Templates  
**ATA Chapter:** 10 – Parking, Mooring, Storage, RTS  
**Status:** DRAFT  
**Version:** A  
**Date:** 2025-12-09

---

## 1. Purpose

This document provides standard templates for ATA 10 drawings in the Q100 (AMPEL360) aircraft project.

---

## 2. Available Templates

### 2.1 Template by Drawing Size

| Template ID | Size | File | Description |
|-------------|------|------|-------------|
| TPL-10-A0 | A0 | A0_Template.svg | General arrangements |
| TPL-10-A1 | A1 | A1_Template.svg | System schematics |
| TPL-10-A2 | A2 | A2_Template.svg | Detail drawings |
| TPL-10-A3 | A3 | A3_Template.svg | Component details |
| TPL-10-A4 | A4 | A4_Template.svg | Labels, simple details |

### 2.2 Template by Drawing Type

| Template ID | Type | File | Description |
|-------------|------|------|-------------|
| TPL-10-GA | General Arrangement | GA_Template.svg | Layout drawings |
| TPL-10-DET | Detail | DET_Template.svg | Component details |
| TPL-10-ASY | Assembly | ASY_Template.svg | Assembly drawings |
| TPL-10-SCH | Schematic | SCH_Template.svg | System diagrams |
| TPL-10-ZON | Zone | ZON_Template.svg | Safety zones |
| TPL-10-LBL | Label | LBL_Template.svg | Warning labels |

---

## 3. Template Elements

### 3.1 Standard Title Block

All templates include a standard title block containing:

```
┌─────────────────────────────────────────────────────────────┐
│ Q100 - AMPEL360 BWB-H2-Hy-E                                 │
├─────────────────────────────────────────────────────────────┤
│ DRAWING NUMBER: Q100-10-XXXX-XXX-XXX                       │
│ TITLE: [Drawing Title]                                      │
│ TYPE: [GA/DET/ASY/INS/SCH/ZON/SAF/LBL/FLW/CHK/LOC/OPR]    │
├─────────────────────────────────────────────────────────────┤
│ REVISION: [A-Z or 0-99]    DATE: YYYY-MM-DD                │
│ SIZE: [A0/A1/A2/A3/A4]     SCALE: [1:1, 1:2, NTS, etc.]    │
│ CREATED BY:                APPROVED BY:                     │
├─────────────────────────────────────────────────────────────┤
│ ☢ H₂ RELATED: [ ]    ⚡ HV RELATED: [ ]    🔴 CRITICAL: [ ] │
│ CLASSIFICATION: [Unclassified/Internal/Confidential]        │
├─────────────────────────────────────────────────────────────┤
│ REVISION HISTORY:                                           │
│ Rev | Date       | Description              | Author        │
│ ────┼────────────┼──────────────────────────┼──────────────│
│  0  | YYYY-MM-DD | Initial release          | [Name]       │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Drawing Border

- Continuous thick line (0.7mm)
- 20mm margin on A0-A2
- 10mm margin on A3-A4
- Zone markings along edges (A-Z horizontal, 1-20 vertical)

### 3.3 Reference Grid

Optional reference grid for complex drawings:
- 10mm or 20mm grid spacing
- Thin gray lines (0.15mm)
- Non-printing layer option

---

## 4. Layer Structure

### 4.1 Standard Layers

| Layer Name | Purpose | Line Weight | Color |
|------------|---------|-------------|-------|
| 0-Border | Drawing border and title block | 0.7mm | Black |
| 1-Geometry | Main drawing geometry | 0.5mm | Black |
| 2-Dimensions | Dimensions and annotations | 0.25mm | Black |
| 3-Hatching | Section hatching | 0.15mm | Black |
| 4-Hidden | Hidden lines | 0.35mm | Gray |
| 5-Center | Center lines | 0.25mm | Blue |
| 6-H2-System | H₂ system components | 0.5mm | Red |
| 7-HV-System | High-voltage components | 0.5mm | Orange |
| 8-Safety | Safety zones and warnings | 0.5mm | Yellow |
| 9-Notes | Notes and callouts | 0.25mm | Black |
| 10-Grid | Reference grid | 0.15mm | Light Gray |

### 4.2 Layer Naming Convention

```
[Number]-[Name]-[Revision]

Example:
6-H2-System-A
7-HV-System-B
```

---

## 5. Standard Symbols Library

### 5.1 Safety Symbols

Templates include standard ISO 7010 symbols:
- Warning signs (triangular yellow)
- Prohibition signs (circular red)
- Mandatory action signs (circular blue)
- Emergency equipment signs (square green)

### 5.2 Component Symbols

Standard symbols for:
- Valves (ball, butterfly, check, relief)
- Sensors (temperature, pressure, flow)
- Electrical components (switches, contactors, breakers)
- Connectors (H₂, HV, data)

### 5.3 Annotation Symbols

- Revision cloud
- Revision triangle
- Detail callout circle
- Section cut line
- Break line
- Centerline

---

## 6. Text Styles

### 6.1 Standard Text Heights

| Purpose | Height (mm) | Font |
|---------|-------------|------|
| Title | 7.0 | Arial Bold |
| Heading | 5.0 | Arial Bold |
| Body text | 3.5 | Arial |
| Dimensions | 3.0 | Arial |
| Notes | 2.5 | Arial |
| Small notes | 2.0 | Arial |

### 6.2 Text Alignment

- Left-aligned for general notes
- Center-aligned for titles
- Right-aligned for dimensions
- Justified for long text blocks

---

## 7. Template Usage Instructions

### 7.1 Starting a New Drawing

1. Copy appropriate template file
2. Rename following naming convention
3. Fill in title block fields
4. Set appropriate scale
5. Configure layers as needed
6. Begin drawing on appropriate layers

### 7.2 Exporting Drawings

1. Save master file in SVG format
2. Export to PDF for distribution
3. Include metadata JSON file
4. Update revision history
5. Commit to version control

---

## 8. Template Maintenance

- Templates maintained by Configuration Management
- Changes require approval
- Version controlled with drawings
- Annual review and update cycle

---

## 9. Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.**
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-12-09

---
