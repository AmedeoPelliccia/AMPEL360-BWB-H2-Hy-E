# 56-28 — Smart Glass (Electrochromic Windows)

## Overview

This subsystem covers advanced smart glass (electrochromic) window systems for the AMPEL360 BWB aircraft, enabling electronic control of window transparency for passenger comfort and energy management.

## Subsystem Structure

### 56-28-00_GENERAL

General subsystem documentation including electrochromic technology overview.

### 56-28-01_LRU — Smart Glass Control Unit

Central controller for electrochromic window management.

**Line Replaceable Items (LRIs):**

| LRI | Component | Description |
|-----|-----------|-------------|
| LRI_01 | Electrochromic Film | Variable tint layer |
| LRI_02 | Voltage Controller | Tint level control electronics |
| LRI_03 | Light Sensors | Ambient light detection |
| LRI_04 | Passenger Interface | Individual window controls |
| LRI_05 | Power Supply | Low-voltage DC supply |

## Key Features

- **Variable Tinting**: 5% to 65% light transmission range
- **Individual Control**: Per-window passenger control
- **Zone Control**: Crew override for cabin zones
- **Auto Mode**: Light-sensor-based automatic tinting
- **Energy Savings**: Reduced cabin cooling load

## Key Interfaces

| Interface | Connected System | ATA | Description |
|-----------|------------------|-----|-------------|
| IF-56-28-001 | Cabin Windows | 56-23 | Electrochromic film integration |
| IF-56-28-002 | Observation Windows | 56-24 | Panoramic window dimming |
| IF-56-28-003 | Electrical Power | 24 | Power distribution |
| IF-56-28-004 | IFE System | 44 | Passenger seat interface |
| IF-56-28-005 | Cabin Management | 21 | Climate coordination |

## Related Documentation

- [LRU Overview](./56-28-01_LRU/56-28-01_001_LRU_Overview.md)
- [Software Documentation](../../56-40_Software/56-40-02_SmartGlassDimming_SW/)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
