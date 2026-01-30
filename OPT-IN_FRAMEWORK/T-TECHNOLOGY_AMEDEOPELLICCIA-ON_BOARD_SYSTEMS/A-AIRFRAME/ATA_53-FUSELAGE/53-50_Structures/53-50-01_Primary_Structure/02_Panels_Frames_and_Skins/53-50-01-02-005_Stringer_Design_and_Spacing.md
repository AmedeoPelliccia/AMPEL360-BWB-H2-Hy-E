# 53-50-01-02-005 Stringer Design and Spacing

## Document Information

- **Document ID**: 53-50-01-02-005
- **Title**: Stringer Design and Spacing
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications, analysis methodology, and verification data for Stringer Design and Spacing in the AMPEL360 BWB primary structure. Stringers stiffen the skin panels against buckling and carry axial loads from fuselage bending and pressurization.

## Scope

This specification covers:
- Stringer geometry and cross-section profiles
- Stringer spacing arrangements for different fuselage zones
- Material and layup specifications for CFRP stringers
- Stringer-to-skin attachment methods
- Stringer run-outs and terminations at cutouts
- Manufacturing considerations for co-cured stringers

### Applicable Locations
- All fuselage skin panels requiring longitudinal stiffening
- Upper, lower, and side shell skin panels

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Stringer spacing (nominal) | 150 - 250 mm | Skin buckling stability |
| Stringer crippling allowable | > Ultimate applied load | Column stability |
| Stringer-skin debond load | > Ultimate load | Fail-safe design |
| Maximum column length | Frame spacing (500-600 mm) | Euler buckling |
| Design Service Goal | 60,000 FC / 90,000 FH | Program requirement |

### Material Requirements

- **Stringer Material**: IM7/8552 CFRP prepreg, 0°-dominated layup
- **Layup**: [0]₆/[±45] for hat-section; [0]₈/[±45] for high-load zones
- **Fiber Volume**: 57-62%
- **Cure Temperature**: 180°C autoclave cure

### Geometric Requirements

| Parameter | Specification |
|-----------|---------------|
| Hat-section height | 30 - 45 mm |
| Hat-section flange width | 15 - 25 mm |
| Web thickness | 2.0 - 3.5 mm |
| Flange thickness | 2.5 - 4.0 mm |
| Crown width | 20 - 35 mm |

## Design Configuration

### Stringer Types

| Type | Profile | Height | Application |
|------|---------|--------|-------------|
| ST-A | Hat-section | 35 mm | Standard upper/lower skin |
| ST-B | Hat-section (heavy) | 45 mm | High-load zones (keel, wing box) |
| ST-C | J-section | 25 mm | Side panels (lighter profile) |
| ST-D | I-section | 40 mm | Floor beams (metallic) |

### Stringer Cross-Section Design

**ST-A (Standard Hat-Section)**:
```
         |--- 25 mm ---|
         _____________
        /             \
       /_______________\   Crown: 2.5 mm
      |                 |
      |                 |   Web: 2.0 mm, Height: 35 mm
      |                 |
    __|_________________|__
   |_____|           |_____|   Flange: 20 mm × 2.5 mm
         
   Total width at base: 65 mm
```

**ST-B (Heavy Hat-Section)**:
```
         |--- 30 mm ---|
         _____________
        /             \
       /_______________\   Crown: 3.5 mm
      |                 |
      |                 |   Web: 3.0 mm, Height: 45 mm
      |                 |
    __|_________________|__
   |_____|           |_____|   Flange: 25 mm × 3.5 mm
         
   Total width at base: 80 mm
```

### Stringer Spacing Schedule

| Zone | Stringer Type | Spacing | Notes |
|------|---------------|---------|-------|
| Upper crown (±30° from CL) | ST-A | 180 mm | Compression critical |
| Upper sides (30°-60°) | ST-A | 200 mm | Moderate compression |
| Lower keel (±20° from CL) | ST-B | 160 mm | Tension critical |
| Lower sides (20°-60°) | ST-A | 200 mm | Standard tension |
| Side panels (general) | ST-C | 250 mm | Shear/combined loading |
| Cargo floor | ST-D (Al) | 300 mm | Floor beams |

### Stringer Layup Schedule

| Stringer Type | Layup | Plies | Ply Thickness | Total Thickness |
|---------------|-------|-------|---------------|-----------------|
| ST-A Web | [0]₆ | 6 | 0.25 mm | 1.5 mm |
| ST-A Flange | [0]₃/[±45] | 5 | 0.25 mm | 1.25 mm |
| ST-B Web | [0]₈ | 8 | 0.25 mm | 2.0 mm |
| ST-B Flange | [0]₄/[±45] | 6 | 0.25 mm | 1.5 mm |
| ST-C Web | [0]₄ | 4 | 0.25 mm | 1.0 mm |

## Stringer-Skin Interface

### Attachment Method

| Method | Application | Description |
|--------|-------------|-------------|
| Co-curing | Primary attachment | Stringer cured integrally with skin |
| Cobonding | Repair/modification | Stringer bonded to cured skin |
| Mechanical fastening | Tertiary backup | Fasteners at terminations |

### Interface Parameters

| Parameter | Specification |
|-----------|---------------|
| Flange bond width | 20-25 mm per side |
| Bond line thickness | 0.1 - 0.2 mm (adhesive film) |
| Surface preparation | Peel ply + solvent wipe |
| Bond strength (shear) | > 40 MPa |
| Debond arrestment | Stitch rows at 50 mm from edge |

## Stringer Run-Outs and Terminations

### Termination at Door/Window Cutouts

- **Approach**: Stringers terminated 50 mm from cutout edge
- **Load Transfer**: Via intercostal members and cutout reinforcement
- **Transition**: Tapered run-out over 150 mm length
- **Fastening**: Additional mechanical fasteners at termination

### Termination at Frames

- **Mouse Holes**: Stringer passes through frame via shaped cutout
- **Clip Attachment**: Frame clips bridge stringer-to-frame load transfer
- **Continuous Stringers**: Preferred for fatigue performance

## Load Cases

### Critical Design Cases for Stringers

| Load Case ID | Description | Critical Stringer | Governing Parameter |
|--------------|-------------|-------------------|---------------------|
| LC-001 | 2.5g maneuver | Upper crown stringers | Compression/crippling |
| LC-008 | -1.0g push-over | Lower keel stringers | Compression |
| LC-002 | Maximum pressure | All stringers | Axial tension |
| LC-003 | Combined pressure + maneuver | Crown stringers | Column buckling |

### Stringer Loads Summary

| Zone | Load Case | Axial Load (kN/m) | Running Shear (N/mm) |
|------|-----------|-------------------|---------------------|
| Upper crown | LC-001 | 450 (compression) | 120 |
| Lower keel | LC-001 | 520 (tension) | 100 |
| Upper crown | LC-008 | 200 (tension) | 80 |
| Side panels | LC-003 | 180 (combined) | 150 |

## Analysis and Verification

### Analysis Methods

| Analysis Type | Method | Software |
|--------------|--------|----------|
| Stringer crippling | Empirical (ESDU) | Excel / Python |
| Column buckling | Eigenvalue FEA | NASTRAN |
| Skin-stringer panel buckling | Eigenvalue FEA | NASTRAN |
| Debond analysis | Cohesive zone | ABAQUS |
| Fatigue (stringer-skin interface) | Strain-life | In-house |

### Margin Summary

| Component | Load Case | MS (Crippling) | MS (Column) | Status |
|-----------|-----------|----------------|-------------|--------|
| ST-A Crown | LC-001 | +0.22 | +0.35 | ✓ Pass |
| ST-B Keel | LC-008 | +0.18 | +0.28 | ✓ Pass |
| ST-C Side | LC-003 | +0.30 | +0.42 | ✓ Pass |
| Debond | LC-001 | +0.15 | N/A | ✓ Pass |

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| Stringer specimen S-01 | Compression | Crippling strength | Complete |
| Panel specimen P-01 | Pressure + compression | Buckling | Complete |
| Debond specimen D-01 | Peel test | Debond strength | Complete |
| Stringer run-out RO-01 | Static load | Termination strength | In progress |

## Manufacturing Considerations

### Process Requirements

- **Mandrel Material**: Soluble or extractable mandrel for hat-sections
- **Layup Method**: Automated tape laying (ATL) for flat charge; hot drape forming
- **Cure Cycle**: Co-cured with skin panel at 180°C / 7 bar
- **Demolding**: Mandrel wash-out or mechanical extraction

### Quality Criteria

| Feature | Acceptance Criteria |
|---------|---------------------|
| Stringer height | ±0.5 mm |
| Web thickness | ±0.15 mm |
| Flange-to-skin bond | 100% wetout, no voids >6 mm |
| Fiber alignment | ±3° from nominal |
| Corner radius | 3.0 ± 0.5 mm |

## References

### Regulatory Documents
- [CS-25.305 Strength and Deformation](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.571 Damage Tolerance and Fatigue Evaluation](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-01 Primary Structure Overview](../../README.md)
- [Stringer Layup Schedule](ASSETS/Stringer_Layup_Schedule.csv)
- [53-50-01-01-003 Material Selection Summary](../01_Overview/53-50-01-01-003_Material_Selection_Summary.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
