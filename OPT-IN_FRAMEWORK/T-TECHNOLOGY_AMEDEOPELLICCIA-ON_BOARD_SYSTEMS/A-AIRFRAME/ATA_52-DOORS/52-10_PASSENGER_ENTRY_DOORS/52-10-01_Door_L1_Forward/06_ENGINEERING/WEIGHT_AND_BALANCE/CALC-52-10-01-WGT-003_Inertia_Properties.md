# Inertia Properties - Door L1 Forward

**Calculation:** CALC-52-10-01-WGT-003  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** MOI Calculation (AI-Assisted)  
**Confidence:** ±20%

## 1. MOMENTS OF INERTIA

### Definition
```
I_xx = Σm_i(y_i² + z_i²)  # About x-axis
I_yy = Σm_i(x_i² + z_i²)  # About y-axis
I_zz = Σm_i(x_i² + y_i²)  # About z-axis
```

## 2. PANEL INERTIA (Simplified)

### Approximation as Thin Plate
```
Mass: 72 kg
Dimensions: 1.88m × 1.12m

I_xx = (1/12) × m × b² = (1/12) × 72 × 1.12² = 7.5 kg⋅m²
I_yy = (1/12) × m × a² = (1/12) × 72 × 1.88² = 21.2 kg⋅m²
I_zz = I_xx + I_yy = 28.7 kg⋅m²
```

## 3. TOTAL DOOR INERTIA

### About Door CG
```
Panel contribution: As above
Frame contribution: +15% (estimated)

I_xx ≈ 8.6 kg⋅m²
I_yy ≈ 24.4 kg⋅m²
I_zz ≈ 33.0 kg⋅m²
```

## 4. PRODUCT OF INERTIA

### Symmetric Door
```
I_xy = I_xz = I_yz ≈ 0
(Due to symmetry)
```

## 5. APPLICATION

### Door Swing Dynamics
```
Angular acceleration during emergency opening:
τ = I_yy × α

For 90° rotation in 2 seconds:
α = π/2 rad / 1 s² = 1.57 rad/s²
τ = 24.4 × 1.57 = 38.3 N⋅m
```

## 6. VALIDATION REQUIRED

- [ ] CAD model for accurate MOI
- [ ] Physical measurement (bifilar/trifilar)
- [ ] Verify with prototype hardware

---

**Status:** Preliminary - Low Confidence  
**Use:** Preliminary dynamics only
