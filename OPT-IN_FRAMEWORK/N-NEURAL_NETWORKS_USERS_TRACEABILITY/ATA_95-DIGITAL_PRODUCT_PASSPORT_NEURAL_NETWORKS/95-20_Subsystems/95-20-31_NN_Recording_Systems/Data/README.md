# 95-20-31 NN Recording Systems – Training Data

This directory contains training datasets, validation data, and synthetic data for the NN Recording Systems models.

## Directory Structure

```
Data/
├── Training_Datasets/
│   ├── 95-20-31-601_CVR_Annotated_Audio.parquet
│   ├── 95-20-31-602_FDR_Events_and_Labels.parquet
│   └── 95-20-31-603_Maintenance_Logs_Annotated.parquet
├── Synthetic_Data/
│   └── 95-20-31-605_Digital_Twin_Recording_Scenarios.parquet
└── README.md (this file)
```

## Training Datasets

### 95-20-31-601: CVR Annotated Audio
**Purpose**: Training data for CVR Transcription and Tagging model  
**Size**: ~2.5 TB  
**Format**: Parquet (audio as binary, metadata as structured)  
**Content**:
- 10,000+ hours of cockpit audio (4 channels)
- Speaker labels (Captain, F/O, ATC, Other)
- Transcribed text
- Event keyword annotations
- Flight phase metadata

**Sources**:
- Commercial flight recordings (anonymized): 7,000 hours
- Simulator sessions: 2,500 hours
- Synthetic audio: 500 hours

**Quality Metrics**:
- Completeness: 99.5%
- Annotation agreement: 95%+
- Noise level: Varied (40-85 dB)

### 95-20-31-602: FDR Events and Labels
**Purpose**: Training data for FDR Anomaly Detector  
**Size**: ~500 GB  
**Format**: Parquet (time-series data)  
**Content**:
- 50,000+ flight hours
- 50+ critical FDR parameters
- Anomaly labels (ground truth)
- Flight phase annotations
- Aircraft configuration data

**Sources**:
- Normal operations: 48,000 hours
- Known anomalies: 1,500 hours
- Synthetic edge cases: 500 hours

**Anomaly Types**:
- Engine: 450 hours
- Flight controls: 300 hours
- Hydraulics: 250 hours
- Electrical: 200 hours
- Environmental: 150 hours
- Multiple systems: 150 hours

### 95-20-31-603: Maintenance Logs Annotated
**Purpose**: Training data for Maintenance Log Summarizer  
**Size**: ~50 GB  
**Format**: Parquet (text + structured data)  
**Content**:
- 50,000+ human-written maintenance logs
- Corresponding event data (CVR/FDR)
- Flight metadata
- Maintenance action records

**Languages**: English (primary), Spanish, French, German

## Synthetic Data

### 95-20-31-605: Digital Twin Recording Scenarios
**Purpose**: Synthetic data for edge cases and rare events  
**Size**: ~100 GB  
**Format**: Parquet  
**Content**:
- 500+ hours of digital twin-generated CVR/FDR data
- Rare failure modes
- Extreme environmental conditions
- Novel aircraft configurations

**Generation Method**: Physics-based digital twin simulation ([CAOS](../../../../CAOS/))

## Data Access and Security

### Access Controls
- **Classification**: Sensitive (contains operational data)
- **Encryption**: AES-256 at rest, TLS 1.3 in transit
- **Access**: Restricted to ML engineering team + authorized personnel
- **Audit**: All access logged

### Privacy Considerations
- CVR audio anonymized (speaker identities removed)
- Aircraft registration numbers redacted
- Flight routes generalized (not specific flights)
- No personally identifiable information (PII)

### Regulatory Compliance
- Complies with GDPR (EU)
- Complies with CCPA (California)
- No data from active investigations
- Retention policy: 7 years from last use

## Data Versioning

Datasets are versioned using semantic versioning:
- Major version: Significant data additions or schema changes
- Minor version: Data quality improvements or minor additions
- Patch version: Bug fixes or metadata corrections

**Current Versions**:
- 95-20-31-601: v1.0.0
- 95-20-31-602: v1.0.0
- 95-20-31-603: v1.0.0
- 95-20-31-605: v1.0.0

## Data Provenance

All datasets tracked in:
- [95-20-02 NN DPP Blockchain](../../95-20-02_NN_DPP_Blockchain/) – Provenance chain
- [95-00-13 Subsystems Components](../../../95-00_GENERAL/95-00-13_Subsystems_Components/) – Component data references

**Hashes** (SHA-256):
- 95-20-31-601: `sha256:95-20-31-601-cvr-audio-v1.0`
- 95-20-31-602: `sha256:95-20-31-602-fdr-events-v1.0`
- 95-20-31-603: `sha256:95-20-31-603-maint-logs-v1.0`
- 95-20-31-605: `sha256:95-20-31-605-synthetic-v1.0`

## Data Quality Assurance

### Validation Checks
- Schema validation (Parquet structure)
- Range checks (parameter values)
- Completeness checks (missing data)
- Consistency checks (cross-validation)
- Label quality (inter-annotator agreement)

### Quality Metrics
- **CVR Audio**: SNR, clipping detection, channel balance
- **FDR Data**: Parameter coverage, anomaly label quality
- **Maintenance Logs**: Text quality, annotation completeness

### Issues and Corrections
Tracked in: `Data/ISSUES.md` (to be created)

## Usage

### Loading Data (Example)

```python
import pyarrow.parquet as pq

# Load CVR data
cvr_data = pq.read_table('Training_Datasets/95-20-31-601_CVR_Annotated_Audio.parquet')

# Load FDR data
fdr_data = pq.read_table('Training_Datasets/95-20-31-602_FDR_Events_and_Labels.parquet')
```

### Data Splits

Recommended splits:
- Training: 70-80%
- Validation: 10-15%
- Test: 10-15%

**Important**: Test set must be held out (not used for any training or hyperparameter tuning)

## References

- [95-20-31-001 Recording Systems NN Overview](../95-20-31-001_Recording_Systems_NN_Overview.md)
- [95-00-13 Subsystems Components](../../../95-00_GENERAL/95-00-13_Subsystems_Components/)
- [95-20-02 NN DPP Blockchain](../../95-20-02_NN_DPP_Blockchain/)

## Document Control

- **Version**: 1.0
- **Last Updated**: 2025-11-18
- **Maintained By**: ML Engineering Team
- **AI Assistance**: Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: **DRAFT** – Subject to human review and approval.
- **Human approver**: _[to be completed]_.

---
