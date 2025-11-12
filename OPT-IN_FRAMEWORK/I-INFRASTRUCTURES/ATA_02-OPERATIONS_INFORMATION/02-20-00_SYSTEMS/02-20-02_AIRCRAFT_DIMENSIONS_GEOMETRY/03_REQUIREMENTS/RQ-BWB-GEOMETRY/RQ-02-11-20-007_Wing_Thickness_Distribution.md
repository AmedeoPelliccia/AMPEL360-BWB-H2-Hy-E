# RQ-02-11-20-007: Wing Thickness Distribution

**Priority:** High  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

The wing thickness distribution shall vary from 14% at the center body edge (BL 19m) to 8% at the wingtip (BL 26m), using supercritical airfoil sections optimized for transonic cruise at M0.82.

## Rationale

**Structural Efficiency:**
- Thicker root sections: Greater structural depth
- Support bending moment distribution
- Accommodate wing box structure
- Provide spar depth for loads

**Aerodynamic Performance:**
- Supercritical airfoils delay shock formation
- Optimized for cruise Mach 0.82
- Minimize wave drag at transonic speeds
- Maintain adequate L/D ratio

**Integration Requirements:**
- Center body thickness: 35% (pressure vessel)
- Transition region: 35% to 14% (smooth)
- Outer wing: 14% to 8% (linear taper)
- Wingtip: 8% (minimum practical thickness)

## Thickness Distribution

**Station Definitions:**

| Location | Buttline (m) | t/c Ratio | Notes |
|----------|--------------|-----------|-------|
| Center body | BL 0 | 35% | Pressure vessel |
| CB edge | BL 19 | 14% | Structural transition |
| Mid semi-span | BL 22.5 | 11% | Primary structure |
| Outer wing | BL 26 | 8% | Tip structure |

## Airfoil Selection

**Supercritical Design:**
- Flat upper surface aft of maximum thickness
- Delayed shock wave formation
- Critical Mach number: Mcr = 0.85
- Cruise Mach: M = 0.82 (design point)

**Performance Targets:**
- Section Cl at cruise: 0.35-0.45
- Drag divergence Mach: M_dd > 0.84
- Off-design performance acceptable
- High-lift device compatibility

## Verification Method

**CAD Analysis:**
- Airfoil sections extracted at defined stations
- Thickness ratios calculated
- Distribution curve verified
- Manufacturing feasibility confirmed

**CFD Validation:**
- Pressure distribution analysis
- Shock location verification
- Drag characteristics validated
- Performance targets confirmed

**Acceptance Criteria:**
- Thickness ratios within ±0.5% of target
- Smooth spanwise distribution
- No discontinuities or kinks
- Aerodynamic performance validated

## Impact on Design

**Structural:**
- Wing box depth adequate for loads
- Spar cap areas optimized
- Torsional stiffness sufficient
- Flutter margins maintained

**Systems Integration:**
- Fuel system (if wing tanks used)
- Flight control system routing
- Leading/trailing edge devices
- Landing gear (if wing-mounted)

## Compliance

**Standards:**
- [CS-25.143](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Controllability)
- [CS-25.251](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Vibration and buffeting)
- Aerodynamic design standards

**Related Requirements:**
- [RQ-02-11-20-004](RQ-02-11-20-004_Leading_Edge_Sweep_37deg.md) (LE Sweep)
- [RQ-02-11-20-005](RQ-02-11-20-005_Planform_Continuity.md) (Planform Continuity)
- [RQ-02-11-20-006](RQ-02-11-20-006_Cross_Section_Geometry.md) (Cross Section Geometry)
