# 60-10_CFLF_GRAD — CFLF Gradient Channel Protocol

**Version:** 1.0  
**Date:** 2025-11-27  
**Status:** Draft  
**Related Standard:** AMPEL360-FAirCCC-ARCH-001 §4.1, §7

---

## Purpose

The **CFLF-GRAD (Collaborative Federated Learning Fabric - Gradient)** protocol implements the upstream transport of DP-masked sparse gradient deltas from aircraft to the learning infrastructure. This L2-LINKS location defines the transport, security, and aggregation protocols.

---

## Protocol Overview

| Aspect | Description |
|--------|-------------|
| **Direction** | Aircraft → Ground → Regional → Fleet Core |
| **Data Type** | DP-masked sparse gradient deltas |
| **Encryption** | mTLS (TLS 1.3) |
| **Encoding** | CBOR for gradient envelopes |
| **Signature** | TPM-anchored signatures |

---

## Transport Layers

### Aircraft → Ground (FAirCCC-A → FAirCCC-G)
- Low-rate, best-effort, preemptible
- Feature gate and scrub (limits, units, PII removal)
- Secure aggregation masking applied
- Envelope signed with TPM

### Ground → Regional (FAirCCC-G → FAirCCC-R)
- Signature verification at ground
- Schema validation
- DP budget checks before forwarding

### Regional → Fleet Core (FAirCCC-R → FAirCCC-F)
- Wait for N≥T clients (secure aggregation threshold)
- Unmask sum only (secure aggregation)
- Apply FedAvg/FedAdam aggregation
- Forward aggregated gradients to Fleet Core

---

## Learning Protocol Steps

### Aircraft-Side (FAirCCC-A)
1. Feature Gate & Scrub (limits, units, PII removal)
2. DP-SGD Step (clip L2, add noise σ)
3. Compression (top-k sparsification + 8-bit quantization)
4. Secure Aggregation Masking
5. Envelope Sign & Send (TPM signature)

### Ground Validation (FAirCCC-G)
- Signature verification
- Schema validation
- DP budget checks

### Regional Aggregation (FAirCCC-R)
- Wait for N≥T clients
- Unmask sum only (secure aggregation)
- Apply FedAvg/FedAdam

### Fleet Core Processing (FAirCCC-F)
- Full evaluation battery
- Drift and fairness gates
- Produce release candidate

---

## Security Mechanisms

### TPM-Anchored Signatures
- Aircraft TPM generates gradient envelope signatures
- Attestation includes SBOM hash + model hash + build provenance

### Secure Aggregation
- Pairwise masks or threshold secret sharing
- Ensures individual gradients remain private
- Only aggregated sum is revealed at regional level

### DP Enforcement
- Server-side DP enforcement at ground and regional
- Per-model privacy budget (ε,δ) tracking
- Contribution thresholds

### Threat Mitigations
- Poisoned gradient detection (outlier clipping)
- Anomaly filters
- Per-model kill-switches

---

## Dual-Location Reference

| Aspect | N-Axis (97-40-20) | L2-LINKS (60-10) |
|--------|-------------------|------------------|
| **Focus** | What to learn | How to transmit |
| **Content** | DP-SGD, privacy, aggregation | Feature gate, transport, SecAgg |
| **Schemas** | Gradient format schema | Transport envelope schema |

---

## Related Documents

* [CFLF-GRAD Channel Specification](../../../../../../CAOS/channels/cflf-grad.md)
* [97-40-20_FEDERATED_LEARNING README](../../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_97-NEURAL_NETWORK_MODELS/97-40_Software/97-40-20_FEDERATED_LEARNING/README.md)
* [23-95_COMM_NN README](../README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---
