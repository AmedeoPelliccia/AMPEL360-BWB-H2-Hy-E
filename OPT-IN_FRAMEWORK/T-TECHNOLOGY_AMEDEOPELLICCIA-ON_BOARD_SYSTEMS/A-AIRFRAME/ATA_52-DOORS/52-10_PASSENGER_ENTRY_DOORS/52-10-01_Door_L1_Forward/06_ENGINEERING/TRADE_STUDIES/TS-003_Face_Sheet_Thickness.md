# Face Sheet Thickness Trade Study

**Study:** TS-003  
**Date:** 2025-11-03  
**Status:** Draft

## 1. DRIVER

Natural frequency too close to engine RPM (25-30 Hz predicted).

## 2. OPTIONS

### Option 1: 4mm (Baseline)
```
Natural frequency: 27.5 Hz (predicted)
Mass: 51.6 kg (2 faces)
Stress: 348 MPa
Status: HIGH RESONANCE RISK
```

### Option 2: 5mm
```
Natural frequency: ~35 Hz (predicted)
Mass: 64.5 kg (+12.9 kg)
Stress: 280 MPa
Status: Above engine max (30 Hz)
Margin: 1.17× separation
Recommended: YES
```

### Option 3: 6mm
```
Natural frequency: ~42 Hz (predicted)
Mass: 77.4 kg (+25.8 kg)
Stress: 232 MPa
Status: High margin (1.4×)
Weight penalty: Excessive
```

## 3. EVALUATION

| Criterion | Weight | 4mm | 5mm | 6mm |
|-----------|--------|-----|-----|-----|
| Frequency separation | 40% | 2 | 9 | 10 |
| Weight | 30% | 10 | 6 | 2 |
| Cost | 20% | 10 | 7 | 4 |
| Stress margin | 10% | 8 | 9 | 10 |
| **Total** | | **6.6** | **7.7** | **6.0** |

## 4. RECOMMENDATION

**Select 5mm face sheets IF GVT shows f₁ < 30 Hz**

Otherwise, keep 4mm and add damping treatment.

---

**Status:** Contingent on GVT  
**Decision Point:** After GVT testing
