# ATA 53 Configuration Items (CI) Structure – AMPEL360 BWB

This document defines the **CI structure**, **numbering convention**, **zone breakdown**, and **metadata model** for ATA 53 – Fuselage in the AMPEL360 BWB program.

---

## 1. CI Numbering Convention

```yaml
format: "CI-[ATA]-[ZONE]-[TYPE]-[ID]"

where:
  ATA:  "53"                           # Fuselage
  ZONE: "3-digit zone number"          # 100, 200, …, 600
  TYPE: "Component type code"          # FR, SKN, SPAR, BEAM, BHD, DOOR, etc.
  ID:   "Identifier within type"       # 100A, U01, FWD, etc.

examples:
  - "CI-53-100-FR-100A"      # Frame 100A, Zone 100
  - "CI-53-200-SKN-L01"      # Lower skin panel 01, Zone 200
  - "CI-53-400-SPAR-FWD"     # Forward wing spar, Zone 400
  - "CI-53-400-BAY-MLG-L"    # Left main landing gear bay structure
```

Top-level CIs:

- `CI-53-000` – ATA 53 Fuselage (all zones).
- `CI-53-100` – Zone 100 Nose Section.
- `CI-53-200` – Zone 200 Forward Cabin.
- `CI-53-300` – Zone 300 Mid Cabin.
- `CI-53-400` – Zone 400 Center Wing Box.
- `CI-53-500` – Zone 500 Aft Cabin.
- `CI-53-600` – Zone 600 Tail Section.

---

## 2. Zone Definitions (BWB-Specific)

```yaml
zone_structure:

  zone_100_nose_section:
    ci: "CI-53-100"
    stations: "0 to 150"
    description: "Forward pressure bulkhead to cockpit"
    major_components:
      - "Forward pressure bulkhead"
      - "Nose landing gear bay"
      - "Avionics bay structure"
      - "Cockpit floor structure"
      - "Windshield frames"

  zone_200_forward_cabin:
    ci: "CI-53-200"
    stations: "150 to 300"
    description: "First class and forward economy cabin"
    major_components:
      - "Upper and lower shell panels"
      - "Forward passenger doors"
      - "Floor beam grid"
      - "Cabin frames and stringers"

  zone_300_mid_cabin:
    ci: "CI-53-300"
    stations: "300 to 450"
    description: "Main economy cabin and BWB blend onset"
    major_components:
      - "Upper and lower shell panels"
      - "Mid passenger doors"
      - "Overwing exits"
      - "Floor beam grid"
      - "Wing-body blend transition"

  zone_400_center_wing_box:
    ci: "CI-53-400"
    stations: "450 to 600"
    description: "Wing integration, center wing box, main landing gear"
    major_components:
      - "Center wing box structure"
      - "Main landing gear bays"
      - "Wing spars (forward/rear)"
      - "Cargo bays"

  zone_500_aft_cabin:
    ci: "CI-53-500"
    stations: "600 to 750"
    description: "Aft cabin and empennage transition"
    major_components:
      - "Shell panels"
      - "Aft galley/lavatory structure"
      - "Empennage attachment structure"

  zone_600_tail_section:
    ci: "CI-53-600"
    stations: "750 to 900"
    description: "Aft pressure bulkhead to tail"
    major_components:
      - "Aft pressure bulkhead"
      - "Tail cone"
      - "APU bay structure"
      - "Empennage supports"
```

---

## 3. CI Attributes and Metadata Model

The canonical metadata for each CI is stored in `CI_Definition.yaml` and indexed in `CI_Database.csv`.

### 3.1 CI_Definition.yaml (logical schema)

```yaml
ci_metadata:
  ci_number: "CI-53-400-SPAR-FWD"
  ci_name: "Forward Wing Spar"
  parent_ci: "CI-53-400"
  zone: "400"

classification:
  type: "Spar"              # Assembly|Skin|Frame|Spar|Beam|Bulkhead|Fitting|Door|Panel|Column|Rib|Track|Bay|...
  criticality: "Critical"   # Critical|High|Medium|Low
  material_primary: "CFRP"  # CFRP|GFRP|Aluminum|Titanium|Steel|Mixed
  structural_role: "Primary"  # Primary|Secondary

physical_properties:
  weight_target_kg: 2200.0
  weight_actual_kg: 2285.0
  weight_margin_percent: -3.9
  cg_x: 0.0
  cg_y: 0.0
  cg_z: 0.0

status:
  design_status: "Released"      # Concept|Preliminary|Detailed|Released|Obsolete
  analysis_status: "Complete"    # Not Started|In Progress|Complete
  test_status: "In Progress"     # Not Started|In Progress|Complete
  production_status: "Tooling"   # Design|Tooling|Production|Complete

traceability:
  requirements:
    - "RQ-53-00-01-001"  # Ultimate Load Capability
    - "RQ-53-00-01-002"  # Limit Load Elastic Behaviour
  parent_drawing: "53-40-1000"
  specification: "53-40-S-001"
  subsystem_ref: "53-20-04_Centerbody_Landing_Gear_Bays"  # link to 53-20 subsystem

interfaces:
  - ci_number: "CI-53-400-SPAR-REAR"
    interface_type: "Structural (spars interconnection)"
  - ci_number: "CI-53-400-BAY-MLG-L-BEAM"
    interface_type: "Load transfer"

approval:
  design_approved_by: "J. Smith"
  design_approved_date: "2025-10-15"
  certification_authority: "EASA"

notes: ""
```

Key points:

- `structural_role` allows programmatic separation of **primary** vs **secondary** structure and drives 53-50 population.
- `subsystem_ref` binds each CI into the 53-20 Subsystems architecture.

### 3.2 CI_Database.csv (skeleton)

**Location**: `53-00-04_Design/02_Configuration_Items/ASSETS/CI_Database.csv`

```csv
CI_Number,CI_Name,Parent_CI,Zone,Type,Material,Weight_kg,Criticality,Structural_Role,Status,Subsystem,Drawing_Number,Specification
CI-53-000,ATA 53 Fuselage,AMPEL360,ALL,Assembly,Mixed,45000,Critical,Primary,Production,53-00_GENERAL,53-00-0000,53-00-A-001
CI-53-100,Nose Section,CI-53-000,100,Assembly,CFRP/Metal,3500,Critical,Primary,Production,53-20-01_Pressure_Shell_Modules,53-10-0000,53-10-A-001
CI-53-100-BHD-FWD,Forward Pressure Bulkhead,CI-53-100,100,Bulkhead,CFRP,450,Critical,Primary,Production,53-20-01_Pressure_Shell_Modules,53-10-1000,53-10-S-001
CI-53-100-FR-100A,Frame 100A,CI-53-100,100,Frame,CFRP,25,High,Primary,Production,53-20-01_Pressure_Shell_Modules,53-10-1001,53-10-S-002
CI-53-100-SKN-U01,Upper Skin Panel 01,CI-53-100,100,Skin,CFRP,180,Critical,Primary,Production,53-20-01_Pressure_Shell_Modules,53-10-2001,53-10-S-010
CI-53-200,Forward Cabin,CI-53-000,200,Assembly,CFRP,8500,Critical,Primary,Production,53-20-02_Door_Surround_Structure,53-20-0000,53-20-A-001
CI-53-200-DOOR-1L-FR,Door Frame 1L,CI-53-200,200,Frame,CFRP/Ti,180,Critical,Primary,Production,53-20-02_Door_Surround_Structure,53-20-2010,53-20-S-005
CI-53-400,Center Wing Box,CI-53-000,400,Assembly,CFRP,12000,Critical,Primary,Production,53-20-04_Centerbody_Landing_Gear_Bays,53-40-0000,53-40-A-001
CI-53-400-SPAR-FWD,Forward Wing Spar,CI-53-400,400,Spar,CFRP,2200,Critical,Primary,Production,53-20-04_Centerbody_Landing_Gear_Bays,53-40-1000,53-40-S-001
CI-53-200-FLR-BEAM-S-L,Secondary Floor Beams Left,CI-53-200,200,Beam,Aluminum,180,High,Secondary,Production,53-20-03_Cabin_Floor_and_Supports,53-20-3002,53-20-S-020
```

This CSV is the **flat index** for all CIs, used by:

- CI dashboards (`Design_Maturity_Dashboard.csv`, `Weight_Status_Dashboard.csv`).
- Primary/secondary structure classification (consumed by 53-50).
- Automated cross-ATA mapping in GenCCC / tooling.

---

## 4. Example CI Folder – CI-53-400-SPAR-FWD (Forward Wing Spar)

**Path**:

```text
53-00-04_Design/
└── 02_Configuration_Items/
    └── Zone_400_Center_Wing_Box/
        └── CI-53-400-SPAR-FWD_Forward_Wing_Spar/
```

Key documents:

- `CI_Definition.yaml` – metadata with `structural_role: Primary` and `subsystem_ref: 53-20-04_Centerbody_Landing_Gear_Bays`.
- `Design_Description.md` – narrative of spar design.
- `Spar_Web_Design.md`, `Spar_Caps_Design.md`, `Attachment_Fittings_Design.md`.
- `Load_Path_Analysis.md` – structural load-path description.
- `Requirements_Traceability.csv` – RQ → CI mapping.
- `ASSETS/*` – drawings, analysis results, test summaries, production plans.

(Structure is as defined in the main `53-00-04_Design/README.md`.)

---

## 5. CI Lifecycle States

Lifecycle states are managed consistently across the program:

```yaml
lifecycle_workflow:

  1_concept:
    activities:
      - "Initial sizing and weight estimate"
      - "Preliminary material selection"
      - "CI number assignment"
    deliverables:
      - "CI_Definition.yaml (minimal)"
      - "Weight budget allocation"

  2_preliminary_design:
    activities:
      - "Initial detailed design and analysis"
      - "First drawings and sketches"
    deliverables:
      - "Design_Description.md (initial)"
      - "Preliminary analysis results"

  3_detailed_design:
    activities:
      - "Finalized geometry and analysis"
      - "Material and process decisions"
    deliverables:
      - "Complete CI package"
      - "Updated CI_Definition.yaml"

  4_design_released:
    activities:
      - "Design approval"
      - "Release to manufacturing"
    deliverables:
      - "Released drawings"
      - "Released CI metadata"

  5_in_production:
    activities:
      - "Manufacturing and inspection"
    deliverables:
      - "Production records"
      - "Quality reports"

  6_in_service:
    activities:
      - "Installation on aircraft"
      - "In-service monitoring"
    deliverables:
      - "Service data"
      - "SHM records (where applicable)"

  7_retired:
    activities:
      - "Removal from service"
      - "Recycling/disposal"
    deliverables:
      - "Retirement documentation"
```

---

## 6. Integration with OPT-IN Framework

```yaml
opt_in_integration:

  requirements_traceability:
    location: "53-00-03_Requirements"
    mechanism: "Requirements_Traceability.csv per CI + TRACE/VERIF CSVs"
    example: "CI-53-400-SPAR-FWD → RQ-53-00-01-001 (Ultimate Load Capability)"

  subsystem_architecture:
    location: "53-20_Subsystems"
    mechanism: "subsystem_ref in CI_Definition.yaml"
    example: "CI-53-400-BAY-MLG-L-BEAM → 53-20-04_Centerbody_Landing_Gear_Bays"

  structural_substantiation:
    location: "53-50_Structures"
    mechanism: "structural_role + CI_Number in 53-50 artefacts"
    example: "CI-53-400-SPAR-FWD (Primary) → 53-50-01_Primary_Structure substantiation"

  production_planning:
    location: "53-00-09_Production_Planning"
    mechanism: "Manufacturing_Plan.md and ASSETS/Production in each CI"
    example: "CI-53-100-SKN-U01 → Layup schedule, cure cycle, tooling"

  certification:
    location: "53-00-10_Certification"
    mechanism: "CI references in compliance checklists and evidence"
    example: "CI-53-400-SPAR-FWD → stress/test reports in evidence list"
```

---

## 7. Document Control

- **Document**: ATA 53 Configuration Items (CI) Structure and Governance
- **File**: `53-00-04_Design/02_Configuration_Items/53-00-04-02-004_CI_Structure_and_Governance.md`
- **Version**: 1.0
- **Date**: 2025-11-22
- **Owner**: ATA 53 Configuration Manager
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

Related documents:

- [../../53-00-03_Requirements/](../../53-00-03_Requirements/) – Fuselage general requirements.
- [../../53-20_Subsystems/](../../53-20_Subsystems/) – Fuselage subsystems architecture.
- [../../53-50_Structures/](../../53-50_Structures/) – Structural substantiation.
- Configuration Management Plan – Program-level CM rules.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.
