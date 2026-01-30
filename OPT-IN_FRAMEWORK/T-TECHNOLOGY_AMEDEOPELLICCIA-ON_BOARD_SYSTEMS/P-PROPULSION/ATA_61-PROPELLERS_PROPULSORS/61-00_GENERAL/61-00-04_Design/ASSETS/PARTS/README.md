# PARTS — ATA 61 Propellers/Propulsors

## Overview

This directory contains **individual component definitions** (source parts) for the AMPEL360 BWB H2 Hy-E hybrid electric propulsion system (Q100 program). These parts serve as the building blocks referenced by:

- **ASSEMBLIES** — CAD assembly products
- **DRAWINGS** — Engineering drawings
- **EXPORTS** — Released output files
- **MODELS** — Analysis and simulation models

## Project Context

The AMPEL360-BWB-H2-Hy-E is a hybrid Blended Wing Body aircraft featuring:

- **H₂ PEM Fuel Cells** — Primary power source
- **Open-Fan Propulsors** — High bypass ratio for efficiency
- **Closed-Loop CO₂ Battery** — Peak-power buffering system
- **SAF Compatibility** — Sustainable Aviation Fuel ready

## Directory Structure

```
PARTS/
├── README.md                     # This file
│
├── FAN_COMPONENTS/              # Fan blades, hub, spinner, etc.
├── NACELLE_COMPONENTS/          # Nacelle barrels, inlet, liners
├── GEARBOX_COMPONENTS/          # Gears, carrier, housing, bearings
├── MOTOR_COMPONENTS/            # Stator, rotor, housing, shaft
├── CONTROLLER_COMPONENTS/       # Enclosure, heatsink, power modules
├── PROPELLER_COMPONENTS/        # Blades, pitch mechanisms
├── MOUNTING_COMPONENTS/         # Mounts, links, dampers
│
├── STANDARD_PARTS/              # Fasteners, bearings, seals, connectors
│   ├── FASTENERS/
│   ├── BEARINGS/
│   ├── SEALS/
│   └── CONNECTORS/
│
└── PART_LIBRARY/                # Master index and specifications
    ├── Q100-61-PRT-MASTER-INDEX.yaml
    ├── MATERIALS/
    └── SPECIFICATIONS/
```

## Naming Convention

All parts follow the Q100-61 prefix scheme:

```
Q100-61-PRT-[SYSTEM]-[COMPONENT]
```

### Part Systems

| Code    | Description          | Directory              |
|---------|----------------------|------------------------|
| FAN     | Fan components       | FAN_COMPONENTS/        |
| NACELLE | Nacelle components   | NACELLE_COMPONENTS/    |
| GEARBOX | Gearbox components   | GEARBOX_COMPONENTS/    |
| MOTOR   | Motor components     | MOTOR_COMPONENTS/      |
| CTRL    | Controller components| CONTROLLER_COMPONENTS/ |
| PROP    | Propeller components | PROPELLER_COMPONENTS/  |
| MNT     | Mounting components  | MOUNTING_COMPONENTS/   |
| STD     | Standard parts       | STANDARD_PARTS/        |

### Examples

- `Q100-61-PRT-FAN-BLADE` — Fan blade part
- `Q100-61-PRT-MOTOR-STATOR-CORE` — Motor stator core
- `Q100-61-PRT-GEARBOX-SUN-GEAR` — Gearbox sun gear
- `Q100-61-STD-FASTENER-INDEX` — Standard fasteners index

## Part Directory Structure

Each part directory contains:

```
Q100-61-PRT-[SYSTEM]-[COMPONENT]/
├── README.md                # Part description and specifications
├── part_definition.yaml     # Part metadata and properties
├── CAD/
│   ├── NATIVE/             # Native CAD files
│   │   ├── CATIA/
│   │   ├── SOLIDWORKS/
│   │   └── NX/
│   └── NEUTRAL/            # Exchange formats (.step, .jt)
├── SPECIFICATIONS/         # Technical specifications
└── VALIDATION/             # Test and validation data
```

## Part Definition Schema

Each `part_definition.yaml` includes:

```yaml
# Part Identification
part_id: "Q100-61-PRT-XXX-YYY"
name: "Part Name"
revision: "A"
status: "Draft|Released|Obsolete"

# Physical Properties
physical:
  mass_kg: 0.0
  center_of_gravity:
    x_mm: 0.0
    y_mm: 0.0
    z_mm: 0.0
  material: "Material Specification"

# Geometry Summary
geometry:
  type: "Solid|Sheet|Assembly"
  bounding_box:
    length_mm: 0.0
    width_mm: 0.0
    height_mm: 0.0

# CAD References
cad_files:
  native:
    catia: "path/to/file.CATPart"
    solidworks: "path/to/file.sldprt"
    nx: "path/to/file.prt"
  neutral:
    step: "path/to/file.step"
    jt: "path/to/file.jt"

# Manufacturing
manufacturing:
  process: "Machined|Cast|Forged|Composite|Additive"
  supplier: "TBD"
  lead_time_weeks: 0

# Quality Requirements
quality:
  inspection_level: "Level I|II|III"
  critical_dimensions: []
  certifications: []

# Assembly References
assemblies:
  - "Q100-61-ASSY-XXX"
```

## Component Categories

| Category              | Parts | Key Components                                        |
|-----------------------|-------|-------------------------------------------------------|
| FAN_COMPONENTS        | 5     | Blade, hub, spinner, retention, pitch mechanism      |
| NACELLE_COMPONENTS    | 5     | Outer/inner barrel, inlet lip, acoustic liner, thrust reverser |
| GEARBOX_COMPONENTS    | 6     | Sun/planet/ring gears, carrier, housing, bearings    |
| MOTOR_COMPONENTS      | 9     | Stator core/winding, rotor core/magnet, housing, end bells, shaft, cooling jacket |
| CONTROLLER_COMPONENTS | 4     | Enclosure, heatsink, power module, busbar            |
| PROPELLER_COMPONENTS  | 6     | Blades (fwd/aft), pitch actuator/link, beta tube, blade bearing |
| MOUNTING_COMPONENTS   | 5     | Fwd/aft mounts, thrust/side links, vibration damper  |

**Total Custom Parts: 40**

## CAD File Naming

CAD files follow the pattern:

```
[PART_ID].[extension]
```

### Examples

| CAD System   | Extension   | Example                              |
|--------------|-------------|--------------------------------------|
| CATIA V5/V6  | .CATPart    | Q100-61-PRT-FAN-BLADE.CATPart       |
| SOLIDWORKS   | .sldprt     | Q100-61-PRT-MOTOR-SHAFT.sldprt      |
| Siemens NX   | .prt        | Q100-61-PRT-GEARBOX-HOUSING.prt     |
| STEP         | .step/.stp  | Q100-61-PRT-NACELLE-INLET-LIP.step  |
| JT           | .jt         | Q100-61-PRT-CTRL-ENCLOSURE.jt       |

## Traceability

All parts must trace to:

- **Requirements**: In `../../../61-00-03_Requirements/`
- **Verification**: In `../../../61-00-07_V_AND_V/`
- **Interfaces**: In `../../../61-00-05_Interfaces/`
- **Assemblies**: In `../ASSEMBLIES/`
- **Drawings**: In `../DRAWINGS/`

## Related Documentation

- [AMPEL360 Assets Standard](../../../../../../../AMPEL360_ASSETS_STANDARD.md)
- [ATA 61 README](../../../../README.md)
- [61-00-04 Design README](../../README.md)
- [Assemblies Directory](../ASSEMBLIES/README.md)
- [Drawings Directory](../DRAWINGS/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
