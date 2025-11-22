# 53-00-04-02-001: CI Master Index – ATA 53 Fuselage

## 1. Overview

This document provides the master index of all Configuration Items (CIs) for the AMPEL360 BWB fuselage (ATA 53). It serves as the authoritative reference for the complete CI hierarchy.

## 2. Top-Level CI

**CI-53-000: ATA 53 Fuselage**
- **Description**: Complete fuselage assembly
- **Weight Target**: 45,000 kg
- **Material**: Mixed (CFRP primary, metals secondary)
- **Status**: Production
- **Criticality**: Critical

## 3. Zone-Level CIs

### CI-53-100: Nose Section
- **Stations**: 0 to 150
- **Weight Target**: 3,500 kg
- **Material**: CFRP/Metal hybrid
- **Major Subsystems**: Pressure bulkhead, nose gear bay, avionics bay
- **Folder**: [Zone_100_Nose_Section/](Zone_100_Nose_Section/)
- **Index**: [Zone_100_Nose_Section/53-00-04-02-101_CI-53-100_Zone_Index.csv](Zone_100_Nose_Section/53-00-04-02-101_CI-53-100_Zone_Index.csv)

### CI-53-200: Forward Cabin
- **Stations**: 150 to 300
- **Weight Target**: 8,500 kg
- **Material**: CFRP primary structure
- **Major Subsystems**: First class cabin, forward doors, floor grid
- **Folder**: [Zone_200_Forward_Cabin/](Zone_200_Forward_Cabin/)
- **Index**: [Zone_200_Forward_Cabin/53-00-04-02-201_CI-53-200_Zone_Index.csv](Zone_200_Forward_Cabin/53-00-04-02-201_CI-53-200_Zone_Index.csv)

### CI-53-300: Mid Cabin
- **Stations**: 300 to 450
- **Weight Target**: 10,500 kg
- **Material**: CFRP primary structure
- **Major Subsystems**: Economy cabin, mid doors, wing-body blend
- **Folder**: [Zone_300_Mid_Cabin/](Zone_300_Mid_Cabin/)
- **Index**: [Zone_300_Mid_Cabin/53-00-04-02-301_CI-53-300_Zone_Index.csv](Zone_300_Mid_Cabin/53-00-04-02-301_CI-53-300_Zone_Index.csv)

### CI-53-400: Center Wing Box (CRITICAL)
- **Stations**: 450 to 600
- **Weight Target**: 12,000 kg
- **Material**: CFRP primary with titanium fittings
- **Major Subsystems**: Wing spars, main gear bays, center box
- **Folder**: [Zone_400_Center_Wing_Box/](Zone_400_Center_Wing_Box/)
- **Index**: [Zone_400_Center_Wing_Box/53-00-04-02-401_CI-53-400_Zone_Index.csv](Zone_400_Center_Wing_Box/53-00-04-02-401_CI-53-400_Zone_Index.csv)
- **Note**: This is the most structurally critical zone

### CI-53-500: Aft Cabin
- **Stations**: 600 to 750
- **Weight Target**: 7,000 kg
- **Material**: CFRP primary structure
- **Major Subsystems**: Aft cabin, aft galleys, empennage attachment
- **Folder**: [Zone_500_Aft_Cabin/](Zone_500_Aft_Cabin/)
- **Index**: [Zone_500_Aft_Cabin/53-00-04-02-501_CI-53-500_Zone_Index.csv](Zone_500_Aft_Cabin/53-00-04-02-501_CI-53-500_Zone_Index.csv)

### CI-53-600: Tail Section
- **Stations**: 750 to 900
- **Weight Target**: 3,500 kg
- **Material**: CFRP with titanium for APU bay
- **Major Subsystems**: Aft bulkhead, tail cone, APU bay, empennage supports
- **Folder**: [Zone_600_Tail_Section/](Zone_600_Tail_Section/)
- **Index**: [Zone_600_Tail_Section/53-00-04-02-601_CI-53-600_Zone_Index.csv](Zone_600_Tail_Section/53-00-04-02-601_CI-53-600_Zone_Index.csv)

## 4. Total CI Count Summary

| Zone | CI Count (Planned) | Primary CIs | Secondary CIs | Status |
|------|-------------------:|------------:|--------------:|--------|
| 100 | ~150 | ~120 | ~30 | In Progress |
| 200 | ~200 | ~160 | ~40 | In Progress |
| 300 | ~220 | ~180 | ~40 | Preliminary |
| 400 | ~250 | ~220 | ~30 | In Progress |
| 500 | ~180 | ~140 | ~40 | Preliminary |
| 600 | ~120 | ~95 | ~25 | Preliminary |
| **Total** | **~1,120** | **~915** | **~205** | - |

**Note**: CI counts are estimates and will be refined as the design matures.

## 5. CI Database

The master CI database containing all CIs is maintained at:
- **[ASSETS/53-00-04-02-A-001_CI_Database.csv](ASSETS/53-00-04-02-A-001_CI_Database.csv)**

This CSV file contains:
- CI Number, Name, Parent CI, Zone
- Type, Material, Weight, Criticality, Structural Role
- Design Status, Analysis Status, Test Status, Production Status
- Subsystem reference, Drawing number, Specification
- Traceability to requirements

## 6. CI Visualization

The CI hierarchy is visualized in:
- **[ASSETS/53-00-04-02-A-002_CI_Hierarchy_Tree.svg](ASSETS/53-00-04-02-A-002_CI_Hierarchy_Tree.svg)**

This provides a graphical representation of the complete CI tree structure.

## 7. Key CI Examples

### Primary Structure CIs (Critical Load-Bearing)

| CI Number | CI Name | Zone | Material | Weight (kg) |
|-----------|---------|------|----------|-------------|
| CI-53-100-BHD-FWD | Forward Pressure Bulkhead | 100 | CFRP | 450 |
| CI-53-200-DOOR-1L-FR | Door 1L Frame Assembly | 200 | CFRP/Ti | 180 |
| CI-53-400-SPAR-FWD | Forward Wing Spar | 400 | CFRP | 2,200 |
| CI-53-400-SPAR-REAR | Rear Wing Spar | 400 | CFRP | 2,000 |
| CI-53-400-BAY-MLG-L | Left Main Gear Bay Structure | 400 | CFRP/Ti | 850 |
| CI-53-600-BHD-AFT | Aft Pressure Bulkhead | 600 | CFRP | 420 |

### Secondary Structure CIs

| CI Number | CI Name | Zone | Material | Weight (kg) |
|-----------|---------|------|----------|-------------|
| CI-53-200-FLR-BEAM-S-L | Secondary Floor Beams Left | 200 | Aluminum | 180 |
| CI-53-300-PANEL-INT-01 | Interior Panel 01 | 300 | GFRP | 25 |
| CI-53-500-FAIRING-AFT-01 | Aft Fairing Panel 01 | 500 | GFRP | 18 |

## 8. CI Naming Convention

See [53-00-04-02-002_CI_Numbering_Convention.md](53-00-04-02-002_CI_Numbering_Convention.md) for detailed naming rules.

**Format**: `CI-53-[ZONE]-[TYPE]-[ID]`

**Common Type Codes**:
- **FR**: Frame
- **SKN**: Skin panel
- **SPAR**: Spar
- **BEAM**: Beam
- **BHD**: Bulkhead
- **DOOR**: Door frame
- **FLR**: Floor structure
- **BAY**: Bay structure
- **FITTING**: Fitting or attachment
- **PANEL**: Panel (interior or exterior)

## 9. CI Lifecycle Status

CIs progress through defined lifecycle states:
1. **Concept**: Initial sizing
2. **Preliminary**: Initial design
3. **Detailed**: Final design
4. **Released**: Approved for manufacturing
5. **In Production**: Being manufactured
6. **In Service**: Installed on aircraft
7. **Retired**: End of life

See [53-00-04-02-003_CI_Lifecycle_Management.md](53-00-04-02-003_CI_Lifecycle_Management.md) for details.

## 10. Accessing CI Details

To find details about a specific CI:

1. Identify the zone from the CI number (e.g., CI-53-400-xxx is in Zone 400)
2. Navigate to the appropriate zone folder
3. Find the CI's dedicated folder
4. Review the `CI_Definition.yaml` and associated documentation

Example path for CI-53-400-SPAR-FWD:
```
02_Configuration_Items/
└── Zone_400_Center_Wing_Box/
    └── CI-53-400-SPAR-FWD_Forward_Wing_Spar/
        ├── CI_Definition.yaml
        ├── Design_Description.md
        ├── Requirements_Traceability.csv
        └── ASSETS/
```

## 11. Integration with Other ATA 53 Folders

### Requirements (53-00-03)
Each CI traces to requirements via `Requirements_Traceability.csv`

### Subsystems (53-20)
Each CI references its parent subsystem via `subsystem_ref` in `CI_Definition.yaml`

### Structures (53-50)
Primary CIs feed into structural substantiation documentation in 53-50

### Production Planning (53-00-09)
Each CI's `Manufacturing_Plan.md` feeds production planning

## 12. Maintenance and Updates

**Responsibility**: ATA 53 Configuration Manager

**Update Frequency**:
- CI Database: Weekly during active design
- Zone Indices: Monthly
- Master Index: Quarterly or after major design reviews

**Change Control**:
All CI additions, deletions, or major modifications require:
1. Change Request
2. Impact Assessment
3. Approval by Configuration Control Board
4. Update to CI Database and indices
5. Notification to affected teams

## 13. Related Documents

- **CI Numbering Convention**: [53-00-04-02-002_CI_Numbering_Convention.md](53-00-04-02-002_CI_Numbering_Convention.md)
- **CI Lifecycle Management**: [53-00-04-02-003_CI_Lifecycle_Management.md](53-00-04-02-003_CI_Lifecycle_Management.md)
- **CI Structure and Governance**: [53-00-04-02-004_CI_Structure_and_Governance.md](53-00-04-02-004_CI_Structure_and_Governance.md)
- **CI Database**: [ASSETS/53-00-04-02-A-001_CI_Database.csv](ASSETS/53-00-04-02-A-001_CI_Database.csv)

---

## Document Control

- **Document ID**: 53-00-04-02-001
- **Title**: CI Master Index – ATA 53 Fuselage
- **Version**: 1.0
- **Date**: 2025-11-22
- **Owner**: ATA 53 Configuration Manager
- **Approval**: _[to be completed]_
- **Status**: DRAFT
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.
