# BIM_CAD_MODELS / 10_MASTER_MODELS

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / BIM_CAD_MODELS / 10_MASTER_MODELS  
**Purpose:** Federated master models - the single source of truth for each installation/location

---

## Contents

This folder contains the **master/federated models** that combine all discipline models into a single coordinated "truth" for each installation location. These are the top-level models used for coordination, clash detection, and client deliverables.

---

## Structure

```
10_MASTER_MODELS/
├── README.md                      # This file
├── 02-00-04-BIM_Master_Index.csv # Master model inventory
├── OPSCTR/                        # Operations Center master models
│   ├── <master model files>
│   └── EXPORTS/
│       ├── IFC/                   # IFC exports for coordination
│       └── VIEW_ONLY/             # glTF, 3D PDF for viewing
├── DATACENTER/                    # Data Center master models
│   ├── <master model files>
│   └── EXPORTS/
│       ├── IFC/
│       └── VIEW_ONLY/
├── H2ROOM/                        # H2 Fuel Room master models
│   ├── <master model files>
│   └── EXPORTS/
│       ├── IFC/
│       └── VIEW_ONLY/
├── GSE_AREA/                      # Ground Support Equipment area
│   ├── <master model files>
│   └── EXPORTS/
│       ├── IFC/
│       └── VIEW_ONLY/
└── 99_ARCHIVE/                    # Archived master models
```

---

## Purpose of Master Models

**Master models** serve as:

1. **Single Source of Truth** - One coordinated model per location combining all disciplines
2. **Coordination Platform** - Where discipline models are federated for clash detection
3. **Client Deliverables** - Source for IFC and view-only exports
4. **As-Built Records** - Final as-built coordination models
5. **Design Reviews** - Comprehensive view of entire installation

**Key principle:** Master models **link/reference** discipline models, they don't contain native geometry.

---

## Location-Based Organization

### OPSCTR/ (Operations Center)

Master models for operations control center facilities:

**Model progression:**
- Concept (LOD200) - Early massing and space planning
- Design (LOD300) - Detailed design coordination
- Design (LOD350) - Pre-construction coordination
- As-Built (LOD400) - Final as-built record

**Typical files:**
- `02-00-04-MSTR-OPSCTR-Design-LOD300-R01.rvt`
- `02-00-04-MSTR-OPSCTR-Design-LOD350-R02.rvt`
- `02-00-04-MSTR-OPSCTR-AsBuilt-LOD400-R00.rvt`

**EXPORTS/IFC/:**
- `02-00-04-MSTR-OPSCTR-Design-LOD300-R02.ifc`
- `02-00-04-MSTR-OPSCTR-AsBuilt-LOD400-R00.ifc`

**EXPORTS/VIEW_ONLY/:**
- `02-00-04-MSTR-OPSCTR-3D_ViewOnly-R02.gltf`
- `02-00-04-MSTR-OPSCTR-3D_PDF-R02.pdf`

### DATACENTER/ (Data Center)

Master models for data center installations:

**Typical files:**
- `02-00-04-MSTR-DATACENTER-Design-LOD300-R01.rvt`
- `02-00-04-MSTR-DATACENTER-AsBuilt-LOD400-R00.rvt`

**Focus areas:**
- Server rack layouts
- Cooling systems
- Power distribution
- Cable management
- Access control

### H2ROOM/ (Hydrogen Fuel Room)

Master models for H2 fuel system installations (if applicable):

**Typical files:**
- `02-00-04-MSTR-H2ROOM-Design-LOD300-R01.rvt`
- `02-00-04-MSTR-H2ROOM-AsBuilt-LOD400-R00.rvt`

**Focus areas:**
- H2 storage systems
- Pressure vessels
- Piping and valves
- Safety systems
- Ventilation

### GSE_AREA/ (Ground Support Equipment Area)

Master models for GSE information and storage areas:

**Typical files:**
- `02-00-04-MSTR-GSE_AREA-Design-LOD300-R01.rvt`
- `02-00-04-MSTR-GSE_AREA-AsBuilt-LOD400-R00.rvt`

**Focus areas:**
- Equipment storage
- Information kiosks
- Charging stations
- Maintenance areas

---

## File Naming Convention

Master models follow the pattern:

```
02-00-04-MSTR-<LOCATION>-<PHASE>-LOD<nnn>-R<nn>.<ext>
```

Where:
- `02-00-04` = ATA chapter and design folder
- `MSTR` = Master model identifier
- `LOCATION` = OPSCTR, DATACENTER, H2ROOM, GSE_AREA
- `PHASE` = Concept, Design, AsBuilt
- `LOD<nnn>` = Level of Development (LOD200-LOD400)
- `R<nn>` = Revision number
- `ext` = File extension (.rvt, .ifc, .gltf, .pdf)

### Examples

**Master Models:**
- `02-00-04-MSTR-OPSCTR-Design-LOD300-R01.rvt`
- `02-00-04-MSTR-DATACENTER-AsBuilt-LOD400-R00.rvt`

**IFC Exports:**
- `02-00-04-MSTR-OPSCTR-Design-LOD300-R02.ifc`
- `02-00-04-MSTR-DATACENTER-Design-LOD300-R01.ifc`

**View-Only Exports:**
- `02-00-04-MSTR-OPSCTR-3D_ViewOnly-R02.gltf`
- `02-00-04-MSTR-OPSCTR-3D_PDF-R02.pdf`

---

## Usage Guidelines

### Creating a Master Model

1. **Start with template** from `05_TEMPLATES/`
2. **Link discipline models** from `20_DISCIPLINE_MODELS/`:
   - ARCH models
   - STR models
   - MEP models
   - IT models
3. **Configure views** for coordination
4. **Set up worksets** (if using Revit)
5. **Name following convention**
6. **Save in appropriate location folder**

### Updating a Master Model

1. **Reload linked models** to get latest discipline updates
2. **Review for clashes** using coordination tools
3. **Document issues** in clash report
4. **Increment revision** if significant changes
5. **Export IFC** if needed for coordination
6. **Update index file**

### Federation Workflow

```
Discipline Models (20_DISCIPLINE_MODELS/)
    ↓ [Link into Master]
Master Model (10_MASTER_MODELS/)
    ↓ [Run Clash Detection]
Coordination Model (30_COORDINATION_MODELS/)
    ↓ [Generate Reports]
Clash Reports & RFIs
    ↓ [Resolve Issues]
Updated Discipline Models
```

### Export Standards

**IFC Exports:**
- Export from master model using IFC 2x3 or IFC 4
- Include all disciplines
- Maintain coordinate system
- Include properties and classifications
- Store in `EXPORTS/IFC/`

**View-Only Exports:**
- glTF format for web viewers
- 3D PDF for offline viewing
- Include basic metadata
- Optimize file size
- Store in `EXPORTS/VIEW_ONLY/`

---

## Level of Development (LOD)

### LOD200 - Concept

- Massing and space planning
- Conceptual design
- Early coordination
- Not for construction

### LOD300 - Design

- Detailed design coordination
- Sufficient for coordination and clash detection
- Basis for construction documents
- Most common for master models

### LOD350 - Pre-Construction

- Detailed coordination
- Fabrication-ready information
- Pre-construction coordination
- Detailed clash resolution

### LOD400 - As-Built

- As-built record
- Fabrication and installation verification
- Final coordination model
- Facility management handover

---

## Coordination Checklist

Before publishing a master model:

✅ All discipline models linked correctly  
✅ Coordinate system aligned  
✅ Levels match across disciplines  
✅ No missing links  
✅ Views configured for coordination  
✅ Worksets organized (if Revit)  
✅ File size optimized  
✅ Metadata complete  
✅ Clash detection run  
✅ Index file updated  

---

## Quality Standards

### Model Quality

- **No warnings** related to linked models
- **Coordinate consistency** across all disciplines
- **Level alignment** verified
- **Grid alignment** verified
- **Performance optimized** (file size, load time)

### Documentation

- **Change log** maintained for each revision
- **Clash reports** generated and tracked
- **RFIs** linked to clash issues
- **Approval records** documented

---

## Related Documentation

- [BIM_CAD_MODELS 00_ADMIN README](../00_ADMIN/README.md)
- [20_DISCIPLINE_MODELS README](../20_DISCIPLINE_MODELS/README.md)
- [30_COORDINATION_MODELS README](../30_COORDINATION_MODELS/README.md)
- [INSTALLATIONS README](../../README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)
- BIM Execution Plan (BEP) - see project documentation

---

**Last Updated:** 2025-11-15  
**Owner:** AMPEL360 BIM Coordination Team
