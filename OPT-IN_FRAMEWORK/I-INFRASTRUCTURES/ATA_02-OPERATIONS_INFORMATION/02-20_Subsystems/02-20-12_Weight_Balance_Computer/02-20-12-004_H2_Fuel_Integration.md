# 02-20-12-004 — H₂ Fuel Integration

**Document ID:** 02-20-12-004_H2_Fuel_Integration  
**Subsystem ID:** 02-20-12 — Weight & Balance Computer (WBC)  
**Group:** [02-20_Subsystems](../README.md)  
**Parent ATA:** ATA_02-OPERATIONS_INFORMATION  
**Axis:** I — Infrastructures  
**Status:** DRAFT / PLACEHOLDER  
**Owner:** Digital Operations & Aircraft Performance Domain  

---

## 1. Purpose

This document defines how **liquid hydrogen (H₂) fuel** is modelled and integrated into the  
**02-20-12 Weight & Balance Computer (WBC)** for the AMPEL360 program.

The H₂ Fuel Integration layer:

- Provides a **consistent W&B representation** of all **H₂ tanks / groups**.  
- Computes **mass and CG contributions** of H₂ at **each W&B phase**  
  (ramp, taxi, takeoff, in-flight, landing).  
- Interfaces with:
  - **ATA 28 — H₂ fuel system** for tank layout, capacities, constraints.  
  - **Hybrid / CO₂ battery models** (ATA 10 / 21 / 28 / 36 as applicable) at W&B level.  
  - [02-20-13_Performance_Computer](../02-20-13_Performance_Computer/) for mission segment evolution.  
- Ensures all **H₂-related W&B computations** are **deterministic, traceable and config-controlled**.

It builds on:

- [02-20-12-001_WB_System_Overview.md](./02-20-12-001_WB_System_Overview.md)  
- [02-20-12-002_Load_Calculation_Engine.md](./02-20-12-002_Load_Calculation_Engine.md)  
- [02-20-12-003_CG_Envelope_Monitoring.md](./02-20-12-003_CG_Envelope_Monitoring.md)  

---

## 2. Scope

### 2.1 Included

This document covers:

- **Data model** for H₂ tanks / groups inside the WBC.  
- Mapping between **ATA 28 tank definitions** and **WBC mass items**.  
- **Phase-based H₂ mass states** (ramp, taxi, T/O, in-flight, landing).  
- Handling of:
  - **Operational reserves** (contingency, alternate, final).  
  - **Boil-off mass** (where relevant for W&B).  
  - **Tank transfer / consumption strategies** at **W&B abstraction level**.  
- Interfaces with:
  - Performance / hybrid models for **segment-based H₂ usage**.  
  - EFB for **input / visualization** of H₂ loading and balances.  

### 2.2 Excluded

This document does **not** specify:

- Detailed **ATA 28 system behaviour** (valves, pressures, temperatures, control laws).  
- Low-level **hybrid powertrain control** (discharge / recharge strategies, electrical details).  
- Detailed **mission energy management** logic (belongs to hybrid / performance docs).  
- NN-based H₂ / hybrid prediction models (covered under ATA 95 & hybrid subsystem docs).

The WBC only provides a **mass & CG abstraction** of H₂ and hybrid components.

---

## 3. H₂ Tank Representation in WBC

### 3.1 Tank / Group Model

Within the WBC, each physical tank or **logical group of tanks** is represented as a  
**mass item** (or a small set of items) compatible with the **Load Calculation Engine**:

```text
H2TankItem {
  tank_id: string         # e.g. H2-CENTER-1, H2-WING-L, H2-WING-R
  group_id: string        # e.g. H2-GRP-CENTER, H2-GRP-WING
  role: enum              # MAIN, RESERVE, BUFFER, BALANCE, EMERGENCY
  mass_kg: float
  arm_m: float            # longitudinal arm vs aircraft datum
  lat_arm_m: float        # optional lateral arm
  vert_arm_m: float       # optional vertical arm
  station_id: string      # reference to WBC station / zone
  phase_applicability: set{RAMP, TAXI, TO, CRZ, APP, LDG}
  source: enum            # CONFIG, EFB_INPUT, SYSTEM_FEEDBACK
}
````

Characteristics:

* Geometry (arms) and **capacity limits** are **imported from ATA 28 data** and kept under
  configuration control (variant, mod status, tank option).
* The **same tank** may appear in multiple phases with different `mass_kg` as mission progresses.
* The LCE treats these as **standard mass items**; H₂ integration logic is what **drives** their
  evolution between phases.

### 3.2 Static Configuration Inputs

From ATA 28 / configuration data, WBC consumes:

* **Tank capacities** (usable / unusable).
* **Min / max operating levels** per tank or group.
* **Geometric arms** and optional inertia proxies.
* **Operational roles** (main, reserve, emergency, buffer, trim tanks).

All such data are **read-only** for WBC and versioned via config IDs
(e.g. `H2CONF_Q100_V1`).

---

## 4. Phase-Based H₂ Mass States

### 4.1 Phases & Reference States

WBC computes H₂ mass & CG for **key W&B phases**:

* `RAMP`: total loaded H₂ at block-on / start of turn.
* `TAXI`: after expected taxi H₂ usage (if modelled separately).
* `TO`: takeoff mass (TOW) including H₂ at brake release.
* `CRZ`: representative **cruise state(s)** when required for W&B / envelope (optional).
* `APP` / `LDG`: approach and landing masses.

For each phase **P**, the H₂ mass items are:

* `mass_kg_P(tank)` updated according to **consumption and boil-off models**.
* Combined with other mass items to get **phase mass & CG** (LCE responsibility).

### 4.2 Taxi & Takeoff H₂ Usage

At minimum, WBC accounts for **taxi fuel / H₂**:

* Configuration parameter: `H2_taxi_burn_kg` (per route / airport / SOP).
* Application:

  * **Ramp → Taxi**: subtract `H2_taxi_burn_kg` from appropriate tank / group.
  * **Taxi → TO**: additional adjustments if required (e.g. long taxi cases).

The same mechanism may be extended for:

* **APU-like functions** using H₂.
* Ground operations where H₂ is used prior to T/O.

### 4.3 In-Flight & Landing H₂ Usage

For mission flight segments, WBC can operate in two modes:

1. **Simple W&B mode** (no detailed segment modelling inside WBC):

   * Use **planned mission H₂ usage** from the performance / flight planning system.
   * Derive:

     * Expected H₂ at top-of-climb (TOC), mid-cruise, and landing.
   * Apply in **coarse steps**:

     * `TO → CRZ → APP → LDG`.

2. **Segment-driven mode** (when hybrid / performance provides more detail):

   * Consume **segment-based H₂ usage profiles** from:

     * 02-20-13 / hybrid subsystem (e.g. `Segment: CLB1, CRZ1, CRZ2, DES1, ...`).
   * WBC aggregates these to produce phases P as above.

In both cases, WBC is **not** responsible for computing detailed consumption;
it relies on **external energy models** and **flight planning**. Its job is to
reflect resulting H₂ masses in W&B.

---

## 5. Boil-Off, Reserves & Special Cases

### 5.1 Boil-Off Modelling (W&B Level)

If **H₂ boil-off** is non-negligible for W&B:

* Model as an additional **mass reduction** over time or segments:

  * `Δmass_boiloff = f(time, tank, conditions)`
* Implement a simple, conservative approximation (e.g. kg/hour per tank group).
* Attribute boil-off mass to **specific tanks** (usually those with highest exposure).

Boil-off contributes to:

* Reduced total H₂ mass at later phases (CRZ, APP, LDG).
* **CG drift** if boil-off is not symmetric between tanks.

Detailed thermodynamic modelling belongs to ATA 28 / propulsion; WBC uses
a **simplified, conservative input model**.

### 5.2 Operational Reserves

The following nominal reserves may be represented explicitly in WBC:

* **Contingency H₂**
* **Alternate H₂**
* **Final reserve H₂**
* **Extra H₂** (company policies, passenger connections, etc.)

Integration options:

* Represent each reserve as:

  * **Named mass partition** within tank groups (logical separation), or
  * **Derived quantities** computed from planned mission usage and tank total.

WBC must at least ensure that:

* The **landing phase** includes the required reserves.
* If a scenario would **violate reserve requirements** (e.g., due to extended taxi or
  diversion), WBC flags it for EFB and CAOS analysis.

### 5.3 Tank Imbalance and Transfer Strategies

In BWB / multi-tank architectures:

* **Tank imbalance** can significantly affect **CG & roll trim**.
* **Transfer strategies** (center → wing, cross-feed, etc.) are governed by ATA 28 / control logic.

At W&B level:

* WBC may receive **planned transfer patterns**:

  * e.g., “center-first consumption, wings maintained above X% until later segment.”
* These are converted into **time / segment-based mass per tank**.
* Resulting **CG evolution** is then fed into:

  * CG Envelope Monitoring (02-20-12-003).
  * Performance and handling analyses (e.g. BWB aero in 02-20-13-006).

WBC does **not** decide transfer strategy; it **reflects** it.

---

## 6. Integration with Performance & Hybrid Models

### 6.1 Interface to Performance Computer (02-20-13)

WBC provides to [02-20-13_Performance_Computer](../02-20-13_Performance_Computer/):

* For **TO / LDG** performance:

  * `TOW_kg`, `LW_kg`, `ZFW_kg`.
  * `CG_%MAC` for respective phases.
  * **H₂ distribution** per main tank group, when required for BWB models.

* For **cruise / hybrid envelope** checks:

  * Phase / segment-based **H₂ mass and CG** snapshots (if requested).
  * Simple **H₂ evolution curves** for W&B-level simulations.

Performance Computer uses this to:

* Refine **drag polars and margins** (see 02-20-13-006 BWB models).
* Evaluate **hybrid power envelopes** and H₂ energy sufficiency (RQ-10-02, etc.).

### 6.2 Interface to Hybrid / Energy System Docs

Hybrid / energy subsystems (ATA 10 / 21 / 28 / 36) are authoritative for:

* **H₂ consumption vs power**.
* **CO₂ battery mass significance** (if dynamic).
* **Segment-based energy flows**.

WBC expects **input abstractions**, e.g.:

```text
H2MissionProfile {
  flight_id,
  variant_id,
  segments: [
    { id: "CLB1",  delta_h2_kg:  XXX, start_time: ..., end_time: ... },
    { id: "CRZ1",  delta_h2_kg:  YYY, ... },
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

WBC maps this into:

* Per-phase H₂ masses and CG.
* Scalar values supporting **envelope checks** and EFB displays.

---

## 7. EFB Integration

For [02-20-11_Electronic_Flight_Bag](../02-20-11_Electronic_Flight_Bag/), WBC supports:

* **Input screens**:

  * H₂ loading per tank group (planned / actual).
  * Reserve policy overview and **min required H₂**.

* **Output / visualizations**:

  * H₂ **loading overview** at ramp / T/O / landing.
  * Simple **“fuel map”** across tanks highlighting:

    * Imbalances beyond thresholds.
    * Reserve shortfalls.

* **Warnings**:

  * Reserves not met.
  * Configurations that would produce CG outside envelope.
  * Tank mass distributions violating local or global limits.

UI specifics are outside this document; here we just define the **data** WBC can provide.

---

## 8. Safety & Certification Considerations

H₂ Fuel Integration in WBC is **safety-significant** because:

* It directly affects **mass & CG**, which drive:

  * Structural limits (MTOW / MLW, local tank limits).
  * Stability & control margins (via CG).
* Mis-modelling H₂ could:

  * Mask operations **outside CG envelope**.
  * Underestimate **takeoff or landing mass**.
  * Misrepresent reserves.

Therefore:

* H₂ mass & CG modelling must be **consistent with ATA 28** certified data.
* WBC implementations are subject to **DO-178C** level consistent with overall WBC DAL
  (likely B/C, subject to authority agreement).
* Configuration control must ensure:

  * Tank definitions and capacities used in WBC **match** the physical aircraft.
  * Changes (mods, new variants) are fully traced.

If NN / AI models are later used to estimate H₂ usage or reserves:

* They must be handled under **ATA 95**, with:

  * **Bounded corrections**,
  * Deterministic fallback,
  * **Runtime monitoring and logging**.
* WBC remains the **deterministic reference** for W&B.

---

## 9. Verification & Test Artefacts (Placeholders)

Dedicated V&V documentation (e.g. `02-20-12-007_WB_V_and_V.md`) will define:

* Test sets like:

  * `TEST_DATA/02-20-12-T-003_WB_H2_Evolution.json`
  * `TEST_DATA/02-20-12-T-005_WB_H2_Reserves_And_Imbalance.json`

Each test case should specify:

* **Input**:

  * Initial H₂ per tank.
  * Mission segment profile & reserves.
  * Tank transfer strategy (if relevant).

* **Expected**:

  * H₂ mass per tank at each phase.
  * Phase mass & CG including H₂.
  * Any warnings / status flags (reserves, imbalance, limits).

These tests must be traceable to:

* H₂-related requirements (e.g., `RQ-02-20-12-H2-MASS-CG`, `RQ-02-20-12-H2-RESERVES`).
* Supporting analyses from ATA 28 / hybrid systems.

---

## 10. Dependencies & Cross-References

### Internal (02-20)

* [./02-20-12-001_WB_System_Overview.md](./02-20-12-001_WB_System_Overview.md)
* [./02-20-12-002_Load_Calculation_Engine.md](./02-20-12-002_Load_Calculation_Engine.md)
* [./02-20-12-003_CG_Envelope_Monitoring.md](./02-20-12-003_CG_Envelope_Monitoring.md)
* `02-20-12-007_WB_V_and_V.md` *(planned)*

Other subsystems:

* [../02-20-11_Electronic_Flight_Bag/](../02-20-11_Electronic_Flight_Bag/)
* [../02-20-13_Performance_Computer/](../02-20-13_Performance_Computer/)
* 02-20-01 Digital Ops Platform / CAOS (for data exchange & analytics).

### Other ATA Chapters

* **ATA 28 — H₂ Fuel System**

  * Tank geometry, capacities, limitations, transfer logic.

* **ATA 31 — Recording**

  * Logging of H₂ masses / balances and W&B snapshots.

* **ATA 95 — Neural Networks**

  * If H₂ usage / hybrid models include NN components, their outputs feed into WBC
    under strict envelope and guardrail policies.

---

## 11. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-12 Weight & Balance Computer
> **Component:** H₂ Fuel Integration
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                         | Notes                           |
| ------- | ---------- | ------------------------------------- | ------------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Performance WG | Initial H₂ integration document |

```
```
