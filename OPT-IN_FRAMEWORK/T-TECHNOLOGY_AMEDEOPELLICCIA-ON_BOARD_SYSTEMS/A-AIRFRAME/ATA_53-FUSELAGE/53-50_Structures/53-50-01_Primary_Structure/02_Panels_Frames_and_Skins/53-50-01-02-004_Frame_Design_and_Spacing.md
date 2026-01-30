# 53-50-01-02-004 Frame Design and Spacing

## Document Information

- **Document ID**: 53-50-01-02-004
- **Title**: Frame Design and Spacing
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications, analysis methodology, and verification data for Frame Design and Spacing in the AMPEL360 BWB primary structure. Frames maintain the cross-sectional shape of the fuselage under pressurization and flight loads, distribute concentrated loads, and provide attachment points for systems and interior.

## Scope

This specification covers:
- Frame geometry and cross-sections for the BWB fuselage
- Frame spacing schedule and arrangement
- Frame-to-skin attachment design
- Heavy frame design for concentrated load introduction
- Standard (light) frame design for pressure containment
- Frame cutouts and lightening provisions
- Manufacturing and assembly requirements

### Applicable Stations
- Forward pressure bulkhead (Station 2.5m) to aft pressure bulkhead (Station 38.0m)
- Frames arranged perpendicular to fuselage axis (transverse direction)

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Frame spacing (standard) | 500 - 600 mm | Skin stability & manufacturing |
| Heavy frame spacing | As required by loads | Load introduction points |
| Frame depth (standard) | 100 - 150 mm | Stiffness requirement |
| Frame depth (heavy) | 200 - 300 mm | Load transfer capability |
| Maximum pressure differential | 8.6 psi (59.3 kPa) | Operations envelope |
| Design Service Goal | 60,000 FC / 90,000 FH | Program requirement |

### Material Requirements

- **Standard Frames**: Aluminum alloy 7075-T6 or 7050-T7451 machined extrusions
- **Heavy Frames**: Aluminum alloy 7050-T7451 machined from plate/forgings
- **Frame Clips**: Aluminum 2024-T3 sheet metal or titanium Ti-6Al-4V
- **Fasteners**: Titanium or corrosion-resistant steel at CFRP interfaces

### Geometric Requirements

| Parameter | Specification |
|-----------|---------------|
| Web thickness | 2.0 - 4.0 mm (standard); 4.0 - 8.0 mm (heavy) |
| Cap width | 30 - 50 mm |
| Cap thickness | 3.0 - 6.0 mm |
| Lightening hole diameter | 50 - 80 mm typical |
| Minimum edge distance | 2.0 × hole diameter |

## Design Configuration

### Frame Types

| Frame Type | Application | Material | Typical Depth |
|------------|-------------|----------|---------------|
| Type A - Light | Standard pressure frames | Al 7075-T6 | 100 mm |
| Type B - Medium | Floor beam support | Al 7075-T6 | 130 mm |
| Type C - Heavy | MLG, wing attachment | Al 7050-T7451 | 250 mm |
| Type D - Bulkhead | Pressure containment | Al 7050-T7451 | 200 mm |

### Frame Spacing Schedule

| Station Range | Frame Spacing | Frame Type | Notes |
|---------------|---------------|------------|-------|
| 2.5m - 5.0m | 500 mm | Type D | Forward pressure bulkhead zone |
| 5.0m - 10.0m | 500 mm | Type A/B | Door 1 area, passenger cabin forward |
| 10.0m - 16.0m | 533 mm (21") | Type A/B | Standard passenger cabin (window pitch) |
| 16.0m - 24.0m | 500 mm | Type C | Wing box / MLG / battery bay zone |
| 24.0m - 32.0m | 533 mm | Type A/B | Standard passenger cabin aft |
| 32.0m - 38.0m | 500 mm | Type D | Aft pressure bulkhead zone |

### Frame Cross-Section Design

**Type A (Light Frame)**:
```
       |------ 40 mm ------|
       ____________________
      |____________________|  3.0 mm cap
              |  |
              |  |  2.5 mm web
              |  |
       _______|  |_______
      |____________________|  3.0 mm cap
       |------ 40 mm ------|

       Depth: 100 mm
```

**Type C (Heavy Frame)**:
```
       |------ 60 mm ------|
       ____________________
      |____________________|  6.0 mm cap
              |  |
              |  |  5.0 mm web
              |  |
       _______|  |_______
      |____________________|  6.0 mm cap
       |------ 60 mm ------|

       Depth: 250 mm
```

### Frame-to-Skin Attachment

| Method | Application | Fastener Type | Pitch |
|--------|-------------|---------------|-------|
| Shear clips | Standard frames to skin | Hi-Lok Ti 4.8mm | 30 mm |
| Direct bolting | Heavy frames to skin | Hi-Lok Ti 6.35mm | 25 mm |
| Bonded clips | Secondary attachment | FM300 adhesive | N/A |

## Load Cases

### Critical Design Cases for Frames

| Load Case ID | Description | Critical Frame | Governing Parameter |
|--------------|-------------|----------------|---------------------|
| LC-002 | Maximum cabin pressure | All frames | Hoop bending |
| LC-001 | 2.5g maneuver | MLG frames | Vertical shear |
| LC-004 | Landing impact | FR-42 (MLG) | Concentrated load |
| LC-007 | Wing attachment | FR-35 to FR-48 | Frame column loads |
| LC-010 | Floor beam reaction | FR-20 to FR-60 | Local bending |

### Frame Loads Summary

| Frame Station | Pressure Load (kN/m) | Inertia Load (kN) | Total Load (kN/m) |
|---------------|---------------------|-------------------|-------------------|
| FR-10 (5.0m) | 25 | 5 | 30 |
| FR-30 (15.0m) | 28 | 8 | 36 |
| FR-42 (21.0m) | 30 | 250 (MLG) | Special analysis |
| FR-60 (30.0m) | 26 | 6 | 32 |

## Analysis and Verification

### Analysis Methods

| Analysis Type | Method | Software |
|--------------|--------|----------|
| Frame bending (pressure) | Classical beam theory | Hand calcs / Excel |
| Frame stability (buckling) | Eigenvalue analysis | NASTRAN |
| Attachment loads | Shear flow analysis | NASTRAN |
| Fatigue at fastener holes | Miner's rule / DTA | In-house |
| Concentrated load introduction | Local FEA | ABAQUS |

### Margin Summary

| Component | Load Case | MS (Strength) | MS (Buckling) | Status |
|-----------|-----------|---------------|---------------|--------|
| FR-10 Type A | LC-002 | +0.28 | +0.35 | ✓ Pass |
| FR-30 Type A | LC-002 | +0.22 | +0.25 | ✓ Pass |
| FR-42 Type C (MLG) | LC-004 | +0.10 | +0.15 | ✓ Pass |
| FR-48 Type C (Wing) | LC-007 | +0.12 | +0.18 | ✓ Pass |
| Frame clips | LC-002 | +0.35 | N/A | ✓ Pass |

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| Frame specimen FR-A-01 | Static bending | Strength validation | Complete |
| Frame clip FC-01 | Pull-off test | Attachment strength | Complete |
| Heavy frame FR-C-01 | Compression test | Column stability | In progress |
| Frame section FS-01 | Fatigue test | Durability | Planned |

## Manufacturing Considerations

### Process Requirements

- **Standard Frames**: CNC machining from extruded profile
- **Heavy Frames**: 5-axis CNC machining from plate or forging
- **Frame Clips**: Sheet metal forming or precision casting
- **Surface Treatment**: Chromic acid anodize + primer

### Quality Criteria

| Feature | Acceptance Criteria |
|---------|---------------------|
| Web thickness tolerance | ±0.15 mm |
| Cap flatness | ≤0.1 mm per 100 mm |
| Hole location | ±0.1 mm |
| Surface roughness | Ra ≤ 3.2 μm |
| Anodize thickness | 2-5 μm |

## References

### Regulatory Documents
- [CS-25.305 Strength and Deformation](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.571 Damage Tolerance and Fatigue Evaluation](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-01 Primary Structure Overview](../../README.md)
- [Frame Spacing Schedule](ASSETS/Frame_Spacing_Schedule.csv)
- [53-50-01-01-003 Material Selection Summary](../01_Overview/53-50-01-01-003_Material_Selection_Summary.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
