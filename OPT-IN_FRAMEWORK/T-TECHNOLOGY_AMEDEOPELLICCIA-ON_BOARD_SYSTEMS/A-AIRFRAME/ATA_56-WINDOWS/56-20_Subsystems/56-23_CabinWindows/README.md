# 56-23 — Passenger Cabin Windows

## Overview

This subsystem covers all passenger cabin window assemblies for the AMPEL360 BWB aircraft. Cabin windows provide natural light and exterior viewing for passengers while maintaining pressure integrity.

## Subsystem Structure

### 56-23-00_GENERAL

General subsystem documentation including subsystem overview and common specifications.

### 56-23-01_LRU — Standard Cabin Window Unit

Standard passenger window assembly with triple-pane construction.

**Line Replaceable Items (LRIs):**

| LRI | Component | Description |
|-----|-----------|-------------|
| LRI_01 | Outer Pane | Structural pressure pane |
| LRI_02 | Middle Pane | Fail-safe backup pane |
| LRI_03 | Inner Pane | Scratch pane (passenger side) |
| LRI_04 | Breathing Hole | Pressure equalization port |
| LRI_05 | Retaining Ring | Pane retention assembly |
| LRI_06 | Window Shade | Manual or electrochromic shade |

### 56-23-02_LRU — Overwing Emergency Exit Window

Emergency exit window assembly with quick-release capability.

**Line Replaceable Items (LRIs):**

| LRI | Component | Description |
|-----|-----------|-------------|
| LRI_01 | Exit Panel | Emergency exit window panel |
| LRI_02 | Handle Assembly | Emergency release handle |
| LRI_03 | Hinge System | Exit panel hinge mechanism |
| LRI_04 | Placard Assembly | Emergency instruction placards |
| LRI_05 | Sealing System | Pressure sealing assembly |

## Key Interfaces

| Interface | Connected System | ATA | Description |
|-----------|------------------|-----|-------------|
| IF-56-23-001 | Cabin Structure | 53 | Window frame mounting |
| IF-56-23-002 | Smart Glass Control | 56-28 | Electrochromic control (if equipped) |
| IF-56-23-003 | Emergency Systems | 26 | Emergency exit indication |
| IF-56-23-004 | Cabin Lighting | 33 | Window reveal lighting |

## Related Documentation

- [Standard Window LRU Overview](./56-23-01_LRU/56-23-01_001_LRU_Overview.md)
- [Emergency Exit LRU Overview](./56-23-02_LRU/56-23-02_001_LRU_Overview.md)
- [CIR Diagrams](../../56-90_Tables_Schemas_Diagrams/ATA_56-90_CIR/)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
