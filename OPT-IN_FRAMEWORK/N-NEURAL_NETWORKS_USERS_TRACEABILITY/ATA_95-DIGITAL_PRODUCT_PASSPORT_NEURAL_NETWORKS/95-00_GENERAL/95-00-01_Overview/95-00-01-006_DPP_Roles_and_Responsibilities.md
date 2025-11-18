# 95-00-01-006 — DPP Roles and Responsibilities

**Document ID**: 95-00-01-006  
**Version**: 1.0  
**Date**: 2025-11-17  
**Status**: Active

---

## 1. Introduction

This document defines the organizational roles and responsibilities for creating, maintaining, and governing Digital Product Passports (DPPs) for neural networks within the AMPEL360 program. Clear role definition ensures accountability, efficient workflows, and compliance with regulatory requirements.

---

## 2. Organizational Structure

The AMPEL360 AI/DPP organization follows a matrix structure:

```
Program Management
├── Chief AI Officer (AI Governance)
│   ├── Neural Networks Engineering Team
│   ├── AI Safety & Assurance Team
│   └── DPP Management Office
├── Chief Technology Officer (Technical Integration)
├── Certification & Regulatory Affairs
├── Configuration Management Authority
└── Quality Assurance & Compliance
```

---

## 3. Executive Leadership Roles

### 3.1 Chief AI Officer (CAIO)

**Responsibilities**:
- **Strategic Vision**: Define AI strategy aligned with AMPEL360 mission (carbon-negative aviation)
- **Portfolio Management**: Prioritize AI system development, allocate resources
- **Governance**: Chair AI Steering Committee, approve AI policies
- **Regulatory Engagement**: Lead engagement with EASA, FAA on AI certification
- **DPP Oversight**: Ensure DPP framework adoption and effectiveness

**DPP Activities**:
- Approve DPP standard and templates
- Review high-risk model DPPs (DAL A, B)
- Sign off on AI Ethics Board recommendations

**Accountable For**: AI program success, regulatory compliance, safety

**Authority**: Veto power on AI system deployment; budget allocation

---

### 3.2 Chief Technology Officer (CTO)

**Responsibilities**:
- **Technical Architecture**: Ensure AI systems integrate with avionics, propulsion, energy systems
- **Platform Strategy**: Select AI hardware platforms (GPUs, NPUs, IMA partitions)
- **Cross-Functional Coordination**: Align AI development with ATA 22, 27, 42, 45, etc.

**DPP Activities**:
- Review interface specifications (95-00-05)
- Approve AI infrastructure decisions (cloud vs. edge inference)

**Accountable For**: Technical feasibility, system integration

---

### 3.3 Program Manager (AMPEL360 Overall)

**Responsibilities**:
- **Schedule Management**: Ensure AI development aligns with aircraft program timeline
- **Risk Management**: Track AI-related risks on program risk register
- **Stakeholder Communication**: Report AI progress to investors, customers, regulators

**DPP Activities**:
- Monitor DPP completion as milestone (e.g., "DPP 90% complete" = certification readiness gate)

**Accountable For**: Program delivery on time, on budget, on quality

---

## 4. AI/ML Engineering Roles

### 4.1 Lead AI Engineer

**Responsibilities**:
- **Model Architecture**: Design neural network architectures for specific applications (flight control, predictive maintenance, etc.)
- **Technical Leadership**: Mentor junior ML engineers, conduct design reviews
- **Innovation**: Identify opportunities for AI application, pilot new techniques

**DPP Activities**:
- Author Design sections (95-00-04)
- Create architecture diagrams (ASSETS)
- Justify design decisions (trade studies, rationale)

**Accountable For**: Model performance, technical quality

**Reports To**: Chief AI Officer

---

### 4.2 ML Engineer (Model Developer)

**Responsibilities**:
- **Data Preparation**: Collect, label, augment training data
- **Model Training**: Implement and train neural networks
- **Validation**: Evaluate model performance on test datasets
- **Iteration**: Refine models based on V&V feedback

**DPP Activities**:
- Document training procedures (95-00-06_Engineering)
- Log hyperparameters, training curves, validation metrics
- Provide model weights and checksums
- Tag model versions in Git

**Accountable For**: Model training quality, reproducibility

**Reports To**: Lead AI Engineer

---

### 4.3 Data Engineer

**Responsibilities**:
- **Data Infrastructure**: Build pipelines for data ingestion, storage, preprocessing
- **Data Quality**: Ensure training data is clean, representative, unbiased
- **Data Versioning**: Manage dataset versions using DVC or similar tools

**DPP Activities**:
- Document data sources (95-00-06)
- Provide dataset checksums (SHA-256)
- Create data lineage diagrams

**Accountable For**: Data quality, data governance

**Reports To**: Lead AI Engineer

---

### 4.4 MLOps Engineer

**Responsibilities**:
- **CI/CD Pipelines**: Automate model training, testing, deployment
- **Model Registry**: Maintain catalog of trained models (MLflow Model Registry)
- **Monitoring**: Implement runtime monitoring, anomaly detection
- **Infrastructure**: Manage AI compute resources (GPUs, Kubernetes clusters)

**DPP Activities**:
- Automate DPP metadata injection (commit hash, build timestamp)
- Integrate DPP generation into CI/CD pipeline
- Maintain version-controlled DPP repository

**Accountable For**: Deployment reliability, operational efficiency

**Reports To**: Lead AI Engineer (or IT/DevOps)

---

## 5. Safety & Assurance Roles

### 5.1 AI Safety Engineer

**Responsibilities**:
- **Hazard Analysis**: Conduct Preliminary Hazard Analysis (PHA), Functional Hazard Assessment (FHA) for AI systems
- **Safety Requirements**: Derive safety requirements from hazard analysis
- **Safety Case**: Develop safety arguments for AI systems
- **Monitoring Specifications**: Define runtime safety monitors (out-of-ODD detection, sanity checks)

**DPP Activities**:
- Author Safety section (95-00-02)
- Document Operational Design Domain (ODD)
- Provide safety assessment reports

**Accountable For**: AI system safety, hazard mitigation

**Reports To**: Safety Board (functionally), Chief AI Officer (administratively)

---

### 5.2 Verification & Validation (V&V) Engineer

**Responsibilities**:
- **Test Planning**: Define test strategies, test cases, acceptance criteria
- **Test Execution**: Run tests (unit, integration, system, HIL, flight test)
- **Coverage Analysis**: Ensure requirements coverage, code coverage
- **Robustness Testing**: Adversarial testing, input fuzzing, corner cases

**DPP Activities**:
- Author V&V section (95-00-07)
- Document test plans, test results, coverage reports
- Provide pass/fail evidence for each test case

**Accountable For**: Model validation, test quality

**Reports To**: Chief Engineer (V&V), Chief AI Officer (matrix)

**Independence**: For DAL A/B systems, V&V team must be independent from development team

---

### 5.3 AI Ethics Officer

**Responsibilities**:
- **Ethical Review**: Assess AI systems for bias, fairness, transparency
- **Governance Framework**: Develop AI ethics policies
- **Stakeholder Engagement**: Address ethical concerns from operators, public, regulators

**DPP Activities**:
- Review DPPs for ethical compliance
- Document ethical considerations in 95-00-02_Safety

**Accountable For**: Ethical AI deployment

**Reports To**: Chief AI Officer, Legal/Compliance

---

## 6. Certification & Regulatory Roles

### 6.1 Certification Manager

**Responsibilities**:
- **Certification Strategy**: Define path to Type Certificate (TC) or STC for AI systems
- **Compliance Planning**: Identify Means of Compliance (MoC), develop compliance matrix
- **Authority Engagement**: Coordinate with EASA, FAA certification specialists
- **Compliance Evidence**: Compile test reports, analyses, simulations for submission

**DPP Activities**:
- Author Certification section (95-00-10)
- Link DPP artifacts to certification requirements (MoC matrix)
- Provide authority correspondence, approval letters

**Accountable For**: Certification approval, regulatory compliance

**Reports To**: Program Manager, Chief AI Officer

---

### 6.2 Regulatory Affairs Specialist

**Responsibilities**:
- **Regulatory Monitoring**: Track evolving AI regulations (EU AI Act, EASA AI Roadmap)
- **Policy Interpretation**: Advise on application of regulations to AMPEL360 AI systems
- **Submission Preparation**: Draft certification applications, issue paper responses

**DPP Activities**:
- Document regulatory context (95-00-01-002)
- Maintain compliance checklist in DPP

**Accountable For**: Regulatory compliance, policy interpretation

**Reports To**: Certification Manager, Legal Department

---

### 6.3 Designated Engineering Representative (DER)

**Responsibilities** (if applicable):
- **Authority Delegation**: Act on behalf of FAA for specific compliance findings
- **Technical Review**: Review and approve engineering data for airworthiness
- **Liaison**: Interface between AMPEL360 and FAA

**DPP Activities**:
- Review DPP compliance evidence
- Sign off on findings of compliance

**Accountable For**: Airworthiness approval (delegated authority)

**Reports To**: FAA (functionally), AMPEL360 Certification Manager (administratively)

---

## 7. Configuration & Quality Management Roles

### 7.1 Configuration Manager

**Responsibilities**:
- **Baseline Management**: Establish and control configuration baselines for AI models
- **Change Control**: Manage Change Control Board (CCB), approve model updates
- **Version Control**: Ensure all models are version-tagged (Git, model registry)
- **Audit Trail**: Maintain records of all changes, approvals, deviations

**DPP Activities**:
- Author EIS/Versions/Tags section (95-00-11)
- Maintain DPP version history
- Ensure DPP consistency with actual deployed models

**Accountable For**: Configuration integrity, traceability

**Reports To**: Configuration Management Authority, Program Manager

---

### 7.2 Quality Assurance (QA) Engineer

**Responsibilities**:
- **Process Compliance**: Audit adherence to AMPEL360 AI development processes
- **Document Review**: Review DPPs for completeness, accuracy, consistency
- **Non-Conformance Management**: Track and resolve quality issues
- **Continuous Improvement**: Recommend process enhancements

**DPP Activities**:
- Conduct DPP quality audits (checklist-based review)
- Verify traceability links (requirements → design → test)
- Approve DPPs before certification submission

**Accountable For**: Process quality, documentation quality

**Reports To**: Quality Assurance Manager

---

### 7.3 DPP Administrator

**Responsibilities**:
- **DPP Tooling**: Maintain DPP generation tools, templates, databases
- **Access Control**: Manage user permissions (role-based access)
- **Data Management**: Ensure DPP data integrity, backup, disaster recovery
- **Training**: Train teams on DPP processes and tools

**DPP Activities**:
- Administer DPP repository (Git, SharePoint, or custom database)
- Generate DPP reports (status dashboards, export to PDF/HTML)
- Provide user support

**Accountable For**: DPP infrastructure, data management

**Reports To**: DPP Management Office, IT

---

## 8. Operational Roles

### 8.1 Aircraft Operator (Airline)

**Responsibilities**:
- **In-Service Monitoring**: Track AI system performance in operational fleet
- **Incident Reporting**: Report anomalies, failures, safety events involving AI
- **Feedback**: Provide operational feedback to AMPEL360 (e.g., false alarms, usability issues)

**DPP Activities**:
- Access operational guidance in DPP (95-10_Operations)
- Review in-service performance logs (95-00-12_Services)
- Contribute to lessons learned

**Accountable For**: Safe aircraft operation, operational data quality

---

### 8.2 Maintenance Organization (MRO)

**Responsibilities**:
- **Model Updates**: Install software updates (OTA or manual upload)
- **Troubleshooting**: Diagnose AI system faults using DPP diagnostic procedures
- **Configuration Verification**: Ensure correct model versions installed

**DPP Activities**:
- Follow maintenance procedures in DPP (95-00-12)
- Log maintenance actions (retraining, patches, hardware replacement)
- Update DPP with field modifications

**Accountable For**: Aircraft maintenance, configuration control

---

## 9. Governance Bodies

### 9.1 AI Steering Committee

**Composition**:
- Chief AI Officer (Chair)
- Chief Technology Officer
- Program Manager
- Certification Manager
- Safety Board Representative
- External Advisor (optional)

**Responsibilities**:
- Strategic AI portfolio decisions
- Resource allocation (budget, headcount)
- Risk escalation and resolution
- Policy approval (AI ethics, data governance)

**Meeting Cadence**: Quarterly (or more frequent as needed)

**DPP Activities**:
- Review DPP program metrics (completion rates, certification progress)
- Approve major DPP framework changes

---

### 9.2 Change Control Board (CCB)

**Composition**:
- Configuration Manager (Chair)
- Lead AI Engineer (technical expert)
- Certification Manager
- Safety Engineer
- V&V Engineer
- Quality Assurance representative

**Responsibilities**:
- Review change requests for AI models
- Assess impact (safety, certification, performance)
- Approve or reject changes
- Authorize baseline updates

**Meeting Cadence**: Weekly or as needed

**DPP Activities**:
- Approve DPP updates for deployed models
- Ensure change traceability in DPP (version deltas)

---

### 9.3 AI Safety Board

**Composition**:
- Chief Safety Officer (Chair)
- AI Safety Engineer
- Independent Safety Assessor (external)
- Human Factors Specialist
- Pilot Representative
- Regulatory Affairs Specialist

**Responsibilities**:
- Review safety cases for AI systems
- Approve safety requirements and mitigations
- Conduct safety audits
- Investigate AI-related incidents

**Meeting Cadence**: Monthly (or ad-hoc for incidents)

**DPP Activities**:
- Review Safety section (95-00-02) before certification submission
- Approve DPPs for high-risk AI systems

---

### 9.4 AI Ethics Board

**Composition**:
- AI Ethics Officer (Chair)
- Legal Counsel
- External Ethicist (academic or NGO)
- Passenger Advocate
- Sustainability Officer

**Responsibilities**:
- Review AI systems for ethical implications
- Develop ethical guidelines
- Address public concerns
- Recommend ethical improvements

**Meeting Cadence**: Quarterly

**DPP Activities**:
- Review DPPs for transparency, fairness, accountability
- Provide ethics sign-off for sensitive AI applications

---

## 10. RACI Matrix

**Key**: R = Responsible, A = Accountable, C = Consulted, I = Informed

| Activity                       | CAIO | Lead AI Eng | ML Eng | Safety Eng | V&V Eng | Cert Mgr | Config Mgr | QA |
| ------------------------------ | ---- | ----------- | ------ | ---------- | ------- | -------- | ---------- | -- |
| Define AI strategy             | A    | C           |        | C          |         | C        |            |    |
| Design model architecture      | C    | A           | R      | C          |         |          |            |    |
| Train model                    | I    | C           | A/R    |            |         |          |            |    |
| Conduct safety analysis        |      | C           |        | A/R        |         | C        |            |    |
| Perform V&V                    |      |             |        |            | A/R     | C        |            |    |
| Compile certification evidence |      | C           |        | C          | C       | A/R      |            |    |
| Manage model versions          |      | C           |        |            |         |          | A/R        |    |
| Approve DPP for release        | A    | C           |        | C          |         | C        | C          | R  |
| Deploy model to fleet          |      | C           |        |            |         | C        | A          | I  |
| Monitor in-service performance | I    | R           |        | C          |         |          |            |    |

---

## 11. Training & Competency Requirements

### 11.1 Core Competencies by Role

| Role               | Required Skills                                                       | Training Program                 |
| ------------------ | --------------------------------------------------------------------- | -------------------------------- |
| ML Engineer        | Python, TensorFlow/PyTorch, ML algorithms, data science               | Internal bootcamp + Coursera     |
| Safety Engineer    | ARP 4754A, ARP 4761, hazard analysis, safety cases                    | SAE courses + mentorship         |
| V&V Engineer       | Test design, [DO-178C](https://www.rtca.org/document/do-178c/), HIL testing, robustness analysis                | DO-178C training + hands-on      |
| Certification Mgr  | CS-25, FAA regulations, certification processes, authority engagement | EASA/FAA workshops + experience  |
| Config Mgr         | CM best practices, Git, baseline management, change control           | CMII certification + AMPEL360 CM |

### 11.2 DPP-Specific Training

All team members involved in DPP creation must complete:

- **DPP Framework Overview** (4 hours): Structure, tools, workflows
- **Role-Specific DPP Training** (4-8 hours): Authoring relevant sections
- **Tool Training** (2-4 hours): DPP repository, templates, CI/CD integration

**Certification**: DPP authorship certification after completing training and authoring 2 DPP sections under mentorship

---

## 12. Document Control

| Version | Date       | Author                 | Changes                                   |
| ------- | ---------- | ---------------------- | ----------------------------------------- |
| 1.0     | 2025-11-17 | AMPEL360 Documentation | Initial release — Roles & Responsibilities|

---

### Document Metadata

- **Originator**: AI prompted by Amedeo Pelliccia
- **Toolchain**: GitHub Copilot + AMPEL360 Documentation Standards
- **Status**: `WORKING`
- **Notes**: This document was generated with AI assistance and must be reviewed and approved by a designated human checker/approver before being used as an official baseline.

---

**Previous Document**: [95-00-01-005_DPP_Lifecycle_Coverage.md](95-00-01-005_DPP_Lifecycle_Coverage.md)

**Next Document**: [95-00-01-007_DPP_Data_Model_and_Identifiers.md](95-00-01-007_DPP_Data_Model_and_Identifiers.md)

**Parent**: [95-00-01_Overview README](README.md)
