# Operational Safety Procedures for Neural Network Systems

**Document ID:** AMPEL360-95-00-00-SAF-OPS  
**Version:** 1.0  
**Date:** 2025-11-04  
**Classification:** Safety Critical

---

## 1. PREFLIGHT PROCEDURES

### 1.1 NN Systems Status Check

**Procedure**:
1. Access NN SYSTEMS status page on MFD
2. Verify all required NN systems show "AVAILABLE"
3. Review confidence levels (should be >95% at startup)
4. Check for any MEL items affecting NN systems
5. Note any cautions or advisories

**Acceptance Criteria**:
- All DAL A/B systems available (no MEL relief)
- DAL C systems: May dispatch per MEL with specific limitations
- No red warnings on NN status page

**If Unacceptable**:
- Consult MEL for dispatch eligibility
- If MEL not applicable: Contact maintenance
- Do not dispatch if DAL A/B system unavailable

### 1.2 Operational Design Domain (ODD) Review

**Procedure**:
1. Review planned route, weather, and aircraft configuration
2. Verify all within certified ODD for NN systems
3. Note any areas where ODD boundaries may be approached
4. Brief crew on expected NN system availability

**ODD Boundaries to Check**:
- Weather: Visibility, ceiling, icing, turbulence
- Aircraft: Weight, CG, configuration
- Route: Terrain, airports, airspace
- Systems: Expected failures or degraded modes

**If Near ODD Boundary**:
- Plan for NN degradation or unavailability
- Review conventional system procedures
- Increase crew monitoring

### 1.3 NN Systems Briefing

**Crew Brief Items**:
- Which NN systems will be active
- Expected NN behavior for planned flight
- Any limitations or cautions
- Degradation scenarios and crew response
- Override procedures if needed

---

## 2. IN-FLIGHT PROCEDURES

### 2.1 NN Systems Monitoring

**Continuous Monitoring**:
- Periodic scan of NN status indicators (every 5-10 minutes)
- Check confidence levels remain high (>95%)
- Verify NN actions make sense given situation
- Note any unusual behavior

**Status Indicators**:
- Green: "ACTIVE" - NN operating nominally
- Amber: "DEGRADED" - NN performance reduced
- White: "ADVISORY" - NN suggestions only, crew decides
- Gray: "OFF" - NN disabled

**If Status Changes**:
- Review synoptic page for details
- Assess impact on flight operations
- Follow abnormal procedures if needed

### 2.2 NN Decision Support

**When NN Suggests Action**:
1. **Understand**: What is NN recommending and why?
2. **Evaluate**: Does it make sense given situation?
3. **Verify**: Check confidence level and ODD status
4. **Decide**: Accept, modify, or reject recommendation
5. **Act**: Implement decision
6. **Monitor**: Observe result

**Decision Criteria**:
- **Accept** if: High confidence (>99%), makes sense, in ODD
- **Modify** if: Moderate confidence, generally makes sense, minor adjustment needed
- **Reject** if: Low confidence, doesn't make sense, out of ODD, or crew disagrees

**Example - Collision Avoidance NN**:
```
NN recommends: "DESCEND 1000 FT"
Confidence: 98.5%
Reason: "Traffic conflict in 30 seconds"

Crew evaluation:
- Check TCAS: Confirms traffic conflict
- Assess situation: Descent makes sense
- Verify altitude: Clear below
Decision: ACCEPT and execute descent
```

### 2.3 Approaching ODD Boundaries

**Warning Signs**:
- ODD status changes from "IN" to "NEAR EDGE"
- Confidence levels decrease
- NN status downgrades to "DEGRADED"
- Unusual NN behavior

**Crew Actions**:
1. Identify which ODD boundary being approached
2. Assess if can remain in ODD:
   - Can route around?
   - Can change altitude?
   - Can adjust aircraft configuration?
3. If staying in ODD: Continue monitoring
4. If exiting ODD: Prepare for NN degradation
   - Review conventional procedures
   - Brief expected changes
   - Increase monitoring

**Example - Weather ODD Boundary**:
```
Approaching thunderstorm (severe turbulence)
- Weather outside NN training data (ODD boundary)
- NN status: "NEAR ODD EDGE"
- Confidence decreasing: 97% → 95% → 92%

Crew actions:
- Review flight control NN limitations
- Prepare for degradation to conventional control
- Brief expected handling changes
- Consider routing around weather
```

---

## 3. ABNORMAL PROCEDURES

### 3.1 NN Performance Degradation

**Indications**:
- NN status: "DEGRADED"
- EICAS message: "NN PERFORMANCE DEGRADED"
- Confidence levels decreasing
- Increased monitor disagreements

**Immediate Actions**:
1. NOTE degradation level (90%, 70%, 50%)
2. VERIFY aircraft control maintained
3. ASSESS impact on flight operations

**Analysis**:
- Review synoptic page: What caused degradation?
- Check ODD status: Are we in ODD?
- Review confidence: Trending up or down?

**Crew Decisions**:
- **If 90% (Level 4)**:
  - Continue operations
  - Increase monitoring
  - Log event

- **If 70% (Level 3)** - NN Advisory Only:
  - Use NN as advisory input only
  - Crew makes all decisions
  - Consider diversion if prolonged
  - Notify ATC/company if needed

- **If 50% (Level 2)** - Conventional Mode:
  - NN disabled, using conventional systems
  - Review conventional procedures
  - Consider MEL implications
  - Likely diversion required

**Post-Flight**:
- Debrief degradation event
- Complete maintenance log entry
- Provide input to safety reporting system

### 3.2 NN Unexpected Behavior

**Indications**:
- NN action not expected
- NN disagrees with crew assessment
- Safety monitor alert
- EICAS caution: "NN OUTPUT UNUSUAL"

**Immediate Actions**:
1. **OVERRIDE** NN if safety concern
   - Announce "OVERRIDING NN" to crew
   - Use override switch/procedure
   - Assume manual control
2. **ASSESS** situation
   - What did NN do that was unexpected?
   - What should NN have done?
   - Is aircraft in safe state?

**Analysis**:
- Review NN explanation (if available)
- Check confidence level
- Verify ODD status
- Consider if this is within NN capabilities

**Crew Decisions**:
- **If clear error**: Keep NN overridden, complete flight conventionally
- **If unclear**: Consult with company/ATC, may cautiously re-engage if safe
- **If NN correct, crew misunderstood**: Re-engage, but increase monitoring

**Examples**:
```
Example 1: NN commands unexpected power change
- Override immediately
- Assess: Power already appropriate
- Decision: NN error, keep overridden
- Log event

Example 2: NN suggests unusual routing
- Override (don't follow routing)
- Check explanation: "Avoid weather ahead" 
- Verify: Weather radar confirms
- Decision: NN was correct, accept routing
- Learn from event
```

**Post-Flight**:
- Required: Report unexpected behavior
- Maintenance log entry
- Detailed description for investigation
- Preserve FDR data if requested

### 3.3 NN / Safety Monitor Disagreement

**Indications**:
- EICAS caution: "NN MONITOR DISAGREE"
- Amber alert on NN status page
- Flashing status indicator

**Immediate Actions**:
1. VERIFY aircraft control maintained
2. NOTE which system (flight control, navigation, etc.)
3. ASSESS disagreement severity

**Analysis**:
- Review synoptic page: What do NN and monitor outputs show?
- Which is more reasonable given situation?
- Is this transient or persistent?

**Crew Decisions**:
- **Transient disagreement** (<3 seconds):
  - Monitor, may resolve automatically
  - If persistent, follow persistent procedure

- **Persistent disagreement** (>3 seconds):
  - System likely degrading to conventional
  - Crew verifies conventional mode engaged
  - Continue flight with conventional system

- **Severe disagreement** (large difference):
  - System automatically reverts to conventional
  - Crew confirms mode
  - Assess need for diversion

**Post-Flight**:
- Maintenance log entry required
- Data download for analysis

---

## 4. EMERGENCY PROCEDURES

### 4.1 NN System Failure

**Memory Items**:
```
NN SYSTEM FAILURE:
1. NN DISCONNECT ............. PUSH (as required)
2. CONVENTIONAL MODE .......... VERIFY ENGAGED
3. MANUAL CONTROL ............. ASSUME (if needed)
```

**Expanded Procedure**:

1. **Recognize Failure**:
   - EICAS warning: "NN SYSTEM FAILED"
   - Red status indicator
   - Loss of NN functionality

2. **Immediate Actions** (Memory Items above)

3. **Assess Aircraft State**:
   - Attitude, airspeed, altitude OK?
   - Conventional systems operating?
   - Other systems affected?

4. **Complete Checklist**:
   - Follow QRH procedure for specific NN system
   - Verify all required systems available
   - Assess MEL implications

5. **Crew Coordination**:
   - PM monitors aircraft while PF handles failure
   - Clear communication
   - Workload management

6. **Operational Decisions**:
   - Can continue to destination?
   - Diversion needed?
   - ATC notification
   - Company notification

**Specific Systems**:

**Flight Control NN Failure**:
- Immediate reversion to conventional control
- Handling may be different (likely heavier)
- Continue flight with conventional control
- May affect dispatch for next flight (check MEL)

**Collision Avoidance NN Failure**:
- TCAS remains available
- ADS-B and radar available
- Visual separation
- May require increased ATC services

**Propulsion NN Failure**:
- Conventional fuel cell control
- May be less efficient
- Monitor fuel closely
- Diversion if insufficient fuel

### 4.2 Multiple NN System Failures

**Indications**:
- Multiple EICAS warnings
- Multiple NN systems showing "FAILED"
- Possibly indicates common cause

**Immediate Actions**:
1. AVIATE: Maintain aircraft control
2. NAVIGATE: Assess position and routing
3. COMMUNICATE: Declare emergency if needed

**Analysis**:
- Is this NN-specific issue or broader electrical/computer problem?
- Are conventional systems still available?
- What caused multiple failures?

**Crew Actions**:
- Treat as serious abnormal situation
- Consider declaring emergency
- Plan for immediate diversion
- Use all available conventional systems
- Request ATC assistance

**Caution**: Multiple NN failures may indicate power, cooling, or computer system problem affecting more than just NNs.

### 4.3 NN In Emergency Situations

**Philosophy**: In emergencies, crew workload prioritized over NN optimization

**General Guidance**:
- **If NN helps**: Use it as tool
- **If NN adds workload**: Disable it
- **If uncertain**: Disable it

**Examples**:

**Engine Failure**:
- NN fuel cell optimization may help manage remaining power
- But if crew busy: Disable NN, use proven procedures
- Crew decision based on workload

**Emergency Descent**:
- NN flight control may help optimize descent
- But use conventional control if crew more comfortable
- Speed is priority, not optimization

**Medical Emergency**:
- NN route optimization may help find nearest airport
- But if crew task-saturated: Use basic procedures
- NN can be distraction in time-critical situation

**Principle**: No time to debug NN issues in emergency. If NN working and helpful, use it. If any doubt, revert to proven conventional procedures.

---

## 5. CREW RESOURCE MANAGEMENT

### 5.1 Crew Coordination

**Division of Duties**:
- **Pilot Flying (PF)**:
  - Controls aircraft
  - Makes NN override decisions
  - Announces NN interactions

- **Pilot Monitoring (PM)**:
  - Monitors NN status
  - Reviews NN suggestions
  - Cross-checks NN actions
  - Manages NN synoptic page

**Communication**:
- PF announces: "ACCEPTING NN RECOMMENDATION" or "OVERRIDING NN"
- PM verifies: "NN STATUS NOMINAL" or "NN DEGRADING"
- Clear callouts for mode changes

**Example**:
```
PM: "NN recommends right turn 10 degrees, traffic avoidance"
PF: "Traffic in sight, NN recommendation reasonable"
PM: "Confidence 99%, TCAS agrees"
PF: "Accepting NN, turning right"
PM: "NN turn complete, status nominal"
```

### 5.2 Automation Management

**Appropriate Use of NN**:
- Use NN when it enhances safety and efficiency
- Don't use NN just because it's available
- Consider crew workload and situational awareness

**Staying in the Loop**:
- Even with NN active, crew monitors aircraft state
- Periodic manual operations to maintain proficiency
- Regular checks that NN actions make sense

**Trust But Verify**:
- Trust NN within its proven ODD
- But always verify critical decisions
- Don't blindly follow NN outside ODD or in novel situations

### 5.3 Decision Authority

**Principle**: Crew has final authority over all NN systems

**Crew Responsibilities**:
- Understand NN capabilities and limitations
- Monitor NN operations
- Override NN when appropriate
- Make final decisions on NN recommendations

**Company Support**:
- Dispatch provides NN status for route
- Maintenance ensures NN systems serviceable
- Training ensures crew competency

**Regulatory Compliance**:
- Crew retains authority per regulations
- NN is assistive technology, not replacement for crew judgment

---

## 6. REPORTING REQUIREMENTS

### 6.1 Mandatory Reports

**Report Required for**:
- Any NN failure (all DAL levels)
- NN unexpected behavior
- Safety monitor activation
- Crew override of NN for safety reasons
- NN performance degradation to Level 2 or worse
- Multiple OOD detections in single flight
- NN contribution to incident or accident

**Reporting Channels**:
1. Maintenance log entry (all events)
2. Company safety reporting system
3. Regulatory authority (serious events)
4. Confidential reporting (if desired)

### 6.2 Report Contents

**Minimum Information**:
- Flight details (flight number, date, aircraft)
- NN system(s) involved
- Event description
- Crew actions taken
- Outcome
- Crew assessment of severity

**Encouraged Additional Information**:
- NN status at time (confidence, ODD, etc.)
- Environmental conditions
- FDR data download (if available)
- Crew suggestions for improvement

### 6.3 Feedback Loop

**Company Responsibilities**:
- Acknowledge all reports within 48 hours
- Investigate reports within 30 days
- Provide feedback to reporting crew
- Implement corrective actions as needed
- Share lessons learned with fleet

**Crew Benefits**:
- Non-punitive reporting culture
- Continuous improvement of NN systems
- Recognition for safety contribution
- Enhanced training based on real-world experience

---

**Document Control**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-04 | AMPEL360 Safety Team | Initial release |

**Classification**: Safety Critical  
**Next Review**: 2025-02-04 (Quarterly)
