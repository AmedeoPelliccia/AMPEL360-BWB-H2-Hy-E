# DRAWINGS — ATA 61 Propellers/Propulsors

## Overview

This directory defines **drawing sets, standards, templates, and symbol libraries** for ATA 61 — Propellers/Propulsors. Individual engineering drawings live in their respective ATA subsections (61-10, 61-20, etc.), while this `61-00` level provides:

- **Drawing Sets**: Organized collections of drawings by system/purpose
- **Drawing Standards**: Naming conventions, revision control, approval workflows
- **Templates**: Standard drawing templates (A0–A4) with AMPEL360 title blocks
- **Symbol Libraries**: Reusable SVG symbols for schematics and diagrams
- **Drawing Types**: Definitions for DRW, SCH, ICD, INST, and DIAG types

## Directory Structure

```
DRAWINGS/
├── README.md                    # This file
├── DRAWING_SETS/               # Organized drawing collections
│   ├── Q100-61-SET-MASTER-INDEX.yaml
│   ├── Q100-61-SET-OFP/        # Open Fan Propulsor Set
│   ├── Q100-61-SET-EMD/        # Electric Motor Drive Set
│   ├── Q100-61-SET-PV/         # Propeller Variants Set
│   ├── Q100-61-SET-MNT/        # Mounting System Set
│   └── Q100-61-SET-FPS/        # Full Propulsor System Set
├── DRAWING_STANDARDS/          # Standards and procedures
│   ├── Q100-61-STD-DRAWING-REQUIREMENTS.md
│   ├── Q100-61-STD-NAMING-CONVENTION.md
│   ├── Q100-61-STD-REVISION-CONTROL.md
│   ├── Q100-61-STD-APPROVAL-WORKFLOW.md
│   └── Q100-61-STD-EXPORT-SETTINGS.md
├── TEMPLATES/                  # Drawing templates
│   ├── Q100-61-TPL-A0-LANDSCAPE.svg
│   ├── Q100-61-TPL-A1-LANDSCAPE.svg
│   ├── Q100-61-TPL-A2-LANDSCAPE.svg
│   ├── Q100-61-TPL-A3-LANDSCAPE.svg
│   ├── Q100-61-TPL-A4-PORTRAIT.svg
│   ├── Q100-61-TPL-TITLE-BLOCK.svg
│   └── Q100-61-TPL-REVISION-BLOCK.svg
├── SYMBOL_LIBRARIES/           # Reusable symbols
│   ├── Q100-61-SYM-ELECTRICAL.svg
│   ├── Q100-61-SYM-HYDRAULIC.svg
│   ├── Q100-61-SYM-PNEUMATIC.svg
│   ├── Q100-61-SYM-GDT.svg
│   ├── Q100-61-SYM-WELD.svg
│   ├── Q100-61-SYM-SURFACE-FINISH.svg
│   └── Q100-61-SYM-PROPULSION.svg
└── DRAWING_TYPES/              # Drawing type definitions
    ├── Q100-61-TYPE-DRW.md
    ├── Q100-61-TYPE-SCH.md
    ├── Q100-61-TYPE-ICD.md
    ├── Q100-61-TYPE-INST.md
    └── Q100-61-TYPE-DIAG.md
```

## Naming Convention

All ATA 61 drawings follow the Q100-61 prefix scheme:

```
Q100-61-[TYPE]-[SYSTEM]-[COMPONENT].[ext]
```

### Types

| Code | Description              |
|------|--------------------------|
| DRW  | Engineering Drawing      |
| SCH  | Schematic                |
| ICD  | Interface Control Drawing|
| INST | Installation Drawing     |
| DIAG | Diagram                  |
| SET  | Drawing Set              |
| STD  | Standard                 |
| TPL  | Template                 |
| SYM  | Symbol Library           |

### Systems

| Code | Description              | OPT-IN Buckets |
|------|--------------------------|----------------|
| OFP  | Open Fan Propulsor       | 61-20_Subsystems, 61-50_Structures, 61-70_Propulsion |
| EMD  | Electric Motor Drive     | 61-40_Software, 61-80_Energy |
| PV   | Propeller Variants       | 61-20_Subsystems |
| MNT  | Mounting System          | 61-50_Structures |
| FPS  | Full Propulsor System    | 61-00_GENERAL, 61-70_Propulsion, 61-90_Tables_Schemas_Diagrams |

## Context

This structure supports the AMPEL360-BWB-H2-Hy-E hybrid BWB aircraft project (Q100 program):

- H₂ PEM fuel-cells
- Open-fan propulsors
- Closed-loop CO₂ battery for peak-power buffering
- SAF compatibility

## Related Documentation

- [AMPEL360_ASSETS_STANDARD.md](../../../../../../../AMPEL360_ASSETS_STANDARD.md)
- [ATA 61 README](../../../../README.md)
- [61-00-04 Design README](../../README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
