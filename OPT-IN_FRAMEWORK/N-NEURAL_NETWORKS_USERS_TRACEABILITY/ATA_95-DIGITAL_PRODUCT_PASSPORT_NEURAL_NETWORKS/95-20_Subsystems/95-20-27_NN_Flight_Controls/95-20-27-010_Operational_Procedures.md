# 95-20-27-010 — Operational Procedures

**Document ID:** 95-20-27-010  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active

---

## 1. Purpose

This document provides operational procedures for flight crews operating the AMPEL360 BWB H₂ Hy-E with the FCS_NN (Flight Control System Neural Network) subsystem.

---

## 2. System Overview for Flight Crews

### 2.1 What is FCS_NN?

The FCS_NN is an advanced flight control system that uses neural networks to enhance:
- **Flight efficiency**: Optimizes control surface deflections for minimum drag
- **Passenger comfort**: Reduces gust-induced loads by 30%
- **Safety**: Provides predictive envelope protection
- **Handling**: Maintains precise flight path tracking

### 2.2 Normal vs Degraded Operation

| Mode | Description | Crew Action |
|------|-------------|-------------|
| **Normal Law** | Full FCS_NN active | Monitor, enjoy enhanced performance |
| **Alternate Law** | Envelope protection only | Increased monitoring, conservative handling |
| **Direct Law** | Conventional FCS | Manual handling, use standard techniques |

---

## 3. Pre-Flight Procedures

### 3.1 FCS_NN System Check

**Location**: Overhead Panel FCS Section

**Procedure**:
1. **FCS_NN Master Switch**: ON
2. **Observe EICAS**: Check for "FCS NN READY" message
3. **BIT Execution**: Press "FCS BIT" button
4. **Wait**: 30 seconds for BIT completion
5. **Verify**: "FCS NN BIT PASS" on EICAS
6. **If BIT FAIL**:
   - Note failure code on EICAS
   - Consult MEL (Minimum Equipment List)
   - If dispatch allowed, expect Direct Law operation

### 3.2 ECAM FCS_NN Page Review

**Access**: ECAM FCS_NN button or AUTO display during startup

**Check**:
- **Model Status**: All models show "ACTIVE" (green)
  - Aero Predictor
  - Control Surface Optimizer
  - Gust Load Alleviation
  - Envelope Protection
  - Flight Path Stabilization
  - Trim Optimizer
- **Health Scores**: All ≥95% (green)
- **IMA Partition Status**: "RUNNING" for all FCS_NN partitions
- **No Cautions/Warnings**

### 3.3 MEL Considerations

| Component | MEL Category | Dispatch Restrictions |
|-----------|--------------|----------------------|
| **FCS_NN Complete System** | B | 3 days, Direct Law, VMCA +10 kt, No Cat II/III |
| **Aero Predictor** | C | 10 days, Reduced optimization |
| **Gust Load Alleviation** | C | 10 days, Avoid severe turbulence |
| **Trim Optimizer** | D | No restriction, +2% fuel penalty |

---

## 4. Normal Operations

### 4.1 Taxi, Takeoff, Initial Climb

**FCS_NN State**: Active, Normal Law

**Crew Actions**:
- **Standard Procedures**: No special actions required
- **Envelope Protection**: Automatic α and speed protection active
- **GLA**: Inactive below 10,000 ft (configurable)
- **Trim Optimization**: Active, monitors CG shift

**Notes**:
- Aircraft may feel slightly "lighter" on controls due to optimization
- Expect smoother handling in gusty conditions
- Auto-trim may be more active than conventional aircraft

### 4.2 Cruise

**FCS_NN State**: Full optimization active

**Crew Actions**:
- **Monitor Fuel Flow**: Observe 2-3% fuel savings vs flight plan
- **Check ECAM FCS_NN Page**: Periodically verify health scores
- **Observe Handling**: Aircraft maintains precise altitude/track

**GLA Operation**:
- **Auto-engages** in turbulence (TI >20%)
- **EICAS message**: "GLA ACTIVE" (cyan advisory)
- **Effectiveness**: Observe reduced vertical accelerations
- **Manual Disable**: GLA button on glareshield (if crew prefers)

**Trim Optimization**:
- **Fuel Transfer**: May occur automatically to optimize CG
- **ECAM Synoptic**: Shows fuel transfer in progress (animated arrows)
- **No Crew Action**: System manages CG autonomously
- **Override**: FUEL TRANSFER switches to MANUAL if needed

### 4.3 Descent, Approach, Landing

**FCS_NN State**: Active, Normal Law (transitions as needed)

**Crew Actions**:
- **Approach Flaps**: FCS_NN adjusts for configuration changes
- **ILS/GLS Approach**: Flight Path Stabilization provides precision tracking
- **Autoland**: Full FCS_NN support for Cat II/III
- **Flare**: NN optimizes flare for smooth touchdown
- **Rollout**: NN assists directional control

**Notes**:
- **Crosswind Landings**: NN provides coordinated roll-yaw response
- **Wind Shear**: NN plus conventional wind shear protection active
- **Go-Around**: NN optimizes pitch-up for TOGA thrust

---

## 5. Abnormal Operations

### 5.1 FCS_NN Degradation

**Indications**:
- **EICAS Caution**: "FCS NN DEGRADED" (amber)
- **ECAM Action**: FCS_NN status page displays automatically
- **Handling Change**: Aircraft may feel less responsive

**Crew Actions**:
1. **Acknowledge Caution**: Press MASTER CAUTION
2. **Review ECAM**: Note which model(s) degraded
3. **Check ECAM Actions**: Follow any crew actions (usually none)
4. **Continue Flight**: Normal Law may still be available
5. **Land at Nearest Suitable Airport**: If further degradation occurs
6. **Post-Flight**: Enter in logbook, notify maintenance

**Degradation Levels**:
- **Minor** (Health 80-95%): Continue as planned, monitor
- **Major** (Health 50-80%): Reduce to Alternate Law, consider diversion
- **Critical** (<50%): Transition to Direct Law, land ASAP

### 5.2 FCS_NN Failure

**Indications**:
- **EICAS Warning**: "FCS NN FAIL" (red)
- **ECAM Alert**: FCS_NN status page displays
- **Flight Control Mode**: Automatic reversion to Direct Law
- **EICAS Message**: "DIRECT LAW" (amber)

**Crew Actions**:
1. **Acknowledge Warning**: Press MASTER WARNING
2. **Confirm Direct Law**: Check PFD for "DIRECT LAW" annunciation
3. **Review ECAM Actions**: Follow any crew actions
4. **Hand-Fly or Disconnect AP**: Assess handling characteristics
5. **Increase Monitoring**: More pilot input required
6. **Consider Diversion**: Evaluate weather, runway length, crew workload
7. **Land ASAP**: Direct Law is safe but not preferred for long flights

**Direct Law Handling**:
- **No Envelope Protection**: Pilot responsible for all limits
- **No Auto-Trim**: Manual trim required
- **No GLA**: Expect normal gust loads
- **Conventional Feel**: Similar to traditional FCS

### 5.3 Envelope Protection Alert

**Indications**:
- **PFD Visual**: Flashing envelope indicator (α, speed, attitude)
- **Aural Alert**: "OVERSPEED" / "STALL" / "BANK ANGLE"
- **Stick Shaker**: (if approaching stall)
- **EICAS Message**: "ENVELOPE PROT ACTIVE" (amber)

**Crew Actions**:
1. **Immediate**: Comply with recovery guidance
   - **Overspeed**: Reduce thrust, extend spoilers, increase pitch
   - **Stall**: Reduce AoA, add thrust, wings level
   - **Bank Angle**: Roll toward wings level
2. **Feel Increased Stick Force**: NN is providing resistance
3. **Allow NN Assistance**: Do not fight the protection
4. **Override if Necessary**: Sustained 150 N force for >2 seconds
5. **Post-Event**: Review on ECAM for causal factors

**Override Considerations**:
- **Only if absolutely necessary** (e.g., terrain avoidance, TCAS RA)
- **Protection will re-engage** once stick force relaxes
- **Override logged**: Maintenance and safety review required

### 5.4 Sensor Failure with FCS_NN

**Indications**:
- **EICAS Caution**: "ADC 1 FAULT" / "IRU 2 FAULT" / etc.
- **ECAM Action**: Sensor status page displays
- **FCS_NN Status**: May remain Normal Law if redundant sensors available

**Crew Actions**:
1. **Follow ECAM Actions**: Standard sensor failure procedure
2. **Monitor FCS_NN Health**: Check ECAM FCS_NN page
3. **If FCS_NN Reverts**: Expect transition to Alternate or Direct Law
4. **Continue or Divert**: Based on MEL and weather

**FCS_NN Reconfiguration**:
- **Automatic**: FCS_NN will reconfigure to use remaining sensors
- **May Degrade**: Some models may become unavailable
- **Crew Notification**: EICAS message indicates reconfiguration

---

## 6. Emergency Procedures

### 6.1 Loss of All Flight Controls

**NOTE**: FCS_NN provides additional layer of redundancy, but conventional procedures still apply.

**Immediate Actions**:
1. **Maintain Aircraft Control**: Use any available control authority
2. **Assess Control Authority**: Pitch, roll, yaw, throttle
3. **Declare Emergency**: ATC notification
4. **FCS_NN Status**: Check if NN can provide assistance
5. **If Partial Control**: Use NN optimization to maximize effectiveness

**FCS_NN Backup**:
- **Degraded Control Authority**: NN can optimize limited control surfaces
- **Asymmetric Thrust**: NN can coordinate with FADEC for directional control
- **Trim Management**: NN can help stabilize aircraft with limited inputs

### 6.2 Uncommanded Control Surface Movements

**Indications**:
- **Aircraft deviates** from commanded flight path
- **Control surface position** does not match pilot input
- **Possible oscillations** or hunting

**Immediate Actions**:
1. **Disconnect Autopilot**: Press AP disconnect button
2. **FCS_NN Master**: OFF (overhead panel)
3. **Assess Control**: Hand-fly in Direct Law
4. **If Control Regained**: Continue flight with FCS_NN off
5. **If No Improvement**: Follow conventional runaway trim/control procedures

**After Securing Aircraft**:
1. **Declare Emergency**: If any doubt about controllability
2. **Divert**: Land at nearest suitable airport
3. **Maintenance**: Do not re-engage FCS_NN

---

## 7. Special Procedures

### 7.1 Cold Weather Operations

**Considerations**:
- **Icing Conditions**: FCS_NN adapts to degraded aerodynamics
- **Envelope Margins**: Automatically reduced (more conservative)
- **Ice Detection**: FCS_NN monitors for ice-induced changes
- **De-Ice Systems**: Coordinate with FCS_NN (no crew action)

**Crew Actions**:
- **Standard De-Ice Procedures**: No special FCS_NN actions
- **Monitor EICAS**: Watch for "FCS NN ICING ADAPT" (cyan advisory)
- **Expect**: Slightly reduced optimization efficiency

### 7.2 High Altitude Operations

**Considerations**:
- **Thin Air**: Reduced control authority
- **Coffin Corner**: Narrow speed margin
- **FCS_NN Advantage**: Precise envelope management

**Crew Actions**:
- **Monitor Speed Margin**: FCS_NN will alert if margin <10 kt
- **Smooth Inputs**: Let NN optimize control deflections
- **Trust Envelope Protection**: Will prevent overspeed or stall

### 7.3 One Engine Inoperative (OEI)

**Considerations**:
- **Asymmetric Thrust**: FCS_NN compensates with rudder/differential thrust
- **V_MC Management**: Envelope protection prevents V_MC exceedance
- **Trim**: Auto-trim handles rudder trim requirement

**Crew Actions**:
- **Standard OEI Procedures**: No special FCS_NN actions
- **Reduced Rudder Input Required**: NN provides most of yaw compensation
- **Monitor**: Observe reduced pilot workload

### 7.4 Severe Turbulence

**Considerations**:
- **GLA Active**: Should reduce loads by ~30%
- **If GLA Uncomfortable**: Crew can disable

**Crew Actions**:
- **Standard Turbulence Procedures**: Reduce speed to V_turb, seat belts, etc.
- **GLA Active**: Observe "GLA ACTIVE" on EICAS (cyan)
- **If Uncomfortable**: Press GLA button on glareshield to disable
- **Re-enable GLA**: Press button again when comfortable
- **Note**: GLA disabled = conventional gust loads (higher)

---

## 8. Performance Monitoring

### 8.1 Fuel Efficiency

**Normal Cruise**:
- **Expect**: 2-3% fuel savings vs flight plan
- **Monitor**: Fuel totalizer compared to flight plan
- **If Not Achieved**: Verify FCS_NN in Normal Law, check ECAM for degradation

### 8.2 Passenger Comfort

**GLA Performance**:
- **Subjective**: Smoother ride in turbulence
- **Objective**: Cabin crew feedback, passenger comments
- **If Complaints**: Check GLA status, consider manual disable

### 8.3 Handling Qualities

**Normal Feel**:
- **Precise**: Aircraft should maintain altitude/track precisely
- **Smooth**: Control surface movements should be smooth
- **Responsive**: Aircraft should respond crisply to inputs

**If Degraded**:
- **Sluggish**: May indicate FCS_NN degradation
- **Oscillations**: May indicate NN issue, consider disabling
- **Unusual Feel**: Consult ECAM, consider Direct Law

---

## 9. Communication and Coordination

### 9.1 Dispatch

**Pre-Flight**:
- **FCS_NN Status**: Brief dispatcher on MEL items
- **Expected Performance**: Fuel savings may affect fuel planning

**In-Flight**:
- **FCS_NN Failure**: Notify dispatch, discuss diversion options
- **Degraded Performance**: ACARS message for maintenance awareness

### 9.2 Maintenance

**Post-Flight**:
- **Logbook Entry**: Any FCS_NN cautions, warnings, or anomalies
- **ACARS Download**: Automatic for maintenance trending
- **Crew Report**: Subjective assessment of NN performance

### 9.3 ATC

**Normal**:
- **No Special Phraseology**: FCS_NN is transparent to ATC

**Degraded/Failed**:
- **Inform ATC**: "FCS degraded, request vectors" (if helpful)
- **Emergency**: "FCS failure, Direct Law, request priority"

---

## 10. Training Requirements

### 10.1 Initial Training

**Ground School**: 4 hours
- FCS_NN system overview
- Normal operation
- Abnormal procedures
- Emergency procedures

**Simulator**: 2 hours
- Normal Law handling
- Degradation scenarios
- Failure modes
- Envelope protection demonstration

### 10.2 Recurrent Training

**Annual**: 1 hour simulator
- FCS_NN failure scenario
- Direct Law handling
- Envelope protection review

### 10.3 Differences Training (from Conventional Aircraft)

**For Pilots New to FCS_NN**: 2 hours simulator
- Handling differences
- Enhanced capabilities
- Failure modes

---

## 11. Limitations

### 11.1 Operational Limitations

| Limitation | Value | Notes |
|------------|-------|-------|
| **Minimum Crew** | 2 pilots | FCS_NN monitoring required |
| **Turbulence** | No limit | GLA may be disabled by crew |
| **Icing** | Standard limits | FCS_NN adapts automatically |
| **Crosswind** | Standard limits | NN assists with crosswind correction |
| **Cat II/III** | Full capability | FCS_NN supports autoland |

### 11.2 MEL Limitations

See section 3.3 above.

---

## 12. Quick Reference

### 12.1 Normal Checklists

**Pre-Flight**:
- FCS_NN Master: ON
- FCS BIT: EXECUTE
- EICAS: "FCS NN READY"

**In-Flight**:
- Monitor ECAM FCS_NN page (periodically)
- Observe fuel savings (2-3% typical)

### 12.2 Abnormal Checklist

**FCS_NN Degraded**:
1. MASTER CAUTION: ACKNOWLEDGE
2. ECAM: REVIEW
3. HEALTH SCORES: CHECK
4. CONTINUE or DIVERT: ASSESS

**FCS_NN Failed**:
1. MASTER WARNING: ACKNOWLEDGE
2. ECAM: REVIEW & COMPLY
3. DIRECT LAW: CONFIRMED
4. HANDLING: ASSESS
5. DIVERT: CONSIDER

### 12.3 Emergency Checklist

**Envelope Protection Alert**:
1. RECOVERY ACTION: IMMEDIATE
2. COMPLY with PFD guidance
3. OVERRIDE if necessary (sustained force)

**FCS_NN Runaway**:
1. AP: DISCONNECT
2. FCS_NN MASTER: OFF
3. CONTROL: ASSESS
4. EMERGENCY: DECLARE

---

## 13. References

- [95-20-27-001_FCS_NN_Overview.md](95-20-27-001_FCS_NN_Overview.md)
- [95-20-27-009_Safety_and_Certification.md](95-20-27-009_Safety_and_Certification.md)
- **Flight Crew Operating Manual (FCOM)**: ATA 27 Flight Controls
- **Quick Reference Handbook (QRH)**: FCS_NN Procedures
- **Minimum Equipment List (MEL)**: ATA 27-XX FCS_NN

**Detailed Training Materials**: `Documentation/Training_Materials/Crew_Training_Guide.pdf`

---

## Document Control

- **Owner**: AMPEL360 Flight Operations
- **Version**: 1.0
- **Status**: Active
- **Classification**: Flight Crew Procedures
- **Last Updated**: 2025-11-17
