# Actuation Forces - Door L1 Forward

**Calculation:** CALC-52-10-01-MEC-002  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Force Balance (AI-Assisted)  
**Confidence:** ±30%

## 1. REQUIREMENTS

### CS-25.783
```
Normal operation force: < 60 N (13.5 lbf)
Emergency operation: < 135 N (30 lbf)
One hand operation required
```

## 2. FORCE COMPONENTS

### Seal Force
```
Primary seal: 200 N
Secondary seal: 100 N
Total seal: 300 N
```

### Latch Force
```
8 latches × 50 N each = 400 N
(Force to disengage)
```

### Friction
```
Hinge friction: 50 N
Seal friction: 100 N
Total friction: 150 N
```

### Pressure Force (if pressurized)
```
Emergency: Should not be possible
Normal: Door cannot open under pressure
```

### Total Force
```
F_total = 300 + 400 + 150 = 850 N
```

## 3. MECHANICAL ADVANTAGE

### Handle Lever Arm
```
Lever ratio: 20:1
Input force = 850 / 20 = 42.5 N
```

**Status:** Meets CS-25.783 requirement (< 60 N) ✓

## 4. POWER ASSIST (Optional)

### Pneumatic Assist
```
If manual force too high:
- Pneumatic cylinder
- Powered by bleed air
- Reduces force to 20 N
```

## 5. VALIDATION REQUIRED

- [ ] Measure actual forces on prototype
- [ ] Test at temperature extremes
- [ ] Verify after 10,000 cycles
- [ ] Human factors testing

---

**Status:** Draft  
**Risk:** MEDIUM
