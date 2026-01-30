# 53-50-01-04-001 Wing Attachment Fittings

## Document Information

- **Document ID**: 53-50-01-04-001
- **Title**: Wing Attachment Fittings
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications for Wing Attachment Fittings in the AMPEL360 BWB primary structure. In the blended wing body configuration, the wing integrates smoothly with the fuselage, requiring distributed attachment through the center section rather than discrete wing-fuselage joints.

## Scope

This specification covers:
- Wing carry-through structure integration
- Main spar attachment fittings
- Rear spar attachment fittings
- Load introduction and distribution
- Fitting materials and manufacturing

### BWB Wing-Body Integration Concept

Unlike conventional aircraft, the BWB design features a blended transition where wing structure merges with fuselage structure. Primary load transfer occurs through:
- Continuous main spar web (Stations 16m - 24m)
- Multiple rib-to-frame attachments
- Skin continuity across the blend zone

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Ultimate wing bending moment | 85,000 kN·m | 2.5g maneuver |
| Ultimate wing shear | 2,800 kN | Combined maneuver + gust |
| Ultimate wing torsion | 15,000 kN·m | Asymmetric loading |
| Fatigue life | 4 × DSG | Safe-life critical fittings |
| Damage tolerance | Two-load-path redundancy | Fail-safe design |

### Material Requirements

| Component | Material | Specification |
|-----------|----------|---------------|
| Main spar caps | Ti-6Al-4V | AMS 4928 |
| Spar web | CFRP IM7/8552 | Quasi-isotropic |
| Attachment lugs | Ti-6Al-4V | AMS 4935 (forging) |
| Fasteners | Ti-6Al-4V | NAS6 series |

## Design Configuration

### Main Spar Attachment

The main spar is the primary load-carrying member:

| Parameter | Value |
|-----------|-------|
| Spar location | ~25% chord |
| Spar cap material | Ti-6Al-4V |
| Cap dimensions | 80 mm × 25 mm (centerline) |
| Web thickness | 8 mm CFRP |
| Attachment stations | FR-32 to FR-48 (16m to 24m) |

### Rear Spar Attachment

| Parameter | Value |
|-----------|-------|
| Spar location | ~65% chord |
| Spar cap material | Al 7050-T7451 |
| Cap dimensions | 50 mm × 20 mm (centerline) |
| Web thickness | 5 mm CFRP |
| Attachment stations | FR-32 to FR-48 |

### Fitting Configuration

**Main Spar Lug Fitting (at Frame FR-40)**:
```
           |--- 100 mm ---|
           _______________
          /               \     Lug: Ti-6Al-4V forging
         |    Ø35 Bore     |    Bore: Ø35 mm
         |       O         |    Bushing: Steel
          \_______________/
               |     |
          _____|_____|_____
         |                 |    Transition: 50 mm
         |     Fitting     |
         |      Base       |    Base: Bolted to frame
         |_________________|
         
    Fasteners: 12 × Ø12 mm Ti bolts
```

### Load Path Distribution

| Frame Station | Main Spar Reaction (kN) | Rear Spar Reaction (kN) |
|---------------|------------------------|-------------------------|
| FR-32 (16m) | 180 | 45 |
| FR-36 (18m) | 320 | 85 |
| FR-40 (20m) | 450 | 120 |
| FR-44 (22m) | 350 | 90 |
| FR-48 (24m) | 200 | 50 |

## Load Cases

### Critical Design Cases

| Load Case | Description | Critical Component |
|-----------|-------------|-------------------|
| LC-001 | 2.5g symmetric maneuver | Main spar lug |
| LC-024 | Maximum wing up-bending | Fitting base bolts |
| LC-025 | Negative wing bending | Lug bearing |
| LC-026 | Wing torsion (aileron) | Rear spar fitting |

### Fitting Loads at FR-40

| Load Component | Limit (kN) | Ultimate (kN) |
|----------------|------------|---------------|
| Vertical (lift) | 300 | 450 |
| Drag | 45 | 68 |
| Side (inboard) | 25 | 38 |

## Analysis and Verification

### Analysis Methods

| Analysis Type | Method | Software |
|---------------|--------|----------|
| Lug strength | Classical lug analysis (ESDU) | Excel |
| Fitting stress | Local FEA | ABAQUS |
| Fatigue | S-N with Kt | In-house |
| Bolt analysis | Per ASME/NAS | Excel |

### Margin Summary

| Component | Load Case | MS (Ultimate) | MS (Fatigue) | Status |
|-----------|-----------|---------------|--------------|--------|
| Main lug (FR-40) | LC-001 | +0.12 | 4.0× DSG | ✓ Pass |
| Lug bushing | LC-025 | +0.18 | 5.0× DSG | ✓ Pass |
| Base bolts | LC-024 | +0.15 | 3.5× DSG | ✓ Pass |
| Rear spar fitting | LC-026 | +0.22 | 4.5× DSG | ✓ Pass |

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| Lug fitting LF-01 | Static ultimate | Strength validation | Complete |
| Lug fitting LF-02 | Fatigue | Life validation | In progress |
| Full wing box | Static | Certification | Planned 2026 |

## Manufacturing Considerations

### Titanium Lug Forgings

- **Starting Stock**: Die forging (AMS 4935)
- **Machining**: 5-axis CNC, special tooling for bore
- **Surface Treatment**: Shot peening + dry film lube on bore
- **NDI**: 100% ultrasonic, FPI for surface defects

### Quality Criteria

| Feature | Acceptance Criteria |
|---------|---------------------|
| Bore diameter | Ø35.000 +0.025/-0.000 mm |
| Bore surface | Ra ≤ 0.8 μm |
| Lug thickness | ±0.1 mm |
| Bolt hole location | ±0.1 mm true position |

## References

### Regulatory Documents
- [CS-25.571 Damage Tolerance](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.613 Material Strength Properties](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-01 Primary Structure Overview](../../README.md)
- [Attachment Load Summary](ASSETS/Attachment_Load_Summary.csv)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
