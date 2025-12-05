# MOUNTING_ASSEMBLY

**Assembly ID**: 61-00-04-A470  
**Version**: 1.0  
**Status**: DRAFT

## Purpose

Structural mounting and attachment assembly for propulsor integration to the AMPEL360 BWB aircraft structure. Provides load transfer, vibration isolation, and structural integrity.

## System Context

The mounting assembly connects the propulsor system to the aircraft structure:

```
                 ┌─────────────────────────────┐
                 │       Aircraft Structure     │
                 │   (BWB Wing/Body Junction)   │
                 └──────────────┬──────────────┘
                                │
                     ┌──────────┴──────────┐
                     │   MOUNTING_ASSEMBLY  │
                     │   (Pylon, Mounts,    │
                     │    Isolation)        │
                     └──────────┬──────────┘
                                │
                 ┌──────────────┴──────────────┐
                 │     PROPULSOR SYSTEM        │
                 │ (Open Fan + Electric Motor) │
                 └─────────────────────────────┘
```

## Components

| Component | Function |
|-----------|----------|
| Forward Mount | Transfers thrust and lateral loads |
| Aft Mount | Transfers vertical and torque loads |
| Vibration Isolators | Attenuates engine vibration to airframe |
| Thrust Links | Primary thrust load path |
| Fire Containment | Fire zone separation and protection |

## Key Requirements

| Requirement | Value |
|-------------|-------|
| Max Thrust Load | TBD kN |
| Max Vertical Load | TBD kN |
| Vibration Isolation | < TBD g at mount interface |
| Fire Rating | 15-minute fire containment |
| Fatigue Life | 60,000 flight cycles |

## Part References

Parts are located in:

```
../../../../PARTS/
```

Key part categories:

- Pylon structure (frames, skins, ribs)
- Mount forgings and fittings
- Vibration isolator assemblies
- Thrust links and pins
- Fire seals and blankets

## Interface Points

- **Aircraft**: Attachment to wing/body structure
- **Propulsor**: Mounting ring interfaces
- **Systems**: Passage for fuel, electrical, hydraulic lines
- **Access**: Maintenance access panels

## Design Standards

- **[CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes)** — Certification Specifications for Large Aeroplanes
- **[CS-E](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-e-engines)** — Certification Specifications for Engines
- Fatigue and damage tolerance per [AC 25.571](https://www.faa.gov/)

## CAD Subdirectory

See `CAD/` for native CAD files:

- `CAD/PRODUCTS/` — Native CAD assembly files
- `CAD/NEUTRAL/` — STEP, JT exchange formats
- `CAD/VISUALIZATION/` — STL, 3D PDF for viewing
- `CAD/RENDERS/` — PNG, GIF visual documentation

## CAD Naming Convention

```
MOUNT_[COMPONENT]_ASSY.[extension]
```

Examples:

- `MOUNT_FWD_ASSY.CATProduct`
- `MOUNT_AFT_ASSY.sldasm`
- `MOUNT_ISOLATOR_ASSY.step`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
