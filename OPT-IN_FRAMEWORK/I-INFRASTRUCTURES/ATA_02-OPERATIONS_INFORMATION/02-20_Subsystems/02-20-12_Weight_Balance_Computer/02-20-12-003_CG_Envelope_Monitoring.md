````markdown
# 02-20-12-003 — CG Envelope Monitoring

**Document ID:** 02-20-12-003_CG_Envelope_Monitoring  
**Subsystem ID:** 02-20-12 — Weight & Balance Computer (WBC)  
**Group:** [02-20_Subsystems](../README.md)  
**Parent ATA:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Status:** DRAFT / PLACEHOLDER  
**Owner:** Digital Operations & Aircraft Performance Domain  

---

## 1. Purpose

This document defines the **CG Envelope Monitoring** concept and logic for the  
**02-20-12 Weight & Balance Computer (WBC)**.

The CG Envelope Monitoring function:

- Ensures that **computed mass & CG states** remain within **approved envelopes**
  at **all relevant phases** (ramp, taxi, takeoff, in-flight, landing).
- Provides **margins and qualitative statuses** (e.g. *WITHIN*, *CLOSE*, *OUT*).
- Supports **real-time feedback** to:
  - [02-20-11_Electronic_Flight_Bag](../02-20-11_Electronic_Flight_Bag/)
  - [02-20-13_Performance_Computer](../02-20-13_Performance_Computer/)
  - CAOS / analytics and recording (ATA 31)
- Establishes a basis for **monitoring rules** (alerts, trend analysis, fleet KPIs).

It builds on:

- [02-20-12-001_WB_System_Overview.md](./02-20-12-001_WB_System_Overview.md)  
- [02-20-12-002_Load_Calculation_Engine.md](./02-20-12-002_Load_Calculation_Engine.md)

---

## 2. Scope

### 2.1 Included

This document covers:

- Definition of **CG envelopes** used by the WBC:
  - Ground envelopes (ramp, taxi, takeoff, landing).
  - In-flight envelopes (cruise, maneuver).
- **Computation of CG margins** and status flags for each relevant phase.
- **Monitoring logic** at:
  - **Per-flight level** (EFB, performance calculations).
  - **Fleet-level aggregation** (CAOS / analytics).
- **Alerting policies** and **recording requirements** for CG-related events.
- Interfaces toward:
  - EFB (crew-facing W&B views and warnings).
  - Performance Computer (for performance feasibility).
  - ATA 31 / CAOS for post-flight analysis.

### 2.2 Excluded

Not covered here:

- Detailed AFM / certification **source envelopes** (polygons, analytical forms)  
  → maintained in configuration / AFM data packages.  
- Detailed **control law / stability** analyses (ATA 27, ATA 95).  
- Cabin / seat map design (ATA 25) and payload planning procedures (Ops manuals).  
- NN-specific monitoring for any **WBC-related NNs** (covered under ATA 95 / WBC NN docs),
  although this document may reference such mechanisms conceptually.

---

## 3. Definitions & Concepts

- **CG Envelope**: The certified region in the (Mass, CG) space within which the
  aircraft is allowed to operate for a given **configuration and phase**.

- **Phase**: Distinct state for which the WBC computes mass & CG, e.g.:
  - `RAMP`, `TAXI`, `TOW`, `CRZ`, `APP`, `LDG`.

- **Margin**:
  - **Mass margin**: difference between computed mass and nearest mass limit
    (e.g. `MTOW − TOW`).
  - **CG margin**: distance from CG to nearest envelope boundary (in `%MAC` or m).

- **Status Levels** (example scheme):
  - `WITHIN_NORMAL`: inside envelope, margin > *threshold_normal*.
  - `CLOSE_TO_LIMIT`: inside envelope, margin ≤ *threshold_normal*.
  - `OUT_OF_LIMIT`: outside envelope (hard prohibition).

- **Envelope Source**:
  - AFM / certified **WBM data**, versioned and under configuration control.

---

## 4. CG Envelope Models

### 4.1 Envelope Types

The WBC shall support (minimum):

- **Ground envelopes**:
  - **Ramp / Taxi** envelope (taxi mass & CG).
  - **Takeoff** envelope (TOW, TOW CG).
  - **Landing** envelope (LW, landing CG).

- **In-flight envelopes**:
  - **Cruise** envelope (mass & CG ranges for typical cruise).
  - **Maneuver** envelope (where required).

Each envelope is defined as:

- A **polygon** in (`Mass_kg`, `CG_%MAC`) space, or
- A **set of piecewise-linear curves** (e.g. forward & aft CG vs mass).

### 4.2 Data Representation (Conceptual)

Configuration / AFM data (external to this document) may represent envelopes as:

```text
EnvelopeDefinition {
  envelope_id,
  phase,
  variant_id,
  polygon_points: [(mass_kg, cg_percent_mac), ...],
  validity_conditions: { flaps_setting, gear_state, config },
  source_reference: "AFM-SECTION-XX.YY",
  version_tag: "Q100_CFGA_v1"
}
````

The CG Envelope Monitoring function treats this data as **read-only** and uses it
to:

* Evaluate whether computed (`mass`, `cg`) lies **inside** the polygon.
* Compute **distance / margin** to the nearest boundary.

---

## 5. Monitoring Logic

### 5.1 Overall Flow

For each phase **P** where WBC computes mass & CG (see LCE):

1. Obtain:

   * Phase result: `mass_P`, `cg_P_%MAC`.
   * Applicable envelope definition(s) for phase **P**.

2. Evaluate:

   * Whether (`mass_P`, `cg_P`) lies **inside** envelope.
   * Mass & CG **margins** vs applicable limits (e.g. MTOW, MLW, forward/aft CG).

3. Determine **status**:

   * `WITHIN_NORMAL`
   * `CLOSE_TO_LIMIT`
   * `OUT_OF_LIMIT`

4. Provide:

   * Metrics and statuses to:

     * EFB (crew view, load workflow).
     * Performance Computer (as part of W&B input).
     * Log / CAOS for monitoring.

### 5.2 Margin Computation

For each phase **P**:

* **Mass margin**:

  * `margin_mass_top = MassLimitUpper(P) − mass_P`
  * `margin_mass_bottom = mass_P − MassLimitLower(P)` (if lower limit exists)

* **CG margin**:

  * Compute minimal signed distance from (`mass_P`, `cg_P`) to envelope boundary.
  * Represent as:

    * `margin_cg_forward` (distance to forward boundary)
    * `margin_cg_aft` (distance to aft boundary)

Normalized margins may also be used (e.g. dividing by envelope width).

### 5.3 Status Thresholds (Example)

Configuration parameters (to be tuned by safety & ops):

```text
thresholds:
  margin_mass_normal_kg: 1000
  margin_cg_normal_percent_mac: 1.0
```

Status determination example:

* If point is **outside** envelope → `OUT_OF_LIMIT`.
* Else if:

  * `min(margin_mass_top, margin_mass_bottom) ≤ margin_mass_normal_kg` OR
  * `min(margin_cg_forward, margin_cg_aft) ≤ margin_cg_normal_percent_mac`
    → `CLOSE_TO_LIMIT`.
* Else → `WITHIN_NORMAL`.

Thresholds may differ per phase (e.g. stricter at takeoff / landing).

### 5.4 Special Cases

* **Multiple envelopes** (e.g. different flaps configs):

  * Select envelope matching the **actual configuration**.
  * If no exact match, follow defined fallback (e.g. most conservative envelope).

* **Missing or invalid data**:

  * Mark status as `INVALID_DATA` and **block operational approval** until resolved.
  * Ensure EFB and Perf Computer reflect the incomplete state.

---

## 6. Integration with Other Subsystems

### 6.1 EFB (02-20-11)

WBC CG Envelope Monitoring provides to EFB:

* Per-scenario, per-phase:

  * `mass_P`, `cg_P`, `status_P`, `margins_P`.
* Visual cues:

  * **CG envelope plot** with actual point and margin shading.
  * Color-coded statuses (*green/amber/red* → exact UI defined in EFB docs).

EFB uses this to:

* Prevent crew from **finalizing loadsheet** with `OUT_OF_LIMIT` conditions.
* Highlight **CLOSE_TO_LIMIT** situations for enhanced awareness.
* Provide quick **“what-if”** feedback when crew adjusts loading.

### 6.2 Performance Computer (02-20-13)

WBC passes:

* For each performance computation request (e.g. TO / LDG):

  * `TOW_kg`, `CG_TOW_%MAC`, `LW_kg`, `CG_LDG_%MAC`, etc.
  * CG envelope status flags and margins, where applicable.

Performance Computer may:

* Use CG & mass values to:

  * Compute V-speeds, distances, and margins.
  * Apply BWB-specific aero models (see 02-20-13-006).
* Apply **operational checks**:

  * Forbid or warn about performance computations for `OUT_OF_LIMIT` states.
  * Apply additional conservatism for `CLOSE_TO_LIMIT`.

### 6.3 CAOS / Analytics (02-20-01) & ATA 31

CG envelope monitoring outputs are recorded per flight:

* **Pre-flight** W&B snapshot (final scenario).
* Optional **updates** if W&B changes during turnaround.

Stored fields may include:

* `flight_id`, `aircraft_id`, `variant_id`.
* Phase-specific: `mass_P`, `cg_P`, `status_P`, `margins_P`.
* Config references (BEM version, envelope version, WBC software version).

Analytics uses this to:

* Monitor **fleet-wide CG distributions**.
* Detect trends: frequent operations near limits, recurrent `CLOSE_TO_LIMIT`.
* Support safety reviews and operational optimization.

---

## 7. Alerting & Monitoring Policy

### 7.1 On-Aircraft / Pre-flight Alerts (EFB / WBC)

Examples:

* **Blocking conditions (hard)**:

  * Any phase required for dispatch (e.g., `TOW`, `LW`) with `OUT_OF_LIMIT`.
* **Advisory conditions (soft)**:

  * `CLOSE_TO_LIMIT` at takeoff or landing:

    * Show amber warning + recommended review (e.g. cargo shift).
* **Configuration mismatches**:

  * Envelope data not matching aircraft configuration version:

    * Block or strong warning until resolved.

### 7.2 Fleet-Level Monitoring

Example KPIs:

* Fraction of flights with **any `OUT_OF_LIMIT` attempt** (should be ~0).
* Fraction of flights with **`CLOSE_TO_LIMIT` at takeoff**.
* Distribution of **CG at TOW / LDG** vs theoretical optimum and envelope center.
* **Trend** of margins over time per fleet / base / route.

Trigger examples:

* If `CLOSE_TO_LIMIT` rate >> baseline for a given station/route:

  * Investigate planning practices, trim policies, or payload patterns.

---

## 8. Verification & Test Artefacts

CG Envelope Monitoring will be verified via:

* Synthetic cases where (`mass`, `cg`) sit:

  * Deep inside envelope (`WITHIN_NORMAL` expected).
  * Near boundaries (`CLOSE_TO_LIMIT` expected).
  * Clearly outside envelope (`OUT_OF_LIMIT` expected).

Suggested test data files (TBD, for future 02-20-12-007 V&V doc):

* `TEST_DATA/02-20-12-T-002_WB_CG_Envelopes.json`:

  * Contains envelope definitions and test points with expected statuses.
* `TEST_DATA/02-20-12-T-004_WB_CG_RuntimeCases.json`:

  * End-to-end scenarios with full W&B and expected CG monitoring outputs.

Each test case should encode:

* Variant ID, config version.
* Phase-specific `mass_P`, `cg_P`.
* Which envelope(s) are active.
* Expected:

  * Boolean “inside envelope” result.
  * Status (`WITHIN_NORMAL`, `CLOSE_TO_LIMIT`, `OUT_OF_LIMIT`).
  * Margins (within tolerance bands).

---

## 9. Dependencies & Cross-References

### Internal (02-20)

* [./02-20-12-001_WB_System_Overview.md](./02-20-12-001_WB_System_Overview.md)
* [./02-20-12-002_Load_Calculation_Engine.md](./02-20-12-002_Load_Calculation_Engine.md)
* `02-20-12-004_WB_Design.md` *(planned – algorithmic details & data structures)*
* `02-20-12-007_WB_V_and_V.md` *(planned – test cases & verification)*

Other subsystems:

* [../02-20-11_Electronic_Flight_Bag/](../02-20-11_Electronic_Flight_Bag/)
* [../02-20-13_Performance_Computer/](../02-20-13_Performance_Computer/)
* `../02-20-01_Digital_Ops_Platform/` *(if present)*

### Other ATA Chapters

* **ATA 28 — H₂ Fuel System**

  * Influences CG evolution via tank layouts and transfer patterns.

* **ATA 27 — Flight Controls**

  * Stability & control margins depend on CG; envelope definitions may originate here.

* **ATA 31 — Recording**

  * Logging of W&B parameters and CG statuses.

* **ATA 95 — Neural Networks**

  * If NN-based W&B assistance is used, CG monitoring is a key **guardrail** and
    shall be included in NN lifecycle & monitoring artefacts.

---

## 10. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-12 Weight & Balance Computer
> **Component:** CG Envelope Monitoring
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                         | Notes                               |
| ------- | ---------- | ------------------------------------- | ----------------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Performance WG | Initial CG Envelope Monitoring spec |

```
```
