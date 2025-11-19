# 02-10_Operations — Operational Use of AMPEL360 Operations Information

**Axis:** I — Infrastructures  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../)  
**Bucket:** 10_Operations (Operational use, turnarounds, procedures)

---

## 1. Purpose

The `02-10_Operations` bucket captures **how AMPEL360 Operations Information
(ATA 02)** is actually **used in daily operations**:

- Gate-to-gate use of operational data and procedures  
- Normal, abnormal and emergency operations at **program level**  
- Turnaround and hydrogen-specific ground operations  
- Interfaces with **[CAOS / AirCCC](../../../CAOS/CAOS_INDEX.md)** for advisory intelligence and monitoring  

It translates the governance and lifecycle framework defined in
[`02-00-00_GENERAL/`](../02-00-00_GENERAL/) into **concrete operational views**.

---

## 2. Scope

Included in this bucket:

- Global operational model for AMPEL360 (mission profiles, phases of flight)
- Normal / abnormal / emergency operations at program level
- Turnaround operations and turnback logic
- Hydrogen-specific ground and flight operational constraints
- Mapping between operations and **CAOS** channels / KPIs

Out of scope (owned elsewhere):

- Detailed performance data, envelopes, limitations  
  → [`02-20-00_SYSTEMS/`](../02-20-00_SYSTEMS/) and their system chapters  
- Detailed engineering analyses (FEA, CFD, etc.)  
  → [`02-00-00_GENERAL/02-00-06_ENGINEERING/`](../02-00-00_GENERAL/02-00-06_ENGINEERING/) and technology ATA chapters  
- Airline-specific OM-A / OM-B / SOPs  
  → Derived by operators from this baseline

---

## 3. Internal Structure of 02-10_Operations

Recommended initial structure:

- [`02-10-00_GLOBAL_OPERATIONS/`](./02-10-00_GLOBAL_OPERATIONS/)  
  Global operational framework: gate-to-gate model, phases of flight, mission
  profiles, roles and responsibilities.

- [`02-10-01_NORMAL_OPERATIONS/`](./02-10-01_NORMAL_OPERATIONS/)  
  Program-level normal operations sequences (taxi, take-off, climb, cruise,
  descent, approach, taxi-in).

- [`02-10-02_ABNORMAL_OPERATIONS/`](./02-10-02_ABNORMAL_OPERATIONS/)  
  Operational handling of non-normal conditions (degradations, MEL-driven
  configurations, dispatch with constraints).

- [`02-10-03_EMERGENCY_OPERATIONS/`](./02-10-03_EMERGENCY_OPERATIONS/)  
  Operational procedures for emergency scenarios (evacuation, H₂ leaks, multiple
  failures, etc.) — *operational view*, not detailed system design.

- [`02-10-04_TURNAROUND_AND_TURNBACK/`](./02-10-04_TURNAROUND_AND_TURNBACK/)  
  Turnaround profiles, minimum turnaround time assumptions, turnback criteria
  linked to performance and system status.

- [`02-10-05_H2_GROUND_OPERATIONS/`](./02-10-05_H2_GROUND_OPERATIONS/)  
  Hydrogen-specific ground operations and constraints (refuelling envelopes,
  safe zones, coordination with ATA 03 GSE).

- [`02-10-06_CAOS_LINKS_AND_PROFILES/`](./02-10-06_CAOS_LINKS_AND_PROFILES/)  
  Mapping between operational scenarios and CAOS telemetry channels, KPIs and
  dashboards.

Each subfolder must contain at least a `README.md` describing:

- Scope and intent  
- Links to relevant `02-20-xx` subsystems and other ATA chapters  
- Any CAOS channels / KPIs that observe or support that operational area  

---

## 4. Relationship to Other Buckets

- **[`02-00-00_GENERAL/`](../02-00-00_GENERAL/)**  
  Owns governance, safety, requirements, lifecycle, certification framework for
  Operations Information.

- **[`02-20-00_SYSTEMS/`](../02-20-00_SYSTEMS/)**  
  Owns systems, performance models, weight & balance, limitations and flight
  planning artefacts that operations rely on.

- **[`02-30_Circularity/`](../02-30_Circularity/)**  
  Provides sustainability and circularity constraints that may impact operations
  (e.g. carbon-negative mission profiles).

- **[`02-90_Tables_Schemas_Diagrams/`](../02-90_Tables_Schemas_Diagrams/)**  
  Hosts schemas and tables referenced from operational documents in 02-10.

- **CAOS layer (`/CAOS`)**  
  - [CAOS Index](../../../CAOS/CAOS_INDEX.md) — concepts and architecture  
  - [CAOS Operations Framework](../../../CAOS/CAOS_OPERATIONS_FRAMEWORK.md) — operational playbook and roles  

CAOS consumes the operational model defined here as the **semantic backbone** for
advisory services, telemetry interpretation and fleet KPIs.

---

## 5. Conventions

- Bucket code format: `02-10-ZZ_DESCRIPTION` where:
  - `02` = ATA chapter (Operations Information)  
  - `10` = Operations bucket (per OPT-IN standard)  
  - `ZZ` = sequence number (00–99)

- Do **not** recreate the 14 lifecycle folders (01_OVERVIEW … 14_META_GOVERNANCE)
  inside this bucket; those belong to [`02-00-00_GENERAL/`](../02-00-00_GENERAL/).

- Keep content **operator-agnostic** (program / aircraft level).  
  Airline-specific tailoring is expected to live outside this repository.

- Each new `02-10-XX_…` folder should:
  - Declare clear **scope** and **interfaces** (which systems, which ATA chapters)  
  - Reference any **CAOS channels / KPIs** that touch that operational topic  
  - Link back to source data (performance, limitations, etc.) instead of duplicating it.

For cross-ATA rules and bucket definitions, see:  
- [OPT-IN_FRAMEWORK_STANDARD.md](../../../OPT-IN_FRAMEWORK_STANDARD.md)

---

## 6. Document Control

> **Status:** Draft / Initial structure  
> **Owner:** AMPEL360 Operations Information Working Group  
> **Applies to:** All operational-use documentation under ATA_02

A formal control table can be added later, for example:

| Version | Date       | Author / Team                         | Changes                         |
|---------|------------|----------------------------------------|---------------------------------|
| 0.1     | YYYY-MM-DD | AMPEL360 Operations Information WG    | Initial 02-10 bucket definition |

