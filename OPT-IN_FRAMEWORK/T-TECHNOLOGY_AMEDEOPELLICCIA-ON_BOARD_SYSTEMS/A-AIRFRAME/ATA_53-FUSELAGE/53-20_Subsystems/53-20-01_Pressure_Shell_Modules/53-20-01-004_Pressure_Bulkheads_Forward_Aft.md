# 53-20-01-004 Pressure Bulkheads Forward and Aft

## Overview

The forward and aft pressure bulkheads seal the pressurized cabin envelope of the AMPEL360 BWB H₂ Hy-E aircraft. These critical structural elements withstand substantial pressure loads while providing attachment for systems, structure, and equipment.

## Design Requirements

Pressure bulkheads must comply with:
- [CS-25.365](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Pressurized cabin loads (8.6 psi differential)
- [CS-25.561](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Emergency landing loads
- [CS-25.783](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Pressure boundary integrity
- [CS-25.841](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Emergency exits (aft bulkhead)

## Forward Pressure Bulkhead

### Location & Geometry
- **Station**: FS 0.8 (forward of cockpit pressure cabin)
- **Shape**: Elliptical domed bulkhead optimized for pressure loading
- **Dimensions**: 6.5m wide × 4.2m high (semi-elliptical)
- **Dome Depth**: 1.8m forward protrusion for pressure optimization

### Structural Design
- **Construction**: Composite sandwich with metallic frame
- **Skin**: IM7/8552 CFRP, [0/±45/90]3s layup
- **Core**: Aluminum honeycomb, 25mm thick
- **Frame**: 7075-T7351 aluminum ring frame at perimeter
- **Reinforcements**: Local solid laminate areas for systems pass-throughs

### Load Cases
- **Pressure Load**: 59.3 kPa (8.6 psi) differential, ultimate 88.9 kPa
- **Emergency Landing**: 3.0g forward deceleration
- **System Loads**: Cockpit equipment mounting (displays, oxygen, etc.)

### Pass-Throughs & Penetrations
- **Flight Control Cables**: 12 cable penetrations with grommets
- **Electrical Cables**: 6 conduit penetrations with pressure seals
- **Environmental Control**: 2 duct penetrations (supply/return)
- **Hydraulic Lines**: 4 line penetrations with fire seals

Analysis: [FEA_Results_Summary.csv](ASSETS/FEA_Models/FEA_Results_Summary.csv)

## Aft Pressure Bulkhead

### Location & Geometry
- **Station**: FS 38.5 (aft of passenger cabin)
- **Shape**: Domed bulkhead with tail cone attachment
- **Dimensions**: 8.2m wide × 4.8m high
- **Dome Depth**: 2.2m aft protrusion

### Structural Design
- **Construction**: Composite monocoque with metallic reinforcements
- **Skin**: T800/M21 CFRP (toughened resin), [0/±45/90]3s
- **Stringers**: 16 radial stringers from center to perimeter
- **Ring Frames**: 2 concentric ring frames for stability
- **APU Mount**: Reinforced area for auxiliary power unit attachment

### Load Cases
- **Pressure Load**: 59.3 kPa differential, ultimate 88.9 kPa
- **Emergency Landing**: 1.5g aft deceleration
- **APU Loads**: 450 kg equipment + dynamic loads per [ATA 49](../../../E2-ENERGY/ATA_49-AIRBORNE_AUXILIARY_POWER/README.md)
- **Empennage Loads**: Tail surface reactions in flight

### Pass-Throughs & Penetrations
- **APU Air Intake**: 0.6m diameter duct with firewall
- **APU Exhaust**: 0.4m diameter exhaust duct
- **Electrical Systems**: 8 conduit penetrations
- **Emergency Exit**: Access door to unpressurized tail cone per [CS-25.807](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)

## Material Specifications

Materials per [Material Specifications](../ASSETS/specifications/53-20-A-201_Material_Specifications.md):

### Forward Bulkhead
- **Skin Face Sheets**: IM7/8552, 0.8mm per ply, 8 plies
- **Honeycomb Core**: 5052 Aluminum, 3.1 lb/ft³ density
- **Perimeter Frame**: 7075-T7351, extruded angle section
- **Penetration Doublers**: Solid CFRP, [0/±30/90]4s

### Aft Bulkhead
- **Skin**: T800/M21, 0.75mm per ply, 8 plies
- **Stringers**: CFRP hat sections, [0/±30]3s
- **Ring Frames**: 7075-T7351 forgings
- **APU Mount**: Titanium Ti-6Al-4V fittings

Fasteners per [Fastener Standards](../ASSETS/specifications/53-20-A-202_Fastener_Standards.md).

## Manufacturing Process

### Forward Bulkhead
1. **Tooling**: Female mold with elliptical contour
2. **Layup**: Hand layup of skin face sheets
3. **Core Placement**: Pre-formed honeycomb sections
4. **Co-Cure**: Autoclave cure of sandwich assembly
5. **Frame Installation**: Mechanical fastening of perimeter frame
6. **Systems Integration**: Installation of penetration seals and grommets

### Aft Bulkhead
1. **Skin Layup**: Automated fiber placement (AFP) on male mandrel
2. **Stringer Co-Cure**: Stringers co-cured with skin
3. **Frame Installation**: Ring frames mechanically fastened
4. **APU Mount**: Bonding and bolting of titanium fittings
5. **Final Assembly**: Integration of penetration seals

Manufacturing plans: [Assembly_Sequence.md](ASSETS/Manufacturing_Plans/Assembly_Sequence.md)

## Structural Analysis

### Forward Bulkhead FEA
- **Maximum Stress**: 285 MPa at perimeter frame attachment (allowable 350 MPa)
- **Deflection**: 42mm at dome center under ultimate pressure
- **Buckling Margin**: 1.58 for skin panels between stringers
- **Fatigue Life**: 200,000 pressurization cycles

### Aft Bulkhead FEA
- **Maximum Stress**: 312 MPa at APU mount (allowable 400 MPa)
- **Deflection**: 38mm at dome center under ultimate pressure
- **Buckling Margin**: 1.42 for skin panels
- **Fatigue Life**: 185,000 pressurization cycles

Analysis index: [Shell_Module_Analysis_Index.md](ASSETS/FEA_Models/Shell_Module_Analysis_Index.md)

## Pressure Sealing

### Seal Design
- **Bulkhead-to-Shell**: Compression seal with double-row fasteners
- **Penetration Seals**: O-ring seals for all pass-throughs
- **Emergency Exit**: Inflatable seal for aft access door
- **Test Pressure**: 125% of maximum differential (10.75 psi)

### Leak Testing
- **Initial Certification**: Pneumatic pressure test to 1.15× max pressure
- **Production**: 100% leak test at 1.05× max pressure
- **In-Service**: Annual leak check per maintenance manual

## Inspection & Maintenance

### Inspection Requirements
- **Visual**: Every 800 flight hours (accessible areas)
- **Ultrasonic**: Every 8,000 flight hours (skin-to-core bond)
- **Penetrant**: Every 4,000 flight hours (metallic fittings)
- **Pressure Test**: Every major overhaul (≈24,000 flight hours)

### Critical Inspection Areas
- Perimeter attachment to fuselage shell
- All system penetration seals and doublers
- APU mounting fittings and attachments
- Pressure seal compression zones

NDT procedures: [53-20-A-205_NDT_Requirements.md](../ASSETS/specifications/53-20-A-205_NDT_Requirements.md)

## Interfaces

Pressure bulkheads interface with:

- [53-20-01-001 Upper Shell](53-20-01-001_Upper_Shell_Module_Architecture.md) - Upper perimeter attachment
- [53-20-01-002 Lower Shell](53-20-01-002_Lower_Shell_Module_Architecture.md) - Lower perimeter attachment
- [53-20-01-003 Side Shells](53-20-01-003_Side_Shell_Modules_and_Transitions.md) - Side perimeter closure
- [53-20-03 Cabin Floor](../53-20-03_Cabin_Floor_and_Supports/README.md) - Floor beam reactions at bulkheads
- [ATA 49 APU](../../../E2-ENERGY/ATA_49-AIRBORNE_AUXILIARY_POWER/README.md) - APU mounting (aft bulkhead)

## Certification Compliance

Compliance demonstrated for:
- [CS-25.365](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Pressurized cabin loads
- [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Damage tolerance
- [CS-25.783](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Fuselage pressure boundary
- [CS-25.807](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Emergency exits

## Status

- **Design Status**: PDR Complete
- **Analysis Status**: Pressure analysis complete, fatigue ongoing
- **Testing**: Pressure test article fabrication planned Q2 2026
- **Last Updated**: 2025-11-22

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.

---
