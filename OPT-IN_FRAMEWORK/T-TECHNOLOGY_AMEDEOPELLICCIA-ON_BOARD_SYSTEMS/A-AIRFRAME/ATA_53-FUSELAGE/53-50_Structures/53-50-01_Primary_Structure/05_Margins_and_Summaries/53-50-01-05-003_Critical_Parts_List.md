# 53-50-01-05-003 Critical Parts List

## Document Information

- **Document ID**: 53-50-01-05-003
- **Title**: Critical Parts List
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Analysis
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document identifies and tracks critical structural parts in the AMPEL360 BWB fuselage that require special attention during design, manufacturing, and in-service maintenance per [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27).

## Scope

Critical parts are classified into:
- **PSE (Principal Structural Elements)**: Carry significant flight/ground loads; failure could be catastrophic
- **FSF (Fatigue Sensitive Features)**: Subject to cyclic loading with potential for fatigue cracking
- **DT (Damage Tolerant)**: Designed for slow crack growth with mandatory inspection

## Classification Criteria

| Classification | Definition | Inspection Requirement |
|----------------|------------|------------------------|
| PSE | Single load path, critical for safety | Enhanced NDI, tracking |
| FSF | Fatigue-critical location | Periodic inspection |
| DT | Damage-tolerant design | Scheduled inspection intervals |
| Standard | Redundant structure | Routine maintenance |

## Critical Parts Summary

### PSE - Principal Structural Elements

| Part ID | Description | Location | Material | Criticality |
|---------|-------------|----------|----------|-------------|
| PSE-001 | MLG Trunnion Fitting (LH) | Station 20m | Ti-6Al-4V | Flight + Ground |
| PSE-002 | MLG Trunnion Fitting (RH) | Station 20m | Ti-6Al-4V | Flight + Ground |
| PSE-003 | Wing Main Spar Lug (LH) | Station 20m | Ti-6Al-4V | Flight |
| PSE-004 | Wing Main Spar Lug (RH) | Station 20m | Ti-6Al-4V | Flight |
| PSE-005 | Engine Forward Mount (LH) | Station 34.5m | Ti-6Al-4V | Propulsion |
| PSE-006 | Engine Forward Mount (RH) | Station 34.5m | Ti-6Al-4V | Propulsion |
| PSE-007 | Thrust Link (LH) | Station 34.5m | 4340 Steel | Propulsion |
| PSE-008 | Thrust Link (RH) | Station 34.5m | 4340 Steel | Propulsion |

### FSF - Fatigue Sensitive Features

| Part ID | Description | Location | Feature | Life Limit (FC) |
|---------|-------------|----------|---------|-----------------|
| FSF-001 | Door 1 Corner Reinforcement | Station 10m | Cutout corner | Monitor |
| FSF-002 | Door 2 Corner Reinforcement | Station 20m | Cutout corner | Monitor |
| FSF-003 | Window Belt (all windows) | Stations 8-35m | Window corners | Monitor |
| FSF-004 | Crown Splice LS-01 | Centerline | Fastener holes | Monitor |
| FSF-005 | Keel Splice LS-03 | Centerline | Fastener holes | Monitor |
| FSF-006 | FPB ECS Penetration | Station 2.5m | Cutout edge | Monitor |
| FSF-007 | APB Tailcone Access | Station 38m | Cutout edge | Monitor |

### DT - Damage Tolerant Elements

| Part ID | Description | Initial Flaw | Critical Length | Inspection Interval |
|---------|-------------|--------------|-----------------|---------------------|
| DT-001 | Upper crown skin | 1.27 mm | 50 mm | 6,000 FC |
| DT-002 | Lower keel skin | 1.27 mm | 60 mm | 8,000 FC |
| DT-003 | Door surround | 0.5 mm | 25 mm | 4,000 FC |
| DT-004 | Window frame | 0.5 mm | 15 mm | 3,000 FC |
| DT-005 | Frame FR-40 (MLG) | 1.0 mm | 30 mm | 5,000 FC |

## Tracking Requirements

### PSE Tracking

| Part ID | Serial Number Required | Traceability | Life Tracking |
|---------|----------------------|--------------|---------------|
| PSE-001 to PSE-008 | Yes | Full material + process | Hours + cycles |

### Inspection Requirements

| Classification | Inspection Type | Frequency | Method |
|----------------|----------------|-----------|--------|
| PSE | Detailed | Every C-check | FPI/ET + Visual |
| FSF | General | Every 2A-check | Visual + HFEC |
| DT | Detailed | Per interval | UT/HFEC |
| Standard | General | Per MPD | Visual |

## Manufacturing Requirements

### PSE Manufacturing Controls

| Control | Requirement |
|---------|-------------|
| Material certification | Full traceability, heat/lot numbers |
| Process qualification | Special process certification |
| NDI | 100% coverage, enhanced technique |
| Documentation | Complete traveler, buy-off stamps |
| First article | Mandatory first article inspection |

### Quality Alerts

| Alert ID | Part | Issue | Status |
|----------|------|-------|--------|
| QA-001 | PSE-001/002 | Bore surface finish | Closed (process qualified) |
| QA-002 | FSF-001/002 | Corner radius tolerance | Open (monitoring) |

## Maintenance Planning

### PSE Maintenance Tasks

| Task ID | Part | Task Description | Interval | M-H |
|---------|------|------------------|----------|-----|
| PSE-T-001 | MLG Trunnion | FPI inspection | 6C | 8 |
| PSE-T-002 | Wing Spar Lug | Detailed visual + HFEC | 4C | 4 |
| PSE-T-003 | Engine Mount | FPI + dimensional | 3C | 6 |
| PSE-T-004 | Thrust Link | FPI + proof load | 12C | 12 |

## Retirement/Life Limits

| Part ID | Safe Life (FC) | Safe Life (FH) | Retirement Action |
|---------|----------------|----------------|-------------------|
| PSE-001/002 | 60,000 | 90,000 | Replace or overhaul |
| PSE-007/008 | 40,000 | 60,000 | Replace |
| All others | On-condition | On-condition | Per DT assessment |

## Design Changes

Any design change affecting critical parts requires:
- Stress analysis update
- Fatigue/DT analysis update
- Certification authority approval
- Service bulletin if in-service

## References

### Regulatory Documents
- [CS-25.571 Damage Tolerance and Fatigue Evaluation](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.1529 Instructions for Continued Airworthiness](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [Critical Elements Tracking](ASSETS/Critical_Elements_Tracking.csv)
- [53-50-03 Fatigue and Damage Tolerance](../../53-50-03_Fatigue_and_Damage_Tolerance/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
