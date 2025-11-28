# 97-40-30_MODEL_DEPLOYMENT — CUC (Deployment)

**Version:** 1.0  
**Date:** 2025-11-27  
**Status:** Draft  
**Related Standard:** AMPEL360-FAirCCC-ARCH-001 §4.1, §8

---

## Purpose

The **CUC (Config & Update Channel)** bucket implements the downstream distribution of signed model bundles, configuration updates, and change logs from Fleet Core to aircraft through a controlled, phased deployment process with human-in-the-loop approval.

This N-Axis bucket focuses on **what to deploy** — bundle packaging, safety cases, and release governance.

---

## FAirCCC Channel Reference

| Channel | Direction | Data | Safety |
|---------|-----------|------|--------|
| **CUC** | F→R→G→A | Signed bundles | Ground-install only |

---

## Bucket Structure

```
97-40-30_MODEL_DEPLOYMENT/
├── 97-40-30-00_GENERAL/          # General governance and overview
├── 97-40-30-10_BUNDLE_PACKAGING/ # Model bundle structure and packaging
├── 97-40-30-20_SAFETY_CASE/      # Assurance arguments and operational limits
├── 97-40-30-30_EVALUATION_REPORT/ # Metrics, datasets, robustness results
├── 97-40-30-40_RELEASE_GOVERNANCE/ # Release approval and signing authority
├── 97-40-30-50_DEPLOYMENT_PHASES/ # Shadow, Canary, Staged, Full deployment
├── 97-40-30-60_COMPATIBILITY/    # Aircraft type, firmware version compatibility
├── 97-40-30-70_ROLLBACK/         # Rollback procedures and points
├── 97-40-30-80_KILL_SWITCHES/    # Per-model, per-tail kill switches
└── 97-40-30-90_SCHEMAS/          # JSON/CBOR schemas for bundles
```

---

## Key Characteristics

* **Direction:** Fleet Core → Regional → Ground → Aircraft
* **Data Type:** Signed model bundles, configuration, change logs
* **Update Rate:** Bulk transfer at gate (disabled airborne)
* **Safety Impact:** Ground-only installation with maintenance approval

---

## S0 Authority Model

* **Sole Signer:** Fleet Core (FAirCCC-F) is the only entity authorized to sign releases
* **HSM-Backed:** All signatures generated via Hardware Security Module
* **Centralized Control:** No regional or ground authority to create releases
* **Human Approval:** Maintenance/dispatch approval gates installation

---

## Update Bundle Contents

Each CUC package contains:
1. `model.weights` – Model delta or full weights
2. `model.meta` – Model ID, version, compatibility info
3. `eval_report.json` – Metrics, datasets, robustness results
4. `safety_case.md` – Assurance arguments and operational limits
5. `changelog.md` – Human-readable change description
6. `signature.sig` – Fleet Core HSM signature (Ed25519)

---

## Deployment Phases

1. **Shadow Mode:** New model runs in parallel, outputs logged only
2. **Canary Deployment:** Limited subset of aircraft (test fleet)
3. **Staged Rollout:** Gradual fleet-wide deployment
4. **Full Deployment:** Complete fleet coverage

---

## Dual-Location Architecture

This bucket (97-40-30) is the **N-Axis** location for CUC, focusing on:
- What to deploy
- Bundle packaging
- Safety cases
- Release governance

The **L2-LINKS** counterpart is located at:
- `T-TECHNOLOGY/L2-LINKS/ATA_23-COMMUNICATIONS/23-95_COMM_NN/23-95-60_PROTOCOLS/60-50_CUC/`

The L2-LINKS location focuses on:
- How to transmit
- HSM signing
- Distribution protocols
- Installation procedures

---

## Related Documents

* [CUC Channel Specification](../../../../../../CAOS/channels/cuc.md)
* [CFLF-GRAD Channel Specification](../../../../../../CAOS/channels/cflf-grad.md)
* [23-95_COMM_NN README](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/23-95_COMM_NN/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---
