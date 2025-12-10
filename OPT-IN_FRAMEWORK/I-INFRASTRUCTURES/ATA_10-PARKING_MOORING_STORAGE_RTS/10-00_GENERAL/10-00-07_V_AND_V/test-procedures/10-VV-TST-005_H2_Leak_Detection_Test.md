# 10-VV-TST-005 — H2 Leak Detection Test

## 1. Test Identification

| Parameter | Value |
|-----------|-------|
| Document Number | 10-VV-TST-005 |
| Test Type | System/Functional |
| Verification Method | Test |
| System/Subsystem | H2 Leak Detection System |
| Status | Draft |
| H2 Related | Yes |
| Cryo Related | No |
| BWB Specific | No |

## 2. Purpose

This test procedure verifies the performance of hydrogen leak detection systems used during parking and storage operations of the AMPEL360-BWB-H2-Hy-E aircraft. The test validates detector sensitivity, response time, alarm thresholds, and system integration.

## 3. Scope

### 3.1 Scope Inclusions
- H2 detector sensor sensitivity verification
- Response time measurement
- Alarm threshold verification
- System integration testing
- False alarm rate assessment
- Environmental effects on detection

### 3.2 Scope Exclusions
- Aircraft-mounted H2 detection systems (covered under other ATAs)
- H2 refueling detection systems (unless integrated with parking systems)

### 3.3 Applicability
- **Aircraft**: AMPEL360-BWB-H2-Hy-E
- **ATA Chapter**: 10 - Parking, Mooring, Storage & RTS
- **Configuration**: Ground-based H2 detection systems for parking/storage areas

## 4. Applicable Documents

### 4.1 Reference Documents
| Document ID | Title | Revision |
|-------------|-------|----------|
| 10-VV-VPL-004 | H2 Safety Verification Plan | A |
| 10-00-03-REQ-XXX | H2 Detection System Requirements | TBD |
| SAE AS6968 | Handling and Storage of Gaseous and Liquid Hydrogen | Current |
| NFPA 2 | Hydrogen Technologies Code | 2020 |

### 4.2 Related Procedures
| Procedure ID | Title | Relationship |
|--------------|-------|--------------|
| 10-VV-TST-006 | H2 Venting Test | Related system |
| 10-VV-INS-003 | H2 System Inspection | Maintenance procedure |

## 5. Requirements Verified

| Requirement ID | Description | Verification Method | Acceptance Criteria |
|----------------|-------------|---------------------|---------------------|
| REQ-10-H2-001 | Detection sensitivity ≤ 10% LEL | Test | Alarm activates at ≤ 10% LEL |
| REQ-10-H2-002 | Response time ≤ 2 seconds | Test | T90 ≤ 2 seconds |
| REQ-10-H2-003 | Temperature range -40°C to +60°C | Test | Functional across range |
| REQ-10-H2-004 | Humidity range 0-100% RH | Test | Functional across range |
| REQ-10-H2-005 | False alarm rate ≤ 1 per 1000 hours | Test | Statistical validation |
| REQ-10-H2-006 | System integration and alarm | Test | Correct alarm propagation |

## 6. Test Setup

### 6.1 Test Article
**Description**: H2 leak detection system including sensors, control unit, and alarm interfaces

**Configuration**:
- H2 Detector Type: [Specify - electrochemical, catalytic, optical, etc.]
- Part Number: [P/N]
- Serial Number: [S/N]
- Control Unit: [Model and S/N]
- Configuration Baseline: [Baseline identifier]

### 6.2 Test Equipment

| Equipment | Specification | Calibration Due | Equipment ID |
|-----------|---------------|-----------------|--------------|
| H2 gas supply | Research grade, 99.999% | N/A | H2-SUPPLY-01 |
| Gas flow controller | 0-1000 sccm, ±1% accuracy | YYYY-MM-DD | GFC-01 |
| Test chamber | 1 m³, sealed, ventilated | N/A | TCHAMBER-01 |
| H2 reference detector | NIST traceable, ±2% | YYYY-MM-DD | H2-REF-01 |
| Data acquisition system | 100 Hz sampling | YYYY-MM-DD | DAQ-01 |
| Environmental chamber | -40°C to +70°C, 0-100% RH | YYYY-MM-DD | ENVCHAM-01 |
| Timer/stopwatch | ±0.01 second | N/A | TIMER-01 |

**Notes on Equipment**:
- All equipment shall be H2-compatible and certified for H2 use
- Calibration certificates shall be available for inspection
- Reference detector accuracy shall meet or exceed test article requirements

### 6.3 Test Facility

**Facility**: H2 Safety Test Facility, [Location TBD]

**Environmental Conditions**:
- Initial tests: Ambient (20±5°C, 30-70% RH)
- Environmental tests: Per environmental chamber capability
- Pressure: Atmospheric

**Safety Equipment**:
- H2 detection system (independent of test article)
- Forced ventilation (minimum 10 air changes per hour)
- Emergency shutdown system
- Fire suppression system
- Emergency communication
- PPE for H2 operations

## 7. Safety Precautions

### 7.1 General Safety
- All personnel shall complete H2 safety training before participating
- PPE: Safety glasses, natural fiber clothing, no synthetic materials
- Emergency procedures reviewed before test
- Emergency exits clearly marked and accessible
- First aid and emergency response equipment available

### 7.2 H2 Safety
- H2 detector placement: Independent detection system operational before H2 introduction
- Ventilation requirements: Forced ventilation operational and verified before H2 use
- Ignition source control: No ignition sources within 7.5 m of test area
- Safety zone establishment: Test area restricted, no unauthorized personnel
- Emergency response procedures: H2 leak response, fire/explosion response
- H2 training requirements: All personnel H2-safety certified
- Maximum H2 concentration: Test chamber design limits H2 to < 25% LEL in worst case
- Purge procedures: Purge chamber with inert gas or air before and after H2 tests

### 7.3 Electrical Safety
- Ground bonding: All equipment properly grounded
- Electrical equipment: Rated for Class I, Division 2 (or equivalent)
- Power isolation: Emergency power cutoff accessible

### 7.4 Test-Specific Safety
- H2 concentration monitoring: Continuous monitoring with independent system
- Automatic ventilation activation: If H2 detected above safe threshold
- Test suspension criteria: Any H2 detection outside test chamber, equipment malfunction

## 8. Pre-Test Requirements

### 8.1 Test Article Preparation
1. Install H2 detector in test chamber per manufacturer instructions
2. Connect detector to control unit and verify power
3. Verify detector is in ready state (self-test passed if applicable)
4. Position reference detector in chamber for comparison

### 8.2 Equipment Calibration Verification
- Verify all test equipment calibration is current
- Document calibration status in test log
- Perform functional check of data acquisition system
- Verify H2 gas supply purity certificate

### 8.3 Safety Verification
- Verify independent H2 detection system operational
- Verify forced ventilation operational (measure air velocity)
- Conduct safety briefing with all test personnel
- Verify emergency procedures are understood
- Verify emergency communication functional
- Verify fire suppression system operational
- Inspect test chamber for leaks (pressure test with air)

### 8.4 Test Readiness Review
- Review test procedure with all personnel
- Verify test setup matches procedure requirements
- Obtain authorization to proceed from test director
- Document test readiness in test log

## 9. Test Procedure

### 9.1 Pre-Test Steps
1. Record ambient conditions (temperature, humidity, pressure)
   - Expected result: Conditions within allowable range
2. Energize test article and allow warm-up per manufacturer specification
   - Expected result: System ready indication
3. Perform zeroing/calibration per manufacturer procedure
   - Expected result: Successful zero
4. Verify data acquisition system recording
   - Expected result: All channels active and recording

### 9.2 Test Execution

#### 9.2.1 Baseline Sensitivity Test
**Objective**: Verify detection sensitivity at ambient conditions

1. Close test chamber, initiate forced ventilation
   - Expected result: Chamber sealed, ventilation flowing
   - Data to record: Timestamp, ambient conditions
   
2. Introduce H2 at controlled rate to achieve 5% LEL concentration
   - Expected result: H2 concentration increases steadily
   - Data to record: H2 flow rate, reference detector reading, test article reading, timestamp
   
3. Monitor test article response, record time to alarm
   - Expected result: Alarm activates at ≤ 10% LEL within ≤ 2 seconds of reaching threshold
   - Data to record: Alarm activation time, H2 concentration at alarm, response time (T90)
   
4. Continue to 15% LEL, maintain for 1 minute
   - Expected result: Alarm remains active, reading stable
   - Data to record: Continuous H2 concentration (both detectors)
   
5. Stop H2 flow, purge chamber with air
   - Expected result: H2 concentration decreases, alarm clears when below threshold
   - Data to record: Purge time, alarm clear time
   
6. Repeat steps 2-5 for 10% LEL, 20% LEL, 40% LEL
   - Expected result: Consistent alarm behavior at each level
   - Data to record: Same as above for each concentration

#### 9.2.2 Response Time Measurement
**Objective**: Accurately measure detector response time (T90)

1. Prepare rapid H2 injection system (pre-mixed gas or fast flow)
   - Expected result: System ready for rapid injection
   
2. Rapidly introduce H2 to achieve > 10% LEL
   - Expected result: Rapid rise in H2 concentration
   - Data to record: High-speed data (100 Hz min), time to 10%, 50%, 90% of final reading
   
3. Calculate T90 (time to reach 90% of final reading)
   - Expected result: T90 ≤ 2 seconds
   - Data to record: T90 value
   
4. Repeat 5 times for statistical validation
   - Expected result: Consistent T90 values
   - Data to record: T90 for each trial, mean, standard deviation

#### 9.2.3 Temperature Effects Test
**Objective**: Verify performance across temperature range

1. Place test article in environmental chamber at -40°C, stabilize for 30 minutes
   - Expected result: Stable temperature
   - Data to record: Temperature vs time
   
2. Perform sensitivity test (5% LEL, 10% LEL)
   - Expected result: Alarm functions correctly
   - Data to record: Alarm threshold, response time
   
3. Repeat at -20°C, 0°C, +20°C (baseline), +40°C, +60°C
   - Expected result: Functional across all temperatures
   - Data to record: Alarm threshold and response time at each temperature
   
4. Analyze sensitivity and response time vs temperature
   - Expected result: Within specification across range
   - Data to record: Plots of sensitivity and response time vs temperature

#### 9.2.4 Humidity Effects Test
**Objective**: Verify performance across humidity range

1. Set environmental chamber to 20°C, 10% RH, stabilize for 30 minutes
   - Expected result: Stable conditions
   - Data to record: Temperature and humidity vs time
   
2. Perform sensitivity test (10% LEL)
   - Expected result: Alarm functions correctly
   - Data to record: Alarm threshold, response time
   
3. Repeat at 30% RH, 50% RH, 70% RH, 90% RH, 100% RH
   - Expected result: Functional across all humidity levels
   - Data to record: Alarm threshold and response time at each humidity level
   
4. Analyze sensitivity and response time vs humidity
   - Expected result: Within specification across range
   - Data to record: Plots of sensitivity and response time vs humidity

#### 9.2.5 False Alarm Test
**Objective**: Assess susceptibility to false alarms

1. Expose detector to potential interferents (one at a time):
   - Methane (if applicable)
   - Carbon monoxide
   - Volatile organic compounds (acetone, isopropanol)
   - Humidity changes
   - Vibration
   - Expected result: No false alarm or within specification
   - Data to record: Detector response to each interferent
   
2. Monitor detector in ambient conditions for extended period (8+ hours minimum)
   - Expected result: No false alarms
   - Data to record: Continuous monitoring log, any alarms

#### 9.2.6 System Integration Test
**Objective**: Verify integration with alarm and control systems

1. Configure complete system (detector, control unit, alarms, indicators)
   - Expected result: System integrated and communicating
   - Data to record: System configuration
   
2. Introduce H2 to trigger alarm
   - Expected result: Alarm propagates to all indicators, visual and audible alarms activate
   - Data to record: Alarm activation on all devices, time delays
   
3. Test alarm acknowledgment and reset
   - Expected result: Alarm can be acknowledged, resets properly after H2 clears
   - Data to record: Acknowledgment and reset behavior
   
4. Test redundancy (if applicable): Simulate sensor failure
   - Expected result: System detects failure, activates trouble alarm
   - Data to record: Failure detection and alarm

### 9.3 Post-Test Steps
1. Stop H2 supply, close valve
2. Purge test chamber thoroughly with air or inert gas
3. Verify H2 concentration < 10% LEL before opening chamber
4. Secure test equipment and H2 supply
5. Download and backup all test data
6. Conduct test debrief, preliminary assessment
7. Complete test log

## 10. Acceptance Criteria

| Parameter | Requirement | Acceptance Criteria | Measurement Method |
|-----------|-------------|---------------------|-------------------|
| Detection sensitivity | ≤ 10% LEL | Alarm at ≤ 10% LEL | Direct measurement |
| Response time (T90) | ≤ 2 seconds | T90 ≤ 2.0 seconds | High-speed data |
| Temperature range | -40°C to +60°C | Functional, alarm within spec | Environmental testing |
| Humidity range | 0-100% RH | Functional, alarm within spec | Environmental testing |
| False alarm rate | ≤ 1 per 1000 hours | No false alarms in test | Extended monitoring |
| System integration | Proper alarm propagation | All alarms activate correctly | Functional test |

**Success Criteria**:
- All test steps completed without safety incidents
- All measured parameters within acceptance criteria
- No unexpected anomalies or failures
- Data quality verified and acceptable

## 11. Data Recording

### 11.1 Data to be Recorded
| Data Parameter | Units | Recording Method | Sample Rate | Accuracy |
|----------------|-------|------------------|-------------|----------|
| H2 concentration (ref) | % LEL | Reference detector | 1 Hz | ±2% |
| H2 concentration (test) | % LEL | Test article | 1 Hz | Per spec |
| Alarm status | On/Off | Digital input | Event | N/A |
| Temperature | °C | Thermocouple | 0.1 Hz | ±1°C |
| Humidity | % RH | Sensor | 0.1 Hz | ±3% |
| Time | seconds | DAQ clock | Continuous | ±0.01 s |

### 11.2 Data Acquisition System
- **System**: [DAQ model and configuration]
- **Configuration**: Minimum 100 Hz for response time tests, 1 Hz otherwise
- **Data Storage**: [Server location and backup procedure]

### 11.3 Manual Observations
- Test setup photos (before, during, after)
- Alarm activation observations (visual, audible)
- Any anomalies or unexpected behavior
- Environmental conditions

### 11.4 Photographic/Video Documentation
- Still photography: Test setup, test article, equipment configuration
- Video recording: Response time tests, alarm activation tests
- Documentation of any anomalies

## 12. Roles and Responsibilities

| Role | Name | Responsibilities |
|------|------|------------------|
| Test Director | [Name] | Overall test responsibility, safety authority |
| Test Engineer | [Name] | Test execution, data acquisition |
| Quality Assurance | [Name] | Procedure compliance verification |
| Safety Monitor | [Name] | H2 safety oversight, stop-work authority |
| Data Analyst | [Name] | Real-time data monitoring, preliminary analysis |

## 13. Anomaly and Non-Conformance Handling

### 13.1 Anomaly Detection
- Any deviation from expected results shall be documented in test log
- Test director shall determine if test should continue or be stopped
- Safety anomalies result in immediate test suspension

### 13.2 Non-Conformance Reporting
- Non-conformances shall be documented per NCR procedure
- NCR number: [To be assigned if needed]
- Disposition options: Use-as-is, Rework, Repair, Scrap

### 13.3 Test Suspension Criteria
- H2 detection outside test chamber
- Equipment malfunction affecting safety
- Test article performance outside specification (depending on severity)
- Safety monitor discretion

## 14. Test Report Requirements

Upon completion, a test report shall be generated containing:
- Test identification and objectives
- Test setup description with photos
- Complete test results and data analysis
- Acceptance criteria assessment
- Anomalies and resolutions
- Conclusions and recommendations
- Statistical analysis of results

Report Number: 10-VV-RPT-003 - H2 Safety Test Report

## 15. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Test Engineer | | | |
| Test Director | | | |
| Quality Assurance | | | |
| Safety Representative | | | |
| H2 Safety Engineer | | | |

## 16. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-10 | AMPEL360 V&V Team | Initial release |

---

## Document Control

- **Generated with assistance from**: AI (GitHub Copilot), prompted by Amedeo Pelliccia
- **Status**: DRAFT – Subject to human review and approval
- **Repository**: AMPEL360-BWB-H2-Hy-E
- **Path**: OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_10-PARKING_MOORING_STORAGE_RTS/10-00_GENERAL/10-00-07_V_AND_V/test-procedures/
- **Last AI Update**: 2025-12-10
