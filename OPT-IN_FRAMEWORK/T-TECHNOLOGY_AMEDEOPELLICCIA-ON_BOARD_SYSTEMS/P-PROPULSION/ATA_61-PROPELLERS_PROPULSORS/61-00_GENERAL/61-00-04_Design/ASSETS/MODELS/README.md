# MODELS — Analytical, Simulation, and Digital Twin Models

**Purpose**: This directory contains physics-based analytical models, simulation models, and digital twin frameworks for the ATA 61 Propellers/Propulsors system supporting the AMPEL360-BWB-H2-Hy-E hybrid electric aircraft (Q100 Program).

---

## Table of Contents

- [Overview](#overview)
- [Domain Categories](#domain-categories)
- [Naming Convention](#naming-convention)
- [Key Models for Hybrid-Electric Integration](#key-models-for-hybrid-electric-integration)
- [Directory Structure](#directory-structure)
- [Model Definition Files](#model-definition-files)
- [Model Library](#model-library)
- [Usage Guidelines](#usage-guidelines)
- [Document Control](#document-control)

---

## Overview

The Q100 hybrid-electric propulsion system integrates:

- **H₂ PEM Fuel Cells** — Primary power source using hydrogen
- **Open-Fan Propulsors** — High-efficiency distributed propulsion
- **CO₂ Battery** — Closed-loop peak-power buffering system
- **Electric Motors** — High power-density permanent magnet motors
- **SAF Compatibility** — Sustainable aviation fuel integration

This MODELS directory provides the analytical foundation for design, verification, and operational monitoring of these systems.

---

## Domain Categories

| Domain | Code | Purpose |
|--------|------|---------|
| **AERODYNAMIC** | AERO | CFD, BEMT, blade/propeller/nacelle aerodynamics |
| **STRUCTURAL** | STR | Static, dynamic, fatigue, and modal analysis |
| **THERMAL** | THM | Heat transfer, cooling system, thermal management |
| **ELECTROMAGNETIC** | EM | Motor electromagnetic performance, losses |
| **SYSTEM_DYNAMICS** | DYN | Control systems, drivetrain dynamics, power electronics |
| **PERFORMANCE** | PERF | System performance maps, mission analysis |
| **DIGITAL_TWIN** | DT | Real-time monitoring, health assessment, calibration |
| **MODEL_LIBRARY** | — | Shared materials, airfoils, and standard conditions |

---

## Naming Convention

All models follow the Q100-61 prefix convention:

```
Q100-61-MDL-[DOMAIN]-[COMPONENT]-[TYPE]
```

### Model Domains

| Code | Domain |
|------|--------|
| `AERO` | Aerodynamic |
| `STR` | Structural |
| `THM` | Thermal |
| `EM` | Electromagnetic |
| `DYN` | System Dynamics |
| `PERF` | Performance |
| `DT` | Digital Twin |

### Library Elements

| Code | Element Type |
|------|--------------|
| `MAT` | Material Property |
| `AFL` | Airfoil Definition |
| `COND` | Standard Conditions |

### Examples

- `Q100-61-MDL-AERO-FAN-BLADE-CFD` — CFD model of fan blade
- `Q100-61-MDL-STR-GEARBOX-HOUSING` — Structural model of gearbox housing
- `Q100-61-MDL-THM-MOTOR` — Thermal model of electric motor
- `Q100-61-MDL-DYN-POWER-SYSTEM` — Power system dynamics model
- `Q100-61-MAT-COMPOSITE-CFRP` — CFRP material properties
- `Q100-61-AFL-FAN-TIP` — Fan blade tip airfoil definition
- `Q100-61-COND-CRUISE-FL350` — Cruise conditions at FL350

---

## Key Models for Hybrid-Electric Integration

The following models are critical for the hybrid-electric propulsion system design:

### Power System Dynamics (Q100-61-MDL-DYN-POWER-SYSTEM)

Simulates the integrated power system including:

- H₂ PEM fuel cell stack dynamics
- CO₂ battery charge/discharge cycles
- Power electronics and DC bus voltage regulation
- Load sharing between fuel cell and battery

### Electric Motor Electromagnetic (Q100-61-MDL-EM-MOTOR-2D/3D)

Predicts motor performance including:

- Torque-speed characteristics
- Efficiency maps across operating envelope
- Electromagnetic losses (copper, iron, magnet)
- Thermal source terms for cooling design

### Motor Thermal Management (Q100-61-MDL-THM-MOTOR)

Models heat generation and removal:

- Winding hot-spot temperature prediction
- Cooling jacket effectiveness
- Transient thermal behavior during takeoff/climb
- Derating limits for sustained operation

### Propulsor Digital Twin (Q100-61-MDL-DT-PROPULSOR)

Real-time health monitoring framework:

- Sensor data fusion algorithms
- Physics-based anomaly detection
- Remaining useful life estimation
- Calibration procedures for model updating

---

## Directory Structure

```
MODELS/
├── README.md                    # This file
│
├── AERODYNAMIC/                 # Aerodynamic analysis models
│   ├── README.md
│   ├── FAN_BLADE/              # Fan blade models
│   ├── PROPELLER/              # Propeller models
│   └── NACELLE/                # Nacelle flow models
│
├── STRUCTURAL/                  # Structural analysis models
│   ├── README.md
│   ├── FAN_BLADE/              # Blade static/dynamic analysis
│   ├── GEARBOX/                # Gearbox structural models
│   ├── MOTOR/                  # Motor rotor/housing structures
│   └── MOUNTING/               # Mount system analysis
│
├── THERMAL/                     # Thermal analysis models
│   ├── README.md
│   ├── MOTOR/                  # Motor thermal management
│   ├── CONTROLLER/             # Power electronics cooling
│   ├── GEARBOX/                # Gearbox oil cooling
│   └── SYSTEM/                 # System-level thermal network
│
├── ELECTROMAGNETIC/             # EM analysis models
│   ├── README.md
│   └── MOTOR/                  # Electric motor EM models
│
├── SYSTEM_DYNAMICS/            # Dynamic system models
│   ├── README.md
│   ├── DRIVETRAIN/             # Torsional dynamics
│   ├── CONTROL/                # Control system models
│   └── POWER_SYSTEM/           # Power generation/storage
│
├── PERFORMANCE/                 # Performance prediction
│   ├── README.md
│   ├── Q100-61-MDL-PERF-PROPULSOR/
│   └── Q100-61-MDL-PERF-MISSION/
│
├── DIGITAL_TWIN/               # Digital twin frameworks
│   ├── README.md
│   ├── Q100-61-MDL-DT-PROPULSOR/
│   └── Q100-61-MDL-DT-MOTOR/
│
└── MODEL_LIBRARY/              # Shared model resources
    ├── README.md
    ├── MATERIALS/              # Material property definitions
    ├── AIRFOILS/               # Airfoil coordinate data
    └── STANDARD_CONDITIONS/    # Operating conditions
```

---

## Model Definition Files

Each model directory contains a `model_definition.yaml` file specifying:

```yaml
model_id: Q100-61-MDL-DOMAIN-COMPONENT-TYPE
model_name: Human-readable model name
version: 1.0.0
status: Draft | Review | Approved

domain: AERO | STR | THM | EM | DYN | PERF | DT
component: FAN_BLADE | PROPELLER | MOTOR | etc.
model_type: CFD | FEA | BEMT | Network | etc.

software:
  name: Software name
  version: Minimum version
  license: License type

geometry:
  source: Reference to CAD/geometry source
  format: STEP | IGES | STL
  revision: Geometry revision

physics:
  equations: Governing equations
  assumptions: Key modeling assumptions
  limitations: Known limitations

operating_conditions:
  reference: Standard conditions reference
  envelope: Operating envelope definition

validation:
  method: Validation approach
  data_source: Test data reference
  metrics: Validation metrics

traceability:
  requirements: [REQ-61-xxx, ...]
  interfaces: [ICD-61-xxx, ...]
  certification: [CS-25.xxx, ...]
```

---

## Model Library

The MODEL_LIBRARY provides shared resources used across multiple models:

### Materials (`MODEL_LIBRARY/MATERIALS/`)

YAML files defining material properties:

- `Q100-61-MAT-COMPOSITE-CFRP.yaml` — Carbon fiber reinforced polymer
- `Q100-61-MAT-TITANIUM-TI6AL4V.yaml` — Titanium alloy Ti-6Al-4V
- `Q100-61-MAT-ALUMINUM-7075.yaml` — Aluminum 7075-T6
- `Q100-61-MAT-STEEL-4340.yaml` — AISI 4340 steel
- `Q100-61-MAT-COPPER-WINDING.yaml` — Copper for motor windings
- `Q100-61-MAT-NDFEB-MAGNET.yaml` — NdFeB permanent magnet
- `Q100-61-MAT-SILICON-STEEL.yaml` — Electrical steel laminations

### Airfoils (`MODEL_LIBRARY/AIRFOILS/`)

Airfoil definitions for blade design:

- `Q100-61-AFL-FAN-ROOT.yaml` — Fan blade root section
- `Q100-61-AFL-FAN-MID.yaml` — Fan blade mid-span section
- `Q100-61-AFL-FAN-TIP.yaml` — Fan blade tip section
- `Q100-61-AFL-PROP-FWD.yaml` — Forward propeller blade
- `Q100-61-AFL-PROP-AFT.yaml` — Aft propeller blade

### Standard Conditions (`MODEL_LIBRARY/STANDARD_CONDITIONS/`)

Operating conditions for analysis:

- `Q100-61-COND-SEA-LEVEL.yaml` — ISA sea level conditions
- `Q100-61-COND-CRUISE-FL350.yaml` — Cruise at FL350
- `Q100-61-COND-HOT-DAY.yaml` — ISA+15°C hot day
- `Q100-61-COND-COLD-DAY.yaml` — ISA-30°C cold day

---

## Usage Guidelines

1. **Creating a New Model**
   - Create model directory following naming convention
   - Copy `model_definition.yaml` template and customize
   - Add necessary subdirectories for mesh, results, etc.
   - Create README.md describing model purpose and usage

2. **Referencing Library Elements**
   - Use relative paths to MODEL_LIBRARY resources
   - Reference by ID in model_definition.yaml

3. **Version Control**
   - Update version in model_definition.yaml for changes
   - Document changes in model README.md
   - Archive superseded versions

4. **Validation**
   - Document validation approach and results
   - Link to test data in 61-00-07_V_AND_V

5. **Traceability**
   - Link to requirements in 61-00-03_Requirements
   - Reference interfaces in 61-00-05_Interfaces
   - Map to certification objectives in 61-00-10_Certification

---

## Related Standards

- [AMPEL360_ASSETS_STANDARD.md](../../../../../../../AMPEL360_ASSETS_STANDARD.md) — Asset naming conventions
- [ARP4754A](https://www.sae.org/standards/content/arp4754a/) — System development process
- [DO-331](https://www.rtca.org/) — Model-Based Development and Verification
- [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) — Equipment, systems, and installations

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-05
