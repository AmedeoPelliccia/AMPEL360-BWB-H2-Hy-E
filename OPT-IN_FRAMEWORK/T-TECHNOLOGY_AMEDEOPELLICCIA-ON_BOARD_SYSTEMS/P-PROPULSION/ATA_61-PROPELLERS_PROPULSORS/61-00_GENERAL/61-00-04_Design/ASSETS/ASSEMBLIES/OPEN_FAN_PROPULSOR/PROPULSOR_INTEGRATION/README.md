# PROPULSOR_INTEGRATION

**Assembly ID**: 61-00-04-A440  
**Version**: 1.0  
**Status**: DRAFT

## Purpose

Integration assembly for the open-fan propulsor system. Contains interface definitions, routing paths, and integration hardware connecting all propulsor subassemblies.

## Integration Scope

| Integration Area | Description |
|-----------------|-------------|
| Structural Integration | Mounting and load path connections |
| Electrical Routing | Power and signal cable paths |
| Fluid Routing | Lubrication, cooling, fire suppression |
| Control Integration | Sensor and actuator interfaces |

## Components

| Component | Description |
|-----------|-------------|
| Interface Brackets | Mounting hardware between subassemblies |
| Wiring Harnesses | Pre-routed electrical connections |
| Fluid Lines | Pre-formed tubing assemblies |
| Fairings | Aerodynamic covers for integration areas |
| Sensors | System-level sensors and probes |

## Part References

```
../../../../../PARTS/
```

## CAD Structure

```
CAD/
├── PRODUCTS/          # Native CAD assembly files
│   ├── CATIA/        # PROPULSOR_INTEG_ASSY.CATProduct
│   ├── SOLIDWORKS/   # PROPULSOR_INTEG_ASSY.sldasm
│   └── NX/           # PROPULSOR_INTEG_ASSY.prt
├── NEUTRAL/          # PROPULSOR_INTEG_ASSY.step, .jt
├── VISUALIZATION/    # Lightweight viewing files
└── RENDERS/          # Visual documentation
```

## CAD Naming Convention

```
PROPULSOR_INTEG_[COMPONENT]_ASSY.[extension]
```

Examples:

- `PROPULSOR_INTEG_ASSY.CATProduct` — Complete integration assembly
- `PROPULSOR_INTEG_HARNESS_ASSY.sldasm` — Wiring harness assembly
- `PROPULSOR_INTEG_ROUTING_ASSY.step` — Fluid routing (neutral)

## Interface Points

- **Fan to Gearbox**: Mechanical coupling
- **Gearbox to Motor**: Drive shaft connection
- **Nacelle to Structure**: Mounting interfaces
- **Control Systems**: FADEC connections

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
