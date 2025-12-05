# FAN_ASSEMBLY

**Assembly ID**: 61-00-04-A410  
**Version**: 1.0  
**Status**: DRAFT

## Purpose

Fan blade, hub, and spinner assembly for the open-fan propulsor. Includes composite fan blades with variable pitch capability and optimized aerodynamic design.

## Components

| Component | Description |
|-----------|-------------|
| Fan Blades | High-efficiency composite blades (qty TBD) |
| Hub Assembly | Central mounting hub with pitch bearings |
| Spinner | Aerodynamic nose cone |
| Pitch Mechanism | Variable pitch actuation (if applicable) |
| Retention System | Blade root retention hardware |

## Part References

```
../../../../../PARTS/
```

## CAD Structure

```
CAD/
├── PRODUCTS/          # Native CAD assembly files
│   ├── CATIA/        # FAN_ASSY.CATProduct
│   ├── SOLIDWORKS/   # FAN_ASSY.sldasm
│   └── NX/           # FAN_ASSY.prt
├── NEUTRAL/          # FAN_ASSY.step, .jt
├── VISUALIZATION/    # Lightweight viewing files
└── RENDERS/          # Visual documentation
```

## CAD Naming Convention

```
FAN_[COMPONENT]_ASSY.[extension]
```

Examples:

- `FAN_ASSY.CATProduct` — Complete fan assembly
- `FAN_HUB_ASSY.sldasm` — Hub subassembly
- `FAN_BLADE_ASSY.step` — Single blade assembly (neutral)

## Interface Points

- **Hub to Gearbox**: Spline coupling to gearbox output shaft
- **Blade to Hub**: Blade root retention system
- **Spinner**: Forward spinner attachment
- **Pitch Control**: Pitch actuation linkages (if variable pitch)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
