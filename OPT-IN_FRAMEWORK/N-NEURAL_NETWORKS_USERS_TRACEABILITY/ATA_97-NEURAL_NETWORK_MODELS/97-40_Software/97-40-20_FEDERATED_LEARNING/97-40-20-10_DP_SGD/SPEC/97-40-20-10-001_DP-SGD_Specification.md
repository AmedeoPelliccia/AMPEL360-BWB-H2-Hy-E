# 97-40-20-10-001 — DP-SGD Specification

**Formal specification for Differentially Private SGD within CFLF-GRAD**

---

## Document Control

| Field              | Value                                                           |
|--------------------|-----------------------------------------------------------------|
| **Document ID**    | 97-40-20-10-001_DP-SGD_Specification                            |
| **ATA Chapter**    | 97 — Neural Network Models / Digital Artifacts                  |
| **Bucket**         | 97-40-20 — FEDERATED_LEARNING                                   |
| **Sub-Bucket**     | 97-40-20-10 — DP_SGD                                            |
| **Version**        | 1.0                                                             |
| **Date**           | 2025-11-27                                                      |
| **Status**         | DRAFT                                                           |
| **Classification** | SPECIFICATION                                                   |
| **Owner**          | N — Neural Networks Users Traceability WG (ATA 95/97)           |
| **Programme**      | AMPEL360-BWB-H₂-Hy-E Q100                                       |

---

## 1. Overview

This specification defines the formal algorithmic approach to **Differentially Private Stochastic Gradient Descent (DP-SGD)** as applied within the AMPEL360 federated learning framework.

---

## 2. Algorithm Definition

### 2.1 Per-Sample Gradient Computation

For a mini-batch of size `B`, compute gradients individually for each sample `i`:

```
g_i = ∇_θ L(θ, x_i, y_i)
```

### 2.2 Gradient Clipping

Clip each per-sample gradient to bound its L2 norm:

```
g̃_i = g_i / max(1, ||g_i||_2 / C)
```

Where `C` is the clipping threshold (`clip_norm`).

### 2.3 Noise Addition

Add calibrated Gaussian noise to the averaged clipped gradients:

```
ḡ = (1/B) * Σ g̃_i + N(0, σ² * C² * I)
```

Where `σ = noise_multiplier`.

### 2.4 Parameter Update

Apply the noised gradient to update model parameters:

```
θ_{t+1} = θ_t - η * ḡ
```

Where `η` is the learning rate.

---

## 3. Privacy Guarantee

For `T` training steps with sampling rate `q = B/N`, the mechanism satisfies (ε, δ)-differential privacy where:

- ε and δ are computed using the RDP accountant or Moments accountant
- Tighter bounds available via privacy amplification by subsampling

---

## 4. Traceability

| Trace Link | Reference |
|------------|-----------|
| Privacy Budget | [97-40-20-20_PRIVACY_BUDGET](../../97-40-20-20_PRIVACY_BUDGET/) |
| Configuration | [97-40-20-10-101_DP-SGD_Profiles.yaml](../CONFIG/97-40-20-10-101_DP-SGD_Profiles.yaml) |
| Schemas | [97-40-20-10-901_DP-SGD_Run_Metadata.schema.json](../SCHEMAS/97-40-20-10-901_DP-SGD_Run_Metadata.schema.json) |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---
