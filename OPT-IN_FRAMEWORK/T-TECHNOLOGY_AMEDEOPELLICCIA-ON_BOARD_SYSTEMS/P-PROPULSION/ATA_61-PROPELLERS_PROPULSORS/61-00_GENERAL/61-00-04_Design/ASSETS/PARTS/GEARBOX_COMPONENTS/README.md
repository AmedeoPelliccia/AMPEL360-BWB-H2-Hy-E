# GEARBOX_COMPONENTS — ATA 61 Parts

## Overview

This directory contains individual part definitions for gearbox system components used in the open-fan propulsor of the AMPEL360 BWB H2 Hy-E hybrid electric aircraft. The gearbox provides speed reduction between the electric motor and the fan.

## Parts Inventory

| Part ID | Name | Description | Status |
|---------|------|-------------|--------|
| Q100-61-PRT-GEARBOX-SUN-GEAR | Sun Gear | Central input gear of planetary gearset | Draft |
| Q100-61-PRT-GEARBOX-PLANET-GEAR | Planet Gear | Intermediate planet gears (qty per stage TBD) | Draft |
| Q100-61-PRT-GEARBOX-RING-GEAR | Ring Gear | Outer ring gear with internal teeth | Draft |
| Q100-61-PRT-GEARBOX-CARRIER | Planet Carrier | Carrier structure supporting planet gears | Draft |
| Q100-61-PRT-GEARBOX-HOUSING | Gearbox Housing | Main housing structure with oil galleries | Draft |
| Q100-61-PRT-GEARBOX-BEARING | Gearbox Bearing | Main shaft and planet bearings | Draft |

## Technical Overview

### Planetary Gear System

The reduction gearbox utilizes a planetary gear arrangement for:
- High power density
- Compact packaging
- Shared load distribution
- Coaxial input/output

### Sun Gear (Q100-61-PRT-GEARBOX-SUN-GEAR)

- **Material**: Case-hardened alloy steel (e.g., AISI 9310)
- **Features**:
  - External helical teeth
  - Spline bore for motor shaft interface
  - Ground tooth profile
  - Shot-peened roots for fatigue life

### Planet Gear (Q100-61-PRT-GEARBOX-PLANET-GEAR)

- **Material**: Case-hardened alloy steel
- **Features**:
  - Helical teeth (internal and external mesh)
  - Needle bearing bore
  - Balanced for high-speed operation

### Ring Gear (Q100-61-PRT-GEARBOX-RING-GEAR)

- **Material**: Case-hardened alloy steel
- **Features**:
  - Internal helical teeth
  - Press-fit or bolted to housing
  - Ground tooth profile

### Planet Carrier (Q100-61-PRT-GEARBOX-CARRIER)

- **Material**: High-strength steel or titanium alloy
- **Features**:
  - Planet pin bores
  - Output spline interface to fan hub
  - Balanced assembly

### Gearbox Housing (Q100-61-PRT-GEARBOX-HOUSING)

- **Material**: Cast aluminum alloy or magnesium alloy
- **Features**:
  - Oil galleries and supply ports
  - Bearing bores (line-bored)
  - Mounting flange to motor housing
  - Accessory mounting provisions

### Gearbox Bearing (Q100-61-PRT-GEARBOX-BEARING)

- **Type**: Angular contact ball or cylindrical roller
- **Features**:
  - Aerospace grade (ABEC 7 or higher)
  - Jet lubrication provisions
  - Matched pairs for preload

## Lubrication System

- Oil type: MIL-PRF-23699 or equivalent
- Jet lubrication to all mesh points
- Scavenge pump return
- Chip detection provisions

## Assembly References

These parts are used in the following assemblies:

- `../ASSEMBLIES/OPEN_FAN_PROPULSOR/GEARBOX_ASSEMBLY/`
- `../ASSEMBLIES/FULL_PROPULSOR_SYSTEM/`

## Related Documents

- [Parts README](../README.md)
- [Gearbox Assembly](../../ASSEMBLIES/OPEN_FAN_PROPULSOR/GEARBOX_ASSEMBLY/README.md)
- [ATA 61 Overview](../../../../../README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
