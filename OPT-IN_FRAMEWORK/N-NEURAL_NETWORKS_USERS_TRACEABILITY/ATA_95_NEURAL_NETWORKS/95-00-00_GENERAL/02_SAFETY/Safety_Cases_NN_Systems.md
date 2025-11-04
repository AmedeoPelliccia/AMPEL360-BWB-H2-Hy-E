# Safety Cases for Neural Network Systems

**Document ID:** AMPEL360-95-00-00-SAF-SC  
**Version:** 1.0  
**Date:** 2025-11-04  
**Classification:** Safety Critical

---

## 1. INTRODUCTION

### 1.1 Purpose

This document presents safety case arguments demonstrating that neural network systems in the AMPEL360 aircraft are acceptably safe for their intended use.

### 1.2 Safety Case Definition

**Safety Case**: A structured argument, supported by evidence, that a system is acceptably safe for a specific application in a specific environment.

### 1.3 Structure

Each safety case follows the Goal Structuring Notation (GSN) pattern:
- **Claims** (Goals): Assertions about system safety
- **Evidence**: Data and artifacts supporting claims
- **Strategies**: Approach to decompose claims
- **Context**: Assumptions and environment

---

## 2. TOP-LEVEL SAFETY CLAIM

### 2.1 Primary Claim

**G1: AMPEL360 NN Systems are Acceptably Safe**

**Definition of "Acceptably Safe"**:
- Risks reduced to As Low As Reasonably Practicable (ALARP)
- Compliance with regulatory requirements (CS-25, 14 CFR 25)
- Probability of catastrophic failure <10⁻⁹ per flight hour
- Probability of hazardous failure <10⁻⁷ per flight hour

**Context**:
- Aircraft: AMPEL360 (hydrogen fuel cell, blended wing body)
- Operation: Commercial passenger transport
- Environment: All weather, day/night, worldwide operations
- Regulations: EASA CS-25, FAA 14 CFR 25, EU AI Act

### 2.2 Argument Strategy

**S1: Argue over NN safety lifecycle**

```
G1: NN Systems Acceptably Safe
    ↓ [S1: Lifecycle approach]
    ├─ G1.1: Safe Development Process
    ├─ G1.2: Hazards Identified and Mitigated
    ├─ G1.3: Requirements Met and Verified
    └─ G1.4: Operational Safety Maintained
```

---

## 3. SUB-CLAIM 1: SAFE DEVELOPMENT PROCESS

### 3.1 Claim

**G1.1: NN Systems Developed Using Rigorous Safety-Focused Process**

### 3.2 Argument

**S1.1: Argue over development phases**

```
G1.1: Safe Development Process
    ↓ [S1.1: Development phases]
    ├─ G1.1.1: Training Data Validated
    ├─ G1.1.2: Model Architecture Justified
    ├─ G1.1.3: Training Process Controlled
    ├─ G1.1.4: Model Verified and Validated
    └─ G1.1.5: Integration Safety Assessed
```

#### 3.2.1 Training Data Validated (G1.1.1)

**Claim**: Training data is representative, unbiased, and of high quality

**Evidence**:
- **E1.1.1-A**: Dataset Coverage Report
  - Demonstrates >99% coverage of operational design domain
  - Statistical analysis of feature distributions
  - Comparison to operational data

- **E1.1.1-B**: Bias Analysis Report
  - Testing across operational factors (weather, location, time, aircraft config)
  - No systematic errors >5% in any category
  - Fairness metrics computed

- **E1.1.1-C**: Data Quality Audit
  - Data provenance documentation
  - Label accuracy verification (multi-annotator consensus)
  - Outlier detection and removal
  - Data validation pipeline

- **E1.1.1-D**: Independent Expert Review
  - Domain experts reviewed dataset
  - Confirmed representativeness
  - Identified and filled gaps

**Argument**:
```
Training data covers >99% of ODD [E1.1.1-A]
    AND
No significant bias detected [E1.1.1-B]
    AND
Data quality validated [E1.1.1-C]
    AND
Expert review confirms adequacy [E1.1.1-D]
    THEREFORE
Training data is adequate for safe deployment
```

#### 3.2.2 Model Architecture Justified (G1.1.2)

**Claim**: NN architecture is appropriate for task and safety requirements

**Evidence**:
- **E1.1.2-A**: Architecture Selection Report
  - Trade study of candidate architectures
  - Justification for chosen design
  - Comparison to state-of-the-art

- **E1.1.2-B**: Architecture Review
  - Independent review by ML experts
  - Verification of design choices
  - No known architectural vulnerabilities

- **E1.1.2-C**: Similar System Precedent
  - Architecture similar to systems deployed in [automotive/aerospace]
  - Proven track record
  - Lessons learned incorporated

**Argument**:
```
Architecture appropriate for task [E1.1.2-A]
    AND
Independent review confirms [E1.1.2-B]
    AND
Similar architecture proven in practice [E1.1.2-C]
    THEREFORE
Architecture is justified
```

#### 3.2.3 Training Process Controlled (G1.1.3)

**Claim**: Model training followed controlled, reproducible process

**Evidence**:
- **E1.1.3-A**: Training Process Documentation
  - Hyperparameters specified
  - Training algorithm documented
  - Convergence criteria defined

- **E1.1.3-B**: Training Reproducibility
  - Independent team re-trained model
  - Achieved similar performance
  - Demonstrates process robustness

- **E1.1.3-C**: Configuration Management
  - All training artifacts version controlled
  - Dataset, code, model weights tracked
  - Traceability established

**Argument**:
```
Training process documented [E1.1.3-A]
    AND
Process is reproducible [E1.1.3-B]
    AND
Configuration managed [E1.1.3-C]
    THEREFORE
Training process is controlled
```

#### 3.2.4 Model Verified and Validated (G1.1.4)

**Claim**: Model performance meets safety requirements

**Evidence**:
- **E1.1.4-A**: Test Results
  - >10 million test cases
  - Accuracy >99.9% (DAL A/B requirement)
  - Precision, recall, F1 scores documented

- **E1.1.4-B**: Corner Case Testing
  - >1000 edge scenarios tested
  - No failures on safety-critical cases
  - Boundary behavior characterized

- **E1.1.4-C**: Stress Testing
  - Beyond-ODD scenarios tested
  - Graceful degradation demonstrated
  - No catastrophic failures observed

- **E1.1.4-D**: Independent Validation
  - IV&V team tested model independently
  - Confirmed performance claims
  - No discrepancies found

**Argument**:
```
Test performance meets requirements [E1.1.4-A]
    AND
Corner cases handled safely [E1.1.4-B]
    AND
Stress tests show graceful degradation [E1.1.4-C]
    AND
Independent validation confirms [E1.1.4-D]
    THEREFORE
Model performance is adequate
```

#### 3.2.5 Integration Safety Assessed (G1.1.5)

**Claim**: NN safely integrated into aircraft systems

**Evidence**:
- **E1.1.5-A**: Integration Safety Assessment
  - Interface hazard analysis
  - Integration testing results
  - No new hazards introduced

- **E1.1.5-B**: Hardware-in-Loop Testing
  - Full system tested with actual hardware
  - 1000+ hours HIL testing
  - No integration issues

- **E1.1.5-C**: Pilot-in-Loop Testing
  - Crew tested NN in simulator
  - Workload acceptable
  - No usability issues

**Argument**:
```
Integration hazards addressed [E1.1.5-A]
    AND
HIL testing successful [E1.1.5-B]
    AND
PIL testing successful [E1.1.5-C]
    THEREFORE
Integration is safe
```

---

## 4. SUB-CLAIM 2: HAZARDS MITIGATED

### 4.1 Claim

**G1.2: All Identified Hazards are Adequately Addressed**

### 4.2 Argument

**S1.2: Argue over hazard analysis process**

```
G1.2: Hazards Adequately Addressed
    ↓ [S1.2: Hazard analysis]
    ├─ G1.2.1: Hazards Comprehensively Identified
    ├─ G1.2.2: Severity Appropriately Classified
    ├─ G1.2.3: Mitigation Strategies Effective
    └─ G1.2.4: Residual Risk Acceptable
```

#### 4.1.1 Hazards Comprehensively Identified (G1.2.1)

**Evidence**:
- **E1.2.1-A**: Functional Hazard Assessment (FHA)
  - 20 system-level hazards identified
  - NN-specific hazards considered
  - Independent review conducted

- **E1.2.1-B**: Failure Modes and Effects Analysis (FMEA)
  - Component-level failure modes analyzed
  - 25+ failure modes documented
  - Effects on aircraft assessed

- **E1.2.1-C**: Common Cause Analysis (CCA)
  - Training data common causes identified
  - Architecture common causes identified
  - Environmental common causes identified

- **E1.2.1-D**: Lessons Learned Review
  - Industry AI/ML incidents reviewed
  - Relevant hazards incorporated
  - Novel hazards specific to AMPEL360 added

**Argument**:
```
FHA completed [E1.2.1-A]
    AND
FMEA completed [E1.2.1-B]
    AND
CCA completed [E1.2.1-C]
    AND
Lessons learned incorporated [E1.2.1-D]
    THEREFORE
Hazard identification is comprehensive
```

#### 4.1.2 Mitigation Strategies Effective (G1.2.3)

**Evidence**:
- **E1.2.3-A**: Safety Architecture
  - Multi-layer defense implemented
  - Independent safety monitors
  - Redundancy for DAL A systems

- **E1.2.3-B**: Fault Injection Testing
  - Safety monitors tested with injected faults
  - >99% detection rate achieved
  - False alarm rate <0.01/FH

- **E1.2.3-C**: Fault Tree Analysis (FTA)
  - Quantitative probability calculations
  - Mitigation effectiveness demonstrated
  - Combined probability meets objectives

**Argument**:
```
Defense-in-depth architecture [E1.2.3-A]
    AND
Safety monitors effective [E1.2.3-B]
    AND
Quantitative analysis shows adequacy [E1.2.3-C]
    THEREFORE
Mitigations are effective
```

#### 4.1.3 Residual Risk Acceptable (G1.2.4)

**Evidence**:
- **E1.2.4-A**: Quantitative Risk Assessment
  - Catastrophic events: <10⁻⁹/FH
  - Hazardous events: <10⁻⁷/FH
  - Meets DAL requirements

- **E1.2.4-B**: ALARP Demonstration
  - Further risk reduction impractical
  - Cost vs. benefit analysis
  - Best practices applied

**Argument**:
```
Quantitative targets met [E1.2.4-A]
    AND
Risk reduced to ALARP [E1.2.4-B]
    THEREFORE
Residual risk is acceptable
```

---

## 5. SUB-CLAIM 3: REQUIREMENTS MET

### 5.1 Claim

**G1.3: All Safety Requirements Met and Verified**

### 5.2 Argument

**S1.3: Argue over requirement categories**

```
G1.3: Requirements Met and Verified
    ↓ [S1.3: Requirement categories]
    ├─ G1.3.1: Functional Requirements Met
    ├─ G1.3.2: Performance Requirements Met
    ├─ G1.3.3: Safety Requirements Met
    └─ G1.3.4: Human Factors Requirements Met
```

#### 5.2.1 Safety Requirements Met (G1.3.3)

**Evidence**:
- **E1.3.3-A**: Safety Requirements Traceability Matrix
  - 15 top-level safety requirements
  - 40+ derived requirements
  - All requirements traced to verification

- **E1.3.3-B**: Verification Results
  - Test reports for each requirement
  - All requirements verified
  - No open issues

- **E1.3.3-C**: Independent Verification
  - IV&V team verified requirements
  - No discrepancies
  - Certification authority reviewed

**Argument**:
```
All requirements traced [E1.3.3-A]
    AND
All requirements verified [E1.3.3-B]
    AND
Independent verification confirms [E1.3.3-C]
    THEREFORE
Safety requirements are met
```

---

## 6. SUB-CLAIM 4: OPERATIONAL SAFETY

### 6.1 Claim

**G1.4: Operational Safety is Maintained Throughout Service Life**

### 6.2 Argument

**S1.4: Argue over operational lifecycle**

```
G1.4: Operational Safety Maintained
    ↓ [S1.4: Operational lifecycle]
    ├─ G1.4.1: Runtime Monitoring Effective
    ├─ G1.4.2: Crew Trained and Competent
    ├─ G1.4.3: Maintenance Adequate
    └─ G1.4.4: Continuous Improvement Active
```

#### 6.2.1 Runtime Monitoring Effective (G1.4.1)

**Evidence**:
- **E1.4.1-A**: Monitoring System Design
  - Three-layer monitoring architecture
  - Independent safety monitors
  - Anomaly detection algorithms

- **E1.4.1-B**: Monitoring Effectiveness Testing
  - Fault injection: >99% detection
  - False alarm rate: <0.01/FH
  - Detection latency: <100ms

- **E1.4.1-C**: Operational Monitoring Data
  - [X] flight hours monitored
  - [Y] anomalies detected and resolved
  - No undetected NN failures

**Argument**:
```
Comprehensive monitoring implemented [E1.4.1-A]
    AND
Monitoring effectiveness validated [E1.4.1-B]
    AND
Operational data confirms effectiveness [E1.4.1-C]
    THEREFORE
Runtime monitoring is effective
```

#### 6.2.2 Crew Trained and Competent (G1.4.2)

**Evidence**:
- **E1.4.2-A**: Training Program
  - Ground school (5 hours)
  - Simulator training (6 hours)
  - Line training (10 hours)
  - Recurrent training (annual)

- **E1.4.2-B**: Training Effectiveness
  - Pilot proficiency assessments
  - >90% pass rate
  - Competency demonstrated

- **E1.4.2-C**: Crew Feedback
  - Post-training surveys
  - Satisfaction >4/5
  - Confidence in NN systems

**Argument**:
```
Comprehensive training program [E1.4.2-A]
    AND
Training effectiveness demonstrated [E1.4.2-B]
    AND
Crew feedback positive [E1.4.2-C]
    THEREFORE
Crew is competent to operate NN systems
```

#### 6.2.3 Continuous Improvement Active (G1.4.4)

**Evidence**:
- **E1.4.4-A**: Operational Data Collection
  - All NN operations logged
  - Data analyzed quarterly
  - Trends identified

- **E1.4.4-B**: Incident Investigation Process
  - All NN anomalies investigated
  - Root cause analysis performed
  - Corrective actions implemented

- **E1.4.4-C**: Model Update Process
  - Periodic revalidation
  - Model updates when needed
  - Fleet-wide deployment process

**Argument**:
```
Operational data monitored [E1.4.4-A]
    AND
Incidents investigated and corrected [E1.4.4-B]
    AND
Model updates deployed as needed [E1.4.4-C]
    THEREFORE
Continuous improvement is active
```

---

## 7. CONFIDENCE ARGUMENT

### 7.1 Confidence in Evidence

**Claim**: The evidence supporting safety claims is trustworthy

**Factors**:

1. **Independence**: Evidence from independent sources
   - IV&V team separate from development
   - Independent safety assessor
   - Certification authority review

2. **Diversity**: Multiple types of evidence
   - Analysis (FHA, FMEA, FTA)
   - Testing (unit, integration, system, HIL, PIL)
   - Operational data
   - Expert review

3. **Currency**: Evidence is up-to-date
   - Revalidation every [time period]
   - Operational data current
   - Reflects latest system configuration

4. **Completeness**: Evidence covers all claims
   - Traceability matrix complete
   - No gaps in argumentation
   - All assumptions documented

### 7.2 Argument

```
Evidence is independent [Multiple independent sources]
    AND
Evidence is diverse [Analysis + Testing + Operations + Review]
    AND
Evidence is current [Regular updates]
    AND
Evidence is complete [Full traceability]
    THEREFORE
Evidence is trustworthy
    THEREFORE
Safety argument is sound
```

---

## 8. ASSUMPTIONS AND LIMITATIONS

### 8.1 Assumptions

**A1: Operational Design Domain Respected**
- Assumption: Aircraft operated within certified ODD
- Justification: Crew procedures, ODD monitoring
- Mitigation if violated: OOD detection, fallback to conventional

**A2: Maintenance Performed per Schedule**
- Assumption: NN systems maintained per AMM
- Justification: Airline quality systems
- Mitigation if violated: BIT detects degradation

**A3: Crew Training Current**
- Assumption: Crew trained and proficient
- Justification: Airline training programs, regulatory oversight
- Mitigation if violated: Proficiency checks, recurrent training

**A4: Software Configuration Controlled**
- Assumption: Only certified software versions loaded
- Justification: Configuration management, startup BIT
- Mitigation if violated: Checksum verification, version control

### 8.2 Limitations

**L1: Test Coverage Not 100%**
- Cannot test all possible scenarios
- Mitigation: Extensive testing (>10M cases), operational monitoring

**L2: Emergent Behavior Possible**
- NN may behave unexpectedly in novel scenarios
- Mitigation: OOD detection, safety monitors, crew oversight

**L3: Adversarial Attacks Possible**
- Determined attacker may craft malicious inputs
- Mitigation: Input sanitization, anomaly detection, security measures

---

## 9. CERTIFICATION STRATEGY

### 9.1 Means of Compliance

**Regulatory Basis**:
- EASA CS 25.1309: Equipment, systems, and installations
- FAA 14 CFR 25.1309: Same
- EASA AI Roadmap (ML applications)
- FAA AI Assurance Framework

**Compliance Approach**:
- Safety case as primary means of compliance
- Supported by traditional analyses (FHA, FMEA, FTA)
- Extended for AI/ML-specific considerations
- Test evidence demonstrating safety objectives met

### 9.2 Certification Evidence Package

**Submitted Documents**:
1. Safety Assessment Report (this document)
2. FHA, FMEA, FTA, CCA reports
3. Test reports (unit, integration, system, HIL, PIL)
4. Model Card and Dataset Card
5. Training program documentation
6. Operational procedures (FCOM, AMM, MEL)
7. Configuration management plan
8. Continuous monitoring plan

### 9.3 Authority Engagement

**Milestones**:
1. Certification Plan submitted and accepted
2. Design Review (architecture, safety monitors)
3. Test Witnessing (selected tests observed by authority)
4. Pre-Certification Review (evidence package review)
5. Type Certificate issuance
6. Post-Certification Monitoring (ongoing)

---

**Document Control**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-04 | AMPEL360 Safety Team | Initial release |

**Classification**: Safety Critical  
**Next Review**: 2025-02-04 (Quarterly)
