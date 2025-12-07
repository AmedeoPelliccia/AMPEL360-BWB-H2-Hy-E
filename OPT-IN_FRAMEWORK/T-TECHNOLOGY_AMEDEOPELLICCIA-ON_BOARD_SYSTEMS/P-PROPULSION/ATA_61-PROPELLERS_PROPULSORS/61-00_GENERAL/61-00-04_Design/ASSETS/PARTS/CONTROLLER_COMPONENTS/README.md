# CONTROLLER_COMPONENTS — ATA 61 Parts

## Overview

This directory contains individual part definitions for motor controller system components used in the hybrid electric propulsion system of the AMPEL360 BWB H2 Hy-E aircraft. The controller manages power delivery to the electric motor.

## Parts Inventory

| Part ID | Name | Description | Status |
|---------|------|-------------|--------|
| Q100-61-PRT-CTRL-ENCLOSURE | Controller Enclosure | Main housing for power electronics | Draft |
| Q100-61-PRT-CTRL-HEATSINK | Controller Heatsink | Thermal management baseplate | Draft |
| Q100-61-PRT-CTRL-POWER-MODULE | Power Module | IGBT/SiC power semiconductor module | Draft |
| Q100-61-PRT-CTRL-BUSBAR | DC Busbar | High-current DC distribution bar | Draft |

## Technical Overview

### Controller Architecture

- **Topology**: 3-phase inverter (6-switch or multi-level)
- **Semiconductors**: Silicon Carbide (SiC) MOSFETs or IGBTs
- **Voltage Class**: TBD VDC
- **Power Rating**: TBD MW

### Controller Enclosure (Q100-61-PRT-CTRL-ENCLOSURE)

- **Material**: Cast aluminum alloy with EMI shielding
- **Features**:
  - IP67 environmental sealing
  - EMI/RFI shielding (DO-160G compliant)
  - Mounting provisions for power modules
  - Connector interfaces (power and signal)
  - Pressure relief valve (altitude operation)

### Controller Heatsink (Q100-61-PRT-CTRL-HEATSINK)

- **Material**: Aluminum alloy (6061-T6) or copper
- **Type**: Liquid-cooled cold plate
- **Features**:
  - Micro-channel or pin-fin cooling structure
  - Thermal interface material (TIM) surface
  - O-ring seal grooves
  - Coolant port fittings
  - Flatness specification for module mounting

### Power Module (Q100-61-PRT-CTRL-POWER-MODULE)

- **Type**: Half-bridge or full-bridge power module
- **Semiconductors**: SiC MOSFETs (preferred) or Si IGBTs
- **Features**:
  - Low-inductance package design
  - Integrated gate driver interface
  - Press-pack or baseplate construction
  - NTC temperature sensors
  - Current sense provisions

### DC Busbar (Q100-61-PRT-CTRL-BUSBAR)

- **Material**: Copper with nickel plating
- **Features**:
  - Laminated construction for low inductance
  - Insulation between positive and negative layers
  - DC link capacitor interface
  - Terminal connections for power input
  - Current carrying capacity: TBD A continuous

## Cooling System Integration

- Shared coolant loop with motor
- Coolant type: Glycol-water mixture or dielectric fluid
- Maximum junction temperature: 150°C (SiC) / 175°C (IGBT)
- Thermal derating provisions

## Safety Features

- Discharge resistor for DC link capacitors
- Pre-charge circuit
- Over-current protection (hardware and software)
- Over-temperature shutdown
- Ground fault detection

## Assembly References

These parts are used in the following assemblies:

- `../ASSEMBLIES/ELECTRIC_MOTOR_DRIVE/CONTROLLER_ASSEMBLY/`
- `../ASSEMBLIES/ELECTRIC_MOTOR_DRIVE/POWER_DISTRIBUTION_ASSEMBLY/`
- `../ASSEMBLIES/FULL_PROPULSOR_SYSTEM/`

## Related Documents

- [Parts README](../README.md)
- [Controller Assembly](../../ASSEMBLIES/ELECTRIC_MOTOR_DRIVE/CONTROLLER_ASSEMBLY/README.md)
- [ATA 61 Overview](../../../../../README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
