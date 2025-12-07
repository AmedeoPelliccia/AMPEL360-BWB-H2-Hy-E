# PROPELLER_COMPONENTS — ATA 61 Parts

## Overview

This directory contains individual part definitions for propeller system components used in the counter-rotating propeller variants of the AMPEL360 BWB H2 Hy-E aircraft. These components support variable-pitch propeller configurations.

## Parts Inventory

| Part ID | Name | Description | Status |
|---------|------|-------------|--------|
| Q100-61-PRT-PROP-BLADE-FWD | Forward Propeller Blade | Forward-rotating propeller blade | Draft |
| Q100-61-PRT-PROP-BLADE-AFT | Aft Propeller Blade | Aft-rotating propeller blade (counter-rotation) | Draft |
| Q100-61-PRT-PROP-PITCH-ACTUATOR | Pitch Actuator | Hydraulic or electric pitch change actuator | Draft |
| Q100-61-PRT-PROP-PITCH-LINK | Pitch Link | Mechanical linkage for pitch actuation | Draft |
| Q100-61-PRT-PROP-BETA-TUBE | Beta Tube | Central pitch control tube | Draft |
| Q100-61-PRT-PROP-BLADE-BEARING | Blade Bearing | Blade root pitch bearing | Draft |

## Technical Overview

### Propeller Configuration

- **Type**: Counter-rotating open rotor (CROR) or single-rotation
- **Blade Count**: TBD blades per row
- **Diameter**: TBD meters
- **Tip Speed**: Subsonic (noise-optimized)

### Forward Propeller Blade (Q100-61-PRT-PROP-BLADE-FWD)

- **Material**: Carbon fiber reinforced polymer (CFRP) composite
- **Features**:
  - Swept planform for noise reduction
  - Variable pitch root interface (±45° range typical)
  - Leading edge erosion protection (nickel or titanium sheath)
  - Lightning strike protection mesh
  - De-icing provisions (electric or hot air)

### Aft Propeller Blade (Q100-61-PRT-PROP-BLADE-AFT)

- **Material**: Carbon fiber reinforced polymer (CFRP) composite
- **Features**:
  - Counter-rotating design (opposite twist direction)
  - Aerodynamic design to capture forward row wake swirl
  - Same root interface as forward blade (common hub)
  - Clipped tips if required for noise mitigation

### Pitch Actuator (Q100-61-PRT-PROP-PITCH-ACTUATOR)

- **Type**: Hydraulic or electric linear actuator
- **Features**:
  - Force capability for full-feather pitch change
  - Redundant actuation paths
  - Position feedback (LVDT or resolver)
  - Emergency feather spring (fail-safe)
  - BITE (Built-In Test Equipment) provisions

### Pitch Link (Q100-61-PRT-PROP-PITCH-LINK)

- **Material**: High-strength steel or titanium
- **Type**: Push-pull rod with spherical bearings
- **Features**:
  - Fatigue-rated design
  - Self-aligning bearing ends
  - Quick-disconnect for maintenance
  - Load-limiting provisions

### Beta Tube (Q100-61-PRT-PROP-BETA-TUBE)

- **Material**: Steel or aluminum alloy
- **Location**: Central rotating tube on shaft axis
- **Features**:
  - Oil transfer for hydraulic actuation
  - Pitch control signal transmission
  - Rotating seal interface
  - Beta (pitch angle) position reference

### Blade Bearing (Q100-61-PRT-PROP-BLADE-BEARING)

- **Type**: Spherical roller or angular contact ball bearing
- **Features**:
  - High radial and thrust load capacity
  - Grease lubrication (sealed)
  - Wear monitoring provisions
  - Matched pair installation

## Pitch Control System

- Normal operating range: Fine pitch to feather
- Reverse thrust capability: Yes (ground operation)
- Pitch rate: TBD °/second
- Control authority: Full Authority Digital Engine Control (FADEC) interface

## Assembly References

These parts are used in the following assemblies:

- `../ASSEMBLIES/PROPELLER_VARIANTS/COUNTER_ROTATING_ASSEMBLY/`
- `../ASSEMBLIES/PROPELLER_VARIANTS/VARIABLE_PITCH_ASSEMBLY/`
- `../ASSEMBLIES/FULL_PROPULSOR_SYSTEM/`

## Related Documents

- [Parts README](../README.md)
- [Propeller Variants](../../ASSEMBLIES/PROPELLER_VARIANTS/README.md)
- [ATA 61 Overview](../../../../../README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
