# Q100-61-PROD-GEARBOX-UNIT — Gearbox Unit

**Product ID**: Q100-61-PROD-GEARBOX-UNIT  
**Version**: 1.0  
**Status**: DRAFT  
**Level**: Sub-Product

## Purpose

The Q100-61-PROD-GEARBOX-UNIT is the reduction gearbox assembly that transmits power from the electric motors to the open-fan rotor. It provides the necessary speed reduction between the high-speed motor output and the fan operating speed.

## Key Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Gear Ratio | 3.5:1 | — | Speed reduction |
| Input Speed | 6,300 | rpm | Motor max speed |
| Output Speed | 1,800 | rpm | Fan max speed |
| Power Capacity | 1,200 | kW | Peak rating |
| Efficiency | 98.5 | % | At rated torque |
| Weight | 185 | kg | Including lubrication |

## Components

- **Planetary Gear Set**: High-efficiency planetary reduction
- **Input Shaft**: Spline connection to motor(s)
- **Output Shaft**: Connection to fan hub
- **Bearings**: Precision roller and ball bearings
- **Lubrication System**: Self-contained oil system

## Interfaces

| Interface | To | Type |
|-----------|-----|------|
| IF-GBU-001 | Electric Drive input | Mechanical shaft |
| IF-GBU-002 | Open Fan output | Mechanical shaft |
| IF-GBU-003 | Controller | Speed/torque sensors |

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
