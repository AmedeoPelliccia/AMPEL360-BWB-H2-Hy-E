# MODULE_TEMPLATES

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / BIM_CAD_MODELS / 05_TEMPLATES / MODULE_TEMPLATES  
**Purpose:** Repeatable assembly templates - the "building blocks" layer of BIM modeling

---

## Purpose

Module templates are **repeatable assemblies** of multiple components that work together as a functional unit. They're larger than individual components but smaller than complete rooms.

Think of modules as **standardized building blocks** that can be replicated across installations, ensuring consistency and accelerating design.

---

## Structure

```
MODULE_TEMPLATES/
├── README.md (this file)
├── 02-00-04-BIM_Module_TPL_Index.csv
├── OPSCTR_CONSOLES/            # Operations center console modules
├── DATACENTER_RACK_ROWS/       # Data center rack row modules
├── SUPPORT_MODULES/            # UPS, battery, network support modules
├── H2_MONITORING_MODULES/      # H2 monitoring and control modules
└── 99_ARCHIVE/                 # Archived module templates
```

---

## Module Categories

### OPSCTR_CONSOLES/

Operations center console and display modules:

**Modules:**
- Console modules (2-seat, 3-seat, supervisor)
- Video wall segments
- Display arrays
- Control panels
- Supervisor stations
- Briefing area modules

**Typical files:**
- `02-00-04-TPL-BIM-OPSCTR-ConsoleModule-2Seats-LOD300-R01.rvt`
- `02-00-04-TPL-BIM-OPSCTR-ConsoleModule-3Seats-LOD300-R01.rvt`
- `02-00-04-TPL-BIM-OPSCTR-VideoWallSegment-LOD300-R01.rvt`
- `02-00-04-TPL-BIM-OPSCTR-SupervisorStation-LOD300-R01.rvt`

**Module includes:**
- Console furniture/structure
- Integrated monitors and displays
- Keyboard/mouse surfaces
- Cable management (underfloor/overhead)
- Power and data connectivity points
- Lighting (task lighting if applicable)

**Parameters:**
- Number of operator positions
- Console width, depth, height
- Display configuration
- Power requirements
- Cable entry points
- Finish/color options

### DATACENTER_RACK_ROWS/

Data center rack row configurations:

**Modules:**
- Standard rack rows (6, 8, 10 racks)
- Hot aisle containment modules
- Cold aisle containment modules
- Row end modules
- Overhead ladder segments
- Underfloor plenum sections

**Typical files:**
- `02-00-04-TPL-BIM-DATACENTER-RackRow-6Racks-LOD300-R01.rvt`
- `02-00-04-TPL-BIM-DATACENTER-RackRow-10Racks-LOD300-R01.rvt`
- `02-00-04-TPL-BIM-DATACENTER-RowEndModule-LOD300-R01.rvt`
- `02-00-04-TPL-BIM-DATACENTER-HotAisleContainment-LOD300-R01.rvt`

**Module includes:**
- Server racks (standard 42U or 48U)
- Overhead cable ladder
- Underfloor cable tray
- PDU placement
- Aisle containment structure (if applicable)
- Lighting
- Environmental sensors

**Parameters:**
- Number of racks in row
- Rack spacing
- Aisle width (hot aisle, cold aisle)
- Containment type (none, hot, cold)
- Power density per rack
- Cable pathway sizes

### SUPPORT_MODULES/

Support equipment modules:

**Modules:**
- UPS modules (single, redundant)
- Battery cabinet modules
- Network equipment cabinets
- Patch panel arrays
- Equipment distribution areas (EDA)
- Intermediate distribution frames (IDF)

**Typical files:**
- `02-00-04-TPL-BIM-UPS_Module-LOD300-R01.rvt`
- `02-00-04-TPL-BIM-BatteryCabinet_Module-LOD300-R01.rvt`
- `02-00-04-TPL-BIM-NetworkCabinet_Module-LOD300-R01.rvt`
- `02-00-04-TPL-BIM-IDF_Module-LOD300-R01.rvt`

**Module includes:**
- Equipment cabinet/enclosure
- Equipment (UPS, batteries, switches, etc.)
- Associated conduit/cabling
- Grounding connections
- Ventilation (if needed)
- Service clearances

**Parameters:**
- Equipment capacity (kVA for UPS, Ah for batteries)
- Redundancy configuration (N, N+1, 2N)
- Footprint and clearances
- Weight (for structural)
- Heat output (for cooling)

### H2_MONITORING_MODULES/

Hydrogen fuel monitoring and control modules:

**Modules:**
- Monitoring stations
- Alarm panel wall bays
- Sensor arrays
- Control panels
- Emergency shutdown stations

**Typical files:**
- `02-00-04-TPL-BIM-H2ROOM-MonitoringStation-LOD300-R01.rvt`
- `02-00-04-TPL-BIM-H2ROOM-AlarmPanelWallBay-LOD300-R01.rvt`
- `02-00-04-TPL-BIM-H2ROOM-SensorArray-LOD300-R01.rvt`

**Module includes:**
- Control panel enclosures
- Display screens
- Sensor mounting
- Alarm indicators
- Emergency controls
- Communication equipment

**Parameters:**
- Number of sensor points
- Panel size and type
- Explosion-proof rating (if required)
- Power requirements
- Mounting type (wall, standalone)

---

## File Naming Convention

Module templates follow the pattern:

```
02-00-04-TPL-BIM-<LOCATION>-<ModuleType>-<Variant>-LOD<nnn>-R<nn>.rvt
```

Where:
- `02-00-04` = ATA chapter and design folder
- `TPL` = Template identifier
- `BIM` = BIM/CAD category
- `LOCATION` = OPSCTR, DATACENTER, H2ROOM (if location-specific)
- `ModuleType` = Type of module (ConsoleModule, RackRow, UPS_Module, etc.)
- `Variant` = Specific variant (2Seats, 10Racks, etc.)
- `LOD<nnn>` = Level of Development (typically LOD300)
- `R<nn>` = Revision number
- `.rvt` = Revit project file (modules are often projects, not families)

---

## Module Creation Guidelines

### Module Development Process

1. **Define module scope** - What's included/excluded
2. **Select components** - Use components from COMPONENT_TEMPLATES
3. **Arrange components** - Create functional layout
4. **Add connectivity** - Power, data, cooling interfaces
5. **Parameterize** - Make module flexible/reusable
6. **Test** - Place in multiple scenarios
7. **Document** - Usage notes, limitations
8. **Finalize** - Optimize, add to library

### Module vs. Component vs. Room

**Component** (smallest):
- Single item (cable tray, floor box, monitor arm)
- Placed individually
- Example: `CableLadder`, `FloorBox`

**Module** (medium):
- Assembly of multiple components
- Repeated multiple times within a room
- Example: `ConsoleModule-2Seats`, `RackRow-10Racks`

**Room** (largest):
- Complete space with multiple modules
- Entire facility or area
- Example: `OperationsCenter`, `DataCenterRoom`

### Parameterization Strategy

**Required parameters:**
- Overall dimensions (length, width, height)
- Capacity (seats, racks, kVA, etc.)
- Configuration options
- Power requirements
- Cooling requirements
- Weight (for structural coordination)

**Optional parameters:**
- Finish/color variations
- Equipment manufacturer
- Custom options/accessories

### LOD for Modules

**LOD300** (most common):
- Accurate dimensions
- Component placement
- Connectivity shown
- Sufficient for coordination

**LOD350** (fabrication):
- Detailed connections
- Mounting details
- Installation sequences
- Fabrication information

---

## Using Module Templates

### Module Placement Workflow

1. **Select appropriate module** from category folder
2. **Load/link into project** 
3. **Place first instance** at desired location
4. **Copy/array** for multiple instances
5. **Adjust parameters** for each instance if needed
6. **Connect utilities** (power, data, cooling)
7. **Coordinate with other disciplines**

### Module Customization

Modules can be customized by:
- Adjusting parameters (seat count, rack count, etc.)
- Swapping components (different monitors, racks, etc.)
- Adding/removing accessories
- Changing finishes/colors

For major changes, create a project-specific variant and document deviation from standard.

---

## Module Standards

### Quality Checklist

Before adding module to library:

✅ All components properly placed and constrained  
✅ Parameters work correctly across range of values  
✅ Connectivity points clearly defined  
✅ Power/cooling requirements calculated  
✅ Service clearances maintained  
✅ Tested at min/max parameter ranges  
✅ No warnings or errors  
✅ File size optimized  
✅ Documentation complete  
✅ Index file updated  

### Module Documentation

Each module should include:
- Purpose and typical use cases
- Parameter descriptions
- Component list (BOM)
- Power requirements
- Cooling requirements
- Installation notes
- Coordination requirements
- Known limitations

---

## Index File

**File:** `02-00-04-BIM_Module_TPL_Index.csv`

Track all module templates:

```csv
Module_File,Category,Description,Capacity,Power_kW,Cooling_BTU,Date_Added,Status
02-00-04-TPL-BIM-OPSCTR-ConsoleModule-2Seats-LOD300-R01.rvt,OPSCTR_CONSOLES,2-seat operator console,2 positions,1.5,5000,2025-01-15,Active
02-00-04-TPL-BIM-DATACENTER-RackRow-10Racks-LOD300-R01.rvt,DATACENTER_RACK_ROWS,10-rack row with containment,10 racks,100,300000,2025-01-15,Active
```

---

## Module Library Management

### Adding New Modules

1. **Identify pattern** - Recurring assembly across projects
2. **Define standard** - Typical configuration
3. **Build module** - Using component templates
4. **Parameterize** - Make flexible
5. **Test** - Multiple scenarios
6. **Document** - Usage and requirements
7. **Add to library** - Appropriate category folder
8. **Update index** - Add to tracking

### Module Maintenance

- **Quarterly review** - Check for outdated modules
- **Update components** - When component templates change
- **Add variants** - As new needs identified
- **Deprecate** - Remove unused modules
- **Consolidate** - Merge similar modules

---

## Related Documentation

- [05_TEMPLATES README](../README.md)
- [COMPONENT_TEMPLATES README](../COMPONENT_TEMPLATES/README.md)
- [ROOM_TEMPLATES README](../ROOM_TEMPLATES/README.md)
- [20_DISCIPLINE_MODELS README](../../20_DISCIPLINE_MODELS/README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)

---

**Last Updated:** 2025-11-15  
**Owner:** AMPEL360 BIM Module Library Team
