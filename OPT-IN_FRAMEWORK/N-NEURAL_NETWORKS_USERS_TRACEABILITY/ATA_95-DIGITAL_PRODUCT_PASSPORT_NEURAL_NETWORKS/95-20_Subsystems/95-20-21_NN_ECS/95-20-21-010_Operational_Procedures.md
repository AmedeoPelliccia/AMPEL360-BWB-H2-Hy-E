# 95-20-21-010 — Operational Procedures

**Document ID**: 95-20-21-010  
**Parent**: 95-20-21 ECS Neural Networks  
**Status**: WORKING

## Overview

This document defines standard operating procedures, crew actions, and operational limitations for the ECS Neural Network subsystem. It provides guidance for normal operations, abnormal situations, and emergency scenarios.

## System Description for Flight Crew

The ECS Neural Network system is an advanced AI-driven environmental control system that:
- Predicts and maintains optimal cabin temperature
- Monitors air quality continuously
- Optimizes HVAC for comfort and efficiency
- Manages cabin pressure automatically
- Controls humidity levels
- Optimizes CO₂ capture

The system operates autonomously with automatic fallback to classical control if needed. Crew monitoring and override capabilities are always available.

## Pre-Flight Procedures

### Ground Power Application

1. **System Initialization**
   - NN ECS initializes automatically with aircraft power-up
   - Status displayed on EICAS: "NN ECS INITIALIZING"
   - Normal initialization time: 30-45 seconds

2. **System Health Check**
   - Verify EICAS display shows: "NN ECS READY"
   - Check MFD Environmental page for green status indicators:
     - Temperature Predictor: ✓
     - Air Quality Monitor: ✓
     - HVAC Optimizer: ✓
     - Pressure Control: ✓
     - Humidity Manager: ✓
     - CO₂ Scrubber: ✓

3. **Abnormal Indications**
   - Amber status: Model degraded but operational → Note in logbook, dispatch per MEL
   - Red status: Model inoperative → Classical control active, dispatch per MEL
   - "NN ECS INOP" message: Complete system failure → Full classical control, dispatch per MEL

### Pre-Flight Configuration

**Standard Settings** (automatically configured):
- Target cabin temperature: 22°C ± 2°C per zone
- Humidity range: 40-60% RH
- CO₂ limit: <1000 ppm
- Pressure schedule: Automatic per altitude

**Crew Adjustable** (via ECS Control Panel):
- Zone temperature offsets: -3°C to +3°C
- Air quality sensitivity: LOW / NORMAL / HIGH
- CO₂ scrubber mode: AUTO / MANUAL / OFF

## Normal Operations

### Taxi

**NN ECS Actions:**
- Temperature prediction active
- HVAC optimization begins
- CO₂ scrubbing may activate if ground air quality poor

**Crew Actions:**
- Monitor cabin temperature trending to target
- Verify air quality index: "GOOD" or better

### Takeoff and Climb

**NN ECS Actions:**
- Pressure control activates automatically
- Smooth pressure transition to cruise altitude
- Temperature compensation for altitude changes
- HVAC adjusts for changing external conditions

**Crew Actions:**
- Monitor pressure schedule on EICAS (automatically controlled)
- Verify comfort parameters remain in green
- Pressure control mode should show "NN-ACTIVE"

**Normal Indications:**
- Cabin pressure: Follows altitude with <500 ft/min rate
- Temperature: Maintains target ±1°C during transitions
- Air quality: Remains "GOOD" or "EXCELLENT"

### Cruise

**NN ECS Actions:**
- Continuous temperature prediction and HVAC optimization
- Air quality monitoring and proactive ventilation
- Humidity management active
- CO₂ scrubbing optimized for maximum capture
- Energy savings mode (15% reduction in HVAC power)

**Crew Actions:**
- Periodic monitoring (every 30 minutes):
  - Check environmental page: All systems green
  - Verify passenger comfort (no excessive calls)
  - Note CO₂ capture performance on ECS page

**Performance Monitoring:**
- Energy savings indicator: Should show 10-20% reduction
- CO₂ captured: Accumulating at ~0.5-1 kg/hour
- Passenger comfort score: >95% target

### Descent and Approach

**NN ECS Actions:**
- Pressure control manages cabin descent rate
- Temperature compensation for altitude and outside air temp changes
- HVAC pre-positioning for landing conditions

**Crew Actions:**
- Monitor smooth pressure transition (passenger comfort)
- Verify cabin altitude rate < 500 ft/min descent
- Pressure control should remain "NN-ACTIVE"

### Landing and Taxi-In

**NN ECS Actions:**
- Continue environmental control
- Gradual reduction of CO₂ scrubbing
- Preparation for door opening (pressure equalization)

**Crew Actions:**
- Monitor cabin pressure approaching ambient
- Verify comfortable temperature for deplaning

### Post-Flight

**NN ECS Actions:**
- Continues operation until shutdown command
- Finalizes CO₂ scrubber regeneration if needed
- Logs performance data

**Crew Actions:**
- Review environmental page for any anomalies
- Note total CO₂ captured for flight in logbook
- If any amber/red indications: Write up in logbook

## Abnormal Operations

### Single Model Degradation (AMBER)

**Indication:** Amber status on specific model, message "NN [MODEL] DEGRADED"

**Meaning:** One neural network model performance degraded, but system continues with reduced capability

**Crew Actions:**
1. Note which model is degraded
2. Verify system continues operation
3. Monitor more frequently
4. Write up in logbook
5. Dispatch per MEL (if allowed)

**System Response:**
- Affected model uses fallback/classical algorithm
- Other models continue normal operation
- Overall system remains operational

### Single Model Failure (RED)

**Indication:** Red status on specific model, message "NN [MODEL] INOP"

**Meaning:** One neural network model inoperative, classical control for that function

**Crew Actions:**
1. Verify classical control for that function is active
2. Expect slightly reduced performance:
   - Less accurate temperature predictions
   - Higher energy usage
   - Less optimal comfort
3. Consider operational adjustments:
   - More frequent temperature adjustments
   - Manual ventilation increases if air quality model failed
4. Write up in logbook
5. Dispatch per MEL (likely allowed)

**System Response:**
- Failed model disabled
- Classical control active for that function
- Other models continue operation
- No safety impact

### Multiple Model Failure

**Indication:** Multiple amber/red statuses, message "NN ECS MULTIPLE FAILURES"

**Meaning:** Several models compromised, significant degradation

**Crew Actions:**
1. Assess overall environmental control status
2. Verify classical control active
3. Manual environmental management may be needed:
   - Adjust zone temps manually
   - Increase ventilation if passengers report discomfort
4. Consider:
   - Reducing altitude if pressure control affected
   - Diversion if unable to maintain comfort
5. Write up in logbook
6. Dispatch per MEL (may be restricted)

### Complete NN ECS Failure

**Indication:** Message "NN ECS INOP", full classical control reversion

**Meaning:** Complete neural network system failure, full fallback to baseline control

**Crew Actions:**
1. Verify EICAS shows "CLASSICAL ECS CONTROL ACTIVE"
2. Environmental control continues with baseline algorithms
3. Expect:
   - Higher workload for temperature management
   - More manual adjustments needed
   - Higher energy usage (no optimization)
   - No CO₂ capture
4. Monitor passenger comfort more frequently
5. Write up in logbook
6. Dispatch per MEL (likely allowed, check specific aircraft MEL)

**System Response:**
- All NN models disabled
- PID controllers active for all functions
- Safe, certified classical control
- Reduced efficiency and comfort
- No safety impact

### Communication Bus Failure

**Indication:** "ECS DATA BUS FAIL" or "ECS COMM FAULT"

**Crew Actions:**
1. Check if environmental control continues
2. If control lost: Use emergency environmental panel
3. If sensors lost: Use backup displays
4. May require manual control via ECS panel

**System Response:**
- Automatic reversion to redundant communication path
- If all paths lost: Safe mode, fixed settings

### Sensor Failures

**Indication:** "ECS SENSOR FAIL" with specific sensor identified

**Crew Actions:**
1. Note affected sensor
2. Verify system continues with sensor fusion
3. Reduced accuracy expected in affected zone
4. Manual adjustments for affected area if needed

**System Response:**
- Sensor fusion continues with remaining sensors
- Affected zone may use adjacent zone data
- Graceful degradation, not system failure

## Emergency Procedures

### Smoke/Fumes in Cabin

**If NN ECS indicates poor air quality:**
1. Verify air quality alert is not false alarm
2. Increase ventilation (AUTO or MANUAL override)
3. If smoke/fumes confirmed: Execute smoke drill per QRH
4. NN ECS air quality monitoring assists in source location

### Rapid Depressurization

**NN Pressure Control Response:**
- Automatic fast pressure relief to equalize
- System supports emergency descent

**Crew Actions:**
1. Execute emergency descent per QRH
2. NN pressure control assists but crew retains authority
3. Manual override available if needed

### Thermal Runaway / Overheat

**If NN HVAC fails to control temperature:**
1. Switch to MANUAL control via ECS panel
2. Reduce heat sources
3. Increase ventilation
4. Consider altitude change for cooling

## System Limitations

### Operating Limits

- **Altitude**: Up to 45,000 ft (pressure control)
- **Temperature**: -40°C to +50°C external (HVAC)
- **Humidity**: 0-100% RH external
- **Passenger Load**: 0-220 passengers

### Performance Limitations

With NN Active:
- Inference latency: <100ms
- Temperature accuracy: ±0.5°C
- Pressure accuracy: ±0.1 psi
- Energy savings: 15% typical

With Classical Control (NN Inoperative):
- Temperature accuracy: ±2°C
- Pressure accuracy: ±0.2 psi
- Energy savings: 0% (baseline)
- Higher crew workload

### Dispatch Limitations

See MEL for specific dispatch restrictions:
- Single model inoperative: Likely dispatchable with notes
- Multiple model failures: May require restrictions
- Complete NN failure: Dispatchable with classical control
- Sensor failures: Depends on quantity and location

## Crew Training Requirements

### Initial Training

- NN ECS system overview: 2 hours ground school
- Normal operations: Simulator scenarios
- Abnormal operations: Simulator scenarios
- Classical control fallback: Simulator practice

### Recurrent Training

- Annual: Abnormal procedures review
- As needed: Software update training

## Maintenance Coordination

### Crew Maintenance Reports

Write up in logbook for:
- Any amber or red NN status indications
- Unusual temperature/pressure behavior
- Air quality alerts
- Passenger comfort complaints
- Any manual overrides used

### Performance Monitoring

Flight crew assists by:
- Noting CO₂ capture totals each flight
- Reporting energy savings trends
- Identifying comfort trends

## Document Control

- **Version**: 1.0
- **Status**: WORKING
- **Last Updated**: 2025-11-17
- **Related Documents**:
  - Flight Crew Operating Manual (FCOM) - ECS Section
  - Quick Reference Handbook (QRH) - ECS Abnormals
  - Minimum Equipment List (MEL) - ATA 21
  - [95-20-21-801 Operations Manual](Documentation/95-20-21-801_Operations_Manual.md)
  - [95-20-21-803 Troubleshooting Guide](Documentation/95-20-21-803_Troubleshooting_Guide.md)

---

**For maintenance procedures, see:**
- [95-20-21-802 Maintenance Procedures](Documentation/95-20-21-802_Maintenance_Procedures.md)
- [Technician Manual](Documentation/Training_Materials/Technician_Manual.md)
