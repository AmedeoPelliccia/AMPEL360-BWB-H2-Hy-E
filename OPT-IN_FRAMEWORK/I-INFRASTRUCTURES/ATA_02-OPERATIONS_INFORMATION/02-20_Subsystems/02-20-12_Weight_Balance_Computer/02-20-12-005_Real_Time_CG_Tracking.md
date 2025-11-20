# 02-20-12-005 — Real-Time CG Tracking

**Document ID:** 02-20-12-005_Real_Time_CG_Tracking  
**Subsystem ID:** 02-20-12 — Weight & Balance Computer (WBC)  
**Group:** [02-20_Subsystems](../README.md)  
**Parent ATA:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Status:** DRAFT / PLACEHOLDER  
**Owner:** Digital Operations & Aircraft Performance Domain  

---

## 1. Purpose

This document defines the **Real-Time CG Tracking** function of the  
**02-20-12 Weight & Balance Computer (WBC)**.

Real-Time CG Tracking:

- Provides a **time-evolving estimate** of aircraft **mass & CG** during taxi and flight.  
- Fuses **pre-flight W&B state** with **onboard measurements** and **energy usage**.  
- Supplies **continuous CG information** to:
  - [02-20-11_Electronic_Flight_Bag](../02-20-11_Electronic_Flight_Bag/)
  - [02-20-13_Performance_Computer](../02-20-13_Performance_Computer/)
  - CAOS / analytics (02-20-01) and **ATA 31** recording.  

The goal is to:

- Track **CG evolution** (e.g. due to H₂ consumption, tank transfers, cabin movements).  
- Support **safety monitoring**, **performance optimization**, and **post-flight analysis**.  
- Provide a framework where optional **NN-based estimators** (ATA 95) can be plugged in  
  without compromising determinism and traceability.

It builds on:

- [02-20-12-001_WB_System_Overview.md](./02-20-12-001_WB_System_Overview.md)  
- [02-20-12-002_Load_Calculation_Engine.md](./02-20-12-002_Load_Calculation_Engine.md)  
- [02-20-12-003_CG_Envelope_Monitoring.md](./02-20-12-003_CG_Envelope_Monitoring.md)  
- [02-20-12-004_H2_Fuel_Integration.md](./02-20-12-004_H2_Fuel_Integration.md)  

---

## 2. Scope

### 2.1 Included

Real-Time CG Tracking covers:

- Definition of **runtime CG state** and update cycles.  
- Integration of:
  - **Initial W&B state** (ramp / TOW snapshot from WBC LCE).  
  - **H₂ / fuel usage** and other mass changes over time.  
  - **Onboard sensors / systems** relevant to CG estimation (weight-on-wheels, fuel/H₂ gauges, inertial data, etc.).  
- Algorithms for:
  - **CG state propagation** over time / segments.  
  - **Sensor & model fusion** (deterministic + optional NN estimator).  
  - **Quality / confidence metrics** and integrity flags.  
- Interfaces to:
  - EFB (visualization, warnings).  
  - Performance Computer (for dynamic performance evaluations).  
  - ATA 31 / CAOS for recording and analysis.  

### 2.2 Excluded

Not covered:

- Detailed design of **sensors** and acquisition hardware (ATA 22/31/34/42).  
- Detailed **hybrid powertrain** behavior (ATA 10 / 28 / 36).  
- Full NN lifecycle / training processes (ATA 95).  
- Editorial procedure content (Ops manuals, FCOM, QRH).

---

## 3. Concept Overview

### 3.1 Runtime CG State

Define a **Real-Time CG State** structure:

```text
RuntimeCGState {
  timestamp,
  flight_phase,           # TAXI, T/O, CLB, CRZ, DES, APP, LDG, ROLLOUT, etc.
  total_mass_kg,
  cg_percent_mac,
  h2_mass_distribution[], # per tank/group (optional detail)
  other_mass_changes[],   # cabin moves, fuel jettison, cargo release, etc. (if available)
  source_quality,         # DET_ONLY, DET+SENSORS, DET+SENSORS+NN
  quality_score,          # 0..1 or low/medium/high
  validity_flags[],       # IN_ENVELOPE, DATA_GAP, SENSOR_FAULT, etc.
  config_refs { wbc_sw_version, wb_config_id, h2_conf_id }
}
````

### 3.2 High-Level Flow

1. **Initialisation at Ramp / TOW**

   * Use LCE output (deterministic W&B) as **initial state**.
   * CG Envelope Monitoring provides initial **status & margins**.

2. **Time / Segment-Based Propagation**

   * Apply **known mass changes** over time:

     * H₂ usage (from performance / hybrid models).
     * Fuel consumption (if any conventional fuel).
     * Discrete events (payload changes, fuel jettison, system draining) where available.

3. **Sensor & Model Fusion**

   * Incorporate **onboard measurements**:

     * Tank gauges / flowmeters.
     * Weight-on-wheels load distributions (ground operations).
     * Inertial / attitude data for indirect CG indicators (if applicable).
   * Optionally integrate **NN estimator** as bounded correction.

4. **Continuous Monitoring & Logging**

   * Provide **updated CG state** at a defined rate (e.g. 1–10 Hz internally, downsampled for EFB).
   * Feed **CG Envelope Monitoring** for dynamic checks.
   * Record selected snapshots to ATA 31 / CAOS.

---

## 4. Inputs & Data Sources

### 4.1 Initial W&B Snapshot

From LCE at **final W&B approval** (before departure):

* `RampMass_kg`, `TaxiMass_kg`, `TOW_kg`, `ZFW_kg`, `LW_kg`.
* `CG_%MAC` for key phases (at least TOW / LW).
* H₂ distribution and other tank/fuel states as per
  [02-20-12-004_H2_Fuel_Integration.md](./02-20-12-004_H2_Fuel_Integration.md).

### 4.2 Time / Segment-Based Mass Changes

From performance / hybrid / ops systems:

* **H₂ usage profile** (segments or continuous rate).
* **Fuel usage profile**, if present.
* Other known mass changes (e.g. refueling during extended ground periods, cargo offload).

### 4.3 Onboard Measurements (Examples)

Depending on aircraft architecture:

* **Ground (TAXI, prior to T/O)**:

  * Weight-on-wheels **load cell data** per gear leg.
  * Sensed H₂ mass per tank (indication systems).

* **In-Flight**:

  * Tank-level H₂ / fuel quantities.
  * Flowmeter-derived usage rates.
  * Optional inertial signatures (limited, advanced use only).

The **Real-Time CG Tracking** function treats these as inputs with:

* **Timestamps** and source IDs.
* Associated **quality indicators** (valid / suspect / fail).

---

## 5. Algorithms (High-Level)

### 5.1 Deterministic Propagation

Base algorithm `ALG-RTCG-01`:

1. Start with `RuntimeCGState₀` at TOW from LCE.
2. At each update step Δt or mission segment:

   * Update **mass items** affected by:

     * H₂ / fuel consumption.
     * Discrete events (if provided).
   * Recompute:

     * `total_mass_kg`
     * `cg_percent_mac`
   * Maintain **consistency** with CG Envelope Monitoring.

This path is **fully deterministic** and **sufficient** for W&B safety arguments.

### 5.2 Sensor Fusion (Deterministic)

Algorithm `ALG-RTCG-02` enhances propagation using sensors:

* When weight-on-wheels data is available on ground:

  * Use **measured gear loads** to refine CG estimate at taxi / pre-takeoff.

* When tank gauges / flowmeters provide data:

  * Adjust **H₂ / fuel mass per tank** to align with measured values (within tolerance).
  * Use filtered estimates (e.g. simple Kalman filter) to handle noise.

Fusion logic must ensure:

* **Consistency** with configuration (no impossible mass values).
* Robustness to **sensor failures / bias** (diagnostics, fallback).

### 5.3 NN-Assisted Estimation (Optional, ATA 95)

Algorithm `ALG-RTCG-03` *(optional)*:

* An **ATA 95 NN estimator** can propose corrections to:

  * CG estimate (e.g. based on sensor patterns, aerodynamic data).
  * H₂ distribution when sensors are sparse.

Principles:

* NN never becomes the **sole source** of CG; it **corrects** the deterministic estimate.
* Corrections Δ are **bounded** and applied via a guarded fusion layer.
* OOD detection, uncertainty metrics and guardrails are mandatory.

All NN aspects must be documented in an ATA 95 model card
and a dedicated WBC NN integration doc (not this document).

---

## 6. Outputs & Interfaces

### 6.1 To EFB (02-20-11)

Real-Time CG Tracking provides:

* Current `total_mass_kg`, `cg_percent_mac`.
* Phase label (`TAXI`, `CLB`, `CRZ`, etc.).
* **Envelope status** from CG Envelope Monitoring:

  * `WITHIN_NORMAL`, `CLOSE_TO_LIMIT`, `OUT_OF_LIMIT`, `INVALID_DATA`.
* Optional:

  * Graphical **CG vs Time** curve.
  * Predicted **landing CG** based on current H₂ usage and mission plan.

EFB uses this for:

* **Crew awareness** (e.g. CG drift trends).
* Potential **performance re-evaluation** triggers (through Perf Computer).

### 6.2 To Performance Computer (02-20-13)

For dynamic performance computations or scenario analysis:

* Current **W&B state** (mass, CG, H₂ distribution) with quality flags.
* Optionally, short-horizon **CG forecasts** based on mission profile.

This enables:

* In-flight or near-real-time checks of **performance margins**
  (e.g. for diversions, alternate planning).

### 6.3 To ATA 31 / CAOS

Recording interface includes:

* Selected **Runtime CG State** snapshots:

  * At key events (brake release, liftoff, top-of-climb, mid-cruise, top-of-descent, touchdown).
  * Periodic downsampled snapshots (e.g. every X minutes).
* Associated **status & quality**:

  * Envelope status, data validity, NN usage flags (if any).
* Configuration & software version references.

CAOS can then:

* Analyze **fleet-wide CG evolution patterns**.
* Detect recurring **near-limit** operations or systematic biases.

---

## 7. Safety, Integrity & Fallback

### 7.1 Integrity Levels

Real-Time CG Tracking is **advisory** unless explicitly used in safety-related functions:

* **Primary safety** for W&B remains the **pre-flight WBC determination** and
  performance calculations built upon it.
* Real-time CG may:

  * Provide **early warning** of unexpected deviations.
  * Support future safety functions (subject to separate certification).

### 7.2 Fallback Behavior

If **sensors fail** or data becomes invalid:

* Fall back to **deterministic propagation** based solely on WBC + mission profile.
* Mark `source_quality` and flags accordingly (e.g. `DET_ONLY`, `SENSOR_FAULT`).
* Inform EFB and Perf Computer that **real-time sensor support** is unavailable.

If **NN assistance** is configured and fails or goes OOD:

* Ignore NN corrections and use deterministic + sensor-fused estimate.
* Log event for ATA 95 lifecycle monitoring.

### 7.3 Alerting (Conceptual)

Example triggers (to be refined):

* **Hard**:

  * Real-time CG estimate goes **outside envelope** → `OUT_OF_LIMIT` alert.

* **Soft**:

  * CG approaching envelope boundary faster than forecast.
  * Significant deviation between deterministic and sensor-based estimates.

Integration of alerting into EFB / cockpit systems is defined in EFB / avionics docs.

---

## 8. Verification & Test Artefacts

Real-Time CG Tracking will be verified via:

* **Simulation-based test cases**:

  * Controlled H₂ / fuel consumption profiles.
  * Known CG evolution vs high-fidelity reference model.

* **Hybrid tests**:

  * Injected sensor data (with noise, bias, failures).
  * Compare estimator output with reference truth.

Suggested future test data files:

* `TEST_DATA/02-20-12-T-006_RT_CG_Scenarios.json`
* `TEST_DATA/02-20-12-T-007_RT_CG_SensorFusion.json`
* `TEST_DATA/02-20-12-T-008_RT_CG_NN_Augmentation.json` (if NN path used)

Each test case should specify:

* Initial W&B snapshot (mass, CG, configuration).
* Mission / energy usage profile.
* Sensor input streams (nominal / faulty).
* Expected:

  * CG evolution within tolerances.
  * Correct status / flags for integrity and envelope monitoring.

---

## 9. Dependencies & Cross-References

### Internal (02-20)

* [./02-20-12-001_WB_System_Overview.md](./02-20-12-001_WB_System_Overview.md)
* [./02-20-12-002_Load_Calculation_Engine.md](./02-20-12-002_Load_Calculation_Engine.md)
* [./02-20-12-003_CG_Envelope_Monitoring.md](./02-20-12-003_CG_Envelope_Monitoring.md)
* [./02-20-12-004_H2_Fuel_Integration.md](./02-20-12-004_H2_Fuel_Integration.md)
* `02-20-12-007_WB_V_and_V.md` *(planned)*

Other subsystems:

* [../02-20-11_Electronic_Flight_Bag/](../02-20-11_Electronic_Flight_Bag/)
* [../02-20-13_Performance_Computer/](../02-20-13_Performance_Computer/)
* 02-20-01 Digital Ops Platform / CAOS

### Other ATA Chapters

* **ATA 28** — H₂ Fuel System (tank definitions & sensing).
* **ATA 31** — Recording (CG & W&B logging).
* **ATA 42** — IMA / avionics (system integration).
* **ATA 95** — Neural Networks (if NN-based CG estimators are used).

---

## 10. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-12 Weight & Balance Computer
> **Component:** Real-Time CG Tracking
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                         | Notes                           |
| ------- | ---------- | ------------------------------------- | ------------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Performance WG | Initial Real-Time CG spec draft |

```
```
