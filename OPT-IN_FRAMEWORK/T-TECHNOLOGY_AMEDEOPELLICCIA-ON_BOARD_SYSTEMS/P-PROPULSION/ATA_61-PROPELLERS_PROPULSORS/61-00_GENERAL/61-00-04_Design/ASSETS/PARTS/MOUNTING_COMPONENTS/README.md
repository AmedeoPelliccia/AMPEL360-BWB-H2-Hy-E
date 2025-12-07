# MOUNTING_COMPONENTS — ATA 61 Parts

## Overview

This directory contains individual part definitions for propulsor mounting and structural attachment components used in the AMPEL360 BWB H2 Hy-E aircraft. These components provide the load path between the propulsion system and the airframe.

## Parts Inventory

| Part ID | Name | Description | Status |
|---------|------|-------------|--------|
| Q100-61-PRT-MNT-FWD-MOUNT | Forward Mount | Forward thrust and vertical load mount | Draft |
| Q100-61-PRT-MNT-AFT-MOUNT | Aft Mount | Aft vertical and lateral load mount | Draft |
| Q100-61-PRT-MNT-THRUST-LINK | Thrust Link | Primary thrust reaction link | Draft |
| Q100-61-PRT-MNT-SIDE-LINK | Side Link | Lateral load reaction link | Draft |
| Q100-61-PRT-MNT-VIBRATION-DAMPER | Vibration Damper | Elastomeric vibration isolation mount | Draft |

## Technical Overview

### Mounting Philosophy

The propulsor mounting system is designed for:
- Safe transfer of thrust, torque, and inertia loads
- Vibration isolation to minimize cabin noise
- Thermal expansion accommodation
- Quick engine change capability
- Fail-safe load paths

### Forward Mount (Q100-61-PRT-MNT-FWD-MOUNT)

- **Material**: Titanium alloy (Ti-6Al-4V) or high-strength steel
- **Location**: Forward attachment to pylon structure
- **Load Types**:
  - Vertical (weight and maneuver loads)
  - Thrust (forward and reverse)
  - Torque (partial reaction)
- **Features**:
  - Spherical bearing for angular misalignment
  - Quick-disconnect fittings
  - Fail-safe redundant load path
  - Fuse pin provisions (if required)

### Aft Mount (Q100-61-PRT-MNT-AFT-MOUNT)

- **Material**: Titanium alloy or high-strength steel
- **Location**: Aft attachment to pylon structure
- **Load Types**:
  - Vertical (weight distribution)
  - Lateral (side loads and yaw)
  - Torque reaction
- **Features**:
  - Bi-axial restraint (vertical and lateral)
  - Thermal expansion slot (axial)
  - Spherical bearing ends
  - Maintenance access provisions

### Thrust Link (Q100-61-PRT-MNT-THRUST-LINK)

- **Material**: High-strength steel (4340 or 300M)
- **Type**: Push-pull rod or A-frame configuration
- **Features**:
  - Primary thrust load path
  - Fatigue-rated design (infinite life or safe-life)
  - Spherical bearing rod ends
  - Adjustable length for alignment
  - Load indicating marks (if applicable)

### Side Link (Q100-61-PRT-MNT-SIDE-LINK)

- **Material**: High-strength steel or titanium
- **Type**: Lateral restraint link
- **Features**:
  - Lateral load reaction
  - Torque reaction contribution
  - Spherical bearing ends
  - Redundant structure (twin link or failsafe single)

### Vibration Damper (Q100-61-PRT-MNT-VIBRATION-DAMPER)

- **Type**: Elastomeric isolator mount
- **Material**: Metal-bonded rubber/elastomer
- **Features**:
  - Tuned stiffness for isolation frequency
  - Progressive rate characteristic
  - Fail-safe (snubber or backup structure)
  - Temperature-rated elastomer (-55°C to +70°C)
  - Ozone and fluid resistant

## Load Requirements

| Load Case | Forward Mount | Aft Mount | Thrust Link | Side Link |
|-----------|---------------|-----------|-------------|-----------|
| Max Thrust | Primary | Secondary | Primary | N/A |
| Max Maneuver | Primary | Primary | Secondary | Primary |
| Ground Handling | Distributed | Distributed | N/A | Primary |
| Crash | Fuse Pin | Fuse Pin | Fuse Pin | N/A |

## Assembly References

These parts are used in the following assemblies:

- `../ASSEMBLIES/MOUNTING_ASSEMBLY/`
- `../ASSEMBLIES/FULL_PROPULSOR_SYSTEM/`

## Related Documents

- [Parts README](../README.md)
- [Mounting Assembly](../../ASSEMBLIES/MOUNTING_ASSEMBLY/README.md)
- [ATA 61 Overview](../../../../../README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
