````markdown
# 02-20-12-002 — Load Calculation Engine

**Document ID:** 02-20-12-002_Load_Calculation_Engine  
**Subsystem ID:** 02-20-12 — Weight & Balance Computer (WBC)  
**Group:** [02-20_Subsystems](../README.md)  
**Parent ATA:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Status:** DRAFT / PLACEHOLDER  
**Owner:** Digital Operations & Aircraft Performance Domain  

---

## 1. Purpose

This document describes the **Load Calculation Engine (LCE)** of the **02-20-12 Weight & Balance Computer**.

The LCE is the **deterministic computation core** that transforms:

- **Loading inputs** (pax, baggage, cargo, H₂, fuel, CO₂ battery, equipment)  
- **Aircraft configuration data** (stations, arms, BEM, limits, envelopes)  

into **authoritative mass & CG outputs**, including:

- Ramp / taxi / takeoff / in-flight / landing **mass & CG states**  
- Checks against **mass and CG envelopes**  
- Structured outputs for **EFB**, **Performance Computer**, and **CAOS / analytics**.

It is the **reference implementation** for W&B calculations; any AI/NN assistance is layered on top and **never replaces** this deterministic core.

For overall subsystem context, see:  
- [02-20-12-001_WB_System_Overview.md](./02-20-12-001_WB_System_Overview.md)

---

## 2. Scope

### 2.1 Included

The Load Calculation Engine covers:

- **Mass item modelling and aggregation**:
  - Representation of **all load contributors** (BEM, pax, bags, cargo, H₂, fuel, CO₂ battery, etc.)
  - Grouping by **compartment / zone / tank**  

- **Deterministic mass & CG computation**:
  - Ramp mass, taxi mass, TOW, ZFW, landing mass  
  - CG (%MAC) for all relevant phases  
  - Optional inertia / moment estimates when required downstream  

- **Hydrogen & hybrid-specific modelling (W&B level)**:
  - H₂ tank groups, mass & CG contribution per tank  
  - Simple **mission-segment evolution** of H₂ mass & CG for interface to performance and hybrid models  

- **Envelope & limit checks**:
  - Mass limits (MRW, MTOW, MLW, MZFW, etc.)  
  - CG envelopes for ground and flight phases  

- **Scenario management**:
  - Support for **multiple alternative loading scenarios** per flight (e.g. disruption / re-plan)  
  - What-if recomputation with shared core logic  

- **Interface preparation**:
  - Generation of W&B outputs for:
    - [02-20-11_Electronic_Flight_Bag](../02-20-11_Electronic_Flight_Bag/)  
    - [02-20-13_Performance_Computer](../02-20-13_Performance_Computer/)  
    - 02-20-01 Digital Ops Platform / CAOS  

### 2.2 Excluded

The LCE does **not** cover:

- Editorial **procedures / loadsheets** (Ops / S1000D responsibility)  
- Detailed fuel / H₂ **system hardware** behaviour (valve logic, tank pressurisation – ATA 28)  
- Flight-control law or automatic trim logic (ATA 27 / ATA 95)  
- NN training, evaluation and lifecycle management (ATA 95 – referenced, but separate)  

NN-assisted estimation (if used) is defined in dedicated ATA 95 / WBC NN documents and **wraps** this engine; the LCE remains valid and sufficient by itself.

---

## 3. Functional Overview

The LCE can be viewed as a three-layer pipeline:

1. **Input Normalisation Layer**  
   - Validates and normalises inputs from EFB, ground systems and configuration data.  
   - Maps raw data to **canonical mass items** and **compartments / stations**.

2. **Mass & CG Computation Layer**  
   - Aggregates mass items into:
     - Phase-specific masses (ramp, taxi, T/O, in-flight, landing)  
     - Phase-specific CG (%MAC) and optional inertia proxies.  

3. **Envelope & Interface Layer**  
   - Checks **limits and envelopes**.  
   - Generates **structured outputs** and status flags for EFB, performance and CAOS.

The main algorithm families (placeholder IDs):

- `ALG-WB-01` — Mass Item Aggregation  
- `ALG-WB-02` — CG & Moment Computation  
- `ALG-WB-03` — Phase Transformation (ramp → taxi → T/O → in-flight → landing)  
- `ALG-WB-04` — H₂ Tank / Hybrid Mass Evolution (W&B level)  
- `ALG-WB-05` — Envelope & Limit Checks  
- `ALG-WB-06` — Scenario / What-if Evaluation  

---

## 4. Data Model (Conceptual)

### 4.1 Mass Items

Every physical contributor is represented as a **mass item**:

| Field              | Type        | Description                                           |
| ------------------ | ---------- | ----------------------------------------------------- |
| `item_id`          | string     | Unique ID (e.g. `PAX-C-12`, `CARGO-HOLD1`, `H2-TK-C`) |
| `category`         | enum       | `BEM`, `PAX`, `BAG`, `CARGO`, `H2`, `FUEL`, `CO2BATT`, `EQUIP`, … |
| `mass_kg`          | float      | Mass in kg                                            |
| `arm_m`            | float      | Longitudinal arm wrt aircraft datum (m)               |
| `lat_arm_m`        | float      | Optional lateral arm                                  |
| `vert_arm_m`       | float      | Optional vertical arm                                 |
| `station_id`       | string     | Station / zone / tank reference                       |
| `phase_applicability` | set     | `RAMP`, `TAXI`, `TO`, `CRZ`, `APP`, `LDG`, etc.       |
| `source`           | enum       | `CONFIG`, `EFB_INPUT`, `SYSTEM_FEEDBACK`, …           |

The **LCE**:

- Computes moments `M = mass_kg × arm_m` (and optional lateral / vertical).  
- Sums per phase to get **total mass** and **total moment**.  

### 4.2 Aircraft Configuration & Reference Data

The engine consumes configuration data (AFM / WBM source), including:

- **BEM** and its reference CG  
- Station positions & reference arms  
- Per-compartment / tank **limits**  
- Mass and CG **envelopes** as tables or polygons in (%MAC, Mass) space  

This data is managed under configuration management; LCE assumes **read-only** access to a consistent snapshot.

---

## 5. Algorithms (High-Level)

### 5.1 Mass & CG Computation (`ALG-WB-01/02`)

For each phase **P** (e.g. `TOW`, `ZFW`, `LW`):

1. Select all mass items where `phase_applicability` includes **P**.  
2. Compute:
   - `M_total = Σ mass_kg`  
   - `M_moment = Σ mass_kg × arm_m`  
3. Compute CG:
   - `x_CG = M_moment / M_total` (in meters)  
   - Convert to `%MAC` using aircraft MAC definition:  
     `CG_%MAC = (x_CG − x_LE_MAC) / MAC_length × 100`  

Optional inertia approximations can be added if needed.

### 5.2 Phase Transformation (`ALG-WB-03`)

The same mass items can be re-used between phases with **known transformations**:

- **Ramp → Taxi**:
  - Subtract **taxi fuel / H₂** burn from appropriate tanks  
- **Taxi → Takeoff**:
  - Additional minor reductions if modelled (APU, extended taxi)  
- **Takeoff → In-Flight → Landing**:
  - Apply **mission-segment fuel / H₂** consumption model  
  - May be driven by 02-20-13 / ATA 10-xx hybrid models for finer resolution  

Transformations operate at **tank / group level**; LCE recomputes phase-specific mass & CG from the resulting mass items.

### 5.3 H₂ Tank & Hybrid Mass Evolution (`ALG-WB-04`)

At W&B level the LCE:

- Represents each **H₂ tank / group** as a mass item (or set of items).  
- Consumes **time- or energy-based consumption profiles**:
  - Simple approximation: `Δmass = f(segment, required_energy)`  
  - Detailed models may come from hybrid subsystem (e.g. ATA 10-xx / RQ-10-02).  

Outputs:

- Phase-specific **H₂ mass per tank / group**  
- Resulting **CG drift** over mission segments (used by performance & control analyses).  

### 5.4 Envelope & Limit Checks (`ALG-WB-05`)

For each computed phase:

- Compare **total mass** vs:
  - MRW, MTOW, MLW, MZFW, etc.  
- Check **CG** vs applicable envelope polygon (ground or flight).  
- For each:
  - Compute **margin**, e.g. `MTOW_margin = MTOW − TOW`.  
  - Generate boolean flags: `WITHIN_LIMITS`, `CLOSE_TO_LIMIT`, `OUT_OF_LIMIT`.  

These results are included in WBC outputs and consumed by EFB / Performance Computer.

### 5.5 Scenario & What-if Evaluation (`ALG-WB-06`)

The LCE handles **multiple scenarios** per flight:

- Each scenario is a full set of loading assumptions (**pax, cargo, tanks**).  
- Scenarios share a common configuration baseline but differ in `mass_items`.  
- The same algorithm chain is run; outputs are tagged with `scenario_id`.  

This enables:

- Rapid evaluation of **load redistribution options**.  
- What-if analysis for **disruptions, last-minute changes, or payload optimisations**.

---

## 6. Interfaces

### 6.1 Inputs

#### 6.1.1 From EFB (02-20-11)

- Flight ID / plan reference  
- Pax counts by cabin section and **optional seat-map detail**  
- Baggage / cargo weights and compartment allocation  
- Fuel / H₂ quantities / targets  
- Manual adjustments from the crew  

Format: **structured JSON** or equivalent message (defined in a future `02-20-12-003_WB_Interfaces.md`).

#### 6.1.2 From Configuration / AFM / WBM

- Aircraft variant (Q80/Q100/Q120) and configuration version  
- BEM, station data, arms, envelopes, mass limits  
- Tank and load station definitions  

#### 6.1.3 From Hybrid / Energy Systems (Optional)

- Segment-based **H₂ consumption** profiles  
- CO₂ battery mass significance (if required for W&B)  

### 6.2 Outputs

#### 6.2.1 To EFB (02-20-11)

- Per scenario:
  - Key masses: `MRW`, `TOW`, `ZFW`, `LW`, etc.  
  - CG per phase (%MAC)  
  - Envelope / limit flags & margins  
  - Summary **loadsheet data**  

#### 6.2.2 To Performance Computer (02-20-13)

- For **selected scenario**:
  - `TOW`, `LW`, `ZFW`, `RampMass`, etc.  
  - `CG_%MAC` per requested phase (e.g. takeoff, landing)  
  - Optional breakdown:
    - Payload vs energy vs structure mass  
    - H₂ distribution by tank group  

Format may be JSON structure like:

```text
WBPerfInput {
  flight_id,
  scenario_id,
  phase,
  tow_kg,
  lw_kg,
  zfw_kg,
  cg_percent_mac,
  h2_distribution[],
  flags[]
}
````

(Exact schema to be defined in `02-20-12-003_WB_Interfaces.md`.)

#### 6.2.3 To CAOS / Analytics (02-20-01)

* Final **per-flight W&B snapshot**: scenario chosen, masses, CG, envelope margins.
* Optional **time-series** if W&B is updated in-flight.

---

## 7. Determinism, Safety & NN Integration

The LCE is designed to be:

* **Deterministic**:

  * Same inputs → same outputs (within numerical tolerance).
* **Auditable**:

  * Easily reconstructed from logged inputs and configuration snapshot.
* **Config-controlled**:

  * No untracked dependency on external ML models.

If **NN assistance** is introduced (e.g., to estimate payload distributions):

* All NN usage is **outside** the LCE and must comply with ATA 95 requirements.

* NN may propose **candidate mass items** or **corrections**, but:

  * LCE **re-evaluates** W&B deterministically.
  * Final safety decisions (envelope / limits) are based on **LCE outputs**.

* Guardrails:

  * NN proposals are **bounded** and subject to WBC validation.
  * Any NN-related information is logged for later analysis.

---

## 8. Verification & Test Hooks

Future test artefacts (suggested):

* `TEST_DATA/02-20-12-T-001_WB_Scenarios_Ramp_TOW_LW.json`
* `TEST_DATA/02-20-12-T-002_WB_CG_Envelopes.json`
* `TEST_DATA/02-20-12-T-003_WB_H2_Evolution.json`

Each test case should specify:

* **Input**:

  * Full set of mass items, configuration snapshot, segment definitions.
* **Expected output**:

  * Key masses, CGs, envelope flags, margin values.

These will be referenced from future `02-20-12-007_WB_V_and_V.md`.

---

## 9. Dependencies & Cross-References

### Internal (02-20)

* [./02-20-12-001_WB_System_Overview.md](./02-20-12-001_WB_System_Overview.md)
* `02-20-12-003_WB_Interfaces.md` *(planned)*
* `02-20-12-004_WB_Design.md` *(planned)*
* `02-20-12-007_WB_V_and_V.md` *(planned)*

Other subsystems:

* [../02-20-11_Electronic_Flight_Bag/](../02-20-11_Electronic_Flight_Bag/)
* [../02-20-13_Performance_Computer/](../02-20-13_Performance_Computer/)
* `../02-20-01_Digital_Ops_Platform/` *(if present)*

### Other ATA Chapters

* ATA 28 — H₂ fuel system (tanks, limits)
* ATA 31 — Recording (W&B parameters logging)
* ATA 95 — Neural Networks (if NN support is added to WBC workflows)

---

## 10. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-12 Weight & Balance Computer
> **Component:** Load Calculation Engine
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                         | Notes                                |
| ------- | ---------- | ------------------------------------- | ------------------------------------ |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Performance WG | Initial Load Calculation description |

```
```
