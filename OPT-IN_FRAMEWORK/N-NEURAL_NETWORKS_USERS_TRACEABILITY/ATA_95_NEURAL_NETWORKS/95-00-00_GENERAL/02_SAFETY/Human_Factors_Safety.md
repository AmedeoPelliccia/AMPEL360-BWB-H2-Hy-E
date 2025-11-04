# Human Factors Safety for Neural Network Systems

**Document ID:** AMPEL360-95-00-00-SAF-HF  
**Version:** 1.0  
**Date:** 2025-11-04  
**Classification:** Safety Critical

---

## 1. INTRODUCTION

### 1.1 Purpose

This document addresses human factors considerations for neural network systems in the AMPEL360 aircraft, ensuring safe and effective crew interaction with AI/ML systems.

### 1.2 Key Principles

1. **Human Authority**: Crew maintains ultimate decision-making authority
2. **Transparency**: NN behavior and limitations clearly communicated
3. **Predictability**: NN actions align with crew expectations
4. **Trust Calibration**: Appropriate level of crew trust in NN systems
5. **Workload Management**: NN assists without overwhelming crew

### 1.3 Scope

Covers crew interface design, training, procedures, and operational considerations for all NN systems.

---

## 2. AUTOMATION SURPRISE PREVENTION

### 2.1 Definition

**Automation Surprise**: Unexpected NN behavior that confuses or startles crew, potentially leading to safety hazards.

### 2.2 Root Causes

#### 2.2.1 Mode Confusion

**Problem**: Crew loses track of which NN mode is active

**Examples**:
- Crew thinks NN is controlling, but it's in advisory mode
- NN automatically degrades to lower authority, crew unaware
- Multiple NNs with conflicting modes

**Prevention**:

1. **Clear Mode Indication**:
   - Dedicated NN mode display on primary flight display
   - Color coding: Green (Active), Amber (Degraded), White (Advisory), Off (Gray)
   - Audible annunciation on mode changes

2. **Mode Simplicity**:
   - Limit number of modes (≤5)
   - Clear mode names matching pilot vocabulary
   - Consistent mode logic across NN systems

3. **Mode Stability**:
   - Avoid frequent automatic mode changes
   - Require crew confirmation for non-critical changes
   - Persistent mode (doesn't revert without crew action)

**Example Mode Display**:
```
┌─────────────────────┐
│ NN FLIGHT CONTROL   │
│ [ACTIVE] 100%       │  ← Green
│ Confidence: 99.8%   │
└─────────────────────┘
```

#### 2.2.2 Unexpected NN Action

**Problem**: NN takes action crew didn't anticipate

**Examples**:
- Flight control NN makes abrupt input
- Collision avoidance NN commands evasive maneuver
- Propulsion NN changes power setting

**Prevention**:

1. **Predictable Behavior**:
   - NN actions consistent with training and procedures
   - No "hidden" behaviors not documented
   - Behavior aligns with crew mental model

2. **Timely Alerts**:
   - Warn crew before autonomous action (when time permits)
   - "NN WILL ADJUST POWER IN 5 SECONDS" message
   - Crew can inhibit if inappropriate

3. **Smooth Actions**:
   - No abrupt or jerky movements
   - Rate limits on NN commands
   - Gradual authority changes

**Example Alert Sequence**:
```
T-5s: "NN OPTIMIZING FUEL FLOW" (advisory message)
T-3s: "ADJUSTING IN 3...2...1..." (countdown)
T-0s: NN makes adjustment (smooth transition)
```

#### 2.2.3 Inconsistent Behavior

**Problem**: NN behaves differently in similar situations

**Examples**:
- Same approach, different NN guidance each time
- Non-deterministic behavior confuses crew
- Performance varies day-to-day

**Prevention**:

1. **Deterministic Where Possible**:
   - Fix random seeds in production models
   - Minimize stochastic behavior
   - Consistent preprocessing

2. **Explain Differences**:
   - When behavior changes, explain why
   - "Different wind conditions" explanation
   - Help crew understand reasoning

3. **Bounds on Variability**:
   - Limit range of NN outputs
   - Prevent wild variations
   - Statistical process control

---

## 3. TRUST CALIBRATION

### 3.1 Trust Spectrum

**Overtrust** ← → **Appropriate Trust** ← → **Undertrust**

- **Overtrust**: Crew blindly follows NN, doesn't monitor → Dangerous
- **Undertrust**: Crew ignores NN, doesn't use → Wastes capability
- **Appropriate Trust**: Crew trusts NN within its limitations → Safe & Effective

### 3.2 Transparency for Trust

#### 3.2.1 NN Capabilities and Limitations

**Communication Strategy**:

1. **Training**:
   - Clear documentation of NN capabilities
   - Explicit limitations (ODD, accuracy, failure modes)
   - Scenarios where NN should/shouldn't be trusted

2. **Operational Aids**:
   - Quick reference cards
   - Cockpit placards for critical limitations
   - Electronic checklist integration

3. **Real-Time Indicators**:
   - Confidence display
   - ODD status (In ODD / Near Boundary / Out of ODD)
   - Performance metrics

**Example Limitation Placard**:
```
┌────────────────────────────────────┐
│ NN VISION NAVIGATION               │
│ LIMITATIONS:                       │
│ • Requires visibility >1 SM        │
│ • Night ops: runway lights req'd   │
│ • Heavy rain/snow: degraded        │
│ • Always cross-check with ILS/GPS  │
└────────────────────────────────────┘
```

#### 3.2.2 Confidence Communication

**Purpose**: Help crew gauge when to trust NN prediction

**Display Elements**:
- Numerical confidence: "99.2%"
- Visual indicator: Progress bar or color
- Historical trend: Confidence over last N cycles

**Interpretation Guidance**:
- >99%: High confidence, likely trustworthy
- 95-99%: Moderate confidence, monitor closely
- <95%: Low confidence, verify independently

**Caveat**: Confidence is calibrated but not perfect. Train crew to use as one factor, not sole decider.

#### 3.2.3 Explainability

**Purpose**: Help crew understand why NN made a decision

**Methods**:

1. **Visual Explanations**:
   - Saliency maps (what NN is "looking at")
   - Attention visualizations
   - Feature importance

2. **Textual Explanations**:
   - "NN recommends LEFT because: closure rate 500 kts, range 2 NM"
   - Natural language generation from NN reasoning

3. **Comparative Explanations**:
   - "NN agrees with TCAS"
   - "NN differs from radar because of visual confirmation"

**Implementation Considerations**:
- Explanations in pilot terminology, not technical jargon
- Concise (1-2 sentences)
- Available on demand (not cluttering display)

**Example Explanation Interface**:
```
Pilot presses "WHY?" button

┌────────────────────────────────────┐
│ NN RECOMMENDED GO-AROUND BECAUSE:  │
│ • Wind shear detected ahead        │
│ • Approach rate above threshold    │
│ • Confidence: 98.5%                │
└────────────────────────────────────┘
```

### 3.3 Building Appropriate Trust

**Training Strategy**:

1. **Simulator Experience**:
   - Expose pilots to NN in safe environment
   - Nominal scenarios (NN works well)
   - Failure scenarios (NN degrades, crew takes over)
   - Build calibrated mental model

2. **Graduated Deployment**:
   - Start with advisory mode (NN suggests, crew decides)
   - Progress to assisted mode (NN acts, crew monitors)
   - Full autonomous only after trust established

3. **Feedback Loops**:
   - Show crew when NN was correct
   - Show when NN was wrong (learning moments)
   - Discuss edge cases and limitations

**Operational Experience**:
- Regular crew feedback surveys
- Adjust NN behavior based on crew input
- Continuous trust calibration

---

## 4. CREW WORKLOAD MANAGEMENT

### 4.1 NN as Workload Reducer

**Objectives**:
- Automate routine tasks → Free crew for high-level decisions
- Handle high-rate tasks → Crew focuses on strategy
- Monitor systems → Alert crew to issues

**Examples**:
- NN optimizes fuel cell parameters → Crew monitors
- NN tracks traffic → Crew makes decisions
- NN diagnoses faults → Crew takes corrective action

### 4.2 Avoiding Workload Increase

**Anti-Patterns**:

1. **Alert Overload**:
   - Too many NN alerts/messages
   - Crew spends time dismissing nuisance alerts
   - Critical alerts lost in noise

   **Solution**:
   - Rigorous alert filtering
   - Prioritization (only safety-critical alerts interrupt)
   - Consolidation of related alerts

2. **Complexity Increase**:
   - NN adds new procedures
   - Crew must learn new modes/interfaces
   - Mental workload increases

   **Solution**:
   - Simplify NN interface
   - Align with existing procedures
   - Minimize new crew actions

3. **Monitoring Burden**:
   - Crew must constantly monitor NN
   - Defeats purpose of automation
   - "Clumsy automation"

   **Solution**:
   - Reliable NN → Crew can trust to operate autonomously
   - Safety monitors alert crew to issues
   - Out-of-the-loop management (see below)

### 4.3 Out-of-the-Loop Problem

**Challenge**: When NN operates autonomously, crew situational awareness degrades

**Manifestation**:
- Crew doesn't notice NN failure immediately
- Crew slow to resume manual control
- Crew makes errors when taking over

**Solutions**:

1. **Keep Crew in the Loop**:
   - Periodic manual operations (every N flights)
   - Crew practices takeover in simulator
   - Active monitoring tasks

2. **Status Awareness**:
   - Display key parameters even when NN controls
   - Crew scans instruments, maintains SA
   - Clear indication of NN actions

3. **Rapid Takeover**:
   - One-button disconnect
   - Aircraft remains controllable during transition
   - Clear mode indication after takeover

---

## 5. CREW INTERFACE DESIGN

### 5.1 Display Requirements

#### 5.1.1 Primary Flight Display Integration

**NN Status Line** (top of PFD):
```
NN: FLT CTRL ACTIVE | NAV ADVISORY | PROP ACTIVE
```

**Benefits**:
- Always visible
- Minimal clutter
- Quick scan

#### 5.1.2 Multifunction Display Page

**Detailed NN Status** (synoptic page):
```
┌────────────────────────────────────────┐
│ NEURAL NETWORK SYSTEMS STATUS          │
├────────────────────────────────────────┤
│ Flight Control NN    [ACTIVE] 100%     │
│   Confidence: 99.8%  ODD: IN           │
│                                        │
│ Collision Avoid NN   [ACTIVE] 100%     │
│   Confidence: 98.2%  ODD: IN           │
│   Traffic: 3 aircraft                  │
│                                        │
│ Fuel Cell Opt NN     [ADVISORY] 90%    │
│   Confidence: 96.5%  ODD: NEAR EDGE    │
│   Power: 85% of optimum                │
│                                        │
│ [MORE] [EXPLAIN] [RESET] [DISABLE ALL] │
└────────────────────────────────────────┘
```

#### 5.1.3 Alert Messages

**Message Prioritization**:

1. **Warning (Red)**: NN failure, immediate action required
   - "NN FLIGHT CONTROL FAILED - REVERT TO MANUAL"

2. **Caution (Amber)**: NN degraded, monitor closely
   - "NN DEGRADED - VERIFY NAVIGATION"

3. **Advisory (White)**: NN status information
   - "NN LOW CONFIDENCE - APPROACHING ODD EDGE"

**Message Requirements**:
- Clear and concise
- Actionable (what should crew do?)
- Non-technical language
- Consistent format

### 5.2 Control Requirements

#### 5.2.1 NN Engage/Disengage

**Physical Controls**:
- Guarded switch: NN ON / OFF
- Must be deliberate action (prevent inadvertent disable)
- Accessible from both seats
- Clear tactile feedback

**Software Controls**:
- Touch screen options for non-critical NNs
- Confirmation required for safety-critical NNs

#### 5.2.2 Override Capability

**Requirement**: Crew can override any NN output

**Implementations**:

1. **Direct Override** (Flight Control):
   - Crew control input immediately takes priority
   - Threshold: >5 lbs force on yoke/rudder
   - NN authority reduced or disabled

2. **Button Override** (Automation):
   - "OVERRIDE" button
   - NN output ignored, manual or conventional used
   - Latching (remains overridden until reset)

3. **Procedure Override** (Non-critical):
   - Crew follows procedure to disable NN
   - Less time-critical systems

**Timing**: Override activation <2 seconds

### 5.3 Feedback Requirements

**Crew Actions Acknowledged**:
- Tactile (button press feels positive)
- Visual (mode change displayed)
- Audible (tone or voice)

**NN Actions Announced**:
- Before action (when time permits)
- During action (status update)
- After action (result confirmation)

---

## 6. TRAINING REQUIREMENTS

### 6.1 Ground School

**Topics**:

1. **NN Fundamentals** (1 hour):
   - What is a neural network (high-level)
   - How it works (conceptually, not mathematically)
   - Why used (benefits over conventional)
   - Limitations (what it can't do)

2. **AMPEL360 NN Systems** (2 hours):
   - Each NN system: purpose, capabilities, limitations
   - ODD for each system
   - Failure modes and crew responses
   - Degradation scenarios

3. **Crew Interface** (1 hour):
   - Display elements and interpretation
   - Control procedures
   - Alert responses
   - Explainability features

4. **Regulatory and Safety** (1 hour):
   - Certification basis
   - Safety philosophy
   - Human factors considerations
   - Reporting requirements

### 6.2 Simulator Training

**Scenarios**:

1. **Nominal Operations** (2 hours):
   - Normal flight with NN systems active
   - Crew monitors, NN performs as expected
   - Build trust and familiarity

2. **Degraded NN Performance** (1 hour):
   - NN confidence drops
   - OOD conditions encountered
   - Graceful degradation to conventional
   - Crew response and monitoring

3. **NN Failures** (2 hours):
   - Sudden NN failure
   - Crew takes over immediately
   - Erroneous NN output
   - Crew recognizes and overrides

4. **Emergency Scenarios** (2 hours):
   - NN behavior during emergencies
   - When to trust vs. override NN
   - Workload management with NN
   - Automation surprise scenarios

### 6.3 Recurrent Training

**Annual** (4 hours):
- Review of NN systems and procedures
- New failure modes or limitations discovered
- Operational lessons learned
- Simulator scenarios (nominal + failures)

### 6.4 Operational Transition

**Line Training** (10 hours):
- Revenue flights with NN systems under supervision
- Instructor pilot monitors crew NN interaction
- Real-world experience with NN
- Feedback and coaching

---

## 7. PROCEDURES

### 7.1 Normal Procedures

#### 7.1.1 Preflight

**NN Systems Check**:
1. Verify NN systems available (status page)
2. Review NN limitations for planned route/weather
3. Note any NN MEL items
4. Brief crew on NN usage plan

#### 7.1.2 In-Flight

**NN Monitoring**:
- Periodic scan of NN status
- Check confidence levels remain high
- Verify NN actions make sense
- Alert to any unusual behavior

**NN Decision Points**:
- When NN suggests action, evaluate:
  - Does it make sense?
  - What is confidence level?
  - Are we in ODD?
  - Do I trust this NN?
- Decide: Accept, modify, or reject NN suggestion

### 7.2 Abnormal Procedures

#### 7.2.1 NN Degradation

**Procedure**:
1. Note degradation level (EICAS)
2. Review synoptic page (determine cause)
3. If in ODD, continue monitoring
4. If near ODD edge, consider manual control
5. If out of ODD, switch to conventional
6. Log event for maintenance

#### 7.2.2 NN Unexpected Behavior

**Procedure**:
1. OVERRIDE NN immediately (if safety issue)
2. Announce "OVERRIDING NN" to crew
3. Assume manual control
4. Assess situation
5. If safe, re-engage NN
6. If unsafe, complete flight conventionally
7. Report event

#### 7.2.3 NN Disagrees with Crew

**Procedure**:
1. Verify crew understanding correct
2. Check NN confidence and explanation
3. If crew confident: Override NN
4. If uncertain: Request ATC/company advice
5. Document disagreement event
6. Debrief post-flight

### 7.3 Emergency Procedures

**NN in Emergency**:
- Crew workload priority: Aviate, Navigate, Communicate
- NN can assist but crew makes final decisions
- If NN adds workload: DISABLE
- If NN helpful: USE
- No time to debug NN issues in emergency

**Memory Item**:
```
NN ERRONEOUS OUTPUT:
1. NN DISCONNECT ............. PUSH (as required)
2. CONVENTIONAL MODE .......... ENGAGE
3. MANUAL CONTROL ............. ASSUME
```

---

## 8. SAFETY ASSURANCE

### 8.1 Human Factors Testing

**Test Objectives**:
- Verify crew can operate NN systems safely
- Identify usability issues
- Validate training effectiveness
- Ensure no negative transfer to manual operations

**Test Methods**:

1. **Pilot-in-Loop Simulation**:
   - Representative crew (range of experience)
   - Nominal and off-nominal scenarios
   - Workload measurement (NASA-TLX)
   - Situational awareness measurement (SAGAT)

2. **Usability Testing**:
   - Crew interaction with NN interface
   - Time to complete tasks
   - Error rates
   - Subjective satisfaction ratings

3. **Trust Assessment**:
   - Trust in automation questionnaire
   - Behavioral trust (do crew use NN appropriately?)
   - Calibration (trust aligned with NN reliability?)

**Acceptance Criteria**:
- Workload acceptable (NASA-TLX <50)
- SA maintained (SAGAT >70%)
- Error rate <5%
- Trust calibrated (within 10% of actual reliability)
- Subjective ratings >4/5

### 8.2 Crew Feedback

**Operational Feedback Loop**:

1. **Reporting System**:
   - Easy-to-use NN anomaly reporting
   - Confidential (non-punitive)
   - Fast response to reports

2. **Analysis**:
   - Categorize reports (interface, behavior, training, etc.)
   - Identify trends and patterns
   - Prioritize issues

3. **Action**:
   - Fix software issues
   - Update procedures/training
   - Modify interface
   - Communicate changes to fleet

4. **Close Loop**:
   - Inform reporting crew of action taken
   - Broadcast lessons learned

**Metrics**:
- Number of NN-related reports per 1000 flight hours
- Types of issues reported
- Crew satisfaction with NN systems
- NN usage rates (are crews using it?)

### 8.3 Continuous Improvement

**NN Human Factors Review** (Quarterly):
- Review operational data
- Analyze crew feedback
- Identify improvements
- Plan updates

**Human Factors Safety Board Member**:
- Part of Safety Assessment Board
- Advocates for crew perspective
- Reviews NN changes for human factors impact

---

## 9. REGULATORY COMPLIANCE

### 9.1 Human Factors Requirements

**EASA CS-25**:
- CS 25.1302: Installed systems and equipment for use by the flight crew
- CS 25.1523: Minimum flight crew

**FAA**:
- 14 CFR 25.1302: Installed systems and equipment for use by flight crewmembers
- AC 25.1302-1: Design Considerations for Minimizing Crew Errors

**EU AI Act**:
- Human oversight requirements for high-risk AI systems

### 9.2 Certification Evidence

**Documentation**:
- Human factors analysis report
- Pilot-in-loop test report
- Crew training program
- Procedures (normal, abnormal, emergency)

**Demonstrations**:
- Simulator demonstrations to certification authority
- Crew can operate safely
- Override/disconnect effective
- Workload acceptable

---

**Document Control**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-04 | AMPEL360 Safety Team | Initial release |

**Classification**: Safety Critical  
**Next Review**: 2025-02-04 (Quarterly)
