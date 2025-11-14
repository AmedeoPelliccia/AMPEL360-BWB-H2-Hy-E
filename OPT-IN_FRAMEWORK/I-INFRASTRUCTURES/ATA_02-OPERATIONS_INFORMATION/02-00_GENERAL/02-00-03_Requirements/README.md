---
Title: "Requirements — ATA 02 General"
Identifier: "AMPEL360-02-00-03-README"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-11-14"
ModifiedAt: "2025-11-14"
Abstract: "Master location for requirements under ATA 02-00 General: taxonomy, master list, traceability, VCRM and change control."
Keywords: ["ATA 02","Requirements","Traceability","VCRM","ODD"]
Compliance:
  - "ATA iSpec 2200"
  - "S1000D"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentGeneral: "../"
  Siblings:
    - "../02-00-01_Overview/"
    - "../02-00-02_Safety/"
    - "../02-00-07_V_AND_V/"
    - "../02-00-10_Certification/"
  CrossRefs:
    Applicability: "../02-00-01_Overview/02-00-01-002A_Applicability_Matrix.md"
    HazardLog: "../02-00-02_Safety/AMPEL360-02-00-02_Hazards.csv"
ChangeLog:
  - { version: "1.0.0", date: "2025-11-14", author: "AMPEL360 Documentation Team", change: "Initial structure and templates" }
---

# Requirements — ATA 02

## Purpose

Provide the complete **requirements system** for ATA 02 (Operations Information), including:

- **Taxonomy** (types & tags)
- **Master list** (authoritative requirements set)
- **Traceability** (RTM)
- **Verification matrix** (VCRM)
- **Change control** (controlled log)

Requirements here are the main bridge between:

- Safety artefacts in `../02-00-02_Safety/`
- Design/ops content in `../../02-10_Operations/`
- V&V in `../02-00-07_V_AND_V/`
- Certification and EIS/versioning in `../02-00-10_Certification/` and `../02-00-11_EIS_Versions_Tags/`

---

## Artefacts

- `02-00-03-001A_Requirements_Taxonomy.md` — types, tags, vocabularies
- `02-00-03-002A_Master_Requirements.csv` — canonical requirements list (single source of truth)
- `02-00-03-003A_Requirements_Traceability_Matrix.csv` — RTM (Req ↔ Design/Implementation/Test/Safety/Cert)
- `02-00-03-004A_VCRM.csv` — Verification Cross Reference Matrix
- `02-00-03-005A_Change_Control_Log.csv` — CM entries for requirement changes
- `02-00-03-006A_Requirements_Quality_Checklist.md` — author/reviewer checklist

---

## Acceptance Criteria (Folder-Level)

- Metadata valid; all files present and correctly named.
- Every requirement in the master CSV has:
  - `ReqID` (unique, matches taxonomy pattern)
  - `Type`, `Priority`, `Owner`, `Status`
  - Clear `Text` and `AcceptanceCriteria`
  - `ODD_ID` where applicable (see Applicability Matrix)
  - Upstream links: at least one hazard or source where safety‑relevant
  - Downstream links: at least one test and/or certification reference where relevant.
- No orphan **high‑criticality** requirements (every SAF/DAL‑relevant item has:
  - Traceability row in RTM
  - At least one VCRM entry).
- VCRM coverage for all DAL‑relevant items is ≥ the program's target threshold.

```det
hash: "<to-be-filled-by-CI>"
kpis:
  req_count: 3
  odd_tagged_pct: 100
  vcrm_coverage_pct: 100
  metadata_complete: true
producer: "AMPEL360 Doc CI"
```

---

## What to do next / how to approach this

- Add or update requirements only in `02-00-03-002A_Master_Requirements.csv`.
- When adding a requirement:
  - Ensure ID and fields conform to `02-00-03-001A_Requirements_Taxonomy.md`.
  - Add corresponding entries in the RTM and VCRM CSVs.
  - Create or update an entry in `02-00-03-005A_Change_Control_Log.csv` for non‑trivial edits.
- Use `02-00-03-006A_Requirements_Quality_Checklist.md` during reviews and as a basis for CI linting.