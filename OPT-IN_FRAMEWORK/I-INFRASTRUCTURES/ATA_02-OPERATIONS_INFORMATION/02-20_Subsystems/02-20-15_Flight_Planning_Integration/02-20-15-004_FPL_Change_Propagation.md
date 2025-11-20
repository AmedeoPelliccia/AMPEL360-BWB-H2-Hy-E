# 02-20-15-004 — FPL Change Propagation

**Document ID:** 02-20-15-004_FPL_Change_Propagation  
**Subsystem:** [02-20-15_Flight_Planning_Integration](./README.md)  
**Parent Group:** 02-20 Turnaround & Ground Ops Coordination *(TBD doc link)*  
**Parent ATA:** [ATA_02-OPERATIONS_INFORMATION](../README.md)  
**Axis:** I — Infrastructures  
**Status:** DRAFT / WORKING  
**Owner:** Digital Operations, Dispatch & Ground Ops Domain  

---

## 1. Purpose

This document specifies how **Flight Planning / ATFM changes** are **propagated** into:

- **02-20-14 Ground Ops Management** (turnaround, GSE, H₂ constraints)  
- **OCC / ops tools**  
- **Predictive Ops NN (02-20-23)**  

via the **02-20-15 Flight Planning Integration** layer.

It defines:

- The main **types of FPL/ATFM changes** relevant to ground operations  
- The **decision logic** used to assess **ground feasibility & risk**  
- The **event flows** for propagating changes to the turnaround engine and OCC  
- The **hooks into test data** and future RTM for assurance

The goal is a coherent, auditable process for **“plan changed in FPL → what does it mean for the ground?”**.

---

## 2. Scope

### 2.1 Included

- Normalised handling of:

  - EOBT / schedule shifts  
  - CTOT / TSAT / slot allocation changes (in cooperation with 02-20-15-003)  
  - Route / performance changes that affect ground timing or requirements  
  - Flight cancellations, delays, diversions from the FPL side  

- Propagation of these changes to:

  - Turnaround state & target times (02-20-14)  
  - GSE / H₂ constraint risk assessment (02-20-14, 02-20-23)  
  - OCC alerts, dashboards and decision-support views  

### 2.2 Excluded

- Detailed slot / regulation semantics (covered in [02-20-15-003](./02-20-15-003_Slots_and_ATFM_Integration.md))  
- Internal FPL system logic (route building, cost index, fuel optimisation)  
- Airline-specific business rules for commercial decisions (e.g. flight cancellation criteria)  

---

## 3. References

- Flight Planning Integration Overview:  
  - [02-20-15-001_FPL_Integration_Overview.md](./02-20-15-001_FPL_Integration_Overview.md)  

- Turnaround ↔ FPL Interface:  
  - [02-20-15-002_Turnaround_to_FPL_Interface.md](./02-20-15-002_Turnaround_to_FPL_Interface.md)  

- Slots & ATFM:  
  - [02-20-15-003_Slots_and_ATFM_Integration.md](./02-20-15-003_Slots_and_ATFM_Integration.md)  

- Ground Ops:  
  - [../02-20-14_Ground_Ops_Management/02-20-14-002_Turnaround_Orchestration.md](../02-20-14_Ground_Ops_Management/02-20-14-002_Turnaround_Orchestration.md)  
  - [../02-20-14_Ground_Ops_Management/02-20-14-A-003_GSE_Allocation_Model.md](../02-20-14_Ground_Ops_Management/02-20-14-A-003_GSE_Allocation_Model.md)  

- Test Data (planned/partial):  
  - [TEST_DATA/02-20-15-T-001_FPL_Delay_Scenarios.json](./TEST_DATA/02-20-15-T-001_FPL_Delay_Scenarios.json)  
  - Ground allocation sets in 02-20-14 (`T-002`, `T-003`)  

---

## 4. Change Types

FPL/ATFM changes are classified to drive consistent propagation behaviour.

### 4.1 Schedule-Related Changes

Changes to **time assumptions** without altering the flight’s route or network context:

- EOBT changes (±Δ minutes)  
- Target departure / off-block constraints from the airline side  
- Buffer adjustments (ground_buffer_min, taxi_buffer_min)  

Represented via:

- `FplUpdateEvent` (see 02-20-15-002)  
- Possibly accompanied by a refreshed `FplPlanSnapshot`  

### 4.2 Slot / ATFM Changes

Changes to **CTOT / TSAT / slot window**, typically triggered by:

- New or updated **SlotRegulation**  
- Re-allocation of slot times (`SlotAllocation`, `SlotUpdateEvent`)

Defined in detail in [02-20-15-003_Slots_and_ATFM_Integration.md](./02-20-15-003_Slots_and_ATFM_Integration.md).

### 4.3 Route / Performance Changes

Changes that may indirectly affect ground requirements:

- Route change resulting in new **fuel uplift** requirements  
- Cruise level / cost index changes that alter **fuel or weight assumptions**  
- Additional performance constraints (e.g. ETOPS alternates, H₂ consumption envelope)

These can affect:

- H₂ fueling duration and sequencing vs other tasks  
- Potential requirement to **re-open fueling** or adjust ground buffer  

### 4.4 Flight Lifecycle Changes

- Flight cancellation  
- Flight diversion (changed departure or arrival airport)  
- Turnaround split/merge (e.g. tail swap, aircraft change)

These must be propagated to 02-20-14 to:

- Stop or reassign GSE tasks  
- Close or transform turnaround entities  

### 4.5 Priority / Criticality Changes

- Emergency designation (MEDICAL, TECH, SECURITY, etc.)  
- “Must-protect” slot or connection priority changes

Used to drive:

- Pre-emption policies in 02-20-14 allocation (e.g. EMERGENCY priority vs BASELINE)  
- OCC decision support and KPI weighting  

---

## 5. Propagation Flows (Conceptual)

### 5.1 Schedule-Only Change (Minor EOBT Shift)

Example: EOBT moves +5 minutes, still consistent with turnaround.

```mermaid
sequenceDiagram
    participant FPL as FPL / Dispatch
    participant FPI as 02-20-15 Integration
    participant GO as 02-20-14 Ground Ops
    participant OCC as OCC / Ops Tools

    FPL->>FPI: FPI.FPL_UPDATE (EOBT +5 min, reason=NORMAL_REPLAN)
    FPI->>GO: Request latest GROUND.TURNAROUND.SNAPSHOT
    GO-->>FPI: Snapshot S1 (feasible, no major constraints)

    FPI->>FPI: Assess feasibility vs new EOBT (OK)
    FPI->>GO: Update target completion & advisory (optional)
    FPI->>OCC: Info: "EOBT updated +5 min, ground feasible"
````

System behaviour:

* **No forced replanning** of GSE; existing allocations remain valid
* Only **target completion times** and OCC views are updated

### 5.2 Earlier CTOT / EOBT (Potential Ground Infeasibility)

Example: CTOT brought forward, plus EOBT -10 minutes, risking missed slot.

```mermaid
sequenceDiagram
    participant FPL as FPL / Dispatch
    participant ATFM as ATFM / Slot Provider
    participant FPI as 02-20-15 Integration
    participant GO as 02-20-14 Ground Ops
    participant NN as 02-20-23 Predictive Ops NN
    participant OCC as OCC / Ops Tools

    ATFM->>FPI: FPI.ATFM_SLOT_UPDATE (CTOT -10 min)
    FPL->>FPI: FPI.FPL_UPDATE (EOBT -10 min, reason=ATFM_REGULATION)
    FPI->>GO: Request GROUND.TURNAROUND.SNAPSHOT (S2)
    GO-->>FPI: Snapshot S2 (critical tasks incomplete, H₂ fueling pending)

    FPI->>FPI: Compute ground feasibility vs new CTOT/EOBT
    alt High risk / infeasible
        FPI->>NN: Request risk assessment (delay + slot risk)
        NN-->>FPI: Risk scores + recommended mitigations
        FPI->>OCC: Alert: "Slot at risk due to ground state" + options
        FPI->>FPL: Advisory (possible need to re-slot or relax CTOT)
    else Feasible
        FPI->>OCC: Info: "Slot remains feasible; monitor only"
    end
```

System behaviour:

* If **infeasible**:

  * OCC sees a **slot-risk alert** with proposed actions (e.g. prioritise H₂ fueling, re-sequence tasks, consider re-slotting)
  * 02-20-14 may be instructed to **re-prioritise** GSE allocations or adopt EMERGENCY priority for certain tasks

* If **feasible** but tight:

  * OCC is informed of reduced margin
  * Predictive Ops NN may adjust risk estimates for future learning

### 5.3 Route / Fuel Change Affecting H₂ Fueling

Example: route change increases required H₂ uplift by 20%, extending fueling duration.

1. FPL sends `FPI.FPL_UPDATE` indicating:

   * Increased planned fuel/H₂ uplift
   * Possibly new performance / range constraints

2. 02-20-15 calculates:

   * New **expected fueling duration** and updated **H₂ fueling time window**
   * Impact on **overlap with loading/boarding** safety rules

3. 02-20-15 notifies 02-20-14 to:

   * Adjust H₂ fueling **task duration** and **time window**
   * Recompute constraints according to [02-20-14-004] and [02-20-14-005]

4. If safety rules would be violated:

   * A **rescheduling** proposal is generated (e.g. shift boarding, move stand, adjust TOBT/EOBT)
   * OCC is alerted with options & trade-offs

---

## 6. Decision Logic

### 6.1 Feasibility Assessment

At each FPL/ATFM change, 02-20-15 uses a **feasibility function**:

```text
feasibility = f(
  turnaround_state,              # From TurnaroundStatusSnapshot
  required_completion_time,      # From FplPlanSnapshot / SlotAllocation
  gse_constraints,               # From 02-20-14
  safety_rules,                  # From 02-20-14-004 / -005
  buffers                        # ground_buffer_min, taxi_buffer_min
)
```

Result is categorised as:

* `FEASIBLE_WITH_MARGIN`
* `FEASIBLE_TIGHT`
* `INFEASIBLE`

Each category drives different propagation behaviour:

| Category             | Behaviour                                                                |
| -------------------- | ------------------------------------------------------------------------ |
| FEASIBLE_WITH_MARGIN | Informational updates to GO/OCC; no replan required.                     |
| FEASIBLE_TIGHT       | OCC informed; Predictive Ops NN may be used; optional re-prioritisation. |
| INFEASIBLE           | OCC alert, recommended mitigations, potential re-slot/retime proposals.  |

### 6.2 Precedence & Roles

* **FPL/ATFM** retain authority over:

  * Route, performance, and network slot decisions

* **02-20-14** retains authority over:

  * Actual turnaround execution and GSE feasibility

* **02-20-15** is responsible for:

  * Making inconsistencies explicit
  * Proposing changes or highlighting risk; not unilaterally enforcing schedule decisions

---

## 7. Data Elements for Change Propagation

This section clarifies the **minimum fields** needed for robust propagation.

### 7.1 Change Vector

All FPL/ATFM changes are normalised to a **change vector**:

```text
FplChangeVector {
  event_id: string,
  flight_id: string,
  airport: string,
  timestamp: datetime,
  delta_eobt_min: int | null,
  delta_ctot_min: int | null,
  delta_tsat_min: int | null,
  route_changed: bool,
  performance_changed: bool,
  slot_regulation_changed: bool,
  priority_changed: bool,
  lifecycle_changed: bool,       # e.g. cancellation/diversion
  source_event_ids: [string]     # link to underlying FplUpdateEvent / SlotUpdateEvent / regs
}
```

This is used internally by 02-20-15 to:

* Select **feasibility heuristics** and **test cases**
* Feed **features** to Predictive Ops NN

### 7.2 Impact Assessment Summary

For each processed change vector, 02-20-15 produces an internal summary:

```text
FplChangeImpact {
  impact_id: string,
  flight_id: string,
  airport: string,
  change_vector_id: string,
  feasibility_category: enum{FEASIBLE_WITH_MARGIN, FEASIBLE_TIGHT, INFEASIBLE},
  key_constraints: [string],          # e.g. ["H2_FUELING_DURATION", "GPU_SHORTAGE"]
  affected_turnaround_tasks: [string],
  recommended_actions: [string],      # human-readable, for OCC
  nn_consulted: bool,
  decision_taken: string | null       # as recorded by OCC/dispatch
}
```

This structure is not necessarily exposed externally but is crucial for:

* Logging, audits and explainability
* Building labelled datasets for 02-20-23

---

## 8. Error Handling & Fallbacks

02-20-15 must handle:

* **Missing or stale turnaround snapshots**
* **Inconsistent identifiers** (e.g. flight ID mismatch between FPL and Ground Ops)
* **Latency** between FPL and ground state updates

Fallback rules:

* If **no recent snapshot** is available:

  * Mark feasibility as **UNKNOWN**
  * Issue a `FPI.DATA_QUALITY_ALERT` to OCC
  * Avoid auto-accepting aggressive schedule tightening

* If **identifier mismatch**:

  * Do not attempt automatic propagation
  * Log and raise `FPI.IDENTIFIER_MISMATCH` event for investigation

* If **high-frequency flapping** (many small changes):

  * Rate-limit propagation to 02-20-14
  * Aggregate changes into a **batched assessment**

---

## 9. Test & Traceability Hooks

* `TEST_DATA/02-20-15-T-001_FPL_Delay_Scenarios.json` exercises:

  * Ground-driven TOBT/EOBT updates
  * FPL-driven schedule changes and their propagation patterns

* Future datasets (`T-002`, `T-003`) are expected to cover:

  * Slot re-allocations vs turnaround feasibility
  * Route change / fuel uplift impacts on H₂ fueling tasks
  * Flight cancellations / diversions and GSE ramp-down behaviour

In the future:

* `02-20-15-A-501_Requirements_Traceability.md` will map:

  * 02-20-15-RQ-xxx (FPL change handling requirements)
  * → to data structures & flows in this document
  * → to test IDs in `02-20-15-T-00x`

---

## 10. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-15 Flight Planning Integration
> **Asset:** FPL Change Propagation
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                      | Notes                                               |
| ------- | ---------- | ---------------------------------- | --------------------------------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Dispatch WG | Initial definition of FPL change propagation logic. |

```
::contentReference[oaicite:0]{index=0}
```
