# 97-40-20-20-301 — RDP Accountant Notes

**Configuration and usage notes for RDP (Rényi Differential Privacy) Accountant**

---

## Document Control

| Field              | Value                                                           |
|--------------------|-----------------------------------------------------------------|
| **Document ID**    | 97-40-20-20-301_RDP_Accountant_Notes                            |
| **ATA Chapter**    | 97 — Neural Network Models / Digital Artifacts                  |
| **Bucket**         | 97-40-20 — FEDERATED_LEARNING                                   |
| **Sub-Bucket**     | 97-40-20-20 — PRIVACY_BUDGET                                    |
| **Version**        | 1.0                                                             |
| **Date**           | 2025-11-27                                                      |
| **Status**         | DRAFT                                                           |
| **Classification** | IMPLEMENTATION NOTES                                            |

---

## 1. Overview

RDP (Rényi Differential Privacy) is the preferred accounting method for AMPEL360 federated learning due to its tight composition bounds.

---

## 2. RDP Definition

For a mechanism M, the α-Rényi divergence between neighboring datasets D, D':

```
D_α(M(D) || M(D')) = (1/(α-1)) * log(E[(M(D)/M(D'))^(α-1)])
```

A mechanism satisfies (α, ε)-RDP if D_α ≤ ε for all neighboring datasets.

---

## 3. Orders Selection

### 3.1 Recommended Orders

```yaml
default_orders: [1.5, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500, 1000]
```

### 3.2 Rationale

- Lower orders (1.5-5): Better for high-noise regimes
- Higher orders (50-1000): Better for low-noise, many-step training
- Full range ensures tight bounds across configurations

---

## 4. Conversion to (ε, δ)-DP

To convert (α, ε_RDP) to (ε, δ)-DP:

```
ε_DP = min_α (ε_RDP(α) + log(1/δ) / (α - 1))
```

The minimum is computed across all tracked orders.

---

## 5. Implementation Libraries

| Library | Language | Notes |
|---------|----------|-------|
| Opacus | Python/PyTorch | Recommended for PyTorch |
| TF Privacy | Python/TensorFlow | For TensorFlow workflows |
| dp-accounting | Python | Standalone accountant |

---

## 6. AMPEL360 Integration

All RDP accounting must:

1. Use orders from approved configuration
2. Report to privacy budget tracker (97-40-20-20)
3. Log to CAOS/DPP with schema 97-40-20-20-901

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---
