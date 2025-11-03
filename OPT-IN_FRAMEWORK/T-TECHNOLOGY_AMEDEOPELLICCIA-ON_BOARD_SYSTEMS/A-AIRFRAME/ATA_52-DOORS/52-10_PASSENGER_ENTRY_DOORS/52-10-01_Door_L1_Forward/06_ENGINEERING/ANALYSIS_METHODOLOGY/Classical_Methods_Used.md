# Classical Engineering Methods Used

**Document:** AMPEL360-52-10-01-ENG-METHODS  
**Date:** 2025-11-03

## Overview

This document catalogs all classical engineering methods and formulas used in the Door L1 Forward engineering analysis.

## STRUCTURAL ANALYSIS METHODS

### 1. Plate Theory (Thin Plates)
**Application:** Panel stress analysis  
**Reference:** Timoshenko, "Theory of Plates and Shells"

**Key Equations:**
```
Maximum stress in rectangular plate under uniform load:
σ_max = β × q × (a/t)²

Maximum deflection:
w_max = α × q × a⁴ / (E × t³)

Where:
- β, α = plate coefficients (depend on boundary conditions and aspect ratio)
- q = uniform pressure load
- a = characteristic dimension
- t = plate thickness
- E = elastic modulus
```

**Coefficients Used:**
- Simply supported: β ≈ 0.287, α ≈ 0.0443
- Clamped edges: β ≈ 0.513, α ≈ 0.0138
- **Note:** Actual boundary conditions are between these limits

### 2. Sandwich Panel Theory
**Application:** Composite door panel analysis  
**Reference:** Allen, "Analysis and Design of Structural Sandwich Panels"

**Key Equations:**
```
Flexural rigidity:
D = E_f × t_f × d² + (E_f × t_f³) / 6

Core shear stress:
τ_core = V / (b × t_c)

Face stress:
σ_face = M × d / (2 × D)

Where:
- E_f = face sheet modulus
- t_f = face sheet thickness
- d = distance between face centroids
- t_c = core thickness
- V = shear force
- M = bending moment
```

### 3. Composite Laminate Theory (CLT)
**Application:** CFRP face sheet analysis  
**Reference:** CMH-17 Composite Materials Handbook

**Approach:**
- Classical Laminated Plate Theory
- ABD matrix formulation
- First ply failure analysis
- Progressive failure analysis (simplified)

**Limitations:**
- AI cannot perform detailed ply-by-ply analysis
- Assumes quasi-isotropic layup approximations
- Interlaminar stresses estimated only

### 4. Static Equilibrium
**Application:** Hinge and latch load distribution  
**Reference:** Beer & Johnston, "Mechanics of Materials"

**Method:**
```
ΣF_x = 0
ΣF_y = 0
ΣF_z = 0
ΣM_x = 0
ΣM_y = 0
ΣM_z = 0
```

**Applied to:**
- Pressure distribution across door
- Load transfer to hinges
- Latch reaction forces
- Frame interface loads

## DYNAMIC ANALYSIS METHODS

### 5. Rayleigh-Ritz Method
**Application:** Natural frequency estimation  
**Reference:** Meirovitch, "Analytical Methods in Vibrations"

**Key Equations:**
```
First natural frequency:
f₁ = (1/2π) × √(k_eff / m_eff)

For beam/plate:
f₁ = (λ₁² / 2π) × √(EI / (m × L⁴))

Where:
- λ₁ = mode shape coefficient
- EI = bending stiffness
- m = mass per unit length
- L = characteristic length
```

**Assumptions:**
- Simplified mode shapes (sine waves, polynomials)
- Neglects rotary inertia
- Uncertainty ±30%

### 6. Modal Superposition (Simplified)
**Application:** Multi-mode frequency prediction  
**Note:** Very approximate without FEA

## FATIGUE & DAMAGE TOLERANCE METHODS

### 7. S-N Curve Approach
**Application:** Fatigue life prediction  
**Reference:** MIL-HDBK-5, CMH-17

**Key Equations:**
```
Basquin's Law:
N = C × σ^(-b)

Miner's Rule (cumulative damage):
D = Σ(n_i / N_i)

Where:
- N = cycles to failure
- σ = stress amplitude
- C, b = material constants
- n_i = cycles at stress level i
- N_i = cycles to failure at stress level i
```

**Limitations:**
- Does not account for load sequence effects
- Scatter in data (factor of 3-10 typical)
- Environmental effects not included

### 8. Paris Law (Crack Growth)
**Application:** Damage tolerance analysis  
**Reference:** ASTM E647

**Key Equations:**
```
da/dN = C × (ΔK)^m

Where:
- da/dN = crack growth rate
- ΔK = stress intensity factor range
- C, m = material constants

Stress intensity factor:
K = Y × σ × √(π × a)
```

**Limitations:**
- Requires material test data
- Geometry factors (Y) are approximate
- Does not include crack closure effects

## WEIGHT & BALANCE METHODS

### 9. Mass Properties Calculation
**Application:** Weight estimation and CG location

**Method:**
```
Total mass:
m_total = Σ(ρ_i × V_i)

Center of gravity:
x_cg = Σ(m_i × x_i) / m_total

Moment of inertia:
I_xx = Σ(m_i × (y_i² + z_i²))
```

**Accuracy:** ±10% for preliminary design

## THERMAL ANALYSIS METHODS

### 10. Thermal Expansion
**Application:** Temperature-induced strain and stress

**Key Equations:**
```
Thermal strain:
ε_thermal = α × ΔT

Thermal stress (constrained):
σ_thermal = E × α × ΔT

Where:
- α = coefficient of thermal expansion
- ΔT = temperature change
- E = elastic modulus
```

### 11. Heat Transfer (Simplified)
**Application:** Temperature distribution estimation

**Note:** Detailed thermal analysis requires FEM

## MECHANISM ANALYSIS METHODS

### 12. Kinematics
**Application:** Door motion and clearances

**Method:**
- Vector loop analysis
- Geometric constraints
- CAD-based visualization recommended

### 13. Force Analysis
**Application:** Actuation requirements

**Method:**
```
F_actuator = F_pressure + F_friction + F_seal + F_inertia

Torque requirements:
T = F × r × η

Where:
- η = mechanical efficiency
- r = moment arm
```

## REFERENCES

### Primary Engineering Handbooks
1. Roark's Formulas for Stress and Strain (8th Ed.)
2. Timoshenko & Woinowsky-Krieger, "Theory of Plates and Shells"
3. Allen, "Analysis and Design of Structural Sandwich Panels"
4. CMH-17, "Composite Materials Handbook"
5. Bruhn, "Analysis and Design of Flight Vehicle Structures"
6. Niu, "Airframe Structural Design"

### Standards Referenced
1. CS-25 (EASA Certification Specifications)
2. FAR Part 25 (FAA Regulations)
3. ASTM E647 (Crack Growth Testing)
4. ASTM D3039 (Composite Tension Testing)
5. ATA iSpec 2200 (Documentation Standards)

### Material Data Sources
1. CMH-17 (Composites)
2. MMPDS (Metallic Materials)
3. Manufacturer data sheets (Hexcel, Cytec)

## LIMITATIONS SUMMARY

**What AI Can Do:**
- Apply classical formulas correctly
- Perform basic calculations
- Identify relevant methods
- Document assumptions

**What AI Cannot Do:**
- Replace FEA for complex geometry
- Account for all real-world effects
- Optimize designs
- Make final engineering decisions
- Guarantee accuracy

**Bottom Line:** Use AI for preliminary estimates only. Always validate with professional tools and testing.

---

*All methods documented for transparency and traceability.*
