# Q100-61-RTE-DATA-FADEC-BUS — FADEC Control Bus Routing

## Overview

Defines the routing for Full Authority Digital Engine Control (FADEC) communication bus.

## Routing Path

```
FADEC Control Unit
    ↓
Dual CAN Bus A/B
    ↓
Motor Controller
    ↓
Sensors and Actuators
```

## Specification

| Parameter | Value |
|-----------|-------|
| Protocol | CAN 2.0B |
| Baud rate | 1 Mbit/s |
| Cable | Twisted pair, shielded |
| Redundancy | Dual bus |
| Termination | 120Ω |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.

---
