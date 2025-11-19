# 95-20-31-009 — Operational Procedures

**Component ID**: 95-20-31-009  
**Parent**: [95-20-31 NN Recording Systems](./README.md)  
**Status**: WORKING

## Overview

This document defines operational procedures for the NN Recording Systems subsystem, covering normal operations, abnormal conditions, maintenance, and system updates.

## Normal Operations

### Pre-Flight Procedures

#### System Initialization

1. **Power-Up Sequence**
   - IMA partition activation (via [95-20-42](../95-20-42_NN_IMA_Integration/))
   - Model loading from secure storage
   - Configuration file validation
   - Self-test execution

2. **Health Checks**
   - Model integrity verification (checksum validation)
   - Input interface testing (CVR, FDR connectivity)
   - Output interface testing (storage, communication links)
   - Resource availability check (CPU, memory, storage)

3. **Calibration** (if applicable)
   - Audio level calibration (CVR channels)
   - FDR parameter validation (range checks)
   - Timestamp synchronization (GPS/INS)

**Duration**: <2 minutes  
**Success Criteria**: All green status indicators, no fault flags  
**Action if Failed**: Proceed with flight (NN non-essential); log fault for maintenance

#### Pre-Flight Checklist

```
[ ] NN Recording System Power ON
[ ] Self-Test PASSED
[ ] Model Version Verified: [X.X]
[ ] Storage Available: [>80 GB]
[ ] CVR Audio Input: OK
[ ] FDR Data Input: OK
[ ] No Fault Flags
[ ] System Ready for Flight
```

### In-Flight Operations

#### Continuous Monitoring Mode

**CVR Transcription**:
- Mode: Real-time or buffered (configurable)
- Processing: Continuous, 30-second segments
- Output: Buffered transcripts (storage at end of flight)
- Alerts: Keyword detection (if configured)

**FDR Anomaly Detection**:
- Mode: Real-time continuous
- Processing: 10 Hz parameter monitoring
- Output: Anomaly scores, event flags
- Alerts: High-priority anomalies (optional crew notification)

**Event Detection**:
- Mode: Background processing
- Processing: Continuous, low-priority
- Output: Event markers (timestamps, classifications)
- Alerts: None (post-flight review only)

#### Crew Interaction

**Minimal Interaction Required**:
- System operates autonomously
- No flight deck controls (except optional ON/OFF)
- Status indication on maintenance page (ECAM/EICAS)

**Optional Alerts** (if configured):
- High-priority FDR anomaly detected
- CVR safety keyword detected ("GPWS", "TCAS", "Fire", etc.)
- System fault (model failure, data corruption)

**Crew Actions**:
- Note alerts in flight log (if any)
- Continue normal operations (NN non-essential for flight safety)
- Report persistent faults to maintenance

### Post-Flight Procedures

#### Data Processing

**Automatic Processing** (if ground power available):
1. **Event Segmentation**: Identify all events of interest (~5 minutes)
2. **Data Compression**: Compress non-critical data (~10 minutes)
3. **Maintenance Log Generation**: Create post-flight summary (~5 minutes)
4. **Data Upload**: Transfer to ground systems (if connected)

**Manual Download** (if automatic processing not available):
1. Connect QAR download equipment
2. Retrieve raw CVR/FDR data
3. Retrieve NN-processed data (transcripts, anomalies, events)
4. Ground-based processing (as needed)

#### Post-Flight Checklist

```
[ ] NN Data Processing Complete
[ ] No Critical Anomalies Detected (or flagged for review)
[ ] Transcripts Generated
[ ] Maintenance Log Available
[ ] Data Uploaded / Downloaded
[ ] System Ready for Next Flight
```

## Abnormal Conditions

### Model Failure

**Symptoms**:
- Inference timeout (>10 seconds)
- Repeated errors in model output
- Checksum validation failure
- Memory overflow

**Actions**:
1. **Automatic Fallback**: Switch to rule-based processing (if available)
2. **Alert Maintenance**: Flag for immediate review
3. **Continue Recording**: Raw CVR/FDR data unaffected
4. **Log Fault**: Record failure details for analysis

**Crew Action**: None required (post-flight maintenance item)

### Input Data Quality Issues

**CVR Audio Degradation**:
- **Symptoms**: High noise, channel failure, clipping
- **Detection**: SNR monitoring, audio quality metrics
- **Actions**: 
  - Flag affected segments in transcripts
  - Adjust processing (skip if quality very poor)
  - Alert maintenance (microphone/audio system check)

**FDR Parameter Issues**:
- **Symptoms**: Missing parameters, out-of-range values, sensor failures
- **Detection**: Data quality monitoring, aircraft fault flags
- **Actions**:
  - Use available parameters for anomaly detection
  - Flag missing/invalid data in outputs
  - Alert maintenance (sensor/DAU check)

### Communication/Storage Failure

**Output Interface Failure**:
- **Symptoms**: Cannot write to storage, communication timeout
- **Actions**:
  - Buffer data in memory (up to capacity)
  - Attempt retry
  - Alert maintenance if persistent
  - Raw CVR/FDR recording unaffected

**Storage Full**:
- **Symptoms**: Storage capacity <10%
- **Actions**:
  - Automatic oldest data cleanup (after verification of backup)
  - Alert maintenance for data download
  - Continue recording (overwrite oldest if necessary)

### Software/Hardware Faults

**IMA Partition Failure**:
- **Symptoms**: NN system unresponsive, partition restart
- **Actions**:
  - Automatic restart attempt
  - Reinitialize models and configuration
  - If restart fails, disable NN system
  - Raw CVR/FDR recording unaffected

**Memory/CPU Overload**:
- **Symptoms**: Processing delays, system sluggishness
- **Actions**:
  - Reduce processing load (skip non-critical functions)
  - Alert maintenance
  - Continue essential functions (FDR anomaly detection priority)

## Maintenance Procedures

### Routine Maintenance

#### Weekly Checks

- **Log File Review**: Check for recurring faults or warnings
- **Performance Metrics**: Review inference times, detection rates
- **Storage Status**: Verify sufficient capacity
- **Data Quality**: Spot-check transcripts and anomaly detections

**Duration**: 30 minutes  
**Tools**: Ground maintenance terminal, analysis software

#### Monthly Checks

- **Model Performance Analysis**: Detailed review of detection accuracy
- **False Positive/Negative Tracking**: Analyze missed or false anomalies
- **Calibration Verification**: Check CVR audio levels, FDR parameter ranges
- **Software Version Check**: Verify latest approved version installed

**Duration**: 2 hours  
**Tools**: Ground maintenance terminal, statistical analysis tools

#### Quarterly Checks

- **Comprehensive System Test**: Full functional test on ground
- **Data Integrity Audit**: Verify all recordings properly stored
- **Security Audit**: Check access logs, encryption status
- **User Feedback Review**: Incorporate operational feedback

**Duration**: Half day  
**Tools**: Full ground test equipment, audit tools

### Model Updates

#### Update Procedure

**Pre-Update**:
1. Receive approved model update package (digitally signed)
2. Verify update authorization and version compatibility
3. Back up current model and configuration
4. Schedule update during maintenance window

**Update**:
1. Connect secure update device
2. Upload new model to secure storage
3. Validate model checksum
4. Update configuration files (if needed)
5. Run self-test with new model

**Post-Update**:
1. Ground functional test (at least 1 hour)
2. Validation flight (if required for major updates)
3. Monitor performance for 10 flights
4. Document update in aircraft log

**Rollback** (if issues detected):
1. Restore previous model from backup
2. Document rollback reason
3. Report to model developers
4. Re-test before next attempt

#### Update Approval

**Authority**: 
- Minor updates (<5% model change): Maintenance supervisor
- Major updates (>5% model change): Chief engineer + regulatory authority

**Validation**:
- Ground testing: Mandatory
- Flight testing: For major updates or DAL-C functions
- Regulatory approval: For major updates affecting certification

### Troubleshooting

#### Common Issues

**Issue**: CVR transcription quality poor  
**Possible Causes**: Noisy cockpit, microphone issues, model outdated  
**Actions**: Check audio input quality, verify microphone function, consider model update

**Issue**: FDR anomaly false positives  
**Possible Causes**: Threshold too sensitive, unusual flight profile, model drift  
**Actions**: Review threshold settings, analyze false positives, consider retraining

**Issue**: Event segmentation missing events  
**Possible Causes**: Novel event type, low-quality input data, model limitations  
**Actions**: Manual review, feedback to model developers, consider model update

**Issue**: Slow processing performance  
**Possible Causes**: Resource overload, hardware degradation, software bug  
**Actions**: Check CPU/memory usage, verify IMA partition health, software diagnostics

## Emergency Procedures

### System Disable

**When to Disable**:
- Critical fault affecting aircraft systems (rare, should not occur)
- Regulatory directive
- Suspected security compromise

**Procedure**:
1. Access maintenance menu
2. Select "NN Recording System"
3. Select "Disable"
4. Confirm action
5. Verify system powered down
6. Log action in aircraft maintenance log

**Effect**:
- NN processing stops
- Raw CVR/FDR recording unaffected
- Re-enable requires maintenance action + self-test

### Data Preservation

**In Case of Incident/Accident**:
1. **DO NOT overwrite CVR/FDR data** (regulatory requirement)
2. Secure NN-processed data (transcripts, anomalies, events)
3. Download all available data immediately
4. Create multiple backup copies
5. Preserve in encrypted, tamper-evident storage
6. Provide to investigation authority as requested

**Data Handling**:
- Chain of custody documentation
- Read-only access for investigators
- No modification or deletion
- Audit trail for all access

## Training Requirements

### Personnel Training

**Maintenance Engineers**:
- Basic NN concepts and terminology
- System architecture and components
- Operational procedures (normal and abnormal)
- Troubleshooting and fault isolation
- Model update procedures
- Data interpretation

**Flight Operations**:
- Awareness of NN system capabilities
- Interpretation of alerts (if any)
- Limitations and when not to rely on NN
- Emergency procedures (disable)

**Safety Investigators**:
- Detailed NN system operation
- Output interpretation
- Limitations and uncertainty
- Data extraction and analysis tools

### Training Materials

- System overview presentation (2 hours)
- Hands-on workshop (4 hours)
- Troubleshooting scenarios (2 hours)
- Assessment and certification

**Recurrent Training**: Annually or when major system updates deployed

## Documentation

### Operational Manuals

- Aircraft Flight Manual (AFM) supplement (if crew interaction required)
- Aircraft Maintenance Manual (AMM) chapter
- Fault Isolation Manual (FIM) chapter
- Component Maintenance Manual (CMM) for NN system
- Training manuals and lesson plans

### Technical Publications

- System schematics and interface diagrams
- Software version control documentation
- Model cards and performance specifications
- Certification documentation

## References

- [95-20-31-001 Recording Systems NN Overview](95-20-31-001_Recording_Systems_NN_Overview.md)
- [95-20-31-007 Integration with ATA 31](95-20-31-007_Integration_with_ATA_31.md)
- [95-20-31-008 Safety and Certification](95-20-31-008_Safety_and_Certification.md)
- [ATA iSpec 2200](https://www.ata.org/resources/specifications) – Technical Publications Standards
- [S1000D](http://www.s1000d.org/) – International Technical Publications Specification

## Document Control

- **Version**: 1.0
- **Status**: WORKING
- **Last Updated**: 2025-11-18

---

## Document Control – AI Involvement

- Generated / updated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-18
