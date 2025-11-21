# 02-90-06: ML/AI Training Datasets

## Purpose

This folder documents ML/AI training datasets, schemas, metadata, and [Digital Product Passport (DPP)](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md) links for traceable AI use.

## Scope

ML training dataset documentation includes:

- **Dataset Catalog**: Inventory of all training datasets
- **Feature Definitions**: Feature engineering documentation
- **Training Data Lineage**: Provenance tracking from source to model
- **DPP Integration**: Blockchain anchors for immutable dataset provenance

All datasets are **metadata-only** in this repository. Actual training data is stored in secure data lakes with appropriate access controls.

## Structure

```
02-90-06_ML_Training_Datasets/
├── README.md (this file)
├── 02-90-06-001_Dataset_Catalog.md
├── 02-90-06-002_Feature_Definitions.md
├── 02-90-06-003_Training_Data_Lineage.md
└── ASSETS/
    ├── Catalog/          # Dataset registry and versions
    ├── Schemas/          # Parquet schemas and feature store definitions
    ├── Metadata/         # Dataset statistics and quality reports
    └── DPP_Links/        # Blockchain anchors and provenance hashes
```

## Key Components

### Dataset Catalog

[Dataset registry](./ASSETS/Catalog/02-90-06-A-001_Dataset_Registry.yaml) includes:

- Dataset name and description
- Purpose (what models use it)
- Owners and stewards
- Storage location (reference only)
- Access controls and governance
- Version history

### Feature Definitions

[Feature documentation](./02-90-06-002_Feature_Definitions.md) specifies:

- Feature name and data type
- Description and business meaning
- Source system or transformation
- Valid ranges and distributions
- Missing value handling
- Update frequency

### Training Data Lineage

[Lineage tracking](./02-90-06-003_Training_Data_Lineage.md) documents:

- Source systems (operations, telemetry, etc.)
- Extraction timestamps
- Transformation steps (cleaning, normalization, augmentation)
- Quality checks applied
- Dataset versions and snapshots
- Links to [DPP](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md)

## DPP Integration

Integration with [ATA 95 Digital Product Passport](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md):

### Blockchain Anchors

[Dataset blockchain anchors](./ASSETS/DPP_Links/02-90-06-A-301_Dataset_Blockchain_Anchors.csv) provide:

- Dataset ID
- Version hash (SHA-256 of dataset metadata + sample)
- Blockchain transaction ID
- Timestamp of anchor
- DPP reference

### Provenance Hashes

[Provenance hashes](./ASSETS/DPP_Links/02-90-06-A-302_Training_Provenance_Hashes.json) link:

- Raw data sources → Processed datasets
- Datasets → Trained models
- Models → Deployments

## Dataset Types

### Flight Operations Datasets

- **Purpose**: Train models for delay prediction, flight optimization
- **Sources**: [Flight Operations Schema](../02-90-01_Database_Schemas/ASSETS/SQL/02-90-01-A-001_Flight_Operations_Schema.sql)
- **Features**: Flight duration, delays, weather, airport congestion

### Energy Data Datasets

- **Purpose**: Energy consumption prediction, anomaly detection
- **Sources**: [Energy Monitoring Schema](../02-90-01_Database_Schemas/ASSETS/SQL/02-90-01-A-003_Energy_Monitoring_Schema.sql)
- **Features**: Power consumption, voltage, current, phase of flight

### Performance Datasets

- **Purpose**: Performance optimization, predictive maintenance
- **Sources**: [Performance Data Schema](../02-90-01_Database_Schemas/ASSETS/SQL/02-90-01-A-002_Performance_Data_Schema.sql)
- **Features**: Takeoff distance, fuel efficiency, climb performance

## Governance and Compliance

### Data Governance

- **Privacy**: No PII (Personally Identifiable Information)
- **Security**: Synthetic or anonymized data only in public repos
- **Quality**: Mandatory data quality checks before training
- **Audit**: All dataset access logged

### Regulatory Compliance

Aligned with:

- [EU AI Act](https://artificialintelligenceact.eu/) – Transparency and data governance requirements
- [GDPR](https://gdpr.eu/) – Data protection (where applicable)
- [DO-178C](https://en.wikipedia.org/wiki/DO-178C) – Software development for safety-critical systems

### Bias and Fairness

- **Bias analysis**: Required for all datasets
- **Fairness metrics**: Documented per use case
- **Mitigation**: Strategies for identified biases

## Usage Guidelines

### For Data Scientists

1. **Review catalog**: Find appropriate dataset
2. **Check provenance**: Verify data lineage
3. **Validate quality**: Review quality reports
4. **Document usage**: Log dataset in model card
5. **Link to DPP**: Reference blockchain anchor

### For ML Engineers

1. **Load from registry**: Use dataset ID for reproducibility
2. **Version control**: Pin dataset version in training config
3. **Monitor drift**: Track distribution changes over time
4. **Update lineage**: Record model training in provenance

### For Auditors

1. **Verify provenance**: Check blockchain anchors
2. **Review quality**: Audit quality reports
3. **Check compliance**: Validate governance controls
4. **Trace usage**: Follow dataset → model → deployment chain

## Cross-References

- [02-90-00-002 Data Dictionary](../02-90-00-002_Data_Dictionary_Master.md)
- [02-90-01 Database Schemas](../02-90-01_Database_Schemas/README.md)
- [ATA 95 Digital Product Passport](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md)
- [EU AI Act](https://artificialintelligenceact.eu/)
- [DO-178C](https://en.wikipedia.org/wiki/DO-178C)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
