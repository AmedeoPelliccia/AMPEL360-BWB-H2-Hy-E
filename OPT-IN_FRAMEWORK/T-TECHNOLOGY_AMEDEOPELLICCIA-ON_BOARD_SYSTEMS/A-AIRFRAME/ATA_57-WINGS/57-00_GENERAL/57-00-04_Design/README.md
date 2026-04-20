---
# AMPEL360 ASSETS INDEX — applies to this XX-..-.. folder only
version: 1
owner: "AMPEL360 Documentation Team"
folder: "57-00-04_Design"

assets:
  # ASSEMBLIES
  - id: "57-00-04-ASSY-001"
    category: "ASSY"
    title: "Wing Primary Structure Assembly"
    source: "ASSETS/ASSEMBLIES/wing_primary_structure.step"
    exports: []
    links:
      reqs: ["REQ-57-00-001"]
      odd: []
      safety: ["HAZ-57-001"]
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  - id: "57-00-04-ASSY-002"
    category: "ASSY"
    title: "Flap System Assembly"
    source: "ASSETS/ASSEMBLIES/flap_system_assembly.step"
    exports: []
    links:
      reqs: ["REQ-57-21-001"]
      odd: []
      safety: []
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  # DRAWINGS
  - id: "57-00-04-D001"
    category: "DRWG"
    title: "Wing Planform Drawing"
    source: "ASSETS/DRAWINGS/57-00-04-D001_Wing_Planform.dwg"
    exports: []
    links:
      reqs: ["REQ-57-00-002"]
      odd: []
      safety: []
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  - id: "57-00-04-D002"
    category: "DRWG"
    title: "Spar Section AA Drawing"
    source: "ASSETS/DRAWINGS/57-00-04-D002_Spar_Section_AA.dxf"
    exports: []
    links:
      reqs: ["REQ-57-25-001"]
      odd: []
      safety: []
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  - id: "57-00-04-D003"
    category: "DRWG"
    title: "Rib Layout BB Drawing"
    source: "ASSETS/DRAWINGS/57-00-04-D003_Rib_Layout_BB.dxf"
    exports: []
    links:
      reqs: ["REQ-57-25-002"]
      odd: []
      safety: []
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  # EXPORTS
  - id: "57-00-04-A001"
    category: "EXPT"
    title: "Wing Exploded View"
    source: "ASSETS/EXPORTS/57-00-04-A001_Wing_Exploded_View.png"
    exports: []
    links:
      reqs: []
      odd: []
      safety: []
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  - id: "57-00-04-A002"
    category: "EXPT"
    title: "CFD Surface Mesh Export"
    source: "ASSETS/EXPORTS/57-00-04-A002_CFD_Surface_Mesh.expt"
    exports: []
    links:
      reqs: []
      odd: []
      safety: []
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  - id: "57-00-04-A003"
    category: "EXPT"
    title: "Loads Heatmap Export"
    source: "ASSETS/EXPORTS/57-00-04-A003_Loads_Heatmap.expt"
    exports: []
    links:
      reqs: []
      odd: []
      safety: []
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  # INSTALLATIONS - LAYOUTS
  - id: "57-00-04-I001"
    category: "INST"
    title: "Fuel Tank Installation Layout"
    source: "ASSETS/INSTALLATIONS/LAYOUTS/57-00-04-I001_Fuel_Tank_Installation.png"
    exports: []
    links:
      reqs: ["REQ-57-26-001"]
      odd: []
      safety: ["HAZ-57-002"]
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  # INSTALLATIONS - DIAGRAMS
  - id: "57-00-04-I010"
    category: "DIAG"
    title: "Structural Attachments Diagram"
    source: "ASSETS/INSTALLATIONS/DIAGRAMS/57-00-04-I010_Structural_Attachments.mermaid"
    exports: []
    links:
      reqs: ["REQ-57-25-003"]
      odd: []
      safety: []
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  # INSTALLATIONS - BIM/CAD
  - id: "57-00-04-B001"
    category: "MODL"
    title: "Wing Structure BIM Model"
    source: "ASSETS/INSTALLATIONS/BIM_CAD_MODELS/57-00-04-B001_Wing_Structure.bim"
    exports: []
    links:
      reqs: []
      odd: []
      safety: []
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  # MODELS - GEOMETRY
  - id: "57-00-04-M001"
    category: "MODL"
    title: "Wing Geometry Model"
    source: "ASSETS/MODELS/GEOMETRY/57-00-04-M001_Wing_Geometry.step"
    exports: []
    links:
      reqs: ["REQ-57-00-003"]
      odd: []
      safety: []
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  # PARTS
  - id: "57-00-04-P001"
    category: "PART"
    title: "Main Spar Part Model"
    source: "ASSETS/PARTS/57-00-04-P001_Main_Spar.step"
    exports: []
    links:
      reqs: ["REQ-57-25-004"]
      odd: []
      safety: ["HAZ-57-001"]
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  - id: "57-00-04-P002"
    category: "PART"
    title: "Rib 12 Part Model"
    source: "ASSETS/PARTS/57-00-04-P002_Rib_12.step"
    exports: []
    links:
      reqs: ["REQ-57-25-005"]
      odd: []
      safety: []
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  - id: "57-00-04-P003"
    category: "PART"
    title: "Aileron Hinge Part Model"
    source: "ASSETS/PARTS/57-00-04-P003_Aileron_Hinge.step"
    exports: []
    links:
      reqs: ["REQ-57-23-001"]
      odd: []
      safety: []
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  # PRODUCTS
  - id: "57-00-04-PRD-001"
    category: "PROD"
    title: "Wing Assembly Baseline Product Document"
    source: "ASSETS/PRODUCTS/57-00-04-PRD_Wing_Assembly_Baseline.pdf"
    exports: []
    links:
      reqs: ["REQ-57-00-001"]
      odd: []
      safety: []
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  - id: "57-00-04-PRD-002"
    category: "PROD"
    title: "Wing Interface Map Product Document"
    source: "ASSETS/PRODUCTS/57-00-04-PRD_Interface_Map.pdf"
    exports: []
    links:
      reqs: ["REQ-57-05-001"]
      odd: []
      safety: []
    status: "Draft"
    version: "0.1.0"
    checksum: "<filled-by-CI>"

  # TEMPLATES
  - id: "57-00-04-T001"
    category: "TMPL"
    title: "CAD Template for Wing Design"
    source: "ASSETS/TEMPLATES/57-00-04-T001_CAD_Template.dwt"
    exports: []
    links:
      reqs: []
      odd: []
      safety: []
    status: "Approved"
    version: "1.0.0"
    checksum: "<filled-by-CI>"

  - id: "57-00-04-T002"
    category: "TMPL"
    title: "Model Card Template for Wing Components"
    source: "ASSETS/TEMPLATES/57-00-04-T002_ModelCard_Wing.md"
    exports: []
    links:
      reqs: []
      odd: []
      safety: []
    status: "Approved"
    version: "1.0.0"
    checksum: "<filled-by-CI>"

  - id: "57-00-04-T003"
    category: "TMPL"
    title: "ICD Template for Wing Interfaces"
    source: "ASSETS/TEMPLATES/57-00-04-T003_ICD_Template.md"
    exports: []
    links:
      reqs: []
      odd: []
      safety: []
    status: "Approved"
    version: "1.0.0"
    checksum: "<filled-by-CI>"
---

# 57-00-04_Design

## Purpose

Reference architectures and design patterns for ATA Chapter 57 — Wings.

## Scope

This folder is part of the **57-00_GENERAL** layer, which provides governance and lifecycle management for ATA Chapter 57.

## Directory Structure

```
57-00-04_Design/
│
├── 57-00-04_Design_Overview.md
│
├── ASSETS/
│   ├── README.md
│   │
│   ├── ASSEMBLIES/
│   │   ├── wing_primary_structure.step
│   │   ├── flap_system_assembly.step
│   │   └── .gitkeep
│   │
│   ├── DRAWINGS/
│   │   ├── 57-00-04-D001_Wing_Planform.dwg
│   │   ├── 57-00-04-D002_Spar_Section_AA.dxf
│   │   ├── 57-00-04-D003_Rib_Layout_BB.dxf
│   │   └── .gitkeep
│   │
│   ├── EXPORTS/
│   │   ├── 57-00-04-A001_Wing_Exploded_View.png
│   │   ├── 57-00-04-A002_CFD_Surface_Mesh.expt
│   │   ├── 57-00-04-A003_Loads_Heatmap.expt
│   │   └── .gitkeep
│   │
│   ├── INSTALLATIONS/
│   │   ├── LAYOUTS/
│   │   │   ├── 57-00-04-I001_Fuel_Tank_Installation.png
│   │   │   └── .gitkeep
│   │   ├── DIAGRAMS/
│   │   │   ├── 57-00-04-I010_Structural_Attachments.mermaid
│   │   │   └── .gitkeep
│   │   ├── BIM_CAD_MODELS/
│   │   │   ├── 57-00-04-B001_Wing_Structure.bim
│   │   │   └── .gitkeep
│   │   └── .gitkeep
│   │
│   ├── MODELS/
│   │   ├── GEOMETRY/
│   │   │   ├── 57-00-04-M001_Wing_Geometry.step
│   │   │   └── .gitkeep
│   │   └── .gitkeep
│   │
│   ├── PARTS/
│   │   ├── 57-00-04-P001_Main_Spar.step
│   │   ├── 57-00-04-P002_Rib_12.step
│   │   ├── 57-00-04-P003_Aileron_Hinge.step
│   │   └── .gitkeep
│   │
│   ├── PRODUCTS/
│   │   ├── 57-00-04-PRD_Wing_Assembly_Baseline.pdf
│   │   ├── 57-00-04-PRD_Interface_Map.pdf
│   │   └── .gitkeep
│   │
│   └── TEMPLATES/
│       ├── 57-00-04-T001_CAD_Template.dwt
│       ├── 57-00-04-T002_ModelCard_Wing.md
│       ├── 57-00-04-T003_ICD_Template.md
│       └── .gitkeep
│
└── README.md
```

## Contents

This folder should contain:
- **[57-00-04_Design_Overview.md](57-00-04_Design_Overview.md)** - Design overview document
- **[ASSETS/](ASSETS/)** - Standardized design artifacts (diagrams, drawings, models, data)
  - See [ASSETS/README.md](ASSETS/README.md) for structure and usage
  - See [ASSETS/INDEX.meta.yaml](ASSETS/INDEX.meta.yaml) for authoritative asset catalog
- Documentation related to reference architectures and design patterns
- Traceability matrices linking to other lifecycle stages
- Evidence and artifacts supporting this lifecycle phase

## Asset Categories

| Category | Description | File Types |
|----------|-------------|------------|
| **ASSEMBLIES** | Wing assembly models | `.step`, `.stp` |
| **DRAWINGS** | Engineering drawings | `.dwg`, `.dxf`, `.pdf` |
| **EXPORTS** | Rendered outputs | `.png`, `.pdf`, `.expt` |
| **INSTALLATIONS** | Installation layouts, diagrams, BIM/CAD models | `.png`, `.mermaid`, `.bim` |
| **MODELS** | Geometry models | `.step`, `.stp` |
| **PARTS** | Individual component models | `.step`, `.stp` |
| **PRODUCTS** | Product-level documentation | `.pdf`, `.md` |
| **TEMPLATES** | CAD and documentation templates | `.dwt`, `.md` |

## Status

- **Phase**: Design
- **Lifecycle Position**: 04 of 14
- **Status**: Active
- **Last Updated**: 2025-11-29

## Related Folders

Part of the canonical 14-folder lifecycle:
1. Overview → 2. Safety → 3. Requirements → **4. Design** → 5. Interfaces → 6. Engineering → 7. V&V → 8. Prototyping → 9. Production Planning → 10. Certification → 11. EIS/Versions/Tags → 12. Services → 13. Subsystems/Components → 14. Ops/Std/Sustain

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- **Standard**: OPT-IN Framework v1.1 (ATA 95 canonical template)
- **Owner**: AMPEL360 Documentation WG
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-29.
