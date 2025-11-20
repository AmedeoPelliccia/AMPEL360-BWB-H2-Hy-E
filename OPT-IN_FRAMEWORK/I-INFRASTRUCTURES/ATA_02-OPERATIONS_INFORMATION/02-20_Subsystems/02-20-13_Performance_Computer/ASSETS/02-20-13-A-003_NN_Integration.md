# 02-20-13-A-003 — NN Integration

**Asset ID:** 02-20-13-A-003  
**Title:** NN Integration Architecture & Data Flows  
**Subsystem:** [02-20-13_Performance_Computer](../README.md)  
**Type:** Architecture Diagram + Interface Notes  
**Formats:** Mermaid / SVG + Markdown Description  
**Status:** PLACEHOLDER (DRAFT)  

---

<img width="1200" height="700" alt="image" src="https://github.com/user-attachments/assets/b037a0ff-3b36-46fd-abec-bed93a4f3bcd" />

## 1. Purpose

This asset documents the **Neural Network (NN) integration architecture** between:

- The **02-20-13 Performance Computer** (deterministic performance core)  
- The **02-20-13-005 NN Performance Predictor** integration layer  
- The **ATA 95 Neural Network ecosystem** (Digital Product Passport, model registry, monitoring)  

Goals:

- Show **where and how NN models plug into** the performance computation chain  
- Clarify **data and control flows** (requests, responses, metadata, logging)  
- Support **certification arguments** (clear separation of deterministic core vs NN corrections)  
- Provide a **reference view** for implementation and test harness design  

For detailed logic and requirements, see:  
- [02-20-13-005_NN_Performance_Predictor.md](../02-20-13-005_NN_Performance_Predictor.md)  
- ATA 95-00-00 GENERAL docs (purpose, traceability, DPP, certification framework)

---

## 2. Files

Located under:

`.../02-20-13_Performance_Computer/ASSETS/`

- **[02-20-13-A-003_NN_Integration.svg](./02-20-13-A-003_NN_Integration.svg)**  
  Visual architecture diagram (exported for general use).  
- `02-20-13-A-003_NN_Integration.mmd` *(optional, recommended)*  
  Mermaid text source for the diagram (GitHub-renderable, easier diff).  
- This description:  
  **[02-20-13-A-003_NN_Integration.md](./02-20-13-A-003_NN_Integration.md)**

---

## 3. Architecture Diagram (Mermaid Source)

> Suggested `02-20-13-A-003_NN_Integration.mmd` content.  
> You can also embed this block directly into `README.md` if desired.

```mermaid
flowchart LR
  %% 02-20-13-A-003_NN_Integration

  %% Upstream clients
  EFB["02-20-11\nElectronic Flight Bag"]
  DISPATCH["CAOS / Dispatch Tools"]
  SIM["Analysis & SIM Tools"]

  %% Performance Computer & NN layer
  subgraph PERF["02-20-13 Performance Computer"]
    CORE["Deterministic Core\n(TO / LDG / CRZ Algorithms)"]
    NN_LAYER["02-20-13-005\nNN Performance Predictor\nIntegration Layer"]
  end

  %% ATA 95 ecosystem
  subgraph ATA95["ATA 95 — Neural Networks"]
    REG["Model Registry &\nDigital Product Passport"]
    INFER["Inference Service(s)"]
    MON["Monitoring & Drift\nMetrics"]
  end

  %% Recording / evidence
  LOG["ATA 31 / CAOS\nPerformance Logs & Evidence"]

  %% Flows from clients into Performance Computer
  EFB --> CORE
  DISPATCH --> CORE
  SIM --> CORE

  %% Deterministic core to NN layer
  CORE -->|"NNPerfRequest\n(inputs, y_base, context)"| NN_LAYER

  %% NN layer to ATA 95 model infra
  NN_LAYER -->|"Resolve model\n(nn_id, version)"| REG
  NN_LAYER -->|"Inference request"| INFER
  INFER -->|"NNPerfResponse\n(Δ, σ, flags, metadata)"| NN_LAYER

  %% Integration & guard rails
  NN_LAYER -->|"Guardrails & fusion\n(y_final, actions)"| CORE

  %% Monitoring & logging
  NN_LAYER -->|"Usage stats,\nOOD events"| MON
  CORE -->|"Trace entries\n(y_base, y_final,\nΔ_applied, nn_id)"| LOG
  MON -->|"Drift alerts /\nretrain triggers"| REG
````

---

## 4. Data Flows & Interfaces (High-Level)

This asset is **illustrative**, not normative. Formal APIs live in:

* `ASSETS/API/02-20-13-NN_Perf_API.json` *(placeholder path)*
* ATA 95 DPP / model registry schemas

### 4.1 From Clients to Performance Computer

Typical clients:

* [02-20-11_Electronic_Flight_Bag](../02-20-11_Electronic_Flight_Bag/)
* CAOS / dispatch / SIM tooling (02-20-01 platform, internal tools)

They send **performance requests** to the Performance Computer, which:

1. Computes **deterministic baseline outputs** (`y_base`) via core algorithms.
2. Passes a structured **NNPerfRequest** into the NN integration layer (when enabled).

### 4.2 NN Integration Layer Responsibilities

The NN layer:

* Builds **request envelopes** with:

  * Inputs used by the deterministic core
  * Baseline outputs `y_base`
  * Context (flight, configuration, environment)
* Resolves which **model family / version** to use (via ATA 95 registry)
* Sends **inference requests** to ATA 95 inference services
* Applies **guard-rails & fusion logic** to compute `y_final`:

  * Envelope checks (OOD vs model validity domain)
  * Δ-bounding & monotonicity constraints
  * Uncertainty-aware weighting (`σ`-dependent)
  * Fallback to deterministic-only behavior on any failure

### 4.3 ATA 95 Ecosystem (Registry, Inference, Monitoring)

Within ATA 95:

* **Model Registry & DPP**

  * Holds model metadata (nn_id, version, training data, limitations)
  * Exposes lookups for the NN layer (e.g., “NN-TO-family-v1.3”)

* **Inference Service(s)**

  * Online inference endpoints (could be on-board, on-ground, or both)
  * Enforce authentication, integrity, version pinning

* **Monitoring & Drift**

  * Collects usage statistics, error metrics, OOD frequency
  * Feeds **drift detection and retraining** decisions
  * Produces artefacts referenced by 02-20-13-TRACE / 95-xx monitoring docs

### 4.4 Logging & Evidence

The Performance Computer logs **trace entries** whenever NN output influences results:

* `y_base`, `y_final`, `Δ_pred`, `Δ_applied`
* `nn_id`, `nn_version`, dataset IDs (via metadata)
* Validity flags / guardrail actions

These feed:

* **ATA 31 / CAOS** data lakes (post-flight analysis)
* **02-20-13 VERIF/EVIDENCE** artefacts
* **ATA 95** monitoring and lifecycle management (e.g., model decommissioning)

---

## 5. Intended Usage

* **Architecture / safety reviews:**
  Show clear separation between **deterministic core** and **NN correction path**, and how guardrails and logging are implemented.

* **Implementation alignment:**
  Provide a shared view for software, data, and safety engineers to implement the NN integration per [02-20-13-005](../02-20-13-005_NN_Performance_Predictor.md).

* **Certification & audits:**
  Used in DO-178C / AI assurance packages to explain:

  * Where NN is used
  * How deterministic fallback works
  * How traceability to ATA 95 DPP is maintained

---

## 6. Toolchain & Source

Recommended pattern:

* **Source diagram:**

  * `02-20-13-A-003_NN_Integration.mmd` (Mermaid)
* **Rendered asset:**

  * Export to `02-20-13-A-003_NN_Integration.svg` for use in slideware / PDFs.

If a separate tool is used (e.g. draw.io), keep:

* `.mmd` as the **canonical, GitHub-diffable source**
* `.svg` as the distribution format

---

## 7. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Asset:** 02-20-13-A-003 NN Integration
> **Maintainer:** Digital Ops & Performance Group

| Version | Date       | Author / Team                         | Notes                            |
| ------- | ---------- | ------------------------------------- | -------------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Performance WG | Initial architecture description |

```
```
