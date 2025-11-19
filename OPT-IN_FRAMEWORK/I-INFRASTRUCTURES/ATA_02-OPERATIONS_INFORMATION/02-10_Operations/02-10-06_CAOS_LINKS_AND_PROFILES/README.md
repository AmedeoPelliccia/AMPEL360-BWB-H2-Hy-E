# 02-10-06_CAOS_LINKS_AND_PROFILES — CAOS Links & Operational Profiles

**Axis:** I — Infrastructures  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../)  
**Bucket:** [02-10_Operations](../README.md)  
**Code:** 02-10-06_CAOS_LINKS_AND_PROFILES  

---

## 1. Purpose

`02-10-06_CAOS_LINKS_AND_PROFILES` is the **binding layer** between:

- The **operational world** of ATA 02 / `02-10_Operations`, and  
- The **CAOS / AirCCC** digital nervous system.

This folder defines **how AMPEL360 operations are “seen” by CAOS**, by:

- Mapping operational phases, scenarios and states to **CAOS channels and events**  
- Defining **operational profiles** used by CAOS (normal, abnormal, emergency, turnaround, H₂ ground, etc.)  
- Documenting **KPIs and metrics** that CAOS derives from Operations Information  
- Capturing the **authority boundaries** between CAOS advisory outputs and crew/operator decision-making  

It is the main reference for making ATA 02 **CAOS-aware**.

---

## 2. Scope

Included:

- Mapping from:
  - Normal / abnormal / emergency operations  
  - Turnaround and H₂ ground operations  
  - Mission profiles and phases of flight  

  to:

  - CAOS channels (telemetry, events)  
  - CAOS KPIs and dashboards  
  - Scenario identifiers used in CAOS use cases

- CAOS **operational profiles**:
  - “Normal mission” profiles  
  - “Stress” / “Degraded” profiles  
  - Turnaround/H₂ operational profiles  
  - Emergency observation profiles (with strict advisory-only behaviour)

- Documentation of **what CAOS “knows”** about operations:
  - Which data from ATA 02 it consumes  
  - Which events it produces  
  - How it tags, aggregates and reports operational situations

Out of scope:

- The internal architecture of CAOS itself  
  → see [CAOS Index](/CAOS/CAOS_INDEX.md)  

- Detailed CAOS governance, roles and phases  
  → see [CAOS Operations Framework](/CAOS/CAOS_OPERATIONS_FRAMEWORK.md)  

- Full scenario narratives and business-level use cases  
  → see [CAOS Use Cases](/CAOS/CAOS_USE_CASES.md)

---

## 3. Position in the OPT-IN / ATA Structure

This folder sits at the intersection of:

- **ATA 02 Operations Information**  
  - [`../../02-00-00_GENERAL/`](../../02-00-00_GENERAL/)  
  - [`../`](../README.md)  

and

- **CAOS / AirCCC**  
  - [CAOS Index](/CAOS/CAOS_INDEX.md)  
  - [CAOS Operations Framework](/CAOS/CAOS_OPERATIONS_FRAMEWORK.md)  
  - [CAOS Use Cases](/CAOS/CAOS_USE_CASES.md)

It consumes:

- Operational structures from:
  - [`../02-10-00_GLOBAL_OPERATIONS/`](../02-10-00_GLOBAL_OPERATIONS/)  
  - [`../02-10-01_NORMAL_OPERATIONS/`](../02-10-01_NORMAL_OPERATIONS/)  
  - [`../02-10-02_ABNORMAL_OPERATIONS/`](../02-10-02_ABNORMAL_OPERATIONS/)  
  - [`../02-10-03_EMERGENCY_OPERATIONS/`](../02-10-03_EMERGENCY_OPERATIONS/)  
  - [`../02-10-04_TURNAROUND_AND_TURNBACK/`](../02-10-04_TURNAROUND_AND_TURNBACK/)  
  - [`../02-10-05_H2_GROUND_OPERATIONS/`](../02-10-05_H2_GROUND_OPERATIONS/)  

- Data and constraints from:  
  - [`../../02-20-00_SYSTEMS/`](../../02-20-00_SYSTEMS/)  
  - [`../../02-90_Tables_Schemas_Diagrams/`](../../02-90_Tables_Schemas_Diagrams/)

For naming rules and mandatory cross-ATA buckets:  
→ [OPT-IN_FRAMEWORK_STANDARD.md](/OPT-IN_FRAMEWORK_STANDARD.md)

---

## 4. Suggested Internal Contents

Recommended internal structure:

### 4.1 Operational–CAOS Mapping

`02-10-06_Operational_to_CAOS_Mapping.md`

- For each operational construct (phase, scenario, profile):
  - Identifier in ATA 02 (e.g. phase name, scenario ID)  
  - Corresponding CAOS:
    - Channel(s)  
    - Event types / messages  
    - KPI group(s)  
- Explicit mapping between:
  - Normal / abnormal / emergency phases  
  - Turnaround/H₂ milestones  
  - CAOS observability model

### 4.2 CAOS Operational Profiles

`02-10-06_CAOS_Operational_Profiles.md`

- Definition of **profiles** used in CAOS analytics, for example:
  - *Standard short-range mission*  
  - *Nominal-range mission*  
  - *Degraded power mission*  
  - *H₂-constrained mission*  
  - *High-stress turnaround pattern*  

- For each profile:
  - Operational assumptions (from ATA 02)  
  - CAOS KPIs tracked  
  - Link to relevant CAOS use cases

### 4.3 KPI Catalogue

`02-10-06_CAOS_KPI_Catalogue.md`

- List and definitions of operations-related CAOS KPIs, e.g.:
  - On-time performance vs. H₂ constraints  
  - Energy efficiency per sector  
  - CO₂ removed per flight / per block hour  
  - Turnaround predictability and variance  
  - Frequency of abnormal / emergency events

- For each KPI:
  - Data sources in ATA 02 / other ATA chapters  
  - Calculation sketch and limitations  
  - CAOS dashboards / reports where it appears

### 4.4 Authority & Safety Boundaries

`02-10-06_CAOS_Authority_and_Boundaries.md`

- Clear rules on:
  - What CAOS may **observe**  
  - What CAOS may **advise**  
  - What CAOS may **never decide or command**  

- Interaction between:
  - Emergency authority (crew, operator)  
  - CAOS advisory outputs  
  - Certification and safety constraints from `02-00-02_SAFETY`

### 4.5 ASSETS

`ASSETS/` substructure (suggested):

- `ASSETS/DIAGRAMS/`
  - Operational phases → CAOS channels map  
  - Profile vs. KPI diagrams  
- `ASSETS/TABLES/`
  - KPI catalogue table  
  - Scenario → Channel → KPI matrices

---

## 5. Links to Other Buckets and ATA Chapters

**Within ATA 02**

- Governance & safety:  
  → [`../../02-00-00_GENERAL/`](../../02-00-00_GENERAL/)  

- Systems and data feeding CAOS:  
  → [`../../02-20-00_SYSTEMS/`](../../02-20-00_SYSTEMS/)  

- Tables / schemas used by CAOS ingestion:  
  → [`../../02-90_Tables_Schemas_Diagrams/`](../../02-90_Tables_Schemas_Diagrams/)  

**Operational specialisations**

- Global operations:  
  → [`../02-10-00_GLOBAL_OPERATIONS/`](../02-10-00_GLOBAL_OPERATIONS/)  

- Normal / Abnormal / Emergency ops:  
  → [`../02-10-01_NORMAL_OPERATIONS/`](../02-10-01_NORMAL_OPERATIONS/)  
  → [`../02-10-02_ABNORMAL_OPERATIONS/`](../02-10-02_ABNORMAL_OPERATIONS/)  
  → [`../02-10-03_EMERGENCY_OPERATIONS/`](../02-10-03_EMERGENCY_OPERATIONS/)  

- Turnaround and H₂ ground operations:  
  → [`../02-10-04_TURNAROUND_AND_TURNBACK/`](../02-10-04_TURNAROUND_AND_TURNBACK/)  
  → [`../02-10-05_H2_GROUND_OPERATIONS/`](../02-10-05_H2_GROUND_OPERATIONS/)  

**CAOS documentation**

- [CAOS Index](/CAOS/CAOS_INDEX.md)  
- [CAOS Operations Framework](/CAOS/CAOS_OPERATIONS_FRAMEWORK.md)  
- [CAOS Use Cases](/CAOS/CAOS_USE_CASES.md)

---

## 6. CAOS Integration Focus

This folder should progressively answer:

1. **What does CAOS “see” from ATA 02?**  
   - Phases, events, states, constraints, profiles.

2. **How does CAOS talk back to operations?**  
   - Advisory outputs, dashboards, alerts, reports.  

3. **How is this bounded by safety and certification?**  
   - No hard commands, no override of certified control laws, traceable advice.

The aim is to make the bridge between **paper operations** and **live CAOS
intelligence** explicit, audit-able and certifiable.

---

## 7. Conventions

- Use `02-10-06_Description` naming for all artefacts in this folder.  
- Keep content:
  - **Aircraft/program-level** (not airline-specific)  
  - **Implementation-agnostic** with respect to CAOS internal code  
- Every document should include:
  - **Scope**  
  - **Cross-References** (ATA 02, other ATA, CAOS docs)  
  - **Assumptions / Limitations**  

Do **not** duplicate CAOS internal architecture documents; link to them instead.

---

## 8. Document Control

> **Status:** Draft / Placeholder  
> **Owner:** AMPEL360 CAOS & Operations Information Working Groups  
> **Applies to:** All CAOS–operations binding for ATA_02

| Version | Date       | Author / Team                              | Changes                                            |
|---------|------------|---------------------------------------------|----------------------------------------------------|
| 0.1     | YYYY-MM-DD | AMPEL360 CAOS & Operations Information WGs | Initial CAOS links & operational profiles layout   |
