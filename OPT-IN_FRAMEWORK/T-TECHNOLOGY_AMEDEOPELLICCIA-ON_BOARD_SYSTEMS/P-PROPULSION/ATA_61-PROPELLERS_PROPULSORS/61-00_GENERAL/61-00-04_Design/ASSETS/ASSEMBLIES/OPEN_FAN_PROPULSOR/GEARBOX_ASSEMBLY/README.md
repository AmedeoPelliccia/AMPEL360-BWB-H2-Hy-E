# GEARBOX_ASSEMBLY

**Assembly ID**: 61-00-04-A430  
**Version**: 1.0  
**Status**: DRAFT

## Purpose

Reduction gearbox assembly for the open-fan propulsor. Provides speed reduction between the electric motor and the fan for optimal propulsive efficiency.

## Components

| Component | Description |
|-----------|-------------|
| Gearbox Housing | Main structural housing with mounting interfaces |
| Ring Gear | Large diameter ring gear |
| Planet Gears | Planetary gear set |
| Sun Gear | Central input gear connected to motor |
| Bearings | High-precision rolling element bearings |
| Lubrication System | Oil system components (pump, filter, sump) |

## Key Specifications

| Parameter | Value |
|-----------|-------|
| Gear Type | Planetary (epicyclic) |
| Reduction Ratio | TBD:1 |
| Input Speed | TBD RPM |
| Output Speed | TBD RPM |
| Max Torque | TBD kNm |
| Lubrication | Synthetic oil, pressure-fed |

## Part References

```
../../../../../PARTS/
```

## CAD Structure

```
CAD/
├── PRODUCTS/          # Native CAD assembly files
│   ├── CATIA/        # GEARBOX_ASSY.CATProduct
│   ├── SOLIDWORKS/   # GEARBOX_ASSY.sldasm
│   └── NX/           # GEARBOX_ASSY.prt
├── NEUTRAL/          # GEARBOX_ASSY.step, .jt
├── VISUALIZATION/    # Lightweight viewing files
└── RENDERS/          # Visual documentation
```

## CAD Naming Convention

```
GEARBOX_[COMPONENT]_ASSY.[extension]
```

Examples:

- `GEARBOX_ASSY.CATProduct` — Complete gearbox assembly
- `GEARBOX_PLANET_ASSY.sldasm` — Planet carrier subassembly
- `GEARBOX_HOUSING_ASSY.step` — Housing assembly (neutral)

## Interface Points

- **Input**: Motor shaft coupling (spline)
- **Output**: Fan hub connection (spline)
- **Mounting**: Structural attachment points
- **Lubrication**: Oil inlet/outlet ports
- **Sensors**: Temperature, pressure, chip detection

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
