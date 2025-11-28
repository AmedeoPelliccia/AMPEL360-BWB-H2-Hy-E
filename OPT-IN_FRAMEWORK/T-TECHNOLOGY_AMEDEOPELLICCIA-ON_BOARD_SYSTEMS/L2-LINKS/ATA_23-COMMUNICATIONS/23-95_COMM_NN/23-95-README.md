# 23-95 — COMM_NN (Transport & Protocols)

**ATA Chapter:** 23 — Communications  
**Subsystem:** 95 — COMM_NN (Neural Network Communications)  
**OPT-IN Axis:** T — Technology (L2-LINKS)  
**Related Standard:** AMPEL360-FAirCCC-ARCH-001

---

## Purpose

This subsystem contains all **transport and protocol logic** for the CFLF-GRAD (Collaborative Federated Learning Fabric – Gradient) system. It covers:

- **Node architecture** (Aircraft, Ground, Regional, Fleet)
- **Security** (authentication, encryption, attestation)
- **Protocol channels** (GRAD, MODEL, TELEM, SAFETY)
- **Operations** (monitoring, incidents)
- **Transport schemas** (envelope formats)

> **Model training & algorithms** are handled in **N-Axis (ATA 97-40-20)**.  
> See [`97-40-20_FEDERATED_LEARNING`](../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_97-NEURAL_NETWORK_MODELS/97-40_Software/97-40-20_FEDERATED_LEARNING/97-40-20-README.md).

---

## Directory Structure

```
23-95_COMM_NN/
├── 23-95-README.md                       ← This file
├── 23-95-00_GENERAL/                     ← 14 lifecycle folders
│   ├── 23-95-00-01_Overview/
│   ├── 23-95-00-02_Safety/
│   ├── 23-95-00-03_Requirements/
│   ├── 23-95-00-04_Design/
│   ├── 23-95-00-05_Interfaces/
│   ├── 23-95-00-06_Engineering/
│   ├── 23-95-00-07_V_AND_V/
│   ├── 23-95-00-08_Prototyping/
│   ├── 23-95-00-09_Production_Planning/
│   ├── 23-95-00-10_Certification/
│   ├── 23-95-00-11_EIS_Versions_Tags/
│   ├── 23-95-00-12_Services/
│   ├── 23-95-00-13_Subsystems_Components/
│   └── 23-95-00-14_Ops_Std_Sustain/
│
├── 23-95-10_AIRCRAFT_NODE/               ← FAirCCC-A
├── 23-95-20_GROUND_NODE/                 ← FAirCCC-G
├── 23-95-30_REGIONAL_NODE/               ← FAirCCC-R
├── 23-95-40_FLEET_CORE/                  ← FAirCCC-F
├── 23-95-50_SECURITY/                    ← Auth, encryption
├── 23-95-60_PROTOCOLS/                   ← GRAD, MODEL, TELEM, SAFETY
├── 23-95-70_OPERATIONS/                  ← Monitoring, incidents
└── 23-95-90_SCHEMAS/                     ← Transport schemas
```

---

## Node Architecture

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

| Node | ID | Description |
|------|-----|-------------|
| **Aircraft (A)** | FAirCCC-A | On-aircraft envelope preparation & signing |
| **Ground (G)** | FAirCCC-G | Ground station validation & staging |
| **Regional (R)** | FAirCCC-R | Regional aggregation & coordination |
| **Fleet (F)** | FAirCCC-F | Fleet core registry & release management |

---

## Protocol Channels (23-95-60)

| Channel | Direction | Data Type | Safety |
|---------|-----------|-----------|--------|
| **CFLF-GRAD** | A→G→R→F | DP-masked gradients | Non-safety |
| **CFLF-MODEL** | F→R→G→A | Trained models | Non-safety |
| **CFLF-TELEM** | A→G→R→F | Anonymized telemetry | Non-safety |
| **CFLF-SAFETY** | F→R→G→A | Safety models | DO-178C/ML |

---

## Security (23-95-50)

| Feature | Implementation |
|---------|----------------|
| **Encryption** | mTLS (TLS 1.3) |
| **Encoding** | CBOR for gradient envelopes |
| **Authentication** | TPM-anchored signatures |
| **Attestation** | SBOM hash + model hash + build provenance |
| **Secure Aggregation** | Pairwise masks or threshold secret sharing |

---

## Separation of Concerns

| Aspect | N-Axis (97-40-20) | This Module (23-95) |
|--------|-------------------|---------------------|
| **Focus** | What to learn | How to transmit |
| **Privacy** | DP-SGD, budget | Secure aggregation |
| **Algorithms** | FedAvg, FedAdam | Protocol layers |
| **Models** | H₂, PredMaint, ANCHORS | Envelope formats |
| **Governance** | Policies, evaluation | Auth, encryption |
| **Integration** | CAOS, DPP | SATCOM, ground IT |

---

## Key Specifications

- [gradient_envelope.schema.json](./23-95-90_SCHEMAS/gradient_envelope.schema.json) — Gradient envelope schema

---

## Traceability

| Reference | Document |
|-----------|----------|
| Architecture | AMPEL360-FAirCCC-ARCH-001 §4.1, §7 |
| CAOS Channel | [CAOS/channels/cflf-grad.md](../../../../../CAOS/channels/cflf-grad.md) |
| Model Layer | [97-40-20_FEDERATED_LEARNING](../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_97-NEURAL_NETWORK_MODELS/97-40_Software/97-40-20_FEDERATED_LEARNING/97-40-20-README.md) |
| Master Mapping | [CFLF-GRAD-OPTIN-STRUCTURE.md](../../../../../OPT-IN_FRAMEWORK/CFLF-GRAD-OPTIN-STRUCTURE.md) |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-27_.

---

**OPT-IN Framework** — L2-LINKS Communications  
*Neural Network Transport Subsystem*
