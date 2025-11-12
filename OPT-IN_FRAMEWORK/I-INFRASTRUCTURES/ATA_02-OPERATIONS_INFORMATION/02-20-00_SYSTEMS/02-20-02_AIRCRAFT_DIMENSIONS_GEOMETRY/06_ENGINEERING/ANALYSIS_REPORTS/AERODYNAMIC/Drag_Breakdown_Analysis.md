# Drag Breakdown Analysis

**Analysis ID:** 02-11-00-AERO-003  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Aerodynamic – Drag Accounting (Cruise)  
**Status:** Planned  
**Date:** 2025-11-10

---

## 0. Inputs and References

This drag breakdown uses the **frozen geometry baseline** and the **cruise CFD solution** as primary inputs.

- Geometry baseline:  
  `02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/01_OVERVIEW/baseline_dimensions.json`  
  - Aspect ratio (AR): from wing span and wing area  
  - Reference area S: wing area

- Cruise CFD analysis (once available):  
  `ANALYSIS_REPORTS/AERODYNAMIC/CFD_Cruise_Analysis.md`

- Calculation sheet (numerical drag build-up):  
  `CALCULATIONS/AERODYNAMIC/Drag_Breakdown_Calc.csv`

**Note:** Any change in the frozen geometry must follow the ECR process and will be detected by the Geometry Baseline Watchdog CI.

---

## 1. Objective

Provide a detailed drag breakdown at cruise conditions to:

- Account for all drag sources contributing to the aircraft drag coefficient.  
- Identify drag reduction opportunities by component and mechanism.  
- Support performance and mission analysis (range, fuel burn).  
- Validate semi-empirical estimates against **CFD** and later **wind tunnel** / flight test data.

---

## 2. Drag Components

### 2.1 Definition of Drag Count

A **drag count** is defined as:

\[
1 \text{ drag count} = 1 \times 10^{-4} \text{ in } C_D
\]

Values in the tables below are expressed as:

\[
\Delta C_D \times 10^{4}
\]

so that, for example, 20 counts = \( \Delta C_D = 0.0020 \).

### 2.2 Cruise Condition (M 0.82, 41,000 ft, CL = 0.52)

| Drag Component     | Drag Count (ΔCD × 10⁴) | Percentage | Method / Source                          |
|--------------------|------------------------|------------|------------------------------------------|
| **Induced drag**   | TBD                    | TBD %      | \( C_{D_i} = \dfrac{C_L^2}{\pi \, AR \, e} \) |
| **Friction drag**  | TBD                    | TBD %      | Flat-plate / wetted area method          |
| Wing               | TBD                    | TBD %      | Wetted area + Cf correlation             |
| Center body        | TBD                    | TBD %      | Wetted area + Cf correlation             |
| Nacelles           | TBD                    | TBD %      | Wetted area + Cf correlation             |
| Vertical tails     | TBD                    | TBD %      | Wetted area + Cf correlation             |
| **Form drag**      | TBD                    | TBD %      | Pressure drag (bluff / separated zones)  |
| **Wave drag**      | TBD                    | TBD %      | CFD transonic analysis / correlations    |
| **Interference**   | TBD                    | TBD %      | Component build-up / empirical factors   |
| Wing–body          | TBD                    | TBD %      | Junction interference factors            |
| Nacelle–wing       | TBD                    | TBD %      | Junction interference factors            |
| **Miscellaneous**  | TBD                    | TBD %      | Gaps, antennas, excrescences             |
| **Total cruise drag** | **TBD**            | **100%**   | Sum of all components                    |

---

## 3. Zero-Lift Drag (CD₀)

Zero-lift drag is defined as the sum of all non-induced contributions:

\[
C_{D_0} = C_{D,\text{friction}} + C_{D,\text{form}} +
          C_{D,\text{wave}} + C_{D,\text{interference}} +
          C_{D,\text{misc}}
\]

Numerical value (from `Drag_Breakdown_Calc.csv`):

\[
C_{D_0} = \text{TBD}
\]

---

## 4. Total Drag at Cruise

Total drag coefficient at the design cruise lift coefficient:

\[
C_{D,\text{total}} = C_{D_0} + C_{D_i}
\]

Where:

\[
C_{D_i} = \frac{C_L^2}{\pi \, AR \, e}
\]

- \( C_L = 0.52 \) (cruise)
- \( AR \) from `baseline_dimensions.json`
- \( e \) = Oswald efficiency factor (estimated from BWB correlations / CFD): TBD

**Target requirement:**

\[
C_{D,\text{total}} < 0.022 \quad \text{at } C_L = 0.52
\]

Compliance status: **TBD** (to be updated once CFD and build-up estimates are available).

---

## 5. L/D Ratio

Lift-to-drag ratio at cruise:

\[
\left( \frac{L}{D} \right)_\text{cruise} =
\frac{C_L}{C_{D,\text{total}}} = \text{TBD}
\]

**Target:** 

\[
\left( \frac{L}{D} \right)_\text{cruise} > 23
\]

---

## 6. Drag Polar

The drag polar used for performance and mission analysis is:

\[
C_D = C_{D_0} + K \, C_L^2
\]

Where:

- \( C_{D_0} \) = zero-lift drag coefficient (Section 3)
- \( K = \dfrac{1}{\pi \, e \, AR} \)

With:

- \( AR \) from `baseline_dimensions.json`
- \( e \) calibrated from CFD / lifting-line / BWB correlations

**Outputs to document:**

- \( C_{D_0} \) (number)  
- \( K \) (number)  
- Valid **CL range** for this polar (e.g. 0.3–0.7).

---

## 7. Sensitivity Analysis

Impact of selected design changes on cruise drag (at M 0.82, 41,000 ft, CL = 0.52):

| Parameter Change           | ΔCD (counts) | Impact Mechanism      | Comment                         |
|---------------------------|--------------|-----------------------|---------------------------------|
| +1° wing sweep            | TBD          | Wave / interference   | Affects shock strength/location |
| +10% wingspan (fixed S)   | TBD          | Induced drag ↓        | Higher AR, check structures     |
| +5% wetted area           | TBD          | Friction drag ↑       | Systems / fairings growth       |
| Laminar flow control (LFC)| TBD          | Friction drag ↓       | Define assumed laminar extent   |
| Nacelle shape optimization| TBD          | Form / interference ↓ | CFD-driven refinement           |

All sensitivity results should be traceable to individual runs or parametric sweeps logged in
`CALCULATIONS/AERODYNAMIC/Drag_Breakdown_Calc.csv` and corresponding CFD cases.

---

## 8. Validation and Traceability

**Cross-checks:**

- Compare **CD_total and component breakdown** against:  
  - `ANALYSIS_REPORTS/AERODYNAMIC/CFD_Cruise_Analysis.md`  
  - Future wind tunnel and flight test data (when available).

- Verify consistency with frozen geometry baseline:  
  - Aspect ratio and reference area must match `baseline_dimensions.json`.  
  - Any geometry change affecting AR or wetted area must follow the ECR process and will be caught by the Geometry Baseline Watchdog.

---

## 9. Data File Structure (Drag_Breakdown_Calc.csv)

Planned column structure:

- `Case_ID`  
- `Mach`  
- `Altitude_ft`  
- `CL`  
- `CD_total`  
- `CD0`  
- `CDi`  
- `CD_friction_wing`  
- `CD_friction_center_body`  
- `CD_friction_nacelles`  
- `CD_friction_vertical_tails`  
- `CD_form`  
- `CD_wave`  
- `CD_interference_wing_body`  
- `CD_interference_nacelle_wing`  
- `CD_misc`  
- `L_over_D`  
- `Source` (CFD / empirical / hybrid)  

This file acts as the **authoritative numerical reference** for the drag breakdown and should be kept in sync with this report.

---

## 10. References

- `ANALYSIS_REPORTS/AERODYNAMIC/CFD_Cruise_Analysis.md`  
- `CALCULATIONS/AERODYNAMIC/Drag_Breakdown_Calc.csv`  
- `04_DESIGN/AERODYNAMIC_DESIGN/Drag_Estimation.md`  
- `02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/01_OVERVIEW/baseline_dimensions.json`

---

**Document Control:**

- **Version:** 1.0 (Draft – Methodology Defined)  
- **Date:** 2025-11-10  
- **Traceability:** Linked to frozen geometry baseline and CFD cruise analysis.

