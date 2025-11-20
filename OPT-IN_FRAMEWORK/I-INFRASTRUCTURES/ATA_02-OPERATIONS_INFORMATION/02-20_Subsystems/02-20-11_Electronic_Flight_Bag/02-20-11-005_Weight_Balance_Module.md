# 02-20-11-005 — EFB Weight & Balance Module

**Subsystem ID:** 02-20-11  
**Group:** [02-20_Subsystems](../README.md)  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Function:** Weight & Balance (W&B) Operational Module  
**Status:** OPERATIONAL  
**Version:** 1.0  

---

## 1. Purpose

This document specifies the **Weight & Balance (W&B) module** implemented in the AMPEL360 Electronic Flight Bag (EFB), covering:

- Real-time W&B computation  
- Integration with **02-20-12_Weight_Balance_Computer**  
- H₂-specific fuel mass, density, CG and boil-off considerations  
- CG envelope visualization  
- Crew workflow and operational constraints  
- AI-enhanced predictions (ATA 95)  
- Failure/fallback logic  

It complements:

- `02-20-11-001_EFB_Overview.md`  
- `02-20-12-001_WB_System_Overview.md`  

---

## 2. Scope

### Included
- CG envelope display and dynamic updates  
- Real-time readouts from ATA 28 fuel system and 02-20-12  
- H₂-specific compensations (density, boil-off, sequencing)  
- Crew W&B workflow for pre-flight and in-flight  
- Safety warnings and envelope exceedance logic  
- NN-based predictions from ATA 95 subsystem  

### Excluded
- Internal algorithms of 02-20-12  
- Tank management control (ATA 28)  
- Flight-control CG protections  

---

## 3. Architecture & Data Flow

```

```
               ┌──────────────────────────┐
               │   02-20-12 Weight &       │
               │   Balance Computer        │
               └───────────▲──────────────┘
                           │
                           │ CG, mass, envelope limits
                           │
```

┌─────────────────────────────┴────────────────────────────┐
│                EFB W&B MODULE (02-20-11)                 │
│                                                         │
│  ┌───────────────────────────────┐    ┌────────────────┐ │
│  │Aircraft State (ATA 42)        │    │Fuel System ATA │ │
│  │- Weight-on-wheels             │    │28 (H₂ levels)  │ │
│  │- Config                       │    │                │ │
│  └───────────────────────────────┘    └────────────────┘ │
│          │                                    │          │
│  ┌───────▼────────────────┐        ┌──────────▼────────┐ │
│  │Deterministic W&B calc  │        │ NN CG predictors   │ │
│  │Fallback algorithms     │◄──────►│ (ATA 95)           │ │
│  └───────────▲────────────┘        └──────────▲────────┘ │
│              │                                  │         │
│              └──────────────EFB UI Layer────────┘         │
└────────────────────────────────────────────────────────────┘

````

---

## 4. Required Inputs

### 4.1 From 02-20-12 (Primary Source)

| Parameter | Details |
|-----------|---------|
| ZFW / ZFWCG | Zero Fuel Weight + CG |
| TOW / TOWCG | Takeoff Weight + CG |
| LW / LWCG | Landing Weight + CG |
| Envelope limits | Forward / aft / lateral CG |
| Fuel sequencing | Active tank schedule |

---

### 4.2 From ATA 28 (Fuel System)

| Parameter | Purpose |
|-----------|---------|
| H₂ tank levels | Mass & CG estimation |
| Cryogenic temperature | Density calculation |
| Pressure | Health monitoring |
| Active tank | Sequencing impact |

---

### 4.3 From ATA 42 (Aircraft State)

- Weight-on-wheels (WOW)  
- Configuration state  
- A/C variant (Q80/Q100/Q120)

---

### 4.4 Crew Inputs

- Passenger count & seating  
- Cargo distribution  
- Special loads  
- Manual overrides (if enabled by operator policy)

---

## 5. Core W&B Features

### 5.1 Real-Time W&B Monitoring

Displayed continuously:

```yaml
wb_monitoring:
  zfw: kg
  zfw_cg: "% MAC"
  tow: kg
  tow_cg: "% MAC"
  lw: kg
  lw_cg: "% MAC"
  envelope_limits:
    fwd: 15
    aft: 35
    lat: ±2
````

Updated:

* Continuously when aircraft is on ground
* Every 1–5 seconds in flight
* Event-driven when H₂ tank sequencing changes

---

### 5.2 CG Envelope Visualization

Graphical representation includes:

* Current CG position
* Predicted CG at:

  * Takeoff
  * Top of climb
  * TOD
  * Landing
* Lateral CG indicator
* H₂ tank contribution overlays
* Safety margins highlighted

Failsafe color coding:

| Color      | Meaning                   |
| ---------- | ------------------------- |
| **Green**  | Within envelope           |
| **Yellow** | Approaching boundary      |
| **Red**    | Out of envelope (warning) |

---

### 5.3 Passenger & Cargo Management

Crew can:

* Enter passenger number per zone
* Assign seating automatically or manually
* Load cargo by compartment
* Add special loads (e.g. pets, dangerous goods)

Automatic checks performed:

* Zone weight limits
* Floor loading
* CG shift
* H₂-interaction effects (fuel sloshing prediction only if ATA 95 model available)

---

### 5.4 H₂-Specific Module

Unique to AMPEL360:

```yaml
h2_corrections:
  cryogenic_density:
    input: tank temperature, pressure
    method: lookup + NN density corrector
  boil_off_prediction:
    model: NN-BOILOFF-v1.0
    output: kg/hr
  cg_shift:
    model: NN-CG-PRED-v1.0
    effect: predicted CG drift from fuel movement
  sequencing_impact:
    source: 02-20-12
    advisory: yes
```

Warnings:

* Excessive boil-off
* Predicted out-of-envelope within X minutes
* Unbalanced tank sequencing

---

## 6. Operational Workflow

### 6.1 Pre-Flight (Before Engine Start)

1. Crew loads:

   * Passengers
   * Cargo
   * Special loads
2. EFB computes:

   * ZFW / ZFWCG
   * TOW / TOWCG
   * Predicted LW / LWCG
3. EFB displays:

   * Forward/aft envelopes
   * H₂ influence
4. Crew validates with dispatcher and signs digitally

---

### 6.2 Takeoff Review

* Final CG value frozen for performance calculations
* 02-20-11-004 references this CG value
* CAOS flags any mismatch between:

  * Dispatcher load sheet
  * EFB values
  * FDR inputs

---

### 6.3 In-Flight Monitoring

Displays:

* CG drift
* Tank sequencing
* Lateral imbalance
* Fuel transfer advisories

NN-enhanced predictions help avoid:

* Out-of-envelope CG
* Lateral imbalance exceeding ±2% MAC
* Unsafe sequencing during turbulence

---

## 7. Safety Warnings & Fallback Logic

### 7.1 Envelope Protection Alerts

| Condition               | Action                                |
| ----------------------- | ------------------------------------- |
| Approaching CG boundary | Yellow advisory                       |
| Exceeding CG            | Red warning + procedure reference     |
| Unbalanced tank         | Alert + reference to ATA 28 procedure |
| NN unavailable          | Use fallback deterministic algorithm  |

---

### 7.2 Fallback Implementation

Fallback triggers:

* No data from 02-20-12
* ATA 28 misalignment
* NN inference timeout
* Corrupted data

Fallback mode:

* Deterministic rules
* Simplified CG model
* Stripped UI
* No predictions

Logged via:

* `02-20-18_Operational_Data_Recording`
* CAOS anomaly channels

---

## 8. AI / NN Enhancements (ATA 95)

Models used:

```yaml
nn_models:
  cg_predictor: NN-CG-PRED-v1.0
  boiloff_predictor: NN-BOILOFF-v1.0
  lateral_balance_predictor: NN-LATBAL-v1.0
```

Enhancements:

* More accurate CG drift prediction
* Boil-off effect on W&B
* Real-time lateral balance estimation
* Prediction horizon: 2–20 minutes

---

## 9. Traceability

### Requirements

* RQ-02-11-WB-001 — EFB must display real-time W&B
* RQ-02-11-WB-002 — H₂ factors must be included
* RQ-02-11-WB-003 — CG envelope must be graphical
* RQ-02-11-WB-004 — NN predictions must be traceable

### Design

* `02-20-11-A-001_EFB_System_Architecture.svg`
* `02-20-12-A-001_WB_Architecture.drawio`

### Interfaces

* 02-20-12 Weight & Balance Computer
* ATA 28 H₂ Fuel System
* ATA 42 Avionics
* ATA 95 NN Runtime

---

## 10. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-11 Electronic Flight Bag
> **Function:** Weight & Balance Module
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Guidelines

| Version | Date       | Author               | Changes                      |
| ------- | ---------- | -------------------- | ---------------------------- |
| 1.0     | 2025-11-19 | AMPEL360 Digital Ops | Initial module specification |

```


