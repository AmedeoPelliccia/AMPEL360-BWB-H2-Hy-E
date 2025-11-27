# CFLF-GRAD OPT-IN Framework Structure

**Document ID:** CFLF-GRAD-OPTIN-STRUCTURE  
**Version:** 1.0  
**Status:** DRAFT  
**Related Standard:** AMPEL360-FAirCCC-ARCH-001

---

## Purpose

This document defines the **dual-location architecture** for the CFLF-GRAD (Collaborative Federated Learning Fabric – Gradient) system within the OPT-IN Framework. The system is properly split across two OPT-IN axes to separate concerns:

- **N-Axis (Neural Networks)** → Model training, DP-SGD, governance, evaluation
- **L2-LINKS (ATA 23)** → Transport protocols, secure aggregation, communication

---

## Dual-Location Architecture

```
OPT-IN_FRAMEWORK/
│
├── N-NEURAL_NETWORKS_USERS_TRACEABILITY/
│   └── ATA_97-NEURAL_NETWORK_MODELS/
│       └── 97-40_SOFTWARE/
│           └── 97-40-20_FEDERATED_LEARNING/     ← MODELS & TRAINING
│               ├── 97-40-20-00_GENERAL/         # 14 lifecycle folders
│               ├── 97-40-20-10_DP_SGD/          # Privacy-preserving training
│               ├── 97-40-20-20_PRIVACY_BUDGET/  # ε,δ tracking
│               ├── 97-40-20-30_COMPRESSION/     # Sparsification, quantization
│               ├── 97-40-20-40_LOCAL_TRAINING/  # On-aircraft training
│               ├── 97-40-20-50_AGGREGATION/     # FedAvg, FedAdam
│               ├── 97-40-20-60_MODEL_GOVERNANCE/# Policies, kill switches
│               ├── 97-40-20-70_EVALUATION/      # Drift, fairness, benchmarks
│               ├── 97-40-20-80_MODELS/          # H₂, PredMaint, ANCHORS
│               └── 97-40-20-90_SCHEMAS/         # Model schemas
│
└── T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/
    └── L2-LINKS/
        └── ATA_23-COMMUNICATIONS/
            └── 23-95_COMM_NN/                   ← TRANSPORT & PROTOCOLS
                ├── 23-95-00_GENERAL/            # 14 lifecycle folders
                ├── 23-95-10_AIRCRAFT_NODE/      # FAirCCC-A
                ├── 23-95-20_GROUND_NODE/        # FAirCCC-G
                ├── 23-95-30_REGIONAL_NODE/      # FAirCCC-R
                ├── 23-95-40_FLEET_CORE/         # FAirCCC-F
                ├── 23-95-50_SECURITY/           # Auth, encryption
                ├── 23-95-60_PROTOCOLS/          # GRAD, MODEL, TELEM, SAFETY
                ├── 23-95-70_OPERATIONS/         # Monitoring, incidents
                └── 23-95-90_SCHEMAS/            # Transport schemas
```

---

## Key Documents

| Document | Location | Purpose |
|----------|----------|---------|
| **This Document** | [`CFLF-GRAD-OPTIN-STRUCTURE.md`](./CFLF-GRAD-OPTIN-STRUCTURE.md) | Master mapping document |
| **97-40-20-README.md** | [`N-Axis`](./N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_97-NEURAL_NETWORK_MODELS/97-40_Software/97-40-20_FEDERATED_LEARNING/97-40-20-README.md) | Models & Training README |
| **23-95-README.md** | [`L2-LINKS`](./T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/23-95_COMM_NN/23-95-README.md) | Transport & Protocols README |
| **DP-SGD-SPEC.md** | [`N-Axis`](./N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_97-NEURAL_NETWORK_MODELS/97-40_Software/97-40-20_FEDERATED_LEARNING/97-40-20-10_DP_SGD/DP-SGD-SPEC.md) | DP-SGD Specification |
| **gradient_envelope.schema.json** | [`L2-LINKS`](./T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/23-95_COMM_NN/23-95-90_SCHEMAS/gradient_envelope.schema.json) | Gradient envelope schema |
| **cflf-grad.md** | [`CAOS`](../CAOS/channels/cflf-grad.md) | CAOS channel definition |

---

## Separation of Concerns

| Aspect | N-Axis (97-40-20) | L2-LINKS (23-95) |
|--------|-------------------|------------------|
| **Focus** | What to learn | How to transmit |
| **Privacy** | DP-SGD, budget | Secure aggregation |
| **Algorithms** | FedAvg, FedAdam | Protocol layers |
| **Models** | H₂, PredMaint, ANCHORS | Envelope formats |
| **Governance** | Policies, evaluation | Auth, encryption |
| **Integration** | CAOS, DPP | SATCOM, ground IT |

---

## Node Architecture (23-95)

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ AIRCRAFT (A) │ ──▶ │  GROUND (G)  │ ──▶ │ REGIONAL (R) │ ──▶ │  FLEET (F)   │
│ 23-95-10     │     │ 23-95-20     │     │ 23-95-30     │     │ 23-95-40     │
├──────────────┤     ├──────────────┤     ├──────────────┤     ├──────────────┤
│ Feature Gate │     │ Sig Verify   │     │ Coordination │     │ Registry     │
│ Envelope     │     │ Validation   │     │ SecAgg Srv   │     │ Release      │
│ TPM Sign     │     │ Poison Det   │     │ Checkpoint   │     │ DPP/CAOS     │
│ Transport    │     │ Staging      │     │ Uplink       │     │ Integrations │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
```

### Node Details

| Node | ID | Location | Responsibilities |
|------|-----|----------|------------------|
| **Aircraft (A)** | FAirCCC-A | 23-95-10 | Feature gate, envelope prep, TPM signing, transport |
| **Ground (G)** | FAirCCC-G | 23-95-20 | Signature verify, schema validation, poison detection, staging |
| **Regional (R)** | FAirCCC-R | 23-95-30 | Coordination, secure aggregation server, checkpointing, uplink |
| **Fleet (F)** | FAirCCC-F | 23-95-40 | Registry, release management, DPP/CAOS integrations |

---

## Protocol Channels (23-95-60)

| Channel | Direction | Data Type | Safety | Description |
|---------|-----------|-----------|--------|-------------|
| **CFLF-GRAD** | A→G→R→F | DP-masked gradients | Non-safety | Upstream gradient contributions |
| **CFLF-MODEL** | F→R→G→A | Trained models | Non-safety | Downstream model distribution |
| **CFLF-TELEM** | A→G→R→F | Anonymized telemetry | Non-safety | Operational metrics |
| **CFLF-SAFETY** | F→R→G→A | Safety models | DO-178C/ML | Safety-critical model updates |

---

## N-Axis Subsystems (97-40-20)

| Subsystem | ID | Purpose |
|-----------|-----|---------|
| **DP-SGD** | 97-40-20-10 | Differentially private stochastic gradient descent |
| **Privacy Budget** | 97-40-20-20 | Per-model, per-aircraft ε/δ accounting |
| **Compression** | 97-40-20-30 | Top-k sparsification + 8-bit quantization |
| **Local Training** | 97-40-20-40 | On-aircraft model training protocols |
| **Aggregation** | 97-40-20-50 | Server-side aggregation (FedAvg, FedAdam) |
| **Model Governance** | 97-40-20-60 | Policies, approvals, kill switches |
| **Evaluation** | 97-40-20-70 | Drift detection, fairness gates, benchmarks |
| **Models** | 97-40-20-80 | H₂ optimization, predictive maintenance, ANCHORS |
| **Schemas** | 97-40-20-90 | JSON schemas for model artifacts |

---

## Lifecycle Folders (XX-00_GENERAL)

Both 97-40-20 and 23-95 include the standard 14 lifecycle folders:

| # | Folder | Purpose |
|---|--------|---------|
| 01 | Overview | System overview and global architecture |
| 02 | Safety | Safety framework and analysis |
| 03 | Requirements | Requirements and traceability |
| 04 | Design | Design specifications and patterns |
| 05 | Interfaces | Interface control documents |
| 06 | Engineering | Analysis, models, and simulation |
| 07 | V_AND_V | Verification and validation |
| 08 | Prototyping | Prototype development |
| 09 | Production_Planning | Manufacturing planning |
| 10 | Certification | Certification evidence |
| 11 | EIS_Versions_Tags | Configuration management |
| 12 | Services | Maintenance and service |
| 13 | Subsystems_Components | Component breakdown |
| 14 | Ops_Std_Sustain | Operational standards |

---

## Traceability

### Standards & Regulations

| Reference | Description |
|-----------|-------------|
| AMPEL360-FAirCCC-ARCH-001 | FAirCCC Architecture Specification |
| [DO-178C](https://www.rtca.org/products/do-178c-software-considerations-in-airborne-systems-and-equipment-certification/) | Software Considerations in Airborne Systems |
| [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes) | EASA Certification Specifications for Large Aeroplanes |

### Internal References

| Reference | Location |
|-----------|----------|
| CAOS Channel Definition | [`CAOS/channels/cflf-grad.md`](../CAOS/channels/cflf-grad.md) |
| OPT-IN Framework | [`OPT-IN_FRAMEWORK/README.md`](./README.md) |
| ATA 97 Models | [`N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_97-NEURAL_NETWORK_MODELS/`](./N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_97-NEURAL_NETWORK_MODELS/) |
| ATA 23 Communications | [`T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/`](./T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/) |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-27_.

---

**OPT-IN Framework** — CFLF-GRAD Dual-Location Architecture  
*Proper separation between Neural Networks axis (model intelligence) and L2-LINKS axis (communication transport)*
