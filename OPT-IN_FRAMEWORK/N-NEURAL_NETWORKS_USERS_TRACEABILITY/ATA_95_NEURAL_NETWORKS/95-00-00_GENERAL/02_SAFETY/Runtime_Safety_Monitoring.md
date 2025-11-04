# Runtime Safety Monitoring for Neural Network Systems

**Document ID:** AMPEL360-95-00-00-SAF-RSM  
**Version:** 1.0  
**Date:** 2025-11-04  
**Classification:** Safety Critical

---

## 1. INTRODUCTION

### 1.1 Purpose

This document specifies the runtime safety monitoring architecture for neural network systems in the AMPEL360 aircraft. Runtime monitoring provides continuous validation that NNs operate safely during flight.

### 1.2 Safety Objectives

- Detect NN failures before they impact aircraft safety
- Enable graceful degradation from NN to conventional systems
- Provide early warning of NN performance degradation
- Log data for post-flight analysis and continuous improvement

### 1.3 Scope

Applies to all DAL A, B, and C neural network systems.

### 1.4 Related Documents

- [Safety_Framework_Overview.md](Safety_Framework_Overview.md)
- [Common_Cause_Analysis.md](Common_Cause_Analysis.md)
- [Fault_Tree_Analysis.md](Fault_Tree_Analysis.md)
- [Safety_Requirements.csv](Safety_Requirements.csv)
- [Human_Factors_Safety.md](Human_Factors_Safety.md)
- [ARP4761](https://www.sae.org/standards/content/arp4761/) - Safety Assessment Process
- [DO-178C](https://www.rtca.org/content/standards-guidance-materials) - Software Considerations

---

## 2. SAFETY MONITOR ARCHITECTURE

### 2.1 Three-Layer Monitoring

```
┌─────────────────────────────────────────────────────┐
│         Layer 3: System-Level Monitor               │
│  (Aircraft state envelope, mission safety)          │
└─────────────────────────────────────────────────────┘
                        ↑
┌─────────────────────────────────────────────────────┐
│         Layer 2: Independent Safety Monitor         │
│  (Conventional algorithm checks NN outputs)         │
└─────────────────────────────────────────────────────┘
                        ↑
┌─────────────────────────────────────────────────────┐
│         Layer 1: NN Self-Monitoring                 │
│  (Confidence, OOD detection, internal checks)       │
└─────────────────────────────────────────────────────┘
                        ↑
              ┌─────────────────┐
              │   Neural Network│
              └─────────────────┘
```

### 2.2 Layer 1: NN Self-Monitoring

**Monitors embedded within or alongside the NN**

#### 2.2.1 Confidence Monitoring

**Purpose**: Detect when NN is uncertain about prediction

**Implementation**:
- Output layer includes confidence/uncertainty estimate
- Methods: softmax probabilities, Bayesian NN, dropout at inference, ensemble variance

**Thresholds**:
- DAL A: Confidence > 99.9% required
- DAL B: Confidence > 99% required
- DAL C: Confidence > 95% required

**Action on Low Confidence**:
1. Flag prediction as uncertain
2. Trigger Layer 2 independent check
3. Log event
4. If persistent, reduce NN authority or fallback

**Implementation Example** (Classification NN):
```python
# Softmax output with confidence
prediction, confidence = nn_model(input)
if confidence < threshold:
    trigger_layer2_check()
    log_low_confidence_event()
    if confidence < fallback_threshold:
        switch_to_conventional()
```

#### 2.2.2 OOD (Out-of-Distribution) Detection

**Purpose**: Detect inputs outside training distribution

**Methods**:

1. **Statistical Distance**:
   - Compute Mahalanobis distance of input from training distribution
   - Flag if distance > threshold

2. **Autoencoder Reconstruction**:
   - Train autoencoder on training inputs
   - Large reconstruction error → OOD

3. **Ensemble Disagreement**:
   - Multiple NN variants
   - High disagreement → OOD

**Thresholds**:
- Calibrated to flag <1% of nominal operations as OOD
- Stress tested to catch >99% of true OOD inputs

**Action on OOD Detection**:
1. Alert crew (amber caution)
2. Reduce NN authority (advisory mode)
3. If far OOD, switch to conventional system
4. Log input for analysis

#### 2.2.3 Temporal Consistency Checking

**Purpose**: Detect sudden unrealistic changes in NN output

**Implementation**:
- Track NN outputs over time
- Flag if change exceeds physical plausibility

**Example** (Flight Control):
```python
# Check for unrealistic rate of change
if abs(nn_output - prev_output) / dt > max_rate_of_change:
    flag_inconsistency()
    rate_limit_output()
```

**Thresholds**:
- Based on aircraft dynamics limits
- Tuned to avoid false alarms on legitimate rapid maneuvers

#### 2.2.4 Input Validation

**Purpose**: Reject clearly invalid inputs before NN processing

**Checks**:
- Range checks (min/max)
- Physical plausibility (e.g., airspeed, altitude)
- Sensor health flags
- Redundancy cross-checks

**Action on Invalid Input**:
- Reject input
- Use last valid input (with timeout)
- Or fallback to conventional

### 2.3 Layer 2: Independent Safety Monitor

**Purpose**: Provide independent verification of NN outputs using conventional algorithms

**Key Requirement**: INDEPENDENCE
- Different hardware (separate processor)
- Different algorithm (not NN-based)
- Different development team
- No shared software libraries
- Independent power source (if DAL A)

#### 2.3.1 Architecture

```
┌──────────────────┐       ┌──────────────────┐
│  Neural Network  │       │ Safety Monitor   │
│  (GPU)           │       │ (CPU - separate) │
└──────────────────┘       └──────────────────┘
        ↓                           ↓
   NN Output                  Monitor Output
        ↓                           ↓
        └────────→ Comparator ←─────┘
                       ↓
            Pass: Use NN output
            Fail: Switch to monitor output
                  Alert crew
                  Log event
```

#### 2.3.2 Safety Monitor Functions

**For Flight Control NN**:
- Envelope protection (α, β, load factor limits)
- Rate limits (pitch, roll, yaw rates)
- Control surface position limits
- Stability margins

**Implementation**: Conventional control laws with proven history

**For Collision Avoidance NN**:
- Simple distance/closure rate calculation
- Conservative miss distance thresholds
- Backup TCAS/radar logic

**For Propulsion NN**:
- Fuel cell parameter limits (temperature, pressure, voltage)
- Flow rate limits
- Power limits

#### 2.3.3 Comparison Logic

**Methods**:

1. **Range Check**: NN output within safe bounds?
   ```
   if min_safe <= nn_output <= max_safe:
       use_nn_output()
   else:
       switch_to_monitor()
   ```

2. **Reasonableness**: NN output makes sense given inputs?
   ```
   expected_range = monitor_predict_range(inputs)
   if nn_output in expected_range:
       use_nn_output()
   else:
       investigate()
   ```

3. **Agreement**: NN and monitor outputs similar?
   ```
   if abs(nn_output - monitor_output) < tolerance:
       use_nn_output()  # NN more optimal
   else:
       use_monitor_output()  # Safety first
   ```

**Tolerance Selection**:
- Tight enough to catch errors
- Loose enough to avoid false alarms
- Tuned based on NN and monitor uncertainties

#### 2.3.4 False Alarm Management

**Challenge**: Too sensitive → nuisance, too permissive → unsafe

**Strategy**:
- Initial: Conservative thresholds
- Tuning: Operational data to reduce false alarms
- Persistence: Require N consecutive or M of N violations
- Severity grading: Warning → Caution → Alert → Fallback

**Example**:
```python
# Multi-level response
disagreement_count = 0
for each cycle:
    if nn_disagrees_with_monitor():
        disagreement_count += 1
        if disagreement_count == 3:
            crew_warning()  # Yellow
        if disagreement_count == 10:
            crew_caution()  # Amber
            reduce_nn_authority()
        if disagreement_count == 30:
            crew_alert()  # Red
            switch_to_conventional()
    else:
        disagreement_count = max(0, disagreement_count - 1)
```

### 2.4 Layer 3: System-Level Monitoring

**Purpose**: Monitor overall aircraft safety regardless of NN performance

**Monitors**:

1. **Envelope Protection**: Aircraft within safe flight envelope
2. **Energy Management**: Sufficient fuel/power for mission
3. **Terrain/Obstacle**: Safe separation maintained
4. **Traffic Separation**: Collision avoidance maintained
5. **System Health**: All critical systems operating

**Action**: Override any NN if system-level safety threatened

---

## 3. ANOMALY DETECTION

### 3.1 Statistical Process Control

**Purpose**: Detect gradual NN performance degradation

**Method**:
- Track NN performance metrics over time
- Establish control limits (mean ± 3σ)
- Flag when metrics exceed control limits

**Metrics**:
- Accuracy (on validation set replayed in-flight)
- Confidence levels
- OOD detection rate
- Disagreement with safety monitor

**Example**:
```
Mean confidence: 99.5%, Std: 0.5%
Control limits: [98.0%, 100%]
If average confidence over 100 cycles < 98.0%:
    flag_degradation()
```

**Action**:
- Immediate: Log event, alert maintenance
- Persistent: Ground aircraft, retrain/update NN

### 3.2 Drift Detection

**Purpose**: Detect concept drift (world changing from training assumptions)

**Methods**:

1. **Performance Trending**: Track accuracy over time
   - Moving average
   - Detect downward trend

2. **Input Distribution Shift**: Monitor input statistics
   - Compare to training distribution (KL divergence, MMD)
   - Significant shift → potential concept drift

3. **Prediction Distribution Shift**: Monitor output statistics
   - Sudden change in output distribution → investigate

**Thresholds**:
- Performance drop > 5% → Warning
- Performance drop > 10% → Mandatory update
- Input distribution shift > 2σ → Warning

### 3.3 Adversarial Attack Detection

**Purpose**: Detect deliberately malicious inputs

**Methods**:

1. **Input Anomaly**: Input very different from training data
   - Use OOD detector

2. **Prediction Anomaly**: Prediction unexpected given input
   - Inconsistent with physics/common sense

3. **Ensemble Disagreement**: Adversarial inputs affect models differently
   - High variance across ensemble → suspect

**Action**:
- Reject suspicious input
- Alert crew and cybersecurity
- Log for investigation
- Increase security posture

---

## 4. GRACEFUL DEGRADATION STRATEGY

### 4.1 Degradation Levels

```
Level 5: Full NN Performance (100%)
  ↓ [Minor issue detected]
Level 4: Reduced NN Authority (90%)
  ↓ [Persistent issues]
Level 3: NN Advisory Only (70%)
  ↓ [NN unreliable]
Level 2: Conventional Systems Only (50%)
  ↓ [Conventional system issue]
Level 1: Emergency Mode (30%)
```

### 4.2 Transition Logic

**Degradation Triggers**:
- Level 5→4: Low confidence >1%, OOD >0.5%, monitor disagreement >0.1%
- Level 4→3: Low confidence >5%, OOD >2%, monitor disagreement >1%
- Level 3→2: Low confidence >10%, OOD >5%, monitor disagreement >5%

**Recovery**:
- Automatic if conditions improve for >1 minute
- Crew can inhibit auto-recovery (manual approval required)

**Crew Actions**:
- Level 5→4: Awareness (EICAS message)
- Level 4→3: Consider mission impact
- Level 3→2: Review emergency procedures
- Level 2→1: Declare emergency if needed

### 4.3 Smooth Transitions

**Requirement**: No abrupt changes

**Implementation**:
- Blend NN and conventional outputs during transition
- Gradual authority reduction over 5-10 seconds

**Example**:
```python
# Smooth blending
nn_authority = transition_from_90_to_50_over_10_sec()
output = nn_authority * nn_output + (1 - nn_authority) * conventional_output
```

---

## 5. DATA LOGGING AND ANALYSIS

### 5.1 Flight Data Recorder Integration

**Logged Data** (for all DAL A/B NNs):
- NN inputs (sampled)
- NN outputs
- Confidence levels
- OOD flags
- Safety monitor outputs
- Disagreement flags
- Degradation level
- Timestamps

**Recording Rate**:
- Safety-critical NNs: Every cycle (10-100 Hz)
- Non-critical NNs: Sampled (1 Hz)

**Retention**:
- Last 25 hours in crash-protected FDR
- Full flight downloadable for analysis

### 5.2 Post-Flight Analysis

**Automated Analysis**:
- Flag anomalies for human review
- Generate summary statistics
- Trend analysis over fleet

**Human Review Triggers**:
- Any Level 3 or worse degradation
- Unusual OOD detection rate
- Novel input patterns
- Crew report of NN anomaly

**Feedback Loop**:
1. Identify issue in post-flight data
2. Root cause analysis
3. Retrain NN or adjust thresholds
4. Validate improvement
5. Fleet-wide update

### 5.3 Continuous Learning

**Operational Data Collection**:
- Collect nominal operations data
- Add to training dataset (after validation)
- Periodic model updates

**Safety Gates**:
- New data validated before training
- Updated model extensively tested before deployment
- A/B testing on limited fleet first
- Full deployment only after demonstrated improvement

---

## 6. HARDWARE REQUIREMENTS

### 6.1 Safety Monitor Hardware

**Requirements for DAL A/B**:
- Independent processor (not shared with NN)
- Separate power source (different bus)
- Independent memory
- Separate sensors (where practical)
- Physically separate (no shared chips)

**Acceptable Configurations**:
- NN on GPU, monitor on CPU ✓
- NN on GPU 1, monitor on GPU 2 (different cards) ✓
- NN and monitor on same GPU ✗ (not independent)

### 6.2 Redundancy

**DAL A Systems**:
- Dual redundant NN channels
- Independent safety monitor
- Total: 3 independent computation paths

**DAL B Systems**:
- Single NN channel
- Independent safety monitor
- Total: 2 independent computation paths

### 6.3 Fault Detection

**Built-In Test (BIT)**:
- Startup BIT: Verify hardware before flight
- Continuous BIT: Watchdog timers, memory checks
- Periodic BIT: Self-test every N minutes

**Fault Response**:
- Startup BIT fail: NN not available, use conventional
- Continuous BIT fail: Switch to backup channel/conventional
- Alert crew and maintenance

---

## 7. CREW INTERFACE

### 7.1 Normal Operations Display

**EICAS/Status Page**:
- NN system status: "NN ACTIVE" (green)
- Performance level: "100%" or "DEGRADED 90%"
- No clutter in normal ops

### 7.2 Abnormal Operations Display

**Caution Messages** (Amber):
- "NN DEGRADED" (Level 4→3)
- "NN ADVISORY ONLY" (Level 3→2)

**Warning Messages** (Red):
- "NN UNAVAILABLE" (Level 2)

**Advisory Messages** (White):
- "NN LOW CONFIDENCE" (transient)
- "NN OOD DETECTED" (transient)

### 7.3 Crew Actions

**Override/Disable**:
- Dedicated NN ON/OFF switch (guarded)
- Pull to disable NN, use conventional
- Action time: <2 seconds

**Status Inquiry**:
- Synoptic page with NN details
- Confidence, OOD rate, degradation reason
- Crew can view NN explanation (for trained crew)

---

## 8. TESTING AND VALIDATION

### 8.1 Monitor Effectiveness Testing

**Fault Injection**:
- Inject known NN failures
- Verify safety monitor detects >99%
- Measure detection latency (<100 ms)

**Corner Cases**:
- Test boundary conditions
- Ensure monitor doesn't false trigger

### 8.2 False Alarm Rate

**Target**:
- DAL A: <0.001 per FH
- DAL B: <0.01 per FH
- DAL C: <0.1 per FH

**Tuning**:
- Operational data used to adjust thresholds
- Balance safety vs. nuisance

### 8.3 Graceful Degradation Testing

**Test Scenarios**:
- Gradual NN degradation
- Sudden NN failure
- Oscillating NN performance

**Verify**:
- Smooth transitions
- Crew situational awareness
- Functionality maintained at each level

---

**Document Control**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-04 | AMPEL360 Safety Team | Initial release |

**Classification**: Safety Critical  
**Next Review**: 2025-02-04 (Quarterly)
