# Core Shear Analysis - Door L1 Forward

**Calculation:** CALC-52-10-01-STR-006  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Sandwich Panel Theory (AI-Assisted)  
**Confidence:** ±30%

## 1. CORE PROPERTIES

### Nomex HRH-10-48
```
Core type: Aramid fiber honeycomb
Density: 48 kg/m³
Cell size: 6.4 mm (1/4 inch)
Thickness: 40 mm

Mechanical Properties:
G_LW = 35 MPa (shear modulus, L direction)
G_WL = 35 MPa (shear modulus, W direction)
τ_ultimate = 1.2 MPa (shear strength)
σ_compression = 1.5 MPa (flatwise compression)
```

## 2. SHEAR LOAD CALCULATION

### From Panel Bending
```
Maximum shear force (edge):
V_max = q × b / 2
V_max = 117.2 kPa × 1.12 m / 2
V_max = 65.6 kN per meter of width
```

### Core Shear Stress
```
τ_core = V / (b × t_core)
τ_core = 65.6 kN/m / (1 m × 0.040 m)
τ_core = 1,640 kPa = 1.64 MPa
```

**⚠️ WARNING:** Exceeds ultimate strength!

## 3. MARGIN OF SAFETY

```
Allowable: 1.2 MPa
Applied: 1.64 MPa
MS = (1.2 / 1.64) - 1 = -0.27
```

**Status:** NEGATIVE MARGIN - REDESIGN REQUIRED

## 4. DESIGN OPTIONS

### Option 1: Increase Core Density
```
Use HRH-10-64 (64 kg/m³):
τ_ultimate = 1.8 MPa
MS = (1.8 / 1.64) - 1 = +0.10
```

### Option 2: Local Reinforcement
```
Add doublers at high shear regions
Reduce effective shear by 30%
τ_reduced = 1.64 × 0.7 = 1.15 MPa
MS = (1.2 / 1.15) - 1 = +0.04
```

### Option 3: Thicker Core
```
Increase to 50 mm:
τ_core = 65.6 / 0.050 = 1.31 MPa
MS = (1.2 / 1.31) - 1 = -0.08
Still negative - not sufficient alone
```

## 5. RECOMMENDED ACTION

**Increase core density to HRH-10-64**

## 6. VALIDATION REQUIRED

- [ ] FEA for accurate shear distribution
- [ ] Core manufacturer data sheet
- [ ] Shear testing per ASTM C273
- [ ] Verify face/core bond strength

---

**Status:** CRITICAL - REDESIGN NEEDED  
**Action:** Change core specification
