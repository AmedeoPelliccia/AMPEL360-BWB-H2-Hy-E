# Risk Assessment Methodology
## AMPEL360 BWB H2 Hy-E Q100 INTEGRA

**Document ID:** AMPEL360-02-00-00-SAF-RAM  
**Version:** 1.0.0  
**Date:** 2025-11-04  
**Classification:** Safety Critical

---

## 1. INTRODUCTION

### 1.1 Purpose

This document defines the methodology for identifying, assessing, and mitigating operational risks for the AMPEL360 aircraft. It provides a systematic approach to ensure all operational hazards are identified and controlled to acceptable levels.

### 1.2 Scope

This methodology applies to:
- Flight operations
- Ground operations
- Hydrogen fuel operations
- Fuel cell propulsion operations
- CAOS AI-assisted operations
- Emergency response operations

### 1.3 Regulatory Basis

- EASA Part-ORO (Organization Requirements)
- ICAO Annex 19 (Safety Management)
- ICAO Doc 9859 (Safety Management Manual)
- CS-25 (Certification Specifications for Large Aeroplanes)

---

## 2. RISK ASSESSMENT PROCESS

### 2.1 Process Overview

```
Step 1: HAZARD IDENTIFICATION
    ↓
Step 2: RISK ANALYSIS
    ↓ (Severity Assessment)
    ↓ (Probability Assessment)
    ↓
Step 3: RISK EVALUATION
    ↓ (Is risk acceptable?)
    ↓
Step 4: RISK MITIGATION
    ↓ (Develop controls)
    ↓
Step 5: RESIDUAL RISK ASSESSMENT
    ↓
Step 6: RISK ACCEPTANCE
    ↓ (Document decision)
    ↓
Step 7: RISK MONITORING
    ↓ (Continuous surveillance)
```

---

## 3. HAZARD IDENTIFICATION

### 3.1 Hazard Identification Methods

**Proactive Methods:**
- Safety Risk Assessment workshops
- What-If analysis
- Failure Modes and Effects Analysis (FMEA)
- Hazard and Operability Study (HAZOP)
- Change analysis
- Job Safety Analysis
- Operational walk-throughs

**Reactive Methods:**
- Incident/accident investigation
- Safety report analysis
- Flight data monitoring analysis
- Audit findings
- Crew debriefs

**Predictive Methods:**
- Industry trend analysis
- Technological risk assessment
- Regulatory intelligence
- Research findings

### 3.2 Hazard Sources

**Operational Environment:**
- Weather (icing, turbulence, wind shear)
- Airports (runway conditions, terrain)
- Airspace (congestion, conflicting traffic)
- Air Traffic Control (communication, procedures)

**Aircraft Systems:**
- H2 fuel system (leaks, temperature, pressure)
- Fuel cell propulsion (thermal, power, degradation)
- CAOS AI system (algorithm errors, data quality)
- BWB flight controls (handling, stability)
- Emergency systems (reliability, accessibility)

**Human Factors:**
- Crew errors (skill-based, rule-based, knowledge-based)
- Fatigue and stress
- Communication breakdowns
- Decision-making under pressure
- Workload management

**Organizational Factors:**
- Procedures (inadequate, unclear, conflicting)
- Training (insufficient, ineffective)
- Scheduling (fatigue-inducing)
- Culture (production pressure, reporting climate)
- Resources (staffing, equipment, budget)

**External Factors:**
- Regulatory changes
- Economic pressures
- Public perception
- Security threats
- Supply chain disruptions

### 3.3 Hazard Documentation

Each identified hazard shall be documented with:
- **Hazard ID**: Unique identifier
- **Hazard Description**: Clear, concise description
- **Operational Context**: When/where it occurs
- **Potential Consequences**: What could happen
- **Existing Controls**: Current mitigations
- **Identification Date**: When identified
- **Identified By**: Person/team who identified it
- **Status**: Open, mitigated, closed

---

## 4. RISK ANALYSIS

### 4.1 Severity Assessment

**Severity Categories:**

| Level | Category | Definition | Operational Examples |
|-------|----------|------------|---------------------|
| **5** | Catastrophic | - Hull loss<br>- Multiple fatalities | - Uncontained H2 explosion<br>- Complete loss of control<br>- Mid-air collision |
| **4** | Hazardous | - Large reduction in safety margins<br>- Serious injury<br>- Major equipment damage | - H2 leak with ignition<br>- Loss of fuel cell propulsion<br>- CAOS critical malfunction |
| **3** | Major | - Significant reduction in safety margins<br>- Minor injuries possible<br>- Significant equipment damage | - Single fuel cell stack failure<br>- H2 system degradation<br>- CAOS advisory conflicts |
| **2** | Minor | - Slight reduction in safety margins<br>- Increased workload<br>- Minor equipment damage | - CAOS advisory error (detected)<br>- Minor H2 system anomaly<br>- Procedural deviation |
| **1** | No Effect | - No safety impact<br>- Nuisance only | - Passenger comfort issue<br>- Cosmetic damage<br>- Administrative error |

**Severity Assessment Criteria:**
- Consider worst realistic case
- Account for existing safety barriers
- Evaluate direct and indirect consequences
- Consider combined effects

### 4.2 Probability Assessment

**Probability Categories:**

| Level | Category | Quantitative | Qualitative Description |
|-------|----------|--------------|------------------------|
| **A** | Frequent | >10⁻³ per FH | Expected to occur frequently in fleet operations |
| **B** | Reasonably Probable | 10⁻³ to 10⁻⁵ per FH | Will occur several times in fleet lifetime |
| **C** | Remote | 10⁻⁵ to 10⁻⁷ per FH | Unlikely but may occur in fleet lifetime |
| **D** | Extremely Remote | 10⁻⁷ to 10⁻⁹ per FH | Very unlikely to occur in fleet lifetime |
| **E** | Extremely Improbable | <10⁻⁹ per FH | Almost inconceivable to occur |

**Probability Assessment Factors:**
- Operational exposure (frequency of operation)
- Equipment reliability
- Human error probability
- Environmental conditions
- Existing barriers effectiveness
- Historical data (when available)

**Probability Estimation Methods:**
- Historical data analysis
- Engineering judgment
- Fault tree analysis
- Event tree analysis
- Human reliability analysis
- Monte Carlo simulation

### 4.3 Risk Level Determination

**Risk Matrix:**

| Severity ↓ / Probability → | A (Frequent) | B (Reasonably Probable) | C (Remote) | D (Extremely Remote) | E (Extremely Improbable) |
|---------------------------|--------------|------------------------|-----------|---------------------|-------------------------|
| **5 - Catastrophic** | 5A (Unacceptable) | 5B (Unacceptable) | 5C (Review) | 5D (Acceptable) | 5E (Acceptable) |
| **4 - Hazardous** | 4A (Unacceptable) | 4B (Review) | 4C (Acceptable) | 4D (Acceptable) | 4E (Acceptable) |
| **3 - Major** | 3A (Review) | 3B (Acceptable) | 3C (Acceptable) | 3D (Acceptable) | 3E (Acceptable) |
| **2 - Minor** | 2A (Acceptable) | 2B (Acceptable) | 2C (Acceptable) | 2D (Acceptable) | 2E (Acceptable) |
| **1 - No Effect** | 1A (Acceptable) | 1B (Acceptable) | 1C (Acceptable) | 1D (Acceptable) | 1E (Acceptable) |

**Risk Categories:**
- 🔴 **Unacceptable**: Immediate action required, operations not permitted
- 🟡 **Review** (ALARP): Requires detailed review and mitigation to ALARP
- 🟢 **Acceptable**: Risk acceptable with current controls, continue monitoring

---

## 5. RISK EVALUATION

### 5.1 Risk Tolerability Assessment

**Acceptability Criteria:**

**Acceptable Risks (Green):**
- Can be accepted with current controls
- Requires periodic monitoring
- May have minor improvements identified
- Documentation in risk register

**ALARP Risks (Yellow):**
- Must be reduced As Low As Reasonably Practicable
- Requires cost-benefit analysis
- Multiple mitigation options evaluated
- Strong justification for residual risk
- Senior management approval required

**Unacceptable Risks (Red):**
- Operations not permitted
- Immediate mitigation required
- Alternative approach must be found
- Cannot be accepted under any circumstances

### 5.2 ALARP Demonstration

**Required Elements:**
1. **Identification of All Mitigations**: Brainstorm all possible risk reductions
2. **Good Practice Review**: Industry standards and best practices
3. **Cost-Benefit Analysis**: 
   - Cost of implementation (financial, operational)
   - Safety benefit (risk reduction)
   - Proportionality assessment
4. **Stakeholder Consultation**: Crew, engineering, regulators
5. **Documentation**: Detailed ALARP case
6. **Approval**: Head of Safety and Accountable Manager

**ALARP Acceptance Criteria:**
- All reasonably practicable mitigations implemented
- Remaining mitigations grossly disproportionate to benefit
- Good practice standards met or exceeded
- Independent review completed
- Regulatory acceptance (if required)

---

## 6. RISK MITIGATION

### 6.1 Mitigation Strategies

**Hierarchy of Controls (in order of preference):**

1. **Elimination**: Remove the hazard entirely
   - Example: Avoid operations in hazardous conditions

2. **Substitution**: Replace with less hazardous alternative
   - Example: Use safer procedures or equipment

3. **Engineering Controls**: Redesign system/procedure
   - Example: Add leak detection systems, automatic shutdowns

4. **Administrative Controls**: Procedures, training, signage
   - Example: SOPs, checklists, briefings, limitations

5. **Personal Protective Equipment**: Last resort
   - Example: Protective gear for H2 refueling

### 6.2 Mitigation Selection Criteria

**Effectiveness:**
- How much does it reduce risk?
- Does it address root cause?
- Is it reliable?

**Practicality:**
- Can it be implemented?
- What are resource requirements?
- Implementation timeline?

**Side Effects:**
- Does it create new hazards?
- Does it affect other operations?
- Crew acceptance?

**Sustainability:**
- Can it be maintained long-term?
- Is it dependent on human compliance?
- Does it require ongoing resources?

### 6.3 Mitigation Implementation

**Implementation Plan:**
1. **Mitigation Design**: Detailed design of control
2. **Resource Allocation**: Budget, personnel, equipment
3. **Schedule**: Implementation timeline
4. **Responsibility Assignment**: Owner of mitigation
5. **Communication**: Inform affected personnel
6. **Training**: If required for new procedures
7. **Verification**: Confirm implementation
8. **Validation**: Confirm effectiveness

---

## 7. RESIDUAL RISK ASSESSMENT

### 7.1 Residual Risk Determination

After mitigations are applied:
1. Re-assess severity (may be reduced by mitigations)
2. Re-assess probability (should be reduced by mitigations)
3. Determine new risk level
4. Compare to acceptability criteria

### 7.2 Residual Risk Documentation

Document for each risk:
- **Mitigations Applied**: List all controls implemented
- **Residual Severity**: Post-mitigation severity
- **Residual Probability**: Post-mitigation probability
- **Residual Risk Level**: New risk rating
- **Acceptability**: Acceptable/ALARP/Unacceptable
- **Justification**: Why residual risk is acceptable

### 7.3 Residual Risk Acceptance

**Acceptance Authority:**

| Residual Risk Level | Acceptance Authority |
|--------------------|---------------------|
| Catastrophic-Frequent (5A) | Not Acceptable |
| Catastrophic-Reasonably Probable (5B) | Not Acceptable |
| Catastrophic-Remote (5C) | Accountable Manager + Regulator |
| Catastrophic-Extremely Remote (5D) | Accountable Manager |
| Hazardous-Frequent (4A) | Not Acceptable |
| Hazardous-Reasonably Probable (4B) | Accountable Manager |
| Hazardous-Remote (4C) | Head of Safety |
| Major-Frequent (3A) | Head of Safety |
| All other acceptable risks | Department Manager |

---

## 8. RISK MONITORING

### 8.1 Monitoring Activities

**Continuous Monitoring:**
- Flight data monitoring for operational deviations
- Safety report analysis for emerging hazards
- System performance tracking (H2, fuel cell, CAOS)
- Trend analysis

**Periodic Review:**
- Quarterly risk register review
- Annual comprehensive risk assessment
- Post-incident risk re-evaluation
- Post-change risk assessment

**Trigger-Based Review:**
- New incident/accident
- System modification
- Procedural change
- Regulatory change
- Industry event

### 8.2 Risk Register Maintenance

**Risk Register Updates:**
- New risks added when identified
- Existing risks re-assessed periodically
- Closed risks archived
- Mitigation status tracked
- Action items followed up

**Risk Register Contents:**
- Risk ID and description
- Severity and probability
- Risk level
- Mitigations planned/implemented
- Residual risk
- Acceptance status and authority
- Review dates
- Status (open/closed)

---

## 9. SPECIAL CONSIDERATIONS

### 9.1 Hydrogen Fuel Risks

**Unique Characteristics:**
- Wide flammability range (4-75% vol)
- Very low ignition energy (0.02 mJ)
- Invisible flame
- High diffusivity (rapid dispersion)
- Cryogenic temperatures (-253°C)
- Embrittlement of metals

**Risk Assessment Focus:**
- Leak scenarios (all phases of operation)
- Fire/explosion scenarios
- Cryogenic exposure
- Confined space accumulation
- Ignition sources
- Human factors (invisible hazards)

### 9.2 Fuel Cell Propulsion Risks

**Unique Characteristics:**
- Novel propulsion technology
- Thermal management critical
- Performance degradation over time
- Multiple parallel stacks
- Complex control algorithms

**Risk Assessment Focus:**
- Thermal runaway scenarios
- Stack failure modes
- Power loss scenarios
- Control system failures
- Maintenance-induced failures

### 9.3 CAOS AI System Risks

**Unique Characteristics:**
- Algorithm-based decisions
- Machine learning (non-deterministic)
- Data-dependent performance
- Complex interactions
- Trust calibration challenges

**Risk Assessment Focus:**
- Algorithm errors (false positives/negatives)
- Data quality issues
- Human-AI interaction failures
- Automation surprise
- Mode confusion
- Over-reliance or under-trust

### 9.4 BWB Configuration Risks

**Unique Characteristics:**
- Non-conventional aerodynamics
- Wide CG range
- Distributed passenger seating
- Unique ground handling

**Risk Assessment Focus:**
- Handling characteristics surprises
- Evacuation challenges
- Ground clearance issues
- Load distribution errors
- Crew training effectiveness

---

## 10. RISK ASSESSMENT DOCUMENTATION

### 10.1 Risk Assessment Report Template

**Standard Sections:**
1. **Executive Summary**: Key findings and recommendations
2. **Scope and Methodology**: What was assessed and how
3. **Hazard Identification**: All hazards identified
4. **Risk Analysis**: Severity, probability, risk level
5. **Risk Evaluation**: Acceptability determination
6. **Mitigation Recommendations**: Proposed controls
7. **Residual Risk**: Post-mitigation assessment
8. **Acceptance Decision**: Authority and justification
9. **Monitoring Plan**: How risk will be tracked
10. **Appendices**: Detailed analysis, data

### 10.2 Quality Assurance

**Risk Assessment Review:**
- Peer review by safety team
- Independent review for high risks
- Management review and approval
- Regulatory submission (if required)

**Review Criteria:**
- Completeness: All hazards identified?
- Accuracy: Severity/probability correct?
- Justification: Assessments well-supported?
- Mitigations: Appropriate and effective?
- Documentation: Clear and traceable?

---

## 11. ROLES AND RESPONSIBILITIES

### 11.1 Risk Assessment Roles

**Accountable Manager:**
- Overall accountability for safety
- Approval of high-level risks
- Resource allocation for mitigations

**Head of Safety:**
- Risk assessment process ownership
- Risk register maintenance
- Coordination of risk assessments
- Approval of moderate risks

**Operational Departments:**
- Identify operational hazards
- Participate in risk assessments
- Implement mitigations
- Monitor residual risks

**Safety Risk Assessment Team:**
- Facilitate risk assessment workshops
- Document risk assessments
- Track mitigation actions
- Report on risk status

**Subject Matter Experts:**
- Provide technical input
- Assess system-specific risks
- Validate mitigations
- Support implementation

### 11.2 Training Requirements

**Risk Assessment Training:**
- All managers: Risk assessment overview (4 hours)
- Safety team: Advanced risk assessment (16 hours)
- SMEs: System-specific risk assessment (8 hours)
- Operational staff: Hazard identification (2 hours)

---

## 12. DOCUMENT CONTROL

**Version History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-11-04 | Safety Department | Initial release |

**Next Review Date:** 2026-05-04

---

**Document Owner:** Head of Safety  
**Classification:** Safety Critical - Unclassified  
**Configuration Control:** Git SHA-256: [hash]
