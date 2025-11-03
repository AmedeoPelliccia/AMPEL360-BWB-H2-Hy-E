# Core Density Trade Study

**Study:** TS-002  
**Date:** 2025-11-03  
**Status:** Draft

## 1. REQUIREMENTS

- Core shear strength adequate
- Minimize weight
- Maintain panel stiffness
- Cost considerations

## 2. OPTIONS

### Option 1: HRH-10-48 (Baseline)
```
Density: 48 kg/m³
Shear strength: 1.2 MPa
Cost: $200/m²
Mass: 4.0 kg
Status: FAILS shear (MS = -0.27)
```

### Option 2: HRH-10-64
```
Density: 64 kg/m³
Shear strength: 1.8 MPa
Cost: $250/m²
Mass: 5.4 kg
Status: PASSES shear (MS = +0.10)
Weight penalty: +1.4 kg
```

### Option 3: HRH-10-96 (Over-design)
```
Density: 96 kg/m³
Shear strength: 2.8 MPa
Cost: $350/m²
Mass: 8.1 kg
Status: High margin (MS = +0.70)
Weight penalty: +4.1 kg
```

## 3. EVALUATION

| Criterion | Weight | -48 | -64 | -96 |
|-----------|--------|-----|-----|-----|
| Strength | 40% | 0 | 8 | 10 |
| Weight | 30% | 10 | 8 | 4 |
| Cost | 20% | 10 | 8 | 4 |
| Availability | 10% | 10 | 10 | 8 |
| **Total** | | **6.0** | **8.2** | **6.4** |

## 4. RECOMMENDATION

**Select HRH-10-64**

Provides adequate strength with minimal weight penalty.

---

**Status:** Approved  
**Action:** Update design to HRH-10-64
