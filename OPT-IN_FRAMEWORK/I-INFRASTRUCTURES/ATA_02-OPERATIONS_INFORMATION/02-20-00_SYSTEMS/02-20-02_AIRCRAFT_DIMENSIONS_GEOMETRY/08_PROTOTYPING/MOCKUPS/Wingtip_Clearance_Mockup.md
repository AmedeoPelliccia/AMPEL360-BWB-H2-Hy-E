# Wingtip Clearance Mockup

**Component:** ATA 02-11-00 - AIRCRAFT_DIMENSIONS_GEOMETRY  
**Document Type:** Mockup Specification  
**Platform:** AMPEL360 BWB H2 Hy-E Q100 INTEGRA  
**Version:** 1.0  
**Date:** 2025-11-11  
**Status:** Development

---

## Purpose

This mockup defines the wingtip clearance testing apparatus for the Blended Wing Body aircraft. The BWB configuration presents unique challenges due to the integrated wing-body design and wide wingspan (65m), requiring careful analysis of wingtip clearances during ground operations, particularly during crosswind landings and taxiing.

---

## Mockup Overview

### Objectives

1. **Validate Wingtip Clearance**: Ensure adequate clearance during all ground operations
2. **Crosswind Landing**: Test maximum crosswind landing attitudes
3. **Taxiway Operations**: Verify clearances during turns and taxiing
4. **Wing Flex Simulation**: Model wing tip deflection under loading
5. **Obstacle Detection**: Validate proximity warning systems

### BWB-Specific Considerations

The blended wing body design introduces several unique factors:
- **Wide Wingspan**: 65m (ICAO Code E) requires careful ground handling
- **Winglet Configuration**: Upward-swept winglets increase effective height
- **Wing Flex**: Large span results in significant tip deflection
- **Banking Angle Limits**: Lower effective dihedral than conventional aircraft
- **Ground Effect**: Enhanced during landing due to wing-body integration

---

## Critical Parameters

### Wingtip Geometry

| Parameter | Left Wing | Right Wing | Units |
|-----------|-----------|------------|-------|
| Semi-span | 32.5 | 32.5 | m |
| Tip Chord | 2.8 | 2.8 | m |
| Tip Height (Static) | 6.5 | 6.5 | m |
| Winglet Height | 2.5 | 2.5 | m |
| Total Tip Height | 9.0 | 9.0 | m |
| Ground Clearance | 2.5 | 2.5 | m |

### Clearance Requirements

| Condition | Minimum Clearance | Design Clearance | Safety Factor |
|-----------|-------------------|------------------|---------------|
| Static (level) | 1.0 m | 2.5 m | 2.5× |
| Landing (touchdown) | 0.8 m | 2.0 m | 2.5× |
| Maximum Roll Angle | 0.5 m | 1.2 m | 2.4× |
| Taxiing (turns) | 1.5 m | 3.0 m | 2.0× |
| Crosswind Landing | 0.8 m | 1.5 m | 1.9× |

---

## Test Scenarios

### Scenario 1: Static Clearance Verification

**Purpose:** Baseline clearance measurement under all loading conditions

**Test Setup:**
- Aircraft positioned level on smooth surface
- All loading conditions (Empty, Typical, MTOW, MLW)
- No wind, no movement
- Full fuel and cargo loading variations

**Measurements:**
- Left wingtip ground clearance
- Right wingtip ground clearance
- Wingtip to wingtip symmetry
- Wing flex under static load

**Expected Results:**
- Clearance ≥ 2.5m ± 0.1m
- Left/right symmetry within 50mm
- Flex deflection < 200mm at MTOW

---

### Scenario 2: Crosswind Landing Simulation

**Purpose:** Validate clearances during maximum crosswind landing attitudes

**Test Setup:**
- Simulated 30 knot crosswind (maximum demonstrated)
- Landing attitude: 3° pitch, 5° roll (into wind)
- Touchdown vertical speed: 2 m/s
- Main gear first contact on windward side

**Critical Measurements:**
- Leeward wingtip clearance at touchdown
- Windward wingtip clearance during roll-out
- Time to level after touchdown
- Maximum dynamic wing flex

**Pass Criteria:**
- Leeward tip clearance ≥ 0.8m
- No ground contact events
- Smooth transition to level attitude

---

### Scenario 3: Taxiway Maneuvering

**Purpose:** Test clearances during ground turns and taxiing

**Test Configurations:**

#### Straight Taxiing
- Speed: 10-20 knots
- Roll angle: 0° (level)
- Side clearance to taxiway edge: ≥15m

#### 90° Turn (Standard Taxiway)
- Turning radius: 35m minimum
- Outer wingtip path radius: 67.5m
- Required taxiway width: 50m (Code E)
- Bank angle: 0° (level maintained)

#### 180° Turn (Loop)
- Turning radius: 40m minimum
- Maximum steering angle: 70°
- Wingtip clearance monitoring: Continuous
- Ground crew spotters: Required

**Measurements:**
- Wingtip trajectory during turns
- Minimum clearance to obstacles
- Steering angle vs. turn radius
- Pilot visibility of wingtips

---

### Scenario 4: Wing Deflection Under Load

**Purpose:** Characterize wing flex and its impact on tip clearance

**Test Matrix:**

| Load Case | Wing Load (kg) | Expected Deflection | Min. Clearance |
|-----------|----------------|---------------------|----------------|
| Empty | 12,000 | +150mm (upward) | 2.65m |
| Typical | 18,000 | 0mm (nominal) | 2.50m |
| MTOW | 22,000 | -200mm (downward) | 2.30m |
| MLW | 20,000 | -150mm (downward) | 2.35m |
| 2.5g Maneuver | 45,000 | +500mm (upward) | 3.00m |
| -1g Push-over | 0 | -100mm (downward) | 2.40m |

**Measurement Methods:**
- Optical tracking of wingtip position
- Strain gauges at wing root
- FEA correlation study
- Dynamic response analysis

---

## Mockup Configuration

### Physical Mockup (1:20 Scale)

#### Scale Model Specifications
- **Scale:** 1:20 (3.25m semi-span at scale)
- **Material:** Carbon fiber composite for realistic flex characteristics
- **Winglets:** Removable for configuration testing
- **Ground Plane:** Adjustable for simulated attitudes
- **Instrumentation:** 
  - 8× laser distance sensors per wingtip
  - 4× strain gauges per wing
  - 2× inclinometers for attitude
  - High-speed camera (1000 fps)

#### Test Platform
- **Motorized Roll Platform:** ±10° range, 0.1° accuracy
- **Pitch Platform:** ±15° range, 0.1° accuracy
- **Load Simulation:** Hydraulic jacks for wing loading
- **Wind Tunnel:** Optional crosswind simulation
- **Obstacle Array:** Movable posts for clearance testing

---

### Digital Simulation

#### FEA Model
- **Software:** ANSYS Mechanical with composite material models
- **Mesh:** 10mm element size at wingtips, 50mm at root
- **Boundary Conditions:** 
  - Fixed at center body attachment points
  - Aerodynamic pressure distribution
  - Gravitational loading
- **Analysis Types:**
  - Static structural for load deflection
  - Modal analysis for vibration modes
  - Transient analysis for landing impact

#### CFD Integration
- **Software:** ANSYS Fluent
- **Purpose:** Ground effect and crosswind loading
- **Mesh:** 20 million cells, refined near wingtips
- **Validation:** Wind tunnel test correlation

---

## Instrumentation and Data Acquisition

### Sensor Array

**Wingtip Clearance Sensors (16 total, 8 per side):**
- Type: Laser distance measurement
- Range: 0.5-10m
- Accuracy: ±5mm
- Sampling: 1000 Hz
- Mounting: Embedded in wingtip structure

**Wing Deflection Sensors (8 total, 4 per side):**
- Type: Strain gauge rosettes
- Location: 25%, 50%, 75%, 95% semi-span
- Range: ±2000 με
- Accuracy: ±1 με
- Sampling: 100 Hz

**Attitude Sensors:**
- Type: MEMS IMU (6-axis)
- Pitch/Roll Accuracy: ±0.05°
- Angular Rate: ±300°/s
- Sampling: 100 Hz

### Data Acquisition System

```
DAQ Specifications:
- Channels: 32 analog, 16 digital
- Resolution: 24-bit
- Sample Rate: 10 kHz aggregate
- Storage: SSD with 1TB capacity
- Interface: Ethernet (GigE)
- Software: LabVIEW Real-Time
```

---

## Test Procedures

### Pre-Test Checklist

- [ ] Calibrate all distance sensors
- [ ] Verify attitude platform zero position
- [ ] Check strain gauge baselines
- [ ] Set up obstacle array (if applicable)
- [ ] Configure data logging system
- [ ] Position high-speed cameras
- [ ] Brief test personnel on procedures
- [ ] Verify emergency stop functionality

### Test Execution

1. **Baseline Measurement**
   - Set aircraft to level attitude (0° pitch, 0° roll)
   - Record all sensor readings for 30 seconds
   - Document environmental conditions

2. **Attitude Sweep**
   - Incrementally adjust pitch: -5° to +10° in 1° steps
   - At each pitch angle, sweep roll: -5° to +5° in 1° steps
   - Hold each attitude for 10 seconds
   - Record minimum clearances

3. **Dynamic Testing**
   - Simulate landing impact (controlled drop test)
   - Measure dynamic deflection and recovery
   - Analyze high-speed video
   - Compare with FEA predictions

4. **Obstacle Clearance**
   - Position obstacles at representative distances
   - Execute simulated taxiway maneuvers
   - Verify proximity warning system activation
   - Document clearance margins

### Post-Test Activities

- [ ] Download and backup all data
- [ ] Generate preliminary plots
- [ ] Compare with acceptance criteria
- [ ] Identify any anomalies
- [ ] Schedule follow-up tests if needed
- [ ] Archive test configuration

---

## Acceptance Criteria

### Quantitative Criteria

| Parameter | Target | Acceptance Range | Measurement |
|-----------|--------|------------------|-------------|
| Static clearance | 2.5 m | 2.3 - 2.7 m | Laser sensor |
| Crosswind clearance | 1.5 m | ≥ 0.8 m | Dynamic measurement |
| Max wing deflection | 200 mm | ≤ 250 mm | Strain gauge + optical |
| Left/right symmetry | 0 mm | ± 50 mm | Differential measurement |
| Turn radius | 35 m | ≤ 40 m | GPS tracking |

### Qualitative Criteria

- ✓ No ground contact in any test scenario
- ✓ Smooth wing flex behavior (no oscillations)
- ✓ Proximity warnings activate appropriately
- ✓ Pilot visibility adequate for ground operations
- ✓ FEA model correlation within 10%

---

## Risk Mitigation

### Identified Risks

| Risk | Severity | Likelihood | Mitigation |
|------|----------|------------|------------|
| Wingtip ground strike | Critical | Low | Emergency stop system, conservative test envelope |
| Sensor failure | Moderate | Medium | Redundant sensors, pre-test calibration |
| Platform malfunction | Moderate | Low | Regular maintenance, fail-safe design |
| Wing damage (scale model) | Moderate | Medium | Load limiters, progressive testing |
| Data loss | Low | Low | Real-time backup, RAID storage |

### Safety Procedures

1. **Pre-Test Safety Brief:** All personnel aware of emergency procedures
2. **Emergency Stop:** Red button accessible from multiple locations
3. **Clearance Zone:** 5m perimeter around test apparatus
4. **Load Limits:** Automatic shutdown if loads exceed 110% design
5. **Witness Protection:** Safety glasses and hearing protection required

---

## Deliverables

### Hardware Deliverables
1. Fully instrumented 1:20 scale wing mockup
2. Motorized attitude test platform
3. Calibration certificates for all sensors
4. Obstacle array and accessories

### Data Deliverables
1. Raw sensor data (HDF5 format)
2. Processed clearance database
3. High-speed video footage
4. Wing deflection analysis

### Documentation Deliverables
1. Test Execution Report
2. Data Analysis Report
3. FEA Correlation Study
4. Recommendations for Full-Scale Aircraft

---

## Schedule

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Design | 3 weeks | Detailed mockup drawings |
| Procurement | 4 weeks | All materials and sensors |
| Fabrication | 6 weeks | Completed mockup |
| Assembly & Calibration | 2 weeks | Operational test rig |
| Testing | 3 weeks | Complete test matrix |
| Analysis | 2 weeks | Final reports |
| **Total** | **20 weeks** | Full package |

---

## References

- ICAO Annex 14 - Aerodromes, Code E Standards
- FAA AC 150/5300-13A - Airport Design
- EASA CS-25 - Large Aeroplanes Certification Specifications
- ATA 02-11-00 Requirements Document
- BWB Aerodynamic Analysis Report

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
| Structures Lead | TBD | ___________ | ______ |
| Flight Test Engineer | TBD | ___________ | ______ |
| Safety Manager | TBD | ___________ | ______ |

---

**Copyright © 2025 AMPEL360 Project. All Rights Reserved.**
