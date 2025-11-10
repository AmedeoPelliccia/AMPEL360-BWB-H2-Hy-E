# FEM Global Model Analysis

**Document ID:** 02-11-00-STR-001  
**Revision:** A  
**Date:** 2025-11-10  
**Status:** Template - Awaiting Data

## 1. Executive Summary

This document describes the finite element model (FEM) of the AMPEL360 Q100 aircraft global structure and presents key analysis results for certification load cases per CS-25.

**Key Findings:** (To be populated)
- Maximum stress locations: TBD
- Critical load cases: TBD
- Minimum margins of safety: TBD
- Design recommendations: TBD

## 2. Scope and Objectives

### 2.1 Scope
- Global FEM model of complete airframe structure
- All CS-25 critical load cases
- Static stress and deflection analysis
- Identification of design-critical regions

### 2.2 Objectives
- Demonstrate structural adequacy per CS-25.305, CS-25.307
- Calculate stress, strain, and deflection under limit and ultimate loads
- Identify critical stress concentrations requiring detailed analysis
- Provide input data for downstream analyses (fatigue, damage tolerance)

### 2.3 Out of Scope
- Detailed joint and fastener analysis (see specialized reports)
- Fatigue life prediction (see STR-005)
- Damage tolerance analysis (see STR-006)
- Dynamic/transient analysis (flutter in AERO-005)

## 3. Model Description

### 3.1 Geometry and Discretization

**Model Content:** (To be populated)
- Total number of nodes: TBD
- Total number of elements: TBD
- Element types used:
  - Shell elements (CQUAD4, CTRIA3): TBD count - for skins, webs, ribs
  - Beam elements (CBEAM, CBAR): TBD count - for stringers, longerons, frames
  - Solid elements (CHEXA, CTETRA): TBD count - for complex joints, landing gear attachments
  - RBE2/RBE3 elements: TBD count - for load application and kinematic coupling

**Geometric Scope:**
- Center body (BWB) including:
  - Upper and lower skins
  - Internal ribs and frames
  - Floor beams and seat tracks
  - Cargo floor structure
- Wing structure including:
  - Wing box (front/rear spars, upper/lower skins)
  - Stringers and intercostals
  - Ribs (full-depth and intercostal)
  - Leading and trailing edge structures
- Empennage (vertical stabilizers)
- Landing gear attachment fittings
- Fuel cell nacelle support structure
- Door frames and window cutouts

**Mesh Quality Metrics:** (To be populated)
- Target element size: TBD mm (critical areas), TBD mm (general areas)
- Aspect ratio: <5:1 for shell elements
- Warpage: <10° for quad elements
- Jacobian ratio: >0.6
- Mesh convergence study results: TBD

### 3.2 Material Models

Materials used in the model (reference TN-004 for detailed properties):

| Material ID | Description | Element Type | Fty (MPa) | Ftu (MPa) | E (GPa) | Density (kg/m³) |
|-------------|-------------|--------------|-----------|-----------|---------|-----------------|
| MAT-001 | Al 7075-T6 (Upper Skins) | Shell | TBD | TBD | 72 | 2810 |
| MAT-002 | Al 7050-T7451 (Lower Skins) | Shell | TBD | TBD | 72 | 2830 |
| MAT-003 | Al 2024-T3 (Webs, Ribs) | Shell | TBD | TBD | 73 | 2780 |
| MAT-004 | CFRP IM7/8552 (Wing Skins) | Shell | TBD | TBD | 165 (E11) | 1600 |
| MAT-005 | CFRP T700/Epoxy (Stiffeners) | Shell | TBD | TBD | 135 (E11) | 1550 |
| MAT-006 | Ti-6Al-4V (Fittings) | Solid | TBD | TBD | 114 | 4430 |
| MAT-007 | Steel 4340 (Landing Gear) | Solid | TBD | TBD | 200 | 7850 |

**Note:** All material properties include appropriate knockdown factors per TN-004.

### 3.3 Boundary Conditions and Constraints

**Symmetric Boundary Conditions:**
- For symmetric load cases: Nodes on XZ plane (Y=0) constrained in Y-direction
- Anti-symmetric cases modeled as half-span with appropriate constraints

**Attachment Points:**
- Main landing gear: Fixed in all DOF at gear trunnion nodes
- Nose landing gear: Fixed in all DOF at gear trunnion nodes
- Alternative: Landing gear represented by spring elements (stiffness TBD kN/mm)

**Ground Constraints:**
- Ground load cases: Landing gear tire contact patches constrained per load case

### 3.4 Mass Representation

**Lumped Masses:**
- Systems and equipment: CONM2 elements at attachment locations
- Fuel (H₂): Distributed pressure loads on tank walls + CONM2 at tank CG
- Payload: Distributed floor loads representing passenger/cargo distribution
- Nacelles and fuel cells: CONM2 at nacelle attachment points

**Total Aircraft Mass:** (To be populated)
- OEW: TBD kg
- MTOW: TBD kg
- Fuel mass: TBD kg
- Max payload: TBD kg

Mass distribution per ATA chapter available in WB-002.

## 4. Load Cases Analyzed

All load cases per TN-003 (Load_Case_Definition_and_Combinations.md) and CS25_Load_Case_List.csv.

### 4.1 Flight Load Cases (Symmetric)

| Load Case ID | Description | CS-25 Ref | Load Factor (nz) | Airspeed | Status |
|--------------|-------------|-----------|------------------|----------|---------|
| LC-F-001 | Positive Maneuvering at VA | 25.337(b) | +3.8 | VA | Planned |
| LC-F-002 | Positive Maneuvering at VC | 25.337(a) | +2.5 | VC | Planned |
| LC-F-003 | Negative Maneuvering at VA | 25.337(b) | -1.5 | VA | Planned |
| LC-F-004 | Negative Maneuvering at VC | 25.337(a) | -1.0 | VC | Planned |
| LC-F-005 | Positive Gust at VC (50 ft/s) | 25.341(a) | TBD | VC | Planned |
| LC-F-006 | Negative Gust at VC (50 ft/s) | 25.341(a) | TBD | VC | Planned |
| LC-F-007 | Positive Gust at VD (25 ft/s) | 25.341(a) | TBD | VD | Planned |
| LC-F-008 | Maximum Cabin Pressure | 25.365 | +1.0 | - | Planned |

### 4.2 Flight Load Cases (Asymmetric)

| Load Case ID | Description | CS-25 Ref | Remarks | Status |
|--------------|-------------|-----------|---------|---------|
| LC-F-101 | Rolling Maneuver | 25.349 | Full aileron deflection | Planned |
| LC-F-102 | Yaw Maneuver | 25.351 | Full rudder deflection | Planned |
| LC-F-103 | Lateral Gust | 25.341 | Side gust at VC | Planned |
| LC-F-104 | Engine Out (Asymmetric Thrust) | 25.363 | One fuel cell inoperative | Planned |

### 4.3 Ground Load Cases

| Load Case ID | Description | CS-25 Ref | Remarks | Status |
|--------------|-------------|-----------|---------|---------|
| LC-G-001 | Level Landing - Limit | 25.479 | Symmetric, nz=TBD | Planned |
| LC-G-002 | Level Landing - Ultimate | 25.479 | Symmetric, nz=1.5× limit | Planned |
| LC-G-003 | Tail-Down Landing | 25.481 | Max rotation angle | Planned |
| LC-G-004 | One-Gear Landing (MLG) | 25.483 | Single main gear | Planned |
| LC-G-005 | Side Load (Drift) Landing | 25.485 | Lateral drift angle | Planned |
| LC-G-006 | Braked Roll | 25.493 | Max braking torque | Planned |
| LC-G-007 | Turning on Ground | 25.495 | Min turning radius | Planned |
| LC-G-008 | Nose Gear Yawing | 25.499 | Steering loads | Planned |
| LC-G-009 | Towing Loads | 25.509 | Forward and reverse tow | Planned |
| LC-G-010 | Jacking Loads | 25.519 | Three jacking points | Planned |

### 4.4 Emergency Landing Cases

| Load Case ID | Description | CS-25 Ref | Remarks | Status |
|--------------|-------------|-----------|---------|---------|
| LC-E-001 | Emergency Landing - Forward | 25.561(b)(2) | nx=+9.0g, nz=-3.0g | Planned |
| LC-E-002 | Emergency Landing - Aft | 25.561(b)(2) | nx=-1.5g, nz=-3.0g | Planned |
| LC-E-003 | Emergency Landing - Lateral | 25.561(b)(3) | ny=±3.0g, nz=-3.0g | Planned |

### 4.5 Pressurization and Special Cases

| Load Case ID | Description | CS-25 Ref | Remarks | Status |
|--------------|-------------|-----------|---------|---------|
| LC-P-001 | Max Operating Pressure | 25.365 | ΔP = TBD psi, cruise condition | Planned |
| LC-P-002 | Proof Pressure | 25.843 | 1.33 × max operating pressure | Planned |
| LC-D-001 | Door Opening/Closing | 25.783 | Door loads during operation | Planned |

**Total Number of Load Cases:** TBD

## 5. Analysis Results

### 5.1 Global Stress and Deflection Summary

**(To be populated after FEM runs)**

**Maximum Stresses - Limit Load:**

| Load Case | Location | Component | Stress Type | Value (MPa) | Allowable (MPa) | Margin of Safety |
|-----------|----------|-----------|-------------|-------------|-----------------|------------------|
| TBD | TBD | TBD | von Mises | TBD | TBD | TBD |
| TBD | TBD | TBD | Principal | TBD | TBD | TBD |
| TBD | TBD | TBD | Shear | TBD | TBD | TBD |

**Maximum Stresses - Ultimate Load:**

| Load Case | Location | Component | Stress Type | Value (MPa) | Allowable (MPa) | Margin of Safety |
|-----------|----------|-----------|-------------|-------------|-----------------|------------------|
| TBD | TBD | TBD | von Mises | TBD | TBD | TBD |
| TBD | TBD | TBD | Principal | TBD | TBD | TBD |

**Maximum Deflections:**

| Load Case | Location | Deflection (mm) | Limit (mm) | Status |
|-----------|----------|----------------|------------|--------|
| TBD | Wing tip | TBD | TBD | TBD |
| TBD | Fuselage crown | TBD | TBD | TBD |

**Margin of Safety Calculation:**
```
MS = (Allowable / Applied Stress) - 1
```
Where:
- MS ≥ 0: Adequate
- MS < 0: Inadequate (redesign required)

### 5.2 Critical Load Cases and Hot Spots

**(To be populated)**

**Critical Flight Load Cases:**
- TBD: Most critical for [component/location]
- TBD: Most critical for [component/location]

**Critical Ground Load Cases:**
- TBD: Most critical for landing gear attachments
- TBD: Most critical for fuselage keel beam

**Identified Hot Spots:**
1. **Location:** TBD
   - **Load Case:** TBD
   - **Stress:** TBD MPa
   - **Margin:** TBD
   - **Recommendation:** TBD

2. **Location:** TBD
   - **Load Case:** TBD
   - **Stress:** TBD MPa
   - **Margin:** TBD
   - **Recommendation:** TBD

### 5.3 Wing Box Results

Detailed wing box stress results reported in STR-002 (Wing_Box_Stress_Analysis.md).

**Summary:**
- Critical ribs/stringers: TBD
- Maximum bending stress: TBD MPa at TBD% span
- Panel buckling check: TBD (see STR-002 for details)

### 5.4 Pressure Vessel Results

Detailed pressure vessel results reported in STR-003 (Pressure_Vessel_Analysis.md).

**Summary:**
- Hoop stress: TBD MPa
- Longitudinal stress: TBD MPa
- von Mises stress: TBD MPa
- Margin vs burst: TBD

### 5.5 Landing Gear Attachment Results

Detailed landing gear results reported in STR-004 (Landing_Gear_Loads.md).

**Summary:**
- Main gear attachment MS: TBD
- Nose gear attachment MS: TBD
- Critical fasteners: TBD

## 6. Mesh Convergence and Model Validation

### 6.1 Mesh Convergence Study

**(To be populated)**

A mesh convergence study was performed to ensure solution accuracy.

| Mesh Refinement Level | Element Count | Max Stress (MPa) | % Change from Previous |
|-----------------------|---------------|------------------|------------------------|
| Coarse | TBD | TBD | - |
| Medium | TBD | TBD | TBD% |
| Fine (Selected) | TBD | TBD | TBD% |
| Very Fine | TBD | TBD | TBD% |

**Convergence Criterion:** Stress change < 5% between consecutive refinements

**Selected Mesh:** Fine mesh (TBD elements) provides adequate accuracy with acceptable computational cost.

### 6.2 Model Validation

**(To be populated)**

**Validation Activities per TN-005:**
1. **Hand Calculations:** Simple beam models compared to FEM for basic load cases
   - Agreement: TBD%
2. **Benchmark Problems:** NAFEMS benchmark cases
   - Results: TBD
3. **Component Testing:** (When available) Comparison to test data
   - Correlation: TBD
4. **Peer Review:** Independent checker verified model setup
   - Status: TBD

**Validation Status:** TBD

## 7. Design Recommendations

**(To be populated after analysis)**

Based on FEM results, the following design actions are recommended:

### 7.1 Immediate Actions (Negative Margins)
- TBD

### 7.2 Design Improvements (Low Margins)
- TBD

### 7.3 Optimization Opportunities
- TBD

### 7.4 Further Analyses Required
- Detailed joint analysis at location TBD
- Fatigue analysis at hot spot TBD
- Damage tolerance analysis for critical region TBD

## 8. Compliance Statement

**(To be finalized)**

The FEM global model demonstrates compliance with the following CS-25 requirements:
- **CS-25.301 (Loads):** Load cases per TN-003 ✓
- **CS-25.303 (Factor of Safety):** Ultimate = 1.5 × Limit ✓
- **CS-25.305 (Strength and Deformation):** All margins ≥ 0 (TBD)
- **CS-25.307 (Proof of Structure):** Analysis method acceptable per CS-25.307(b) ✓

**Overall Compliance:** TBD pending final analysis results

## 9. References

### 9.1 Design Inputs
- 04_DESIGN/ - CAD geometry and structural arrangement
- TN-001: Modelling Assumptions and Conventions
- TN-002: Coordinate Systems and Reference Frames
- TN-003: Load Case Definition and Combinations
- TN-004: Materials Allowables Selection

### 9.2 Calculations
- CS25_Load_Case_List.csv
- Wing_Box_Section_Calcs.csv
- Gear_Loads_Spreadsheet.csv

### 9.3 Simulations
- SIMULATIONS/FEM/Global_Model_InputDeck/

### 9.4 Standards
- CS-25 Amendment 27
- Analysis_Standards_Applied.csv

### 9.5 Related Analysis Reports
- STR-002: Wing_Box_Stress_Analysis
- STR-003: Pressure_Vessel_Analysis
- STR-004: Landing_Gear_Loads
- STR-005: Fatigue_Analysis
- STR-006: Damage_Tolerance_Analysis
- CERT-002: Structural_Substantiation

## 10. Required Visualizations

The following PNG visualizations shall be created:

- **02-11-00-STR-001-FIG-01_FEM_Model_Overview.png**
  - 3D isometric view of complete FEM model
  - Color-coded by component (wing box, center body, empennage, landing gear)
  - Include coordinate system reference

- **02-11-00-STR-001-FIG-02_FEM_LoadCases_Map.png**
  - Schematic showing main CS-25 load case categories
  - Flight (maneuver/gust), Ground (landing/taxi), Pressure, Emergency
  - Indicate critical load cases for each structural region

## 11. Revision History

| Revision | Date | Author | Description |
|----------|------|--------|-------------|
| A | 2025-11-10 | System | Initial template - awaiting FEM data |

---

**DOCUMENT STATUS:** Template - Requires FEM Model Completion

**NEXT ACTIONS:**
1. Complete FEM global model (target: Week 6)
2. Run all load cases per CS25_Load_Case_List.csv
3. Post-process results and populate Section 5
4. Generate required PNG visualizations
5. Update traceability matrix in Engineering_Analysis_Overview.md

**END OF DOCUMENT**
