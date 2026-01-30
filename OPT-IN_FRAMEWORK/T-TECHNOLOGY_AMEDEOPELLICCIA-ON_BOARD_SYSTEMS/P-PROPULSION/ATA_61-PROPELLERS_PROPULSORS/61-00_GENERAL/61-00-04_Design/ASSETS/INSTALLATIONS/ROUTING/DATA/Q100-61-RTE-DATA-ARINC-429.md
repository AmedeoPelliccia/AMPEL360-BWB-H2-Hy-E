# Q100-61-RTE-DATA-ARINC-429 — ARINC-429 Interface Routing

## Overview

Defines the routing for ARINC-429 data bus interface to aircraft avionics.

## Data Exchanged

| Label | Parameter | Direction |
|-------|-----------|-----------|
| 206 | Engine N1 | Tx |
| 207 | Engine N2 | Tx |
| 211 | EGT | Tx |
| 310 | Fuel flow (equiv) | Tx |
| 312 | Thrust command | Rx |

## Routing

```
FADEC ARINC-429 Port
    ↓
Pylon Conduit
    ↓
Wing Junction Box
    ↓
Aircraft Avionics Bus
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.

---
