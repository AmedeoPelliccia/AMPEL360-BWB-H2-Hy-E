---
Title: "Applicability Matrix — ATA 02"
Identifier: "AMPEL360-02-00-01-002A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-11-13"
ModifiedAt: "2025-11-13"
ReviewDue: "2026-05-13"
Effectivity: "Q100 INTEGRA (TBD variants)"
Abstract: "Matrix describing applicability of operational information by aircraft configuration, mission profile, operating environment, and airport class."
Keywords: ["Applicability","ODD","Operations","Scope","ATA 02"]
Compliance:
  - "ATA iSpec 2200"
  - "S1000D"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentGeneral: "../"
  Siblings:
    - "./02-00-01-001A_Purpose_Scope.md"
  CrossRefs:
    Requirements: "../02-00-03_Requirements/"
    Certification: "../02-00-10_Certification/"
    Safety: "../02-00-02_Safety/"
  CrossATABuckets:
    - "../../02-10_Operations/"
    - "../../02-20_Subsystems/"
    - "../../02-90_Tables_Schemas_Diagrams/"
ChangeLog:
  - { version: "1.0.0", date: "2025-11-13", author: "AMPEL360 Documentation Team", change: "Initial creation" }
---

# Applicability Matrix (ATA 02)

> Use this table to declare **where the operational information applies within the Operational Design Domain (ODD)**.  
> Each row corresponds to a **coherent applicability slice** (aircraft config × mission × environment × airport class).

| RowID | ODD ID | Aircraft Config  | Mission Profile | Environment & Altitude        | Airport Class | Applicability Notes              | Evidence Ref(s)          |
|-----:|:-------|:------------------|:----------------|:------------------------------|:--------------|:---------------------------------|:-------------------------|
| 01   | ODD-01 | BWB Q100 INTEGRA  | Design Range    | ISA @ FL350–410               | Cat C/D       | Nominal operations               | REQ-02-001; CERT-02-010  |
| 02   | ODD-02 | BWB Q100 INTEGRA  | Short-range     | Hot/High (≥ ISA+20; >6k ft)   | Cat B/C       | Thrust derating required         | REQ-02-015               |
| 03   | ODD-03 | BWB Q100 INTEGRA  | ETOPS-like      | Cold-soaked (≤ ISA−30)        | Cat C/D       | Additional de-icing handling     | REQ-02-021; CERT-02-034  |

> **NOTE:** The values above are examples. Replace with program-authoritative ODD slices and references.

---

## Guidance

### Purpose
- This matrix **scopes applicability** of all documentation under ATA 02 (and referenced sections).  
- It is the **bridge** between:
  - `02-00-03_Requirements` (what must hold), and  
  - `02-00-10_Certification` (how conformity is shown).

### How to populate rows
1. Start from your **ODD definition**: list distinct combinations of aircraft configuration, mission, environment, and airport class relevant to the document.
2. Assign a **stable `ODD ID`** per distinct slice (e.g., `ODD-01`, `ODD-02`) and reuse that ID in:
   - requirements tables in `02-00-03_Requirements`, and
   - compliance tables in `02-00-10_Certification`.
3. Fill **Applicability Notes** with concise statements:
   - operational limitations;
   - additional procedures/mitigations;
   - explicit exclusions (*“Not applicable for …”*).
4. Add **Evidence Ref(s)**:
   - Requirement IDs (e.g., `REQ-02-xxx`);
   - Certification artefacts (e.g., `CERT-02-xxx`);
   - Supporting analyses/simulations (e.g., `ANALYSIS-ENV-xx`).

### Extending the matrix (optional columns)
- **Turnaround Time Class** (short/standard/extended)
- **Ground Power Source** (APU/FEGP/Hybrid/H₂ GSE)
- **Runway Condition** (dry/wet/contaminated)
- **Airspace Type** (controlled/uncontrolled; PBN class)
- **Crew Min Category** (Cat I/II/III if relevant to Ops info)

> When adding columns: prefer **categorical values**; keep names consistent across ATAs when comparable.

### Consistency rules
- If a requirement/procedure is **only applicable** to some ODD slices, reference the **`RowID`/`ODD ID`** directly.
- If globally applicable, either:
  - add an explicit row (e.g., `ODD-00 – All certified configurations`), or
  - state “Global applicability” in the referencing document.
- Avoid overlapping/ambiguous slices.

### Workflow suggestion
1. **Define ODD IDs**: align with the top-level ODD list and register the canonical `ODD-xx` identifiers.
2. **Update this matrix** with approved slices and references.
3. **Back-propagate IDs**:
   - Tag requirements in `02-00-03_Requirements` with relevant `ODD ID`s.
   - Tag certification items in `02-00-10_Certification` with the same `ODD ID`s.
4. **Review for gaps**:
   - Every ODD slice here should have ≥1 linked requirement and (where needed) certification evidence.
   - Harmonize any slice referenced elsewhere but missing here.

---

## Validation rules (for CI/CSDB)

- **RowID**: integer, unique.
- **ODD ID**: `^ODD-\d{2}$`, unique across this matrix.
- **Aircraft Config / Mission / Environment / Airport Class**: non-empty, controlled vocabulary where available.
- **Evidence Ref(s)**: at least one ID; each must match known patterns (e.g., `^REQ-02-\d{3}$`, `^CERT-02-\d{3}$`).
- **Cross-links**: for every `ODD ID`, at least one reference exists in `../02-00-03_Requirements/` or `../02-00-10_Certification/`.

---

## Acceptance Criteria (for this subject)

- Metadata valid (identifier format, ISO dates, allowed enums).
- Table has ≥1 approved ODD slice.
- No duplicate `RowID` or `ODD ID`.
- All `Evidence Ref(s)` resolve to existing artefacts or tracked placeholders.
- Links to **Requirements**, **Certification**, and **Safety** folders present.

---

```det
hash: "<to-be-filled-by-CI>"
kpis:
  matrix_rows: 3
  odd_ids_unique: true
  evidence_refs_present: true
  metadata_complete: true
trace:
  requirements_ref: "../02-00-03_Requirements/"
  certification_ref: "../02-00-10_Certification/"
  safety_ref: "../02-00-02_Safety/"
producer: "AMPEL360 Doc CI"
