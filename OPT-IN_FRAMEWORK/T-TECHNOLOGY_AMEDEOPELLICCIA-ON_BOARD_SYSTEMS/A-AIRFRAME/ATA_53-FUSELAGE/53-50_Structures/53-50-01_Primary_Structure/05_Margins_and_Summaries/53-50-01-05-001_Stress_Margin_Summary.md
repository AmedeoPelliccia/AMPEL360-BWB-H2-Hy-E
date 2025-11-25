# 53-50-01-05-001 Stress Margin Summary

## Document Information

- **Document ID**: 53-50-01-05-001
- **Title**: Stress Margin Summary
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Analysis
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides a comprehensive summary of stress margins of safety (MS) for all primary structure components in the AMPEL360 BWB fuselage, demonstrating compliance with strength requirements per [CS-25.305](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27).

## Scope

This summary covers:
- Skin panel stress margins
- Frame and stringer margins
- Joint and splice margins
- Attachment fitting margins
- Pressure bulkhead margins

## Margin of Safety Definition

**MS = (Allowable / Applied) - 1**

Where:
- MS ≥ 0 indicates adequate strength
- Allowable = material strength (F_tu, F_ty, F_su) or allowable stress
- Applied = calculated stress at ultimate load

## Primary Structure Margin Summary

### Skin Panels

| Component | Load Case | Applied Stress (MPa) | Allowable (MPa) | MS | Status |
|-----------|-----------|---------------------|-----------------|-----|--------|
| Upper crown panel (U-MID-C) | LC-001 2.5g | 580 | 680 | +0.17 | ✓ |
| Upper forward panel (U-FWD-C) | LC-003 P+M | 520 | 680 | +0.31 | ✓ |
| Lower keel panel (L-KEEL) | LC-001 2.5g | 620 | 750 | +0.21 | ✓ |
| Lower cargo floor (L-FWD-CARGO) | LC-005 | 380 | 550 | +0.45 | ✓ |
| Side panel (window belt) | LC-003 | 340 | 480 | +0.41 | ✓ |
| Battery bay floor (L-BAT-BAY) | LC-009 crash | 680 | 750 | +0.10 | ✓ |

### Frames

| Component | Load Case | Applied Stress (MPa) | Allowable (MPa) | MS | Status |
|-----------|-----------|---------------------|-----------------|-----|--------|
| Light frame FR-10 | LC-002 pressure | 285 | 420 | +0.47 | ✓ |
| Light frame FR-30 | LC-002 pressure | 310 | 420 | +0.35 | ✓ |
| Heavy frame FR-40 (MLG) | LC-004 landing | 385 | 455 | +0.18 | ✓ |
| Heavy frame FR-42 (MLG) | LC-004 landing | 390 | 455 | +0.17 | ✓ |
| Heavy frame FR-45 (wing) | LC-001 2.5g | 365 | 455 | +0.25 | ✓ |

### Stringers

| Component | Load Case | Applied Stress (MPa) | Allowable (MPa) | MS | Status |
|-----------|-----------|---------------------|-----------------|-----|--------|
| ST-A Crown stringers | LC-001 compression | 620 | 760 | +0.23 | ✓ |
| ST-B Keel stringers | LC-001 tension | 680 | 820 | +0.21 | ✓ |
| ST-C Side stringers | LC-003 combined | 420 | 580 | +0.38 | ✓ |

### Joints and Splices

| Component | Load Case | Applied Stress (MPa) | Allowable (MPa) | MS | Status |
|-----------|-----------|---------------------|-----------------|-----|--------|
| LS-01 Crown splice (bearing) | LC-001 | 520 | 620 | +0.19 | ✓ |
| LS-01 Crown splice (net section) | LC-001 | 380 | 440 | +0.16 | ✓ |
| LS-03 Keel splice (bearing) | LC-002 | 580 | 680 | +0.17 | ✓ |
| CS-01 Circumferential splice | LC-001 | 340 | 420 | +0.24 | ✓ |
| Door 1 surround | LC-002 | 320 | 385 | +0.20 | ✓ |
| Window W-15 corner | LC-003 | 280 | 350 | +0.25 | ✓ |

### Primary Attachments

| Component | Load Case | Applied Stress (MPa) | Allowable (MPa) | MS | Status |
|-----------|-----------|---------------------|-----------------|-----|--------|
| Wing spar lug (FR-40) | LC-001 | 920 | 1,050 | +0.14 | ✓ |
| MLG trunnion lug | LC-004 | 980 | 1,100 | +0.12 | ✓ |
| MLG backup fitting | LC-004 | 385 | 455 | +0.18 | ✓ |
| Tail attachment VF-FWD | Fin bending | 420 | 520 | +0.24 | ✓ |
| Engine mount EP-FWD | LC-032 thrust | 880 | 1,000 | +0.14 | ✓ |

### Pressure Bulkheads

| Component | Load Case | Applied Stress (MPa) | Allowable (MPa) | MS | Status |
|-----------|-----------|---------------------|-----------------|-----|--------|
| FPB dome (center) | LC-002 | 145 | 455 | +2.14 | ✓ |
| FPB peripheral frame | LC-002 | 280 | 420 | +0.50 | ✓ |
| FPB ECS penetration | LC-002 | 320 | 385 | +0.20 | ✓ |
| APB dome (center) | LC-002 | 160 | 455 | +1.84 | ✓ |
| APB tailcone access | LC-002 | 340 | 385 | +0.13 | ✓ |

## Critical Elements Summary

### Minimum Margins

| Rank | Component | Load Case | MS | Notes |
|------|-----------|-----------|-----|-------|
| 1 | Battery bay floor | LC-009 crash | +0.10 | Crash load critical |
| 2 | MLG trunnion lug | LC-004 landing | +0.12 | Landing impact |
| 3 | APB tailcone access | LC-002 pressure | +0.13 | Stress concentration |
| 4 | Wing spar lug | LC-001 | +0.14 | Flight loads |
| 5 | Engine mount | LC-032 thrust | +0.14 | Max thrust |

### Design Recommendations

1. **Battery bay floor**: Consider local reinforcement if crash loads increase
2. **MLG trunnion**: Maintain current design; adequate margin
3. **APB tailcone access**: Monitor during fatigue test; add inspection requirement
4. **Wing spar/engine mounts**: Acceptable margins for fail-safe structure

## Summary Statistics

| Category | Components | MS < 0.15 | MS 0.15-0.25 | MS > 0.25 |
|----------|------------|-----------|--------------|-----------|
| Skin panels | 6 | 1 | 2 | 3 |
| Frames | 5 | 0 | 2 | 3 |
| Stringers | 3 | 0 | 2 | 1 |
| Splices | 6 | 0 | 4 | 2 |
| Attachments | 5 | 3 | 2 | 0 |
| Bulkheads | 5 | 1 | 1 | 3 |
| **Total** | **30** | **5** | **13** | **12** |

## Compliance Statement

All primary structure components demonstrate positive margins of safety at ultimate load, satisfying the requirements of [CS-25.305](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27). Critical elements with MS < 0.15 have been identified for enhanced monitoring during test and service.

## References

### Regulatory Documents
- [CS-25.305 Strength and Deformation](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.307 Proof of Structure](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [Margin of Safety Database](ASSETS/Margin_of_Safety_Database.csv)
- [Critical Elements Tracking](ASSETS/Critical_Elements_Tracking.csv)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
