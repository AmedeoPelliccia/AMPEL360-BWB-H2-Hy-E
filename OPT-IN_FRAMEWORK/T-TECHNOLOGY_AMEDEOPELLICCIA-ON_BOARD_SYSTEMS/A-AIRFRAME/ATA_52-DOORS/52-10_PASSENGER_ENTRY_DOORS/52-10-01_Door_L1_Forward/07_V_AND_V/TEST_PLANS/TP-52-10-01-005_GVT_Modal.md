# Test Plan - Ground Vibration Test (GVT)
## Door L1 Forward Modal Survey

**Test Plan:** TP-52-10-01-005  
**Priority:** CRITICAL - MANDATORY BEFORE FLIGHT  
**Revision:** 1.0  
**Date:** 2025-11-03  
**Status:** Ready for Execution (Awaiting Hardware)

---

## 1. TEST OBJECTIVES

### 1.1 Primary Objective
Determine damping ratio at Mode 1 (≈25 Hz) to assess resonance risk with engine harmonic frequency.

### 1.2 Secondary Objectives
- Measure natural frequencies (first 5 modes)
- Identify mode shapes
- Quantify damping ratios for all modes
- Validate finite element analysis predictions
- Assess structural dynamic characteristics

### 1.3 Critical Requirement
**PASS/FAIL CRITERION:**
```
If ζ < 3.0% at Mode 1 → FAIL → REDESIGN REQUIRED
If ζ ≥ 3.0% at Mode 1 → PASS → Proceed to flight
```

**Rationale:** Engine operates at 25 Hz (1500 RPM). Insufficient damping at this frequency could lead to:
- Excessive vibration during flight
- Structural fatigue
- Passenger discomfort
- Potential airworthiness issue

---

## 2. TEST ARTICLE DESCRIPTION

### 2.1 Configuration
- Door L1 Forward complete assembly
- Panel dimensions: 2100 mm × 1200 mm
- Sandwich construction: CFRP face sheets + Nomex honeycomb
- Mass: 114 kg (estimated)
- Installed in fuselage test fixture

### 2.2 Boundary Conditions
- **Latches:** All 8 latches engaged (operational configuration)
- **Hinges:** 3 hinges connected to fixture
- **Seals:** Installed but not inflated
- **Cabin:** Unpressurized (atmospheric)
- **Support:** Rigid fixture simulating fuselage interface

### 2.3 As-Tested Configuration
Complete dimensional survey and mass properties measurement before test.

---

## 3. TEST SETUP

### 3.1 Excitation System

#### Shaker Configuration
- **Type:** Electrodynamic shaker
- **Model:** MB Dynamics Modal 50
- **Location:** Panel geometric center
- **Attachment:** Stinger rod (flexible coupling)
- **Direction:** Normal to surface (Z-axis)
- **Force capacity:** 220 N peak

#### Excitation Signal
- **Method:** Swept sine
- **Frequency range:** 5-500 Hz
- **Sweep rate:** 2 octaves/minute
- **Input level:** 0.1g constant acceleration
- **Repeat:** 3 sweeps for repeatability

### 3.2 Instrumentation

#### Accelerometers
- **Quantity:** 20 triaxial accelerometers
- **Type:** PCB 356A01 (or equivalent)
- **Sensitivity:** 100 mV/g
- **Frequency range:** 1-5000 Hz
- **Layout:** 4×5 grid on panel surface
- **Total channels:** 60 (20 sensors × 3 axes)

#### Grid Layout
```
     Column 1  Column 2  Column 3  Column 4  Column 5
Row 1   A1       A2        A3        A4        A5
Row 2   A6       A7        A8        A9        A10
Row 3   A11      A12       A13       A14       A15
Row 4   A16      A17       A18       A19       A20

Dimensions:
- Row spacing: 525 mm
- Column spacing: 420 mm
- Edge margin: 100 mm
```

#### Data Acquisition
- **System:** NI PXI-8880 (or equivalent)
- **Sampling rate:** 5000 Hz per channel
- **Anti-aliasing filter:** 2000 Hz (40% of sample rate)
- **Resolution:** 24-bit
- **Dynamic range:** >100 dB

---

## 4. TEST PROCEDURE

### 4.1 Pre-Test Activities

#### Installation (Day 1)
1. Position door in test fixture
2. Engage all latches per specification
3. Connect hinges with proper torque
4. Verify seal installation
5. Document as-installed configuration

#### Instrumentation (Day 2)
1. Mount accelerometers per grid layout
2. Apply adhesive mounting (beeswax or cyanoacrylate)
3. Route cables with strain relief
4. Connect to data acquisition system
5. Verify sensor orientation (X, Y, Z)

#### Calibration (Day 2)
1. Perform sensor calibration check
2. Verify excitation shaker force
3. Measure background noise
4. Establish baseline measurements
5. Document all calibration data

### 4.2 Test Execution

#### Phase 1: Low-Level Survey (Day 3)
```
Purpose: Identify resonance frequencies
Input: 0.05g swept sine, 5-500 Hz
Sweep rate: 2 oct/min
Duration: ~15 minutes per sweep
Repeat: 3 times
```

**Data Recording:**
- All 60 channels continuous
- Force input from shaker
- Frequency response functions (FRF)

**Analysis:**
- Peak picking to identify natural frequencies
- Preliminary damping estimation

#### Phase 2: Resonance Dwell (Day 3-4)
```
Purpose: Measure damping at each resonance
Method: Dwell at each identified frequency
Duration: 2 minutes per mode
Input: 0.1g constant level
```

**For Each Mode:**
1. Excite at resonance frequency
2. Achieve steady-state response
3. Record time history
4. Shut off excitation
5. Record free decay response
6. Measure decay rate (logarithmic decrement)

**Priority:** Mode 1 (≈25 Hz) is CRITICAL

#### Phase 3: Mode Shape Extraction (Day 4)
```
Purpose: Characterize mode shapes
Method: Multi-reference modal analysis
Excitation: Random burst or impact
Points: All 20 accelerometer locations
```

**Data Collection:**
- Phase relationships between sensors
- Amplitude distribution
- Transfer functions
- Coherence verification

### 4.3 Post-Test Activities (Day 5)
1. Remove instrumentation
2. Inspect test article for damage
3. Document any anomalies
4. Archive all raw data
5. Begin data analysis

---

## 5. DATA ANALYSIS

### 5.1 Frequency Identification

#### Method 1: Peak Picking
- Identify peaks in FRF magnitude
- Record frequency at maximum response
- Estimate uncertainty ±0.5 Hz

#### Method 2: Half-Power Bandwidth
- Measure frequencies at 3 dB down from peak
- Calculate center frequency
- Provides damping estimate

#### Method 3: Circle Fit (Nyquist Plot)
- Plot FRF in complex plane
- Fit circle to resonance region
- Extract frequency and damping

### 5.2 Damping Calculation

#### Logarithmic Decrement Method
```
From free decay response:
δ = ln(A₁/A₂)

Where:
A₁ = amplitude at peak 1
A₂ = amplitude at peak 2 (one cycle later)

Damping ratio:
ζ = δ / (2π)
```

#### Half-Power Bandwidth Method
```
ζ = Δf / (2 × fn)

Where:
Δf = f₂ - f₁ (half-power bandwidth)
fn = natural frequency
f₁, f₂ = frequencies at 3 dB down
```

#### Uncertainty Analysis
- Repeat measurements: 3 times per mode
- Calculate mean and standard deviation
- Report damping as: ζ ± σ
- Target uncertainty: ±15% on damping

### 5.3 Mode Shape Visualization
- Normalize to unit modal mass
- Create animation of mode shapes
- Identify nodal lines
- Classify mode types (bending, torsion, etc.)
- Compare with FEA predictions

---

## 6. ACCEPTANCE CRITERIA

### 6.1 Primary Criterion (CRITICAL)
**Mode 1 Damping:**
```
PASS: ζ₁ ≥ 3.0%
FAIL: ζ₁ < 3.0%
```

### 6.2 Secondary Criteria
- Frequency measurement uncertainty: ±10%
- Damping measurement uncertainty: ±15%
- Coherence > 0.9 for all measurements
- Repeatability: <5% variation between sweeps

### 6.3 Data Quality Requirements
- No sensor dropouts or failures
- Clean FRF curves (smooth, no noise spikes)
- Consistent results across 3 sweeps
- All 5 modes clearly identified

---

## 7. CONTINGENCY ACTIONS

### 7.1 If Mode 1 Damping < 3.0%

#### Option A: Increase Face Sheet Thickness
**Modification:**
- Change: 4mm → 5mm CFRP face sheets
- **Effect:** Mode 1 frequency increases to ≈27 Hz
- **Weight penalty:** +12 kg
- **Cost:** $80,000 (redesign + refabrication)
- **Schedule:** +6 weeks

**Evaluation:**
- Shifts resonance away from 25 Hz engine frequency
- Margin: 27 Hz / 25 Hz = 1.08 (8% separation)
- Still requires ζ ≥ 2.5% for acceptability

#### Option B: Add Constrained Layer Damping (CLD)
**Modification:**
- Material: Viscoelastic damping tape
- Coverage: 30% of panel area
- Locations: High strain regions (FEA guidance)
- **Effect:** Increases damping to 5-8%
- **Weight penalty:** +3 kg
- **Cost:** $15,000 (material + installation)
- **Schedule:** +2 weeks

**Evaluation:**
- Maintains current design geometry
- Minimal weight impact
- Proven technology
- Recommended first approach

#### Option C: Add Tuned Mass Dampers
**Modification:**
- Small masses at strategic locations
- Tuned to Mode 1 frequency
- **Effect:** Increases damping to 4-6%
- **Weight penalty:** +5 kg
- **Cost:** $25,000
- **Schedule:** +3 weeks

### 7.2 If Multiple Modes Have Low Damping
- Comprehensive damping treatment required
- May need material selection review
- Consider alternative core materials
- Full redesign may be necessary

### 7.3 If Frequency Differs Significantly from Predictions
- Update FEA model
- Verify mass and stiffness assumptions
- Check boundary conditions
- Re-run all structural analyses

---

## 8. DELIVERABLES

### 8.1 Test Report
**Document:** TR-52-10-01-005_GVT_Results/Test_Report.md

**Contents:**
1. Executive summary with pass/fail
2. Test configuration description
3. Instrumentation details
4. Measured natural frequencies (first 5 modes)
5. Damping ratios for all modes
6. Mode shapes with animations
7. Correlation with FEA predictions
8. Raw data files and processing scripts
9. Photos and videos of test setup
10. Recommendations for flight clearance

### 8.2 Data Package
- Raw time history data (HDF5 format)
- Frequency response functions (all channels)
- Modal parameters (frequencies, damping, mode shapes)
- Calibration certificates
- As-tested configuration drawings

### 8.3 Compliance Evidence
- Requirement RQ-52-10-01-018 verification
- CS-25 compliance demonstration
- Certification test data for authorities

---

## 9. SCHEDULE & RESOURCES

### 9.1 Duration
- **Setup:** 2 days
- **Testing:** 2 days
- **Analysis:** 3 days
- **Reporting:** 2 days
- **Total:** 9 days (2 weeks elapsed)

### 9.2 Cost Estimate
| Item | Cost |
|------|------|
| Test facility rental | $8,000 |
| Instrumentation | $5,000 |
| Test engineers (2) | $12,000 |
| Data analysis | $3,000 |
| Report preparation | $2,000 |
| **Total** | **$30,000** |

### 9.3 Personnel
- Lead test engineer (1)
- Instrumentation technician (1)
- Structural analyst (1)
- Quality inspector (1)

### 9.4 Equipment
See TEST_PROCEDURES/Test_Equipment_List.csv

---

## 10. SAFETY

### 10.1 Hazards
- Shaker reaction forces
- Electrical hazards (data acquisition)
- Tripping hazards (cables)
- Moving parts during excitation

### 10.2 Precautions
- Secure all cables and equipment
- Establish safety perimeter (2m radius)
- Use lockout/tagout procedures
- Personal protective equipment (safety glasses, hearing protection)
- Emergency stop button accessible

### 10.3 Emergency Procedures
- Kill power to shaker immediately if anomaly detected
- Evacuate test area if structural failure suspected
- First aid kit and fire extinguisher on site

---

## 11. REFERENCES

- CS-25.629 Aeroelastic stability requirements
- CS-25.305 Strength and deformation
- ARP 4754A Guidelines for Development of Civil Aircraft
- NASA TM-2000-209893 "Modal Testing Technology"
- Door L1 Forward Design Documentation (04_DESIGN/)
- Door L1 Forward Requirements (03_REQUIREMENTS/)

---

## 12. APPROVALS

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Test Engineer | TBD | | |
| Structures Lead | TBD | | |
| Chief Engineer | TBD | | |
| Quality Assurance | TBD | | |
| DER (Designated Engineering Representative) | TBD | | |

---

**Document Control:**
- **Classification:** Internal Use
- **Status:** Ready for Execution
- **Next Review:** After hardware availability
- **Critical Path Item:** YES - Must complete before first flight

---

*This test is MANDATORY for flight clearance due to Mode 1 resonance risk at engine harmonic frequency (25 Hz).*
