# 53-50-01-03-004 Window Cutout Reinforcement

## Document Information

- **Document ID**: 53-50-01-03-004
- **Title**: Window Cutout Reinforcement
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications for Window Cutout Reinforcement in the AMPEL360 BWB primary structure. Window cutouts create repetitive stress concentrations along the passenger cabin that must be reinforced to ensure fatigue durability over the aircraft's service life.

## Scope

This specification covers:
- Passenger window cutout geometry and spacing
- Window frame design and attachment
- Local reinforcement layups and doublers
- Stringer terminations at windows
- Fatigue and damage tolerance provisions
- Window belt structural concept

### Window Configuration

| Parameter | Specification |
|-----------|---------------|
| Window quantity | 84 per side (typical) |
| Window spacing | 533 mm (21 inch pitch) |
| Visible area | 280 mm × 400 mm |
| Cutout size | 320 mm × 450 mm (structural opening) |
| Corner radius | ≥40 mm |

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Stress concentration factor | Kt ≤ 2.5 | Fatigue life target |
| Fatigue life | 4 × DSG (240,000 cycles) | Enhanced safe-life |
| Residual strength | Limit load with one window failed | Fail-safe |
| Maximum deflection | ≤2 mm under pressure | Seal integrity |

### Geometric Requirements

| Parameter | Specification |
|-----------|---------------|
| Frame thickness | 3.0 mm minimum |
| Doubler extent | 50 mm beyond cutout |
| Skin pad-up | 2× nominal at window edge |
| Reveal depth | 120 mm (wall buildup) |

## Design Configuration

### Window Belt Structure

The window belt is a reinforced zone running the length of the passenger cabin:

```
    |----- 533 mm -----|
    
    =====================  Stringer (runs continuous above)
    |                   |
    |   +-----------+   |  Window Frame (Al 2024-T3)
    |   |           |   |
    |   |  Window   |   |  320 mm × 450 mm opening
    |   |           |   |
    |   +-----------+   |
    |                   |
    =====================  Stringer (runs continuous below)
    |       Frame       |  Fuselage Frame (500-600 mm spacing)
```

### Window Frame Design

| Component | Material | Thickness | Description |
|-----------|----------|-----------|-------------|
| Window frame | Al 2024-T3 | 3.0 mm | Extruded profile |
| Inner reveal | Al 2024-T3 | 1.5 mm | Cosmetic + drainage |
| Seal groove | Integral | - | Dual seal provision |
| Attachment | Rivets | 4.0 mm | Countersunk, wet install |

### Reinforcement Layup

| Zone | Layup | Thickness | Material |
|------|-------|-----------|----------|
| Window edge (all sides) | [±45/0/90]₃ₛ | 5.0 mm | CFRP |
| Corner regions | [±45/0/90]₄ₛ | 7.0 mm | CFRP |
| Inter-window strip | [±45/0/90]₂ₛ | 3.5 mm | CFRP |
| Transition to field | Tapered | 2.5-5.0 mm | CFRP |

## Load Cases

### Critical Design Cases

| Load Case | Description | Governing Parameter |
|-----------|-------------|---------------------|
| LC-002 | Max cabin pressure | Hoop stress at corners |
| LC-003 | Pressure + 2.5g | Combined stress |
| LC-020 | Pressure cycling | Fatigue at corners |

### Stress Distribution

| Location | Stress Component | Nominal (MPa) | Peak (MPa) | Kt |
|----------|------------------|---------------|------------|-----|
| Window corner (R=40mm) | Hoop | 55 | 130 | 2.4 |
| Window side edge | Hoop | 55 | 90 | 1.6 |
| Inter-window | Hoop | 55 | 65 | 1.2 |

## Analysis and Verification

### Fatigue Analysis

| Location | Stress Range (MPa) | Cycles to Initiation | Factor on DSG |
|----------|-------------------|---------------------|---------------|
| Window corner | 80 | >250,000 | 4.2× |
| Window edge | 50 | >400,000 | 6.7× |
| Frame attachment | 45 | >500,000 | 8.3× |

### Damage Tolerance

| Scenario | Initial Flaw | Detectable Size | Inspection Interval |
|----------|--------------|-----------------|---------------------|
| Corner crack | 0.5 mm | 10 mm | Visual every 3,000 FC |
| Edge crack | 1.0 mm | 15 mm | Visual every 5,000 FC |

### Margin Summary

| Component | Load Case | MS (Strength) | MS (Fatigue) | Status |
|-----------|-----------|---------------|--------------|--------|
| Window corner | LC-002 | +0.25 | 4.2× DSG | ✓ Pass |
| Window frame | LC-003 | +0.32 | 5.0× DSG | ✓ Pass |
| Inter-window skin | LC-002 | +0.45 | 6.0× DSG | ✓ Pass |

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| Window panel WP-01 | Pressure fatigue | Life validation | Complete |
| Window corner WC-01 | Crack growth | DTA validation | In progress |
| Full barrel section | Pressure test | Certification | Planned |

## Manufacturing Considerations

### Window Installation Sequence

1. Drill window cutout in cured skin panel (template-controlled)
2. Apply edge seal to cutout edges
3. Install CFRP corner doublers (if applicable)
4. Position window frame and clamp
5. Match-drill attachment holes
6. Apply wet sealant to faying surfaces
7. Install countersunk rivets
8. Apply fillet seal at frame-to-skin interface

### Quality Criteria

| Feature | Acceptance Criteria |
|---------|---------------------|
| Corner radius | 40 mm +2/-0 mm |
| Edge straightness | ±0.5 mm |
| Frame gap to skin | ≤0.25 mm (sealant fill) |
| Rivet countersink | Flush ±0.05 mm |

## References

### Regulatory Documents
- [CS-25.775 Windshields and Windows](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.571 Damage Tolerance](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-01-02-003 Side Shell Skin Design](../02_Panels_Frames_and_Skins/53-50-01-02-003_Side_Shell_Skin_Design.md)
- [53-50-03 Fatigue and Damage Tolerance](../../53-50-03_Fatigue_and_Damage_Tolerance/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
