# Test Plan - Functional Test
## Door L1 Forward

**Test Plan:** TP-52-10-01-010  
**Priority:** HIGH  
**Revision:** 1.0  
**Date:** 2025-11-03  
**Status:** Draft

---

## 1. TEST OBJECTIVES

Demonstrate all operational functions of Door L1 Forward including normal operation, emergency operation, and safety systems.

---

## 2. TEST REQUIREMENTS

### 2.1 Normal Operations
- Door opening and closing (50 cycles)
- Powered actuation
- Manual operation
- Seal inflation/deflation
- Latch engagement/disengagement

### 2.2 Emergency Operations
- Emergency opening from inside
- Emergency opening from outside
- Slide deployment and inflation
- Emergency lighting activation
- Escape route marking

### 2.3 Safety Systems
- Pressure interlock operation
- Warning systems
- Position indicators
- Override functions

---

## 3. ACCEPTANCE CRITERIA

| Function | Requirement | Acceptance |
|----------|-------------|------------|
| Opening time (emergency) | ≤15 seconds | Must meet |
| Manual opening force | ≤220 N | Must meet |
| Slide deployment time | ≤6 seconds | Must meet |
| Latch engagement | 100% reliable | Must meet |
| Pressure interlock | Prevent opening >1 psi | Must meet |
| Warning activation | <1 second delay | Must meet |
| Seal inflation | <30 seconds | Must meet |
| Door operation cycles | 50 cycles no failure | Must meet |

---

## 4. TEST PROCEDURE

### 4.1 Normal Operation Tests

#### Test 1: Powered Opening/Closing (20 cycles)
1. Start from closed and latched position
2. Activate powered opening
3. Measure opening time
4. Verify full open position
5. Close door with power
6. Measure closing time
7. Verify latch engagement
8. Repeat 20 times

#### Test 2: Manual Operation (10 cycles)
1. Disable powered actuation
2. Manually open door
3. Measure opening force (max)
4. Verify smooth operation
5. Manually close door
6. Engage latches manually
7. Repeat 10 times

#### Test 3: Seal System
1. Close and latch door
2. Activate seal inflation
3. Measure inflation time
4. Verify seal pressure (5 psi)
5. Check leak rate
6. Deflate seal
7. Verify deflation time

### 4.2 Emergency Operation Tests

#### Test 4: Emergency Opening - Inside
1. Close and latch door
2. Inflate seals (simulate pressurization)
3. Pull emergency handle (inside)
4. Measure opening time
5. Verify slide deployment
6. Measure slide inflation time
7. Check emergency lighting
8. Document: MUST be <15 seconds total

#### Test 5: Emergency Opening - Outside
1. Close and latch door
2. Activate external emergency release
3. Measure opening time
4. Verify door can be opened from outside

#### Test 6: Slide Deployment
1. Arm slide system
2. Open door (emergency mode)
3. Measure slide deployment time
4. Verify slide inflation pressure
5. Inspect slide attachment (girt bar)
6. Test slide detachment

### 4.3 Safety System Tests

#### Test 7: Pressure Interlock
1. Close and latch door
2. Pressurize cabin to 1 psi
3. Attempt to open door (powered)
4. **Expected:** Door refuses to open
5. Attempt to disengage latches
6. **Expected:** Latches refuse to disengage
7. Increase to 5 psi
8. Verify interlock still active
9. Depressurize cabin
10. Verify door can now open

#### Test 8: Warning Systems
1. Open door slightly (not fully closed)
2. Verify "DOOR OPEN" warning activates
3. Measure warning delay (<1 second)
4. Attempt pressurization
5. Verify pressure warning system
6. Close door fully
7. Verify warning clears

#### Test 9: Position Indicators
1. Cycle door through positions
2. Verify indicator accuracy:
   - Fully closed and latched
   - Closed but unlatched
   - Partially open
   - Fully open
3. Check cockpit indications
4. Verify flight deck warnings

### 4.4 Durability Tests

#### Test 10: Cyclic Operation (50 cycles)
1. Perform 50 complete open/close cycles
2. Alternate powered and manual operation
3. Monitor for degradation
4. Check for wear or damage
5. Measure operation consistency
6. Inspect latches and hinges after 50 cycles

---

## 5. INSTRUMENTATION

- Force gauges (opening force)
- Stopwatches/timers (opening time)
- Pressure sensors (seal, cabin)
- Position sensors (door angle)
- Video cameras (documentation)
- Accelerometers (impact measurement)

---

## 6. TEST SETUP

### 6.1 Test Fixture
- Full-scale fuselage section
- Pressurization capability (up to 10 psi)
- Electrical power (28V DC, 115V AC)
- Pneumatic supply (seal inflation)
- Access platform and stairs

### 6.2 Safety
- Slide inflation containment
- Personnel protective equipment
- Emergency stop buttons
- Video surveillance

---

## 7. DELIVERABLES

### 7.1 Test Report
- Pass/fail for each test
- Measured data vs. requirements
- Photos and videos
- Anomaly log
- Recommendations

### 7.2 Data Package
- Force measurements
- Timing data
- Pressure recordings
- Position sensor data
- Warning system logs

---

## 8. SCHEDULE & COST

- **Duration:** 2 weeks
- **Setup:** 3 days
- **Testing:** 5 days
- **Analysis:** 2 days
- **Cost:** $45,000
- **Status:** Draft - Awaiting prototype

---

## 9. PERSONNEL

- Test engineer (lead)
- Instrumentation technician
- Safety observer
- Flight crew representative (for procedure validation)
- Quality inspector

---

## 10. SPECIAL CONSIDERATIONS

### 10.1 Slide System
- Slide inflation is destructive (one-time)
- Requires slide repack after test
- Consider mock slide for cyclic tests
- Real slide for final emergency demo

### 10.2 Pressurization
- Gradual pressure increase
- Monitor seal integrity
- Safety pressure relief set at 12 psi
- Remote operation during pressure tests

---

## 11. REFERENCES

- CS-25.783 Doors
- CS-25.807 Emergency exits
- CS-25.809 Emergency exit arrangement
- CS-25.810 Emergency egress assist means
- CS-25.811 Emergency exit marking
- CS-25.812 Emergency lighting
- Door L1 Forward Operational Requirements (03_REQUIREMENTS/RQ-OPERATIONAL/)

---

**Note:** This is a critical test for operational approval. Many requirements are demonstrated through this functional testing.
