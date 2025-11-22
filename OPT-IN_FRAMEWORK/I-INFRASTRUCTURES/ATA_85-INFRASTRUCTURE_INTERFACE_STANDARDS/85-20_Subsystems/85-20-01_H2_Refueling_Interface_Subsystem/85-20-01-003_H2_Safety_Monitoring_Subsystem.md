# 85-20-01-003 — H2 Safety Monitoring Subsystem

## Document Metadata

```yaml
document_id: "85-20-01-003"
title: "H2 Safety Monitoring Subsystem"
parent_system: "85-20-01 H2 Refueling Interface Subsystem"
category: "Component Specification"
status: "DRAFT"
version: "1.0"
last_updated: "2025-11-21"
```

## Purpose

This document specifies the safety monitoring systems that detect hazardous conditions during H2 refueling and initiate protective actions. This subsystem is critical for achieving DAL-A safety objectives.

## H2 Leak Detection System

### Detection Technology

**Primary Sensors:** Electrochemical H2 sensors (3 sensors minimum, 2oo3 voting)

**Secondary Sensors:** Catalytic bead sensors (dissimilar technology for diversity)

**Sensor Locations:**
- Near coupling/receptacle (2 sensors within 0.5m)
- Under aircraft fuselage near refueling area (2 sensors)
- Ground level surrounding refueling area (4 sensors in 360° coverage)

**Standards:** [ISO 26142](https://www.iso.org/standard/43498.html) (Hydrogen detection apparatus — Stationary applications)

### Detection Thresholds

| Threshold | H2 Concentration | Action |
|-----------|------------------|--------|
| Advisory | 0.1% (1000 ppm) | Yellow alarm, notify operator |
| Warning | 0.4% (4000 ppm) | Orange alarm, reduce flow rate |
| Critical | 1.0% (10,000 ppm) | Red alarm, automatic emergency shutdown |
| LFL (Lower Flammable Limit) | 4.0% | (Reference only; system acts well below LFL) |

**Rationale:** Act at 10% of LFL (4%) = 0.4% for safety margin

### Sensor Performance

- **Response Time:** <2 seconds to 90% of final reading
- **Accuracy:** ±10% of reading or ±0.1% H2 (whichever greater)
- **Drift:** <±0.2% H2 per year
- **Operating Temperature:** -30 to +50°C
- **Self-Test:** Automatic self-test every 24 hours

### Sensor Failure Detection

**Fail-to-Warn State:** If sensor fails, assume unsafe condition

**Detection Methods:**
- Sensor current/voltage out of normal range
- Response to periodic calibration gas exposure
- Comparison to redundant sensors (2oo3 voting detects one failed sensor)

**Action on Sensor Failure:** Inhibit refueling until sensor replaced

## Safety Interlocks

### Pre-Refueling Interlocks

Refueling inhibited unless all conditions met:

1. ✓ Aircraft positioned and chocked
2. ✓ Grounding/bonding verified (resistance <1 ohm)
3. ✓ H2 detection system operational (all sensors passed self-test)
4. ✓ Safety zone clear (no ignition sources, no unauthorized personnel)
5. ✓ Weather conditions acceptable (wind <30 kt, no thunderstorms)
6. ✓ Refueling authorization received (via 85-20-06 data link)
7. ✓ Aircraft fuel system ready (tank not overpressure, vent open)

**Implementation:** Hardwired safety relay logic (independent of software control)

### Active Refueling Interlocks

Refueling automatically terminated if:

1. ✗ H2 detected above warning threshold (0.4%)
2. ✗ Grounding/bonding lost
3. ✗ Coupling leak detected
4. ✗ Over-pressure condition (>1.1x max operating pressure)
5. ✗ Emergency stop button pressed (aircraft or ground)
6. ✗ Evacuation signal received (from 85-20-04)
7. ✗ Aircraft movement detected (accelerometer on aircraft or visual system)

**Implementation:** Dual-redundant safety relay logic with fail-safe defaults

## Emergency Shutdown System

### Shutdown Triggers

**Automatic:**
- H2 critical threshold exceeded (1.0%)
- Coupling rupture detected (rapid pressure drop)
- Fire detected (via 85-20-08 fire detection)
- Evacuation signal (via 85-20-04)

**Manual:**
- Emergency stop button (aircraft crew)
- Emergency stop button (ground operator)
- Remote shutdown (operations center via 85-20-06)

### Shutdown Sequence

**Phase 1: Immediate (0-1 second)**
1. Close H2 flow valves (solenoid valves, fast-acting)
2. Activate visual/audible alarm (rotating beacon, siren)
3. Log shutdown event with timestamp

**Phase 2: Controlled Depressurization (1-10 seconds)**
1. Open vent valves to safe location (upwind, elevated)
2. Monitor H2 concentration during venting
3. Maintain grounding/bonding during venting

**Phase 3: Post-Shutdown (10+ seconds)**
1. Verify zero H2 flow
2. Verify H2 concentration decreasing
3. Notify ARFF and operations center (via 85-20-06)
4. Secure scene, initiate investigation

**Recovery:** Manual reset required after investigation and clearance

### Shutdown Performance

- **Valve Closure Time:** <1 second from trigger to zero flow
- **Alarm Activation:** <0.5 seconds from trigger
- **Notification:** <2 seconds to operations center

## Grounding and Bonding Verification

### Bonding System

**Ground Cable:** Dedicated grounding cable connecting aircraft structure to ground infrastructure

**Cable Specifications:**
- Conductor: Copper, minimum 25 mm² cross-section
- Clamp: Heavy-duty, teeth or pins for low-resistance contact
- Insulation: Visible color (yellow with green stripe)

**Hose Bonding:** Conductive wire integrated in H2 hose assembly, bonded at both ends

### Continuity Verification

**Method:** Automatic ohmmeter test before refueling authorization

**Test Points:**
- Aircraft structure → Ground infrastructure
- Hose nozzle → Ground infrastructure
- Coupling (when connected)

**Acceptance Criteria:** <1 ohm total resistance

**Test Frequency:** Before each refueling operation, and continuous during refueling

**Action on Failure:** Inhibit refueling, alert operator to verify/correct bonding

## Environmental Monitoring

### Wind Speed and Direction

**Purpose:** Ensure H2 dispersion if leaked, avoid accumulation

**Sensor:** Ultrasonic anemometer near refueling area

**Limits:**
- **Maximum Wind Speed:** 30 knots (15 m/s) — above this, refueling delayed
- **Wind Direction:** Monitored to position personnel and equipment upwind of aircraft

### Temperature Monitoring

**Purpose:** Monitor coupling and hose temperature (compression heating)

**Sensors:** Thermocouples on coupling nozzle and high-pressure hose

**Limits:**
- **Advisory:** +65°C (warn operator, check for excessive flow rate)
- **Warning:** +85°C (reduce flow rate)
- **Critical:** +100°C (emergency shutdown)

### Lightning and Thunderstorm Detection

**Purpose:** Avoid refueling during electrical storm (lightning risk)

**Detection:** Integration with airport weather system or local lightning detection

**Action:** Inhibit refueling if thunderstorm within 10 km or lightning detected within 30 minutes

## Fire Detection Interface

**Integration with 85-20-08 Safety and Monitoring Subsystem**

**Sensors:** Optical flame detectors monitoring refueling area

**Action on Fire Detection:**
1. Emergency shutdown of H2 refueling
2. Activate fire suppression system (if available)
3. Alert ARFF immediately
4. Prepare for emergency evacuation (85-20-04)

## Monitoring and Alarms

### Operator Interface

**HMI (Human-Machine Interface) on Ground Control Cabinet:**
- Real-time H2 concentration display (from all sensors)
- Grounding continuity status
- Weather conditions (wind, temperature)
- Refueling status and progress
- Alarm annunciation panel

**Alarm Levels:**
- **Advisory (Yellow):** Condition requiring attention, refueling can continue
- **Warning (Orange):** Condition requiring action, refueling rate reduced
- **Critical (Red):** Hazardous condition, automatic emergency shutdown

### Remote Monitoring

**Integration with 85-20-06 Data and Communications:**
- Real-time status to operations center
- Historical data logging for trend analysis
- Predictive maintenance alerts (sensor drift, valve cycle count)

## Maintenance and Calibration

### H2 Sensor Calibration

**Frequency:** Every 6 months or 200 refueling operations (whichever first)

**Method:**
1. Expose sensor to known H2 concentration (span gas)
2. Verify sensor reading within ±10% of span gas concentration
3. Adjust calibration if necessary
4. Re-test with span gas and zero gas (ambient air)

**Records:** Calibration certificate for each sensor, stored electronically

### Safety System Testing

**Functional Test (Monthly):**
1. Simulate H2 leak (apply calibration gas to sensor)
2. Verify alarm activation and valve closure
3. Test emergency stop buttons (aircraft and ground)
4. Verify grounding continuity test function

**Comprehensive Test (Annual):**
1. Full system functional test (all interlocks and alarms)
2. Response time verification (valve closure <1s)
3. Sensor cross-calibration (compare all sensors)
4. Inspection of grounding cables and clamps

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_.
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-21

---

*Reference: [85-20-01 H2 Refueling Interface Subsystem README](./README.md)*
