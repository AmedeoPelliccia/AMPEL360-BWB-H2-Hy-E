# 57-00-03-10 — Functional Decomposition

## Purpose

This document maps chapter-level functional requirements to the subsystem structure in 57-20_Subsystems.

## Scope

Decomposition covers all functional requirements from [57-00-03-10_Functional_Requirements.md](./57-00-03-10_Functional_Requirements.md).

## Subsystem Structure

The wing subsystems follow this hierarchy:

| Code | Subsystem | Description |
|------|-----------|-------------|
| 57-21 | Wing Box | Primary structural load path |
| 57-22 | Leading Edge | LE structure, slats, ice protection |
| 57-23 | Trailing Edge | TE structure, flaps, ailerons, spoilers |
| 57-24 | Wing Tip | Tip structure, winglets (if applicable) |
| 57-25 | Wing-Body Fairing | BWB blend zone |
| 57-26 | Fuel System Integration | Wing fuel tanks, interfaces |
| 57-27 | Control Surfaces | Movable surfaces, actuation |
| 57-28 | Secondary Structure | Access panels, fairings |
| 57-29 | Wing Attachments | Root fittings, interfaces |

## Functional Allocation Matrix

### Lift Generation

| Requirement | 57-21 | 57-22 | 57-23 | 57-24 | 57-25 |
|-------------|-------|-------|-------|-------|-------|
| RQ-57-00-03-10-001 | ● | ● | ● | ● | ● |
| RQ-57-00-03-10-002 | ● | ● | ● | ● | ● |
| RQ-57-00-03-10-003 | — | ● | ● | — | ● |

### Flight Control Integration

| Requirement | 57-22 | 57-23 | 57-27 |
|-------------|-------|-------|-------|
| RQ-57-00-03-10-010 | ● | ● | ● |
| RQ-57-00-03-10-011 | — | ● | ● |
| RQ-57-00-03-10-012 | ● | ● | ● |

### Fuel System Integration

| Requirement | 57-21 | 57-26 |
|-------------|-------|-------|
| RQ-57-00-03-10-020 | ● | ● |
| RQ-57-00-03-10-021 | — | ● |
| RQ-57-00-03-10-022 | ● | ● |

### Ice Protection Integration

| Requirement | 57-22 | 57-24 |
|-------------|-------|-------|
| RQ-57-00-03-10-030 | ● | ● |
| RQ-57-00-03-10-031 | ● | ● |

### Sensing and Monitoring

| Requirement | 57-21 | 57-22 | 57-23 | 57-25 | 57-29 |
|-------------|-------|-------|-------|-------|-------|
| RQ-57-00-03-10-040 | — | ● | — | — | — |
| RQ-57-00-03-10-041 | ● | ● | ● | ● | ● |
| RQ-57-00-03-10-042 | ● | — | — | ● | ● |

**Legend:**
- ● = Primary allocation
- — = Not applicable

## Derived Requirements

Each allocated requirement generates derived requirements at the subsystem level. These are documented in:

- `57-20_Subsystems/57-21_Wing_Box/Requirements/`
- `57-20_Subsystems/57-22_Leading_Edge/Requirements/`
- `57-20_Subsystems/57-23_Trailing_Edge/Requirements/`
- etc.

## Traceability

### Upstream

- [57-00-03-10_Functional_Requirements.md](./57-00-03-10_Functional_Requirements.md)

### Downstream

- Subsystem requirements in [57-20_Subsystems](../../../57-20_Subsystems/)
- Verification activities in [57-00-07_V_AND_V](../../57-00-07_V_AND_V/)

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
