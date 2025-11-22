# 02_Configuration_Items – Fuselage Configuration Items

## Purpose

This folder contains the complete Configuration Item (CI) structure for the AMPEL360 BWB fuselage. Every structural component is tracked as a CI with full traceability, lifecycle management, and design documentation.

## Contents

### Core CI Documentation
- **[53-00-04-02-001_CI_Master_Index.md](53-00-04-02-001_CI_Master_Index.md)** – Master index of all fuselage CIs
- **[53-00-04-02-002_CI_Numbering_Convention.md](53-00-04-02-002_CI_Numbering_Convention.md)** – CI numbering scheme and rules
- **[53-00-04-02-003_CI_Lifecycle_Management.md](53-00-04-02-003_CI_Lifecycle_Management.md)** – CI lifecycle states and change control
- **[53-00-04-02-004_CI_Structure_and_Governance.md](53-00-04-02-004_CI_Structure_and_Governance.md)** – CI structure, metadata model, and governance

### Zone Directories
- **[Zone_100_Nose_Section/](Zone_100_Nose_Section/)** – CI-53-100 and child CIs
- **[Zone_200_Forward_Cabin/](Zone_200_Forward_Cabin/)** – CI-53-200 and child CIs
- **[Zone_300_Mid_Cabin/](Zone_300_Mid_Cabin/)** – CI-53-300 and child CIs
- **[Zone_400_Center_Wing_Box/](Zone_400_Center_Wing_Box/)** – CI-53-400 and child CIs (critical zone)
- **[Zone_500_Aft_Cabin/](Zone_500_Aft_Cabin/)** – CI-53-500 and child CIs
- **[Zone_600_Tail_Section/](Zone_600_Tail_Section/)** – CI-53-600 and child CIs

### CI Management Assets
- **[ASSETS/](ASSETS/)** – CI database, tracking files, and dashboards

## CI Hierarchy Overview

```yaml
ci_structure:
  top_level: "CI-53-000"            # ATA 53 Fuselage

  zone_level:
    - "CI-53-100"  # Nose Section (Stations 0-150)
    - "CI-53-200"  # Forward Cabin (Stations 150-300)
    - "CI-53-300"  # Mid Cabin (Stations 300-450)
    - "CI-53-400"  # Center Wing Box (Stations 450-600) - CRITICAL
    - "CI-53-500"  # Aft Cabin (Stations 600-750)
    - "CI-53-600"  # Tail Section (Stations 750-900)

  component_level:
    # Examples:
    - "CI-53-100-BHD-FWD"     # Forward Pressure Bulkhead
    - "CI-53-200-DOOR-1L"     # Door 1L Frame Assembly
    - "CI-53-400-SPAR-FWD"    # Forward Wing Spar
    - "CI-53-400-BAY-MLG-L"   # Left Main Landing Gear Bay
```

## CI Metadata Model

Each CI is defined by a `CI_Definition.yaml` file containing:

```yaml
ci_metadata:
  ci_number: "CI-XX-XXX-TYPE-ID"
  ci_name: "Descriptive Name"
  parent_ci: "Parent CI Number"
  zone: "Zone Number"

classification:
  type: "Component Type"
  criticality: "Critical|High|Medium|Low"
  material_primary: "Primary Material"
  structural_role: "Primary|Secondary"

physical_properties:
  weight_target_kg: 0.0
  weight_actual_kg: 0.0
  weight_margin_percent: 0.0
  cg_x: 0.0
  cg_y: 0.0
  cg_z: 0.0

status:
  design_status: "Concept|Preliminary|Detailed|Released|Obsolete"
  analysis_status: "Not Started|In Progress|Complete"
  test_status: "Not Started|In Progress|Complete"
  production_status: "Design|Tooling|Production|Complete"

traceability:
  requirements: []
  parent_drawing: ""
  specification: ""
  subsystem_ref: ""  # Link to 53-20 subsystem

interfaces: []

approval:
  design_approved_by: ""
  design_approved_date: ""
  certification_authority: "EASA|FAA|Both|N/A"
```

## Standard CI Folder Structure

Each CI has its own folder with this structure:

```text
CI-XX-XXX-TYPE-ID_Descriptive_Name/
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

## Key Features

### 1. Traceability
- **To Requirements**: Each CI links to requirements in [../../53-00-03_Requirements/](../../53-00-03_Requirements/)
- **To Subsystems**: Each CI references its parent subsystem in [../../53-20_Subsystems/](../../53-20_Subsystems/)
- **To Certification**: CIs support structural substantiation in [../../53-50_Structures/](../../53-50_Structures/)

### 2. Lifecycle Management
CIs progress through defined lifecycle states:
1. Concept
2. Preliminary Design
3. Detailed Design
4. Design Released
5. In Production
6. In Service
7. Retired

### 3. Primary vs. Secondary Structure
The `structural_role` field enables automatic filtering:
- **Primary Structure**: Critical load-bearing components → substantiation in 53-50-01
- **Secondary Structure**: Non-critical components → substantiation in 53-50-02

### 4. Configuration Control
All CI changes follow formal change management:
- Change Request → Impact Assessment → Approval → Implementation → Verification

## CI Database

The master CI database is maintained in:
- **[ASSETS/53-00-04-02-A-001_CI_Database.csv](ASSETS/53-00-04-02-A-001_CI_Database.csv)**

This CSV file is the single source of truth for all CI metadata and feeds dashboards and reporting tools.

## Usage

### For Design Engineers
1. Review CI structure and numbering convention
2. Create CI folder for new component
3. Fill in `CI_Definition.yaml` with complete metadata
4. Develop design documentation
5. Link to requirements and subsystems
6. Update CI database

### For Configuration Managers
1. Monitor CI status through dashboards
2. Review change requests for impact
3. Maintain CI database integrity
4. Generate status reports
5. Coordinate design reviews

### For Certification Team
1. Use CI database to identify primary structure
2. Link CIs to substantiation documents in 53-50
3. Track certification status by CI
4. Generate compliance evidence lists

## Related Documentation

- **Design Philosophy**: [../01_Design_Overview/53-00-04-01-001_Design_Philosophy.md](../01_Design_Overview/53-00-04-01-001_Design_Philosophy.md)
- **Requirements**: [../../53-00-03_Requirements/](../../53-00-03_Requirements/)
- **Subsystems**: [../../53-20_Subsystems/](../../53-20_Subsystems/)
- **Structures**: [../../53-50_Structures/](../../53-50_Structures/)
- **Templates**: [../ASSETS/templates/](../ASSETS/templates/)

---

## Document Control

- **Folder**: `02_Configuration_Items`
- **Version**: 1.0
- **Date**: 2025-11-22
- **Owner**: ATA 53 Configuration Manager
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Last AI update: _2025-11-22_.
