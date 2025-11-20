# 02-20-13-002 — Takeoff Performance

**Document ID:** 02-20-13-002  
**ATA Chapter:** 02-20-13 Takeoff Performance  
**Aircraft Program:** AMPEL360 BWB H₂ Hy-E (Q80/Q100/Q120)  
**Document Type:** Algorithm Design Specification  
**Status:** DRAFT / PLACEHOLDER  

---

## 1. Purpose and Scope

This document specifies the **takeoff performance algorithms** used by AMPEL360 operational tools (EFB, dispatch tools, performance servers) to:

- Compute **takeoff performance limits and margins**
- Provide **operationally usable outputs** (V-speeds, limiting weights, margins)
- Cover both **regulatory compliance** and **fleet-operations efficiency**
- Correctly represent the **hydrogen-electric / CO₂ battery hybrid** propulsion architecture

It applies to:

- **Normal operations** (all systems nominal)
- **Abnormal / degraded conditions** (OEI, degraded battery boost, derated thrust, MEL/CDL items)
- **All certified runway conditions** (dry, wet, contaminated, slopes, obstacles)

---

## 2. References

> **TODO:** Replace placeholders with actual repo paths and add hyperlinks.

- [RQ-02-20-13-001_Takeoff_Performance_Requirements.md](./RQ-02-20-13-001_Takeoff_Performance_Requirements.md)
- [02-20-13-VERIF.md](./VERIF.md)
- [02-20-13-TRACE.csv](./TRACE.csv)
- [02-20-13-EVIDENCE/](./EVIDENCE/)
- Aircraft Flight Manual (AFM) – Takeoff Performance Section  
- EASA CS-25 / FAA 14 CFR Part 25 – Subpart B (Performance)  
- Propulsion & Energy System Models  
  - 70-00-00 Propulsion General  
  - 24-20-xx HV Electrical Power System  
  - 21-80-xx ECS / CO₂ Battery Thermal Constraints  

---

## 3. Operational Use Cases

The algorithms defined here must support, at minimum:

1. **Pre-flight dispatch planning**
   - Compute **limiting takeoff weight (LTOW)** for each candidate runway
   - Provide **V1 / VR / V2** and flap configurations
   - Evaluate **reduced thrust / derate / FLEX** options where applicable

2. **On-board performance (EFB)**
   - Re-compute performance with **updated actual conditions** (QNH, OAT, wind, contamination)
   - Rapid **“what-if” analysis** (changed runway, intersection, MEL items)

3. **Abnormal / contingency**
   - RTO from any speed up to V1 (brake energy & stopping distance)
   - OEI climb gradient compliance
   - Degraded battery / fuel-cell capability (power-limited takeoff)

4. **Post-flight analysis / data mining**
   - Log computed vs achieved margins
   - Feed performance monitoring / tuning of performance models

---

## 4. Inputs

The algorithms rely on the following **input classes**:

### 4.1 Environmental Inputs

- Pressure altitude, temperature (OAT / ISA deviation)
- QNH / QFE (for runway elevation & pressure correction)
- Wind (headwind / tailwind component, crosswind)
- Runway conditions:
  - Dry / wet / contaminated (contamination depth, type)
  - Runway surface type (asphalt, concrete, etc.)
  - Contaminant friction coefficient / µ-equivalent

### 4.2 Runway / Obstacle Inputs

- Runway length TORA / TODA / ASDA
- Runway slope (average, or segmented if available)
- Runway heading, identifier
- Obstacle database:
  - Obstacle height, distance from threshold, lateral offset
  - Required obstacle clearance criteria

### 4.3 Aircraft Configuration / Mass Inputs

- Takeoff weight **W\_TO**
- Center of gravity (CG)
- Flap / slat configuration
- Anti-ice / bleed configuration (equivalent electrical / thermal loads)
- MEL / CDL items affecting performance (drag, thrust, or configuration changes)

### 4.4 Propulsion & Energy System Inputs

- Available thrust / propulsive power as function of:
  - OAT, altitude, Mach, shaft speed
  - State-of-charge of CO₂ battery
  - Fuel-cell stack operating limits (current, voltage, temperature)
- Available **hybrid boost power** (CO₂ battery) vs time
- Any **limitations** on continuous power vs time for takeoff segment

---

## 5. Outputs

Typical outputs per **runway / configuration**:

- **V-speeds:** V₁, Vᵣ, V₂ (and Vmcg / Vmca if required)
- **Required distances:**
  - Accelerate-stop distance (ASD)
  - Accelerate-go distance (AGD)
  - All-engines takeoff distance (TOD, TOFL)
- **Limiting weights:**
  - Field-length-limited weight (W\_FL)
  - Climb-limited weight (W\_CL)
  - Obstacle-limited weight (W\_OBS)
  - Brake-energy-limited weight (W\_BE, if applicable)
- **Margins:**
  - Distance margin vs ASDA / TORA / TODA
  - Climb gradient margin vs regulatory minimum
  - Power / thrust margin vs limits (including CO₂ battery / fuel-cell limits)
- **Operational flags:**
  - Takeoff viable / non-viable
  - Notes on limiting constraints (e.g. “OEI second segment climb limited”)

---

## 6. Algorithm Suite Overview

Each algorithm receives a common **input state vector** and returns outputs plus diagnostics.  
Algorithms are identified for traceability as **ALG-TO-xx**.

### 6.1 ALG-TO-01 — Balanced Field Length / Limiting Weight

Purpose: Find **balanced field condition** where:

> accelerate-stop distance ≈ accelerate-go distance

High-level algorithm:

1. Select candidate **V₁** and **takeoff weight W**.
2. Compute:
   - ASD(W, V₁) using deceleration model (brakes, reverse, aerodynamic drag)
   - AGD(W, V₁) using OEI performance model
3. Enforce constraints:
   - ASD ≤ ASDA (incl. regulatory safety factors)
   - AGD ≤ TODA
4. Iterate on **V₁** (and if needed W) until:
   - |ASD − AGD| < tolerance  
   - Both within declared distances
5. If infeasible, reduce W and repeat.

Outputs:

- Balanced field **V₁**, required distances
- Minimum weight for feasible balanced field or **“NO SOLUTION”** flag

### 6.2 ALG-TO-02 — V-Speeds Determination

V-speeds are computed such that:

- V₁ within allowable range [V\_min, V\_max] (brake / engine / control limits)
- Vᵣ ≥ Vmu + margin
- V₂ guarantees OEI climb gradient

Basic logic:

1. For given W, config, conditions:
   - Compute **Vmcg, Vmca, Vmu** and corresponding margins.
2. Define candidate Vᵣ and V₂ as:
   - V₂ = k₂ · Vs\_OEI (k₂ > 1.13 typical)
   - Vᵣ = V₂ − ΔV (account for rotation & liftoff)
3. Select **V₁** through ALG-TO-01.
4. Verify:
   - V₂ ≥ V₂,min (regulatory)
   - Vᵣ ≥ Vᵣ,min (control & tail-strike limits)
5. If constraints violated, iterate on V₂, Vᵣ, and W.

### 6.3 ALG-TO-03 — Climb-Limited Takeoff Weight

Purpose: ensure compliance with **OEI climb gradients**:

- 1st segment, 2nd segment, en-route, etc.  

Algorithm:

1. For each segment and W:
   - Compute thrust / power available (including hybrid boost envelope).
   - Compute drag (configuration, gear, flaps).
   - Calculate climb gradient γ = (T − D − W·sin(γ)) / W → approximate via Δh/Δs.
2. Compare with regulatory minimum γ\_req (including environmental & bank angle effects).
3. Find maximum W such that γ ≥ γ\_req for all segments.

Output: **W\_CL** and segment-wise margins.

### 6.4 ALG-TO-04 — Obstacle-Limited Takeoff Weight

Purpose: ensure required **clearance over obstacles** in takeoff path.

Simplified approach:

1. Build takeoff trajectory:
   - Ground roll until liftoff  
   - Initial climb (all-engines or OEI as per basis)  
   - Screen height segment (typically 35 ft OEI, 15 ft AEO)
2. For each obstacle:
   - Compute height of aircraft at horizontal position of obstacle.
   - Check margin vs required obstacle clearance (e.g. 35 ft).
3. Iteratively reduce W (or adjust V₂) until clearance satisfied.

Output: **W\_OBS** and minimum margin.

### 6.5 ALG-TO-05 — Field-Length-Limited Weight

Purpose: compute weight limited purely by **declared distances** (TORA/TODA/ASDA), independent of obstacles.

Algorithm:

1. For each W:
   - Compute ASD, AGD, TOFL (all-engines).
2. Apply safety / regulatory factors.
3. Find maximum W such that:
   - ASD ≤ ASDA  
   - AGD ≤ TODA  
   - TOFL ≤ TORA × factor (if applicable)

Output: **W\_FL**.

### 6.6 ALG-TO-06 — Brake Energy / Rejected Takeoff Limits

Purpose: ensure brakes / wheels stay within thermal and structural limits in **RTO at V₁**.

Algorithm:

1. Model energy absorbed by brakes during RTO:
   - E\_brakes = Δ(kinetic energy) × allocation factor
2. Compare E\_brakes with brake energy capacity curves vs speed & weight.
3. Account for:
   - Initial brake / wheel temperature
   - Autobrake / manual braking profile
4. Compute **maximum allowed V₁** or **maximum W** for brake limits.

Output: W\_BE or equivalent constraint on V₁.

### 6.7 ALG-TO-07 — Hybrid Power / CO₂ Battery Constraints

Hydrogen-electric specifics:

1. For given W and profile, compute **required power vs time** for:
   - Ground roll
   - Rotation & liftoff
   - Initial climb, OEI segments
2. Validate against:
   - Fuel-cell stack power capability vs time & temperature
   - CO₂ battery discharge limits (max power, energy, C-rate)
3. Apply **margin factors** to ensure:
   - No violation of thermal / current / voltage limits
   - Adequate power for worst-case ambient conditions

Output:

- Pass/fail flag for **power-limited takeoff**
- Maximum allowable **hybrid boost duration** and margin

---

## 7. Data Models and Interpolation

Key data components:

- **Aerodynamic models**: CL, CD, CM vs α, Mach, flap, gear
- **Thrust / power models**: maps vs altitude, OAT, Mach, shaft speed
- **Mass & inertia**: reference weights, inertial properties
- **Brake / tire models**: µ vs speed, pressure, contamination, temperature

Implementation notes:

- Use **monotonic interpolation** for critical curves (no artificial oscillations).
- Enforce **bounds checking** (no extrapolation beyond certified envelopes).
- Every data source must be **versioned and traceable** to its origin (CFD, wind tunnel, flight test, analysis).

---

## 8. Assumptions, Limitations and Safety Margins

Examples (to be refined):

- **Headwind credit** limited (e.g. 50% of steady headwind) and **no tailwind credit** beyond approved limits.
- Only **approved contamination states** and µ-values are allowed.
- No performance credit for **reverse thrust** unless explicitly approved.
- Minimum **system availability assumptions** (number of engines / stacks / battery modules ONLINE).
- **Thermal soak** and preceding flight profile may limit available power; default conservative assumptions if no detailed history.

> **TODO:** Align final assumptions with AFM and certification basis; document any differences between **planning** vs **dispatch** policies.

---

## 9. Verification and Validation Strategy

The correctness of these algorithms will be demonstrated through:

1. **Analytical cross-checks**
   - Comparison against simplified hand-calculation cases.
   - Sensitivity analyses (ΔOAT, Δwind, Δslope).

2. **Model vs Source Data**
   - Interpolation accuracy vs input data (CFD, WT, performance analyses).
   - No significant bias across the envelope.

3. **AFM Concordance**
   - Spot checks against AFM tables / curves.
   - Define acceptance bands (e.g. ±1–2% distance, ±1 kt speed).

4. **Monte Carlo / Robustness**
   - Randomized sampling of inputs to verify monotonic / expected behaviour.
   - Check for numerical instabilities, non-physical discontinuities.

5. **Flight Test Correlation (later phases)**
   - Progressive tuning of models against actual flight-test measurements.
   - Document deviations and model updates in [CHANGES.md](./CHANGES.md) and [TRACE.csv](./TRACE.csv).

> Detailed test cases, procedures and results are referenced in **[VERIF.md](./VERIF.md)** and supporting evidence under **[EVIDENCE/](./EVIDENCE/)**.

---

## 10. Interfaces and Implementation Notes

These algorithms are consumed by:

- **EFB applications** (ATA 31)  
- **Dispatch / flight planning tools**  
- **On-board monitoring** (to cross-check expected vs actual TO performance)  

Key interface considerations:

- Stateless, **pure-function style** APIs where possible:
  - `takeoff_performance(inputs) → outputs, diagnostics`
- All numeric outputs should carry:
  - Units
  - Source / model version
  - Validity flags (OK, WARNING, INVALID)

Logging:

- For each operational use, log:
  - Inputs (sanitized)
  - Outputs
  - Model version ID
  - Any warnings / limit hits  

This enables **traceability** and **post-incident analysis** under ATA 95 NN / data governance framework.

---

## 11. Open Points / TODOs

- [ ] Finalise **regulatory margins** and safety factors (EASA/FAA harmonisation).
- [ ] Freeze **data model interfaces** for propulsion / aero / brake subsystems.
- [ ] Define **performance levels of service**: on-board vs ground-based computations.
- [ ] Add **examples**: worked takeoff case (numerical) for documentation.
- [ ] Link to **AI/NN-based enhancements** (if any) under ATA 95, with fallback to deterministic baseline.

---


