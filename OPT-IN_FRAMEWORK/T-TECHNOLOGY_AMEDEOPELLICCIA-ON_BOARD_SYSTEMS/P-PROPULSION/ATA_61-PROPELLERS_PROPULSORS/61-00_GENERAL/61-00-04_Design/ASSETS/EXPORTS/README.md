# 61-00-04 Design EXPORTS

This directory contains all **exported and packaged design data** for ATA 61 Propellers/Propulsors systems, organized by purpose and recipient.

## Purpose

The EXPORTS directory serves as the single source of truth for **deliverable design artifacts** for the AMPEL360-BWB-H2-Hy-E hybrid propulsion system, including:

- CAD models in neutral formats for interoperability
- Visualization exports for design review and stakeholder communication
- Manufacturing data packages for production facilities
- Analysis models for FEA, CFD, thermal, and electromagnetic validation
- Drawing packages and technical publications
- Supplier packages for external partners
- Release history and archive management

## Directory Structure

```
EXPORTS/
├── README.md                     # This file
├── Q100-61-EXPORT-SETTINGS.yaml  # Export settings standards
│
├── NEUTRAL_FORMATS/              # Neutral CAD formats for interoperability
│   ├── README.md
│   ├── STEP/                     # STEP AP242 exports
│   ├── JT/                       # JT format with PMI
│   ├── IGES/                     # Legacy IGES support
│   └── PARASOLID/                # Parasolid kernel exports
│
├── VISUALIZATION/                # Visualization and review exports
│   ├── README.md
│   ├── 3DPDF/                    # 3D PDF for interactive review
│   ├── GLTF/                     # glTF/GLB for web viewing
│   ├── STL/                      # STL mesh exports
│   │   ├── HIGH_RES/             # High resolution for visualization
│   │   └── LOW_RES/              # Low resolution for quick view
│   └── OBJ/                      # OBJ for general 3D applications
│
├── MANUFACTURING/                # Manufacturing export formats
│   ├── README.md
│   ├── CNC/                      # CNC machining data
│   ├── 3D_PRINT/                 # Additive manufacturing exports
│   ├── SHEET_METAL/              # Sheet metal flat patterns
│   └── COMPOSITES/               # Composite layup data
│
├── ANALYSIS/                     # Analysis model exports
│   ├── README.md
│   ├── FEA_MESH/                 # FEA mesh exports
│   ├── CFD_GEOMETRY/             # CFD surface geometry
│   ├── THERMAL/                  # Thermal analysis models
│   └── ELECTROMAGNETIC/          # EM analysis exports
│
├── DOCUMENTATION/                # Document packages
│   ├── README.md
│   ├── DRAWING_PACKAGES/         # Packaged drawing releases
│   │   └── MANIFESTS/            # Package manifest files
│   ├── DATA_SHEETS/              # Component data sheets
│   └── TECHNICAL_PUBLICATIONS/   # CMM, IPC, AMM publications
│
├── SUPPLIER_PACKAGES/            # External supplier data
│   └── README.md
│
└── RELEASE_HISTORY/              # Release versioning and archive
    ├── README.md
    └── ARCHIVE/                  # Archived releases
```

## Naming Convention (Q100-61 Prefix)

All exported files follow the Q100 program naming convention:

```
Q100-61-[TYPE]-[SYSTEM/COMPONENT]-[VARIANT].[ext]
```

### Export Type Codes

| Code | Type                    | Purpose                              |
|------|-------------------------|--------------------------------------|
| EXP  | Neutral Format Export   | STEP, JT, IGES, Parasolid exports    |
| VIS  | Visualization Export    | 3D PDF, glTF, STL, OBJ               |
| MFG  | Manufacturing Export    | CNC, 3D Print, Sheet Metal           |
| FEA  | FEA Mesh Export         | Nastran, Abaqus, ANSYS meshes        |
| CFD  | CFD Geometry Export     | Surface geometry for CFD             |
| THM  | Thermal Analysis Export | Thermal model exports                |
| EM   | Electromagnetic Export  | EM analysis geometry                 |
| PKG  | Drawing Package         | Packaged drawing releases            |
| DS   | Data Sheet              | Component data sheets                |
| TP   | Technical Publication   | CMM, IPC, AMM documents              |
| SUP  | Supplier Package        | Supplier data packages               |
| REL  | Release Package         | Official release packages            |

### System/Component Abbreviations

| Code | System/Component                       |
|------|----------------------------------------|
| FPS  | Full Propulsor System                  |
| EMD  | Electric Motor Drive                   |
| GBX  | Gearbox                                |
| FAN  | Fan/Propeller                          |
| NAC  | Nacelle                                |
| INL  | Inlet                                  |
| OFP  | Outlet/Flow Path                       |
| MNT  | Mounting/Attachment                    |
| CTL  | Control System                         |
| PWR  | Power Electronics                      |
| CLG  | Cooling System                         |

### Example File Names

```
Q100-61-EXP-FPS-TOP-ASSY.step         → Full Propulsor System top-level STEP assembly
Q100-61-VIS-EMD-MOTOR-ASSY.gltf       → Motor Assembly web visualization
Q100-61-MFG-3DP-FAN-BLADE-PROTO.stl   → Fan blade 3D print prototype
Q100-61-FEA-GBX-HOUSING.nas           → Gearbox housing FEA mesh (Nastran)
Q100-61-CFD-NAC-SURFACE.stl           → Nacelle CFD surface geometry
Q100-61-PKG-OFP-RELEASE-R01.zip       → Drawing package release 01
Q100-61-DS-EMD-MOTOR-SPEC.md          → Motor specification data sheet
Q100-61-SUP-GBX-VENDOR-PKG.zip        → Gearbox supplier package
Q100-61-REL-FPS-V1.0.0.zip            → Full system release v1.0.0
```

## Export Standards

All exports in this directory SHALL comply with:

- **[CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)** - EASA Certification Specifications for Large Aeroplanes
- **[Part 21](https://www.easa.europa.eu/document-library/regulations/commission-regulation-eu-no-7482012)** - EASA Certification Procedures
- **ISO 10303-242 (STEP AP242)** - Industrial automation systems and integration
- **ISO/IEC 9001:2015** - Quality Management Systems
- **AS9100D** - Aerospace Quality Management

## Usage Guidelines

### Adding New Exports

1. Determine the appropriate export category and subdirectory
2. Follow the Q100-61 naming convention strictly
3. Update the relevant index or manifest file
4. Include metadata: version, date, author, checksum
5. Link to source design files in INDEX.meta.yaml

### Quality Control

All exports MUST:

- Be validated against source data
- Include version information
- Pass format validation checks
- Be traceable to requirements
- Include export date and responsible engineer

### Access Control

- **Internal Use**: Most exports are for internal team use
- **Supplier Access**: SUPPLIER_PACKAGES may be shared under NDA
- **Authority Access**: Packages for regulatory review
- **Customer Access**: Deliverables for airline/operator use

## Traceability

Exports are linked to:

- **Requirements**: Via requirement IDs in INDEX.meta.yaml
- **Safety Analysis**: Via hazard IDs in safety documentation
- **Design Artifacts**: Via source file references
- **Manufacturing Plans**: Via manufacturing work packages

## Related Documentation

- [AMPEL360_ASSETS_STANDARD.md](../../../../../../../AMPEL360_ASSETS_STANDARD.md) - Asset management standard
- [61-00-04_Design README](../../README.md) - Design folder overview
- [ATA_03_NUMBERING_GUIDE.md](../../../../../../../ATA_03_NUMBERING_GUIDE.md) - ATA numbering conventions
- [Q100-61-EXPORT-SETTINGS.yaml](Q100-61-EXPORT-SETTINGS.yaml) - Detailed export settings

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
