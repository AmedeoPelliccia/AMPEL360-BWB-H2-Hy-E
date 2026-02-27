# Lift Distribution Analysis — AMPEL360 Q100 INTEGRA BWB

## 1. Summary

This document presents the baseline aerodynamic geometry parameters for the
AMPEL360 Q100 INTEGRA Blended Wing Body configuration. Values listed here are
frozen and monitored by the Geometry Baseline Watchdog CI workflow.

## 2. Reference Geometry

- Wingspan (b): **52.0 m**
- Wing area (S): **845.0 m²**
- Aspect ratio (AR): **3.2**
- Sweep (Λ): **35.0°**

## 3. Methodology

Lift distribution was computed using a vortex-lattice method (VLM) at the
design cruise condition (M 0.85, FL 350). The spanwise loading was optimised
for minimum induced drag while respecting structural and flutter constraints.

## 4. Key Results

| Station (η) | Cl   | ΔCl/Cl_design |
|-------------|------|---------------|
| 0.00        | 0.45 | 0.0 %         |
| 0.25        | 0.52 | 0.0 %         |
| 0.50        | 0.48 | 0.0 %         |
| 0.75        | 0.38 | 0.0 %         |
| 1.00        | 0.02 | 0.0 %         |

## 5. Traceability

- Baseline source: `01_OVERVIEW/baseline_dimensions.json`
- Requirements: REQ-02-11-001 (wingspan), REQ-02-11-002 (wing area)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-AIR-T`
- Last AI update: _2026-02-27_.

---
