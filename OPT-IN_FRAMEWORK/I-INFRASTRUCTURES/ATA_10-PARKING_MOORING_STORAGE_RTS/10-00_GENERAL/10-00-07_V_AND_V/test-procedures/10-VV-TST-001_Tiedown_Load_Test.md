# 10-VV-TST-001 - Tiedown Load Test

## 1. Document Identification

| Parameter | Value |
|-----------|-------|
| Document Number | 10-VV-TST-001 |
| V&V Type | Test Procedure |
| Verification Method | Test |
| Status | Active |
| Revision | A |
| Date | 2025-12-10 |

## 2. Purpose

Verify that tiedown attachment points on the AMPEL360 BWB H₂ aircraft can withstand the design loads specified in the requirements without failure or permanent deformation.

## 3. Scope

### 3.1 Test Articles
- 3 representative tiedown attachment points (full-scale)
- Complete attachment hardware (brackets, fittings)

### 3.2 Test Objectives
- Verify structural strength at 150% design load
- Measure deflection and strain under load
- Verify no permanent deformation at design load
- Document failure mode (if failure occurs)

## 4. Applicable Documents

- 10-VV-VPL-002_Tiedown_Verification_Plan.md
- Requirements: REQ-10-01-001 through REQ-10-01-004
- Design drawings: Tiedown attachment structure
- CS-25.561 (Emergency Landing Conditions)

## 5. Requirements Verified

| Req ID | Requirement Description | Verification Method |
|--------|------------------------|---------------------|
| REQ-10-01-001 | Tiedown points withstand 1.5× maximum design load | Test |
| REQ-10-01-004 | No damage to aircraft structure under design loads | Test |

## 6. Test Setup

### 6.1 Test Equipment
- Hydraulic test rig (300 kN capacity)
- Load cell (±0.5% accuracy)
- Strain gauges (10 per specimen)
- LVDTs for deflection measurement (±0.01mm)
- High-speed camera for failure documentation
- Data acquisition system (1000 Hz sampling)

### 6.2 Test Specimens
- Specimen 1: Forward tiedown point (nose section)
- Specimen 2: Wing tiedown point (mid-span)
- Specimen 3: Aft tiedown point (center section)

### 6.3 Test Environment
- Temperature: 23°C ± 2°C
- Humidity: 50% ± 10% RH
- Laboratory conditions

### 6.4 Safety Precautions
- Safety barriers around test area
- Remote operation of hydraulic system
- High-speed camera for failure observation
- Personnel PPE: Safety glasses, ear protection

## 7. Test Procedure

### Step 1: Pre-Test Inspection and Setup
**Objective**: Ensure test article and equipment ready

**Actions**:
1. Inspect test specimen for pre-existing damage
2. Install strain gauges at critical locations
3. Install LVDTs for deflection measurement
4. Mount specimen in test rig
5. Calibrate load cell and verify zero offset
6. Perform data acquisition system check
7. Document specimen configuration (photographs)

**Expected Result**: Test article properly installed, instrumentation functional

**Data to Record**: Pre-test condition, photographs, instrumentation zero readings

### Step 2: Proof Load Application (50% Design Load)
**Objective**: Verify test setup and instrumentation

**Actions**:
1. Apply load gradually to 50% of design load (rate: 1 kN/s)
2. Hold load for 30 seconds
3. Record strain and deflection
4. Reduce load to zero
5. Inspect specimen for any visible damage

**Expected Result**: Linear load-deflection response, no damage

**Data to Record**: Load, strain (all channels), deflection, time

### Step 3: Design Load Test (100% Design Load)
**Objective**: Verify performance at design load

**Actions**:
1. Apply load gradually to 100% of design load
2. Hold load for 60 seconds
3. Record strain and deflection continuously
4. Reduce load to zero over 30 seconds
5. Inspect specimen for permanent deformation
6. Measure any residual deflection

**Expected Result**: No permanent deformation, residual deflection < 2% of maximum

**Data to Record**: Load, strain, deflection vs. time; post-test measurements

### Step 4: Ultimate Load Test (150% Design Load)
**Objective**: Verify structural margin

**Actions**:
1. Apply load gradually to 150% of design load (rate: 1 kN/s)
2. Hold load for 60 seconds
3. Record strain and deflection continuously
4. If no failure, reduce load to zero
5. If failure occurs, document failure mode and load at failure
6. Post-test inspection and measurement

**Expected Result**: No failure at 150% design load

**Data to Record**: Load, strain, deflection vs. time; failure load (if applicable); failure mode

### Step 5: Post-Test Verification
**Objective**: Document final condition

**Actions**:
1. Detailed visual inspection
2. Measure permanent deformation (if any)
3. Photograph specimen final condition
4. Document failure mode and location (if failure)
5. Archive data files

**Expected Result**: Complete documentation of test results

**Data to Record**: Post-test photographs, permanent deformation measurements, observations

## 8. Pass/Fail Criteria

| Parameter | Criteria | Tolerance | Measurement Method |
|-----------|----------|-----------|-------------------|
| Maximum Load Capability | ≥ 150% design load | N/A | Load cell |
| Permanent Deformation at Design Load | ≤ 2% of elastic deflection | ±0.1mm | LVDT post-test |
| Failure Location | Design-intended location | N/A | Visual inspection |
| No premature failure | No failure < 150% design load | N/A | Load at failure |

## 9. H₂/BWB Considerations

### 9.1 BWB Configuration
- Test specimens represent actual aircraft structure from BWB design
- Load directions represent actual tiedown geometry

### 9.2 H₂ Safety
- No H₂ systems involved in this structural test
- Standard laboratory safety procedures apply

## 10. Data Recording

### 10.1 Continuous Data (During Load Application)
- Load (kN) - 1000 Hz
- Strain (10 channels) - 1000 Hz
- Deflection (3 LVDTs) - 1000 Hz
- Time stamp

### 10.2 Discrete Data
- Pre-test photographs
- Post-test photographs
- Inspection observations
- Permanent deformation measurements

## 11. Results

*[To be completed during test execution]*

### 11.1 Specimen 1 Results

| Load Level | Max Strain (με) | Max Deflection (mm) | Pass/Fail | Notes |
|------------|----------------|-------------------|-----------|-------|
| 50% Design | | | | |
| 100% Design | | | | |
| 150% Design | | | | |

### 11.2 Specimen 2 Results

| Load Level | Max Strain (με) | Max Deflection (mm) | Pass/Fail | Notes |
|------------|----------------|-------------------|-----------|-------|
| 50% Design | | | | |
| 100% Design | | | | |
| 150% Design | | | | |

### 11.3 Specimen 3 Results

| Load Level | Max Strain (με) | Max Deflection (mm) | Pass/Fail | Notes |
|------------|----------------|-------------------|-----------|-------|
| 50% Design | | | | |
| 100% Design | | | | |
| 150% Design | | | | |

## 12. Observations and Anomalies

*[To be completed during test execution]*

## 13. Conclusions

*[To be completed after test execution]*

[Summary of test results and verification of requirements]

## 14. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Test Engineer | | | |
| QA Engineer | | | |
| Structures Engineer | | | |

## 15. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-10 | AMPEL360 Test Team | Initial release |

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-10
