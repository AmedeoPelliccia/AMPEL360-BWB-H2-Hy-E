# 02-20-12-A-501 — Requirements Traceability Matrix (RTM)

**Asset ID:** 02-20-12-A-501_Requirements_Traceability  
**Title:** WBC Requirements Traceability Matrix  
**Subsystem:** [02-20-12_Weight_Balance_Computer](../02-20-12_Weight_Balance_Computer/)  
**Type:** Traceability / Certification Asset  
**Status:** DRAFT / PLACEHOLDER  
**Owner:** Digital Operations & Aircraft Performance Domain  

---

## 1. Purpose

This document defines the **Requirements Traceability Matrix (RTM)** for the  
**02-20-12 Weight & Balance Computer (WBC)**.

It provides **bi-directional traceability** between:

- Operational / safety / certification **requirements**  
- WBC **design artefacts** and **algorithms**  
- **Implementation units** (SW components – to be linked later)  
- **Verification**: test cases, analyses, reviews and recorded evidence  

The RTM is intended to be **DO-178C–friendly** and compatible with higher-level  
aircraft safety / certification artefacts.

---

## 2. Scope & Coverage

The RTM covers **deterministic WBC functions**:

- Static W&B calculation (Ramp / Taxi / TOW / CRZ / APP / LDG)  
- BWB CG envelope monitoring (phase-based)  
- H₂ fuel integration at W&B abstraction level  
- Real-time CG tracking (deterministic + sensor fusion; optional NN augmentation)  
- Integration with **ATA 28 H₂ Fuel System**  
- Scenario / what-if evaluation for operations and CAOS

Out of scope for this document (but referenced where needed):

- Detailed ATA 28 system requirements  
- Detailed hybrid / energy requirements (ATA 10/21/36, 02-20-13)  
- ATA 95 NN lifecycle requirements  
- UI/UX specifics (EFB visualisation & alerting)

---

## 3. Reference Documents

**WBC Design & Architecture**

- [02-20-12-001_WB_System_Overview.md](../02-20-12-001_WB_System_Overview.md)  
- [02-20-12-002_Load_Calculation_Engine.md](../02-20-12-002_Load_Calculation_Engine.md)  
- [02-20-12-003_CG_Envelope_Monitoring.md](../02-20-12-003_CG_Envelope_Monitoring.md)  
- [02-20-12-004_H2_Fuel_Integration.md](../02-20-12-004_H2_Fuel_Integration.md)  
- [02-20-12-005_Real_Time_CG_Tracking.md](../02-20-12-005_Real_Time_CG_Tracking.md)  
- [02-20-12-006_Integration_with_ATA_28.md](../02-20-12-006_Integration_with_ATA_28.md)  

**Architecture & Analysis Assets**

- [02-20-12-A-001_WB_Architecture.md](./02-20-12-A-001_WB_Architecture.md)  
- [02-20-12-A-002_CG_Envelope_BWB.md](./02-20-12-A-002_CG_Envelope_BWB.md)  
- [02-20-12-A-003_H2_Fuel_Effects.md](./02-20-12-A-003_H2_Fuel_Effects.md)  
- [02-20-12-A-101_Calculation_Algorithms.md](./02-20-12-A-101_Calculation_Algorithms.md)  

**Planned / Related**

- `02-20-12-007_WB_V_and_V.md` *(planned – V&V plan & coverage)*  
- `TEST_DATA/02-20-12-T-001_WB_Scenarios_Ramp_TOW_LW.json`  
- `TEST_DATA/02-20-12-T-002_WB_CG_Envelopes.json`  
- `TEST_DATA/02-20-12-T-003_WB_H2_Evolution.json`  
- `TEST_DATA/02-20-12-T-005_WB_H2_Reserves_And_Imbalance.json`  
- `TEST_DATA/02-20-12-T-006_RT_CG_Scenarios.json`  
- `TEST_DATA/02-20-12-T-007_RT_CG_SensorFusion.json`  
- `TEST_DATA/02-20-12-T-008_RT_CG_NN_Augmentation.json`  

*(Test artefacts are placeholders / to be created.)*

---

## 4. Requirement Taxonomy (02-20-12)

For WBC, requirements are grouped as:

- `RQ-02-20-12-WB-CORE-*` — Core mass & CG computation  
- `RQ-02-20-12-CG-*` — CG envelope monitoring & limits  
- `RQ-02-20-12-H2-*` — H₂ representation & evolution at W&B level  
- `RQ-02-20-12-RT-*` — Real-time CG tracking  
- `RQ-02-20-12-ATA28-*` — Integration with ATA 28 H₂ fuel system  
- `RQ-02-20-12-SAF-*` — Safety / integrity / fault behaviour  

**NOTE:** Formal requirement statements may live in dedicated RQ docs  
(e.g. `../RQ/02-20-12-RQ_WB_Core.md`). This RTM references the IDs independently  
of their storage location.

---

## 5. High-Level Requirement Set (Summary)

> **All texts below are requirement *summaries* for traceability – not the normative wording.**

### 5.1 Core W&B

- **RQ-02-20-12-WB-CORE-001** —  
  WBC shall compute **total mass and CG** for at least phases  
  *Ramp, Taxi, TOW, Cruise, Approach, Landing* based on configured mass items.

- **RQ-02-20-12-WB-CORE-002** —  
  WBC shall support **multiple load scenarios** (what-if) for the same flight.

- **RQ-02-20-12-WB-CORE-003** —  
  WBC shall expose W&B results to **EFB**, **Performance Computer**, and **CAOS**  
  via defined interfaces.

### 5.2 CG Envelopes (BWB)

- **RQ-02-20-12-CG-001** —  
  WBC shall evaluate each phase mass/CG against the **BWB CG envelope** applicable  
  to the **variant and phase**.

- **RQ-02-20-12-CG-002** —  
  WBC shall compute **margins** to forward/aft CG and mass limits and classify  
  state as `WITHIN_NORMAL`, `CLOSE_TO_LIMIT`, or `OUT_OF_LIMIT`.

- **RQ-02-20-12-CG-003** —  
  WBC shall support **phase-specific envelopes** (e.g. TOW vs CRZ vs LDG) and  
  log envelope status for **post-flight analysis**.

### 5.3 H₂ Integration

- **RQ-02-20-12-H2-001** —  
  WBC shall represent each H₂ tank/group as **mass items** consistent with  
  ATA 28 configuration, including arms and capacities.

- **RQ-02-20-12-H2-002** —  
  WBC shall propagate **H₂ mass evolution** across mission segments (including taxi)  
  using mission profiles and ATA 28 inputs.

- **RQ-02-20-12-H2-003** —  
  WBC shall represent **H₂ reserves and boil-off** at W&B abstraction level and  
  support checking for **reserve shortfalls**.

### 5.4 Real-Time CG

- **RQ-02-20-12-RT-001** —  
  Real-Time CG Tracking shall produce a **time-resolved mass/CG estimate** from  
  pre-flight W&B and mission profile.

- **RQ-02-20-12-RT-002** —  
  Real-Time CG Tracking shall **fuse sensor data** (ATA 28 etc.) where available  
  and degrade gracefully when sensors are degraded.

- **RQ-02-20-12-RT-003** —  
  If **NN-based corrections** are used, they shall be **bounded**, monitored, and  
  always backed by deterministic fallback.

### 5.5 ATA 28 Integration & Safety

- **RQ-02-20-12-ATA28-001** —  
  WBC shall import H₂ tank configuration and runtime data from ATA 28 via a  
  defined, configuration-controlled interface.

- **RQ-02-20-12-ATA28-002** —  
  WBC shall correctly flag degraded modes and **fall back to conservative  
  estimates** upon ATA 28 sensor faults.

- **RQ-02-20-12-SAF-001** —  
  WBC shall detect and flag **impossible or unsafe states** (negative tank mass,  
  missing envelope, invalid MAC, etc.) and expose machine-readable error codes.

---

## 6. RTM — Requirements ↔ Design ↔ Verification (Excerpt)

> This is the **working matrix**; additional rows will be appended as requirements are refined.

| Req ID                      | Summary (non-normative)                                        | Design / Algorithm References                                                                                                                                     | Verification Method(s)        | Planned Evidence / Test Artefacts                                                                                         |
| --------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| RQ-02-20-12-WB-CORE-001     | Compute mass & CG for phases (Ramp..LDG)                       | [02-20-12-002](../02-20-12-002_Load_Calculation_Engine.md) · [A-001](./02-20-12-A-001_WB_Architecture.md) · [A-101 §5–6](./02-20-12-A-101_Calculation_Algorithms.md) · ALG-WB-01 · ALG-WB-02 | Test + Analysis               | `02-20-12-T-001_WB_Scenarios_Ramp_TOW_LW.json` · Unit tests for ALG-WB-01/02 · Integration tests with EFB/Perf outputs   |
| RQ-02-20-12-WB-CORE-002     | What-if scenarios support                                      | [02-20-12-002](../02-20-12-002_Load_Calculation_Engine.md) · [A-101 §10](./02-20-12-A-101_Calculation_Algorithms.md) · ALG-WB-06                                  | Test                          | Scenario batch tests using multiple payload / H₂ configurations                                                          |
| RQ-02-20-12-CG-001          | Evaluate mass/CG vs BWB envelope                               | [02-20-12-003](../02-20-12-003_CG_Envelope_Monitoring.md) · [A-002](./02-20-12-A-002_CG_Envelope_BWB.md) · [A-101 §9](./02-20-12-A-101_Calculation_Algorithms.md) · ALG-WB-05               | Test + Analysis               | `02-20-12-T-002_WB_CG_Envelopes.json` · Envelope boundary tests (inside/edge/outside)                                   |
| RQ-02-20-12-CG-002          | Compute CG margins & status categories                         | Same as above (ALG-WB-05)                                                                                                                                         | Test                          | Margin verification against known reference points · Status mapping checks                                              |
| RQ-02-20-12-H2-001          | Represent H₂ tanks as mass items                               | [02-20-12-004](../02-20-12-004_H2_Fuel_Integration.md) · [02-20-12-006](../02-20-12-006_Integration_with_ATA_28.md) · [A-003](./02-20-12-A-003_H2_Fuel_Effects.md) · ALG-WB-04             | Test + Review                 | Static config import tests (`H2TankConfig`) · Mass item mapping checks                                                  |
| RQ-02-20-12-H2-002          | H₂ mass evolution over mission                                 | [02-20-12-004](../02-20-12-004_H2_Fuel_Integration.md) · [A-003](./02-20-12-A-003_H2_Fuel_Effects.md) · ALG-WB-03 · ALG-WB-04                                     | Test + Analysis               | `02-20-12-T-003_WB_H2_Evolution.json` · Comparison vs analytical/ops reference profiles                                 |
| RQ-02-20-12-H2-003          | Model reserves & boil-off at W&B level                         | [02-20-12-004](../02-20-12-004_H2_Fuel_Integration.md) · [A-003](./02-20-12-A-003_H2_Fuel_Effects.md)                                                             | Test + Review                 | `02-20-12-T-005_WB_H2_Reserves_And_Imbalance.json`                                                                      |
| RQ-02-20-12-RT-001          | Runtime CG(t) from deterministic profile                       | [02-20-12-005](../02-20-12-005_Real_Time_CG_Tracking.md) · [A-101 §11](./02-20-12-A-101_Calculation_Algorithms.md) · ALG-RTCG-01                                  | Test + Analysis               | `02-20-12-T-006_RT_CG_Scenarios.json` · Comparison vs high-fidelity W&B time history                                    |
| RQ-02-20-12-RT-002          | Sensor fusion for CG(t)                                        | [02-20-12-005](../02-20-12-005_Real_Time_CG_Tracking.md) · [02-20-12-006](../02-20-12-006_Integration_with_ATA_28.md) · ALG-RTCG-02                               | Test + Analysis               | `02-20-12-T-007_RT_CG_SensorFusion.json` · Sensor fault & noise scenarios                                               |
| RQ-02-20-12-RT-003          | Bounded NN corrections with fallback (optional)                | [02-20-12-005](../02-20-12-005_Real_Time_CG_Tracking.md) · [A-101 §13](./02-20-12-A-101_Calculation_Algorithms.md) · ALG-RTCG-03 · ATA 95 model card              | Test + Review + Analysis      | `02-20-12-T-008_RT_CG_NN_Augmentation.json` · ATA 95 evidence package                                                   |
| RQ-02-20-12-ATA28-001       | Config & runtime interface to ATA 28                           | [02-20-12-006](../02-20-12-006_Integration_with_ATA_28.md) · [A-001](./02-20-12-A-001_WB_Architecture.md)                                                        | Test + Review                 | Interface tests with simulated ATA 28 data · ICD review                                                                 |
| RQ-02-20-12-ATA28-002       | Degraded/fault behaviour on ATA 28 issues                      | [02-20-12-006](../02-20-12-006_Integration_with_ATA_28.md) · [02-20-12-005](../02-20-12-005_Real_Time_CG_Tracking.md)                                            | Test + Analysis               | Fault injection tests (`02-20-12-T-009_WB_ATA28_FaultCases.json`, placeholder)                                         |
| RQ-02-20-12-SAF-001         | Error codes for impossible/unsafe states                       | [02-20-12-002](../02-20-12-002_Load_Calculation_Engine.md) · [02-20-12-003](../02-20-12-003_CG_Envelope_Monitoring.md) · [A-101 §15](./02-20-12-A-101_Calculation_Algorithms.md)           | Test + Review                 | Negative tank mass, missing envelope, invalid MAC simulations                                                          |

*(This table is intentionally non-exhaustive; more rows to be added as the requirement set matures.)*

---

## 7. Algorithm-Level Trace (ALG ↔ Requirements)

Excerpt tying **algorithm IDs** (from [A-101](./02-20-12-A-101_Calculation_Algorithms.md))  
to requirements:

| Algorithm ID | Description                                      | Primary Requirements Covered                                                                                           |
| ------------ | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| ALG-WB-01    | Mass Item Aggregation                            | RQ-02-20-12-WB-CORE-001, -002, -RT-001 (indirect)                                                                     |
| ALG-WB-02    | CG & Moment Computation                          | RQ-02-20-12-WB-CORE-001, -CG-001, -CG-002                                                                            |
| ALG-WB-03    | Phase Transformation                             | RQ-02-20-12-WB-CORE-001, -H2-002                                                                                      |
| ALG-WB-04    | H₂ Tank / Hybrid Mass Evolution                  | RQ-02-20-12-H2-001, -H2-002, -H2-003                                                                                  |
| ALG-WB-05    | Envelope & Limit Check                           | RQ-02-20-12-CG-001, -CG-002, -CG-003                                                                                  |
| ALG-WB-06    | Scenario & What-If Evaluation                    | RQ-02-20-12-WB-CORE-002                                                                                                |
| ALG-RTCG-01  | Deterministic Runtime CG Propagation             | RQ-02-20-12-RT-001                                                                                                     |
| ALG-RTCG-02  | Sensor-Based CG Refinement                       | RQ-02-20-12-RT-002, -ATA28-002                                                                                         |
| ALG-RTCG-03  | NN-Assisted CG Corrections (bounded, optional)   | RQ-02-20-12-RT-003, plus ATA 95-specific requirements (outside this subsystem)                                        |

This mapping ensures:

- **Each requirement** is supported by at least one **explicit algorithm**; and  
- Each algorithm can be traced back to at least one **justifying requirement**.

---

## 8. Verification Coverage Structure (Skeleton)

`02-20-12-007_WB_V_and_V.md` will organise V&V around:

- **Unit tests** per algorithm (e.g. ALG-WB-01/02)  
- **Integration tests** per functional chain (WBC ↔ EFB, WBC ↔ Perf Computer, WBC ↔ ATA 28)  
- **Scenario tests** per requirement group (Core / CG / H₂ / RT / ATA 28 / SAF)  
- **Analysis & reviews** for numerical stability and envelope geometry

Example mapping (to be refined):

| Verification Artefact                              | Scope                                    | Req IDs (primary)                                 |
| -------------------------------------------------- | ---------------------------------------- | ------------------------------------------------- |
| `02-20-12-T-001_WB_Scenarios_Ramp_TOW_LW.json`     | Core W&B phases                          | RQ-02-20-12-WB-CORE-001/002                       |
| `02-20-12-T-002_WB_CG_Envelopes.json`              | Envelope in/near/out                     | RQ-02-20-12-CG-001/002/003                        |
| `02-20-12-T-003_WB_H2_Evolution.json`             | H₂ evolution & CG drift                  | RQ-02-20-12-H2-001/002/003                        |
| `02-20-12-T-005_WB_H2_Reserves_And_Imbalance.json`| Reserves, imbalance, boil-off            | RQ-02-20-12-H2-003, -SAF-001                      |
| `02-20-12-T-006_RT_CG_Scenarios.json`             | Deterministic CG(t) vs reference         | RQ-02-20-12-RT-001                                |
| `02-20-12-T-007_RT_CG_SensorFusion.json`          | Sensor fusion, fault behaviour           | RQ-02-20-12-RT-002, -ATA28-002                    |
| `02-20-12-T-008_RT_CG_NN_Augmentation.json`       | NN corrections & bounds                  | RQ-02-20-12-RT-003                                |

---

## 9. Certification & Safety Notes

- WBC outputs are **safety significant** (mass/CG, envelope checks, real-time CG).  
- DAL is expected to be **B or C** (subject to system safety assessment and  
  certification authority agreement).  
- This RTM should be aligned with:

  - **System-level requirements** under ATA 02 / ATA 28 / ATA 31 / ATA 95  
  - The overall **aircraft safety assessment** and **AFM/WBM** source data

For DO-178C alignment, the RTM:

- Supports **High-Level Requirements (HLR) ↔ Software Requirements ↔ Design**  
- Is complemented by separate **source code ↔ object code ↔ test evidence** trace,  
  which will reference the same **RQ** and **ALG** IDs defined here.

---

## 10. Maintenance & Change Control

- Any change to a **requirement** (`RQ-02-20-12-*`) must be reflected here by:
  - Updating the affected row(s) or adding new rows.  
  - Updating **Design / Algorithm References** and **Verification Artefacts** as needed.  

- Any new algorithm introduced in [A-101](./02-20-12-A-101_Calculation_Algorithms.md) must be:
  - Linked to at least one requirement.  
  - Added to §7 (Algorithm-Level Trace).

- This file should be referenced by the **subsystem-level change process**  
  (e.g. CCB records) to ensure **traceability remains consistent**.

---

## 11. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia  
> **Subsystem:** 02-20-12 Weight & Balance Computer  
> **Asset:** Requirements Traceability Matrix  
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework  

| Version | Date       | Author / Team                         | Notes                                                    |
| ------- | ---------- | ------------------------------------- | -------------------------------------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Performance WG | Initial RTM skeleton for 02-20-12 WBC (excerpted set)   |
```
