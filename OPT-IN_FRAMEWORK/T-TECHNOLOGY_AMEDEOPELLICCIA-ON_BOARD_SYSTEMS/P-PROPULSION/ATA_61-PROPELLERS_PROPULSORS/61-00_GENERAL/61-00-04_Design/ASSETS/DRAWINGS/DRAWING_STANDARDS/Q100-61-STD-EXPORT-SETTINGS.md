# Q100-61-STD-EXPORT-SETTINGS — Export Settings Standard

## Purpose

This document defines the file format and export specifications for ATA 61 engineering drawings in the AMPEL360-BWB-H2-Hy-E project.

## Scope

Applies to all drawing exports, templates, and symbol libraries under ATA 61.

---

## 1. Primary File Formats

### 1.1 Released Drawings

| Format | Extension | Use Case |
|--------|-----------|----------|
| SVG | `.svg` | Primary released format (Git-friendly) |
| DXF | `.dxf` | CAD interchange |
| PNG | `.png` | Documentation/preview (if needed) |

### 1.2 Source Files

| Format | Extension | Use Case |
|--------|-----------|----------|
| Native CAD | `.dwg`, `.step`, etc. | CAD authoring |
| SVG | `.svg` | Vector graphics authoring |

---

## 2. SVG Export Settings

### 2.1 Required Settings

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="[paper_width_mm]mm"
     height="[paper_height_mm]mm"
     viewBox="0 0 [width] [height]">
```

### 2.2 Paper Sizes (mm)

| Size | Width | Height |
|------|-------|--------|
| A0 | 1189 | 841 |
| A1 | 841 | 594 |
| A2 | 594 | 420 |
| A3 | 420 | 297 |
| A4 Portrait | 210 | 297 |
| A4 Landscape | 297 | 210 |

### 2.3 SVG Options

| Setting | Value |
|---------|-------|
| Embed fonts | Yes |
| Convert text to paths | For release versions |
| Image embedding | Embed, do not link |
| Decimal precision | 3 decimal places |
| Color space | sRGB |

---

## 3. Line Weights

### 3.1 Standard Line Weights

| Line Type | Weight (mm) | Use |
|-----------|-------------|-----|
| Thin | 0.18 | Dimension lines, hatching |
| Medium | 0.35 | Hidden lines, center lines |
| Thick | 0.50 | Visible outlines |
| Extra Thick | 0.70 | Cutting planes, borders |

### 3.2 SVG Stroke Widths

```css
.thin { stroke-width: 0.18; }
.medium { stroke-width: 0.35; }
.thick { stroke-width: 0.50; }
.extra-thick { stroke-width: 0.70; }
```

---

## 4. Colors

### 4.1 Standard Colors

| Purpose | Hex Code | Name |
|---------|----------|------|
| Primary lines | `#000000` | Black |
| Dimension lines | `#000000` | Black |
| Center lines | `#000000` | Black |
| Construction | `#808080` | Gray |
| Title block text | `#000000` | Black |
| Border | `#000000` | Black |

### 4.2 Color Printing

All released drawings shall be printable in black and white without loss of information.

---

## 5. Text Settings

### 5.1 Standard Fonts

| Priority | Font |
|----------|------|
| Primary | Arial |
| Secondary | Helvetica |
| Fallback | sans-serif |

### 5.2 Text Heights

| Use | Height (mm) |
|-----|-------------|
| Title | 5.0 |
| Drawing Number | 4.0 |
| Dimensions | 2.5 |
| Notes | 2.5 |
| Annotations | 2.0 |

---

## 6. DXF Export Settings

### 6.1 AutoCAD Compatibility

| Setting | Value |
|---------|-------|
| DXF Version | AutoCAD 2018 (R2018) |
| Units | Millimeters |
| Decimal precision | 4 |

### 6.2 Layer Mapping

| Layer | Purpose |
|-------|---------|
| 0 | Default |
| VISIBLE | Visible outlines |
| HIDDEN | Hidden lines |
| CENTER | Center lines |
| DIMENSION | Dimensions |
| TEXT | Annotations |
| BORDER | Drawing border |
| TITLEBLOCK | Title block |

---

## 7. PNG Export Settings

### 7.1 Resolution

| Use | Resolution |
|-----|------------|
| Documentation | 150 DPI |
| High quality | 300 DPI |

### 7.2 Format

| Setting | Value |
|---------|-------|
| Color depth | 24-bit RGB |
| Compression | PNG (lossless) |
| Background | White or transparent |

---

## 8. File Naming for Exports

```
[DRAWING_ID].[ext]           # Primary file
[DRAWING_ID]_preview.png     # Preview image
[DRAWING_ID].dxf             # CAD interchange
```

---

## 9. Quality Checks

Before export, verify:

- [ ] All text is legible at intended scale
- [ ] No overlapping elements
- [ ] All layers are visible that should be
- [ ] Line weights are correct
- [ ] File size is reasonable (< 10MB for SVG)

---

## 10. References

- ISO 128 — Technical Drawings
- [Q100-61-STD-DRAWING-REQUIREMENTS.md](./Q100-61-STD-DRAWING-REQUIREMENTS.md)
- SVG 1.1 Specification (W3C)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
