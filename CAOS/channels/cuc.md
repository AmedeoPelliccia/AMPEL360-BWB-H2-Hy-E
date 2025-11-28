# CUC – Config & Update Channel

**Channel Type:** Downstream Update Distribution (Fleet Core → Regional → Ground → Aircraft)  
**Safety Classification:** Ground-install only (Parked/Maintenance state)  
**Related Standard:** AMPEL360-FAirCCC-ARCH-001 §4.1, §8

## Purpose

The Config & Update Channel (CUC) distributes signed model bundles, configuration updates, and change logs from Fleet Core to aircraft through a controlled, phased deployment process with human-in-the-loop approval.

## Key Characteristics

* **Direction:** F→R→G→A (Fleet Core to Regional to Ground to Aircraft)
* **Data Type:** Signed model bundles, configuration, change logs
* **Update Rate:** Bulk transfer at gate (disabled airborne)
* **Safety Impact:** Ground-only installation with maintenance approval

## S0 Authority Model

* **Sole Signer:** Fleet Core (FAirCCC-F) is the only entity authorized to sign releases
* **HSM-Backed:** All signatures generated via Hardware Security Module
* **Centralized Control:** No regional or ground authority to create releases
* **Human Approval:** Maintenance/dispatch approval gates installation

## Update Bundle Contents

Each CUC package contains:
1. `model.weights` – Model delta or full weights
2. `model.meta` – Model ID, version, compatibility info
3. `eval_report.json` – Metrics, datasets, robustness results
4. `safety_case.md` – Assurance arguments and operational limits
5. `changelog.md` – Human-readable change description
6. `signature.sig` – Fleet Core HSM signature (Ed25519)

## Deployment Phases

1. **Shadow Mode:** New model runs in parallel, outputs logged only
2. **Canary Deployment:** Limited subset of aircraft (test fleet)
3. **Staged Rollout:** Gradual fleet-wide deployment
4. **Full Deployment:** Complete fleet coverage

## Installation Policy

* **State Requirement:** Aircraft must be in Parked or Maintenance mode
* **Recording:** Installation logged by CM/DM systems
* **Rollback:** Always available; one-click via Ground station
* **Verification:** Post-install health checks mandatory

## Use Cases

* ML model updates (maintenance, efficiency, operations)
* Configuration parameter updates
* Non-safety system optimizations
* Advisory system improvements

## Security & Validation

### Ground Station (FAirCCC-G)
- Signature verification (Fleet Core public key)
- Bundle integrity checks (SHA-256 hashes)
- Compatibility validation (aircraft type, firmware version)
- Installation state verification (Parked/Maintenance)

### Aircraft (FAirCCC-A)
- Signature verification before installation
- Rollback point creation
- Post-install validation
- Operational limits enforcement

## Data Schema

*Detailed CUC manifest schema in AMPEL360-FAirCCC-ARCH-001 §8.1 and §16*

## Security & Transport

* **Encryption:** mTLS (TLS 1.3)
* **Encoding:** Bundle metadata in JSON/CBOR, weights in binary format
* **Authentication:** Certificate pinning for Fleet Core identity
* **Integrity:** SHA-256 hashes for all bundle components
* **Signature:** Ed25519 signatures from Fleet Core HSM

## Threat Mitigations

* Supply-chain tampering protection (SLSA attestations)
* Rogue update prevention (HSM-only signing)
* Rollback capability (always maintained)
* Phased deployment (canary testing)
* Kill-switches (per-model, per-tail)

---

## OPT-IN Framework Mapping

CUC is the downstream complement to CFLF-GRAD. The FAirCCC system uses a dual-location OPT-IN architecture:

### Dual-Location Structure

| Axis | Location | Focus |
|------|----------|-------|
| **N-Axis** | `N-NEURAL_NETWORKS/ATA_97-NEURAL_NETWORK_MODELS/97-40_Software/97-40-30_MODEL_DEPLOYMENT/` | What to deploy |
| **L2-LINKS** | `T-TECHNOLOGY/L2-LINKS/ATA_23-COMMUNICATIONS/23-95_COMM_NN/23-95-60_PROTOCOLS/60-50_CUC/` | How to install |

### Separation of Concerns

| Aspect | N-Axis (97-40-30) | L2-LINKS (23-95-60-50) |
|--------|-------------------|------------------------|
| **Content** | Bundle, safety case, governance | HSM signing, distribution, install |
| **Schemas** | Bundle manifest schema | Transport envelope schema |

### Related Documents

* [CUC OPT-IN Structure Master Mapping](../../OPT-IN_FRAMEWORK/CUC-OPTIN-STRUCTURE.md)
* [CFLF-GRAD OPT-IN Structure](../../OPT-IN_FRAMEWORK/CFLF-GRAD-OPTIN-STRUCTURE.md)
* [97-40-30_MODEL_DEPLOYMENT README](../../OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_97-NEURAL_NETWORK_MODELS/97-40_Software/97-40-30_MODEL_DEPLOYMENT/README.md)
* [23-95_COMM_NN README](../../OPT-IN_FRAMEWORK/T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/23-95_COMM_NN/README.md)

---

*Note: This is a stub document. GenCCC will auto-link and expand this content based on the FAirCCC architecture specification.*

---

- **Authorship:** Content generated through prompt engineering methods using AI assistants and agent tools, prompted and partially reviewed by **Amedeo Pelliccia**, with automated checking tools for validation.
- Status: **DRAFT**
- Repository: `AMPEL360-BWB-H2-Hy-E`
