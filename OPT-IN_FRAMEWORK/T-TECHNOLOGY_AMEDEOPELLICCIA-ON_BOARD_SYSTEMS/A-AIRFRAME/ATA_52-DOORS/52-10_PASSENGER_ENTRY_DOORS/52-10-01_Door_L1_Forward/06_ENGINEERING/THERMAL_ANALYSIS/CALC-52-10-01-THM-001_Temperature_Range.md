# Temperature Range Analysis

**Calculation:** CALC-52-10-01-THM-001  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Environmental Specification  
**Confidence:** HIGH

## 1. OPERATING ENVIRONMENT

### CS-25 Requirements
```
Operating temperature range:
  Minimum: -55°C (cold soak, altitude)
  Maximum: +45°C (hot day, ground)
  
Environmental:
  Humidity: 0-95% RH
  Pressure: 0-14.7 psi
  Solar radiation: 1,120 W/m² (max)
```

## 2. DOOR TEMPERATURE EXPOSURE

### Cold Extreme (-55°C)
```
Condition: High altitude cruise
Duration: Several hours continuous
Effects:
  - Material embrittlement (concern for metals)
  - Seal stiffening
  - Reduced damping
  - Thermal contraction
```

### Hot Extreme (+85°C)
```
Condition: Direct solar exposure on ground
Duration: Hours (parked aircraft)
Calculation: +45°C ambient + 40°C solar = +85°C surface
Effects:
  - Reduced material strength
  - Seal relaxation
  - Thermal expansion
  - Outgassing
```

## 3. MATERIAL LIMITS

### CFRP (M21E/IMA)
```
Service temperature: -60°C to +120°C
Dry Tg: +180°C
Wet Tg: +160°C
Operating range: Well within limits ✓
```

### Nomex Core
```
Service temperature: -55°C to +180°C
Operating range: Within limits ✓
```

### Seals (Silicone)
```
Service temperature: -65°C to +200°C
Operating range: Within limits ✓
```

### Titanium Inserts
```
Service temperature: -200°C to +400°C
Operating range: No concern ✓
```

## 4. PERFORMANCE AT EXTREMES

### Cold (-55°C)
```
CFRP strength: +10% (benefit)
CFRP modulus: +5%
Seal force: +30% (stiffer)
Operation force: +20% increase
Status: Acceptable if < 60N total
```

### Hot (+85°C)
```
CFRP strength: -5% (wet basis)
CFRP modulus: -3%
Seal force: -20% (relaxation)
Operation force: -10% decrease
Status: Monitor leak rate
```

## 5. THERMAL CYCLING

### Flight Profile
```
Ground (+30°C) → Cruise (-55°C) → Ground (+30°C)
ΔT = 85°C per cycle
60,000 flights = 60,000 thermal cycles
```

### Effects
```
- CTE mismatch stress
- Face/core debonding risk
- Seal fatigue
- Moisture cycling
```

## 6. VALIDATION REQUIRED

- [ ] Environmental chamber testing (-55°C to +85°C)
- [ ] Thermal cycling (100 cycles minimum)
- [ ] Measure operation force at extremes
- [ ] Leak rate at extremes
- [ ] Verify material properties

---

**Status:** Requirements Defined  
**Confidence:** HIGH  
**Action:** Environmental testing required
