# MOTOR_ASSEMBLY

**Assembly ID**: 61-00-04-A451  
**Version**: 1.0  
**Status**: DRAFT

## Purpose

High-power electric motor assembly for the AMPEL360 BWB H2 Hy-E hybrid electric propulsion system. Permanent Magnet Synchronous Motor (PMSM) designed for aviation propulsion applications.

## Components

| Component | Description |
|-----------|-------------|
| Motor Housing | Structural casing with cooling jacket |
| Stator Assembly | Wound stator with laminated core |
| Rotor Assembly | Permanent magnet rotor with shaft |
| Bearings | High-speed precision bearings |
| Cooling System | Liquid cooling manifolds and passages |
| Position Sensors | Resolver or encoder for commutation |

## Key Specifications

| Parameter | Value |
|-----------|-------|
| Motor Type | PMSM (Permanent Magnet Synchronous) |
| Rated Power | TBD kW |
| Peak Power | TBD kW |
| Max Speed | TBD RPM |
| Efficiency | > 95% at rated load |
| Cooling | Liquid cooled |

## Part References

```
../../../../../PARTS/
```

## CAD Structure

```
CAD/
├── PRODUCTS/          # Native CAD assembly files
│   ├── CATIA/        # MOTOR_ASSY.CATProduct
│   ├── SOLIDWORKS/   # MOTOR_ASSY.sldasm
│   └── NX/           # MOTOR_ASSY.prt
├── NEUTRAL/          # MOTOR_ASSY.step, .jt
├── VISUALIZATION/    # Lightweight viewing files
└── RENDERS/          # Visual documentation
```

## CAD Naming Convention

```
MOTOR_[COMPONENT]_ASSY.[extension]
```

Examples:

- `MOTOR_ASSY.CATProduct` — Complete motor assembly
- `MOTOR_STATOR_ASSY.sldasm` — Stator subassembly
- `MOTOR_ROTOR_ASSY.step` — Rotor assembly (neutral)

## Interface Points

- **Output Shaft**: Coupling to gearbox input
- **Electrical**: 3-phase power terminals, sensor connections
- **Cooling**: Coolant inlet/outlet ports
- **Mounting**: Structural attachment points

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
