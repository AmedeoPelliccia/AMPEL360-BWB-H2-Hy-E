# 53-10-21-001 — ANCHORS System Page

| Field | Value |
|-------|-------|
| **Document ID** | 53-10-21-001 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | OPERATIONAL |

---

## 1. Purpose

This document defines the ANCHORS system page display for crew interface.

## 2. Scope

Applicable to all ECAM/EICAS system page displays.

## 3. System Page Layout

```
┌─────────────────────────────────────────────────────────────┐
│                    ANCHORS SYSTEM PAGE                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BATTERIES              CO₂ CAPTURE           WATER         │
│  ┌─────┐ ┌─────┐       ┌─────────┐          ┌─────┐        │
│  │ 85% │ │ 82% │       │ 7.2kg/h │          │ 92% │        │
│  │ 32°C│ │ 31°C│       │ CRUISE  │          │ OK  │        │
│  └──┬──┘ └──┬──┘       └────┬────┘          └──┬──┘        │
│     │       │               │                  │            │
│  ┌─────┐ ┌─────┐       ┌─────────┐          ┌─────┐        │
│  │ 78% │ │ 80% │       │ CART 45%│          │RECYC│        │
│  │ 33°C│ │ 32°C│       │ 38.5 kg │          │ ON  │        │
│  └─────┘ └─────┘       └─────────┘          └─────┘        │
│                                                             │
│  ENERGY HARVEST         THERMAL              DPP            │
│  ┌─────────┐           ┌─────────┐          ┌─────┐        │
│  │ +2.3 kW │           │ 42°C    │          │SYNC │        │
│  │ SOLAR+TH│           │ NOMINAL │          │ OK  │        │
│  └─────────┘           └─────────┘          └─────┘        │
│                                                             │
│  MODE: AUTO    STATUS: NORMAL    FLT: 4,521 kg CO₂ TOTAL   │
└─────────────────────────────────────────────────────────────┘
```

## 4. Display Elements

| Element | Description | Normal Indication |
|---------|-------------|-------------------|
| BATTERIES | SoC and temperature for each pack | Green, 30-90% SoC, 20-40°C |
| CO₂ CAPTURE | Capture rate and mode | Green, 5-10 kg/hr |
| CARTRIDGE | Fill level and mass | Green, 10-90% |
| WATER | Recycling status | Green, OK |
| ENERGY HARVEST | Power generation | Green, > 1 kW |
| THERMAL | ThermalBus temperature | Green, 30-50°C |
| DPP | Sync status | Green, SYNC OK |

## 5. Color Coding

| Color | Meaning |
|-------|---------|
| Green | Normal operation |
| Amber | Caution, monitor required |
| Red | Warning, action required |
| White | Status information |
| Blue | Advisory |

## 6. Related Documents

- [53-10-20-001_EICAS_ECAM_Catalog.md](../53-10-20_Alerts/53-10-20-001_EICAS_ECAM_Catalog.md) — Alert catalog
- [53-10-22-001_ANCHORS_Panel_Operations.md](../53-10-22_Controls/53-10-22-001_ANCHORS_Panel_Operations.md) — Panel operations

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---

*END OF DOCUMENT*
