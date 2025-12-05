# NACELLE_ASSEMBLY

**Assembly ID**: 61-00-04-A420  
**Version**: 1.0  
**Status**: DRAFT

## Purpose

Nacelle structure assembly for the open-fan propulsor. Provides aerodynamic fairing, acoustic treatment, and structural support for propulsor components.

## Components

| Component | Description |
|-----------|-------------|
| Inlet Cowl | Forward nacelle section with intake lip |
| Fan Cowl | Mid-section housing fan and accessories |
| Acoustic Liners | Noise attenuation panels |
| Access Doors | Maintenance access panels |
| Thrust Reverser | Reverse thrust mechanism (if applicable) |

## Part References

```
../../../../../PARTS/
```

## CAD Structure

```
CAD/
├── PRODUCTS/          # Native CAD assembly files
│   ├── CATIA/        # NACELLE_ASSY.CATProduct
│   ├── SOLIDWORKS/   # NACELLE_ASSY.sldasm
│   └── NX/           # NACELLE_ASSY.prt
├── NEUTRAL/          # NACELLE_ASSY.step, .jt
├── VISUALIZATION/    # Lightweight viewing files
└── RENDERS/          # Visual documentation
```

## CAD Naming Convention

```
NACELLE_[COMPONENT]_ASSY.[extension]
```

Examples:

- `NACELLE_ASSY.CATProduct` — Complete nacelle assembly
- `NACELLE_INLET_ASSY.sldasm` — Inlet section subassembly
- `NACELLE_COWL_ASSY.step` — Fan cowl assembly (neutral)

## Interface Points

- **Forward**: Interface with aircraft structure/pylon
- **Fan**: Clearance to fan blade tips
- **Aft**: Exhaust/thrust reverser interface
- **Services**: Passages for electrical, fluid lines

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
