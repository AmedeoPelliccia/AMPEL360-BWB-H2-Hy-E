# 95-20-28 NN Fuel System — Document Index

## Component Specifications

| ID | Document | Description | Status |
|----|----------|-------------|--------|
| 95-20-28-001 | [Fuel_System_NN_Overview.md](../95-20-28-001_Fuel_System_NN_Overview.md) | Overall architecture and system overview | WORKING |
| 95-20-28-002 | [Fuel_Quantity_Estimator.md](../95-20-28-002_Fuel_Quantity_Estimator.md) | Fuel quantity estimation NN component | WORKING |
| 95-20-28-003 | [Leak_Detection_Monitor.md](../95-20-28-003_Leak_Detection_Monitor.md) | Leak detection and anomaly monitoring | WORKING |
| 95-20-28-004 | [Fuel_Transfer_Optimizer.md](../95-20-28-004_Fuel_Transfer_Optimizer.md) | Fuel transfer optimization NN component | WORKING |
| 95-20-28-005 | [Fuel_Temperature_Predictor.md](../95-20-28-005_Fuel_Temperature_Predictor.md) | Temperature prediction and thermal management | WORKING |
| 95-20-28-006 | [Water_Contamination_Detector.md](../95-20-28-006_Water_Contamination_Detector.md) | Water contamination detection | WORKING |
| 95-20-28-007 | [Integration_with_ATA_28.md](../95-20-28-007_Integration_with_ATA_28.md) | Integration with ATA 28 Fuel System | WORKING |
| 95-20-28-008 | [Safety_and_Certification.md](../95-20-28-008_Safety_and_Certification.md) | Safety analysis and certification strategy | WORKING |
| 95-20-28-009 | [Operational_Procedures.md](../95-20-28-009_Operational_Procedures.md) | Operational procedures and crew guidance | WORKING |

## Model Cards

| ID | Model Card | Model Name | Version | Status |
|----|------------|------------|---------|--------|
| 95-20-28-A-101 | [Fuel_Quantity_Estimator_v1.0.yaml](../ASSETS/Model_Cards/95-20-28-A-101_Fuel_Quantity_Estimator_v1.0.yaml) | Fuel Quantity Estimator | v1.0 | Production |
| 95-20-28-A-102 | [Leak_Detection_Monitor_v1.0.yaml](../ASSETS/Model_Cards/95-20-28-A-102_Leak_Detection_Monitor_v1.0.yaml) | Leak Detection Monitor | v1.0 | Production |
| 95-20-28-A-103 | [Fuel_Transfer_Optimizer_v1.0.yaml](../ASSETS/Model_Cards/95-20-28-A-103_Fuel_Transfer_Optimizer_v1.0.yaml) | Fuel Transfer Optimizer | v1.0 | Production |

## Data Assets

| ID | Dataset | Description | Location |
|----|---------|-------------|----------|
| 95-20-28-601 | Fuel_Quantity_Sensor_Logs.parquet | Training data for fuel quantity estimation | Data/Training_Datasets/ |
| 95-20-28-602 | Fuel_Transfer_Events.parquet | Training data for transfer optimization | Data/Training_Datasets/ |
| 95-20-28-605 | Digital_Twin_Fuel_Scenarios.parquet | Synthetic data from digital twin simulations | Data/Synthetic_Data/ |

## Documentation

| Document | Description | Location |
|----------|-------------|----------|
| API_Specs.md | API specifications for NN Fuel System | Documentation/ |
| Data_Dictionary.md | Data dictionary for all inputs/outputs | Documentation/ |
| Test_Strategy.md | Testing and validation strategy | Documentation/ |

## Models

| Type | Description | Location |
|------|-------------|----------|
| Source | Python source code for all models | Models/Source/ |
| Configs | Training and deployment configurations | Models/Configs/ |
| Trained | ONNX model artifacts | Models/Trained/ |
| Scripts | Deployment and testing scripts | Models/Scripts/ |

## Tests

| Type | Description | Location |
|------|-------------|----------|
| Unit | Unit tests for individual components | Tests/Unit/ |
| Integration | Integration tests with ATA 28 | Tests/Integration/ |
| Scenarios | End-to-end scenario tests | Tests/Scenarios/ |

## Cross-References

### Links to ATA 95-00 GENERAL

- [95-00-03 Requirements](../../95-00_GENERAL/95-00-03_Requirements/)
- [95-00-06 Engineering](../../95-00_GENERAL/95-00-06_Engineering/)
- [95-00-07 V&V](../../95-00_GENERAL/95-00-07_V_AND_V/)
- [95-00-10 Certification](../../95-00_GENERAL/95-00-10_Certification/)

### Links to Other Subsystems

- [95-20-01 NN Core Platform](../../95-20-01_NN_Core_Platform/)
- [95-20-02 NN DPP Blockchain](../../95-20-02_NN_DPP_Blockchain/)
- [95-20-42 NN IMA Integration](../../95-20-42_NN_IMA_Integration/)

### External References

- [ATA 28 Fuel System](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)
- [DO-178C](https://www.rtca.org/product/do-178c/)
- [EASA SC-AI](https://www.easa.europa.eu/en/document-library/general-publications/special-condition-sc-ai)

## Document Control

- **Version**: 1.0  
- **Last Updated**: 2025-11-18  
- **Maintained By**: AMPEL360 NN Fuel System Team

---

## Document Control – AI Involvement

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.  
- Status: **DRAFT** – Subject to human review and approval.  
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-18_.
