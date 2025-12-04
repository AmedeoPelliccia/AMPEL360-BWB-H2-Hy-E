# FULL_PROPULSOR_SYSTEM Assembly

**Assembly ID**: 61-00-04-A400  
**Version**: 1.0  
**Status**: DRAFT

## Purpose

Top-level integrated propulsion system assembly for the AMPEL360 BWB H2 Hy-E aircraft. This is the master assembly that integrates all propulsor sub-systems into a complete, flight-ready unit.

## System Overview

The FULL_PROPULSOR_SYSTEM represents the complete hybrid-electric propulsion unit:

```
┌─────────────────────────────────────────────────────────────────┐
│                    FULL_PROPULSOR_SYSTEM (A400)                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────┐    ┌────────────────────┐              │
│  │ OPEN_FAN_PROPULSOR │◄───┤ELECTRIC_MOTOR_DRIVE│              │
│  │      (A401)        │    │      (A450)         │              │
│  │  ┌─────────┐       │    │  ┌─────────┐        │              │
│  │  │   FAN   │       │    │  │  MOTOR  │        │              │
│  │  ├─────────┤       │    │  ├─────────┤        │              │
│  │  │ NACELLE │       │    │  │CONTROLLER│       │              │
│  │  ├─────────┤       │    │  ├─────────┤        │              │
│  │  │ GEARBOX │◄──────┼────┤─►│  POWER  │        │              │
│  │  └─────────┘       │    │  │  DIST   │        │              │
│  └────────────────────┘    │  └─────────┘        │              │
│                            └────────────────────┘               │
│                                                                  │
│  ┌────────────────────┐    ┌────────────────────┐              │
│  │ PROPELLER_VARIANTS │    │  MOUNTING_ASSEMBLY  │              │
│  │      (A460)        │    │      (A470)         │              │
│  └────────────────────┘    └────────────────────┘              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Constituent Assemblies

| Assembly ID | Name | Description |
|-------------|------|-------------|
| 61-00-04-A401 | OPEN_FAN_PROPULSOR | Open-fan propulsor with nacelle and gearbox |
| 61-00-04-A450 | ELECTRIC_MOTOR_DRIVE | Electric motor, controller, power distribution |
| 61-00-04-A460 | PROPELLER_VARIANTS | Alternative propeller configurations |
| 61-00-04-A470 | MOUNTING_ASSEMBLY | Structural mounting and vibration isolation |

## Key System Parameters

| Parameter | Value |
|-----------|-------|
| Propulsion Type | Hybrid-Electric (H₂ Fuel Cell + Battery) |
| Max Thrust | TBD kN |
| Fan Diameter | TBD m |
| Bypass Ratio | TBD (Open Fan) |
| Electric Power | TBD kW |
| Weight (Dry) | TBD kg |

## CAD Structure

This top-level assembly includes a DMU (Digital Mock-Up) subdirectory for:

- System-level clash detection
- Clearance verification
- Installation sequence visualization
- Maintenance access studies

```
CAD/
├── PRODUCTS/          # Native CAD assembly files
│   ├── CATIA/        # PROPULSOR_SYSTEM_TOP_ASSY.CATProduct
│   ├── SOLIDWORKS/   # PROPULSOR_SYSTEM_TOP_ASSY.sldasm
│   └── NX/           # PROPULSOR_SYSTEM_TOP_ASSY.prt
├── NEUTRAL/          # PROPULSOR_SYSTEM_TOP_ASSY.step, .jt
├── VISUALIZATION/    # Lightweight viewing files
├── RENDERS/          # Visual documentation
└── DMU/              # Digital Mock-Up files
    ├── CLASH_STUDIES/
    ├── CLEARANCE_CHECKS/
    └── INSTALLATION_SEQUENCES/
```

## Part References

All parts are referenced from:

```
../../../../PARTS/
```

## Interface Summary

### Mechanical Interfaces

- Aircraft structure mounting (via MOUNTING_ASSEMBLY)
- Accessory gearbox connections
- Inlet/exhaust ducting

### Electrical Interfaces

- HV power from fuel cell/battery system (ATA 24/28)
- Control signals from FADEC (ATA 76)
- Sensor data to health monitoring (ATA 45)

### Fluid Interfaces

- Lubrication system
- Cooling circuits
- Fire suppression (ATA 26)

## Traceability

### Requirements

- REQ-61-001: Propulsion system thrust requirements
- REQ-61-010: Electric motor integration
- REQ-61-020: Mounting and load path requirements

### Verification

- System integration testing (SIT)
- Iron bird testing
- Ground run testing
- Flight test validation

## Export Settings

### STEP Export (AP242)

```
File: PROPULSOR_SYSTEM_TOP_ASSY.step
Format: AP242 Managed Model-Based 3D Engineering
Include: Full assembly structure, colors, PMI
```

### JT Export

```
File: PROPULSOR_SYSTEM_TOP_ASSY.jt
Version: JT 10.5
LOD: Multiple levels for DMU visualization
```

## Related Documents

- [Open Fan Propulsor](OPEN_FAN_PROPULSOR/README.md)
- [Electric Motor Drive](ELECTRIC_MOTOR_DRIVE/README.md)
- [Propeller Variants](PROPELLER_VARIANTS/README.md)
- [Mounting Assembly](MOUNTING_ASSEMBLY/README.md)
- [Parts Directory](../PARTS/README.md)
- [Drawings Directory](../DRAWINGS/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
