# 53-00-04_Design – Fuselage Design Documentation (ATA 53)

## 1. Purpose

The **53-00-04_Design** folder contains the **design-intent documentation** for the AMPEL360 BWB fuselage under **ATA 53**. It concentrates:

- **Design philosophy and strategy** for the BWB fuselage and centerbody.
- **Configuration Items (CIs)** – the design definition of every structural component.
- **Interface Control Documents (ICDs)** with other ATA chapters.
- **Design-level analysis** (global models, load cases, high-level stress results).
- **Design reviews and approval records** (PDR, CDR, TRR).

This folder represents **Stage 4 – Design** in the **14-folder lifecycle** defined by the OPT-IN Framework v1.1.

---

## 2. Scope

### 2.1 In Scope

- **Design Philosophy and Strategy**
  - BWB-specific design drivers.
  - Material strategy at fuselage level.
  - Manufacturing considerations that influence the design.

- **Configuration Items (CIs)**
  - Full CI hierarchy for ATA 53 (Zones 100–600).
  - CI metadata (numbering, zone, type, structural role, weight, status).
  - CI-level design descriptions, materials, manufacturing plans.
  - CI-level requirements traceability to [53-00-03_Requirements](../53-00-03_Requirements/).
  - CI-level analysis and test references (as design evidence, not certification).

- **Interface Management**
  - Interface Control Documents (ICDs) between ATA 53 and:
    - ATA 21, 25, 26, 27, 32, 54, 95, 99 (as applicable).
  - Interface load definitions and geometric compatibility.

- **Design Analysis (Design-Intent Level)**
  - Global FEA model descriptions tied to the CI hierarchy.
  - Load case definitions for design and sizing.
  - High-level stress analysis results and optimization studies.

- **Design Reviews**
  - PDR / CDR / TRR documentation and action tracking.
  - Design approval records tied to CI and drawing status.

### 2.2 Out of Scope

- **Requirements Definition**  
  Covered in [53-00-03_Requirements/](../53-00-03_Requirements/) (general fuselage requirements).

- **Certification-Grade Structural Substantiation**  
  Detailed stress, fatigue and DT, and test correlation live under:
  - [53-50_Structures/](../../53-50_Structures/) (primary/secondary structure, margins, DT, tests).

- **Manufacturing Processes & Industrialization**  
  Covered under:
  - [53-00-09_Production_Planning/](../53-00-09_Production_Planning/).

- **As-Built Configuration & Effectivity**  
  Tracked in the production/PLM system; only design-intent lives here.

---

## 3. Directory Structure

```text
53-00-04_Design/
├── README.md
│
├── 01_Design_Overview/
│   ├── README.md
│   ├── 53-00-04-01-001_Design_Philosophy.md
│   ├── 53-00-04-01-002_BWB_Design_Drivers.md
│   ├── 53-00-04-01-003_Material_Strategy.md
│   └── 53-00-04-01-004_Manufacturing_Considerations.md
│
├── 02_Configuration_Items/
│   ├── README.md
│   ├── 53-00-04-02-001_CI_Master_Index.md
│   ├── 53-00-04-02-002_CI_Numbering_Convention.md
│   ├── 53-00-04-02-003_CI_Lifecycle_Management.md
│   ├── 53-00-04-02-004_CI_Structure_and_Governance.md
│   │
│   ├── Zone_100_Nose_Section/
│   │   ├── README.md
│   │   ├── 53-00-04-02-101_CI-53-100_Zone_Index.csv
│   │   └── CI-53-100-…/   # carpetas de CI con su propio CI_Definition.yaml
│   │
│   ├── Zone_200_Forward_Cabin/
│   │   ├── README.md
│   │   ├── 53-00-04-02-201_CI-53-200_Zone_Index.csv
│   │   └── CI-53-200-…/
│   │
│   ├── Zone_300_Mid_Cabin/
│   │   ├── README.md
│   │   ├── 53-00-04-02-301_CI-53-300_Zone_Index.csv
│   │   └── CI-53-300-…/
│   │
│   ├── Zone_400_Center_Wing_Box/
│   │   ├── README.md
│   │   ├── 53-00-04-02-401_CI-53-400_Zone_Index.csv
│   │   └── CI-53-400-…/
│   │
│   ├── Zone_500_Aft_Cabin/
│   │   ├── README.md
│   │   ├── 53-00-04-02-501_CI-53-500_Zone_Index.csv
│   │   └── CI-53-500-…/
│   │
│   ├── Zone_600_Tail_Section/
│   │   ├── README.md
│   │   ├── 53-00-04-02-601_CI-53-600_Zone_Index.csv
│   │   └── CI-53-600-…/
│   │
│   └── ASSETS/
│       ├── 53-00-04-02-A-001_CI_Database.csv
│       ├── 53-00-04-02-A-002_CI_Hierarchy_Tree.svg
│       ├── 53-00-04-02-A-003_CI_Status_Dashboard.csv
│       ├── 53-00-04-02-A-004_CI_Weight_Tracking.csv
│       ├── 53-00-04-02-A-005_CI_Requirements_Matrix.csv
│       └── 53-00-04-02-A-006_CI_Change_Log.csv
│
├── 03_Interface_Control_Documents/
│   ├── README.md
│   ├── 53-00-04-03-001_ICD-53-25_Fuselage_to_Equipment.md
│   ├── 53-00-04-03-002_ICD-53-27_Fuselage_to_Flight_Controls.md
│   ├── 53-00-04-03-003_ICD-53-32_Fuselage_to_Landing_Gear.md
│   ├── 53-00-04-03-004_ICD-53-52_Fuselage_to_Doors.md
│   ├── 53-00-04-03-005_ICD-53-54_Fuselage_to_Nacelles.md
│   └── ASSETS/
│       ├── 53-00-04-03-A-001_Interface_Loads_Summary.csv
│       └── 53-00-04-03-A-002_Interface_Drawings_Index.csv
│
├── 04_Design_Analysis/
│   ├── README.md
│   │
│   ├── Global_FEA_Model/
│   │   ├── 53-00-04-04-001_Global_FEA_Model_Description.md
│   │   ├── 53-00-04-04-002_Element_Mesh_Definition.csv
│   │   ├── 53-00-04-04-003_Material_Properties.csv
│   │   ├── 53-00-04-04-004_Boundary_Conditions.md
│   │   └── 53-00-04-04-005_Load_Cases_Summary.csv
│   │
│   ├── Load_Cases_Definition/
│   │   ├── README.md
│   │   ├── 53-00-04-04-011_Maneuver_Loads.csv
│   │   ├── 53-00-04-04-012_Gust_Loads.csv
│   │   ├── 53-00-04-04-013_Landing_Loads.csv
│   │   ├── 53-00-04-04-014_Pressure_Loads.csv
│   │   └── 53-00-04-04-015_Combined_Loads.csv
│   │
│   ├── Stress_Analysis_Results/
│   │   ├── README.md
│   │   ├── 53-00-04-04-021_Primary_Structure_Stress.csv
│   │   ├── 53-00-04-04-022_Joints_and_Splices_Stress.csv
│   │   └── 53-00-04-04-023_Critical_Details_Stress.csv
│   │
│   └── Optimization_Studies/
│       ├── 53-00-04-04-031_Weight_Optimization.md
│       ├── 53-00-04-04-032_Thickness_Optimization.csv
│       └── 53-00-04-04-033_Layup_Optimization.md
│
├── 05_Design_Reviews/
│   ├── README.md
│   │
│   ├── PDR_Preliminary_Design_Review/
│   │   ├── 53-00-04-05-001_PDR_Report.md
│   │   ├── 53-00-04-05-002_PDR_Action_Items.csv
│   │   └── 53-00-04-05-003_PDR_Presentation.md
│   │
│   ├── CDR_Critical_Design_Review/
│   │   ├── 53-00-04-05-011_CDR_Report.md
│   │   ├── 53-00-04-05-012_CDR_Action_Items.csv
│   │   └── 53-00-04-05-013_CDR_Presentation.md
│   │
│   └── TRR_Test_Readiness_Review/
│       ├── 53-00-04-05-021_TRR_Report.md
│       └── 53-00-04-05-022_TRR_Checklist.csv
│
└── ASSETS/
    ├── templates/
    │   ├── 53-00-04-A-001_CI_Definition_Template.yaml
    │   ├── 53-00-04-A-002_Design_Description_Template.md
    │   ├── 53-00-04-A-003_Analysis_Report_Template.md
    │   └── 53-00-04-A-004_Manufacturing_Plan_Template.md
    │
    ├── standards/
    │   ├── 53-00-04-A-011_Design_Standards.md
    │   ├── 53-00-04-A-012_Drawing_Standards.md
    │   ├── 53-00-04-A-013_Material_Standards.md
    │   └── 53-00-04-A-014_Analysis_Standards.md
    │
    ├── tools/
    │   ├── 53-00-04-A-021_CI_Management_Guide.md
    │   ├── 53-00-04-A-022_PLM_Integration_Guide.md
    │   ├── 53-00-04-A-023_Weight_Tracking_Tool.md
    │   └── 53-00-04-A-024_Status_Reporting_Guide.md
    │
    └── dashboards/
        ├── 53-00-04-A-101_Design_Maturity_Dashboard.csv
        ├── 53-00-04-A-102_Weight_Status_Dashboard.csv
        ├── 53-00-04-A-103_Critical_Items_Dashboard.csv
        └── 53-00-04-A-104_Change_Management_Dashboard.csv
```

---

## 4. Configuration Items (CIs)

### 4.1 CI Hierarchy (Overview)

All fuselage components are organized as **Configuration Items (CIs)** following a strict hierarchy:

```yaml
ci_structure:
  top_level: "CI-53-000"            # ATA 53 Fuselage

  zone_level:
    - "CI-53-100"  # Nose Section
    - "CI-53-200"  # Forward Cabin
    - "CI-53-300"  # Mid Cabin
    - "CI-53-400"  # Center Wing Box (critical)
    - "CI-53-500"  # Aft Cabin
    - "CI-53-600"  # Tail Section
```

Example component-level CIs:

- `CI-53-400-SPAR-FWD` – Forward Wing Spar (Zone 400).
- `CI-53-200-DOOR-1L` – Passenger Door 1L (Zone 200).
- `CI-53-100-BHD-FWD` – Forward Pressure Bulkhead (Zone 100).

### 4.2 Standard CI Folder Structure

Each CI has its own folder:

```text
CI-53-400-SPAR-FWD_Forward_Wing_Spar/
├── README.md
├── CI_Definition.yaml
├── Design_Description.md
├── Material_Specification.md
├── Manufacturing_Plan.md
├── Requirements_Traceability.csv
├── ASSETS/
│   ├── Drawings/
│   ├── Analysis/
│   ├── Test_Data/
│   └── Production/
└── CHANGELOG.md
```

- `CI_Definition.yaml` – single source for CI metadata (number, zone, structural_role, status, etc.).
- `Requirements_Traceability.csv` – CI-level mapping to requirements in [53-00-03_Requirements](../53-00-03_Requirements/).
- `ASSETS` – drawings, design-level analysis outputs, test summaries, and production-intent information.

---

## 5. Relationship to Other ATA 53 Folders

### 5.1 53-00-03_Requirements

- **What lives there**: General fuselage requirements, organized by category and requirement ID, e.g.:
  - `RQ-53-00-01-001` – Ultimate Load Capability
  - `RQ-53-00-01-002` – Limit Load Elastic Behaviour
  - …

- **Link from CIs**:
  Each CI's `Requirements_Traceability.csv` references requirement IDs like:
  
  ```csv
  Requirement_ID,Requirement_Title,Verification_Method,Status
  RQ-53-00-01-001,Ultimate Load Capability,Test + Analysis,Planned
  RQ-53-00-01-002,Limit Load Elastic Behaviour,Analysis,In Progress
  ```

### 5.2 53-20_Subsystems

- **What lives there**: Fuselage subsystems (pressure shell modules, door surround structure, floor and supports, gear bays, etc.).
- **Link from CIs**:
  - Each CI includes a `subsystem_ref` field in `CI_Definition.yaml` pointing to its owning subsystem, e.g.:
    
    ```yaml
    traceability:
      subsystem_ref: "53-20-04_Centerbody_Landing_Gear_Bays"
    ```

### 5.3 53-50_Structures

- **What lives there**: Certification-grade structural substantiation:
  - Primary vs secondary structure breakdown.
  - Detailed stress, fatigue and DT.
  - Test definitions and correlation.
  - Structural margins of safety.

- **Boundary**:
  - `53-00-04_Design` holds **design-intent** analysis artefacts:
    - Global FEA model descriptions.
    - Load case definitions.
    - High-level stress results needed to understand the design.
  - `53-50_Structures` holds **substantiation-grade** artefacts:
    - Controlled stress reports.
    - DT analyses.
    - Test correlation reports and certification evidence.
  
  Design artefacts in `04_Design_Analysis/` shall not replace or duplicate the controlled substantiation in [53-50_Structures](../../53-50_Structures/), but shall reference it.

### 5.4 53-00-09_Production_Planning

- `Manufacturing_Plan.md` and `ASSETS/Production/` in each CI feed into detailed production planning under [53-00-09_Production_Planning](../53-00-09_Production_Planning/).

---

## 6. File Format Standards

All CI-related documentation shall use formats that are **version-control friendly**:

```yaml
metadata_files:
  format: "YAML (.yaml)"
  usage: "CI_Definition files and structured configuration"

text_documents:
  format: "Markdown (.md)"
  usage: "Design descriptions, reports, procedures"

data_files:
  format: "CSV (.csv)"
  usage: "Matrices, dashboards, databases, traceability tables"

drawings:
  format: "SVG (.svg)"
  usage: "Technical drawings, interface diagrams, geometry views"

prohibited:
  - "PDF (for internal authoring; allowed only as external deliverable)"
  - "Excel (XLSX) – use CSV instead"
  - "Word (DOCX) – use Markdown instead"

exceptions:
  - "Supplier / vendor-provided documents (kept as received)"
  - "Scanned legacy documents used as reference only"
```

---

## 7. CI Lifecycle and Change Management

Lifecycle states (summary; full details in `CI_Lifecycle_Management.md`):

```yaml
ci_lifecycle:
  1_concept:            "Preliminary sizing and weight estimate"
  2_preliminary_design: "Initial detailed design"
  3_detailed_design:    "Final design with full analysis"
  4_design_released:    "Approved for manufacturing (under change control)"
  5_in_production:      "Being manufactured"
  6_in_service:         "Installed on aircraft"
  7_retired:            "Removed / end-of-life"
```

When a CI changes, the process is governed by:

- **Change Request → Impact Assessment → Approval → Implementation → Verification**, as documented in `CI_Lifecycle_Management.md` and the program Configuration Management Plan.

---

## 8. Document Control

- **Folder**: `53-00-04_Design`
- **Status**: OPERATIONAL
- **Version**: 2.0 (updated with CI integration)
- **Date**: 2025-11-22
- **Owner**: ATA 53 Chief Design Engineer
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Next Review**: Q2 2026

**Changelog**:

- **v2.0 (2025-11-22)** – Integrated CI structure under `02_Configuration_Items/`
  - Added CI hierarchy and CI database.
  - Added CI metadata template (including `structural_role` and `subsystem_ref`).
  - Clarified boundaries with `53-00-03_Requirements`, `53-20_Subsystems`, and `53-50_Structures`.
- **v1.0 (2025-11-15)** – Initial design folder structure (overview, ICDs, design analysis approach).

**AI Assistance:**
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Last AI update: _2025-11-22_.
