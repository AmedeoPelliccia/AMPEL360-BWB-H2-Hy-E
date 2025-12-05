# SYMBOL_LIBRARIES — ATA 61 Symbol Libraries

## Overview

This directory contains reusable SVG symbol libraries for ATA 61 engineering drawings and schematics. Symbols are organized by discipline and follow industry standards.

## Available Libraries

| Library | Description | Standard Reference |
|---------|-------------|-------------------|
| [Q100-61-SYM-ELECTRICAL.svg](./Q100-61-SYM-ELECTRICAL.svg) | Electrical schematic symbols | IEC 60617 / IEEE Std 315 |
| [Q100-61-SYM-HYDRAULIC.svg](./Q100-61-SYM-HYDRAULIC.svg) | Hydraulic system symbols | ISO 1219 |
| [Q100-61-SYM-PNEUMATIC.svg](./Q100-61-SYM-PNEUMATIC.svg) | Pneumatic system symbols | ISO 1219 |
| [Q100-61-SYM-GDT.svg](./Q100-61-SYM-GDT.svg) | Geometric dimensioning & tolerancing | ASME Y14.5 / ISO 1101 |
| [Q100-61-SYM-WELD.svg](./Q100-61-SYM-WELD.svg) | Welding symbols | AWS A2.4 / ISO 2553 |
| [Q100-61-SYM-SURFACE-FINISH.svg](./Q100-61-SYM-SURFACE-FINISH.svg) | Surface finish symbols | ISO 1302 |
| [Q100-61-SYM-PROPULSION.svg](./Q100-61-SYM-PROPULSION.svg) | Propulsion-specific symbols | Q100 project standard |

## Usage

### In SVG Editors

1. Open the symbol library file
2. Copy desired symbol
3. Paste into your drawing
4. Scale as needed (preserve aspect ratio)

### Symbol Reference

Symbols can be referenced using SVG `<use>` element:

```xml
<use xlink:href="Q100-61-SYM-ELECTRICAL.svg#motor" x="100" y="100"/>
```

## Symbol Naming Convention

Within each library, symbols use this ID pattern:

```
<symbol id="[category]-[name]">
```

Examples:
- `motor-dc` — DC motor symbol
- `valve-check` — Check valve symbol
- `gdt-position` — Position tolerance symbol

## Adding New Symbols

1. Add to the appropriate library file
2. Use consistent line weights and colors
3. Include symbol ID for reference
4. Update this README if adding new categories

## Related Documentation

- [DRAWINGS README](../README.md)
- [Drawing Standards](../DRAWING_STANDARDS/README.md)
- [Templates](../TEMPLATES/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
