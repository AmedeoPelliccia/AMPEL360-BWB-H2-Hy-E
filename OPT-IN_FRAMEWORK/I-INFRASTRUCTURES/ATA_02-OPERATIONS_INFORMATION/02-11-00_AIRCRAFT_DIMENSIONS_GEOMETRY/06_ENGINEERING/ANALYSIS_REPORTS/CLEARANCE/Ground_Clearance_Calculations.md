# Ground Clearance Calculations — AMPEL360 Q100 INTEGRA BWB

## 1. Summary

This document presents the baseline landing gear geometry parameters for the
AMPEL360 Q100 INTEGRA Blended Wing Body configuration. Values listed here
are frozen and monitored by the Geometry Baseline Watchdog CI workflow.

## 2. Landing Gear Geometry

- Main landing gear (MLG) height: **1.5 m**
- Nose landing gear (NLG) height: **1.2 m**
- Wheelbase: **15.0 m**
- Main gear track: **8.0 m**

## 3. Ground Clearance Assessment

| Condition            | Clearance (m) | Requirement (m) | Margin |
|---------------------|--------------|----------------|--------|
| Static, MTOW        | 0.45         | 0.30           | +50 %  |
| Max nose-up rotation | 0.25         | 0.15           | +67 %  |
| One-wheel landing    | 0.20         | 0.10           | +100 % |

## 4. Design Notes

The landing gear arrangement is a tricycle configuration with the MLG
retracting inboard into the centre-body. Track and wheelbase are set to
satisfy lateral tip-over stability (55° cone) and directional control
on wet runways per CS-25.237.

## 5. Traceability

- Baseline source: `01_OVERVIEW/baseline_dimensions.json`
- Requirements: REQ-02-11-020 (MLG height), REQ-02-11-021 (NLG height)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-AIR-T`
- Last AI update: _2026-02-27_.

---
