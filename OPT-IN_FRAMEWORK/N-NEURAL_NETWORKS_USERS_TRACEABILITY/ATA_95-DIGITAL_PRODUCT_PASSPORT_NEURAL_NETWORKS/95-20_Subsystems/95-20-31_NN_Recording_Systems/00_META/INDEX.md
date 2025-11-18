# 95-20-31 NN Recording Systems – Document Index

## Component Specifications

| ID | Document | Description | Status |
|----|----------|-------------|--------|
| 95-20-31-001 | [Recording_Systems_NN_Overview.md](../95-20-31-001_Recording_Systems_NN_Overview.md) | System architecture and overview | WORKING |
| 95-20-31-002 | [CVR_Transcription_And_Tagging.md](../95-20-31-002_CVR_Transcription_And_Tagging.md) | CVR speech-to-text system | WORKING |
| 95-20-31-003 | [FDR_Anomaly_Detector.md](../95-20-31-003_FDR_Anomaly_Detector.md) | FDR anomaly detection system | WORKING |
| 95-20-31-004 | [Event_Detection_And_Segmentation.md](../95-20-31-004_Event_Detection_And_Segmentation.md) | Event detection and segmentation | WORKING |
| 95-20-31-005 | [Data_Reduction_And_Compression_Optimizer.md](../95-20-31-005_Data_Reduction_And_Compression_Optimizer.md) | Data compression system | WORKING |
| 95-20-31-006 | [Maintenance_Log_Summarizer.md](../95-20-31-006_Maintenance_Log_Summarizer.md) | Maintenance report generation | WORKING |
| 95-20-31-007 | [Integration_with_ATA_31.md](../95-20-31-007_Integration_with_ATA_31.md) | ATA 31 integration specifications | WORKING |
| 95-20-31-008 | [Safety_and_Certification.md](../95-20-31-008_Safety_and_Certification.md) | Safety assessment and certification | WORKING |
| 95-20-31-009 | [Operational_Procedures.md](../95-20-31-009_Operational_Procedures.md) | Operational procedures and maintenance | WORKING |

## Model Cards

| Model ID | File | Model Name | Version | Status |
|----------|------|------------|---------|--------|
| 95-20-31-A-101 | [95-20-31-A-101_CVR_Transcriber_v1.0.yaml](../ASSETS/Model_Cards/95-20-31-A-101_CVR_Transcriber_v1.0.yaml) | CVR Transcriber | v1.0 | Development |
| 95-20-31-A-102 | [95-20-31-A-102_FDR_Anomaly_Detector_v1.0.yaml](../ASSETS/Model_Cards/95-20-31-A-102_FDR_Anomaly_Detector_v1.0.yaml) | FDR Anomaly Detector | v1.0 | Development |
| 95-20-31-A-103 | [95-20-31-A-103_Event_Segmenter_v1.0.yaml](../ASSETS/Model_Cards/95-20-31-A-103_Event_Segmenter_v1.0.yaml) | Event Segmenter | v1.0 | Development |

## Training Datasets

| Dataset ID | File | Description | Size |
|------------|------|-------------|------|
| 95-20-31-601 | [Data/Training_Datasets/95-20-31-601_CVR_Annotated_Audio.parquet](../Data/Training_Datasets/) | CVR annotated audio corpus | 2.5 TB |
| 95-20-31-602 | [Data/Training_Datasets/95-20-31-602_FDR_Events_and_Labels.parquet](../Data/Training_Datasets/) | FDR events with labels | 500 GB |
| 95-20-31-603 | [Data/Training_Datasets/95-20-31-603_Maintenance_Logs_Annotated.parquet](../Data/Training_Datasets/) | Maintenance logs corpus | 50 GB |
| 95-20-31-605 | [Data/Synthetic_Data/95-20-31-605_Digital_Twin_Recording_Scenarios.parquet](../Data/Synthetic_Data/) | Synthetic scenarios from digital twin | 100 GB |

## Diagrams and Schematics

| Asset ID | File | Description | Format |
|----------|------|-------------|--------|
| 95-20-31-D-001 | [ASSETS/Diagrams/95-20-31_System_Architecture.pdf](../ASSETS/Diagrams/) | System architecture diagram | PDF |

## Documentation

| File | Description |
|------|-------------|
| [95-20-31_API_Specs.md](../Documentation/95-20-31_API_Specs.md) | API specifications for NN interfaces |
| [95-20-31_Data_Dictionary.md](../Documentation/95-20-31_Data_Dictionary.md) | Data schemas and definitions |
| [95-20-31_Test_Strategy.md](../Documentation/95-20-31_Test_Strategy.md) | Testing approach and test cases |

## Models

### Configurations
- `Models/Configs/training_config_cvr_transcriber.yaml`
- `Models/Configs/training_config_fdr_anomaly.yaml`
- `Models/Configs/training_config_event_segmenter.yaml`

### Source Code
- `Models/Source/cvr_transcriber_v1.0.py`
- `Models/Source/fdr_anomaly_detector_v1.0.py`
- `Models/Source/event_segmenter_v1.0.py`

### Trained Models
- `Models/Trained/cvr_transcriber_v1.0.onnx`
- `Models/Trained/fdr_anomaly_detector_v1.0.onnx`
- `Models/Trained/event_segmenter_v1.0.onnx`

### Scripts
- `Models/Scripts/inspect_onnx_model.py`
- `Models/Scripts/test_onnx_model_recording.py`
- `Models/Scripts/deploy_to_ima_recording.py`

## Tests

### Unit Tests
- `Tests/Unit/test_cvr_transcriber.py`
- `Tests/Unit/test_fdr_anomaly.py`
- `Tests/Unit/test_event_segmenter.py`

### Integration Tests
- `Tests/Integration/test_recording_pipeline.py`
- `Tests/Integration/test_ata31_integration.py`

### Scenario Tests
- `Tests/Scenarios/95-20-31_Recording_Scenarios.md`

## Meta Information

| File | Description |
|------|-------------|
| [Traceability_Map_95-20-31.csv](Traceability_Map_95-20-31.csv) | Requirements traceability matrix |
| 95-20-31-011_NN_Recording_Taxonomy.md | Subsystem taxonomy |
| 95-20-31-012_NN_Recording_Assets_Registry.json | Asset registry |
| 95-20-31-013_CAOS_NN_Recording_Hooks.md | CAOS integration |

## Document Control

- **Version**: 1.0
- **Last Updated**: 2025-11-18
- **Maintained By**: Documentation Team
- **AI Assistance**: Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.

---
