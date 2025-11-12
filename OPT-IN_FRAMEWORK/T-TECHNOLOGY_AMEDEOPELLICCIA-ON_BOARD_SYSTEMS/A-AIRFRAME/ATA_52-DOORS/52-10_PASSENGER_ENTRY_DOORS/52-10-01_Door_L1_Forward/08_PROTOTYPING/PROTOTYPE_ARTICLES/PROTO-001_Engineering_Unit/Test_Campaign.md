# Test Campaign
## PROTO-001 Engineering Development Unit

**Document:** PROTO-001-TEST-CAMPAIGN  
**Status:** Planning  
**Date:** 2025-11-03

### Test Objectives

1. **Ground Vibration Test (GVT)** - CRITICAL GO/NO-GO
2. Static ultimate pressure test
3. Proof pressure test
4. Initial fatigue screening
5. FEA correlation

---

## TEST 1: GROUND VIBRATION TEST (GVT)

**Priority:** **CRITICAL - GO/NO-GO DECISION GATE**

### Objective
Measure modal frequencies and **damping ratios** to assess resonance risk.

### Setup
- Door mounted in test frame (simulated boundary conditions)
- 20 accelerometers (triaxial)
- Shaker excitation (0-100 Hz sweep)
- Impact hammer for modal ID

### Test Matrix
1. Frequency response functions (all locations)
2. Mode shape extraction (0-100 Hz)
3. **Damping ratio measurement (Mode 1 critical)**
4. Operating deflection shapes

### Critical Measurements

| Mode | Predicted Freq | Target Damping | Decision Criteria |
|------|----------------|----------------|-------------------|
| Mode 1 | 25.13 Hz | **≥3%** | **GO if ≥3%, NO-GO if <3%** |
| Mode 2 | 42 Hz | >2% | Info only |
| Mode 3 | 67 Hz | >2% | Info only |

### **GO/NO-GO DECISION**
- **PROCEED:** If Mode 1 damping ≥3%
- **REDESIGN:** If Mode 1 damping <3%
  - Add damping treatments
  - Modify internal structure
  - Retest before proceeding

**Budget:** $30,000  
**Duration:** 2 weeks  
**Criticality:** MANDATORY

---

## TEST 2: PROOF PRESSURE

**Priority:** HIGH

### Objective
Demonstrate structural integrity at proof load (1.5× limit).

### Setup
- Door sealed and pressurized in test chamber
- Pressure: 12.75 psi (1.5× 8.5 psi cabin pressure)
- Strain gauges: 30 locations
- Displacement sensors: 10 locations

### Procedure
1. Ramp to 12.75 psi at 1 psi/min
2. Hold for 3 seconds
3. Inspect for permanent deformation
4. Release pressure
5. Measure residual strains

### Acceptance
- [ ] No visible damage
- [ ] No permanent deformation
- [ ] All strains within elastic range

**Budget:** $15,000  
**Duration:** 1 week

---

## TEST 3: STATIC ULTIMATE

**Priority:** HIGH

### Objective
Demonstrate ultimate load capability (17 psi).

### Setup
- Same as proof test
- Instrumentation increased
- Failure containment

### Procedure
1. Ramp to 17 psi (2× limit load)
2. Hold for 3 seconds or until failure
3. Document failure mode
4. Forensic analysis

### Success Criteria
- [ ] Sustains 17 psi for 3 seconds
- [ ] Failure mode understood
- [ ] Correlation with FEA

**Budget:** $25,000  
**Duration:** 1 week  
**Note:** Destructive test, end of PROTO-001 life

---

## TEST 4: INITIAL FATIGUE

**Priority:** MEDIUM

### Objective
Screen for early fatigue issues (before ultimate test).

### Setup
- Pressure cycling fixture
- 8.5 psi (limit load)
- Automated cycling

### Test Plan
- 1000 cycles (representative)
- Inspect every 100 cycles
- Monitor for crack initiation

### Acceptance
- [ ] No cracks or damage
- [ ] No stiffness degradation

**Budget:** $20,000  
**Duration:** 2 weeks

---

## TEST 5: FEA CORRELATION

### Objective
Update finite element model with test data.

### Data to Correlate
- Modal frequencies
- Mode shapes
- Damping ratios
- Static deflections
- Strain distributions
- Ultimate strength

### Analysis Tasks
1. Update material properties
2. Refine boundary conditions
3. Adjust damping model
4. Predict PROTO-002 behavior
5. Certification analysis preparation

**Budget:** $15,000  
**Duration:** 3 weeks (parallel with testing)

---

## TEST SCHEDULE

| Week | Activity | Milestone |
|------|----------|-----------|
| 1-2 | GVT setup and testing | **GO/NO-GO DECISION** |
| 3 | Proof pressure | Structural validation |
| 4-5 | Fatigue screening | Durability check |
| 6 | Static ultimate | Failure mode |
| 7-9 | FEA correlation | Model update |

**Total Duration:** 9 weeks  
**Total Budget:** $105,000

---

## RISK MITIGATION

### If Mode 1 Damping <3%
1. STOP all remaining tests
2. Convene design review
3. Implement damping solution:
   - Viscoelastic material patches
   - Internal stiffeners
   - Constrained layer damping
4. Retest GVT before proceeding
5. Budget impact: +$100k, +8 weeks

---

**Document Control:** PROTO-001-TEST-CAMPAIGN-001  
**Revision:** A  
**Date:** 2025-11-03
