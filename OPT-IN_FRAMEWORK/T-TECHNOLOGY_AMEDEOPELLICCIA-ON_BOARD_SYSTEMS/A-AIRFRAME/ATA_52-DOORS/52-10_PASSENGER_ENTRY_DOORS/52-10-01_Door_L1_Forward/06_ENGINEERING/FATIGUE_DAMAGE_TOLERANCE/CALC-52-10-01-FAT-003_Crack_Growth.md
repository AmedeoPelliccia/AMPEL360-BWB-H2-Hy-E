# Crack Growth Analysis - Door Panel

**Calculation:** CALC-52-10-01-FAT-003  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Paris Law (AI-Assisted)  
**Confidence:** ±60% (Very Low)

## 1. DAMAGE TOLERANCE PHILOSOPHY

### CS-25.571 Requirements
```
- Assume manufacturing defect or in-service damage
- Demonstrate residual strength with damage
- Establish inspection intervals
- Prevent catastrophic failure
```

## 2. INITIAL FLAW ASSUMPTION

### Manufacturing Defect
```
Type: Delamination in CFRP face sheet
Size: a_0 = 2 mm (detectable limit)
Location: High stress region (panel center)
```

## 3. CRACK GROWTH MODEL

### Paris Law
```
da/dN = C × (ΔK)^m

For CFRP (Mode I):
C ≈ 1.0 × 10^-8 (m/cycle)(MPa√m)^-m
m ≈ 3.5
```

### Stress Intensity Factor
```
K = Y × σ × √(π × a)

Where:
Y = geometry factor ≈ 1.12 (surface crack)
σ = 348 MPa (operating stress)
a = crack half-length
```

## 4. CRACK GROWTH PREDICTION

### Initial Condition
```
a_0 = 2 mm
ΔK_0 = 1.12 × 348 × √(π × 0.002)
ΔK_0 ≈ 31 MPa√m
```

### Growth Rate
```
da/dN = 1.0E-8 × 31^3.5
da/dN ≈ 8.4 × 10^-6 m/cycle
da/dN ≈ 0.0084 mm/cycle
```

### Cycles to Critical Size
```
Critical size: a_c = 25 mm (1/45 of panel width)
Growth: 23 mm required

N = Δa / (da/dN_avg)
N ≈ 23 / 0.010 (average rate)
N ≈ 2,300 flights
```

**⚠️ WARNING:** Only 3.8% of design life!

## 5. INSPECTION INTERVAL

### Required Inspection
```
Detectable size: 10 mm (visual/NDI)
Inspection interval: N/4 = 575 flights
Recommended: 500 flights (conservative)
```

## 6. RESIDUAL STRENGTH

### With 25mm Damage
```
Net section stress:
σ_net = σ × (w / (w - 2a))
σ_net = 348 × (1120 / 1070)
σ_net ≈ 364 MPa

Allowable: 2,724 MPa
MS = (2724 / 364) - 1 = +6.5
```

**Adequate residual strength**

## 7. VALIDATION REQUIRED

- [ ] Fracture toughness testing (ASTM E399)
- [ ] Crack growth testing (ASTM E647)
- [ ] Full-scale damage tolerance test
- [ ] NDI capability demonstration
- [ ] DER approval of inspection program

---

**Status:** CRITICAL - Requires Testing  
**Risk:** HIGH - Short inspection interval
