# 02-10-04_TURNAROUND_AND_TURNBACK — Turnaround & Turnback Operations

**Axis:** I — Infrastructures  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../)  
**Bucket:** [02-10_Operations](../README.md) (Operational use, turnarounds, procedures)  
**Code:** 02-10-04_TURNAROUND_AND_TURNBACK  

---

## 1. Purpose

`02-10-04_TURNAROUND_AND_TURNBACK` defines, at **program level**, how AMPEL360
handles:

- **Turnaround operations** (gate-to-gate cycles, ground times, service sequences)  
- **Turnback decisions** (return to departure aerodrome after take-off or early
  in the mission)  

with particular focus on:

- Hydrogen refuelling / conditioning constraints  
- CO₂ battery and energy-system implications  
- Operational use of ATA 02 data (performance, W&B, limitations, planning)  
- Interfaces with **CAOS / AirCCC** for prediction, monitoring and post-analysis  

---

## 2. Scope

Included:

- Definition of **turnaround phases** and their operational objectives  
- Standard AMPEL360 **turnaround profiles** (e.g. minimum, nominal, extended)  
- Use of Operations Information (ATA 02) for:
  - Ground-time planning and rotation building  
  - Hydrogen and energy system readiness checks  
  - Payload and mission planning constraints  
- Program-level **turnback rationale and triggers**, including:
  - Performance / energy margins  
  - Technical status (H₂ system, fuel cells, CO₂ battery)  
  - Airport infrastructure and hydrogen availability  
- How turnaround and turnback events are observed and logged via **CAOS**

Out of scope:

- Detailed SOPs for ground handlers or specific airports  
- Company-specific rotation policies and commercial constraints  
- Engineering-level analysis of system behaviours (owned by `02-00-xx` and
  Technology ATA chapters)

---

## 3. Position in the OPT-IN / ATA Structure

- **Global operations framework**  
  → [`../02-10-00_GLOBAL_OPERATIONS/`](../02-10-00_GLOBAL_OPERATIONS/)

- **Normal / Abnormal / Emergency ops**  
  → [`../02-10-01_NORMAL_OPERATIONS/`](../02-10-01_NORMAL_OPERATIONS/)  
  → [`../02-10-02_ABNORMAL_OPERATIONS/`](../02-10-02_ABNORMAL_OPERATIONS/)  
  → [`../02-10-03_EMERGENCY_OPERATIONS/`](../02-10-03_EMERGENCY_OPERATIONS/)

- **Systems & performance providers**  
  → [`../../02-20-00_SYSTEMS/`](../../02-20-00_SYSTEMS/)  
- **Circularity & sustainability impacts**  
  → [`../../02-30_Circularity/`](../../02-30_Circularity/)  

For bucket rules, cross-ATA structure and naming, see:  
→ [OPT-IN_FRAMEWORK_STANDARD.md](/OPT-IN_FRAMEWORK_STANDARD.md)

---

## 4. Suggested Internal Contents

Recommended internal files / structure:

### 4.1 Turnaround Concept & Profiles  
`02-10-04_Turnaround_Concept_and_Profiles.md`

- Definitions of:
  - **Turnaround** for AMPEL360 (inbound block-in to outbound block-out)  
  - Minimum vs. nominal vs. extended turnaround profiles  
- Dependencies on:
  - Hydrogen refuelling (ATA 28 / ATA 03 GSE)  
  - CO₂ battery charge/conditioning  
  - Maintenance tasks and inspections  
- Cross-links:
  - [`../../02-20-00_SYSTEMS/`](../../02-20-00_SYSTEMS/) (turnaround-related limits)  
  - [`../../02-30_Circularity/`](../../02-30_Circularity/) (carbon-negative mission design)

### 4.2 Turnaround Ground Flow  
`02-10-04_Turnaround_Ground_Flow.md`

- Gate flow overview:
  - Arrival, deboarding, servicing, refuelling, boarding, pushback  
- Interfaces with ATA 03 GSE and airport infrastructure  
- Turnaround **critical path** elements for AMPEL360 (H₂, power, cooling, CO₂)

### 4.3 Turnback Philosophy and Criteria  
`02-10-04_Turnback_Philosophy_and_Criteria.md`

- Definitions:
  - **Turnback**, **early diversion**, **continue to destination**  
- Program-level criteria using data from ATA 02:
  - Energy margins vs. required  
  - Performance vs. runway / weather / obstacle environment  
  - Availability of hydrogen / support at alternate fields  
- Relationship to:
  - [`../02-10-02_ABNORMAL_OPERATIONS/`](../02-10-02_ABNORMAL_OPERATIONS/)  
  - [`../02-10-03_EMERGENCY_OPERATIONS/`](../02-10-03_EMERGENCY_OPERATIONS/)

### 4.4 ASSETS

`ASSETS/` substructure (suggested):

- `ASSETS/DIAGRAMS/02-10-04_Turnaround_Flow.svg`  
- `ASSETS/TABLES/02-10-04_Turnaround_Profiles_vs_Times.md`  
- `ASSETS/TABLES/02-10-04_Turnback_Decision_Matrix.md`

---

## 5. Links to Other Buckets and ATA Chapters

**Within ATA 02**

- Governance, safety, lifecycle:  
  → [`../../02-00-00_GENERAL/`](../../02-00-00_GENERAL/)  
- Systems and data feeding turnaround/turnback:  
  → [`../../02-20-00_SYSTEMS/`](../../02-20-00_SYSTEMS/)  
- Tables and schemas used for rotations and decision matrices:  
  → [`../../02-90_Tables_Schemas_Diagrams/`](../../02-90_Tables_Schemas_Diagrams/)

**Other ATA chapters (to be linked as they are instantiated)**

- **ATA 03 – SUPPORT_INFORMATION_GSE**  
  - Ground service equipment, H₂ trucks / refuellers, power carts  
- **ATA 28 – HYDROGEN FUEL SYSTEM**  
  - Refuelling profiles, cooling / conditioning times, pressure/temperature limits  
- **ATA 71 – POWERPLANT (Fuel Cells)**  
  - Power availability on turnarounds, warm-up / cool-down constraints  
- **ATA 95 – Neural Networks / DPP**  
  - Predictive insight feeding turnaround and turnback decisions

Use relative links to these chapters once their directories exist.

---

## 6. CAOS Integration

Turnaround and turnback are **key CAOS focal points**:

This folder should describe:

- How **CAOS**:
  - Monitors turnarounds (timestamps, durations, constraint violations)  
  - Tracks hydrogen and energy-related readiness indicators  
  - Flags conditions that may recommend longer turnarounds or different rotations  

- How **turnback decisions** can be:
  - Supported with advisory outputs (energy/payload/alternate assessment)  
  - Logged for fleet-wide analysis (routes / conditions / system states leading to turnback)

Reference documents:

- [CAOS Index](/CAOS/CAOS_INDEX.md)  
- [CAOS Operations Framework](/CAOS/CAOS_OPERATIONS_FRAMEWORK.md)

CAOS remains **advisory-only**; final decisions stay with crew and operator.

---

## 7. Conventions

- Use `02-10-04_Description` naming for artefacts in this folder.  
- Keep content **operator-agnostic** and **program-level**.  
- Do **not** duplicate:
  - Performance / turnaround data owned by `02-20-00_SYSTEMS/`  
  - Detailed airport- or airline-specific ground procedures  

Each document should clearly include:

- **Scope**  
- **Cross-References** (ATA 02, other ATA chapters, CAOS)  
- **Assumptions** (e.g. infrastructure level, hydrogen availability, standard day)

---

## 8. Document Control

> **Status:** Draft / Placeholder  
> **Owner:** AMPEL360 Operations Information Working Group  
> **Applies to:** Turnaround and turnback operational concepts for AMPEL360 BWB H₂ Hy-E

| Version | Date       | Author / Team                         | Changes                                          |
|---------|------------|----------------------------------------|--------------------------------------------------|
| 0.1     | YYYY-MM-DD | AMPEL360 Operations Information WG    | Initial turnaround & turnback operations layout  |
