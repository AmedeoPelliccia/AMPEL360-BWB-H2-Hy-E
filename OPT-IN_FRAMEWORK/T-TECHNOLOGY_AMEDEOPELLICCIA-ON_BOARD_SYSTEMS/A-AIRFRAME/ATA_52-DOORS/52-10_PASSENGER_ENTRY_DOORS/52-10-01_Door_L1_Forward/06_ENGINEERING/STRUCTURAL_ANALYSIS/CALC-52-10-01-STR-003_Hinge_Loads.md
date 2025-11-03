# Hinge Load Analysis - Door L1 Forward

**Calculation:** CALC-52-10-01-STR-003  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Static Equilibrium (AI-Assisted)  
**Confidence:** ±25%

## 1. HINGE CONFIGURATION

### Layout
```
Number of hinges: 3
Location: Forward edge of door
Spacing: 
  - Top hinge: 200 mm from top
  - Middle hinge: 940 mm from top (center)
  - Bottom hinge: 1,680 mm from top
Vertical span: 1,480 mm
```

## 2. LOAD ANALYSIS

### Pressure Load
```
Ultimate pressure: 117.2 kPa
Door area: 2.106 m²
Total force: 247 kN (perpendicular to door)
```

### Moment About Hinge Line
```
Center of pressure: w/2 = 560 mm from hinge line
Moment arm: 0.56 m

M_total = F × d
M_total = 247 kN × 0.56 m
M_total = 138 kN⋅m
```

## 3. HINGE REACTIONS

### Vertical Load Distribution
```
Assuming equal distribution (conservative):
R_v = F_total / 3
R_v = 247 kN / 3
R_v ≈ 82 kN per hinge (vertical component)
```

### Horizontal Reactions (From Moment)
```
For 3 hinges with moment:
R_h_top and R_h_bottom carry most of moment
R_h_middle ≈ 0 (near center)

Moment balance:
R_h_top × 1.48 m - R_h_bottom × 1.48 m = 138 kN⋅m

If R_h_top = -R_h_bottom (symmetric):
R_h = 138 / 1.48 = 93 kN
```

### Combined Hinge Reactions
```
Top hinge:
  - Vertical: 82 kN
  - Horizontal: 93 kN
  - Resultant: √(82² + 93²) = 124 kN

Middle hinge:
  - Vertical: 82 kN
  - Horizontal: ~0 kN
  - Resultant: 82 kN

Bottom hinge:
  - Vertical: 82 kN
  - Horizontal: -93 kN
  - Resultant: 124 kN
```

## 4. HINGE SIZING

### Allowable Loads (Typical Aviation Hinges)
```
Hinge type: Heavy-duty piano hinge
Material: Ti-6Al-4V or 15-5PH stainless
Ultimate load capacity: 180 kN (typical)
```

### Margin of Safety
```
MS = (Allowable / Applied) - 1
MS = (180 / 124) - 1
MS = +0.45
```

**Status:** Acceptable margin

## 5. VALIDATION REQUIRED

- [ ] FEA to refine load distribution
- [ ] Hinge manufacturer load ratings
- [ ] Static test with load cells at each hinge
- [ ] Verify bolt preload and bearing stress

---

**Status:** Draft - Requires Testing  
**Confidence:** LOW
