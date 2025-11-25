# 53-30-10-00 — Interface Summary

**Document ID:** 53-30-10-00-003  
**Version:** 1.0  
**Date:** 2025-11-25  
**Status:** DRAFT

---

## 1. Purpose

This document summarizes interfaces for the Harvesting subsystem.

---

## 2. Physical Interfaces

| IF ID | Interface | Type | Connected System |
|:--|:--|:--|:--|
| IF-H-001 | ECS recirculation duct | Duct flange | ATA 21 |
| IF-H-002 | Heat source mounting | Bracket | Thermal sources |
| IF-H-003 | Condensate drain | Fitting | Water system |
| IF-H-004 | Structure mounting | Fasteners | ATA 53-50 |

---

## 3. Electrical Interfaces

| IF ID | Interface | Type | Parameters |
|:--|:--|:--|:--|
| IF-H-010 | Power output | Connector | 28 VDC, 100 A max |
| IF-H-011 | Control/monitoring | CAN bus | 500 kbps |
| IF-H-012 | Discrete signals | Wiring | 28 VDC logic |

---

## 4. Fluid Interfaces

| IF ID | Interface | Fluid | Parameters |
|:--|:--|:--|:--|
| IF-H-020 | Cabin air inlet | Air | 1 kg/s max |
| IF-H-021 | Cabin air outlet | Air | Reduced CO₂ |
| IF-H-022 | Condensate output | Water | 2 L/h max |

---

## 5. Data Interfaces

| IF ID | Interface | Protocol | Data |
|:--|:--|:--|:--|
| IF-H-030 | Performance data | CAN | Power output, flow |
| IF-H-031 | Status/health | CAN | BITE data |
| IF-H-032 | DPP data | Ethernet | Asset info |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25
