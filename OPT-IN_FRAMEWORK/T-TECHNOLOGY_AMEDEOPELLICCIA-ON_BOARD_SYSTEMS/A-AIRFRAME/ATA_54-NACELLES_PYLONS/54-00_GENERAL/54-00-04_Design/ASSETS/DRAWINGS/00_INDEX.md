# 54-00-04_Design / ASSETS / DRAWINGS

## Purpose

The `DRAWINGS` directory contains the **2D design authority** for the AMPEL360 BWB nacelle and pylon structures (ATA 54). These drawings provide the graphical reference for:

- Configuration Items (CIs) in `54-00-04_Design/02_Configuration_Items/`
- Assemblies in [54-00-04_Design/ASSETS/ASSEMBLIES/](../ASSEMBLIES/)
- Inputs and evidence for **54-50_Structures** analysis and [54-00-03_Requirements](../../../54-00-03_Requirements/) verification

All drawings are stored as **YAML metadata files** with placeholder status pending CAD model completion.

---

## Directory Structure

```text
54-00-04_Design/ASSETS/DRAWINGS/
├── 00_INDEX.md                    (this file)
│
├── GA/                             # General Arrangement drawings
│   ├── 54-00-04-D001_DRWG_Nacelle_Primary_Structure_GA.yaml
│   └── 54-00-04-D003_DRWG_Pylon_General_Arrangement.yaml
│
├── DETAIL/                         # Detail drawings
│   ├── 54-00-04-D002_DRWG_Nacelle_Primary_Structure_Dimensions.yaml
│   └── 54-00-04-D004_DRWG_Pylon_Wing_Attachment_Details.yaml
│
├── INTERFACE/                      # Interface control drawings
│   ├── 54-00-04-D005_DRWG_Nacelle_Pylon_Interface.yaml
│   └── 54-00-04-D007_DRWG_Engine_Mount_Interface.yaml
│
├── INSTALLATION/                   # Installation drawings
│   ├── 54-00-04-D006_DRWG_Thrust_Reverser_Installation.yaml
│   └── 54-00-04-D010_DRWG_SHM_Sensor_Locations.yaml
│
├── SECTION/                        # Section/structural drawings
│   ├── 54-00-04-D008_DRWG_Nacelle_Cross_Sections.yaml
│   └── 54-00-04-D009_DRWG_Pylon_Load_Path_Diagram.yaml
│
└── TEMPLATES/                      # Drawing templates
    └── 54-00-04-D000_DRWG_Template.yaml
```

---

## Drawing Register

### Complete Drawing List

| Drawing ID | Title | Type | Related Assembly | Status | Version |
|------------|-------|------|------------------|--------|---------|
| 54-00-04-D001 | Nacelle Primary Structure - General Arrangement | GA | 54-00-04-A001 | Planned | 0.1.0 |
| 54-00-04-D002 | Nacelle Primary Structure - Dimensions | Detail | 54-00-04-A001 | Planned | 0.1.0 |
| 54-00-04-D003 | Pylon General Arrangement | GA | 54-00-04-A002 | Planned | 0.1.0 |
| 54-00-04-D004 | Pylon-Wing Attachment Details | Detail | 54-00-04-A002 | Planned | 0.1.0 |
| 54-00-04-D005 | Nacelle-Pylon Interface Drawing | Interface | 54-00-04-A003 | Planned | 0.1.0 |
| 54-00-04-D006 | Thrust Reverser Installation | Installation | 54-00-04-A004 | Planned | 0.1.0 |
| 54-00-04-D007 | Engine Mount Interface Drawing | Interface | 54-00-04-A005 | Planned | 0.1.0 |
| 54-00-04-D008 | Nacelle Cross-Sections | Section | 54-00-04-A001 | Planned | 0.1.0 |
| 54-00-04-D009 | Pylon Load Path Diagram | Section | 54-00-04-A002 | Planned | 0.1.0 |
| 54-00-04-D010 | SHM Sensor Locations | Installation | 54-00-03-07-001 | Planned | 0.1.0 |

---

## Status Summary

### By Drawing Type

| Type | Count | Status |
|------|-------|--------|
| GA (General Arrangement) | 2 | All Planned |
| Detail | 2 | All Planned |
| Interface | 2 | All Planned |
| Installation | 2 | All Planned |
| Section | 2 | All Planned |
| **Total** | **10** | **All Planned** |

### By Assembly

| Assembly ID | Assembly Title | Drawing Count | Drawing IDs |
|-------------|----------------|---------------|-------------|
| 54-00-04-A001 | Nacelle Primary Structure Assembly | 3 | D001, D002, D008 |
| 54-00-04-A002 | Pylon Structure Assembly | 3 | D003, D004, D009 |
| 54-00-04-A003 | Nacelle-Pylon Interface Assembly | 1 | D005 |
| 54-00-04-A004 | Thrust Reverser Structure Assembly | 1 | D006 |
| 54-00-04-A005 | Engine Mount Structure Assembly | 1 | D007 |
| 54-00-03-07-001 | Nacelle Structure SHM (Requirement) | 1 | D010 |

---

## Traceability Matrix

### Drawing → Assembly Traceability

| Drawing ID | Drawing Title | Related Assembly ID | Assembly Title |
|------------|---------------|---------------------|----------------|
| 54-00-04-D001 | Nacelle Primary Structure - General Arrangement | 54-00-04-A001 | Nacelle Primary Structure Assembly |
| 54-00-04-D002 | Nacelle Primary Structure - Dimensions | 54-00-04-A001 | Nacelle Primary Structure Assembly |
| 54-00-04-D003 | Pylon General Arrangement | 54-00-04-A002 | Pylon Structure Assembly |
| 54-00-04-D004 | Pylon-Wing Attachment Details | 54-00-04-A002 | Pylon Structure Assembly |
| 54-00-04-D005 | Nacelle-Pylon Interface Drawing | 54-00-04-A003 | Nacelle-Pylon Interface Assembly |
| 54-00-04-D006 | Thrust Reverser Installation | 54-00-04-A004 | Thrust Reverser Structure Assembly |
| 54-00-04-D007 | Engine Mount Interface Drawing | 54-00-04-A005 | Engine Mount Structure Assembly |
| 54-00-04-D008 | Nacelle Cross-Sections | 54-00-04-A001 | Nacelle Primary Structure Assembly |
| 54-00-04-D009 | Pylon Load Path Diagram | 54-00-04-A002 | Pylon Structure Assembly |
| 54-00-04-D010 | SHM Sensor Locations | 54-00-04-A001, 54-00-04-A002 | Nacelle & Pylon Primary Structures |

### Drawing → Requirement Traceability

| Drawing ID | Related Requirement IDs | Requirement Titles |
|------------|-------------------------|-------------------|
| 54-00-04-D001 | 54-00-03-01-001 | Nacelle Structural Integrity |
| 54-00-04-D002 | 54-00-03-01-001 | Nacelle Structural Integrity |
| 54-00-04-D003 | 54-00-03-01-001 | Nacelle Structural Integrity |
| 54-00-04-D004 | 54-00-03-01-001, 54-00-03-05-001 | Nacelle Structural Integrity, Pylon-Wing Interface |
| 54-00-04-D005 | 54-00-03-05-002 | Nacelle-Pylon Interface Requirements |
| 54-00-04-D006 | 54-00-03-01-001, 78-00-03-01-001 | Nacelle Structural Integrity, Thrust Reverser Req |
| 54-00-04-D007 | 54-00-03-05-003, 71-00-03-01-001 | Engine Mount Interface, Engine Mount Requirements |
| 54-00-04-D008 | 54-00-03-01-001 | Nacelle Structural Integrity |
| 54-00-04-D009 | 54-00-03-01-001 | Nacelle Structural Integrity |
| 54-00-04-D010 | 54-00-03-07-001 | Nacelle Structure SHM Compatibility |

---

## Naming Convention

All drawings follow the established pattern:

```
<XX>-<YY>-<ZZ>-D<nnn>_<CATEGORY>_<ShortName>.yaml
```

Where:
- `XX-YY-ZZ` = ATA reference (54-00-04)
- `D<nnn>` = Drawing number (D001, D002, etc.)
- `CATEGORY` = DRWG for all drawings
- `ShortName` = Descriptive name in PascalCase with underscores

---

## Integration with Other Structures

### Configuration Items (CIs)

Each CI's definition should reference its primary drawings. Future CI definitions in `54-00-04_Design/02_Configuration_Items/` will link back to these drawings.

### Assemblies

Assembly metadata files in [ASSETS/ASSEMBLIES/](../ASSEMBLIES/) reference their main assembly drawings. Each assembly YAML should include a `cad_master_drawing` field pointing to the relevant drawing ID.

### Requirements

Requirements in [54-00-03_Requirements](../../../54-00-03_Requirements/) use these drawings as verification evidence for geometry- and interface-related requirements.

### Structures Analysis

Structural analysis reports in **54-50_Structures** will reference drawing IDs as geometry authority.

---

## Next Steps

1. **Complete CAD Models**: Develop 3D CAD models for each assembly
2. **Generate SVG Drawings**: Export 2D drawings as SVG files from approved CAD models
3. **Update Drawing Status**: Change status from "Planned" to "In Progress" → "Review" → "Approved"
4. **Establish Drawing Review Process**: Define review and approval workflow
5. **Link to PDM/PLM System**: Integrate with Product Lifecycle Management tools
6. **Create Drawing Standards Document**: Define detailed standards for line types, dimensions, annotations

---

## Document Control

- **Folder**: `54-00-04_Design/ASSETS/DRAWINGS`
- **Status**: OPERATIONAL – Initial structure and metadata defined
- **Version**: 1.0
- **Date**: 2026-01-02
- **Owner**: ATA 54 Nacelle & Pylon Drawing Authority
- **Repository**: `AMPEL360-AIR-T`
- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Human approver**: _[to be completed]_.
- **Last AI update**: 2026-01-02

---
