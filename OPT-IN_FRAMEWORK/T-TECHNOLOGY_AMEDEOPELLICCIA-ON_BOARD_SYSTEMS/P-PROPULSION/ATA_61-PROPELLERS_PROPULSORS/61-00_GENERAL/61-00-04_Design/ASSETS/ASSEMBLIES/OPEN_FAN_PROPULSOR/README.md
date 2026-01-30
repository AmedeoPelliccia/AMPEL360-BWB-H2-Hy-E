# OPEN_FAN_PROPULSOR Assembly

**Assembly ID**: 61-00-04-A401  
**Version**: 1.0  
**Status**: DRAFT

## Purpose

Open-fan propulsor system assembly for the AMPEL360 BWB H2 Hy-E aircraft. The open-fan design provides high bypass ratio and improved fuel efficiency compared to conventional turbofans.

## System Context

The open-fan propulsor integrates:

- High-efficiency composite fan blades
- Aerodynamically optimized nacelle
- Reduction gearbox for optimal fan speed
- Electric motor drive integration points

## Sub-Assemblies

| Assembly ID | Name | Description |
|-------------|------|-------------|
| 61-00-04-A410 | FAN_ASSEMBLY | Fan blades, hub, spinner, pitch mechanism |
| 61-00-04-A420 | NACELLE_ASSEMBLY | Nacelle structure, acoustic liners, inlet |
| 61-00-04-A430 | GEARBOX_ASSEMBLY | Reduction gearbox, bearings, lubrication |
| 61-00-04-A440 | PROPULSOR_INTEGRATION | System integration, interfaces, routing |

## Part References

Parts are located in:

```
../../../../PARTS/
```

Key part categories:

- Fan blades (composite, variable pitch)
- Hub components
- Spinner assembly
- Nacelle panels and frames
- Gearbox housing and internals

## Interface Points

- **Forward**: Nacelle inlet interface
- **Aft**: Exhaust/thrust reverser interface
- **Structural**: Mounting points to aircraft structure
- **Electrical**: Motor drive connection points
- **Fluid**: Lubrication and cooling interfaces

## CAD Subdirectory

See `FAN_ASSEMBLY/CAD/`, `NACELLE_ASSEMBLY/CAD/`, etc. for native CAD files.

## Related Documents

- [Fan Assembly](FAN_ASSEMBLY/README.md)
- [Nacelle Assembly](NACELLE_ASSEMBLY/README.md)
- [Gearbox Assembly](GEARBOX_ASSEMBLY/README.md)
- [Propulsor Integration](PROPULSOR_INTEGRATION/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
