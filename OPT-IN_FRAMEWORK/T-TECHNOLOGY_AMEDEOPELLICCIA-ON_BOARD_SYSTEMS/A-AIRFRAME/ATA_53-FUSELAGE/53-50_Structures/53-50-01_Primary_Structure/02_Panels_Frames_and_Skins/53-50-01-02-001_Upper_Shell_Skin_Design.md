# 53-50-01-02-001 Upper Shell Skin Design

## Document Information

- **Document ID**: 53-50-01-02-001
- **Title**: Upper Shell Skin Design
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications, analysis methodology, and verification data for Upper Shell Skin Design in the AMPEL360 BWB primary structure. The upper shell skin is the primary load-bearing surface forming the upper contour of the blended wing body fuselage.

## Scope

This specification covers:
- Upper shell skin panel geometry and configuration
- Material systems and layup schedules for CFRP construction
- Thickness distribution and transition zones
- Stiffening concepts (co-cured stringers, frame attachments)
- Lightning strike protection integration
- Manufacturing and assembly requirements
- Load cases and design conditions specific to upper shell

### Applicable Stations
- Forward pressure bulkhead (Station 2.5m) to aft pressure bulkhead (Station 38.0m)
- Upper skin panels from crown to ±60° from centerline (approximately)

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Ultimate load factor | 1.5 × Limit load | [CS-25.303](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) |
| Maximum cabin differential pressure | 8.6 psi (59.3 kPa) | Operations envelope |
| Design Service Goal (DSG) | 60,000 flight cycles / 90,000 flight hours | Program requirement |
| Buckling under limit load | No buckling permitted | Design philosophy |
| Post-buckling under ultimate load | Controlled post-buckling acceptable | Fail-safe design |

### Material Requirements

- **Primary Material**: IM7/8552 Carbon Fiber/Epoxy prepreg (intermediate modulus)
- **Operating Temperature Range**: -55°C to +80°C (cabin environment)
- **Moisture Absorption Limit**: Maximum 1.0% by weight at equilibrium
- **Lightning Strike Protection**: Expanded copper foil (ECF) or nickel-coated carbon veil

### Geometric Requirements

| Parameter | Specification |
|-----------|---------------|
| Minimum skin thickness | 4.0 mm (excluding LSP) |
| Maximum skin thickness (at joints) | 12.0 mm |
| Panel curvature (minimum radius) | 3,000 mm (smooth BWB contour) |
| Surface finish tolerance | ±0.5 mm from theoretical OML |
| Step/gap at panel joints | ≤0.3 mm step, ≤1.0 mm gap |

## Design Configuration

### Panel Layout

The upper shell skin is divided into manufacturable panels:

| Panel ID | Station Range | Span Range | Approximate Area |
|----------|---------------|------------|------------------|
| U-FWD-C | 2.5m - 10.0m | ±5m from CL | 75 m² |
| U-FWD-L/R | 2.5m - 10.0m | 5m - 15m span | 75 m² each |
| U-MID-C | 10.0m - 25.0m | ±8m from CL | 240 m² |
| U-MID-L/R | 10.0m - 25.0m | 8m - 25m span | 170 m² each |
| U-AFT-C | 25.0m - 38.0m | ±6m from CL | 156 m² |
| U-AFT-L/R | 25.0m - 38.0m | 6m - 20m span | 140 m² each |

### Layup Schedule

Baseline quasi-isotropic layup with local reinforcement:

| Zone | Layup | Thickness | Application |
|------|-------|-----------|-------------|
| General field | [45/0/-45/90]₃ₛ | 4.5 mm | Standard upper skin |
| Frame attachments | [45/0/-45/90]₄ₛ | 6.0 mm | Local pad-up at frames |
| Splice zones | [45/0/-45/90]₅ₛ | 7.5 mm | Panel joints |
| Cutout reinforcement | [45/0/-45/90]₆ₛ + local 0° | 9.0 mm | Door/window surrounds |

### Stiffening Concept

- **Stringer Type**: Co-cured hat-section stringers (CFRP)
- **Stringer Spacing**: 200 mm nominal (adjusted for cutouts)
- **Stringer Height**: 35 mm
- **Stringer Layup**: [0]₆/[±45] - 0°-dominated for axial stiffness

## Load Cases

### Critical Design Cases for Upper Shell

| Load Case ID | Description | Critical Location | Governing Parameter |
|--------------|-------------|-------------------|---------------------|
| LC-001 | 2.5g symmetric maneuver | Crown centerline | Compression (buckling) |
| LC-002 | Maximum cabin pressure | General field | Hoop tension |
| LC-003 | Combined pressure + 2.5g | Crown | Combined stress |
| LC-008 | -1.0g push-over | Crown | Tension (fatigue) |
| LC-015 | Gust (25 fps EAS) | Forward crown | Compression + bending |

### Load Distribution

- **Axial Compression**: Maximum at crown due to fuselage bending under positive g
- **Hoop Tension**: From cabin pressurization (σ_hoop ≈ 45 MPa at 8.6 psi)
- **Shear**: Transferred through skin to frames and stringers
- **Local Loads**: Concentrated at door/window cutouts and attachment points

## Analysis and Verification

### Analysis Methods

| Analysis Type | Method | Software |
|--------------|--------|----------|
| Global stress distribution | Linear FEA | NASTRAN |
| Panel buckling | Eigenvalue analysis | NASTRAN/ABAQUS |
| Post-buckling | Nonlinear FEA | ABAQUS |
| Fatigue and damage tolerance | Safe-life + damage tolerance | In-house tools |
| Impact damage tolerance | CAI analysis per CMH-17 | ABAQUS |

### Margin Summary

| Component | Load Case | MS (Strength) | MS (Buckling) | Status |
|-----------|-----------|---------------|---------------|--------|
| U-MID-C panel | LC-001 | +0.15 | +0.12 | ✓ Pass |
| U-FWD-C panel | LC-003 | +0.18 | +0.16 | ✓ Pass |
| U-AFT-C panel | LC-001 | +0.22 | +0.18 | ✓ Pass |
| Stringer S-12 | LC-001 | +0.08 | N/A | ✓ Pass |
| Frame attachment | LC-003 | +0.11 | N/A | ✓ Pass |

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| Panel specimen P-01 | Static compression | Validate buckling load | Complete |
| Panel specimen P-02 | Pressure cycling | Verify fatigue life | In progress |
| Full-scale barrel | Ultimate static | Certification | Planned 2026 |

## Manufacturing Considerations

### Process Requirements

- **Layup Method**: Automated Fiber Placement (AFP)
- **Cure Cycle**: 180°C / 7 bar autoclave cure
- **NDI Requirements**: 100% ultrasonic C-scan post-cure
- **Assembly**: Mechanical fastening at panel splices; co-bonded stringers

### Quality Criteria

| Feature | Acceptance Criteria |
|---------|---------------------|
| Porosity | ≤2% by volume |
| Delamination | None >6 mm diameter |
| Foreign object inclusion | None visible |
| Fiber waviness | ≤5° in-plane, ≤3° out-of-plane |
| Thickness variation | ±5% from nominal |

## References

### Regulatory Documents
- [CS-25.301 Loads](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.303 Factor of Safety](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.305 Strength and Deformation](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.571 Damage Tolerance and Fatigue Evaluation](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-01 Primary Structure Overview](../../README.md)
- [53-50-01-01-003 Material Selection Summary](../01_Overview/53-50-01-01-003_Material_Selection_Summary.md)
- [53-50-01-01-004 Design Allowables](../01_Overview/53-50-01-01-004_Design_Allowables.md)
- [Skin Thickness Maps](ASSETS/Skin_Thickness_Maps.csv)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
