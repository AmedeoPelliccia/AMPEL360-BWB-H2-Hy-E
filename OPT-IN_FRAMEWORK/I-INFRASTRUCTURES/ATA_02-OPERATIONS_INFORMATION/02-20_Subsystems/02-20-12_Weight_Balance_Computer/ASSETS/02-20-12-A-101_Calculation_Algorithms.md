# 02-20-12-A-101 — Calculation Algorithms

**Asset ID:** 02-20-12-A-101  
**Title:** W&B Calculation Algorithms (Deterministic Core)  
**Subsystem:** [02-20-12_Weight_Balance_Computer](../02-20-12_Weight_Balance_Computer/)  
**Type:** Algorithm Catalogue & Pseudocode  
**Formats:** Markdown · (optional) Language-Specific Specs  
**Status:** DRAFT / PLACEHOLDER  

---

## 1. Purpose

This asset defines the **canonical algorithm set** for the  
**02-20-12 Weight & Balance Computer (WBC)** deterministic core.

It provides:

- A **catalogue of algorithm IDs** (`ALG-WB-*`, `ALG-RTCG-*`)  
- **Inputs / outputs / invariants** for each algorithm  
- **Language-agnostic pseudocode** for implementation teams  
- A basis for **traceability** to requirements, code and tests

It is the **reference for how WBC actually computes mass & CG**, independent of  
any NN / AI assistance (which is layered on top and documented elsewhere).

---

## 2. Scope

### 2.1 Included

This document covers algorithms for:

- **Static W&B computation** at phase level:
  - Mass item aggregation
  - CG / moment computation
  - Phase transformation (ramp → taxi → T/O → in-flight → landing)
- **H₂ integration at W&B abstraction level**
- **Envelope evaluation** (within / close / out)
- **Scenario / what-if handling**
- **Real-time CG propagation** & sensor fusion (conceptual)

### 2.2 Excluded

Not covered here:

- Detailed **H₂ thermodynamics** or fuel system control (ATA 28).  
- Detailed **hybrid energy dispatch** (ATA 10/21/36, 02-20-13).  
- NN / AI algorithm internals (ATA 95).  
- UI-level logic (EFB rendering, cockpit alert priorities).  

---

## 3. Relationship to Other Documents

This asset underpins:

- [02-20-12-001_WB_System_Overview.md](../02-20-12-001_WB_System_Overview.md)  
- [02-20-12-002_Load_Calculation_Engine.md](../02-20-12-002_Load_Calculation_Engine.md)  
- [02-20-12-003_CG_Envelope_Monitoring.md](../02-20-12-003_CG_Envelope_Monitoring.md)  
- [02-20-12-004_H2_Fuel_Integration.md](../02-20-12-004_H2_Fuel_Integration.md)  
- [02-20-12-005_Real_Time_CG_Tracking.md](../02-20-12-005_Real_Time_CG_Tracking.md)  
- [02-20-12-006_Integration_with_ATA_28.md](../02-20-12-006_Integration_with_ATA_28.md)  

and feeds into:

- `02-20-12-007_WB_V_and_V.md` *(planned)* for test case derivation.  
- Performance & hybrid integration in 02-20-13 (especially `02-20-13-006`).

---

## 4. Algorithm Catalogue (Overview)

| ID            | Name                                       | Primary Doc                        | Purpose                                                |
| ------------- | ------------------------------------------ | ---------------------------------- | ------------------------------------------------------ |
| ALG-WB-01     | Mass Item Aggregation                      | 02-20-12-002                       | Sum mass items per phase                               |
| ALG-WB-02     | CG & Moment Computation                    | 02-20-12-002                       | Compute CG in meters and %MAC                          |
| ALG-WB-03     | Phase Transformation                       | 02-20-12-002 / 004                 | Transform Ramp → Taxi → T/O → CRZ → APP → LDG          |
| ALG-WB-04     | H₂ Tank / Hybrid Mass Evolution            | 02-20-12-004                       | Update H₂ mass per tank / group                        |
| ALG-WB-05     | Envelope & Limit Check                     | 02-20-12-003 / A-002               | Compare mass/CG to BWB envelopes & limits             |
| ALG-WB-06     | Scenario & What-If Evaluation              | 02-20-12-002 / 001                 | Run same chain across multiple load scenarios          |
| ALG-RTCG-01   | Deterministic Runtime CG Propagation       | 02-20-12-005                       | CG(t) using mission profile only                       |
| ALG-RTCG-02   | Sensor-Based CG Refinement                 | 02-20-12-005                       | Fuse deterministic path with ATA 28 sensors            |
| ALG-RTCG-03   | NN-Assisted CG Corrections (Optional)      | 02-20-12-005 / ATA 95              | Apply bounded ΔCG from NN estimators                   |

Sections below define each algorithm in more detail.

---

## 5. ALG-WB-01 — Mass Item Aggregation

### 5.1 Purpose

Aggregate all **mass items** applicable to a given **W&B phase** into:

- Total mass
- Total longitudinal (and optional lateral/vertical) moments

### 5.2 Inputs

- `phase P` (e.g. `RAMP`, `TAXI`, `TOW`, `CRZ`, `APP`, `LDG`)  
- Set of mass items `Items`:

```text
MassItem {
  item_id: string
  category: enum    # BEM, PAX, BAG, CARGO, H2, FUEL, CO2BATT, EQUIP, ...
  mass_kg: float
  arm_m: float      # longitudinal
  lat_arm_m: float  # optional
  vert_arm_m: float # optional
  phase_applicability: set{ ... }
  station_id: string
}
````

### 5.3 Outputs

* `M_total_kg` — total mass at phase P
* `M_moment_mkg` — total longitudinal moment
* Optional:

  * `M_moment_lat_mkg`, `M_moment_vert_mkg`

### 5.4 Invariants

* Ignore any items where `mass_kg < 0` (invalid) or `phase_applicability` does not include `P`.
* If `Items_P` (set of applicable items) is empty → **error flag** (`NO_MASS_ITEMS_FOR_PHASE`).

### 5.5 Pseudocode

```text
function ALG_WB_01_aggregate_mass_items(Items, phase P):
    M_total_kg       := 0.0
    M_moment_mkg     := 0.0
    M_moment_lat_mkg := 0.0
    M_moment_vert_mkg:= 0.0

    for each item in Items:
        if P not in item.phase_applicability:
            continue
        if item.mass_kg <= 0:
            continue  # or log anomaly

        M_total_kg   += item.mass_kg
        M_moment_mkg += item.mass_kg * item.arm_m

        if item.lat_arm_m is defined:
            M_moment_lat_mkg  += item.mass_kg * item.lat_arm_m
        if item.vert_arm_m is defined:
            M_moment_vert_mkg += item.mass_kg * item.vert_arm_m

    if M_total_kg <= 0:
        raise / flag NO_MASS_ITEMS_FOR_PHASE

    return (M_total_kg, M_moment_mkg, M_moment_lat_mkg, M_moment_vert_mkg)
```

---

## 6. ALG-WB-02 — CG & Moment Computation

### 6.1 Purpose

Convert total mass and moment into **CG in meters** and **CG as %MAC**, using
aircraft configuration data.

### 6.2 Inputs

* Output of `ALG-WB-01`: `M_total_kg`, `M_moment_mkg`
* Aircraft configuration:

```text
MAC {
  x_LE_MAC_m: float   # position of MAC leading edge wrt datum
  MAC_length_m: float
}
```

### 6.3 Outputs

* `x_CG_m` — CG in meters from aircraft datum
* `CG_percent_MAC` — CG as percentage of MAC

### 6.4 Invariants

* `M_total_kg > 0`
* `MAC_length_m > 0`

### 6.5 Pseudocode

```text
function ALG_WB_02_compute_cg(M_total_kg, M_moment_mkg, MAC):
    x_CG_m := M_moment_mkg / M_total_kg

    CG_percent_MAC :=
        ( (x_CG_m - MAC.x_LE_MAC_m) / MAC.MAC_length_m ) * 100.0

    return (x_CG_m, CG_percent_MAC)
```

Optional lateral/vertical CGs can be computed identically if needed.

---

## 7. ALG-WB-03 — Phase Transformation

### 7.1 Purpose

Apply **known mass changes** between phases, especially **H₂/fuel burns**, to derive
mass items for downstream phases (Taxi, TOW, CRZ, APP, LDG).

### 7.2 Inputs

* Initial mass items set `Items_RAMP`
* Taxi burn `Δm_taxi` per tank / group
* Mission profile (coarse) — e.g. segment-level H₂/fuel usage
* Rules for which tanks / groups contribute to which burns

### 7.3 Outputs

* Mass item sets for phases:

  * `Items_TAXI`, `Items_TOW`, `Items_CRZ_k`, `Items_APP`, `Items_LDG`

### 7.4 Pseudocode (Simplified)

```text
function ALG_WB_03_phase_transform(Items_RAMP, TaxiBurn, MissionProfile):
    Items_TAXI := copy(Items_RAMP)
    apply_burn(Items_TAXI, TaxiBurn)

    Items_TOW := copy(Items_TAXI)
    # if any additional pre-T/O burn, apply here

    Items_CRZ := apply_mission_burns(Items_TOW, MissionProfile.cruise_segments)
    Items_APP := apply_mission_burns(Items_CRZ, MissionProfile.descent_segments)
    Items_LDG := apply_mission_burns(Items_APP, MissionProfile.approach_segments)

    return (Items_TAXI, Items_TOW, Items_CRZ, Items_APP, Items_LDG)
```

`apply_burn` must respect tank capacities and never create negative masses; any
overflow or inconsistency must be **flagged**.

---

## 8. ALG-WB-04 — H₂ Tank / Hybrid Mass Evolution

### 8.1 Purpose

Compute **H₂ mass per tank / group** over phases or segments, using mission profile
and ATA 28 configuration/runtime data.

### 8.2 Inputs

* `H2TankConfig[]` (from ATA 28)
* `H2RuntimeState` (initial measured masses)
* `H2MissionProfile` (segment-based ΔH₂)

### 8.3 Outputs

* For each phase / segment:

  * Updated `mass_kg` per `H2TankItem`

### 8.4 Pseudocode (Phase-Level Approximation)

```text
function ALG_WB_04_h2_evolution(H2_state0, H2MissionProfile):
    H2_state := copy(H2_state0)

    for each segment in H2MissionProfile.segments in time order:
        Δm := segment.delta_h2_kg   # positive consumption

        # Apply according to strategy: e.g., center-first, balanced, etc.
        distribute_burn_over_tanks(H2_state, Δm, strategy=segment.strategy)

        ensure_no_tank_negative_mass(H2_state)

    return H2_state
```

Detailed segment outputs can be **sampled** at phase boundaries (TOW, CRZ, LDG)
to drive `ALG-WB-03`.

---

## 9. ALG-WB-05 — Envelope & Limit Check

### 9.1 Purpose

Given `(mass_kg, CG_%MAC)` for a phase and an applicable **BWB CG envelope**,
determine:

* Whether point is **inside** the envelope polygon
* **Margins** vs forward/aft CG and mass limits
* **Status**: `WITHIN_NORMAL`, `CLOSE_TO_LIMIT`, `OUT_OF_LIMIT`

### 9.2 Inputs

* `mass_kg`, `CG_percent_MAC`
* `EnvelopeDefinition` (from `02-20-12-A-002_CG_Envelope_BWB.md`)
* Thresholds for **“close to limit”**

### 9.3 Outputs

* `inside: bool`
* `margin_mass_top`, `margin_mass_bottom`
* `margin_cg_forward`, `margin_cg_aft`
* `status: enum`

### 9.4 Pseudocode (Skeleton)

```text
function ALG_WB_05_envelope_check(mass_kg, CG_percent_MAC, Env, thresholds):
    point := (mass_kg, CG_percent_MAC)

    inside := point_in_polygon(point, Env.polygon_points)

    (margin_mass_top, margin_mass_bottom) := compute_mass_margins(point, Env)
    (margin_cg_forward, margin_cg_aft)   := compute_cg_margins(point, Env)

    if not inside:
        status := OUT_OF_LIMIT
    else:
        min_mass_margin := min_positive(margin_mass_top, margin_mass_bottom)
        min_cg_margin   := min_positive(margin_cg_forward, margin_cg_aft)

        if min_mass_margin <= thresholds.mass_normal_kg
           or min_cg_margin <= thresholds.cg_normal_percent_mac:
            status := CLOSE_TO_LIMIT
        else:
            status := WITHIN_NORMAL

    return (inside,
            margin_mass_top, margin_mass_bottom,
            margin_cg_forward, margin_cg_aft,
            status)
```

`point_in_polygon` and margin functions must be **numerically stable** and
tolerant to small floating-point noise.

---

## 10. ALG-WB-06 — Scenario & What-If Evaluation

### 10.1 Purpose

Run the full static W&B chain (`ALG-WB-01..05`) across **multiple loading scenarios**
and collate results.

### 10.2 Inputs

* Scenario set:

```text
Scenario {
  scenario_id: string
  description: string
  Items_RAMP: [MassItem]
  MissionProfile: H2MissionProfile
}
```

* Envelope definitions, thresholds, MAC config, etc.

### 10.3 Outputs

For each `scenario_id` and each phase `P`:

* `mass_kg`, `CG_%MAC`
* Envelope status & margins
* Errors / warnings

### 10.4 Pseudocode

```text
function ALG_WB_06_run_scenarios(Scenarios, EnvSet, MAC, thresholds):
    results := []

    for each S in Scenarios:
        # Phase transforms, including H₂ evolution
        (Items_TAXI, Items_TOW, Items_CRZ, Items_APP, Items_LDG) :=
            ALG_WB_03_phase_transform(S.Items_RAMP,
                                      TaxiBurn_from_S(S),
                                      S.MissionProfile)

        for each phase P in [RAMP, TAXI, TOW, CRZ, APP, LDG]:
            Items_P := select_items_for_phase(P, ...)

            (M_total, M_mom, _, _) :=
                ALG_WB_01_aggregate_mass_items(Items_P, P)

            (x_CG_m, CG_percent_MAC) :=
                ALG_WB_02_compute_cg(M_total, M_mom, MAC)

            Env := select_envelope(EnvSet, S.variant_id, P, config=S.config)

            (inside, m_top, m_bot, cg_f, cg_a, status) :=
                ALG_WB_05_envelope_check(M_total, CG_percent_MAC, Env, thresholds)

            store_result(results, S.scenario_id, P,
                         M_total, CG_percent_MAC, status,
                         m_top, m_bot, cg_f, cg_a)

    return results
```

---

## 11. ALG-RTCG-01 — Deterministic Runtime CG Propagation

### 11.1 Purpose

From a **known initial W&B state** at TOW or ramp, propagate **CG over time** using
segment-based H₂/fuel usage and phase transformations.

### 11.2 Inputs

* Initial `RuntimeCGState₀` (from LCE at TOW)
* `H2MissionProfile` (and fuel profile if applicable)

### 11.3 Outputs

* Discrete time series: `RuntimeCGState[t_k]`

### 11.4 Pseudocode (Simplified)

```text
function ALG_RTCG_01_propagate_deterministic(CG0, Items0, MissionProfile, MAC):
    CG_state := []
    Items    := copy(Items0)

    time := MissionProfile.start_time

    append(CG_state, (time, compute_cg_from_items(Items, MAC)))

    for each segment in MissionProfile.segments:
        apply_burn(Items, segment.delta_h2_kg, strategy=segment.strategy)
        time := segment.end_time

        (M_total, M_mom, _, _) := ALG_WB_01_aggregate_mass_items(Items, phase_from_time(time))
        (_, CG_percent) := ALG_WB_02_compute_cg(M_total, M_mom, MAC)

        append(CG_state, (time, CG_percent))

    return CG_state
```

No sensors, no NN — purely **model-driven**.

---

## 12. ALG-RTCG-02 — Sensor-Based CG Refinement

### 12.1 Purpose

Refine deterministic `CG(t)` using **ATA 28 sensor data** and, optionally,
weight-on-wheels / other measurements.

### 12.2 Inputs

* Deterministic `CG_state_model[t_k]` from `ALG-RTCG-01`
* Time-aligned `H2RuntimeState[t_k]` and other sensor streams

### 12.3 Outputs

* `CG_state_fused[t_k]` with **quality indicators**

### 12.4 Pseudocode (Sketch)

```text
function ALG_RTCG_02_fuse_sensors(CG_state_model, H2_sensors, MAC):
    CG_state_fused := []

    for each time sample t_k:
        model_CG := CG_state_model[t_k]

        sensors := H2_sensors[t_k]
        if sensors are valid:
            Items_from_sensors := reconstruct_items_from_sensors(sensors)
            (M_total, M_mom, _, _) := ALG_WB_01_aggregate_mass_items(Items_from_sensors,
                                                                     phase_from_time(t_k))
            (_, sensor_CG_percent) :=
                ALG_WB_02_compute_cg(M_total, M_mom, MAC)

            fused_CG := weighted_average(model_CG, sensor_CG_percent,
                                         weights=quality_weights(sensors))
            quality  := HIGH
        else:
            fused_CG := model_CG
            quality  := LOW

        append(CG_state_fused, (t_k, fused_CG, quality))

    return CG_state_fused
```

Exact fusion logic (e.g., Kalman filter) can be refined later; this document fixes
only the **conceptual structure**.

---

## 13. ALG-RTCG-03 — NN-Assisted CG Corrections (Optional)

### 13.1 Purpose

Apply **bounded corrections** `ΔCG` from an NN estimator (ATA 95) on top of the
deterministic + sensor-fused CG, while preserving **guardrails** and **fallback**.

### 13.2 Inputs

* `CG_state_fused[t_k]` from `ALG-RTCG-02`
* NN estimator outputs `ΔCG_nn[t_k]` + confidence/uncertainty

### 13.3 Outputs

* `CG_state_final[t_k]` with flags `source_quality` & NN usage indicators

### 13.4 Pseudocode (High-Level)

```text
function ALG_RTCG_03_apply_nn_corrections(CG_state_fused, NN_outputs, bounds):
    CG_state_final := []

    for each time sample t_k:
        (cg_fused, quality) := CG_state_fused[t_k]
        nn_output           := NN_outputs[t_k]

        if nn_output.valid and quality != LOW:
            ΔCG := clamp(nn_output.delta_cg_percent,
                         -bounds.max_delta_percent,
                         +bounds.max_delta_percent)

            if nn_output.uncertainty <= bounds.max_uncertainty:
                cg_final := cg_fused + ΔCG
                source_quality := "DET+SENSORS+NN"
            else:
                cg_final := cg_fused
                source_quality := "DET+SENSORS"  # ignore NN
        else:
            cg_final := cg_fused
            source_quality := "DET+SENSORS"

        append(CG_state_final, (t_k, cg_final, source_quality))

    return CG_state_final
```

NN configuration, training and monitoring are handled in **ATA 95 model cards**.

---

## 14. Numerical Conventions & Units

* **Mass:** kg (SI)

* **Arm / distances:** meters (m)

* **Moments:** kg·m

* **CG:**

  * `x_CG_m` (m)
  * `CG_percent_MAC` (%)

* **Tolerance** examples (to refine):

  * **Mass equality checks:** ±0.5 kg or variant-specific.
  * **CG equality checks:** ±0.01 %MAC.
  * **Polygon inclusion tolerance:** small ε margin for points exactly on edges.

---

## 15. Error Handling & Guardrails

* Any impossible condition (negative tank mass, zero total mass, MAC_length ≤ 0)
  must produce a **diagnostic flag** and not silently continue.
* For operational use, WBC should provide:

  * A **machine-readable error code**
  * A **human-readable summary** for EFB / maintenance displays

Example codes:

| Code                      | Description                                 |
| ------------------------- | ------------------------------------------- |
| `NO_MASS_ITEMS_FOR_PHASE` | No applicable items in phase                |
| `NEGATIVE_TANK_MASS`      | H₂/fuel tank mass < 0 after evolution       |
| `INVALID_MAC_DEFINITION`  | MAC config invalid                          |
| `ENVELOPE_DATA_MISSING`   | No CG envelope found for requested phase    |
| `SENSOR_DATA_DEGRADED`    | ATA 28 sensor inputs flagged SUSPECT / FAIL |

---

## 16. V&V Hooks

`02-20-12-007_WB_V_and_V.md` (planned) should:

* Map each algorithm ID to **test cases** and **test data files**, e.g.:

  * `ALG-WB-01/02` → `TEST_DATA/02-20-12-T-001_WB_Scenarios_Ramp_TOW_LW.json`
  * `ALG-WB-05` → `TEST_DATA/02-20-12-T-002_WB_CG_Envelopes.json`
  * `ALG-WB-04` → `TEST_DATA/02-20-12-T-003_WB_H2_Evolution.json`
  * `ALG-RTCG-01/02/03` → `TEST_DATA/02-20-12-T-006/..._RT_CG_*.json`

* Ensure **traceability**:

  * Requirement → Algorithm ID → Code module → Test case(s).

---

## 17. Dependencies & Cross-References

### Internal (02-20-12)

* [../02-20-12-001_WB_System_Overview.md](../02-20-12-001_WB_System_Overview.md)
* [../02-20-12-002_Load_Calculation_Engine.md](../02-20-12-002_Load_Calculation_Engine.md)
* [../02-20-12-003_CG_Envelope_Monitoring.md](../02-20-12-003_CG_Envelope_Monitoring.md)
* [../02-20-12-004_H2_Fuel_Integration.md](../02-20-12-004_H2_Fuel_Integration.md)
* [../02-20-12-005_Real_Time_CG_Tracking.md](../02-20-12-005_Real_Time_CG_Tracking.md)
* [../02-20-12-006_Integration_with_ATA_28.md](../02-20-12-006_Integration_with_ATA_28.md)
* [./02-20-12-A-002_CG_Envelope_BWB.md](./02-20-12-A-002_CG_Envelope_BWB.md)
* [./02-20-12-A-003_H2_Fuel_Effects.md](./02-20-12-A-003_H2_Fuel_Effects.md)

### Other Subsystems / ATA

* 02-20-11 — EFB (input/output flows).
* 02-20-13 — Performance Computer, especially `02-20-13-006_BWB_Specific_Calculations.md`.
* ATA 28 — H₂ Fuel System (TankConfig & RuntimeState).
* ATA 31 — Recording (logging mass/CG, envelope status, runtime CG).
* ATA 95 — NN lifecycle & model cards (for `ALG-RTCG-03`).

---

## 18. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-12 Weight & Balance Computer
> **Asset:** W&B Calculation Algorithms (Deterministic Core)
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                         | Notes                                       |
| ------- | ---------- | ------------------------------------- | ------------------------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Performance WG | Initial definition of ALG-WB / ALG-RTCG set |

```
```
