# Test Plan - Proof Pressure Test
## Door L1 Forward

**Test Plan:** TP-52-10-01-002  
**Priority:** HIGH  
**Revision:** 1.0  
**Date:** 2025-11-03  
**Status:** Complete - Awaiting Hardware

---

## 1. TEST OBJECTIVES

### 1.1 Primary Objective
Demonstrate structural integrity at proof pressure (12.75 psi) with no permanent deformation or yield.

### 1.2 Secondary Objectives
- Verify leak rate < 0.05 CFM at 8.5 psi
- Measure elastic deformation
- Confirm seal effectiveness
- Validate pressure retention capability

---

## 2. TEST REQUIREMENTS

### 2.1 Load Conditions
- **Proof pressure:** 12.75 psi (1.5 × 8.5 psi normal operating)
- **Operating pressure:** 8.5 psi (typical cruise altitude)
- **Leak test pressure:** 8.5 psi

### 2.2 Acceptance Criteria
**PASS:**
- No permanent deformation after unload
- Strain returns to zero (within ±50 με)
- Leak rate < 0.05 CFM @ 8.5 psi
- No visible damage

**FAIL:**
- Permanent deformation > 0.5 mm
- Residual strain > 100 με
- Leak rate > 0.05 CFM
- Any cracks or damage

---

## 3. TEST PROCEDURE

### 3.1 Leak Test (8.5 psi)
```
1. Pressurize to 8.5 psi
2. Hold for 10 minutes
3. Measure pressure decay
4. Calculate leak rate (CFM)
5. Acceptance: < 0.05 CFM
```

### 3.2 Proof Pressure Test (12.75 psi)
```
1. Ramp to 12.75 psi @ 0.5 psi/min
2. Hold for 3 minutes
3. Monitor strain and displacement
4. Depressurize @ 0.2 psi/min
5. Measure residual deformation
```

### 3.3 Post-Test
- Visual inspection
- NDT inspection
- Compare pre/post dimensions
- Document any changes

---

## 4. INSTRUMENTATION

- Strain gauges: 12 locations
- Displacement: 3 LVDTs
- Pressure sensors: 2 (redundant)
- Leak detector: Inficon Protec

---

## 5. SAFETY

### 5.1 Hazards
- Pressure hazard (12.75 psi = 221 kN force)
- Remote operation required
- Safety barriers

---

## 6. DELIVERABLES

- Test report with pass/fail assessment
- Leak rate measurement
- Load-displacement curves
- Strain recovery data
- Post-test inspection report

---

## 7. SCHEDULE & COST

- **Duration:** 2 days
- **Cost:** $25,000
- **Status:** Awaiting prototype

---

## 8. REFERENCES

- CS-25.365 Pressurized compartment loads
- CS-25.783 Doors - proof and ultimate loads
- PROC-001 Pressure Test Setup
- PROC-003 Leak Rate Measurement

---

**Note:** This test must be completed before ultimate strength test to verify elastic behavior.
