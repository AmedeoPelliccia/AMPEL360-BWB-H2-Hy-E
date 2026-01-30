# Q100-61-PROD-ELECTRIC-DRIVE-UNIT — Electric Drive Unit

**Product ID**: Q100-61-PROD-ELECTRIC-DRIVE-UNIT  
**Version**: 1.0  
**Status**: DRAFT  
**Level**: Sub-Product

## Purpose

The Q100-61-PROD-ELECTRIC-DRIVE-UNIT is the electric motor and power electronics assembly for the AMPEL360 BWB H2 Hy-E propulsion system. It converts electrical power from the aircraft's 800 VDC bus into mechanical power for the propulsor.

## Key Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Motor Count | 2 | — | Dual motors for redundancy |
| Power (Continuous) | 2× 500 | kW | Per motor |
| Power (Peak) | 2× 600 | kW | 30-second rating |
| Input Voltage | 800 | VDC | From fuel cell/battery |
| Max RPM | 6,300 | rpm | Motor shaft |
| Efficiency | 97 | % | At rated power |
| Weight | 420 | kg | Motors + inverters + cooling |

## Components

- **Electric Motors**: 2× Permanent Magnet Synchronous Motor (PMSM)
- **Power Electronics**: 2× SiC-based inverter/rectifier
- **Cooling System**: Liquid cooling with glycol-water
- **HV Junction Box**: Power distribution and isolation

## Interfaces

| Interface | To | Type |
|-----------|-----|------|
| IF-EDU-001 | Gearbox input | Mechanical shaft |
| IF-EDU-002 | Controller | Motor control signals |
| IF-EDU-003 | Aircraft HV bus | 800 VDC power input |
| IF-EDU-004 | Cooling circuit | Fluid connection |

## Related Documents

- [Product Definition YAML](product_definition.yaml)
- [Product Structure YAML](product_structure.yaml)
- [Parent Product](../Q100-61-PROD-PROPULSOR-SYSTEM/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
