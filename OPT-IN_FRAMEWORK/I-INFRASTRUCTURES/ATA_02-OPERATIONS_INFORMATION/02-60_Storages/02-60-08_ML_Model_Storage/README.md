# 02-60-08 – ML Model Storage

## Purpose

This directory defines the storage infrastructure for neural network models, training datasets, and ML artifacts. It ensures traceability and compliance with the [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206) and integration with [ATA 95 Digital Product Passport](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/).

---

## Scope

ML model storage encompasses:

- **Trained Models**: Neural network models (ONNX, TensorFlow, PyTorch formats)
- **Training Datasets**: Labeled data used for model training
- **Feature Stores**: Feature engineering pipelines and feature data
- **Model Metadata**: Performance metrics, hyperparameters, training provenance
- **DPP Integration**: Blockchain-anchored hashes and lineage tracking

---

## Key Documents

- **[02-60-08-001_Model_Registry.md](./02-60-08-001_Model_Registry.md)** – Model registry design (versions, stages, metadata)
- **[02-60-08-002_Dataset_Versioning.md](./02-60-08-002_Dataset_Versioning.md)** – Dataset versioning and DVC integration
- **[02-60-08-003_Feature_Store.md](./02-60-08-003_Feature_Store.md)** – Feature store architecture (Feast)
- **[02-60-08-004_Model_Artifacts.md](./02-60-08-004_Model_Artifacts.md)** – Types of artifacts and storage structure
- **[02-60-08-005_DPP_Integration.md](./02-60-08-005_DPP_Integration.md)** – Digital Product Passport linkage

---

## ASSETS

### Configurations
- **02-60-08-A-001_MLflow_Registry_Config.yaml** – MLflow registry configuration
- **02-60-08-A-002_DVC_Storage_Config.yaml** – DVC remote storage setup
- **02-60-08-A-003_Feast_Feature_Store.yaml** – Feature store definition

### Models
- **02-60-08-A-101_Model_Storage_Structure.md** – Repository organization
- **02-60-08-A-102_ONNX_Model_Repository/** – ONNX model directory structure
- **02-60-08-A-103_Training_Dataset_Catalog.json** – Dataset catalog schema

### DPP Links
- **02-60-08-A-201_Blockchain_Anchors.json** – Blockchain hash anchors (no private keys)
- **02-60-08-A-202_Provenance_Hashes.csv** – Asset provenance hashes

---

## Technology Stack

- **MLflow** (model registry and tracking)
- **DVC** (Data Version Control for datasets)
- **Feast** (feature store)
- **ONNX** (model interchange format)
- **Blockchain** (Ethereum/Polygon for DPP anchoring)

---

## Model Lifecycle

```
Training → Validation → Staging → Production → Archived
   │          │           │           │           │
   └──────────┴───────────┴───────────┴───────────┘
                    │
              DPP Registration
         (Blockchain anchor, metadata)
```

---

## EU AI Act Compliance

Per [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206) requirements for high-risk AI systems:

- **Training Data Documentation**: Complete dataset provenance and characteristics
- **Model Documentation**: Architecture, training process, performance metrics
- **Traceability**: Immutable audit trail via blockchain anchoring
- **Retention**: Model artifacts retained for model lifetime + 5 years

---

## References

### Internal Documents
- [02-60-00-001 Storage Architecture Overview](../02-60-00-001_Storage_Architecture_Overview.md)
- ATA 95 Digital Product Passport: `OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/`

- [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206)
- [MLflow Documentation](https://www.mlflow.org/docs/latest/index.html)
- [DVC Documentation](https://dvc.org/doc)

---

## Document Control

- **Directory**: 02-60-08_ML_Model_Storage
- **Version**: 1.0
- **Status**: DRAFT
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.
