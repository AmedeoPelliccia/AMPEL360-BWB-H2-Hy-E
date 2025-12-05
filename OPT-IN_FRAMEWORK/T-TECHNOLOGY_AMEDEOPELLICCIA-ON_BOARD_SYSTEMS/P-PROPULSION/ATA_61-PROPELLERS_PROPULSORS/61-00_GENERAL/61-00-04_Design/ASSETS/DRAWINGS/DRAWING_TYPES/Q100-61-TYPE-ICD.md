# Q100-61-TYPE-ICD — Interface Control Drawing Type Definition

## Overview

Interface Control Drawings (ICD) define the physical, electrical, and functional interfaces between systems or major components. They are the authoritative source for interface requirements.

## Purpose

- Define mechanical interface geometry
- Specify electrical connector pinouts
- Document functional interface requirements
- Control interface changes
- Support system integration

## Naming Convention

```
Q100-61-ICD-[SYSTEM1]-[SYSTEM2]-[SEQ].svg
```

Examples:
- `Q100-61-ICD-OFP-EMD-001.svg` (Fan to Motor interface)
- `Q100-61-ICD-MNT-NAC-001.svg` (Mount to Nacelle interface)
- `Q100-61-ICD-FPS-ATA24-001.svg` (Propulsor to Electrical Power)

## Required Content

### Mechanical Interfaces

| Element | Required | Notes |
|---------|:--------:|-------|
| Interface plane definition | ✓ | With tolerances |
| Bolt pattern geometry | ✓ | Location, size, quantity |
| Alignment features | ✓ | Pins, keys, datums |
| Clearance envelopes | ✓ | Keep-out zones |
| Sealing requirements | As needed | O-ring grooves, gaskets |
| Thermal interface | As needed | Heat transfer requirements |

### Electrical Interfaces

| Element | Required | Notes |
|---------|:--------:|-------|
| Connector type | ✓ | Part number, manufacturer |
| Pin assignments | ✓ | Complete pinout |
| Signal definitions | ✓ | Name, type, range |
| Grounding requirements | ✓ | Bonding, shielding |
| Power requirements | ✓ | Voltage, current |
| EMC requirements | As needed | Filtering, shielding |

### Fluid Interfaces

| Element | Required | Notes |
|---------|:--------:|-------|
| Port type and size | ✓ | Thread, fitting type |
| Pressure rating | ✓ | Operating and proof |
| Flow requirements | ✓ | Rate, direction |
| Fluid compatibility | ✓ | Media specification |
| Sealing | ✓ | O-ring, gasket specs |

### Functional Interfaces

| Element | Required | Notes |
|---------|:--------:|-------|
| Control signals | ✓ | Commands, feedback |
| Timing requirements | As needed | Response times |
| Data protocols | As needed | CAN, ARINC, etc. |
| Failure modes | ✓ | Interface failure handling |

## Interface Control Requirements

### Change Control

- All interface changes require ICD revision
- Both sides of interface must approve changes
- Revision tracked in revision block

### Tolerance Stack-up

- Show worst-case tolerance analysis
- Identify critical dimensions
- Document assumptions

## Layout Guidelines

1. Show both sides of interface clearly
2. Use section views for complex geometry
3. Include coordinate system reference
4. Provide dimensional details in tables

## Related Drawing Types

| Type | Relationship |
|------|--------------|
| DRW | Implements interface in hardware |
| SCH | Shows functional connections |
| INST | Shows installation context |

## Examples of Use

- Hub-to-motor mechanical interface
- Nacelle-to-pylon attachment
- Propulsor electrical connector interface
- Cooling system fluid interface

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
