# 02-10-01_NORMAL_OPERATIONS — Normal Operations

**Axis:** I — Infrastructures  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../)  
**Bucket:** [02-10_Operations](../README.md) (Operational use, turnarounds, procedures)  
**Code:** 02-10-01_NORMAL_OPERATIONS  

---

## 1. Purpose

`02-10-01_NORMAL_OPERATIONS` defines **program-level normal operations** for
AMPEL360, using the information provided by ATA 02:

- Gate-to-gate sequence from **power-up to shutdown**  
- Standard **phases of flight** for the AMPEL360 BWB H₂ Hy-E family  
- Crew and ground interactions with **Operations Information (ATA 02)**  
- How normal operations are observed and supported by **CAOS / AirCCC**

This material is **airline-agnostic**: it is a *baseline* for OM-A/OM-B,
not an operator-specific manual.

---

## 2. Scope

Included:

- High-level **normal operations flow** (gate, taxi-out, take-off, climb,
  cruise, descent, approach, taxi-in, turnaround)
- Use of key data from ATA 02 during each phase:
  - Weight & balance
  - Performance and limitations
  - Flight planning artefacts
- Interaction with **hydrogen-specific constraints** (refuelling status,
  tank conditions, CO₂ battery operating windows)
- Normal use of **CAOS advisory outputs** (if any) by crew and dispatch

Out of scope:

- Detailed non-normal and emergency operations  
  → see [`02-10-02_ABNORMAL_OPERATIONS/`](../02-10-02_ABNORMAL_OPERATIONS/) and  
  [`02-10-03_EMERGENCY_OPERATIONS/`](../02-10-03_EMERGENCY_OPERATIONS/)

- Detailed performance tables and envelopes  
  → see [`../../02-20-00_SYSTEMS/`](../../02-20-00_SYSTEMS/) (performance, W&B, flight planning)

- Engineering analyses (FEA/CFD/etc.)  
  → see [`../../02-00-00_GENERAL/02-00-06_ENGINEERING/`](../../02-00-00_GENERAL/02-00-06_ENGINEERING/)

---

## 3. Position in the OPT-IN / ATA Structure

- **General lifecycle** (governance, safety, requirements, etc.)  
  → [`../../02-00-00_GENERAL/`](../../02-00-00_GENERAL/)

- **Operations bucket root**  
  → [`../README.md`](../README.md)

- **Systems and performance**  
  → [`../../02-20-00_SYSTEMS/`](../../02-20-00_SYSTEMS/)  
    (e.g. performance, weight & balance, limitations, flight planning)

- **CAOS / AirCCC operational intelligence**  
  - [CAOS Index](/CAOS/CAOS_INDEX.md)  
  - [CAOS Operations Framework](/CAOS/CAOS_OPERATIONS_FRAMEWORK.md)

For cross-ATA bucket rules and naming conventions see:  
- [OPT-IN_FRAMEWORK_STANDARD.md](/OPT-IN_FRAMEWORK_STANDARD.md)

---

## 4. Suggested Internal Contents

Recommended files and substructure inside this folder:

- `02-10-01_Normal_Ops_Gate_to_Gate.md`  
  - Narrative gate-to-gate description (from “cold & dark” or “turnaround” to shutdown)  
  - Highlights where ATA 02 data is read / updated in each step  
  - Links to performance and W&B artefacts in `02-20-00_SYSTEMS/`

- `02-10-01_Phases_of_Flight_Normal.md`  
  - Definition of phases of flight used for normal ops (e.g. `PREFLIGHT`, `TAXI_OUT`,
    `TAKEOFF`, `CLIMB`, `CRUISE`, `DESCENT`, `APPROACH`, `LANDING`, `TAXI_IN`)  
  - Entry/exit conditions and key ATA 02 data needed in each phase  
  - Mapping to CAOS telemetry / event markers (if applicable)

- `02-10-01_Crew_Information_Use.md`  
  - What information (from ATA 02) is expected to be presented to crew  
  - At which phase, and via which interface (EFB, cockpit displays, manuals, etc.)  
  - Relationship to operator OM-A/OM-B/QRH

- `ASSETS/`  
  - `ASSETS/DIAGRAMS/02-10-01-Gate_to_Gate_Flow.svg`  
  - `ASSETS/TABLES/02-10-01-Phase_vs_Data_Map.md`

These artefacts should stay **free of airline-specific policies** and focus on
the **aircraft/program design intent**.

---

## 5. Links to Other Buckets and Chapters

**Within ATA 02**

- Governance, safety, lifecycle:  
  → [`../../02-00-00_GENERAL/`](../../02-00-00_GENERAL/)

- Systems / data providers used during normal ops (examples):  
  - Performance data, operating limitations, flight planning:  
    → [`../../02-20-00_SYSTEMS/`](../../02-20-00_SYSTEMS/)  
  - Operational procedures catalogues and tables:  
    → [`../../02-90_Tables_Schemas_Diagrams/`](../../02-90_Tables_Schemas_Diagrams/)

**Other ATA chapters typically referenced**

(These may evolve as the project matures and folders are created.)

- Hydrogen fuel system operational aspects: `ATA_28-…`  
- Fuel cell powerplant operations: `ATA_71-…`  
- Doors / emergency exits in normal configuration: `ATA_52-DOORS`  
- Support and GSE operations: `ATA_03-SUPPORT_INFORMATION_GSE`

When adding references, use **relative links** into the corresponding
chapter once its structure is instantiated.

---

## 6. CAOS Integration

Normal operations are expected to be **observable by CAOS**. This folder
should, over time, document:

- Which **events / phases** are emitted into CAOS channels (e.g. phase changes,
  key configuration changes, H₂ status milestones)
- Which **KPIs** are computed on top of normal ops (on-time performance,
  hydrogen usage per sector, CO₂ captured per flight, etc.)
- How CAOS advisory outputs (if any) are **presented to crew/dispatch** in
  normal operations, and under what authority limitations

Reference documents:

- [CAOS Index](/CAOS/CAOS_INDEX.md)  
- [CAOS Operations Framework](/CAOS/CAOS_OPERATIONS_FRAMEWORK.md)

---

## 7. Conventions

- Code format: `02-10-01_Description` for all items owned here.  
- Do **not** duplicate detailed data already owned by:
  - `02-20-00_SYSTEMS/` (performance, W&B, limitations, planning)  
  - System-specific ATA chapters (e.g. ATA 28, 71, 52, …)  
- Always include at least:
  - A clear **Scope** section  
  - A **Links / Cross-References** section  
  - A **CAOS Integration** note (even if “Not yet applicable”)

---

## 8. Document Control

> **Status:** Draft / Placeholder  
> **Owner:** AMPEL360 Operations Information Working Group  
> **Applies to:** Normal operations (program level) for AMPEL360 BWB H₂ Hy-E

A formal control table can be added later:

| Version | Date       | Author / Team                         | Changes                                 |
|---------|------------|----------------------------------------|-----------------------------------------|
| 0.1     | YYYY-MM-DD | AMPEL360 Operations Information WG    | Initial definition of normal operations |
