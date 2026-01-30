# 56-25 — Window Heating (Anti-Ice & Anti-Fog)

## Overview

This subsystem covers all window heating systems for the AMPEL360 BWB aircraft, providing anti-ice and anti-fog protection for cockpit and cabin windows.

## Subsystem Structure

### 56-25-00_GENERAL

General subsystem documentation including heating system architecture.

### 56-25-01_LRU — Windshield Heating Controller

Central controller for windshield heating management.

**Line Replaceable Items (LRIs):**

| LRI | Component | Description |
|-----|-----------|-------------|
| LRI_01 | Power Controller | Main power regulation unit |
| LRI_02 | Temperature Sensors | Panel temperature monitoring |
| LRI_03 | Current Monitoring | Power consumption tracking |
| LRI_04 | Overheat Protection | Thermal runaway prevention |
| LRI_05 | Diagnostic Interface | BITE and fault reporting |

## Key Interfaces

| Interface | Connected System | ATA | Description |
|-----------|------------------|-----|-------------|
| IF-56-25-001 | Windshields | 56-21 | Heating element power |
| IF-56-25-002 | Side Windows | 56-22 | Heating element power |
| IF-56-25-003 | Electrical Power | 24 | 115VAC/28VDC supply |
| IF-56-25-004 | Ice Protection | 30 | System integration |
| IF-56-25-005 | EICAS | 31 | Status display |

## Related Documentation

- [LRU Overview](./56-25-01_LRU/56-25-01_001_LRU_Overview.md)
- [Heating Load Profiles](../../56-90_Tables_Schemas_Diagrams/ATA_56-90_CIR/56-90-25_56-25-TABLE_001-HeatingLoadProfiles.csv)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
