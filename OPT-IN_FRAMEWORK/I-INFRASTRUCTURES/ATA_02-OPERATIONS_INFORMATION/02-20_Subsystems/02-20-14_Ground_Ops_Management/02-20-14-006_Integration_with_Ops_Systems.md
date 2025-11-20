# 02-20-14-006 — Integration with Operations Systems

**Document ID:** 02-20-14-006_Integration_with_Ops_Systems  
**Subsystem:** [02-20-14_Ground_Ops_Management](./README.md)  
**Parent ATA:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Status:** DRAFT / PLACEHOLDER  
**Owner:** Digital Operations & Ground Turnaround Domain  

---

## 1. Purpose

This document defines how **02-20-14 Ground Ops Management** integrates with:

- `02-20-01_Digital_Ops_Platform` / **CAOS**  
- `02-20-11_Electronic_Flight_Bag` (EFB)  
- `02-20-12_Weight_Balance_Computer` (WBC)  
- `02-20-13_Performance_Computer`  
- `02-20-17_Weather_Information_System`  
- `02-20-23_Predictive_Operations_NN`  
- Additional cross-ATA functions (e.g. ATA 31 Recording, airport/A-CDM systems)

It specifies:

- The **integration patterns** (event-driven, API, batch).  
- The **logical interfaces and payloads** (high-level data contracts).  
- Key **responsibilities and ownership boundaries** between subsystems.  
- How Ground Ops Management contributes to and consumes from the **CAOS ecosystem**.

It complements:

- [02-20-14-001_Ground_Ops_Overview.md](./02-20-14-001_Ground_Ops_Overview.md)  
- [02-20-14-002_Turnaround_Orchestration.md](./02-20-14-002_Turnaround_Orchestration.md)  
- [02-20-14-003_GSE_and_Ramp_Services.md](./02-20-14-003_GSE_and_Ramp_Services.md)  
- [02-20-14-004_Loading_and_Fueling_Coordination.md](./02-20-14-004_Loading_and_Fueling_Coordination.md)  
- [02-20-14-005_Constraints_and_Slot_Management.md](./02-20-14-005_Constraints_and_Slot_Management.md)  

---

## 2. Scope

### 2.1 Included

This document covers:

- **Logical interfaces** between 02-20-14 and other 02-20 subsystems.  
- Use of the **CAOS event bus** (topic structure, event types, responsibilities).  
- High-level **request/response** APIs where relevant (e.g. queries to WBC/Performance).  
- **Data ownership** and **source-of-truth** conventions for turnaround-related data.  
- **Security & identity** considerations at the interface level (roles, tenancy).  

### 2.2 Excluded

Not covered in detail:

- Concrete **transport protocols** or message formats (e.g. HTTP vs gRPC, JSON schema).  
- Low-level **deployment details** or infrastructure (clusters, queues, routing).  
- Detailed **EFB UI design** (handled in 02-20-11).  
- Detailed **model lifecycle** for Predictive Ops NN (ATA 95 / 02-20-23).  

These are defined in:

- `02-20-01_Digital_Ops_Platform` implementation docs.  
- EFB / WBC / Performance subsystem design documents.

---

## 3. Integration Overview

### 3.1 Position in the CAOS Ecosystem

Ground Ops Management is a **CAOS-native subsystem**:

- Maintains the **authoritative Turnaround Instance** per flight (phases, tasks, resources).  
- Publishes **ground events** on the CAOS bus.  
- Subscribes to **flight, slot, weather, predictive** events.  
- Provides **APIs** for OCC tools, EFB and other subsystems to query turnaround state.

High-level architecture:

```mermaid
flowchart LR
  subgraph CAOS["02-20-01 Digital Ops Platform / CAOS"]
    BUS["Event Bus\n(topics, streams)"]
    API["Shared APIs\n(query/report)"]
  end

  subgraph GOM["02-20-14 Ground Ops Management"]
    TA["Turnaround Engine\n(phases, tasks, GSE, constraints)"]
  end

  subgraph FLIGHT["Flight-Side Systems"]
    EFB["02-20-11 EFB"]
    WBC["02-20-12 WBC"]
    PERF["02-20-13 Performance"]
  end

  subgraph ENV["Environment & Prediction"]
    WX["02-20-17 Weather"]
    PRED["02-20-23 Predictive Ops NN"]
  end

  TA <--> BUS
  TA <--> API

  EFB <--> API
  WBC <--> BUS
  PERF <--> BUS
  WX  --> BUS
  PRED <--> BUS
````

### 3.2 Source-of-Truth Principles

* **Turnaround state** (phases, tasks, GSE allocation, health) → Ground Ops (02-20-14).
* **Mass/CG and envelope** → WBC (02-20-12).
* **Performance feasibility** → Performance Computer (02-20-13).
* **Weather** → 02-20-17.
* **Predictive risk & recommendations** → 02-20-23.

Ground Ops aggregates these into a **coherent operational view**, but does not override
the numerical authority of WBC/Performance/Weather.

---

## 4. CAOS / Digital Ops Platform Integration (02-20-01)

### 4.1 Event Topics (Conceptual)

Indicative event families published **by Ground Ops**:

* `GROUND.TURNAROUND.*`

  * `GROUND.TURNAROUND.CREATED`
  * `GROUND.TURNAROUND.UPDATED`
  * `GROUND.TURNAROUND.PHASE_CHANGED`
  * `GROUND.TURNAROUND.HEALTH_CHANGED`

* `GROUND.TASK.*`

  * `GROUND.TASK.STATUS_CHANGED`

* `GROUND.GSE.*`

  * `GROUND.GSE.ALLOCATION_CREATED`
  * `GROUND.GSE.ALLOCATION_CONFLICT`
  * `GROUND.GSE.STATUS_CHANGED`

* `GROUND.H2_FUELING.*`

  * `GROUND.H2_FUELING.STATE_CHANGED`
  * `GROUND.H2_FUELING.WINDOW_UPDATED`

Events consumed **by Ground Ops** (from CAOS / other subsystems):

* `FLIGHT.STATUS.UPDATE` (off-block, on-block, ETA/ATA, etc.)
* `SLOT.UPDATE` (slot/CTOT/TOBT/TSAT changes)
* `WX.FLIGHT.WEATHER_SUMMARY` (02-20-17)
* `PREDOPS.TURNAROUND.RISK_UPDATE` (02-20-23)
* `WBC.STATUS.*`, `PERF.STATUS.*` (status broadcasts from 02-20-12/13)

### 4.2 API Endpoints (Logical)

Ground Ops exposes CAOS-facing APIs (examples, endpoint names indicative):

* `GET /ground/turnarounds/{turnaroundId}`

  * Returns current **Turnaround Instance** (phases, tasks, GSE, health).

* `GET /ground/turnarounds/by-flight/{flightId}`

  * Convenience lookup for OCC / other tools.

* `GET /ground/turnarounds/{turnaroundId}/timeline`

  * Timeline view (planned vs actual milestones, CTOT/TOBT overlay).

* `POST /ground/turnarounds/{turnaroundId}/what-if`

  * Scenario analysis: effect of changes in stand, fueling window, GSE availability.

CAOS may also provide aggregated views across flights using Ground Ops data.

---

## 5. EFB Integration (02-20-11)

### 5.1 Objectives

For flight crew, EFB shall receive from Ground Ops:

* **Turnaround status**: current phase, estimated off-block, health state.
* **H₂ fueling status**: planned vs actual fueling times, safety state, constraints.
* **Loading readiness**: major milestones (cargo complete, cabin ready, boarding windows).
* **Constraints & alerts**: curfew risks, slot risk, special ground constraints.

### 5.2 Data Flow (Sequence)

```mermaid
sequenceDiagram
  participant GOM as 02-20-14\nGround Ops
  participant CAOS as 02-20-01\nCAOS
  participant EFB as 02-20-11\nEFB

  GOM->>CAOS: GROUND.TURNAROUND.PHASE_CHANGED
  GOM->>CAOS: GROUND.H2_FUELING.STATE_CHANGED
  CAOS-->>EFB: Aggregated Ground Status\n(phase, fueling, readiness)
  EFB->>CAOS: Crew Queries (e.g. /ground/status?flightId=X)
  CAOS->>GOM: API call for current turnaround state
  GOM-->>CAOS: Turnaround snapshot
  CAOS-->>EFB: Snapshot for display
```

### 5.3 Example Information Elements

EFB “Ground” page (conceptual):

* `currentPhase`: TA-P4 LOADING & H₂ FUELING
* `estimatedOffBlockTime`: `2025-11-20T14:27Z`
* `groundHealth`: `AT_RISK` (reason: fueling delay, slot window tight)
* `h2FuelingState`: `ACTIVE` (ETA completion, safety mode)
* `loadingStatus`: cargo complete, boarding started, WBC intermediate OK

Ground Ops provides this as a **single coherent JSON structure** via CAOS APIs.

---

## 6. WBC Integration (02-20-12)

### 6.1 Responsibilities

* **Ground Ops**:

  * Sends **load/fuel events** derived from ramp operations.
  * Requests **intermediate and final WBC evaluations** when needed.
  * Enforces WBC-driven constraints (e.g. forbid additional load in aft hold).

* **WBC**:

  * Maintains **mass/CG and envelope calculations**.
  * Returns **status & constraints** in machine-readable form.

### 6.2 Event & API Interaction

Typical patterns:

* Ground Ops → WBC (via CAOS bus / API):

  * `LOAD.EVENT.CARGO_UPDATED`
  * `LOAD.EVENT.PAX_FINALIZED`
  * `FUEL.EVENT.H2_MASS_UPDATED`
  * `FUEL.EVENT.SESSION_COMPLETED`
  * `REQUEST.WBC.EVAL_INTERMEDIATE`
  * `REQUEST.WBC.EVAL_FINAL`

* WBC → Ground Ops:

  * `WBC.STATUS.INTERMEDIATE` (CG, mass, envelope).
  * `WBC.STATUS.FINAL`.
  * `WBC.ALERT.LOADING_SEQUENCE_CONSTRAINT`.
  * `WBC.ALERT.OUT_OF_ENVELOPE`.

### 6.3 Coordination Example (Sequence)

```mermaid
sequenceDiagram
  participant GOM as 02-20-14\nGround Ops
  participant WBC as 02-20-12\nWBC
  participant PERF as 02-20-13\nPerformance

  GOM->>WBC: FUEL.EVENT.H2_MASS_UPDATED
  GOM->>WBC: LOAD.EVENT.CARGO_UPDATED
  GOM->>WBC: REQUEST.WBC.EVAL_INTERMEDIATE
  WBC-->>GOM: WBC.STATUS.INTERMEDIATE (CG, envelope)
  GOM->>PERF: Request performance pre-check (optional)
  PERF-->>GOM: Constraints (e.g. margin warnings)
  GOM: Update turnaround health & rules for boarding/loading
```

Ground Ops uses these outputs to **update rules** in
[02-20-14-004_Loading_and_Fueling_Coordination.md](./02-20-14-004_Loading_and_Fueling_Coordination.md).

---

## 7. Performance Computer Integration (02-20-13)

### 7.1 Objectives

* **Before pushback**, Ground Ops & crew must know if performance is **feasible** with:

  * Actual TOW & CG (from WBC).
  * Runway condition & contamination.
  * De-icing status, weather, H₂ reserves.

* Ground Ops triggers or monitors calls to Performance as part of **close-out**.

### 7.2 Interaction Overview

Ground Ops provides to Performance:

* `PerfInput` snapshot:

  * `flightId`, `aircraftVariant`, `runway`, `config`,
  * `TOW`, `CG`, `H2Reserves`, `HybridEnergyStatus`,
  * `ContaminationState`, `DeicingStatus`, `Wind`, `Temp`, etc.

Performance returns:

* `PerfResult`:

  * `feasible`: bool
  * `limitingFactor`: string (e.g. “Runway length”, “Brake energy”)
  * `recommendedMitigations`: [e.g. reduce payload, change runway]

### 7.3 Sequence Example

```mermaid
sequenceDiagram
  participant GOM as 02-20-14\nGround Ops
  participant WBC as 02-20-12\nWBC
  participant PERF as 02-20-13\nPerformance

  GOM->>WBC: REQUEST.WBC.EVAL_FINAL
  WBC-->>GOM: WBC.STATUS.FINAL (TOW, CG, envelope)
  GOM->>PERF: PERF.REQUEST.CALC (PerfInput)
  PERF-->>GOM: PERF.RESULT (feasible, limitingFactor)
  GOM: Update readiness_state (READY_FOR_PUSH or WAITING_ACTION)
```

If Performance is **not feasible**, Ground Ops:

* Adjusts `LoadingPlan` / `FuelingPlan`.
* Commands further WBC evaluations.
* Updates turnaround health and CTOT/TOBT implications via CAOS.

---

## 8. Weather Information System Integration (02-20-17)

### 8.1 Inputs from Weather System

Ground Ops consumes from 02-20-17:

* Flight-specific weather summary:

  * Winds aloft, surface wind, temperature, QNH.
  * Icing risk, convective activity.
  * Crosswind / tailwind vs runway selection.

* Airport environmental conditions:

  * Temperature extremes (affecting GSE operations).
  * Precipitation type and rate (impacting de-icing / contamination).

### 8.2 Usage in Ground Ops

Ground Ops uses weather inputs to:

* Adjust **turnaround plans** (e.g. extra time for de-icing, slower boarding).
* Trigger additional **GSE tasks** (e.g. de-icing operations).
* Provide environment context to **Predictive Ops** and **Performance Computer**.

Weather events may be consumed from CAOS topics like:

* `WX.FLIGHT.WEATHER_SUMMARY`
* `WX.AIRPORT.CONDITIONS`

Ground Ops does **not** own weather data; it uses these inputs to refine tasks & constraints.

---

## 9. Predictive Ops NN Integration (02-20-23)

### 9.1 Data Provided to Predictive Ops

Ground Ops exports to 02-20-23:

* Turnaround plans and **actual progression** (phases, tasks, timestamps).
* GSE availability, usage metrics, conflicts.
* Constraint breaches or near misses (curfews, slot windows, H₂ concurrency).
* Final outcomes (on-time vs delayed, cause labels).

### 9.2 Predictions Consumed by Ground Ops

Predictive Ops NN returns:

* **Risk scores** per turnaround:

  * Probability of **off-block delay**.
  * Probability of **slot miss**.
  * Probability of **H₂ fueling delay**, **GSE shortage**, etc.

* **Mitigation recommendations**, e.g.:

  * Pre-position additional GSE.
  * Advance or compress certain tasks.
  * Swap stand to one with fewer constraints.

Ground Ops integrates these as **advisory inputs**:

* They may adjust turnaround plan & allocations where **constraints allow**.
* Hard constraints (safety, regulation) always override recommendations.

---

## 10. External / Airport Systems & ATA 31

### 10.1 Airport A-CDM / Stand & Slot Systems

Ground Ops exchanges information (via CAOS or direct integration) with:

* Airport **A-CDM** systems for CTOT/TOBT/TSAT.
* Stand & gate assignment systems.
* H₂ infrastructure monitoring systems.

Integration is typically at **airport/airline system level** (non-airborne), following:

* Local A-CDM specifications.
* Operator IT integration patterns.

Ground Ops ensures that **Turnaround Instances** remain consistent with these external
decisions and constraints.

### 10.2 ATA 31 — Recording

Key Ground Ops events and states may be persisted under ATA 31:

* Turnaround milestones & health states.
* H₂ fueling states and anomalies (digital, not the detailed ATA 28 sensor data).
* GSE conflict and shortage events.

This enables:

* Post-flight **analytics and investigations**.
* Continuous improvement of Predictive Ops and procedure design.

Recording formats and retention policies are defined in ATA 31 / CAOS data governance.

---

## 11. Security, Identity & Multi-Tenancy (Overview)

High-level principles:

* **Role-based access control (RBAC)**:

  * Flight crew (via EFB) see only flights they operate.
  * Ground handlers see only relevant flights/stands.
  * OCC / airline central users see network-level views.

* **Tenant separation**:

  * Where multiple airlines or handlers share infrastructure, data is partitioned
    by operator, except for **aggregated GSE/stand-level data** required for planning.

* **Auditability**:

  * Key changes (e.g. stand swaps, fueling window changes, manual overrides) are logged
    with actor identity and timestamps.

Concrete mechanisms (OAuth, mTLS, etc.) are defined in 02-20-01 CAOS security docs.

---

## 12. Relationships to Other Documents

* **02-20-14 Ground Ops Subsystem Docs**:

  * [02-20-14-001_Ground_Ops_Overview.md](./02-20-14-001_Ground_Ops_Overview.md)
  * [02-20-14-002_Turnaround_Orchestration.md](./02-20-14-002_Turnaround_Orchestration.md)
  * [02-20-14-003_GSE_and_Ramp_Services.md](./02-20-14-003_GSE_and_Ramp_Services.md)
  * [02-20-14-004_Loading_and_Fueling_Coordination.md](./02-20-14-004_Loading_and_Fueling_Coordination.md)
  * [02-20-14-005_Constraints_and_Slot_Management.md](./02-20-14-005_Constraints_and_Slot_Management.md)

* **Related subsystems**:

  * `../02-20-01_Digital_Ops_Platform/`
  * `../02-20-11_Electronic_Flight_Bag/`
  * `../02-20-12_Weight_Balance_Computer/`
  * `../02-20-13_Performance_Computer/`
  * `../02-20-17_Weather_Information_System/`
  * `../02-20-23_Predictive_Operations_NN/`

* **Planned assets** (suggested):

  * `ASSETS/02-20-14-A-001_Ground_Ops_Architecture.md`
  * `ASSETS/02-20-14-A-002_Turnaround_Timeline.md`
  * `ASSETS/02-20-14-A-003_GSE_Allocation_Model.md`
  * `ASSETS/02-20-14-A-501_Requirements_Traceability.md`

---

## 13. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-14 Ground Ops Management
> **Asset:** Integration with Operations Systems
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                        | Notes                             |
| ------- | ---------- | ------------------------------------ | --------------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Ground Ops WG | Initial integration specification |

```
```
