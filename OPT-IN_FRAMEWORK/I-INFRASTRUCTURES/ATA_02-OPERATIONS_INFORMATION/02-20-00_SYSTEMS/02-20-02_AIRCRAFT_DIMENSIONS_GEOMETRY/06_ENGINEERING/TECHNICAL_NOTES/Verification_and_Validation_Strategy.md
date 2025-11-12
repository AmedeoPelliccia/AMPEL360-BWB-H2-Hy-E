# Verification and Validation Strategy

**Document ID:** 02-11-00-TN-005  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Status:** Draft  
**Date:** 2025-11-10

---

## 1. Purpose

Define verification and validation (V&V) strategy for engineering analyses to ensure accuracy, reliability, and compliance with certification requirements.

---

## 2. Definitions

### 2.1 Verification

**"Are we building the product right?"**

Verification confirms that:
- Analysis methods are correctly implemented
- Models accurately represent design intent
- Calculations are free from errors

**Methods:** Code verification, mesh convergence, hand calculations, independent checks

### 2.2 Validation

**"Are we building the right product?"**

Validation confirms that:
- Analysis results match physical reality
- Models predict actual behavior
- Assumptions are appropriate

**Methods:** Test correlation, comparison with flight data, benchmarking against known solutions

---

## 3. Verification Activities

### 3.1 FEM Verification

**Model Quality Checks:**
- [ ] No duplicate nodes or elements
- [ ] No free edges or unconnected elements
- [ ] Element aspect ratios < 10:1 (preferably < 5:1)
- [ ] Element warping < 10°
- [ ] Normal directions consistent (all pointing outward)

**Mesh Convergence Study:**
- [ ] Refine mesh by factor of 2× (in each direction)
- [ ] Verify stresses converge within 5%
- [ ] Verify displacements converge within 2%

**Load and Boundary Condition Checks:**
- [ ] Applied loads balance (sum of reactions = applied loads)
- [ ] Boundary conditions do not over-constrain model
- [ ] Load paths are continuous and logical

**Hand Calculation Verification:**
- [ ] Compare FEM results to hand calculations for simple load cases
- [ ] Verify beam bending stress: σ = M × c / I
- [ ] Verify hoop stress in pressure vessel: σ = P × r / t

### 3.2 CFD Verification

**Mesh Independence:**
- [ ] Refine mesh by factor of 1.5× to 2×
- [ ] Verify CL and CD converge within 1%
- [ ] Verify pressure distribution converges

**Residual Convergence:**
- [ ] All residuals < 10⁻⁶
- [ ] Force and moment coefficients stable (< 0.1% variation over 500 iterations)

**Conservation Checks:**
- [ ] Mass flow in = mass flow out (for internal flows)
- [ ] Energy balance satisfied

**Code-to-Code Comparison:**
- [ ] Compare ANSYS Fluent results with OpenFOAM or similar solver
- [ ] Verify agreement within 5% for CL, CD

### 3.3 Performance Analysis Verification

**Energy Balance:**
- [ ] Breguet range equation: Verify range calculation using energy method
- [ ] Climb performance: Verify using point-mass equations of motion

**Sanity Checks:**
- [ ] Take-off distance reasonable compared to similar aircraft
- [ ] Cruise L/D in expected range for BWB configuration (20-25)
- [ ] Specific fuel consumption in expected range for H₂ engines

---

## 4. Validation Activities

### 4.1 Structural Validation

**Component Testing:**
- [ ] Wing box section: Load to ultimate, compare measured strain to FEM predictions
- [ ] Pressure vessel barrel: Pressurize to proof load, measure hoop strain
- [ ] Landing gear drop test: Measure gear stroke and compare to simulation

**Full-Scale Static Test (if performed):**
- [ ] Instrument critical locations with strain gauges
- [ ] Apply limit and ultimate loads
- [ ] Compare measured strains and deflections to FEM predictions
- [ ] Target: Agreement within 10% for critical locations

**Acceptance Criteria:**
- Measured strain within 15% of predicted
- Failure mode matches prediction

### 4.2 Aerodynamic Validation

**Wind Tunnel Testing:**
- [ ] Test scaled model (e.g., 1:10 scale) in wind tunnel
- [ ] Measure lift, drag, and moment coefficients
- [ ] Compare to CFD predictions at same Reynolds number
- [ ] Target: Agreement within 5% for CL, 10% for CD

**Flight Test Validation:**
- [ ] Measure in-flight pressures, forces, and accelerations
- [ ] Compare to CFD and performance predictions
- [ ] Update models as necessary

**Acceptance Criteria:**
- Lift coefficient within 3% of CFD prediction
- Drag coefficient within 10% of CFD prediction (drag is harder to predict accurately)

### 4.3 Performance Validation

**Flight Test:**
- [ ] Measure take-off distance, climb rate, cruise speed, landing distance
- [ ] Compare to performance analysis predictions
- [ ] Verify fuel consumption matches SFC assumptions

**Acceptance Criteria:**
- Take-off and landing distances within 5% of predicted
- Range within 10% of predicted (difficult to measure precisely)

---

## 5. Independent Review

### 5.1 Peer Review

**Process:**
- All critical analyses reviewed by senior engineer (not the original analyst)
- Reviewer checks assumptions, methods, calculations, and conclusions
- Findings documented in review checklist

**Criteria:**
- Assumptions appropriate and documented
- Methods compliant with standards
- Results reasonable and properly interpreted

### 5.2 Third-Party Review (if required)

**Process:**
- External expert reviews analysis for certification authority
- Reviewer has access to models, data, and documentation
- Findings addressed and documented

---

## 6. Traceability Matrix

### 6.1 Verification Traceability

| Analysis | Verification Method | Status | Reference |
|----------|---------------------|--------|-----------|
| Global FEM | Mesh convergence, hand calc | Planned | FEM_Global_Model.md |
| Wing box stress | Component test correlation | Planned | Wing_Box_Stress_Analysis.md |
| Pressure vessel | Pressure test correlation | Planned | Pressure_Vessel_Analysis.md |
| CFD cruise | Mesh independence, wind tunnel | Planned | CFD_Cruise_Analysis.md |
| Take-off performance | Flight test correlation | Planned | Takeoff_Performance.md |

### 6.2 Validation Traceability

| Analysis | Validation Method | Status | Test Data Reference |
|----------|-------------------|--------|---------------------|
| FEM Global Model | Full-scale static test | Planned | Test Report TBD |
| CFD Cruise | Wind tunnel + flight test | Planned | Test Report TBD |
| Landing gear loads | Drop test | Planned | Test Report TBD |
| Range performance | Flight test | Planned | Flight Test Report TBD |

---

## 7. Documentation Requirements

### 7.1 Analysis Report Content

Each analysis report must include:
- **Objective:** What is being analyzed
- **Methodology:** How the analysis is performed
- **Assumptions:** Clearly stated and justified
- **Results:** Quantitative results with margins of safety
- **Verification:** Evidence of verification (convergence, hand calc, etc.)
- **Validation:** Comparison to test data (if available)
- **Conclusions:** Engineering assessment of results

### 7.2 Version Control

- All analysis files (FEM, CFD, scripts) under version control
- Analysis reports tagged with model version
- Changes to baseline design trigger impact assessment and re-analysis

---

## 8. Acceptance Criteria Summary

### 8.1 Verification Acceptance

| Analysis Type | Convergence Criterion | Hand Calc Agreement |
|---------------|----------------------|---------------------|
| FEM stress | < 5% change with mesh refinement | Within 10% |
| FEM deflection | < 2% change with mesh refinement | Within 5% |
| CFD CL | < 1% change with mesh refinement | Within 5% (theory) |
| CFD CD | < 2% change with mesh refinement | Within 10% (theory) |

### 8.2 Validation Acceptance

| Analysis Type | Test Agreement Criterion |
|---------------|--------------------------|
| FEM strain | Within 15% of measured |
| FEM deflection | Within 10% of measured |
| CFD CL | Within 5% of wind tunnel |
| CFD CD | Within 10% of wind tunnel |
| Performance (TO/LDG) | Within 5% of flight test |

---

## 9. Non-Conformance and Corrective Action

### 9.1 Discrepancy Resolution

If verification or validation fails:
1. **Investigate:** Identify root cause (model error, test error, assumption)
2. **Correct:** Update model, re-run analysis, or re-test
3. **Document:** Record discrepancy, corrective action, and revised results
4. **Re-verify/Re-validate:** Confirm corrective action resolves issue

### 9.2 Engineering Judgment

In cases where test data is not available or validation is not possible:
- Rely on conservative assumptions and margins
- Perform sensitivity studies to bound uncertainty
- Document engineering rationale

---

## 10. References

- NASA-STD-7009A – Standard for Models and Simulations
- AIAA G-077-1998 – Guide for the Verification and Validation of Computational Fluid Dynamics Simulations
- ASME V&V 20-2009 – Standard for Verification and Validation in Computational Fluid Dynamics and Heat Transfer
- CS-25.307 – Proof of Structure
- SAE ARP 4754A – Guidelines for Development of Civil Aircraft and Systems

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Author:** Chief Engineer – Verification & Validation
- **Reviewed by:** Program Chief Engineer
- **Date:** 2025-11-10
