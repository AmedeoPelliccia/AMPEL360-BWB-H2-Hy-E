# Thermal Expansion Analysis

**Calculation:** CALC-52-10-01-THM-002  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** CTE Analysis (AI-Assisted)  
**Confidence:** ±20%

## 1. COEFFICIENT OF THERMAL EXPANSION

### Materials
```
CFRP (quasi-iso): α = 1.0 × 10⁻⁶ /°C
Nomex core: α = 30 × 10⁻⁶ /°C
Titanium: α = 8.6 × 10⁻⁶ /°C
Aluminum frame: α = 23 × 10⁻⁶ /°C
```

## 2. THERMAL STRAIN

### Temperature Change
```
ΔT_max = 85°C (from -55°C to +30°C)
```

### Panel Expansion
```
CFRP face:
ε_thermal = α × ΔT
ε_thermal = 1.0E-6 × 85 = 85 × 10⁻⁶

ΔL = ε × L
ΔL_height = 85E-6 × 1,880 = 0.16 mm
ΔL_width = 85E-6 × 1,120 = 0.10 mm
```

**Negligible expansion**

### Core Expansion
```
Core α = 30E-6 /°C (much higher)
ΔL_core = 30E-6 × 85 × 40 = 0.10 mm (through thickness)
```

**Also small**

## 3. CTE MISMATCH STRESS

### Face/Core Interface
```
Strain mismatch:
Δε = (α_core - α_face) × ΔT
Δε = (30 - 1) × 10⁻⁶ × 85 = 2,465 × 10⁻⁶

If constrained:
σ_thermal = E × Δε
σ_thermal = 65,000 × 2.465E-3 = 160 MPa
```

**⚠️ Significant stress at interface**

### Mitigation
```
- Adhesive allows some slip (not fully constrained)
- Actual stress ~30% of calculated = 48 MPa
- Face/core bond strength: 2-3 MPa (shear)
- Margin adequate if distributed over area
```

## 4. ALUMINUM FRAME / CFRP PANEL

### Mismatch
```
Δα = α_Al - α_CFRP
Δα = 23E-6 - 1E-6 = 22E-6 /°C

Over 1,880 mm:
ΔL_difference = 22E-6 × 85 × 1,880 = 3.5 mm
```

### Design Solution
```
- Floating attachments (allow slip)
- Compliance in hinges
- Gaps at corners
- Flexible seals accommodate movement
```

## 5. SEAL COMPRESSION

### Cold Condition
```
Panel shrinks: 0.2 mm
Seal compresses more: +0.2 mm
New compression: 3.2 mm (vs. 3.0 nominal)
Status: Acceptable
```

### Hot Condition
```
Panel expands: +0.2 mm
Seal relaxes: -0.2 mm
New compression: 2.6 mm (vs. 3.0 nominal)
Status: Verify leak rate
```

## 6. VALIDATION REQUIRED

- [ ] Thermal chamber testing with gap measurements
- [ ] Verify seal performance at extremes
- [ ] Check for buckling or distortion
- [ ] Measure thermal stresses (strain gauges)

---

**Status:** Draft - Testing Required  
**Confidence:** MEDIUM  
**Risk:** MEDIUM
