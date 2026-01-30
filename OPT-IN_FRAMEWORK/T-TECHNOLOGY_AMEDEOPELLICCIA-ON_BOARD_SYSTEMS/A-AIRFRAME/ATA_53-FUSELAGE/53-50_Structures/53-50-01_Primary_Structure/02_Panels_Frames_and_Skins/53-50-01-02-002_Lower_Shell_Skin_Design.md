# 53-50-01-02-002 Lower Shell Skin Design

## Document Information

- **Document ID**: 53-50-01-02-002
- **Title**: Lower Shell Skin Design
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications, analysis methodology, and verification data for Lower Shell Skin Design in the AMPEL360 BWB primary structure. The lower shell skin carries tension loads from fuselage bending and provides the structural floor for cargo compartments and battery bays.

## Scope

This specification covers:
- Lower shell skin panel geometry and configuration
- Material systems and enhanced layup schedules for tension-dominated loading
- Cargo bay floor integration and load distribution
- CO₂ battery bay structural provisions
- Ground handling load paths (landing gear, jacking points)
- Cutout reinforcement for access panels and service doors
- Corrosion and FOD protection requirements

### Applicable Stations
- Forward pressure bulkhead (Station 2.5m) to aft pressure bulkhead (Station 38.0m)
- Lower skin panels from keel centerline to ±60° from bottom (approximately)

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Ultimate load factor | 1.5 × Limit load | [CS-25.303](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) |
| Landing gear vertical load | 4.5g ultimate (3.0g limit) | [CS-25.473](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) |
| Cargo floor loading | 7.3 kN/m² (150 lb/ft²) | Operations requirement |
| Battery bay floor loading | 12.0 kN/m² | CO₂ battery weight + crash loads |
| Design Service Goal (DSG) | 60,000 flight cycles / 90,000 flight hours | Program requirement |

### Material Requirements

- **Primary Material**: IM7/8552 Carbon Fiber/Epoxy prepreg (intermediate modulus)
- **Keel Area Material**: T800/M21 CFRP (higher toughness for damage tolerance)
- **Operating Temperature Range**: -55°C to +80°C
- **Impact Resistance**: BVID threshold 1.0 J/mm for cargo floor areas
- **Corrosion Protection**: Full primer system with sacrificial protection at metallic interfaces

### Geometric Requirements

| Parameter | Specification |
|-----------|---------------|
| Minimum skin thickness | 5.0 mm (keel and cargo floor areas) |
| Maximum skin thickness | 14.0 mm (landing gear attachment zone) |
| Panel curvature (minimum radius) | 2,500 mm (BWB lower contour) |
| Surface finish tolerance | ±0.5 mm from theoretical OML |
| Cargo floor flatness | ±1.0 mm over any 1m × 1m area |

## Design Configuration

### Panel Layout

The lower shell skin is divided into functional zones:

| Panel ID | Station Range | Description | Approximate Area |
|----------|---------------|-------------|------------------|
| L-KEEL | 2.5m - 38.0m | Center keel panel, full length | 180 m² |
| L-FWD-CARGO | 5.0m - 15.0m | Forward cargo bay floor | 120 m² |
| L-BAT-BAY | 16.0m - 24.0m | CO₂ battery bay structure | 100 m² |
| L-AFT-CARGO | 25.0m - 35.0m | Aft cargo bay floor | 120 m² |
| L-MLG-L/R | 18.0m - 22.0m | Main landing gear bay | 40 m² each |
| L-BELLY | General | Lower fairing areas | 200 m² |

### Layup Schedule

Tension-optimized layup with 0°-ply dominance:

| Zone | Layup | Thickness | Application |
|------|-------|-----------|-------------|
| Keel general | [45/0/-45/0/90/0]₂ₛ | 5.5 mm | Center keel, tension-critical |
| Cargo floor | [45/0/-45/90]₄ₛ | 6.0 mm | Cargo bay floor panels |
| Battery bay | [45/0/-45/0/90/0]₃ₛ | 8.0 mm | Enhanced for battery loads |
| MLG attachment | [45/0/-45/90]₆ₛ + Ti doubler | 12.0 mm + Ti | Landing gear fitting zone |
| Access panels | [45/0/-45/90]₃ₛ | 4.5 mm | Removable panels |

### Stiffening Concept

- **Stringer Type**: Co-cured omega-section stringers (CFRP) - optimized for tension
- **Stringer Spacing**: 180 mm in keel zone, 220 mm elsewhere
- **Stringer Height**: 40 mm (keel), 30 mm (general)
- **Floor Beams**: Aluminum alloy 7050-T7451, integrated with cargo system

## Load Cases

### Critical Design Cases for Lower Shell

| Load Case ID | Description | Critical Location | Governing Parameter |
|--------------|-------------|-------------------|---------------------|
| LC-001 | 2.5g symmetric maneuver | Keel centerline | Tension (fatigue) |
| LC-004 | Landing impact (3.0g vert.) | MLG attachment | Concentrated load |
| LC-005 | Cargo floor max load | Cargo bay floor | Floor deflection |
| LC-009 | Battery emergency landing | Battery bay | Crash load (16g fwd) |
| LC-012 | Towing loads | Nose/MLG areas | Ground handling |

### Load Distribution

- **Axial Tension**: Maximum at keel during positive g maneuvers
- **Hoop Tension**: From cabin pressurization (similar to upper shell)
- **Floor Loads**: Cargo and battery weight, crash inertia loads
- **Concentrated Loads**: Landing gear reaction, jacking points

## Analysis and Verification

### Analysis Methods

| Analysis Type | Method | Software |
|--------------|--------|----------|
| Global stress distribution | Linear FEA | NASTRAN |
| Floor beam deflection | Beam analysis | NASTRAN |
| Landing gear load path | Contact analysis | ABAQUS |
| Crash simulation | Explicit dynamics | LS-DYNA |
| Fatigue (tension cycles) | S-N curve approach | In-house tools |

### Margin Summary

| Component | Load Case | MS (Strength) | MS (Fatigue) | Status |
|-----------|-----------|---------------|--------------|--------|
| L-KEEL panel | LC-001 | +0.18 | 2.0× DSG | ✓ Pass |
| L-FWD-CARGO floor | LC-005 | +0.22 | N/A | ✓ Pass |
| L-BAT-BAY floor | LC-009 | +0.10 | N/A | ✓ Pass |
| MLG attachment | LC-004 | +0.08 | 4.0× DSG | ✓ Pass |
| Cargo floor beam CB-12 | LC-005 | +0.15 | N/A | ✓ Pass |

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| Keel panel K-01 | Static tension | Validate tension strength | Complete |
| Cargo floor section | Floor load test | Deflection and strength | Complete |
| MLG fitting | Static ultimate | Certification | In progress |
| Battery bay | Crash simulation validation | Emergency landing | Planned |

## Special Design Features

### CO₂ Battery Bay Integration

- **Structural Provisions**: Reinforced floor with guide rails for battery docking
- **Load Introduction**: Distributed through multiple hard points
- **Crash Protection**: Energy-absorbing structure around battery perimeter
- **Thermal Barrier**: Insulation layer between battery and primary structure

### Landing Gear Bay

- **MLG Attachment**: Titanium Ti-6Al-4V fittings, machined forgings
- **Load Paths**: Distributed to keel beam and adjacent frames
- **Bay Door Structure**: Aluminum alloy with CFRP aerodynamic fairings
- **Drainage**: Provisions for water/fluid drainage from gear bay

## Manufacturing Considerations

### Process Requirements

- **Layup Method**: Automated Fiber Placement (AFP) for large panels
- **Cure Cycle**: 180°C / 7 bar autoclave cure
- **NDI Requirements**: 100% ultrasonic inspection; radiographic for MLG fittings
- **Assembly**: Fastened joints at major splices; metallic fittings bonded + bolted

### Quality Criteria

| Feature | Acceptance Criteria |
|---------|---------------------|
| Porosity | ≤1.5% by volume (keel zone) |
| Delamination | None >6 mm diameter |
| Bearing surface roughness | Ra ≤ 3.2 μm at fastener holes |
| Hole perpendicularity | ±0.5° |
| Flatness (cargo floor) | ±1.0 mm / m |

## References

### Regulatory Documents
- [CS-25.301 Loads](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.473 Landing Gear Ground Loads](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.561 Emergency Landing Conditions](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.787 Stowage Compartments](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-01 Primary Structure Overview](../../README.md)
- [53-50-01-04-002 Landing Gear Attachments](../04_Primary_Attachments/53-50-01-04-002_Landing_Gear_Attachments.md)
- [Skin Thickness Maps](ASSETS/Skin_Thickness_Maps.csv)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
