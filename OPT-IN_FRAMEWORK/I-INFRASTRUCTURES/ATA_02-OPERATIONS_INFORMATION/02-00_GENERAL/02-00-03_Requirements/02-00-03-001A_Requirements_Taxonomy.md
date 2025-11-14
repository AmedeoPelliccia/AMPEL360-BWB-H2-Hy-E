---
Title: "Requirements Taxonomy — ATA 02"
Identifier: "AMPEL360-02-00-03-001A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
Language: "en"
CreatedAt: "2025-11-14"
ModifiedAt: "2025-11-14"
Abstract: "Controlled categories, tags and vocabularies for ATA 02 requirements authoring and governance."
Keywords: ["Taxonomy","Types","Tags","Vocabulary","ATA 02"]
Compliance:
  - "AMPEL360 Documentation Standard v1.1"
Links:
  Master: "./02-00-03-002A_Master_Requirements.csv"
  VCRM: "./02-00-03-004A_VCRM.csv"
  RTM: "./02-00-03-003A_Requirements_Traceability_Matrix.csv"
ChangeLog:
  - { version: "1.0.0", date: "2025-11-14", author: "AMPEL360 Documentation Team", change: "Initial taxonomy" }
---

# Requirements Taxonomy — ATA 02

## 1) Types

Use `Type` to classify requirements:

- **FR** — Functional Requirement (operational behaviour, procedures, workflows).
- **NFR** — Non‑Functional Requirement (performance, reliability, maintainability, usability).
- **SAF** — Safety Requirement (from FHA/FMEA/FTA/CCA/safety objectives).
- **DATA** — Data/records requirement (integrity, retention, logging, auditability).
- **PROC** — Process/governance requirement (reviews, training, publication rules).

## 2) Criticality, DAL and Priority

- For safety‑driven requirements:
  - Use **DAL** A/B/C/D/E where applicable, aligned with `02-00-02_Safety` and ARP4754A/ARP4761 flow‑down.
- For all requirements:
  - Use **Priority**:
    - `MUST` — mandatory for compliance with safety/certification or key operational objectives.
    - `SHOULD` — strongly recommended; deviations require justification.
    - `COULD` — desirable; opportunistic improvements.

## 3) Verification Method (for VCRM)

Verification methods (`VerificationMethod` / shorthand in VCRM):

- **TST** — Test (simulation, integration test, system test, field trial).
- **ANL** — Analysis (analytical proof, modelling, data analysis).
- **REV** — Review (document/code review, safety case review).
- **INS** — Inspection (checklist‑based inspection of artefacts or processes).

Multiple methods may be used; choose the **primary** one for VCRM, and note others in `Notes`.

## 4) Controlled Tags (examples)

Use tags in `Text` or `CrossATARefs` / `Links` for filtering and CI checks:

- Operational context:
  - `turnaround`, `de-icing`, `degraded-ops`, `NOTAM`, `AODB`, `stand-allocation`
- Environment:
  - `hot-high`, `cold-soak`, `Cat-III`, `ETOPS-like`
- Infrastructure and energy:
  - `FEGP`, `H2-GSE`, `APU-off`
- Safety & monitoring:
  - `monitoring`, `ERP`, `HF`, `NN`, `training`, `deployment`

Projects may extend this list but should avoid redefining existing tags.

## 5) ID Patterns

- `ReqID`: `REQ-02-###` (e.g. `REQ-02-001`)
- `TestID`: `TR-02-<Family>-###` (e.g. `TR-02-Perf-001`, `TR-02-Proc-021`)
- `CertID`: `CERT-02-###`
- Hazards (if used here): `HZ-02-####`
- ODD entries: `ODD-##` (see Applicability Matrix)

All IDs must be **unique within ATA 02** and stable once used in V&V or certification.

```det
hash: "<ci>"
kpis:
  allowed_types: ["FR","NFR","SAF","DATA","PROC"]
  allowed_verify: ["TST","ANL","REV","INS"]
  id_regex:
    req: "^REQ-02-\\d{3}$"
    odd: "^ODD-\\d{2}$"
producer: "AMPEL360 Doc CI"
```

---

## What to do next / how to approach this

- When proposing a new requirement, first pick:
  - `Type` from the allowed list.
  - `Priority` and (if safety‑driven) `DAL`.
- Ensure your `ReqID` and `TestID` follow the patterns above.
- CI can use the `id_regex` and `allowed_types` to lint `02-00-03-002A_Master_Requirements.csv` and `02-00-03-004A_VCRM.csv`.
