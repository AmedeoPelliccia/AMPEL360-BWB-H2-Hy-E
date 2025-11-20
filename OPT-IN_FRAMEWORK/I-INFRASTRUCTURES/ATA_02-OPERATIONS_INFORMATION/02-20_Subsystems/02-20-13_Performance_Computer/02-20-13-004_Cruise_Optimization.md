# 02-20-13-004 — Cruise Optimization

**Document ID:** 02-20-13-004  
**ATA Chapter:** 02-20-13 Performance Tools – Cruise Optimization  
**Aircraft Program:** AMPEL360 BWB H₂ Hy-E (Q80/Q100/Q120)  
**Document Type:** Algorithm Design Specification  
**Status:** DRAFT / PLACEHOLDER  

---

## 1. Purpose and Scope

This document specifies the **cruise optimization algorithms** used by AMPEL360 operational tools (OFP/dispatch, EFB, performance servers) to:

- Determine **optimal cruise profiles** (speed, altitude, step climbs)  
- Implement **cost index (CI)**-driven optimization including **time, hydrogen consumption, grid energy, CO₂ balance and component ageing**  
- Generate **flight plans and guidance targets** compatible with FMS / MCP and ATC constraints  
- Respect **hydrogen-electric / CO₂ battery hybrid** system constraints and thermal envelopes  

It covers:

- **Pre-flight** planning (OFP generation)  
- **In-flight** re-optimization (reroutes, level changes, system degradations)  
- **Post-flight** analysis and model tuning  

---

## 2. References

> **TODO:** Replace placeholders with actual repo paths and add hyperlinks.

- [RQ-02-20-13-003_Cruise_Optimization_Requirements.md](./RQ-02-20-13-003_Cruise_Optimization_Requirements.md)  
- [02-20-13-VERIF.md](./VERIF.md)  
- [02-20-13-TRACE.csv](./TRACE.csv)  
- [02-20-13-EVIDENCE/](./EVIDENCE/)  

Technical / regulatory:

- AFM / FCOM – Cruise/Climb/Descent Performance sections  
- EASA CS-25 / FAA 14 CFR Part 25 – Performance (cruise & operational)  
- Propulsion & Energy System Models  
  - 70-00-00 Propulsion General  
  - 24-20-xx HV Electrical Power System  
  - 21-80-xx ECS / thermal management  
- ATA 95 – Neural Networks / Predictive models (if used as augmentations)  

---

## 3. Operational Use Cases

The algorithms must support at least:

1. **Pre-flight OFP generation (ground systems)**
   - Select **economical FL & speed schedule** between departure and destination  
   - Compute **block time, hydrogen usage, grid energy usage (if relevant), CO₂ balance proxy**  
   - Evaluate alternatives: different routes, levels, CI values  

2. **In-flight re-optimization (EFB / FMS support)**
   - Recompute optimal FL and Mach:
     - After ATC level changes  
     - After reroutes / direct segments  
     - After changes in wind / temperature forecast  
   - Respond to **system degradations** (reduced propulsion / power / thermal margin)  

3. **Hybrid power & thermal management**
   - Maintain **fuel-cell and CO₂ battery** within safe and efficient operating regions  
   - Avoid **excessive cycling** that reduces component life or thermal margins  
   - Provide profiles that support **energy recovery periods** where needed  

4. **What-if / strategy evaluation**
   - Compare:
     - Min-time vs min-hydrogen vs eco-CO₂ profiles  
     - Different CI values for same city pair  
   - Show **sensitivity** to winds, CI and weight assumptions  

5. **Post-flight analytics**
   - Compare planned vs achieved:
     - Cruise Mach / altitude  
     - Hydrogen & energy consumption  
     - Deviation from optimal profile due to ATC / weather / constraints  

---

## 4. Inputs

### 4.1 Route / Airspace Inputs

- Sequence of waypoints and constraints:
  - Latitude / longitude / altitude constraints  
  - Speed limits (IAS/Mach caps)  
  - Required times of arrival (RTA) where applicable  
- Available flight levels (per direction, RVSM structure)  
- Airspace restrictions:
  - No-fly zones, mandatory routes  
  - Oceanic / procedural segments  

### 4.2 Atmosphere / Wind Inputs

- Vertical and horizontal profiles of:
  - Temperature vs altitude  
  - Pressure / density vs altitude  
  - Winds (head/tail and crosswind component) vs altitude and along route  
- Turbulence / CB zones (if considered for derates / penalties)  

### 4.3 Aircraft / Weight State

- Initial **takeoff weight W\_TO** and **weight at TOC** (from climb models)  
- Weight evolution along route:
  - Hydrogen mass flow rate vs power, altitude, Mach  
  - Any non-propulsive mass changes (fuel transfer, dumps, etc., if applicable)  
- Configuration assumptions (clean cruise, anti-ice ON/OFF, etc.)  

### 4.4 Propulsion & Energy System Inputs

- Fuel-cell stack efficiency maps vs:
  - Power, temperature, pressure  
- CO₂ battery:
  - Allowed charge/discharge band during cruise  
  - Efficiency vs C-rate and temperature  
  - State-of-charge (SOC) at TOC and minimum SOC reserves  
- Thermal management limits:
  - Max continuous power for given ambient  
  - Required cool-down phases / reduced power zones  

### 4.5 Cost / Objective Parameters

- **Cost Index vector** (multi-dimensional CI), e.g.:

  - C\_time [cost per minute]  
  - C\_H2 [cost per kg hydrogen]  
  - C\_grid [cost per kWh from battery charging]  
  - C\_CO2 [cost per kg CO₂ equivalent, incl. credits for carbon-negative ops]  
  - C\_age [equivalent cost of component ageing / cycles]  

- Operational policy flags:
  - Prefer **time** vs **energy** vs **CO₂** vs **component life**  
  - Hard constraints (e.g. must meet RTA, cannot exceed specific energy budgets)  

---

## 5. Outputs

For each route / CI / scenario:

- **Optimized cruise profile**:
  - Cruise Mach vs along-track distance  
  - Altitude profile including **step climbs / step descents**  
  - Estimated TOC, TOD and potential level segments  

- **Performance metrics**:
  - Block time, airborne time  
  - Hydrogen consumption (kg)  
  - Grid/CO₂ battery net energy use (kWh in/out)  
  - Net CO₂ balance indicator (e.g. kg CO₂ eq vs baseline)  

- **System constraints and margins**:
  - Max fuel-cell temperature margin  
  - CO₂ battery SOC envelope over flight  
  - Thermal and power margins  

- **Operational flags**:
  - Profile feasible / not feasible  
  - ATC / RVSM compatibility issues  
  - RTA achieved / not achieved  

All outputs must carry **units**, **model/data version IDs**, and **validity flags**.

---

## 6. Algorithm Suite Overview

Cruise algorithms are identified as **ALG-CRZ-xx** and share a common input structure:

```text
cruise_inputs → ALG-CRZ-xx → optimized_profile, metrics, diagnostics
````

### 6.1 ALG-CRZ-01 — Cost Function and CI Mapping

Purpose: convert **Cost Index / policy settings** into a **scalar objective function** suitable for optimization.

High-level logic:

1. Define total mission cost:

   * J = C_time · t + C_H2 · m_H2 + C_grid · E_grid + C_CO2 · E_CO2eq + C_age · A
2. Map operational **CI presets** (e.g. CI = 0, 50, 100) to parameter sets:

   * CI → (C_time, C_H2, C_grid, C_CO2, C_age)
3. Support **multi-objective mode** (e.g. Pareto analysis) if requested.

Output:

* Configured **objective function** (callable) for use by other algorithms.

### 6.2 ALG-CRZ-02 — Speed Schedule Optimization (Fixed Altitude / Segment)

Purpose: find **optimal Mach / IAS** for a given level segment, weight range and cost function.

Steps:

1. For candidate Mach M:

   * Compute drag, thrust / power required
   * Compute hydrogen and energy consumption rate
   * Compute segment time Δt and cost ΔJ
2. Solve:

   * Either derivative-based optimum (dJ/dM = 0)
   * Or discrete search over allowed speed range [M_min, M_max]
3. Enforce constraints:

   * Buffet margins, Mach/IAS limits
   * Thermal / power limits (fuel-cell and battery)

Outputs:

* Optimal Mach for segment: M_opt
* Sensitivity dJ/dM and neighbouring cost values for robustness analysis.

### 6.3 ALG-CRZ-03 — Altitude and Step-Climb Optimization

Purpose: determine **optimal altitude profile** (continuous or stepped) over the route.

Algorithm (discrete dynamic programming sketch):

1. Discretize:

   * Route into along-track segments s_i
   * FL into discrete levels FL_k
2. For each (s_i, FL_k):

   * Use ALG-CRZ-02 to get optimal speed and cost for segment
3. Evaluate transitions:

   * Same level (cruise)
   * Step climb / step descent to neighbouring FL (with climb/descend cost)
4. Run DP / shortest-path on state graph to minimize total J subject to:

   * RVSM rules, ATC constraints
   * Climb gradients, energy limits
5. Reconstruct:

   * Sequence of FLs (step climbs), Mach schedule

Output:

* Altitude profile (FL vs distance/time)
* Associated Mach schedule and segment-wise metrics.

### 6.4 ALG-CRZ-04 — Hybrid Power & Thermal Feasibility Check

Purpose: verify that the candidate cruise profile is **power- and thermal-feasible** for hybrid systems.

Steps:

1. For each segment:

   * Compute required propulsive power and **non-propulsive loads** (ECS, avionics, etc.)
2. Evaluate:

   * Fuel-cell power share
   * CO₂ battery charge/discharge schedule
3. Check against limits:

   * P_stack ≤ P_max(T, h, lifetime)
   * |P_battery| ≤ P_battery,max(SOC, T)
   * SOC within [SOC_min, SOC_max] envelope
4. If infeasible:

   * Propose **profile adjustments** (lower FL, different Mach, relaxation of CI)
   * Return **infeasible** flag and constraint details

Outputs:

* Feasibility flag per segment and for whole profile
* Recommended adjustments (qualitative hints for optimizers).

### 6.5 ALG-CRZ-05 — RTA-Constrained Optimization

Purpose: integrate **Required Time of Arrival** constraints into cruise optimization.

Algorithm:

1. Introduce RTA as a **time constraint** at a given waypoint (or destination).
2. Modify objective:

   * Primary: meet RTA within tolerance Δt_RTA
   * Secondary: minimize cost J subject to |t_arrival − t_RTA| ≤ Δt_RTA
3. Solve via:

   * Time-bias adjustment of CI
   * Local speed/altitude adjustments near RTA fix
4. Ensure RTA-compatible profile remains **hybrid-feasible** via ALG-CRZ-04.

Outputs:

* Cruise profile satisfying RTA (if possible)
* Residual time error and cost penalty.

### 6.6 ALG-CRZ-06 — Contingency & Drift-Down Envelope

Purpose: maintain cruise optimization **consistent with engine/stack-out drift-down** and contingency requirements.

Steps:

1. For each point along route:

   * Compute drift-down paths and minimum safe altitudes for:

     * Single stack/engine out
     * Other defined failures
2. Impose constraint:

   * Planned FL must be ≥ min operational FL and compatible with drift-down safe levels.
3. If optimization proposes infeasible FL:

   * Reject or penalize such states in DP/optimization.

Outputs:

* Drift-down envelope vs route
* Constraint mask for altitude optimization.

### 6.7 ALG-CRZ-07 — Top-of-Climb (TOC) and Top-of-Descent (TOD) Placement

Purpose: coordinate **climb, cruise, and descent** so that cruise optimization is consistent with vertical profile.

Sketch:

1. Use climb and descent performance models (linked to other documents) to:

   * Compute time, distance, and energy for climb/descent for candidate FLs.
2. For selected cruise FL:

   * Determine TOC and TOD positions.
3. Recompute cruise distance and re-optimize cruise if TOC/TOD adjustments change segment lengths significantly.

Outputs:

* TOC, TOD locations
* Consistent end-to-end vertical profile.

---

## 7. Data Models and Interpolation

Required data:

* **Aero**: drag polars vs Mach, altitude, weight, configuration.
* **Propulsion & energy**: efficiency maps, power limits, thermal response.
* **Atmospheric & wind**: gridded along-route data, possibly from forecast models.

Implementation rules:

* Use **monotone, bounded interpolation** for critical performance curves.
* No extrapolation beyond certified envelope; outside region → **INVALID** flag.
* All data model versions recorded in [TRACE.csv](./TRACE.csv) with:

  * Origin (analysis, CFD, WT, flight test)
  * Validity range
  * Change history

---

## 8. Assumptions, Limitations and Safety Margins

Examples (to refine):

* Atmosphere: ISA + ΔT with bounded deviations; extreme conditions treated via **conservative margins**.
* Winds: optimization uses forecast; operational tools must handle **forecast error** via buffers.
* Hybrid systems:

  * No credit for **short-term overload** beyond certified continuous limits.
  * Battery usage during cruise constrained to maintain **landing and diversion reserves**.
* Cost assumptions: CI parameters derive from **airline config / operator policy** and are not hard-coded.

All assumptions must be consistent with AFM, operational documentation and certification basis.

---

## 9. Verification and Validation Strategy

1. **Analytical sanity checks**

   * Known textbook cases (e.g. max-range vs max-endurance Mach) recovered as special cases.
   * Smooth behaviour: small input changes → small output changes.

2. **Comparisons vs reference tools**

   * Concordance with legacy performance tools or high-fidelity simulations.
   * Define acceptable bands for time and energy deviations.

3. **Monte Carlo robustness**

   * Randomized wind/temperature errors to verify robustness of optimal profiles.
   * Check for numerical instabilities or unrealistic FL oscillations.

4. **Flight data correlation (later phases)**

   * Compare optimized profiles with flown profiles and measured consumption.
   * Calibrate models and cost function parameters; document updates in [CHANGES.md](./CHANGES.md) and [TRACE.csv](./TRACE.csv).

Evidence, test cases, and results are captured in **[VERIF.md](./VERIF.md)** and **[EVIDENCE/](./EVIDENCE/)**.

---

## 10. Interfaces and Implementation Notes

Consumers:

* **OFP / dispatch systems**
* **EFB performance modules**
* **FMS / guidance** (via targets and constraints)
* **Analytics / ATA 95 NN systems** for advisory optimization

Interface guidelines:

* Deterministic, stateless functions:

  * `optimize_cruise_profile(inputs) → profile, metrics, diagnostics`
* All outputs tagged with:

  * Units, data/model versions, CI preset ID
  * Validity / quality flags and summary of active constraints

Logging:

* Log each optimization run:

  * Inputs (sanitized)
  * Selected CI and constraints
  * Profile and key metrics
  * Any limit / feasibility flags

This supports **traceability**, **post-event analysis**, and potential **AI-assisted tuning** under ATA 95.

---

## 11. Open Points / TODOs

* [ ] Finalize **CI parameterization**, including CO₂ and ageing components.
* [ ] Decide optimization framework (LP/DP, nonlinear programming, or hybrid).
* [ ] Integrate with climb/descent modules for consistent gate-to-gate trajectory.
* [ ] Define interface to **AI/NN-based advisory tools** (if any), including deterministic fallback.
* [ ] Add worked example: single city-pair, several CI values, comparative plots.

---

*Editor’s note:*
This is a **skeleton specification**. Detailed mathematical formulations, pseudo-code and references to validated data and software implementations will be added as the performance models and certification basis are refined.

```
```
