# 02-20-13-006 — BWB- & H₂-Specific Performance Calculations

**Document ID:** 02-20-13-006  
**ATA Chapter:** 02-20-13 Performance Tools – BWB / H₂ Specifics  
**Aircraft Program:** AMPEL360 BWB H₂ Hy-E (Q80/Q100/Q120)  
**Document Type:** Aerodynamic & Energy Model Specification  
**Status:** DRAFT / PLACEHOLDER  

---

## 1. Purpose and Scope

This document defines the **specialized models and calculation methods** needed to correctly capture:

- **Blended-Wing-Body (BWB)** aerodynamics and mass distribution, and  
- **Hydrogen-electric / CO₂ battery hybrid** propulsion & energy characteristics  

for use by:

- Takeoff performance algorithms (02-20-13-002)  
- Landing performance algorithms (02-20-13-003)  
- Cruise / CI optimization algorithms (02-20-13-004)  
- NN Performance Predictor integration (02-20-13-005)  

The aim is to provide a **common toolbox of sub-models** (ALG-BWB-xx) so that all performance tools use **consistent BWB & H₂ physics** rather than legacy “tube-and-wing + kerosene” assumptions.

---

## 2. References

> **TODO:** Replace placeholders with actual repo paths and hyperlinks.

Performance tools:

- [02-20-13-002_Takeoff_Performance.md](./02-20-13-002_Takeoff_Performance.md)  
- [02-20-13-003_Landing_Performance.md](./02-20-13-003_Landing_Performance.md)  
- [02-20-13-004_Cruise_Optimization.md](./02-20-13-004_Cruise_Optimization.md)  
- [02-20-13-005_NN_Performance_Predictor.md](./02-20-13-005_NN_Performance_Predictor.md)  

Aero / structures / systems:

- 02-xx-xx Aerodynamic data packs (CL/CD/CM tables, BWB-specific polars)  
- 70-00-00 Propulsion General (open-fan / hybrid propulsion architecture)  
- 21-xx-xx ECS & cryogenic system models (H₂ storage / boil-off / thermal)  
- 24-20-xx HV electrical power system models (HVDC bus, CO₂ battery)  

Neural networks & traceability (if NN-enhanced models are used):

- ATA 95-00-00 General / Neural Networks documentation

---

## 3. BWB Geometry & Aerodynamic Representation

### 3.1 Equivalent Reference Quantities (ALG-BWB-01)

BWB configurations do not have a conventional “wing + fuselage” separation. For performance tools, the following **equivalent reference values** must be defined:

- Reference **wing area** Sref,BWB  
- Reference **span** bref,BWB  
- Reference **mean aerodynamic chord (MAC)** and reference point  
- Equivalent **wing-body drag area** (CD₀·Sref)  

Algorithm sketch:

1. Integrate contributions from **planform panels** (outer wing, center body, blends).  
2. Define Sref,BWB as:
   - Either geometric wetted projection, or  
   - Certification-agreed reference area (frozen and documented).  
3. Derive MAC from integrated chord distribution.

Outputs:

- `Sref_BWB`, `bref_BWB`, `MAC_BWB`, `x_LE_MAC`, `y_MAC_ref`  

### 3.2 Non-Elliptic Lift Distribution & CLmax (ALG-BWB-02)

BWB lift distribution is **non-elliptic** and heavily influenced by:

- Planform and twist  
- Distributed flaps & elevons  
- Center body camber  

ALG-BWB-02 provides:

- CL(α, Mach, config)  
- CLmax,stall (global)  
- Local lift distribution metrics for **control & performance margins**  

Notes:

- CLmax may **vary strongly with CG and control law**; performance tools must use validated envelopes.  
- Data comes from CFD / WT / flight-test and is **not** assumed elliptical.

### 3.3 Pitching Moment and Trim Penalties (ALG-BWB-03)

Because the BWB has **no separate tail**, trim is achieved via:

- Elevons / flaperons  
- Possible camber control  

ALG-BWB-03 provides:

- CM(α, Mach, config, CG)  
- Required control surface deflections for trim  
- Associated **drag penalties** (ΔCD_trim)  

Outputs are used by performance tools to:

- Adjust drag polars for trimmed condition  
- Account for **trim drag** impact on takeoff / climb / cruise / landing.

---

## 4. Aero-Propulsive Integration & Distributed Propulsion

### 4.1 Propulsor–Airframe Interactions (ALG-BWB-04)

For distributed / open-fan propulsion embedded in the BWB:

- Local flow acceleration & distortion influence propulsor performance  
- Powered lift and wake-filling reduce effective drag  

ALG-BWB-04 defines:

- Thrust / power correction factors vs:
  - Angle of attack, flap setting, lift coefficient  
  - Propulsor placement and operating point  
- Effective **propulsive efficiency** η\_p,BWB vs Mach, altitude, load.

### 4.2 Boundary-Layer Ingestion (BLI) Models (ALG-BWB-05)

If BLI is employed, net propulsive benefit is modeled via:

- Ingested boundary-layer profile (velocity deficit profile)  
- BLI-specific **η\_BLI gain factors**  

Outputs used by performance tools:

- ΔCD\_BLI (equivalent drag reduction)  
- Corrected thrust requirement **T_req,BLI** vs non-BLI reference  
- Validity envelope (Re, Mach, α range).

> **TODO:** Clarify whether BLI effects are implemented as **pre-processed data** or run-time corrections.

---

## 5. Hydrogen & Hybrid Energy System Effects

### 5.1 Hydrogen Mass & CG Evolution (ALG-H2-01)

Cryogenic hydrogen tanks embedded in BWB cause:

- Significant **CG migration** as hydrogen is consumed  
- Non-linear impact on **inertia properties**  

ALG-H2-01 provides:

- m\_H2(t) and **tank-by-tank mass distribution**  
- CG(t) and inertia tensor evolution  
- Simple interface: for given aircraft **weight state** and mission progress, return:
  - total weight  
  - CG position  
  - inertia subset relevant to performance (e.g. pitch inertia trend).

### 5.2 Boil-off & Venting Models (ALG-H2-02)

Boil-off and venting may affect:

- Effective **usable hydrogen**  
- Thermal / pressure constraints and energy balance  

ALG-H2-02 defines:

- Boil-off rate vs:
  - Mission phase  
  - Ambient temperature  
  - Tank insulation and fill level  
- Impact on **usable hydrogen** and performance reserves.

### 5.3 CO₂ Battery & Hybrid Boost Envelopes (ALG-HYB-01)

Hybridization with a high-power **CO₂ battery** introduces:

- Transient **boost capability**  
- Limits on **continuous discharge / charge**  
- Effect on **takeoff, climb, and contingency performance**  

ALG-HYB-01 provides:

- Max P\_boost(t) for given SOC, temperature, mission phase  
- Allowed cumulative **boost energy** over phases (takeoff, climb, go-around)  
- Minimum SOC reserves for:
  - Diversion  
  - Abnormal / emergency scenarios.

Outputs feed:

- Takeoff algorithms (power-limited TO)  
- Climb / drift-down envelopes  
- Cruise and descent energy management.

---

## 6. BWB- & H₂-Specific Performance Metrics

### 6.1 Carbon-Negative Performance Indicators (ALG-BWB-06)

For AMPEL360, performance tools must expose:

- Net **CO₂ equivalent** metric vs a conventional baseline:
  - H₂ production pathway  
  - Grid energy for battery charging  
  - Any CO₂ capture / sequestration contributions.

ALG-BWB-06 defines:

- **Mission-level CO₂eq balance**:
  - Emissions avoided vs reference  
  - Credits for carbon capture (if applicable).  
- Per-flight metrics used in cruise optimization & reporting.

### 6.2 Comfort & Cabin-Related Penalties (ALG-BWB-07)

Unique BWB cabin layout may impact:

- Pressurization loads  
- Ventilation / ECS power  
- Noise / vibration 

ALG-BWB-07 provides simplified **performance penalties or corrections** linked to:

- ECS power vs cabin zone distribution  
- Additional power demand from BWB-specific cabin systems.

---

## 7. Algorithm Suite Overview

BWB and H₂-specific algorithms are identified as **ALG-BWB-xx** and **ALG-H2/HYB-xx**.  
They are **subroutines**, called by high-level performance modules, e.g.:

```text
inputs_performance
  ├─► ALG-BWB-01/02/03        # geometry, CL/CD/CM, trim drag
  ├─► ALG-BWB-04/05           # aero-propulsive interaction, BLI
  ├─► ALG-H2-01/02, ALG-HYB-01# H₂ mass/CG, boil-off, CO₂ battery envelope
  └─► TO/LND/CRZ algorithms   # 02-20-13-002/003/004 core logic
````

Each algorithm:

* Has a **well-defined interface** (inputs, outputs, units).
* Has a **validity envelope** (Mach, Re, α, configuration, etc.).
* Is versioned and traceable to data sources (CFD, WT, flight test, system models).

> **TODO:** Provide per-algorithm interface tables in ASSETS/API/02-20-13-BWB_Specific_Calculations_API.md.

---

## 8. Data Sets, Parameterization and Interpolation

Data sources:

* High-fidelity **CFD** and wind-tunnel data for BWB aero
* System models for hydrogen tanks, CO₂ battery, fuel-cell stacks
* Structural models for CG and inertia evolution

Implementation rules:

* Use **monotonic interpolation** for safety-critical curves (CLmax, drag polars, power limits).
* Enforce **bounds checking**; outside envelope → mark as **INVALID** and handled at higher level.
* Each dataset must be tagged with:

  * Dataset ID, origin, validation status
  * Applicable mission phases and configurations.

---

## 9. Assumptions, Limitations, and Safety Margins

Examples to be refined:

* BWB aero data assumed valid within specified **Mach / Re / α ranges**; outside, revert to conservative extrapolation or declared **non-usable**.
* Hydrogen system models may use **simplified boil-off** where full thermodynamic simulation is unavailable, with conservative safety margins.
* Hybrid system (CO₂ battery + fuel cells) uses:

  * Conservative limits for temperature and C-rate
  * No performance credit for short-term overload beyond certified limits.
* Any **powered-lift** or BLI benefits are only credited **within proven and certified envelopes**.

All assumptions must be:

* Explicitly documented
* Aligned with AFM and certification basis
* Referenced from the requirements and verification artefacts.

---

## 10. Verification and Validation Strategy

Validation is multi-layered:

1. **Model vs Source Data**

   * Check that ALG-BWB and ALG-H2/HYB reproduce reference CFD/WT/system data within defined tolerances.

2. **End-to-End Performance Checks**

   * Plug BWB/H₂-specific models into TO/LND/CRZ algorithms.
   * Compare results vs:

     * High-fidelity simulation chains
     * (Later) flight-test data.

3. **Sensitivity and Robustness**

   * Vary key parameters (CG, H₂ mass, SOC, temperature) and verify:

     * Qualitative behaviour makes sense
     * No non-physical discontinuities or instabilities.

4. **Safety Properties**

   * Demonstrate that:

     * Power-limited cases are correctly flagged
     * BLI / powered-lift benefits **never** reduce safety margins outside validated envelopes.

Verification artefacts will be captured in:

* [02-20-13-VERIF.md](./VERIF.md)
* [02-20-13-EVIDENCE/BWB_Specific_Calculations/](./EVIDENCE/BWB_Specific_Calculations/)

---

## 11. Interfaces, Implementation Notes and Tooling

Consumers:

* 02-20-13 performance tools (TO/LND/CRZ/NN integration)
* 70-00-00 propulsion analysis tools
* 21-xx / 24-xx H₂ and electrical system studies

Implementation guidance:

* Provide **language-agnostic reference equations** and **test vectors**.
* Reference implementations may exist in:

  * `tools/perf_core/ALG_BWB_xx.py`
  * `tools/perf_core/ALG_H2_HYB_xx.py`

Logging:

* For debugging / traceability, performance tools may log:

  * Input / output of ALG-BWB/H2/HYB calls
  * Data/model version IDs
  * Any envelope / validity warnings.

---

## 12. Open Points / TODOs

* [ ] Freeze **reference geometry definition** (Sref, MAC, etc.) for all AMPEL360 variants (Q80/Q100/Q120).
* [ ] Finalize **BLI and powered-lift modelling approach** (run-time vs pre-tabulated).
* [ ] Complete hydrogen tank and CG evolution models, including **multi-tank management logic**.
* [ ] Define **CO₂ battery ageing / life-consumption model** hooks for performance–maintenance coupling.
* [ ] Add **worked numerical examples**:
  - BWB CL/CD/CM vs tube-and-wing equivalent
  - Takeoff case with hybrid boost constraint
  - Cruise case with BLI benefit and carbon-negative metrics.

---

*Editor’s note:*
This is a **skeleton specification** for BWB- and H₂-specific performance models. Detailed equations, data references and validated numerical examples will be added as aerodynamic, propulsion and energy-system models mature.

```
```
