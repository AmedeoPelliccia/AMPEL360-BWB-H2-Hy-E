# 02-20-14-001 — Ground Ops Overview

**Document ID:** 02-20-14-001_Ground_Ops_Overview  
**Subsystem:** [02-20-14_Ground_Ops_Management](./README.md)  
**Parent ATA:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Status:** DRAFT / PLACEHOLDER  
**Owner:** Digital Operations & Ground Turnaround Domain  

---

## 1. Purpose

This document provides the **high-level overview** of the  
**02-20-14 Ground Ops Management** subsystem, including:

- The **concept of operations (ConOps)** for AMPEL360 turnarounds.  
- The **main actors, roles and responsibilities** on the ground.  
- The **turnaround phase model** and key milestones.  
- The **digital integration** between ground actors, CAOS, and flight-side systems  
  (EFB, WBC, Performance Computer, Predictive Ops NN).  

It is the entry point for more detailed specifications:

- [02-20-14-002_Turnaround_Orchestration.md](./02-20-14-002_Turnaround_Orchestration.md)  
- [02-20-14-003_GSE_and_Ramp_Services.md](./02-20-14-003_GSE_and_Ramp_Services.md)  
- [02-20-14-004_Loading_and_Fueling_Coordination.md](./02-20-14-004_Loading_and_Fueling_Coordination.md)  
- [02-20-14-005_Constraints_and_Slot_Management.md](./02-20-14-005_Constraints_and_Slot_Management.md)  
- [02-20-14-006_Integration_with_Ops_Systems.md](./02-20-14-006_Integration_with_Ops_Systems.md)  

---

## 2. Scope

### 2.1 Included

Ground Ops Management covers **digital coordination** of:

- **Turnaround orchestration**:
  - From **block-on** to **block-off**, including delays and irregular ops.  
  - Phase / milestone tracking, timestamps, SLAs and responsibilities.

- **Ramp & GSE services**:
  - Ground power, conditioned air, tows, catering, cleaning, water/LAV, de-icing, etc.  
  - Status of equipment and ground crews (allocated, en route, in use, faulted).

- **Loading & fueling coordination**:
  - Passenger and baggage flows, cargo loading, special loads.  
  - **H₂ fueling** and hybrid/CO₂ battery handling constraints (sequence, safety buffers).  
  - Alignment with **W&B** and **Performance** outputs.

- **Stand / gate / slot / airport constraints**:
  - Stand compatibility (size, jetway/remote, H₂ fueling capability).  
  - Slot/capacity constraints relevant for turnaround feasibility.

- **Integration with operations systems**:
  - `02-20-01_Digital_Ops_Platform` / CAOS event bus.  
  - `02-20-11_Electronic_Flight_Bag` (crew view of ground status).  
  - `02-20-12_Weight_Balance_Computer` (loadsheet / CG dependencies).  
  - `02-20-13_Performance_Computer` (de-icing, contamination, weight/CG constraints).  
  - `02-20-23_Predictive_Operations_NN` (turnaround risk and mitigation suggestions).

### 2.2 Excluded

The subsystem **does not** define:

- Detailed **airport infrastructure control** (e.g. A-CDM, stand allocation engine internals).  
- **H₂ fueling equipment design** or safety cases (ATA 28 / ATA 10).  
- Crew rostering, long-term maintenance planning, or network scheduling.  
- Onboard flight system design (ATA 27/42/95 etc.) — those are consumers/partners.

---

## 3. Concept of Operations (ConOps)

### 3.1 Turnaround as a Digital Workflow

Each AMPEL360 flight has an associated **Turnaround Instance**:

- Created at **schedule planning** or **slot allocation**.  
- Activated upon **inbound off-block** or **estimated arrival**.  
- Completed at **outbound off-block**.

The Turnaround Instance tracks:

- **Phases** (Block-on, Deboarding, Cleaning, Fueling, Boarding, Pushback, etc.).  
- **Milestones** (doors open, last pax off/on, fueling start/stop, cargo hold closed, etc.).  
- **Resources** (GSE units, crews, stands, service contracts).  
- **Constraints** (H₂ safety windows, curfews, slot times, W&B readiness).  

The subsystem exposes this state via:

- APIs / events on `02-20-01_Digital_Ops_Platform`.  
- Views and summaries in OCC tools, EFB, and CAOS dashboards.

### 3.2 Event-Driven Integration

Ground Ops Management is **event-centric**:

- Inbound flight events: ETA/ATA, landing, block-on, gate/stand change.  
- Ground events: GSE arrival/ready/fault, start/complete of tasks, fueling states.  
- Flight-side events: W&B finalised, performance data confirmed, crew ready.  
- Predictive events: risk of delay, recommended mitigation actions.

These events drive updates to:

- Turnaround status (ON-TIME / AT RISK / DELAYED).  
- Resource requests (e.g. additional GPU, backup fueling unit).  
- Notifications to EFB, OCC, and CAOS.

---

## 4. Main Actors & Roles

Ground Ops Management models a set of **roles** (human/organizational) and **systems**:

### 4.1 Ground Actors

- **Ramp Agent / Turnaround Coordinator**  
  - Oversees the turnaround at stand level.  
  - Confirms milestones (e.g. “boarding complete”, “fueling complete”).  

- **Ground Handling Crew**  
  - Baggage handlers, cargo loaders, cabin cleaners, catering teams, etc.  
  - Tasks and timings tracked per service.

- **H₂ Fueling Team**  
  - Specialised team handling liquid H₂ operations.  
  - Interfaces closely with safety systems and ATA 28.

- **Maintenance / Engineering Team**  
  - Handles MEL-related actions, defect rectification, technical delays.  

- **Operations Control Center (OCC)**  
  - Monitors network-level status.  
  - Makes decisions on gate swaps, aircraft swaps, delay acceptance, etc.

### 4.2 Digital Systems

- **Ground Ops Management (this subsystem)**  
  - Maintains the **authoritative digital model** of the turnaround.

- **CAOS / Digital Ops Platform (02-20-01)**  
  - Multi-flight event bus and analytics platform.  

- **EFB (02-20-11)**  
  - Provides crew with timely ground status, expected push time, constraints.

- **WBC (02-20-12) & Performance Computer (02-20-13)**  
  - Provide performance & load-critical data (e.g. final TOW, de-icing impacts).

- **Predictive Ops NN (02-20-23)**  
  - Provides risk scores and what-if simulations (e.g. “H₂ fueling delay risk”).

---

## 5. Turnaround Phase Model (High-Level)

Detailed phase definitions are given in  
[02-20-14-002_Turnaround_Orchestration.md](./02-20-14-002_Turnaround_Orchestration.md).  
This section provides a **high-level outline**.

Typical phases (names and ordering are configurable per airline/airport):

1. **PRE-ARRIVAL**  
   - Flight inbound, stand allocated, GSE and crews pre-planned.

2. **BLOCK-ON & ARRIVAL**  
   - Aircraft chocks in, parking brake set, GPU connection, safety checks.

3. **DEBOARDING & FIRST-PASS SAFETY**  
   - Passengers disembark; safety checks ensure fueling / servicing preconditions.

4. **CLEANING / CATERING / MAINTENANCE**  
   - Cabin turnaround, catering loading, minor maintenance as needed.

5. **LOADING & H₂ FUELING**  
   - Cargo/baggage loading/unloading under W&B constraints.  
   - H₂ fueling/defueling, respecting safety perimeters and time buffers.

6. **BOARDING**  
   - Passenger boarding with linkage to WBC (actual vs planned load).  

7. **CLOSE-OUT & PUSHBACK**  
   - Doors closed, final W&B and performance confirmed, pushback clearance.

Each phase has:

- **Entry conditions** (what must be true).  
- **Tasks** (with responsible actors and expected duration).  
- **Exit criteria** (what confirms phase completion).  

Ground Ops Management maintains the **current phase**, **phase progress**, and **critical path**.

---

## 6. Information Model (Conceptual)

This section sketches the **core objects** handled by the subsystem.

### 6.1 Key Entities

- `Turnaround`  
  - Identified by flight ID, date, aircraft tail, stand, etc.  
  - Contains phases, milestones, resource allocations.

- `Phase`  
  - Name, planned start/end, actual start/end, SLA.  
  - Set of tasks and dependencies.

- `Task`  
  - Task type (fueling, cleaning, GSE arrival, door close, etc.).  
  - Assigned actor (crew / handler / equipment).  
  - Status and timestamps.

- `Resource` (GSE / crew / stand)  
  - Type, capabilities, availability window, utilisation status.

- `Constraint`  
  - Time window (curfew, slot); stand restrictions; H₂ handling rules.  
  - Logic for whether certain tasks are allowed at specific times/configurations.

- `Event`  
  - Time-stamped state change (phase transition, task start/end, resource state).

### 6.2 ConOps-Level Data Flow

```mermaid
flowchart LR
  subgraph OPS["Ops & Planning (CAOS / OCC)"]
    PLAN["Flight & Turnaround Plan\n(schedule, stand, slots)"]
  end

  subgraph GOM["02-20-14 Ground Ops Management"]
    TA["Turnaround Instance\n(phases, tasks, resources)"]
    KPI["Turnaround KPIs & Status\n(ON-TIME / AT-RISK / DELAYED)"]
  end

  subgraph RAMP["Ramp & Service Providers"]
    GSE["GSE & Ground Crews"]
  end

  subgraph FLIGHT["Flight-Side Systems"]
    EFB["02-20-11 EFB"]
    WBC["02-20-12 WBC"]
    PERF["02-20-13 Performance"]
  end

  subgraph PRED["02-20-23 Predictive Ops NN"]
    NNOPS["Turnaround Risk & Mitigations"]
  end

  PLAN --> TA
  TA --> KPI
  GSE -->|Task updates\n(events)| TA
  TA -->|Ground status\n& milestones| EFB
  TA -->|Load/fueling events| WBC
  WBC -->|Final loadsheet\n& TOW| PERF
  NNOPS -->|Risk scores\n& suggestions| TA
  TA -->|Aggregated view| OPS
````

---

## 7. Integration with Other Subsystems

### 7.1 With EFB (02-20-11)

Ground Ops Management provides:

* **Ground timeline & status** to the crew:

  * Current phase, estimated time to off-block.
  * H₂ fueling timelines and constraints.
  * GSE readiness (e.g. de-icing scheduled, GPU connected).

* **Notifications**:

  * “Cargo loading complete”, “Fueling complete, awaiting loadsheet”, etc.

### 7.2 With WBC (02-20-12)

* Sends **loading/fueling events** and **special load information**.
* Receives flags like:

  * “Loadshed required”, “CG at limit”, “Loading sequence constraint”.
* Ground Ops uses these to:

  * Reprioritise tasks.
  * Coordinate with handlers (e.g. moving bags/cargo for CG or performance reasons).

### 7.3 With Performance Computer (02-20-13)

* Provides:

  * De-icing status, contamination flags, runway condition info (when sourced from ground).
* Consumes:

  * “Performance feasible / infeasible given current load & conditions” flags.
* Supports coordinated decision-making on:

  * Fuel uplift changes, payload offload, runway/slot selection.

### 7.4 With Predictive Ops NN (02-20-23)

* Sends:

  * Planned and actual turnaround timelines, task durations, resource usage.
* Receives:

  * **Delay risk predictions**, **choke point identification**, **mitigation suggestions**
    (e.g. request extra ground crew, split stand turn, alternate fueling unit).

---

## 8. Safety & Operations Considerations (Overview)

More detailed safety aspects reside in:

* H₂ / fueling chapters (ATA 28).
* Turnaround orchestration and constraints docs (02-20-14-002/004/005).

From the overview perspective:

* Ground Ops Management is **operationally critical** but typically treated as a
  **ground / airline system** (DO-278A-type environment) rather than airborne software.
* It must **not contradict** aircraft AFM limitations or safety envelopes:

  * WBC and Performance remain **authoritative** for weight/CG and performance.
* It should implement:

  * **Safe defaults** when external information (e.g. stand constraints, H₂ capabilities) is missing.
  * Clear **error/status propagation** to OCC and crew.

---

## 9. Relationships to Other Documents

* Subsystem README:

  * [02-20-14_Ground_Ops_Management/README.md](./README.md)

* Detailed functional specs:

  * [02-20-14-002_Turnaround_Orchestration.md](./02-20-14-002_Turnaround_Orchestration.md)
  * [02-20-14-003_GSE_and_Ramp_Services.md](./02-20-14-003_GSE_and_Ramp_Services.md)
  * [02-20-14-004_Loading_and_Fueling_Coordination.md](./02-20-14-004_Loading_and_Fueling_Coordination.md)
  * [02-20-14-005_Constraints_and_Slot_Management.md](./02-20-14-005_Constraints_and_Slot_Management.md)
  * [02-20-14-006_Integration_with_Ops_Systems.md](./02-20-14-006_Integration_with_Ops_Systems.md)

* Architecture & RTM assets (suggested):

  * `ASSETS/02-20-14-A-001_Ground_Ops_Architecture.md`
  * `ASSETS/02-20-14-A-002_Turnaround_Timeline.md`
  * `ASSETS/02-20-14-A-003_GSE_Allocation_Model.md`
  * `ASSETS/02-20-14-A-501_Requirements_Traceability.md`

---

## 10. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-14 Ground Ops Management
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                        | Notes                                |
| ------- | ---------- | ------------------------------------ | ------------------------------------ |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Ground Ops WG | Initial Ground Ops overview & ConOps |

```
```
