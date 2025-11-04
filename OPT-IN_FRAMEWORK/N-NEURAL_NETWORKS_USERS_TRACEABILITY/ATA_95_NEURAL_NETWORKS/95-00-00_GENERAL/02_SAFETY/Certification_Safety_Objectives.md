# Certification Safety Objectives for Neural Network Systems

**Document ID:** AMPEL360-95-00-00-SAF-CERT  
**Version:** 1.0  
**Date:** 2025-11-04  
**Classification:** Safety Critical

---

## 1. INTRODUCTION

### 1.1 Purpose

This document defines the certification strategy and safety objectives for neural network systems in the AMPEL360 aircraft, ensuring compliance with applicable airworthiness regulations.

### 1.2 Regulatory Basis

**EASA Requirements**:
- CS-25: Large Aeroplanes
- CS 25.1309: Equipment, systems, and installations
- AMC 20-115C: Airborne Software
- EASA AI Roadmap (Machine Learning Applications)

**FAA Requirements**:
- 14 CFR Part 25: Airworthiness Standards
- 14 CFR 25.1309: Equipment, systems, and installations  
- AC 20-115D: Airborne Software Assurance
- FAA AI Assurance Framework (Draft)

**EU Regulations**:
- EU AI Act: High-Risk AI Systems requirements

---

## 2. SAFETY OBJECTIVES BY DAL

### 2.1 Design Assurance Level (DAL) Assignment

| NN System | Function | Failure Condition | DAL | Probability Objective |
|-----------|----------|------------------|-----|----------------------|
| Primary Flight Control NN | Control augmentation | Catastrophic | A | <10⁻⁹ per FH |
| Collision Avoidance NN | Traffic separation | Hazardous | B | <10⁻⁷ per FH |
| Navigation NN | Position estimation | Hazardous | B | <10⁻⁷ per FH |
| Fuel Cell Optimization NN | Power management | Major | C | <10⁻⁵ per FH |
| Route Planning NN | Flight efficiency | Minor | D | <10⁻³ per FH |
| Predictive Maintenance NN | Maintenance scheduling | No Effect | E | None |

### 2.2 Safety Objectives for DAL A Systems

**Applicable to**: Primary Flight Control NN

**Objective SO-A-001**: System failures shall not prevent continued safe flight and landing
- **Requirement**: No single point of failure
- **Compliance**: Dual redundant NN + independent safety monitor
- **Verification**: Fault injection testing, FMEA

**Objective SO-A-002**: Probability of catastrophic failure <10⁻⁹ per flight hour
- **Requirement**: Quantitative probabilistic analysis
- **Compliance**: FTA with conservative assumptions + multiple barriers
- **Verification**: Probability calculation validated by independent assessor

**Objective SO-A-003**: Hardware redundancy with dissimilar monitoring
- **Requirement**: Independent safety monitor using conventional algorithm
- **Compliance**: NN on GPU, monitor on separate CPU, different algorithms
- **Verification**: Independence analysis, fault injection

**Objective SO-A-004**: Graceful degradation to safe conventional mode
- **Requirement**: Automatic failover within 1 second
- **Compliance**: Degradation state machine with smooth transitions
- **Verification**: Degradation scenario testing

**Objective SO-A-005**: Crew override capability
- **Requirement**: Manual control takes precedence, <2 sec activation
- **Compliance**: Override switch/yoke force threshold
- **Verification**: PIL simulation, override timing tests

### 2.3 Safety Objectives for DAL B Systems

**Applicable to**: Collision Avoidance NN, Navigation NN, Propulsion Optimization NN

**Objective SO-B-001**: Hazardous failures extremely improbable (<10⁻⁷ per FH)
- **Requirement**: Quantitative analysis demonstrates probability objective
- **Compliance**: Testing + safety monitor + crew oversight
- **Verification**: FTA, test-based probability estimation

**Objective SO-B-002**: Independent safety monitoring
- **Requirement**: Conventional algorithm monitors NN outputs
- **Compliance**: Separate processor, diverse algorithm
- **Verification**: Monitor effectiveness testing (>99% detection)

**Objective SO-B-003**: Operational Design Domain (ODD) enforcement
- **Requirement**: Detect and handle out-of-distribution inputs
- **Compliance**: OOD detection algorithm, boundary warnings
- **Verification**: OOD detection coverage testing

**Objective SO-B-004**: Performance monitoring and degradation detection
- **Requirement**: Real-time tracking of NN performance metrics
- **Compliance**: Statistical process control, drift detection
- **Verification**: Monitoring system functional testing

**Objective SO-B-005**: Crew awareness and override
- **Requirement**: Clear status indication, manual override available
- **Compliance**: Dedicated displays, override procedures
- **Verification**: Human factors testing, PIL simulation

### 2.4 Safety Objectives for DAL C Systems

**Applicable to**: Fuel Cell Optimization NN, Structural Health Monitoring NN

**Objective SO-C-001**: Major failures remote (<10⁻⁵ per FH)
- **Requirement**: Analysis demonstrates low failure probability
- **Compliance**: Testing + safety limits + conventional backup
- **Verification**: Test-based probability, limit protection testing

**Objective SO-C-002**: Safety envelopes enforced
- **Requirement**: NN outputs bounded by safety limits
- **Compliance**: Independent limit checking
- **Verification**: Boundary testing, fault injection

**Objective SO-C-003**: Performance validation
- **Requirement**: Accuracy and reliability demonstrated
- **Compliance**: >100,000 test cases, accuracy >95%
- **Verification**: Test reports, validation datasets

---

## 3. AI/ML-SPECIFIC CERTIFICATION OBJECTIVES

### 3.1 Training Data Objectives

**Objective ML-001**: Training data is representative of operational environment
- **Requirement**: Coverage >99% of operational design domain
- **Compliance**: Dataset statistics, expert review
- **Verification**: Coverage analysis, distribution comparison

**Objective ML-002**: Training data is free from significant bias
- **Requirement**: No systematic errors >5% in any operational category
- **Compliance**: Bias testing across operational factors
- **Verification**: Fairness metrics, subgroup analysis

**Objective ML-003**: Training data quality is validated
- **Requirement**: Label accuracy >99%, outliers removed
- **Compliance**: Multi-annotator consensus, expert validation
- **Verification**: Quality audit, error analysis

**Objective ML-004**: Training data provenance is documented
- **Requirement**: Source, collection method, preprocessing documented
- **Compliance**: Data cards, traceability
- **Verification**: Documentation review

### 3.2 Model Development Objectives

**Objective ML-005**: Model architecture is justified and appropriate
- **Requirement**: Architecture selection documented and reviewed
- **Compliance**: Trade study, expert review
- **Verification**: Architecture review meeting

**Objective ML-006**: Training process is controlled and reproducible
- **Requirement**: Hyperparameters fixed, process documented
- **Compliance**: Training pipeline version controlled
- **Verification**: Independent re-training achieves similar performance

**Objective ML-007**: Model performance meets requirements
- **Requirement**: Accuracy thresholds per DAL (A: >99.9%, B: >99%, C: >95%)
- **Compliance**: Extensive testing on validation sets
- **Verification**: Test reports, independent validation

**Objective ML-008**: Corner cases and edge scenarios tested
- **Requirement**: >1000 edge cases tested for DAL A/B systems
- **Compliance**: Corner case test suite
- **Verification**: Corner case test results

**Objective ML-009**: Behavior beyond ODD characterized
- **Requirement**: Stress testing demonstrates graceful degradation
- **Compliance**: Beyond-ODD test scenarios
- **Verification**: Stress test reports

### 3.3 Runtime Assurance Objectives

**Objective ML-010**: Confidence estimation is calibrated
- **Requirement**: Confidence aligns with actual accuracy (±10%)
- **Compliance**: Calibration testing and tuning
- **Verification**: Calibration curves, reliability diagrams

**Objective ML-011**: OOD detection is effective
- **Requirement**: >99% detection of true OOD inputs, <1% false positives
- **Compliance**: OOD detector algorithm validated
- **Verification**: OOD detection testing

**Objective ML-012**: Performance degradation is detected
- **Requirement**: >5% accuracy drop detected within 100 cycles
- **Compliance**: Statistical process control
- **Verification**: Degradation detection testing

**Objective ML-013**: Adversarial robustness demonstrated
- **Requirement**: Resilient to adversarial attacks in threat model
- **Compliance**: Adversarial training, input validation
- **Verification**: Adversarial testing

### 3.4 Explainability Objectives

**Objective ML-014**: Safety-critical decisions are explainable
- **Requirement**: Explanation available for DAL A/B/C decisions
- **Compliance**: Explainability algorithms (SHAP, LIME, attention)
- **Verification**: Explanation quality assessment, crew comprehension testing

**Objective ML-015**: Explanations support incident investigation
- **Requirement**: Post-flight reconstruction of NN decisions
- **Compliance**: FDR integration, explanation logging
- **Verification**: Reconstruction testing

---

## 4. VERIFICATION AND VALIDATION APPROACH

### 4.1 V&V Strategy

```
Level 5: Operational Validation
    ↓ [Flight test, early service]
Level 4: System Integration Testing
    ↓ [HIL, PIL, full mission simulation]
Level 3: System Testing
    ↓ [NN + monitors + interfaces]
Level 2: Subsystem Testing
    ↓ [NN alone, safety monitor alone]
Level 1: Component Testing
    ↓ [Model validation, unit tests]
```

### 4.2 Test Requirements by DAL

| Test Category | DAL A | DAL B | DAL C | DAL D | DAL E |
|--------------|-------|-------|-------|-------|-------|
| Nominal test cases | >10M | >10M | >100K | >10K | >1K |
| Corner case tests | >1K | >1K | >100 | >10 | Optional |
| Stress tests (beyond ODD) | Required | Required | Required | Optional | Optional |
| Adversarial tests | Required | Required | Optional | Optional | Optional |
| Long-duration tests (hours) | >1000 | >100 | >10 | Optional | Optional |
| HIL testing (hours) | >100 | >10 | >1 | Optional | Optional |
| PIL testing (hours) | >10 | >5 | >1 | Optional | Optional |

### 4.3 Independent Verification & Validation (IV&V)

**Objective**: Provide independent assessment of NN safety

**Scope**:
- All DAL A and B systems require IV&V
- DAL C systems recommended
- IV&V team separate from development team

**Activities**:
- Independent testing on different test sets
- Code review of inference software
- Architecture review
- Training process review
- Safety analysis review

**Deliverable**: IV&V report confirming safety objectives met or identifying issues

---

## 5. CONFIGURATION MANAGEMENT

### 5.1 Configuration Items

**Software**:
- Inference code (C++, Python, etc.)
- ML framework version (TensorFlow, PyTorch)
- Compiler version and options
- Operating system and libraries

**Data**:
- Trained model weights (binary file)
- Model architecture definition
- Training dataset (or representative subset)
- Validation dataset

**Documentation**:
- Model card
- Dataset card
- Training process documentation
- Test reports

### 5.2 Version Control

**Requirement**: All configuration items version controlled

**Implementation**:
- Git for code
- DVC (Data Version Control) for models and datasets
- Unique version identifier for each release
- Cryptographic checksums for model files

**Verification**: Configuration audit, checksum verification at startup

### 5.3 Change Control

**Process**:
1. Change request submitted
2. Impact analysis (safety, performance, certification)
3. Approval by change board
4. Implementation and testing
5. Regression testing (ensure no negative impacts)
6. Certification authority notification (if applicable)
7. Deployment

**Certification Impact**:
- Minor changes (bug fixes, performance tuning): May not require recertification
- Major changes (architecture, training data): Require recertification
- Determination made by certification authority

---

## 6. OPERATIONAL APPROVAL

### 6.1 Flight Test Program

**Objectives**:
- Validate NN performance in actual operational environment
- Verify safety monitors effective
- Confirm crew procedures adequate
- Identify any unforeseen issues

**Test Phases**:

1. **Ground Tests** (100 hours):
   - Engine runs with NN systems active
   - Taxi tests
   - High-speed taxi

2. **Flight Tests** (50 hours):
   - Initial flights with NN advisory only
   - Progressive increase in NN authority
   - Nominal and off-nominal scenarios
   - Degradation scenarios
   - Emergency procedures

3. **Early Service** (500 hours):
   - Limited revenue flights under special conditions
   - Enhanced monitoring
   - Rapid feedback loop

**Success Criteria**:
- No safety events attributable to NN
- NN performance meets predictions
- Crew feedback positive
- Safety monitors effective

### 6.2 Crew Training and Licensing

**Training Program Approval**:
- Curriculum submitted to authority
- Instructor qualifications verified
- Training devices (simulators) approved

**Pilot Type Rating**:
- May require type rating with NN endorsement
- Demonstrated proficiency in NN operations
- Demonstrated proficiency in manual operations (without NN)

---

## 7. CONTINUED OPERATIONAL SAFETY

### 7.1 Post-Certification Monitoring

**Requirements**:
- Continuous monitoring of NN operational performance
- Anomaly reporting system
- Trend analysis
- Periodic safety assessments

**Reporting to Authority**:
- Quarterly operational reports
- Immediate reporting of safety events
- Annual safety review

### 7.2 Model Updates

**Process**:
1. Trigger (performance degradation, new data available, bug fix)
2. Develop updated model
3. Verification testing (same as original)
4. Safety impact analysis
5. Authority approval (if required)
6. Fleet-wide deployment

**Certification Considerations**:
- Minor updates: May not require recertification
- Major updates: Require recertification or amended TC
- Determination by authority

### 7.3 Safety Bulletins

**Issuance Criteria**:
- New NN limitation discovered
- Operational procedure change needed
- Software/hardware issue identified

**Distribution**:
- All operators
- Certification authorities
- Training organizations

---

## 8. COMPLIANCE MATRIX

### 8.1 CS 25.1309 / 14 CFR 25.1309 Compliance

| Requirement | Compliance Means | Evidence |
|-------------|-----------------|----------|
| (a) Equipment and systems shall be designed... | Safety analysis (FHA, FMEA, FTA, CCA) | Safety assessment reports |
| (b) Probability requirements for failure conditions | Quantitative FTA, test-based probabilities | FTA report, test reports |
| (c) Warning information provided to crew | Alerts and displays designed per human factors | PIL test report, interface specification |
| (d) Analysis considers single failures, combinations, and common causes | FMEA for single failures, CCA for common causes | FMEA report, CCA report |

### 8.2 AMC 20-115C (Software) Compliance

**DO-178C Objectives Extended for ML**:

| DO-178C Objective | ML Extension | Evidence |
|------------------|--------------|----------|
| Software Plans | Include ML-specific plans (data, training) | ML Development Plan |
| Software Requirements | Include ODD, performance, explainability | Requirements Specification |
| Software Design | Document NN architecture, training process | Design Documentation |
| Software Implementation | Code + trained weights | Source code, model files |
| Software Testing | Testing + dataset validation + bias analysis | Test reports, dataset validation |
| Software Configuration Management | Model and dataset versioning | CM plan, version control audit |
| Software Quality Assurance | Independent validation, adversarial testing | IV&V report, adversarial test report |

### 8.3 EU AI Act Compliance

**High-Risk AI System Requirements**:

| Requirement | Compliance | Evidence |
|-------------|-----------|----------|
| Risk management system | Safety assessment process | Safety assessment reports |
| Data governance | Dataset validation, quality control | Dataset card, quality audit |
| Technical documentation | Comprehensive documentation | Complete documentation package |
| Record-keeping | Logging of operations and decisions | FDR integration, log files |
| Transparency | Explainability, information to users | Explainability implementation, FCOM |
| Human oversight | Crew override, monitoring | Human factors analysis, PIL tests |
| Accuracy, robustness, cybersecurity | Testing and validation | Test reports, security analysis |

---

## 9. CERTIFICATION SCHEDULE

### 9.1 Milestones

| Milestone | Target Date | Deliverables | Authority Review |
|-----------|------------|--------------|------------------|
| Certification Plan | Month 0 | CP document | Authority acceptance |
| System Design Review | Month 12 | Design docs, preliminary safety analysis | Design approval |
| Test Plan Review | Month 18 | Test plans | Test plan acceptance |
| Completion of Testing | Month 30 | Test reports | Test witnessing |
| Pre-Certification Review | Month 33 | Complete evidence package | Evidence review |
| Type Certificate | Month 36 | TC issuance | TC granted |
| Entry Into Service | Month 37 | Operational approval | Operations authorization |

### 9.2 Authority Engagement

**Planned Interactions**:
- Monthly telecons with certification team
- Quarterly in-person meetings
- Test witnessing for critical tests (FHA, corner cases, PIL)
- Pre-certification review meeting

---

**Document Control**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-04 | AMPEL360 Safety Team | Initial release |

**Classification**: Safety Critical  
**Next Review**: 2025-02-04 (Quarterly)
