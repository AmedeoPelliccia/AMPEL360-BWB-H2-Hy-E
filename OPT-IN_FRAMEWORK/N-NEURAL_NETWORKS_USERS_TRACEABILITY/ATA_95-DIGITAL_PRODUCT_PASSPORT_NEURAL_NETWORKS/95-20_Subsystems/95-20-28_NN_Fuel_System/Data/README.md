# Data Directory — 95-20-28 NN Fuel System

This directory contains training datasets, validation datasets, and synthetic data for the Neural Network Fuel System models.

## Directory Structure

```
Data/
├── Training_Datasets/      # Real-world training data
├── Synthetic_Data/         # Digital twin and simulation data
└── README.md              # This file
```

## Training Datasets

### 95-20-28-601_Fuel_Quantity_Sensor_Logs.parquet

- **Size**: ~1.5 GB
- **Records**: 5,000+ flight hours
- **Features**: Tank level sensors, attitude data, fuel flow, temperature, pressure
- **Purpose**: Training data for Fuel Quantity Estimator (95-20-28-002)
- **Quality**: Validated, cleaned, representative of operational conditions

### 95-20-28-602_Fuel_Transfer_Events.parquet

- **Size**: ~800 MB
- **Records**: 10,000+ simulated scenarios
- **Features**: Tank levels, CG position, transfer commands, flight phase
- **Purpose**: Training data for Fuel Transfer Optimizer (95-20-28-004)
- **Quality**: Validated against flight test data and simulations

## Synthetic Data

### 95-20-28-605_Digital_Twin_Fuel_Scenarios.parquet

- **Size**: ~2.0 GB
- **Records**: 20,000+ synthetic scenarios
- **Features**: Complete fuel system state vectors
- **Purpose**: Augmentation for all models, edge case coverage
- **Source**: AMPEL360 Digital Twin Fuel System Simulator
- **Validation**: Verified against known physics and operational constraints

## Data Quality

### Validation Criteria

- **Completeness**: >99% for all features
- **Accuracy**: Cross-validated with reference measurements
- **Representativeness**: Covers all flight phases, environmental conditions, and operational scenarios
- **Diversity**: Multiple aircraft, seasons, flight profiles, operational contexts

### Data Governance

- **Provenance**: Complete lineage tracked in [95-20-02 DPP Blockchain](../../95-20-02_NN_DPP_Blockchain/)
- **Version Control**: All datasets versioned and immutable
- **Access Control**: Restricted to authorized personnel
- **Privacy**: No PII or sensitive operational data included

## Data Format

### Parquet Format

All datasets use Apache Parquet format for:
- Efficient columnar storage
- Schema enforcement
- Compression efficiency
- Fast query performance

### Schema Documentation

Detailed schema documentation available in:
- [Data_Dictionary.md](../Documentation/95-20-28_Data_Dictionary.md)

## Usage Guidelines

### Training

```python
import pandas as pd

# Load training data
df = pd.read_parquet('Training_Datasets/95-20-28-601_Fuel_Quantity_Sensor_Logs.parquet')

# Apply preprocessing
# ... (see model training configs)
```

### Validation

- Use 80/10/10 split (train/val/test) as specified in model configs
- Maintain temporal ordering for time-series data
- Ensure no data leakage between splits

### Synthetic Data Augmentation

- Blend synthetic data at 20-30% ratio with real data
- Validate that model performance doesn't degrade
- Use for edge cases and rare scenarios not well-represented in real data

## Data Updates

### Update Procedure

1. New data must be validated against quality criteria
2. Impact analysis on existing models
3. Version increment and documentation update
4. Blockchain provenance recording
5. Model retraining evaluation

### Data Retention

- Training data: Retained indefinitely for certification traceability
- Operational data: Anonymized and aggregated for continuous improvement
- Test data: Retained per certification requirements

## Certification Compliance

All datasets meet requirements for:
- **[DO-178C](https://www.rtca.org/product/do-178c/)**: Data quality and traceability
- **[EASA SC-AI](https://www.easa.europa.eu/en/document-library/general-publications/special-condition-sc-ai)**: Training data requirements for AI/ML systems
- **Data Protection**: GDPR and aviation data protection standards

## Document Control

- **Version**: 1.0  
- **Last Updated**: 2025-11-18  
- **Maintained By**: AMPEL360 ML Engineering Team

---

## Document Control – AI Involvement

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.  
- Status: **DRAFT** – Subject to human review and approval.  
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-18_.
