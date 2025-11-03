# Test Procedure - Pressure Test Setup

**Procedure:** PROC-001  
**Revision:** DRAFT  
**Date:** 2025-11-03  
**Applies To:** TP-001 (Static), TP-002 (Proof), TP-003 (Fatigue)

---

## 1. SAFETY WARNINGS

⚠️ **PRESSURE HAZARD**
- Ultimate test: 17.0 psi = 295 kN total force
- Catastrophic failure energy: ~10 kJ
- **MANDATORY:** Clear all personnel from test area during pressurization
- Use remote monitoring only
- Barriers required within 10m radius

⚠️ **ACOUSTIC HAZARD**
- Sudden failure produces >140 dB sound
- Hearing protection mandatory for all personnel

⚠️ **PROJECTILE HAZARD**
- Failed components can become projectiles
- Lexan blast shields required
- Personnel behind barriers only

---

## 2. TEST ARTICLE PREPARATION

### 2.1 Pre-Test Inspection

#### Visual Inspection
- [ ] No visible damage (scratches, dents, cracks)
- [ ] All components present and properly installed
- [ ] No foreign objects or debris
- [ ] Surface finish per specification
- [ ] Paint/coating intact
- [ ] Labels and markings present

#### NDT Inspection
- [ ] Ultrasonic C-scan (100% coverage)
- [ ] Document any indications
- [ ] Verify core bond integrity
- [ ] Check for delaminations
- [ ] Measure skin thickness (5 locations)
- [ ] Archive all scan data

#### Dimensional Verification
- [ ] Overall dimensions ±2mm tolerance
- [ ] Seal groove depth and width
- [ ] Latch hole locations ±0.5mm
- [ ] Hinge mounting points
- [ ] Mass measurement (±0.5 kg)

#### Photographic Documentation
- [ ] 8 standard views (front, back, 4 edges, 2 angles)
- [ ] Close-ups of critical areas
- [ ] Serial number and identification
- [ ] Date and configuration

### 2.2 Instrumentation Installation

#### Strain Gauges (24 locations)

**Rosettes at Latch Points (8 locations):**
```
Locations: Each of 8 latch attachment points
Type: 3-element 0°/45°/90° rosette
Model: Vishay CEA-06-062UR-350
Installation:
1. Clean surface with acetone
2. Apply M-Bond 200 adhesive
3. Cure per manufacturer spec
4. Solder lead wires (3-wire quarter bridge)
5. Apply protective coating (M-Coat A)
6. Label each gauge (SG-L1 through SG-L8)
```

**Uniaxial at Mid-Panel (8 locations):**
```
Locations: 4×2 grid on panel center region
Type: Single element (0° or 90°)
Model: Vishay CEA-06-125UN-350
Orientation: 4 in 0° direction, 4 in 90° direction
Installation: Same as rosettes
Labels: SG-P1 through SG-P8
```

**Rosettes at Hinges (4 locations):**
```
Locations: 3 hinge points + 1 spare
Type: 3-element rosette
Installation: Same as latch points
Labels: SG-H1 through SG-H4
```

**Critical Stress Concentrations (4 locations):**
```
Locations: Per FEA analysis
Type: As required (rosette or uniaxial)
Labels: SG-C1 through SG-C4
```

#### Displacement Transducers (5 LVDTs)

**Panel Center:**
```
Location: Geometric center of panel
Type: LVDT (linear variable differential transformer)
Model: Micro-Epsilon WDS-2000
Range: 0-50 mm
Resolution: 0.01 mm
Mounting: Magnetic base on fixture, probe contact on panel
Label: LVDT-1
```

**Four Corners:**
```
Locations: 100mm from each corner
Type: Same as center
Range: 0-25 mm
Mounting: Same as center
Labels: LVDT-2 through LVDT-5
```

#### Pressure Sensors (3 units)

**Cabin Side Primary:**
```
Location: Inside pressure chamber, center
Type: Absolute pressure transducer
Model: Honeywell TJE (0-30 psi range)
Accuracy: ±0.1% FS
Output: 4-20 mA
Label: P-1
```

**Cabin Side Redundant:**
```
Location: Inside chamber, offset from primary
Type: Same as primary
Purpose: Redundancy for critical measurement
Label: P-2
```

**External Reference:**
```
Location: Outside chamber
Type: Barometric pressure sensor
Purpose: Atmospheric pressure reference
Label: P-3
```

#### Acoustic Emission (4 sensors)

**Purpose:** Early warning of crack initiation

```
Locations: 4 quadrants of panel
Type: Piezoelectric AE sensor
Model: Physical Acoustics Pico
Frequency: 100-1000 kHz
Mounting: Vacuum grease coupling
Labels: AE-1 through AE-4
```

### 2.3 Installation in Test Chamber

#### Test Fixture Preparation
1. Clean fixture mounting surfaces
2. Verify fixture integrity (no damage from previous tests)
3. Lubricate hinge pins per spec
4. Check latch mechanism operation
5. Verify seal groove cleanliness

#### Door Installation Sequence
1. Lift door with overhead crane (2-point lift)
2. Position door in fixture opening
3. Align hinge pins (bottom to top)
4. Install hinge hardware (torque to 50 N·m)
5. Verify hinge articulation (smooth, no binding)
6. Engage all 8 latches per operational sequence
7. Verify latch indicators (all green)
8. Install and inflate seals (5 psi seal pressure)
9. Verify seal contact (no gaps)

#### Instrumentation Connections
1. Route all cables with strain relief
2. Connect to data acquisition system
3. Verify channel assignments
4. Perform continuity checks
5. Zero all sensors
6. Record baseline readings

#### Safety Barriers
1. Install Lexan blast shields (4 panels, 10mm thick)
2. Position shields 2m from door, 360° coverage
3. Post warning signs and barricades
4. Verify remote camera views
5. Establish personnel exclusion zone (10m radius)

---

## 3. TEST SEQUENCE

### 3.1 Leak Check (0.5 psi)

**Purpose:** Verify chamber integrity before high-pressure test

1. **Close chamber:**
   - Secure door and all access panels
   - Verify all penetrations sealed
   - Check O-ring condition

2. **Pressurize slowly:**
   - Rate: 0.1 psi/min
   - Target: 0.5 psi
   - Monitor pressure sensor P-1

3. **Hold pressure:**
   - Duration: 10 minutes
   - Record pressure every 30 seconds
   - Calculate leak rate

4. **Acceptance:**
   - Leak rate < 0.1 CFM
   - If fail: locate and seal leaks, repeat

### 3.2 Proof Pressure Test (12.75 psi)

**Purpose:** Demonstrate no permanent deformation

1. **Pressurization:**
   ```
   Starting pressure: 0 psi
   Rate: 0.5 psi/min
   Target: 12.75 psi
   Duration: ~26 minutes
   ```

2. **Hold at proof:**
   - Duration: 3 minutes
   - Monitor all channels continuously
   - Watch for acoustic emission events
   - Record strain and displacement

3. **Depressurization:**
   ```
   Rate: 0.2 psi/min
   Target: 0 psi
   Duration: ~64 minutes
   ```

4. **Residual measurement:**
   - Wait 10 minutes for elastic recovery
   - Measure residual strain (must be <100 με)
   - Measure residual displacement (must be <0.5 mm)

### 3.3 Ultimate Pressure Test (17.0 psi)

⚠️ **CRITICAL - DESTRUCTIVE TEST**

1. **Pre-test verification:**
   - [ ] All personnel clear of test area
   - [ ] Remote monitoring operational
   - [ ] Safety barriers in place
   - [ ] Emergency depressurization ready
   - [ ] All instruments recording

2. **Pressurization to ultimate:**
   ```
   Starting pressure: 0 psi
   Rate: 0.5 psi/min
   Target: 17.0 psi
   Duration: ~34 minutes
   ```

3. **Hold at ultimate:**
   - **Minimum:** 3 seconds
   - **Maximum:** Until failure or 10 minutes
   - Monitor for signs of impending failure:
     - Acoustic emission spike
     - Strain exceeding 10,000 με
     - Displacement exceeding 50 mm
     - Unusual sounds (cracking, popping)
     - Visual deformation

4. **Emergency stop criteria:**
   - **STOP IMMEDIATELY IF:**
     - Acoustic emission count rate >100/sec
     - Strain >10,000 με
     - Displacement >50 mm
     - Visible crack propagation
     - Abnormal sounds
     - Safety concern

5. **Depressurization:**
   - Rate: 0.2 psi/min (if no failure)
   - Immediate dump if failure occurs

---

## 4. DATA RECORDING

### 4.1 Data Acquisition System

**Configuration:**
- System: NI PXI-8880 or equivalent
- Channels: 60 (24 strain + 5 displacement + 3 pressure + 4 AE + spares)
- Sample rate: 1000 Hz per channel
- Resolution: 24-bit
- Storage: Redundant (local + network)

**Recording Strategy:**
- Continuous recording during entire test
- Trigger: Pressure-based (start at 0.1 psi)
- Backup saves: Every 1 psi increment
- Post-test: Archive all data files

### 4.2 Video Recording

**Cameras:**
- High-speed camera: 1000 fps (for ultimate test)
- Standard cameras: 3 angles, 30 fps
- Infrared camera: Thermal monitoring (if available)

**Recording:**
- Start before pressurization
- Continue until depressurization complete
- Archive all video files

---

## 5. FAILURE CRITERIA

### 5.1 Automatic Stop Conditions

System shall automatically halt pressurization if:
- Strain exceeds 10,000 με
- Displacement exceeds 50 mm
- Acoustic emission spike (>100 events/sec)
- Pressure drop >0.5 psi/min (leak)

### 5.2 Manual Stop Authority

Test engineer shall stop test if:
- Any safety concern
- Unexpected behavior
- Equipment malfunction
- Personnel in exclusion zone

---

## 6. POST-TEST ACTIVITIES

### 6.1 Immediate (Within 1 hour)

1. **Depressurize slowly:**
   - Rate: 0.2 psi/min
   - Monitor for secondary failures

2. **Make safe:**
   - Verify 0 psi
   - Open chamber slowly
   - Approach test article cautiously
   - Inspect for hazards

3. **Initial documentation:**
   - Photos from all angles
   - Video walkthrough
   - Note any visible damage
   - Mark failure locations

### 6.2 Detailed Inspection (Day 1-2)

1. **Visual inspection:**
   - Document all damage
   - Measure crack lengths
   - Note delamination extent
   - Check seal condition
   - Inspect latches and hinges

2. **NDT inspection:**
   - Ultrasonic C-scan
   - Compare pre-test vs. post-test
   - Identify internal damage
   - Map delamination areas

3. **Measurement:**
   - Permanent deformation
   - Residual strains (if gauges intact)
   - Dimensional changes

4. **Remove instrumentation:**
   - Carefully remove strain gauges
   - Disconnect LVDTs
   - Inspect sensor mounting areas
   - Salvage reusable equipment

### 6.3 Analysis (Day 3-7)

1. **Data processing:**
   - Load all data files
   - Plot stress-strain curves
   - Create load-displacement curves
   - Analyze failure progression
   - Calculate margins

2. **Correlation:**
   - Compare with FEA predictions
   - Identify discrepancies
   - Update analysis models
   - Validate design assumptions

3. **Report preparation:**
   - Test report document
   - Data package
   - Recommendations

---

## 7. EQUIPMENT LIST

See: Test_Equipment_List.csv for complete inventory

---

## 8. REFERENCES

- TP-52-10-01-001 Static Ultimate Strength Test Plan
- TP-52-10-01-002 Proof Pressure Test Plan  
- TP-52-10-01-003 Fatigue Test Plan
- Door L1 Forward Stress Analysis (CALC-STR-001)

---

## 9. APPROVALS

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Test Engineer | | | |
| Safety Officer | | | |
| Quality Inspector | | | |

---

**Document Status:** DRAFT - For review only. Do not use for testing until approved.
