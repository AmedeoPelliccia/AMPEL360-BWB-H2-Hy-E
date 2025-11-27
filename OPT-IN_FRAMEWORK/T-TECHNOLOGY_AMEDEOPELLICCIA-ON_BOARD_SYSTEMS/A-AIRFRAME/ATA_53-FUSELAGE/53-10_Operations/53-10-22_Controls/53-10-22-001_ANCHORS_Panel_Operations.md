# 53-10-22-001 — ANCHORS Panel Operations

| Field | Value |
|-------|-------|
| **Document ID** | 53-10-22-001 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | OPERATIONAL |

---

## 1. Purpose

This document defines the ANCHORS control panel operations for crew interface.

## 2. Scope

Applicable to all ANCHORS control panel operations.

## 3. Panel Location

The ANCHORS control panel is located on the overhead panel (OVHD).

## 4. Control Elements

| Control | Type | Positions | Function |
|---------|------|-----------|----------|
| ANCHORS MASTER | Switch | ON/OFF | Master system control |
| ANCHORS MODE | Selector | AUTO/ECO/MAX/STBY | Mode selection |
| CO2 CAPTURE | Switch | ON/OFF/RESET | CO₂ system control |
| BATT [1-4] ISOL | Pushbutton | ISOL/NORM | Individual pack isolation |
| FIRE AGENT | Guarded pushbutton | DISCH | Fire suppression |
| CO2 ISOL VALVE | Guarded switch | OPEN/CLOSE | CO₂ isolation |

## 5. Panel Layout

```
┌─────────────────────────────────────────────────────────────┐
│                    ANCHORS OVHD PANEL                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐     │
│  │ ANCHORS │   │  MODE   │   │   CO2   │   │CO2 ISOL │     │
│  │ MASTER  │   │ ●AUTO   │   │ CAPTURE │   │  VALVE  │     │
│  │  [ON]   │   │  ECO    │   │  [ON]   │   │ [OPEN]  │     │
│  │         │   │  MAX    │   │         │   │         │     │
│  │   OFF   │   │  STBY   │   │ OFF RST │   │  CLOSE  │     │
│  └─────────┘   └─────────┘   └─────────┘   └─────────┘     │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ BATT 1  │ BATT 2  │ BATT 3  │ BATT 4  │ FIRE AGENT │   │
│  │  ISOL   │  ISOL   │  ISOL   │  ISOL   │   DISCH    │   │
│  │   ○     │   ○     │   ○     │   ○     │   [GUARDED]│   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 6. Normal Operations

| Operation | Procedure |
|-----------|-----------|
| System startup | ANCHORS MASTER → ON, wait for INIT complete |
| Mode change | ANCHORS MODE → select desired mode |
| CO₂ reset | CO2 CAPTURE → RESET, then ON |
| Battery isolation | BATT [X] ISOL → press (illuminates when isolated) |

## 7. Related Documents

- [53-10-21-001_ANCHORS_System_Page.md](../53-10-21_Displays/53-10-21-001_ANCHORS_System_Page.md) — System page display
- [53-10-20-001_EICAS_ECAM_Catalog.md](../53-10-20_Alerts/53-10-20-001_EICAS_ECAM_Catalog.md) — Alert catalog

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---

*END OF DOCUMENT*
