# 02-10-00_GLOBAL_OPERATIONS — Global Operational Framework

**ATA Chapter:** ATA_02-OPERATIONS_INFORMATION  
**Bucket:** 10_Operations (Operational use, turnarounds, procedures)  
**Code:** 02-10-00_GLOBAL_OPERATIONS  

---

## 1. Purpose

`02-10-00_GLOBAL_OPERATIONS` defines the **global operational framework** for the
AMPEL360 program from the perspective of **Operations Information (ATA 02)**.

It provides a **program-level, aircraft-agnostic** view of:

- How AMPEL360 flights are structured gate-to-gate  
- Which operational concepts are considered “standard” for the BWB H₂ Hy-E family  
- How operational information in ATA 02 is intended to be **used** by crews,
  dispatch, maintenance and CAOS services

This folder is **not** an airline OM-A/OM-B replacement; it is the **baseline
operational reference** on top of which operator-specific manuals are built.

---

## 2. Scope

Included in this folder:

- High-level **gate-to-gate operational model** (from aircraft power-up to shutdown)
- Definition of **phases of flight** as used by AMPEL360 (taxi-out, take-off, climb,
  cruise, descent, approach, taxi-in, turnaround)
- Standard **mission profiles** (e.g. short-range, nominal range, extended range)
- Global **roles and responsibilities** (flight crew, ground crew, dispatch) in
  relation to ATA 02 information
- How operational data flows between **aircraft, ground, fleet, and CAOS**

Explicitly **out of scope** here:

- Detailed step-by-step normal/abnormal/emergency procedures  
  → These live in dedicated folders (e.g. `02-10-01_NORMAL_OPERATIONS/`,
  `02-10-02_ABNORMAL_OPERATIONS/`, `02-10-03_EMERGENCY_OPERATIONS/`).
- Detailed performance numbers, envelopes, and limitations  
  → Owned by `02-20_Subsystems/` (performance, W&B, limitations) and their
  underlying system chapters.
- Operator-specific policies, union agreements, rostering, etc.

---

## 3. Position in the OPT-IN Framework

- **Axis:** I — Infrastructures  
- **Chapter:** ATA_02-OPERATIONS_INFORMATION  
- **Bucket:** `02-10_Operations` (operational use, turnarounds, procedures)

Relationship to other elements:

- `02-00-00_GENERAL/`  
  Provides governance, safety, requirements, lifecycle and certification framework
  for Operations Information.

- `02-10-00_GLOBAL_OPERATIONS/` *(this folder)*  
  Provides the **global operational model** and common language for all other
  `02-10-xx_…` operational topics.

- `02-20_Subsystems/`  
  Owns detailed **systems, performance models and data** used by operations
  (weight & balance, performance tables, flight planning, limitations).

- CAOS / AirCCC  
  Uses the operational model defined here as the **semantic backbone** for telemetry,
  KPIs and advisory services.

---

## 4. Intended Stakeholders

- **Flight Operations engineering** (defining operating profiles and policies)
- **Flight crew training** (to derive OM-A / OM-B content)
- **Dispatch / Network operations** (to map schedule and payload assumptions)
- **Maintenance planning** (for turnaround and utilization assumptions)
- **CAOS / AirCCC teams** (for channel design and KPI definition)
- **Certification & liaison teams** (to explain how the aircraft is intended to be used)

---

## 5. Suggested Contents of This Folder

Recommended child files (can evolve over time):

1. `02-10-00_Global_Operations_Concept.md`  
   - Narrative description of the global operational concept for AMPEL360  
   - Typical mission profiles and utilisation assumptions  
   - Relationship to hydrogen infrastructure and network design

2. `02-10-00_Phases_of_Flight_Model.md`  
   - Formal definition of phases of flight used in ATA 02 and CAOS  
   - Entry/exit conditions for each phase  
   - Links to performance and limitations in `02-20_Subsystems/`

3. `02-10-00_Gate_to_Gate_Flow_Diagram.md` (or `.svg` in `ASSETS/`)  
   - Visual gate-to-gate flow including ground, flight, and turnaround segments

4. `02-10-00_Roles_and_Responsibilities.md`  
   - RACI-style view (crew, ground, maintenance, dispatch)  
   - Which roles consume which ATA 02 information in which phase

5. `ASSETS/`  
   - `ASSETS/DIAGRAMS/` — operational flow diagrams, swimlanes  
   - `ASSETS/TABLES/` — high-level operational profiles, utilisation tables

You can create these gradually; this README should remain the **stable entry point**.

---

## 6. Cross-References

**Within ATA 02:**

- `../02-00-00_GENERAL/` — governance, safety and lifecycle for Operations Information  
- `../02-20_Subsystems/` — performance, limitations, weight & balance, flight planning  
- `../02-90_Tables_Schemas_Diagrams/` — any schemas and tables referenced from here

**Other ATA chapters (examples):**

- `../../ATA_03-SUPPORT_INFORMATION_GSE/` — ground support equipment and refuelling ops  
- `../../ATA_28-HYDROGEN_FUEL_SYSTEM/` (when instantiated) — hydrogen system behaviour  
- `../../ATA_71-POWER_PLANT/` — fuel cell powerplant operational constraints

**CAOS / AirCCC:**

- `../../../CAOS/CAOS_INDEX.md` — definition of CAOS layers and channels  
- `../../../CAOS/CAOS_OPERATIONS_FRAMEWORK.md` — operational playbook and roles

---

## 7. Document Control

> **Status:** Draft / Placeholder  
> **Owner:** AMPEL360 Operations Information Working Group  
> **Change Policy:**  
> - Structural changes to this folder require review by:
>   - ATA 02 technical authority  
>   - CAOS architecture lead (for consistency with channels and KPIs)  
> - Content should remain **airline-agnostic** and focused on aircraft/program level.

A more formal table can be added later:

| Version | Date       | Author / Team                         | Changes                      |
|---------|------------|----------------------------------------|------------------------------|
| 0.1     | YYYY-MM-DD | AMPEL360 Operations Information WG    | Initial folder definition    |
