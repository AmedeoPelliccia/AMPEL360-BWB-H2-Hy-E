# 02-20-12-A-001 — W&B System Architecture

**Asset ID:** 02-20-12-A-001  
**Title:** Weight & Balance System Architecture  
**Subsystem:** [02-20-12_Weight_Balance_Computer](../02-20-12_Weight_Balance_Computer/)  
**Type:** Architecture Diagram + Explanatory Notes  
**Formats:** Markdown (Mermaid) · SVG (optional export)  
**Status:** DRAFT / PLACEHOLDER  



<img width="1200" height="700" alt="image" src="https://github.com/user-attachments/assets/86a5ed64-b7ca-4405-9beb-bdbb85888ee0" />

---

## 1. Purpose

This asset captures the **top-level architecture** of the  
**02-20-12 Weight & Balance Computer (WBC)**, showing:

- Internal **functional blocks**:
  - `02-20-12-002_Load_Calculation_Engine`
  - `02-20-12-003_CG_Envelope_Monitoring`
  - `02-20-12-004_H2_Fuel_Integration`
  - `02-20-12-005_Real_Time_CG_Tracking`
  - `02-20-12-006_Integration_with_ATA_28`
- External **interfaces and data flows** to:
  - `02-20-11_Electronic_Flight_Bag`
  - `02-20-13_Performance_Computer`
  - `02-20-01` Digital Ops / CAOS
  - ATA 28, ATA 31, ATA 95 and other relevant ATA chapters

It is intended as a **visual anchor** for requirements, design and V&V documents in  
the 02-20-12 subsystem.

---

## 2. Files

Located under:

`.../02-20-12_Weight_Balance_Computer/ASSETS/`

- **02-20-12-A-001_WB_Architecture.md** ← this document (canonical text + Mermaid)
- *(optional, recommended later)*:
  - `02-20-12-A-001_WB_Architecture.mmd` — Mermaid-only source (for reuse)
  - `02-20-12-A-001_WB_Architecture.svg` — exported diagram for slides / PDFs

---

## 3. Architecture Diagram (Mermaid)

> This Mermaid block is intended to render directly on GitHub.
> It shows upstream providers, the internal WBC blocks, and downstream consumers.

```mermaid
flowchart LR
  %% 02-20-12-A-001_WB_Architecture

  %% Upstream / context
  subgraph UP["Upstream & Context Systems"]
    EFB_IN["02-20-11\nElectronic Flight Bag\n(Loading Inputs)"]
    OPS["02-20-01\nDigital Ops / Load Planning\n& Flight Plan Data"]
    ATA28["ATA 28\nH₂ Fuel System\n(Tanks, Gauges, Modes)"]
  end

  %% WBC core
  subgraph WBC["02-20-12 — Weight & Balance Computer"]
    LCE["02-20-12-002\nLoad Calculation Engine"]
    CGMON["02-20-12-003\nCG Envelope Monitoring"]
    H2INT["02-20-12-004\nH₂ Fuel Integration"]
    RTCG["02-20-12-005\nReal-Time CG Tracking"]
    ATA28INT["02-20-12-006\nIntegration with ATA 28"]
  end

  %% Downstream / consumers
  subgraph DOWN["Downstream Consumers & Data Sinks"]
    EFB_OUT["02-20-11\nElectronic Flight Bag\n(W&B & CG Views)"]
    PERF["02-20-13\nPerformance Computer"]
    CAOS["02-20-01\nCAOS / Analytics Platform"]
    ATA31["ATA 31\nRecording & Flight Data"]
    ATA95["ATA 95\nNN Systems\n(optional assistance)"]
  end

  %% Upstream flows into WBC
  EFB_IN -->|"Loading data,\nmanual adjustments"| LCE
  OPS -->|"Planned payload,\nflight plan, scenarios"| LCE
  ATA28 -->|"Config & runtime\nH₂ tank states"| ATA28INT
  ATA28INT -->|"Mapped H₂ tanks\n(W&B mass items)"| H2INT
  H2INT -->|"H₂ mass & CG\nper phase"| LCE

  %% Internal WBC flows
  LCE -->|"Mass & CG\nper phase"| CGMON
  LCE -->|"Initial runtime\nW&B snapshot"| RTCG
  RTCG -->|"Updated mass & CG\n(time-based)"| CGMON

  %% Downstream flows from WBC
  LCE -->|"Ramp/TOW/LW,\nCG, envelopes"| EFB_OUT
  CGMON -->|"Status, margins\n(WITHIN/CLOSE/OUT)"| EFB_OUT

  LCE -->|"TOW/LW/ZFW,\nCG per phase"| PERF
  RTCG -->|"Runtime CG state\n+ quality flags"| PERF

  LCE -->|"Per-flight W&B\nsnapshots"| CAOS
  CGMON -->|"Envelope status\nstatistics"| CAOS
  RTCG -->|"Runtime CG traces\n(subsampled)"| CAOS

  LCE -->|"Key W&B states\n(TOW, LW, CG)"| ATA31
  RTCG -->|"Runtime CG\nrecording points"| ATA31

  %% Optional NN assistance (ATA 95)
  RTCG <-->|"NN-assisted\nestimation ΔCG\n(bound & monitored)"| ATA95
````

---

## 4. Narrative Overview

### 4.1 Upstream & Context

* **02-20-11 EFB (Inputs)**
  Provides planned **loading data** (pax, bags, cargo, H₂ quantities) and crew
  adjustments. This drives the deterministic W&B computations in the **Load
  Calculation Engine (LCE)**.

* **02-20-01 Digital Ops / Load Planning**
  Supplies **flight plan**, route, alternates, and potentially **pre-computed
  scenarios**. These influence both W&B scenarios and H₂ / mission-profile inputs.

* **ATA 28 H₂ Fuel System**
  Is the **authoritative source** of:

  * Tank geometry, capacities, roles.
  * H₂ quantities, gauges, flowmeters, system modes, faults.
    WBC integrates this information via `02-20-12-006_Integration_with_ATA_28` and
    `02-20-12-004_H2_Fuel_Integration`.

### 4.2 Internal WBC Blocks

* **02-20-12-002 — Load Calculation Engine (LCE)**
  Deterministic core that:

  * Represents all **mass items** (BEM, payload, H₂, CO₂ battery if significant).
  * Computes **Ramp, Taxi, TOW, ZFW, LW** and **CG (%MAC)** per phase.
  * Prepares structured outputs for EFB, Performance Computer, and CAOS.

* **02-20-12-003 — CG Envelope Monitoring**
  Evaluates mass & CG results against **AFM / certified envelopes**, providing:

  * **Margins and statuses** (`WITHIN_NORMAL`, `CLOSE_TO_LIMIT`, `OUT_OF_LIMIT`).
  * Inputs for crew feedback (EFB), performance gating, and fleet analytics.

* **02-20-12-004 — H₂ Fuel Integration**
  Converts ATA 28 H₂ configuration and consumption profiles into:

  * Per-tank or per-group **H₂ mass items**.
  * **Phase-based H₂ states** (ramp, taxi, T/O, cruise, approach, landing).
    Feeding directly into the LCE for W&B computations.

* **02-20-12-005 — Real-Time CG Tracking**
  Tracks **time-evolving** mass & CG during taxi and flight by:

  * Propagating the **initial W&B snapshot** from the LCE.
  * Fusing **H₂/fuel usage**, sensor data, and (optionally) NN estimates.
  * Providing runtime CG states and quality flags to EFB, Perf Computer, and ATA 31.

* **02-20-12-006 — Integration with ATA 28**
  Defines the **interfaces and contracts** to ATA 28:

  * Configuration-time tank geometry and capacities.
  * Runtime H₂ quantities, system modes and sensor faults.
    Serves as the **formal bridge** between H₂ system design and WBC.

### 4.3 Downstream Consumers

* **02-20-11 EFB (Outputs)**
  Receives W&B results (Ramp/TOW/LW, CG, envelope statuses) and real-time CG
  trends to support **crew decision-making** and loadsheet workflows.

* **02-20-13 Performance Computer**
  Consumes authoritative **TOW/LW/ZFW, CG** (and H₂ distribution where needed) for:

  * Takeoff & landing performance.
  * Cruise / hybrid envelope computations.
    Runtime CG states can be used for **in-flight performance checks**.

* **02-20-01 CAOS / Analytics**
  Ingests W&B snapshots, CG envelope statuses, and runtime CG traces to:

  * Monitor **fleet-wide loading patterns**.
  * Identify **near-limit operations** and optimization opportunities.

* **ATA 31 Recording**
  Receives selected W&B and CG states (from both LCE and Real-Time CG Tracking)
  as part of **flight data recording** for post-flight analysis.

* **ATA 95 Neural Networks (optional)**
  When enabled and approved, NN models from ATA 95 may:

  * Assist **Real-Time CG Tracking** or other WBC functions with **bounded ΔCG**.
  * Always sit behind **guardrails and deterministic fallback**.

---

## 5. Intended Usage

This asset should be referenced in:

* `02-20-12-001_WB_System_Overview.md` as the **canonical architecture view**.
* Design-level docs (`02-20-12-004/005/006`) when discussing **interfaces and flows**.
* V&V planning (`02-20-12-007_WB_V_and_V.md` once created) as the **baseline context**
  for end-to-end tests.

It is also suitable for:

* Internal reviews (architecture, safety, certification).
* Presentations to authorities or partners as a **high-level system picture**.

---

## 6. Toolchain & Source

Recommended workflow:

* Maintain the **Mermaid block** here (or in `.mmd`) as the **canonical source**.
* When needed for slideware / PDFs:

  * Export to `02-20-12-A-001_WB_Architecture.svg` using a Mermaid-compatible tool.
* Keep SVG **generated** from Mermaid (no manual edits), to preserve diffability and traceability.

---

## 7. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-12 Weight & Balance Computer
> **Asset:** 02-20-12-A-001 W&B System Architecture
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                         | Notes                                       |
| ------- | ---------- | ------------------------------------- | ------------------------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Performance WG | Initial W&B system architecture description |

```
```
