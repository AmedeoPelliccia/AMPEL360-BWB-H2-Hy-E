# VARIABLE_PITCH_ASSEMBLY

**Assembly ID**: 61-00-04-A462  
**Version**: 1.0  
**Status**: DRAFT

## Purpose

Variable pitch propeller mechanism assembly for the AMPEL360 BWB H2 Hy-E aircraft. Enables blade angle adjustment for optimal efficiency across the flight envelope and provides feathering and reverse thrust capability.

## Design Features

| Feature | Benefit |
|---------|---------|
| Pitch Optimization | Best efficiency at all flight conditions |
| Feathering | Minimize drag during engine-out |
| Reverse Thrust | Ground deceleration capability |
| Fine Pitch | Improved takeoff performance |

## Components

| Component | Description |
|-----------|-------------|
| Pitch Control Mechanism | Actuator and linkage system |
| Beta Tube | Hollow shaft for pitch actuation |
| Blade Trunnions | Blade pivot bearings |
| Pitch Lock | Safety mechanism to prevent over-speed |
| Position Feedback | Blade angle sensors |

## Operating Modes

| Mode | Blade Angle | Application |
|------|-------------|-------------|
| Feather | ~85° | Engine-out, minimum drag |
| Fine | ~15° | Takeoff, low speed |
| Cruise | ~30-45° | Cruise efficiency |
| Reverse | Negative | Ground deceleration |

## Part References

```
../../../../../PARTS/
```

## CAD Structure

```
CAD/
├── PRODUCTS/          # Native CAD assembly files
│   ├── CATIA/        # VAR_PITCH_ASSY.CATProduct
│   ├── SOLIDWORKS/   # VAR_PITCH_ASSY.sldasm
│   └── NX/           # VAR_PITCH_ASSY.prt
├── NEUTRAL/          # VAR_PITCH_ASSY.step, .jt
├── VISUALIZATION/    # Lightweight viewing files
└── RENDERS/          # Visual documentation
```

## CAD Naming Convention

```
VAR_PITCH_[COMPONENT]_ASSY.[extension]
```

Examples:

- `VAR_PITCH_ASSY.CATProduct` — Complete variable pitch assembly
- `VAR_PITCH_ACTUATOR_ASSY.sldasm` — Pitch actuator subassembly
- `VAR_PITCH_MECHANISM_ASSY.step` — Pitch mechanism (neutral)

## Interface Points

- **Hub**: Connection to propeller hub
- **Actuator**: Hydraulic/electric pitch actuator
- **Control**: FADEC pitch command signals
- **Feedback**: Blade angle position sensors

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
