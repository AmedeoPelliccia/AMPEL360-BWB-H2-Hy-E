# 57-00-03-60 — Load Cases Index

## Purpose

This document provides an index to structural load cases for ATA 57 (WINGS), with links to analysis content under 57-00-06_Engineering.

## Scope

Load cases cover all design conditions per [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) structural requirements.

## Load Cases Summary

### Flight Loads (CS-25.321–365)

| Case ID | Description | CS-25 Ref | Analysis |
|---------|-------------|-----------|----------|
| LC-57-FL-001 | Symmetric pull-up | CS-25.331 | Pending |
| LC-57-FL-002 | Symmetric push-over | CS-25.331 | Pending |
| LC-57-FL-003 | Rolling maneuver (aileron) | CS-25.349 | Pending |
| LC-57-FL-004 | Yaw maneuver | CS-25.351 | Pending |
| LC-57-FL-005 | Pitch maneuver | CS-25.331 | Pending |
| LC-57-FL-006 | Vertical gust (1-cos) | CS-25.341 | Pending |
| LC-57-FL-007 | Lateral gust | CS-25.341 | Pending |
| LC-57-FL-008 | Continuous turbulence | CS-25.341 | Pending |
| LC-57-FL-009 | High-lift configuration | CS-25.345 | Pending |

### Ground Loads (CS-25.471–519)

| Case ID | Description | CS-25 Ref | Analysis |
|---------|-------------|-----------|----------|
| LC-57-GL-001 | Level landing | CS-25.473 | Pending |
| LC-57-GL-002 | One-wheel landing | CS-25.479 | Pending |
| LC-57-GL-003 | Side load landing | CS-25.485 | Pending |
| LC-57-GL-004 | Braked roll | CS-25.493 | Pending |
| LC-57-GL-005 | Pivoting | CS-25.499 | Pending |
| LC-57-GL-006 | Towing | CS-25.509 | Pending |
| LC-57-GL-007 | Jacking | CS-25.519 | Pending |

### Emergency and Limit Cases

| Case ID | Description | CS-25 Ref | Analysis |
|---------|-------------|-----------|----------|
| LC-57-EM-001 | Emergency landing | CS-25.561 | Pending |
| LC-57-EM-002 | Ditching | CS-25.563 | Pending |
| LC-57-EM-003 | Bird strike | Special condition | Pending |

### Fatigue and Damage Tolerance

| Case ID | Description | Reference | Analysis |
|---------|-------------|-----------|----------|
| LC-57-FT-001 | Standard fatigue spectrum | AMC 25.571 | Pending |
| LC-57-FT-002 | Damage tolerance crack growth | AMC 25.571 | Pending |
| LC-57-FT-003 | Residual strength | AMC 25.571 | Pending |

### Flutter and Aeroelastic

| Case ID | Description | CS-25 Ref | Analysis |
|---------|-------------|-----------|----------|
| LC-57-AE-001 | Flutter survey | CS-25.629 | Pending |
| LC-57-AE-002 | Divergence | CS-25.629 | Pending |
| LC-57-AE-003 | Control reversal | CS-25.629 | Pending |
| LC-57-AE-004 | Failure cases | CS-25.629(d) | Pending |

---

## Load Combinations

| Combination ID | Description | Load Cases Combined |
|----------------|-------------|---------------------|
| COMB-57-001 | Max positive load factor + max fuel | LC-57-FL-001 |
| COMB-57-002 | Max negative load factor + min fuel | LC-57-FL-002 |
| COMB-57-003 | Max roll + gust | LC-57-FL-003 + LC-57-FL-006 |
| COMB-57-004 | Landing + roll | LC-57-GL-001 + LC-57-GL-004 |

---

## Analysis Links

### Engineering Analysis Location

Detailed load analysis reports are located in:

- [57-00-06_Engineering](../../57-00-06_Engineering/)
  - `Loads/` — Load analysis reports
  - `Stress/` — Stress analysis reports
  - `Fatigue/` — Fatigue analysis reports
  - `Flutter/` — Aeroelastic analysis reports

### External Models and Simulation

- Aeroelastic models — [57-40_Software](../../../57-40_Software/)
- FEM models — [57-00-06_Engineering](../../57-00-06_Engineering/)

---

## Traceability

### Upstream

- [57-00-03-60_Structural_Requirements.md](./57-00-03-60_Structural_Requirements.md)
- [57-00-03-40_Regulatory_Requirements.md](../57-00-03-40_COMPLIANCE/57-00-03-40_Regulatory_Requirements.md)

### Downstream

- [57-00-06_Engineering](../../57-00-06_Engineering/) — Analysis reports
- [57-00-07_V_AND_V](../../57-00-07_V_AND_V/) — Test correlation

---

## Document Control

| Field | Value |
|-------|-------|
| Generated with | AI assistance (GitHub Copilot) |
| Prompted by | **Amedeo Pelliccia** |
| Status | **DRAFT** |
| Human Approver | _[to be completed]_ |
| Repository | `AMPEL360-BWB-H2-Hy-E` |
| Last AI Update | 2025-11-29 |

---
