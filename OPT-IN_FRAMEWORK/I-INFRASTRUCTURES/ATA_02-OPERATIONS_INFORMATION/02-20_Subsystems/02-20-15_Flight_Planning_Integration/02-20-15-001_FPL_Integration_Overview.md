# 02-20-15-001 — Flight Planning Integration Overview

**Document ID:** 02-20-15-001_FPL_Integration_Overview  
**Subsystem:** [02-20-15_Flight_Planning_Integration](./README.md)  
**Parent Group:** [02-20 Turnaround & Ground Ops Coordination](../02-20-00_Turnaround_and_Ground_Ops.md) *(TBD)*  
**Parent ATA:** [ATA_02-OPERATIONS_INFORMATION](../README.md)  
**Axis:** I — Infrastructures  
**Status:** DRAFT / PLACEHOLDER  
**Owner:** Digital Operations, Dispatch & Ground Ops Domain  

---

## 1. Purpose

This document provides a **conceptual overview** of how:

- **Ground Ops Management (02-20-14)**  
- **Flight Planning / Dispatch systems**  
- **ATFM / slot management** and  
- **Predictive Ops NN (02-20-23)**  

interact within **AMPEL360 CAOS** to maintain a coherent view of:

- **Planned flight** (route, times, slot, performance assumptions)  
- **Turnaround reality** (GSE constraints, H₂ fueling, ramp progress)  
- **Operational risk** (delay probability, slot infringement risk)  

It defines:

- The **logical integration architecture** (see A-001)  
- Core **data exchanges** and key timestamps  
- High-level **use cases** and event flows  
- Hooks into **Predictive Ops NN** for decision support  

---

## 2. Scope

### 2.1 Included

- Mapping between **turnaround status** (02-20-14) and:

  - EOBT / TOBT / TSAT / CTOT, target off-block / takeoff times  
  - Delay codes and cause attribution (GSE-related vs other)  

- Integration patterns for:

  - Propagating ground-driven changes (e.g. delayed H₂ fueling) to FPL  
  - Receiving FPL changes (route, slot, constraints) and assessing turnaround impact  

- Information flows to/from:

  - **Dispatch / OCC tools**  
  - **ATFM / slot management services**  
  - **Predictive Ops NN (02-20-23)**  

### 2.2 Excluded

- Internal algorithms for route building, performance calculations, or cost index optimisation  
- ATC procedures, airspace sector design and network operations details  
- Detailed NN training / assurance (covered in ATA 95 / 02-20-23)  

---

## 3. Key Concepts & Data

### 3.1 Core Time Stamps

This subsystem focuses on the coherence of:

- **EOBT** — Estimated Off-Block Time (FPL view)  
- **TOBT** — Target Off-Block Time (airport/ground view)  
- **TSAT** — Target Start-up Approval Time (ATC/ATFM)  
- **CTOT** — Calculated Take-Off Time (slot constraint)  
- **AOBT / ATOT** — Actual Off-Block / Take-Off Time (realised performance)  

02-20-15 maintains **traceability** between:

- Ground events (from 02-20-14: tasks, GSE, constraints)  
- Derived **updates** to TOBT/EOBT/TSAT/CTOT  
- Final KPIs and delay attribution (for 02-20-23 training)  

### 3.2 Integration Context

```mermaid
flowchart LR
    GO["02-20-14 Ground Ops Mgmt\n(Turnaround, GSE, H₂ constraints)"]
    FP["Flight Planning & Dispatch\n(FPL, EOBT, route)"]
    ATFM["ATFM / Slots\n(CTOT, regulations)"]
    OCC["OCC / Ops Tools"]
    NN["02-20-23 Predictive Ops NN"]

    GO -->|Turnaround status,\nGSE constraints,\nexpected off-block| FP
    GO -->|Delay causes,\nstate, KPIs| NN
    FP -->|Updated EOBT,\nroute, fuel,\nslot needs| ATFM
    ATFM -->|Slot allocations\n(CTOT, TSAT)| FP
    FP -->|Consolidated plan| OCC
    GO -->|Operational view\n(progress, risk)| OCC
    NN -->|Risk scores,\nrecommendations| FP
    NN -->|Advisories\n(pre-position, buffers)| GO
````

---

## 4. Representative Use Cases

### 4.1 Ground-Driven EOBT Update

1. Ground Ops detects **H₂ fueling delay** or **GSE shortage** for a turnaround.

2. 02-20-14 emits updated **expected off-block** time and delay cause.

3. 02-20-15:

   * Maps this to updated **TOBT / EOBT**
   * Pushes a tentative update to **flight planning / dispatch**
   * Triggers re-check of **slot feasibility** (CTOT / TSAT vs new EOBT).

4. Dispatch/OCC either:

   * Accepts update → FPL / ATFM notified, or
   * Requests mitigations (stand swap, resource prioritisation, schedule tweak).

5. All updates are logged for **traceability & NN training**.

### 4.2 FPL-Driven Ground Impact

1. Flight Planning updates **route / cruise level** to comply with a regulation.

2. CTOT moves, affecting required **turnaround completion time**.

3. 02-20-15:

   * Receives new schedule from FPL/ATFM
   * Compares with current 02-20-14 turnaround progress & GSE constraints
   * Computes **feasibility** and flags potential **ground-driven risk**.

4. If risk is high:

   * 02-20-23 is invoked to estimate delay probability and suggest buffers.
   * OCC can trigger mitigation actions (e.g. prioritise H₂ fueling, re-sequence tasks).

---

## 5. Interfaces (Preview)

Detailed interface specs will live in:

* [02-20-15-002_Turnaround_to_FPL_Interface.md](./02-20-15-002_Turnaround_to_FPL_Interface.md)
* [02-20-15-003_Slots_and_ATFM_Integration.md](./02-20-15-003_Slots_and_ATFM_Integration.md)
* [02-20-15-004_FPL_Change_Propagation.md](./02-20-15-004_FPL_Change_Propagation.md)
* [02-20-15-005_Predictive_Ops_FPL_Hooks.md](./02-20-15-005_Predictive_Ops_FPL_Hooks.md)

Key payload families (to be formalised):

* **Turnaround → FPL:**

  * Turnaround ID, stand, phase, tasks progress
  * GSE / H₂ constraint status
  * Proposed new TOBT / expected off-block, delay cause

* **FPL / ATFM → Turnaround:**

  * FPL updates (route, cruise, fuel, restrictions)
  * CTOT / TSAT / slot regulation updates
  * Required buffers or latest acceptable off-block time

* **Predictive Ops NN:**

  * Risk scores: `p_departure_delay`, `p_slot_infringement`
  * Recommended buffers / stand choices / pre-positioning

---

## 6. Links to Other Assets

* Ground Ops:

  * [../02-20-14_Ground_Ops_Management/README.md](../02-20-14_Ground_Ops_Management/README.md)
  * [../02-20-14_Ground_Ops_Management/02-20-14-A-003_GSE_Allocation_Model.md](../02-20-14_Ground_Ops_Management/02-20-14-A-003_GSE_Allocation_Model.md)

* Predictive Ops NN (planned):

  * `../02-20-23_Predictive_Ops_NN/` (TBD path)

* Test Data:

  * [TEST_DATA/02-20-15-T-001_FPL_Delay_Scenarios.json](./TEST_DATA/02-20-15-T-001_FPL_Delay_Scenarios.json)

---

## 7. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-15 Flight Planning Integration
> **Asset:** FPL Integration Overview
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                      | Notes                       |
| ------- | ---------- | ---------------------------------- | --------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Dispatch WG | Initial conceptual overview |
