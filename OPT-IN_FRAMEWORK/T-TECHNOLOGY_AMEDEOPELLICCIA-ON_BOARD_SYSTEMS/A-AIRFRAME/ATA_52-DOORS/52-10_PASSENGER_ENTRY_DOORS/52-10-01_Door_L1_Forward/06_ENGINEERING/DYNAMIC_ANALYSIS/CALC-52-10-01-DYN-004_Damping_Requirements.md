# Damping Requirements - Door Panel

**Calculation:** CALC-52-10-01-DYN-004  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Vibration Theory (AI-Assisted)  
**Confidence:** ±40%

## 1. DAMPING FUNDAMENTALS

### Definition
```
ζ = Damping ratio (fraction of critical damping)
ζ_critical = 2√(km)
```

### Typical Values
```
Bare CFRP sandwich: ζ = 0.01-0.02 (1-2%)
With adhesive: ζ = 0.015-0.025
With CLD: ζ = 0.03-0.06 (3-6%)
```

## 2. REQUIRED DAMPING

### For Resonance Mitigation
```
If f_structure ≈ f_excitation:
  Minimum ζ_req = 0.05 (5%)
  
If margin > 20%:
  Minimum ζ_req = 0.02 (2%)
```

## 3. DAMPING SOURCES

### Material Damping
```
CFRP: ζ_material ≈ 0.008
Nomex core: ζ_core ≈ 0.015
Adhesive: ζ_adhesive ≈ 0.010

Combined (estimated):
ζ_total ≈ 0.020 (2%)
```

**Insufficient for resonance case**

## 4. DAMPING ENHANCEMENT

### Constrained Layer Damping (CLD)
```
Viscoelastic layer: 2 mm 3M ISD112
Constraint layer: 0.5 mm aluminum
Location: Inner face (cabin side)
Coverage: 70% of panel area

Expected result: ζ ≈ 0.045 (4.5%)
```

### Free Layer Damping (FLD)
```
Self-adhesive damping tape
Thickness: 3 mm
Coverage: 50% of panel

Expected result: ζ ≈ 0.030 (3%)
Less effective than CLD
```

## 5. VALIDATION METHOD

### GVT Measurement
```
Method: Half-power bandwidth
Procedure:
  1. Identify resonant peak
  2. Find f_1 and f_2 at -3 dB
  3. Calculate: ζ = (f_2 - f_1) / (2 × f_n)
```

### Acceptance Criteria
```
Mode 1 damping: ζ > 0.03 (3%)
If ζ < 0.03: Add damping treatment
```

## 6. VALIDATION REQUIRED

- [ ] GVT to measure actual damping
- [ ] If low, implement CLD
- [ ] Retest to verify improvement

---

**Status:** Draft  
**Action:** Measure in GVT
