# 60-60-10_AIRCRAFT_TELEMETRY — Aircraft Telemetry Collection

## Purpose

This section defines the on-board data collection and encoding protocols for aircraft telemetry transmission in the PMT system.

## Telemetry Categories

| Section | Data Type | Sensors |
|---------|-----------|---------|
| 10-10_Structural_Strain | Strain measurements | Fiber optic strain gauges |
| 10-20_Thermal_Monitoring | Temperature data | Thermocouple arrays, IR sensors |
| 10-30_Cycle_Counters | Fatigue cycles | Landing gear, control surfaces |
| 10-40_H2_Systems | Hydrogen system health | Fuel cell, storage tanks, lines |
| 10-50_Data_Encoding | Protocol encoding | Compression, serialization |
| 10-90_Schemas | Data schemas | JSON/Protobuf definitions |

## Data Collection Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Aircraft Systems                      │
├─────────────┬─────────────┬─────────────┬───────────────┤
│  Structural │   Thermal   │    Cycle    │  H2 Systems   │
│   Strain    │  Monitoring │  Counters   │               │
└──────┬──────┴──────┬──────┴──────┬──────┴───────┬───────┘
       │             │             │              │
       └─────────────┴──────┬──────┴──────────────┘
                            │
                    ┌───────▼───────┐
                    │ Data Encoding │
                    └───────┬───────┘
                            │
                    ┌───────▼───────┐
                    │   CFLF-TELEM  │
                    │   A→G Link    │
                    └───────────────┘
```

## Sampling Rates

| Data Type | Normal Rate | High-Rate Trigger |
|-----------|-------------|-------------------|
| Structural strain | 1 Hz | 100 Hz (anomaly) |
| Thermal | 0.1 Hz | 10 Hz (exceedance) |
| Cycle counters | Event-based | N/A |
| H2 systems | 1 Hz | 10 Hz (anomaly) |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
