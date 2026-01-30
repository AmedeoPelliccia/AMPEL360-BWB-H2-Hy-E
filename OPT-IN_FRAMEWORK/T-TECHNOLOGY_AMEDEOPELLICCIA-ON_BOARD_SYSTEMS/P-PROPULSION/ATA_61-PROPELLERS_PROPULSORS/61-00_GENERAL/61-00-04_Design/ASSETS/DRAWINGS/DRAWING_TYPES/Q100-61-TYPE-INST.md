# Q100-61-TYPE-INST — Installation Drawing Type Definition

## Overview

Installation Drawings (INST) show how components or systems are installed in their operational environment, including mounting, routing, and access provisions.

## Purpose

- Define component mounting location
- Show wire/tube/hose routing
- Identify access panels and service points
- Support maintenance planning
- Guide installation procedures

## Naming Convention

```
Q100-61-INST-[SYSTEM]-[LOCATION]-[SEQ].svg
```

Examples:
- `Q100-61-INST-EMD-NACELLE-001.svg` (Motor in nacelle)
- `Q100-61-INST-OFP-HUB-001.svg` (Blade installation)
- `Q100-61-INST-FPS-PYLON-001.svg` (Propulsor on pylon)

## Required Content

### All Installation Drawings

| Element | Required | Notes |
|---------|:--------:|-------|
| Component location | ✓ | Position in structure |
| Mounting hardware | ✓ | Fasteners, brackets |
| Clearance envelopes | ✓ | For operation and maintenance |
| Access requirements | ✓ | Panels, doors |
| Reference structure | ✓ | Adjacent components |
| Installation sequence | As needed | When order matters |

### Mechanical Installation

| Element | Required | Notes |
|---------|:--------:|-------|
| Torque values | ✓ | For all fasteners |
| Alignment requirements | ✓ | Shim, adjust |
| Support points | ✓ | Jack points, lifting |
| Weight and CG | As needed | For balance |
| Vibration isolation | As needed | Mount type |

### Routing (Wire, Tube, Hose)

| Element | Required | Notes |
|---------|:--------:|-------|
| Routing path | ✓ | Complete path shown |
| Support/clamp locations | ✓ | All supports |
| Bend radii | ✓ | Minimum radius |
| Clearances | ✓ | From heat, moving parts |
| Connector locations | ✓ | Termination points |
| Protection | As needed | Conduit, sleeving |

## View Requirements

- Overall view showing location in aircraft/system
- Detail views for critical areas
- Section views for enclosed spaces
- Routing views (plan, elevation as needed)

## Dimensional Requirements

- Reference to aircraft/system coordinate system
- Location dimensions from datums
- Clearance dimensions
- Not typically fully dimensioned (use DRW for that)

## Installation Notes

Include as needed:
- Special tools required
- Safety precautions
- Inspection requirements
- Test requirements after installation
- Weight and balance impact

## Related Drawing Types

| Type | Relationship |
|------|--------------|
| DRW | Component detail drawings |
| ICD | Interface requirements |
| SCH | Connection routing |

## Examples of Use

- Motor installation in nacelle
- Blade installation on hub
- Controller mounting in equipment bay
- Wiring harness routing
- Hydraulic line installation

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
