# O-ORGANIZATION — Overview

## *OPT-IN Axis O — Organization / ATA 00–05 Skeleton*

This directory contains the **organizational backbone** of the AMPEL360 program along four core ATA chapters:

- `ATA_00-GENERAL`
- `ATA_01-MAINTENANCE_POLICY_INFORMATION`
- `ATA_04-AIRWORTHINESS_LIMITATIONS`
- `ATA_05-TIME_LIMITS_MAINTENANCE_CHECKS`

Each ATA chapter:

- Implements the **standard XX-00 lifecycle skeleton** (`XX-00-01_Overview` … `XX-00-14_Ops_Std_Sustain`).
- Implements the **cross-ATA bucket layer** (`XX-10_Operations` … `XX-90_Tables_Schemas_Diagrams`).
- Is anchored in the **O-Axis** as part of the organizational and policy layer of AMPEL360.

---

## 1. ATA 00 – GENERAL (`ATA_00-GENERAL`)

**Purpose:** General program-level information and organizational context.

### 1.1 Lifecycle Layer — `00-00_GENERAL`

Folders:

- `00-00-01_Safety` — Safety governance and high-level safety principles  
- `00-00-02_Overview` — Program and organizational overview  
- `00-00-03_Requirements` — Organizational and program-level requirements  
- `00-00-04_Design` — Design philosophy at program/organization level  
- `00-00-05_Interfaces` — High-level organizational interfaces (internal/external)  
- `00-00-06_Engineering` — Engineering governance, methods and standards  
- `00-00-07_V_AND_V` — V&V policy and approval strategy  
- `00-00-08_Prototyping` — Prototyping, demonstrators and piloting approach  
- `00-00-09_Production_Planning` — Industrialization and production planning policies  
- `00-00-10_Certification` — Certification strategy and authority interface principles  
- `00-00-11_EIS_Versions_Tags` — Entry-into-service, baselines and tagging strategy  
- `00-00-12_Services` — Service and support concept from organizational view  
- `00-00-13_Subsystems_Components` — High-level breakdown of main subsystems/components  
- `00-00-14_Ops_Std_Sustain` — Operational standards & sustainability policy

Example governance artefact:

- `00-00-14_Ops_Std_SustainSHM_Governance_Standard.md`  
  Organizational standard for **SHM (Structural Health Monitoring) governance** under Ops/Sustainability.

### 1.2 Cross-ATA Buckets — `00-10` … `00-90`

- `00-10_Operations` — Operations-related organizational standards  
- `00-20_Subsystems` — Organizational breakdown by subsystem family  
- `00-30_ANCHORS` — Anchors for circularity, sustainability and lifetime commitments  
- `00-40_Software` — Software governance and policy (non-ATA 95-specific)  
- `00-50_Structures` — Structural governance and responsibilities  
- `00-60_Storages` — Storage and inventory governance (data, parts, energy)  
- `00-70_Propulsion` — High-level propulsion governance roles and responsibilities  
- `00-80_Energy` — Energy & sustainability governance structures  
- `00-90_Tables_Schemas_Diagrams` — Shared tables, schemas and diagrams for O-Organization

---

## 2. ATA 01 – MAINTENANCE POLICY INFORMATION (`ATA_01-MAINTENANCE_POLICY_INFORMATION`)

**Purpose:** Organizational layer for **maintenance policy and maintenance information frameworks**.

### 2.1 Lifecycle Layer — `01-00_GENERAL`

Folders:

- `01-00-01_Overview` — Maintenance policy overview  
- `01-00-02_Safety` — Safety implications of maintenance policies  
- `01-00-03_Requirements` — Maintenance-related requirements and constraints  
- `01-00-04_Design` — Design rules driven by maintenance policy (maintainability)  
- `01-00-05_Interfaces` — Interfaces between maintenance org, operators, OEM, MROs  
- `01-00-06_Engineering` — Engineering rules feeding maintenance policy (RCM, MSG-3, etc.)  
- `01-00-07_V_AND_V` — V&V of maintenance programs and tools  
- `01-00-08_Prototyping` — Trial programs, pilot maintenance schemes  
- `01-00-09_Production_Planning` — Alignment of maintenance policy with production planning  
- `01-00-10_Certification` — Maintenance policy aspects subject to authority approval  
- `01-00-11_EIS_Versions_Tags` — Maintenance program versions and tagging  
- `01-00-12_Services` — Maintenance support services and info services  
- `01-00-13_Subsystems_Components` — Maintenance views by subsystem/component  
- `01-00-14_Ops_Std_Sustain` — Maintenance standards linked to operations and sustainability

### 2.2 Cross-ATA Buckets — `01-10` … `01-90`

- `01-10_Operations` — Maintenance-operations interfaces and turnarounds  
- `01-20_Subsystems` — Maintenance policy by subsystem domain  
- `01-30_ANCHORS` — Maintenance-related anchors (life limits, inspection anchors)  
- `01-40_Software` — Maintenance of software items and digital assets  
- `01-50_Structures` — Structural maintenance policy (inspections, repairs)  
- `01-60_Storages` — Spare parts, stocks, logistic storage policies  
- `01-70_Propulsion` — Engine/APU maintenance policy hooks  
- `01-80_Energy` — Maintenance of energy systems and circular assets  
- `01-90_Tables_Schemas_Diagrams` — Maintenance policy tables, schemas and diagrams

---

## 3. ATA 04 – AIRWORTHINESS LIMITATIONS (`ATA_04-AIRWORTHINESS_LIMITATIONS`)

**Purpose:** Organizational view of **airworthiness limitations** and their management.

### 3.1 Lifecycle Layer — `04-00_GENERAL`

Folders:

- `04-00-01_Overview` — Airworthiness limitations overall picture  
- `04-00-02_Safety` — Safety case aspects linked to airworthiness limitations  
- `04-00-03_Requirements` — Regulatory and internal requirements for limitations  
- `04-00-04_Design` — Design rules and constraints imposed by limitations  
- `04-00-05_Interfaces` — Interfaces with fleets, operators, authorities  
- `04-00-06_Engineering` — Analyses supporting limitations (fatigue, damage tolerance…)  
- `04-00-07_V_AND_V` — V&V of life limits, inspections and compliance evidence  
- `04-00-08_Prototyping` — Validation on prototypes/demonstrators  
- `04-00-09_Production_Planning` — Incorporation of limitations into production and configuration control  
- `04-00-10_Certification` — Formal airworthiness limitations declaration and updates  
- `04-00-11_EIS_Versions_Tags` — Versions and tags for limitations sets across EIS baselines  
- `04-00-12_Services` — Service bulletins and service information linked to limitations  
- `04-00-13_Subsystems_Components` — Limitations per subsystem/component  
- `04-00-14_Ops_Std_Sustain` — Operational and sustainability standards derived from limitations

### 3.2 Cross-ATA Buckets — `04-10` … `04-90`

- `04-10_Operations` — Ops procedures constrained by limitations  
- `04-20_Subsystems` — Airworthiness limitations by subsystem  
- `04-30_ANCHORS` — Limitation anchors (inspection milestones, life limits)  
- `04-40_Software` — Airworthiness-relevant software limitation aspects (if applicable)  
- `04-50_Structures` — Structural life limits and inspections  
- `04-60_Storages` — Storage-related limitations (time/condition-based)  
- `04-70_Propulsion` — Engine/APU life limits  
- `04-80_Energy` — Limitations for energy/circular assets if classified as airworthiness items  
- `04-90_Tables_Schemas_Diagrams` — Official limitations tables and schemas

---

## 4. ATA 05 – TIME LIMITS & MAINTENANCE CHECKS (`ATA_05-TIME_LIMITS_MAINTENANCE_CHECKS`)

**Purpose:** Organizational structure for **time limits and maintenance checks**.

### 4.1 Lifecycle Layer — `05-00_GENERAL`

Folders:

- `05-00-01_Overview` — Overview of time limits and maintenance checks  
- `05-00-02_Safety` — Safety rationale behind checks and intervals  
- `05-00-03_Requirements` — Regulatory and internal time-limit requirements  
- `05-00-04_Design` — Design assumptions feeding time-limit definitions  
- `05-00-05_Interfaces` — Interfaces to operators, MROs, CMS, MPD  
- `05-00-06_Engineering` — Analyses and reliability studies backing intervals  
- `05-00-07_V_AND_V` — Verification & validation of intervals and task sets  
- `05-00-08_Prototyping` — Trials / pilot programs for new check schemes  
- `05-00-09_Production_Planning` — Alignment of checks with production/configuration baselines  
- `05-00-10_Certification` — Authority approval path for maintenance programs  
- `05-00-11_EIS_Versions_Tags` — Tracking of changes vs EIS and fleet versions  
- `05-00-12_Services` — Service concepts tied to maintenance checks (e.g. PBH, by-the-hour)  
- `05-00-13_Subsystems_Components` — Time limits per subsystem/component  
- `05-00-14_Ops_Std_Sustain` — Ops standards and sustainability aspects (e.g. optimized check patterns)

### 4.2 Cross-ATA Buckets — `05-10` … `05-90`

- `05-10_Operations` — Integration of time limits into ops planning (OCC, schedule)  
- `05-20_Subsystems` — Subsystem-specific time limits and checks  
- `05-30_ANCHORS` — Anchor tasks, major checks, structural milestones  
- `05-40_Software` — Time or usage limits related to software where applicable  
- `05-50_Structures` — Structural checks (C/D checks, SHM-driven)  
- `05-60_Storages` — Shelf-life limits and storage checks  
- `05-70_Propulsion` — Engine/APU time limits and check cycles  
- `05-80_Energy` — Energy storage and circular container time limits  
- `05-90_Tables_Schemas_Diagrams` — MPD-style tables, schemas and check diagrams

---

## 5. How to Use the O-ORGANIZATION Skeleton

- Use **`00-00_*` / `01-00_*` / `04-00_*` / `05-00_*`** folders for **lifecycle-stage documents** at organizational level.  
- Use **`XX-10`…`XX-90`** folders for **cross-ATA, cross-system buckets** (operations, subsystems, software, etc.).  
- Keep all documents **tagged** in front-matter as:

```yaml
applicability: [O-Axis]
linked_ata:
  - ATA_00
  - ATA_01
  - ATA_04
  - ATA_05
axis: O
````

* Reference LC-05 and LC-03/LC-06 when the document has strong organizational/ops/finance ties.

This O-ORGANIZATION skeleton is the **organizational spine**: all policies, limitations, and maintenance philosophies should attach here before being propagated to other axes and LC channels.

```
::contentReference[oaicite:0]{index=0}
```
