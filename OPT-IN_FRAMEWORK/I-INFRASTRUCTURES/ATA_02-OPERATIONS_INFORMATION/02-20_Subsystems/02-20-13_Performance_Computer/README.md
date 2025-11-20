# 02-20-13 — Performance Computer

**Subsystem ID:** 02-20-13  
**Group:** [02-20_Subsystems](../README.md)  
**Parent ATA:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Status:** ACTIVE  
**Owner:** Digital Operations & Aircraft Performance Domain  
**Version:** 1.0  

---

## 1. Purpose

The **Performance Computer** is the **authoritative computation engine** for all  
AMPEL360 **aircraft performance calculations**, providing:

- **Takeoff performance** (V-speeds, runway requirements, obstacle clearance)  
- **Landing performance** (distances, braking, contaminated runway logic)  
- **Climb, cruise and descent optimization** (including cost index logic)  
- **BWB-specific performance corrections** for the AMPEL360 blended wing body  
- **H₂-specific performance constraints**, via integration with W&B and ATA 28  
- **AI/NN-enhanced predictions** (ATA 95), with deterministic fallback

It serves as the **backend for EFB performance modules** and as a core service for  
ops, dispatch and CAOS analytics.

---

## 2. Scope

### Included

- Core algorithms for:
  - Takeoff, landing, climb, cruise, descent  
  - Limit checks (runway, gradients, brake energy, etc.)  
- H₂ and BWB-specific performance modelling  
- Interfaces to:
  - `02-20-11_Electronic_Flight_Bag`  
  - `02-20-12_Weight_Balance_Computer`  
  - `02-20-17_Weather_Information_System`  
  - `02-20-23_Predictive_Operations_NN`  
  - ATA 42 (aircraft state) via platform  
- Deterministic + NN-enhanced calculation paths  
- Test harnesses and validation datasets  

### Excluded

- Flight-control law logic (handled under ATA 27/95 where relevant)  
- AFM editorial content (tables, charts – referenced as input)  
- Detailed AI/NN safety case (managed under ATA 95)  

---

## 3. Directory Structure

```text
02-20-13_Performance_Computer/
├── README.md                                  ← You are here
│
├── 02-20-13-001_Performance_System_Overview.md    # High-level overview
├── 02-20-13-002_Takeoff_Performance.md           # TO performance algorithms
├── 02-20-13-003_Landing_Performance.md           # LND performance algorithms
├── 02-20-13-004_Cruise_Optimization.md           # Cruise / CI / profiles
├── 02-20-13-005_NN_Performance_Predictor.md      # AI/NN integration layer
├── 02-20-13-006_BWB_Specific_Calculations.md     # BWB- and H₂-specific models
│
├── ASSETS/
│   ├── 02-20-13-A-001_Performance_Architecture.drawio
│   ├── 02-20-13-A-002_Takeoff_Charts.svg
│   ├── 02-20-13-A-003_NN_Integration.svg
│   └── Model_Cards/
│       └── 02-20-13-A-101_Performance_NN_v1.0.yaml
│
└── TEST_DATA/
    ├── 02-20-13-T-001_TO_RunwayCases.json
    ├── 02-20-13-T-002_LDG_DistanceCases.json
    ├── 02-20-13-T-003_Cruise_Profiles.json
    └── 02-20-13-T-004_BWB_Corrections.json
````

*(TEST_DATA es sugerido; puedes adaptarlo a tu patrón real de pruebas.)*

---

## 4. System High-Level Description

The Performance Computer:

* Implements the **reference performance model** for AMPEL360 variants
* Is **traceable to AFM performance data** and certification analyses
* Provides **APIs** to EFB, dispatch, CAOS and external tools via:

  * `02-20-01_Digital_Ops_Platform` (REST/events)
* Supports both:

  * **Deterministic** (classical) algorithms
  * **NN-enhanced** models for improved accuracy and robustness

It is designed for:

* Onboard usage (via EFB)
* Ground-side computations (e.g., dispatch, what-if analysis)
* CAOS scenario analysis and optimization studies

---

## 5. Key Functional Capabilities

### 5.1 Takeoff Performance

Detailed in: `02-20-13-002_Takeoff_Performance.md`

* V1 / VR / V2 calculation
* Runway length required (dry, wet, contaminated)
* Field length and obstacle-limited performance
* Engine-out climb gradients
* BWB-specific low-speed aerodynamics
* H₂ mass / CG influence via 02-20-12

### 5.2 Landing Performance

Detailed in: `02-20-13-003_Landing_Performance.md`

* VREF / VAPP
* Landing distance required (LDR)
* Braking action and autobrake profiles
* Contaminated runway case handling
* Reverse thrust and configuration penalties

### 5.3 Climb / Cruise / Descent Optimization

Detailed in: `02-20-13-004_Cruise_Optimization.md`

* Climb schedules (speed/Mach profiles)
* Cruise altitude selection (including cost index)
* Descent profiles (idle / continuous descent)
* H₂ consumption profiles and optimum trajectories
* Integration with 02-20-17 Weather & 02-20-23 Predictive Ops

### 5.4 BWB & H₂-Specific Modelling

Detailed in: `02-20-13-006_BWB_Specific_Calculations.md`

* BWB drag polars
* Ground effect for blended geometry
* Non-conventional flap systems
* H₂ mass and CG feedback into performance
* Boil-off impact on TOW and climb margins

### 5.5 NN-Enhanced Performance

Detailed in: `02-20-13-005_NN_Performance_Predictor.md`

* Uses ATA 95 models (e.g., `NN-PERF-CALC-v1.0`)
* Corrections to:

  * Drag polars
  * Takeoff and landing distances
  * Turbulence and wind impact
* Always with **deterministic fallback** and full traceability

---

## 6. Interfaces

### 6.1 To EFB (02-20-11)

* Takeoff / landing performance results for:

  * `02-20-11-004_Performance_Calculations.md`
* Validated speeds and margins
* Advisory labels when NN enhancement is active

### 6.2 To W&B Computer (02-20-12)

* Input from WBC:

  * TOW, LW, CG, ZFW, envelopes
* Performance responds to:

  * Out-of-envelope CG scenarios
  * H₂ tank-driven CG drifts

### 6.3 To Weather System (02-20-17)

* Ingests:

  * Winds aloft
  * Temperature profiles
  * Icing layers
  * Turbulence predictions
* Outputs:

  * Adjusted performance margins
  * Recommended profiles (altitude, route segments)

### 6.4 To Predictive Ops (02-20-23)

* Provides:

  * Performance margins and constraints
  * Aircraft-specific capabilities under conditions
* Consumes:

  * Delay and turnaround risk predictions
  * Scenario-level constraints for CAOS simulations

### 6.5 To ATA 95 (Neural Networks)

* Consumes NN models defined in ATA 95
* Reports:

  * Model usage
  * Error statistics
  * Drift indicators

---

## 7. Safety & Certification

The Performance Computer is **safety-significant**:

* Provides data critical to:

  * Takeoff decision making
  * Landing performance viability
  * Fuel and alt strategy
* Likely **DO-178C DAL B or C** (subject to authority agreement), since performance errors can lead to safety events.

Evidence and safety arguments will live in a dedicated cert package (e.g.):

* `ASSETS/Certification/02-20-13-A-501_Performance_DO-178C_Evidence.pdf` *(placeholder)*

The Performance Computer must:

* Be **fully traceable** to AFM performance data
* Support **configuration control** across aircraft variants
* Provide **robust fallback** if NN models are unavailable

---

## 8. Dependencies & Cross-References

### Internal (02-20)

* `../02-20-00-001_Subsystems_Overview.md`
* `../02-20-00-002_Subsystems_Integration_Map.md`
* `../02-20-00-004_CAOS_Operations_Integration.md`
* `../02-20-11_Electronic_Flight_Bag/`
* `../02-20-12_Weight_Balance_Computer/`
* `../02-20-17_Weather_Information_System/`
* `../02-20-23_Predictive_Operations_NN/`

### Other ATA Chapters

* ATA 28 — H₂ fuel system (mass & limitations)
* ATA 42 — IMA / avionics (aircraft state inputs)
* ATA 95 — Neural networks / performance models
* ATA 31 — Recording (for performance data logging and post-flight analysis)

---

## 9. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-13 Performance Computer
> **Maintainer:** Digital Ops & Performance Group
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                         | Notes                    |
| ------- | ---------- | ------------------------------------- | ------------------------ |
| 1.0     | 2025-11-19 | AMPEL360 Digital Ops & Performance WG | Initial subsystem README |


::contentReference[oaicite:0]{index=0}
```
