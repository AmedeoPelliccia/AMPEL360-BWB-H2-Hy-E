# Wind Tunnel Geometry Model Specifications

**Component:** ATA 02-11-00 - AIRCRAFT_DIMENSIONS_GEOMETRY  
**Document Type:** Technical Specification  
**Platform:** AMPEL360 BWB H2 Hy-E Q100 INTEGRA  
**Version:** 1.0  
**Date:** 2025-11-11  
**Status:** Development

---

## Purpose

This document specifies the requirements and configuration for wind tunnel testing of the 1:20 scale AMPEL360 Blended Wing Body geometry model. The testing aims to validate aerodynamic characteristics, verify CFD predictions, and optimize the external geometry for maximum performance.

---

## Test Objectives

### Primary Objectives

1. **Aerodynamic Coefficient Validation**
   - Measure lift, drag, and pitching moment vs. angle of attack
   - Validate CFD predictions (±10% accuracy target)
   - Establish aerodynamic database for flight simulation

2. **Stall Characteristics**
   - Identify stall angle and behavior
   - Assess stall progression (tip vs. root)
   - Evaluate post-stall recovery

3. **Control Surface Effectiveness**
   - Measure elevon control power
   - Assess rudder/fin effectiveness
   - Evaluate trim requirements

4. **Reynolds Number Effects**
   - Test range: Re = 1.0 - 3.0 × 10⁶
   - Boundary layer transition study
   - Scale effects correlation

### Secondary Objectives

1. **Flow Visualization**
   - Surface flow patterns (oil flow, tufts)
   - Boundary layer transition location
   - Separation and reattachment zones
   - Wingtip vortex characterization

2. **Pressure Distribution**
   - Chordwise pressure distribution (50 taps)
   - Spanwise load distribution
   - Validation of pressure-sensitive paint (PSP)

3. **Dynamic Stability**
   - Pitch damping (forced oscillation)
   - Roll damping
   - Unsteady aerodynamics

---

## Wind Tunnel Facility Requirements

### Facility Specification

**Recommended Facilities:**
- TU Delft Low Speed Wind Tunnel (Netherlands)
- NASA Langley 14×22 ft Wind Tunnel (USA)
- DLR Göttingen Wind Tunnel (Germany)
- Politecnico di Milano Wind Tunnel (Italy)

**Minimum Requirements:**
| Parameter | Requirement |
|-----------|-------------|
| Test Section Size | 4.0 m (W) × 3.0 m (H) minimum |
| Maximum Velocity | 80 m/s (M = 0.24) |
| Turbulence Intensity | < 0.5% |
| Flow Angularity | < 0.3° |
| Dynamic Pressure Range | 100 - 2500 Pa |
| Reynolds Number (based on MAC) | 1.0 - 3.0 × 10⁶ |

### Model Mounting

**Sting Mount Configuration:**
- **Type:** Rear sting mount through fuselage centerline
- **Mounting Location:** FS 22 (1100mm scale), BL 0, WL 400mm
- **Sting Diameter:** 80mm maximum
- **Angle of Attack Range:** -5° to +20°
- **Sideslip Range:** -10° to +10°

**Force Balance:**
- 6-component strain gauge balance
- Load ranges matched to expected forces
- Accuracy: ±0.1% of full-scale reading
- Natural frequency: >50 Hz (all components)

---

## Test Configuration Matrix

### Baseline Configuration Tests

| Test Series | Description | AoA Range | Sideslip | Configuration |
|-------------|-------------|-----------|----------|---------------|
| **A1** | Polar (clean) | -5° to +20° | 0° | Gear up, flaps 0° |
| **A2** | Polar (landing) | -5° to +20° | 0° | Gear down, flaps 15° |
| **A3** | Sideslip effects | 0°, 5°, 10° | -10° to +10° | Clean |
| **A4** | Reynolds sweep | 0°, 5°, 10° | 0° | Re = 1.0, 1.5, 2.0, 2.5, 3.0 × 10⁶ |

### Control Surface Deflection Tests

| Test Series | Control Surface | Deflection Range | AoA | Notes |
|-------------|-----------------|------------------|-----|-------|
| **B1** | Elevons (symmetric) | -20° to +20° | 0°, 5°, 10° | Pitch control |
| **B2** | Elevons (differential) | ±10° | 0°, 5° | Roll control |
| **B3** | Rudders | -25° to +25° | 0°, 5° | Yaw control |
| **B4** | Elevons + Rudders | Combined | 0°, 5° | Coordinated turn |

### Dynamic Testing

| Test Series | Description | Frequency | Amplitude | Parameters |
|-------------|-------------|-----------|-----------|------------|
| **C1** | Pitch oscillation | 0.5 - 5 Hz | ±5° | Pitch damping (Cmq + Cmα̇) |
| **C2** | Roll oscillation | 0.5 - 5 Hz | ±10° | Roll damping (Clp) |
| **C3** | Yaw oscillation | 0.5 - 5 Hz | ±10° | Yaw damping (Cnr) |

---

## Instrumentation Plan

### Force and Moment Measurement

**6-Component Balance:**

| Component | Range | Resolution |
|-----------|-------|------------|
| Lift (L) | ±500 N | 0.1 N |
| Drag (D) | ±100 N | 0.02 N |
| Side Force (Y) | ±100 N | 0.02 N |
| Rolling Moment (l) | ±50 Nm | 0.01 Nm |
| Pitching Moment (m) | ±50 Nm | 0.01 Nm |
| Yawing Moment (n) | ±50 Nm | 0.01 Nm |

**Sampling Rate:** 1000 Hz (time-averaged over 10 seconds for static tests)

### Pressure Measurement

**Surface Pressure Taps:**
- **Total Taps:** 50
- **Distribution:**
  - Centerline section: 15 taps (upper/lower)
  - Mid-span section (BL = ±800mm): 10 taps each
  - Tip section (BL = ±1500mm): 5 taps each

**Pressure Scanner:**
- Type: Scanivalve DSA 3217 (or equivalent)
- Channels: 64
- Range: ±10 psi (±69 kPa)
- Accuracy: ±0.05% FS
- Sample Rate: 500 Hz per channel

**Reference Pressure:**
- Static pressure: Measured upstream of test section
- Dynamic pressure: Pitot-static probe at test section

### Flow Visualization

**Tufts:**
- 100× wool tufts, 20mm length
- Attached with double-sided tape
- Locations: Distributed across upper surface
- Video recording: 2× HD cameras (60 fps)

**Oil Flow:**
- Mixture: Light mineral oil + fluorescent pigment
- Application: Spray on surface before run
- Lighting: UV lamps for fluorescence
- Photography: High-resolution DSLR (after run)

**Smoke Flow:**
- Smoke source: Smoke wire or rake upstream
- Illumination: Laser sheet
- Recording: High-speed camera (500 fps)
- Locations: Wing root, mid-span, tip regions

**Pressure-Sensitive Paint (PSP):**
- Paint: UniFIB or equivalent
- Excitation: UV LED array
- Imaging: 2× CCD cameras (16-bit)
- Calibration: In-situ pressure taps

---

## Test Procedures

### Pre-Test Activities

1. **Model Installation (Day 1)**
   - Mount model on sting
   - Level and align with facility axes
   - Install instrumentation cables
   - Perform balance calibration

2. **System Checks (Day 1)**
   - Pressure tap functionality (leak check)
   - Force balance zero reading
   - Data acquisition system test
   - Flow visualization camera setup

3. **Facility Calibration (Day 1)**
   - Empty tunnel calibration run
   - Determine wall corrections
   - Verify flow quality (velocity, turbulence)

### Test Execution

**Daily Routine:**
- **Morning:** Balance zero check, tunnel warm-up
- **Testing:** 4-6 hours of productive testing
- **Evening:** Data review, plan next day

**Typical Test Run (10 minutes):**
1. Set model attitude (AoA, sideslip)
2. Set control surface deflections (if applicable)
3. Tunnel speed ramp-up (20 seconds)
4. Stabilization period (10 seconds)
5. Data acquisition (10 seconds, time-averaged)
6. Tunnel speed ramp-down (20 seconds)
7. Save data, prepare next run

**Data Acquisition per Run:**
- Balance forces/moments (1000 Hz, 10 sec)
- Pressure taps (500 Hz, 10 sec)
- Tunnel conditions (100 Hz, 10 sec)
- Video (continuous, 60 fps)

### Post-Test Activities

1. **Model Inspection**
   - Visual check for damage
   - Dimensional verification (key features)
   - Photograph any observations

2. **Data Processing**
   - Convert raw voltages to engineering units
   - Apply tare corrections (sting, instrumentation)
   - Apply wall corrections (solid/wake blockage)
   - Non-dimensionalize (CL, CD, Cm, etc.)

3. **Preliminary Analysis**
   - Plot polars (CL vs. α, CD vs. CL, etc.)
   - Identify anomalies or outliers
   - Compare with CFD predictions
   - Generate test report

---

## Expected Results

### Aerodynamic Coefficients (Clean Configuration, Re = 2.5×10⁶)

| Condition | CL | CD | Cm | L/D |
|-----------|-----|-----|-----|-----|
| α = 0° | 0.35 | 0.022 | +0.015 | 15.9 |
| α = 5° | 0.65 | 0.035 | +0.005 | 18.6 |
| α = 10° | 0.95 | 0.055 | -0.010 | 17.3 |
| α = 14° (stall) | 1.15 | 0.085 | -0.025 | 13.5 |
| CL_max | 1.20 | — | — | — |

**Note:** These are CFD predictions; wind tunnel results will validate/correct.

### Flow Phenomena

**Expected Observations:**
- **Laminar-Turbulent Transition:** ~35% chord (upper), ~45% chord (lower)
- **Flow Separation (α > 12°):** Initiates at wing tip, progresses inboard
- **Wingtip Vortex:** Strong coherent vortex, visible in smoke visualization
- **Center Body Junction Flow:** Potential separation bubble at wing-body junction

### Reynolds Number Sensitivity

**Drag Coefficient Trend:**
- Re = 1.0×10⁶: CD₀ ≈ 0.025 (higher due to laminar separation bubble)
- Re = 2.5×10⁶: CD₀ ≈ 0.022 (nominal, fully turbulent)
- Re = 5.0×10⁶: CD₀ ≈ 0.020 (full-scale equivalent, projected)

**Scale Effect Correction:**
- Form factor method (ITTC recommendations)
- Transitional flow corrections
- Extrapolation to full-scale Re = 50×10⁶

---

## Data Deliverables

### Raw Data

1. **Force Balance Data:** Binary files (HDF5 format)
2. **Pressure Data:** CSV files (time-series)
3. **Tunnel Conditions:** Temperature, pressure, humidity logs
4. **Video Files:** MP4 format, HD resolution

### Processed Data

1. **Aerodynamic Database:** Excel workbook with all coefficients
   - Sheets: CL, CD, Cm, CY, Cl, Cn vs. α, β, δe, δr, δa
   - Includes uncertainty estimates (±σ)

2. **Polars and Plots:** PDF report with graphs
   - Lift curve (CL vs. α)
   - Drag polar (CD vs. CL)
   - Pitching moment (Cm vs. CL)
   - Control effectiveness (dCm/dδ vs. α)

3. **Flow Visualization Images:** High-resolution JPEGs
   - Tufts (10+ images per configuration)
   - Oil flow (5+ images)
   - Smoke flow (20+ images)
   - PSP false-color pressure maps (10+ images)

### Analysis Reports

1. **Test Summary Report (20 pages)**
   - Objectives and test matrix
   - Facility and model description
   - Results summary
   - Comparison with CFD
   - Conclusions and recommendations

2. **Detailed Technical Report (100 pages)**
   - Comprehensive data tables
   - All plots and visualizations
   - Uncertainty analysis
   - CFD validation study
   - Full-scale extrapolation

---

## Quality Assurance

### Data Quality Checks

**Real-Time Monitoring:**
- Balance load check (within range?)
- Repeatability check (run-to-run consistency)
- Symmetry check (left vs. right sideslip)
- Reynolds number verification

**Post-Processing Checks:**
- Moment reference center consistency
- Drag polar shape (CD vs. CL²)
- Pitching moment slope (Cmα)
- Static margin calculation

### Acceptance Criteria

| Parameter | Criterion | Action if Failed |
|-----------|-----------|------------------|
| Repeatability | σ(CL) < 0.005, σ(CD) < 0.001 | Repeat test point |
| Symmetry | CY, Cl, Cn ≈ 0 at β = 0° | Check model alignment |
| Balance Load | Within 80% of capacity | Reduce dynamic pressure |
| CFD Agreement | Within ±10% for CL, ±20% for CD | Investigate discrepancy |

---

## Schedule and Cost

### Test Campaign Duration

| Activity | Duration | Days |
|----------|----------|------|
| Model Transport & Install | 2 days | 1-2 |
| Facility Calibration | 1 day | 3 |
| Baseline Testing (Series A) | 5 days | 4-8 |
| Control Surface Testing (Series B) | 3 days | 9-11 |
| Dynamic Testing (Series C) | 2 days | 12-13 |
| Flow Visualization (Tuft, Oil, Smoke) | 2 days | 14-15 |
| PSP Testing | 2 days | 16-17 |
| Contingency / Repeat Tests | 2 days | 18-19 |
| Model Removal & Debrief | 1 day | 20 |
| **Total** | **20 days** | **3-4 weeks** |

### Budget Estimate

| Item | Cost (USD) |
|------|-----------|
| Tunnel Rental (20 days @ $5,000/day) | $100,000 |
| Personnel (2 engineers, 1 technician, 20 days) | $30,000 |
| Model Transport (shipping + insurance) | $5,000 |
| Instrumentation (PSP paint, tufts, etc.) | $8,000 |
| Data Processing & Analysis | $15,000 |
| Report Preparation | $10,000 |
| Contingency (10%) | $17,000 |
| **Total** | **$185,000** |

---

## Safety Considerations

### Model Integrity

- **Maximum Dynamic Pressure:** 2500 Pa (safety factor 2.0 on structural design)
- **Pre-Test Inspection:** Check for cracks, loose parts
- **In-Test Monitoring:** Video surveillance for vibration or distress
- **Emergency Shutdown:** Tunnel operator can instantly stop flow

### Personnel Safety

- Tunnel access restricted during operation
- Emergency stop buttons at multiple locations
- High-voltage PSP equipment: Qualified personnel only
- Chemical handling (oil, PSP paint): PPE required

---

## Related Documents

- 1-20_Scale_BWB_Geometry_Model.md
- Geometry_Model_Test_Results.csv
- AMPEL360 CFD Validation Report (TBD)
- ATA 02-11-00 Requirements Document

---

## Document Control

**Revision History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-11 | AMPEL360 Engineering | Initial release |

**Approval:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Aerodynamics Lead | TBD | ___________ | ______ |
| Test Engineer | TBD | ___________ | ______ |
| Project Manager | TBD | ___________ | ______ |

---

**Copyright © 2025 AMPEL360 Project. All Rights Reserved.**
