# CUC OPT-IN Structure — Master Mapping

**Version:** 1.0  
**Date:** 2025-11-27  
**Status:** Draft  
**Related Standard:** AMPEL360-FAirCCC-ARCH-001 §4.1, §8

---

## Purpose

This document provides the master mapping for the **CUC (Config & Update Channel)** across the OPT-IN Framework dual-location architecture. CUC is the downstream complement to CFLF-GRAD, distributing signed model bundles from Fleet Core to aircraft.

---

## Channel Overview

| Attribute | Value |
|-----------|-------|
| **Channel** | CUC |
| **Direction** | Fleet Core → Regional → Ground → Aircraft |
| **Data** | Signed model bundles, configuration, change logs |
| **Safety** | Ground-install only (Parked/Maintenance state) |

---

## Dual-Location Architecture

```
OPT-IN_FRAMEWORK/
│
├── N-NEURAL_NETWORKS_USERS_TRACEABILITY/    ← What to Deploy
│   └── ATA_97-NEURAL_NETWORK_MODELS/
│       └── 97-40_Software/
│           └── 97-40-30_MODEL_DEPLOYMENT/     ← CUC (Deployment)
│               ├── 97-40-30-00_GENERAL/
│               ├── 97-40-30-10_BUNDLE_PACKAGING/
│               ├── 97-40-30-20_SAFETY_CASE/
│               ├── 97-40-30-30_EVALUATION_REPORT/
│               ├── 97-40-30-40_RELEASE_GOVERNANCE/
│               ├── 97-40-30-50_DEPLOYMENT_PHASES/
│               ├── 97-40-30-60_COMPATIBILITY/
│               ├── 97-40-30-70_ROLLBACK/
│               ├── 97-40-30-80_KILL_SWITCHES/
│               └── 97-40-30-90_SCHEMAS/
│
└── T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/  ← How to Install
    └── L2-LINKS/
        └── ATA_23-COMMUNICATIONS/
            └── 23-95_COMM_NN/
                └── 23-95-60_PROTOCOLS/
                    └── 60-50_CUC/
```

---

## Separation of Concerns

| Aspect | N-Axis (97-40-30) | L2-LINKS (23-95-60-50) |
|--------|-------------------|------------------------|
| **Focus** | What to deploy | How to install |
| **Content** | Bundle, safety case, governance | HSM signing, distribution, install |
| **Schemas** | Bundle manifest schema | Transport envelope schema |

---

## N-Axis Structure (97-40-30_MODEL_DEPLOYMENT)

| Bucket | Purpose |
|--------|---------|
| `97-40-30-00_GENERAL` | General governance and overview |
| `97-40-30-10_BUNDLE_PACKAGING` | Model bundle structure and packaging |
| `97-40-30-20_SAFETY_CASE` | Assurance arguments and operational limits |
| `97-40-30-30_EVALUATION_REPORT` | Metrics, datasets, robustness results |
| `97-40-30-40_RELEASE_GOVERNANCE` | Release approval and signing authority |
| `97-40-30-50_DEPLOYMENT_PHASES` | Shadow, Canary, Staged, Full deployment |
| `97-40-30-60_COMPATIBILITY` | Aircraft type, firmware version compatibility |
| `97-40-30-70_ROLLBACK` | Rollback procedures and points |
| `97-40-30-80_KILL_SWITCHES` | Per-model, per-tail kill switches |
| `97-40-30-90_SCHEMAS` | JSON/CBOR schemas for bundles |

---

## L2-LINKS Structure (23-95-60-50)

| Aspect | Description |
|--------|-------------|
| **Transport** | mTLS (TLS 1.3), JSON/CBOR metadata, binary weights |
| **Security** | HSM-backed Ed25519 signatures, certificate pinning |
| **Validation** | Signature verification, integrity checks, compatibility validation |

---

## Update Bundle Contents

Each CUC package contains:

| File | Description |
|------|-------------|
| `model.weights` | Model delta or full weights |
| `model.meta` | Model ID, version, compatibility info |
| `eval_report.json` | Metrics, datasets, robustness results |
| `safety_case.md` | Assurance arguments and operational limits |
| `changelog.md` | Human-readable change description |
| `signature.sig` | Fleet Core HSM signature (Ed25519) |

---

## Deployment Phases

1. **Shadow Mode:** New model runs in parallel, outputs logged only
2. **Canary Deployment:** Limited subset of aircraft (test fleet)
3. **Staged Rollout:** Gradual fleet-wide deployment
4. **Full Deployment:** Complete fleet coverage

---

## S0 Authority Model

| Aspect | Description |
|--------|-------------|
| **Sole Signer** | Fleet Core (FAirCCC-F) only |
| **HSM-Backed** | All signatures via Hardware Security Module |
| **Centralized Control** | No regional/ground authority to create releases |
| **Human Approval** | Maintenance/dispatch approval gates installation |

---

## Key Documents

| Document | Location |
|----------|----------|
| [CUC Channel Spec](CAOS/channels/cuc.md) | CAOS channel definition |
| [97-40-30 README](OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_97-NEURAL_NETWORK_MODELS/97-40_Software/97-40-30_MODEL_DEPLOYMENT/README.md) | N-Axis bucket |
| [60-50 README](OPT-IN_FRAMEWORK/T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/23-95_COMM_NN/23-95-60_PROTOCOLS/60-50_CUC/README.md) | L2-LINKS protocol |
| [23-95 README](OPT-IN_FRAMEWORK/T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/23-95_COMM_NN/README.md) | COMM_NN overview |

---

## Related Channels

| Channel | Direction | N-Axis | L2-Axis |
|---------|-----------|--------|---------|
| **CFLF-GRAD** | A→G→R→F | 97-40-20 | 23-95-60-10 |
| **CFLF-MODEL** | F→R→G→A | 97-40-30 | 23-95-60-20 |
| **CFLF-TELEM** | A→G→R→F | 97-40-20 | 23-95-60-30 |
| **CFLF-SAFETY** | F→R→G→A | 97-40-30 | 23-95-60-40 |
| **CUC** | F→R→G→A | 97-40-30 | 23-95-60-50 |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---
