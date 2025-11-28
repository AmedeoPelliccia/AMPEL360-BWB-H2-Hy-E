# 97-40-20-20-001 — Privacy Budget Model

**Formal specification of the privacy budget model for CFLF-GRAD**

---

## Document Control

| Field              | Value                                                           |
|--------------------|-----------------------------------------------------------------|
| **Document ID**    | 97-40-20-20-001_Privacy_Budget_Model                            |
| **ATA Chapter**    | 97 — Neural Network Models / Digital Artifacts                  |
| **Bucket**         | 97-40-20 — FEDERATED_LEARNING                                   |
| **Sub-Bucket**     | 97-40-20-20 — PRIVACY_BUDGET                                    |
| **Version**        | 1.0                                                             |
| **Date**           | 2025-11-27                                                      |
| **Status**         | DRAFT                                                           |
| **Classification** | SPECIFICATION                                                   |

---

## 1. Overview

This specification defines the formal privacy budget model used within AMPEL360 federated learning to track and enforce differential privacy guarantees.

---

## 2. Budget Definition

### 2.1 Privacy Parameters

| Parameter | Symbol | Definition |
|-----------|--------|------------|
| **Epsilon** | ε | Privacy loss parameter (lower = more private) |
| **Delta** | δ | Failure probability bound |

### 2.2 Budget Scopes

Privacy budgets are tracked at multiple scopes:

| Scope | Description | Typical Budget |
|-------|-------------|----------------|
| **Per-Model** | Budget per model family | ε ≤ 10 per training campaign |
| **Per-Aircraft** | Budget per physical asset | ε ≤ 5 per rolling year |
| **Per-Fleet** | Global fleet budget | ε ≤ 50 per rolling year |
| **Per-Region** | Regulatory domain budget | Varies by jurisdiction |

---

## 3. Composition Rules

### 3.1 Basic Composition

For sequential mechanisms M₁, M₂:
```
ε_total = ε₁ + ε₂
δ_total = δ₁ + δ₂
```

### 3.2 Advanced Composition (RDP)

Using Rényi Differential Privacy:
```
RDP(α) = log(E[exp((α-1) * privacy_loss)])
```

Convert to (ε, δ)-DP via:
```
ε = min_α (RDP(α) + log(1/δ) / (α-1))
```

---

## 4. Budget Lifecycle

### 4.1 Allocation
- Budgets allocated per model/aircraft at registration
- Default profiles from 97-40-20-20-101

### 4.2 Consumption
- Each DP-SGD run reports (ε, δ) spent
- Accumulated using composition rules

### 4.3 Exhaustion
- Warning at 80% consumption
- Hard stop at 95% consumption
- Renewal requires governance review

---

## 5. Traceability

| Trace Link | Reference |
|------------|-----------|
| DP-SGD Config | [97-40-20-10_DP_SGD](../../97-40-20-10_DP_SGD/) |
| Privacy Profiles | [97-40-20-20-101_Privacy_Profiles.yaml](../POLICIES/97-40-20-20-101_Privacy_Profiles.yaml) |
| Run Schema | [97-40-20-20-901_Privacy_Budget_Run.schema.json](../SCHEMAS/97-40-20-20-901_Privacy_Budget_Run.schema.json) |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---
