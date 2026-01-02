# ATA 54 Assembly Template

This template provides a standardized structure for defining assemblies in ATA Chapter 54 (Nacelles & Pylons).

## Instructions

1. Copy this template and rename following the pattern: `ASM-54-XXX-NNN_Description.yaml`
2. Replace all `<placeholders>` with actual values
3. Remove sections that are not applicable
4. Ensure all referenced files exist or create placeholders for them
5. Update INDEX.meta.yaml with the new assembly entry

---

```yaml
assembly_metadata:
  assembly_id: "ASM-54-<AREA>-<NNN>"  # e.g., ASM-54-NAC-002
  assembly_name: "<Descriptive Assembly Name>"
  ata_chapter: "54"
  zone: "<ZZZ-ZZZ>"  # e.g., 540-560
  parent_ci: "CI-54-<PARENT>"  # Parent Configuration Item
  related_cis:
    - "CI-54-<RELATED-1>"
    - "CI-54-<RELATED-2>"
  structure_classification: "<Primary|Secondary>"
  plm_item_id: "TC-ASM-54-<AREA>-<NNN>"
  cad_master_drawing: "54-<XX>-<NNNN>"
  version:
    design_version: "1.0"
    status: "<Preliminary|Released|Obsolete>"
    last_update: "<YYYY-MM-DD>"
    author: "<Team or Engineer Name>"

components:
  - part_number: "54-<AREA>-<NNNN>-<NN>"
    ci_number: "CI-54-<CI>"
    description: "<Component Description>"
    quantity: <N>
    material: "<Material Specification>"
    primary_load_path: <true|false>
    notes: "<Additional information>"

  # Add more components as needed

assembly_sequence:
  step_001: "<First assembly step description>"
  step_002: "<Second assembly step description>"
  # Continue numbering steps sequentially

tooling_required:
  - tooling_id: "<TOOL-ID>"
    description: "<Tooling description and purpose>"
  # Add more tooling as needed

quality_control:
  dimensional:
    tolerance_mm: <X.X>
    reference_drawing: "54-<XX>-<NNNN>"
    critical_dimensions:
      - "<Critical dimension 1>"
      - "<Critical dimension 2>"
  ndt:
    method: "<Inspection method>"
    coverage: "<Coverage percentage or description>"
    report_ref: "<Path to NDT report>"
  fasteners:
    torque_spec_nm: <NNN>
    torque_tolerance_percent: <X>
    inspection_coverage: "<Coverage description>"
  acceptance_criteria:
    - "<Criterion 1>"
    - "<Criterion 2>"
    # Add more criteria as needed

links:
  requirements_traceability_file: "../../54-00-03_Requirements/<filename>.csv"
  stress_report: "../MODELS/<filename>.md"
  fea_model_description: "../MODELS/<filename>.md"
  manufacturing_plan: "../../54-00-09_Production_Planning/<filename>.md"
  qc_plan: "../DATA/<filename>.csv"
  # Add additional links as needed

notes: |
  <Free-form notes about the assembly>
  
  Key design considerations:
  - <Consideration 1>
  - <Consideration 2>
  
  Safety features:
  - <Safety feature 1>
  - <Safety feature 2>
  
  Maintenance considerations:
  - <Maintenance consideration 1>
  - <Maintenance consideration 2>
  
  Future enhancements:
  - <Enhancement 1>
  - <Enhancement 2>
```

## Assembly ID Conventions

| Area Code | Description | Example |
|-----------|-------------|---------|
| NAC | Nacelle assemblies | ASM-54-NAC-001 |
| PYL | Pylon assemblies | ASM-54-PYL-001 |
| COW | Cowling assemblies | ASM-54-COW-001 |
| REV | Thrust reverser assemblies | ASM-54-REV-001 |
| INL | Inlet assemblies | ASM-54-INL-001 |
| EXH | Exhaust assemblies | ASM-54-EXH-001 |

## Material Specifications

Common materials used in ATA 54:

- **CFRP-Epoxy**: Carbon Fiber Reinforced Polymer with epoxy matrix
- **Al-7075-T73**: Aluminum alloy, high strength
- **Al-2024-T3**: Aluminum alloy, general purpose
- **Ti-6Al-4V**: Titanium alloy, aerospace grade
- **Ti-10V-2Fe-3Al**: Titanium alloy, high strength
- **Steel-15-5PH**: Precipitation hardening stainless steel
- **Steel-4340**: High strength steel
- **Nomex-Honeycomb**: Aramid fiber honeycomb core
- **Kevlar-Honeycomb**: Kevlar honeycomb for acoustic panels

## Quality Control Methods

Common inspection methods:

- **Ultrasonic**: For internal defect detection
- **X-ray**: For density and porosity inspection
- **Eddy Current**: For surface cracks
- **Dye Penetrant**: For surface crack detection
- **Visual**: For general inspection
- **Dimensional**: For tolerance verification
- **Pressure Test**: For seal verification
- **Load Test**: For structural verification

## Related Standards

- CS-25: Certification Specifications for Large Aeroplanes
- DO-178C: Software Considerations in Airborne Systems
- DO-254: Design Assurance for Airborne Electronic Hardware
- ATA iSpec 2200: Information Standards for Aviation Maintenance

## Document Control

- **Template Version**: 1.0
- **Status**: Active
- **Last Updated**: 2026-01-02
- **Owner**: AMPEL360 ATA 54 Design Team
- **Standard**: AMPEL360 ASSETS Standard v1.0
