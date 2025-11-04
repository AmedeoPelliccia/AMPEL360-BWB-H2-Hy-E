# Uncertainty Assessment

**Document:** AMPEL360-52-10-01-ENG-UNCERT  
**Date:** 2025-11-03

## Overview

This document quantifies the uncertainties in all AI-assisted engineering calculations for the Door L1 Forward.

## UNCERTAINTY SOURCES

### 1. Model Simplification
**Impact:** Medium to High

**Sources:**
- Complex 3D geometry simplified to 2D models
- Boundary conditions idealized (clamped vs. elastic restraint)
- Material properties assumed isotropic or quasi-isotropic
- Load distribution approximated

**Typical Error:** ±20-40%

### 2. AI Calculation Limitations
**Impact:** Medium

**Sources:**
- Limited precision in symbolic math
- Potential for formula transcription errors
- Inability to iterate complex solutions
- No optimization capabilities

**Typical Error:** ±10-20%

### 3. Material Property Variability
**Impact:** Low to Medium

**Sources:**
- Published data ranges (e.g., CMH-17 basis values)
- Temperature effects
- Moisture absorption (composites)
- Manufacturing variation

**Typical Error:** ±10-25%

### 4. Geometric Tolerances
**Impact:** Low

**Sources:**
- Manufacturing tolerances
- Assembly gaps
- Thermal expansion
- In-service wear

**Typical Error:** ±5-15%

## UNCERTAINTY BY ANALYSIS TYPE

### Static Stress Analysis

| Load Case | Method | Nominal Uncertainty | Confidence Bound (95%) |
|-----------|--------|--------------------|-----------------------|
| Ultimate pressure | Plate theory | ±40% | ±80% |
| Hinge loads | Statics | ±25% | ±50% |
| Latch loads | Distribution | ±30% | ±60% |
| Composite stress | CLT | ±35% | ±70% |
| Core shear | Sandwich theory | ±30% | ±60% |
| Edge band bearing | Empirical | ±40% | ±80% |

**Overall Confidence:** LOW  
**Recommendation:** Professional FEA required

### Dynamic Analysis

| Parameter | Method | Nominal Uncertainty | Confidence Bound (95%) |
|-----------|--------|--------------------|-----------------------|
| Natural frequency | Rayleigh-Ritz | ±30% | ±60% |
| Mode shapes | Estimated | ±50% | ±100% |
| Damping ratio | Assumed | ±75% | Not quantifiable |
| Resonance margin | Calculated | ±40% | ±80% |

**Overall Confidence:** VERY LOW  
**Recommendation:** Ground Vibration Test (GVT) mandatory

### Fatigue & Damage Tolerance

| Analysis | Method | Nominal Uncertainty | Confidence Bound (95%) |
|----------|--------|--------------------|-----------------------|
| S-N life | Handbook curves | ±50% | Factor of 3-10 |
| Crack growth rate | Paris law | ±60% | Factor of 5-20 |
| Inspection interval | Conservative | ±40% | Factor of 2-4 |
| Residual strength | Net section | ±35% | ±70% |

**Overall Confidence:** VERY LOW  
**Recommendation:** Full-scale fatigue testing required

### Weight & Balance

| Parameter | Method | Nominal Uncertainty | Confidence Bound (95%) |
|-----------|--------|--------------------|-----------------------|
| Component mass | Density × volume | ±10% | ±20% |
| Total door mass | Summation | ±12% | ±25% |
| CG location | First moment | ±15% | ±30% |
| MOI | Second moment | ±20% | ±40% |

**Overall Confidence:** MEDIUM  
**Recommendation:** Weigh actual hardware

### Thermal Analysis

| Parameter | Method | Nominal Uncertainty | Confidence Bound (95%) |
|-----------|--------|--------------------|-----------------------|
| Temperature range | Specification | ±5% | ±10% |
| Thermal expansion | CTE tables | ±20% | ±40% |
| Thermal stress | Linear elastic | ±30% | ±60% |
| Seal compression | Empirical | ±40% | ±80% |

**Overall Confidence:** MEDIUM  
**Recommendation:** Environmental testing required

### Mechanism Analysis

| Parameter | Method | Nominal Uncertainty | Confidence Bound (95%) |
|-----------|--------|--------------------|-----------------------|
| Kinematics | Geometry | ±5% | ±10% |
| Actuation force | Force balance | ±30% | ±60% |
| Operation time | Estimate | ±40% | ±80% |
| Manual override | Human factors | ±50% | ±100% |

**Overall Confidence:** LOW to MEDIUM  
**Recommendation:** Prototype testing required

## COMBINED UNCERTAINTIES

When multiple uncertain parameters combine in a calculation:

**Root Sum Square (RSS) Method:**
```
σ_total = √(σ₁² + σ₂² + ... + σₙ²)
```

**Conservative (Worst Case) Method:**
```
σ_total = σ₁ + σ₂ + ... + σₙ
```

**Approach Used:** Conservative for safety-critical items, RSS for others

## EXAMPLE CALCULATION

**Case:** Ultimate stress in door panel

**Inputs:**
- Pressure load: 17.0 psi (±5% uncertainty)
- Geometry: 1.88m × 1.12m (±2% uncertainty)
- Thickness: 48mm (±5% uncertainty)
- Material modulus: 65 GPa (±15% uncertainty)

**Calculation Uncertainty:**
- Model simplification: ±40%
- AI calculation: ±10%

**Combined Uncertainty (RSS):**
```
σ_total = √(5² + 2² + 5² + 15² + 40² + 10²)
σ_total ≈ ±44%
```

**Conservative Bound:** ±77%

**Result:** 
- Nominal stress: 478 MPa
- Lower bound (conservative): 110 MPa
- Upper bound (conservative): 846 MPa

**Safety Factor Required:** Minimum 2.0 with FEA validation

## UNCERTAINTY REDUCTION STRATEGIES

### Short Term (Preliminary Design)
1. Apply conservative safety factors (1.5× minimum)
2. Use lower bound material properties
3. Assume worst-case boundary conditions
4. Multiple calculation methods where possible

### Medium Term (Detailed Design)
1. Professional FEA with mesh refinement
2. Material property testing
3. Component testing for validation
4. Design of experiments (DOE) for sensitivity

### Long Term (Certification)
1. Full-scale structural testing
2. Fatigue testing to failure
3. Ground vibration testing
4. Environmental qualification testing

## CONFIDENCE LEVELS

**High Confidence (±10%):**
- Geometric properties
- Material density
- Basic statics

**Medium Confidence (±20-30%):**
- Weight estimates
- CG location
- Temperature ranges
- Simple loads

**Low Confidence (±40-50%):**
- Stress predictions
- Natural frequencies
- Thermal stresses
- Complex loads

**Very Low Confidence (>±50%):**
- Fatigue life
- Crack growth
- Mode shapes
- Damping ratios

## RISK MITIGATION

**For analyses with high uncertainty:**
1. Apply safety factors of 1.5-2.0
2. Plan early testing
3. Use conservative assumptions
4. Design for adjustability
5. Plan contingency solutions

## VALIDATION THRESHOLDS

**Before manufacturing release, reduce uncertainty to:**
- Static stress: ±10% (via FEA + test)
- Natural frequency: ±5% (via GVT)
- Weight: ±3% (via weighing)
- Fatigue life: Factor of 4 safety

## DOCUMENTATION REQUIREMENTS

Every calculation must state:
1. Nominal uncertainty range
2. Confidence level (High/Medium/Low/Very Low)
3. Key assumptions
4. Validation plan
5. Safety factors applied

## CONCLUSION

AI-assisted calculations provide useful preliminary estimates but have significant uncertainties. All results must be:
- Treated as order-of-magnitude estimates
- Validated with professional tools
- Tested before certification
- Approved by licensed engineers

**Remember:** Uncertainty is not a deficiency—it's transparency. The goal is to quantify what we don't know so we can plan appropriate validation.

---

*Honest assessment of limitations enables appropriate risk management.*
