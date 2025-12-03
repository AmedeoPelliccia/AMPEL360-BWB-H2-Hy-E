# 61-00-01-002 Global Architecture

## Document Information

- **Document ID**: 61-00-01-002
- **Title**: ATA 61 Global Architecture — Electric Ducted Fan Propulsors
- **Version**: 1.0
- **Date**: 2025-12-03
- **Status**: Draft
- **Category**: Overview / Architecture
- **ATA Chapter**: 61 — Propellers/Propulsors

## Purpose

This document describes the high-level architecture of the **ATA 61 Propellers/Propulsors** system for the AMPEL360 Q100 Blended Wing Body (BWB) hydrogen-electric aircraft. It provides an architectural overview of the Electric Ducted Fan (EDF) propulsion system, its major components, and integration with the aircraft's hydrogen-electric power train.

## System Overview

The AMPEL360 Q100 uses a **Distributed Electric Propulsion (DEP)** architecture featuring four Electric Ducted Fan (EDF) units arranged along the trailing edge of the BWB airframe. This configuration leverages:

- **Boundary Layer Ingestion (BLI)**: EDFs ingest the aircraft's boundary layer, improving propulsive efficiency
- **Thrust Vectoring Capability**: Differential thrust enables enhanced yaw control
- **Redundancy**: Multi-propulsor configuration ensures continued operation after failures
- **Acoustic Benefits**: Lower tip speeds and distributed thrust reduce noise signatures

### Propulsor Configuration

```
                    AMPEL360 Q100 BWB — Rear View
    ┌─────────────────────────────────────────────────────────────┐
    │                      BWB Trailing Edge                       │
    │                                                              │
    │       ┌─────┐       ┌─────┐   ┌─────┐       ┌─────┐         │
    │       │EDF 1│       │EDF 2│   │EDF 3│       │EDF 4│         │
    │       │ P-OB│       │ P-IB│   │ S-IB│       │ S-OB│         │
    │       └──┬──┘       └──┬──┘   └──┬──┘       └──┬──┘         │
    │          │             │         │             │            │
    │       Port          Port     Starboard     Starboard        │
    │       Outboard      Inboard   Inboard      Outboard         │
    └─────────────────────────────────────────────────────────────┘
```

| Propulsor | Position | Designation | Function |
|-----------|----------|-------------|----------|
| EDF 1 | Port Outboard | P-OB | Primary thrust, yaw control |
| EDF 2 | Port Inboard | P-IB | Primary thrust, BLI |
| EDF 3 | Starboard Inboard | S-IB | Primary thrust, BLI |
| EDF 4 | Starboard Outboard | S-OB | Primary thrust, yaw control |

## Architecture Layers

### Layer 1: Propulsor Unit

Each EDF propulsor unit is a self-contained module containing:

```
┌─────────────────────────────────────────────────────────────────┐
│                     EDF Propulsor Unit                          │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 Aerodynamic Nacelle                      │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │    │
│  │  │   Inlet     │→ │   Fan       │→ │   Nozzle    │      │    │
│  │  │             │  │   Rotor     │  │             │      │    │
│  │  └─────────────┘  └──────┬──────┘  └─────────────┘      │    │
│  │                         │                               │    │
│  │                  ┌──────┴──────┐                        │    │
│  │                  │   Stator    │                        │    │
│  │                  │   Vanes     │                        │    │
│  │                  └─────────────┘                        │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                Electric Motor Assembly                   │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │    │
│  │  │   Stator    │  │   Rotor     │  │   Bearings  │      │    │
│  │  │   Windings  │  │   Magnets   │  │   Housing   │      │    │
│  │  └──────┬──────┘  └──────┬──────┘  └─────────────┘      │    │
│  │         └────────────────┼───────────────────────────────│    │
│  │                          ↓                               │    │
│  │                  ┌─────────────┐                         │    │
│  │                  │   Shaft     │                         │    │
│  │                  │   Assembly  │                         │    │
│  │                  └─────────────┘                         │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │               Propulsor Control Unit (PCU)               │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │    │
│  │  │ Inverter/   │  │ Controller  │  │ Health      │      │    │
│  │  │ Power Elec. │  │ Logic       │  │ Monitoring  │      │    │
│  │  └─────────────┘  └─────────────┘  └─────────────┘      │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    Support Systems                        │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │    │
│  │  │ Cooling     │  │ Sensors     │  │ Wiring      │      │    │
│  │  │ Loop        │  │ Suite       │  │ Harness     │      │    │
│  │  └─────────────┘  └─────────────┘  └─────────────┘      │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

### Layer 2: Subsystem Architecture

Detailed subsystem breakdown per [61-20 Subsystems](../../61-20_Subsystems/README.md):

| Subsystem | ID | Key Parameters |
|-----------|-----|----------------|
| [Electric Motor](../../61-20_Subsystems/61-20-01_Electric_Motor/) | 61-20-01 | 4 MW, >96% efficiency |
| [Ducted Fan](../../61-20_Subsystems/61-20-02_Ducted_Fan/) | 61-20-02 | Variable pitch, BLI-optimized |
| [Blade System](../../61-20_Subsystems/61-20-03_Blade_System/) | 61-20-03 | Composite blades, acoustic treatment |
| [Propulsor Control Unit](../../61-20_Subsystems/61-20-04_Propulsor_Control_Unit/) | 61-20-04 | Dual-redundant, DO-178C DAL A |
| [Cooling Loop](../../61-20_Subsystems/61-20-05_Cooling_Loop/) | 61-20-05 | Cryo-assisted cooling option |
| [Health Sensing](../../61-20_Subsystems/61-20-06_Health_Sensing/) | 61-20-06 | Vibration, thermal, EM monitoring |

### Layer 3: Aircraft Integration

Integration with hydrogen-electric power train and aircraft systems:

```
┌─────────────────────────────────────────────────────────────────┐
│               AMPEL360 Q100 Power Architecture                  │
│                                                                  │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────────────┐    │
│  │ LH₂ Storage │→→→│ H₂ Fuel     │→→→│ Power Generation     │    │
│  │ (ATA 28)    │   │ Distribution│   │ ┌─────────────────┐ │    │
│  └─────────────┘   └─────────────┘   │ │ Fuel Cell Stack │ │    │
│                                       │ │ OR              │ │    │
│                                       │ │ H₂ Turbine Gen  │ │    │
│                                       │ └────────┬────────┘ │    │
│                                       └──────────┼──────────┘    │
│                                                  ↓               │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │             Electrical Power Distribution (ATA 24)       │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │    │
│  │  │ DC Bus      │  │ Converter   │  │ Protection  │      │    │
│  │  │ 800V DC     │  │ Units       │  │ Systems     │      │    │
│  │  └──────┬──────┘  └─────────────┘  └─────────────┘      │    │
│  │         │                                                │    │
│  └─────────┼────────────────────────────────────────────────┘    │
│            │                                                     │
│            ↓                                                     │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              ATA 61 Propulsor Array                      │    │
│  │       ┌─────┐    ┌─────┐  ┌─────┐    ┌─────┐            │    │
│  │       │EDF 1│    │EDF 2│  │EDF 3│    │EDF 4│            │    │
│  │       └─────┘    └─────┘  └─────┘    └─────┘            │    │
│  └─────────────────────────────────────────────────────────┘    │
│                            ↓                                     │
│                      [ THRUST → ]                                │
└─────────────────────────────────────────────────────────────────┘
```

## Interface Architecture

### Electrical Interfaces

| Interface | Type | Voltage/Current | Reference |
|-----------|------|-----------------|-----------|
| Power In | DC | 800 VDC / 5000 A max | ATA 24 ICD |
| Control Bus | AFDX/CAN | Low voltage | ATA 76 ICD |
| Health Data | ARINC 664 | Low voltage | ATA 45 ICD |

### Mechanical Interfaces

| Interface | Type | Load Path | Reference |
|-----------|------|-----------|-----------|
| Nacelle Mount | Bolted flange | Thrust, torque, weight | ATA 54 ICD |
| Cooling Duct | Quick-disconnect | Coolant flow | ATA 21 ICD |
| Service Access | Hinged panels | Maintenance access | ATA 61-10 |

### Thermal Interfaces

| Interface | Heat Load | Cooling Method | Reference |
|-----------|-----------|----------------|-----------|
| Motor Cooling | 160 kW per unit | Liquid cooling loop | 61-20-05 |
| PCU Cooling | 20 kW per unit | Integrated liquid cooling | 61-20-05 |
| Cryo Pre-cooling | TBD | LH₂ cold sink (optional) | ATA 28 ICD |

## Redundancy and Safety Architecture

### Propulsor-Level Redundancy

- **Dual-Winding Motors**: Each motor has two independent stator windings
- **Redundant PCU Channels**: Two independent control lanes per propulsor
- **Cross-Strapping**: Power can be redistributed between propulsors

### System-Level Redundancy

| Failure Mode | Mitigation | Residual Capability |
|--------------|------------|---------------------|
| Single EDF loss | Thrust redistribution | 75% thrust available |
| Two EDF loss (same side) | Asymmetric thrust compensation | Continued flight, reduced performance |
| Two EDF loss (opposite) | Symmetric operation | 50% thrust available |
| Power source loss | Battery backup / H₂ turbine switch | Emergency power |
| Control system loss | Backup control lane activation | Continued operation |

### Safety-Critical Functions

Per [61-00-02 Safety](../61-00-02_Safety/README.md):

| Function | DAL | Notes |
|----------|-----|-------|
| Thrust Control | DAL A | Loss could lead to LOC |
| Overspeed Protection | DAL A | Blade release hazard |
| Thermal Protection | DAL B | Motor damage prevention |
| Health Monitoring | DAL C | Prognostic functions |

## Technology Adaptations for H₂/Hybrid-Electric

### Hydrogen Integration

Traditional propeller/propulsor concepts are adapted for hydrogen-powered architectures:

| Traditional Approach | AMPEL360 Adaptation |
|----------------------|---------------------|
| Jet fuel thermal management | Cryogenic LH₂ cold sink integration |
| Mechanical drive shaft | Direct electric drive |
| Single engine per nacelle | Multiple distributed EDFs |
| Hydraulic pitch control | Electric pitch actuation |
| Conventional oil cooling | Cryo-assisted liquid cooling option |

### BWB Configuration Benefits

The Blended Wing Body configuration enhances propulsor integration:

- **Aft-Mounted EDFs**: Trailing edge location enables BLI
- **Wide Body Integration**: More space for distributed propulsors
- **Structural Efficiency**: Load paths through BWB structure
- **Noise Shielding**: Airframe masks forward-propagating noise

## References

### Internal References

- [61-00-01-001 Domain Description](61-00-01-001_ATA_61_Domain_Description.md)
- [61-00-01-003 Terminology Glossary](61-00-01-003_Terminology_Glossary.md)
- [61-00-01-004 Traceability Matrix](61-00-01-004_Traceability_Matrix.md)
- [61-00-02 Safety](../61-00-02_Safety/README.md)
- [61-00-04 Design](../61-00-04_Design/README.md)
- [61-20 Subsystems](../../61-20_Subsystems/README.md)

### Related ATA Chapters

- [ATA 24 Electrical Power](../../ATA_24-ELECTRICAL_POWER/)
- [ATA 28 Fuel (H₂)](../../ATA_28-FUEL_SAF_CRYOGENIC_H2/)
- [ATA 54 Nacelles/Pylons](../../ATA_54-NACELLES_PYLONS/)
- [ATA 71 Power Plant](../../../P-PROPULSION/ATA_71-POWER_PLANT/)
- [ATA 76 Engine Controls](../../../P-PROPULSION/ATA_76-ENGINE_CONTROLS/)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-03_.

---
