# Q100-61-TYPE-SCH — Schematic Drawing Type Definition

## Overview

Schematics (SCH) are functional diagrams that show the logical connections and relationships between system components using standardized symbols.

## Purpose

- Show electrical circuit topology
- Document hydraulic/pneumatic flow paths
- Define control logic
- Support troubleshooting
- Enable system analysis

## Types of Schematics

| Subtype | Description | Symbol Library |
|---------|-------------|----------------|
| Electrical | Power and signal wiring | Q100-61-SYM-ELECTRICAL |
| Hydraulic | Hydraulic system flow | Q100-61-SYM-HYDRAULIC |
| Pneumatic | Pneumatic system flow | Q100-61-SYM-PNEUMATIC |
| Control | Logic and control flow | Q100-61-SYM-ELECTRICAL |

## Naming Convention

```
Q100-61-SCH-[SYSTEM]-[SUBTYPE]-[SEQ].svg
```

Examples:
- `Q100-61-SCH-EMD-PWR-001.svg` (Power schematic)
- `Q100-61-SCH-OFP-PITCH-001.svg` (Pitch control schematic)
- `Q100-61-SCH-FPS-SYS-001.svg` (System schematic)

## Required Content

### All Schematics

| Element | Required | Notes |
|---------|:--------:|-------|
| Standard symbols | ✓ | From symbol libraries |
| Component identification | ✓ | Reference designators |
| Connection lines | ✓ | Clear, non-crossing where possible |
| Signal/flow direction | ✓ | Arrows or conventions |
| Title and drawing number | ✓ | In title block |
| Legend | As needed | For non-standard symbols |

### Electrical Schematics

| Element | Required | Notes |
|---------|:--------:|-------|
| Wire numbers | ✓ | Unique identification |
| Connector pin assignments | ✓ | For all connectors |
| Ground symbols | ✓ | Clearly indicated |
| Power distribution | ✓ | Voltage levels noted |
| Fuse/breaker ratings | ✓ | When applicable |

### Fluid Schematics (Hydraulic/Pneumatic)

| Element | Required | Notes |
|---------|:--------:|-------|
| Flow direction arrows | ✓ | On all lines |
| Pressure specifications | ✓ | Operating pressures |
| Line sizes | ✓ | Pipe/tube sizes |
| Component ratings | ✓ | Capacity, pressure |
| Filter locations | ✓ | With ratings |

## Symbol Standards

- Electrical: IEC 60617 / IEEE Std 315
- Hydraulic/Pneumatic: ISO 1219
- See [SYMBOL_LIBRARIES/](../SYMBOL_LIBRARIES/) for available symbols

## Layout Guidelines

1. Signal/flow direction: Left-to-right, top-to-bottom
2. Minimize line crossings
3. Use junction dots for connected lines
4. Group related components
5. Maintain consistent spacing

## Related Drawing Types

| Type | Relationship |
|------|--------------|
| DRW | Shows physical implementation |
| ICD | Defines interface connections |
| DIAG | High-level system view |

## Examples of Use

- Motor power circuit
- Pitch control hydraulics
- Sensor signal routing
- Emergency shutdown logic

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
