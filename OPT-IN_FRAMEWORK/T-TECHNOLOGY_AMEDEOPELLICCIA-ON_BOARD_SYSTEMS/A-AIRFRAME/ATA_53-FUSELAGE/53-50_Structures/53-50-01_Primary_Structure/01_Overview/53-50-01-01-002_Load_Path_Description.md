# 53-50-01-01-002 Load Path Description

## Document Information

- **Document ID**: 53-50-01-01-002
- **Title**: Load Path Description
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Analysis
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document describes the primary load paths through the AMPEL360 BWB fuselage structure, identifying how flight loads, ground loads, and internal loads are transmitted through structural members to achieve equilibrium.

## Scope

Load paths described include:
- Wing bending and torsion transfer
- Fuselage bending and torsion
- Pressure loads
- Landing gear loads
- Engine/pylon loads
- Emergency and crash loads

## Load Path Fundamentals

### Definition

A **load path** is the route through which forces are transmitted from their point of application to their reaction points. Effective load path design ensures:
- **Continuity**: No discontinuities that create stress concentrations
- **Efficiency**: Direct paths minimize structural weight
- **Redundancy**: Multiple paths provide fail-safe capability
- **Clarity**: Unambiguous load transfer for analysis and verification

## BWB Primary Load Paths

### 1. Wing Bending Loads

**Load Source**: Aerodynamic lift distribution across wing span

**Load Path**:
1. **Distributed Lift** → Upper and lower wing skins (tension/compression)
2. **Skin Loads** → Longitudinal stringers and spars
3. **Spar Caps** → Main structural box through fuselage center section
4. **Fuselage Center Section** → Distributed across wide BWB body
5. **Root Attachment** → Bulkheads and frame structures

**Key Structural Elements**:
- Upper skin panels (compression under positive lift)
- Lower skin panels (tension under positive lift)
- Longitudinal stringers (continuous load distribution)
- Main spar webs (shear transfer)
- Spar caps (concentrated bending moment)

**BWB Advantage**: 
- Wide load distribution reduces peak stresses
- Fuselage structure participates in wing bending, reducing wing root stress concentration
- Smooth load transition across blended wing-body junction

### 2. Wing Torsion Loads

**Load Source**: Aerodynamic forces, aileron deflection, control surface actuation

**Load Path**:
1. **Torsional Moment** → Closed box structure (leading edge to trailing edge)
2. **Shear Flow** → Wing skins (upper and lower)
3. **Ribs and Spars** → Transfer to attachment points
4. **Wing-Body Interface** → Distributed across multiple attachment fittings

**Key Structural Elements**:
- Continuous skins forming closed torsion box
- Ribs providing shear webs
- Spar webs resisting warping
- Attachment fittings at wing-body interface

### 3. Fuselage Bending Loads

**Load Source**: Pressure differential, tail loads, cargo/passenger distribution

**Load Path**:
1. **Longitudinal Bending** → Upper and lower longerons and skin panels
2. **Skin Panels** → Continuous skin with stringers (tension/compression)
3. **Frames** → Maintain fuselage shape, distribute local loads
4. **Bulkheads** → React concentrated loads, provide end closures

**Key Structural Elements**:
- Longerons (primary bending members)
- Skin panels with stringers (distributed bending)
- Frames (lateral load distribution, shape maintenance)
- Pressure bulkheads (end closures)

**BWB Considerations**:
- Lower fuselage bending stresses due to wide cross-section and high moment of inertia
- Load distribution more uniform than conventional cylindrical fuselage

### 4. Pressure Loads

**Load Source**: Cabin pressurization (typical differential: 8.6 psi / 59 kPa)

**Load Path**:
1. **Internal Pressure** → Perpendicular to fuselage skins
2. **Hoop Tension** → Circumferential frames and skins
3. **Longitudinal Tension** → Stringers and longerons
4. **Bulkhead Loads** → Forward and aft pressure bulkheads

**Key Structural Elements**:
- **Skins**: Thin-walled pressure vessel
- **Frames**: Circumferential members resisting hoop tension, maintaining fuselage shape
- **Stringers**: Longitudinal members resisting longitudinal tension
- **Pressure Bulkheads**: Dome structures reacting net pressure force

**Design Equations** (Thin-Walled Pressure Vessel):
- Hoop Stress: σ_hoop = (p × r) / t
- Longitudinal Stress: σ_long = (p × r) / (2 × t)
  - Where: p = pressure, r = radius, t = wall thickness

**BWB Pressure Vessel**:
- Large, non-circular cross-section requires careful frame design
- Pressure loads combined with wing bending loads in integrated structure
- Frame spacing optimized for combined pressure and flight loads

### 5. Landing Gear Loads

**Load Source**: Ground reaction during landing, taxiing, braking

**Load Path**:
1. **Tire Contact** → Strut assembly
2. **Strut Loads** → Landing gear attachment fittings (high-strength titanium or steel)
3. **Attachment Fittings** → Fuselage primary frames and bulkheads
4. **Primary Frames** → Distributed to fuselage shell structure (skins, stringers, frames)
5. **Shell Structure** → Overall aircraft structure

**Critical Load Cases**:
- Vertical landing impact (limit load: 3g, ultimate load: 4.5g per [CS-25.473](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27))
- Braking loads (longitudinal deceleration)
- Side loads (crosswind landing, turning)
- Towing and pushback (ground handling)

**Key Structural Elements**:
- **Main Fitting**: Titanium or high-strength steel multi-bolt fitting
- **Reaction Structure**: Reinforced frames and bulkheads
- **Load Distribution**: Spanwise beams and longerons spreading load

**Design Considerations**:
- High load concentration requires robust fittings and reinforcement
- Multiple load paths for fail-safe design
- Fatigue-critical area requiring careful detail design and inspection

### 6. Engine/Pylon Loads

**Load Source**: Thrust, engine weight, inertia, gyroscopic moments

**Load Path**:
1. **Engine Mounts** → Pylon structure
2. **Pylon** → Wing or fuselage attachment fittings
3. **Attachment Fittings** → Primary wing structure (ribs, spars, skins)
4. **Wing Structure** → Distributed across wingspan and into fuselage center section

**Critical Load Cases**:
- Maximum thrust (forward)
- Engine failure with asymmetric thrust (side load, yaw moment)
- Engine seizure (abrupt torque)
- Crash loads (engine separation as designed)

**Key Structural Elements**:
- Engine mounts (2-point or 3-point attachment)
- Pylon box structure (fail-safe design)
- Wing attachment fittings (redundant load paths)
- Wing spars and ribs

**Design Considerations**:
- Pylon designed to separate in crash to protect fuel system
- Vibration isolation to prevent fatigue
- Thermal effects from engine operation

### 7. Tail Loads

**Load Source**: Horizontal and vertical stabilizer aerodynamic forces

**Load Path**:
1. **Stabilizer Aerodynamic Forces** → Stabilizer structure
2. **Stabilizer Root** → Attachment fittings on fuselage
3. **Attachment Fittings** → Aft fuselage frames and longerons
4. **Aft Fuselage** → Forward through fuselage bending members

**Critical Load Cases**:
- Maximum control surface deflection
- Gust loads
- Maneuvering loads
- Asymmetric loads (e.g., rudder deflection)

**Key Structural Elements**:
- Stabilizer attachment fittings
- Reinforced aft fuselage frames
- Longerons and keels

### 8. Cargo and Equipment Loads

**Load Source**: Cargo, passengers, seats, galleys, lavatories

**Load Path**:
1. **Load Application Point** → Floor beams and seat tracks
2. **Floor Structure** → Floor beams and cross-beams (secondary structure)
3. **Floor Supports** → Floor support columns or longerons
4. **Primary Structure** → Fuselage frames and skins

**Critical Load Cases**:
- Normal operations (1g + dynamic factor)
- Emergency landing (9g forward, 1.5g sideward, 3g upward, 6g downward per [CS-25.561](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27))
- Ditching and crash scenarios

**Design Considerations**:
- Seats and cargo restraints designed for emergency loads
- Floor structure provides load distribution to primary structure
- Crashworthiness requirements dictate floor and seat design

## Load Combinations

### Flight Loads

Per [CS-25.301](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27), structure must withstand combinations of:
- Maneuvering loads (pull-up, roll, yaw)
- Gust loads (vertical and lateral gusts)
- Ground loads (landing, taxiing, braking)
- Pressurization loads

**Critical Combinations**:
- **High-speed cruise with positive gust**: High wing bending + pressure
- **Maximum maneuver at maximum weight**: Peak bending and torsion
- **Landing impact**: Concentrated gear loads + fuselage bending
- **Asymmetric thrust**: Engine failure with side loads and yaw

### Load Factors

- **Limit Load**: Maximum expected in service (probability ~10^-5 per flight)
- **Ultimate Load**: 1.5 × Limit Load (per [CS-25.303](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27))
- **Proof Load**: Test load to verify structural integrity (often between limit and ultimate)

Structure must:
- Carry limit loads without permanent deformation
- Carry ultimate loads for 3 seconds without failure

## Load Path Verification

### Analysis Methods

1. **Finite Element Analysis (FEA)**:
   - Global model for overall load distribution
   - Local models for detailed stress analysis
   - Nonlinear analysis for ultimate load and post-buckling

2. **Hand Calculations**:
   - Preliminary sizing and verification
   - Simple load path checks
   - Sanity checks on FEA results

3. **Testing**:
   - Component tests validate load paths and failure modes
   - Full-scale static test verifies ultimate load capability
   - Fatigue test validates damage tolerance and durability

### Margin of Safety

For each structural element:

**MS = (Allowable / Applied) - 1**

- MS ≥ 0: Acceptable (positive margin)
- MS < 0: Unacceptable (negative margin, redesign required)

Typical margins:
- 0.0 to 0.1: Fully optimized, low margin (acceptable but monitored)
- 0.1 to 0.3: Good design (adequate margin for uncertainties)
- > 0.5: Conservative design (potential for weight reduction)

## Load Path Redundancy and Fail-Safe Design

### Multiple Load Paths

Critical structural areas incorporate redundancy:
- **Multiple stringers and frames**: Failure of one element does not lead to catastrophic failure
- **Crack stoppers**: Tear straps and doublers limit crack growth
- **Inspection intervals**: Based on time for detectable crack to grow to critical size

### Damage Scenarios

Per [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27), structure evaluated for:
- **Obvious damage**: Large, easily detectable (e.g., dent, hole)
- **Detectable damage**: Requires inspection to find
- **Undetectable damage**: Cannot be found with practical inspection methods

Each scenario has different residual strength requirements and inspection intervals.

## References

### Regulatory Documents
- [EASA CS-25.301 Loads](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.303 Factor of Safety](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.571 Damage Tolerance and Fatigue](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-01-01-001 Primary Structure Philosophy](53-50-01-01-001_Primary_Structure_Philosophy.md)
- [53-50-01-01-003 Material Selection Summary](53-50-01-01-003_Material_Selection_Summary.md)
- [53-50-01-05-001 Stress Margin Summary](../05_Margins_and_Summaries/53-50-01-05-001_Stress_Margin_Summary.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-22

---
