# 95-00-01-008 — DPP Scope Limitations and Exclusions

**Document ID**: 95-00-01-008  
**Version**: 1.0  
**Date**: 2025-11-17  
**Status**: Active

---

## 1. Introduction

This document clarifies the boundaries of the Digital Product Passport (DPP) framework for neural networks in AMPEL360. Understanding what is **included** and **excluded** ensures appropriate expectations and prevents scope creep.

---

## 2. Systems Included in DPP Scope

### 2.1 AI/ML Systems Subject to DPP

The following neural network and machine learning systems **MUST** have a DPP:

**Safety-Critical AI (DAL A, B, C)**:
- Flight control neural networks (ATA 27, 22)
- Envelope protection models
- Predictive maintenance for critical systems (ATA 45)
- Energy management AI (hydrogen fuel cells, battery management) (ATA 24, 28)

**Mission-Critical AI (DAL D, E)**:
- Route optimization algorithms (ATA 34)
- CO₂ capture process control (ATA 21-80-00)
- Cabin comfort optimization (ATA 44)
- Operational efficiency models (ATA 02)

**Rationale**: All AI systems with potential impact on safety, airworthiness, or environmental performance are included.

### 2.2 Data-Driven Software vs. Neural Networks

**Included**:
- Deep learning models (CNNs, RNNs, LSTMs, transformers, GANs)
- Classical machine learning with complex decision boundaries (SVM, gradient boosting, random forests)
- Reinforcement learning agents
- Ensemble models combining multiple ML techniques

**Rationale**: Systems exhibiting non-deterministic or emergent behavior require DPP for transparency and assurance.

---

## 3. Systems Excluded from DPP Scope

### 3.1 Conventional Software (DO-178C Compliant)

**Excluded**:
- Deterministic control laws (e.g., PID controllers with fixed coefficients)
- Rule-based expert systems (if/then logic without learning)
- Traditional avionics software (flight management systems without AI)

**Rationale**: Conventional software is governed by existing standards (DO-178C, DO-254). DPP is specifically tailored for AI/ML uncertainty and lifecycle.

**Documentation**: Conventional software documented per standard software development plans, not DPP.

### 3.2 Off-the-Shelf AI Models (Unmodified)

**Excluded**:
- Commercial off-the-shelf (COTS) AI tools used for ground operations (e.g., supply chain optimization, HR analytics) **if not integrated into aircraft systems**
- Generic image recognition models for marketing materials

**Rationale**: Non-airborne, non-operational AI systems do not impact aircraft airworthiness.

**Caveat**: If a COTS model is integrated into an aircraft system (e.g., COTS object detection for collision avoidance), it **MUST** have a DPP (may reference vendor documentation).

### 3.3 Statistical Models (Simple)

**Excluded**:
- Linear regression with < 10 parameters
- Kalman filters with fixed matrices
- Moving average filters

**Rationale**: Simple statistical models with well-understood behavior and closed-form solutions do not require AI-specific assurance.

**Documentation**: Treated as conventional algorithms, documented in system design specifications (ATA XX-00-04).

### 3.4 Human-In-The-Loop Tools

**Excluded**:
- Design optimization tools run by engineers (e.g., FEA optimization with AI suggestions, **if final design decision made by human**)
- AI-assisted coding tools (GitHub Copilot, ChatGPT) used during development (**if code reviewed and owned by humans**)

**Rationale**: AI serves as a productivity aid; human retains decision authority and accountability.

**Documentation**: Tool usage logged in engineering notebooks, but AI tool itself does not have a DPP.

---

## 4. Lifecycle Stages Partially Covered

### 4.1 Research & Exploration (Pre-Concept)

**Coverage**: Minimal

DPP begins at **concept approval** (95-00-01_Overview stage). Early research prototypes, proof-of-concepts, and feasibility studies are **not** required to have a full DPP.

**Documentation**: Research findings documented in technical reports, not DPP.

**Transition**: When a research prototype is approved for development, a DPP is initiated.

### 4.2 Decommissioned Models (Post-Retirement)

**Coverage**: Archival only

After model retirement (95-00-14_Ops_Std_Sustain), the DPP transitions to **read-only archival mode**. No further updates are made, but DPP remains accessible for:

- Historical reference
- Regulatory audits
- Incident investigations (if model was involved in historical event)
- Lessons learned for future programs

**Retention Period**: Minimum 10 years post-retirement (per aviation regulatory standards)

---

## 5. Data Elements Not Included in DPP

### 5.1 Raw Training Data

**Excluded**: Full raw training datasets (terabytes of sensor logs, flight data)

**Rationale**: Storage and transfer impractical; privacy concerns (GDPR).

**Included Instead**:
- Dataset metadata (size, sources, collection dates)
- Dataset checksums (SHA-256)
- Statistical summaries (distribution plots, feature statistics)
- Pointers to dataset storage location (data lake, archive)

**Access**: Raw data available on request to authorized personnel (e.g., certification authorities) via secure data room.

### 5.2 Model Weights (Binary Files)

**Excluded**: Full model weight files (large binary blobs) in DPP JSON

**Rationale**: DPP remains lightweight and human-readable.

**Included Instead**:
- Model weight file checksum (SHA-256)
- Pointer to model registry (MLflow, S3 bucket)
- Model size (number of parameters, memory footprint)

**Access**: Model weights retrievable via API or model registry using UUID.

### 5.3 Proprietary Algorithms (Trade Secrets)

**Excluded**: Source code of proprietary algorithms (if intellectual property)

**Rationale**: Balance transparency with commercial confidentiality.

**Included Instead**:
- High-level algorithm description (e.g., "LSTM with attention mechanism")
- Architecture diagram (layers, connections)
- References to published papers (if based on public research)

**Access**: Full source code available to certification authorities under NDA; not publicly disclosed.

### 5.4 Personal Data (GDPR Protected)

**Excluded**: Personally identifiable information (PII) from operational logs

**Rationale**: GDPR compliance, privacy protection.

**Included Instead**:
- Anonymized aggregate statistics (e.g., "Model processed 10,000 flights across 25 aircraft")
- Incident summaries with PII redacted

**Access**: Full logs (with PII) accessible only to authorized personnel (safety board, legal, authorities) under data protection agreements.

---

## 6. Functional Limitations

### 6.1 Real-Time Performance Monitoring

**Not Included**: Real-time streaming of operational metrics (live dashboards)

**Rationale**: DPP is a **documentation system**, not a real-time monitoring system.

**Alternatives**:
- Operational monitoring via aircraft health management systems (ATA 45)
- DPP periodically updated with aggregated operational statistics (e.g., quarterly)

### 6.2 Automated Model Updates

**Not Included**: Automatic retraining and deployment without human approval

**Rationale**: Aviation safety requires human oversight and regulatory approval for model changes.

**Process**: All model updates follow **Change Control Board (CCB)** approval process (95-00-11_EIS_Versions_Tags).

### 6.3 Incident Root Cause Analysis

**Not Included**: Full incident investigation reports (if AI system implicated in safety event)

**Rationale**: Incident investigations are governed by separate aviation accident investigation protocols (ICAO Annex 13).

**Included in DPP**: Summary of incident, model behavior during event, and corrective actions taken (cross-reference to full investigation report).

---

## 7. Geographic & Regulatory Scope

### 7.1 Primary Jurisdictions

DPP designed to satisfy requirements in:

- **European Union** (EASA, EU DPP Regulation, EU AI Act)
- **United States** (FAA, 14 CFR)
- **International** (ICAO standards)

### 7.2 Jurisdictions with Limited Alignment

DPP **may not** fully satisfy requirements in jurisdictions with unique AI regulations:

- **China** (CAAC) — Additional documentation may be required
- **Russia** (Rosaviatsia) — Local certification requirements may differ
- **Emerging Markets** — Regulatory frameworks still developing

**Mitigation**: DPP designed to be **extensible** (additional fields can be added for jurisdiction-specific requirements).

---

## 8. Temporal Limitations

### 8.1 Snapshot vs. Continuous

DPP represents a **versioned snapshot** of model state, not a continuous real-time record.

**Update Frequency**:
- **During Development**: Updated at each lifecycle gate (PDR, CDR, certification submission)
- **In Service**: Updated quarterly (or after significant events: incidents, major updates)

**Real-Time Data**: Operational telemetry stored separately in aircraft health monitoring systems; aggregated into DPP periodically.

### 8.2 Historical Reconstruction Limitations

While DPP aims for full **reproducibility**, certain limitations exist:

**Challenges**:
- **Compute Environment Evolution**: Training performed on specific hardware (GPU model, driver version) that may be obsolete
- **Software Library Updates**: Dependencies may have breaking changes in newer versions
- **Random Seed Sensitivity**: Some models exhibit minor variations despite fixed random seeds (GPU non-determinism)

**Mitigation**:
- DPP captures environment specifications (library versions, hardware details)
- Reproducibility validated during certification (retraining from DPP records)
- Acceptable tolerance defined (e.g., < 0.1% variation in performance metrics)

---

## 9. Interoperability Limitations

### 9.1 Cross-Program Reuse

DPP is optimized for **AMPEL360 program**. Reuse in other aircraft programs (e.g., regional jets, military aircraft) may require adaptation.

**Considerations**:
- Different ATA chapter structures
- Different certification authorities and standards
- Different operational environments (ODD)

**Portability**: DPP data model designed to be **generalizable** (JSON schema can be extended or adapted).

### 9.2 Legacy System Integration

DPP may have limited integration with **legacy documentation systems** (e.g., paper-based archives, proprietary databases).

**Workaround**: Manual data entry or one-time migration scripts to populate DPP from legacy sources.

---

## 10. Resource Constraints

### 10.1 Small-Scale Models

For **trivial models** (< 1000 parameters, non-safety-critical), a full DPP may be **overkill**.

**Alternative**: Lightweight DPP (subset of mandatory fields only).

**Example**: Cabin lighting optimization neural network (DAL E) — simplified DPP with core metadata only.

### 10.2 Rapid Prototyping

During **early prototyping** (95-00-08_Prototyping), maintaining a complete DPP may slow iteration.

**Compromise**: Lightweight "proto-DPP" during prototyping; full DPP required before certification submission.

---

## 11. Known Gaps & Future Enhancements

### 11.1 Current Gaps

| Gap Area                          | Impact               | Planned Resolution          | Timeline |
| --------------------------------- | -------------------- | --------------------------- | -------- |
| Continuous learning (in-flight)   | Not supported        | Prohibit per regulations    | N/A      |
| Explainable AI (XAI) standards    | Emerging area        | Adopt as standards mature   | 2026     |
| Quantum ML models                 | Future technology    | Extend DPP schema           | 2027+    |
| Multi-modal AI (vision+language)  | Limited guidance     | Develop multi-modal DPP     | 2026     |
| Federated learning                | Distributed training | Adapt DPP for FL workflows  | 2027     |

### 11.2 Planned Enhancements

**DPP Schema Version 2.0** (Target: 2026):
- Enhanced explainability artifacts (SHAP, LIME integration)
- Support for ensemble models (multiple sub-models in one DPP)
- Carbon footprint calculation automation (direct integration with energy monitoring)
- Real-time traceability updates (API-driven)

**Tooling Improvements**:
- Automated DPP generation from training logs (reduce manual effort)
- Natural language querying of DPP database (e.g., "Show all models with accuracy > 95%")
- Augmented reality (AR) visualization of model architectures

---

## 12. Scope Boundary Summary

### 12.1 In Scope

✅ All neural networks and ML models in AMPEL360 aircraft systems  
✅ Safety-critical and mission-critical AI (DAL A-E)  
✅ Lifecycle from concept through retirement  
✅ Training, validation, certification, operational data  
✅ Traceability to requirements, tests, certification artifacts  

### 12.2 Out of Scope

❌ Conventional deterministic software (DO-178C only)  
❌ Non-airborne AI tools (ground operations, marketing)  
❌ Simple statistical models (linear regression, Kalman filters)  
❌ Raw training datasets (metadata only)  
❌ Real-time operational monitoring (separate system)  
❌ Full incident investigation reports (summaries only)  

### 12.3 Partially in Scope

⚠️ Research prototypes (minimal DPP until concept approval)  
⚠️ Retired models (archival mode, read-only)  
⚠️ COTS AI models (if integrated into aircraft, must have DPP)  
⚠️ Proprietary algorithms (high-level description, full details under NDA)  

---

## 13. Stakeholder Communication

### 13.1 Setting Expectations

**For Certification Authorities**:
- DPP provides comprehensive compliance evidence
- Some proprietary details available under NDA
- Real-time monitoring data available on request (not in DPP)

**For Operators**:
- DPP contains operational guidance, performance metrics
- Raw operational logs not in DPP (available via separate systems)
- DPP updated periodically (not real-time)

**For Developers**:
- DPP is a documentation tool, not a development tool
- Lightweight DPP during prototyping; full DPP before certification
- Automated tooling reduces manual effort

### 13.2 Escalation Process

**Out-of-Scope Requests**:
- Requests for features/data outside DPP scope reviewed by **AI Steering Committee**
- Decision: Add to future DPP version, provide via alternative system, or decline

**Example**: Request for "real-time model performance dashboard"  
**Resolution**: Not a DPP function; refer to aircraft health monitoring system (ATA 45)

---

## 14. Document Control

| Version | Date       | Author                 | Changes                                         |
| ------- | ---------- | ---------------------- | ----------------------------------------------- |
| 1.0     | 2025-11-17 | AMPEL360 Documentation | Initial release — Scope Limitations & Exclusions|

---

### Document Metadata

- **Originator**: AI prompted by Amedeo Pelliccia
- **Toolchain**: GitHub Copilot + AMPEL360 Documentation Standards
- **Status**: `WORKING`
- **Notes**: This document was generated with AI assistance and must be reviewed and approved by a designated human checker/approver before being used as an official baseline.

---

**Previous Document**: [95-00-01-007_DPP_Data_Model_and_Identifiers.md](95-00-01-007_DPP_Data_Model_and_Identifiers.md)

**Parent**: [95-00-01_Overview README](README.md)
