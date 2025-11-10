# Flutter Analysis

**Analysis ID:** 02-11-00-AERO-005  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Aeroelastic – Flutter Stability  
**Status:** Planned – Methodology Defined  
**Date:** 2025-11-10

---

## 0. Scope and Inputs

This document defines the methodology and reporting structure for the flutter analysis of the AMPEL360 BWB H₂ Hy-E Q100 configuration.

The analysis is based on:

- **Global FEM model**  
  `ANALYSIS_REPORTS/STRUCTURAL/FEM_Global_Model.md`
- **Frozen geometry baseline**  
  `02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/01_OVERVIEW/baseline_dimensions.json`
- **Design speeds and flight envelope**  
  (from performance / certification requirements – TBD)

Any geometry or stiffness changes affecting the aeroelastic model must follow the ECR process and remain consistent with the frozen geometry baseline.

---

## 1. Objective

Demonstrate freedom from aeroelastic instabilities (flutter, divergence, and control reversal) in accordance with **CS-25.629**, by showing that:

- Flutter speed \( V_F \) satisfies:
  \[
  V_F \ge 1.2 \times V_D
  \]
- No unstable aeroelastic phenomena occur within or below the operational flight envelope.  
- Adequate damping margins are maintained for all relevant modes, mass configurations, and Mach numbers.

---

## 2. Certification Requirements (CS-25.629)

### 2.1 Speed Range

- **Design dive speed:**  
  \[
  V_D = 1.25 \times V_C = \text{TBD KEAS}
  \]
- **Required flutter margin:**  
  \[
  V_F \ge 1.2 \times V_D
  \]
- **Minimum acceptable flutter speed:**  
  \[
  V_F \ge \text{TBD KEAS}
  \]

Analysis will cover:

- From low subsonic speeds up to at least \( 1.2 \times V_D \)  
- Relevant Mach numbers: **M = 0.0 to 0.85** (ground to dive)

### 2.2 Mass and Stiffness Range

The flutter analysis must envelope realistic **mass and stiffness** ranges, including:

- Minimum to maximum operational weight  
- Forward to aft **CG envelope**  
- Hydrogen tank fill states:
  - Full tanks
  - Reserve/final-approach configuration
  - Minimum fuel (structurally critical)

For each mass case, updated mass matrices and mode shapes will be generated from the global FEM and imported into the aeroelastic solver.

---

## 3. Analysis Methodology

### 3.1 Structural Model

- **Tool:** MSC Nastran (or equivalent)  
- **Model:** Global airframe FEM, including:
  - Wing / center body / vertical surfaces
  - Engine / nacelle mounts
  - Control surfaces (aileron/spoiler/elevon surfaces as applicable)
- **Normal modes:** First **~50 modes** (target frequency range: 0–20 Hz, TBD)  
- **Mass representation:**
  - Structural mass from FEM
  - Concentrated masses for:
    - Fuel (H₂ tanks, distribution by tank location)
    - Payload and cabin interior
    - Systems / equipment / engines

Modal assurance checks (MAC) will be performed to confirm mode tracking between configurations.

### 3.2 Aerodynamic Model

- **Method:** Doublet Lattice Method (DLM) or equivalent lifting surface theory  
- **Mach numbers:** Discrete set from **M = 0.0 to 0.85**  
- **Aerodynamic panels:**
  - 500+ panels over lifting surfaces (wing + center body + verticals)
  - Adequate refinement near control surfaces and tips
- **Unsteady aerodynamics:**  
  Frequency-dependent generalized aerodynamic forces (GAF) generated over log-spaced reduced frequency range.

### 3.3 Coupled Aeroelastic Model

- Structural and aerodynamic models will be **matched** through:
  - Structural grid ↔ aerodynamic lattice mapping  
  - Control surface definitions (hinge lines, deflection DOFs)
- Reduced-order aeroelastic model derived for:
  - Each Mach number
  - Each mass / CG / fuel configuration

### 3.4 Flutter Solution

- **Solution method:** p–k method (complex eigenvalue analysis)  
- **Software:** MSC Nastran **SOL 145** and/or ZAERO (TBD)  
- **Outputs:**
  - Damping vs. airspeed (V–g diagrams)
  - Frequency vs. airspeed (V–f diagrams)
  - Mode shapes at critical speeds

Convergence criteria for p–k solutions (e.g. tolerance on eigenvalues and iteration count) will be documented.

---

## 4. Flight Conditions and Configurations

### 4.1 Flight Condition Grid (Planned)

For each configuration, speeds will be analyzed from low speed up to and beyond **VD**:

| Mach | Altitude (ft) | V (KEAS) Range      | Notes                              |
|------|---------------|---------------------|------------------------------------|
| 0.3  | TBD           | Low to VD           | Low-altitude check (if applicable) |
| 0.6  | TBD           | Low to VD           | Mid-subsonic                       |
| 0.82 | 41,000        | Cruise to 1.2×VD    | Cruise & high-speed envelope       |
| 0.85 | TBD           | Up to 1.2×VD (TBD)  | Margin beyond cruise Mach          |

### 4.2 Mass / CG Configurations

Configurations to be analyzed:

- **Cruise, full fuel** (mid-mission weight, nominal CG)  
- **Cruise, empty/low fuel** (lighter weight, CG shift)  
- **Maximum weight, forward CG** (worst-case stiffness + inertia)  
- **Minimum weight, aft CG** (reduced stiffness margin, less damping)  

Additional configurations may be added if sensitivity indicates critical trends.

---

## 5. Critical Modes

### 5.1 Wings and Control Surfaces

Key modes to be monitored for flutter onset:

- **1st wing bending:** \( f \approx \text{TBD Hz} \)  
- **1st wing torsion:** \( f \approx \text{TBD Hz} \)  
- **2nd wing bending:** \( f \approx \text{TBD Hz} \)  
- **Aileron / elevon rotation:** \( f \approx \text{TBD Hz} \)

### 5.2 Center Body and Global Modes

- **1st center body bending (vertical):** \( f \approx \text{TBD Hz} \)  
- **1st center body torsion:** \( f \approx \text{TBD Hz} \)  
- **Symmetric / anti-symmetric global modes** potentially interacting with control surfaces.

### 5.3 Mode Tracking Table (Template)

| Mode ID | Description           | Frequency (Hz) | Dominant Region      | Notes / Coupling Risk        |
|--------|------------------------|----------------|----------------------|------------------------------|
| TBD    | 1st wing bending       | TBD            | Wing                 | Candidate for bending–torsion|
| TBD    | 1st wing torsion       | TBD            | Wing                 | High torsional energy        |
| TBD    | Center body bending    | TBD            | Center body          | BWB-specific global mode     |
| TBD    | Aileron / elevon mode  | TBD            | Control surface      | Possible control flutter     |

---

## 6. Flutter Results (Planned Outputs)

### 6.1 V–g and V–f Diagrams

For each configuration and Mach number, the following will be produced:

- **V–g diagrams:** Damping coefficient g vs. airspeed V  
  - **Requirement:**  
    \[
    g > 0.03 \quad \text{(positive damping)} \quad \forall V \le V_F
    \]
- **V–f diagrams:** Frequency vs. airspeed for critical modes  
  - Used to identify mode coalescence and crossing.

### 6.2 Flutter Speed Summary

| Configuration        | Flutter Speed VF (KEAS) | VD (KEAS) | 1.2×VD (KEAS) | Margin (VF / VD) | Status  |
|----------------------|-------------------------|-----------|---------------|------------------|---------|
| Cruise, full fuel    | TBD                     | TBD       | TBD           | TBD              | Pending |
| Cruise, empty fuel   | TBD                     | TBD       | TBD           | TBD              | Pending |
| Max weight, fwd CG   | TBD                     | TBD       | TBD           | TBD              | Pending |
| Min weight, aft CG   | TBD                     | TBD       | TBD           | TBD              | Pending |

**Acceptance:** For each configuration,  

\[
V_F \ge 1.2 \times V_D \quad \text{and} \quad g > 0 \text{ at } V \le V_F
\]

### 6.3 Divergence and Control Reversal

In addition to classical flutter:

- **Divergence:** Check for static divergence (zero damping, zero frequency trend with increasing V).  
- **Control reversal:** Evaluate control surface effectiveness vs. speed to ensure:
  - No sign change of control derivative (e.g. \( \partial M / \partial \delta \)) within flight envelope.  

Any observed trends must be documented with plots and corrective design actions if necessary.

---

## 7. Sensitivity Analysis

Impact of design and parameter changes on flutter speed and margins:

| Parameter Change     | Effect on Flutter Speed | Qualitative Impact          |
|----------------------|-------------------------|-----------------------------|
| +10% wing stiffness  | VF increases (favorable)| Higher structural frequency |
| +5% wing mass        | VF decreases (unfavorable) | More inertia, lower freq  |
| Aft CG shift         | May reduce flutter margin | Changes mode coupling     |
| Engine mass increase | Alters wing bending–torsion coupling | Check nacelle / pylon modes |

Where required, **what-if** FEM variants will be generated (stiffness/mass scaling) to study trends and guide structural modifications.

---

## 8. Ground Vibration Test (GVT)

Prior to first flight:

- Perform **GVT** to measure:
  - Natural frequencies
  - Damping ratios
  - Mode shapes for relevant modes
- Update FEM:
  - Calibrate model to GVT results (frequency + MAC-based correlation)
  - Re-run flutter analysis with **GVT-correlated** FEM

GVT planning will include excitation and sensor layouts that adequately capture key BWB modes (global bending/torsion and control surface motion).

---

## 9. Flight Flutter Test

Per **CS-25.629**, flight flutter testing shall:

- Demonstrate freedom from flutter up to at least **VD** (with margin)  
- Use appropriate excitation:
  - Aeroelastic vane, rotating mass, or inertial shaker  
- Monitor in real time:
  - Structural response (accelerometers, strain gauges)
  - Modal damping trends

Test points will be expanded gradually (build-up approach), with predefined abort criteria based on damping and response levels.

---

## 10. References

- CS-25.629 – Aeroelastic Stability Requirements  
- MSC Nastran Aeroelastic Analysis User's Guide  
- ZAERO User's Manual (if used)  
- `ANALYSIS_REPORTS/STRUCTURAL/FEM_Global_Model.md`  
- `04_DESIGN/STRUCTURAL_DESIGN/Wing_Box_Design.md`

---

**Document Control:**

- **Version:** 1.0 (Draft – Methodology Defined)  
- **Date:** 2025-11-10  
- **Owner:** Aeroelasticity / Loads & Dynamics Team  
- **Traceability:** Linked to global FEM and frozen geometry baseline.

