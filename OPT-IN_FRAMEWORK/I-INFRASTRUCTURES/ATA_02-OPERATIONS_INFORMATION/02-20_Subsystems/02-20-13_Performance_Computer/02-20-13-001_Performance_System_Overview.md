# 02-20-13-001 — Performance System Overview

**Subsystem ID:** 02-20-13  
**Group:** [02-20_Subsystems](../README.md)  
**Parent ATA:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Status:** FRAMEWORK_DEFINED  
**Version:** 1.0  

---

## 1. Purpose

This document provides the **high-level system overview** of the  
**AMPEL360 Performance Computer (02-20-13)**, including:

- Role and mission within AMPEL360 operations  
- High-level architecture and main components  
- Interfaces with other 02-20 subsystems and other ATA chapters  
- Deterministic vs AI/NN-enhanced computation paths  
- Safety, certification and traceability hooks  

It acts as the **entry point** for the more detailed performance specification:

- `02-20-13-002_Takeoff_Performance.md`  
- `02-20-13-003_Landing_Performance.md`  
- `02-20-13-004_Cruise_Optimization.md`  
- `02-20-13-005_NN_Performance_Predictor.md`  
- `02-20-13-006_BWB_Specific_Calculations.md`  

---

## 2. System Mission

The **Performance Computer** is the **authoritative engine** for:

- **Takeoff performance**:
  - V-speeds (V1/VR/V2)
  - Runway length required
  - Obstacle-limited field length
  - Engine-out climb gradients
- **Landing performance**:
  - VREF/VAPP
  - Landing distance required (LDR)
  - Braking profiles and contaminated runway logic
- **Climb, cruise and descent profiles**:
  - Optimal speeds and altitudes
  - Cost-index-based optimization
  - Hydrogen consumption profiles
- **BWB and H₂-specific corrections**:
  - Blended wing-body aerodynamics
  - Cryogenic hydrogen mass and CG effects

It serves:

- **Flight crew** via `02-20-11_Electronic_Flight_Bag`  
- **Dispatch and planning** via `02-20-15_Flight_Planning_Integration`  
- **CAOS / AirCCC** via `02-20-01_Digital_Ops_Platform`  
- **Predictive ops** via `02-20-23_Predictive_Operations_NN`  

---

## 3. Architectural Overview

### 3.1 Logical Architecture

See also:  
→ `ASSETS/02-20-13-A-001_Performance_Architecture.drawio`  
→ `ASSETS/02-20-13-A-002_Takeoff_Charts.svg`  

```text
                  ┌─────────────────────────────────┐
                  │   02-20-13 Performance Computer │
                  └───────────────┬─────────────────┘
                                  │
          ┌───────────────────────┼──────────────────────────┐
          │                       │                          │
          ▼                       ▼                          ▼
 ┌────────────────┐     ┌──────────────────┐        ┌──────────────────┐
 │ Deterministic  │     │  NN Integration  │        │   Data Services  │
 │ Algorithms     │◄───►│  Layer (ATA 95)  │◄──────►│ (APIs, Logging,  │
 │ (TO/LND/CRZ)   │     │  Perf Predictors │        │  CAOS, DPP, etc.)│
 └────────────────┘     └──────────────────┘        └──────────────────┘
````

### 3.2 Context Diagram

```text
          ┌───────────────────────────┐
          │ 02-20-11 EFB             │
          │ (Perf UI, crew-facing)   │
          └────────────▲─────────────┘
                       │
                       │ Perf requests & results
                       ▼
              ┌──────────────────────┐
              │ 02-20-13 Performance │
              │      Computer        │
              └─────────┬────────────┘
                        │
     ┌──────────────────┼─────────────────────┐
     │                  │                     │
     ▼                  ▼                     ▼
┌───────────┐   ┌───────────────┐     ┌──────────────┐
│ 02-20-12  │   │ 02-20-17 WX   │     │ ATA 42 / 28  │
│  W&B      │   │ Weather Sys   │     │ A/C State &  │
│ Computer  │   │               │     │ Fuel System  │
└───────────┘   └───────────────┘     └──────────────┘
```

---

## 4. Main Components

### 4.1 Deterministic Performance Engine

Defined in:

* `02-20-13-002_Takeoff_Performance.md`
* `02-20-13-003_Landing_Performance.md`
* `02-20-13-004_Cruise_Optimization.md`

Responsibilities:

* Implement **certification-grade algorithms** based primarily on:

  * AFM tables
  * Engineering aerodynamic/propulsion models
* Always available as **fallback** if NN layer is offline or out of envelope
* Supports all AMPEL360 variants (Q80/Q100/Q120) via config

### 4.2 NN Performance Integration Layer

Defined in:

* `02-20-13-005_NN_Performance_Predictor.md`

Responsibilities:

* Host / call **ATA 95 NN models** such as:

  * `NN-PERF-TAKEOFF-v1.0`
  * `NN-PERF-LDG-v1.0`
  * `NN-PERF-CRZ-v1.0`
* Combine NN corrections with deterministic results:

  * Drag polar corrections
  * Distance corrections
  * Fuel burn corrections
* Enforce:

  * Validity envelopes
  * Fallback and traceability

### 4.3 BWB/H₂ Correction Module

Defined in:

* `02-20-13-006_BWB_Specific_Calculations.md`

Responsibilities:

* BWB geometry corrections:

  * Ground effect
  * Flap/aileron mixed control effects
  * Non-conventional spanwise lift distribution
* H₂ integration:

  * Mass and CG effect on performance margins
  * Boil-off impacts in long loiter / extended ground times

### 4.4 Data Services & Integration

Exposes performance results to:

* `02-20-01_Digital_Ops_Platform` (API + events)
* `02-20-11_Electronic_Flight_Bag` (crew UI)
* `02-20-23_Predictive_Operations_NN` (for network modelling)
* CAOS / AirCCC for analytics

Also handles:

* Logging to `02-20-18_Operational_Data_Recording`
* DPP-relevant metadata (versions, hashes, model IDs)

---

## 5. Inputs & Outputs

### 5.1 Inputs

From `02-20-12_Weight_Balance_Computer`:

* ZFW, ZFWCG
* TOW, TOWCG
* LW, LWCG
* CG envelopes (forward, aft, lateral)

From `02-20-17_Weather_Information_System`:

* Winds (surface + aloft)
* Temperatures
* Icing levels
* Turbulence (deterministic + NN)

From ATA 42 / ATA 28 (via Digital Ops Platform):

* Runway data (length, slope, condition)
* Aircraft configuration (flaps/slats, anti-ice, etc.)
* Fuel mass/limits from H₂ system

From ops/dispatch (via 02-20-15 / 02-20-16):

* Planned route
* Alternate airports
* Payload / planned TOW

---

### 5.2 Outputs

To `02-20-11_Electronic_Flight_Bag`:

* V-speeds (TO & LND)
* Field/landing distances required
* Performance margins (%)
* Suggested speeds / altitudes / CI settings

To `02-20-15_Flight_Planning_Integration`:

* Profile fuel/time estimations
* Performance-limited weights
* Scenario-based “what-if” results

To `02-20-23_Predictive_Operations_NN` & CAOS:

* Performance capability descriptors:

  * Available margins
  * Climbs achievable
  * Contaminated runway effect factors

To logging / DPP:

* Computation context (input set, version, model IDs)
* Hashes of tables / model parameters used

---

## 6. Deterministic vs NN-Enhanced Paths

### 6.1 Deterministic Path

* Always present, always the **certification baseline**
* Derived from AFM data and engineering models
* Used when:

  * NN disabled or not available
  * Inputs out of NN validation envelope
  * Data quality issues (sensors or weather inputs)

### 6.2 NN-Enhanced Path

Handled via `02-20-13-005_NN_Performance_Predictor.md`:

* Uses fleet data to refine:

  * Distance, speed, fuel flow predictions
  * BWB/H₂ coupling phenomena not fully captured in AFM
* Marked as **advisory improvement**, not authoritative override
* Must:

  * Log predictions and errors
  * Provide explanation and uncertainty bounds (via ATA 95 guidance)

### 6.3 Fallback Logic

If any of the following occurs:

* NN runtime unavailable
* Model version mismatch
* Input out-of-scope
* Self-check failure or drift detection

Then:

* System reverts to **pure deterministic** performance
* EFB is notified (icon / label)
* Event logged to `02-20-18_Operational_Data_Recording`

---

## 7. Integration with Other Subsystems

### 7.1 With 02-20-11 EFB

* EFB acts as **primary UI**, Performance Computer as **backend**
* For each performance request:

  * EFB sends context: airport, runway, config, contingency
  * 02-20-13 returns structured response:

    * Speeds, distances
    * Margins and notes
    * Flags if NN-augmented

### 7.2 With 02-20-12 W&B

* WBC is **authoritative** for TOW/ZFW/LW/CG
* Performance Computer:

  * Refuses to compute if CG out of envelope (unless “emergency mode” procedures)
  * Provides margins conditioned on W&B status

### 7.3 With 02-20-17 Weather

* Performance depends strongly on:

  * Headwind/tailwind, crosswind
  * Temperature
  * Runway contamination from weather

* For advanced cases:

  * 02-20-17 passes predictive turbulence/wind scenarios
  * Performance Computer can compute ranges of outcomes

### 7.4 With 02-20-23 Predictive Ops NN

* Performance envelopes help CAOS/02-20-23 to:

  * Estimate delay risks tied to performance constraints
  * Evaluate rerouting options
  * Model payload-restriction impacts

---

## 8. Safety & Certification Overview

A deeper safety case is expected in a dedicated cert package, but at overview level:

* **Safety relevance:**

  * Incorrect performance output can cause:

    * Overrun
    * Tailstrike
    * Inadequate climb performance

* **Target SW level:**

  * Likely **DO-178C DAL B or C** (to be confirmed with authority)

* **Assurance principles:**

  * Deterministic core is *certification anchor*
  * NN-enhanced outputs are:

    * Advisory
    * Fully traceable
    * Subject to strict fallback logic

* **Evidence references (planned):**

  * `ASSETS/Certification/02-20-13-A-501_Performance_DO-178C_Evidence.pdf` (placeholder)
  * `ASSETS/Model_Cards/02-20-13-A-101_Performance_NN_v1.0.yaml`

---

## 9. Traceability Skeleton

### 9.1 Requirements (examples / placeholders)

* RQ-02-13-001 — System shall compute takeoff performance for all certified runways and configurations.
* RQ-02-13-002 — System shall compute landing performance including contaminated runway cases.
* RQ-02-13-003 — System shall support cruise profile optimization considering hydrogen fuel.
* RQ-02-13-004 — Any NN-enhanced result shall have deterministic fallback and traceability to ATA 95.

### 9.2 Design Artefacts

* `ASSETS/02-20-13-A-001_Performance_Architecture.drawio`
* `02-20-13-002_Takeoff_Performance.md`
* `02-20-13-003_Landing_Performance.md`
* `02-20-13-004_Cruise_Optimization.md`
* `02-20-13-005_NN_Performance_Predictor.md`

### 9.3 Interfaces

* 02-20-11 EFB
* 02-20-12 W&B Computer
* 02-20-17 Weather Information System
* 02-20-23 Predictive Operations NN
* ATA 42, ATA 28, ATA 95

---

## 10. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-13 Performance Computer
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                         | Changes                          |
| ------- | ---------- | ------------------------------------- | -------------------------------- |
| 1.0     | 2025-11-19 | AMPEL360 Digital Ops & Performance WG | Initial performance overview doc |

```


