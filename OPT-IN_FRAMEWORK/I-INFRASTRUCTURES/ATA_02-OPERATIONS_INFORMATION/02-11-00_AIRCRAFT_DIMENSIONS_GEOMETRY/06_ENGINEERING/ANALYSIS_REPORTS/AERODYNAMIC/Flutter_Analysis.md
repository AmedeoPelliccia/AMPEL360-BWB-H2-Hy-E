# Flutter Analysis

**Analysis ID:** 02-11-00-AERO-005  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Aeroelastic - Flutter Stability  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Demonstrate freedom from flutter, divergence, and control reversal per CS-25.629:
- Flutter speed VF ≥ 1.2 × VD (design dive speed)
- No unstable aeroelastic phenomena within flight envelope
- Adequate damping margins throughout operational range

---

## 2. Requirements (CS-25.629)

### 2.1 Speed Range
- **VD (design dive speed):** 1.25 × VC = TBD KEAS
- **Required flutter margin:** VF ≥ 1.2 × VD
- **Minimum flutter speed:** VF ≥ TBD KEAS

### 2.2 Mass and Stiffness Range
Analysis must cover:
- Minimum to maximum operational weight
- Forward to aft CG range
- Fuel distribution extremes (H₂ tank fill states)

---

## 3. Analysis Methodology

### 3.1 Structural Model
- **FEM:** Global structural model (from MSC Nastran)
- **Modes:** First 50 normal modes (up to 20 Hz)
- **Mass representation:** Concentrated masses for fuel, payload, systems

### 3.2 Aerodynamic Model
- **Method:** Doublet Lattice Method (subsonic) or lifting surface theory
- **Panels:** 500+ aerodynamic panels on lifting surfaces
- **Mach numbers:** 0.0 to 0.85 (cruise + margin)

### 3.3 Flutter Solution
- **Method:** p-k method (complex eigenvalue)
- **Software:** MSC Nastran SOL 145 or ZAERO
- **Output:** V-g-f diagrams (velocity-damping-frequency)

---

## 4. Critical Modes

### 4.1 Wing Modes
- **1st bending:** f ≈ TBD Hz
- **1st torsion:** f ≈ TBD Hz
- **2nd bending:** f ≈ TBD Hz
- **Aileron rotation:** f ≈ TBD Hz

### 4.2 Center Body Modes
- **1st bending (vertical):** f ≈ TBD Hz
- **1st torsion:** f ≈ TBD Hz

---

## 5. Flutter Results

### 5.1 V-g Diagram
Plot of damping (g) vs. airspeed (V) for critical modes.

**Requirement:** g > 0.03 (positive damping) for all speeds up to VF.

### 5.2 Flutter Speed Summary

| Configuration | Flutter Speed VF (KEAS) | VD (KEAS) | 1.2×VD (KEAS) | Margin | Status |
|---------------|-------------------------|-----------|---------------|--------|--------|
| Cruise, full fuel | TBD | TBD | TBD | TBD | Pending |
| Cruise, empty fuel | TBD | TBD | TBD | TBD | Pending |
| Max weight, fwd CG | TBD | TBD | TBD | TBD | Pending |
| Min weight, aft CG | TBD | TBD | TBD | TBD | Pending |

---

## 6. Sensitivity Analysis

Impact of design changes on flutter speed:

| Parameter | Effect on Flutter Speed |
|-----------|-------------------------|
| +10% wing stiffness | VF increases (favorable) |
| +5% wing mass | VF decreases (unfavorable) |
| Aft CG shift | May reduce flutter margin |
| Engine mass increase | Affects wing bending-torsion coupling |

---

## 7. Ground Vibration Test (GVT)

Before first flight, a GVT must be conducted to:
- Measure actual structural frequencies and mode shapes
- Validate FEM predictions
- Update flutter analysis with measured data

---

## 8. Flight Flutter Test

Per CS-25.629, flight flutter testing required to:
- Demonstrate freedom from flutter up to VD
- Use excitation system (e.g., vane or inertial shaker)
- Monitor structural response and damping

---

## 9. References

- CS-25.629 – Aeroelastic Stability Requirements
- MSC Nastran Aeroelastic Analysis User's Guide
- ZAERO User's Manual
- `ANALYSIS_REPORTS/STRUCTURAL/FEM_Global_Model.md`
- `04_DESIGN/STRUCTURAL_DESIGN/Wing_Box_Design.md`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
