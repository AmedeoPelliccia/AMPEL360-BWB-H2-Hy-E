---
Title: "Applicability Matrix — ATA 03"
Identifier: "AMPEL360-03-00-01-002A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
ReviewDue: "2026-06-07"
Effectivity: "Q100 INTEGRA (TBD variants)"
Abstract: "Matrix describing applicability of GSE and support information by aircraft configuration, airport class, ground infrastructure capability, and operational environment."
Keywords: ["Applicability","GSE","Ground Support Equipment","Airport Infrastructure","Scope","ATA 03"]
Compliance:
  - "ATA iSpec 2200"
  - "S1000D"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentGeneral: "../"
  Siblings:
    - "./03-00-01-001A_Purpose_Scope.md"
  CrossRefs:
    Requirements: "../03-00-03_Requirements/"
    Certification: "../03-00-10_Certification/"
    Safety: "../03-00-02_Safety/"
  CrossATABuckets:
    - "../../03-10_Operations/"
    - "../../03-20_Subsystems/"
    - "../../03-90_Tables_Schemas_Diagrams/"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial creation" }
---

# Applicability Matrix (ATA 03)

> Use this table to declare **where the GSE and support information applies** within different operational contexts.  
> Each row corresponds to a **coherent applicability slice** (aircraft config × airport class × H₂ infrastructure × ground power capability).

| RowID | GSE-ID | Aircraft Config  | Airport Class | H₂ Infrastructure | Ground Power Capability | Applicability Notes                          | Evidence Ref(s)          |
|-----:|:-------|:------------------|:--------------|:------------------|:------------------------|:---------------------------------------------|:-------------------------|
| 01   | GSE-01 | BWB Q100 INTEGRA  | Cat D         | Fixed H₂ hydrant  | 400Hz AC + DC fast charge | Full-service hub airport with H₂ infrastructure | REQ-03-001; CERT-03-010  |
| 02   | GSE-02 | BWB Q100 INTEGRA  | Cat C         | Mobile H₂ bowser  | 400Hz AC + slow charge  | Regional airport with mobile H₂ support      | REQ-03-015; SAFE-03-012  |
| 03   | GSE-03 | BWB Q100 INTEGRA  | Cat B         | Mobile H₂ bowser  | GPU only (no DC charge) | Small airport; limited charging capability   | REQ-03-021; OPS-03-008   |
| 04   | GSE-04 | BWB Q100 INTEGRA  | Cat C/D       | Any H₂ type       | With thermal management | Cold weather operations (≤ −20°C)           | REQ-03-028; SAFE-03-019  |
| 05   | GSE-05 | BWB Q100 INTEGRA  | Cat C/D       | Any H₂ type       | Enhanced cooling        | Hot weather operations (≥ ISA+20)            | REQ-03-032; SAFE-03-022  |

> **NOTE:** The values above represent initial applicability slices. These will be refined with program-specific operational design domain (ODD) data and airport capability surveys.

---

## Guidance

### Purpose
- This matrix **scopes applicability** of all GSE specifications and support documentation under ATA 03.
- It is the **bridge** between:
  - `03-00-03_Requirements` (GSE functional and performance requirements), and
  - `03-00-10_Certification` (how GSE compliance and safety is demonstrated).

### How to populate rows
1. Start from your **GSE operational domain**: list distinct combinations of aircraft configuration, airport class, H₂ infrastructure type, and ground power capability.
2. Assign a **stable `GSE-ID`** per distinct slice (e.g., `GSE-01`, `GSE-02`) and reuse that ID in:
   - requirements tables in `03-00-03_Requirements`,
   - safety analyses in `03-00-02_Safety`, and
   - compliance tables in `03-00-10_Certification`.
3. Fill **Applicability Notes** with concise statements:
   - GSE configuration variations;
   - operational limitations or constraints;
   - additional procedures/mitigations required;
   - explicit exclusions (*"Not applicable for …"*).
4. Add **Evidence Ref(s)**:
   - Requirement IDs (e.g., `REQ-03-xxx`);
   - Safety items (e.g., `SAFE-03-xxx`);
   - Operational procedures (e.g., `OPS-03-xxx`);
   - Certification artefacts (e.g., `CERT-03-xxx`);
   - Supporting analyses (e.g., `ANALYSIS-GSE-xx`).

### Extending the matrix (optional columns)

Consider adding columns for:
- **Turnaround Type** (quick turn / standard / overnight / extended maintenance)
- **H₂ Refueling Rate** (kg/min — affects turnaround time)
- **Battery Charging Rate** (kW — DC fast charge vs. slow charge)
- **Cargo Configuration** (full cargo / mixed / passenger only)
- **Maintenance Access Level** (line maintenance / base maintenance)
- **Environmental Conditions** (temperature range, humidity, altitude)

> When adding columns: prefer **categorical values**; keep names consistent across ATAs when comparable.

### Airport Class Definitions

For reference:
- **Cat D:** Major airports, runway ≥1,800m, full IFR, comprehensive services
- **Cat C:** Regional airports, runway 1,200-1,800m, IFR capable, standard services  
- **Cat B:** Small airports, runway 900-1,200m, VFR primary, limited services
- **Cat A:** Very small airports, runway <900m, VFR only, minimal services

### H₂ Infrastructure Types

- **Fixed H₂ hydrant:** Permanent underground or above-ground pipeline system with aircraft connection points
- **Mobile H₂ bowser:** Road-transportable cryogenic tanker truck with transfer equipment
- **Hybrid system:** Combination of fixed storage with mobile distribution
- **Future: H₂ generation on-site:** Electrolyzer systems producing H₂ from renewable electricity (not currently baselined)

### Consistency rules
- If a GSE specification or procedure is **only applicable** to some operational contexts, reference the **`RowID`/`GSE-ID`** directly.
- If globally applicable across all contexts, either:
  - add an explicit row (e.g., `GSE-00 – All certified configurations`), or
  - state "Global applicability" in the referencing document.
- Avoid overlapping/ambiguous slices — each operational context should map to exactly one GSE-ID.

### Workflow suggestion
1. **Define GSE-IDs**: align with the top-level operational domain list and register the canonical `GSE-xx` identifiers.
2. **Update this matrix** with approved contexts and references.
3. **Back-propagate IDs**:
   - Tag requirements in `03-00-03_Requirements` with relevant `GSE-ID`s.
   - Tag safety items in `03-00-02_Safety` with the same `GSE-ID`s.
   - Tag certification items in `03-00-10_Certification` with the same `GSE-ID`s.
4. **Review for gaps**:
   - Every GSE context here should have ≥1 linked requirement and (where needed) safety analysis and certification evidence.
   - Harmonize any context referenced elsewhere but missing here.

---

## Validation rules (for CI/CSDB)

- **RowID**: integer, unique.
- **GSE-ID**: `^GSE-\d{2}$`, unique across this matrix.
- **Aircraft Config / Airport Class / H₂ Infrastructure / Ground Power Capability**: non-empty, controlled vocabulary where available.
- **Evidence Ref(s)**: at least one ID; each must match known patterns (e.g., `^REQ-03-\d{3}$`, `^SAFE-03-\d{3}$`, `^CERT-03-\d{3}$`, `^OPS-03-\d{3}$`).
- **Cross-links**: for every `GSE-ID`, at least one reference exists in `../03-00-03_Requirements/` or `../03-00-02_Safety/` or `../03-00-10_Certification/`.

---

## Acceptance Criteria (for this subject)

- Metadata valid (identifier format, ISO dates, allowed enums).
- Table has ≥1 approved GSE operational context.
- No duplicate `RowID` or `GSE-ID`.
- All `Evidence Ref(s)` resolve to existing artefacts or tracked placeholders.
- Links to **Requirements**, **Safety**, and **Certification** folders present.

---

```det
hash: "<to-be-filled-by-CI>"
kpis:
  matrix_rows: 5
  gse_ids_unique: true
  evidence_refs_present: true
  metadata_complete: true
trace:
  requirements_ref: "../03-00-03_Requirements/"
  safety_ref: "../03-00-02_Safety/"
  certification_ref: "../03-00-10_Certification/"
producer: "AMPEL360 Doc CI"
revision: "initial"
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.
