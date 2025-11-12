# CFD Cruise M0.82 – Setup Definition

**Analysis ID:** 02-11-00-AERO-001  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Condition:** Cruise, Mach 0.82 @ FL410 (ISA)  
**Status:** Setup Defined – Ready for Meshing / Solution  

---

## 1. Geometry and Baseline Traceability

- Source geometry: `CAD/BWB_Q100/Geometry/Cruise_Config.x_t` (TBD)
- Frozen geometry baseline:  
  - `02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/01_OVERVIEW/baseline_dimensions.json`
- Key baseline parameters:
  - Wingspan **b** = 52.0 m  
  - Wing area **S** = 845.0 m²  
  - Aspect ratio **AR** = 3.2  
  - Cruise sweep **Λ** = 35.0°

> Any modification to these values must go through ECR and update of `baseline_dimensions.json`.

---

## 2. Flight Condition

- Mach number: **0.82**
- Altitude: **41,000 ft** (12,497 m)
- Atmosphere: **ISA**
- Static pressure: **18.75 kPa**
- Static temperature: **216.65 K**
- Reynolds number (MAC-based): **≈ 4.5×10⁷**
- Target CL: **0.52**
- Estimated α: **2.5°** (to be refined after trim)

---

## 3. Solver Configuration

- Code: **ANSYS Fluent**
- Solver: **Pressure-based, steady RANS**
- Turbulence model: **k–ω SST**
- Energy: **On** (compressible)
- Discretization:
  - Pressure: **Second-order**
  - Momentum: **Second-order upwind**
  - k, ω: **Second-order upwind**
- Convergence:
  - Residuals < 1×10⁻⁵
  - CL, CD, CM stabilized (no trend over 200 iterations)

---

## 4. Mesh Strategy

- Mesh type: Hybrid unstructured (tet + prism layers)
- Target cell count (medium mesh): **~25M**
- Boundary layer:
  - y⁺ < 1
  - ≥ 25 layers
  - Growth factor ≤ 1.2
- Refinement:
  - Wing leading edge and shock region (40–60% chord)
  - Nacelle–wing junctions
  - Trailing edge and tip region

Mesh levels for independence:

- Coarse: ~10–12M cells
- Medium: ~25M cells
- Fine: ~40–50M cells

---

## 5. Boundary Conditions

- Far-field / inlet:
  - Type: **Pressure far-field**
  - Mach: 0.82
  - p = 18.75 kPa
  - T = 216.65 K
- Outlet:
  - Type: Pressure outlet
  - Backflow T = 216.65 K
  - Backflow p ≈ 18.75 kPa
- Aircraft:
  - Wall, no-slip, adiabatic
- Symmetry:
  - Symmetry plane (if half-model)

---

## 6. Monitors and Outputs

Monitors:

- CL, CD, CM on `wall-aircraft`
- Residuals for continuity, x/y/z-momentum, energy, k, ω

Post-processing outputs (minimum):

- Cp contours (upper/lower surface)
- Mach contours on symmetry and a few spanwise cuts
- Streamlines around nacelles and tip
- Drag breakdown by component (wing, center body, nacelles, tail if any)

---

## 7. Journal Automation

- Journal file: `SIMULATIONS/CFD/scripts/CFD_Cruise_M082_setup.jou`
- Usage:

```bash
fluent 3d -g -i SIMULATIONS/CFD/scripts/CFD_Cruise_M082_setup.jou
```

---

## 8. Document Control

* Version: 1.0
* Prepared by: [TBD]
* Reviewed by: [TBD]
* Date: 2025-11-10
