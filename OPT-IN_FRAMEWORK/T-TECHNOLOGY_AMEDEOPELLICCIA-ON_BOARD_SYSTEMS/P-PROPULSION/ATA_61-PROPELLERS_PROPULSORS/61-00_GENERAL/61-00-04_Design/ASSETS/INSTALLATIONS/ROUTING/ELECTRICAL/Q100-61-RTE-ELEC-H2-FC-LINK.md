# Q100-61-RTE-ELEC-H2-FC-LINK — H₂ Fuel Cell Power Link

## Overview

Defines the routing for power connection from the H₂ PEM fuel cell system to the propulsion DC bus.

## System Context

The H₂ PEM fuel cell provides primary power for the hybrid-electric propulsion system:
- Voltage: 650-800 VDC (variable with load)
- Current: Up to 400A continuous
- Power: Up to 300 kW

## Routing Path

```
H₂ PEM Fuel Cell Stack
    ↓
DC/DC Converter (if applicable)
    ↓
Main DC Bus Panel
    ↓
Distribution to Propulsors
```

## Cable Specification

| Parameter | Value |
|-----------|-------|
| Conductor | 350 kcmil, aluminum or copper |
| Insulation | XLPE, 1000V rated |
| Jacket | Orange, flame retardant |
| Configuration | Pos + Neg + Ground |

## Safety Requirements

- Arc-flash rated connections
- Hydrogen-safe routing (avoid H₂ zones)
- Emergency disconnect accessible
- Insulation monitoring

## Interface

| End | Connection |
|-----|------------|
| Fuel cell | Bus bar terminal |
| DC bus | Lug terminal, fused |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.

---
