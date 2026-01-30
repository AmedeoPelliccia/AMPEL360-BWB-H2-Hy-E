# 53-30-00-05 — ICD ATA 24-80 Electrical Power

**Document ID:** 53-30-00-05-003  
**Version:** 1.0  
**Date:** 2025-11-25  
**Status:** DRAFT

---

## 1. Purpose

This Interface Control Document defines electrical interfaces between ANCHORS systems and ATA 24 Electrical Power systems.

---

## 2. Interface Summary

| Interface ID | ANCHORS Element | Electrical Element | Type |
|:--|:--|:--|:--|
| IF-24-80-001 | Harvesting output | Auxiliary bus | Power supply |
| IF-24-80-002 | Battery swap bay | Main bus | Power/charging |
| IF-24-80-003 | Controllers | Avionics bus | Control power |
| IF-24-80-004 | Sensors | Essential bus | Instrument power |

---

## 3. Power Supply Interfaces

### IF-24-80-001: Harvesting Output

**Description:** Power output from energy harvesting systems to aircraft bus.

| Parameter | Value | Tolerance |
|:--|:--|:--|
| Voltage | 28 VDC | ±4 V |
| Current capacity | 200 A max | — |
| Power quality | MIL-STD-704F | — |
| Ripple | < 1.5 V p-p | — |

### IF-24-80-002: Battery Swap Bay

**Description:** High-power interface for swappable battery packs.

| Parameter | Value | Tolerance |
|:--|:--|:--|
| Voltage | 800 VDC nominal | ±50 V |
| Current capacity | 500 A | — |
| Connector | Custom high-power | — |
| Interlock | Hardware-based | — |

### IF-24-80-003: Controller Power

**Description:** Power supply for ANCHORS controllers.

| Parameter | Value | Tolerance |
|:--|:--|:--|
| Voltage | 28 VDC | ±4 V |
| Current | 10 A max | — |
| Backup | Battery-backed | — |

---

## 4. Grounding Interface

| Grounding Type | Requirement |
|:--|:--|
| Equipment ground | < 2.5 mΩ to structure |
| Fault ground | Dedicated conductor |
| EMI ground | Single-point bonding |

---

## 5. EMI/EMC Requirements

| Parameter | Requirement |
|:--|:--|
| Conducted emissions | MIL-STD-461G CE102 |
| Radiated emissions | MIL-STD-461G RE102 |
| Susceptibility | MIL-STD-461G CS/RS |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25
