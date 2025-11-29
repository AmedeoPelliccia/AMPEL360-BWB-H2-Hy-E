# 57-00-03-30 — Safety Allocation

## Purpose

This document allocates wing safety requirements to subsystems and digital protections (ATA 22/27/34).

## Scope

Allocation covers all safety requirements from [57-00-03-30_Safety_Requirements.md](./57-00-03-30_Safety_Requirements.md).

## Allocation to Wing Subsystems

### Structural Safety Allocation

| Requirement | 57-21 Wing Box | 57-22 LE | 57-23 TE | 57-25 BWB | 57-29 Attach |
|-------------|----------------|----------|----------|-----------|--------------|
| RQ-57-00-03-30-001 | ● | ● | ● | ● | ● |
| RQ-57-00-03-30-002 | ● | ● | ● | ● | ● |
| RQ-57-00-03-30-003 | ● | ● | ● | ● | ● |

### Flight Safety Allocation

| Requirement | 57-22 LE | 57-23 TE | 57-27 Controls | ATA 22 | ATA 27 |
|-------------|----------|----------|----------------|--------|--------|
| RQ-57-00-03-30-010 | ● | ● | — | ● | ● |
| RQ-57-00-03-30-011 | — | ● | ● | ● | ● |
| RQ-57-00-03-30-012 | — | ● | ● | ● | — |

### Systems Safety Allocation

| Requirement | 57-26 Fuel | ATA 28 | ATA 30 | ATA 24 |
|-------------|------------|--------|--------|--------|
| RQ-57-00-03-30-020 | ● | ● | — | — |
| RQ-57-00-03-30-021 | — | — | ● | ● |
| RQ-57-00-03-30-022 | — | — | — | ● |

**Legend:**
- ● = Primary allocation
- — = Not applicable

## Digital Protection Allocation

### ATA 22 (Auto Flight) Protection

| Hazard | Protection | Requirement |
|--------|------------|-------------|
| Loss of lift | Stall protection | RQ-57-00-03-30-010 |
| Control surface runaway | Rate limiting | RQ-57-00-03-30-011 |
| Flutter | Active suppression | RQ-57-00-03-30-012 |

### ATA 27 (Flight Controls) Protection

| Hazard | Protection | Requirement |
|--------|------------|-------------|
| Control jam | Redundant paths | RQ-57-00-03-30-011 |
| Surface failure | Failure annunciation | RQ-57-00-03-30-011 |
| Asymmetric deployment | Position monitoring | RQ-57-00-03-30-011 |

### ATA 34 (Navigation) Support

| Function | Contribution | Requirement |
|----------|--------------|-------------|
| Air data | AOA sensing for stall warning | RQ-57-00-03-30-010 |
| Pitot/static | Airspeed for envelope protection | RQ-57-00-03-30-012 |

## OFEC Integration (23-95-61)

Safety-related telemetry requirements:

| Parameter | Source | Update Rate | Purpose |
|-----------|--------|-------------|---------|
| Structural loads | SHM | 10 Hz | Damage detection |
| Control position | ATA 27 | 20 Hz | Failure detection |
| Flutter proximity | Aeroelastics | 5 Hz | Protection system |

## Traceability

### Parent Requirements

- [57-00-03-30_Safety_Requirements.md](./57-00-03-30_Safety_Requirements.md)

### Related ATA Chapters

- ATA 22 — Auto Flight
- ATA 24 — Electrical Power
- ATA 27 — Flight Controls
- ATA 28 — Fuel
- ATA 30 — Ice and Rain Protection
- ATA 34 — Navigation

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
