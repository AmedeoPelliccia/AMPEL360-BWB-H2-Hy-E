# Lightning Protection Trade Study

**Study:** TS-004  
**Date:** 2025-11-03  
**Status:** Draft

## 1. REQUIREMENTS

### CS-25.581
```
- Withstand lightning strike (200 kA)
- No ignition of fuel/vapors
- No loss of critical functions
- Damage limits defined
```

## 2. OPTIONS

### Option 1: Expanded Copper Foil (ECF)
```
Type: Copper mesh embedded in outer ply
Weight: 0.8 kg
Cost: $5k
Conductivity: Excellent
Protection: Zone 1A/2A capable
Status: BASELINE
```

### Option 2: Aluminum Mesh
```
Type: Aluminum screen
Weight: 0.5 kg
Cost: $3k
Conductivity: Good
Protection: Zone 2A only
Issue: Galvanic with CFRP
Status: Not recommended
```

### Option 3: Metallized Paint
```
Type: Silver-filled coating
Weight: 0.3 kg
Cost: $2k
Conductivity: Poor
Protection: Zone 3 only
Status: Insufficient
```

### Option 4: Lightning Diverter Strips
```
Type: External copper strips
Weight: 1.2 kg
Cost: $8k
Conductivity: Excellent
Protection: Zone 1A capable
Issue: Aerodynamic drag
Status: Over-design
```

## 3. EVALUATION

| Criterion | Weight | ECF | Al Mesh | Paint | Strips |
|-----------|--------|-----|---------|-------|--------|
| Protection | 50% | 10 | 6 | 2 | 10 |
| Weight | 20% | 8 | 10 | 10 | 4 |
| Cost | 15% | 7 | 9 | 10 | 4 |
| Integration | 15% | 9 | 5 | 10 | 6 |
| **Total** | | **8.6** | **6.7** | **5.5** | **7.1** |

## 4. RECOMMENDATION

**Select Option 1: Expanded Copper Foil**

Best balance of protection and integration.

## 5. VALIDATION

- [ ] Lightning strike testing (Zone 1A/2A)
- [ ] Witness panel inspection
- [ ] Functional check after strike
- [ ] FAA AC 20-53 compliance

---

**Status:** Baseline Selected  
**Action:** Lightning strike testing required
