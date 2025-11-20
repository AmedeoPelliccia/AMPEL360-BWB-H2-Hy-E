
# 02-20-11-006 — EFB Weather Integration

**Subsystem ID:** 02-20-11  
**Group:** [02-20_Subsystems](../README.md)  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Function:** Weather Information Display & Prediction  
**Status:** OPERATIONAL  
**Version:** 1.0  

---

## 1. Purpose

This document describes the **weather information integration** capabilities of the AMPEL360 Electronic Flight Bag (EFB), including:

- Data sources (METAR/TAF, TAF, SIGMET, AIRMET, GRIB, satellite, radar)  
- Integration with the **02-20-17_Weather_Information_System**  
- AI-enhanced predictive turbulence via **ATA 95**  
- Weather overlays for navigation and performance planning  
- Pilot workflows, display modes, and advisories  
- Fallback and degraded modes  
- Logging and CAOS risk intelligence integration  

It complements:

- `02-20-11-001_EFB_Overview.md`  
- `02-20-17-001_Weather_System_Overview.md`  
- `02-20-11-004_Performance_Calculations.md`

---

## 2. Scope

### Included
- Weather display UI  
- Graphical layers and overlays  
- Weather → performance → W&B cross-integration  
- Predictive turbulence (NN-based)  
- Update frequencies and data quality logic  
- Crew alerts and operational guidance  

### Excluded
- Internal algorithm design of NN models (ATA 95)  
- Weather data ingestion architecture of the ground backend  
- Aircraft radar system (ATA 34)  

---

## 3. Weather Architecture Overview

```

┌──────────────────────────────────────────────────────────────┐
│                    EFB WEATHER MODULE                         │
│--------------------------------------------------------------│
│  ┌──────────────────────────┐   ┌───────────────────────────┐ │
│  │ Raw Weather Data         │   │ Predictive ML Models      │ │
│  │ (02-20-17)               │   │ (ATA 95)                  │ │
│  └──────────▲───────────────┘   └─────────▲────────────────┘ │
│             │                                 │               │
│  ┌──────────┴────────────┐        ┌──────────┴────────────┐ │
│  │ Weather Processing     │        │ Turbulence Predictor  │ │
│  │ Engine                 │◄──────►│ NN-WEATHER-PRED-v1.0 │ │
│  └──────────▲────────────┘        └──────────▲────────────┘ │
│             │                                 │               │
│         EFB UI (Maps, Layers, Advisories, Textual Data)      │
└──────────────────────────────────────────────────────────────┘

````

Primary sources provided by `02-20-17`:

- METAR / TAF  
- SIGMET / AIRMET  
- NOTAM-integrated weather (via Dispatch)  
- GRIB global model (winds aloft)  
- Satellite imagery  
- Radar mosaics  
- Lightning maps  
- Volcanic ash & convective storm alerts  

---

## 4. Weather Data Types & Update Frequency

### 4.1 Textual Weather

| Source | Frequency | Notes |
|--------|-----------|-------|
| **METAR** | Every 30–60 min | Auto-updates via backend |
| **TAF** | Every 6 hrs | With amendments |
| **D-ATIS** | On demand | If operator supports integration |
| **SIGMET/AIRMET** | Real-time | Turbulence/icing/storms |

---

### 4.2 Graphical Weather

| Type | Frequency | Layers |
|------|-----------|--------|
| Satellite IR | 30 min | Cloud tops, fronts |
| Radar mosaics | 5–10 min | Precipitation, storms |
| Winds aloft (GRIB) | 6 hr | Multi-level wind vectors |
| Icing risk | 15 min | Derived + predictive layer |
| Turbulence | 15 min | Derived + AI-enhanced layer |

---

### 4.3 Predictive Turbulence (ATA 95)

The EFB uses:

```yaml
ai_model:
  id: NN-WEATHER-PRED-v1.0
  purpose: turbulence prediction
  horizon: "15 minutes ahead"
  metrics:
    pod: 0.85
    far: 0.12
````

Capabilities:

* Predicts vertical & horizontal shear patterns
* Warns crew of **anticipated turbulence zones**
* Integrates with flight-planning and cruise-optimization modules

---

## 5. Display Modes

The EFB weather module supports three display tiers:

### 5.1 **Textual Mode**

* METAR/TAF raw text
* Highlighted critical conditions:

  * Low visibility
  * Strong crosswind
  * Windshear reports
  * Convective activity

### 5.2 **Graphical Mode (Map)**

Selectable overlays:

* Radar
* Turbulence (NN-enhanced)
* Winds aloft
* Icing layers
* Storm cells
* Cloud coverage
* Flight route (from planning module)
* Alternate airports

### 5.3 **Hybrid Mode**

Combined textual + graphical card:

* Surface weather + cross-section
* Vertical profiles along route
* Potential reroutes suggested by **02-20-15 Flight Planning**
* CAOS advisories visible as overlays

---

## 6. Route-Based Weather

### Route Integration

The EFB automatically overlays weather onto:

* Active flight plan (if available)
* Stored routes
* Dispatch releases

Includes:

* AIRMET/SIGMET along route corridor
* Predicted turbulence in the next 15 minutes
* Winds aloft impact on cruise optimization
* Weather hazards at destination and alternates

### Vertical Flight Profile

Displayed along distance axis:

* Temperature
* Wind barbs
* Turbulence probability
* Icing probability
* Top-of-climb and top-of-descent markers

---

## 7. Hydrogen-Specific Weather Considerations

Although weather doesn't directly affect hydrogen density, the module includes:

```yaml
h2_relevant_weather:
  extreme_temps:
    below_-40C: "alert — cryo system load increases"
  high_winds_on_ground:
    >35 kt: "refueling risk advisory"
  lightning:
    within_5km: "H₂ operations suspended"
  humidity_extremes:
    icing_interaction: true
```

These feed into:

* `02-20-21_H2_Operations_Management`
* Turnaround timelines (02-20-14)

---

## 8. CAOS Integration for Weather Risk

### CAOS provides the EFB with:

* Turbulence probability score (TPI)
* Weather-driven operational risk index
* Storm-track predictions
* Gate/ground-impact forecasts
* Causality links (weather → turnaround delays)

These appear as:

* Map overlays
* Banner warnings
* Predictive time-to-hazard

---

## 9. Safety Warnings & Operational Logic

### 9.1 Weather Alerts

| Condition             | Crew Action                 |
| --------------------- | --------------------------- |
| Severe turbulence     | Review altitudes or reroute |
| Icing conditions      | Apply anti-ice corrections  |
| Storm proximity       | Navigate around zones       |
| Crosswind above limit | Check OM-B procedures       |
| Low visibility        | Adjust landing minima       |

### 9.2 NN Failure Modes

If NN models are unavailable:

* Use deterministic turbulence sources
* Disable predictive layer
* Show “AI unavailable” banner
* Log event to operations recorder

---

## 10. Fallback Modes

### 10.1 Degraded Data Mode

Triggered by:

* Loss of 02-20-17 data link
* Backend outage
* Corrupted GRIB sources
* Partial satellite/radar coverage

Displayed to crew:

```
Weather Data Degraded — Some Layers Unavailable
```

Fallback layers:

* METAR/TAF only
* Cached satellite images (max 6 hr old)
* No turbulence prediction

---

### 10.2 Offline Mode

If no connectivity:

* Local cached weather
* Cached METAR/TAF up to 24 h old
* Warning displayed prominently

---

## 11. Traceability

### Requirements

* RQ-02-11-WX-001 — EFB must display textual weather
* RQ-02-11-WX-002 — EFB must support graphical layers
* RQ-02-11-WX-003 — Integration with NN turbulence prediction
* RQ-02-11-WX-004 — Weather must integrate with flight plan

### Design

* `02-20-11-A-001_EFB_System_Architecture.svg`
* `02-20-17-A-001_Weather_Architecture.drawio`

### Interfaces

* 02-20-17 Weather Information System
* ATA 34 avionics (optional)
* 02-20-15 Flight Planning
* 02-20-13 Performance Computer
* CAOS

---

## 12. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-11 — Electronic Flight Bag
> **Function:** Weather Integration
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author               | Changes                          |
| ------- | ---------- | -------------------- | -------------------------------- |
| 1.0     | 2025-11-19 | AMPEL360 Digital Ops | Initial weather integration spec |

```

---

