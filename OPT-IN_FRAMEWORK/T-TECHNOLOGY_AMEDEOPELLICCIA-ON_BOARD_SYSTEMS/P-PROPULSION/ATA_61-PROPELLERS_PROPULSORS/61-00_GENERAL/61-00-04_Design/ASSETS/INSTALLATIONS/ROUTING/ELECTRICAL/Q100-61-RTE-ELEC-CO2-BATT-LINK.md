# Q100-61-RTE-ELEC-CO2-BATT-LINK — CO₂ Battery Buffer Link

## Overview

Defines the routing for power connection from the closed-loop CO₂ battery system to the propulsion DC bus.

## System Context

The CO₂ battery provides peak power buffering for the hybrid-electric propulsion system:
- Voltage: 700 VDC nominal
- Power: Up to 500 kW (burst, 30 sec)
- Energy: 50 kWh capacity
- Function: Peak power during takeoff and go-around

## Routing Path

```
CO₂ Battery Pack
    ↓
Battery Management System (BMS)
    ↓
Contactor/Disconnect
    ↓
Main DC Bus Panel
    ↓
Distribution to Propulsors
```

## Cable Specification

| Parameter | Value |
|-----------|-------|
| Conductor | 500 kcmil, copper |
| Insulation | Silicone, 1000V rated |
| Jacket | Orange, high-temp |
| Configuration | Pos + Neg + Sense + Ground |

## Safety Requirements

- Active BMS monitoring
- Thermal runaway protection
- Automatic disconnect on fault
- Ground fault monitoring

## Interface

| End | Connection |
|-----|------------|
| Battery | Bus bar with contactors |
| DC bus | Lug terminal, fused |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.

---
