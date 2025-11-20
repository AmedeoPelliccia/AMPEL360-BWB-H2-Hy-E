# 02-20-13-003 — Landing Performance

**Document ID:** 02-20-13-003  
**ATA Chapter:** 02-20-13 Landing Performance  
**Aircraft Program:** AMPEL360 BWB H₂ Hy-E (Q80/Q100/Q120)  
**Document Type:** Algorithm Design Specification  
**Status:** DRAFT / PLACEHOLDER  

---

## 1. Purpose and Scope

This document specifies the **landing performance algorithms** used by AMPEL360 operational tools (EFB, dispatch systems, performance servers) to:

- Compute **landing performance limits and margins**
- Provide **operationally usable outputs** (VREF, VAPP, limiting landing weights, distance margins)
- Cover both **regulatory compliance** and **fleet-operations efficiency**
- Correctly represent the **hydrogen-electric / CO₂ battery hybrid** propulsion and **braking/regen** characteristics

It applies to:

- **Normal operations** (all systems nominal)
- **Abnormal / degraded conditions** (inoperative systems, degraded spoilers, brake / antiskid / reverser failures, MEL/CDL)
- **All certified runway conditions** (dry, wet, contaminated, slopes, obstacles)
- Both **dispatch landing calculations** and **on-board re-computation** during flight.

---

## 2. References

> **TODO:** Replace placeholders with actual repo paths and add hyperlinks.

- [RQ-02-20-13-002_Landing_Performance_Requirements.md](./RQ-02-20-13-002_Landing_Performance_Requirements.md)  
- [02-20-13-VERIF.md](./VERIF.md)  
- [02-20-13-TRACE.csv](./TRACE.csv)  
- [02-20-13-EVIDENCE/](./EVIDENCE/)  
- Aircraft Flight Manual (AFM) – Landing Performance Section  
- EASA CS-25 / FAA 14 CFR Part 25 – Subpart B (Performance, Landing)  
- Brake/Wheel/Tire Certification Data (ATA 32)  
- Propulsion & Energy System Models  
  - 70-00-00 Propulsion General  
  - 24-20-xx HV Electrical Power System  
  - 21-80-xx ECS / CO₂ Battery Thermal Constraints  

---

## 3. Operational Use Cases

The algorithms defined here must support, at minimum:

1. **Pre-flight and en-route dispatch planning**
   - Compute **limiting landing weight (LLW)** for each destination and alternate runway
   - Evaluate **dry vs wet/contaminated** cases
   - Check compliance with regulatory **landing distance factors** (dispatch vs actual)

2. **On-board EFB landing performance**
   - Re-compute landing performance with **actual or forecast conditions** (QNH, OAT, wind, runway state)
   - “What-if” evaluations (new runway, change of direction, change of autobrake, reversers, flap setting)
   - **In-flight re-planning** after system failures (e.g. antiskid inoperative, reverser inop)

3. **Abnormal and contingency operations**
   - Landing with degraded braking capability
   - Landing with reduced number of spoilers/spoiler panels
   - Landing with **propulsive asymmetry** (engine/stack out, fixed pitch issues, etc.)
   - Short-field / contaminated operations when approved

4. **Post-flight analysis and monitoring**
   - Compare **computed vs actual** landing distance and deceleration profile
   - Feed data to **fleet monitoring**, model tuning, and safety analytics

---

## 4. Inputs

The algorithms rely on the following **input classes**:

### 4.1 Environmental Inputs

- Destination / runway **elevation** and pressure altitude  
- QNH / QFE  
- OAT / ISA deviation  
- Wind (headwind / tailwind component, crosswind)  
- Visibility / RVR (for potential operational minima checks – informational)  

### 4.2 Runway / Surface / Obstacle Inputs

- Runway identifiers, heading, and **LDA** (Landing Distance Available)  
- Runway slope (average, and segmented if supported)  
- Runway surface type and **condition**:
  - Dry, damp, wet
  - Contaminated (type, depth, coverage)  
- **Friction / µ-equivalent** data, if available  
- Optionally, obstacles and approach path constraints:
  - Obstacle height vs distance from threshold vs lateral offset
  - Glide path and minimum approach angle constraints

### 4.3 Aircraft Configuration / Mass Inputs

- Planned or actual **landing weight W\_LDG**  
- CG position  
- Flap / slat configuration  
- Slat/flap failures, spoiler failures, gear configuration  
- Autobrake selection and reverser configuration (both as **requested** and **available**)  
- MEL/CDL items changing drag, lift, braking, or control characteristics  

### 4.4 Propulsion & Energy / Braking Inputs

- Available **reverse thrust / reverse torque** per engine/propulsor (if applicable)  
- Status of **fuel-cell stacks** and CO₂ battery regarding:
  - Electrical availability for antiskid, brake-by-wire, flight controls, spoilers  
  - **Regenerative braking capability** vs SOC, temperature, power limits  
- Brake system state:
  - Brake type, size, energy capacity curves  
  - Initial brake temperature / simple thermal state model  
  - Brake wear / tire wear (if modeled explicitly)  

> Note: **No performance credit** is taken for electrical regeneration into the CO₂ battery unless explicitly approved in certification basis. Regenerative effects are primarily modeled as **thermal & system-availability constraints**, not as thrust/drag/performance credit.

---

## 5. Outputs

For each candidate runway / configuration, algorithms shall generate:

- **Speeds**
  - VREF
  - VAPP (VREF plus additive)
  - V\_GA (go-around reference speed, if required)
- **Landing distances**
  - Required Landing Distance (RLD)
  - Field length requirements for:
    - Dry dispatch
    - Wet/contaminated operational landing
  - Distance to full stop (or to a specific speed)  
- **Limiting weights**
  - Field-length-limited landing weight (**W\_LFL**)  
  - Brake-energy / temperature limited weight (**W\_LBE**)  
  - Structural / tire-speed-limited weight (**W\_LSTR** / W\_TIRE, if applicable)  
  - Go-around climb limited weight (**W\_GA**)  
- **Margins and flags**
  - Distance margin vs LDA (with appropriate regulatory factors)
  - Brake energy and temperature margin vs limits
  - Go-around climb gradient margin vs regulatory minima
  - Flags: “Landing allowed / not allowed”, “Contaminated runway – special procedures”, etc.

Outputs must include **units, model version, and validity flags**.

---

## 6. Algorithm Suite Overview

Each algorithm receives a common **input state vector** and returns outputs and diagnostics.  
Landing algorithms are identified as **ALG-LND-xx**.

### 6.1 ALG-LND-01 — VREF and VAPP Determination

Purpose: compute the **reference landing speed** and **approach speed** consistent with AFM criteria.

High-level logic:

1. Given W\_LDG, configuration, and CG:
   - Compute Vs\_LDG (stall speed in landing configuration).
2. Determine VREF:
   - VREF = k\_REF · Vs\_LDG (e.g. 1.23·Vs\_LDG, or AFM-specified formula).
3. Determine VAPP:
   - VAPP = VREF + additives (gust, wind, operational additives).
   - Enforce minimum and maximum VAPP boundaries.

Outputs:

- VREF, VAPP, additive breakdown  
- Applicable margins to stall, tail-strike, flap/gear limits.

### 6.2 ALG-LND-02 — Landing Distance Model (Dry/Wet/Contaminated)

Purpose: compute **required landing distance** (RLD) from 50 ft screen height to full stop (or to a defined speed).

Steps:

1. **Airborne segment**
   - From 50 ft to main-wheel touchdown:
     - Energy dissipation via aerodynamic drag and thrust idle.
     - Time and distance to touchdown.
2. **Ground roll**
   - Model deceleration due to:
     - Brakes (including antiskid modulation)
     - Aerodynamic drag (lift dump, spoilers, flaps)
     - Reverse thrust (credit as limited by regulations and AFM)
     - Rolling resistance and µ according to runway condition.
3. Integrate deceleration to obtain **distance to stop**.
4. Apply regulatory **factors**:
   - Dispatch factor (e.g. 1.67 or per regulations)
   - Operational / in-flight factors for “actual” landing.

Outputs:

- RLD\_DRY, RLD\_WET, RLD\_CONT for each configuration  
- Decomposition of contributions (airborne vs ground roll).

### 6.3 ALG-LND-03 — Field-Length-Limited Landing Weight (W_LFL)

Purpose: determine **maximum landing weight** that satisfies landing distance constraints for the selected runway and conditions.

Algorithm:

1. For trial W:
   - Compute VREF, VAPP (ALG-LND-01).
   - Compute required landing distance RLD for the given runway condition (ALG-LND-02).
2. Apply regulatory landing distance factors.
3. Check:
   - RLD\_factored ≤ LDA (or potential declared shorter distances).
4. Iterate on W until a maximum W is found that satisfies inequality.

Output:

- W\_LFL and associated distance margins.

### 6.4 ALG-LND-04 — Brake Energy / Temperature Limits (W_LBE)

Purpose: ensure that **brakes and wheels remain within energy and temperature limits** over the landing and possible rejected landing profile.

Algorithm:

1. Compute kinetic energy to be absorbed by brakes:
   - At touchdown (VTD ~ VREF / VAPP) → E\_brakes\_LDG
   - Include potential scenarios: go-around then subsequent landing, or long taxi etc. (as defined).
2. Use brake energy capacity curves vs speed, weight, and initial temperature.
3. Model **temperature rise** and post-landing cooling profile.
4. Determine maximum W such that:
   - E\_brakes ≤ E\_limit
   - T\_max ≤ T\_allowable (short-term & turn-around).

Outputs:

- W\_LBE  
- Constraints on brake cooling time / turn-around if relevant.

### 6.5 ALG-LND-05 — Structural / Tire-Speed Limits (W_LSTR / W_TIRE)

Purpose: enforce **structural and tire speed limits** for the landing.

Algorithm:

1. For given W and VAPP / VTD:
   - Compute maximum wheel speed at touchdown.
2. Check against:
   - Tire speed limits
   - Landing gear structural limits (sink rate, side load if modeled)
3. Determine maximum weight that keeps the landing within allowable limits.

Output:

- W\_LSTR and/or W\_TIRE, and margin to limits.

### 6.6 ALG-LND-06 — Go-Around / Missed Approach Performance (W_GA)

Purpose: ensure **go-around performance** from approach/landing configuration meets regulatory climb gradients.

Algorithm:

1. For each candidate W:
   - Compute go-around thrust / power available (incl. hybrid boost envelope).
   - Compute drag in go-around configuration (flaps/gear as per procedure).
2. Calculate go-around climb gradient:
   - γ\_GA(W) vs required γ\_req (OEI and AEO as applicable).
3. Determine maximum W such that γ\_GA ≥ γ\_req.

Output:

- W\_GA and associated climb gradient margins.

### 6.7 ALG-LND-07 — Hybrid Power & Regenerative Braking Constraints

Purpose: specifically address **hydrogen-electric / CO₂ battery aspects** relevant to landing performance.

Algorithm:

1. From landing profile and braking schedule:
   - Compute electrical power requirement for:
     - Brake-by-wire actuators, spoilers, flight controls
     - Any powered systems critical for deceleration.
2. Verify:
   - CO₂ battery and fuel-cell stacks can support these loads (voltage, current, SOC, temperature).
3. Model regenerative braking power:
   - Ensure regen power peak and energy do not exceed battery limits.
4. **No landing distance credit** is taken from regen alone; it is only used to:
   - Bound safe operation (no overvoltage/overcurrent)
   - Ensure energy balance and thermal margin.

Outputs:

- Pass/fail for **power-limited landing**  
- Maximum allowable regen profile and any operational notes.

---

## 7. Data Models and Interpolation

Required models:

- **Aero models**: CL, CD, CM vs α, Mach, flap, spoiler/gear state.  
- **Ground friction / µ models**: vs speed, contamination state, pressure, temperature.  
- **Brake models**: torque vs pressure, µ-brake vs temp, wear, and pressure.  
- **Propulsion models**: idle and reverse thrust vs altitude, OAT, Mach, prop setting.  
- **Energy system models**: battery and fuel-cell power limits vs SOC, temperature, time.

Implementation notes:

- Use **monotonic interpolation** where safety could be compromised by oscillations.  
- Explicit **bounds checking**: no extrapolation past certified envelope.  
- Model versioning:
  - Every dataset tagged with ID, origin (CFD, WT, flight test), and validity range.  
  - All versions logged into [TRACE.csv](./TRACE.csv).

---

## 8. Assumptions, Limitations, and Safety Margins

Examples (to be refined):

- **Wind credit**:
  - Limited headwind credit (e.g. ≤ 50% of steady headwind, no gust credit).
  - Tailwind penalties as per AFM; tailwind operations may be prohibited on contaminated runways.
- **Reverse thrust credit**:
  - Taken only when explicitly authorised in AFM / certification basis and possibly **restricted** for contaminated runways.
- **Runway condition assumptions**:
  - Use conservative µ-values for each reported condition (e.g. “WET”, “COMPACT SNOW”, “SLUSH”).
- **System availability**:
  - Minimum required configuration for performance credit (e.g. all spoilers functional, antiskid operative).
- **Thermal history**:
  - If previous landing/taxi data are not available, assume conservative initial brake temperature.

All assumptions and limitations must be clearly documented and **aligned with AFM** and the agreed certification basis.

---

## 9. Verification and Validation Strategy

Algorithm correctness will be shown via:

1. **Analytical checks**
   - Simplified test cases vs hand calculations.
   - Monotonicity checks (e.g. higher W → longer distance).

2. **Model vs Source Data**
   - Interpolation accuracy checks against underlying aero/brake/µ data.
   - Trends across envelope (no non-physical kinks).

3. **AFM Concordance**
   - Spot checks vs AFM landing distance tables and graphs.
   - Acceptable error bands (e.g. ±2–3% distance, ±2 kt VREF).

4. **Monte Carlo / Robustness**
   - Random sampling of inputs to detect discontinuities and failure modes.
   - Sensitivity to wind, µ, slope, and weight.

5. **Flight Test Correlation**
   - Progressive tuning of model vs measured landing distances and deceleration traces.
   - Documentation of updates in [CHANGES.md](./CHANGES.md) and [TRACE.csv](./TRACE.csv).

Detailed test cases and evidence will be maintained in **[VERIF.md](./VERIF.md)** and **[EVIDENCE/](./EVIDENCE/)**.

---

## 10. Interfaces and Implementation Notes

Algorithms will be used by:

- **EFB landing performance apps** (ATA 31)  
- **Dispatch / OCC tools**  
- **On-board monitoring and FDM** (for performance & safety analytics)  

Interface expectations:

- Stateless, deterministic APIs:
  - `landing_performance(inputs) → outputs, diagnostics`
- All numeric outputs to carry:
  - Units
  - Model/data version
  - Validity/quality flags (OK/WARNING/INVALID)

Logging:

- Log each operational computation:
  - Inputs (sanitized)
  - Outputs and margins
  - Model/data version
  - Limits hit or warnings

This supports **traceability** and **post-event investigation**, and feeds into **ATA 95** AI/NN traceability if ML-based landing prediction or monitoring functions are added.

---

## 11. Open Points / TODOs

- [ ] Freeze **landing distance factors** and methodology for dispatch vs in-flight (regulatory agreement).  
- [ ] Finalise **µ vs condition** lookup and contamination modeling approach.  
- [ ] Integrate **brake thermal model** with fleet monitoring for realistic initial temperatures.  
- [ ] Add **worked numerical examples** (dry vs wet vs contaminated case).  
- [ ] Define interface and boundaries with any **AI/NN-enhanced landing monitoring** (ATA 95), including deterministic fallback paths.  

---

_Editor’s note:_  
This is a **skeleton specification**. Engineering teams will refine each ALG-LND-xx section with full equations, pseudo-code, and explicit references to validated datasets as development progresses.
```
