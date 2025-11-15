# BIM_CAD_MODELS — Administration

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / BIM_CAD_MODELS / 00_ADMIN  
**Purpose:** Administrative files, metadata, and change tracking for BIM/CAD models

---

## Contents

This folder contains:

- **README.md** - This file, describing the BIM_CAD_MODELS structure
- **CHANGELOG.md** - Revision history of all BIM/CAD models in this folder tree
- **02-00-04-BIM_Metadata_Template.xlsx** - Standard metadata template for BIM models (LOD, discipline, version, etc.)

---

## BIM_CAD_MODELS Structure

```
BIM_CAD_MODELS/
├── 00_ADMIN/                      # Administrative files (this folder)
├── 05_TEMPLATES/                  # Reusable BIM/CAD templates
├── 10_MASTER_MODELS/              # Master coordination models (IFC)
├── 20_DISCIPLINE_MODELS/          # Discipline-specific models
│   ├── ARCH/                      # Architecture
│   ├── STR/                       # Structure
│   ├── MEP/                       # Mechanical, Electrical, Plumbing
│   └── IT/                        # IT infrastructure (racks, cabling)
├── 30_COORDINATION_MODELS/        # Coordination models (Navisworks, etc.)
├── 40_ANALYSIS_EXPORTS/           # Analysis exports
│   ├── CFD/                       # Computational Fluid Dynamics
│   ├── FEA/                       # Finite Element Analysis
│   └── ENERGY/                    # Energy analysis
├── 50_DELIVERABLES/               # Client/stakeholder deliverables
│   ├── VIEW_ONLY/                 # View-only formats (glTF, 3D PDF)
│   └── CLIENT_ISSUED/             # Official client-issued packages
└── 99_ARCHIVE/                    # Archived/superseded models
```

---

## File Naming Convention

All BIM/CAD models follow the pattern:

```
02-00-04-<DISCIPLINE>-<FACILITY>-<SYSTEM>-LOD<nnn>-R<nn>.<ext>
```

Where:
- `02-00-04` = ATA chapter and design folder
- `DISCIPLINE` = ARCH, STR, MEP, IT, COORD, etc.
- `FACILITY` = OPSCTR (Operations Center), DATACENTER, etc.
- `SYSTEM` = Specific system or component
- `LOD<nnn>` = Level of Development (LOD100-LOD500)
- `R<nn>` = Revision number (R01, R02, etc.)
- `ext` = File extension (.rvt, .ifc, .dwg, .nwc, etc.)

### Examples

- `02-00-04-ARCH-OPSCTR-L1-LOD300-R01.rvt` - Architecture, Operations Center Level 1, LOD300
- `02-00-04-MEP-OPSCTR-HVAC-LOD300-R01.rvt` - MEP HVAC system
- `02-00-04-IT-OPSCTR-RACKS-LOD300-R01.rvt` - IT infrastructure racks
- `02-00-04-OPSCTR_Master.ifc` - Master coordination model (IFC format)

---

## Level of Development (LOD) Guidelines

| LOD | Description | Typical Use |
|-----|-------------|-------------|
| LOD 100 | Conceptual | Early concept, massing studies |
| LOD 200 | Approximate geometry | Schematic design |
| LOD 300 | Precise geometry | Design development, coordination |
| LOD 350 | Coordination | Detailed coordination with other disciplines |
| LOD 400 | Fabrication | Construction documentation |
| LOD 500 | As-built | Facility management, as-built record |

---

## Usage Guidelines

### Adding a New BIM/CAD Model

1. **Place model** in appropriate discipline folder under `20_DISCIPLINE_MODELS/`
2. **Follow naming convention** strictly
3. **Update CHANGELOG.md** with revision entry
4. **Fill metadata template** (`02-00-04-BIM_Metadata_Template.xlsx`)
5. **Generate IFC export** to `10_MASTER_MODELS/` if master model
6. **Create coordination model** in `30_COORDINATION_MODELS/` for clash detection

### Model Coordination Workflow

1. Discipline teams work in `20_DISCIPLINE_MODELS/`
2. Export to IFC and place in `10_MASTER_MODELS/`
3. Coordination lead creates Navisworks model in `30_COORDINATION_MODELS/`
4. Run clash detection and coordination reviews
5. Resolve clashes in discipline models
6. Iterate until coordination complete

### Analysis Exports

When performing specialized analysis:
- Export CFD meshes to `40_ANALYSIS_EXPORTS/CFD/`
- Export FEA models to `40_ANALYSIS_EXPORTS/FEA/`
- Export energy models to `40_ANALYSIS_EXPORTS/ENERGY/`

### Deliverables

Client-facing deliverables go to `50_DELIVERABLES/`:
- View-only 3D models (glTF, 3D PDF) → `VIEW_ONLY/`
- Official packages → `CLIENT_ISSUED/`

---

## Related Documentation

- [INSTALLATIONS README](../README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)
- BIM Execution Plan (BEP) - see project documentation
- Discipline Modeling Standards - see project documentation

---

**Last Updated:** 2025-11-14  
**Owner:** AMPEL360 BIM/CAD Team
