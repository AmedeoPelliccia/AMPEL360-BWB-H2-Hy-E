# 61-20_Subsystems — ATA 61 EDF Propulsor Subsystems

## Purpose

Functional subsystems for Electric Ducted Fan (EDF) propulsors (design-driven).

## Scope

This is a **cross-ATA root bucket** present in every ATA chapter. For ATA 61, it provides the structure for EDF nacelle subsystems including electric motors, ducted fans, control units, cooling systems, and health monitoring.

## EDF Subsystems

The following subsystems are defined for the AMPEL360 Q100 distributed propulsion system:

| Subsystem ID | Name | Description |
|--------------|------|-------------|
| [61-20-01](61-20-01_Electric_Motor/) | Electric Motor | 4 MW motor per propulsor |
| [61-20-02](61-20-02_Ducted_Fan/) | Ducted Fan | Fan rotor/stator unit |
| [61-20-03](61-20-03_Blade_System/) | Blade System | Blades, materials, aero profiling |
| [61-20-04](61-20-04_Propulsor_Control_Unit/) | Propulsor Control Unit | PCU hardware |
| [61-20-05](61-20-05_Cooling_Loop/) | Cooling Loop | Oil/liquid/cryo cooling interface |
| [61-20-06](61-20-06_Health_Sensing/) | Health Sensing | Vibration, strain, temperature, EM sensors |

## Internal Structure

The internal structure of this bucket is **design-driven** and flexible:
- Organize contents based on how systems are conceived, designed, and implemented
- No mandatory 01-14 lifecycle duplication within buckets
- Maintain traceability to lifecycle phases via metadata or index files

## Naming Convention

Items within this bucket follow the pattern:
- **61-20-XX_DESCRIPTION**
  - 61 = ATA chapter
  - 20 = Bucket number
  - XX = Sequential number (01, 02, 03, etc.)
  - DESCRIPTION = Descriptive name

## Key Interfaces

The EDF subsystems interface with:
- **ATA 24**: Electrical power supply
- **ATA 28**: Fuel system (cryogenic interface)
- **ATA 45**: Central maintenance system
- **ATA 72**: Engine/propulsion integration
- **ATA 76**: Engine controls
- **ATA 95**: Digital Product Passport

## Status

- **Bucket**: 20_Subsystems
- **Status**: Active
- **Applicability**: ATA 61 (Propellers/Propulsors)
- **Last Updated**: 2025-12-01

## Document Control

- **Standard**: OPT-IN Framework v1.1
- **Owner**: AMPEL360 Propulsion Team

---

**Note**: This bucket contains EDF propulsor subsystem definitions for the AMPEL360 Q100 hydrogen-electric aircraft.
