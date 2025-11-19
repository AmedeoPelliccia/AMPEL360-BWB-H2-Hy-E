# 02-20-11-004 — EFB Performance Calculations

**Subsystem ID:** 02-20-11  
**Group:** [02-20_Subsystems](../README.md)  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Function:** EFB Performance Module (UI + AI-enhanced backend)  
**Status:** OPERATIONAL  
**Version:** 1.0  

---

## 1. Purpose

This document defines the **performance calculation function** implemented in the AMPEL360 Electronic Flight Bag (EFB), including:

- Takeoff / landing performance capabilities  
- Cruise and climb/descent optimization  
- Ground-effect and BWB-specific corrections  
- Hydrogen-fuel-specific constraints  
- Integration with the **Performance Computer (02-20-13)**  
- AI-enhanced predictions via **ATA 95 Neural Networks**  
- Fallback logic and operational safety boundaries  
- Interaction with other cockpit subsystems  

It complements:

- `02-20-11-001_EFB_Overview.md`  
- `02-20-11-002_Class_3_EFB_Implementation.md`  
- `02-20-13-001_Performance_System_Overview.md`  

---

## 2. Scope

### Included
- Performance calculation UI (EFB front-end)  
- Local deterministic algorithms (fallbacks)  
- Integration with 02-20-13 Performance Computer  
- NN-enhanced modules (ATA 95 models)  
- Output presentation, limitations, and warnings  
- Aircraft configuration inputs and H₂-fuel constraints  

### Excluded
- Internal design of NN models (`ATA 95`)  
- Internal flight-control-level performance algorithms  
- Low-level avionics data-handling (ATA 42)  

---

## 3. Performance Module Architecture

```

┌───────────────────────────────────────────────────────────────┐
│                     EFB PERFORMANCE MODULE                     │
│                                                               │
│  ┌──────────────┐     ┌──────────────────┐     ┌───────────┐ │
│  │  Deterministic│     │ Performance API  │     │  NN Models│ │
│  │  Algorithms   │◄───►│  (02-20-13)      │◄───►│ (ATA 95)  │ │
│  └──────────────┘     └──────────────────┘     └───────────┘ │
│            ▲                         ▲                       │
│            │                         │                       │
│       EFB UI Layer             Aircraft Data                │
│            │               (via ATA 42 IMA / WiFi)           │
└────────────┴─────────────────────────────────────────────────┘

````

Main integration points:

| Source | Data | Frequency |
|--------|------|-----------|
| ATA 42 | airspeed, altitude, TAT, config | 1–10 Hz |
| 02-20-13 | computed performance values | On demand |
| ATA 95 | AI-enhanced predictions | On demand |
| 02-20-12 | CG / weight & balance | Continuous |

---

## 4. Inputs & Required Data

### 4.1 Aircraft State Inputs (via ATA 42)

| Parameter | Use |
|----------|-----|
| Weight on wheels | TO/LND mode logic |
| TAT / SAT | Air density |
| Pressure altitude | ISA deviation |
| Airspeed | Flap/slat logic |
| A/C configuration | Surfaces, spoilers |

---

### 4.2 Environmental Inputs

| Source | Data |
|--------|------|
| METAR/TAF | Wind, temp, QNH |
| Weather system (02-20-17) | Icing probability, turbulence |
| Runway database | Length, slope, surface |

---

### 4.3 Airframe Configuration Inputs

| Parameter | Purpose |
|----------|---------|
| Flap/slat setting | TO/LND speeds |
| Engine/propulsor mode | Performance margin |
| Anti-ice ON/OFF | Corrections |
| CG position | Speed corrections |
| H₂ fuel mass | Weight & balance |

---

## 5. Performance Calculation Types

### 5.1 Takeoff Performance

Computed parameters:

```yaml
takeoff:
  speeds:
    V1: computed
    VR: computed
    V2: computed
  runway_required:
    dry: meters
    wet: meters
    contaminated: meters
  obstacle_clearance:
    screen_height: 35 ft
  risk_controls:
    - runway length check
    - slope adjustments
    - density altitude effects
    - icing penalties
  ai_enhancement:
    model: NN-PERF-TAKEOFF-v1.0
    improves:
      - ground effect modeling (BWB)
      - low-speed aerodynamic prediction
      - crosswind sensitivity
    accuracy_gain: "~3.5% reduction in modeled error"
````

---

### 5.2 Landing Performance

```yaml
landing:
  speeds:
    VREF: computed
    VAPP: computed
  runway_required:
    dry: meters
    wet: meters
  braking_action:
    - normal
    - degraded
    - autobrake profiles
  ai_enhancement:
    model: NN-PERF-LDG-v1.0
    capabilities:
      - touchdown-point prediction
      - flare distance estimation
    accuracy_gain: "~2.1% typical"
```

---

### 5.3 Climb / Cruise / Descent Optimization

```yaml
cruise_optimization:
  objectives:
    - minimize H₂ consumption
    - minimize time
    - minimize cost index
  outputs:
    - optimal altitude
    - optimal cruise Mach
    - step-climb schedule
  ai_enhancement:
    model: NN-PERF-CRZ-v1.0
    capabilities:
      - learned drag polar corrections
      - dynamic H₂ boil-off impact
      - predictive turbulence avoidance
```

---

### 5.4 BWB-Specific Corrections

Because AMPEL360 is a **blended-wing-body**, the EFB includes:

* Low-speed ground-effect correction
* BWB flap/lift curve behavior
* Pitch-to-speed sensitivity
* High-bank-angle drag rise
* Coupled CG/tank-sequencing effects (from `02-20-12`)

These are provided by:

* Deterministic models from 02-20-13
* NN compensators from ATA 95

---

## 6. Hydrogen-Specific Performance Considerations

The EFB module includes special logic for **H₂ mass, density and boil-off**.

```yaml
h2_performance_corrections:
  boil_off_rate_prediction:
    source: NN-BOILOFF-v1.0
  cryogenic_density:
    source: ATA 28 sensors + 02-20-12 conversion table
  cg_shift_prediction:
    source: 02-20-12 + NN-CG-PRED-v1.0
  impact_on_takeoff_weight:
    dynamic: true
```

The EFB alerts crew when:

* H₂ mass is near structural limit
* CG envelope near limits
* Predicted boil-off affects TO/LND performance

---

## 7. Output & Presentation in the EFB

Outputs are standardized across all AMPEL360 variants.

### 7.1 Performance Summary Block

```
Takeoff RWY: 25L
Wind: 270/12G20  OAT: 31°C  QNH: 1009 hPa

V1   132 kt
VR   137 kt
V2   143 kt
Runway Required: 1780 m (dry)
Performance Margin: +12.5%
```

### 7.2 Risk Indicators

* **Yellow** → performance margin < 10%
* **Red** → insufficient runway
* **Blue** → AI-enhanced prediction used

### 7.3 CAOS Integration

Displays:

* Turbulence ahead (via NN-WEATHER-PRED)
* Turnaround delays affecting performance planning
* Operational risk advisories

---

## 8. AI / NN Integration (ATA 95)

The EFB uses the following models:

```yaml
nn_models_used:
  - NN-PERF-TAKEOFF-v1.0
  - NN-PERF-LDG-v1.0
  - NN-PERF-CRZ-v1.0
  - NN-WEATHER-PRED-v1.0
  - NN-BOILOFF-v1.0
  - NN-CG-PRED-v1.0
```

NN models are accessed through:

* `02-20-13` Performance Computer API
* Shared inference runtime (ATA 95 subsystem)

Fallback modes:

* Deterministic model only
* Table-lookup mode
* Minimum feature mode (if essential inputs missing)

Fallback logic is fully described in:
→ `02-20-11-009_Safety_and_Certification.md`

---

## 9. Failure Modes & Warnings

### 9.1 Failure Detection

* Missing ATA 42 data
* Invalid runway data
* NN inference timeout
* Integrity violation of input data
* Extreme conditions (beyond validation envelope)

### 9.2 Crew Warnings

| Condition              | Action                                |
| ---------------------- | ------------------------------------- |
| Missing NN model       | Use deterministic fallback            |
| Out-of-envelope inputs | Alert + block performance calculation |
| Runway insufficient    | Red warning                           |
| H₂ CG shift risk       | Advisory + recheck of 02-20-12        |

### 9.3 Logging

All failures are logged to:
→ `02-20-18_Operational_Data_Recording`
→ CAOS risk-learning channels

---

## 10. Traceability

### Requirements

* RQ-02-11-PERF-001 — EFB must compute TO/LND performance
* RQ-02-11-PERF-002 — EFB must integrate with 02-20-13
* RQ-02-11-PERF-003 — H₂ corrections must be included
* RQ-02-11-PERF-004 — AI/NN predictions must be traceable and fallback-capable

### Design

* 02-20-11-A-001 System Architecture
* 02-20-13-A-001 Performance Architecture

### Interfaces

* ATA 42 avionics data
* 02-20-13 Performance Computer
* 02-20-12 Weight & Balance
* ATA 95 NN Models
* 02-20-17 Weather

---

## 11. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-11 Electronic Flight Bag — Performance Module
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author               | Changes                                  |
| ------- | ---------- | -------------------- | ---------------------------------------- |
| 1.0     | 2025-11-19 | AMPEL360 Digital Ops | Initial performance module specification |

```

`

o directamente las **ASSETS**/diagramas correspondientes.
```
