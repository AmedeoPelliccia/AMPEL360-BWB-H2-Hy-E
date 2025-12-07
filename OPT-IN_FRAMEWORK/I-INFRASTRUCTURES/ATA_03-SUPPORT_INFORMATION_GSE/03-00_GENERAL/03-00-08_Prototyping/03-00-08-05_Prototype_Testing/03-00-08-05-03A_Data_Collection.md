# 03-00-08-05-03A - Data Collection

## 1. Purpose

This document defines standards and practices for data collection during prototype testing within the AMPEL360-BWB-H2-Hy-E program, ensuring data quality, integrity, and traceability.

## 2. Scope

This specification covers data acquisition systems, measurement techniques, data formats, quality assurance, and archiving for all prototype testing activities.

## 3. Applicable Documents

- ATA 03-00-08-05-01A_Test_Objectives
- ATA 03-00-08-05-02A_Test_Procedures
- ATA 03-00-07_V_AND_V
- ISO/IEC 17025 - Testing and Calibration Laboratories

## 4. Description

### 4.1 Overview

High-quality data collection is essential for deriving meaningful conclusions from prototype tests. Proper instrumentation, calibration, data acquisition, and management ensure that test results are accurate, reliable, and defensible.

### 4.2 Requirements

**Data Acquisition Systems:**

**Hardware:**
- Multi-channel data acquisition (DAQ) systems
- Analog-to-digital converters (ADC)
- Signal conditioning
- Network-connected sensors (IoT)
- Video recording systems
- Environmental monitoring

**Software:**
- Data acquisition software (LabVIEW, NI DAQmx, etc.)
- Real-time monitoring and visualization
- Data logging and archiving
- Post-processing and analysis tools

**Sensor Types:**
- Strain gauges (structural loads)
- Thermocouples and RTDs (temperature)
- Pressure transducers (pneumatic, hydraulic, cryogenic)
- Load cells (force, torque)
- Accelerometers (vibration, shock)
- Flow meters (liquid, gas)
- Position sensors (LVDT, encoders)
- Leak detectors (H2, helium tracer)

### 4.3 Methodology

**Data Collection Process:**

1. **Instrumentation Planning**
   - Identify parameters to measure
   - Select appropriate sensors
   - Determine sampling rates
   - Plan sensor locations
   - Define measurement ranges

2. **Sensor Installation**
   - Install per manufacturer specifications
   - Verify mounting and wiring
   - Protect from environmental factors
   - Label clearly for traceability
   - Document installation (photos, notes)

3. **Calibration**
   - Calibrate all sensors before use
   - Use traceable calibration standards
   - Record calibration data
   - Apply calibration factors in DAQ
   - Re-calibrate per schedule or after events

4. **Data Acquisition Setup**
   - Configure DAQ channels
   - Set sampling rates and filters
   - Define trigger conditions
   - Set up real-time displays
   - Test data acquisition chain

5. **Pre-Test Verification**
   - Perform shakedown test
   - Verify all channels reading
   - Check data quality (noise, drift)
   - Confirm recording is functioning
   - Review and approve setup

6. **During-Test Monitoring**
   - Monitor data in real-time
   - Watch for anomalies or failures
   - Ensure continuous recording
   - Take manual notes/observations
   - Capture video as planned

7. **Post-Test Data Management**
   - Stop recording and save files
   - Backup data immediately
   - Perform initial quality checks
   - Archive raw data
   - Document any issues

**Data Quality Assurance:**

- **Accuracy**: Sensors calibrated, within specifications
- **Precision**: Repeatability demonstrated
- **Completeness**: No missing data (or documented gaps)
- **Traceability**: Sensor IDs, calibration dates recorded
- **Integrity**: Data checksums, no tampering

**Data Formats:**

- Raw data: Binary (e.g., .tdms, .dat) for efficiency
- Processed data: CSV, HDF5 for analysis
- Metadata: JSON, XML for context
- Video: MP4, AVI with timestamps
- Documentation: PDF for test logs

**Sampling Rates:**

- Structural static tests: 1-10 Hz
- Vibration tests: 1-10 kHz (Nyquist consideration)
- Thermal tests: 0.1-1 Hz
- Pressure transient tests: 100-1000 Hz
- H2 leak detection: Continuous

## 5. Deliverables

| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Instrumentation Plan | Document | Test Engineer | Pre-test |
| Sensor Calibration Records | Certificates | Calibration Lab | Pre-test |
| DAQ Configuration File | Config File | DAQ Engineer | Pre-test |
| Raw Test Data | Binary/CSV | DAQ System | During/Post-test |
| Data Quality Report | Report | Data Engineer | Post-test |

## 6. Quality Criteria

**Data Quality Metrics:**
- Calibration current (within 6 months typical)
- Sensor drift < 2% over test duration
- Data completeness > 99%
- Signal-to-noise ratio > 20 dB
- Sampling rate adequate (> 2x Nyquist)

**Acceptance Criteria:**
- All required parameters recorded
- Data quality checks passed
- Calibration records on file
- Data archived with metadata
- No unexplained anomalies

## 7. Cross-References

- Related ATA Chapters: ATA 03-00-07 (V&V)
- Parent Document: 03-00-08_Prototyping
- Related Engineering Docs: 03-00-06_Engineering
- Related V&V Docs: 03-00-07_V_AND_V

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation WG | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-07.

---
