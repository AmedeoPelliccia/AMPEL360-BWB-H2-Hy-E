# 53-20-02 Door Surround Structure

## Purpose

This subsystem defines the structural reinforcement frames surrounding all doors and access openings in the AMPEL360 BWB H₂ Hy-E aircraft fuselage. Door frames provide local reinforcement for pressure loads, structural discontinuities, and door attachment interfaces.

## Scope

Door surround structures include reinforcement frames for:
- Passenger entry doors (L1/R1, L2/R2)
- Cargo doors (forward and aft cargo compartments)
- Emergency exits (L3/R3, overwing exits)
- Service doors (avionics, equipment access)
- All associated reinforcements and doublers

## Key Components

### Door Frame Types
- **Type I Passenger Doors**: Primary entry doors with integral stairs capability
- **Type II Emergency Exits**: Evacuation exits per [CS-25.807](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)
- **Type III Cargo Doors**: Large cargo loading doors
- **Type IV Service Doors**: Equipment and avionics bay access

### Structural Elements
- **Primary Frame**: Main structural ring around door opening
- **Doubler Panels**: Local thickness build-up around frame
- **Stringer Doublers**: Reinforced stringers adjacent to cutout
- **Frame Doublers**: Reinforced frames at door corners

## Requirements

Door surround structures must comply with:
- [CS-25.783](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Doors (pressure boundary)
- [CS-25.807](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Emergency exits
- [CS-25.809](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Emergency exit arrangement
- [CS-25.365](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Pressurized cabin loads

## Related Documents

- [53-20-02-001 Passenger Door Frames](53-20-02-001_Passenger_Door_Frames.md)
- [53-20-02-002 Cargo Door Frames](53-20-02-002_Cargo_Door_Frames.md)
- [53-20-02-003 Emergency Exit Frames](53-20-02-003_Emergency_Exit_Frames.md)
- [53-20-02-004 Service Door Frames](53-20-02-004_Service_Door_Frames.md)
- [53-20-02-005 Door Frame Reinforcements](53-20-02-005_Door_Frame_Reinforcements.md)

## ASSETS

Detailed design artifacts:

- [Frame_Drawings/](ASSETS/Frame_Drawings/) - Door frame layout drawings
- [Load_Analysis/](ASSETS/Load_Analysis/) - Stress analysis and load calculations
- [Installation_Procedures/](ASSETS/Installation_Procedures/) - Frame installation procedures
- [Interface_Specs/](ASSETS/Interface_Specs/) - Interface control documents

## Interfaces

Door surround structures interface with:
- **ATA 52**: Door assemblies and mechanisms per [ATA 52 Doors](../../ATA_52-DOORS/README.md)
- **53-20-01**: Pressure shell modules at cutout perimeters
- **53-20-03**: Cabin floor beams at door threshold
- **53-20-05**: Cabin liner attachment at door reveals

## Safety Considerations

Critical safety aspects:
- Fail-safe design with multiple load paths
- Crack stoppers at frame corners
- Adequate stiffness to prevent door binding
- Maintenance accessibility for inspection

## Status

- **Status**: Active Development
- **Design Phase**: Preliminary Design Review (PDR) Complete
- **Next Milestone**: Frame testing and validation
- **Last Updated**: 2025-11-22

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.

---
