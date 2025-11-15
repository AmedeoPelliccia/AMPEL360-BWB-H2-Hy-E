# PARAMETER_SETS

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / BIM_CAD_MODELS / 05_TEMPLATES / PARAMETER_SETS  
**Purpose:** The "brain" of BIM standards - parameters, views, filters, and export configurations

---

## Purpose

Parameter sets define **how BIM models are organized, viewed, and exported**. They ensure consistency across all projects by standardizing:
- Custom parameters (shared parameters)
- View templates and configurations
- Filters and graphic overrides
- Browser organization schemes
- Export settings for IFC, DWG, etc.

This is the **control center** for BIM standards - get this right, and everything else falls into place.

---

## Structure

```
PARAMETER_SETS/
├── README.md (this file)
├── 02-00-04-BIM_ParameterSets_Index.csv
├── SHARED_PARAMETERS/          # Shared parameter definition files
├── VIEW_TEMPLATES/             # View template configuration files
├── FILTERS_AND_OVERRIDES/      # View filters and graphic overrides
├── BROWSER_ORGANIZATION/       # Browser organization schemes
├── EXPORT_SETTINGS/            # IFC, DWG, and other export configs
└── 99_ARCHIVE/                 # Archived parameter sets
```

---

## Parameter Set Categories

### SHARED_PARAMETERS/

Shared parameter definition files (Revit .txt format):

**Purpose:** Define custom parameters that can be shared across all models, families, and projects.

**Parameter files:**
- Core parameters (project-wide)
- Discipline-specific parameters (IT, MEP, ARCH)
- Asset tracking parameters
- Coordination parameters

**Typical files:**
- `02-00-04-TPL-BIM-SharedParameters-Core-R01.txt`
- `02-00-04-TPL-BIM-SharedParameters-IT-R01.txt`
- `02-00-04-TPL-BIM-SharedParameters-MEP-R01.txt`
- `02-00-04-TPL-BIM-SharedParameters-AssetTracking-R01.txt`

**Core shared parameters:**
- Project Information (Project Name, Number, Phase, LOD)
- Asset Identification (Asset ID, Location Code, System Code)
- Coordination (Clash Status, RFI Number, Submittal Number)
- Installation (Install Date, Installer, Warranty Expiration)
- Operations (Manufacturer, Model, Serial Number, Barcode)

**Discipline-specific parameters:**
- **IT:** Rack Unit Position, Network Port, MAC Address, IP Address
- **MEP:** Circuit Number, Panel Name, Voltage, Phase, BTU Output
- **ARCH:** Fire Rating, Acoustic Rating, Finish Code

### VIEW_TEMPLATES/

View template configuration files:

**Purpose:** Standardize how views look across all models - visibility, graphics, filters, scale, detail level.

**Template categories:**
- Coordination views (clash detection, multi-discipline review)
- Documentation views (construction documents, details)
- 3D review views (client presentations, design review)
- Analysis views (energy, clash, quantity takeoff)

**Typical files:**
- `02-00-04-TPL-BIM-ViewTemplates-Coordination-R01.rvt`
- `02-00-04-TPL-BIM-ViewTemplates-Documentation-R01.rvt`
- `02-00-04-TPL-BIM-ViewTemplates-3DReview-R01.rvt`
- `02-00-04-TPL-BIM-ViewTemplates-Analysis-R01.rvt`

**Coordination view templates:**
- Multi-discipline overlay views
- Clash detection views
- System isolation views
- Discipline-specific coordination

**Documentation view templates:**
- Floor plans (by LOD)
- Reflected ceiling plans
- Sections and elevations
- Detail views
- Schedule templates

**3D view templates:**
- Shaded with edges
- Realistic rendering
- Hidden line
- Transparent discipline views

### FILTERS_AND_OVERRIDES/

View filters and graphic override schemes:

**Purpose:** Define how elements are colored, patterned, and highlighted in views based on parameters.

**Filter categories:**
- Discipline filters (color by ARCH, MEP, IT, STR)
- System filters (color by system type)
- Status filters (existing, new, demo, temporary)
- LOD filters (color by level of development)
- Phase filters (phase-based graphics)

**Typical files:**
- `02-00-04-TPL-BIM-ViewFilters-Disciplines-R01.rvt`
- `02-00-04-TPL-BIM-ViewFilters-Systems-R01.rvt`
- `02-00-04-TPL-BIM-ViewFilters-Status-R01.rvt`
- `02-00-04-TPL-BIM-ViewFilters-LOD-R01.rvt`

**Standard color schemes:**
- **Discipline colors:**
  - ARCH: Gray
  - STR: Brown
  - MEP-M: Blue
  - MEP-E: Red
  - MEP-P: Green
  - IT: Orange

### BROWSER_ORGANIZATION/

Project browser organization schemes:

**Purpose:** Define how views, sheets, and schedules are organized in the project browser.

**Organization schemes:**
- By discipline (ARCH, MEP, IT, STR)
- By location (OPSCTR, DATACENTER, H2ROOM, GSE_AREA)
- By system (HVAC, Electrical, IT Network, Fire Protection)
- By level (L1, L2, etc.)

**Typical files:**
- `02-00-04-TPL-BIM-BrowserOrganization-ByDiscipline-R01.rvt`
- `02-00-04-TPL-BIM-BrowserOrganization-ByLocation-R01.rvt`
- `02-00-04-TPL-BIM-BrowserOrganization-BySystem-R01.rvt`

**Browser organization benefits:**
- Faster navigation
- Consistent structure across projects
- Easier for team members to find views
- Supports coordination workflows

### EXPORT_SETTINGS/

Export configuration files for various formats:

**Purpose:** Standardize how BIM models are exported to IFC, DWG, and other formats.

**Export types:**
- IFC export (coordination, as-built)
- DWG export (2D documentation)
- NWC export (Navisworks coordination)
- FBX export (visualization)

**Typical files:**
- `02-00-04-TPL-BIM-IFC_ExportSettings-R01.rvt`
- `02-00-04-TPL-BIM-DWG_ExportSettings-R01.rvt`
- `02-00-04-TPL-BIM-NWC_ExportSettings-R01.rvt`

**IFC export settings:**
- IFC version (2x3 Coordination View 2.0, IFC4)
- Coordinate base (project base point, survey point)
- Property sets to include
- Classification systems (Uniclass, OmniClass)
- Level of detail

**DWG export settings:**
- Layer naming convention
- Line weights and colors
- Scale and units
- Coordinate system
- View range settings

---

## File Naming Convention

Parameter set files follow the pattern:

```
02-00-04-TPL-BIM-<Type>-<Description>-R<nn>.<ext>
```

Where:
- `02-00-04` = ATA chapter and design folder
- `TPL` = Template identifier
- `BIM` = BIM/CAD category
- `Type` = SharedParameters, ViewTemplates, ViewFilters, BrowserOrganization, IFC_ExportSettings, etc.
- `Description` = Specific description (Core, Coordination, ByDiscipline, etc.)
- `R<nn>` = Revision number
- `ext` = File extension (`.txt` for shared parameters, `.rvt` for Revit settings)

---

## Using Parameter Sets

### Loading Shared Parameters

**In Revit:**
1. Manage tab → Shared Parameters
2. Browse to shared parameter file
3. Load desired parameter groups
4. Add parameters to families or project

**Best practice:** Load at project startup, keep synced across team

### Applying View Templates

**In Revit:**
1. Open a view
2. Properties palette → View Template
3. Select appropriate template from library
4. Apply template

**Workflow:** 
- Apply coordination templates for coordination views
- Apply documentation templates for construction documents
- Apply 3D templates for presentations

### Using Filters

Filters are typically embedded in view templates, but can be applied individually:
1. View → Visibility/Graphics → Filters tab
2. Add desired filters
3. Set visibility and graphic overrides

### Setting Browser Organization

**In Revit:**
1. View tab → User Interface → Browser Organization
2. Select appropriate organization scheme
3. Apply to project

---

## Parameter Standards

### Shared Parameter Guidelines

**Naming conventions:**
- Use clear, descriptive names
- Start with category (IT_, MEP_, ARCH_)
- Use underscores, not spaces
- Example: `IT_RackUnitPosition`, `MEP_CircuitNumber`

**Parameter types:**
- Use appropriate data type (Text, Integer, Number, Yes/No, URL)
- Set units where applicable
- Make instance vs. type parameters appropriately

**Grouping:**
- Group related parameters together
- Use standard group names (Project Information, Asset Information, etc.)

### View Template Standards

**Template naming:**
- Include purpose (Coordination, Documentation, 3D Review)
- Include discipline if applicable
- Example: `CD-ARCH-Floor Plan-LOD300`, `3D-Coordination-MEP`

**Template settings:**
- Set appropriate detail level
- Configure visibility/graphics overrides
- Set scale and display options
- Include view-specific filters

---

## Quality Standards

Before adding parameter set to library:

✅ Parameter names clear and unambiguous  
✅ Data types appropriate  
✅ Units set correctly  
✅ No duplicate parameters  
✅ Tested in actual project  
✅ Documentation complete  
✅ Compatible with existing parameters  
✅ Index file updated  
✅ Version controlled  

---

## Index File

**File:** `02-00-04-BIM_ParameterSets_Index.csv`

Track all parameter sets:

```csv
File_Name,Type,Description,Version,Date_Updated,Status
02-00-04-TPL-BIM-SharedParameters-Core-R01.txt,SHARED_PARAMETERS,Core project parameters,R01,2025-01-15,Active
02-00-04-TPL-BIM-ViewTemplates-Coordination-R01.rvt,VIEW_TEMPLATES,Coordination view templates,R01,2025-01-15,Active
02-00-04-TPL-BIM-IFC_ExportSettings-R01.rvt,EXPORT_SETTINGS,IFC export configuration,R01,2025-01-15,Active
```

---

## Parameter Set Maintenance

### Version Control

- **All parameter sets** must be version controlled
- **Shared parameters** are especially critical - changes affect all projects
- **Document changes** in CHANGELOG
- **Test thoroughly** before releasing updates
- **Communicate changes** to all teams

### Update Process

1. **Identify need** for new parameter or view template
2. **Draft proposal** with clear definition
3. **Review with BIM team** and stakeholders
4. **Test in pilot project**
5. **Document** usage and examples
6. **Release** with version number increment
7. **Notify teams** of update
8. **Archive** previous version

---

## Related Documentation

- [05_TEMPLATES README](../README.md)
- [BIM_CAD_MODELS 00_ADMIN README](../../00_ADMIN/README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)
- BIM Execution Plan (BEP) - see project documentation
- BIM Standards Manual - see project documentation

---

**Last Updated:** 2025-11-15  
**Owner:** AMPEL360 BIM Standards Team
