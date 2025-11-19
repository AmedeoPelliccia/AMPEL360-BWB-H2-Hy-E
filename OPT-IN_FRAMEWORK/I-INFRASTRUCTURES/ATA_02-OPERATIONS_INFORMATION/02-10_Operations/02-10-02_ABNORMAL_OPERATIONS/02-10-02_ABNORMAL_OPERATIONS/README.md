# 02-10-02_ABNORMAL_OPERATIONS — Abnormal Operations

**Axis:** I — Infrastructures  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../)  
**Bucket:** [02-10_Operations](../README.md) (Operational use, turnarounds, procedures)  
**Code:** 02-10-02_ABNORMAL_OPERATIONS  

---

## 1. Purpose

`02-10-02_ABNORMAL_OPERATIONS` defines **program-level abnormal operations**
for AMPEL360, i.e. **non-normal** but not yet emergency conditions, and how
they use information from ATA 02.

Typical cases include:

- System degradations with **dispatched or in-flight restrictions**  
- MEL/CDL-driven configurations impacting performance or procedures  
- Hydrogen / fuel-cell / CO₂ battery limitations still within a *controlled* envelope  
- Ground or turnaround issues that require adapted but non-emergency handling  

This folder provides the **baseline abnormal operations playbook** for the
AMPEL360 BWB H₂ Hy-E family, from which operators can derive OM-A/OM-B/QRH
content.

---

## 2. Scope

Included:

- Classification of **abnormal scenarios** relevant to Operations Information:
  - Performance and W&B degradations
  - System downgrades impacting flight planning and dispatch
  - Hydrogen and energy-system constraints (e.g. reduced tank capacity,
    limited fuel cell availability, CO₂ battery offline)
- Operational consequences:
  - Route / altitude / payload restrictions
  - Additional monitoring and cross-checks
  - Modified turnaround or refuelling sequences
- Use of **ATA 02 data** to evaluate, accept, or reject dispatch and continuation:
  - Performance margins vs. required
  - Weight & balance envelopes
  - Operational limitations tables
- Interfaces with **CAOS / AirCCC** for detection, monitoring and advisory support

Out of scope:

- Full emergency procedures (time-critical, “memory items”-type content)  
  → see [`../02-10-03_EMERGENCY_OPERATIONS/`](../02-10-03_EMERGENCY_OPERATIONS/)

- Purely normal operations (no degradation)  
  → see [`../02-10-01_NORMAL_OPERATIONS/`](../02-10-01_NORMAL_OPERATIONS/)

- Detailed technical failure analysis (FMEA, FHA, FTA, etc.)  
  → see [`../../02-00-00_GENERAL/02-00-02_SAFETY/`](../../02-00-00_GENERAL/02-00-02_SAFETY/) and
     the relevant Technology ATA chapters (28, 71, 95, …)

- Detailed system performance models  
  → see [`../../02-20-00_SYSTEMS/`](../../02-20-00_SYSTEMS/)

---

## 3. Position in the OPT-IN / ATA Structure

- **General lifecycle & governance**  
  → [`../../02-00-00_GENERAL/`](../../02-00-00_GENERAL/)

- **Operations bucket root**  
  → [`../README.md`](../README.md)

- **Normal operations**  
  → [`../02-10-01_NORMAL_OPERATIONS/`](../02-10-01_NORMAL_OPERATIONS/)

- **Emergency operations**  
  → [`../02-10-03_EMERGENCY_OPERATIONS/`](../02-10-03_EMERGENCY_OPERATIONS/)

- **Systems & performance providers**  
  → [`../../02-20-00_SYSTEMS/`](../../02-20-00_SYSTEMS/)  
    (performance data, weight & balance, limitations, flight planning)

For global rules on buckets and naming, see:  
- [OPT-IN_FRAMEWORK_STANDARD.md](/OPT-IN_FRAMEWORK_STANDARD.md)

---

## 4. Suggested Internal Contents

Recommended internal files / structure:

- `02-10-02_Abnormal_Ops_Taxonomy.md`  
  - Taxonomy of abnormal scenarios (by system, by operational impact, by phase of flight)  
  - Link each scenario to the relevant **ATA 02 tables** and **system chapters**

- `02-10-02_Abnormal_Ops_Operational_Consequences.md`  
  - For each category of abnormal condition:
    - Dispatch impact (GO / NO-GO / GO-IF) at program level
    - Payload, route, altitude and meteorological constraints
    - Additional monitoring requirements for crew and dispatch
  - Cross-links to:
    - [`../../02-20-00_SYSTEMS/`](../../02-20-00_SYSTEMS/)
    - [`../../02-90_Tables_Schemas_Diagrams/`](../../02-90_Tables_Schemas_Diagrams/)

- `02-10-02_Scenarios_and_Examples.md`  
  - Representative example scenarios, e.g.:
    - One fuel cell string offline (derated power capability)
    - CO₂ battery available but capacity reduced
    - One H₂ tank unavailable (reduced usable fuel)
  - For each scenario:
    - “Program-level” expected handling
    - References to source data and chapters

- `ASSETS/`  
  - `ASSETS/DIAGRAMS/` — flowcharts for abnormal decision paths  
  - `ASSETS/TABLES/` — scenario vs. impact matrices

The goal is not to encode operator SOPs, but to **encode the design intent**
and operational consequences that are stable at aircraft/program level.

---

## 5. Links to Other Buckets and Chapters

**Within ATA 02**

- Governance & safety:  
  → [`../../02-00-00_GENERAL/`](../../02-00-00_GENERAL/)  
  → [`../../02-00-00_GENERAL/02-00-02_SAFETY/`](../../02-00-00_GENERAL/02-00-02_SAFETY/)

- Systems / data providers:  
  → [`../../02-20-00_SYSTEMS/`](../../02-20-00_SYSTEMS/)  
  → [`../../02-90_Tables_Schemas_Diagrams/`](../../02-90_Tables_Schemas_Diagrams/)

**Typical other ATA chapters touched by abnormal ops** (links to be instantiated later):

- **ATA 28 – Hydrogen Fuel System**  
  - Tank availability, pressure/temperature windows, refuelling constraints
- **ATA 71 – Power Plant (Fuel Cells)**  
  - Derated power, stack offline scenarios
- **ATA 95 – Neural Networks / DPP**  
  - Abnormal behaviour of advisory models and fallback / reversion policies
- **ATA 03 – Support Information GSE**  
  - GSE unavailability or constraints that push the aircraft into abnormal turnaround

When referencing these chapters, use **relative links** once their directories exist.

---

## 6. CAOS Integration

Abnormal operations are a **primary target** for CAOS observation and advisory:

This folder should progressively document:

- Which abnormal conditions are:
  - **Detected** or **confirmed** by CAOS  
  - **Only observed** (no advisory) vs. those with **advisory suggestions**

- How CAOS channels capture abnormal events:
  - Telemetry channels (e.g. OFEC / PMT / other defined channels)
  - Event markers for transitions from normal → abnormal → emergency

- Which **KPIs** are tracked:
  - Frequency of certain abnormal scenarios
  - Impact on payload, delay, mission completion
  - Hydrogen and energy system stress caused by abnormal ops

- Boundaries and authority:
  - CAOS is **advisory-only**; final authority remains with crew and operator  
  - Any suggestion must be traceable back to the underlying data and models

Reference documents:

- [CAOS Index](/CAOS/CAOS_INDEX.md)  
- [CAOS Operations Framework](/CAOS/CAOS_OPERATIONS_FRAMEWORK.md)

---

## 7. Conventions

- Code format: `02-10-02_Description` for all artefacts in this folder.
- Always include:
  - **Scope** — what part of abnormal ops is covered  
  - **Links / Cross-References** — to 02-20, 02-90, and other ATA chapters  
  - **CAOS Integration** — even if “Not yet applicable” at early stages

- Do **not** duplicate:
  - Detailed safety analysis already in safety folders  
  - Raw performance or W&B tables already in `02-20-00_SYSTEMS/`

- Keep descriptions at **program/aircraft level**, not airline level.

---

## 8. Document Control

> **Status:** Draft / Placeholder  
> **Owner:** AMPEL360 Operations Information Working Group  
> **Applies to:** Abnormal (non-emergency) operations for AMPEL360 BWB H₂ Hy-E

| Version | Date       | Author / Team                         | Changes                                  |
|---------|------------|----------------------------------------|------------------------------------------|
| 0.1     | YYYY-MM-DD | AMPEL360 Operations Information WG    | Initial abnormal operations definition   |
