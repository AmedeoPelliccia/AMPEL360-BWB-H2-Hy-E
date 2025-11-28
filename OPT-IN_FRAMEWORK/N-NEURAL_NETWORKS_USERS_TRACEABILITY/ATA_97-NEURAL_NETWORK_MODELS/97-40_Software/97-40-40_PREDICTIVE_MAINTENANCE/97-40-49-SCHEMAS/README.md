# 97-40-49-SCHEMAS

## Purpose

This directory contains the data and model schemas for the Predictive
Maintenance neural network models.

## Schema Categories

| Schema Type | Format | Description |
|-------------|--------|-------------|
| Feature | JSON Schema | Feature vector definitions |
| Model | ONNX/Protobuf | Model interface definitions |
| Config | YAML | Training configuration |
| Metrics | JSON | Evaluation metrics format |

## Core Schemas

| Schema | Description |
|--------|-------------|
| rul_prediction.v1.json | RUL prediction output format |
| anomaly_score.v1.json | Anomaly detection output format |
| maintenance_schedule.v1.json | Optimization output format |
| model_metadata.v1.json | Model registry schema |

## Related Sections

- [23-95-69-SCHEMAS](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/23-95_COMM_NN/23-95-60_PROTOCOLS/23-95-69-SCHEMAS/) — Protocol schemas

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
