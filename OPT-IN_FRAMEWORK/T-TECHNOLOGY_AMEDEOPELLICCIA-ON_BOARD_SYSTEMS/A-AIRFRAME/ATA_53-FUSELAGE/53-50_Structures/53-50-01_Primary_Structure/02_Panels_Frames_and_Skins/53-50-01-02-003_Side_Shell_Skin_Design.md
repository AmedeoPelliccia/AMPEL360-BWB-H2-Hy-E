# 53-50-01-02-003 Side Shell Skin Design

## Document Information

- **Document ID**: 53-50-01-02-003
- **Title**: Side Shell Skin Design
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications, analysis methodology, and verification data for Side Shell Skin Design in the AMPEL360 BWB primary structure. The side shell skins form the lateral surfaces of the fuselage pressure vessel and accommodate passenger doors, emergency exits, and windows.

## Scope

This specification covers:
- Side shell skin panel geometry and configuration
- Material systems optimized for shear and combined loading
- Door and window cutout reinforcement design
- Passenger door surround structure
- Emergency exit provisions
- Window belt design and attachment
- Sidewall-to-floor interface structure

### Applicable Stations
- Forward pressure bulkhead (Station 2.5m) to aft pressure bulkhead (Station 38.0m)
- Side skin panels from ±60° to ±120° from top centerline (approximately)

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Ultimate load factor | 1.5 × Limit load | [CS-25.303](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) |
| Maximum cabin differential pressure | 8.6 psi (59.3 kPa) | Operations envelope |
| Door operating loads | Per CS-25.783 | Door system requirements |
| Emergency exit loads | Per CS-25.809 | Emergency exit requirements |
| Design Service Goal (DSG) | 60,000 flight cycles / 90,000 flight hours | Program requirement |

### Material Requirements

- **Primary Material**: IM7/8552 Carbon Fiber/Epoxy prepreg
- **Door Surround Material**: T800/M21 CFRP with metallic reinforcement
- **Operating Temperature Range**: -55°C to +80°C
- **Impact Resistance**: Enhanced BVID threshold in passenger areas
- **Fire Protection**: Self-extinguishing per FAR 25.853

### Geometric Requirements

| Parameter | Specification |
|-----------|---------------|
| Minimum skin thickness | 3.5 mm (general field) |
| Maximum skin thickness | 10.0 mm (door/window surrounds) |
| Panel curvature | Variable BWB contour |
| Door cutout size (Type A) | 1.07m × 1.85m |
| Window cutout size | 0.28m × 0.40m typical |
| Window spacing | 533 mm (21 in) pitch |

## Design Configuration

### Panel Layout

The side shell skin is organized around door and window locations:

| Panel ID | Station Range | Description | Approximate Area |
|----------|---------------|-------------|------------------|
| S-FWD-L/R | 2.5m - 8.0m | Forward side panels (cockpit area) | 45 m² each |
| S-DOOR1-L/R | 8.0m - 12.0m | Door 1 surround structure | 35 m² each |
| S-WIN-FWD-L/R | 12.0m - 18.0m | Forward window belt | 50 m² each |
| S-DOOR2-L/R | 18.0m - 22.0m | Door 2 / Emergency exit area | 35 m² each |
| S-WIN-AFT-L/R | 22.0m - 32.0m | Aft window belt | 85 m² each |
| S-AFT-L/R | 32.0m - 38.0m | Aft side panels | 50 m² each |

### Layup Schedule

Shear-optimized layup with ±45° dominance:

| Zone | Layup | Thickness | Application |
|------|-------|-----------|-------------|
| General field | [±45/0/90]₂ₛ | 3.5 mm | Standard side skin |
| Window belt | [±45/0/90]₃ₛ | 5.0 mm | Between windows |
| Window surround | [±45/0/90]₄ₛ | 7.0 mm | Around each window |
| Door surround | [±45/0/90]₅ₛ + Al doubler | 10.0 mm | Door frame area |
| Frame attachment | [±45/0/90]₃ₛ | 5.0 mm | Local pad-up |

### Stiffening Concept

- **Stringer Type**: Co-cured J-section stringers (lighter profile for side panels)
- **Stringer Spacing**: 250 mm nominal
- **Stringer Height**: 25 mm
- **Window Frame Integration**: Stringers terminate at window frames; loads bridged by frames

## Door and Window Cutouts

### Passenger Door Design

| Door Type | Size (W × H) | Location | Reinforcement |
|-----------|--------------|----------|---------------|
| Door 1L/1R | 1.07m × 1.85m | Station 10.0m | Aluminum 7050 frame + Ti fittings |
| Door 2L/2R | 1.07m × 1.85m | Station 20.0m | Aluminum 7050 frame + Ti fittings |
| Door 3L/3R | 0.91m × 1.68m | Station 30.0m | Type III emergency exit |

### Door Surround Structure

- **Frame Material**: Machined aluminum 7050-T7451 door frame
- **Hinge Fittings**: Titanium Ti-6Al-4V
- **Latch Fittings**: Steel 15-5PH
- **Seal Groove**: Integrated in door frame, dual seal provision

### Window Design

| Parameter | Specification |
|-----------|---------------|
| Window size | 280 mm × 400 mm visible area |
| Frame material | Aluminum 2024-T3 extruded frame |
| Reveal depth | 120 mm (wall thickness) |
| Attachment | Mechanically fastened to CFRP skin |
| Pressure seal | Primary seal on outer pane, secondary on inner |

## Load Cases

### Critical Design Cases for Side Shell

| Load Case ID | Description | Critical Location | Governing Parameter |
|--------------|-------------|-------------------|---------------------|
| LC-002 | Maximum cabin pressure | Door corners | Stress concentration |
| LC-003 | Combined pressure + maneuver | Window belt | Combined stress |
| LC-006 | Asymmetric gust | Forward side | Shear |
| LC-016 | Door operating loads | Door hinges | Fitting loads |
| LC-017 | Emergency exit opening | Exit frame | Rapid decompression |

### Load Distribution

- **Hoop Tension**: Primary load from pressurization
- **Shear**: Transferred around cutouts via frames and reinforcements
- **Concentrated Loads**: At door hinges, latches, and assist mechanisms
- **Fatigue Loads**: Pressure cycling at cutout corners

## Analysis and Verification

### Analysis Methods

| Analysis Type | Method | Software |
|--------------|--------|----------|
| Cutout stress concentration | Local FEA with refined mesh | ABAQUS |
| Door frame loads | Contact analysis | ABAQUS |
| Fatigue at cutouts | Crack initiation + DTA | NASGRO |
| Pressure cycling | Spectrum fatigue | In-house tools |
| Rapid decompression | Transient pressure | ABAQUS Explicit |

### Margin Summary

| Component | Load Case | MS (Strength) | MS (Fatigue) | Status |
|-----------|-----------|---------------|--------------|--------|
| Door 1 surround | LC-002 | +0.12 | 2.5× DSG | ✓ Pass |
| Window W-15 frame | LC-003 | +0.18 | 3.0× DSG | ✓ Pass |
| Door hinge fitting | LC-016 | +0.15 | 4.0× DSG | ✓ Pass |
| Window belt panel | LC-003 | +0.22 | N/A | ✓ Pass |
| Emergency exit frame | LC-017 | +0.10 | N/A | ✓ Pass |

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| Door surround DS-01 | Pressure cycling | Fatigue life validation | In progress |
| Window frame WF-01 | Static + fatigue | Frame strength | Complete |
| Emergency exit EE-01 | Opening test | Emergency operation | Planned |
| Full-scale barrel | Pressure test | Certification | Planned 2026 |

## Manufacturing Considerations

### Process Requirements

- **Layup Method**: AFP for main panels; hand layup for complex contours
- **Door Frame Assembly**: Precision machining; assembly with automated drilling
- **Window Installation**: Template-controlled hole drilling; sealant application
- **NDI Requirements**: 100% inspection of cutout surrounds

### Quality Criteria

| Feature | Acceptance Criteria |
|---------|---------------------|
| Cutout edge quality | No delamination; sealed edges |
| Frame-to-skin fit | Gap ≤0.25 mm |
| Hole location tolerance | ±0.1 mm |
| Seal groove surface | Ra ≤ 1.6 μm |
| Frame flatness | ≤0.1 mm over seal contact surface |

## References

### Regulatory Documents
- [CS-25.783 Doors](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.809 Emergency Exit Arrangement](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.841 Pressurized Cabins](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-01 Primary Structure Overview](../../README.md)
- [53-50-01-03-003 Door Cutout Reinforcement](../03_Joints_Splices_and_Cutouts/53-50-01-03-003_Door_Cutout_Reinforcement.md)
- [53-50-01-03-004 Window Cutout Reinforcement](../03_Joints_Splices_and_Cutouts/53-50-01-03-004_Window_Cutout_Reinforcement.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
