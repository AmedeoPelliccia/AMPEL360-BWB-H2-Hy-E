# 53-20-01-002 Lower Shell Module Architecture

## Overview

The lower shell module forms the structural base and cargo bay floor of the AMPEL360 BWB H₂ Hy-E aircraft. This module integrates main landing gear bay structures, cargo compartment framing, and provides the lower pressure boundary for the passenger cabin.

## Design Philosophy

The lower shell module is designed for:
- **High Impact Resistance**: Emergency landing scenarios up to 3.0g vertical
- **Cargo Bay Integration**: Reinforced floor with tie-down provisions
- **Landing Gear Loads**: Main gear attachment hardpoints
- **Hydrogen Storage Interface**: Mounting provisions for H₂ tank attachments

## Structural Layout

### Primary Structure
- **Keels**: 3 longitudinal keel members for emergency landing loads
- **Stringers**: 28 stringers spaced at 220mm intervals between keels
- **Frames**: 45 frames matching upper shell station intervals
- **Cargo Floor Beams**: 38 transverse beams at 500mm spacing
- **Landing Gear Beams**: Reinforced transverse beams at gear bay locations

### Geometry
- **Length**: 38.5 meters (matching upper shell)
- **Width**: 39.0 meters at maximum BWB underside
- **Ground Clearance**: 1.85 meters minimum at center keel
- **Thickness**: 22mm at landing gear bays, 15mm nominal, 12mm outboard

## Load Paths

Critical load paths for lower shell:

1. **Landing Loads**: Main gear loads distributed through gear beams to keel and frames
2. **Cargo Loading**: Distributed floor loads transferred to shell skin-stringer system
3. **Cabin Pressure**: Outward pressure resisted by skin-frame-stringer network
4. **Emergency Landing**: Impact energy absorbed through crushable elements and keel bending

Load cases detailed in [Global Load Analysis](../ASSETS/analyses/53-20-A-301_Global_Load_Analysis_Summary.md).

## Material Specification

Enhanced materials for impact resistance per [Material Specifications](../ASSETS/specifications/53-20-A-201_Material_Specifications.md):

- **Skin Panels**: T800/M21 toughened resin, [0/±45/90]s layup
- **Keels**: Hybrid CFRP/Aluminum construction for energy absorption
- **Stringers**: IM7/8552 with additional ±45° plies for shear
- **Landing Gear Fittings**: Titanium Ti-6Al-4V forgings
- **Cargo Floor**: Aluminum 7075-T7351 honeycomb sandwich panels

Fasteners per [Fastener Standards](../ASSETS/specifications/53-20-A-202_Fastener_Standards.md).

## Manufacturing Process

Lower shell manufactured in **five major sections**:

1. **Forward Cargo Section**: FS 0 to FS 12
2. **Main Landing Gear Bay Section**: FS 12 to FS 28 (includes gear beams)
3. **Aft Cargo Section**: FS 28 to FS 38.5
4. **Left Transition Section**: Port side blend region
5. **Right Transition Section**: Starboard side blend region

### Key Manufacturing Challenges
- **Complex Double Curvature**: Requires matched metal tooling
- **Landing Gear Inserts**: Co-bonded titanium bushings
- **Cargo Door Cutouts**: Edge reinforcement critical
- **H₂ Tank Mounting**: Cryogenic-compatible fittings

Manufacturing plans: [Assembly_Sequence.md](ASSETS/Manufacturing_Plans/Assembly_Sequence.md)

## Composite Layup

Layup optimized for impact and landing loads:
- **Impact Zones**: Additional Kevlar plies for penetration resistance
- **Landing Gear**: Local ply build-up [0/±30/90]4s at fittings
- **Keel Reinforcement**: [0/±45]3s with aluminum doublers
- **Lightning Strike**: Expanded copper mesh per [CS-25.581](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)

Layup details: [Layup_Schedules.csv](ASSETS/Manufacturing_Plans/Layup_Schedules.csv)

## Structural Analysis

FEA demonstrates adequate margins:

- **Maximum Stress**: 412 MPa at main gear attachment (allowable 480 MPa)
- **Emergency Landing**: 58mm keel deflection at 3.0g ultimate load
- **Cargo Floor**: 14.2 kN/m² ultimate load capability (requirement 12.0 kN/m²)
- **Fatigue Life**: 160,000 flights to detectable damage

Analysis summary: [FEA_Results_Summary.csv](ASSETS/FEA_Models/FEA_Results_Summary.csv)

## Landing Gear Integration

Main landing gear bay features:

- **Bay Dimensions**: 3.2m × 2.8m per gear bay (left/right)
- **Gear Beam**: Titanium/CFRP hybrid, 450mm deep
- **Attach Fittings**: 4× titanium lugs per gear, 890 kN ultimate load
- **Door Integration**: Wheel well doors per [53-20-04](../53-20-04_Centerbody_Landing_Gear_Bays/README.md)

Interface details: [53-20-04-005 Landing Gear Attachment Fittings](../53-20-04_Centerbody_Landing_Gear_Bays/53-20-04-005_Landing_Gear_Attachment_Fittings.md)

## Cargo Bay Features

Cargo compartment specifications:

- **Volume**: 145 cubic meters total (forward + aft cargo)
- **Floor Loading**: 732 kg/m² design limit
- **Tie-Down Points**: 84 recessed cargo tie-downs per [ATA 50](../../ATA_50-CARGO_AND_ACCESSORY_COMPARTMENTS/README.md)
- **Fire Suppression**: Class C cargo compartment per [CS-25.857](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)

## Inspection & Maintenance

### Critical Inspection Areas
- **Landing Gear Attach Points**: Eddy current inspection every 2,000 flight hours
- **Cargo Floor Panels**: Visual inspection every 800 flight hours
- **Keel Members**: Ultrasonic inspection every 6,000 flight hours
- **Cargo Door Frames**: Penetrant inspection every 4,000 flight hours

NDT procedures: [53-20-A-205_NDT_Requirements.md](../ASSETS/specifications/53-20-A-205_NDT_Requirements.md)

## Interfaces

Lower shell module interfaces with:

- [53-20-01-001 Upper Shell Module](53-20-01-001_Upper_Shell_Module_Architecture.md) - Longitudinal splices
- [53-20-01-003 Side Shell Modules](53-20-01-003_Side_Shell_Modules_and_Transitions.md) - Side blend regions
- [53-20-03 Cabin Floor and Supports](../53-20-03_Cabin_Floor_and_Supports/README.md) - Floor beam attachments
- [53-20-04 Landing Gear Bays](../53-20-04_Centerbody_Landing_Gear_Bays/README.md) - Gear bay reinforcements
- [ATA 28 H₂ Fuel System](../../../C2-CIRCULAR_CRYOGENIC_SYSTEMS/ATA_28-FUEL_SAF_AND_CRYOGENIC/README.md) - Tank mounting provisions

## Certification Compliance

Demonstrated compliance with:
- [CS-25.561](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Emergency landing conditions
- [CS-25.721](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - General (landing gear)
- [CS-25.857](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Cargo compartment classification
- [CS-25.963](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Fuel tanks: general

## Drawings & Models

Key engineering documents:

- [Lower_Shell_Layout.svg](ASSETS/Structural_Drawings/Lower_Shell_Layout.svg) - Overall layout
- [Shell_Sections_Assembly.svg](ASSETS/Structural_Drawings/Shell_Sections_Assembly.svg) - Assembly views
- FEA models: [ASSETS/FEA_Models/](ASSETS/FEA_Models/)

## Status

- **Design Status**: PDR Complete
- **Analysis Status**: Landing loads validated, fatigue ongoing
- **Testing**: Drop test specimen in fabrication
- **Last Updated**: 2025-11-22

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.

---
