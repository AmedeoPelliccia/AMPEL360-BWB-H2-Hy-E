# 56-26 — Rain Repellent System

## Overview

This subsystem covers the rain repellent system for the AMPEL360 BWB aircraft, providing improved visibility during rain conditions by applying a hydrophobic coating to cockpit windshields.

## Subsystem Structure

### 56-26-00_GENERAL

General subsystem documentation including system architecture and operating procedures.

### 56-26-01_LRU — Rain Repellent System

Complete rain repellent fluid application system.

**Line Replaceable Items (LRIs):**

| LRI | Component | Description |
|-----|-----------|-------------|
| LRI_01 | Fluid Reservoir | Rain repellent fluid storage |
| LRI_02 | Pump Assembly | Pressurized fluid delivery |
| LRI_03 | Spray Nozzles | Windshield application nozzles |
| LRI_04 | Control Valve | Fluid flow control |
| LRI_05 | Fluid Level Sensor | Quantity indication |

## Key Interfaces

| Interface | Connected System | ATA | Description |
|-----------|------------------|-----|-------------|
| IF-56-26-001 | Windshields | 56-21 | Spray application surface |
| IF-56-26-002 | Electrical Power | 24 | Pump motor power |
| IF-56-26-003 | EICAS | 31 | Fluid level indication |
| IF-56-26-004 | Cockpit Controls | - | Pilot activation switch |

## Related Documentation

- [LRU Overview](./56-26-01_LRU/56-26-01_001_LRU_Overview.md)
- [Rain Repellent Schematic](../../56-90_Tables_Schemas_Diagrams/ATA_56-90_CIR/56-90-26_56-26-FIG_001-RainRepellentSchematic.svg)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
