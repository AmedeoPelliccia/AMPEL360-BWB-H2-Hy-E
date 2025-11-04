# Damage Scenarios - Door Panel

**Calculation:** CALC-52-10-01-FAT-005  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Failure Modes Analysis (AI-Assisted)  
**Confidence:** ±50% (Very Low)

## 1. POTENTIAL DAMAGE SCENARIOS

### Scenario 1: Impact Damage (Most Common)
```
Source: Ground service equipment, hail, bird strike
Location: Exterior face sheet
Typical size: 25-50 mm diameter
Depth: Through face sheet + core crush

Inspection detectability: Visual (if exterior)
Residual strength: Reduced 30-50% locally
Action required: Repair before flight
```

### Scenario 2: Delamination (Manufacturing)
```
Source: Manufacturing defect, poor cure
Location: Face/core interface
Typical size: 10-100 mm
Growth: Slow under fatigue

Inspection detectability: UT (C-scan) only
Residual strength: Reduced compression 20%
Action required: Monitor if < 25mm, repair if growing
```

### Scenario 3: Lightning Strike
```
Source: Direct or swept stroke
Location: Exterior surface, edges
Typical damage: 5-15 mm fiber burn
Depth: 1-3 mm into face

Inspection detectability: Visual
Residual strength: Local reduction
Action required: Engineering evaluation
```

### Scenario 4: Moisture Ingress
```
Source: Seal failure, impact hole
Location: Core
Effect: Core deterioration, weight gain
Detection: Weight monitoring, UT

Inspection detectability: Gravimetric
Residual strength: Reduced face/core bond
Action required: Dry out or repair
```

### Scenario 5: Fatigue Crack
```
Source: Cyclic pressure loads
Location: High stress regions, fastener holes
Size: 2-25 mm
Growth: Per Paris law (FAT-003)

Inspection detectability: 10 mm (visual)
Residual strength: Per net section
Action required: Immediate repair
```

## 2. CRITICALITY RANKING

| Scenario | Probability | Severity | Risk | Priority |
|----------|-------------|----------|------|----------|
| Impact | Medium | High | HIGH | 1 |
| Delamination | Low | Medium | MEDIUM | 3 |
| Lightning | Low | Medium | MEDIUM | 4 |
| Moisture | Low | Low | LOW | 5 |
| Fatigue crack | Very Low | Critical | HIGH | 2 |

## 3. DAMAGE TOLERANCE DEMONSTRATION

### Test Matrix
```
1. Impact damage (50 mm) + ultimate pressure
2. Delamination (25 mm) + fatigue (2× life)
3. Lightning strike simulation + residual strength
4. Through-crack (25 mm) + residual strength
5. Multiple damages + ultimate load
```

## 4. REPAIR PHILOSOPHY

### Minor Damage (< 10 mm)
```
Method: Fill with resin
Approval: Mechanic-level repair
Time: 2-4 hours
Return to service: Immediately
```

### Major Damage (10-50 mm)
```
Method: External patch (scarf or bolted)
Approval: Engineering disposition
Time: 8-16 hours
Return to service: After inspection
```

### Critical Damage (> 50 mm)
```
Method: Panel replacement
Approval: DER + certification
Time: 2-5 days
Return to service: After testing
```

## 5. RESIDUAL STRENGTH ANALYSIS

### Impact Damage (50 mm)
```
Effective stress concentration: Kt = 2.0
Local stress: 348 × 2.0 = 696 MPa
Allowable: 2,724 MPa
MS = (2724 / 696) - 1 = +2.9
```

**Adequate strength with damage**

### Through-Crack (25 mm)
```
Net section: w_eff = 1120 - 50 = 1070 mm
Stress increase: 1120 / 1070 = 1.047
Applied stress: 348 × 1.047 = 364 MPa
MS = (2724 / 364) - 1 = +6.5
```

**High margin even with damage**

## 6. VALIDATION REQUIRED

- [ ] Full-scale damage tolerance testing
- [ ] Impact testing at various energies
- [ ] Lightning strike testing
- [ ] Residual strength demonstration
- [ ] Repair validation testing
- [ ] DER approval of damage limits

---

**Status:** CRITICAL - Testing Required  
**Risk:** HIGH - Certification Critical
