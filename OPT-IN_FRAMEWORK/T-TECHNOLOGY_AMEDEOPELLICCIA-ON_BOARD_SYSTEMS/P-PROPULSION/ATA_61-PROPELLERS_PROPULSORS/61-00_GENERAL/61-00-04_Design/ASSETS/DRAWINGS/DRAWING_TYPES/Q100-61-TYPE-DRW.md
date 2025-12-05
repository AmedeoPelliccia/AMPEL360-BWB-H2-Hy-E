# Q100-61-TYPE-DRW — Engineering Drawing Type Definition

## Overview

Engineering Drawings (DRW) are fully dimensioned technical drawings that define the geometry, materials, and manufacturing requirements for parts and assemblies.

## Purpose

- Define part geometry with precise dimensions
- Specify materials and surface finishes
- Document assembly relationships
- Provide manufacturing instructions
- Support quality inspection

## Naming Convention

```
Q100-61-DRW-[SYSTEM]-[COMPONENT]-[SEQ].svg
```

Examples:
- `Q100-61-DRW-OFP-BLADE-001.svg`
- `Q100-61-DRW-EMD-MOTOR-001.svg`
- `Q100-61-DRW-MNT-MOUNT-001.svg`

## Required Content

### Part Drawings

| Element | Required | Notes |
|---------|:--------:|-------|
| All dimensions | ✓ | Fully dimensioned |
| GD&T callouts | ✓ | Per ASME Y14.5 / ISO 1101 |
| Material specification | ✓ | With callout |
| Surface finish | ✓ | Per ISO 1302 |
| Heat treatment | As needed | When applicable |
| Protective finish | As needed | Coating, anodizing, etc. |
| Part number | ✓ | In title block |
| Drawing scale | ✓ | In title block |

### Assembly Drawings

| Element | Required | Notes |
|---------|:--------:|-------|
| All parts identified | ✓ | Item numbers |
| Parts list/BOM | ✓ | Complete bill of materials |
| Assembly dimensions | ✓ | Critical dimensions |
| Installation notes | As needed | Special instructions |
| Section views | As needed | For clarity |
| Detail views | As needed | For complex features |

## View Requirements

- Orthographic views as needed (front, top, side)
- Isometric or perspective for clarity
- Section views for internal features
- Detail views for complex areas
- Auxiliary views for angled surfaces

## Dimensioning Standards

- Use millimeters (mm) as primary unit
- Apply tolerances per ISO 2768 (general) or as specified
- GD&T per ASME Y14.5 / ISO 1101
- Reference datums clearly identified

## Related Drawing Types

| Type | Relationship |
|------|--------------|
| SCH | Referenced for electrical/hydraulic connections |
| ICD | Defines interfaces shown on DRW |
| INST | Shows installation context |

## Examples of Use

- Fan blade detail drawing
- Hub assembly drawing
- Motor housing drawing
- Mounting bracket detail

## Quality Requirements

- All dimensions verifiable
- No implied dimensions
- Complete material callout
- Traceable to requirements

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
