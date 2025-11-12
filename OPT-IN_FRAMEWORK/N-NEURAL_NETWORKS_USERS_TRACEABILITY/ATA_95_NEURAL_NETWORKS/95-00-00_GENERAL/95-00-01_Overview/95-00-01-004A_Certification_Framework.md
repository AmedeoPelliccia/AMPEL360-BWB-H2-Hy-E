# ATA 95 - Neural Networks Systems
## Certification Framework

**Document ID:** AMPEL360-95-00-00-OVR-CF  
**Version:** 1.0  
**Date:** 2025-11-04  
**Classification:** Regulatory Compliance

---

## 1. INTRODUCTION

This document establishes the certification framework for neural network systems integrated into the AMPEL360 BWB H2 Hy-E Q100 INTEGRA aircraft, ensuring compliance with international aviation regulations and standards while addressing the unique characteristics of AI/ML systems.

---

## 2. REGULATORY LANDSCAPE

### 2.1 Primary Regulatory Authorities

#### 2.1.1 European Union Aviation Safety Agency (EASA)
- **Primary Regulation**: CS-25 (Large Aeroplanes)
- **AI Guidance**: EASA AI Roadmap 2.0 (2024)
- **Concept Paper**: "Artificial Intelligence in Aviation" (CON-01)
- **Acceptable Means of Compliance**: AMC 25-19 (Software)
- **Status**: Active, with ongoing ML-specific amendments

#### 2.1.2 Federal Aviation Administration (FAA)
- **Primary Regulation**: 14 CFR Part 25
- **AI Framework**: FAA AI Assurance Framework (2024)
- **Policy Statement**: PS-AIR-25-11 (Machine Learning Systems)
- **Advisory Circular**: AC 20-115D (Software Certification)
- **Status**: Draft guidance under review

#### 2.1.3 International Civil Aviation Organization (ICAO)
- **Standards**: Annex 6 (Aircraft Operations)
- **Guidance**: Doc 10019 (Manual on Remotely Piloted Aircraft Systems)
- **AI Working Group**: Panel on Artificial Intelligence in Aviation
- **Status**: Development of AI-specific SARPs

### 2.2 Cross-Jurisdictional Compliance

The AMPEL360 certification strategy targets simultaneous EASA and FAA approval through:
- Harmonized certification basis
- Joint authority participation in key milestones
- Mutual recognition agreements where applicable
- Transparent sharing of certification evidence

---

## 3. STANDARDS AND GUIDANCE

### 3.1 Software and Hardware Standards

#### DO-178C: Software Considerations in Airborne Systems

**Standard Application to ML Systems:**

| Objective | Traditional Software | ML Extension | Rationale |
|-----------|---------------------|--------------|-----------|
| Requirements Traceability | Source code to requirements | Training data + model to requirements | Data is part of specification |
| Source Code Testing | Statement/branch coverage | Neuron activation coverage | Coverage metrics adapted |
| Dead Code Elimination | Remove unused functions | Prune unused pathways | Similar concept, different implementation |
| Verification Testing | Deterministic test cases | Statistical test distribution | ML outputs are probabilistic |
| Configuration Management | Code version control | Model + data versioning | Data versioning added |

**DAL-Specific Compliance:**

- **DAL A (Catastrophic)**: Full DO-178C + ML supplements, 100% coverage
- **DAL B (Hazardous)**: Modified DO-178C objectives + ML validation
- **DAL C (Major)**: Reduced rigor with ML-specific testing
- **DAL D (Minor)**: Functional testing with performance validation

#### DO-254: Design Assurance Guidance for Airborne Electronic Hardware

**Application to Neural Processing Hardware:**

- **FPGA/ASIC Design**: Full DO-254 compliance for custom NN accelerators
- **COTS GPUs/TPUs**: Service experience + qualification testing
- **Safety Monitoring**: Independent hardware monitors per DO-254
- **Environmental Testing**: Extended for AI processor thermal profiles

#### DO-200B: Standards for Processing Aeronautical Data

**Relevance to ML Training Data:**

- **Data Quality**: Type 1 (flight-critical) data requirements applied
- **Data Integrity**: Cryptographic verification of training datasets
- **Data Currency**: Expiration and update requirements
- **Data Provenance**: Complete source documentation required

### 3.2 Safety Assessment Standards

#### ARP4761: Guidelines and Methods for Safety Assessment

**ML-Specific Extensions:**

```
Traditional FHA Process          ML-Enhanced Process
      ↓                                ↓
Functional Definition      →    Functional Definition + ODD
      ↓                                ↓
Failure Conditions         →    Failure + OOD Conditions
      ↓                                ↓
Severity Classification    →    Severity + Confidence Bounds
      ↓                                ↓
Safety Requirements        →    Safety + Explainability Requirements
```

**New Hazard Categories for ML:**
- Model Degradation (gradual performance loss)
- OOD Inputs (operating outside training distribution)
- Adversarial Inputs (malicious data injection)
- Training Data Corruption
- Model Update Errors

#### ARP4754A: Guidelines for Development of Civil Aircraft and Systems

**ML Lifecycle Integration:**

| Phase | Traditional Process | ML-Specific Additions |
|-------|-------------------|----------------------|
| Requirements | Functional requirements | ODD definition, performance targets |
| Design | Architecture definition | Model architecture, training strategy |
| Implementation | Coding | Training, hyperparameter tuning |
| Verification | Testing | Validation set evaluation, corner case testing |
| Validation | System validation | Test set evaluation, real-world validation |
| Certification | Evidence compilation | Model cards, dataset cards, explainability reports |

---

## 4. EU AI ACT COMPLIANCE

### 4.1 High-Risk AI System Classification

**AMPEL360 NN Systems as High-Risk AI:**

The EU AI Act (Regulation 2024/1689) classifies aviation AI systems as high-risk under Annex III, Section 1(a): "AI systems intended to be used as safety components in the management and operation of road traffic and the supply of water, gas, heating and electricity."

**Applicable Requirements:**

1. **Risk Management System** (Article 9)
   - Continuous risk assessment throughout lifecycle
   - Risk mitigation measures documented
   - Residual risk acceptability criteria

2. **Data Governance** (Article 10)
   - Training data quality requirements
   - Bias detection and mitigation
   - Data representativeness validation

3. **Technical Documentation** (Article 11)
   - Model cards for all NN systems
   - Dataset cards with provenance
   - Intended purpose and limitations

4. **Record-Keeping** (Article 12)
   - Automatic logging of all NN decisions
   - Minimum 10-year retention for aviation
   - Audit trail accessibility

5. **Transparency** (Article 13)
   - User information about NN capabilities
   - Limitations clearly communicated
   - Confidence levels displayed

6. **Human Oversight** (Article 14)
   - Human-in-the-loop for DAL A/B systems
   - Override mechanisms always available
   - Alert systems for anomalies

7. **Accuracy, Robustness, Cybersecurity** (Article 15)
   - Performance metrics defined and monitored
   - Adversarial robustness testing
   - Secure development practices

### 4.2 Conformity Assessment

**Chosen Route: Annex VII (Internal Control + Technical Documentation)**

For aviation safety components with existing sectoral legislation (EASA CS-25):
- Internal quality management system
- Technical documentation per Article 11
- Post-market monitoring system
- Declaration of conformity with EU AI Act

---

## 5. EASA AI ROADMAP ALIGNMENT

### 5.1 EASA AI Roadmap 2.0 Phases

**Phase 1 (2020-2024): Foundation**
- ✅ Concept papers published
- ✅ Industry consultation completed
- ✅ Initial guidance materials released

**Phase 2 (2024-2027): Guidance Development** ← *Current Phase*
- Acceptable Means of Compliance (AMC) for ML
- Certification Specifications amendments
- Type Certificate application guidance

**Phase 3 (2027-2030): Implementation**
- First ML system certifications
- Lessons learned incorporation
- Regulatory framework refinement

### 5.2 EASA Trustworthiness Pillars

EASA defines five pillars for trustworthy AI in aviation:

#### Pillar 1: Explainability
- **Requirement**: All safety-relevant NN decisions must be explainable
- **AMPEL360 Approach**: SHAP/LIME for all DAL A-C systems
- **Evidence**: Explainability reports in certification package

#### Pillar 2: Traceability
- **Requirement**: Complete audit trail from data to decision
- **AMPEL360 Approach**: Seven-layer traceability framework
- **Evidence**: Digital thread documentation, blockchain ledger

#### Pillar 3: Fairness
- **Requirement**: No discrimination or bias in NN operation
- **AMPEL360 Approach**: Bias testing across diverse scenarios
- **Evidence**: Bias analysis reports, diverse test datasets

#### Pillar 4: Safety Assurance
- **Requirement**: Demonstrable safety equivalent to traditional systems
- **AMPEL360 Approach**: Safety monitoring + fallback systems
- **Evidence**: FHA, FTA, FMEA, test reports

#### Pillar 5: Resilience
- **Requirement**: Robust operation under perturbations
- **AMPEL360 Approach**: Adversarial training, OOD detection
- **Evidence**: Stress testing, adversarial testing results

---

## 6. FAA AI ASSURANCE FRAMEWORK

### 6.1 Framework Principles

The FAA AI Assurance Framework (2024) defines four assurance objectives:

#### Objective 1: Define and Document AI System
- System boundaries and interfaces
- Operational Design Domain (ODD)
- Performance requirements and limitations
- Safety analysis and mitigation

#### Objective 2: Develop AI System with Appropriate Assurance
- Data management and quality
- Model development and validation
- V&V activities
- Configuration management

#### Objective 3: Verify AI System Performance
- Requirements-based testing
- Robustness testing (OOD, adversarial)
- Safety verification
- Human factors validation

#### Objective 4: Demonstrate Continued Safety
- Runtime monitoring
- Performance degradation detection
- Update management
- Incident reporting

### 6.2 FAA Certification Approach

**Special Conditions (SC):**

Due to novel nature of ML systems, FAA will issue Special Conditions for AMPEL360 addressing:
- ML training and validation requirements
- OOD detection and handling
- Model update approval process
- Explainability requirements for safety-critical systems
- Human-machine interface requirements

**Issue Papers:**

Planned issue papers for FAA certification:
1. ML System Architecture and Safety Monitoring
2. Training Data Quality and Management
3. Model Validation and Test Coverage
4. OOD Detection and Mitigation
5. Human Factors and Crew Training
6. Model Update Process and Recertification

---

## 7. CERTIFICATION PROCESS

### 7.1 Overall Certification Timeline

```
Year 1-2: Requirements and Planning
├── Define certification basis
├── Develop Plan for Software/Hardware Aspects of Certification (PSAC/PHAC)
├── Authority engagement and agreement
└── Issue papers submission and resolution

Year 3-4: Development and Verification
├── Model training and validation
├── Requirements-based testing
├── Safety analysis (FHA, FTA, FMEA)
├── Robustness testing
└── Preliminary certification evidence

Year 5: Type Certification
├── Certification test campaigns
├── Authority witnessing of tests
├── Final certification evidence compilation
├── Type Certification review
└── Type Certificate issuance

Ongoing: Post-Certification
├── Production approval
├── Operational approval
├── Continued airworthiness
└── Model update approvals
```

### 7.2 Certification Deliverables by DAL

#### DAL A Systems

**Required Documents:**
1. Plan for Software Aspects of Certification (PSAC-ML)
2. Software Development Plan (SDP-ML)
3. Software Verification Plan (SVP-ML)
4. Software Configuration Management Plan (SCMP-ML)
5. Software Quality Assurance Plan (SQAP-ML)
6. Software Requirements Standards (SRS)
7. Software Design Standards (SDS)
8. Software Code Standards (SCS)
9. System Safety Assessment (SSA)
10. Software Accomplishment Summary (SAS-ML)
11. Model Card (detailed)
12. Dataset Card (comprehensive)
13. Explainability Report
14. Robustness Test Report
15. Human Factors Validation Report

#### DAL B Systems

**Required Documents:**
- Items 1-10 from DAL A (with reduced rigor)
- Model Card (standard)
- Dataset Card (standard)
- Safety Analysis
- Test Reports
- Human Factors Assessment

#### DAL C Systems

**Required Documents:**
- PSAC-ML (simplified)
- Development Plan
- Model Card
- Dataset Card
- Safety Analysis (reduced)
- Test Summary

#### DAL D Systems

**Required Documents:**
- Development Summary
- Model Card
- Test Results
- Basic safety assessment

---

## 8. CERTIFICATION EVIDENCE FOR ML SYSTEMS

### 8.1 Model Card Requirements

**Mandatory Sections:**

```markdown
## Model Details
- Model ID and version
- Architecture description
- Training framework and tools
- Hyperparameters
- Model size and computational requirements

## Intended Use
- Operational Design Domain (ODD)
- Aircraft systems integration
- Design Assurance Level (DAL)
- Use cases and scenarios

## Training Data
- Dataset ID and version
- Data sources and provenance
- Dataset size and characteristics
- Preprocessing and augmentation
- Bias analysis

## Performance Metrics
- Training/validation/test split
- Accuracy, precision, recall, F1
- Confidence calibration
- Worst-case performance
- Performance across diverse conditions

## Limitations
- Known failure modes
- OOD behavior
- Computational constraints
- Update constraints

## Ethical Considerations
- Fairness assessment
- Privacy protections
- Transparency measures

## Certification Status
- DAL classification
- Certification basis
- Test completion status
- Authority approval status
```

### 8.2 Dataset Card Requirements

**Mandatory Sections:**

```markdown
## Dataset Details
- Dataset ID and version
- Collection period and location
- Data types and formats
- Dataset size

## Provenance
- Data sources (sensors, simulations, operational)
- Collection methods
- Quality assurance procedures
- Chain of custody

## Preprocessing
- Cleaning procedures
- Normalization/standardization
- Augmentation techniques
- Filtering criteria

## Statistics
- Distributive properties
- Class balance
- Feature correlations
- Outlier analysis

## Bias Analysis
- Demographic representation
- Environmental condition coverage
- Edge case inclusion
- Known biases and mitigations

## Intended Use
- Training/validation/test purposes
- Applicable systems
- ODD alignment
- Restrictions

## Maintenance
- Update frequency
- Version control
- Deprecation policy
```

---

## 9. SPECIAL TOPICS

### 9.1 Model Update Certification

**Classification of Updates:**

| Update Type | Certification Required | Approval Authority | Process |
|------------|----------------------|-------------------|---------|
| **Critical** (safety issue) | Full recertification | EASA/FAA | Emergency AD process |
| **Major** (architecture change) | Partial recertification | EASA/FAA | Amended TC |
| **Minor** (hyperparameters) | Validation required | Internal DER* | Design approval |
| **Patch** (data only) | Testing required | Internal | Configuration control |

*DER = Designated Engineering Representative

**Update Approval Process:**

```
1. Change Request
   ↓
2. Impact Assessment (safety, performance, interfaces)
   ↓
3. Update Development (new model training)
   ↓
4. Verification Testing (regression + new scenarios)
   ↓
5. Certification Evidence Update
   ↓
6. Authority Approval (if required)
   ↓
7. Fleet Deployment
   ↓
8. Post-Deployment Monitoring (30 days minimum)
```

### 9.2 Continued Airworthiness

**Ongoing Monitoring Requirements:**

- **Performance Metrics**: Monthly reporting to authorities
- **Incident Reporting**: Any NN-related anomaly reportable
- **Degradation Thresholds**: Automatic alerts for performance drops >5%
- **OOD Events**: Logging and quarterly review
- **Model Drift**: Continuous monitoring with annual validation

**Airworthiness Directives (ADs):**

Potential AD triggers:
- Safety-critical NN failure or near-miss
- Systematic performance degradation
- Newly discovered OOD vulnerability
- Security vulnerability in NN system

### 9.3 Human Factors Certification

**Crew Interface Requirements:**

- **Display Design**: Follows human-centered design principles
- **Alerting Philosophy**: Consistent with CS 25.1322
- **Workload Assessment**: NASA-TLX or similar methodology
- **Training Requirements**: Documented in Type Rating
- **Override Mechanisms**: Intuitive and always accessible

**Certification Tests:**

- Simulator validation with representative crew
- Workload assessment across normal and abnormal procedures
- Usability testing with diverse pilot population
- Training effectiveness validation

---

## 10. CERTIFICATION COST AND SCHEDULE

### 10.1 Estimated Certification Costs

| Activity | DAL A System | DAL B System | DAL C System |
|----------|-------------|--------------|--------------|
| Certification Planning | $200K | $100K | $50K |
| Development Assurance | $2M | $1M | $400K |
| Testing and Validation | $3M | $1.5M | $600K |
| Safety Analysis | $500K | $300K | $150K |
| Documentation | $400K | $200K | $80K |
| Authority Fees | $100K | $75K | $40K |
| **Total per System** | **$6.2M** | **$3.2M** | **$1.3M** |

**AMPEL360 Total Certification (24 NN systems):**
- 2 × DAL A = $12.4M
- 10 × DAL B = $32M
- 9 × DAL C = $11.7M
- 3 × DAL D = $0.9M ($300K each)
- **Total: ~$57M** (ATA 95 NN certification component)

### 10.2 Certification Schedule

**Critical Path Activities:**

```
Months 1-6: Certification Basis Agreement
Months 6-24: Development with Authority Oversight
Months 24-48: Verification and Validation
Months 48-54: Certification Testing
Months 54-60: Authority Review and Approval
```

**Parallelization Opportunities:**

- Multiple NN systems certified concurrently
- Ground testing while flight test aircraft prepared
- Simulation validation before flight tests
- Documentation development throughout

---

## 11. INTERNATIONAL HARMONIZATION

### 11.1 Bilateral Aviation Safety Agreements (BASA)

**EASA-FAA Technical Implementation Procedures (TIP):**
- Mutual acceptance of certification findings
- Joint participation in key milestones
- Harmonized Special Conditions where possible
- Shared test data and analysis

### 11.2 Other Authorities

**Transport Canada Civil Aviation (TCCA):**
- Recognition through BASA with EASA
- Canadian-specific Special Conditions if required

**Civil Aviation Administration of China (CAAC):**
- Separate validation process
- Additional documentation in Chinese
- China-specific operational validation

**Other Jurisdictions:**
- Case-by-case validation based on export plans

---

## 12. EMERGING REGULATORY DEVELOPMENTS

### 12.1 Standards Under Development

**EUROCAE WG-114: AI Assurance**
- DO-356: AI Assurance Guidance (expected 2026)
- ED-XXX: NN System Certification (in development)

**SAE G-34: Artificial Intelligence in Aviation**
- ARP-XXXX: AI System Safety Assessment (draft)
- ARP-XXXX: ML Test and Evaluation Methods (draft)

**ISO/IEC JTC 1/SC 42: Artificial Intelligence**
- ISO/IEC 5338: AI Lifecycle (published 2023)
- ISO/IEC 42001: AI Management System (published 2023)

### 12.2 Future Regulatory Trends

**Anticipated Regulatory Changes (2025-2030):**

- Standardization of ML certification approaches
- Harmonized international guidance
- Streamlined update approval processes
- Risk-based certification (less prescriptive)
- Industry best practices recognition

---

## 13. DOCUMENT CONTROL

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-09-20 | Certification Lead | Initial framework draft |
| 0.5 | 2025-10-25 | Regulatory Affairs | EU AI Act integration |
| 1.0 | 2025-11-04 | Chief Engineer | Released version |

**Document Status:** ✅ RELEASED  
**Next Review:** 2026-05-04 (Semi-annual)  
**Approved By:** Chief Engineer - AI Systems, Certification Lead, Legal

---

## 14. REFERENCES

### 14.1 Regulatory Documents

- EASA CS-25 Amendment 27 (2023)
- EASA AI Roadmap 2.0 (2024)
- EASA CON-01: Artificial Intelligence Concept Paper (2024)
- FAA 14 CFR Part 25
- FAA AI Assurance Framework (2024)
- EU AI Act (Regulation 2024/1689)

### 14.2 Standards

- DO-178C: Software Considerations in Airborne Systems (2012)
- DO-254: Design Assurance Guidance for Airborne Electronic Hardware (2000)
- DO-200B: Standards for Processing Aeronautical Data (1998)
- ARP4761: Guidelines and Methods for Safety Assessment (1996)
- ARP4754A: Guidelines for Development of Civil Aircraft and Systems (2010)

### 14.3 Industry Guidance

- EASA AMC 20-115D: Airborne Software Certification (2024)
- FAA AC 20-115D: Airborne Software Assurance (2024)
- SAE ARP5150: Safety Assessment of Transport Airplanes (1993)

---

**Related Documents:**
- ATA_95_Purpose_Scope.md
- Applicability_Matrix.md
- Traceability_Requirements.md
- Interface_Documentation.md
- User_Accountability_Model.md
