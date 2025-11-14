---
Title: "02-00-02-A002 — FMEA View: Training Phase (CSV-Based)"
Identifier: "AMPEL360-02-00-02-A002"
Version: "1.0.0"
Status: "Template / View Definition"
AccessLevel: "Internal"
Author: "AMPEL360 Safety Team"
CreatedAt: "2025-11-14"
ModifiedAt: "2025-11-14"
Scope: "FMEA view for Training Phase related to ATA 02 Operations Information."
Abstract: "Defines how to filter and interpret FMEA entries concerning training activities from the canonical CSV source."
Keywords: ["FMEA", "Training", "ATA 02", "Safety", "Human Factors", "View Definition"]
Compliance:
  - "ARP4754A/ARP4761"
  - "DO-178C (as applicable)"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentSafety: "./"
  CanonicalFMEA: "./02-00-02-004A_Failure_Modes_Effects_Analysis.csv"
  RelatedDocs:
    - "./02-00-02-007A_Hazard_Analysis_Methodology.md"
    - "./02-00-02-008A_Human_Factors_Safety.md"
    - "./02-00-02-003A_Emergency_Response_Procedures.md"
    - "./02-00-02-009A_Operational_Safety_Procedures.md"
    - "./02-00-02-010A_Runtime_Safety_Monitoring.md"
    - "./02-00-02-011A_Safety_Cases_NN_Systems.md"
  V_AND_V: "../02-00-07_V_AND_V/"
  Requirements: "../02-00-03_Requirements/"
ChangeLog:
  - {version: "1.0.0", date: "2025-11-14", author: "AI (prompted by Amedeo Pelliccia)", change: "Initial creation"}
---

# 02-00-02-A002 — FMEA View: Training Phase (CSV-Based)

This asset defines the **FMEA view for the Training Phase** related to ATA 02 Operations Information.

The **canonical data source** for all FMEA content is:

- `./02-00-02-004A_Failure_Modes_Effects_Analysis.csv`

This file describes how to **filter and interpret** the subset of FMEA entries that concern training activities, rather than providing a separate Excel workbook or duplicate data.

---

## 1. Scope — Training Phase

This view covers failure modes in the **training lifecycle** for personnel who create, review, approve, publish, or use ATA 02 operations information, including:

- Initial and recurrent **training of ops personnel** (crews, dispatch, ground ops, MRO).
- Training for **Ops Information Lead, Safety, Tech Pubs, HF, and Monitoring roles**.
- Training on:
  - Structure and navigation of ATA 02.
  - Use and interpretation of limits, procedures, applicability tags.
  - ERP, degraded operations, and runtime monitoring outputs.
  - NN/AI-related ops information use (where applicable).

Typical `Function/Item` values in the parent CSV for this view:

- `Ops Training – General`
- `Ops Training – ATA 02 Structure`
- `Ops Training – ERP & Degraded Ops`
- `Ops Training – Runtime Monitoring & Alerts`
- `Ops Training – NN-Assisted Ops` (if applicable)
- `Safety/ERP Training – Internal Staff`

---

## 2. Relationship to the Canonical FMEA CSV

All training-related FMEA entries must reside in:

- `./02-00-02-004A_Failure_Modes_Effects_Analysis.csv`

Typical columns:

```csv
RowID,Function/Item,Failure_Mode,NN/IT_Cause,Local_Effect,System_Effect,Ops_Effect,Detection_Method,Mitigation/Compensation,Severity,Probability,DAL,References
```

This **view** is implemented by **filtering** the parent CSV, not by keeping a separate Excel workbook with independent content.

### 2.1 Recommended Filtering Rule

For the "Training Phase" view, include rows where:

- `Function/Item` contains `Training`, `Training –`, or
- `References` contains a stable tag such as `#TrainingFMEA`.

This makes scripting and dashboarding easier and prevents drift between views.

---

## 3. Example Rows for the Training Phase View

The following examples illustrate the kind of entries that belong to this view. They must be entered in the parent CSV, not here:

```csv
RowID,Function/Item,Failure_Mode,NN/IT_Cause,Local_Effect,System_Effect,Ops_Effect,Detection_Method,Mitigation/Compensation,Severity,Probability,DAL,References
10,Ops Training – ATA 02 Structure,Incomplete training coverage for ATA 02 content model,Training material outdated or missing modules,Staff misunderstand where to find or place safety-relevant ops information,Misplaced or missing updates to safety-relevant documents,Delays or errors in applying correct procedures/limits,Training audits + periodic syllabus review,Regular review of training materials against ATA 02 overview and safety framework + mandatory refresher,Major,Occasional,C,"H-02-0XX; S-02-REQ-0XX; #TrainingFMEA; 02-00-02-008A_Human_Factors_Safety.md"
11,Ops Training – ERP & Degraded Ops,Insufficient training on ERP and degraded ops procedures,Infrequent or purely theoretical training,Staff do not recognize when to trigger ERP or how to apply degraded ops fallbacks,Information issues not contained promptly leading to extended exposure to incorrect data,Runtime monitoring alerts and incidents not handled correctly,Post-incident reviews + training records checks,Scenario-based ERP/degraded ops drills with documented outcomes and updated materials,Hazardous,Remote,B,"H-02-0YY; S-02-REQ-0YY; TR-ERP-Drill-001; #TrainingFMEA; 02-00-02-003A_Emergency_Response_Procedures.md; 02-00-02-009A_Operational_Safety_Procedures.md"
```

Adjust IDs, severities, and links per your actual hazard and requirement set.

---

## 4. How to Use This View

### 4.1 For Safety / HF / Ops Training Owners

1. **Filter the FMEA CSV**
   - Open `./02-00-02-004A_Failure_Modes_Effects_Analysis.csv`.
   - Filter:
     - `Function/Item` starting with `Ops Training –`, or
     - `References` containing `#TrainingFMEA`.

2. **Check coverage across key training topics**
   Make sure you have FMEA coverage for:
   - Understanding ATA 02 structure and navigation.
   - Interpreting limitations, warnings, applicability tags.
   - Handling ERP, runtime monitoring alerts, and degraded ops.
   - Human Factors aspects (workload, SA, error traps) for training and documentation.
   - NN/AI-assisted ops information (if applicable; see `./02-00-02-011A_Safety_Cases_NN_Systems.md`).

3. **Connect to hazards, requirements, and tests**
   - For each row, ensure `References` include:
     - At least one **HazardID** (e.g. `H-02-0XX`).
     - At least one training-related requirement (e.g. `S-02-REQ-HF-XXX`).
     - Any **V&V test IDs** for drills/evaluations (e.g. `TR-Training-Scenario-001`).

### 4.2 For Spreadsheet Users

If you prefer Excel for analysis:

1. **Import the canonical CSV** into Excel.
2. Apply filters/pivots to create the **"Training Phase"** view using the rules above.
3. Perform your analysis (e.g., completeness checks, risk ranking).
4. Apply any content changes **back to the CSV**:
   - The CSV remains the **sole source of truth** for FMEA content.
   - Excel should remain a **derived working view** only.

> Rule: New or modified FMEA content must be reflected in  
> `./02-00-02-004A_Failure_Modes_Effects_Analysis.csv` to exist in the safety record.

---

## 5. Integration with the Safety Framework

- **Parent FMEA CSV**  
  → `./02-00-02-004A_Failure_Modes_Effects_Analysis.csv`

- **Hazard Analysis & Methodology**  
  → `./02-00-02-007A_Hazard_Analysis_Methodology.md`  
  → Hazards CSV: `./AMPEL360-02-00-02_Hazards.csv` (or equivalent)

- **Human Factors and Training**  
  → `./02-00-02-008A_Human_Factors_Safety.md`  
  → Training materials: `../../02-90_Tables_Schemas_Diagrams/` (HF & training content)

- **Operational Safety Procedures & ERP**  
  → `./02-00-02-009A_Operational_Safety_Procedures.md`  
  → `./02-00-02-003A_Emergency_Response_Procedures.md`

- **Runtime Monitoring**  
  → `./02-00-02-010A_Runtime_Safety_Monitoring.md` (training in alert handling)

- **NN Interplay Training** (if relevant)  
  → `./02-00-02-011A_Safety_Cases_NN_Systems.md`

- **V&V / Tests**  
  → `../02-00-07_V_AND_V/` (training drills, simulations, knowledge checks)  
  → `./02-00-02-014A_Safety_Validation_Tests.csv` (index including training-related tests)

---

## 6. Document Control

- Generated by: AI (prompted by Amedeo Pelliccia); pending approval by **[Approver]**  
- **Owner**: AMPEL360 Safety Team  
- **Status**: Template / View Definition  
- **Last Updated**: 2025-11-14

---

## What to do next / how to approach this

1. **Tag existing training-related FMEA rows**
   - In `./02-00-02-004A_Failure_Modes_Effects_Analysis.csv`, add:
     - `Function/Item` entries for training (e.g., `Ops Training – ERP & Degraded Ops`).
     - `#TrainingFMEA` in `References` for all relevant rows.

2. **Check completeness against HF & ERP docs**
   - Use:
     - [02-00-02-008A_Human_Factors_Safety.md](./02-00-02-008A_Human_Factors_Safety.md)
     - [02-00-02-003A_Emergency_Response_Procedures.md](./02-00-02-003A_Emergency_Response_Procedures.md)
     - [02-00-02-009A_Operational_Safety_Procedures.md](./02-00-02-009A_Operational_Safety_Procedures.md)  
   - Derive training-related failure modes (e.g., "staff unaware of ERP triggers") and ensure they appear in the FMEA CSV.

3. **Wire FMEA rows into requirements and tests**
   - For each training-phase FMEA row:
     - Add a training or HF requirement in `../02-00-03_Requirements/`.
     - Map at least one validation artefact (e.g., scenario-based training test) in `../02-00-07_V_AND_V/` and `./02-00-02-014A_Safety_Validation_Tests.csv`.

4. **Optimize workflow**
   - Add to your safety / training change checklist:
     - "Training-related hazards/FMEA rows updated (tagged `#TrainingFMEA`)?"
     - "Requirements & tests linked to training-FMEA rows?"
   - Consider a simple script later that:
     - Extracts all `#TrainingFMEA` rows into a generated HTML/Excel view for training reviews.

5. **Extend pattern to Deployment Phase view**
   - Mirror this structure for `02-00-02-A003_FMEA_View_Deployment_Phase`, keeping CSV as the canonical source and using a simple tag (e.g., `#DeploymentFMEA`) to define that view.
