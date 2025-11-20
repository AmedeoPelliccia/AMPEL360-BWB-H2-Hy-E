# 02-20-11-007 — Charts & Navigation Data

**Subsystem ID:** 02-20-11  
**Group:** [02-20_Subsystems](../README.md)  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Function:** Charts, Maps & Navigation Data Module  
**Status:** OPERATIONAL  
**Version:** 1.0  

---

## 1. Purpose

This document defines the **Charts & Navigation Data module** of the AMPEL360 Electronic Flight Bag (EFB), including:

- Chart types supported (terminal, enroute, airport diagrams, terrain maps, overlays)  
- Navigation data cycle management (AIRAC)  
- Integration with weather, performance, W&B, and CAOS  
- Jeppesen/Navigraph data ingestion  
- Rendering pipeline and HF considerations  
- Safety limits, fallback, and currency validation  

It complements:

- `02-20-11-001_EFB_Overview.md`  
- `02-20-11-006_Weather_Integration.md`  
- `02-20-11-004_Performance_Calculations.md`  

---

## 2. Scope

### Included

- Display and interaction with all operationally-relevant charts  
- AIRAC cycle handling (28-day cycle)  
- Overlays: weather, terrain, aircraft state  
- Georeferenced aircraft symbol (optional)  
- Integration with all flight phases  
- CAOS-driven operational hints  

### Excluded

- Internal provider formats (Jeppesen/Navigraph proprietary structures)  
- Avionics-level navigation databases (managed under ATA 42)  
- Airline back-end content management  

---

## 3. Chart Types Supported

### 3.1 Terminal Charts

- SID (Standard Instrument Departure)  
- STAR (Standard Terminal Arrival Route)  
- IAP (Instrument Approach Procedure):  
  - ILS, RNAV, RNP AR, VOR, NDB, GLS  
- Transition altitudes and restrictions  
- Noise abatement profiles  

### 3.2 Airport / Ground Charts

- Airport taxi diagrams  
- Hotspot markings  
- Runway incursion warnings  
- Parking stands and gate assignment compatibility  
- H₂ refueling zones (AMPEL360-specific)  

### 3.3 Enroute Charts

- Airways (low/high)  
- Waypoints, NAVAIDs  
- FIR/UIR boundaries  
- Terrain awareness shading  
- Grid MORA values  

### 3.4 Synthetic Charts (On-Device Rendering)

- Terrain elevation model (DEM-based)  
- Weather overlays (METAR/TAF, satellite, turbulence)  
- CAOS operational overlays (predictive hazards)  
- NOTAM visualization (graphical pins)  

---

## 4. Navigation Data

### 4.1 AIRAC Cycle

EFB handles 28-day AIRAC updates:

```yaml
nav_data:
  provider: "Jeppesen or Navigraph"
  cycle_length: "28 days"
  current_cycle: "2025-11-28"
  next_cycle: "2025-12-26"
  update_method: 
    - ground_wifi
    - delta_updates
  verification:
    - signature_check
    - checksum_sha256
````

If nav data is **out of date**, EFB issues:

* Yellow advisory if <1 cycle overdue
* Red operational block if >1 cycle overdue (per operator policy)

---

## 5. Rendering Pipeline & Architecture

### 5.1 Data Flow

```
   Provider Data (Encrypted Packages)
                │
                ▼
       Digital Ops Platform (02-20-01)
                │
                ▼
             EFB Device
                │
╔════════════════════════════════════╗
║ EFB Charts & Navigation Module     ║
║                                    ║
║ • Vector charts (Jepp/NVG)         ║
║ • Raster fallback                  ║
║ • Weather overlays (02-20-17)      ║
║ • Aircraft position (ATA 42)       ║
║ • CAOS alerts (02-20-01)           ║
╚════════════════════════════════════╝
```

### 5.2 Rendering Capabilities

* Vector rendering at 60 FPS (zoom/pan)
* Geo-referenced overlays
* Terrain gradient shading
* Dynamic text scaling
* Multi-layered maps (stacked order):

  1. Base chart
  2. Terrain
  3. Weather
  4. NOTAMs
  5. CAOS advisories
  6. Aircraft symbol

---

## 6. Overlays

### 6.1 Weather Overlays (via 02-20-17)

* Radar composite
* Winds aloft
* Icing probability layers
* Turbulence prediction (NN-based)
* Satellite IR
* Storm cells with predictive vectors

### 6.2 Terrain Overlays

* DEM-derived shading
* Contours
* Minimum Safe Altitudes
* Off-route obstruction buffers

### 6.3 NOTAM Overlays

* Graphical icons
* Text popup
* Relevance filter (route, altitude, area of interest)
* Automatic expiration
* Validity cross-check with nav cycle

### 6.4 CAOS Overlays

From Digital Ops Platform (02-20-01):

* Predictive hotspots (e.g., congestion, gate changes)
* Crew workload advisories
* Crosswind alerts
* Runway occupancy predictions

CAOS data is always **advisory**, never authoritative.

---

## 7. Aircraft Position Display

* Uses GNSS/IRS position via ATA 42 (read-only)
* High-rate update: 1–5 Hz
* Position smoothing applied
* HF considerations:

  * Aircraft symbol never obscures relevant minima
  * Contrast modes: day/night/low brightness

Operator may enable or disable georeferencing based on approval.

---

## 8. Interaction Model (HF-Compliant)

### 8.1 Gesture-Based Interaction

* Two-finger zoom
* One-finger pan
* Double-tap “fit to screen”
* Long-press tooltips on symbols
* Reliable under turbulence (gesture filtering)

### 8.2 Quick Filters

* Weather on/off
* Terrain on/off
* NOTAMs
* CAOS overlays
* Alternate runways/approaches

### 8.3 Phase-of-Flight Adaptation

* Taxi phase → airport chart auto-open
* Takeoff → SID selected
* Cruise → enroute
* Descent → STAR / IAP
* Landing → airport + runway depiction

This is configurable per operator.

---

## 9. Integration with Other Subsystems

### 9.1 Performance Module (02-20-11-004)

* Displays runway length, obstacles, slope
* Merges performance margins onto airport chart
* Highlights contaminated runway segments

### 9.2 W&B Module (02-20-11-005)

* Used to verify runway suitability
* CG limits may influence recommended runway/approach

### 9.3 Weather System (02-20-17)

* Weather overlays (radar, turbulence)
* Predictive storm tracks

### 9.4 Flight Planning System (02-20-15)

* Synchronizes route
* Displays alternates and ETOPS points
* AOC updates can trigger re-render

### 9.5 ATA 95 NN Models

Used indirectly via 02-20-17 or 02-20-23 modules:

* Predictive turbulence model
* Predictive NOTAM clustering
* Route-relevance ranking

---

## 10. Safety Boundaries & Fallback

### 10.1 Fallback Modes

* Raster charts only (if vector parsing fails)
* No georeferencing (if ATA 42 data invalid)
* No weather overlays (if weather system offline)
* No CAOS overlays (if not validated)

### 10.2 Failure Detection

Detected errors include:

* Broken or missing chart package
* AIRAC mismatch
* Failed checksum
* Corrupted layer
* Out-of-date navigation cycle

### 10.3 Crew Warnings

| Condition              | Severity  | EFB Action                 |
| ---------------------- | --------- | -------------------------- |
| AIRAC out-of-date      | Yellow    | Advisory                   |
| >1 cycle overdue       | Red       | Block navigation mode      |
| Missing airport charts | Red       | Alert + fallback reference |
| Vector engine fail     | Yellow    | Switch to raster           |
| CAOS advisory invalid  | No hazard | Hide overlay               |

---

## 11. Traceability

### Requirements

* RQ-02-11-CHART-001 — Display all required operational charts
* RQ-02-11-CHART-002 — Georeferenced aircraft symbol (if approved)
* RQ-02-11-CHART-003 — Weather & CAOS overlays
* RQ-02-11-CHART-004 — AIRAC cycle management

### Design References

* 02-20-11-A-002_EFB_System_Architecture.svg
* 02-20-17-A-002_Data_Flow.svg

### Interfaces

* 02-20-01 Digital Ops Platform
* 02-20-17 Weather Information System
* 02-20-15 Flight Planning Integration
* ATA 42 IMA system

---

## 12. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-11 Electronic Flight Bag
> **Function:** Charts & Navigation Module
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author               | Changes               |
| ------- | ---------- | -------------------- | --------------------- |
| 1.0     | 2025-11-19 | AMPEL360 Digital Ops | Initial specification |

```


Solo dime cuál seguimos.
```
