# Resonance Risk Assessment - Door Panel

**Calculation:** CALC-52-10-01-DYN-003  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Frequency Comparison (AI-Assisted)  
**Confidence:** ±30%

## 1. EXCITATION SOURCES

### Primary Engine (H2-Powered)
```
Idle: 400 RPM = 6.7 Hz
Cruise: 1200 RPM = 20.0 Hz
Max continuous: 1500 RPM = 25.0 Hz
Max takeoff: 1650 RPM = 27.5 Hz
```

### Propeller/Fan
```
Blades: 20
Blade passing frequency: 20 × 25 Hz = 500 Hz
```

### Aerodynamic Buffet
```
Typical range: 10-100 Hz
Peak energy: 15-30 Hz (transonic)
```

## 2. DOOR NATURAL FREQUENCIES

### Predicted Modes
```
Mode 1: 25-30 Hz (±30% uncertainty)
  Range: 17.5-39 Hz
Mode 2: 35-45 Hz
Mode 3: 60-80 Hz
```

## 3. RESONANCE MARGIN

### Definition
```
Margin = |f_structure - f_excitation| / f_excitation

Required margin: >20% (or >1.2× separation)
```

### Analysis
```
Engine max continuous: 25 Hz
Door Mode 1: 25-30 Hz (nominal)

Worst case:
Margin = |25 - 25| / 25 = 0%
```

**🔴 CRITICAL: ZERO MARGIN - RESONANCE RISK**

## 4. DAMPING REQUIREMENTS

### Typical Composite Damping
```
Structural damping: ζ = 1-2% of critical
With viscoelastic layer: ζ = 3-5%
```

### Required Damping (for resonance)
```
If resonance unavoidable:
Minimum ζ_req = 5% of critical
```

## 5. RISK ASSESSMENT

| Scenario | Probability | Severity | Risk Level |
|----------|------------|----------|------------|
| Resonance at cruise | High | High | CRITICAL |
| High vibration | Medium | Medium | HIGH |
| Fatigue acceleration | High | High | CRITICAL |
| Passenger discomfort | High | Medium | HIGH |

## 6. MITIGATION STRATEGIES

### Option 1: Redesign Structure
```
Target: f₁ > 35 Hz (1.4× engine max)
Method: Increase face sheet to 5 mm
Result: f₁ ≈ 35-38 Hz
Cost: +3 kg weight, $5k tooling
```

### Option 2: Add Damping
```
Method: Constrained layer damping (CLD)
Material: 3M ISD112 or equivalent
Thickness: 2 mm viscoelastic + 0.5 mm constraint
Result: ζ = 4-6%
Cost: +1.5 kg, $3k material
```

### Option 3: Active Vibration Control
```
Method: Piezoelectric actuators
Control: Adaptive algorithm
Result: 20 dB reduction
Cost: $20k system + certification
```

## 7. RECOMMENDED APPROACH

1. **Immediate:** Conduct GVT on prototype
2. **If f₁ < 27 Hz:** Implement Option 1 (redesign)
3. **If 27 Hz < f₁ < 30 Hz:** Implement Option 2 (damping)
4. **If f₁ > 30 Hz and ζ > 3%:** Accept design

## 8. TEST PLAN

### Ground Vibration Test (GVT)
```
Excitation: Impact hammer and shaker
Frequency range: 5-200 Hz
Measurements: 15 accelerometers
Output:
  - Natural frequencies (±0.5 Hz)
  - Damping ratios (±0.5%)
  - Mode shapes (animation)
```

### Flight Test (if required)
```
Instrumentation: 8 accelerometers
Conditions: Full operational envelope
Success criteria:
  - Vibration < 0.5g RMS
  - No resonance observed
  - No structural damage
```

## 9. VALIDATION REQUIRED

- [ ] GVT test BEFORE first flight
- [ ] Verify all modes and damping
- [ ] If resonance found, implement mitigation
- [ ] Retest after modification

---

**Status:** CRITICAL ISSUE  
**Risk Level:** HIGH  
**Action Required:** GVT + Potential Redesign
