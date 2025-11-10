# FEM Global Model Analysis

**Analysis ID:** 02-11-00-STR-001  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Structural - Finite Element Model  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Develop and validate a global finite element model (FEM) of the AMPEL360 BWB aircraft to:
- Determine structural load paths and stress distributions
- Calculate deflections and deformations under design load cases
- Provide basis for detailed structural sizing
- Support certification compliance demonstrations per CS-25.305

---

## 2. Scope

### 2.1 Model Extent
- **Full airframe:** Center body, wing box, vertical stabilizers, landing gear attachments
- **Elements:** Shell elements for skin and webs, beam elements for stringers and frames
- **Nodes:** Approximately 500,000 nodes, 450,000 elements
- **Material models:** Isotropic (aluminum alloys), orthotropic (carbon fiber composites)

### 2.2 Load Cases
Load cases per CS-25 requirements:
- Symmetric maneuvers (2.5g and -1.0g)
- Gust loads (vertical and lateral)
- Landing loads (limit and ultimate)
- Pressurization loads (differential pressure 8.0 psi)
- Combined load cases per CS-25.365

---

## 3. Methodology

### 3.1 Modeling Approach
- **Software:** MSC Nastran
- **Element types:** CQUAD4, CTRIA3, CBEAM, CROD
- **Connection:** RBE2/RBE3 for load introduction
- **Coordinate system:** Aircraft reference frame (nose +X, right wing +Y, up +Z)

### 3.2 Boundary Conditions
- **Fuselage:** Constrained at center body center node (3 translations, 3 rotations)
- **Landing gear:** Spring elements representing gear stiffness
- **Engines:** Mass elements at engine CG with appropriate inertia relief

### 3.3 Material Properties
- **Aluminum 7075-T6:** E=71 GPa, ν=0.33, ρ=2810 kg/m³
- **Carbon/Epoxy:** E₁=135 GPa, E₂=10 GPa, G₁₂=5 GPa, ρ=1600 kg/m³
- **Allowables:** Per MIL-HDBK-5J and CMH-17 (A-basis for critical structures, B-basis for redundant)

---

## 4. Analysis Results

### 4.1 Mass Properties (from FEM)
- **Structural mass:** TBD kg
- **CG location:** TBD m from nose
- **Moments of inertia:** Ixx = TBD, Iyy = TBD, Izz = TBD kg·m²

### 4.2 Load Distribution
- **Wing root bending moment:** TBD kN·m at 2.5g pull-up
- **Center body hoop stress:** TBD MPa at max cabin pressure
- **Landing gear reaction loads:** TBD kN vertical, TBD kN drag

### 4.3 Stress Results
- **Wing upper surface:** Max compressive stress TBD MPa (allowable: TBD MPa)
- **Wing lower surface:** Max tensile stress TBD MPa (allowable: TBD MPa)
- **Pressure vessel:** Max hoop stress TBD MPa (allowable: TBD MPa)

### 4.4 Deflection Results
- **Wingtip deflection:** TBD m at 2.5g (limit load)
- **Center body deflection:** TBD mm under pressurization
- **Landing gear stroke:** TBD mm at max vertical load

---

## 5. Margin of Safety Calculations

Margin of Safety (MS) = (Allowable / Applied) - 1

| Component | Load Case | Applied Stress (MPa) | Allowable (MPa) | MS | Status |
|-----------|-----------|----------------------|-----------------|-----|--------|
| Wing box upper skin | 2.5g maneuver | TBD | TBD | TBD | Pending |
| Wing box lower skin | 2.5g maneuver | TBD | TBD | TBD | Pending |
| Pressure vessel | Max cabin ΔP | TBD | TBD | TBD | Pending |
| Landing gear attach | Landing impact | TBD | TBD | TBD | Pending |

**Requirement:** All MS ≥ 0.0 for limit load, MS ≥ 0.0 for ultimate load (1.5× limit)

---

## 6. Validation and Verification

### 6.1 Model Verification
- [ ] Mesh convergence study completed
- [ ] Free-free mode shapes match hand calculations
- [ ] Mass and CG match weight and balance estimates
- [ ] Load paths are continuous and logical

### 6.2 Model Validation
- [ ] Correlation with component test data (if available)
- [ ] Comparison with similar aircraft FEM results
- [ ] Independent check by senior stress engineer

---

## 7. References

### 7.1 Design Documents
- `04_DESIGN/STRUCTURAL_DESIGN/Wing_Box_Design.md`
- `04_DESIGN/STRUCTURAL_DESIGN/Center_Body_Structure.md`

### 7.2 Input Data
- `CALCULATIONS/STRUCTURAL/Wing_Box_Section_Calcs.csv`
- `SIMULATIONS/FEM/Global_Model_InputDeck/ampel360_q100_global_model.dat`

### 7.3 Standards
- CS-25.305 – Strength and Deformation
- CS-25.301 – Loads
- MSC Nastran User's Guide

---

## 8. Conclusions and Recommendations

### 8.1 Conclusions
- TBD upon analysis completion

### 8.2 Recommendations
- TBD upon analysis completion

### 8.3 Next Steps
1. Complete detailed FEM mesh for all structural components
2. Define all load cases per CS-25 requirements
3. Execute FEM analysis for limit and ultimate loads
4. Post-process results and calculate margins of safety
5. Document results and update this report

---

**Document Control:**
- **Prepared by:** Structural Analysis Team
- **Reviewed by:** Chief Structural Engineer
- **Approved by:** Program Chief Engineer
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
