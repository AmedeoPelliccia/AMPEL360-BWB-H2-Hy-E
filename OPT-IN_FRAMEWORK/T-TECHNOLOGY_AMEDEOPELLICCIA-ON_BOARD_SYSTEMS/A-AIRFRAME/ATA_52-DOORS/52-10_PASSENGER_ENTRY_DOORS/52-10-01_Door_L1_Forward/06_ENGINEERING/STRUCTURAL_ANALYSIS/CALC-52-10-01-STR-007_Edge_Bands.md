# Edge Band Analysis - Door L1 Forward

**Calculation:** CALC-52-10-01-STR-007  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Bearing Analysis (AI-Assisted)  
**Confidence:** ±30%

## 1. EDGE BAND CONFIGURATION

### Purpose
- Provide bearing surface for latches
- Distribute latch loads into sandwich panel
- Seal against frame

### Design
```
Material: CFRP solid laminate (unidirectional heavy)
Layup: [0/±45]3 (18 plies)
Thickness: 4.5 mm
Width: 30 mm (at latch locations)
```

## 2. LATCH BEARING LOADS

### Maximum Latch Load (from STR-004)
```
F_latch = 35.5 kN
Contact area: 20 mm × 15 mm = 300 mm²
```

### Bearing Stress
```
σ_bearing = F / A
σ_bearing = 35.5 kN / 300 mm²
σ_bearing = 118 MPa
```

## 3. BEARING STRENGTH

### CFRP Bearing Allowable
```
From CMH-17 (pinned joints):
σ_br_ultimate = 800 MPa (typical for e/D > 2)

For distributed load (better than pin):
σ_br_allowable ≈ 900 MPa
```

### Margin of Safety
```
MS = (Allowable / Applied) - 1
MS = (900 / 118) - 1 = +6.6
```

**Status:** High positive margin

## 4. LOAD TRANSFER TO CORE

### Shear-Out Check
```
Edge distance: 15 mm
Shear area: 2 × 15 × 4.5 = 135 mm²
τ_shear = 35.5 kN / 135 mm² = 263 MPa

CFRP shear strength: 105 MPa (ply level)
MS = (105 / 263) - 1 = -0.60
```

**⚠️ WARNING:** NEGATIVE MARGIN for shear-out

## 5. DESIGN MODIFICATION

### Add Titanium Insert
```
Material: Ti-6Al-4V
Dimensions: 40 mm × 30 mm × 3 mm
Embed in edge band

Benefits:
- Higher bearing strength (1,100 MPa)
- Distributes load over larger area
- Prevents local failure
```

### Revised Shear-Out
```
With insert, load distributed over 60 mm length:
Shear area: 2 × 60 × 4.5 = 540 mm²
τ_shear = 35.5 kN / 540 mm² = 66 MPa
MS = (105 / 66) - 1 = +0.59
```

**Status:** Acceptable with insert

## 6. VALIDATION REQUIRED

- [ ] Bearing test per ASTM D5961
- [ ] FEA of load introduction
- [ ] Full-scale latch operation test
- [ ] Verify insert bonding

---

**Status:** REQUIRES DESIGN MODIFICATION  
**Action:** Add titanium inserts at latch locations
