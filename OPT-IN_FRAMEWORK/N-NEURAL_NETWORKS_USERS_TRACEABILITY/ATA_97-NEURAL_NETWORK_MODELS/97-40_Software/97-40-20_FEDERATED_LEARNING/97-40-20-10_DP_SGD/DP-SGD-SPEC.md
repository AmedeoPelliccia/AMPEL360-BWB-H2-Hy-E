# DP-SGD Specification

**Document ID:** 97-40-20-10-SPEC-001  
**Version:** 1.0  
**Status:** DRAFT  
**ATA Reference:** 97-40-20-10

---

## 1. Purpose

This document specifies the Differentially Private Stochastic Gradient Descent (DP-SGD) implementation for the CFLF-GRAD federated learning system. DP-SGD ensures that individual aircraft contributions to model updates cannot be reconstructed from the aggregated gradients.

---

## 2. Scope

This specification covers:

- Gradient clipping (L2 norm)
- Gaussian noise addition
- Privacy budget (ε, δ) enforcement
- Integration with local training protocols

---

## 3. Algorithm Overview

### 3.1 Standard DP-SGD Flow

```
┌─────────────────────────────────────────────────────────────┐
│  DP-SGD Training Step                                       │
├─────────────────────────────────────────────────────────────┤
│  1. Compute per-sample gradients g_i                        │
│  2. Clip: g̃_i = g_i / max(1, ||g_i||₂ / C)                  │
│  3. Aggregate: g̃ = (1/n) Σ g̃_i                              │
│  4. Add noise: g̃_noisy = g̃ + N(0, σ²C²I)                   │
│  5. Update: θ ← θ - η × g̃_noisy                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Parameters

| Parameter | Symbol | Description | Default |
|-----------|--------|-------------|---------|
| **Clipping Bound** | C | Maximum L2 norm for gradients | 1.0 |
| **Noise Multiplier** | σ | Gaussian noise scale | 1.1 |
| **Learning Rate** | η | Step size | 0.01 |
| **Batch Size** | n | Samples per batch | 256 |

---

## 4. Privacy Guarantees

### 4.1 Privacy Budget Accounting

The system uses the **moments accountant** method to track privacy budget consumption:

- **ε (epsilon)**: Privacy loss parameter (lower = more private)
- **δ (delta)**: Probability of privacy failure (typically 10⁻⁵)

### 4.2 Budget Limits

| Model Type | Max ε per Round | Max ε Lifetime | δ |
|------------|-----------------|----------------|---|
| Non-safety | 1.0 | 10.0 | 10⁻⁵ |
| Advisory | 0.5 | 5.0 | 10⁻⁶ |
| Safety-related | N/A (no FL) | N/A | N/A |

### 4.3 Budget Enforcement

- Per-aircraft, per-model budget tracking
- Automatic contribution blocking when budget exhausted
- No raw data transmission under any circumstances

---

## 5. Gradient Processing Pipeline

### 5.1 Aircraft-Side Processing

```
┌─────────────────┐
│ Local Dataset   │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 1. Train Step   │ ← Compute raw gradients
└────────┬────────┘
         ↓
┌─────────────────┐
│ 2. Per-Sample   │ ← Clip each sample's gradient
│    Clipping     │    g̃_i = g_i / max(1, ||g_i||₂ / C)
└────────┬────────┘
         ↓
┌─────────────────┐
│ 3. Aggregate    │ ← Average clipped gradients
│    & Noise      │    g̃_noisy = g̃ + N(0, σ²C²I)
└────────┬────────┘
         ↓
┌─────────────────┐
│ 4. Compression  │ ← See 97-40-20-30_COMPRESSION
│   (top-k, quant)│
└────────┬────────┘
         ↓
┌─────────────────┐
│ 5. Envelope     │ ← See 23-95_COMM_NN
│    & Transport  │
└─────────────────┘
```

### 5.2 Implementation Requirements

| ID | Requirement | Rationale |
|----|-------------|-----------|
| DP-001 | Per-sample gradient computation | Enables per-sample clipping |
| DP-002 | Deterministic clipping at bound C | Prevents gradient explosion |
| DP-003 | Calibrated Gaussian noise | Achieves target (ε, δ) |
| DP-004 | Secure RNG for noise generation | Prevents noise prediction |
| DP-005 | Budget check before contribution | Prevents over-spending |

---

## 6. Integration Points

### 6.1 Upstream (Model Training)

- Receives model architecture from `97-40-20-80_MODELS`
- Receives training config from `97-40-20-40_LOCAL_TRAINING`

### 6.2 Downstream (Compression)

- Outputs noised gradients to `97-40-20-30_COMPRESSION`
- Passes privacy metadata for envelope construction

### 6.3 Privacy Budget

- Reports consumption to `97-40-20-20_PRIVACY_BUDGET`
- Queries remaining budget before training

---

## 7. Threat Model

### 7.1 Adversary Capabilities

| Threat | Mitigation |
|--------|------------|
| Gradient inversion attack | Noise addition prevents reconstruction |
| Membership inference | Per-sample clipping bounds contribution |
| Model poisoning | Server-side validation (see 23-95-20) |
| Colluding servers | Secure aggregation (see 23-95) |

### 7.2 Non-Threats (Out of Scope)

- Physical access to aircraft systems
- Compromise of on-aircraft TPM
- Attacks on unrelated systems

---

## 8. Validation

### 8.1 Test Cases

| ID | Test | Expected Outcome |
|----|------|------------------|
| DP-T01 | Gradient norm after clipping | ≤ C |
| DP-T02 | Noise distribution | Matches N(0, σ²C²I) |
| DP-T03 | Budget accounting | Correct (ε, δ) |
| DP-T04 | Budget exhaustion | Contribution blocked |

### 8.2 Certification Evidence

Evidence artifacts are stored in:
- `97-40-20-00_GENERAL/97-40-20-00-07_V_AND_V/`
- `97-40-20-00_GENERAL/97-40-20-00-10_Certification/`

---

## 9. References

| Reference | Description |
|-----------|-------------|
| Abadi et al. (2016) | Deep Learning with Differential Privacy |
| Mironov (2017) | Rényi Differential Privacy |
| AMPEL360-FAirCCC-ARCH-001 | FAirCCC Architecture Specification |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-27_.

---
