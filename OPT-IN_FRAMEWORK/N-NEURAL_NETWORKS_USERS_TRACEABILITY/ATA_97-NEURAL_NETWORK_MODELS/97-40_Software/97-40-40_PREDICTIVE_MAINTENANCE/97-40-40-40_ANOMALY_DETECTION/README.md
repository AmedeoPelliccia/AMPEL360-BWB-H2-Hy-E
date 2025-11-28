# 97-40-40-40_ANOMALY_DETECTION — Anomaly Detection Models

## Purpose

This section contains the neural network models for detecting anomalies in aircraft telemetry data that may indicate emerging failures or degradation.

## Anomaly Detection Approaches

| Approach | Model Type | Use Case |
|----------|------------|----------|
| Reconstruction | Autoencoder | Time-series anomalies |
| Classification | One-class NN | Known failure modes |
| Clustering | Deep clustering | Unknown patterns |
| Hybrid | Ensemble | Production deployment |

## Model Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Telemetry Input                           │
└───────────────────────────┬─────────────────────────────────┘
                            │
       ┌────────────────────┼────────────────────┐
       │                    │                    │
┌──────▼──────┐      ┌──────▼──────┐      ┌──────▼──────┐
│ Autoencoder │      │  One-class  │      │    Deep     │
│   (Recon)   │      │    NN       │      │  Clustering │
└──────┬──────┘      └──────┬──────┘      └──────┬──────┘
       │                    │                    │
       └────────────────────┼────────────────────┘
                            │
                    ┌───────▼───────┐
                    │   Ensemble    │
                    │   Combiner    │
                    └───────┬───────┘
                            │
                    ┌───────▼───────┐
                    │ Anomaly Score │
                    │  & Alert      │
                    └───────────────┘
```

## Alert Thresholds

| Severity | Score Range | Action |
|----------|-------------|--------|
| Normal | < 0.3 | No action |
| Warning | 0.3 - 0.7 | Monitor closely |
| Alert | 0.7 - 0.9 | Maintenance review |
| Critical | > 0.9 | Immediate inspection |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
