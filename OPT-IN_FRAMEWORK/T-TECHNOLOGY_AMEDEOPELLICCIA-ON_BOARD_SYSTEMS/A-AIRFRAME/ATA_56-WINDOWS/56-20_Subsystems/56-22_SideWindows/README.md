# 56-22 — Cockpit Side Windows

## Overview

This subsystem covers all cockpit side window assemblies for the AMPEL360 BWB aircraft. Side windows provide lateral visibility for the flight crew and may include sliding or emergency exit functionality.

## Subsystem Structure

### 56-22-00_GENERAL

General subsystem documentation including subsystem overview and common specifications.

### 56-22-01_LRU — Captain Side Window Assembly

Captain's side window unit with sliding panel capability.

**Line Replaceable Items (LRIs):**

| LRI | Component | Description |
|-----|-----------|-------------|
| LRI_01 | Fixed Panel | Non-opening portion of side window |
| LRI_02 | Sliding Panel | Openable window for ground operations |
| LRI_03 | Sliding Mechanism | Track and latch system |
| LRI_04 | Seals | Pressure and weather sealing |
| LRI_05 | Emergency Release | Quick-release mechanism |

### 56-22-02_LRU — First Officer Side Window Assembly

First Officer's side window unit (mirror structure of 56-22-01).

## Key Interfaces

| Interface | Connected System | ATA | Description |
|-----------|------------------|-----|-------------|
| IF-56-22-001 | Window Heating Controller | 56-25 | Heating power and control |
| IF-56-22-002 | Electrical Power | 24 | Primary power supply |
| IF-56-22-003 | Flight Deck Structure | 53 | Structural mounting |
| IF-56-22-004 | Emergency Systems | 26 | Emergency exit indication |

## Related Documentation

- [LRU Overview - Captain Side](./56-22-01_LRU/56-22-01_001_LRU_Overview.md)
- [LRU Overview - First Officer Side](./56-22-02_LRU/56-22-02_001_LRU_Overview.md)
- [CIR Diagrams](../../56-90_Tables_Schemas_Diagrams/ATA_56-90_CIR/)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
