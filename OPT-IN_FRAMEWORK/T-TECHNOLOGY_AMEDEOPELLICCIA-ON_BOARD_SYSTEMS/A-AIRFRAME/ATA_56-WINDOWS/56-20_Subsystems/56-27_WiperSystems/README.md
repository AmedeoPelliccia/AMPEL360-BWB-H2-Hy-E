# 56-27 — Wiper Systems

## Overview

This subsystem covers windshield wiper systems for the AMPEL360 BWB aircraft, providing mechanical rain removal capability for cockpit windshields.

## Subsystem Structure

### 56-27-00_GENERAL

General subsystem documentation including wiper system architecture.

### 56-27-01_LRU — Wiper Drive Unit

Windshield wiper drive and control assembly.

**Line Replaceable Items (LRIs):**

| LRI | Component | Description |
|-----|-----------|-------------|
| LRI_01 | Motor Assembly | Wiper drive motor |
| LRI_02 | Linkage Arm | Mechanical linkage system |
| LRI_03 | Wiper Blade | Windshield contact blade |
| LRI_04 | Park Switch | Auto-park position sensing |
| LRI_05 | Speed Controller | Variable speed control |

## Key Interfaces

| Interface | Connected System | ATA | Description |
|-----------|------------------|-----|-------------|
| IF-56-27-001 | Windshields | 56-21 | Wiper contact surface |
| IF-56-27-002 | Electrical Power | 24 | Motor power supply |
| IF-56-27-003 | Cockpit Controls | - | Speed selector |

## Operating Modes

| Mode | Wiper Speed | Application |
|------|-------------|-------------|
| OFF | Parked | Normal operation |
| LOW | 160 cycles/min | Light rain |
| HIGH | 250 cycles/min | Heavy rain |
| INTERMITTENT | Variable | Light precipitation |

## Related Documentation

- [LRU Overview](./56-27-01_LRU/56-27-01_001_LRU_Overview.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
