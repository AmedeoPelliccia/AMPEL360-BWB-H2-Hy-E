# 02-20-11-001 — Electronic Flight Bag (EFB) Overview

**Subsystem ID:** 02-20-11
**Group:** [02-20_Subsystems](../README.md)
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)
**Axis:** I — Infrastructures
**Status:** OPERATIONAL
**Version:** 3.2

---

# 1. Purpose

This document provides the **complete technical and operational overview** of the
AMPEL360 **Electronic Flight Bag (EFB)** subsystem, including:

* Functional scope & mission role
* Technical architecture (HW + SW)
* Operational capabilities
* AI/NN-enhanced modules (ATA 95 linkage)
* CAOS & Digital Ops Platform integration
* Certification baseline
* Traceability, DPP embedding, and version governance

The EFB is the **primary digital interface** for AMPEL360 flight crew and a core
component of the aircraft’s digital operations ecosystem.

---

# 2. Scope

## Included

* Class 3 / Portable EFB configuration
* Flight crew operational applications
* Integration with 02-20 subsystems (Performance, W&B, Weather, Planning…)
* Interfaces with ATA 42, 03, 28, 31 and 95
* Data flows to/from CAOS / AirCCC
* Safety, certification and cybersecurity coverage
* DPP anchors and software lifecycle tracking

## Excluded

* Airline-specific backend (MDM, Document Server)
* Internal CAOS architecture
* Detailed NN design (handled by ATA 95)
* Human factors testing reports (referenced but not reproduced here)

---

# 3. System Mission

The AMPEL360 EFB delivers:

* **Paperless cockpit** (digital library > 10k documents)
* **Real-time performance calculations** (AI-enhanced, BWB-tuned)
* **Dynamic Weight & Balance** (H₂-aware)
* **Weather visualization + predictive hazards**
* **Charts & navigation data**
* **Crew coordination tools**
* **Operational risk visibility** (CAOS advisories)
* **Data interchange with AOC, dispatch & planning systems**

It is a **critical operational tool**, though non-safety-critical in authority (DAL D).

---

# 4. Architecture Overview

See diagram:
→ `ASSETS/02-20-11-A-001_EFB_System_Architecture.drawio`
→ `ASSETS/02-20-11-A-002_EFB_System_Architecture.svg`

## 4.1 Hardware Configuration (Class 3 / Portable)

| Component    | Specification                          |
| ------------ | -------------------------------------- |
| Devices      | iPad Pro 12.9”, dual (Captain / FO)    |
| Mounts       | DO-160 vibration-tested, quick-release |
| Power        | Aircraft 28V DC → USB-C                |
| Connectivity | WiFi 802.11ac, LTE fallback            |
| Ports        | USB-C (data/power)                     |

---

## 4.2 EFB Software Stack

```
┌───────────────────────────────────────────────────────────────┐
│                   EFB SOFTWARE PLATFORM (iOS)                  │
│                                                               │
│  ┌──────────────┬──────────────┬──────────────┬────────────┐ │
│  │ Documents    │ Performance  │ W&B          │ Weather     │ │
│  ├──────────────┼──────────────┼──────────────┼────────────┤ │
│  │ Charts/Nav   │ Flight Plan  │ CAOS Advisor │ Settings    │ │
│  └──────────────┴──────────────┴──────────────┴────────────┘ │
│                                                               │
│      02-20-01 Digital Ops Platform API Layer (REST/Events)    │
└───────────────────────────────────────────────────────────────┘
```

---

## 4.3 Integration with Subsystems

| Subsystem                         | Purpose                                      | Mode           |
| --------------------------------- | -------------------------------------------- | -------------- |
| **02-20-12 W&B Computer**         | Real-time CG/H₂ mass/limits                  | Data consumer  |
| **02-20-13 Performance Computer** | Takeoff/landing/cruise calcs                 | Consumer + UI  |
| **02-20-17 Weather System**       | METAR/TAF/GRIB + predictive                  | Bi-directional |
| **02-20-23 Predictive Ops NN**    | Delays, turnaround risk, resource prediction | Consumer       |
| **02-20-01 Digital Ops Platform** | Docs, KPIs, events, CAOS insights            | Bidirectional  |

---

## 4.4 Integration with ATA Chapters

| ATA                       | Interface                                              |
| ------------------------- | ------------------------------------------------------ |
| **ATA 42 (IMA/avionics)** | Position, altitude, speed, config, H₂ quant            |
| **ATA 28 (H₂ fuel)**      | Tank levels (read-only)                                |
| **ATA 31 (Recording)**    | EFB events → ops recording                             |
| **ATA 03 (GSE)**          | Document/updates via ground network                    |
| **ATA 95 (NN)**           | Uses: performance predictor, weather predictor, ops NN |

---

# 5. Functional Overview

## 5.1 Digital Document Library

YAML excerpt:

```yaml
document_library:
  total_documents: 12_847
  categories:
    AFM: 2450
    OM: 4200
    QRH: 850
    MEL: 320
    AMM: 3200
    Training: 1827
  features:
    full_text_search_ms: 500
    revision_tracking: auto
    annotations: shared
    offline_access: true
  update:
    frequency: daily
    delta_updates: true
    verification: digital_signature + blockchain_hash
```

---

## 5.2 Performance Calculations (AI-Enhanced)

Powered by:
→ `02-20-13_Performance_Computer`
→ `ATA 95 | Model: NN-PERF-CALC-v1.0`

Capabilities:

* Takeoff / landing performance
* Speeds V1/VR/V2/VREF
* Obstacle clearance
* Cruise optimization
* BWB ground-effect correction
* AI boost: **±1.2% accuracy** validated over >1000 flights
* Fallback: deterministic table lookup

---

## 5.3 Weight & Balance (H₂-Aware)

Powered by:
→ `02-20-12_Weight_Balance_Computer`

Features:

* CG tracking (forward/aft/lateral)
* Real-time passenger + cargo loading input
* H₂ fuel dynamics:

  * Cryogenic density → mass
  * Boil-off rate
  * Tank sequencing
  * CG shift prediction

Warnings:

* Out-of-envelope (visual + auditory)
* Predictive CG at destination

---

## 5.4 Weather Integration (Predictive)

Powered by:
→ `02-20-17_Weather_Information_System`
→ `ATA 95 | Model: NN-WEATHER-PRED-v1.0`

Data sources:

* METAR/TAF
* SIGMET/AIRMET
* Satellite IR
* GRIB upper-air
* Lightning networks
* Predictive turbulence

---

## 5.5 Charts & Navigation Data

* Jeppesen/Navigraph data
* 28-day AIRAC cycles
* Vector maps, layers, overlays
* Route preview + terrain + weather stacking

---

## 5.6 CAOS Advisory Integration

Via:
→ `02-20-01 Digital Ops Platform`
→ `02-20-23 Predictive Ops NN`

Displayed advisories:

* Turnaround delay risk
* H₂ refuelling conflict windows
* Weather hazards
* Crew workload alerts
* Network-level constraints (AOC)

Authority model:
**advisory only — no command authority.**

---

# 6. Interfaces

## 6.1 Input Data

| Source   | Frequency       | Type             |
| -------- | --------------- | ---------------- |
| ATA 42   | 1–10 Hz         | Aircraft state   |
| 02-20-12 | Continuous      | CG/W&B           |
| 02-20-13 | On-demand       | Perf outputs     |
| 02-20-17 | 15min–real-time | Weather          |
| 02-20-23 | Event-based     | Predictions      |
| CAOS     | Event/Batch     | Insights         |
| AOC      | Mixed           | Releases, NOTAMs |

---

## 6.2 Output Data

* Performance suggestions
* CG/W&B advisory states
* Crew annotations + signatures
* Operational events → `02-20-18_Operational_Data_Recording`
* CAOS feedback acknowledgements

---

# 7. Safety, Certification & Cybersecurity

Detailed docs:
→ `02-20-11-009_Safety_and_Certification.md`
→ `ASSETS/Certification/`

## 7.1 Certification Baseline

```yaml
certification:
  faa_ac_120_76d: compliant
  easa_amc_20_25: compliant
  efb_class: "Class 3 Portable"
  software:
    standard: DO-178C
    dal: DAL D
  security:
    standard: DO-326A / ED-202A
```

## 7.2 Human Factors

* HF validation in simulator
* Line evaluations
* Colour, font and interaction consistency with EFB HF guidelines

---

# 8. Operational Statistics (Current Fleet)

```yaml
fleet:
  aircraft_equipped: 12
  units_installed: 24
  flight_hours: 15280
  flights: 8450
performance:
  availability: 0.998
  document_access_time_s: 2
  perf_calc_time_s: 5
  update_success_rate: 0.9995
pilot_rating: 4.7
fuel_savings:
  cruise: 2.5%
  alternates: 1.2%
```

---

# 9. DPP Integration

```json
{
  "subsystem_id": "02-20-11",
  "software_version": "3.2.0",
  "build_hash": "sha256:a7c3f9d1e8b2c5f4...",
  "document_pack_version": "2025.11.15",
  "certification_summary": {
    "AC_120_76D": "compliant",
    "AMC_20_25": "compliant",
    "DO_178C": "DAL D"
  },
  "nn_models": [
    "NN-PERF-CALC-v1.0",
    "NN-WEATHER-PRED-v1.0",
    "NN-DELAY-PRED-v1.1"
  ]
}
```

---

# 10. Traceability

## Requirements

* RQ-02-01-001 Document Management
* RQ-02-02-001 Performance Calculator
* RQ-02-03-001 Weight & Balance
* RQ-02-04-001 Weather Visualization

## Design

* 02-20-11-A-001 System Architecture
* 02-20-11-A-003 Class 3 Integration Diagram

## Interfaces

* 02-00-05-03-001 ATA 42 IMA
* 02-20-13 Performance API
* 02-20-17 Weather Integration API

## ATA 95 linkage

* 95-20-27 Flight Control NN (performance model inputs)
* 95-20 Subsystems (NN runtime)

---

# 11. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-11 Electronic Flight Bag
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Guidelines

| Version | Date       | Author               | Changes                                |
| ------- | ---------- | -------------------- | -------------------------------------- |
| 3.2     | 2025-11-19 | AMPEL360 Digital Ops | Complete technical overview (this doc) |

---


