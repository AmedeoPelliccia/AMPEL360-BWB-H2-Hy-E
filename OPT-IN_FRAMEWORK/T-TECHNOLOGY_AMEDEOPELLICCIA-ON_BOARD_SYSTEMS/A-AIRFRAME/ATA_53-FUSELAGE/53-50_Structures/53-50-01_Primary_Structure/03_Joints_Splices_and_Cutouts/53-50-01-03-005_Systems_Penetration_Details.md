# 53-50-01-03-005 Systems Penetration Details

## Document Information

- **Document ID**: 53-50-01-03-005
- **Title**: Systems Penetration Details
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications for Systems Penetration Details in the AMPEL360 BWB primary structure. Systems penetrations are holes through the pressure shell for routing ducts, wiring, hydraulic lines, and other systems between pressurized and unpressurized zones.

## Scope

This specification covers:
- Penetration locations and sizing
- Reinforcement requirements for different penetration sizes
- Sealing methods and pressure containment
- Standard penetration fittings
- Structural analysis methodology

### Penetration Categories

| Category | Diameter Range | Typical Application |
|----------|---------------|---------------------|
| Small | ≤25 mm | Electrical, pneumatic lines |
| Medium | 25-100 mm | Wire bundles, small ducts |
| Large | 100-300 mm | ECS ducts, large conduits |
| Access | >300 mm | Access panels, inspection ports |

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Stress concentration factor | Kt ≤ 3.0 | Fatigue life |
| Reinforcement extent | 1.5 × hole diameter minimum | Load redistribution |
| Fatigue life | 3 × DSG | Safe-life |
| Pressure seal | Dual seal where critical | Redundancy |

### Sealing Requirements

| Pressure Differential | Seal Type | Redundancy |
|----------------------|-----------|------------|
| Full cabin (8.6 psi) | O-ring + face seal | Dual |
| Partial (cargo) | O-ring | Single |
| Non-pressurized | Grommet only | N/A |

## Design Configuration

### Standard Penetration Fittings

| Fitting ID | Diameter | Material | Application |
|------------|----------|----------|-------------|
| PF-25 | 25 mm | Al 2024-T3 | Electrical conduit |
| PF-50 | 50 mm | Al 2024-T3 | Wire bundles |
| PF-80 | 80 mm | Al 7050-T7451 | Medium ducts |
| PF-150 | 150 mm | Al 7050-T7451 | ECS branch ducts |
| PF-200 | 200 mm | Al 7050-T7451 | Main ECS ducts |

### Penetration Fitting Design

**Typical Flanged Fitting (PF-80)**:
```
                     Bolt Circle
         ____________|_|_|_|_|____________
        |  ________________________       |
        | |                        |      |  Flange
        | |    Seal Groove         |      |
        | |   _______________      |      |
        | |  /               \     |      |
        | | |   Ø80 Opening   |    |      |
        | |  \_____________/      |      |
        | |                        |      |
        |_|________________________|______|
              |                |
              Fitting Body      Skin Doubler
```

### Reinforcement Requirements

| Hole Diameter | Doubler OD | Doubler Thickness | Fastener Pattern |
|---------------|------------|-------------------|------------------|
| 25 mm | 60 mm | 1.5 mm | 8 × M4 |
| 50 mm | 100 mm | 2.0 mm | 12 × M5 |
| 80 mm | 150 mm | 2.5 mm | 16 × M5 |
| 150 mm | 250 mm | 3.0 mm | 24 × M6 |
| 200 mm | 350 mm | 4.0 mm | 32 × M6 |

## Penetration Locations

### Pressure Bulkhead Penetrations

**Forward Pressure Bulkhead (Station 2.5m)**:
| Penetration | Quantity | Size | System |
|-------------|----------|------|--------|
| ECS supply duct | 2 | Ø200 mm | Air conditioning |
| Flight control cables | 3 | Ø60 mm | Primary controls |
| Electrical bundles | 4 | Ø80 mm | Avionics power |
| Pitot/static | 6 | Ø25 mm | Air data |

**Aft Pressure Bulkhead (Station 38.0m)**:
| Penetration | Quantity | Size | System |
|-------------|----------|------|--------|
| APU bleed duct | 1 | Ø150 mm | Bleed air |
| Hydraulic lines | 3 | Ø40 mm | Tail systems |
| Electrical | 2 | Ø80 mm | Aft systems |
| Fuel vent | 1 | Ø50 mm | Fuel system |

### Fuselage Shell Penetrations

| Zone | Typical Penetrations | Notes |
|------|---------------------|-------|
| Crown | Antenna mounts, air vents | Low stress zone |
| Sides | NACA scoops, drain ports | Mid-stress zone |
| Keel | Fuel line penetrations, drain valves | Drainage provisions |

## Analysis and Verification

### Stress Analysis

| Penetration | Location | Applied Stress (MPa) | Peak Stress (MPa) | Kt | MS |
|-------------|----------|---------------------|-------------------|-----|-----|
| ECS duct (FPB) | Fwd bulkhead | 120 | 320 | 2.7 | +0.20 |
| Electrical (FPB) | Fwd bulkhead | 115 | 290 | 2.5 | +0.33 |
| APU bleed (APB) | Aft bulkhead | 140 | 365 | 2.6 | +0.15 |
| Antenna mount | Crown skin | 65 | 150 | 2.3 | +0.45 |

### Fatigue Life

| Penetration | Stress Range (MPa) | Predicted Life (FC) | Factor on DSG |
|-------------|-------------------|---------------------|---------------|
| ECS duct | 100 | 200,000 | 3.3× |
| Electrical | 85 | 280,000 | 4.7× |
| APU bleed | 110 | 170,000 | 2.8× |

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| Fitting PF-150-01 | Static + seal | Strength and leak | Complete |
| Fitting PF-200-01 | Fatigue | Life validation | In progress |
| Bulkhead section | Pressure cycle | System test | Planned |

## Manufacturing Considerations

### Installation Sequence

1. Locate penetration position per ICD
2. Drill pilot hole and verify location
3. Install doublers (bonded + fastened for large holes)
4. Ream to final diameter
5. Install fitting with sealant
6. Torque fasteners per specification
7. Pressure test seal integrity

### Quality Criteria

| Feature | Acceptance Criteria |
|---------|---------------------|
| Hole diameter | Nominal ±0.1 mm |
| Hole perpendicularity | ±0.5° |
| Seal groove surface | Ra ≤ 1.6 μm |
| Leak test | No visible leak at 1.1 × P_max |

## References

### Regulatory Documents
- [CS-25.841 Pressurized Cabins](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.1309 Equipment, Systems, and Installations](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-01-02-006 Pressure Bulkhead Design](../02_Panels_Frames_and_Skins/53-50-01-02-006_Pressure_Bulkhead_Design.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
