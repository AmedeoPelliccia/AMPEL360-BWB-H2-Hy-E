# 95-00-01-003 — DPP Key Concepts and Definitions

**Document ID**: 95-00-01-003  
**Version**: 1.0  
**Date**: 2025-11-17  
**Status**: Active

---

## 1. Core Terminology

### 1.1 Digital Product Passport (DPP)

A **Digital Product Passport** is a comprehensive digital record that captures the identity, provenance, technical specifications, lifecycle history, and sustainability characteristics of a product or system. In the context of ATA 95, the DPP specifically documents neural networks and AI systems deployed in the AMPEL360 aircraft.

**Key Attributes**:
- Unique identifier (UUID or similar)
- Structured data schema (JSON, XML, or graph database)
- Version-controlled evolution
- Machine-readable and human-accessible
- Interoperable across systems and organizations

---

## 2. AI/ML System Concepts

### 2.1 Neural Network

An **artificial neural network** is a computational model inspired by biological neural structures, consisting of interconnected nodes (neurons) organized in layers. In AMPEL360 applications, neural networks perform tasks such as control law adaptation, predictive maintenance, and energy optimization.

**Characteristics**:
- **Architecture**: Input layer, hidden layers, output layer
- **Activation Functions**: ReLU, sigmoid, tanh, softmax
- **Learning Paradigm**: Supervised, unsupervised, reinforcement learning
- **Inference Mode**: Forward propagation from inputs to outputs

### 2.2 Machine Learning Model

A **machine learning model** is a parameterized function learned from data that makes predictions or decisions. This broader category includes:

- **Neural Networks**: Deep learning architectures
- **Tree-Based Models**: Decision trees, random forests, gradient boosting
- **Kernel Methods**: Support vector machines (SVM)
- **Probabilistic Models**: Bayesian networks, Gaussian processes
- **Ensemble Methods**: Combining multiple models for robustness

In AMPEL360, "neural network" and "ML model" are used interchangeably when referring to deep learning systems.

### 2.3 Training Data

**Training data** is the curated dataset used to optimize model parameters during the learning phase. For safety-critical aviation systems, training data must be:

- **Representative**: Covers operational design domain (ODD)
- **Balanced**: Adequate samples of normal and edge cases
- **Labeled**: Ground truth annotations (for supervised learning)
- **Versioned**: Tracked with provenance and quality metrics
- **Privacy-Compliant**: Anonymized where necessary (GDPR)

**AMPEL360 Standard**: All training datasets documented in 95-00-06_Engineering with SHA-256 hashes for integrity verification.

### 2.4 Model Validation & Testing

**Validation** is the process of assessing whether a trained model meets performance requirements on data not used during training.

**Key Metrics**:
- **Accuracy**: Proportion of correct predictions
- **Precision/Recall**: For classification tasks
- **RMSE/MAE**: For regression tasks
- **Robustness**: Performance under input perturbations
- **Generalization**: Performance on out-of-distribution data

**Distinct from Training**: Validation uses held-out data; training optimizes on learning set.

### 2.5 Inference

**Inference** is the operational phase where a trained model processes new inputs to produce outputs (predictions, decisions, control commands). In AMPEL360:

- **Real-Time Inference**: Flight control, energy management (millisecond latency)
- **Near-Real-Time**: Predictive maintenance alerts (second latency)
- **Batch Inference**: Post-flight data analysis, trend analysis

**Inference Environment**: Certified hardware (ATA 42), deterministic execution, runtime monitoring.

---

## 3. Lifecycle Concepts

### 3.1 Model Versioning

Each neural network in AMPEL360 is assigned a **semantic version number**: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (architecture redesign, incompatible interface)
- **MINOR**: Non-breaking enhancements (retraining with expanded dataset, hyperparameter tuning)
- **PATCH**: Hotfixes (bug corrections, numerical stability improvements)

Example: `FlightControlNN v2.3.1`

### 3.2 Model Lineage / Provenance

**Model lineage** traces the origin and evolution of a neural network:

```
Base Model (v1.0)
  ├─ Transfer Learning → Variant A (v1.1)
  └─ Retraining → Version 2.0
        └─ Hyperparameter Tuning → Version 2.1
```

Captured in DPP:
- Parent model (if transfer learning)
- Training configuration (hyperparameters, optimizer, learning rate schedule)
- Dataset version
- Commit hash of training code
- Compute infrastructure (GPU type, training duration)

### 3.3 Operational Design Domain (ODD)

The **Operational Design Domain** defines the conditions under which a neural network is validated to operate safely:

**Example for AMPEL360 Flight Control NN**:
- **Altitude**: 0 – 45,000 ft
- **Airspeed**: 120 – 450 knots
- **Environmental**: -55°C to +50°C, ISA ±15°C
- **Weather**: VMC and IMC (instrument meteorological conditions)
- **Aircraft Configuration**: Clean, takeoff, landing, flaps extended
- **Failure States**: Single system faults (per CS 25.1309)

**Out-of-ODD Behavior**: Model outputs flagged as unreliable; fallback to conventional control laws.

### 3.4 Model Drift

**Model drift** (also called *concept drift*) occurs when the statistical properties of input data change over time, degrading model performance.

**Detection Methods**:
- Statistical tests (KS test, chi-squared)
- Performance monitoring (accuracy degradation)
- Anomaly detection on feature distributions

**Mitigation**:
- Periodic retraining with updated data
- Adaptive learning (cautiously, with certification constraints)
- Model replacement with updated version

---

## 4. Safety & Assurance Concepts

### 4.1 Explainability / Interpretability

**Explainability** is the ability to understand why a model produced a specific output.

**Levels**:
- **Global Interpretability**: Overall model behavior (e.g., feature importance)
- **Local Interpretability**: Specific prediction explanation (e.g., SHAP values, LIME)
- **Post-Hoc Analysis**: Saliency maps, attention visualization

**AMPEL360 Requirement**: High-risk models (DAL A/B) must provide local explanations for certification authorities.

### 4.2 Robustness

**Robustness** measures a model's resilience to input perturbations, adversarial attacks, and distribution shifts.

**Testing Approaches**:
- **Adversarial Examples**: Intentionally crafted inputs to fool the model
- **Input Fuzzing**: Random perturbations within bounds
- **Corner Case Testing**: Extreme but plausible scenarios

**Acceptance Criteria**: Performance degradation < 5% under bounded perturbations (AMPEL360 standard).

### 4.3 Certification Credit

**Certification credit** refers to the extent to which a neural network's validation evidence can be reused across:

- Different aircraft variants
- Software updates
- Regulatory jurisdictions (EASA ↔ FAA)

**Enablers**:
- Modular architecture (plug-and-play models)
- Standardized test harnesses
- Comprehensive DPP documentation

### 4.4 Runtime Monitoring

**Runtime monitoring** involves continuous observation of model behavior during operation to detect anomalies, performance degradation, or safety violations.

**AMPEL360 Implementation**:
- **Input Range Checks**: Flag out-of-ODD conditions
- **Output Sanity Checks**: Physics-based constraints (e.g., control surface limits)
- **Confidence Scoring**: Model uncertainty estimates
- **Logging**: Timestamped records for post-flight analysis

---

## 5. Data & Information Concepts

### 5.1 Data Module (S1000D)

A **Data Module** is the smallest self-contained unit of technical documentation in the S1000D standard. Each neural network DPP can be composed of multiple data modules:

- **DMC-AMPEL360-95-00-01-001-A**: Purpose and Scope
- **DMC-AMPEL360-95-20-10-001-A**: Specific system (e.g., flight control NN)
- **DMC-AMPEL360-95-40-01-001-A**: Software architecture

### 5.2 Digital Twin

A **digital twin** is a virtual replica of a physical asset (or, in ATA 95, a neural network) that mirrors its real-world state and behavior.

**AMPEL360 Use Cases**:
- **Shadow Mode Testing**: Digital twin runs in parallel with physical system; outputs compared but not used for control
- **What-If Analysis**: Simulate model updates before deployment
- **Incident Reconstruction**: Replay flight data to diagnose failures

### 5.3 Traceability Matrix

A **traceability matrix** links DPP elements to requirements, design decisions, test cases, and certification artifacts.

**Example**:

| Requirement ID | Model Component       | Test Case ID | Cert Evidence    |
| -------------- | --------------------- | ------------ | ---------------- |
| REQ-FC-001     | Pitch Control Layer   | TC-FC-101    | EASA-DOA-2025-42 |
| REQ-PM-012     | Anomaly Detection NN  | TC-PM-045    | FAA-STC-2026-18  |

Maintained in 95-00-03_Requirements folder.

---

## 6. Environmental & Sustainability Concepts

### 6.1 Carbon Footprint of AI

The **carbon footprint** of a neural network includes:

- **Training Emissions**: Energy consumed during model training (GPU/TPU hours × grid carbon intensity)
- **Inference Emissions**: Energy consumed during operational use
- **Embodied Carbon**: Manufacturing of AI accelerator hardware
- **Data Center Infrastructure**: Cooling, networking overhead

**AMPEL360 Tracking**: CO₂e (carbon dioxide equivalent) logged in DPP per ISO 14067 methodology.

### 6.2 Transfer Learning

**Transfer learning** is a technique where a model trained on one task is adapted for a related task, reducing training time and data requirements.

**Circular Economy Benefit**: Reuse of learned representations (e.g., feature extractors trained on public datasets, fine-tuned for AMPEL360-specific data).

### 6.3 Model Retirement & Archival

**Model retirement** is the formal process of decommissioning a neural network at end-of-life.

**Steps**:
1. **Notification**: Stakeholders informed of retirement timeline
2. **Data Archival**: Training data, weights, and logs stored per retention policy (95-00-14)
3. **Lessons Learned**: Post-mortem analysis captured in DPP
4. **Disposal**: Secure deletion of models from operational systems; archival copies retained for regulatory compliance (minimum 10 years post-EIS)

---

## 7. Organizational & Governance Concepts

### 7.1 Model Owner

The **model owner** is the individual or team responsible for a neural network's lifecycle:

- Requirements definition
- Design and training oversight
- Validation and certification
- Maintenance and updates
- Retirement decision

**AMPEL360 Assignment**: Each model listed in 95-00-13_Subsystems_Components with designated owner.

### 7.2 Configuration Control

**Configuration control** ensures that only approved versions of neural networks are deployed in aircraft.

**Mechanisms**:
- **Baseline Management**: Frozen versions tagged in version control
- **Change Control Board (CCB)**: Reviews and approves model updates
- **Deployment Authorization**: Formal sign-off before OTA (over-the-air) updates

Governed by 95-00-11_EIS_Versions_Tags processes.

### 7.3 Continuous Integration / Continuous Deployment (CI/CD)

**CI/CD** pipelines automate testing and deployment of neural network updates.

**AMPEL360 Pipeline**:
1. **Code Commit**: Training scripts, model architectures pushed to Git
2. **Automated Testing**: Unit tests, integration tests, performance benchmarks
3. **Validation Gate**: Comparison against baseline (regression checks)
4. **Staging Deployment**: Deploy to test aircraft or simulator
5. **Approval Gate**: CCB review, authority concurrence
6. **Production Deployment**: OTA update to fleet (with rollback capability)

**Tool Stack**: Jenkins/GitLab CI + MLflow + Kubernetes

---

## 8. Acronyms & Abbreviations

| Acronym | Definition                                      |
| ------- | ----------------------------------------------- |
| AI      | Artificial Intelligence                         |
| ANN     | Artificial Neural Network                       |
| CCB     | Configuration Control Board                     |
| CI/CD   | Continuous Integration / Continuous Deployment  |
| DAL     | Design Assurance Level                          |
| DMC     | Data Module Code (S1000D)                       |
| DPP     | Digital Product Passport                        |
| FMEA    | Failure Modes and Effects Analysis              |
| GDPR    | General Data Protection Regulation              |
| GPU     | Graphics Processing Unit                        |
| IMA     | Integrated Modular Avionics                     |
| LIME    | Local Interpretable Model-agnostic Explanations |
| MAE     | Mean Absolute Error                             |
| ML      | Machine Learning                                |
| NN      | Neural Network                                  |
| ODD     | Operational Design Domain                       |
| OTA     | Over-The-Air                                    |
| RMSE    | Root Mean Squared Error                         |
| SHAP    | SHapley Additive exPlanations                   |
| SVM     | Support Vector Machine                          |
| UUID    | Universally Unique Identifier                   |

---

## 9. References

- ISO/IEC 5338:2023 — AI System Lifecycle Process
- ISO/IEC 22989:2022 — AI Concepts and Terminology
- EASA Concept Paper: Artificial Intelligence (CP-01, Issue 02)
- S1000D Issue 6.0 — International Specification for Technical Publications

---

## 10. Document Control

| Version | Date       | Author                 | Changes                                |
| ------- | ---------- | ---------------------- | -------------------------------------- |
| 1.0     | 2025-11-17 | AMPEL360 Documentation | Initial release — Key Concepts & Defs  |

---

### Document Metadata

- **Originator**: AI prompted by Amedeo Pelliccia
- **Toolchain**: GitHub Copilot + AMPEL360 Documentation Standards
- **Status**: `WORKING`
- **Notes**: This document was generated with AI assistance and must be reviewed and approved by a designated human checker/approver before being used as an official baseline.

---

**Previous Document**: [95-00-01-002_Regulatory_and_Standards_Context.md](95-00-01-002_Regulatory_and_Standards_Context.md)

**Next Document**: [95-00-01-004_DPP_Objectives_for_Neural_Networks.md](95-00-01-004_DPP_Objectives_for_Neural_Networks.md)

**Parent**: [95-00-01_Overview README](README.md)
