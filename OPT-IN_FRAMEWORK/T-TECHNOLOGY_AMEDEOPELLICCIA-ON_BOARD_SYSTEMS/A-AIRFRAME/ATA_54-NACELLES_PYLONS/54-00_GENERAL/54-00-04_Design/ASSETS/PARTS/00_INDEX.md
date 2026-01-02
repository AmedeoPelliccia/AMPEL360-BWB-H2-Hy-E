# PARTS — Individual Part Definitions

## Overview

This folder contains detailed part-level specifications for individual components that make up the assemblies in the ATA 54 Nacelles & Pylons system. Each part has a dedicated YAML file with comprehensive metadata including materials, dimensions, manufacturing processes, interfaces, and traceability.

## Folder Structure

```
PARTS/
├── 00_INDEX.md                    (This file)
├── PARTS_CATALOG.csv              (Tabular catalog of all parts)
├── STRUCTURAL/                    (Primary structural parts)
│   ├── 54-00-04-P001_PART_Nacelle_Inlet_Lip.yaml
│   ├── 54-00-04-P002_PART_Fan_Cowl_Forward_Panel.yaml
│   ├── 54-00-04-P003_PART_Fan_Cowl_Aft_Panel.yaml
│   ├── 54-00-04-P004_PART_Core_Cowl_Panel.yaml
│   ├── 54-00-04-P005_PART_Nacelle_Structural_Frame.yaml
│   ├── 54-00-04-P006_PART_Pylon_Forward_Spar.yaml
│   └── 54-00-04-P007_PART_Pylon_Aft_Spar.yaml
├── FITTINGS/                      (Attachment and interface fittings)
│   ├── 54-00-04-P008_PART_Pylon_Wing_Attachment_Fitting.yaml
│   ├── 54-00-04-P009_PART_Engine_Mount_Forward_Fitting.yaml
│   ├── 54-00-04-P010_PART_Engine_Mount_Aft_Fitting.yaml
│   └── 54-00-04-P011_PART_Nacelle_Pylon_Interface_Bracket.yaml
├── MOVABLE/                       (Movable components)
│   ├── 54-00-04-P012_PART_Thrust_Reverser_Blocker_Door.yaml
│   └── 54-00-04-P013_PART_TR_Actuation_Link.yaml
├── SECONDARY/                     (Secondary structure and panels)
│   └── 54-00-04-P014_PART_Access_Panel_Fan_Cowl.yaml
├── HARDWARE/                      (Standard hardware items)
│   └── 54-00-04-P015_PART_Fastener_HiLok_HL11.yaml
└── TEMPLATES/                     (Part definition templates)
    └── 54-00-04-P000_PART_Template.yaml
```

## Part Register

### Summary Statistics

| Category | Count | Total Mass (kg) | Percentage |
|----------|-------|-----------------|------------|
| Structural | 7 | 161.5 | 71.2% |
| Fittings | 4 | 23.0 | 10.1% |
| Movable | 2 | 15.7 | 6.9% |
| Secondary | 1 | 1.8 | 0.8% |
| Hardware | 1 | 0.015 | <0.1% |
| **Total** | **15** | **227.0** | **100%** |

*Note: Hardware mass shown is per unit; actual quantities are in the hundreds to thousands per aircraft.*

### Complete Part List

#### Structural Parts (7 parts, 161.5 kg)

| Part ID | Title | Material | Mass (kg) | Parent Assembly | Status |
|---------|-------|----------|-----------|-----------------|--------|
| 54-00-04-P001 | Nacelle Inlet Lip | CFRP-Epoxy | 12.5 | A001 - Primary Nacelle Structure | Draft |
| 54-00-04-P002 | Fan Cowl Forward Panel | CFRP-Epoxy | 18.5 | A001 - Primary Nacelle Structure | Draft |
| 54-00-04-P003 | Fan Cowl Aft Panel | CFRP-Epoxy | 21.0 | A001 - Primary Nacelle Structure | Draft |
| 54-00-04-P004 | Core Cowl Panel | CFRP-Epoxy | 16.5 | A001 - Primary Nacelle Structure | Draft |
| 54-00-04-P005 | Nacelle Structural Frame | Ti-6Al-4V | 9.5 | A001 - Primary Nacelle Structure | Draft |
| 54-00-04-P006 | Pylon Forward Spar | CFRP-Epoxy | 45.0 | A002 - Pylon Structure | Draft |
| 54-00-04-P007 | Pylon Aft Spar | CFRP-Epoxy | 38.5 | A002 - Pylon Structure | Draft |

#### Fittings (4 parts, 23.0 kg)

| Part ID | Title | Material | Mass (kg) | Parent Assembly | Status |
|---------|-------|----------|-----------|-----------------|--------|
| 54-00-04-P008 | Pylon Wing Attachment Fitting | Steel 15-5PH | 8.5 | A002 - Pylon Structure | Draft |
| 54-00-04-P009 | Engine Mount Forward Fitting | Ti-10V-2Fe-3Al | 6.8 | A005 - Engine Mount | Draft |
| 54-00-04-P010 | Engine Mount Aft Fitting | Ti-10V-2Fe-3Al | 5.9 | A005 - Engine Mount | Draft |
| 54-00-04-P011 | Nacelle-Pylon Interface Bracket | Ti-6Al-4V | 1.8 | A003 - Nacelle-Pylon Interface | Draft |

#### Movable Parts (2 parts, 15.7 kg)

| Part ID | Title | Material | Mass (kg) | Parent Assembly | Status |
|---------|-------|----------|-----------|-----------------|--------|
| 54-00-04-P012 | Thrust Reverser Blocker Door | CFRP-Epoxy | 14.5 | A004 - Thrust Reverser | Draft |
| 54-00-04-P013 | TR Actuation Link | Ti-6Al-4V | 1.2 | A004 - Thrust Reverser | Draft |

#### Secondary Structure (1 part, 1.8 kg)

| Part ID | Title | Material | Mass (kg) | Parent Assembly | Status |
|---------|-------|----------|-----------|-----------------|--------|
| 54-00-04-P014 | Access Panel - Fan Cowl | Al 7075-T73 | 1.8 | A001 - Primary Nacelle Structure | Draft |

#### Hardware (1 part type, 0.015 kg per unit)

| Part ID | Title | Material | Mass (kg) | Parent Assembly | Status |
|---------|-------|----------|-----------|-----------------|--------|
| 54-00-04-P015 | Fastener - Hi-Lok HL11 | Steel | 0.015 | All Assemblies | Draft |

*Note: Hardware items like fasteners are used in large quantities (hundreds to thousands) across all assemblies.*

## Part → Assembly Traceability Matrix

| Part ID | Part Title | Parent Assembly ID | Assembly Title |
|---------|------------|-------------------|----------------|
| P001 | Nacelle Inlet Lip | 54-00-04-A001 | Primary Nacelle Structure Assembly |
| P002 | Fan Cowl Forward Panel | 54-00-04-A001 | Primary Nacelle Structure Assembly |
| P003 | Fan Cowl Aft Panel | 54-00-04-A001 | Primary Nacelle Structure Assembly |
| P004 | Core Cowl Panel | 54-00-04-A001 | Primary Nacelle Structure Assembly |
| P005 | Nacelle Structural Frame | 54-00-04-A001 | Primary Nacelle Structure Assembly |
| P006 | Pylon Forward Spar | 54-00-04-A002 | Pylon Structure Assembly |
| P007 | Pylon Aft Spar | 54-00-04-A002 | Pylon Structure Assembly |
| P008 | Pylon Wing Attachment Fitting | 54-00-04-A002 | Pylon Structure Assembly |
| P009 | Engine Mount Forward Fitting | 54-00-04-A005 | Engine Mount Assembly |
| P010 | Engine Mount Aft Fitting | 54-00-04-A005 | Engine Mount Assembly |
| P011 | Nacelle-Pylon Interface Bracket | 54-00-04-A003 | Nacelle-Pylon Interface Assembly |
| P012 | Thrust Reverser Blocker Door | 54-00-04-A004 | Thrust Reverser Assembly |
| P013 | TR Actuation Link | 54-00-04-A004 | Thrust Reverser Assembly |
| P014 | Access Panel - Fan Cowl | 54-00-04-A001 | Primary Nacelle Structure Assembly |
| P015 | Fastener - Hi-Lok HL11 | All | Used across all assemblies |

## Material Distribution

### Material Usage by Mass

| Material | Part Count | Total Mass (kg) | Percentage | Applications |
|----------|-----------|-----------------|------------|--------------|
| CFRP-Epoxy | 7 | 166.5 | 73.3% | Primary structures, cowls, doors |
| Ti-6Al-4V | 3 | 12.5 | 5.5% | Structural frames, brackets |
| Ti-10V-2Fe-3Al | 2 | 12.7 | 5.6% | Engine mount fittings |
| Steel 15-5PH | 1 | 8.5 | 3.7% | Wing attachment fitting |
| Al 7075-T73 | 1 | 1.8 | 0.8% | Access panels |
| Steel (hardware) | 1 | 0.015 (per unit) | - | Fasteners |
| **Total** | **15** | **227.0** | **100%** | - |

### Material Properties Summary

| Material | Density (g/cm³) | Tensile Strength (MPa) | Elastic Modulus (GPa) | Key Advantages |
|----------|----------------|------------------------|----------------------|----------------|
| CFRP-Epoxy | 1.55 | 2500-2900 | 150-170 | High strength-to-weight, corrosion resistance |
| Ti-6Al-4V | 4.43 | 895 | 114 | Excellent strength, corrosion resistance, high temp |
| Ti-10V-2Fe-3Al | 4.65 | 1170 | 107 | Superior strength-to-weight, high performance |
| Steel 15-5PH | 7.80 | 1310 | 197 | Very high strength, corrosion resistant |
| Al 7075-T73 | 2.81 | 505 | 72 | Lightweight, good strength, low cost |

## Requirements Traceability

Parts trace to the following requirements in `54-00-03_Requirements`:

| Requirement ID | Requirement Title | Related Parts |
|----------------|-------------------|---------------|
| 54-00-03-01-001 | Nacelle Structural Requirements | P001, P002, P003, P004, P005, P014 |
| 54-00-03-01-002 | Pylon Structural Requirements | P006, P007 |
| 54-00-03-02-001 | Aerodynamic Performance Requirements | P001 |
| 54-00-03-03-001 | Thermal Protection Requirements | P004 |
| 54-00-03-04-001 | Load Path Requirements | P005 |
| 54-00-03-04-002 | Pylon Load Path Requirements | P006, P007 |
| 54-00-03-05-001 | Pylon-Wing Interface Requirements | P008 |
| 54-00-03-05-002 | Nacelle-Pylon Interface Requirements | P011 |
| 54-00-03-05-003 | Engine Mount Interface Requirements | P009, P010 |
| 54-00-03-06-001 | Thrust Reverser Structural Requirements | P012, P013 |
| 54-00-03-08-001 | Acoustic Requirements | P002 |
| 78-00-03-01-001 | Thrust Reverser Functional Requirements | P012, P013 |
| 71-00-03-01-001 | Powerplant Installation Requirements | P009, P010 |

*Note: Some requirement IDs are placeholders pending creation in the Requirements folder.*

## Manufacturing Processes

| Process | Parts Using Process | Lead Time Range |
|---------|---------------------|-----------------|
| Autoclave Cure (Composites) | P001, P002, P003, P004, P006, P007, P012 | 12-18 weeks |
| CNC Machining (Titanium) | P005, P011, P013 | 8-10 weeks |
| Forging + Machining (Titanium) | P009, P010 | 20-22 weeks |
| Investment Casting + Machining (Steel) | P008 | 20 weeks |
| Sheet Metal Forming | P014 | 4 weeks |
| Standard Production (Hardware) | P015 | 2 weeks |

## Critical Parts

Parts designated as **critical** for certification:

| Part ID | Title | Cert Basis | Special Conditions |
|---------|-------|------------|-------------------|
| P001 | Nacelle Inlet Lip | CS-25.571, CS-25.1093 | Bird strike test, anti-icing cert |
| P002 | Fan Cowl Forward Panel | CS-25.571, CS-36 | Acoustic certification |
| P003 | Fan Cowl Aft Panel | CS-25.571, CS-25.933 | TR interface load test |
| P004 | Core Cowl Panel | CS-25.571, CS-25.1191 | Fire resistance test |
| P005 | Nacelle Structural Frame | CS-25.571, CS-25.613 | Fatigue testing |
| P006 | Pylon Forward Spar | CS-25.571, CS-25.613 | Static/fatigue, lightning strike |
| P007 | Pylon Aft Spar | CS-25.571, CS-25.613 | Static/fatigue, lightning strike |
| P008 | Pylon Wing Attachment Fitting | CS-25.571, CS-25.613, CS-25.899 | Fail-safe demonstration |
| P009 | Engine Mount Forward Fitting | CS-25.571, CS-25.613, CS-25.903 | Fuse pin demonstration |
| P010 | Engine Mount Aft Fitting | CS-25.571, CS-25.613, CS-25.903 | High-temp endurance |
| P012 | Thrust Reverser Blocker Door | CS-25.933, CS-25.571 | TR functional, high-cycle fatigue |
| P013 | TR Actuation Link | CS-25.933, CS-25.571 | High-cycle fatigue (20,000+ cycles) |

## Maintenance and Inspection

### Inspection Intervals

| Inspection Interval | Part IDs | Inspection Type |
|---------------------|----------|----------------|
| 500 FH | P012, P014 | Visual, functional test |
| 600 FH | P004 | Visual, thermal imaging |
| 800 FH | P002 | Visual, tap test |
| 1000 FH | P001, P003, P013 | Visual, NDT spot checks |
| 2000 FH | P005, P009, P010, P011, P015 | Visual, eddy current |
| 3000 FH | P006, P007 | Visual, ultrasonic spot checks |
| 4000 FH | P008 | Visual, magnetic particle |

### Special Maintenance Requirements

- **Anti-icing systems** (P001): Check integrity every 2000 FH
- **Acoustic panels** (P002): Condition check every 1600 FH
- **Thermal barrier coatings** (P004): Condition check every 1200 FH
- **Spherical bearings** (P009, P010, P013): Lubrication every 500-1000 FH
- **Thrust reverser actuation** (P012, P013): Functional test every 500 FH

## Design Templates

The `TEMPLATES/` subfolder contains:

- **54-00-04-P000_PART_Template.yaml** — Master template for creating new part definitions

Use this template when defining new parts to ensure consistency in metadata structure and completeness.

## Related Documentation

- **Parent Folder**: [54-00-04_Design](../)
- **Assemblies**: [ASSETS/ASSEMBLIES/](../ASSEMBLIES/)
- **Requirements**: [54-00-03_Requirements](../../54-00-03_Requirements/)
- **Drawings**: [ASSETS/DRAWINGS/](../DRAWINGS/)
- **Asset Index**: [ASSETS/INDEX.meta.yaml](../INDEX.meta.yaml)

## File Naming Convention

All part files follow the standardized naming pattern:

```
54-00-04-P<nnn>_PART_<ShortName>.yaml
```

Where:
- `54-00-04` = ATA reference (Chapter 54, Section 00, Subsection 04)
- `P<nnn>` = Part number (P001, P002, etc.)
- `PART` = Category indicator
- `<ShortName>` = Descriptive name in PascalCase with underscores

## Document Control

- **Version**: 1.0
- **Status**: Active
- **Last Updated**: 2026-01-02
- **Owner**: AMPEL360 ATA 54 Design Team
- **Review Cycle**: Quarterly or upon significant changes

---

*This index is automatically maintained. When adding new parts, update this file, the PARTS_CATALOG.csv, and the parent INDEX.meta.yaml.*
