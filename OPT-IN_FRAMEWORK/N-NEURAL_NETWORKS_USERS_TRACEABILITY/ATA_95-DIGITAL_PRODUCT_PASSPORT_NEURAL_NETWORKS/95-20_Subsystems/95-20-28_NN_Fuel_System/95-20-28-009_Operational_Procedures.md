# 95-20-28-009 — Operational Procedures

**Component ID**: 95-20-28-009  
**Parent**: [95-20-28 Fuel System Neural Networks](README.md)  
**Status**: WORKING

## Overview

This document describes the operational procedures for the Neural Network Fuel System subsystem, including normal operations, abnormal conditions, emergency procedures, and maintenance requirements.

## Normal Operations

### Pre-Flight Procedures

#### System Initialization

1. **Power-Up Sequence**
   - IMA partition initialization
   - NN model loading and verification
   - Self-test execution (BIT - Built-In Test)
   - Sensor connectivity check

2. **Pre-Flight Checks**
   - Verify system status display shows "NORMAL"
   - Check all NN models loaded successfully
   - Verify sensor health indicators
   - Review any deferred maintenance items

3. **Fuel Quantity Verification**
   - Compare NN fuel quantity estimates with manual dipstick readings
   - Acceptable deviation: ±2% of tank capacity
   - Document any discrepancies in aircraft log

4. **Water Contamination Check**
   - Review water detector status
   - Perform manual drain check if required
   - Verify no water contamination alerts

### In-Flight Operations

#### Continuous Monitoring

The NN Fuel System operates continuously during flight:

1. **Fuel Quantity Estimation** (5 Hz update rate)
   - Real-time fuel level tracking
   - Automatic attitude compensation
   - Cross-validation with flow-based calculations

2. **Leak Detection Monitoring** (1 Hz update rate)
   - Continuous anomaly detection
   - Flow balance verification
   - Automatic alerting if threshold exceeded

3. **Fuel Transfer Optimization** (0.5 Hz update rate)
   - Continuous CG optimization
   - Automated transfer sequencing
   - Manual override always available

4. **Temperature Prediction** (2 Hz update rate)
   - Proactive thermal management
   - Cooling system optimization
   - Temperature trend monitoring

#### Flight Crew Interface

**Primary Display Elements:**
- Total fuel remaining (NN estimate + confidence)
- Individual tank levels
- CG position (current and predicted)
- System health status
- Active alerts/advisories

**Advisory Messages:**
- "FUEL QTY EST DEGRADED" - Sensor issues, using backup estimation
- "LEAK DETECTION MONITOR" - Possible anomaly detected
- "FUEL TRANSFER AUTO" - Automated transfer in progress
- "TEMP MGMT ACTIVE" - Thermal management system active

#### Pilot Actions

**Normal Monitoring:**
- Monitor fuel quantity displays
- Verify CG remains within limits
- Acknowledge advisory messages as appropriate
- Report any unusual indications

**Manual Override:**
- Pilots can override automated fuel transfer at any time
- Override procedure: Press "FUEL XFER MANUAL" button
- System reverts to classical fuel management
- NN system continues monitoring only

### Post-Flight Procedures

1. **System Shutdown**
   - Normal automatic shutdown with aircraft power-down
   - Data logging automatically saved
   - Model performance metrics recorded

2. **Post-Flight Review**
   - Review any alerts or advisories from the flight
   - Document any system anomalies
   - Report persistent issues to maintenance

## Abnormal Conditions

### Sensor Failures

#### Single Sensor Failure

**Indication:**
- "FUEL SENSOR FAIL [location]" advisory
- Degraded accuracy for affected measurement
- System continues operating with reduced confidence

**Crew Action:**
- Note the failure in aircraft log
- Monitor fuel quantity more closely
- Consider conservative fuel planning for subsequent flights

**System Response:**
- Automatic sensor fusion degradation
- Increased reliance on remaining sensors
- Confidence scores adjusted accordingly

#### Multiple Sensor Failures

**Indication:**
- "FUEL QTY EST DEGRADED" caution
- "FUEL SENSOR FAIL MULTIPLE" caution
- Significantly reduced estimation confidence

**Crew Action:**
- Revert to manual fuel management
- Use flow-based fuel calculations
- Consider diversion if fuel state uncertain

**System Response:**
- Automatic fallback to classical algorithms
- NN continues providing advisory estimates only
- Maintenance action required before next flight

### Model Failures

#### Single Model Failure

**Indication:**
- "NN [MODEL NAME] DEGRADED" advisory
- Specific function operates in backup mode
- Other functions continue normally

**Crew Action:**
- Note the failure in aircraft log
- Monitor affected function closely
- Use manual procedures for affected function if required

**System Response:**
- Affected function falls back to classical algorithm
- Other NN functions continue operating
- Diagnostic data logged for maintenance analysis

#### Multiple Model Failures

**Indication:**
- "NN FUEL SYS DEGRADED" caution
- "REVERT TO MANUAL FUEL MGMT" caution

**Crew Action:**
- Immediately revert to manual fuel management
- Use standard fuel system procedures per AFM
- Consider operational limitations for flight continuation

**System Response:**
- Complete reversion to classical fuel system control
- NN system disabled for safety
- Comprehensive diagnostic data logged

### Communication Failures

#### ARINC 429 Communication Loss

**Indication:**
- "FUEL DATA COMM FAIL" caution
- Loss of sensor data or inability to send commands

**Crew Action:**
- Verify aircraft electrical system status
- Revert to backup fuel system displays
- Follow AFM procedures for fuel system degradation

**System Response:**
- Maintain last known good state
- Automatic timeout and safe mode activation
- Attempt communication recovery

### Fuel System Anomalies

#### Leak Detection Alert

**Indication:**
- "FUEL LEAK DETECTED [location]" warning
- Visual and aural alert
- Affected tank/system highlighted on display

**Crew Action:**
- **IMMEDIATE**: Execute fuel leak checklist per AFM
- Isolate affected tank if possible
- Consider fuel jettison if required and available
- Declare emergency if appropriate
- Divert to nearest suitable airport

**System Response:**
- Continuous monitoring of leak severity
- Automatic fuel isolation recommendations
- Enhanced leak detection sensitivity
- Logging of all relevant data for investigation

#### Abnormal Fuel Imbalance

**Indication:**
- "FUEL IMBALANCE" caution
- CG position approaching limits
- Transfer system unable to correct

**Crew Action:**
- Review fuel transfer system status
- Attempt manual fuel transfer
- Follow AFM fuel imbalance procedures
- Consider operational limitations

**System Response:**
- Aggressive transfer optimization
- Priority on CG correction
- Alert if automatic correction not possible
- Recommend manual intervention

#### Water Contamination Detection

**Indication:**
- "FUEL WATER DETECTED [tank]" advisory/caution
- Contamination level and trend displayed

**Crew Action:**
- Note in aircraft log
- Monitor for increased contamination or engine issues
- Schedule fuel drain at next suitable airport
- Consider precautionary landing if severe

**System Response:**
- Continuous monitoring of water content
- Trend analysis for worsening contamination
- Alert escalation if content increases rapidly
- Integration with engine monitoring for ice detection

## Emergency Procedures

### Total NN Fuel System Failure

**Indication:**
- "NN FUEL SYSTEM FAIL" warning
- All NN functions offline
- Reversion to conventional fuel system

**Immediate Actions:**
- Verify aircraft continues to fly normally
- Revert to manual fuel management per AFM
- Monitor fuel quantity by alternative means (flow, time)

**Secondary Actions:**
- Review electrical system status
- Consider IMA reset if appropriate
- Follow AFM procedures for system failures
- Land at nearest suitable airport

**System Response:**
- Complete shutdown of NN system
- Full reversion to certified classical fuel system
- Protection of critical flight data
- Comprehensive diagnostics logged

## Maintenance Procedures

### Routine Maintenance

#### Daily/Pre-Flight

- Review aircraft log for any fuel system anomalies
- Perform visual inspection of fuel system
- Verify NN system status indicators
- Check for any deferred maintenance items

#### Weekly

- Download and review system performance logs
- Analyze NN model performance metrics
- Review any alerts or advisories
- Verify sensor calibration status

#### Monthly

- Detailed log file analysis
- Model performance evaluation
- Sensor accuracy verification
- Calibration checks as required

#### Quarterly

- Comprehensive system health assessment
- Sensor calibration verification with reference standards
- Review model drift indicators
- Software version verification

#### Annually

- Full system validation
- Model retraining evaluation
- Certification evidence review
- Comprehensive sensor recalibration

### Troubleshooting

#### Low Confidence Scores

**Symptoms:**
- Persistent confidence scores <0.7
- "LOW CONFIDENCE" advisories

**Troubleshooting Steps:**
1. Check sensor health and calibration
2. Review recent environmental conditions
3. Verify model version is current
4. Check for data quality issues
5. Review training data representativeness

**Resolution:**
- Recalibrate sensors if required
- Update model if available and certified
- Document any edge cases not covered by training data

#### Persistent False Alarms

**Symptoms:**
- Repeated leak alerts with no actual leak
- False water contamination warnings

**Troubleshooting Steps:**
1. Verify sensor functionality with known good reference
2. Check for environmental factors (temperature, pressure extremes)
3. Review alert thresholds and sensitivity settings
4. Analyze historical data for patterns

**Resolution:**
- Recalibrate affected sensors
- Adjust alert thresholds if approved by engineering
- Document conditions causing false alarms
- Consider model retraining if systematic issue

### Software Updates

#### Update Procedure

1. **Pre-Update:**
   - Verify update package authenticity and certification
   - Review release notes and known issues
   - Back up current configuration and logs

2. **Update Installation:**
   - Load update via approved method (ground cart, OTA)
   - Verify checksum and digital signature
   - Install update per maintenance manual procedures

3. **Post-Update Verification:**
   - Execute comprehensive BIT
   - Verify all NN models load correctly
   - Perform ground functional test
   - Document update in aircraft log

4. **Flight Test (if required):**
   - First flight after major update requires test profile
   - Verify all functions operate as expected
   - Monitor for any anomalies
   - Complete sign-off per maintenance procedures

## Training Requirements

### Flight Crew Training

- Initial: 2 hours ground school + 2 hours simulator
- Recurrent: 1 hour annually
- Topics: System operation, monitoring, abnormal procedures, limitations

### Maintenance Personnel Training

- Initial: 8 hours classroom + 4 hours hands-on
- Recurrent: 4 hours annually
- Topics: System architecture, troubleshooting, software updates, calibration

### Engineering Support

- Specialized training for system engineers supporting the NN Fuel System
- Includes deep dives into model architecture, training, and validation

## Document Control

- **Version**: 1.0  
- **Status**: WORKING  
- **Last Updated**: 2025-11-18  
- **Related Documents**:
  - Aircraft Flight Manual (AFM) fuel system procedures
  - Maintenance Manual fuel system chapter
  - Quick Reference Handbook (QRH) fuel system abnormals

---

## Document Control – AI Involvement

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.  
- Status: **DRAFT** – Subject to human review and approval.  
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-18_.
