---
Title: "ATA 02 — 02-00-02 Safety"
Identifier: "AMPEL360-02-00-02_SFT"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Safety Team"
CreatedAt: "2025-11-13"
ModifiedAt: "2025-11-13"
Scope: "Safety framework and evidence for ATA 02 General layer (Operations Information)."
Abstract: "Defines objectives, methods, artifacts, and evidence required to assure safe operations information for ATA 02."
Keywords: ["ATA 02", "Safety", "FHA", "FMEA", "FTA", "CCA", "HF", "MoC", "Validation"]
Compliance:
  - "ARP4754A/ARP4761"
  - "DO-178C/DO-254 (as applicable)"
  - "DO-160 (environmental)"
  - "ATA iSpec 2200 / S1000D"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentGeneral: "../"
  Siblings:
    - "../02-00-01_OVR.md"
    - "../02-00-03_Requirements/"
    - "../02-00-07_V_AND_V/"
  CrossATABuckets:
    - "../../02-10_Operations/"
    - "../../02-20_Subsystems/"
    - "../../02-90_Tables_Schemas_Diagrams/"
ChangeLog:
  - {version: "1.0.0", date: "2025-11-13", author: "AMPEL360 Safety Team", change: "Initial creation"}
---

# 02-00-02 — Safety (ATA 02: Operations Information)

## 1. Purpose

The `02-00-02_Safety` layer provides the **safety backbone** for **ATA 02 — Operations Information**. It defines:

- Safety **objectives** and **Means of Compliance (MoC)** specific to operations information.
- Safety **analyses** (FHA, FMEA, FTA, CCA) focused on information-centric hazards.
- **Human Factors**, runtime **monitoring**, **emergency procedures**, and **operational safety procedures**.
- Safety **cases** (including NN interplay with ATA 95).
- The **framework overview**, hazard methodology, requirements and test structures, and supporting assets.

All content is aligned with program safety and certification goals and with the OPT-IN framework and AMPEL360 standards.

---

## 2. Mandatory Outputs and File Pattern

The following outputs are **mandatory** for ATA 02 `02-00-02_Safety`, with canonical identifiers and naming patterns:

- **Objectives & MoC**  
  - `02-00-02-001A_Certification_Safety_Objectives.md`

- **Analyses**  
  - **CCA**: `02-00-02-002A_Common_Cause_Analysis.md`  
  - **Emergency Response Procedures (ERP)**: `02-00-02-003A_Emergency_Response_Procedures.md`  
  - **FMEA** (CSV): `02-00-02-004A_Failure_Modes_Effects_Analysis.csv`  
    - FMEA View: Training Phase: `02-00-02-A002_FMEA_View_Training_Phase.md`
  - **FTA** (method): `02-00-02-005A_Fault_Tree_Analysis.md`  
  - **FHA** (CSV): `02-00-02-006A_Functional_Hazard_Assessment.csv`

- **Methods and Framework**  
  - Hazard methodology: `02-00-02-007A_Hazard_Analysis_Methodology.md`  
  - Safety framework overview: `02-00-02-012A_Safety_Framework_Overview.md`

- **Human Factors**  
  - `02-00-02-008A_Human_Factors_Safety.md`

- **Operational Procedures & Monitoring**  
  - Operational safety procedures: `02-00-02-009A_Operational_Safety_Procedures.md`  
  - Runtime safety monitoring: `02-00-02-010A_Runtime_Safety_Monitoring.md`

- **Safety Cases**  
  - NN / AI interplay safety cases: `02-00-02-011A_Safety_Cases_NN_Interplay.md`

- **Requirements & Tests (CSV views)**  
  - Safety requirements view (CSV index / filter): `02-00-02-013A_Safety_Requirements_View.csv`  
  - Safety validation tests (V&V view): `02-00-02-014A_Safety_Validation_Tests.csv`

- **ASSETS** (templates, reports, diagrams)  
  - Folder: `ASSETS/` under `02-00-02_Safety/`, with:
    - `ASSETS/Safety_Validation_Reports/` (runbooks & reports)  
    - `ASSETS/Templates/` (FHA/FMEA/FTA/HF/ERP/Monitoring templates)  
    - `ASSETS/Diagrams/` (FTA trees, safety framework maps, etc.)

### 2.1 Naming Rules

- **Subject documents** (this folder):  
  - `02-00-02-00xA_Descriptive_Name.ext`  
  - `x` increments per subject (001A, 002A, …, 014A).

- **Assets** (within `ASSETS/...`):  
  - `02-00-02-A00x_*` for asset files, where:
    - `A00x` aligns with the subject it supports, when applicable  
    - Example: `02-00-02-A001_FHA_Template.xlsx`.

---

## 3. Evidence Policy and Traceability

The safety layer is **evidence-driven**. Each analysis and method must be backed by:

- **Requirements** under:  
  - `../02-00-03_Requirements/` (with safety tags and IDs like `S-02-REQ-###`).

- **Verification & Validation evidence** under:  
  - `../02-00-07_V_AND_V/` (test plans, reports, analyses) and  
  - `../02-00-10_Certification/` for formal certification artefacts.

### 3.1 Minimum Traceability Expectations

For every safety-relevant topic (hazard, analysis, monitoring rule, ERP behaviour):

- **Safety Objectives**  
  - Origin in `02-00-02-001A_Certification_Safety_Objectives.md`.

- **Hazards**  
  - Listed in `AMPEL360-02-00-02_Hazards.csv` (referenced from the methodology doc).

- **Requirements**  
  - At least one requirement in `../02-00-03_Requirements/` (e.g. `S-02-REQ-001`), referenced in:
    - Hazards CSV (mitigation).
    - Analyses (FMEA / FTA / CCA).
    - Safety case structures (NN interplay, framework overview).

- **Tests / V&V**  
  - At least one test or analysis in `../02-00-07_V_AND_V/` (e.g. `TR-Ops-Performance-001`), referenced in:
    - Requirements (verification method / link).
    - Safety validation tests view `02-00-02-014A_Safety_Validation_Tests.csv`.

- **Evidence & Lifecycle**  
  - Version and EIS tag references via:
    - `../02-00-11_EIS_Versions_Tags/`
    - Certification records in `../02-00-10_Certification/`.

### 3.2 Validation Campaigns

- Use runbooks in `ASSETS/Safety_Validation_Reports` for:
  - HIL / PIL activities as relevant.
  - Corner-case and defect injection campaigns (e.g. monitoring and ERP tests).
- Each runbook references:
  - In-scope requirements and hazards.
  - Planned tests (from `02-00-02-014A_Safety_Validation_Tests.csv`).
  - Entry/exit criteria and responsibilities.

---

## 4. Relationship to the Lifecycle Structure

`02-00-02_Safety` is **folder 2 of 14** in the ATA 02 General lifecycle:

1. `02-00-01_OVR` — Overview  
2. `02-00-02_Safety` — Safety (this layer)  
3. `02-00-03_Requirements` — Requirements  
4. `02-00-04_Design` — Design  
5. `02-00-05_Interfaces` — Interfaces  
6. `02-00-06_Engineering` — Engineering  
7. `02-00-07_V_AND_V` — Verification & Validation  
8. `02-00-08_Prototyping`  
9. `02-00-09_Production_Planning`  
10. `02-00-10_Certification`  
11. `02-00-11_EIS_Versions_Tags`  
12. `02-00-12_Services`  
13. `02-00-13_Subsystems_Components`  
14. `02-00-14_Ops_Std_Sustain`

`02-00-02_Safety`:

- **Consumes**: overview, operational scope, structural rules (`../02-00-01_OVR.md` and `02-00-01` documents).  
- **Feeds**:  
  - Requirements (`../02-00-03_Requirements/`).  
  - V&V (`../02-00-07_V_AND_V/`).  
  - Certification (`../02-00-10_Certification/`).  
  - EIS / versioning rules (`../02-00-11_EIS_Versions_Tags/`).

---

## 5. Safety Workbench (Quick Links)

Use this section as your **working table of contents** when operating in `02-00-02_Safety`:

- **Objectives & MoC**  
  - `./02-00-02-001A_Certification_Safety_Objectives.md`

- **Analyses**  
  - CCA: `./02-00-02-002A_Common_Cause_Analysis.md`  
  - ERP: `./02-00-02-003A_Emergency_Response_Procedures.md`  
  - FMEA (CSV): `./02-00-02-004A_Failure_Modes_Effects_Analysis.csv`  
    - FMEA View: Training Phase: `./02-00-02-A002_FMEA_View_Training_Phase.md`
  - FTA (method): `./02-00-02-005A_Fault_Tree_Analysis.md`  
  - FHA (CSV): `./02-00-02-006A_Functional_Hazard_Assessment.csv`

- **Methods & Framework**  
  - Hazard methodology: `./02-00-02-007A_Hazard_Analysis_Methodology.md`  
  - Safety framework overview: `./02-00-02-012A_Safety_Framework_Overview.md`

- **Human Factors & Ops Procedures**  
  - Human Factors safety: `./02-00-02-008A_Human_Factors_Safety.md`  
  - Operational safety procedures: `./02-00-02-009A_Operational_Safety_Procedures.md`  

- **Monitoring & NN Interplay**  
  - Runtime safety monitoring: `./02-00-02-010A_Runtime_Safety_Monitoring.md`  
  - NN interplay safety cases: `./02-00-02-011A_Safety_Cases_NN_Interplay.md`

- **Requirements & Tests Views**  
  - Safety requirements view (CSV): `./02-00-02-013A_Safety_Requirements_View.csv`  
  - Safety validation tests (CSV): `./02-00-02-014A_Safety_Validation_Tests.csv`

- **Assets**  
  - Templates, reports, diagrams: `./ASSETS/`

---

## 6. Document Control

- **Generated by**: AI (prompted by Amedeo Pelliccia); pending approval by `[Approver]`.  
- **Phase**: Safety  
- **Lifecycle Position**: 02 of 14 (ATA 02 General layer)  
- **Status**: Active (within Draft version line)  
- **Standard**: OPT-IN Framework v1.1 (aligned with ATA 95 canonical template)  
- **Owner**: AMPEL360 Documentation WG (Safety)  
- **Last Updated**: 2025-11-13

---

## 7. How to Use This Folder (Contributor Guidance)

When working under `02-00-02_Safety`:

1. **Start from the Framework Overview**  
   - Use `02-00-02-012A_Safety_Framework_Overview.md` to understand where your change sits (objectives, analyses, requirements, V&V, monitoring, ERP, NN).

2. **Choose the right artefact**  
   - New hazard → update Hazard Methodology and Hazards CSV.  
   - New failure mode → update FMEA/FTA and link to requirements.  
   - New monitoring rule → update Runtime Safety Monitoring and related requirements/tests.  
   - NN-related change → update NN Interplay safety case and associated artefacts.

3. **Maintain traceability**  
   - For each safety change, ensure:
     - A hazard (if applicable).  
     - A requirement in `../02-00-03_Requirements/`.  
     - A test / evidence item in `../02-00-07_V_AND_V/`.  
     - Proper EIS/version tagging in front-matter and `../02-00-11_EIS_Versions_Tags/` where relevant.

4. **Update the workbench and assets**  
   - If you add a new CSV or method document, update the **Outputs** and **Workbench** sections here.  
   - Add or update templates and reports under `ASSETS/` in the same change set.

---

## What to do next / how to approach this

1. **Create the folder & place this file**
   - Path:  
     `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-00_GENERAL/02-00-02_Safety/02-00-02_Safety.md`.

2. **Verify identifiers & links**
   - Ensure all referenced `02-00-02-00xA_*` files exist (or create stubs) and that paths match your repo structure.
   - Align sibling link `../02-00-01_OVR.md` with your actual overview filename (you already have `ATA 02 — 02-00-01 Overview`).

3. **Seed ASSETS structure**
   - Under `02-00-02_Safety/ASSETS/` create:
     - `Safety_Validation_Reports/` (include a minimal `README` or template runbook).
     - `Templates/` (e.g., FHA/FMEA CSV templates, ERP bulletin template).
     - `Diagrams/` (drop your safety framework and FTA diagrams here).

4. **Integrate into your workflow**
   - In your contribution/PR template for ATA 02, add:
     - “If safety artefacts changed, did you update `02-00-02_Safety.md` workbench/links?”
     - “Hazard → Requirement → Test → Evidence traceability checked?”

5. **Plan incremental tightening**
   - As your content matures, extend this file with:
     - A short “Safety RACI” reference to `Roles & Responsibilities`.
     - A checklist for introducing new safety artefacts (mandatory IDs, front-matter fields, link targets).
