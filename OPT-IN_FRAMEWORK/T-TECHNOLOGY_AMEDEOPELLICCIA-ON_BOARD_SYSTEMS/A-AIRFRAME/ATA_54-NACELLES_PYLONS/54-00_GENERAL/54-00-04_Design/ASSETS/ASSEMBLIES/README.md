# ATA 54 — NACELLES PYLONS Assemblies

## Overview

This folder contains assembly definitions for ATA Chapter 54 (Nacelles & Pylons) components. Each assembly is defined in YAML format following the AMPEL360 ASSETS Standard.

## Assembly Categories

### NACELLE_ASSEMBLIES
Complete nacelle assemblies including inlet, fan cowl, core cowl, and exhaust sections.

**Key Assemblies:**
- Primary Nacelle Structure
- Inlet Assembly
- Fan Cowl Assembly
- Core Cowl Assembly
- Exhaust Nozzle Assembly
- Acoustic Panels Assembly

### PYLON_ASSEMBLIES
Structural pylon assemblies connecting the engine to the wing or fuselage.

**Key Assemblies:**
- Forward Pylon Structure
- Aft Pylon Structure
- Pylon Fairing Assembly
- Engine Mount Assembly
- Systems Integration Assembly

### COWLING_ASSEMBLIES
Aerodynamic cowlings and fairings for nacelles and pylons.

**Key Assemblies:**
- Fan Cowl Doors
- Thrust Reverser Cowlings
- Pylon Fairing Panels
- Access Door Assemblies

### THRUST_REVERSER_ASSEMBLIES
Thrust reverser system assemblies for landing deceleration.

**Key Assemblies:**
- Cascade Assembly
- Blocker Door Assembly
- Actuation System Assembly
- Locking Mechanism Assembly

## Assembly File Format

Each assembly is defined using YAML with the following structure:

```yaml
assembly_metadata:
  assembly_id: "ASM-54-XXX-NNN"
  assembly_name: "Descriptive Name"
  ata_chapter: "54"
  zone: "XXX"
  parent_ci: "CI-54-XXX"
  related_cis: []
  structure_classification: "Primary|Secondary"
  plm_item_id: "TC-ASM-54-XXX-NNN"
  cad_master_drawing: "54-XX-NNNN"
  version:
    design_version: "1.0"
    status: "Preliminary|Released"
    last_update: "YYYY-MM-DD"
    author: "Team Name"

components:
  - part_number: "54-XXX-NNNN-NN"
    ci_number: "CI-54-XXX"
    description: "Component Description"
    quantity: N
    material: "Material Specification"
    primary_load_path: true|false

assembly_sequence:
  step_001: "Step description"
  step_002: "Step description"

tooling_required:
  - tooling_id: "TOOL-ID"
    description: "Tooling description"

quality_control:
  dimensional:
    tolerance_mm: X.X
    reference_drawing: "54-XX-NNNN"
  ndt:
    method: "Method description"
    coverage: "Coverage percentage"
  acceptance_criteria:
    - "Criterion 1"
    - "Criterion 2"

links:
  requirements_traceability_file: "path/to/file"
  stress_report: "path/to/file"
  fea_model_description: "path/to/file"
  manufacturing_plan: "path/to/file"
```

## Naming Conventions

Assembly IDs follow the pattern: `ASM-54-XXX-NNN`

Where:
- `54` = ATA Chapter
- `XXX` = Component area (NAC, PYL, COW, REV)
- `NNN` = Sequential number (001, 002, etc.)

Examples:
- `ASM-54-NAC-001` — Primary Nacelle Structure
- `ASM-54-PYL-001` — Forward Pylon Structure
- `ASM-54-COW-001` — Fan Cowl Doors
- `ASM-54-REV-001` — Cascade Assembly

## Traceability

All assemblies must maintain traceability to:
1. **Requirements**: Linked via requirements_traceability_file
2. **Safety Analysis**: Referenced in FHA/FMEA documents
3. **Manufacturing**: Connected to production plans
4. **Quality Control**: Tied to inspection procedures
5. **Configuration Items**: Parent and related CIs

## Integration with PLM

Each assembly has a `plm_item_id` field for integration with Teamcenter or equivalent PLM systems. This enables:
- BOM management
- Change control
- Effectivity tracking
- Supplier collaboration

## Related Documentation

- [AMPEL360_ASSETS_STANDARD.md](../../../../../../../../AMPEL360_ASSETS_STANDARD.md) — Asset naming and structure standards
- [54-00-03_Requirements](../../54-00-03_Requirements/) — Requirements traceability
- [54-00-02_Safety](../../54-00-02_Safety/) — Safety analysis
- [54-00-06_Engineering](../../54-00-06_Engineering/) — Engineering analysis

## Document Control

- **Version**: 1.0
- **Status**: Active
- **Last Updated**: 2026-01-02
- **Owner**: AMPEL360 ATA 54 Design Team
- **Standard**: AMPEL360 ASSETS Standard v1.0
