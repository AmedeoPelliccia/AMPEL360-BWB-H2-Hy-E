# 97-40-20-10_DP_SGD — Differentially Private SGD

**Differentially Private Stochastic Gradient Descent for CFLF-GRAD**

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
| **Classification** | ALGORITHM / PRIVACY / GOVERNANCE                                |
| **Owner**          | N — Neural Networks Users Traceability WG (ATA 95/97)           |
| **Programme**      | AMPEL360-BWB-H₂-Hy-E Q100                                       |

---

## 1. Purpose

This document defines the **governance, conceptual design and parameterization** of  
**Differentially Private Stochastic Gradient Descent (DP-SGD)** used within the  
**97-40-20 FEDERATED_LEARNING** bucket and the **CFLF-GRAD** fabric.

It provides a reference for:

- How DP-SGD is configured and applied in AMPEL360 federated learning.
- Which parameters are **tunable** and which are **constrained by governance**.
- How DP-SGD integrates with **privacy budgeting (97-40-20-20)** and **CFLF-GRAD channels**.

---

## 2. Scope

The scope of this document includes:

1. **DP-SGD Algorithm Overview**
   - Per-sample gradient computation.
   - Gradient clipping strategies.
   - Gaussian noise injection.

2. **Key Parameters & Configuration**
   - `clip_norm` (L2 clipping threshold).
   - `noise_multiplier` (σ for Gaussian noise).
   - Batch composition and sampling rates.
   - Number of training steps / rounds.

3. **Privacy Accounting Integration**
   - Interfaces with the **97-40-20-20_PRIVACY_BUDGET** bucket.
   - Passing effective ε, δ to DPP / CAOS for traceability.

4. **CFLF-GRAD Integration**
   - Consistency of DP-SGD configuration across **A/G/R/F nodes**.
   - Constraints for **CFLF-GRAD** (gradient channel) and **CFLF-MODEL**.

Implementation details (code, libraries, concrete frameworks) are captured in  
sub-documents under this same directory.

---

## 3. Position in OPT-IN & ATA

### 3.1 OPT-IN Axes

DP-SGD sits primarily on the **N — NEURAL_NETWORKS_USERS_TRACEABILITY** axis:

- Defines **how gradients are computed and privatized** before leaving the node.
- Ensures that **user, aircraft and mission data** are protected by design.
- Exposes configuration and accounting hooks to **CAOS** and **DPP**.

It interacts with:

- **T / L2-LINKS (ATA 23)** for transport of **DP-masked gradients** (CFLF-GRAD).
- **I — INFRASTRUCTURES (AirCCC / CAOS)** for deployment and orchestration.

### 3.2 Relevant ATA Chapters

- **ATA 97** – Home of this bucket (model artifacts & lifecycle).
- **ATA 95** – Neural Networks safety/governance framework.
- **ATA 23** – Communications channels carrying gradients and models.
- **ATA 02 / 42** – Operational context and compute platforms where training runs.

---

## 4. DP-SGD Conceptual Overview

DP-SGD in AMPEL360 follows the standard pattern:

1. **Per-Sample Gradients**
   - For each mini-batch, gradients are computed **per training example** (or per small group).

2. **L2 Gradient Clipping**
   - Each per-sample gradient is clipped to an L2 norm of at most `clip_norm`:
     - Large gradients are scaled down to avoid any single sample dominating.

3. **Gaussian Noise Injection**
   - After averaging the clipped gradients, **Gaussian noise** with standard deviation
     proportional to `noise_multiplier × clip_norm` is added.

4. **Parameter Update**
   - The noised, clipped gradient is used to update model parameters via SGD or a variant.

5. **Privacy Accounting**
   - A **privacy accountant** tracks the cumulative (ε, δ) using:
     - Sampling rate.
     - Number of steps / rounds.
     - `noise_multiplier`.

All these steps must be **deterministically configurable and auditable** for each federated learning run.

---

## 5. Key Parameters

### 5.1 Core Parameters

| Parameter         | Type    | Description                                                         | Governance Notes                               |
|-------------------|---------|---------------------------------------------------------------------|------------------------------------------------|
| `clip_norm`       | float   | L2 norm upper bound for per-sample gradients                        | Must be defined per model / use case           |
| `noise_multiplier`| float   | σ multiplier for Gaussian noise (relative to `clip_norm`)           | Direct impact on ε; subject to policy bounds   |
| `batch_size`      | int     | Local batch size for DP-SGD                                         | Influences privacy amplification               |
| `sampling_rate`   | float   | Fraction of dataset sampled per step                                | Input to privacy accountant                    |
| `num_steps`       | int     | Number of DP-SGD steps per round or epoch                           | Contributes to total ε                         |
| `learning_rate`   | float   | Step size for gradient updates                                      | Standard training hyperparameter               |
| `momentum`        | float   | Momentum term (if used)                                             | Optional                                       |

### 5.2 Governance Constraints (examples)

Concrete values are defined in configuration files under this bucket, but typical rules include:

- **Minimum `noise_multiplier`** for given use cases (e.g. passenger telemetry vs synthetic data).
- **Maximum `num_steps`** per privacy budget period.
- **Fixed / bounded `clip_norm`** per model family (H₂, PredMaint, ANCHORS, etc.).

---

## 6. Interfaces & Artifacts (97-40-20-10)

Within this directory, DP-SGD is represented by:

- **Specifications**
  - `DP-SGD-SPEC.md` — Algorithm details, equations, proofs outline.
- **Configuration Templates**
  - YAML/JSON configs with allowed ranges and defaults for key parameters.
- **Implementation Notes**
  - Pseudocode and framework-specific guidance (e.g. PyTorch, JAX, TF).
- **Test & Evaluation Reports**
  - Privacy–utility trade-off studies.
  - Ablation on `clip_norm`, `noise_multiplier`, and batch sizes.

All artifacts **must be traceable** to:

- Specific **models** under `97-40-20-80_MODELS/`.
- Specific **federated runs** recorded via DPP and CAOS events.

---

## 7. Integration with CFLF-GRAD & AST-L

DP-SGD is a **local node mechanism** that prepares gradients for the **CFLF-GRAD channel**:

- **Before transmission**:
  - Gradients are **clipped and noised** according to this specification.
  - Metadata describing the DP configuration (e.g. `(clip_norm, noise_multiplier, ε, δ)` range)
    is attached using **AST-L (AMPEL360 AirSynTech Language)** descriptors.

- **On the wire (23-95 / L2-LINKS)**:
  - Gradients are wrapped into a **`gradient_envelope`** schema and then transported via
    `CFLF-GRAD` channel, as defined in **23-95_COMM_NN**.

- **At aggregation nodes (G/R/F)**:
  - Only DP-processed gradients are accepted.
  - Any deviation (e.g. missing DP metadata) is treated as a **policy violation**.

---

## 8. Safety & Governance Considerations

Even when used primarily for **non-safety channels**:

1. **Policy Enforcement**
   - DP-SGD configuration must be loaded from **signed configuration artifacts**.
   - Runtime can only select from **approved profiles**, not arbitrary values.

2. **Auditability**
   - For each training run, the following must be recorded:
     - Model ID (DPP reference).
     - DP-SGD configuration profile ID.
     - Aggregated privacy budget consumed (ε, δ).
     - CFLF channels used and nodes involved.

3. **Safety-Adjacent Uses**
   - For channels like **CFLF-SAFETY**, any DP-SGD usage must:
     - Be aligned with safety case documentation under ATA 95.
     - Be explicitly listed in model assurance documentation.

---

## 9. Directory Structure (97-40-20-10_DP_SGD)

Expected internal structure with consistent ID numbering:

```text
97-40-20-10_DP_SGD/
├── README.md                                          # This file (97-40-20-10-000)
├── SPEC/
│   └── 97-40-20-10-001_DP-SGD_Specification.md       # Formal specification
├── CONFIG/
│   ├── 97-40-20-10-101_DP-SGD_Profiles.yaml          # Approved DP profiles
│   └── 97-40-20-10-102_DP-SGD_Defaults.yaml          # Default parameters
├── IMPLEMENTATION_NOTES/
│   └── 97-40-20-10-301_DP-SGD_Framework_Guides.md    # Framework-specific notes
├── TESTS/
│   └── 97-40-20-10-701_Privacy_Utility_Reports.md    # Trade-off evaluations
└── SCHEMAS/
    └── 97-40-20-10-901_DP-SGD_Run_Metadata.schema.json  # CAOS/DPP logging
```

**ID Numbering Convention:**
- `0xx` → Specifications (formal documents)
- `1xx` → Configuration (profiles, defaults)
- `3xx` → Implementation notes
- `7xx` → Tests and evaluation reports
- `9xx` → Schemas and machine-readable artifacts

This structure can evolve as the program grows, but **README.md remains the anchor** for the bucket.

---

## 10. Related Documents

* `97-40-20-00_GENERAL/README.md` — Federated Learning General (CFLF-GRAD overview).
* `97-40-20-20_PRIVACY_BUDGET/` — Privacy accounting and budget policies.
* `97-40-20-80_MODELS/` — Models trained with DP-SGD.
* `T-.../ATA_23-COMMUNICATIONS/23-95_COMM_NN/` — Gradient/channel transport.
* `T-.../ATA_23-COMMUNICATIONS/23-96_AIR_SYNTECH_LANGUAGE/` — AST-L semantics.
* `CAOS/CAOS_CROSS_ATA_MAP.md` — Integration in CAOS autonomy backbone.
* `DPP/` (ATA 97) — Lifecycle traceability for federated models and runs.

---

## Authorship & Review

* **Authorship:** Content generated through prompt engineering methods using AI assistants and agent tools, prompted and partially reviewed by **Amedeo Pelliccia**, with automated checking tools for validation.
* **Status:** **DRAFT** – Subject to human review and approval.
* **Human approver:** *[to be completed]*.
* **Repository:** `AMPEL360-BWB-H2-Hy-E`
* **Last AI update:** *2025-11-27*.


