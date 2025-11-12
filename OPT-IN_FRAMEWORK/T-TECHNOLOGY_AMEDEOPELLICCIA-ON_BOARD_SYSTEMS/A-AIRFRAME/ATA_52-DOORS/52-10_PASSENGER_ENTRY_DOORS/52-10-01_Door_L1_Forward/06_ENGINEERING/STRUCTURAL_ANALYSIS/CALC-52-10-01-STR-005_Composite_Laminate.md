# Composite Laminate Analysis - Door L1 Forward

**Calculation:** CALC-52-10-01-STR-005  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Classical Laminate Theory (AI-Assisted)  
**Confidence:** ±35%

## 1. LAMINATE DEFINITION

### Layup Configuration
```
Material: M21E/IMA (Hexcel)
Ply thickness: 0.25 mm
Face sheet thickness: 4 mm = 16 plies
Layup: [45/0/-45/90]2s (quasi-isotropic)
```

## 2. PLY PROPERTIES (CMH-17)

### Unidirectional Properties (Room Temp, Dry)
```
E11 = 165 GPa (fiber direction)
E22 = 9.2 GPa (transverse)
G12 = 5.3 GPa (shear)
ν12 = 0.33
t_ply = 0.25 mm

Strengths (B-basis):
σ_11_tu = 2,860 MPa (tension)
σ_11_cu = 1,530 MPa (compression)
σ_22_tu = 62 MPa (transverse tension)
σ_22_cu = 228 MPa (transverse compression)
τ_12_u = 105 MPa (shear)
```

## 3. LAMINATE STIFFNESS (CLT)

### Quasi-Isotropic Approximation
```
For [45/0/-45/90]2s layup:

E_x ≈ E_y ≈ 65 GPa (in-plane modulus)
G_xy ≈ 24 GPa (in-plane shear)
ν_xy ≈ 0.30

Laminate thickness: 4 mm
```

### Membrane Stiffness [A]
```
A11 = A22 ≈ 260 kN/mm
A66 ≈ 96 kN/mm
A12 ≈ 78 kN/mm
```

### Bending Stiffness [D]
```
D11 = D22 ≈ 1,387 N⋅m (per unit width)
D66 ≈ 512 N⋅m
D12 ≈ 416 N⋅m
```

## 4. STRESS ANALYSIS

### Applied Loading (from STR-002)
```
Maximum face stress: 348 MPa
Predominantly bending load
```

### Ply-Level Stresses (Estimated)
```
For quasi-isotropic under uniform stress:
σ_ply ≈ σ_applied / efficiency

Efficiency factors (approximate):
- 0° plies: 1.2 (carry more load)
- 45° plies: 0.8
- 90° plies: 0.8

Maximum ply stress:
σ_0° ≈ 348 × 1.2 = 418 MPa
```

## 5. FAILURE ANALYSIS

### Tsai-Wu Failure Criterion
```
Simplified form for 0° plies under σ_11:
FI = σ_11 / σ_11_tu (tension)
FI = 418 / 2,860 = 0.15

Failure Index < 1.0 → Safe
```

### Margin of Safety
```
MS = (1.0 / FI) - 1
MS = (1.0 / 0.15) - 1 = +5.7
```

**Status:** High positive margin

### With Uncertainty (±35%)
```
Worst case FI: 0.15 × 1.35 = 0.20
MS_worst = (1.0 / 0.20) - 1 = +4.0
```

**Still safe with margin**

## 6. CRITICAL PLIES

### Most Critical
```
1. 0° plies (highest stress)
2. 90° plies (transverse loading)
3. ±45° plies (shear loading)
```

### Failure Modes to Check
```
- Fiber breakage (0° plies in tension)
- Matrix cracking (90° plies)
- Delamination (interlaminar shear)
- Fiber microbuckling (0° plies in compression)
```

## 7. ENVIRONMENTAL EFFECTS

### Hot-Wet Conditions (-55°C to +85°C, 85% RH)
```
Knockdown factors (from CMH-17):
- Modulus: 0.85 (15% reduction)
- Strength: 0.75 (25% reduction)

Hot-wet MS:
MS_hw = (2,860 × 0.75) / (418 × 1.35) - 1
MS_hw = +2.8
```

**Still acceptable**

## 8. VALIDATION REQUIRED

- [ ] Detailed CLT analysis with software
- [ ] Coupon testing per ASTM D3039
- [ ] Measure actual laminate properties
- [ ] Progressive failure analysis (FEA)
- [ ] Environmental testing

---

**Status:** Draft - HIGH UNCERTAINTY  
**Confidence:** LOW  
**Risk:** HIGH
