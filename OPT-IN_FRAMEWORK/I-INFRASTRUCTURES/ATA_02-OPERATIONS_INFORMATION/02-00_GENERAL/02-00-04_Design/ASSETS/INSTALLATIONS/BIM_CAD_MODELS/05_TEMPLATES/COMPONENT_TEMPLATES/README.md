# COMPONENT_TEMPLATES

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / BIM_CAD_MODELS / 05_TEMPLATES / COMPONENT_TEMPLATES  
**Purpose:** Reusable BIM component families and blocks - the "Lego bin" of BIM modeling

---

## Purpose

Component templates are the smallest reusable elements in BIM modeling. They represent individual products, fixtures, fittings, and accessories that can be placed multiple times across different projects and locations.

Think of this as your **component library** - standardized, parameterized families that ensure consistency and speed up modeling.

---

## Structure

```
COMPONENT_TEMPLATES/
├── README.md (this file)
├── 02-00-04-BIM_Component_TPL_Index.csv
├── CABLE_MANAGEMENT/           # Cable trays, ladders, ducts
├── POWER_AND_OUTLETS/          # Floor boxes, outlets, PDUs
├── RACK_AND_CONSOLE_ACCESSORIES/ # Rack panels, monitor arms, trays
├── SAFETY_AND_SIGNAGE/         # Safety signs, floor markings, emergency
└── 99_ARCHIVE/                 # Archived component templates
```

---

## Component Categories

### CABLE_MANAGEMENT/

Cable pathway components for structured cabling systems:

**Components:**
- Cable ladders (various widths and heights)
- Overhead trays (perforated, solid, wire mesh)
- Floor ducts and pathways
- Cable tray fittings (elbows, tees, crosses)
- Conduit and fittings
- Cable supports and hangers

**Typical files:**
- `02-00-04-TPL-BIM-CableLadder-LOD300-R01.rfa`
- `02-00-04-TPL-BIM-OverheadTray-LOD300-R01.rfa`
- `02-00-04-TPL-BIM-FloorDuct-LOD300-R01.rfa`
- `02-00-04-TPL-BIM-CableTray_Elbow-LOD300-R01.rfa`

**Parameters to include:**
- Width, height, length
- Material (steel, aluminum, fiberglass)
- Load capacity
- Finish (galvanized, powder coat, etc.)
- Manufacturer, model number

### POWER_AND_OUTLETS/

Power distribution components for facilities:

**Components:**
- Floor boxes (power, data, combo)
- Technical outlets (isolated ground, hospital grade)
- Rack-mounted PDUs
- Power strips
- Transformers (small equipment transformers)
- UPS units (rack-mount and standalone)

**Typical files:**
- `02-00-04-TPL-BIM-FloorBox-LOD300-R01.rfa`
- `02-00-04-TPL-BIM-TechnicalOutlet-LOD300-R01.rfa`
- `02-00-04-TPL-BIM-PDU_RackMount-LOD300-R01.rfa`
- `02-00-04-TPL-BIM-IsolatedGround_Outlet-LOD300-R01.rfa`

**Parameters to include:**
- Voltage, amperage, phases
- Number of outlets/receptacles
- NEMA configuration
- Mounting type (floor, wall, rack)
- Circuit protection features

### RACK_AND_CONSOLE_ACCESSORIES/

Equipment rack and console accessories:

**Components:**
- Rack blank panels (filler panels)
- Monitor arms and mounts
- Keyboard trays
- Cable management accessories (vertical, horizontal)
- Rack shelves
- Rack drawers
- Equipment slides
- Fan trays

**Typical files:**
- `02-00-04-TPL-BIM-RackBlankPanel-LOD300-R01.rfa`
- `02-00-04-TPL-BIM-MonitorArm-LOD300-R01.rfa`
- `02-00-04-TPL-BIM-KeyboardTray-LOD300-R01.rfa`
- `02-00-04-TPL-BIM-CableMgmt_Vertical-LOD300-R01.rfa`

**Parameters to include:**
- Rack unit (U) size
- Weight capacity
- Adjustment range
- Mounting style
- Material and finish

### SAFETY_AND_SIGNAGE/

Safety equipment and signage components:

**Components:**
- Safety signs (emergency exit, fire equipment, warnings)
- Floor markings and striping
- Emergency buttons (E-stop, EPO)
- Fire extinguisher cabinets
- First aid stations
- Eyewash/safety shower stations
- Safety barriers and railings

**Typical files:**
- `02-00-04-TPL-BIM-SafetySign-LOD200-R01.rfa`
- `02-00-04-TPL-BIM-FloorMarking-LOD200-R01.rfa`
- `02-00-04-TPL-BIM-EmergencyButton-LOD300-R01.rfa`
- `02-00-04-TPL-BIM-FireExtinguisherCabinet-LOD300-R01.rfa`

**Parameters to include:**
- Sign size and orientation
- Text content (editable)
- Mounting height
- Material (metal, plastic, vinyl)
- Illumination (if applicable)

---

## File Naming Convention

Component templates follow the pattern:

```
02-00-04-TPL-BIM-<ComponentType>-LOD<nnn>-R<nn>.rfa
```

Where:
- `02-00-04` = ATA chapter and design folder
- `TPL` = Template identifier
- `BIM` = BIM/CAD category
- `ComponentType` = Descriptive component name
- `LOD<nnn>` = Level of Development (typically LOD300 for components)
- `R<nn>` = Revision number
- `.rfa` = Revit family file (or `.dwg` for AutoCAD blocks)

---

## Component Creation Guidelines

### Family/Block Standards

**For Revit Families (.rfa):**
- Use appropriate family template
- Include shared parameters (from PARAMETER_SETS)
- Define type parameters for common variants
- Include multiple level of detail representations
- Test in project environment before finalizing
- Include manufacturer information
- Add URL for product specs (if available)

**For AutoCAD Blocks (.dwg):**
- Use standard layer naming
- Include attribute definitions
- Provide multiple scale representations
- Use standard insertion point
- Test insertion and scaling

### Parameterization Best Practices

**Essential parameters:**
- Geometry (width, height, depth, length)
- Material/finish
- Manufacturer and model
- Weight (for structural coordination)
- Power requirements (if applicable)
- Heat output (for cooling calculations)

**Optional parameters:**
- Color/appearance
- Mounting options
- Accessories and options
- Installation notes

### LOD for Components

Most component templates should be **LOD300**:
- Generic representation with accurate dimensions
- Sufficient detail for coordination
- Not over-modeled (avoid excessive detail)
- Fast to load and place

**LOD200** for:
- Signage and markings (simple 2D representations)
- Placeholders during early design

**LOD350+** for:
- Fabrication-critical components
- Custom-manufactured items

---

## Using Component Templates

### Placement Workflow

1. **Select component** from appropriate category folder
2. **Load into project** (Revit: Load Family, AutoCAD: Insert Block)
3. **Select appropriate type** from family types
4. **Place in model** at correct location
5. **Adjust parameters** if needed (size, finish, etc.)
6. **Tag and annotate** per project standards

### Customization

**When to customize:**
- Project-specific requirements
- Custom equipment not in library
- Manufacturer-specific models

**How to customize:**
1. Copy template to project folder
2. Rename with project-specific name
3. Modify parameters and geometry
4. Save as new family
5. Consider contributing back to template library if useful for other projects

---

## Component Library Management

### Adding New Components

1. **Identify need** - recurring component across multiple projects
2. **Select base template** (or create from scratch)
3. **Parameterize properly** - include all relevant parameters
4. **Test thoroughly** - place in test project, verify behavior
5. **Document** - add to index file
6. **Categorize** - place in appropriate subfolder
7. **Commit** - add to version control with clear description

### Quality Standards

Before adding component to library:

✅ Opens without errors or warnings  
✅ Parameters work correctly (no broken formulas)  
✅ Multiple level of detail included  
✅ Appropriate subcategory assigned  
✅ Shared parameters loaded  
✅ Manufacturer information included  
✅ File size optimized (no unnecessary detail)  
✅ Tested in actual project  
✅ Naming convention followed  
✅ Index file updated  

### Maintenance

**Regular maintenance:**
- Quarterly review for outdated components
- Update for new product releases
- Deprecate discontinued products
- Consolidate duplicate components

---

## Index File

**File:** `02-00-04-BIM_Component_TPL_Index.csv`

Track all component templates:

```csv
Component_File,Category,Description,Manufacturer,Model,LOD,Date_Added,Status
02-00-04-TPL-BIM-CableLadder-LOD300-R01.rfa,CABLE_MANAGEMENT,Cable ladder 300mm wide,Generic,N/A,LOD300,2025-01-15,Active
02-00-04-TPL-BIM-FloorBox-LOD300-R01.rfa,POWER_AND_OUTLETS,Floor box 2-gang,Wiremold,RFB4,LOD300,2025-01-15,Active
```

---

## Related Documentation

- [05_TEMPLATES README](../README.md)
- [MODULE_TEMPLATES README](../MODULE_TEMPLATES/README.md)
- [ROOM_TEMPLATES README](../ROOM_TEMPLATES/README.md)
- [BIM_CAD_MODELS 00_ADMIN README](../../00_ADMIN/README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)

---

**Last Updated:** 2025-11-15  
**Owner:** AMPEL360 BIM Component Library Team
