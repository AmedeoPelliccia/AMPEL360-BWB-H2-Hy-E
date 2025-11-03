# Test Plan - Static Ultimate Strength Test
## Door L1 Forward

**Test Plan:** TP-52-10-01-001  
**Priority:** HIGH  
**Revision:** 1.0  
**Date:** 2025-11-03  
**Status:** Complete - Awaiting Hardware

---

## 1. TEST OBJECTIVES

### 1.1 Primary Objective
Demonstrate ultimate structural capability at 17.0 psi cabin differential pressure without rupture or catastrophic failure.

### 1.2 Secondary Objectives
- Measure strain distribution under ultimate load
- Verify margin of safety
- Validate FEA predictions
- Assess failure modes
- Demonstrate compliance with CS-25.365

---

## 2. TEST REQUIREMENTS

### 2.1 Load Conditions
- **Ultimate pressure:** 17.0 psi (1.5 × limit load)
- **Limit pressure:** 11.33 psi (design cabin pressure 8.5 psi + safety factor)
- **Total force:** 17.0 psi × 2.52 m² = 295 kN (66,000 lbf)

### 2.2 Acceptance Criteria
**PASS:**
- No rupture at 17.0 psi
- No visible cracks or delamination
- Strain < 10,000 με at critical locations

**FAIL:**
- Any structural failure
- Panel rupture
- Face sheet delamination
- Core crushing

---

## 3. TEST ARTICLE

### 3.1 Configuration
- Door L1 Forward complete assembly
- All 8 latches engaged
- 3 hinges connected to test fixture
- Seals inflated per specification
- Instrumented with 24 strain gauges

### 3.2 Pre-Test Inspection
- Visual inspection
- NDT ultrasonic scan (C-scan)
- Dimensional verification
- Mass measurement
- Photographic documentation

---

## 4. TEST SETUP

### 4.1 Test Fixture
- Pressure chamber: 3m × 3m × 3m
- Door installed in simulated fuselage section
- Rigid fixture for latch and hinge attachment
- Safety barriers and blast shields

### 4.2 Instrumentation
**Strain Gauges (24 locations):**
- 8 rosettes at latch points
- 8 uniaxial at mid-panel (0/90 orientation)
- 4 rosettes at hinge locations
- 4 at critical stress concentrations

**Displacement (5 LVDTs):**
- Panel center
- Four corner locations

**Pressure Sensors (3):**
- Cabin side (redundant)
- External reference
- Differential measurement

**Acoustic Emission (4 sensors):**
- Monitor crack initiation/propagation

---

## 5. TEST PROCEDURE

### 5.1 Preparation
1. Install door in test fixture
2. Verify seal engagement
3. Install all instrumentation
4. Calibrate sensors
5. Perform leak check at 0.5 psi
6. Clear personnel from test area

### 5.2 Load Application
```
Phase 1: Ramp to Limit Load (11.33 psi)
- Rate: 0.5 psi/min
- Hold: 3 minutes
- Monitor all channels

Phase 2: Ramp to Ultimate Load (17.0 psi)
- Rate: 0.5 psi/min
- Hold: 3 seconds minimum
- Record all data

Phase 3: Unload
- Rate: 0.2 psi/min
- Monitor for permanent deformation
```

### 5.3 Data Recording
- Sample rate: 1000 Hz all channels
- Continuous recording during test
- Trigger on pressure threshold
- Redundant data storage

---

## 6. SAFETY

### 6.1 Hazards
⚠️ **CRITICAL:** 17.0 psi = 295 kN total force
- Catastrophic failure energy: ~10 kJ
- Projectile risk if panel ruptures
- Loud noise (>140 dB) if failure occurs

### 6.2 Precautions
- Remote monitoring (personnel > 10m from chamber)
- Lexan blast shields
- Video surveillance
- Emergency depressurization system
- Hearing protection required

---

## 7. DELIVERABLES

### 7.1 Test Report
- Executive summary with pass/fail
- Measured strain data
- Load-displacement curves
- Comparison with FEA predictions
- Photos and videos
- Recommendations

### 7.2 Data Package
- Raw strain gauge data
- Pressure time history
- Displacement measurements
- Acoustic emission records
- Post-test inspection report

---

## 8. SCHEDULE & COST

- **Duration:** 3 days
- **Cost:** $45,000
- **Status:** Awaiting prototype

---

## 9. REFERENCES

- CS-25.365 Pressurized compartment loads
- CS-25.561 Emergency landing conditions
- Door L1 Forward Stress Analysis (06_ENGINEERING/CALC-STR-001)

---

**Critical Path:** Required before fatigue testing
