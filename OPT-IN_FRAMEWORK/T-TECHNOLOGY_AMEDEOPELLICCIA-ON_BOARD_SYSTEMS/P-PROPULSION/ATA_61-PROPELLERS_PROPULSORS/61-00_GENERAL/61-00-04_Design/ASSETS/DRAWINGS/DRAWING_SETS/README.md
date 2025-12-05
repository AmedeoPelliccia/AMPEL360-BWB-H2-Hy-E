# DRAWING_SETS — ATA 61 Propellers/Propulsors

## Overview

Drawing sets organize related drawings into logical groups that support specific phases, systems, or deliverables. Each set is self-contained with its own scope, drawing list, and revision status.

## Available Sets

| Set ID           | Name                     | OPT-IN Buckets | Status |
|------------------|--------------------------|----------------|--------|
| Q100-61-SET-OFP  | Open Fan Propulsor Set   | 61-20_Subsystems, 61-50_Structures, 61-70_Propulsion | Active |
| Q100-61-SET-EMD  | Electric Motor Drive Set | 61-40_Software, 61-80_Energy | Active |
| Q100-61-SET-PV   | Propeller Variants Set   | 61-20_Subsystems | Active |
| Q100-61-SET-MNT  | Mounting System Set      | 61-50_Structures | Active |
| Q100-61-SET-FPS  | Full Propulsor System Set| 61-00_GENERAL, 61-70_Propulsion, 61-90_Tables_Schemas_Diagrams | Active |

## Master Index

The master index is maintained in [Q100-61-SET-MASTER-INDEX.yaml](./Q100-61-SET-MASTER-INDEX.yaml).

## Set Structure

Each drawing set folder contains:

```
Q100-61-SET-[ID]/
├── README.md          # Set overview and purpose
├── set_definition.yaml # YAML definition with scope and metadata
└── drawing_list.md     # List of drawings in this set
```

## Usage

1. Locate the appropriate set for your drawing based on system/subsystem
2. Review the set's `README.md` for scope and guidelines
3. Add new drawings following the naming convention in `set_definition.yaml`
4. Update `drawing_list.md` when adding or removing drawings

## Related Documentation

- [DRAWINGS README](../README.md)
- [Naming Convention](../DRAWING_STANDARDS/Q100-61-STD-NAMING-CONVENTION.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
