# Q100-61-PROD-CONTROLLER-UNIT — Controller Unit

**Product ID**: Q100-61-PROD-CONTROLLER-UNIT  
**Version**: 1.0  
**Status**: DRAFT  
**Level**: Sub-Product

## Purpose

The Q100-61-PROD-CONTROLLER-UNIT is the digital control system for the AMPEL360 BWB H2 Hy-E propulsion system. It provides full-authority digital control (FADEC) for the electric propulsion system, including motor control, power management, and health monitoring.

## Key Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Architecture | Dual-channel | — | DAL A certification |
| Motor Controllers | 2 | — | Integrated with FADEC |
| Control Rate | 10 | kHz | Motor control loop |
| Health Parameters | 100+ | — | Monitored parameters |
| Weight | 45 | kg | Including harnesses |

## Components

- **FADEC**: Dual-channel Full Authority Digital Engine Control
- **Motor Controllers**: Integrated motor control algorithms
- **Power Management Unit**: Intelligent power distribution
- **Sensors**: Temperature, vibration, position, current, voltage
- **Health Monitoring Unit**: Prognostics and diagnostics

## Interfaces

| Interface | To | Type |
|-----------|-----|------|
| IF-CTL-001 | Electric Drive | Motor control |
| IF-CTL-002 | Open Fan | Pitch control |
| IF-CTL-003 | Aircraft Bus | ARINC 429 / CAN-FD |
| IF-CTL-004 | Sensors | Various analog/digital |

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
