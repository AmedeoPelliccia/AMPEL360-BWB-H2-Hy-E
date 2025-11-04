# Inspection Intervals - Door Panel

**Calculation:** CALC-52-10-01-FAT-004  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Damage Tolerance (AI-Assisted)  
**Confidence:** ±50% (Very Low)

## 1. INSPECTION PHILOSOPHY

### Damage Tolerance Approach
```
- Assume damage exists
- Detect before critical size
- Establish repeat inspections
- Ensure structural integrity
```

## 2. FLAW SIZES

### Detectable Flaw
```
Visual inspection: 25 mm
Detailed visual: 10 mm
Ultrasonic (C-scan): 5 mm
Eddy current: 2 mm (surface only)
```

### Critical Flaw
```
a_critical = 25 mm (from FAT-003)
Based on residual strength requirement
```

## 3. INSPECTION INTERVALS

### Initial Inspection
```
Before first flight:
- Visual inspection (100% coverage)
- UT inspection (critical areas)
- Record baseline
```

### Repeat Inspections

#### Method 1: Crack Growth Based
```
From FAT-003:
Growth from 10 mm → 25 mm in ~1,500 flights

Inspection interval: 1,500 / 4 = 375 flights
Apply safety factor: 375 / 1.5 = 250 flights
```

#### Method 2: Damage Tolerance
```
Per CS-25.571(b):
Inspection interval ≤ N_critical / 2

N_critical ≈ 2,300 flights
Interval ≤ 1,150 flights
```

### Recommended Interval
```
Visual inspection: 500 flights (conservative)
Detailed inspection: 1,000 flights
UT inspection: 2,000 flights
```

## 4. INSPECTION LOCATIONS

### Critical Areas
```
1. Panel center (max stress)
2. Latch attachment points
3. Hinge attachments
4. Edge band interfaces
5. Lightning strike zones
```

### Inspection Coverage
```
Visual: 100% of exterior
Detailed: 80% of structure
UT: 40% (critical areas)
```

## 5. ACCEPTANCE CRITERIA

### Allowable Damage
```
Scratches: < 0.1 mm deep
Delaminations: < 5 mm diameter
Impact damage: None visible
Cracks: None allowed
Corrosion: None allowed
```

### Rejection Criteria
```
Any damage > allowable → Repair
Cracks of any size → Engineering evaluation
Delamination > 10 mm → Repair
Multiple damages → Engineering evaluation
```

## 6. MAINTENANCE PROGRAM

### Structure
```
Phase Check: Visual inspection (500 flights)
C-Check: Detailed inspection (1,000 flights)
D-Check: Major inspection + UT (4,000 flights)
```

### Documentation
```
- Inspection findings log
- Repair records
- NDI reports
- Engineering dispositions
```

## 7. VALIDATION REQUIRED

- [ ] Full-scale fatigue test with inspections
- [ ] NDI capability demonstration
- [ ] Damage detection reliability study
- [ ] DER approval of inspection program
- [ ] Maintenance manual procedures

---

**Status:** CRITICAL - DER Approval Required  
**Risk:** HIGH - Safety of Flight Item
