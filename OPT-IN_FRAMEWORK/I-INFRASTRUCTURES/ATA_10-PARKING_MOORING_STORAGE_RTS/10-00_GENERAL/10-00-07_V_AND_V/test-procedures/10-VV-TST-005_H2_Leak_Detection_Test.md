# 10-VV-TST-005 - H2 Leak Detection System Test Procedure

## 1. Test Identification

| Parameter | Value |
|-----------|-------|
| **Test Procedure Number** | 10-VV-TST-005 |
| **Test Type** | Functional / Safety Critical |
| **Verification Method** | Test |
| **System/Subsystem** | ATA 10 - H2 Leak Detection System |
| **Revision** | A |
| **Date** | 2025-12-10 |
| **Status** | Draft |
| **Safety Critical** | **YES** |

## 2. Purpose

### 2.1 Objective
To verify that the hydrogen leak detection system:
1. Detects hydrogen gas at or below 0.4% concentration (10% Lower Explosive Limit)
2. Responds within 2 seconds of leak initiation
3. Activates alarms and safety interlocks within 3 seconds
4. Operates reliably across all environmental conditions
5. Provides redundant detection in critical areas

### 2.2 Acceptance Criteria
- **Detection Threshold**: ≤0.4% H2 concentration (10% LEL = 0.4% H2 by volume)
- **Response Time**: ≤2 seconds from leak start to detection
- **Alarm Activation**: ≤3 seconds from detection to alarm
- **False Alarm Rate**: Zero false alarms during 8-hour monitoring period
- **Redundancy**: All redundant sensors functional
- **Environmental Range**: Function from -40°C to +55°C

## 3. Scope

### 3.1 Applicability
- **Aircraft**: AMPEL360-BWB-H2 (All variants)
- **System**: H2 Leak Detection System
- **Test Article**: Production-representative sensors and control unit
- **Monitoring Zones**: All zones around LH2 tank and distribution system

### 3.2 Test Limitations
- Tests conducted with H2 gas, not LH2
- Controlled environment testing
- Does not include full aircraft integration (separate test)

## 4. Requirements Verified

| Requirement ID | Requirement Description | Verification Method | Acceptance Criteria |
|----------------|-------------------------|---------------------|---------------------|
| RQ-10-30-HSF-001 | Detect H2 at ≥0.4% concentration | Test | Detection at 0.4% ± 0.05% |
| RQ-10-30-HSF-002 | Response time ≤2 seconds | Test | Timed response ≤2.0 sec |
| RQ-10-30-HSF-003 | Alarm activation within 3 seconds | Test | Alarm ≤3.0 sec from detection |
| RQ-10-30-HSF-004 | Redundant sensors in critical zones | Inspection + Test | All redundant sensors functional |
| RQ-10-30-HSF-005 | Sensor self-test capability | Test | Self-test detects failures |

## 5. Test Setup

### 5.1 Test Article

**H2 Detection System Components:**
- Part Number: [PN-TBD]
- Serial Numbers: [SN-TBD]
- Configuration: Production-representative
- Quantity: Complete zone coverage (estimated 8-12 sensors)

**Sensor Specifications:**
- Type: Catalytic bead or electrochemical
- Range: 0-4% H2 (0-100% LEL)
- Accuracy: ±0.1% H2
- Response time: <1 second (manufacturer spec)

### 5.2 Test Equipment and Instrumentation

| Equipment ID | Description | Specification | Calibration Due | Status |
|--------------|-------------|---------------|-----------------|--------|
| H2-CAL-001 | H2 Calibration Gas Cylinder | 0.4% H2 in air, certified | [Date] | [TBD] |
| H2-CAL-002 | H2 Calibration Gas Cylinder | 1.0% H2 in air, certified | [Date] | [TBD] |
| H2-CAL-003 | H2 Calibration Gas Cylinder | 2.0% H2 in air, certified | [Date] | [TBD] |
| FLW-001 | Mass Flow Controller | 0-10 SLPM, ±2% accuracy | [Date] | [TBD] |
| TIM-001 | High-accuracy timer | ±0.01 second | [Date] | [TBD] |
| DAQ-001 | Data Acquisition System | 100 Hz sampling | [Date] | [TBD] |
| TEMP-001 | Temperature Chamber | -40°C to +60°C | [Date] | [TBD] |
| HUM-001 | Humidity Chamber | 10-95% RH | [Date] | [TBD] |
| H2-MON-001 | Independent H2 Monitor | Safety backup | [Date] | [TBD] |

### 5.3 Test Facility

**Location**: H2-Qualified Test Facility [TBD]

**Environmental Requirements:**
| Parameter | Requirement | Tolerance | Notes |
|-----------|-------------|-----------|-------|
| Temperature (ambient) | 20°C | ±5°C | For baseline tests |
| Humidity | 50% RH | ±20% | For baseline tests |
| Ventilation | ≥6 ACH | N/A | Continuous during testing |
| Air velocity | <0.5 m/s | N/A | Minimize drift during release |

### 5.4 Test Configuration

**Test Chamber Setup:**
```
┌────────────────────────────────────┐
│  Test Chamber (2m x 2m x 2m)       │
│                                    │
│  [Sensor Under Test]               │
│         ↑                          │
│         │ 0.5m                     │
│         │                          │
│    [H2 Release Point]              │
│                                    │
│  [Exhaust Vent] ←──────────────── │
│                                    │
└────────────────────────────────────┘
```

**H2 Release System:**
- Controlled release via mass flow controller
- Release point 0.5m below sensor (H2 rises)
- Release rate variable: 0.1 to 2.0 SLPM
- Shut-off valve for emergency stop

## 6. Safety Precautions

### 6.1 DANGER - HYDROGEN GAS HAZARDS

⚠️ **CRITICAL SAFETY WARNINGS** ⚠️

**HYDROGEN IS:**
- Extremely flammable (LEL 4%, UEL 75%)
- Colorless, odorless, and invisible
- Lighter than air (rapid dispersion and accumulation at ceiling)
- Wide flammability range
- Low ignition energy (0.02 mJ)
- Can cause asphyxiation in confined spaces

**FAILURE TO FOLLOW SAFETY PROCEDURES CAN RESULT IN:**
- Fire or explosion
- Serious injury or death
- Facility damage

### 6.2 Personnel Requirements

**Minimum Personnel**: 3
1. Test Engineer (lead)
2. Safety Officer (H2-qualified)
3. Test Technician

**Required Qualifications:**
- H2 safety training (minimum 8-hour course)
- Facility safety orientation
- Emergency response training
- CPR/First Aid certification (at least one person)

**Personal Protective Equipment (PPE):**
- [ ] Safety glasses with side shields (mandatory)
- [ ] Flame-resistant lab coat or coveralls
- [ ] Closed-toe leather shoes (no synthetic materials)
- [ ] Natural fiber clothing (no synthetics)
- [ ] Static-dissipative footwear
- [ ] NO metal jewelry, watches, or conductive items

### 6.3 Facility Safety Requirements

**Before Test Begins:**
- [ ] Facility H2 monitoring system operational (independent of test article)
- [ ] Ventilation system running at ≥6 air changes/hour
- [ ] Fire suppression system armed and tested
- [ ] Emergency lighting functional
- [ ] Emergency exits clear and marked
- [ ] Explosion-proof electrical equipment only
- [ ] All ignition sources eliminated within 25 feet:
  - [ ] No open flames
  - [ ] No smoking
  - [ ] No static-generating materials
  - [ ] No spark-producing tools
  - [ ] Bonding/grounding verified
- [ ] Exclusion zone established (25-foot radius)
- [ ] Warning signs posted
- [ ] Fire extinguishers accessible (Class B)

### 6.4 H2 Cylinder Safety

**H2 Gas Cylinder Handling:**
- [ ] Cylinders secured to wall/stand (chain or strap)
- [ ] Cylinders stored upright
- [ ] Cylinder valves closed when not in use
- [ ] Regulators rated for H2 service
- [ ] No oil or grease on fittings
- [ ] Leak check all connections with soap solution (never flame)
- [ ] Never exceed cylinder pressure rating

### 6.5 Emergency Procedures

**IN CASE OF H2 LEAK (other than controlled release):**
1. **STOP** - Cease all operations immediately
2. **NOTIFY** - Alert all personnel: "Hydrogen Leak!"
3. **EVACUATE** - Leave area immediately, do not run
4. **ISOLATE** - Close H2 cylinder valve if safe to do so
5. **VENTILATE** - Ensure ventilation system running
6. **CALL EMERGENCY** - Dial [Emergency Number]
7. **DO NOT RE-ENTER** until facility safety officer clears area

**IN CASE OF FIRE:**
1. **EVACUATE** immediately
2. **ACTIVATE** fire alarm
3. **CALL** emergency services: [Emergency Number]
4. **DO NOT** attempt to fight H2 fire unless specifically trained
5. **SHUT OFF** H2 supply if safe and possible

**IN CASE OF INJURY:**
1. **EVACUATE** injured person from hazard area
2. **PROVIDE** first aid if trained
3. **CALL** medical emergency: [Emergency Number]

**Emergency Contacts:**
- **Test Director**: [Name, Phone]
- **Safety Officer**: [Name, Phone]
- **Facility Emergency**: [Phone]
- **Fire Department**: [Phone]
- **Medical Emergency**: 911 or [Local]

### 6.6 Test-Specific Safety

**During H2 Release:**
- [ ] Continuous monitoring with independent H2 detector
- [ ] Safety officer monitoring at all times
- [ ] Ready to shut off H2 supply instantly
- [ ] Maximum H2 concentration: 2% (50% LEL) in chamber
- [ ] If concentration exceeds 2%, stop test immediately
- [ ] Purge chamber between tests (5 minutes minimum)

## 7. Test Prerequisites

### 7.1 Pre-Test Checklist

**Documentation:**
- [ ] Test procedure reviewed and approved
- [ ] Safety plan reviewed by all personnel
- [ ] Emergency procedures briefed
- [ ] Data sheets prepared

**Equipment:**
- [ ] All test equipment calibrated and certified
- [ ] H2 cylinders inspected and secured
- [ ] Independent H2 monitor operational
- [ ] Data acquisition system tested
- [ ] Test article installed and connected
- [ ] Power supply verified (intrinsically safe)

**Facility:**
- [ ] Ventilation system operational and verified
- [ ] Fire suppression system armed
- [ ] Emergency lighting tested
- [ ] Exclusion zone established
- [ ] Warning signs posted
- [ ] Access controlled

**Personnel:**
- [ ] All personnel briefed on safety
- [ ] PPE donned and inspected
- [ ] Roles and responsibilities assigned
- [ ] Emergency procedures reviewed

### 7.2 Configuration Verification

**Verify:**
- [ ] Sensor installation matches design
- [ ] Sensor positioning correct per drawing
- [ ] Wiring connections correct
- [ ] Power supply correct voltage
- [ ] Grounding verified
- [ ] No damage to sensors or wiring
- [ ] Sensor labels legible and correct

## 8. Test Procedure

### 8.1 Pre-Test Operations

#### Step 1: System Power-Up and Self-Test
**Action:**
1. Apply power to H2 detection system
2. Observe system boot sequence
3. Initiate self-test function
4. Record results

**Expected Result:**
- System powers up without errors
- Self-test completes successfully
- All sensors report "ready" status
- No alarms activated

**Pass/Fail Criteria:**
- All sensors pass self-test
- System ready indication displayed

**Data to Record:**
- Power-up time
- Self-test results for each sensor
- Any error messages

---

#### Step 2: Baseline Reading
**Action:**
1. Allow system to stabilize (15 minutes)
2. Record baseline readings from all sensors
3. Verify zero or ambient reading

**Expected Result:**
- All sensors read 0% H2 or stable ambient
- No drift observed
- Readings consistent across sensors

**Pass/Fail Criteria:**
- Readings <0.1% H2
- Drift <0.05% over 15 minutes

**Data to Record:**
- Initial reading each sensor
- Final reading each sensor (after 15 min)
- Ambient temperature and humidity

---

### 8.2 Functional Tests - Detection Threshold

#### Test 3: 0.2% H2 Detection (Below Threshold)
**Purpose**: Verify no false alarm below detection threshold

| Parameter | Value |
|-----------|-------|
| H2 Concentration | 0.2% (5% LEL) |
| Flow Rate | 0.5 SLPM |
| Duration | 60 seconds |
| Expected | Detection but no alarm |

**Procedure:**
1. Start data acquisition
2. Open H2 flow to 0.5 SLPM
3. Monitor sensor readings
4. Observe for 60 seconds
5. Close H2 valve
6. Purge chamber for 5 minutes
7. Record results

**Pass/Fail Criteria:**
- Sensor detects H2
- Reading approximately 0.2% ± 0.1%
- **NO ALARM** activated (below threshold)

---

#### Test 4: 0.4% H2 Detection (At Threshold)
**Purpose**: Verify alarm at specified threshold

| Parameter | Value |
|-----------|-------|
| H2 Concentration | 0.4% (10% LEL) |
| Flow Rate | 1.0 SLPM |
| Duration | Until alarm |
| Expected | Alarm activation |

**Procedure:**
1. Start data acquisition and timer
2. Open H2 flow to achieve 0.4% concentration
3. Record time when H2 flow starts (T0)
4. Record time when sensor detects 0.4% (T1)
5. Record time when alarm activates (T2)
6. Close H2 valve after alarm confirmed
7. Purge chamber for 5 minutes

**Timing Requirements:**
- Response Time (T1 - T0): ≤2.0 seconds
- Alarm Time (T2 - T1): ≤3.0 seconds
- Total Time (T2 - T0): ≤5.0 seconds

**Pass/Fail Criteria:**
- Alarm activates
- Response time ≤2.0 sec
- Alarm activation ≤3.0 sec from detection

---

#### Test 5: 1.0% H2 Detection (Above Threshold)
**Purpose**: Verify rapid response to higher concentration

| Parameter | Value |
|-----------|-------|
| H2 Concentration | 1.0% (25% LEL) |
| Flow Rate | 2.0 SLPM |
| Duration | Until alarm |
| Expected | Rapid alarm activation |

**Procedure:** [Same as Test 4]

**Pass/Fail Criteria:**
- Alarm activates even faster than at threshold
- Response time ≤1.5 sec
- System shows urgency (e.g., faster alarm rate)

---

### 8.3 Response Time Tests

#### Test 6-10: Repeated Response Time Measurements
**Purpose**: Verify consistent response time (5 trials)

Repeat Test 4 five times to establish statistical confidence:
- Trial 1: [Record times]
- Trial 2: [Record times]
- Trial 3: [Record times]
- Trial 4: [Record times]
- Trial 5: [Record times]

**Statistical Analysis:**
- Calculate mean response time
- Calculate standard deviation
- Verify all trials pass criteria
- 95% confidence interval within specification

---

### 8.4 Redundancy Tests

#### Test 11: Single Sensor Failure Simulation
**Purpose**: Verify redundant coverage

**Procedure:**
1. Disable one sensor (simulate failure)
2. Perform Test 4 (0.4% H2 release)
3. Verify remaining sensors detect and alarm
4. Re-enable sensor
5. Repeat for each sensor in redundant pair

**Pass/Fail Criteria:**
- System continues to function with one sensor failed
- Alarm activates from redundant sensor
- System indicates sensor failure

---

### 8.5 Environmental Tests

#### Test 12: Low Temperature (-20°C)
**Purpose**: Verify operation at low temperature

**Procedure:**
1. Place sensors in cold chamber
2. Stabilize at -20°C (30 minutes)
3. Perform Test 4 (0.4% H2 detection)
4. Record performance

**Pass/Fail Criteria:**
- Sensors function at -20°C
- Response time ≤2.5 sec (slightly relaxed)
- Alarm activates

*Note: Full -40°C test requires special chamber, document separately*

---

#### Test 13: High Temperature (+45°C)
**Purpose**: Verify operation at elevated temperature

**Procedure:**
1. Place sensors in warm chamber
2. Stabilize at +45°C (30 minutes)
3. Perform Test 4 (0.4% H2 detection)
4. Record performance

**Pass/Fail Criteria:**
- Sensors function at +45°C
- Response time ≤2.5 sec (slightly relaxed)
- Alarm activates

---

#### Test 14: High Humidity (90% RH)
**Purpose**: Verify operation in humid conditions

**Procedure:**
1. Place sensors in humidity chamber
2. Stabilize at 90% RH (1 hour)
3. Perform Test 4 (0.4% H2 detection)
4. Record performance

**Pass/Fail Criteria:**
- Sensors function at 90% RH
- No moisture-related failures
- Alarm activates

---

### 8.6 False Alarm Tests

#### Test 15: 8-Hour Stability Test
**Purpose**: Verify no false alarms

**Procedure:**
1. Power up system
2. Monitor for 8 continuous hours
3. No H2 introduced
4. Record any alarms

**Pass/Fail Criteria:**
- **ZERO** false alarms in 8 hours
- Stable readings throughout

---

### 8.7 Post-Test Operations

**Step 1: System Shutdown**
- Verify no H2 in chamber (<0.1%)
- Power down detection system
- Close all H2 cylinder valves
- Remove and secure test article

**Step 2: Data Backup**
- Save all data files
- Backup to secure location
- Verify data integrity

**Step 3: Facility Securing**
- Verify ventilation continues
- Monitor for 30 minutes after test
- Secure H2 cylinders
- Remove exclusion zone signage

## 9. Data Recording and Analysis

### 9.1 Data to be Collected

| Data Item | Measurement Method | Recording Frequency | Accuracy Required |
|-----------|-------------------|---------------------|-------------------|
| H2 concentration | Sensor output | 10 Hz | ±0.05% |
| Response time | High-speed timer | Per event | ±0.01 sec |
| Alarm activation | Digital I/O | Per event | ±0.01 sec |
| Temperature | Thermocouple | 1 Hz | ±1°C |
| Humidity | RH sensor | 1 Hz | ±5% RH |

### 9.2 Statistical Analysis

For repeated tests, calculate:
- Mean response time
- Standard deviation
- 95% confidence interval
- Maximum and minimum values
- Pass rate (percentage of trials passing)

## 10. Pass/Fail Criteria Summary

### 10.1 Overall Test Acceptance

**Test PASSES if:**
- ✅ All sensors detect 0.4% H2
- ✅ Response time ≤2.0 seconds (95% of trials)
- ✅ Alarm activation ≤3.0 seconds from detection
- ✅ Zero false alarms during 8-hour test
- ✅ Redundant sensors provide backup
- ✅ Function across environmental range
- ✅ No safety incidents

**Test FAILS if:**
- ❌ Any sensor fails to detect 0.4% H2
- ❌ Response time >2.0 seconds (any trial)
- ❌ Alarm fails to activate
- ❌ Any false alarms occur
- ❌ Redundancy not effective
- ❌ Environmental limits exceeded

## 11. Test Results Documentation

Results documented in: **10-VV-RPT-003_H2_Safety_Test_Report.md**

## 12. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Test Engineer** | [TBD] | | |
| **Safety Officer** | [TBD] | | |
| **H2 Systems Engineer** | [TBD] | | |
| **Quality Assurance** | [TBD] | | |

## 13. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-10 | AMPEL360 V&V Team | Initial release |

---

## Document Control

- **Document Type**: Test Procedure - Safety Critical
- **ATA Chapter**: 10 - Parking, Mooring, Storage & RTS
- **Safety Critical**: **YES**
- **Classification**: Controlled Document
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

*Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.*
*Status: DRAFT – Requires H2 safety expert review and approval before use.*
*Last AI update: 2025-12-10*

---
