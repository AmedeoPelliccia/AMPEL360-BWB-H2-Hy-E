# 97-40-20-10-301 — DP-SGD Framework Guides

**Implementation notes for DP-SGD across ML frameworks**

---

## Document Control

| Field              | Value                                                           |
|--------------------|-----------------------------------------------------------------|
| **Document ID**    | 97-40-20-10-301_DP-SGD_Framework_Guides                         |
| **ATA Chapter**    | 97 — Neural Network Models / Digital Artifacts                  |
| **Bucket**         | 97-40-20 — FEDERATED_LEARNING                                   |
| **Sub-Bucket**     | 97-40-20-10 — DP_SGD                                            |
| **Version**        | 1.0                                                             |
| **Date**           | 2025-11-27                                                      |
| **Status**         | DRAFT                                                           |
| **Classification** | IMPLEMENTATION NOTES                                            |

---

## 1. Overview

This document provides framework-specific implementation guidance for DP-SGD within the AMPEL360 federated learning infrastructure.

---

## 2. PyTorch (Opacus)

### 2.1 Library Reference
- **Library**: Opacus (https://opacus.ai)
- **Version**: >= 1.0

### 2.2 Basic Setup

```python
from opacus import PrivacyEngine

privacy_engine = PrivacyEngine()
model, optimizer, dataloader = privacy_engine.make_private(
    module=model,
    optimizer=optimizer,
    data_loader=dataloader,
    noise_multiplier=config.noise_multiplier,
    max_grad_norm=config.clip_norm,
)
```

### 2.3 Privacy Accounting

```python
epsilon = privacy_engine.get_epsilon(delta=config.target_delta)
```

---

## 3. TensorFlow (TF Privacy)

### 3.1 Library Reference
- **Library**: TensorFlow Privacy
- **Version**: >= 0.8

### 3.2 Basic Setup

```python
from tensorflow_privacy.privacy.optimizers.dp_optimizer_keras import DPKerasSGDOptimizer

optimizer = DPKerasSGDOptimizer(
    l2_norm_clip=config.clip_norm,
    noise_multiplier=config.noise_multiplier,
    num_microbatches=config.batch_size,
    learning_rate=config.learning_rate
)
```

---

## 4. JAX (dp-accounting)

### 4.1 Library Reference
- **Library**: dp-accounting
- **Custom**: AMPEL360 JAX wrapper

### 4.2 Privacy Computation

```python
from dp_accounting import rdp_accountant

rdp = rdp_accountant.compute_rdp(
    q=sampling_rate,
    noise_multiplier=config.noise_multiplier,
    steps=num_steps,
    orders=orders
)
eps = rdp_accountant.get_privacy_spent(orders, rdp, target_delta=config.target_delta)
```

---

## 5. AMPEL360 Integration Requirements

All DP-SGD implementations must:

1. **Report configuration** to the privacy budget system (97-40-20-20)
2. **Use approved profiles** from 97-40-20-10-101
3. **Log run metadata** according to schema 97-40-20-10-901
4. **Attach AST-L descriptors** for CFLF-GRAD transmission

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---
