# COUNTER_ROTATING_ASSEMBLY

**Assembly ID**: 61-00-04-A461  
**Version**: 1.0  
**Status**: DRAFT

## Purpose

Counter-rotating propeller assembly for the AMPEL360 BWB H2 Hy-E aircraft. Dual propeller configuration with blades rotating in opposite directions for improved efficiency and torque cancellation.

## Design Features

| Feature | Benefit |
|---------|---------|
| Torque Cancellation | Eliminates yaw moment from engine torque |
| Swirl Recovery | Rear stage recovers energy from front stage swirl |
| Higher Efficiency | Improved propulsive efficiency vs. single rotation |
| Compact Installation | Achieves high thrust in smaller diameter |

## Components

| Component | Description |
|-----------|-------------|
| Forward Propeller | Front stage propeller with hub |
| Aft Propeller | Rear stage propeller with hub |
| Differential Gearbox | Epicyclic gear for counter-rotation |
| Blade Pitch Mechanism | Independent pitch control per stage |
| Inter-stage Fairing | Aerodynamic cover between stages |

## Part References

```
../../../../../PARTS/
```

## CAD Structure

```
CAD/
├── PRODUCTS/          # Native CAD assembly files
│   ├── CATIA/        # COUNTER_ROT_ASSY.CATProduct
│   ├── SOLIDWORKS/   # COUNTER_ROT_ASSY.sldasm
│   └── NX/           # COUNTER_ROT_ASSY.prt
├── NEUTRAL/          # COUNTER_ROT_ASSY.step, .jt
├── VISUALIZATION/    # Lightweight viewing files
└── RENDERS/          # Visual documentation
```

## CAD Naming Convention

```
COUNTER_ROT_[COMPONENT]_ASSY.[extension]
```

Examples:

- `COUNTER_ROT_ASSY.CATProduct` — Complete counter-rotating assembly
- `COUNTER_ROT_FWD_PROP_ASSY.sldasm` — Forward propeller subassembly
- `COUNTER_ROT_AFT_PROP_ASSY.step` — Aft propeller assembly (neutral)

## Interface Points

- **Gearbox Input**: Coupling from electric motor
- **Forward Stage**: Forward propeller attachment
- **Aft Stage**: Aft propeller attachment
- **Pitch Control**: Dual pitch actuation systems

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
