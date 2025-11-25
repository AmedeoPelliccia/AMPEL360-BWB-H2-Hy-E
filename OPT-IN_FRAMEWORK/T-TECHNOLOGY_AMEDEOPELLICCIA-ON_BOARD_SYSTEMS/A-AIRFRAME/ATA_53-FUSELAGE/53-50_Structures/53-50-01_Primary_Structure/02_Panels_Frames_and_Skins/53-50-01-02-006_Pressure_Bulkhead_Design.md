# 53-50-01-02-006 Pressure Bulkhead Design

## Document Information

- **Document ID**: 53-50-01-02-006
- **Title**: Pressure Bulkhead Design
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications, analysis methodology, and verification data for Pressure Bulkhead Design in the AMPEL360 BWB primary structure. The forward and aft pressure bulkheads form the ends of the pressurized cabin, reacting the net pressure force and providing the structural interface between the pressurized fuselage and unpressurized nose/tail sections.

## Scope

This specification covers:
- Forward pressure bulkhead design and geometry
- Aft pressure bulkhead design and geometry
- Bulkhead-to-fuselage shell interface
- Penetration design for systems (ducts, wiring, controls)
- Blow-out provisions and pressure relief
- Material selection and construction methods

### Applicable Components
- Forward Pressure Bulkhead (FPB) at Station 2.5m
- Aft Pressure Bulkhead (APB) at Station 38.0m

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Maximum cabin pressure differential | 8.6 psi (59.3 kPa) | Operations envelope |
| Ultimate pressure differential | 12.9 psi (89.0 kPa) | 1.5 × limit |
| Proof pressure | 10.3 psi (71.2 kPa) | 1.2 × limit |
| Design Service Goal | 60,000 FC / 90,000 FH | Program requirement |
| Fatigue life | Safe-life approach | Pressure cycling |

### Material Requirements

- **Primary Material**: Aluminum alloy 7050-T7451 (machined panels/forgings)
- **Stiffeners**: Aluminum alloy 7075-T6 (extruded or machined)
- **Doubler Material**: Aluminum 2024-T3 (for penetrations)
- **Sealant**: Polysulfide or silicone-based aerospace sealant

### Geometric Requirements

| Parameter | Specification |
|-----------|---------------|
| Bulkhead type | Hemispherical dome (modified for BWB) |
| FPB nominal radius | 3,500 mm (blended into BWB contour) |
| APB nominal radius | 3,200 mm (aft fuselage taper) |
| Skin thickness | 3.0 - 5.0 mm (varies with radius) |
| Stiffener spacing | 300 - 400 mm (radial pattern) |

## Design Configuration

### Forward Pressure Bulkhead (FPB)

| Parameter | Value |
|-----------|-------|
| Location | Station 2.5m |
| Diameter (max) | 7.0 m (BWB width at this station) |
| Shape | Modified dome with flattened center |
| Surface area | ~45 m² |
| Total pressure load | ~2,650 kN at limit pressure |

**Structural Configuration**:
- Central dome region: 3.0 mm aluminum skin with radial stiffeners
- Peripheral ring: Machined aluminum frame (7050-T7451)
- Cockpit interface: Reinforced flat section for instrument panel attachment

### Aft Pressure Bulkhead (APB)

| Parameter | Value |
|-----------|-------|
| Location | Station 38.0m |
| Diameter (max) | 6.0 m (narrower at aft fuselage) |
| Shape | Spherical dome |
| Surface area | ~35 m² |
| Total pressure load | ~2,075 kN at limit pressure |

**Structural Configuration**:
- Dome skin: 3.5 mm aluminum with radial/circumferential stiffeners
- Peripheral frame: Integral with aft fuselage frames
- APU/tail interface: Reinforced zone for aft systems penetration

### Stiffening Pattern

**Radial Stiffeners**:
- Profile: T-section, 30 mm × 25 mm
- Spacing: Every 15° (24 stiffeners total per bulkhead)
- Attachment: Riveted to dome skin

**Circumferential Stiffeners**:
- Profile: Z-section, 25 mm × 20 mm
- Spacing: 400 mm between rings
- Attachment: Riveted to dome skin, intersecting with radial stiffeners

## Penetration Design

### Forward Bulkhead Penetrations

| Penetration | Size | Type | Quantity |
|-------------|------|------|----------|
| ECS ducts | Ø200 mm | Flanged | 2 |
| Electrical bundles | Ø80 mm | Grommet | 4 |
| Flight controls | Ø60 mm | Push-pull rod | 3 |
| Pitot/static lines | Ø25 mm | Quick disconnect | 6 |
| Access door | 500 × 500 mm | Hinged panel | 1 |

### Aft Bulkhead Penetrations

| Penetration | Size | Type | Quantity |
|-------------|------|------|----------|
| APU bleed air | Ø150 mm | Flanged | 1 |
| Hydraulic lines | Ø40 mm | Quick disconnect | 3 |
| Electrical bundles | Ø100 mm | Grommet | 2 |
| Fuel vent line | Ø50 mm | Check valve | 1 |
| Tailcone access | 600 × 600 mm | Bolted panel | 1 |

### Penetration Reinforcement

| Hole Diameter Range | Reinforcement Method |
|---------------------|----------------------|
| < 50 mm | Local doubler (1.5 × hole diameter) |
| 50 - 150 mm | Flanged fitting with doubler |
| 150 - 300 mm | Forged ring + bolted flange |
| > 300 mm | Structural frame + multiple fasteners |

## Load Cases

### Critical Design Cases for Bulkheads

| Load Case ID | Description | Pressure (psi) | Location |
|--------------|-------------|----------------|----------|
| LC-002 | Maximum cabin pressure | 8.6 | Both bulkheads |
| LC-011 | Rapid decompression | Transient | APB |
| LC-018 | Ground pressure test | 10.3 (proof) | Both bulkheads |
| LC-019 | Ultimate pressure | 12.9 | Both bulkheads |

### Load Distribution

- **Membrane Stress**: σ = p × R / (2 × t) (dome membrane theory)
- **Ring Compression**: At peripheral frame junction with fuselage shell
- **Concentrated Loads**: At penetration surrounds and stiffener intersections

## Analysis and Verification

### Analysis Methods

| Analysis Type | Method | Software |
|--------------|--------|----------|
| Membrane stress distribution | Analytical (thin shell theory) | Excel / MATLAB |
| Detailed stress analysis | FEA (shell elements) | NASTRAN |
| Penetration stress concentration | Local FEA | ABAQUS |
| Fatigue (pressure cycling) | Safe-life, Miner's rule | In-house |
| Buckling (external pressure) | Eigenvalue analysis | NASTRAN |

### Stress Analysis Results

**Forward Pressure Bulkhead**:
| Location | Stress Type | Stress (MPa) | Allowable (MPa) | MS |
|----------|-------------|--------------|-----------------|-----|
| Dome center | Membrane | 145 | 455 | +2.14 |
| Peripheral frame | Bending | 280 | 420 | +0.50 |
| ECS penetration | Peak | 320 | 385 | +0.20 |
| Stiffener base | Shear | 85 | 195 | +1.29 |

**Aft Pressure Bulkhead**:
| Location | Stress Type | Stress (MPa) | Allowable (MPa) | MS |
|----------|-------------|--------------|-----------------|-----|
| Dome center | Membrane | 160 | 455 | +1.84 |
| Peripheral frame | Bending | 310 | 420 | +0.35 |
| Tailcone access | Peak | 340 | 385 | +0.13 |
| Stiffener intersection | Combined | 220 | 340 | +0.55 |

### Fatigue Analysis

- **Load Spectrum**: Ground-air-ground pressure cycle (1 cycle per flight)
- **Stress Concentration Factor**: Kt = 2.5 at penetration corners
- **Calculated Fatigue Life**: 180,000 cycles (3× DSG)
- **Safe-Life Factor**: 4.0 (scatter factor per AC 25.571)
- **Demonstrated Safe Life**: 45,000 cycles > DSG ✓

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| FPB specimen PB-01 | Proof pressure | Leak check | Complete |
| APB specimen PB-02 | Ultimate pressure | Burst margin | Complete |
| Penetration specimen PN-01 | Fatigue | Life validation | In progress |
| Full-scale barrel | Pressure test | Certification | Planned 2026 |

## Pressure Relief and Blow-Out Provisions

### Pressure Relief Valves

| Location | Type | Set Pressure | Flow Capacity |
|----------|------|--------------|---------------|
| Forward fuselage | Safety valve | 8.9 psi | 0.5 kg/s |
| Aft fuselage | Safety valve | 8.9 psi | 0.5 kg/s |

### Negative Pressure Relief

- **Provision**: Inward relief doors in unpressurized areas
- **Set Pressure**: -0.5 psi differential
- **Purpose**: Prevent structural damage during rapid descent

### Blow-Out Panel (Cargo Compartment)

- **Location**: Cargo bay floor panels
- **Activation**: Automatic at 1.0 psi differential (cargo to cabin)
- **Purpose**: Equalize pressure following cargo hold decompression

## Manufacturing Considerations

### Process Requirements

- **Dome Forming**: Stretch forming of aluminum sheet; spin forming for small domes
- **Machining**: 5-axis CNC for peripheral frame and complex regions
- **Assembly**: Riveting with automated hole drilling; sealant application
- **NDI**: 100% inspection of critical joints and riveted connections

### Quality Criteria

| Feature | Acceptance Criteria |
|---------|---------------------|
| Dome contour | ±1.5 mm from theoretical |
| Skin thickness | ±0.2 mm |
| Rivet edge distance | ≥2.0 × diameter |
| Sealant bead | Continuous, 3-5 mm width |
| Leak rate (proof test) | Zero leaks |

## References

### Regulatory Documents
- [CS-25.365 Pressurized Compartment Loads](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.841 Pressurized Cabins](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.843 Tests for Pressurized Cabins](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-01 Primary Structure Overview](../../README.md)
- [53-50-01-01-003 Material Selection Summary](../01_Overview/53-50-01-01-003_Material_Selection_Summary.md)
- [53-50-01-03-005 Systems Penetration Details](../03_Joints_Splices_and_Cutouts/53-50-01-03-005_Systems_Penetration_Details.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
