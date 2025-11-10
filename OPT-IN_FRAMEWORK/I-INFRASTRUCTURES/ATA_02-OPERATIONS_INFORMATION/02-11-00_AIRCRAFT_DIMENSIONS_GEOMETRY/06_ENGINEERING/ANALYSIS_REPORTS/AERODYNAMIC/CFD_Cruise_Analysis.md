# CFD Cruise Analysis

**Analysis ID:** 02-11-00-AERO-001  
**Component Code:** 02-11-00  
**Title:** CFD Cruise Performance – BWB H₂ Hy-E Q100 INTEGRA  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Aerodynamic – CFD Cruise Performance  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Perform computational fluid dynamics (CFD) analysis of the blended-wing-body (BWB) configuration at cruise conditions to:

- Validate aerodynamic design and drag predictions  
- Assess transonic flow characteristics around the wing and center body  
- Support wing geometry optimization for cruise efficiency  
- Provide high-fidelity data for performance and mission analysis  

---

## 2. Flight Condition Definition

### 2.1 Cruise Point

- **Mach number:** 0.82  
- **Altitude:** 41,000 ft (12,497 m)  
- **Atmosphere:** ISA (T = 216.65 K, −56.5 °C)  
- **Static pressure:** 18.75 kPa  
- **Reynolds number:** 45×10⁶ (based on MAC)  

### 2.2 Aircraft Configuration

- **Gross weight (mid-cruise):** 180,000 kg  
- **CG location:** 25% MAC  
- **Target lift coefficient:** CL ≈ 0.52  
- **Estimated angle of attack:** α ≈ 2.5° (to be refined after trim analysis)  
- **Configuration:** Clean wing, cruise flap setting, nominal engine nacelle installation  

### 2.3 Geometry Reference (Frozen Baseline)

The CFD model geometry shall be consistent with the frozen geometry baseline defined in:

- `02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/01_OVERVIEW/baseline_dimensions.json`  
- `04_DESIGN/AERODYNAMIC_DESIGN/Wing_Planform.md`

**Monitored baseline values (for traceability):**

- **Wingspan (b):** 52.0 m  
- **Wing area (S):** 845.0 m²  
- **Aspect ratio (AR):** 3.2  
- **Cruise sweep (Λ):** 35.0°  

> **NOTE:** Any change to these frozen dimensions requires an approved ECR and must be reflected in the geometry baseline watchdog system before being used for new CFD runs.

---

## 3. CFD Methodology

### 3.1 Software and Solver

- **Software:** ANSYS Fluent  
- **Solver:** Pressure-based, steady RANS (Reynolds-Averaged Navier–Stokes)  
- **Turbulence model:** k–ω SST (Shear Stress Transport)  
- **Discretization schemes:**  
  - Momentum: 2nd-order upwind  
  - Turbulence quantities: 2nd-order upwind  
- **Convergence criteria:**  
  - Residuals < 1×10⁻⁵ for all equations  
  - Integrated forces and moments converged and oscillation-free  

### 3.2 Computational Domain

- **Domain size:** ≈ 20× aircraft length in all directions (far-field boundaries)  
- **Symmetry:** Half-model with symmetry plane (if applicable)  
- **Mesh type:** Hybrid unstructured (tetrahedra + prism layers)  
- **Total cell count:** ~25 million cells (target)  
- **Boundary layer resolution:**  
  - First cell height sized for y⁺ < 1 at walls  
  - At least 25–30 prism layers with smooth growth to outer mesh  

### 3.3 Boundary Conditions

- **Inlet / Far-field:** Mach 0.82, static pressure 18.75 kPa, ISA temperature  
- **Outlet:** Pressure outlet / far-field  
- **Aircraft surface:** No-slip wall, adiabatic  
- **Symmetry plane:** Symmetry boundary condition (if half-model used)  

---

## 4. Results (to be populated)

### 4.1 Aerodynamic Coefficients

| Parameter                 | Value (CFD) | Target     | Status   |
|---------------------------|-------------|------------|----------|
| Lift coefficient (CL)     | TBD         | 0.52       | Pending  |
| Drag coefficient (CD)     | TBD         | < 0.022    | Pending  |
| Pitching moment (CM)      | TBD         | ~0 (trim)  | Pending  |
| L/D ratio                 | TBD         | > 23       | Pending  |

- **Trim condition:** To be checked against control surface deflections and CG envelope.  
- **Comparison:** To be cross-checked with low-fidelity methods and performance sizing tools.

### 4.2 Surface Pressure Distribution

- **Upper surface:** Shock location, strength and extent TBD from Cp contours  
- **Lower surface:** Pressure recovery characteristics TBD  
- **Leading edge:** Suction peak magnitude and extent TBD  

Intended post-processing:

- Cp distributions at selected spanwise stations (root, mid-span, near tip)  
- Comparison with design polars from `Wing_Planform.md`  

### 4.3 Flow Visualization

Qualitative flow-field visualization to include:

- Shock wave patterns on upper surface (Mach contours)  
- Boundary layer behavior (separation / reattachment, if any)  
- Tip vortex formation and roll-up  
- Engine nacelle and pylon interference effects  

---

## 5. Drag Breakdown

| Component          | Drag Count (ΔCD × 10⁴) | Percentage |
|--------------------|------------------------|------------|
| Induced drag       | TBD                    | TBD %      |
| Friction drag      | TBD                    | TBD %      |
| Form drag          | TBD                    | TBD %      |
| Wave drag (shock)  | TBD                    | TBD %      |
| Interference drag  | TBD                    | TBD %      |
| **Total**          | **TBD**                | **100%**   |

> **Note:** Drag breakdown methodology (pressure/friction integration, component tagging, and far-field methods) shall be documented in `CALCULATIONS/AERODYNAMIC/Drag_Breakdown_Calc.csv` and associated scripts.

---

## 6. Validation and Verification

### 6.1 Mesh Independence Study

- [ ] Define at least three mesh levels (coarse, medium, fine)  
- [ ] Show CD variation < 1% between medium and fine mesh  
- [ ] Document CL, CD, CM vs. cell count  

### 6.2 Comparison with Experiments / Other Data

- [ ] Compare with wind tunnel data (when available)  
- [ ] Compare with low-order aerodynamic models (VLM / panel methods)  
- [ ] Future: Correlate with flight test data where applicable  

---

## 7. Data Management and Traceability

- Input geometry model shall be traceable to:  
  - `02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/01_OVERVIEW/baseline_dimensions.json`  
  - ECR records for any geometry changes since baseline freeze.  

- CFD case setup and meshes shall be stored under:  
  - `SIMULATIONS/CFD/Cruise_M082_CFD_Setup.md`  
  - Associated solver input / result files in the CFD data repository.  

> **Consistency rule:** If the geometry used in CFD deviates from the frozen baseline, an ECR must be raised, and the geometry baseline watchdog will enforce alignment in downstream documents.

---

## 8. References

- `04_DESIGN/AERODYNAMIC_DESIGN/Wing_Planform.md`  
- `SIMULATIONS/CFD/Cruise_M082_CFD_Setup.md`  
- `CALCULATIONS/AERODYNAMIC/Drag_Breakdown_Calc.csv`  
- `02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/01_OVERVIEW/baseline_dimensions.json`  

---

**Document Control:**  
- **Version:** 1.0 (Draft – CFD case not yet solved)  
- **Prepared by:** [TBD]  
- **Reviewed by:** [TBD]  
- **Approved by:** [TBD]  
- **Date:** 2025-11-10  

