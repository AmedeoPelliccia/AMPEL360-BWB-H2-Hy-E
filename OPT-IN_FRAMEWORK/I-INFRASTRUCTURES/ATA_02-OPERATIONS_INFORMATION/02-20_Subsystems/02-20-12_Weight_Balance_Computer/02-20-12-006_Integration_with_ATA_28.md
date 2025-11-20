# 02-20-12-006 — Integration with ATA 28

**Document ID:** 02-20-12-006_Integration_with_ATA_28  
**Subsystem ID:** 02-20-12 — Weight & Balance Computer (WBC)  
**Group:** [02-20_Subsystems](../README.md)  
**Parent ATA:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Status:** DRAFT / PLACEHOLDER  
**Owner:** Digital Operations & Aircraft Performance Domain  

---

## 1. Purpose

This document specifies how the **02-20-12 Weight & Balance Computer (WBC)**  
integrates with **ATA 28 — H₂ Fuel System** for the AMPEL360 family.

The goals are to:

- Define **data flows and responsibilities** between WBC and ATA 28.  
- Ensure a **consistent, configuration-controlled representation** of:
  - H₂ tanks / groups  
  - H₂ quantities and limits  
  - Relevant fuel system states affecting mass & CG  
- Provide a clear interface framework for:
  - [02-20-12-004_H2_Fuel_Integration.md](./02-20-12-004_H2_Fuel_Integration.md)  
  - [02-20-12-005_Real_Time_CG_Tracking.md](./02-20-12-005_Real_Time_CG_Tracking.md)  
  - [02-20-13_Performance_Computer](../02-20-13_Performance_Computer/) and hybrid subsystems  

ATA 28 remains **authoritative** for physical H₂ system design and operation;  
WBC consumes **abstracted data and states** for weight & balance purposes.

---

## 2. Scope

### 2.1 Included

This document covers:

- **Configuration-time interface**:
  - Import of tank geometry, capacities, constraints and roles into WBC.  
- **Runtime interface**:
  - Exchange of H₂ quantities per tank / group.  
  - System states relevant to W&B (e.g. tank availability, isolation, transfer modes).  
- **Mission / planning interface**:
  - H₂ mission/segment profiles used by WBC for phase-based mass & CG calculations.  
- **Error / failure propagation**:
  - Handling of ATA 28 sensor faults and degraded modes from WBC perspective.

### 2.2 Excluded

Not covered:

- Detailed **ATA 28 fuel system design and control logic**  
  (valves, pressurisation, fault management).  
- Electrical / hybrid powertrain control (ATA 10 / 21 / 36).  
- NN-based H₂ prediction / anomaly detection (ATA 95).  
- UI design for EFB or maintenance tools.

---

## 3. Roles & Responsibilities

### 3.1 ATA 28 — Responsibilities

ATA 28 is responsible for:

- **Tank design and configuration**:
  - Physical locations, capacities, operating limits.  
- **H₂ sensing and control**:
  - Tank-level gauges, flowmeters, valve states, transfer logic.  
- **Safety and protection**:
  - Overpressure, leak detection, isolation strategies.  
- **Authoritative data sources**:
  - All **H₂ quantities** and **tank availability states** as seen by the aircraft.

### 3.2 WBC — Responsibilities

WBC is responsible for:

- Mapping ATA 28 data into **W&B mass items**, as defined in:  
  - [02-20-12-002_Load_Calculation_Engine.md](./02-20-12-002_Load_Calculation_Engine.md)  
  - [02-20-12-004_H2_Fuel_Integration.md](./02-20-12-004_H2_Fuel_Integration.md)  
- Computing **phase-specific mass & CG** using the mapped H₂ items.  
- Supporting **CG Envelope Monitoring** and **Real-Time CG Tracking**.  
- Providing **H₂-related W&B data** to:
  - EFB (02-20-11)  
  - Performance Computer (02-20-13)  
  - CAOS / analytics (02-20-01)  
  - ATA 31 recording  

WBC never overrides ATA 28 sensor values; it **consumes** them with filtering and  
integrity checks for W&B use.

---

## 4. Interface Types

### 4.1 Configuration Interface (Static Data)

This interface imports **configuration data** from ATA 28 repositories / databases  
into WBC’s configuration layer.

Example conceptual structure:

```text
H2TankConfig {
  tank_id,
  group_id,
  role,                   # MAIN, RESERVE, BUFFER, TRIM, EMERGENCY
  usable_capacity_kg,
  unusable_capacity_kg,
  arm_m, lat_arm_m, vert_arm_m,
  station_id,
  operating_limits {
    min_normal_level_kg,
    max_normal_level_kg,
    imbalance_limits,
    temperature_limits (if W&B-relevant)
  },
  variant_id,
  config_version_id,      # e.g. H2CONF_Q100_V1
  source_reference        # link to ATA 28 config artefact
}
````

This data is:

* Maintained under **ATA 28 configuration control**.
* Synced into WBC via **config baselines** (e.g. per aircraft / fleet).
* Referenced in WBC via IDs like `wbc_config_id`, `h2_conf_id`.

### 4.2 Runtime State Interface

During operation, WBC consumes **runtime state** from ATA 28, including:

* **Tank quantities**:

  * Measured H₂ mass/level per tank or group.
* **Flow / consumption**:

  * Flowmeter readings, aggregated usage rates.
* **Valve / configuration states**:

  * Tank isolation, crossfeed availability, pump status.
* **Fault indicators**:

  * Sensor fault flags, degraded modes.

Conceptual structure:

```text
H2RuntimeState {
  timestamp,
  variant_id,
  config_version_id,
  tank_states: [
    {
      tank_id,
      quantity_kg_measured,
      quantity_kg_estimated,
      sensor_status,   # OK, SUSPECT, FAIL
      valve_state,     # OPEN, CLOSED, ISOLATED, BYPASSED
      available_for_use: bool
    },
    ...
  ],
  flowmeters: [
    {
      id,
      flow_kg_per_h,
      status
    }
  ],
  system_mode,          # e.g. NORMAL, DEGRADED, EMERGENCY
  faults[]              # list of ATA 28 fault codes / statuses
}
```

Real-Time CG Tracking uses this to:

* Update **H₂ mass items** per tank.
* Assess **data quality** and choose between:

  * Deterministic propagation only.
  * Deterministic + sensor fusion (recommended path).

### 4.3 Mission / Segment Interface

WBC may also receive **mission-level H₂ usage profiles** from ATA 28 / performance / planning:

```text
H2MissionProfile {
  flight_id,
  variant_id,
  segments: [
    { id: "CLB1",  delta_h2_kg: XXX, start_time: ..., end_time: ... },
    { id: "CRZ1",  delta_h2_kg: YYY, ... },
    ...
  ],
  reserves: {
    contingency_kg,
    alternate_kg,
    final_kg,
    extra_kg
  }
}
```

WBC uses this for:

* Phase-wise **H₂ mass & CG predictions**.
* Checking **reserves and tank limits** (via 02-20-12-004).

---

## 5. Data Flow Overview

### 5.1 Pre-Flight / Turnaround

1. **Config sync**:

   * Aircraft variant & configuration established.
   * WBC loads corresponding `H2TankConfig` set.

2. **Planned H₂ load**:

   * EFB / Ops specify H₂ quantities per tank / group.
   * ATA 28 validates planned loading against system constraints.
   * WBC receives planned H₂ distribution via EFB + config interplay.

3. **Final H₂ at ramp**:

   * ATA 28 provides **measured fill levels**.
   * WBC reconciles planned vs measured values (within tolerances) and
     computes **Ramp W&B state**.

### 5.2 Taxi, Takeoff, Climb

* ATA 28 continuously updates **tank quantities** and states.
* WBC:

  * Applies **taxi H₂ usage model** and sensor data.
  * Computes **TOW** and **TOW CG** using latest states.
  * Updates Real-Time CG State and Envelope Monitoring.

### 5.3 Cruise, Descent, Landing

* ATA 28 provides ongoing **consumption and tank status**.
* WBC:

  * Propagates W&B with **segment usage + sensors**.
  * Predicts and monitors **landing mass & CG**.
  * Flags reserve issues or unexpected H₂ distribution patterns.

### 5.4 Post-Flight

* Selected states (e.g., TOW, TOC, TOD, LW) are recorded via ATA 31 / CAOS,
  including **H₂ distribution and envelope margins**.

---

## 6. Failure & Degraded Modes (From WBC Viewpoint)

### 6.1 Sensor Faults

If ATA 28 reports:

* **Tank gauge failure**:

  * WBC falls back to **model-based estimates** (mission profile) for that tank.
  * Marks H₂ data for that tank as **degraded**; Real-Time CG flags reflect lower quality.

* **Flowmeter failure**:

  * WBC relies more on tank-level or mission profile data.
  * Differences in mass balance may be logged for post-flight analysis.

### 6.2 System Mode Changes

If ATA 28 switches to **DEGRADED / EMERGENCY** modes:

* WBC must:

  * Maintain a **safe, conservative W&B estimate**.
  * **Clamp** or increase uncertainty of H₂-based corrections.
  * Inform EFB / Perf Computer about reduced confidence.

### 6.3 Integrity & Alerts

WBC shall not:

* Hide serious ATA 28 anomalies; instead it:

  * Passes through major fault indicators in **status flags**.
  * Records them for **post-flight analysis**.

Any WBC internal approximation (e.g. continued mission model after multiple sensor failures)
must be **clearly flagged** and subject to operational limitations.

---

## 7. Integration with NN / ATA 95 (Optional)

If NN models (ATA 95) are used to:

* Predict H₂ usage,
* Reconstruct H₂ distributions from partial sensors, or
* Anomaly-detect H₂ system behaviour,

then:

* **Models live in ATA 95**, not in ATA 28 or WBC.
* WBC may consume **NN-assisted H₂ estimates** as **additional inputs**, but:

  * H₂ system behaviour truth remains ATA 28.
  * NN outputs are **bounded corrections** on top of deterministic models + sensors.
* All NN usage is:

  * Logged for traceability.
  * Subject to guardrails and fallbacks (see ATA 95 & relevant hybrid docs).

Details reside in ATA 95 model cards and integration docs; here we just mark WBC–ATA 28
interface as **NN-aware but NN-agnostic**.

---

## 8. Verification & Test Artefacts

Integration with ATA 28 will be verified through:

* **Interface tests**:

  * Simulated ATA 28 configuration and runtime states.
  * WBC correctness in mapping to mass items and W&B states.

* **Scenario tests**:

  * Typical missions with **nominal H₂ loading and consumption**.
  * Extreme cases (hot/high, long taxi, diversion) verifying reserves and CG behaviour.

* **Failure injection tests**:

  * Sensor faults (gauge, flowmeter).
  * Tank isolation / transfer anomalies.
  * WBC degraded-mode behaviour.

Suggested future test files:

* `TEST_DATA/02-20-12-T-005_WB_H2_Reserves_And_Imbalance.json`
* `TEST_DATA/02-20-12-T-009_WB_ATA28_FaultCases.json`

These will be referenced from `02-20-12-007_WB_V_and_V.md` (planned).

---

## 9. Dependencies & Cross-References

### Internal (02-20)

* [./02-20-12-001_WB_System_Overview.md](./02-20-12-001_WB_System_Overview.md)
* [./02-20-12-002_Load_Calculation_Engine.md](./02-20-12-002_Load_Calculation_Engine.md)
* [./02-20-12-003_CG_Envelope_Monitoring.md](./02-20-12-003_CG_Envelope_Monitoring.md)
* [./02-20-12-004_H2_Fuel_Integration.md](./02-20-12-004_H2_Fuel_Integration.md)
* [./02-20-12-005_Real_Time_CG_Tracking.md](./02-20-12-005_Real_Time_CG_Tracking.md)
* `02-20-12-007_WB_V_and_V.md` *(planned)*

Other subsystems:

* [../02-20-11_Electronic_Flight_Bag/](../02-20-11_Electronic_Flight_Bag/)
* [../02-20-13_Performance_Computer/](../02-20-13_Performance_Computer/)
* 02-20-01 Digital Ops Platform / CAOS

### Other ATA Chapters

* **ATA 28 — H₂ Fuel System**

  * Tank design, sensing, system modes and faults.

* **ATA 31 — Recording**

  * Logging of H₂-related W&B data.

* **ATA 95 — Neural Networks**

  * Any NN-based H₂ predictors or anomaly detectors that influence WBC inputs.

---

## 10. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-12 Weight & Balance Computer
> **Component:** Integration with ATA 28
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                         | Notes                                   |
| ------- | ---------- | ------------------------------------- | --------------------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Performance WG | Initial WBC–ATA 28 integration document |

```
```
