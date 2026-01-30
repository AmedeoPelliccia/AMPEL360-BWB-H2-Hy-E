# Q100-61-RTE-DATA-HEALTH-MON — Health Monitoring Data Routing

## Overview

Defines the routing for propulsion health monitoring and predictive maintenance data.

## Data Sources

| Source | Parameters |
|--------|------------|
| Motor | Temperature, vibration, current |
| Gearbox | Temperature, vibration, oil debris |
| Controller | Temperature, faults, efficiency |
| Fan | Balance, pitch, speed |

## Routing

```
Sensor Network
    ↓
Data Acquisition Unit
    ↓
Health Monitoring Processor
    ↓
Aircraft Data Recorder
    ↓
Ground Link (when available)
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.

---
