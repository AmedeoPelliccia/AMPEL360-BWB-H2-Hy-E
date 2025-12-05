# MOTOR_COMPONENTS — ATA 61 Parts

## Overview

This directory contains individual part definitions for electric motor components used in the hybrid electric propulsion system of the AMPEL360 BWB H2 Hy-E aircraft. The high-power electric motor is the primary propulsion driver.

## Parts Inventory

| Part ID | Name | Description | Status |
|---------|------|-------------|--------|
| Q100-61-PRT-MOTOR-STATOR-CORE | Stator Core | Laminated silicon steel stator core | Draft |
| Q100-61-PRT-MOTOR-STATOR-WINDING | Stator Winding | Concentrated or distributed winding assembly | Draft |
| Q100-61-PRT-MOTOR-ROTOR-CORE | Rotor Core | Laminated rotor core with magnet pockets | Draft |
| Q100-61-PRT-MOTOR-ROTOR-MAGNET | Rotor Magnet | Rare-earth permanent magnets (NdFeB) | Draft |
| Q100-61-PRT-MOTOR-HOUSING | Motor Housing | Main housing with cooling jacket integration | Draft |
| Q100-61-PRT-MOTOR-END-BELL-DE | End Bell (Drive End) | Drive-end bearing housing | Draft |
| Q100-61-PRT-MOTOR-END-BELL-NDE | End Bell (Non-Drive End) | Non-drive-end bearing housing with resolver | Draft |
| Q100-61-PRT-MOTOR-SHAFT | Motor Shaft | High-speed main shaft | Draft |
| Q100-61-PRT-MOTOR-COOLING-JACKET | Cooling Jacket | Liquid cooling jacket for thermal management | Draft |

## Technical Overview

### Motor Type

- **Configuration**: Permanent Magnet Synchronous Motor (PMSM)
- **Magnet Arrangement**: Interior Permanent Magnet (IPM) or Surface Mount (SPM)
- **Power Class**: Megawatt-class for propulsion

### Stator Core (Q100-61-PRT-MOTOR-STATOR-CORE)

- **Material**: Non-oriented silicon steel laminations (e.g., M19 or Hiperco)
- **Features**:
  - Laser-cut or stamped laminations
  - Stacked and bonded assembly
  - Slot geometry optimized for winding
  - Press-fit or shrink-fit to housing

### Stator Winding (Q100-61-PRT-MOTOR-STATOR-WINDING)

- **Type**: Distributed or concentrated winding
- **Conductor**: Litz wire or rectangular bar (hairpin)
- **Features**:
  - High fill factor design
  - Class H or higher insulation
  - VPI (Vacuum Pressure Impregnation) treatment
  - Thermal sensors embedded

### Rotor Core (Q100-61-PRT-MOTOR-ROTOR-CORE)

- **Material**: Non-oriented silicon steel laminations
- **Features**:
  - Magnet pockets for IPM configuration
  - Flux barriers for saliency optimization
  - Balance holes
  - Keyway or interference fit to shaft

### Rotor Magnet (Q100-61-PRT-MOTOR-ROTOR-MAGNET)

- **Material**: Neodymium-Iron-Boron (NdFeB) - N42SH or higher grade
- **Features**:
  - High-temperature grade for thermal stability
  - Segmented for eddy current reduction
  - Protective coating (nickel or epoxy)
  - Magnetized after assembly

### Motor Housing (Q100-61-PRT-MOTOR-HOUSING)

- **Material**: Cast aluminum alloy (A356-T6)
- **Features**:
  - Integral cooling jacket passages
  - Stator bore (precision machined)
  - Mounting flange interface
  - Terminal box provisions

### End Bells (Q100-61-PRT-MOTOR-END-BELL-DE/NDE)

- **Material**: Cast aluminum alloy
- **Features**:
  - Bearing housing (precision bored)
  - Seal grooves for oil/grease seals
  - Resolver/encoder mounting (NDE)
  - Shaft grounding provisions

### Motor Shaft (Q100-61-PRT-MOTOR-SHAFT)

- **Material**: High-strength steel (4340 or equivalent)
- **Features**:
  - Hollow bore (if required for weight reduction)
  - Precision ground bearing journals
  - Spline interface to gearbox
  - Dynamic balancing

### Cooling Jacket (Q100-61-PRT-MOTOR-COOLING-JACKET)

- **Type**: Liquid-cooled (glycol-water or dielectric fluid)
- **Features**:
  - Spiral or axial flow channels
  - O-ring sealed interfaces
  - Port fittings for coolant lines
  - Flow optimization for uniform cooling

## Thermal Management

- Coolant inlet temperature: TBD °C
- Maximum winding temperature: 180°C (Class H)
- Continuous power rating at design point: TBD MW

## Assembly References

These parts are used in the following assemblies:

- `../ASSEMBLIES/ELECTRIC_MOTOR_DRIVE/MOTOR_ASSEMBLY/`
- `../ASSEMBLIES/FULL_PROPULSOR_SYSTEM/`

## Related Documents

- [Parts README](../README.md)
- [Motor Assembly](../../ASSEMBLIES/ELECTRIC_MOTOR_DRIVE/MOTOR_ASSEMBLY/README.md)
- [ATA 61 Overview](../../../../../README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
