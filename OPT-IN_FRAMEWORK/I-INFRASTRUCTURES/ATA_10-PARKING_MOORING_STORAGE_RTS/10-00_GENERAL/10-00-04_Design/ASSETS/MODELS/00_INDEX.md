# ATA 10 — MODELS Index

## Overview

This index provides a complete catalog of all models, assemblies, components, and simulations in the ATA 10 Parking, Mooring, Storage & RTS MODELS directory.

## Quick Navigation

- [Assemblies](#assemblies)
- [Components](#components)
  - [Tiedown Components](#tiedown-components)
  - [Mooring Components](#mooring-components)
  - [Parking Components](#parking-components)
  - [H2 Systems Components](#h2-systems-components)
- [Simulations](#simulations)
  - [Finite Element Analysis (FEA)](#finite-element-analysis-fea)
  - [Computational Fluid Dynamics (CFD)](#computational-fluid-dynamics-cfd)
- [Templates](#templates)

---

## Assemblies

Top-level assembly documentation for major ATA 10 systems.

| Model ID | Document | Description | Status |
|----------|----------|-------------|--------|
| 10-MDL-ASM-001 | [BWB_Parking_Configuration.md](./assemblies/10-MDL-ASM-001_BWB_Parking_Configuration.md) | BWB-specific parking configuration with wingspan considerations | ACTIVE |
| 10-MDL-ASM-002 | [Tiedown_System_Assembly.md](./assemblies/10-MDL-ASM-002_Tiedown_System_Assembly.md) | Complete tiedown system assembly | ACTIVE |
| 10-MDL-ASM-003 | [Mooring_Equipment_Assembly.md](./assemblies/10-MDL-ASM-003_Mooring_Equipment_Assembly.md) | Mooring equipment assembly for wind restraint | ACTIVE |
| 10-MDL-ASM-004 | [H2_Safety_Equipment_Assembly.md](./assemblies/10-MDL-ASM-004_H2_Safety_Equipment_Assembly.md) | H2 safety equipment assembly | ACTIVE |

---

## Components

### Tiedown Components

Tiedown system components for securing the aircraft during parking and storage.

| Model ID | Document | Description | CAD Available | Status |
|----------|----------|-------------|---------------|--------|
| 10-MDL-TD-001 | [Tiedown_Ring.md](./components/tiedown/10-MDL-TD-001_Tiedown_Ring.md) | Aircraft tiedown ring attachment point | TBD | ACTIVE |
| 10-MDL-TD-002 | [Tiedown_Fitting.md](./components/tiedown/10-MDL-TD-002_Tiedown_Fitting.md) | Tiedown cable fitting and connector | TBD | ACTIVE |
| 10-MDL-TD-003 | [Ground_Anchor.md](./components/tiedown/10-MDL-TD-003_Ground_Anchor.md) | Ground anchor point for tiedown cables | TBD | ACTIVE |

### Mooring Components

Mooring system components for wind restraint and aircraft stabilization.

| Model ID | Document | Description | CAD Available | Status |
|----------|----------|-------------|---------------|--------|
| 10-MDL-MR-001 | [Mooring_Mast.md](./components/mooring/10-MDL-MR-001_Mooring_Mast.md) | Mooring mast structure | TBD | ACTIVE |
| 10-MDL-MR-002 | [Mooring_Cable.md](./components/mooring/10-MDL-MR-002_Mooring_Cable.md) | High-strength mooring cable assembly | TBD | ACTIVE |
| 10-MDL-MR-003 | [Mooring_Clamp.md](./components/mooring/10-MDL-MR-003_Mooring_Clamp.md) | Cable clamp and tensioning device | TBD | ACTIVE |

### Parking Components

Parking system components for ground handling and aircraft security.

| Model ID | Document | Description | CAD Available | Status |
|----------|----------|-------------|---------------|--------|
| 10-MDL-PK-001 | [Wheel_Chock.md](./components/parking/10-MDL-PK-001_Wheel_Chock.md) | Aircraft wheel chock - BWB configuration | TBD | ACTIVE |
| 10-MDL-PK-002 | [Ground_Lock.md](./components/parking/10-MDL-PK-002_Ground_Lock.md) | Ground lock mechanism | TBD | ACTIVE |
| 10-MDL-PK-003 | [Parking_Brake_Lock.md](./components/parking/10-MDL-PK-003_Parking_Brake_Lock.md) | Parking brake lock device | TBD | ACTIVE |

### H2 Systems Components

Hydrogen system components for safe parking and storage operations.

| Model ID | Document | Description | CAD Available | Status |
|----------|----------|-------------|---------------|--------|
| 10-MDL-H2-001 | [H2_Vent_Valve.md](./components/h2-systems/10-MDL-H2-001_H2_Vent_Valve.md) | H2 vent valve for safe gas release | TBD | ACTIVE |
| 10-MDL-H2-002 | [H2_Detector_Housing.md](./components/h2-systems/10-MDL-H2-002_H2_Detector_Housing.md) | Housing for H2 leak detector | TBD | ACTIVE |
| 10-MDL-H2-003 | [Cryo_Insulation_Cover.md](./components/h2-systems/10-MDL-H2-003_Cryo_Insulation_Cover.md) | Cryogenic insulation cover for fuel system | TBD | ACTIVE |

---

## Simulations

### Finite Element Analysis (FEA)

Structural analysis simulations for load-bearing components.

| Simulation ID | Document | Analysis Type | Status |
|---------------|----------|---------------|--------|
| 10-SIM-FEA-001 | [Tiedown_Load_Analysis.md](./simulations/fea/10-SIM-FEA-001_Tiedown_Load_Analysis.md) | Tiedown system load and stress analysis | ACTIVE |
| 10-SIM-FEA-002 | [Mooring_Stress_Analysis.md](./simulations/fea/10-SIM-FEA-002_Mooring_Stress_Analysis.md) | Mooring system stress and fatigue analysis | ACTIVE |

### Computational Fluid Dynamics (CFD)

Fluid dynamics simulations for H2 safety and ventilation.

| Simulation ID | Document | Analysis Type | Status |
|---------------|----------|---------------|--------|
| 10-SIM-CFD-001 | [H2_Dispersion_Analysis.md](./simulations/cfd/10-SIM-CFD-001_H2_Dispersion_Analysis.md) | H2 dispersion for safety scenarios | ACTIVE |
| 10-SIM-CFD-002 | [Ventilation_Flow_Analysis.md](./simulations/cfd/10-SIM-CFD-002_Ventilation_Flow_Analysis.md) | Ventilation flow in parking/storage areas | ACTIVE |

---

## Templates

Standard templates for model documentation and management.

| Template | Document | Purpose |
|----------|----------|---------|
| Model Specification | [model-specification-template.md](./model-templates/model-specification-template.md) | Template for documenting model specifications |
| Release Checklist | [model-release-checklist.md](./model-templates/model-release-checklist.md) | Checklist for releasing models to production |
| Validation Template | [model-validation-template.md](./model-templates/model-validation-template.md) | Template for model validation documentation |

---

## CAD File Locations

### Native CAD Files

- **CATIA**: `cad-native/catia/`
- **SolidWorks**: `cad-native/solidworks/`
- **NX**: `cad-native/nx/`

### Exchange Formats

- **STEP**: `exchange-formats/step/`
- **IGES**: `exchange-formats/iges/`
- **JT**: `exchange-formats/jt/`

### Visualization Formats

- **STL**: `visualization/stl/`
- **OBJ**: `visualization/obj/`
- **glTF**: `visualization/gltf/`

---

## Statistics

- **Total Assemblies**: 4
- **Total Components**: 12
  - Tiedown: 3
  - Mooring: 3
  - Parking: 3
  - H2 Systems: 3
- **Total Simulations**: 4
  - FEA: 2
  - CFD: 2
- **Total Templates**: 3

---

## Related Documentation

- [README.md](./README.md) - MODELS directory overview and guidelines
- [model-metadata.schema.json](./model-metadata.schema.json) - Metadata schema definition
- [ATA 10 Design Overview](../../README.md) - Parent design documentation
- [AMPEL360 Assets Standard](../../../../../../../AMPEL360_ASSETS_STANDARD.md) - Organization-wide asset standards

---

## Document Control

- **Document ID**: 10-00-04-MODELS-INDEX
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-12-09
- **Owner**: AMPEL360 ATA 10 Design Team
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
