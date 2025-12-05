# Q100-61-RTE-ELEC-POWER-MAIN — Main Power Routing

## Overview

Defines the routing for main power cables from the aircraft DC bus to the motor controller.

## Routing Path

```
DC Bus Panel (Zone 200)
    ↓
    ├── [EMI filter]
    ↓
Wing/Body Junction (Zone 300)
    ↓
    ├── [Firewall penetration]
    ↓
Pylon Conduit
    ↓
Controller Bay
    ↓
Motor Controller DC Input
```

## Cable Specification

| Parameter | Value |
|-----------|-------|
| Conductor | 2/0 AWG, stranded copper |
| Insulation | XLPE, 1000V rated |
| Jacket | Orange, high-temp |
| Shield | Braided copper, 85% coverage |
| Bundle | Pos + Neg + Ground |

## Routing Requirements

- Minimum bend radius: 200mm
- Support spacing: 300mm maximum
- Separation from control: 100mm minimum
- Firewall penetration: FAR 25.867 compliant
- Conduit: EMI shielded throughout pylon

## Connection Points

| Point | Connector | Torque |
|-------|-----------|--------|
| DC bus panel | Lug terminal | 40 Nm |
| Firewall | Bulkhead fitting | Per spec |
| Controller | Terminal block | 25 Nm |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.

---
