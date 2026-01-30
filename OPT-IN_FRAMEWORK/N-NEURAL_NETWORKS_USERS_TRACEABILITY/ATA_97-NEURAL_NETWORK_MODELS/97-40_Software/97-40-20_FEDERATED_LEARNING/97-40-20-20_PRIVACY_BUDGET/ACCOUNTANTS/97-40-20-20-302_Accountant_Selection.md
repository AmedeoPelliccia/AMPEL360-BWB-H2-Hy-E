# 97-40-20-20-302 — Accountant Selection

**Criteria and rationale for privacy accountant selection**

---

## Document Control

| Field              | Value                                                           |
|--------------------|-----------------------------------------------------------------|
| **Document ID**    | 97-40-20-20-302_Accountant_Selection                            |
| **ATA Chapter**    | 97 — Neural Network Models / Digital Artifacts                  |
| **Bucket**         | 97-40-20 — FEDERATED_LEARNING                                   |
| **Sub-Bucket**     | 97-40-20-20 — PRIVACY_BUDGET                                    |
| **Version**        | 1.0                                                             |
| **Date**           | 2025-11-27                                                      |
| **Status**         | DRAFT                                                           |
| **Classification** | IMPLEMENTATION NOTES                                            |

---

## 1. Overview

This document provides guidance on selecting the appropriate privacy accountant for different AMPEL360 federated learning scenarios.

---

## 2. Available Accountants

| Accountant | Tightness | Computation | Recommended Use |
|------------|-----------|-------------|-----------------|
| **RDP** | Tight | Moderate | Default for most cases |
| **Moments** | Moderate | Fast | Legacy compatibility |
| **Gaussian** | Basic | Very Fast | Simple mechanisms |
| **zCDP** | Tight | Moderate | Concentrated DP |

---

## 3. Selection Criteria

### 3.1 Use RDP When:
- Training with DP-SGD
- Multiple composition steps
- Tight bounds required for budget compliance
- Standard AMPEL360 federated learning

### 3.2 Use Moments When:
- Simple, single-step mechanisms
- Backward compatibility required
- Quick approximation sufficient

### 3.3 Use Gaussian When:
- Single Gaussian mechanism
- Quick estimation needed
- Proof-of-concept work

---

## 4. Default Configuration

For AMPEL360 production use:

```yaml
accountant:
  type: "RDP"
  orders: [1.5, 2, 3, 4, 5, 10, 20, 50, 100]
  target_delta: 1.0e-5
```

---

## 5. Decision Matrix

| Scenario | Accountant | Rationale |
|----------|------------|-----------|
| HIGH_PRIVACY profile | RDP | Tightest bounds critical |
| BALANCED_PRIVACY profile | RDP | Standard choice |
| RELAXED_PRIVACY profile | RDP or Moments | Flexibility acceptable |
| SIMULATION_ONLY | None | No DP required |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---
