# ATA 95 - Neural Networks Systems
## User Accountability Model

**Document ID:** AMPEL360-95-00-00-OVR-UAM  
**Version:** 1.0  
**Date:** 2025-11-04  
**Classification:** Human Factors and Operations

---

## 1. INTRODUCTION

This document establishes the user accountability framework for neural network systems in the AMPEL360 BWB H2 Hy-E Q100 INTEGRA aircraft, defining human oversight requirements, decision authority, audit trails, and accountability mechanisms to ensure safe and responsible AI/ML system operation.

---

## 2. ACCOUNTABILITY PRINCIPLES

### 2.1 Fundamental Principles

**1. Human Authority Primacy**
> Humans always retain ultimate decision-making authority over neural network recommendations and actions.

**2. Meaningful Human Control**
> Human operators must have sufficient understanding, oversight, and intervention capability to maintain meaningful control.

**3. Transparency and Explainability**
> Neural network decisions must be explainable to users in a manner that supports informed decision-making.

**4. Traceability and Auditability**
> All user interactions with NN systems must be logged and available for review.

**5. Competence and Training**
> Users must be adequately trained and qualified to interact with NN systems.

**6. Shared Responsibility**
> Accountability is distributed across designers, operators, maintainers, and regulators, with clear delineation of responsibilities.

---

## 3. STAKEHOLDER ROLES AND RESPONSIBILITIES

### 3.1 Flight Crew

#### 3.1.1 Pilot in Command (PIC)

**Authority:**
- Ultimate responsibility for aircraft safety
- Final authority over all NN system recommendations
- Can override any NN decision at any time

**Responsibilities:**
- Monitor NN system status and performance
- Understand NN capabilities and limitations
- Intervene when NN operates outside acceptable parameters
- Report anomalies and incidents
- Maintain proficiency through recurrent training

**Decision Rights:**
- Accept or reject NN recommendations
- Select NN operating modes
- Deactivate NN systems (with fallback engagement)
- Declare emergencies and override automation

**Accountability:**
- Responsible for safe operation of aircraft
- Accountable for decisions made (whether following NN or overriding)
- Must document rationale for significant overrides

#### 3.1.2 First Officer / Copilot

**Authority:**
- Shares monitoring responsibility with PIC
- Can alert PIC to NN anomalies
- Can override NN in emergencies (if designated)

**Responsibilities:**
- Cross-check NN outputs
- Monitor NN confidence levels and explanations
- Communicate NN status to PIC
- Execute procedures for NN failures

**Accountability:**
- Shared responsibility for flight safety
- Accountable for monitoring effectiveness

### 3.2 Maintenance Personnel

#### 3.2.1 Line Maintenance Technicians

**Authority:**
- Perform routine NN system checks
- Execute prescribed maintenance tasks
- Clear routine faults

**Responsibilities:**
- Conduct pre-flight and post-flight NN system checks
- Document NN system anomalies
- Replace NN hardware components per manual
- Perform software updates under supervision

**Accountability:**
- Responsible for maintenance task execution
- Accountable for proper documentation
- Must follow approved procedures exactly

#### 3.2.2 Specialized NN Maintenance Engineers

**Authority:**
- Diagnose complex NN system failures
- Approve non-routine repairs
- Perform model updates
- Configure NN system parameters

**Responsibilities:**
- Root cause analysis of NN failures
- Validation of maintenance actions
- Configuration management
- Training of line maintenance personnel

**Accountability:**
- Accountable for diagnostic accuracy
- Responsible for configuration integrity
- Must document all changes in detail

### 3.3 Engineering and Development

#### 3.3.1 NN System Designers

**Responsibilities:**
- Design NN systems meeting safety requirements
- Define operational design domain (ODD)
- Document limitations and failure modes
- Provide explainability mechanisms

**Accountability:**
- Accountable for design adequacy
- Responsible for certification evidence
- Must support continued airworthiness

#### 3.3.2 Data Scientists / ML Engineers

**Responsibilities:**
- Train and validate neural network models
- Ensure dataset quality and representativeness
- Document training procedures
- Monitor model performance in service

**Accountability:**
- Accountable for model quality
- Responsible for bias mitigation
- Must maintain data provenance

### 3.4 Operational Management

#### 3.4.1 Chief Pilot / Director of Operations

**Authority:**
- Approve NN system operational procedures
- Define crew training requirements
- Establish performance monitoring programs

**Responsibilities:**
- Ensure crew competency
- Review NN system performance trends
- Recommend operational limitations
- Liaison with regulatory authorities

**Accountability:**
- Accountable for operational safety
- Responsible for crew readiness

#### 3.4.2 Safety Manager

**Authority:**
- Investigate NN-related incidents
- Recommend safety improvements
- Escalate safety concerns

**Responsibilities:**
- Safety event analysis
- Risk assessment
- Corrective action tracking
- Regulatory reporting

**Accountability:**
- Accountable for safety oversight
- Responsible for lessons learned implementation

---

## 4. HUMAN-AI INTERACTION MODES

### 4.1 Operating Mode Matrix

| Mode | Human Role | NN Role | Override | Examples |
|------|-----------|---------|----------|----------|
| **Advisory** | Decision Maker | Recommender | Always | Route optimization, maintenance scheduling |
| **Supervised** | Monitor | Executor | Always | Autopilot augmentation, fuel cell optimization |
| **Monitored** | Overseer | Autonomous | On alert | System health monitoring, sensor validation |
| **Manual** | Controller | Disabled | N/A | Emergency procedures, manual flight |

### 4.2 Mode Selection Authority

**Mode Changes Allowed:**
- Pilot: Advisory ↔ Supervised ↔ Manual (any time)
- Pilot: Supervised → Manual (emergency override)
- System: Supervised → Manual (automatic fallback on fault)
- System: Cannot transition from Manual to Supervised without pilot command

**Mode Transitions:**

```
         Pilot Command
Advisory ←→ Supervised ←→ Manual
         ↑         ↓
         |    System Fault
         |    (Automatic)
         └─────────┘
```

### 4.3 Crew Interface Requirements

#### 4.3.1 Display Requirements

**Primary Flight Display (PFD) Integration:**
- NN status icon (green/amber/red)
- Confidence level indicator (numeric or bar)
- Mode annunciator (Advisory/Supervised/Manual)
- Alert flags for NN anomalies

**Multi-Function Display (MFD) Details:**
- NN system synoptic page
- Detailed confidence and explanation
- Alternative recommendations
- Performance history

**Engine Indicating and Crew Alerting System (EICAS/ECAM):**
- NN advisory messages (white)
- NN caution messages (amber)
- NN warning messages (red - rare, only for critical failures)

#### 4.3.2 Control Interface

**Mode Control Panel:**
- NN System On/Off switches
- Mode selector (Advisory / Supervised)
- Manual override button (guarded)

**Input Mechanisms:**
- Accept NN recommendation (single click)
- Reject NN recommendation (with alternative input)
- Request explanation (info button)
- Silence nuisance alerts (temporary, auto-resets)

#### 4.3.3 Feedback and Transparency

**Real-Time Feedback:**
```
┌─────────────────────────────────────┐
│ FUEL CELL OPTIMIZATION              │
│                                     │
│ Status: NOMINAL          [■■■■■]97% │
│ Mode: SUPERVISED                    │
│                                     │
│ Current: 1.25 kg/min                │
│ Recommended: 1.23 kg/min (-2%)      │
│                                     │
│ Reason: Reduce power for efficiency │
│ Confidence: HIGH                    │
│                                     │
│ [ACCEPT]  [REJECT]  [INFO]          │
└─────────────────────────────────────┘
```

**Explanation View (on request):**
```
┌─────────────────────────────────────┐
│ FUEL CELL OPTIMIZATION - EXPLAINED  │
│                                     │
│ Top Factors:                        │
│ 1. Low power demand (42%)           │
│ 2. Optimal stack temp (31%)         │
│ 3. Stable flight condition (18%)    │
│                                     │
│ Alternatives Considered:            │
│ • 1.25 kg/min (current)             │
│ • 1.23 kg/min (recommended)         │
│ • 1.20 kg/min (aggressive)          │
│                                     │
│ Expected Outcome:                   │
│ • Fuel savings: 3.2 kg this flight  │
│ • Risk: NONE                        │
│                                     │
│ [CLOSE]                             │
└─────────────────────────────────────┘
```

---

## 5. DECISION AUTHORITY FRAMEWORK

### 5.1 Authority Hierarchy

```
Level 1: PILOT IN COMMAND
         │
         ├─→ Can override any NN decision
         ├─→ Can disable any NN system
         └─→ Final authority on all operations
         
Level 2: AIRCRAFT SYSTEMS (with NN)
         │
         ├─→ Execute within certified ODD
         ├─→ Recommend actions to crew
         └─→ Automatic fallback on fault
         
Level 3: SAFETY MONITORS
         │
         ├─→ Verify NN outputs
         ├─→ Trigger fallback if needed
         └─→ Alert crew to anomalies
         
Level 4: CONVENTIONAL FALLBACK SYSTEMS
         │
         └─→ Maintain safe operation if NN fails
```

### 5.2 Decision Authority Matrix

| Scenario | Primary Authority | Backup Authority | NN Role |
|----------|------------------|------------------|---------|
| Normal Operations | Pilot (accepts NN rec) | Pilot | Advisory/Supervised |
| NN High Confidence | Pilot (usually accepts) | Pilot | Advisory |
| NN Low Confidence | Pilot (evaluates carefully) | Pilot | Advisory only |
| NN OOD Detected | Pilot (manual control) | Conventional system | Disabled |
| System Fault | Automatic fallback | Pilot | Disabled |
| Emergency | Pilot (manual) | Pilot | Disabled |

### 5.3 Override Protocol

**Pilot Override Procedure:**

1. **Identify Need**: NN recommendation inconsistent with pilot judgment
2. **Evaluate**: Check NN confidence, explanation, alternatives
3. **Decide**: Accept, reject, or request more information
4. **Act**: Input manual command or select alternative
5. **Monitor**: Observe system response and aircraft behavior
6. **Document**: Record override rationale (post-flight)

**Automatic Override (System-Initiated):**

1. **Detect**: Safety monitor identifies NN fault or disagreement
2. **Fallback**: Automatic transition to conventional system
3. **Alert**: Crew notified via EICAS/ECAM
4. **Log**: Event recorded for analysis
5. **Maintain**: Conventional system continues operation
6. **Report**: Maintenance action required before NN re-engagement

---

## 6. TRAINING AND COMPETENCY

### 6.1 Flight Crew Training Requirements

#### 6.1.1 Initial Type Rating

**Ground School (8 hours NN systems):**
- NN system overview and capabilities
- Operational Design Domain (ODD)
- Human-AI interaction modes
- Failure recognition and management
- Override procedures
- Explainability and transparency features

**Simulator Training (4 hours NN scenarios):**
- Normal operations with NN assistance
- NN recommendation acceptance/rejection
- NN failure recognition and fallback
- Manual override procedures
- OOD condition handling
- Emergency scenarios with NN disabled

**Line Training (5 sectors with NN):**
- Supervised NN system operation
- Real-world decision-making with NN
- Anomaly recognition
- Communication and crew resource management

#### 6.1.2 Recurrent Training (Annual)

**Ground Refresher (2 hours):**
- NN system updates and improvements
- Lessons learned from fleet experience
- Regulatory changes
- Human factors and common errors

**Simulator Proficiency Check (1 hour):**
- NN failure scenarios
- Override procedures
- Emergency management

### 6.2 Maintenance Personnel Training

#### 6.2.1 Line Maintenance (2-day course)

**Theory:**
- NN system architecture
- BITE procedures
- Routine checks and servicing
- Troubleshooting basics

**Practical:**
- Hands-on BITE operation
- Log download and interpretation
- Component replacement
- Software update procedures

#### 6.2.2 Specialized NN Engineer (5-day course + OJT)

**Advanced Topics:**
- NN model architecture and training
- Configuration management
- Advanced diagnostics
- Model update procedures
- Performance analysis

**On-the-Job Training:**
- Supervised maintenance actions
- Real-world troubleshooting
- Documentation standards

### 6.3 Competency Assessment

**Flight Crew:**
- Written exam (90% pass required)
- Simulator check ride (proficient grade required)
- Line check (satisfactory performance)
- Annual proficiency check

**Maintenance:**
- Written exam (80% pass required)
- Practical skills assessment
- OJT sign-off by qualified instructor

---

## 7. AUDIT TRAIL REQUIREMENTS

### 7.1 Events Requiring Logging

**Flight Operations:**
- [ ] All NN predictions and recommendations
- [ ] Crew responses (accept/reject/override)
- [ ] Mode changes (Advisory/Supervised/Manual)
- [ ] NN confidence levels
- [ ] Explanations provided to crew
- [ ] OOD detections
- [ ] Fallback activations
- [ ] System faults and alerts

**Maintenance:**
- [ ] All configuration changes
- [ ] Software/model updates
- [ ] BITE test results
- [ ] Component replacements
- [ ] Calibration activities
- [ ] Fault investigations
- [ ] Maintenance personnel identity

**Engineering:**
- [ ] Model training and validation
- [ ] Dataset updates
- [ ] Certification evidence generation
- [ ] Design changes
- [ ] Safety analysis updates

### 7.2 Audit Log Structure

```json
{
  "auditLogEntry": {
    "eventId": "AUDIT-UUID",
    "timestamp": "2025-11-05T12:34:56.789Z",
    "eventType": "PilotOverride",
    "userId": "PILOT-LIC-123456",
    "userName": "Capt. John Smith",
    "userRole": "PilotInCommand",
    "aircraftId": "AMPEL360-001",
    "flightId": "FLIGHT-2025-1105-003",
    "nnSystemId": "NN-95-30-01",
    "context": {
      "flightPhase": "cruise",
      "altitude": 35000,
      "systemStatus": "NOMINAL"
    },
    "action": {
      "description": "Pilot rejected NN recommendation",
      "nnRecommendation": {"flowRate": 1.25},
      "pilotInput": {"flowRate": 1.10},
      "rationale": "Conservative setting due to unexpected turbulence forecast"
    },
    "outcome": {
      "systemResponse": "Accepted manual input",
      "safetyImpact": "None",
      "efficiencyImpact": "Slight increase in fuel consumption"
    },
    "cryptographicHash": "SHA-256:...",
    "immutable": true
  }
}
```

### 7.3 Audit Trail Access

**Access Permissions:**

| Role | Real-Time Access | Historical Access | Export | Analysis |
|------|-----------------|------------------|---------|----------|
| Pilot | Own actions (summary) | Own actions (30 days) | No | No |
| Safety Manager | All events (summary) | All events (5 years) | Yes | Yes |
| Maintenance | Maintenance events | All maint events | Yes | Limited |
| Regulator | All events (on request) | All events | Yes | Yes |
| Investigator | All events | All events | Yes | Yes |

### 7.4 Retention Requirements

| Data Type | Retention Period | Storage | Reason |
|-----------|-----------------|---------|---------|
| Operational Logs | 20 years | Secure database | Airworthiness |
| Training Records | 10 years | HR system | Competency evidence |
| Maintenance Logs | 20 years | Maintenance system | Parts traceability |
| Certification Evidence | Permanent | Immutable archive | Type certificate |
| Safety Investigations | Permanent | Safety management | Lessons learned |

---

## 8. ACCOUNTABILITY IN PRACTICE

### 8.1 Scenario-Based Accountability

#### Scenario 1: Normal NN Recommendation Accepted

**Situation:** NN recommends fuel cell flow rate adjustment in cruise.

**Accountability:**
- **NN System**: Provides accurate, explainable recommendation
- **Pilot**: Evaluates recommendation, accepts if reasonable
- **Outcome**: If positive → credit shared; if negative → joint review

**Analysis:**
- Was NN recommendation within ODD? (Yes → NN validated)
- Was pilot evaluation appropriate? (Yes → pilot validated)
- Were procedures followed? (Yes → no fault)

#### Scenario 2: Pilot Overrides NN Recommendation

**Situation:** Pilot manually sets fuel cell flow rate different from NN.

**Accountability:**
- **Pilot**: Responsible for decision and outcome
- **NN System**: Logged disagreement for analysis
- **Review**: If outcome negative, investigate pilot rationale and NN accuracy

**Analysis:**
- Was pilot override justified? (Evaluate situation)
- Was NN recommendation poor? (Review model performance)
- Is additional training needed? (Pilot or model improvement)

#### Scenario 3: NN Provides Incorrect Recommendation

**Situation:** NN recommends action that leads to suboptimal outcome.

**Accountability:**
- **NN System / Developers**: Primary accountability
- **Pilot**: Should have recognized poor recommendation (if obvious)
- **Review**: Root cause analysis, model improvement, crew guidance

**Analysis:**
- Was input OOD? (ODD violation → OOD detector improvement)
- Was model inadequate? (Model deficiency → retraining)
- Should pilot have caught it? (Training or interface improvement)

#### Scenario 4: NN System Failure

**Situation:** NN system faults, fallback system engages.

**Accountability:**
- **System Designers**: Hardware/software reliability
- **Maintenance**: Pre-flight checks adequate?
- **Pilot**: Proper failure management and safe continuation

**Analysis:**
- Was failure predictable? (Maintenance or design issue)
- Did fallback work correctly? (Redundancy validation)
- Was crew response appropriate? (Training validation)

### 8.2 Shared Responsibility Model

```
           Outcome
              │
    ┌─────────┼─────────┐
    │         │         │
  Good     Neutral     Bad
    │         │         │
    ├─────────┴─────────┤
    │                   │
Design/Training      Review
Validated         & Improve
    │                   │
    │                   ├→ Was NN accurate?
    │                   ├→ Was pilot reasonable?
    │                   ├→ Were procedures adequate?
    │                   ├→ Was training sufficient?
    │                   └→ System improvement needed?
    │
    └→ Continue Operations
```

---

## 9. INCIDENT INVESTIGATION FRAMEWORK

### 9.1 Investigation Triggers

**Mandatory Investigation:**
- Safety event involving NN system
- NN recommendation leading to hazardous situation
- Repeated NN failures or anomalies
- Pilot reports of confusing or misleading NN behavior
- Regulatory inquiry

**Optional Investigation:**
- NN performance degradation
- High rate of pilot overrides
- Unusual NN behavior (even if no safety impact)

### 9.2 Investigation Process

**Phase 1: Data Collection (Days 1-3)**
- Retrieve all audit logs
- Download flight data recorder (FDR) / quick access recorder (QAR)
- Interview crew and witnesses
- Collect maintenance records
- Gather NN system diagnostic data

**Phase 2: Analysis (Days 4-14)**
- Reconstruct timeline of events
- Analyze NN decisions and explanations
- Evaluate pilot actions and rationale
- Review procedures and training
- Identify contributing factors

**Phase 3: Root Cause Determination (Days 15-21)**
- Identify primary cause (NN, human, procedure, other)
- Identify contributing factors
- Assess adequacy of safeguards
- Determine accountability

**Phase 4: Corrective Actions (Days 22-30)**
- Develop recommendations
- Assign responsibilities for implementation
- Set timelines for corrective actions
- Plan verification of effectiveness

**Phase 5: Reporting and Closure (Days 31-45)**
- Document findings and recommendations
- Report to regulatory authority
- Share lessons learned with fleet
- Update training and procedures
- Close investigation

### 9.3 Just Culture Principles

AMPEL360 operates under a Just Culture framework:

**Encouraged:**
- Reporting of errors, near-misses, and safety concerns
- Learning from mistakes
- Continuous improvement

**Tolerated (with coaching):**
- Honest mistakes
- Lapses in attention or vigilance
- Knowledge gaps (if training was adequate)

**Not Tolerated:**
- Willful violations of procedures
- Reckless disregard for safety
- Deliberate circumvention of safety systems
- Failure to report known hazards

---

## 10. CONTINUOUS IMPROVEMENT

### 10.1 Feedback Mechanisms

**Flight Crew:**
- Post-flight NN system feedback form
- Anonymous reporting system (for concerns)
- Regular crew meetings to discuss NN experiences
- Suggestion program for improvements

**Maintenance:**
- Maintenance action feedback
- Reliability reporting
- Difficulty reports (procedures, tools, documentation)

**Engineering:**
- Model performance monitoring
- Field data analysis
- Benchmarking against objectives

### 10.2 Human Factors Monitoring

**Metrics Tracked:**
- Pilot override rate (by NN system and scenario)
- Time to decision (with vs. without NN)
- Workload assessment (NASA-TLX surveys)
- Error rates (with NN assistance vs. manual)
- Situational awareness scores

**Targets:**
- Override rate: <5% (excluding justified overrides)
- Decision time: Not significantly increased
- Workload: Same or lower than without NN
- Error rate: Lower than without NN
- Situational awareness: Maintained or improved

### 10.3 Adaptation and Updates

**Trigger for Updates:**
- Model performance below threshold
- High rate of unjustified overrides
- User feedback indicating confusion or distrust
- New operational scenarios identified
- Regulatory guidance changes

**Update Process:**
- Identify improvement need
- Develop solution (model, procedure, training, interface)
- Validate effectiveness
- Obtain regulatory approval (if required)
- Implement across fleet
- Monitor effectiveness

---

## 11. REGULATORY COMPLIANCE

### 11.1 EASA Requirements

**AMC 25.1302 (Installed Systems and Equipment)**
- Crew interface must support proper monitoring
- Alerts must be appropriate and not nuisance
- Automation surprises minimized

**EU AI Act (Article 14 - Human Oversight)**
- Users must be able to understand NN decisions
- Users must be able to intervene effectively
- Risks must be minimized through appropriate interface

### 11.2 FAA Requirements

**AC 25-11B (Electronic Flight Deck Displays)**
- Information must be clear and unambiguous
- Crew must not be overloaded with information
- Failure modes must be evident

**FAA AI Assurance Framework**
- Human authority must be preserved
- Automation must be transparent
- Procedures must be validated

---

## 12. DOCUMENT CONTROL

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-10-12 | Human Factors Lead | Initial framework |
| 0.5 | 2025-10-29 | Operations Team | Stakeholder roles defined |
| 1.0 | 2025-11-04 | Chief Engineer | Released version |

**Document Status:** ✅ RELEASED  
**Next Review:** 2026-05-04 (Semi-annual)  
**Approved By:** Chief Engineer - AI Systems, Chief Pilot, Human Factors Lead

---

**Related Documents:**
- ATA_95_Purpose_Scope.md
- Applicability_Matrix.md
- Traceability_Requirements.md
- Interface_Documentation.md
- Certification_Framework.md
- Flight Crew Operating Manual (FCOM) - NN Systems Supplement
- Maintenance Manual - NN Systems Procedures
