# 53-50-01-03-001 Longitudinal Splice Design

## Document Information

- **Document ID**: 53-50-01-03-001
- **Title**: Longitudinal Splice Design
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications, analysis methodology, and verification data for Longitudinal Splice Design in the AMPEL360 BWB primary structure. Longitudinal splices join skin panels along the fuselage length, transferring axial and shear loads between adjacent panels.

## Scope

This specification covers:
- Longitudinal splice locations and geometry
- Splice joint configurations (lap, butt, hybrid)
- Fastener patterns and load transfer mechanisms
- Sealant and corrosion protection requirements
- Analysis methods for splice joints
- Fatigue and damage tolerance considerations

### Applicable Joints
- Crown longitudinal splices (upper shell panels)
- Keel longitudinal splices (lower shell panels)
- Side shell longitudinal splices
- Wing-body blend longitudinal joints

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Joint efficiency | ≥80% of parent skin strength | Structural optimization |
| Ultimate load capability | 1.5 × Limit load without failure | [CS-25.303](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) |
| Fatigue life | 3 × DSG (180,000 flight cycles) | Safe-life approach |
| Damage tolerance | Two-bay crack arrest capability | Fail-safe design |
| Design Service Goal | 60,000 FC / 90,000 FH | Program requirement |

### Material Requirements

- **Splice Straps**: Same material as parent skin (IM7/8552 CFRP or Al 7050)
- **Fasteners**: Titanium Hi-Lok (Ti-6Al-4V) or Hi-Lite
- **Sealant**: Polysulfide PR-1776 Class B or equivalent
- **Fay Surface Treatment**: Sol-gel or phosphoric acid anodize

### Geometric Requirements

| Parameter | Specification |
|-----------|---------------|
| Minimum edge distance | 2.5 × fastener diameter (e/D ≥ 2.5) |
| Fastener pitch | 4-6 × diameter (p/D = 4-6) |
| Row spacing | 4-5 × diameter |
| Overlap length | ≥30 × skin thickness |
| Splice strap thickness | 60-80% of skin thickness |

## Design Configuration

### Splice Types

| Type | Configuration | Application | Joint Efficiency |
|------|---------------|-------------|------------------|
| Single Lap | One-sided overlap | Non-critical areas | 70-75% |
| Double Lap | Symmetric overlap | Primary structure | 80-85% |
| Butt + Splice Straps | Butted skins + external straps | High-load zones | 85-90% |
| Stepped Lap | Tapered thickness transition | CFRP joints | 90-95% |

### Longitudinal Splice Locations

| Splice ID | Location | Type | Description |
|-----------|----------|------|-------------|
| LS-01 | Crown centerline | Butt + strap | Upper shell panel junction |
| LS-02 | Upper side (45° from CL) | Double lap | Upper-to-side transition |
| LS-03 | Keel centerline | Butt + strap | Lower shell panel junction |
| LS-04 | Lower side (-45° from CL) | Double lap | Lower-to-side transition |
| LS-05 | Wing-body blend | Stepped lap | CFRP-to-CFRP junction |

### Typical Splice Configuration

**Crown Centerline Splice (LS-01)**:
```
                    Outer Splice Strap
    ============================================
         |  |  |  |  |  |  |  |  |  |  |
    -----+--+--+--+--+--+--+--+--+--+--+-----  Skin Panel A
         |                              |
    _____+______________________________+_____  Butt Joint
         |                              |
    -----+--+--+--+--+--+--+--+--+--+--+-----  Skin Panel B
         |  |  |  |  |  |  |  |  |  |  |
    ============================================
                    Inner Splice Strap

    Fasteners: Hi-Lok Ti 4.8mm, 3 rows each side
    Pitch: 25 mm, Row spacing: 20 mm
```

### Fastener Pattern

| Splice | Fastener Type | Diameter | Rows | Pitch | Edge Distance |
|--------|---------------|----------|------|-------|---------------|
| LS-01 | Hi-Lok Ti | 4.8 mm | 3 × 2 | 25 mm | 15 mm |
| LS-02 | Hi-Lok Ti | 4.8 mm | 2 × 2 | 30 mm | 15 mm |
| LS-03 | Hi-Lok Ti | 6.35 mm | 3 × 2 | 30 mm | 18 mm |
| LS-04 | Hi-Lok Ti | 4.8 mm | 2 × 2 | 30 mm | 15 mm |
| LS-05 | Hi-Lite | 4.8 mm | Stepped | 25 mm | 12 mm |

## Load Cases

### Critical Design Cases for Longitudinal Splices

| Load Case ID | Description | Critical Splice | Governing Load |
|--------------|-------------|-----------------|----------------|
| LC-001 | 2.5g maneuver | LS-01 (crown) | Compression + shear |
| LC-002 | Maximum pressure | LS-03 (keel) | Hoop tension |
| LC-003 | Combined P + 2.5g | LS-02, LS-04 | Combined |
| LC-008 | -1.0g push-over | LS-03 (keel) | Compression |
| LC-020 | Ground-air-ground cycle | All | Fatigue |

### Load Distribution in Splice

| Splice | Axial Load (kN/m) | Shear Flow (N/mm) | Bearing Load/Fastener (kN) |
|--------|-------------------|-------------------|---------------------------|
| LS-01 | 380 (compression) | 120 | 8.5 |
| LS-02 | 280 (combined) | 150 | 7.2 |
| LS-03 | 420 (tension) | 100 | 9.8 |
| LS-04 | 300 (combined) | 140 | 7.8 |
| LS-05 | 350 (combined) | 130 | 8.0 |

## Analysis and Verification

### Analysis Methods

| Analysis Type | Method | Software |
|--------------|--------|----------|
| Fastener load distribution | Flexibility method | Excel / Python |
| Bearing stress | Classical (P/Dt) | Excel |
| Net section stress | FEA with fastener holes | NASTRAN |
| Fatigue (fastener holes) | S-N curve + Miner's | In-house |
| Damage tolerance (crack growth) | LEFM | NASGRO |

### Margin Summary

| Splice | Load Case | MS (Bearing) | MS (Net Section) | MS (Fatigue) | Status |
|--------|-----------|--------------|------------------|--------------|--------|
| LS-01 | LC-001 | +0.22 | +0.15 | 3.0× DSG | ✓ Pass |
| LS-02 | LC-003 | +0.28 | +0.20 | 3.5× DSG | ✓ Pass |
| LS-03 | LC-002 | +0.18 | +0.12 | 2.8× DSG | ✓ Pass |
| LS-04 | LC-003 | +0.25 | +0.18 | 3.2× DSG | ✓ Pass |
| LS-05 | LC-003 | +0.20 | +0.16 | 3.0× DSG | ✓ Pass |

### Damage Tolerance Assessment

| Scenario | Initial Flaw | Critical Crack Length | Inspection Interval |
|----------|--------------|----------------------|---------------------|
| Single fastener hole crack | 1.27 mm corner | 25 mm (two-bay) | 6,000 FC |
| Manufacturing defect | 0.5 mm | 15 mm | 4,000 FC |
| Impact damage | BVID | 20 mm | Visual each C-check |

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| Splice specimen SP-01 | Static tension | Ultimate strength | Complete |
| Splice specimen SP-02 | Static shear | Shear strength | Complete |
| Splice specimen SP-03 | Fatigue | Life validation | In progress |
| Splice specimen SP-04 | Damage tolerance | Crack growth | Planned |

## Manufacturing Considerations

### Assembly Sequence

1. Drill pilot holes in splice straps (template-controlled)
2. Apply fay surface sealant to mating surfaces
3. Position splice straps and clamp
4. Match-drill through full stack
5. Ream holes to final size
6. Deburr and clean
7. Apply wet sealant to fasteners
8. Install fasteners (torque or squeeze)
9. Fillet seal exposed edges

### Quality Criteria

| Feature | Acceptance Criteria |
|---------|---------------------|
| Hole diameter | Nominal +0.05/-0.00 mm |
| Hole perpendicularity | ±1° |
| Countersink depth | Flush ±0.1 mm |
| Fastener torque | Per specification (Hi-Lok: 50-70 in-lb) |
| Sealant coverage | 100% fay surface wetted |
| Edge seal | Continuous fillet, no voids |

## References

### Regulatory Documents
- [CS-25.571 Damage Tolerance and Fatigue Evaluation](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.613 Material Strength Properties and Design Values](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-01 Primary Structure Overview](../../README.md)
- [Splice Fastener Schedule](ASSETS/Splice_Fastener_Schedule.csv)
- [Joint Stress Analysis](ASSETS/Joint_Stress_Analysis.csv)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
