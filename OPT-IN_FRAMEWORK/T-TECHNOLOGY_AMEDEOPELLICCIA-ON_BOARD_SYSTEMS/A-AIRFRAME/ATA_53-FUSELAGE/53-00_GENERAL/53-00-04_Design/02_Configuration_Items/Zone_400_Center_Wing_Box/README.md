# Zone 400: Center Wing Box – Configuration Items

## Overview

This folder contains all Configuration Items (CIs) for **Zone 400 – Center Wing Box**, the most structurally critical zone of the AMPEL360 BWB fuselage.

**Zone CI**: `CI-53-400`  
**Stations**: 450 to 600  
**Weight Target**: 12,000 kg  
**Material**: CFRP primary structure with titanium fittings  
**Criticality**: CRITICAL

## Description

Zone 400 is the structural heart of the BWB, where:
- Wing spars integrate with the centerbody
- Main landing gear bays are located
- Maximum bending and torsion loads are transferred
- Wing, fuselage, and landing gear loads converge

## Major Subsystems

- **Center Wing Box**: Primary load-carrying structure
- **Wing Spars**: Forward and rear spars, continuous through centerbody
- **Main Landing Gear Bays**: Left and right gear bays with reinforced structure
- **Cargo Bays**: Lower deck cargo compartments
- **Wing-Body Integration**: Structural blend and load transfer

## Key CIs in This Zone

| CI Number | CI Name | Type | Weight (kg) | Structural Role | Status |
|-----------|---------|------|-------------|-----------------|--------|
| CI-53-400 | Center Wing Box | Assembly | 12,000 | Primary | Production |
| CI-53-400-SPAR-FWD | Forward Wing Spar | Spar | 2,200 | Primary | Production |
| CI-53-400-SPAR-REAR | Rear Wing Spar | Spar | 2,000 | Primary | Production |
| CI-53-400-BAY-MLG-L | Left Main Gear Bay | Bay | 850 | Primary | Production |
| CI-53-400-BAY-MLG-R | Right Main Gear Bay | Bay | 850 | Primary | Production |
| CI-53-400-RIB-001 | Wing Rib 001 | Rib | 120 | Primary | Detailed |
| CI-53-400-SKN-U-001 | Upper Skin Panel 001 | Skin | 450 | Primary | Production |
| CI-53-400-SKN-L-001 | Lower Skin Panel 001 | Skin | 420 | Primary | Production |

## Zone Index

Complete list of all CIs in this zone: [53-00-04-02-401_CI-53-400_Zone_Index.csv](53-00-04-02-401_CI-53-400_Zone_Index.csv)

## Critical Design Drivers

1. **Wing Bending Loads**: High bending moments from wing lift distribution
2. **Landing Gear Reactions**: Concentrated loads from main gear during landing
3. **Torsion Loads**: Wing torsion transferred through center box
4. **Pressurization**: Cabin pressure loads in centerbody
5. **Fatigue and Damage Tolerance**: Critical for long service life

## Design Philosophy

- **Multiple Load Paths**: Redundant structure for fail-safe design
- **Efficient Load Transfer**: Direct load paths from wing to fuselage
- **Inspectable Design**: Access for NDI and visual inspection
- **Damage Tolerance**: Design to sustain damage until detection

## Materials

- **Primary Structure**: CFRP (IM7/8552 and T800/3900)
- **Gear Bay Structure**: CFRP with titanium reinforcements
- **Fittings**: Titanium Ti-6Al-4V for high-load attachments
- **Fasteners**: Titanium and steel (300M) for critical joints

## Manufacturing Considerations

- Large composite panels via Automated Fiber Placement (AFP)
- Autoclave curing for primary structure
- Precision machining of titanium fittings
- Complex assembly with tight tolerances

## Analysis and Substantiation

**Design Analysis** (this folder):
- Global FEA model integration
- Load case definitions
- Preliminary stress results

**Certification Analysis** ([../../53-50_Structures/](../../53-50_Structures/)):
- Detailed stress analysis with margins
- Fatigue and damage tolerance analysis
- Test correlation and certification evidence

## Interfaces

### Internal (within ATA 53)
- Zone 300 (Mid Cabin): Wing-body blend transition
- Zone 500 (Aft Cabin): Aft wing attachment

### External (other ATAs)
- **ATA 32** (Landing Gear): Gear bay interfaces, load transfer
- **ATA 57** (Wings): Wing spar attachment, load distribution
- **ATA 71** (Propulsion): Thrust reaction structure

## Subsystem Reference

Primary subsystem: [../../53-20_Subsystems/53-20-04_Centerbody_Landing_Gear_Bays/](../../53-20_Subsystems/)

## CI Folders

Each CI has its own folder with standard structure:

```
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

## Status and Maturity

**Overall Zone Status**: Production (most CIs released)

**Design Maturity**: 85% (as of 2025-11-22)
- 90% of primary structure released
- 75% of secondary structure released
- 60% of fittings and brackets released

## Risk Items

1. **Landing Gear Bay Structure**: Complex load introduction, ongoing analysis
2. **Spar-to-Centerbody Joints**: Critical interface, requires full-scale testing
3. **Manufacturing Tolerances**: Tight tolerances for wing alignment

## Related Documentation

- **Design Philosophy**: [../../01_Design_Overview/53-00-04-01-001_Design_Philosophy.md](../../01_Design_Overview/53-00-04-01-001_Design_Philosophy.md)
- **BWB Design Drivers**: [../../01_Design_Overview/53-00-04-01-002_BWB_Design_Drivers.md](../../01_Design_Overview/53-00-04-01-002_BWB_Design_Drivers.md)
- **Requirements**: [../../../53-00-03_Requirements/](../../../53-00-03_Requirements/)
- **Structures**: [../../../53-50_Structures/](../../../53-50_Structures/)

---

## Document Control

- **Folder**: `Zone_400_Center_Wing_Box`
- **Zone CI**: CI-53-400
- **Version**: 1.0
- **Date**: 2025-11-22
- **Owner**: Zone 400 Lead Design Engineer
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.
