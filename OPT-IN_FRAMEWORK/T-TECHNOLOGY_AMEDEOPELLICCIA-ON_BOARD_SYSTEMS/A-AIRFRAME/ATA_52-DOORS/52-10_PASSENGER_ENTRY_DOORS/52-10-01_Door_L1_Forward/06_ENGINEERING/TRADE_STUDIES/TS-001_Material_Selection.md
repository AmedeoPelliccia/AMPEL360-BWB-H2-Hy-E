# Material Selection Trade Study

**Study:** TS-001  
**Date:** 2025-11-03  
**Status:** Draft

## 1. REQUIREMENTS

### Key Requirements
- Ultimate strength: 2.0× cabin pressure (17 psi)
- Weight: < 140 kg total door
- Fatigue life: 60,000 flights minimum
- Temperature: -55°C to +85°C
- Lightning strike protection required
- Damage tolerance per CS-25.571

## 2. CANDIDATE MATERIALS

### Option 1: CFRP Sandwich (Baseline)
```
Face sheets: M21E/IMA epoxy/carbon
Core: Nomex HRH-10-48
```

**Pros:**
- Lightweight (72 kg panel)
- High strength-to-weight
- Good fatigue resistance
- Proven in aerospace

**Cons:**
- Expensive ($50k material)
- Requires autoclave
- Lightning protection needed
- Damage detection difficult

**Score: 8.5/10**

### Option 2: Aluminum Sandwich
```
Face sheets: 2024-T3 aluminum
Core: Aluminum honeycomb 5052
```

**Pros:**
- Lower cost ($25k material)
- Easy inspection
- Good conductivity (lightning)
- Established processes

**Cons:**
- Heavier (95 kg panel)
- Lower fatigue life
- Corrosion concerns
- Does not meet weight target

**Score: 6.0/10**

### Option 3: Hybrid (CFRP/Aluminum)
```
Outer face: CFRP
Inner face: Aluminum
Core: Nomex
```

**Pros:**
- Moderate weight (82 kg)
- Easy interior mounting
- Lightning protection
- Damage tolerance

**Cons:**
- Galvanic corrosion risk
- Complex manufacturing
- CTE mismatch
- Higher cost than baseline

**Score: 7.0/10**

## 3. EVALUATION MATRIX

| Criterion | Weight | CFRP | Aluminum | Hybrid |
|-----------|--------|------|----------|--------|
| Weight | 25% | 10 | 4 | 7 |
| Cost | 20% | 6 | 9 | 5 |
| Strength | 20% | 10 | 7 | 9 |
| Fatigue | 15% | 9 | 6 | 8 |
| Manufacturing | 10% | 6 | 9 | 5 |
| Maintainability | 10% | 5 | 8 | 7 |
| **Total** | | **8.1** | **6.7** | **7.0** |

## 4. RECOMMENDATION

**Select Option 1: CFRP Sandwich (Baseline)**

### Justification
- Only option meeting weight target
- Best strength-to-weight ratio
- Proven technology for doors
- Worth the additional cost for weight savings

### Conditions
- Add expanded copper foil for lightning
- Establish NDI inspection program
- Prototype testing required

---

**Status:** Recommendation Approved  
**Next:** Detailed design of CFRP sandwich
