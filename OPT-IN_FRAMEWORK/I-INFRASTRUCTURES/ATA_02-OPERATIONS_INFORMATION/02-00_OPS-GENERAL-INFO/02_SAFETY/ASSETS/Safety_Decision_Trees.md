# Safety Decision Trees
## AMPEL360 BWB H2 Hy-E Q100 INTEGRA

**Document ID:** AMPEL360-02-00-00-SAF-DECTREE  
**Version:** 1.0.0  
**Date:** 2025-11-04  
**Classification:** Safety Critical

---

This document provides decision trees for critical safety decisions during AMPEL360 operations.

---

## 1. EMERGENCY SEVERITY CLASSIFICATION

```
START: Event Occurred
    │
    ▼
Is there immediate threat to life or aircraft?
    │
    ├─YES──► LEVEL 3: DISTRESS
    │         • MAYDAY call
    │         • Maximum priority
    │         • Emergency services on standby
    │         • Possible aircraft loss scenario
    │
    └─NO
      │
      ▼
Is there significant safety concern requiring
immediate action or priority handling?
    │
    ├─YES──► LEVEL 2: EMERGENCY
    │         • PAN-PAN call
    │         • Priority handling
    │         • Immediate action required
    │         • Significant safety concern
    │
    └─NO
      │
      ▼
Is there potential emergency developing or
precautionary measures needed?
    │
    ├─YES──► LEVEL 1: ALERT
    │         • Enhanced monitoring
    │         • Precautionary measures
    │         • Normal operations continue
    │         • Heightened awareness
    │
    └─NO──► NORMAL OPERATIONS
             • Standard procedures
             • Continue monitoring
```

**Reference:** [Emergency_Response_Framework.md Section 2.1](../Emergency_Response_Framework.md#21-emergency-levels)

---

## 2. DIVERSION DECISION

```
START: Abnormal Condition
    │
    ▼
Can aircraft safely reach destination?
    │
    ├─NO──► IMMEDIATE DIVERSION REQUIRED
    │         • Nearest suitable airport
    │         • Declare emergency if needed
    │         • Coordinate with ATC
    │
    └─YES/UNCERTAIN
      │
      ▼
Assess Risk Factors:
  • System degradation trend
  • Weather at destination vs alternates
  • Available emergency services
  • Fuel state
  • Passenger/cargo considerations
    │
    ▼
Risk Assessment Score:
    │
    ├─HIGH RISK──► DIVERT NOW
    │               • Don't delay
    │               • Shorter = safer
    │
    ├─MODERATE──► PLAN DIVERSION
    │             • Monitor closely
    │             • Brief nearest alternates
    │             • Ready to execute
    │
    └─LOW RISK──► CONTINUE WITH CAUTION
                  • Enhanced monitoring
                  • Update crew and company
                  • Alternate plan ready
```

**Risk Factors Scoring:**
- Worsening condition: +3
- Limited fuel state: +3
- Poor weather ahead: +2
- Better alternate available: +2
- Passenger medical: +1-3 (severity)
- Score ≥7: Divert now
- Score 4-6: Plan diversion
- Score <4: Continue with monitoring

**Reference:** [Operations_Safety_Framework.md](../Operations_Safety_Framework.md)

---

## 3. EVACUATION GO/NO-GO DECISION

```
START: Aircraft on Ground, Emergency Condition
    │
    ▼
Is there IMMEDIATE threat to occupants?
  • Fire visible/spreading
  • Smoke filling cabin
  • Structural failure imminent
  • Explosion risk
    │
    ├─YES──► EVACUATE IMMEDIATELY
    │         Command: "EVACUATE, EVACUATE!"
    │         • All available exits
    │         • Leave all belongings
    │         • Assist others
    │
    └─NO
      │
      ▼
Assess Evacuation Environment:
    │
    ▼
Is evacuation environment SAFE?
  • Fire/hazards outside?
  • Adequate slide deployment?
  • Weather acceptable?
  • Surface conditions OK?
    │
    ├─NO──► REMAIN ON BOARD (Safer Inside)
    │        • Monitor situation
    │        • Prepare for evacuation
    │        • Coordinate with emergency services
    │        • Reevaluate continuously
    │
    └─YES
      │
      ▼
Can CONTROLLED deplaning be done safely?
  • No immediate threat
  • Emergency services arrived
  • Stairs/jetway available
  • Time permits
    │
    ├─YES──► CONTROLLED DEPLANING
    │         • Selected exits
    │         • Orderly process
    │         • Assist passengers
    │
    └─NO──► PRECAUTIONARY EVACUATION
             • Use slides
             • Orderly but quick
             • All exits if needed
```

**BWB Specific Considerations:**
- Multiple evacuation levels
- Wider cabin cross-section
- Crew positioning critical
- 90-second target maintained

**Reference:** [Emergency_Response_Framework.md](../Emergency_Response_Framework.md), [BWB_Operational_Safety.md](../BWB_Operational_Safety.md)

---

## 4. CAOS RECOMMENDATION OVERRIDE DECISION

```
START: CAOS Provides Recommendation
    │
    ▼
Is recommendation CLEARLY UNSAFE?
  • Violates limits
  • Conflicts with regulations
  • Intuition says wrong
    │
    ├─YES──► OVERRIDE IMMEDIATELY
    │         • Manual action
    │         • Report event
    │
    └─NO
      │
      ▼
Is crew's understanding of situation
BETTER than CAOS's?
  • Crew has info CAOS lacks
  • Local conditions unknown to CAOS
  • Recent changes not in CAOS data
    │
    ├─YES──► OVERRIDE WITH JUSTIFICATION
    │         • Document reasoning
    │         • Report for learning
    │
    └─NO
      │
      ▼
Check CAOS Confidence Level and Explanation
    │
    ▼
Is confidence level HIGH (>90%) and
explanation MAKES SENSE?
    │
    ├─YES──► ACCEPT RECOMMENDATION
    │         • Implement as suggested
    │         • Monitor outcome
    │
    ├─MODERATE (70-90%)──► VERIFY BEFORE ACCEPTING
    │                      • Cross-check with other sources
    │                      • Discuss with crew
    │                      • Use judgment
    │
    └─LOW (<70%)──► TREAT AS ADVISORY ONLY
                     • Manual decision primary
                     • CAOS input considered
                     • Crew judgment prevails
```

**Key Principle:** Flight crew retains final authority. CAOS is advisory.

**Reference:** [CAOS_Safety_Integration.md Section 2.1](../CAOS_Safety_Integration.md#21-authority-and-responsibility)

---

## 5. RISK ACCEPTANCE AUTHORITY

```
START: Risk Identified and Assessed
    │
    ▼
Determine RESIDUAL RISK LEVEL
(After mitigations applied)
    │
    ▼
Severity × Probability = Risk Level
    │
    ├─5A, 5B, 4A (Red)──► UNACCEPTABLE
    │                      • Operations not permitted
    │                      • Further mitigation required
    │                      • Re-assess after mitigation
    │
    ├─5C, 4B, 3A (Yellow)──► ALARP Required
    │                         • Detailed justification needed
    │                         • Cost-benefit analysis
    │                         │
    │                         ▼
    │                    Who Can Accept?
    │                         │
    │                         ├─5C──► Accountable Manager + Regulator
    │                         ├─4B──► Accountable Manager
    │                         └─3A──► Head of Safety
    │
    └─All Others (Green)──► ACCEPTABLE
                             │
                             ▼
                        Who Can Accept?
                             │
                             ├─4C, 4D──► Accountable Manager
                             ├─3B, 3C, 3D──► Head of Safety
                             └─2x, 1x──► Department Manager
```

**Risk Matrix Reference:**
- Severity: 5 (Catastrophic) to 1 (No Effect)
- Probability: A (Frequent) to E (Extremely Improbable)

**Reference:** [Risk_Assessment_Methodology.md Section 7](../Risk_Assessment_Methodology.md#7-residual-risk-assessment)

---

## 6. CONTINUATION VS. RETURN DECISION

```
START: Problem Identified After Takeoff
    │
    ▼
Is immediate return REQUIRED by regulations?
  • Engine failure (twin below performance)
  • Fire warning (uncontained)
  • Pressurization failure (high altitude)
  • Flight control malfunction (major)
    │
    ├─YES──► RETURN IMMEDIATELY
    │         • Execute memory items
    │         • Declare emergency
    │         • Nearest suitable airport
    │
    └─NO
      │
      ▼
Assess Problem Severity:
    │
    ├─GETTING WORSE──► RETURN
    │                   • Don't continue with
    │                     deteriorating condition
    │
    ├─STABLE──► Continue Assessment Below
    │
    └─IMPROVING──► CONTINUE (with monitoring)
                    • May be transient issue
                    • Monitor carefully
                    │
                    ▼
Compare Return vs. Continue Options:
    │
    ├─RETURN Benefits:
    │   • Known airport
    │   • Heavy weight landing accepted
    │   • Company maintenance available
    │   • Less time/distance
    │   • Passenger preference
    │
    └─CONTINUE Benefits:
        • Burn down to lower weight
        • Destination may have better services
        • Weather better at destination
        • Avoid over water return
        │
        ▼
Apply Decision Criteria:
  □ Safety is priority #1
  □ Can destination be reached safely?
  □ Is destination weather acceptable?
  □ Are required systems operational?
  □ Is performance adequate?
    │
    ├─ALL YES──► CONTINUE TO DESTINATION
    │            • Enhanced monitoring
    │            • Brief crew and company
    │            • Alternate plan ready
    │
    └─ANY NO──► RETURN OR DIVERT
                 • Choose best option
                 • Coordinate with ATC/Company
```

**Reference:** [Operations_Safety_Framework.md](../Operations_Safety_Framework.md)

---

## 7. EMERGENCY POWER MANAGEMENT

```
START: Power System Degraded
    │
    ▼
How many FUEL CELL STACKS available?
    │
    ├─8 Stacks (100%)──► FULL CAPABILITY
    │                     • No limitations
    │                     • Continue normal ops
    │
    ├─7 Stacks (87%)──► NEAR FULL
    │                    • Minor limitations
    │                    • Monitor closely
    │                    • Continue to destination
    │
    ├─6 Stacks (75%)──► MODERATE
    │                    • Significant limitations apply:
    │                      - Reduced climb rate
    │                      - Lower ceiling
    │                      - Consider diversion
    │
    ├─5 Stacks (62%)──► LIMITED
    │                    • Major limitations:
    │                      - Significantly reduced performance
    │                      - DIVERT RECOMMENDED
    │                      - Declare emergency
    │
    └─<5 Stacks (<50%)──► EMERGENCY
                           • LAND IMMEDIATELY
                           • Nearest suitable airport
                           • Load shedding required
                           │
                           ▼
                      LOAD SHEDDING PRIORITY:
                      Keep (Essential):
                        ☑ Flight controls
                        ☑ Navigation (primary)
                        ☑ Communications (1 radio)
                        ☑ Flight instruments
                      
                      Shed (Non-Essential):
                        ☐ Galley
                        ☐ IFE
                        ☐ Cabin lighting (reduced)
                        ☐ Secondary systems
```

**Fuel Cell Stack Management:**
- CAOS automatically manages load distribution
- Crew monitors and can override
- Emergency manual control available

**Reference:** [Fuel_Cell_Safety_Operations.md Section 5.2](../Fuel_Cell_Safety_Operations.md#52-fuel-cell-stack-failure)

---

## 8. H2 SYSTEM ISOLATION DECISION

```
START: H2 System Anomaly Detected
    │
    ▼
What is LEAK DETECTION reading?
    │
    ├─>5% LEL──► ISOLATE IMMEDIATELY
    │             • Emergency H2 shutdown
    │             • Fuel cells to alternate fuel (if available)
    │             • Maximum ventilation
    │             • Land ASAP
    │
    ├─2.5-5% LEL──► PREPARE TO ISOLATE
    │                │
    │                ▼
    │           Is leak INCREASING?
    │                │
    │                ├─YES──► ISOLATE NOW
    │                │
    │                └─NO──► MONITOR CLOSELY
    │                         • Leak may stabilize
    │                         • Ready to isolate
    │                         • Plan diversion
    │
    ├─1-2.5% LEL──► ENHANCED MONITORING
    │                • Increase ventilation
    │                • Identify source if possible
    │                • Consider isolation if worsening
    │                • Plan precautionary landing
    │
    └─<1% LEL──► NORMAL MONITORING
                  • Note in log
                  • Assess trend
                  • Inform maintenance
```

**Factors to Consider:**
- **Flight Phase:** More aggressive on ground
- **Fire Risk:** Any ignition sources nearby?
- **Fuel Remaining:** Can complete flight without H2?
- **Alternatives:** Is alternate fuel available?

**Post-Isolation:**
- Fuel cells shutdown or switch to alternate fuel
- Use APU or RAT for essential power
- Land at nearest suitable airport

**Reference:** [H2_Operational_Safety.md Section 5.2](../H2_Operational_Safety.md#52-h2-leak---in-flight)

---

## 9. DOCUMENT CONTROL

**Version History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-11-04 | Safety Department | Initial release |

**Next Review Date:** 2026-05-04

**Related Documents:**
- [Operations_Safety_Framework.md](../Operations_Safety_Framework.md)
- [Risk_Assessment_Methodology.md](../Risk_Assessment_Methodology.md)
- [Emergency_Response_Framework.md](../Emergency_Response_Framework.md)
- [H2_Operational_Safety.md](../H2_Operational_Safety.md)
- [Fuel_Cell_Safety_Operations.md](../Fuel_Cell_Safety_Operations.md)
- [CAOS_Safety_Integration.md](../CAOS_Safety_Integration.md)

---

**Document Owner:** Head of Safety  
**Classification:** Safety Critical - Unclassified
