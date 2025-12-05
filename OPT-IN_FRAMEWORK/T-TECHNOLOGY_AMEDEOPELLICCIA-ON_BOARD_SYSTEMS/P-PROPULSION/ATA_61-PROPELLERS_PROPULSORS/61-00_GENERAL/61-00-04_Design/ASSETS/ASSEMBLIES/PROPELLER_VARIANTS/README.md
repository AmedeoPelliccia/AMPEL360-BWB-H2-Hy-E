# PROPELLER_VARIANTS Assembly

**Assembly ID**: 61-00-04-A460  
**Version**: 1.0  
**Status**: DRAFT

## Purpose

Alternative propeller configurations for the AMPEL360 BWB H2 Hy-E aircraft. Contains variant designs that may be used in different mission profiles or as design alternatives.

## Variant Overview

### Counter-Rotating Propeller (61-00-04-A461)

Dual propeller configuration with blades rotating in opposite directions to:

- Cancel torque effects
- Improve propulsive efficiency
- Reduce swirl losses

### Variable Pitch Propeller (61-00-04-A462)

Single propeller with adjustable blade pitch for:

- Optimal efficiency across flight envelope
- Reverse thrust capability
- Feathering for engine-out scenarios

## Sub-Assemblies

| Assembly ID | Name | Description |
|-------------|------|-------------|
| 61-00-04-A461 | COUNTER_ROTATING_ASSEMBLY | Dual counter-rotating propeller system |
| 61-00-04-A462 | VARIABLE_PITCH_ASSEMBLY | Variable pitch mechanism and control |

## Design Considerations

| Variant | Pros | Cons |
|---------|------|------|
| Counter-Rotating | Higher efficiency, no torque reaction | Complexity, weight, noise |
| Variable Pitch | Operational flexibility, feathering | Mechanism complexity, maintenance |

## Part References

Parts are located in:

```
../../../../PARTS/
```

Key part categories:

- Propeller blades (composite, metal leading edge)
- Hub assemblies
- Pitch control mechanisms
- Actuators and linkages
- Bearings and seals

## Interface Points

- **Gearbox**: Connection to reduction gearbox output
- **Control**: Pitch control signals and feedback
- **Sensing**: RPM, blade angle, vibration sensors

## CAD Subdirectory

See `COUNTER_ROTATING_ASSEMBLY/CAD/`, `VARIABLE_PITCH_ASSEMBLY/CAD/` for native CAD files.

## Related Documents

- [Counter-Rotating Assembly](COUNTER_ROTATING_ASSEMBLY/README.md)
- [Variable Pitch Assembly](VARIABLE_PITCH_ASSEMBLY/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
