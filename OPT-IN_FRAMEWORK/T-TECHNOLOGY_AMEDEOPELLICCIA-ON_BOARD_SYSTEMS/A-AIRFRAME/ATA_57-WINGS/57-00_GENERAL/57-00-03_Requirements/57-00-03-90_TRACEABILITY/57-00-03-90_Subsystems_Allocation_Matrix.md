# 57-00-03-90 — Subsystems Allocation Matrix

## Purpose

This document provides the mapping of chapter-level requirements to 57-20 subsystems.

## Scope

Allocation covers all chapter-level requirements and their distribution to wing subsystems.

## Subsystem Structure

| Code | Subsystem | Description |
|------|-----------|-------------|
| 57-21 | Wing Box | Primary structural box |
| 57-22 | Leading Edge | LE structure, slats, ice protection |
| 57-23 | Trailing Edge | TE structure, flaps, ailerons, spoilers |
| 57-24 | Wing Tip | Tip structure, winglets |
| 57-25 | Wing-Body Fairing | BWB blend zone |
| 57-26 | Fuel System Integration | Wing fuel tanks, interfaces |
| 57-27 | Control Surfaces | Movable surfaces, actuation |
| 57-28 | Secondary Structure | Access panels, fairings |
| 57-29 | Wing Attachments | Root fittings, interfaces |

---

## Allocation Matrix

### Functional Requirements (57-00-03-10)

| Requirement | 57-21 | 57-22 | 57-23 | 57-24 | 57-25 | 57-26 | 57-27 | 57-28 | 57-29 |
|-------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| RQ-57-00-03-10-001 | ● | ● | ● | ● | ● | — | — | — | — |
| RQ-57-00-03-10-002 | ● | ● | ● | ● | ● | — | — | — | — |
| RQ-57-00-03-10-010 | — | ● | ● | — | — | — | ● | — | — |
| RQ-57-00-03-10-020 | ● | — | — | — | — | ● | — | — | — |
| RQ-57-00-03-10-030 | — | ● | — | ● | — | — | — | — | — |
| RQ-57-00-03-10-040 | — | ● | — | — | — | — | — | — | — |
| RQ-57-00-03-10-041 | ● | ● | ● | — | ● | — | — | — | ● |

### Safety Requirements (57-00-03-30)

| Requirement | 57-21 | 57-22 | 57-23 | 57-24 | 57-25 | 57-26 | 57-27 | 57-28 | 57-29 |
|-------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| RQ-57-00-03-30-001 | ● | ● | ● | ● | ● | — | — | — | ● |
| RQ-57-00-03-30-002 | ● | ● | ● | ● | ● | — | — | — | ● |
| RQ-57-00-03-30-003 | ● | ● | ● | ● | ● | — | — | — | ● |
| RQ-57-00-03-30-010 | — | ● | ● | — | ● | — | ● | — | — |
| RQ-57-00-03-30-011 | — | — | ● | — | — | — | ● | — | — |
| RQ-57-00-03-30-020 | ● | — | — | — | — | ● | — | — | — |

### Structural Requirements (57-00-03-60)

| Requirement | 57-21 | 57-22 | 57-23 | 57-24 | 57-25 | 57-26 | 57-27 | 57-28 | 57-29 |
|-------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| RQ-57-00-03-60-001 | ● | ● | ● | ● | ● | ○ | ○ | ○ | ● |
| RQ-57-00-03-60-002 | ● | ● | ● | ● | ● | ○ | ○ | ○ | ● |
| RQ-57-00-03-60-010 | ● | ● | ● | ● | ● | — | — | — | ● |
| RQ-57-00-03-60-011 | ● | ● | ● | ● | ● | — | — | — | ● |

### Interface Requirements (57-00-03-50)

| Requirement | 57-21 | 57-22 | 57-23 | 57-24 | 57-25 | 57-26 | 57-27 | 57-28 | 57-29 |
|-------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| RQ-57-00-03-50-001 | ● | — | — | — | ● | — | — | — | ● |
| RQ-57-00-03-50-010 | ● | — | — | — | — | ● | — | — | — |
| RQ-57-00-03-50-011 | — | ● | — | ● | — | — | — | — | — |
| RQ-57-00-03-50-013 | ● | ● | ● | ● | ● | ● | ● | ● | ● |

### Digital Requirements (57-00-03-80)

| Requirement | 57-21 | 57-22 | 57-23 | 57-24 | 57-25 | 57-26 | 57-27 | 57-28 | 57-29 |
|-------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| RQ-57-00-03-80-010 | ● | ● | ● | — | ● | — | — | — | ● |
| RQ-57-00-03-80-030 | ● | — | — | — | ● | — | — | — | ● |
| RQ-57-00-03-80-042 | — | — | ● | — | — | — | ● | — | — |

**Legend:**
- ● = Primary allocation
- ○ = Secondary allocation (supporting)
- — = Not applicable

---

## Allocation Summary

| Subsystem | Requirements Allocated |
|-----------|----------------------|
| 57-21 Wing Box | 18 |
| 57-22 Leading Edge | 14 |
| 57-23 Trailing Edge | 15 |
| 57-24 Wing Tip | 8 |
| 57-25 Wing-Body Fairing | 12 |
| 57-26 Fuel Integration | 5 |
| 57-27 Control Surfaces | 8 |
| 57-28 Secondary Structure | 3 |
| 57-29 Wing Attachments | 12 |

---

## Derived Requirements

Each allocation generates derived requirements at the subsystem level. These are tracked in:

- `57-20_Subsystems/57-21_Wing_Box/Requirements/`
- `57-20_Subsystems/57-22_Leading_Edge/Requirements/`
- etc.

---

## Related Documents

- [57-00-03-10_Functional_Decomposition.md](../57-00-03-10_FUNCTIONAL/57-00-03-10_Functional_Decomposition.md)
- [57-00-03-90_Req_Traceability_Matrix.md](./57-00-03-90_Req_Traceability_Matrix.md)
- [57-20_Subsystems](../../../57-20_Subsystems/)

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
