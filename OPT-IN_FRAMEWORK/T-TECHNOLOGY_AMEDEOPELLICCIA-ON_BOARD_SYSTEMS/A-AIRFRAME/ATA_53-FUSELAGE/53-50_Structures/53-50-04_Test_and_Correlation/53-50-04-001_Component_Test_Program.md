# 53-50-04-001 Component Test Program

## Document Information

- **Document ID**: 53-50-04-001
- **Title**: Component Test Program
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Testing
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document defines the component test program for the AMPEL360 BWB fuselage structure, providing validation of design allowables, joint strengths, and damage tolerance characteristics.

## Scope

The component test program includes:
- Material characterization tests
- Allowables development tests
- Subcomponent static tests
- Subcomponent fatigue tests
- Damage tolerance validation tests

## Test Matrix Summary

### Material Characterization

| Test Type | Specimens | Material | Standard |
|-----------|-----------|----------|----------|
| Tension (0°, 90°, ±45°) | 30 each | IM7/8552 | ASTM D3039 |
| Compression (0°, 90°) | 20 each | IM7/8552 | ASTM D6641 |
| Shear (in-plane) | 15 | IM7/8552 | ASTM D3518 |
| Open-hole tension | 20 | IM7/8552 | ASTM D5766 |
| Open-hole compression | 20 | IM7/8552 | ASTM D6484 |
| CAI (various energies) | 30 | IM7/8552 | ASTM D7137 |

### Joint and Fitting Tests

| Test Article | Quantity | Test Type | Purpose |
|--------------|----------|-----------|---------|
| Splice joint (longitudinal) | 6 | Static tension | Ultimate strength |
| Splice joint (circumferential) | 4 | Static shear | Shear strength |
| Frame clip | 10 | Pull-off | Attachment strength |
| Stringer run-out | 4 | Compression | Termination strength |
| Door surround | 2 | Pressure cycle | Fatigue life |
| Window frame | 3 | Pressure cycle | Fatigue life |
| MLG fitting | 2 | Static + fatigue | Certification |

### Subcomponent Tests

| Test Article | Size | Test Type | Loads Applied |
|--------------|------|-----------|---------------|
| Skin-stringer panel (crown) | 1m × 2m | Compression | Axial + pressure |
| Skin-stringer panel (keel) | 1m × 2m | Tension | Axial + pressure |
| Frame section | 3m arc | Pressure | Internal + bending |
| Door cutout panel | 2m × 3m | Pressure + fatigue | Combined |

## Test Schedule

| Test Phase | Start Date | End Date | Status |
|------------|------------|----------|--------|
| Material characterization | 2024-06 | 2025-03 | Complete |
| Allowables development | 2024-09 | 2025-06 | Complete |
| Joint tests | 2025-01 | 2025-09 | In progress |
| Subcomponent static | 2025-06 | 2026-03 | Planned |
| Subcomponent fatigue | 2025-09 | 2026-12 | Planned |

## Test Facilities

| Test Type | Facility | Equipment |
|-----------|----------|-----------|
| Coupon tests | Materials lab | MTS 100 kN |
| Component static | Structures lab | MTS 2 MN |
| Pressure cycling | Barrel test rig | Pneumatic loading |
| Fatigue | Fatigue lab | Servo-hydraulic |

## Data Requirements

- Load-displacement curves
- Strain gauge data (bonded + optical)
- DIC (Digital Image Correlation) for buckling
- Acoustic emission for damage onset
- Post-test fractography

## References

### Regulatory Documents
- [CS-25.307 Proof of Structure](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [Test Matrix](ASSETS/Test_Matrix.csv)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
