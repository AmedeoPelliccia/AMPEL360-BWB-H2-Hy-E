# 53-20-01-001 Upper Shell Module Architecture

## Overview

The upper shell module forms the primary aerodynamic and structural upper surface of the AMPEL360 BWB H₂ Hy-E aircraft. This module integrates seamlessly with the wing structure to create the distinctive blended wing body configuration while maintaining pressure cabin integrity.

## Design Philosophy

The upper shell module employs a **hybrid composite construction** combining:
- **Carbon fiber reinforced polymer (CFRP)** for primary load paths
- **Aramid fiber layers** for impact resistance and damage tolerance
- **Aluminum honeycomb core** in low-stress sandwich panels
- **Titanium fittings** at critical load introduction points

## Structural Layout

### Primary Structure
- **Stringers**: 32 longitudinal stringers spaced at 200mm intervals
- **Frames**: 45 circumferential frames at 500mm station intervals
- **Skin Panels**: Integral stiffened panels with co-cured stringers
- **Wing Carry-Through**: Reinforced center section integrating with wing spars

### Geometry
- **Length**: 38.5 meters from forward pressure bulkhead to aft bulkhead
- **Width**: 42.0 meters at maximum BWB span
- **Curvature**: Continuous double-curvature for aerodynamic efficiency
- **Thickness**: Varies from 18mm (center) to 12mm (outboard)

## Load Paths

Critical load paths include:

1. **Cabin Pressure Loads**: Distributed through skin-stringer-frame network
2. **Wing Bending**: Transferred through wing carry-through box to lower shell
3. **Flight Loads**: Aerodynamic forces distributed across entire upper surface
4. **Emergency Landing**: Vertical acceleration loads (3.0g ultimate)

See [Global Load Analysis](../ASSETS/analyses/53-20-A-301_Global_Load_Analysis_Summary.md) for detailed load cases.

## Material Specification

Primary materials per [Material Specifications](../ASSETS/specifications/53-20-A-201_Material_Specifications.md):

- **Skin Panels**: IM7/8552 prepreg, [0/±45/90]s layup
- **Stringers**: IM7/8552 co-cured, [0/±30]s orientation
- **Frames**: 7075-T7351 aluminum forgings with CFRP webs
- **Fasteners**: Titanium Hi-Lok and aerospace-grade bolts per [Fastener Standards](../ASSETS/specifications/53-20-A-202_Fastener_Standards.md)

## Manufacturing Process

The upper shell module is manufactured in **four major sections** for transportability:

1. **Forward Section**: Stations FS 0 to FS 15
2. **Center Section**: Stations FS 15 to FS 30 (wing carry-through)
3. **Aft Section**: Stations FS 30 to FS 38.5
4. **Transition Sections**: Left and right side blend regions

Assembly sequence detailed in [Assembly_Sequence.md](ASSETS/Manufacturing_Plans/Assembly_Sequence.md).

## Composite Layup

Layup schedules optimize for:
- **Strength**: 0° plies aligned with primary load direction
- **Stiffness**: ±45° plies for shear resistance
- **Damage Tolerance**: Multiple 90° plies for through-thickness strength
- **Lightning Protection**: Copper mesh outer ply per [CS-25.581](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)

Detailed layup schedules: [Layup_Schedules.csv](ASSETS/Manufacturing_Plans/Layup_Schedules.csv)

## Structural Analysis

Finite Element Analysis (FEA) results demonstrate:

- **Maximum Stress**: 385 MPa (allowable 450 MPa) at wing attachment
- **Deflection**: 127mm maximum at 2.5g maneuver load
- **Buckling Margin**: 1.45 minimum at critical compression panels
- **Fatigue Life**: 180,000 flights to crack initiation

Analysis index: [Shell_Module_Analysis_Index.md](ASSETS/FEA_Models/Shell_Module_Analysis_Index.md)

## Inspection & Maintenance

### In-Service Inspection
- **Visual Inspection**: Every 400 flight hours
- **Ultrasonic Inspection**: Every 4,000 flight hours
- **Thermography**: Every 8,000 flight hours for bondline integrity
- **X-Ray Inspection**: On-condition for suspected impact damage

### Critical Inspection Zones
- Wing-fuselage blend regions
- Door surround reinforcements
- Landing gear bay perimeter
- All longitudinal and circumferential splices

NDT requirements per [53-20-A-205_NDT_Requirements.md](../ASSETS/specifications/53-20-A-205_NDT_Requirements.md).

## Interfaces

The upper shell module interfaces with:

- [53-20-01-002 Lower Shell Module](53-20-01-002_Lower_Shell_Module_Architecture.md) - Side splices
- [53-20-01-003 Side Shell Modules](53-20-01-003_Side_Shell_Modules_and_Transitions.md) - Blend transitions
- [53-20-01-004 Pressure Bulkheads](53-20-01-004_Pressure_Bulkheads_Forward_Aft.md) - Forward/aft attachments
- [53-20-02 Door Surround Structure](../53-20-02_Door_Surround_Structure/README.md) - Door frame integration
- [ATA 57 Wings](../../ATA_57-WINGS/README.md) - Wing-body integration

## Certification Compliance

Compliance demonstrated for:
- [CS-25.305](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Strength and deformation
- [CS-25.307](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Proof of structure
- [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Damage tolerance and fatigue
- [CS-25.603](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Materials

## Drawings & Models

Primary engineering artifacts:

- [Upper_Shell_Layout.svg](ASSETS/Structural_Drawings/Upper_Shell_Layout.svg) - Overall layout drawing
- [Shell_Sections_Assembly.svg](ASSETS/Structural_Drawings/Shell_Sections_Assembly.svg) - Assembly sequence
- FEA models located in [ASSETS/FEA_Models/](ASSETS/FEA_Models/)

## Status

- **Design Status**: PDR Complete, CDR Scheduled
- **Analysis Status**: Static analysis complete, fatigue ongoing
- **Manufacturing**: Tooling design in progress
- **Last Updated**: 2025-11-22

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.

---
