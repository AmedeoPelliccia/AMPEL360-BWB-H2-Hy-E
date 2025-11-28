# 57-20_Subsystems

**Version:** 1.1  
**Date:** 2025-11-28  
**Status:** Active

---

## Purpose

This layer contains the **physical wing subsystems**, each with a complete 14-step lifecycle documentation structure. Unlike 57-00_GENERAL (which covers the wing globally) or 57-10_Operations (which is a lean operational chapter), 57-20_Subsystems replicates the lifecycle per subsystem.

---

## Scope

This is a **cross-ATA root bucket** for ATA 57 (Wings). It provides dedicated lifecycle documentation for each physically distinct wing subsystem.

---

## Structure

```
57-20_Subsystems/
├── 57-20-00_Subsystems_Overview/
│   ├── 57-20-00-01_Overview.md
│   ├── 57-20-00-02_Scope_and_Methodology.md
│   └── 57-20-00-03_Subsystems_Index.md
│
├── 57-21_FLAPS/
├── 57-22_SPOILERS/
├── 57-23_AILERONS/
├── 57-24_SLATS/
├── 57-25_WING_STRUCTURE/
├── 57-26_FUEL_TANKS/
├── 57-27_H2_WING_INTEGRATION/
├── 57-28_WING_ICE_PROTECTION/
└── 57-29_WING_SENSORS_ACTUATION/
```

Each subsystem folder (`57-2x_<NAME>`) contains:
- `57-2x_GENERAL-<NAME>/` — 14 lifecycle files (01-14)
- `ASSETS/` — Diagrams, installations, and exports

---

## Subsystems

| ID | Subsystem | Description |
|----|-----------|-------------|
| [57-21](57-21_FLAPS/README.md) | FLAPS | Trailing edge high-lift devices |
| [57-22](57-22_SPOILERS/README.md) | SPOILERS | Lift-dump and speed brake devices |
| [57-23](57-23_AILERONS/README.md) | AILERONS | Roll control surfaces |
| [57-24](57-24_SLATS/README.md) | SLATS | Leading edge high-lift devices |
| [57-25](57-25_WING_STRUCTURE/README.md) | WING_STRUCTURE | Primary wing structure |
| [57-26](57-26_FUEL_TANKS/README.md) | FUEL_TANKS | Wing fuel storage |
| [57-27](57-27_H2_WING_INTEGRATION/README.md) | H2_WING_INTEGRATION | Hydrogen integration |
| [57-28](57-28_WING_ICE_PROTECTION/README.md) | WING_ICE_PROTECTION | Ice protection systems |
| [57-29](57-29_WING_SENSORS_ACTUATION/README.md) | WING_SENSORS_ACTUATION | Sensors and actuation |

---

## 14-Step Lifecycle (per subsystem)

Each subsystem follows the canonical lifecycle:

| Phase | Name | Purpose |
|-------|------|---------|
| 01 | Overview | ATA domain description and architecture |
| 02 | Safety | Safety framework and analysis |
| 03 | Requirements | Requirements and traceability |
| 04 | Design | Design specifications |
| 05 | Interfaces | Interface control documents |
| 06 | Engineering | Analysis, models, simulation |
| 07 | V_AND_V | Verification and validation |
| 08 | Prototyping | Prototype development |
| 09 | Production_Planning | Manufacturing planning |
| 10 | Certification | Certification evidence |
| 11 | EIS_Versions_Tags | Configuration management |
| 12 | Services | Maintenance and service |
| 13 | Subsystems_Components | Component breakdown |
| 14 | Ops_Std_Sustain | Operational standards |

---

## Relationship to Other 57-XX Layers

| Layer | Purpose | Lifecycle |
|-------|---------|-----------|
| [57-00_GENERAL](../57-00_GENERAL/) | Global wing governance | Full 14-folder lifecycle |
| [57-10_Operations](../57-10_Operations/) | Operational chapter | Lean (no lifecycle repetition) |
| **57-20_Subsystems** | Physical subsystems | Full 14-folder lifecycle per subsystem |

---

## Naming Convention

| Element | Pattern | Example |
|---------|---------|---------|
| Subsystem folder | `57-2x_<NAME>` | `57-21_FLAPS` |
| GENERAL folder | `57-2x_GENERAL-<NAME>` | `57-21_GENERAL-FLAPS` |
| Lifecycle file | `57-2x-YY_<Phase>.md` | `57-21-01_Overview.md` |

---

## Status

- **Bucket**: 20_Subsystems
- **Status**: Active
- **Applicability**: ATA 57 (Wings)
- **Last Updated**: 2025-11-28

---

## Document Control

- **Standard**: OPT-IN Framework v1.2
- **Owner**: AMPEL360 Documentation WG
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **ACTIVE** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
