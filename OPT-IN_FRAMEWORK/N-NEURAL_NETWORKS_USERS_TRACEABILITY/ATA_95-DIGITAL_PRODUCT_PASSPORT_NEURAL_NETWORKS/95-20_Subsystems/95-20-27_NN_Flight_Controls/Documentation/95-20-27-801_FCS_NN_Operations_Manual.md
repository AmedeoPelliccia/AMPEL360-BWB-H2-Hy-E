# 95-20-27-801 — FCS NN Operations Manual

**Document ID:** 95-20-27-801  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active  
**Classification:** Flight Operations

---

## 1. Introduction

### 1.1 Purpose

This Operations Manual provides comprehensive guidance for flight crews operating the AMPEL360 BWB H₂ Hy-E aircraft equipped with the FCS_NN (Flight Control System Neural Network) subsystem.

### 1.2 Scope

This manual covers:
- Normal operations procedures
- Abnormal and emergency procedures
- Performance optimization guidelines
- Crew coordination and communication
- Operational limitations

### 1.3 Related Documents

- **95-20-27-010**: Operational Procedures (Quick Reference)
- **FCOM ATA 27**: Flight Controls Chapter
- **QRH**: Quick Reference Handbook
- **MEL**: Minimum Equipment List

---

## 2. System Description for Operators

### 2.1 FCS_NN Overview

The FCS_NN subsystem enhances the conventional flight control system with six neural network models:

1. **Aerodynamic Predictor**: Provides real-time aerodynamic predictions (1000× faster than CFD)
2. **Control Surface Optimizer**: Optimizes control deflections for minimum drag
3. **Gust Load Alleviation**: Reduces gust-induced loads by 30%
4. **Envelope Protection**: Prevents flight envelope exceedances
5. **Flight Path Stabilization**: Maintains precise trajectory tracking
6. **Trim Optimizer**: Optimizes trim for fuel efficiency

**Benefits**:
- 2-3% fuel savings per flight
- 30% reduction in structural loads
- Enhanced passenger comfort
- Improved handling qualities
- Predictive envelope protection

### 2.2 Control Modes

| Mode | Description | FCS_NN Status | Pilot Workload |
|------|-------------|---------------|----------------|
| **Normal Law** | Full FCS_NN active | All models operational | Low |
| **Alternate Law** | Envelope protection only | Degraded optimization | Medium |
| **Direct Law** | Conventional FCS | FCS_NN disabled | High |

Mode transitions are automatic based on system health. Crew is notified via EICAS/ECAM.

---

## 3. Pre-Flight Operations

### 3.1 Pre-Flight Briefing

**Pilot Flying (PF)** and **Pilot Monitoring (PM)** should discuss:

- Current FCS_NN status (check dispatch release)
- Any MEL items affecting FCS_NN
- Expected weather (turbulence, icing) and GLA operation
- Fuel planning (include 2-3% FCS_NN savings)
- Abnormal procedures review (if first flight of day)

### 3.2 Exterior Inspection

**Standard exterior inspection applies**. No special FCS_NN-related items.

### 3.3 Flight Deck Setup

**Overhead Panel — FCS Section**:

1. **FCS_NN MASTER**: Check OFF → ON
2. **Observe EICAS**: "FCS NN INITIALIZING" (cyan, 10-15 seconds)
3. **Wait for**: "FCS NN READY" (green)
4. **If "FCS NN FAULT"**:
   - Note fault code
   - Check MEL for dispatch eligibility
   - Expect Direct Law operation

**ECAM FCS_NN Page**:

- Press **ECAM FCS** button or allow auto-display during startup
- **Verify**:
  - All models show "ACTIVE" (green)
  - Health scores ≥95% (green)
  - IMA partitions "RUNNING"
  - No cautions or warnings

### 3.4 Built-In Test (BIT)

**Execute BIT**:

1. Press **FCS BIT** button (overhead panel)
2. **Observe EICAS**: "FCS NN BIT IN PROGRESS" (cyan, 30 seconds)
3. **Wait for**:
   - **Pass**: "FCS NN BIT PASS" (green) → Continue
   - **Fail**: "FCS NN BIT FAIL" + code → Consult MEL

**BIT Tests**:
- Model integrity (CRC checks)
- Inference test (known input → expected output)
- Interface loopback (sensors, actuators)
- IMA partition health

---

## 4. Normal Flight Operations

### 4.1 Taxi

**FCS_NN Status**: Active, Normal Law

**Procedures**:
- Standard taxi procedures apply
- FCS_NN has minimal effect during taxi (low speed)
- Verify control surface movement during flight control check

### 4.2 Takeoff

**FCS_NN Status**: Active, Normal Law

**Procedures**:
- **Standard takeoff procedures**
- Envelope protection automatically active (α, speed limits)
- Control feel may be slightly lighter due to optimization
- Trim may adjust automatically (no crew action required)

**Notes**:
- FCS_NN optimizes control deflections for best climb performance
- Expect smoother rotation and initial climb

### 4.3 Climb

**FCS_NN Status**: Active, Normal Law

**Procedures**:
- **Standard climb procedures**
- Monitor fuel flow (should be 2-3% lower than flight plan prediction)
- Trim optimizer adjusts CG via fuel transfer (if needed)

**ECAM Observations**:
- May see "FUEL TRANSFER IN PROGRESS" (cyan)
- Fuel synoptic shows transfer with arrows
- No crew action required unless manual override desired

### 4.4 Cruise

**FCS_NN Status**: Active, Normal Law (Full Optimization)

**Procedures**:
- **Standard cruise procedures**
- FCS_NN provides maximum efficiency in this phase

**Performance Monitoring**:
- **Fuel Flow**: Should be 2-3% below flight plan
- **Drag Optimization**: CD displayed on ECAM FCS page
- **CG Position**: May shift ±2% MAC for optimal L/D

**GLA Operation**:
- GLA auto-activates if turbulence intensity >20%
- **EICAS**: "GLA ACTIVE" (cyan advisory)
- Expect smoother ride, reduced vertical accelerations
- **To Disable**: Press **GLA** button on glareshield (if uncomfortable)

**Trim Optimization**:
- Continuous automatic trim adjustments
- Elevator and stabilizer may move slowly (normal)
- Fuel transfers may occur for CG management

### 4.5 Descent

**FCS_NN Status**: Active, Normal Law

**Procedures**:
- **Standard descent procedures**
- FCS_NN optimizes for fuel efficiency during descent

**Notes**:
- Speed management handled by Flight Path Stabilization
- Expect precise VNAV tracking

### 4.6 Approach

**FCS_NN Status**: Active, Normal Law

**Procedures**:
- **Standard approach procedures**
- Flight Path Stabilization provides precision tracking
- Envelope protection remains active

**ILS/GLS Approach**:
- Expect very precise localizer/glideslope tracking
- Cross-track error typically <3m lateral, <5ft vertical
- Smoother approach in gusty conditions (GLA active)

**CAT II/III Autoland**:
- Full FCS_NN support for autoland
- Flight Path Stabilization provides precision guidance
- Standard autoland monitoring procedures apply

### 4.7 Landing

**FCS_NN Status**: Active, Normal Law

**Procedures**:
- **Standard landing procedures**
- FCS_NN optimizes flare for smooth touchdown
- Crosswind correction automatically coordinated

**Flare**:
- NN optimizes pitch rate for gentle touchdown
- Expect smooth, consistent landings

**Rollout**:
- NN assists with directional control
- Standard rollout procedures apply

### 4.8 After Landing / Shutdown

**Procedures**:
- Standard after-landing checklist
- **FCS_NN MASTER**: Leave ON until shutdown
- FCS_NN auto-logs flight data for maintenance

---

## 5. Abnormal Operations

### 5.1 FCS_NN Degradation

**See 95-20-27-010 Section 5.1 for detailed procedures**

**Summary**:
1. Acknowledge EICAS caution
2. Review ECAM for degraded model(s)
3. Assess impact on flight
4. Continue or divert based on severity

### 5.2 FCS_NN Failure

**See 95-20-27-010 Section 5.2 for detailed procedures**

**Summary**:
1. Acknowledge EICAS warning
2. Confirm Direct Law engagement
3. Assess handling characteristics
4. Consider diversion
5. Land as soon as practical

### 5.3 Envelope Protection Activation

**See 95-20-27-010 Section 5.3 for detailed procedures**

**Summary**:
1. Comply with recovery guidance (immediate)
2. Do not fight protection unless necessary
3. Override only for terrain/TCAS avoidance

---

## 6. Emergency Operations

### 6.1 Loss of Flight Controls

**See 95-20-27-010 Section 6.1 for detailed procedures**

**Summary**:
1. Maintain aircraft control (any means available)
2. Assess control authority
3. Declare emergency
4. FCS_NN may provide backup (if operational)

### 6.2 Uncommanded Control Surface Movements

**See 95-20-27-010 Section 6.2 for detailed procedures**

**Summary**:
1. Disconnect autopilot
2. FCS_NN Master: OFF
3. Assess control in Direct Law
4. Declare emergency if needed
5. Divert to nearest suitable airport

---

## 7. Performance Optimization

### 7.1 Maximizing Fuel Efficiency

To maximize FCS_NN fuel savings:

- **Fly Smoothly**: Minimize large control inputs
- **Trust the System**: Let NN optimize control deflections
- **Allow Fuel Transfers**: Do not override automatic CG management
- **Use GLA**: Keep GLA enabled for load reduction (less structural stress = longer life)

### 7.2 Passenger Comfort

To maximize passenger comfort:

- **Enable GLA**: Especially in moderate+ turbulence
- **Smooth Inputs**: Let Flight Path Stabilization do the work
- **Cruise Altitude**: FCS_NN is most effective at optimal cruise altitude

---

## 8. Crew Coordination

### 8.1 Callouts

**Standard callouts apply**, plus:

- **"FCS NN DEGRADED"** (PM, upon EICAS caution)
- **"FCS NN FAILED, DIRECT LAW"** (PM, upon EICAS warning)
- **"ENVELOPE PROTECTION ACTIVE"** (PM, upon activation)
- **"GLA ACTIVE"** (PM, first activation per flight)

### 8.2 Pilot Flying / Pilot Monitoring Duties

**Pilot Flying (PF)**:
- Fly the aircraft (no change from standard procedures)
- Monitor handling characteristics
- Call for checklists as needed

**Pilot Monitoring (PM)**:
- Monitor FCS_NN status on ECAM
- Call out any degradations or failures
- Execute checklists
- Coordinate with ATC/Dispatch as needed

---

## 9. Special Procedures

### 9.1 Cold Weather / Icing

**Considerations**:
- FCS_NN adapts automatically to icing conditions
- Envelope margins automatically reduced (more conservative)
- Expect "FCS NN ICING ADAPT" (cyan) on EICAS

**Crew Actions**:
- Standard de-icing/anti-icing procedures
- No special FCS_NN actions required
- Monitor handling (may feel slightly different)

### 9.2 Severe Turbulence

**Considerations**:
- GLA should be active (if not, consider enabling)
- Expect 30% reduction in load factor variations

**Crew Actions**:
- Standard severe turbulence procedures (speed, seatbelts, etc.)
- GLA will activate automatically
- If uncomfortable, GLA can be disabled (expect harder ride)

### 9.3 One Engine Inoperative (OEI)

**Considerations**:
- FCS_NN automatically compensates for asymmetric thrust
- Reduced rudder input required from crew
- V_MC protection active (envelope protection)

**Crew Actions**:
- Standard OEI procedures
- Observe reduced pilot workload (NN handling most yaw compensation)

---

## 10. Limitations

### 10.1 Operational Limitations

- **Minimum Crew**: 2 pilots (FCS_NN monitoring required)
- **Turbulence**: No limit (GLA may be disabled by crew)
- **Icing**: Standard limits apply (FCS_NN adapts automatically)
- **Crosswind**: Standard limits apply (NN assists with correction)
- **CAT II/III**: Full capability (FCS_NN supports autoland)

### 10.2 MEL Dispatch Restrictions

See **95-20-27-010 Section 3.3** for complete MEL considerations.

---

## 11. Training

### 11.1 Initial Operating Experience (IOE)

**Recommended IOE**:
- 10 sectors with training captain
- Focus on FCS_NN monitoring and degradation scenarios
- Practice abnormal procedures (simulated failures)

### 11.2 Recurrent Training

**Annual Simulator**:
- FCS_NN degradation scenario
- FCS_NN failure → Direct Law
- Envelope protection demonstration

---

## 12. Appendices

### Appendix A: FCS_NN Status Codes

| Code | Meaning | Action |
|------|---------|--------|
| NN-001 | Aero Predictor Degraded | Monitor, continue |
| NN-002 | Control Optimizer Degraded | Monitor, consider diversion |
| NN-003 | GLA Degraded | Avoid severe turbulence |
| NN-004 | Envelope Protection Degraded | Increased monitoring, conservative handling |
| NN-005 | Flight Path Stab Degraded | Manual flying, monitor autopilot |
| NN-099 | Complete FCS_NN Failure | Direct Law, land ASAP |

### Appendix B: ECAM FCS_NN Page Layout

```
┌─────────────────────────────────────┐
│         FCS NN STATUS               │
├─────────────────────────────────────┤
│  Mode: NORMAL LAW             [GRN] │
│                                     │
│  Models:                            │
│    Aero Predictor        98% [GRN]  │
│    Control Optimizer     97% [GRN]  │
│    Gust Load Allev       99% [GRN]  │
│    Envelope Protect     100% [GRN]  │
│    Flight Path Stab      96% [GRN]  │
│    Trim Optimizer        95% [GRN]  │
│                                     │
│  IMA Partition: P1-P6   [ALL RUN]   │
│  CPU: 45%   MEM: 52/68 MB           │
│                                     │
│  Performance:                       │
│    Fuel Savings: -2.8%              │
│    Load Reduction: 32%              │
│    Latency: 6.2ms avg               │
└─────────────────────────────────────┘
```

### Appendix C: Quick Reference Checklist

**Pre-Flight**:
- [ ] FCS_NN MASTER: ON
- [ ] EICAS: "FCS NN READY"
- [ ] Execute FCS BIT
- [ ] ECAM FCS page: All GREEN

**In-Flight Monitoring** (PM):
- [ ] Health scores >95% (green)
- [ ] Fuel savings 2-3% (typical)
- [ ] No cautions/warnings

**FCS_NN Degraded**:
1. MASTER CAUTION: Acknowledge
2. ECAM: Review
3. Continue or Divert: Assess
4. Logbook: Enter

**FCS_NN Failed**:
1. MASTER WARNING: Acknowledge
2. DIRECT LAW: Confirm
3. Handling: Assess (hand-fly if AP on)
4. DIVERT: Consider
5. LAND ASAP: Nearest suitable

---

## Document Control

- **Owner**: AMPEL360 Flight Operations
- **Version**: 1.0
- **Status**: Active
- **Classification**: Flight Operations Manual
- **Last Updated**: 2025-11-17

---

**END OF OPERATIONS MANUAL**
