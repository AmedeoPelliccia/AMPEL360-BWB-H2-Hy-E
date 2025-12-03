# 61-00-01-001 ATA 61 Domain Description

## Document Information

- **Document ID**: 61-00-01-001
- **Title**: ATA 61 Domain Description — Propellers/Propulsors
- **Version**: 1.0
- **Date**: 2025-12-03
- **Status**: Draft
- **Category**: Overview / Domain Definition
- **ATA Chapter**: 61 — Propellers/Propulsors

## Purpose

This document defines the scope, boundaries, and key concepts of the **ATA 61 Propellers/Propulsors** domain within the AMPEL360 BWB H2/Hybrid-Electric aircraft program. It establishes the foundational understanding for all subsequent lifecycle phases (Safety, Requirements, Design, etc.) and ensures consistent terminology and domain boundaries across the project.

## Scope

The ATA 61 domain encompasses all propulsor systems that generate thrust for the AMPEL360 Q100 Blended Wing Body (BWB) aircraft, including:

- **Electric Ducted Fans (EDFs)**: Distributed propulsion units
- **Propeller assemblies** (if applicable for variant configurations)
- **Propulsor control systems**: Electronic and software-based thrust management
- **Propulsor integration interfaces**: Connections to power, thermal, and aircraft systems

### In-Scope Components

| Component Category | Description |
|--------------------|-------------|
| Electric Motors | 4 MW-class motors driving each EDF unit |
| Ducted Fans | Rotor/stator assemblies with aerodynamic nacelle |
| Blade Systems | Fan blades, materials, and aerodynamic profiles |
| Propulsor Control Unit (PCU) | Electronic control hardware and embedded software |
| Cooling Loop | Oil/liquid/cryogenic cooling interfaces |
| Health Sensing | Vibration, strain, temperature, and EM sensors |

### Out-of-Scope

The following are addressed in related but separate ATA chapters:

| Related Domain | ATA Chapter | Notes |
|----------------|-------------|-------|
| Power Plant Integration | ATA 71 | Engine/propulsion nacelle integration |
| Engine Core | ATA 72 | Turbine engines (if hybrid configuration) |
| Electrical Power Distribution | ATA 24 | Power supply to propulsors |
| Fuel Systems (H₂) | ATA 28 | Cryogenic hydrogen storage and distribution |
| Engine Controls | ATA 76 | FADEC and higher-level control integration |

## Domain Boundaries

### Interface Boundaries

The ATA 61 domain interfaces with the following systems:

```
┌─────────────────────────────────────────────────────────────────┐
│                     AMPEL360 Q100 Aircraft                      │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                   ATA 61 Domain                          │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │   │
│  │  │ Electric     │  │ Ducted Fan   │  │ PCU          │    │   │
│  │  │ Motor        │←→│ Assembly     │←→│ Controller   │    │   │
│  │  └──────────────┘  └──────────────┘  └──────────────┘    │   │
│  │         ↑                 ↑                 ↑            │   │
│  │         │                 │                 │            │   │
│  └─────────┼─────────────────┼─────────────────┼────────────┘   │
│            │                 │                 │                │
│     ┌──────┴──────┐   ┌──────┴──────┐   ┌──────┴──────┐        │
│     │ ATA 24      │   │ ATA 28      │   │ ATA 76      │        │
│     │ Electrical  │   │ H₂ Fuel     │   │ Engine      │        │
│     │ Power       │   │ System      │   │ Controls    │        │
│     └─────────────┘   └─────────────┘   └─────────────┘        │
└─────────────────────────────────────────────────────────────────┘
```

### Functional Boundaries

| Boundary Type | ATA 61 Responsibility | Adjacent System Responsibility |
|---------------|-----------------------|--------------------------------|
| **Electrical Interface** | Power reception and distribution within propulsor | Power generation and transmission (ATA 24) |
| **Thermal Interface** | Internal motor cooling; thermal rejection to coolant | Coolant supply and heat rejection (ATA 21, 28) |
| **Control Interface** | Local propulsor control and health monitoring | Flight control system integration (ATA 22, 76) |
| **Structural Interface** | Propulsor mounting loads and vibration isolation | Nacelle/pylon structure (ATA 54, 71) |

## Key Concepts

### Distributed Electric Propulsion (DEP)

The AMPEL360 Q100 uses a **Distributed Electric Propulsion** architecture with multiple Electric Ducted Fan (EDF) units. This approach provides:

- **Thrust Vectoring**: Differential thrust for enhanced control
- **Boundary Layer Ingestion (BLI)**: Improved propulsive efficiency
- **Redundancy**: Multiple units ensure continued operation after failures
- **Noise Reduction**: Lower blade tip speeds compared to conventional propellers

### Hydrogen-Electric Integration

The propulsors are powered by an **H₂/Hybrid-Electric** power train:

1. **Hydrogen Fuel Cells** or **H₂ Turbine Generators** produce electrical power
2. **Power Electronics** convert and distribute power to motors
3. **Electric Motors** (ATA 61) drive the fan assemblies
4. **Cryogenic Integration**: Motor cooling may leverage LH₂ cold sink

### Propulsor Hierarchy

```
AMPEL360 Q100 Propulsion System
├── Propulsor Unit #1 (Port)
│   ├── Electric Motor (61-20-01)
│   ├── Ducted Fan (61-20-02)
│   ├── PCU (61-20-04)
│   └── Sensors (61-20-06)
├── Propulsor Unit #2 (Port Inboard)
│   └── [Same structure]
├── Propulsor Unit #3 (Starboard Inboard)
│   └── [Same structure]
└── Propulsor Unit #4 (Starboard)
    └── [Same structure]
```

## Regulatory Framework

The ATA 61 domain must comply with:

- [EASA CS-25 Subpart E — Powerplant](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27): Powerplant installation requirements
- [EASA CS-E](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-e-amendment-6): Engines (for hybrid configurations)
- [EASA CS-P](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-p-amendment-1): Propellers (applicable requirements)
- [FAA 14 CFR Part 25 Subpart E](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25/subpart-E): Powerplant (US certification)
- [FAA 14 CFR Part 33](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-33): Airworthiness Standards: Aircraft Engines

### Special Conditions

Due to the novel hydrogen-electric propulsion architecture, the following special conditions may apply:

- **Electric Propulsion Special Condition** for high-voltage motor systems
- **Hydrogen Fuel Systems Special Condition** for cryogenic interfaces
- **Distributed Propulsion Special Condition** for multi-propulsor redundancy architecture

## References

### Internal References

- [ATA 61 Overview README](README.md)
- [61-00-01-002 Global Architecture](61-00-01-002_Global_Architecture.md)
- [61-00-01-003 Terminology Glossary](61-00-01-003_Terminology_Glossary.md)
- [61-00-01-004 Traceability Matrix](61-00-01-004_Traceability_Matrix.md)
- [61-20 Subsystems](../../61-20_Subsystems/README.md)

### External Standards

- ATA iSpec 2200 Chapter 61
- SAE AS6518 — Digital Product Definition
- ISO 16750 — Road Vehicles Environmental Conditions (applicable test standards)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-03_.

---
