---
Title: "Purpose & Scope — ATA 02 General"
Identifier: "AMPEL360-02-00-01-001A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-11-13"
ModifiedAt: "2025-11-13"
ReviewDue: "2026-05-13"
Scope: "Overview for ATA 02-00 General layer within I-INFRASTRUCTURES"
Abstract: "Defines the purpose and scope of ATA 02 Operations Information within the OPT-IN I-axis."
Keywords: ["ATA 02","Operations Information","General","Overview","OPT-IN","I-Infrastructures"]
Effectivity: "TBD (Q100 INTEGRA variants)"
Compliance:
  - "ATA iSpec 2200"
  - "S1000D"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentGeneral: "../"
  Siblings:
    - "../02-00-02_Safety/"
    - "../02-00-03_Requirements/"
    - "../02-00-04_Design/"
    - "../02-00-05_Interfaces/"
    - "../02-00-06_Engineering/"
    - "../02-00-07_V_AND_V/"
    - "../02-00-08_Prototyping/"
    - "../02-00-09_Production_Planning/"
    - "../02-00-10_Certification/"
    - "../02-00-11_EIS_Versions_Tags/"
    - "../02-00-12_Services/"
    - "../02-00-13_Subsystems_Components/"
    - "../02-00-14_Ops_Std_Sustain/"
  CrossATABuckets:
    - "../../02-10_Operations/"
    - "../../02-20_Subsystems/"
    - "../../02-30_Circularity/"
    - "../../02-40_Software/"
    - "../../02-50_Structures/"
    - "../../02-60_Storages/"
    - "../../02-70_Propulsion/"
    - "../../02-80_Energy/"
    - "../../02-90_Tables_Schemas_Diagrams/"
ChangeLog:
  - { version: "1.0.0", date: "2025-11-13", author: "AMPEL360 Documentation Team", change: "Initial creation" }
---

# Purpose & Scope

## Purpose
Establish the operational information baseline for the AMPEL360 program, ensuring consistent, certifiable, and traceable **operations content** across infrastructure-driven topics.

## Scope
- **In-scope:** turnaround rules, handling/servicing constraints, operating envelopes, airport/infrastructure interfaces, cross-references to system-specific operations content.
- **Out-of-scope:** detailed design, subsystem internal engineering (owned by their technical ATA chapters).

## Interfaces
- Links to buckets in this chapter (e.g., `02-10_Operations`) and to other ATA chapters (e.g., **03** Support/GSE, **10** Parking/Storage/RTS).
- Traceability hooks to:
  - **Requirements:** `../02-00-03_Requirements/`
  - **V&V:** `../02-00-07_V_AND_V/`
  - **Certification:** `../02-00-10_Certification/`

## Acceptance Criteria (for this subject)
- Metadata present and valid (identifier format, ISO8601 dates, allowed `Status`/`AccessLevel`).
- Scope clearly separates **ops context** from **design content**.
- Links to at least **Applicability Matrix** and **Safety** subjects exist:
  - `./02-00-01-002A_Applicability_Matrix.md`
  - `../02-00-02_Safety/`

---

```det
hash: "<to-be-filled-by-CI>"
kpis:
  refs_ok: true
  metadata_complete: true
  lint_warnings: 0
trace:
  requirements_ref: "../02-00-03_Requirements/"
  vv_ref: "../02-00-07_V_AND_V/"
  cert_ref: "../02-00-10_Certification/"
producer: "AMPEL360 Doc CI"
