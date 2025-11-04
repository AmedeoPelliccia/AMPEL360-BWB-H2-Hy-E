# Latch Load Analysis - Door L1 Forward

**Calculation:** CALC-52-10-01-STR-004  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Force Distribution (AI-Assisted)  
**Confidence:** ±30%

## 1. LATCH CONFIGURATION

### Layout
```
Number of latches: 8
Location: Aft edge and top/bottom edges
Distribution:
  - 4 latches on aft vertical edge
  - 2 latches on top edge
  - 2 latches on bottom edge
```

## 2. LOAD DISTRIBUTION

### Total Pressure Force
```
Ultimate pressure: 117.2 kPa
Door area: 2.106 m²
Total force: 247 kN
```

### Non-Uniform Distribution Factor
```
K = 1.15 (aft latches carry more load)
Due to pressure center and hinge location
```

### Latch Load Calculation
```
Average load per latch: F_avg = 247 / 8 = 30.9 kN
Maximum latch load: F_max = F_avg × K
F_max = 30.9 × 1.15 = 35.5 kN
```

## 3. INDIVIDUAL LATCH LOADS

### Aft Edge Latches (4 latches)
```
Load per latch: 35.5 kN (maximum)
Total load carried: 142 kN
```

### Top/Bottom Edge Latches (4 latches)
```
Load per latch: 26.2 kN (reduced)
Total load carried: 105 kN
```

**Check:** 142 + 105 = 247 kN ✓

## 4. LATCH CAPACITY

### Typical Aviation Latch Specifications
```
Type: Rotary latch with roller
Material: 17-4PH or 15-5PH stainless steel
Ultimate capacity: 50 kN (typical)
```

### Margin of Safety
```
MS = (Allowable / Applied) - 1
MS = (50 / 35.5) - 1
MS = +0.41
```

**Status:** Acceptable margin

## 5. VALIDATION REQUIRED

- [ ] FEA for accurate load distribution
- [ ] Latch manufacturer specifications
- [ ] Static test with individual latch load cells
- [ ] Verify engagement and backlash

---

**Status:** Draft  
**Risk:** MEDIUM
