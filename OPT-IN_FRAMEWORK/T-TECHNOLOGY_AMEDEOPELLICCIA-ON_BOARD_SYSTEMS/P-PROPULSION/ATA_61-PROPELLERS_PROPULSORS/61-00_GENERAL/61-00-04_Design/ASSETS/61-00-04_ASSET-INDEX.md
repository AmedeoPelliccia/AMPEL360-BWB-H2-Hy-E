# 61-00-04 Design Assets Index

> **ATA Chapter**: 61 - Propellers/Propulsors  
> **Section**: 61-00 General  
> **Subsection**: 61-00-04 Design  
> **Program**: Q100 AMPEL360-BWB-H2-Hy-E  
> **Last Updated**: 2025-12-05

---

## Table of Contents

1. [Overview](#overview)
2. [Power Architecture](#power-architecture)
3. [ASSETS Directory Map](#assets-directory-map)
4.  [Directory Index](#directory-index)
   - [ASSEMBLIES](#1-assemblies)
   - [DRAWINGS](#2-drawings)
   - [EXPORTS](#3-exports)
   - [INSTALLATIONS](#4-installations)
   - [MODELS](#5-models)
   - [PARTS](#6-parts)
   - [PRODUCTS](#7-products)
   - [TEMPLATES](#8-templates)
5. [Naming Convention](#naming-convention)
6. [Quick Navigation](#quick-navigation)
7. [Cross-References](#cross-references)
8.  [Revision History](#revision-history)

---

## Overview

This directory contains all design assets for **ATA 61 - Propellers/Propulsors** supporting the Q100 Hybrid-Electric Propulsion System. 

| Property | Value |
|----------|-------|
| **Program** | AMPEL360-BWB-H2-Hy-E |
| **Aircraft Type** | Blended Wing Body (BWB) |
| **Propulsion** | Hybrid-Electric (H₂ PEM + CO₂ Battery) |
| **Motor Power** | 2. 5 MW |
| **Voltage** | 800 VDC |

[↑ Back to Top](#61-00-04-design-assets-index)

---

## Power Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Q100 HYBRID-ELECTRIC SYSTEM                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌──────────────┐      ┌──────────────┐      ┌──────────────┐  │
│   │  H₂ PEM      │      │   CO₂        │      │   800 VDC    │  │
│   │  FUEL CELL   │─────▶│   BATTERY    │─────▶│   BUS        │  │
│   │  (Primary)   │      │   (Buffer)   │      │              │  │
│   └──────────────┘      └──────────────┘      └──────┬───────┘  │
│                                                       │          │
│                                                       ▼          │
│   ┌──────────────┐      ┌──────────────┐      ┌──────────────┐  │
│   │  OPEN FAN    │◀─────│  REDUCTION   │◀─────│  ELECTRIC    │  │
│   │  PROPULSOR   │      │  GEARBOX     │      │  MOTOR       │  │
│   │              │      │              │      │  (2.5 MW)    │  │
│   └──────────────┘      └──────────────┘      └──────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

[↑ Back to Top](#61-00-04-design-assets-index)

---

## ASSETS Directory Map

```
61-00-04_Design/
├── 00-04_index.md                    ← YOU ARE HERE
│
└── ASSETS/
    ├── ASSEMBLIES/                   → CAD assembly products
    │   ├── OPEN_FAN_PROPULSOR/
    │   ├── ELECTRIC_MOTOR_DRIVE/
    │   ├── PROPELLER_VARIANTS/
    │   ├── MOUNTING_ASSEMBLY/
    │   └── FULL_PROPULSOR_SYSTEM/
    │
    ├── DRAWINGS/                     → Engineering drawing sets
    │   ├── DRAWING_SETS/
    │   ├── DRAWING_STANDARDS/
    │   ├── TEMPLATES/
    │   ├── SYMBOL_LIBRARIES/
    │   └── DRAWING_TYPES/
    │
    ├── EXPORTS/                      → Released output formats
    │   ├── NEUTRAL_FORMATS/
    │   ├── VISUALIZATION/
    │   ├── MANUFACTURING/
    │   ├── ANALYSIS/
    │   ├── DOCUMENTATION/
    │   ├── SUPPLIER_PACKAGES/
    │   └── RELEASE_HISTORY/
    │
    ├── INSTALLATIONS/                → Installation & routing
    │   ├── INSTALLATION_DEFINITIONS/
    │   ├── INSTALLATION_PROCEDURES/
    │   ├── ROUTING/
    │   ├── CLEARANCES/
    │   ├── ACCESS_PANELS/
    │   ├── SPECIAL_TOOLING/
    │   └── INSTALLATION_STANDARDS/
    │
    ├── MODELS/                       → Analysis & simulation
    │   ├── AERODYNAMIC/
    │   ├── STRUCTURAL/
    │   ├── THERMAL/
    │   ├── ELECTROMAGNETIC/
    │   ├── SYSTEM_DYNAMICS/
    │   ├── PERFORMANCE/
    │   ├── DIGITAL_TWIN/
    │   └── MODEL_LIBRARY/
    │
    ├── PARTS/                        → Component definitions
    │   ├── FAN_COMPONENTS/
    │   ├── NACELLE_COMPONENTS/
    │   ├── GEARBOX_COMPONENTS/
    │   ├── MOTOR_COMPONENTS/
    │   ├── CONTROLLER_COMPONENTS/
    │   ├── PROPELLER_COMPONENTS/
    │   ├── MOUNTING_COMPONENTS/
    │   ├── STANDARD_PARTS/
    │   └── PART_LIBRARY/
    │
    ├── PRODUCTS/                     → Configured products
    │   ├── PRODUCT_DEFINITIONS/
    │   ├── PRODUCT_VARIANTS/
    │   ├── PRODUCT_CONFIGURATIONS/
    │   ├── BILL_OF_MATERIALS/
    │   ├── PRODUCT_SPECIFICATIONS/
    │   ├── CERTIFICATION/
    │   ├── PRODUCT_LIFECYCLE/
    │   └── PRODUCT_STANDARDS/
    │
    └── TEMPLATES/                    → Standardized templates
        ├── CAD_TEMPLATES/
        ├── DRAWING_TEMPLATES/
        ├── DOCUMENT_TEMPLATES/
        ├── DATA_TEMPLATES/
        ├── ANALYSIS_TEMPLATES/
        ├── PROJECT_TEMPLATES/
        ├── CERTIFICATION_TEMPLATES/
        └── TEMPLATE_STANDARDS/
```

[↑ Back to Top](#61-00-04-design-assets-index)

---

## Directory Index

### 1. ASSEMBLIES

> **Path**: [`ASSETS/ASSEMBLIES/`](ASSETS/ASSEMBLIES/)  
> **Purpose**: CAD assembly products and product structures  
> **Naming**: `Q100-61-ASSY-[SYSTEM]-[SUBSYSTEM]`

| Subdirectory | Description | Link |
|--------------|-------------|------|
| Open Fan Propulsor | Fan, nacelle, gearbox integration | [`OPEN_FAN_PROPULSOR/`](ASSETS/ASSEMBLIES/OPEN_FAN_PROPULSOR/) |
| Electric Motor Drive | Stator, rotor, housing assembly | [`ELECTRIC_MOTOR_DRIVE/`](ASSETS/ASSEMBLIES/ELECTRIC_MOTOR_DRIVE/) |
| Propeller Variants | Constant-speed, variable-pitch | [`PROPELLER_VARIANTS/`](ASSETS/ASSEMBLIES/PROPELLER_VARIANTS/) |
| Mounting Assembly | Pylon interface, vibration isolation | [`MOUNTING_ASSEMBLY/`](ASSETS/ASSEMBLIES/MOUNTING_ASSEMBLY/) |
| Full Propulsor System | Complete top-level assembly | [`FULL_PROPULSOR_SYSTEM/`](ASSETS/ASSEMBLIES/FULL_PROPULSOR_SYSTEM/) |

**Key Assemblies**:
- [`Q100-61-ASSY-FPS-TOP`](ASSETS/ASSEMBLIES/FULL_PROPULSOR_SYSTEM/) - Full Propulsor System
- [`Q100-61-ASSY-OFP-FAN`](ASSETS/ASSEMBLIES/OPEN_FAN_PROPULSOR/FAN_ASSEMBLY/) - Open Fan Assembly
- [`Q100-61-ASSY-EMD-MOTOR`](ASSETS/ASSEMBLIES/ELECTRIC_MOTOR_DRIVE/MOTOR_ASSEMBLY/) - Electric Motor Assembly

[↑ Back to Top](#61-00-04-design-assets-index) | [↑ Directory Index](#directory-index)

---

### 2.  DRAWINGS

> **Path**: [`ASSETS/DRAWINGS/`](ASSETS/DRAWINGS/)  
> **Purpose**: Engineering drawing sets, standards, templates  
> **Naming**: `Q100-61-DRW-[SYSTEM]-[COMPONENT]`

| Subdirectory | Description | Link |
|--------------|-------------|------|
| Drawing Sets | Organized packages by system | [`DRAWING_SETS/`](ASSETS/DRAWINGS/DRAWING_SETS/) |
| Drawing Standards | Requirements and conventions | [`DRAWING_STANDARDS/`](ASSETS/DRAWINGS/DRAWING_STANDARDS/) |
| Templates | Sheet formats (A0-A4) | [`TEMPLATES/`](ASSETS/DRAWINGS/TEMPLATES/) |
| Symbol Libraries | GD&T, weld, electrical symbols | [`SYMBOL_LIBRARIES/`](ASSETS/DRAWINGS/SYMBOL_LIBRARIES/) |
| Drawing Types | Part, assembly, schematic, ICD | [`DRAWING_TYPES/`](ASSETS/DRAWINGS/DRAWING_TYPES/) |

**Drawing Sets by System**:
- [`OPEN_FAN_PROPULSOR/`](ASSETS/DRAWINGS/DRAWING_SETS/OPEN_FAN_PROPULSOR/) - Fan drawings
- [`ELECTRIC_MOTOR_DRIVE/`](ASSETS/DRAWINGS/DRAWING_SETS/ELECTRIC_MOTOR_DRIVE/) - Motor drawings
- [`GEARBOX/`](ASSETS/DRAWINGS/DRAWING_SETS/GEARBOX/) - Gearbox drawings
- [`NACELLE/`](ASSETS/DRAWINGS/DRAWING_SETS/NACELLE/) - Nacelle drawings
- [`MOUNTING/`](ASSETS/DRAWINGS/DRAWING_SETS/MOUNTING/) - Mounting drawings
- [`FULL_PROPULSOR_SYSTEM/`](ASSETS/DRAWINGS/DRAWING_SETS/FULL_PROPULSOR_SYSTEM/) - System drawings

[↑ Back to Top](#61-00-04-design-assets-index) | [↑ Directory Index](#directory-index)

---

### 3. EXPORTS

> **Path**: [`ASSETS/EXPORTS/`](ASSETS/EXPORTS/)  
> **Purpose**: Released/published outputs for distribution  
> **Naming**: `Q100-61-EXP-[TYPE]-[SYSTEM]`

| Subdirectory | Formats | Link |
|--------------|---------|------|
| Neutral Formats | STEP, JT, IGES, Parasolid | [`NEUTRAL_FORMATS/`](ASSETS/EXPORTS/NEUTRAL_FORMATS/) |
| Visualization | 3DPDF, glTF, STL, OBJ | [`VISUALIZATION/`](ASSETS/EXPORTS/VISUALIZATION/) |
| Manufacturing | CNC, 3D Print, Sheet Metal | [`MANUFACTURING/`](ASSETS/EXPORTS/MANUFACTURING/) |
| Analysis | FEA mesh, CFD geometry | [`ANALYSIS/`](ASSETS/EXPORTS/ANALYSIS/) |
| Documentation | Drawing packages, data sheets | [`DOCUMENTATION/`](ASSETS/EXPORTS/DOCUMENTATION/) |
| Supplier Packages | Vendor data bundles | [`SUPPLIER_PACKAGES/`](ASSETS/EXPORTS/SUPPLIER_PACKAGES/) |
| Release History | Version tracking | [`RELEASE_HISTORY/`](ASSETS/EXPORTS/RELEASE_HISTORY/) |

**Export Formats**:
| Format | Path | Purpose |
|--------|------|---------|
| STEP | [`NEUTRAL_FORMATS/STEP/`](ASSETS/EXPORTS/NEUTRAL_FORMATS/STEP/) | CAD exchange (AP242) |
| JT | [`NEUTRAL_FORMATS/JT/`](ASSETS/EXPORTS/NEUTRAL_FORMATS/JT/) | Lightweight viz + PMI |
| glTF | [`VISUALIZATION/GLTF/`](ASSETS/EXPORTS/VISUALIZATION/GLTF/) | Web 3D viewing |
| STL | [`VISUALIZATION/STL/`](ASSETS/EXPORTS/VISUALIZATION/STL/) | 3D printing, CFD |

[↑ Back to Top](#61-00-04-design-assets-index) | [↑ Directory Index](#directory-index)

---

### 4.  INSTALLATIONS

> **Path**: [`ASSETS/INSTALLATIONS/`](ASSETS/INSTALLATIONS/)  
> **Purpose**: Installation definitions, procedures, routing  
> **Naming**: `Q100-61-INST-[TYPE]-[SYSTEM]`

| Subdirectory | Description | Link |
|--------------|-------------|------|
| Installation Definitions | Interface and mounting specs | [`INSTALLATION_DEFINITIONS/`](ASSETS/INSTALLATIONS/INSTALLATION_DEFINITIONS/) |
| Installation Procedures | Step-by-step procedures | [`INSTALLATION_PROCEDURES/`](ASSETS/INSTALLATIONS/INSTALLATION_PROCEDURES/) |
| Routing | Electrical, fluid, data paths | [`ROUTING/`](ASSETS/INSTALLATIONS/ROUTING/) |
| Clearances | Envelope definitions | [`CLEARANCES/`](ASSETS/INSTALLATIONS/CLEARANCES/) |
| Access Panels | Maintenance access locations | [`ACCESS_PANELS/`](ASSETS/INSTALLATIONS/ACCESS_PANELS/) |
| Special Tooling | Installation tools | [`SPECIAL_TOOLING/`](ASSETS/INSTALLATIONS/SPECIAL_TOOLING/) |
| Installation Standards | Torque, fastener specs | [`INSTALLATION_STANDARDS/`](ASSETS/INSTALLATIONS/INSTALLATION_STANDARDS/) |

**Key Routing (Hybrid-Electric)**:
| Route | Description | Link |
|-------|-------------|------|
| H₂ Fuel Cell Link | Primary power connection | [`ROUTING/ELECTRICAL/Q100-61-RTE-ELEC-H2-FC-LINK`](ASSETS/INSTALLATIONS/ROUTING/ELECTRICAL/) |
| CO₂ Battery Link | Buffer power connection | [`ROUTING/ELECTRICAL/Q100-61-RTE-ELEC-CO2-BATT-LINK`](ASSETS/INSTALLATIONS/ROUTING/ELECTRICAL/) |
| Cooling Supply | Motor/controller cooling | [`ROUTING/FLUID/Q100-61-RTE-FLD-COOLING-SUPPLY`](ASSETS/INSTALLATIONS/ROUTING/FLUID/) |
| FADEC Bus | Control data bus | [`ROUTING/DATA/Q100-61-RTE-DATA-FADEC-BUS`](ASSETS/INSTALLATIONS/ROUTING/DATA/) |

[↑ Back to Top](#61-00-04-design-assets-index) | [↑ Directory Index](#directory-index)

---

### 5.  MODELS

> **Path**: [`ASSETS/MODELS/`](ASSETS/MODELS/)  
> **Purpose**: Analytical, simulation, and digital twin models  
> **Naming**: `Q100-61-MDL-[DOMAIN]-[COMPONENT]`

| Subdirectory | Domain | Link |
|--------------|--------|------|
| Aerodynamic | CFD, BEMT | [`AERODYNAMIC/`](ASSETS/MODELS/AERODYNAMIC/) |
| Structural | FEA static/dynamic | [`STRUCTURAL/`](ASSETS/MODELS/STRUCTURAL/) |
| Thermal | Heat transfer | [`THERMAL/`](ASSETS/MODELS/THERMAL/) |
| Electromagnetic | Motor EM analysis | [`ELECTROMAGNETIC/`](ASSETS/MODELS/ELECTROMAGNETIC/) |
| System Dynamics | Drivetrain, control | [`SYSTEM_DYNAMICS/`](ASSETS/MODELS/SYSTEM_DYNAMICS/) |
| Performance | Propulsor, mission | [`PERFORMANCE/`](ASSETS/MODELS/PERFORMANCE/) |
| Digital Twin | Real-time monitoring | [`DIGITAL_TWIN/`](ASSETS/MODELS/DIGITAL_TWIN/) |
| Model Library | Materials, airfoils | [`MODEL_LIBRARY/`](ASSETS/MODELS/MODEL_LIBRARY/) |

**Key Models (Hybrid-Electric)**:
| Model | Description | Link |
|-------|-------------|------|
| Power System | H₂ PEM + CO₂ battery dynamics | [`SYSTEM_DYNAMICS/POWER_SYSTEM/`](ASSETS/MODELS/SYSTEM_DYNAMICS/POWER_SYSTEM/) |
| Motor EM | Electric motor electromagnetic | [`ELECTROMAGNETIC/MOTOR/`](ASSETS/MODELS/ELECTROMAGNETIC/MOTOR/) |
| Propulsor Digital Twin | Real-time monitoring ROM | [`DIGITAL_TWIN/Q100-61-MDL-DT-PROPULSOR/`](ASSETS/MODELS/DIGITAL_TWIN/) |

**Model Library**:
- [`MATERIALS/`](ASSETS/MODELS/MODEL_LIBRARY/MATERIALS/) - Material properties (CFRP, Ti, Al, Cu)
- [`AIRFOILS/`](ASSETS/MODELS/MODEL_LIBRARY/AIRFOILS/) - Blade airfoil data
- [`STANDARD_CONDITIONS/`](ASSETS/MODELS/MODEL_LIBRARY/STANDARD_CONDITIONS/) - Operating conditions

[↑ Back to Top](#61-00-04-design-assets-index) | [↑ Directory Index](#directory-index)

---

### 6.  PARTS

> **Path**: [`ASSETS/PARTS/`](ASSETS/PARTS/)  
> **Purpose**: Individual component definitions (source parts)  
> **Naming**: `Q100-61-PRT-[SYSTEM]-[COMPONENT]`

| Subdirectory | Components | Count | Link |
|--------------|------------|-------|------|
| Fan Components | Blade, hub, spinner | 5 | [`FAN_COMPONENTS/`](ASSETS/PARTS/FAN_COMPONENTS/) |
| Nacelle Components | Barrels, inlet, liner | 5 | [`NACELLE_COMPONENTS/`](ASSETS/PARTS/NACELLE_COMPONENTS/) |
| Gearbox Components | Gears, carrier, housing | 6 | [`GEARBOX_COMPONENTS/`](ASSETS/PARTS/GEARBOX_COMPONENTS/) |
| Motor Components | Stator, rotor, shaft | 9 | [`MOTOR_COMPONENTS/`](ASSETS/PARTS/MOTOR_COMPONENTS/) |
| Controller Components | Enclosure, heatsink | 4 | [`CONTROLLER_COMPONENTS/`](ASSETS/PARTS/CONTROLLER_COMPONENTS/) |
| Propeller Components | Blades, pitch actuator | 6 | [`PROPELLER_COMPONENTS/`](ASSETS/PARTS/PROPELLER_COMPONENTS/) |
| Mounting Components | Mounts, links, dampers | 5 | [`MOUNTING_COMPONENTS/`](ASSETS/PARTS/MOUNTING_COMPONENTS/) |
| Standard Parts | Fasteners, bearings, seals | Catalog | [`STANDARD_PARTS/`](ASSETS/PARTS/STANDARD_PARTS/) |
| Part Library | Master index, standards | Reference | [`PART_LIBRARY/`](ASSETS/PARTS/PART_LIBRARY/) |

**Key Parts**:
| Part | Link |
|------|------|
| Fan Blade | [`Q100-61-PRT-FAN-BLADE/`](ASSETS/PARTS/FAN_COMPONENTS/Q100-61-PRT-FAN-BLADE/) |
| Motor Stator Core | [`Q100-61-PRT-MOTOR-STATOR-CORE/`](ASSETS/PARTS/MOTOR_COMPONENTS/Q100-61-PRT-MOTOR-STATOR-CORE/) |
| Gearbox Sun Gear | [`Q100-61-PRT-GEARBOX-SUN-GEAR/`](ASSETS/PARTS/GEARBOX_COMPONENTS/Q100-61-PRT-GEARBOX-SUN-GEAR/) |

**Master Index**: [`Q100-61-PRT-MASTER-INDEX. yaml`](ASSETS/PARTS/PART_LIBRARY/Q100-61-PRT-MASTER-INDEX.yaml)

[↑ Back to Top](#61-00-04-design-assets-index) | [↑ Directory Index](#directory-index)

---

### 7.  PRODUCTS

> **Path**: [`ASSETS/PRODUCTS/`](ASSETS/PRODUCTS/)  
> **Purpose**: Released/configured product definitions  
> **Naming**: `Q100-61-PROD-[PRODUCT]-[VARIANT]`

| Subdirectory | Description | Link |
|--------------|-------------|------|
| Product Definitions | Top-level product specs | [`PRODUCT_DEFINITIONS/`](ASSETS/PRODUCTS/PRODUCT_DEFINITIONS/) |
| Product Variants | LH, RH, Center, Extended | [`PRODUCT_VARIANTS/`](ASSETS/PRODUCTS/PRODUCT_VARIANTS/) |
| Product Configurations | Baseline and options | [`PRODUCT_CONFIGURATIONS/`](ASSETS/PRODUCTS/PRODUCT_CONFIGURATIONS/) |
| Bill of Materials | Structured BOMs | [`BILL_OF_MATERIALS/`](ASSETS/PRODUCTS/BILL_OF_MATERIALS/) |
| Product Specifications | Performance, environmental | [`PRODUCT_SPECIFICATIONS/`](ASSETS/PRODUCTS/PRODUCT_SPECIFICATIONS/) |
| Certification | Type certificate, airworthiness | [`CERTIFICATION/`](ASSETS/PRODUCTS/CERTIFICATION/) |
| Product Lifecycle | Development, production | [`PRODUCT_LIFECYCLE/`](ASSETS/PRODUCTS/PRODUCT_LIFECYCLE/) |
| Product Standards | Configuration management | [`PRODUCT_STANDARDS/`](ASSETS/PRODUCTS/PRODUCT_STANDARDS/) |

**Product Hierarchy**:
```
Q100-61-PROD-PROPULSOR-SYSTEM
├── Q100-61-PROD-OPEN-FAN-UNIT
├── Q100-61-PROD-ELECTRIC-DRIVE-UNIT
├── Q100-61-PROD-GEARBOX-UNIT
├── Q100-61-PROD-NACELLE-UNIT
└── Q100-61-PROD-CONTROLLER-UNIT
```

| Product | Link |
|---------|------|
| Propulsor System | [`Q100-61-PROD-PROPULSOR-SYSTEM/`](ASSETS/PRODUCTS/PRODUCT_DEFINITIONS/Q100-61-PROD-PROPULSOR-SYSTEM/) |
| Open Fan Unit | [`Q100-61-PROD-OPEN-FAN-UNIT/`](ASSETS/PRODUCTS/PRODUCT_DEFINITIONS/Q100-61-PROD-OPEN-FAN-UNIT/) |
| Electric Drive Unit | [`Q100-61-PROD-ELECTRIC-DRIVE-UNIT/`](ASSETS/PRODUCTS/PRODUCT_DEFINITIONS/Q100-61-PROD-ELECTRIC-DRIVE-UNIT/) |

**Variants**:
| Variant | Link |
|---------|------|
| Left Hand (LH) | [`Q100-61-VAR-PROPULSOR-LH/`](ASSETS/PRODUCTS/PRODUCT_VARIANTS/Q100-61-VAR-PROPULSOR-LH/) |
| Right Hand (RH) | [`Q100-61-VAR-PROPULSOR-RH/`](ASSETS/PRODUCTS/PRODUCT_VARIANTS/Q100-61-VAR-PROPULSOR-RH/) |
| Center | [`Q100-61-VAR-PROPULSOR-CENTER/`](ASSETS/PRODUCTS/PRODUCT_VARIANTS/Q100-61-VAR-PROPULSOR-CENTER/) |

[↑ Back to Top](#61-00-04-design-assets-index) | [↑ Directory Index](#directory-index)

---

### 8. TEMPLATES

> **Path**: [`ASSETS/TEMPLATES/`](ASSETS/TEMPLATES/)  
> **Purpose**: Standardized templates and reusable patterns  
> **Naming**: `Q100-61-TPL-[CATEGORY]-[NAME]`

| Subdirectory | Content | Link |
|--------------|---------|------|
| CAD Templates | Part, assembly, startup models | [`CAD_TEMPLATES/`](ASSETS/TEMPLATES/CAD_TEMPLATES/) |
| Drawing Templates | Sheet formats, title blocks | [`DRAWING_TEMPLATES/`](ASSETS/TEMPLATES/DRAWING_TEMPLATES/) |
| Document Templates | Specs, reports, procedures | [`DOCUMENT_TEMPLATES/`](ASSETS/TEMPLATES/DOCUMENT_TEMPLATES/) |
| Data Templates | YAML, CSV, JSON schemas | [`DATA_TEMPLATES/`](ASSETS/TEMPLATES/DATA_TEMPLATES/) |
| Analysis Templates | FEA, CFD, simulation | [`ANALYSIS_TEMPLATES/`](ASSETS/TEMPLATES/ANALYSIS_TEMPLATES/) |
| Project Templates | Directory structures, READMEs | [`PROJECT_TEMPLATES/`](ASSETS/TEMPLATES/PROJECT_TEMPLATES/) |
| Certification Templates | Compliance, test plans | [`CERTIFICATION_TEMPLATES/`](ASSETS/TEMPLATES/CERTIFICATION_TEMPLATES/) |
| Template Standards | Usage guidelines | [`TEMPLATE_STANDARDS/`](ASSETS/TEMPLATES/TEMPLATE_STANDARDS/) |

**Common Templates**:
| Template | Purpose | Link |
|----------|---------|------|
| Part Definition | YAML part schema | [`Q100-61-TPL-YAML-PART-DEF. yaml`](ASSETS/TEMPLATES/DATA_TEMPLATES/YAML_SCHEMAS/) |
| Assembly Definition | YAML assembly schema | [`Q100-61-TPL-YAML-ASSY-DEF. yaml`](ASSETS/TEMPLATES/DATA_TEMPLATES/YAML_SCHEMAS/) |
| Part README | README template | [`Q100-61-TPL-README-PART.md`](ASSETS/TEMPLATES/PROJECT_TEMPLATES/README_TEMPLATES/) |
| A1 Drawing | Sheet format | [`Q100-61-TPL-DRW-A1-LANDSCAPE.svg`](ASSETS/TEMPLATES/DRAWING_TEMPLATES/SHEET_FORMATS/) |

[↑ Back to Top](#61-00-04-design-assets-index) | [↑ Directory Index](#directory-index)

---

## Naming Convention

### Prefix Reference

| Prefix | Type | Example |
|--------|------|---------|
| `Q100-61-ASSY-` | Assembly | `Q100-61-ASSY-OFP-FAN` |
| `Q100-61-DRW-` | Drawing | `Q100-61-DRW-FAN-BLADE` |
| `Q100-61-EXP-` | Export | `Q100-61-EXP-FPS-TOP-ASSY. step` |
| `Q100-61-INST-` | Installation | `Q100-61-INST-DEF-PROPULSOR-TO-PYLON` |
| `Q100-61-MDL-` | Model | `Q100-61-MDL-AERO-FAN-BLADE-CFD` |
| `Q100-61-PRT-` | Part | `Q100-61-PRT-FAN-BLADE` |
| `Q100-61-PROD-` | Product | `Q100-61-PROD-PROPULSOR-SYSTEM` |
| `Q100-61-TPL-` | Template | `Q100-61-TPL-YAML-PART-DEF` |
| `Q100-61-VAR-` | Variant | `Q100-61-VAR-PROPULSOR-LH` |
| `Q100-61-CFG-` | Configuration | `Q100-61-CFG-BASELINE-R01` |
| `Q100-61-BOM-` | Bill of Materials | `Q100-61-BOM-PROPULSOR-SYSTEM` |
| `Q100-61-RTE-` | Routing | `Q100-61-RTE-ELEC-H2-FC-LINK` |

### System Codes

| Code | System |
|------|--------|
| `OFP` | Open Fan Propulsor |
| `EMD` | Electric Motor Drive |
| `GBX` | Gearbox |
| `NAC` | Nacelle |
| `CTL` | Controller |
| `MNT` | Mounting |
| `FPS` | Full Propulsor System |
| `PV` | Propeller Variants |

[↑ Back to Top](#61-00-04-design-assets-index)

---

## Quick Navigation

### By Activity

| Task | Go To |
|------|-------|
| **Start New Part** | [`TEMPLATES/DATA_TEMPLATES/YAML_SCHEMAS/`](ASSETS/TEMPLATES/DATA_TEMPLATES/YAML_SCHEMAS/) |
| **Create Drawing** | [`TEMPLATES/DRAWING_TEMPLATES/`](ASSETS/TEMPLATES/DRAWING_TEMPLATES/) |
| **Export for Supplier** | [`EXPORTS/SUPPLIER_PACKAGES/`](ASSETS/EXPORTS/SUPPLIER_PACKAGES/) |
| **Run Analysis** | [`MODELS/`](ASSETS/MODELS/) |
| **Installation Procedure** | [`INSTALLATIONS/INSTALLATION_PROCEDURES/`](ASSETS/INSTALLATIONS/INSTALLATION_PROCEDURES/) |
| **Check BOM** | [`PRODUCTS/BILL_OF_MATERIALS/`](ASSETS/PRODUCTS/BILL_OF_MATERIALS/) |
| **Certification Data** | [`PRODUCTS/CERTIFICATION/`](ASSETS/PRODUCTS/CERTIFICATION/) |

### By System

| System | Parts | Assembly | Drawings | Models |
|--------|-------|----------|----------|--------|
| **Fan** | [`FAN_COMPONENTS/`](ASSETS/PARTS/FAN_COMPONENTS/) | [`OPEN_FAN_PROPULSOR/`](ASSETS/ASSEMBLIES/OPEN_FAN_PROPULSOR/) | [`OPEN_FAN_PROPULSOR/`](ASSETS/DRAWINGS/DRAWING_SETS/OPEN_FAN_PROPULSOR/) | [`AERODYNAMIC/FAN_BLADE/`](ASSETS/MODELS/AERODYNAMIC/FAN_BLADE/) |
| **Motor** | [`MOTOR_COMPONENTS/`](ASSETS/PARTS/MOTOR_COMPONENTS/) | [`ELECTRIC_MOTOR_DRIVE/`](ASSETS/ASSEMBLIES/ELECTRIC_MOTOR_DRIVE/) | [`ELECTRIC_MOTOR_DRIVE/`](ASSETS/DRAWINGS/DRAWING_SETS/ELECTRIC_MOTOR_DRIVE/) | [`ELECTROMAGNETIC/MOTOR/`](ASSETS/MODELS/ELECTROMAGNETIC/MOTOR/) |
| **Gearbox** | [`GEARBOX_COMPONENTS/`](ASSETS/PARTS/GEARBOX_COMPONENTS/) | [`OPEN_FAN_PROPULSOR/`](ASSETS/ASSEMBLIES/OPEN_FAN_PROPULSOR/) | [`GEARBOX/`](ASSETS/DRAWINGS/DRAWING_SETS/GEARBOX/) | [`STRUCTURAL/GEARBOX/`](ASSETS/MODELS/STRUCTURAL/GEARBOX/) |
| **Nacelle** | [`NACELLE_COMPONENTS/`](ASSETS/PARTS/NACELLE_COMPONENTS/) | [`OPEN_FAN_PROPULSOR/`](ASSETS/ASSEMBLIES/OPEN_FAN_PROPULSOR/) | [`NACELLE/`](ASSETS/DRAWINGS/DRAWING_SETS/NACELLE/) | [`AERODYNAMIC/NACELLE/`](ASSETS/MODELS/AERODYNAMIC/NACELLE/) |
| **Controller** | [`CONTROLLER_COMPONENTS/`](ASSETS/PARTS/CONTROLLER_COMPONENTS/) | [`ELECTRIC_MOTOR_DRIVE/`](ASSETS/ASSEMBLIES/ELECTRIC_MOTOR_DRIVE/) | [`ELECTRIC_MOTOR_DRIVE/`](ASSETS/DRAWINGS/DRAWING_SETS/ELECTRIC_MOTOR_DRIVE/) | [`THERMAL/CONTROLLER/`](ASSETS/MODELS/THERMAL/CONTROLLER/) |

### By Deliverable

| Deliverable | Location |
|-------------|----------|
| **STEP Exports** | [`EXPORTS/NEUTRAL_FORMATS/STEP/`](ASSETS/EXPORTS/NEUTRAL_FORMATS/STEP/) |
| **Drawing Packages** | [`EXPORTS/DOCUMENTATION/DRAWING_PACKAGES/`](ASSETS/EXPORTS/DOCUMENTATION/DRAWING_PACKAGES/) |
| **BOMs** | [`PRODUCTS/BILL_OF_MATERIALS/`](ASSETS/PRODUCTS/BILL_OF_MATERIALS/) |
| **Certification Docs** | [`PRODUCTS/CERTIFICATION/`](ASSETS/PRODUCTS/CERTIFICATION/) |
| **Supplier Data** | [`EXPORTS/SUPPLIER_PACKAGES/`](ASSETS/EXPORTS/SUPPLIER_PACKAGES/) |

[↑ Back to Top](#61-00-04-design-assets-index)

---

## Cross-References

### ATA 61 Sections

| Section | Description | Link |
|---------|-------------|------|
| 61-00 | General | [`../`](.. /) |
| 61-00-01 | Overview | [`../61-00-01_Overview/`](../61-00-01_Overview/) |
| 61-00-02 | Applicability | [`../61-00-02_Applicability/`](../61-00-02_Applicability/) |
| 61-00-03 | Acronyms | [`../61-00-03_Acronyms/`](../61-00-03_Acronyms/) |
| **61-00-04** | **Design** | **YOU ARE HERE** |
| 61-00-05 | Maintenance | [`../61-00-05_Maintenance/`](../61-00-05_Maintenance/) |

### ATA 61 Subsystems

| Subsystem | Description | Link |
|-----------|-------------|------|
| 61-10 | Propeller Assembly | [`../../61-10_PROPELLER_ASSEMBLY/`](../../61-10_PROPELLER_ASSEMBLY/) |
| 61-20 | Controlling | [`../../61-20_CONTROLLING/`](../../61-20_CONTROLLING/) |
| 61-30 | Braking | [`../../61-30_BRAKING/`](../../61-30_BRAKING/) |
| 61-40 | Indicating | [`../../61-40_INDICATING/`](../../61-40_INDICATING/) |
| 61-50 | Propulsor Duct | [`../../61-50_PROPULSOR_DUCT/`](../../61-50_PROPULSOR_DUCT/) |

### Related ATA Chapters

| Chapter | Description | Link |
|---------|-------------|------|
| 24 | Electrical Power | [`../../../ATA_24-ELECTRICAL_POWER/`](../../../ATA_24-ELECTRICAL_POWER/) |
| 28 | Fuel (H₂) | [`../../../ATA_28-FUEL/`](../../../ATA_28-FUEL/) |
| 71 | Power Plant | [`../../../ATA_71-POWER_PLANT/`](../../../ATA_71-POWER_PLANT/) |
| 72 | Engine | [`../../../ATA_72-ENGINE/`](../../../ATA_72-ENGINE/) |

[↑ Back to Top](#61-00-04-design-assets-index)

---

## Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-05 | Q100 Team | Initial release - 8 ASSETS directories |

---

## Contact

| Role | Contact |
|------|---------|
| **Program** | Q100 Hybrid-Electric Propulsion |
| **Owner** | Propulsion Systems Team |
| **Repository** | [AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E](https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E) |

---

[↑ Back to Top](#61-00-04-design-assets-index)
