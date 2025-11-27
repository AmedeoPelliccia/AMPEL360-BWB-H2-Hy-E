# CFLF-GRAD OPT-IN Structure — Master Mapping

**Version:** 1.0  
**Date:** 2025-11-27  
**Status:** Draft  
**Related Standard:** AMPEL360-FAirCCC-ARCH-001 §4.1, §7

---

## Purpose

This document provides the master mapping for the **CFLF-GRAD (Collaborative Federated Learning Fabric - Gradient)** channel across the OPT-IN Framework dual-location architecture.

---

## Channel Overview

| Attribute | Value |
|-----------|-------|
| **Channel** | CFLF-GRAD |
| **Direction** | Aircraft → Ground → Regional → Fleet Core |
| **Data** | DP-masked sparse gradient deltas |
| **Safety** | Non-safety only |

---

## Dual-Location Architecture

```
OPT-IN_FRAMEWORK/
│
├── N-NEURAL_NETWORKS_USERS_TRACEABILITY/    ← What to Learn
│   └── ATA_97-NEURAL_NETWORK_MODELS/
│       └── 97-40_Software/
│           └── 97-40-20_FEDERATED_LEARNING/   ← CFLF-GRAD (Learning)
│               ├── 97-40-20-00_GENERAL/
│               ├── 97-40-20-10_DP_SGD/
│               ├── 97-40-20-20_PRIVACY_BUDGET/
│               ├── 97-40-20-30_COMPRESSION/
│               ├── 97-40-20-40_LOCAL_TRAINING/
│               ├── 97-40-20-50_AGGREGATION/
│               ├── 97-40-20-60_MODEL_GOVERNANCE/
│               ├── 97-40-20-70_EVALUATION/
│               ├── 97-40-20-80_MODELS/
│               └── 97-40-20-90_SCHEMAS/
│
└── T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/  ← How to Transmit
    └── L2-LINKS/
        └── ATA_23-COMMUNICATIONS/
            └── 23-95_COMM_NN/
                └── 23-95-60_PROTOCOLS/
                    └── 60-10_CFLF_GRAD/
```

---

## Separation of Concerns

| Aspect | N-Axis (97-40-20) | L2-LINKS (23-95-60-10) |
|--------|-------------------|------------------------|
| **Focus** | What to learn | How to transmit |
| **Content** | DP-SGD, privacy budget, aggregation | Feature gate, transport, SecAgg |
| **Schemas** | Gradient format schema | Transport envelope schema |

---

## N-Axis Structure (97-40-20_FEDERATED_LEARNING)

| Bucket | Purpose |
|--------|---------|
| `97-40-20-00_GENERAL` | General governance and overview |
| `97-40-20-10_DP_SGD` | Differentially Private SGD implementation |
| `97-40-20-20_PRIVACY_BUDGET` | ε,δ tracking per model/aircraft |
| `97-40-20-30_COMPRESSION` | Top-k sparsification + quantization |
| `97-40-20-40_LOCAL_TRAINING` | On-aircraft training procedures |
| `97-40-20-50_AGGREGATION` | FedAvg/FedAdam aggregation logic |
| `97-40-20-60_MODEL_GOVERNANCE` | Model lifecycle and approval gates |
| `97-40-20-70_EVALUATION` | Evaluation battery and drift gates |
| `97-40-20-80_MODELS` | Model artifacts and weights |
| `97-40-20-90_SCHEMAS` | CBOR/JSON schemas for gradients |

---

## L2-LINKS Structure (23-95-60-10)

| Aspect | Description |
|--------|-------------|
| **Transport** | mTLS (TLS 1.3), CBOR envelopes |
| **Security** | TPM-anchored signatures, secure aggregation |
| **Validation** | Schema validation, DP budget checks |

---

## Key Documents

| Document | Location |
|----------|----------|
| [CFLF-GRAD Channel Spec](../CAOS/channels/cflf-grad.md) | CAOS channel definition |
| [97-40-20 README](N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_97-NEURAL_NETWORK_MODELS/97-40_Software/97-40-20_FEDERATED_LEARNING/README.md) | N-Axis bucket |
| [60-10 README](T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/23-95_COMM_NN/23-95-60_PROTOCOLS/60-10_CFLF_GRAD/README.md) | L2-LINKS protocol |
| [23-95 README](T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/23-95_COMM_NN/README.md) | COMM_NN overview |

---

## Related Channels

| Channel | N-Axis | L2-Axis |
|---------|--------|---------|
| **CFLF-GRAD** | 97-40-20 | 23-95-60-10 |
| **CFLF-MODEL** | 97-40-30 | 23-95-60-20 |
| **CFLF-TELEM** | 97-40-20 | 23-95-60-30 |
| **CFLF-SAFETY** | 97-40-30 | 23-95-60-40 |
| **CUC** | 97-40-30 | 23-95-60-50 |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---
