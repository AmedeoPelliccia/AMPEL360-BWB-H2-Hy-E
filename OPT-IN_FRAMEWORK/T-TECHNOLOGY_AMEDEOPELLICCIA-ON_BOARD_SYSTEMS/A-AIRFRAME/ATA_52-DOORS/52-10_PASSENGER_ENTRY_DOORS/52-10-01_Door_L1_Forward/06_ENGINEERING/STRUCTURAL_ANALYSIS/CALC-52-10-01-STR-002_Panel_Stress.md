# Panel Stress Analysis - Door L1 Forward

**Calculation:** CALC-52-10-01-STR-002  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Plate Theory (AI-Assisted)  
**Confidence:** ±40%

## 1. PANEL GEOMETRY

### Dimensions
```
Length (a): 1,880 mm
Width (b): 1,120 mm
Aspect ratio: 1.68
```

### Sandwich Construction
```
Face sheets: 2 × 4 mm CFRP (M21E/IMA)
Core: 40 mm Nomex HRH-10-48
Total thickness: 48 mm
```

## 2. MATERIAL PROPERTIES

### CFRP Face Sheets (Quasi-Isotropic)
```
E_face = 65 GPa
σ_tu = 2,724 MPa (room temp dry, CMH-17 B-basis)
σ_cu = 1,816 MPa (compression)
ν = 0.3
ρ = 1,600 kg/m³
```

### Nomex Core
```
G_core = 35 MPa
σ_core_shear = 1.2 MPa
E_core = 80 MPa (perpendicular)
ρ = 48 kg/m³
```

## 3. PLATE THEORY ANALYSIS

### Boundary Conditions
- Assumed: Simply supported on all edges
- Reality: Elastic restraint at frame
- **Note:** Actual conditions between simply supported and clamped

### Maximum Bending Stress
```
Using Roark's formulas for rectangular plates:

For a/b = 1.68, uniform pressure q:
β ≈ 0.42 (interpolated coefficient)

σ_max = β × q × (b/t_eff)²

Where:
q = 117.2 kPa (ultimate pressure)
b = 1.12 m
t_eff = 48 mm (sandwich equivalent)

σ_max = 0.42 × 117.2 × (1120/48)²
σ_max ≈ 268 MPa (face stress)
```

### Maximum Deflection
```
α ≈ 0.062 (deflection coefficient)
D = E_face × t_face × d² (simplified)
d = 44 mm (face centroid separation)

w_max = α × q × b⁴ / D
w_max ≈ 15 mm
```

## 4. FACE SHEET STRESS

### Bending Stress Distribution
```
Top face (compression): σ = -268 MPa
Bottom face (tension): σ = +268 MPa
Neutral axis: σ = 0
```

### Combined with Membrane Stress
```
Membrane stress (if edges restrained):
σ_membrane ≈ 0.3 × σ_bending = 80 MPa

Total stress:
σ_total = σ_bending + σ_membrane
σ_total ≈ 348 MPa (conservative)
```

## 5. MARGIN OF SAFETY

### Tension Face
```
Allowable: 2,724 MPa
Applied: 348 MPa
MS = (2724/348) - 1 = +6.8
```

### Compression Face
```
Allowable: 1,816 MPa (compression strength)
Applied: 348 MPa
MS = (1816/348) - 1 = +4.2
```

### With Uncertainty (±40%)
```
Worst case applied: 348 × 1.4 = 487 MPa
MS_worst = (1816/487) - 1 = +2.7
```

**Status:** Positive margins even in worst case

## 6. DEFLECTION CHECK

```
Maximum allowable: 25 mm (h/75)
Predicted: 15 mm
Margin: (25/15) - 1 = +0.67
```

## 7. CRITICAL ASSUMPTIONS

1. Simply supported edges (conservative for stress)
2. Uniform pressure distribution
3. Quasi-isotropic CFRP properties
4. No impact of cutouts/windows
5. Room temperature properties

**⚠️ All assumptions require validation**

## 8. VALIDATION REQUIRED

- [ ] FEA with actual boundary conditions
- [ ] Pressure test with strain gauges at max stress location
- [ ] Deflection measurement (LVDT)
- [ ] Compare with actual support stiffness

## 9. NEXT STEPS

1. Refine with professional FEA
2. Account for cutouts and reinforcements
3. Check local stress concentrations
4. Verify face/core bond strength

---

**Status:** Draft - Requires Professional Validation  
**Confidence:** LOW  
**Risk Level:** MEDIUM
