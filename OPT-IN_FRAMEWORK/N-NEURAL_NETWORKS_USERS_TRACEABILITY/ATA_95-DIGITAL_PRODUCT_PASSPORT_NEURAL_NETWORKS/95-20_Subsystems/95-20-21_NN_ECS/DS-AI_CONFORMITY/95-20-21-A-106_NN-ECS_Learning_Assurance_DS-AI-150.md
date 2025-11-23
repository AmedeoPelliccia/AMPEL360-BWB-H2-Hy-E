# 95-20-21-A-106 — NN-ECS Learning Assurance (DS-AI-150)

**Document ID**: 95-20-21-A-106  
**Version**: 0.1  
**Status**: DRAFT  
**DS.AI Section**: DS-AI.150

## 1. Objective

Define the Learning Assurance approach for NN-ECS subsystem in accordance with DS.AI.150 requirements, addressing ML-specific verification and validation activities.

## 2. Learning Assurance Strategy

### 2.1 Assurance Level
- **AI Level**: 2A or 2B (per AI Subsystems Register)
- **Target AL**: AL2-AL3 (per DS.AI Table 5)
- **Target TQL**: TQL2-TQL3 (per DS.AI Table 5)
- **Rationale**: H2-H3 hazard classification requires medium-high assurance

### 2.2 Learning Assurance Objectives
1. Demonstrate data quality and representativeness
2. Validate model training and generalization
3. Verify intended behaviour within ODD
4. Detect and handle out-of-ODD scenarios
5. Ensure robustness to input perturbations
6. Maintain performance monitoring in operation

## 3. Data Assurance

### 3.1 Data Quality Requirements

| Aspect | Requirement | Verification Method |
|--------|-------------|---------------------|
| Completeness | 100% of required parameters | Data schema validation |
| Correctness | <1% erroneous values | Statistical outlier detection + manual review |
| Consistency | No contradictory labels | Cross-validation checks |
| Representativeness | Coverage of full ODD | ODD coverage analysis |
| Balance | No data imbalance >5:1 | Distribution analysis |

### 3.2 Training Data Validation
- **Source**: Operational flight data + flight test data + synthetic data
- **Volume**: Minimum 10,000 flight hours equivalent
- **Coverage**: All flight phases, environmental conditions, passenger loads
- **Quality Checks**: Automated validation + manual spot checks
- **Traceability**: Data lineage tracking per [ASSETS/95-20-21-A-206_NN-ECS_Data_Lineage_Diagram_ED-324.md](./ASSETS/95-20-21-A-206_NN-ECS_Data_Lineage_Diagram_ED-324.md) (TBD)

### 3.3 Test Data Independence
- **Independence**: Test set completely separate from training data
- **Validation Split**: 70% train, 15% validation, 15% test
- **Cross-Validation**: K-fold cross-validation (k=5) for hyperparameter tuning

## 4. Model Training Assurance

### 4.1 Training Process Controls
- **Reproducibility**: Fixed random seeds, version-controlled code and configs
- **Monitoring**: Training/validation loss curves, convergence criteria
- **Hyperparameter Tuning**: Systematic grid/random search with validation set
- **Early Stopping**: Prevent overfitting through early stopping on validation loss
- **Model Selection**: Holdout test set for final model selection

### 4.2 Training Documentation
For each model, document in training run records ([ASSETS/TRAINING_RUNS/](../ASSETS/TRAINING_RUNS/)):
- Model architecture and hyperparameters
- Training/validation/test datasets used
- Git commit hash for reproducibility
- Training metrics and convergence plots
- Final model performance on test set
- Known issues and limitations

### 4.3 Overfitting Prevention
- Regularization techniques (dropout, L2 regularization)
- Data augmentation where applicable
- Validation-based early stopping
- Test set performance verification

## 5. Model Verification

### 5.1 Functional Requirements Verification
Test each specified behaviour from [95-20-21-A-105_NN-ECS_Intended_Behaviour_DS-AI-150.md](./95-20-21-A-105_NN-ECS_Intended_Behaviour_DS-AI-150.md):
- [ ] Accuracy requirements met on test set
- [ ] Latency requirements met
- [ ] Update rate requirements met
- [ ] Boundary condition handling verified

### 5.2 Robustness Testing
- **Input Perturbations**: Small perturbations should not cause large output changes
- **Adversarial Testing**: Resistance to adversarial examples
- **Noise Robustness**: Performance under sensor noise conditions
- **Missing Data**: Graceful handling of missing input features

### 5.3 Out-of-ODD Detection
- **Method**: TBD (e.g., uncertainty quantification, anomaly detection)
- **Validation**: Test with known out-of-ODD inputs
- **Threshold Tuning**: Balance false positive vs. false negative rates
- **Operational Procedures**: Define response when OOD detected

### 5.4 Interpretability and Explainability
- **Model Architecture**: Inherently interpretable where possible (e.g., decision trees for simple functions)
- **Post-hoc Explanations**: SHAP values, feature importance for complex models
- **Validation**: Explanations align with domain knowledge
- **Documentation**: Explanation methods documented in model cards

## 6. ML-Specific Test Coverage

### 6.1 Test Categories

| Test Category | Target Coverage | Method |
|---------------|-----------------|--------|
| Nominal Operation | 100% | Requirements-based test cases |
| Boundary Conditions | 100% | Edge case testing for each input parameter |
| Off-Nominal Scenarios | Representative | Fault injection, degraded sensor scenarios |
| Out-of-ODD | Defined set | Test cases known to be outside ODD |
| Robustness | Statistical | Perturbation testing, noise injection |
| Adversarial | Limited | Adversarial example generation |

### 6.2 Test Quality Level (TQL)
Per DS.AI TQL2-TQL3:
- Independent test team
- Automated test execution where feasible
- Test coverage analysis
- Test result traceability to requirements

## 7. Operational Monitoring

### 7.1 Performance Monitoring
- Real-time prediction accuracy tracking
- Input distribution monitoring (detect drift)
- Out-of-ODD detection rate
- Failure rate monitoring

### 7.2 Anomaly Detection
- Unusual prediction patterns
- Sudden performance degradation
- Unexpected input patterns
- System health indicators

### 7.3 Data Collection for Continuous Improvement
- Operational data logging (with privacy safeguards)
- Edge case identification
- Performance feedback loop
- Model update triggering criteria

## 8. Model Update Process

### 8.1 Update Triggers
- Performance degradation detected
- New operational scenarios identified
- Safety-related issues discovered
- Scheduled periodic updates

### 8.2 Update Verification
- Full re-verification per this learning assurance plan
- Regression testing on previous test cases
- Delta certification approach (if applicable)
- Certification authority approval

## 9. Traceability

- **Parent Document**: [95-20-21-001_ECS_NN_Overview.md](../95-20-21-001_ECS_NN_Overview.md)
- **Intended Behaviour**: [95-20-21-A-105_NN-ECS_Intended_Behaviour_DS-AI-150.md](./95-20-21-A-105_NN-ECS_Intended_Behaviour_DS-AI-150.md)
- **OD/ODD**: [95-20-21-A-102_NN-ECS_Operational_Domain_ODD_DS-AI-120.md](./95-20-21-A-102_NN-ECS_Operational_Domain_ODD_DS-AI-120.md)
- **Test Evidence**: [10_CERTIFICATION/ASSETS/Reports/](../10_CERTIFICATION/ASSETS/Reports/)
- **Model Cards**: [ASSETS/MODELS/](../ASSETS/MODELS/)
- **Dataset Cards**: [ASSETS/DATASETS/](../ASSETS/DATASETS/)
- **Training Runs**: [ASSETS/TRAINING_RUNS/](../ASSETS/TRAINING_RUNS/)
- **Related Standards**: DS.AI.150, DO-178C, ED-324

## 10. Open Issues

- [ ] Define specific out-of-ODD detection methods
- [ ] Establish operational monitoring infrastructure
- [ ] Create detailed test cases for each model
- [ ] Define model update and re-certification process
- [ ] Establish data collection and feedback mechanisms
- [ ] Document explainability approaches for each model

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval by V&V Lead and Certification Manager.
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-23

---
