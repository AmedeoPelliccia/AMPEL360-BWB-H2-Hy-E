# Pressure Load Analysis - Door L1 Forward

**Calculation:** CALC-52-10-01-STR-001  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Classical Mechanics (AI-Assisted)  
**Confidence:** ±30%

## 1. LOAD DEFINITION

### Operating Conditions
- Cabin pressure: 8.5 psi (58.6 kPa)
- External pressure: 0 psi (altitude)
- Temperature: -55°C to +45°C

### Design Loads (CS-25.365)
- Limit pressure: 8.5 psi
- Proof pressure: 12.75 psi (1.5 × limit)
- Ultimate pressure: 17.0 psi (2.0 × limit)

## 2. PRESSURE DISTRIBUTION

### Door Geometry
```
Width (w) = 1,120 mm
Height (h) = 1,880 mm
Area (A) = 2.106 m²
```

### Total Force Calculation
```
Ultimate pressure: P = 17.0 psi = 117.2 kPa

Total force: F = P × A
F = 117.2 kPa × 2.106 m²
F = 247 kN
```

## 3. LOAD DISTRIBUTION

### Latch Loads (8 latches)
```
Force per latch = F_total / n_latches × K_distribution
F_latch = 247 kN / 8 × 1.15 (non-uniform factor)
F_latch = 35.5 kN per latch (max)
```

### Hinge Reactions (3 hinges)
```
Moment about hinge line:
M = P × A × (w/2)
M = 247 kN × 0.56 m
M = 138 kN⋅m

Reaction per hinge:
R_hinge = M / (3 × hinge_spacing)
R_hinge ≈ 46 kN (vertical component)
```

## 4. STRESS ESTIMATION (AI-BASED)

### Panel Bending Stress
Using plate theory (simply supported):
```
σ_max = K × P × (a/t)²

Where:
K ≈ 0.75 (plate coefficient, estimated)
a = 1,120 mm (short span)
t_eff = 48 mm (sandwich thickness)

σ_max ≈ 0.75 × 0.117 × (1120/48)²
σ_max ≈ 478 MPa
```

**⚠️ WARNING:** This is a simplified estimate with ±40% uncertainty

## 5. MARGINS OF SAFETY (PRELIMINARY)

```
Material allowable (CFRP): 2,724 MPa
Applied stress (estimated): 478 MPa

MS = (Allowable/Applied) - 1
MS = (2724/478) - 1 = +4.7

With ±40% uncertainty:
Worst case: MS = +2.0 (still positive)
```

## 6. VALIDATION REQUIRED

- [ ] FEA with proper boundary conditions
- [ ] Pressure test to ultimate
- [ ] Strain gauge validation
- [ ] Update calculations based on test

---

**Status:** Draft - Requires Professional Validation  
**Next Action:** FEA Analysis
