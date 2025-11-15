# BIM_CAD_MODELS / 05_TEMPLATES

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / BIM_CAD_MODELS / 05_TEMPLATES  
**Purpose:** Reusable BIM/CAD templates for consistent model creation

---

## Contents

This folder contains reusable BIM/CAD templates that serve as starting points for all modeling work:

- **ROOM_TEMPLATES/** - Room and space templates (shells, generic rooms)
- **MODULE_TEMPLATES/** - Module-level templates (console modules, rack modules)
- **COMPONENT_TEMPLATES/** - Component families and blocks (cable ladders, floor boxes)
- **PARAMETER_SETS/** - Shared parameters, view templates, browser organization
- **99_ARCHIVE/** - Archived/superseded templates

---

## Structure

```
05_TEMPLATES/
├── README.md                      # This file
├── 02-00-04-BIM_TPL_Index.csv    # Template inventory
├── ROOM_TEMPLATES/                # Room and space templates
├── MODULE_TEMPLATES/              # Module-level templates
├── COMPONENT_TEMPLATES/           # Component families and blocks
├── PARAMETER_SETS/                # Shared parameters and view templates
└── 99_ARCHIVE/                    # Archived templates
```

---

## Template Categories

### ROOM_TEMPLATES/

Generic room and space templates for different facility types:

- Generic room shells (LOD200)
- Operations center room templates
- Data center room templates
- Control room templates
- Equipment room templates

**Typical files:**
- `02-00-04-TPL-BIM-GenericRoom-LOD200-R01.rvt`
- `02-00-04-TPL-BIM-OPSCTR-RoomShell-LOD200-R01.rvt`
- `02-00-04-TPL-BIM-DATACENTER-RoomShell-LOD200-R01.rvt`

**Use:** Starting point for architectural space modeling

### MODULE_TEMPLATES/

Module-level templates for repeatable assemblies:

- Console module templates
- Rack module templates
- Workstation module templates
- Equipment cluster templates

**Typical files:**
- `02-00-04-TPL-BIM-OPSCTR-ConsoleModule-LOD300-R01.rvt`
- `02-00-04-TPL-BIM-DATACENTER-RackModule-LOD300-R01.rvt`
- `02-00-04-TPL-BIM-OPSCTR-WorkstationModule-LOD300-R01.rvt`

**Use:** Creating repeatable equipment layouts and assemblies

### COMPONENT_TEMPLATES/

Component-level families and blocks:

- Cable ladder families
- Floor box families
- Overhead tray families
- Conduit fitting families
- Equipment mounting families
- Power distribution families

**Typical files:**
- `02-00-04-TPL-BIM-CableLadder-LOD300-R01.rfa` (Revit family)
- `02-00-04-TPL-BIM-FloorBox-LOD300-R01.rfa`
- `02-00-04-TPL-BIM-OverheadTray-LOD300-R01.rfa`
- `02-00-04-TPL-BIM-Conduit_Fitting-LOD300-R01.dwg` (AutoCAD block)

**Use:** Library of reusable components for detailed modeling

### PARAMETER_SETS/

Shared parameters and view configuration templates:

- Shared parameter files (Revit)
- View template files
- Browser organization templates
- Project parameter templates
- Family parameter standards

**Typical files:**
- `02-00-04-TPL-BIM-SharedParameters-R01.txt`
- `02-00-04-TPL-BIM-ViewTemplates-R01.rvt`
- `02-00-04-TPL-BIM-BrowserOrganization-R01.rvt`
- `02-00-04-TPL-BIM-ProjectParameters-R01.xlsx`

**Use:** Ensure consistent parameters and views across all models

---

## File Naming Convention

All BIM templates follow the pattern:

```
02-00-04-TPL-BIM-<TYPE>-LOD<nnn>-R<nn>.<ext>
```

Where:
- `02-00-04` = ATA chapter and design folder
- `TPL` = Template identifier
- `BIM` = BIM/CAD category
- `TYPE` = Descriptive type (GenericRoom, ConsoleModule, CableLadder, etc.)
- `LOD<nnn>` = Level of Development (LOD200, LOD300, etc.)
- `R<nn>` = Revision number
- `ext` = File extension (.rvt, .rfa, .dwg, .txt, etc.)

### Examples

**Room Templates:**
- `02-00-04-TPL-BIM-GenericRoom-LOD200-R01.rvt`
- `02-00-04-TPL-BIM-OPSCTR-RoomShell-LOD200-R01.rvt`

**Module Templates:**
- `02-00-04-TPL-BIM-OPSCTR-ConsoleModule-LOD300-R01.rvt`
- `02-00-04-TPL-BIM-DATACENTER-RackModule-LOD300-R01.rvt`

**Component Templates:**
- `02-00-04-TPL-BIM-CableLadder-LOD300-R01.rfa`
- `02-00-04-TPL-BIM-FloorBox-LOD300-R01.rfa`

**Parameter Sets:**
- `02-00-04-TPL-BIM-SharedParameters-R01.txt`
- `02-00-04-TPL-BIM-ViewTemplates-R01.rvt`

---

## Usage Guidelines

### Using a Template

1. **Select appropriate template** from category folder
2. **Copy template** to your working location in 20_DISCIPLINE_MODELS/
3. **Rename** following the discipline model naming convention
4. **Customize** for your specific project/location
5. **Do NOT modify** the original template file

### Creating a New Template

1. **Identify need** - Recurring element that would benefit from standardization
2. **Create template** with best practices embedded
3. **Select appropriate category** folder
4. **Follow naming convention** strictly
5. **Test template** - Have someone else use it to verify
6. **Document usage** in template (embedded notes or readme)
7. **Update index** (`02-00-04-BIM_TPL_Index.csv`)
8. **Commit to repository** with clear description

### Template Standards

**All templates must include:**

- **Correct units** (metric or imperial as per project standard)
- **Standard layers/levels** (per BIM Execution Plan)
- **Shared parameters loaded** (Revit templates)
- **View templates configured** (standard views)
- **Title block configured** (with metadata fields)
- **Default settings** (object styles, line weights, etc.)
- **Minimal content** (template, not example project)

### Template Quality Checklist

Before adding a template to this library:

✅ Verified units and coordinate system  
✅ Standard layers/levels configured  
✅ Shared parameters loaded (if Revit)  
✅ View templates configured  
✅ Title block present with metadata fields  
✅ Default settings appropriate  
✅ No project-specific content  
✅ Template tested by another user  
✅ Documentation included (embedded or readme)  
✅ Index file updated  

---

## Revit-Specific Guidelines

### Shared Parameters

All Revit templates should load the standard shared parameters file:
- `02-00-04-TPL-BIM-SharedParameters-R01.txt`

Key parameter categories:
- Project Information (Project Name, Number, Phase)
- Asset Identification (Asset ID, Location, System)
- Level of Development (LOD, Model Status, Approval Date)
- Coordination (Clash Status, RFI Reference, Submittal Number)

### View Templates

Standard view templates to include:
- Plan views (LOD200, LOD300, LOD400)
- Section views (discipline-specific)
- 3D views (coordination, presentation)
- Schedule templates

### Browser Organization

Standard browser organization:
- By discipline
- By level
- By system
- By LOD

---

## AutoCAD-Specific Guidelines

### Layers

Standard layer naming convention:
- Discipline-specific prefixes (A-, S-, M-, E-, P-, IT-)
- Standard layer naming (per project CAD standards)
- Consistent color and linetype assignments

### Blocks

Component blocks should include:
- Attribute definitions for metadata
- Multiple scale representations
- Annotation blocks with leader lines
- Standard insertion points

---

## Version Control

### Template Versioning

- Templates are versioned using revision numbers (R01, R02, etc.)
- Major changes increment revision
- Document changes in header/properties
- Archive previous versions to 99_ARCHIVE/

### Update Process

1. Make changes to working copy
2. Test thoroughly with actual project
3. Increment revision number
4. Update index file
5. Archive previous version
6. Commit with detailed change description
7. Notify users of template update

---

## Related Documentation

- [BIM_CAD_MODELS 00_ADMIN README](../00_ADMIN/README.md)
- [INSTALLATIONS README](../../README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)
- BIM Execution Plan (BEP) - see project documentation
- CAD Standards Manual - see project documentation

---

**Last Updated:** 2025-11-15  
**Owner:** AMPEL360 BIM Standards Team
