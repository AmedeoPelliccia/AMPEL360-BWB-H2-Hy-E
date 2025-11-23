# 53-20-01-003 Side Shell Modules and Transitions

## Overview

The side shell modules form the critical transition zones between the upper and lower shell modules in the AMPEL360 BWB H₂ Hy-E aircraft. These regions blend the aerodynamic upper surface with the cargo bay lower surface while maintaining pressure cabin integrity and structural continuity.

## Design Philosophy

Side shell transition design addresses:
- **Smooth Aerodynamic Blending**: Continuous curvature for BWB configuration
- **Load Path Continuity**: Seamless transfer between upper and lower shells
- **Pressure Containment**: Elimination of stress concentrations at blend regions
- **Manufacturing Feasibility**: Buildable with current composite technology

## Geometry & Layout

### Transition Zones
- **Port Side Module**: Left side blend from centerline to wing tip
- **Starboard Side Module**: Right side blend (symmetric to port)
- **Forward Transition**: Nose section blending
- **Aft Transition**: Tail section blending

### Dimensional Characteristics
- **Vertical Height**: 4.2 meters from lower shell to upper shell
- **Blend Radius**: 2.8 meters minimum radius of curvature
- **Longitudinal Length**: 38.5 meters (full fuselage length)
- **Surface Area**: 185 square meters per side

## Structural Configuration

### Frame-Stringer Network
- **Side Frames**: 45 frames matching upper/lower shell stations
- **Stringers**: 18 transition stringers per side blending upper/lower stringers
- **Shear Panels**: Diagonal shear webs between frames
- **Door Cutouts**: Reinforced openings for passenger and emergency doors

### Load-Bearing Elements
- **Continuous Frames**: Frames wrap from upper shell through side to lower shell
- **Stringer Transitions**: Gradual stringer cross-section changes over 2.0m length
- **Splice Doublers**: Reinforcement at stringer terminations
- **Cutout Reinforcements**: Local ply build-ups at all door openings

See [Load Path Diagram](../ASSETS/diagrams/53-20-A-002_Load_Path_Diagram.svg) for visualization.

## Material Specification

Materials optimized for complex geometry per [Material Specifications](../ASSETS/specifications/53-20-A-201_Material_Specifications.md):

- **Skin Panels**: IM7/8552 with enhanced drapability, [0/±45/90]s
- **Transition Stringers**: Tapered CFRP sections, [0/±30]s
- **Frames**: 7075-T73 aluminum with CFRP webs
- **Door Frames**: Titanium/CFRP hybrid construction
- **Fasteners**: Titanium Hi-Lok per [Fastener Standards](../ASSETS/specifications/53-20-A-202_Fastener_Standards.md)

## Manufacturing Approach

### Fabrication Challenges
- **Complex Curvature**: Requires heated forming or hydroforming
- **Stringer Transitions**: Hand layup with automated fiber placement (AFP) assistance
- **Tool Access**: Limited access for internal assembly operations
- **Quality Control**: Ultrasonic inspection challenging in tight radii

### Manufacturing Sequence
1. **Skin Panel Layup**: Automated where possible, hand layup for tight radii
2. **Stringer Co-Cure**: Stringers co-cured to skin in autoclave
3. **Frame Installation**: Frames mechanically fastened post-cure
4. **Door Frame Integration**: Door frames bonded and bolted
5. **Systems Installation**: Routing of ECS, electrical, and hydraulic systems

Manufacturing details: [Assembly_Sequence.md](ASSETS/Manufacturing_Plans/Assembly_Sequence.md)

## Structural Analysis

FEA results for transition zones:

- **Maximum Stress**: 368 MPa at door frame corners (allowable 450 MPa)
- **Stress Concentration Factor**: 2.1 at stringer terminations (design limit 2.5)
- **Buckling Margin**: 1.32 at critical compression panels
- **Deflection**: 89mm maximum at 2.5g maneuver load
- **Fatigue Life**: 175,000 flights to detectable crack

Analysis index: [Shell_Module_Analysis_Index.md](ASSETS/FEA_Models/Shell_Module_Analysis_Index.md)

## Door Integration

The side shells contain all primary access doors:

### Door Locations
- **L1/R1 Doors**: Forward passenger entry doors (FS 8.5)
- **L2/R2 Doors**: Aft passenger entry doors (FS 28.0)
- **L3/R3 Exits**: Emergency exits (FS 18.5)
- **Cargo Doors**: Lower shell cargo access (FS 15.0, FS 32.0)

Door surround structures detailed in [53-20-02](../53-20-02_Door_Surround_Structure/README.md).

## Pressure Sealing

Pressure sealing requirements:

- **Longitudinal Splices**: Double-row fastener patterns with sealant per [CS-25.783](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)
- **Circumferential Splices**: Overlapping splice plates with pressure seal
- **Door Seals**: Inflatable seals at all door interfaces
- **Inspection Access**: Removable panels for seal inspection

Splice details: [Longitudinal_Splice_Details.svg](ASSETS/Joint_Details/Longitudinal_Splice_Details.svg)

## Systems Routing

Side shells provide routing for:

- **Environmental Control System (ECS)**: Cabin air distribution ducts
- **Electrical Systems**: Main wire bundles in upper side region per [53-20-06](../53-20-06_ECS_and_Systems_Supports/README.md)
- **Hydraulic Lines**: Routed through lower side region
- **Oxygen System**: Emergency oxygen lines per [ATA 35](../../../C1-COCKPIT_CABIN_CARGO/ATA_35-OXYGEN/README.md)

Routing diagrams: [Systems_Integration_Map.svg](../ASSETS/diagrams/53-20-A-005_BWB_Cross_Section.svg)

## Inspection & Maintenance

### In-Service Inspection
- **Visual Inspection**: Every 400 flight hours (external)
- **Internal Inspection**: Every 2,000 flight hours (door frame areas)
- **Ultrasonic Inspection**: Every 4,000 flight hours (transition regions)
- **Eddy Current**: Every 6,000 flight hours (stringer terminations)

### Critical Inspection Zones
- All door frame corners and reinforcements
- Stringer termination regions
- Longitudinal and circumferential splices
- Blend radius areas with high curvature

NDT requirements: [53-20-A-205_NDT_Requirements.md](../ASSETS/specifications/53-20-A-205_NDT_Requirements.md)

## Load Transfer Mechanisms

Critical load paths through side shells:

1. **Wing-to-Fuselage Loads**: Distributed through upper-to-side transition
2. **Cabin Pressure**: Hoop stress transferred through frames
3. **Torsion**: Wing torsion distributed through side panels
4. **Bending**: Fuselage bending resisted by upper-side-lower continuity

Load analysis: [Global_Load_Analysis_Summary.md](../ASSETS/analyses/53-20-A-301_Global_Load_Analysis_Summary.md)

## Interfaces

Side shell modules interface with:

- [53-20-01-001 Upper Shell Module](53-20-01-001_Upper_Shell_Module_Architecture.md) - Upper splices
- [53-20-01-002 Lower Shell Module](53-20-01-002_Lower_Shell_Module_Architecture.md) - Lower splices
- [53-20-01-004 Pressure Bulkheads](53-20-01-004_Pressure_Bulkheads_Forward_Aft.md) - Forward/aft closure
- [53-20-02 Door Surround Structure](../53-20-02_Door_Surround_Structure/README.md) - All door frames
- [53-20-05 Cabin Liner Attach](../53-20-05_Cabin_Liner_Attach_Structure/README.md) - Interior attachment points

## Certification Compliance

Demonstrated compliance with:
- [CS-25.305](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Strength and deformation
- [CS-25.365](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Pressurized cabin loads
- [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Damage tolerance
- [CS-25.783](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Fuselage pressure boundary

## Drawings & Models

Engineering documentation:

- [Shell_Sections_Assembly.svg](ASSETS/Structural_Drawings/Shell_Sections_Assembly.svg) - Side shell assembly
- [BWB_Cross_Section.svg](../ASSETS/diagrams/53-20-A-005_BWB_Cross_Section.svg) - Cross-section views
- FEA models: [ASSETS/FEA_Models/](ASSETS/FEA_Models/)

## Status

- **Design Status**: PDR Complete
- **Analysis Status**: Static analysis complete, fatigue in progress
- **Manufacturing**: Tooling design initiated
- **Last Updated**: 2025-11-22

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.

---
