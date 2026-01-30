# 60-50_CUC — Config & Update Channel Protocol

**Version:** 1.0  
**Date:** 2025-11-27  
**Status:** Draft  
**Related Standard:** AMPEL360-FAirCCC-ARCH-001 §4.1, §8

---

## Purpose

The **CUC (Config & Update Channel)** protocol implements the downstream distribution of signed model bundles from Fleet Core to aircraft. This L2-LINKS location defines the transport, security, and installation protocols.

---

## Protocol Overview

| Aspect | Description |
|--------|-------------|
| **Direction** | Fleet Core → Regional → Ground → Aircraft |
| **Data Type** | Signed model bundles, configuration, change logs |
| **Encryption** | mTLS (TLS 1.3) |
| **Encoding** | Bundle metadata in JSON/CBOR, weights in binary |
| **Signature** | Ed25519 signatures from Fleet Core HSM |

---

## Transport Layers

### Fleet Core → Regional (FAirCCC-F → FAirCCC-R)
- High-bandwidth backbone
- Certificate pinning for Fleet Core identity
- Bulk transfer with integrity verification

### Regional → Ground (FAirCCC-R → FAirCCC-G)
- Regional distribution network
- Signature propagation (no re-signing)
- Caching for offline ground stations

### Ground → Aircraft (FAirCCC-G → FAirCCC-A)
- Gate-only transfer (disabled airborne)
- Installation state verification (Parked/Maintenance)
- Post-install validation

---

## Security Mechanisms

### HSM Signing
- Fleet Core HSM generates all release signatures
- Ed25519 algorithm for compact, fast verification
- Key rotation and escrow procedures

### Verification Chain
1. **Ground Station:** Signature verification, bundle integrity, compatibility
2. **Aircraft:** Signature re-verification, rollback point creation
3. **Post-Install:** Health checks, operational limits enforcement

### Threat Mitigations
- Supply-chain tampering protection (SLSA attestations)
- Rogue update prevention (HSM-only signing)
- Rollback capability (always maintained)
- Phased deployment (canary testing)
- Kill-switches (per-model, per-tail)

---

## Installation Policy

| Requirement | Description |
|-------------|-------------|
| **State** | Aircraft must be in Parked or Maintenance mode |
| **Recording** | Installation logged by CM/DM systems |
| **Rollback** | Always available; one-click via Ground station |
| **Verification** | Post-install health checks mandatory |

---

## Dual-Location Reference

| Aspect | N-Axis (97-40-30) | L2-LINKS (60-50) |
|--------|-------------------|------------------|
| **Focus** | What to deploy | How to install |
| **Content** | Bundle, safety case, governance | HSM signing, distribution, install |
| **Schemas** | Bundle manifest schema | Transport envelope schema |

---

## Related Documents

* [CUC Channel Specification](../../../../../../CAOS/channels/cuc.md)
* [97-40-30_MODEL_DEPLOYMENT README](../../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_97-NEURAL_NETWORK_MODELS/97-40_Software/97-40-30_MODEL_DEPLOYMENT/README.md)
* [23-95_COMM_NN README](../README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---
