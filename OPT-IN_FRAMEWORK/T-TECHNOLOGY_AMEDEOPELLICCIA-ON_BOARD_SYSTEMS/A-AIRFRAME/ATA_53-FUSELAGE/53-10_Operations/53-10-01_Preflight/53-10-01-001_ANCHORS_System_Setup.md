# 53-10-01-001 — ANCHORS System Setup

| Field | Value |
|-------|-------|
| **Document ID** | 53-10-01-001 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | OPERATIONAL |

---

## 1. Purpose

This procedure defines the cockpit preparation and ANCHORS system setup sequence for pre-flight operations.

## 2. Scope

Applicable to all AMPEL360 BWB aircraft variants equipped with ANCHORS systems.

## 3. Prerequisites

- Aircraft on ground power or APU running
- All circuit breakers in normal position
- Previous flight data downloaded (if applicable)

## 4. Procedure

| Step | Action | Expected Result | Notes |
|------|--------|-----------------|-------|
| 1 | Verify ANCHORS CB — IN | System powered | OVHD panel |
| 2 | Select ANCHORS → ON | INIT indication | MFD |
| 3 | Monitor self-test | PASS within 60 s | Auto sequence |
| 4 | Verify STANDBY mode | Green STANDBY | Status page |
| 5 | Check Battery SoH | All packs > 70% | Minimum dispatch |
| 6 | Check CO₂ cartridge | Fill level > 10% | Capacity available |
| 7 | Verify no faults | No amber/red | EICAS/ECAM |

## 5. Completion Criteria

- ANCHORS system in STANDBY mode
- No active faults or warnings
- Battery SoH meets dispatch requirements
- CO₂ cartridge capacity sufficient for planned flight

## 6. Related Documents

- [53-10-00-OPS_Overview.md](../53-10-00-OPS_Overview.md) — Operations Overview
- [53-10-01-002_Fuselage_ANCHORS_Exterior_Check.md](./53-10-01-002_Fuselage_ANCHORS_Exterior_Check.md) — Exterior check

## 7. Traceability

| Requirement ID | Description |
|----------------|-------------|
| REQ-53-10-001 | Pre-flight ANCHORS initialization |
| REQ-53-30-001 | Battery SoH minimum for dispatch |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---

*END OF DOCUMENT*
