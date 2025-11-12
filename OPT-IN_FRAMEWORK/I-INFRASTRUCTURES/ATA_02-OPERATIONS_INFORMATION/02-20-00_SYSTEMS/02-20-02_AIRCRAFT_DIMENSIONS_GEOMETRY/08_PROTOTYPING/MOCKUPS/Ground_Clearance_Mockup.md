# Ground Clearance Mockup

**Component:** ATA 02-11-00 - AIRCRAFT_DIMENSIONS_GEOMETRY  
**Document Type:** Mockup Specification  
**Platform:** AMPEL360 BWB H2 Hy-E Q100 INTEGRA  
**Version:** 1.0  
**Date:** 2025-11-11  
**Status:** Development

---

## Purpose

This mockup document defines the ground clearance measurement and validation mockup for the Blended Wing Body (BWB) aircraft. The mockup is designed to validate critical clearance requirements during various aircraft attitudes and loading conditions.

---

## Mockup Overview

### Objectives

1. **Validate Minimum Clearances**: Verify that all critical points meet or exceed minimum clearance requirements
2. **Test Loading Conditions**: Evaluate clearances under Empty, Typical, MTOW, and MLW conditions
3. **Attitude Simulation**: Test pitch and roll attitudes within operational envelope
4. **Ground Contact Prevention**: Ensure no inadvertent ground contact during normal operations

### Scale and Scope

- **Scale:** 1:10 physical mockup or full-scale digital twin simulation
- **Critical Points:** 13 measurement locations
- **Loading Conditions:** 4 distinct weight scenarios
- **Attitude Range:** 
  - Pitch: -5° to +10°
  - Roll: -5° to +5°

---

## Critical Measurement Points

### Primary Clearance Points

| Point ID | Location | Nominal Clearance | Min. Acceptable | Criticality |
|----------|----------|-------------------|-----------------|-------------|
| CP-01 | Left Wingtip | 2.5 m | 1.0 m | HIGH |
| CP-02 | Right Wingtip | 2.5 m | 1.0 m | HIGH |
| CP-03 | Forward Belly | 1.8 m | 0.5 m | CRITICAL |
| CP-04 | Center Belly | 1.8 m | 0.5 m | CRITICAL |
| CP-05 | Aft Belly | 1.8 m | 0.5 m | CRITICAL |
| CP-06 | Left Engine Intake | 2.0 m | 0.5 m | CRITICAL |
| CP-07 | Right Engine Intake | 2.0 m | 0.5 m | CRITICAL |
| CP-08 | Aft Tail Tip | 3.2 m | 1.0 m | HIGH |
| CP-09 | Nose Gear Door | 1.5 m | 1.0 m | MEDIUM |
| CP-10 | Left Main Gear Door | 1.5 m | 1.0 m | MEDIUM |
| CP-11 | Right Main Gear Door | 1.5 m | 1.0 m | MEDIUM |
| CP-12 | Left TE Tip | 2.8 m | 1.5 m | MEDIUM |
| CP-13 | Right TE Tip | 2.8 m | 1.5 m | MEDIUM |

---

## Test Configuration

### Physical Mockup (1:10 Scale)

#### Materials
- **Structure:** Aluminum frame with acrylic body panels
- **Landing Gear:** Adjustable hydraulic simulators for compression modeling
- **Sensors:** Digital distance sensors (accuracy ±1mm at scale)
- **Ground Plane:** Level granite surface plate with reference grid

#### Measurement System
- **Primary:** Laser distance sensors (13 locations)
- **Secondary:** Contact probes for verification
- **Data Acquisition:** Real-time logging at 100 Hz
- **Visualization:** Live 3D clearance display

#### Adjustable Parameters
- **Pitch Control:** ±15° using motorized platform
- **Roll Control:** ±10° using motorized platform
- **Gear Compression:** 0-150mm (scale) via hydraulic system
- **Loading:** Ballast weights for different loading conditions

### Digital Twin Simulation

#### Software Tools
- **CAD Model:** CATIA V6 with full surface definition
- **FEA Integration:** ANSYS for structural deflection analysis
- **Visualization:** Custom Python tool (Ground_Clearance_Prototype_Tool_v1.py)
- **Validation:** Cross-check with physical mockup data

#### Simulation Parameters
- **Mesh Resolution:** 5mm element size for critical areas
- **Contact Detection:** Penetration tolerance 0.1mm
- **Material Properties:** Composite structures with realistic stiffness
- **Ground Plane:** Rigid surface with friction coefficient μ=0.8

---

## Test Matrix

### Loading Conditions

| Condition | Weight (kg) | CG Location (FS) | Gear Compression |
|-----------|-------------|------------------|------------------|
| Empty | 45,000 | FS 21.5 | Minimal (5%) |
| Typical | 68,000 | FS 22.0 | Normal (100%) |
| MTOW | 85,000 | FS 22.5 | Maximum (110%) |
| MLW | 75,000 | FS 22.3 | High (105%) |

### Attitude Test Cases

| Test Case | Pitch (°) | Roll (°) | Loading | Expected Result |
|-----------|-----------|----------|---------|-----------------|
| TC-01 | 0 | 0 | Typical | All clearances > min |
| TC-02 | +5 | 0 | MTOW | Forward belly critical |
| TC-03 | -3 | 0 | Empty | Tail clearance reduced |
| TC-04 | 0 | +3 | Typical | Right wing reduced |
| TC-05 | 0 | -3 | Typical | Left wing reduced |
| TC-06 | +7 | +2 | MTOW | Combined worst case |
| TC-07 | -5 | -3 | Empty | Alternate worst case |
| TC-08 | +10 | 0 | MTOW | Extreme nose-up |
| TC-09 | 0 | +5 | MTOW | Extreme right roll |
| TC-10 | 0 | -5 | MTOW | Extreme left roll |

---

## Acceptance Criteria

### Pass/Fail Thresholds

**PASS Criteria:**
- All CRITICAL points maintain ≥0.5m clearance under all test cases
- All HIGH priority points maintain ≥1.0m clearance under normal operations
- No contact detected in any test case
- Measurement repeatability within ±5% (physical mockup) or ±1% (digital twin)

**WARNING Criteria:**
- Any clearance within 20% of minimum threshold
- Clearance margin <0.3m for CRITICAL points
- Unexpected clearance reductions compared to baseline

**FAIL Criteria:**
- Any ground contact event
- CRITICAL point clearance <0.5m
- HIGH priority clearance <0.8m under normal operations
- Measurement system failure or data corruption

---

## Mockup Construction Plan

### Phase 1: Design and Procurement (4 weeks)
- [ ] Finalize 1:10 scale CAD model
- [ ] Design adjustable platform system
- [ ] Procure sensors and data acquisition hardware
- [ ] Order structural materials

### Phase 2: Assembly (3 weeks)
- [ ] Construct aluminum frame
- [ ] Install motorized pitch/roll platform
- [ ] Mount acrylic body panels
- [ ] Install sensor array
- [ ] Integrate hydraulic gear simulation

### Phase 3: Calibration (2 weeks)
- [ ] Calibrate all distance sensors
- [ ] Verify pitch/roll platform accuracy
- [ ] Test data acquisition system
- [ ] Establish baseline measurements

### Phase 4: Testing (3 weeks)
- [ ] Execute test matrix
- [ ] Collect and analyze data
- [ ] Compare with digital twin
- [ ] Document findings

### Phase 5: Validation (2 weeks)
- [ ] Cross-validate physical and digital results
- [ ] Generate validation report
- [ ] Identify any design changes needed
- [ ] Archive data and mockup

---

## Instrumentation Specifications

### Distance Sensors

| Parameter | Specification |
|-----------|---------------|
| Type | Laser triangulation |
| Range | 50-500mm (scaled) |
| Accuracy | ±0.5mm |
| Resolution | 0.1mm |
| Sample Rate | 100 Hz |
| Output | 4-20mA analog |

### Attitude Sensors

| Parameter | Specification |
|-----------|---------------|
| Type | MEMS inclinometer |
| Pitch Range | ±15° |
| Roll Range | ±10° |
| Accuracy | ±0.1° |
| Resolution | 0.01° |
| Output | Digital (CAN bus) |

---

## Data Collection and Analysis

### Data Format

```
Timestamp, Test_Case, Pitch, Roll, Loading, CP01, CP02, CP03, ..., CP13, Pass/Fail
2025-11-11T10:00:00, TC-01, 0.0, 0.0, Typical, 2.51, 2.49, 1.82, ..., 2.79, PASS
```

### Analysis Methods

1. **Statistical Analysis:**
   - Mean, standard deviation, min/max for each clearance point
   - Correlation between attitude and clearance reduction
   - Confidence intervals (95%)

2. **Comparative Analysis:**
   - Physical mockup vs. digital twin
   - Expected vs. measured clearances
   - Worst-case identification

3. **Visualization:**
   - 3D clearance envelope plots
   - Time-series clearance data
   - Heat maps for critical zones

---

## Risk Assessment

### Potential Issues

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Sensor calibration drift | Medium | Medium | Daily calibration checks |
| Platform alignment error | Low | High | Precision alignment fixtures |
| Data acquisition failure | Low | High | Redundant DAQ system |
| Model-to-mockup deviation | Medium | Medium | Regular correlation updates |
| Unexpected ground contact | Low | Critical | Emergency stop system |

---

## Deliverables

1. **Physical Mockup:** Fully instrumented 1:10 scale model
2. **Test Data:** Complete dataset from all test cases
3. **Validation Report:** Comparison of physical and digital results
4. **Clearance Database:** Tabulated clearance values for all conditions
5. **Recommendations:** Design modifications if needed

---

## Related Documents

- Ground_Clearance_Prototype_Tool_v1.py
- Geometry_Envelope_Tool_v1.py
- ATA 02-11-00 Requirements Document
- BWB Structural Deflection Analysis

---

## Document Control

**Revision History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-11 | AMPEL360 Engineering | Initial release |

**Approval:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Lead Engineer | TBD | ___________ | ______ |
| Test Manager | TBD | ___________ | ______ |
| Quality Assurance | TBD | ___________ | ______ |

---

**Copyright © 2025 AMPEL360 Project. All Rights Reserved.**
