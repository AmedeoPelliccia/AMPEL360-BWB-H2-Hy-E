# 97-40-20-20-701 — Budget Usage Examples

**Example scenarios and budget traces for privacy budget governance**

---

## Document Control

| Field              | Value                                                           |
|--------------------|-----------------------------------------------------------------|
| **Document ID**    | 97-40-20-20-701_Budget_Usage_Examples                           |
| **ATA Chapter**    | 97 — Neural Network Models / Digital Artifacts                  |
| **Bucket**         | 97-40-20 — FEDERATED_LEARNING                                   |
| **Sub-Bucket**     | 97-40-20-20 — PRIVACY_BUDGET                                    |
| **Version**        | 1.0                                                             |
| **Date**           | 2025-11-27                                                      |
| **Status**         | DRAFT                                                           |
| **Classification** | REPORTS / EXAMPLES                                              |

---

## 1. Overview

This document provides example scenarios demonstrating privacy budget allocation, consumption, and tracking within the AMPEL360 federated learning framework.

---

## 2. Example 1: H₂ Efficiency Model Training

### 2.1 Scenario

Training a hydrogen efficiency prediction model across a fleet of 50 aircraft over 6 months.

### 2.2 Budget Allocation

| Scope | Profile | ε_max | δ_max |
|-------|---------|-------|-------|
| Per-Model (H2_EFFICIENCY) | BALANCED | 5.0 | 1e-5 |
| Per-Aircraft | BALANCED | 5.0 | 1e-5 |
| Fleet Total | BALANCED | 50.0 | 1e-4 |

### 2.3 Training Runs

| Round | Nodes | ε_spent | Cumulative ε | Status |
|-------|-------|---------|--------------|--------|
| 1 | 50 | 0.3 | 0.3 | OK |
| 2 | 48 | 0.3 | 0.6 | OK |
| ... | ... | ... | ... | ... |
| 10 | 50 | 0.3 | 3.0 | OK |
| 15 | 50 | 0.3 | 4.5 | Warning (90%) |
| 16 | 50 | 0.3 | 4.8 | Hard Stop (96%) |

### 2.4 Outcome

- Training paused at round 16
- Governance review triggered
- Budget renewed for next period

---

## 3. Example 2: Predictive Maintenance Model

### 3.1 Scenario

Monthly update of predictive maintenance model using sensor data.

### 3.2 Budget Consumption

| Month | ε_spent | Cumulative | % Used |
|-------|---------|------------|--------|
| Jan | 0.8 | 0.8 | 16% |
| Feb | 0.9 | 1.7 | 34% |
| Mar | 0.7 | 2.4 | 48% |
| Apr | 0.8 | 3.2 | 64% |
| May | 0.9 | 4.1 | 82% (Warning) |
| Jun | 0.5 | 4.6 | 92% (Near Limit) |

### 3.3 Actions Taken

- Reduced training frequency after May warning
- Requested budget increase for next year

---

## 4. Example 3: High-Privacy Crew Data

### 4.1 Scenario

Behavioral pattern analysis using crew interaction data.

### 4.2 Strict Budget

| Scope | Profile | ε_max | δ_max |
|-------|---------|-------|-------|
| Per-Model | HIGH_PRIVACY | 1.0 | 1e-6 |

### 4.3 Result

- Only 3 training rounds possible
- High noise → lower model accuracy
- Acceptable trade-off for sensitive data

---

## 5. Budget Renewal Process

1. Submit renewal request to Governance WG
2. Provide usage report and justification
3. Review by Data Protection Officer
4. Approval and budget reset

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---
