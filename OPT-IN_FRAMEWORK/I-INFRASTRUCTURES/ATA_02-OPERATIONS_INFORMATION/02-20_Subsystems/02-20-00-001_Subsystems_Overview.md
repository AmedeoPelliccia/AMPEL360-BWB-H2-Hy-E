# 02-20-00-001 — Subsystems Overview

**Subsystems Group:** 02-20_Subsystems  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../README.md)  
**Axis:** I — Infrastructures  
**Status:** FRAMEWORK_DEFINED  

---

## 1. Purpose

This document provides a **high-level overview** of all **digital operations
subsystems** grouped under `02-20_Subsystems` in ATA 02 — Operations Information.

It explains:

- What each subsystem **is responsible for**
- How subsystems **interact** with each other
- Which **ATA chapters** they depend on
- How they are **seen by CAOS / AirCCC** and by **ATA 95 Neural Networks**

It is the **entry point** for engineers, operators and cert teams who need
to navigate the AMPEL360 digital operations stack.

---

## 2. Scope

Included in this overview:

- Description of each `02-20-XX_…` subsystem and its **role in operations**
- Logical grouping into:
  - **Core Ops Platform**
  - **Onboard Operational Tools (EFB, W&B, Performance…)**
  - **Ground / Dispatch / AOC Integration**
  - **Data, Recording & Predictive Operations**
- Summary of **cross-ATA dependencies**
- Summary of **CAOS and ATA 95 integration points**

Details of architecture, interfaces and certification live in the individual
subsystem folders (e.g. `02-20-11_Electronic_Flight_Bag/`).

Out of scope:

- Full technical architectures (see each `02-20-XX_…/README.md`)
- Detailed safety analysis (see `../02-00-00_GENERAL/02-00-02_SAFETY/`)
- Detailed ML model documentation (see ATA 95 / model cards)

---

## 3. Subsystems Landscape

### 3.1 Core Digital Ops Platform

- **[02-20-01_Digital_Ops_Platform](./02-20-01_Digital_Ops_Platform/)**  
  Central **digital operations platform** providing:
  - Shared data layer (ops data lake / lakehouse)
  - Common services (auth, notifications, audit, APIs)
  - Integration backbone for all other 02-20 subsystems  
  It is the “platform below the apps”.

---

### 3.2 Flight Deck & Onboard Ops Tools

These subsystems live closest to the **crew** and the **aircraft**:

- **[02-20-11_Electronic_Flight_Bag](./02-20-11_Electronic_Flight_Bag/)**  
  Class 3 EFB platform providing:
  - Digital document management
  - Performance calculations
  - Weight & Balance functions
  - Weather and NOTAM integration
  - Charts and navigation data
  - UI for selected CAOS / predictive insights  

- **[02-20-12_Weight_Balance_Computer](./02-20-12_Weight_Balance_Computer/)**  
  Core W&B engine:
  - Mass properties and CG envelope monitoring
  - H₂ fuel integration (cryogenic effects, boil-off, tank sequencing)
  - Real-time CG tracking and prediction
  - Interfaces with ATA 28 (H₂ fuel) and 21/25/44 (cabin / payload)

- **[02-20-13_Performance_Computer](./02-20-13_Performance_Computer/)**  
  Performance computation stack:
  - Takeoff / landing performance
  - Climb / cruise / descent optimization
  - BWB-specific performance logic
  - NN-based enhancements referencing ATA 95  
  (e.g. `02-20-13-005_NN_Performance_Predictor.md`)

---

### 3.3 Ground & Turnaround Management

These subsystems orchestrate **ground operations** and **turnarounds**:

- **[02-20-14_Ground_Ops_Management](./02-20-14_Ground_Ops_Management/)**  
  Manages:
  - Turnaround timelines and milestones
  - GSE coordination (ATA 03)
  - H₂ refuelling sequencing (link to 02-20-21 and ATA 28)
  - Cargo loading, boarding bridge integration, gate operations

- **[02-20-21_H2_Operations_Management](./02-20-21_H2_Operations_Management/)**  
  H₂-specific operations layer:
  - H₂ refuelling / defuelling procedures (ops view)
  - Safety monitoring and infrastructure coordination
  - Emergency H₂ operational procedures at program level

---

### 3.4 Flight Planning & Dispatch Integration

These subsystems connect AMPEL360 to **airline planning and dispatch**:

- **[02-20-15_Flight_Planning_Integration](./02-20-15_Flight_Planning_Integration/)**  
  Connects to flight planning tools for:
  - Route and trajectory optimization
  - H₂ fuel planning and range assessment
  - Weather and NOTAM integration for planning stage
  - Alternate selection and policy enforcement

- **[02-20-16_Dispatch_System_Integration](./02-20-16_Dispatch_System_Integration/)**  
  AOC / dispatch integration:
  - Flight release workflows
  - Operational messages (delays, re-routes, restrictions)
  - Real-time updates back to EFB and onboard systems

---

### 3.5 Weather & Operational Data

- **[02-20-17_Weather_Information_System](./02-20-17_Weather_Information_System/)**  
  Weather data aggregation layer:
  - Ingests METAR, TAF, SIGMET, GRIB, satellite, turbulence products
  - Feeds EFB and planning tools
  - Hosts NN-based predictive weather services (e.g. turbulence prediction)

- **[02-20-18_Operational_Data_Recording](./02-20-18_Operational_Data_Recording/)**  
  Ops data recording and linkage to ATA 31 & DPP:
  - Event logging for operations
  - Performance monitoring
  - DPP integration (`02-20-18-005_DPP_Integration.md`)
  - Feeds predictive / analytics subsystems and CAOS

---

### 3.6 Crew & Passenger Operations

- **[02-20-19_Crew_Resource_Management](./02-20-19_Crew_Resource_Management/)**  
  Crew-focused digital tools:
  - Task and procedure management
  - Comms tools
  - Workload monitoring (including NN-based workload prediction)

- **[02-20-22_Passenger_Experience_Management](./02-20-22_Passenger_Experience_Management/)**  
  Passenger-facing operations support:
  - Boarding and seating management
  - In-flight service coordination
  - Comfort monitoring integration (ECS, lighting, etc.)

---

### 3.7 Predictive & AI-Driven Operations

- **[02-20-23_Predictive_Operations_NN](./02-20-23_Predictive_Operations_NN/)**  
  Dedicated AI/ML subsystem for operations:
  - Delay prediction NNs
  - Turnaround optimization NNs
  - Reinforcement Learning for resource allocation
  - Anchored into ATA 95 (NN traceability, model cards, DPP)

---

## 4. Cross-ATA Dependencies

High-level cross-ATA dependencies are captured in:

- [`02-20-00-002_Subsystems_Integration_Map.md`](./02-20-00-002_Subsystems_Integration_Map.md)  
- [`02-20-00-003_Cross_ATA_Dependencies.csv`](./02-20-00-003_Cross_ATA_Dependencies.csv)  

Typical dependencies include:

- **ATA 03 – Support Information / GSE**  
  → Ground operations, H₂ refuelling GSE, power carts, boarding equipment.

- **ATA 28 – Hydrogen Fuel System**  
  → H₂ quantity, states, refuelling limits, safety interlocks.

- **ATA 31 – Indicating & Recording Systems**  
  → Ops data recording and replay.

- **ATA 42 – Integrated Modular Avionics**  
  → IMA, AOC connectivity, EFB data links.

- **ATA 71 – Powerplant (Fuel Cells)**  
  → Power availability, derating, constraints.

- **ATA 95 – Neural Networks / Digital Product Passport**  
  → NN models for performance, weather, predictive ops; DPP anchoring.

For global OPT-IN bucket rules and naming conventions, see:  
- [OPT-IN_FRAMEWORK_STANDARD.md](../../../OPT-IN_FRAMEWORK_STANDARD.md)

---

## 5. CAOS & ATA 95 Integration

CAOS / AirCCC and ATA 95 models use 02-20 subsystems as **primary data sources**.

Details are elaborated in:

- [`02-20-00-004_CAOS_Operations_Integration.md`](./02-20-00-004_CAOS_Operations_Integration.md)  
- ATA 95 GENERAL and subsystem docs (e.g. `95-20_Subsystems/…`)

At a high level:

- **CAOS**:
  - Consumes events, KPIs and states from EFB, W&B, performance, planning, ground ops,
    recording and predictive ops subsystems.
  - Provides back advisory insights surfaced in EFB, AOC and dashboards.

- **ATA 95 NNs**:
  - Live behind `02-20-13`, `02-20-17`, `02-20-19`, `02-20-23` as AI components.
  - Are governed by ATA 95 documentation, model cards and DPP entries.

---

## 6. Usage & Navigation

For each subsystem:

1. Start from its `README.md` in `02-20-XX_…/`  
2. Use the local **Scope / Interfaces / CAOS Integration / Certification** sections  
3. Traverse cross-links to:
   - `../02-10_Operations/` for operational usage
   - `../02-30_Circularity/` for sustainability constraints
   - `../02-90_Tables_Schemas_Diagrams/` for data schemas
   - `/ATA_95-…/` for NN details and traceability

---

## 7. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia  
> **Toolchain:** GitHub Copilot / MCP Doc Control / AMPEL360 Doc Guidelines  
> **Scope:** Overview of all 02-20 subsystems

| Version | Date       | Author / Team                          | Changes                          |
|---------|------------|-----------------------------------------|----------------------------------|
| 0.1     | YYYY-MM-DD | AMPEL360 Digital Operations & CAOS WG  | Initial subsystems overview      |
