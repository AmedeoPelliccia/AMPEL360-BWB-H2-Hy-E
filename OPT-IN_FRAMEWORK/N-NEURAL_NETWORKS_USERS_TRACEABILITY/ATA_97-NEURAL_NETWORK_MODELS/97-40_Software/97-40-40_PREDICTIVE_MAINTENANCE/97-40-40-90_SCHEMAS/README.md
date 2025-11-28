# 97-40-40-90_SCHEMAS — PMT Model Schemas

## Purpose

This directory contains the data and model schemas for the Predictive Maintenance neural network models.

## Schema Categories

| Schema Type | Format | Description |
|-------------|--------|-------------|
| Feature | JSON Schema | Feature vector definitions |
| Model | ONNX/Protobuf | Model interface definitions |
| Config | YAML | Training configuration |
| Metrics | JSON | Evaluation metrics format |

## Schema Versioning

Schemas follow semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR**: Breaking changes requiring consumer updates
- **MINOR**: Backward-compatible additions
- **PATCH**: Backward-compatible fixes

## Core Schemas

| Schema | Description |
|--------|-------------|
| rul_prediction.v1.json | RUL prediction output format |
| anomaly_score.v1.json | Anomaly detection output format |
| maintenance_schedule.v1.json | Optimization output format |
| model_metadata.v1.json | Model registry schema |

## Cross-References

| Schema | Used By |
|--------|---------|
| feature_vector.v1.json | 97-40-40-20 Feature Engineering |
| rul_prediction.v1.json | 97-40-40-30 RUL Models |
| anomaly_score.v1.json | 97-40-40-40 Anomaly Detection |
| maintenance_schedule.v1.json | 97-40-40-50 Maintenance Optimization |
| caos_interface.v1.json | 97-40-40-60 CAOS Integration |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
