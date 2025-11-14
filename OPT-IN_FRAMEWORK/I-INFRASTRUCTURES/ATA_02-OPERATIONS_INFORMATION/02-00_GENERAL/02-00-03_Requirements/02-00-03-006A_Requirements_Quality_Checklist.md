---
Title: "Requirements Quality Checklist — ATA 02"
Identifier: "AMPEL360-02-00-03-006A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
Language: "en"
CreatedAt: "2025-11-14"
ModifiedAt: "2025-11-14"
Abstract: "Author/reviewer checklist to ensure clarity, testability, traceability and applicability tagging for ATA 02 requirements."
Keywords: ["Checklist","Quality","Lint","ATA 02"]
Links:
  Master: "./02-00-03-002A_Master_Requirements.csv"
  VCRM: "./02-00-03-004A_VCRM.csv"
  RTM: "./02-00-03-003A_Requirements_Traceability_Matrix.csv"
ChangeLog:
  - { version: "1.0.0", date: "2025-11-14", author: "AMPEL360 Documentation Team", change: "Initial checklist" }
---

# Requirements Quality Checklist (ATA 02)

Use this checklist when authoring or reviewing any requirement in `02-00-03-002A_Master_Requirements.csv`.

- [ ] **Unique ID**
  - `ReqID` follows `REQ-02-###` pattern and is not reused.
- [ ] **Clear title**
  - Short, descriptive, and aligned with the main obligation.
- [ ] **Type and Priority**
  - `Type` ∈ {FR, NFR, SAF, DATA, PROC}.
  - `Priority` ∈ {MUST, SHOULD, COULD}.
- [ ] **Safety / DAL (if applicable)**
  - For safety‑driven requirements, `DAL` is set and consistent with safety flow‑down.
- [ ] **Text**
  - Single clear obligation per requirement.
  - Unambiguous, measurable, and free of "etc." / "as appropriate" wording.
- [ ] **Acceptance Criteria**
  - Objective, testable, and linked to V&V artefacts (e.g. `AC-02-0xx`).
- [ ] **ODD_ID**
  - Assigned if requirement is ODD‑specific; otherwise explicitly marked as `Global`.
- [ ] **Traceability**
  - `Source` references at least one hazard, stakeholder need or regulation.
  - `SafetyRefs` populated for safety‑relevant requirements.
  - `TestRefs` and `CertRefs` populated or planned for DAL‑relevant items.
- [ ] **Cross‑ATA References**
  - `CrossATARefs` used when another ATA owns part of the implementation.
- [ ] **Status**
  - Reflects lifecycle: Draft / Reviewed / Approved / Deprecated.
- [ ] **Change Control**
  - Non‑trivial edits have a corresponding entry in `02-00-03-005A_Change_Control_Log.csv`.

```det
hash: "<ci>"
kpis:
  checklist_items: 11
  blocking_items: 7
producer: "AMPEL360 Doc CI"
```

---

## What to do next / how to approach this

- Integrate this checklist into:
  - PR templates for requirements changes.
  - CI linting (e.g. block merges if key fields are missing for SAF/MUST items).
- Over time, refine which items are **blocking** vs **advisory** based on project experience.
