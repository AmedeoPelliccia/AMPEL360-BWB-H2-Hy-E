# Q100-61-PROD-OPEN-FAN-UNIT — Open Fan Unit

**Product ID**: Q100-61-PROD-OPEN-FAN-UNIT  
**Version**: 1.0  
**Status**: DRAFT  
**Level**: Sub-Product

## Purpose

The Q100-61-PROD-OPEN-FAN-UNIT is the open-fan rotor assembly for the AMPEL360 BWB H2 Hy-E propulsion system. It provides high-efficiency thrust generation through an unducted, large-diameter fan configuration.

## Key Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Fan Diameter | 2.8 | m | Unducted configuration |
| Blade Count | 12 | — | CFRP blades |
| Pitch Range | -5 to +30 | degrees | Variable pitch |
| Max RPM | 1,800 | rpm | At takeoff |
| Cruise RPM | 1,200 | rpm | FL350, M0.78 |
| Weight | 380 | kg | Including hub and actuators |

## Components

- **Fan Blades**: 12× CFRP variable-pitch blades
- **Fan Hub**: Titanium alloy (Ti-6Al-4V)
- **Spinner**: Composite aerodynamic fairing
- **Pitch Actuation System**: Hydraulic/electric actuators
- **De-icing System**: Electrothermal

## Interfaces

| Interface | To | Type |
|-----------|-----|------|
| IF-OFU-001 | Gearbox output shaft | Mechanical coupling |
| IF-OFU-002 | Controller | Pitch control signals |
| IF-OFU-003 | Nacelle | Structural mounting |

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
