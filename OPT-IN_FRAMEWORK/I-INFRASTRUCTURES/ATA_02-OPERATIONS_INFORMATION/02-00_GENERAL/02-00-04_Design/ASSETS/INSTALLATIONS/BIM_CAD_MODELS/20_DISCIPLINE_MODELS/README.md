# BIM_CAD_MODELS / 20_DISCIPLINE_MODELS

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / BIM_CAD_MODELS / 20_DISCIPLINE_MODELS  
**Purpose:** Discipline-specific BIM models organized by discipline → location

---

## Contents

This folder contains the **workhorse layer** of BIM modeling - the discipline-specific models that are created by individual design teams and later federated into master models. Each discipline maintains its own models organized by location.

---

## Structure

```
20_DISCIPLINE_MODELS/
├── README.md                      # This file
├── 02-00-04-BIM_Discipline_Index.csv  # Discipline model inventory
├── ARCH/                          # Architecture models
│   ├── 00_ADMIN/
│   ├── OPSCTR/
│   ├── DATACENTER/
│   ├── H2ROOM/
│   ├── GSE_AREA/
│   └── 99_ARCHIVE/
├── STR/                           # Structural models
│   ├── 00_ADMIN/
│   ├── OPSCTR/
│   ├── DATACENTER/
│   └── 99_ARCHIVE/
├── MEP/                           # Mechanical, Electrical, Plumbing
│   ├── 00_ADMIN/
│   ├── OPSCTR/
│   ├── DATACENTER/
│   ├── H2ROOM/
│   ├── GSE_AREA/
│   └── 99_ARCHIVE/
├── IT/                            # IT infrastructure (racks, cabling)
│   ├── 00_ADMIN/
│   ├── OPSCTR/
│   ├── DATACENTER/
│   ├── H2ROOM/
│   ├── GSE_AREA/
│   └── 99_ARCHIVE/
├── SAFE/                          # Fire/Safety (optional separate discipline)
│   └── ...
└── 99_ARCHIVE/                    # Cross-discipline archive
```

---

## Organization Pattern

**Discipline → Location → Models**

This organization pattern:
1. Groups models by **discipline team** (who creates/owns them)
2. Subdivides by **location** (where they're installed)
3. Keeps **LOD progression** within each location

### Why Discipline-First?

- **Team ownership** - Each discipline team manages their own folder
- **Concurrent work** - Teams work in parallel without conflicts
- **Clear responsibility** - Obvious who owns each model
- **Standard workflow** - Matches typical design team structure

---

## Discipline Categories

### ARCH/ (Architecture)

Architectural models including:
- Building shells and enclosures
- Interior walls and partitions
- Doors and windows
- Room finishes
- Casework and millwork
- Ceilings

**See:** [ARCH/00_ADMIN/README.md](ARCH/00_ADMIN/README.md)

### STR/ (Structural)

Structural models including:
- Structural framing
- Foundations
- Floor slabs
- Structural supports
- Equipment mounting structures

**Location-specific considerations:**
- OPSCTR: Raised floor systems, structural supports for equipment
- DATACENTER: Heavy load floor structures for server racks

### MEP/ (Mechanical, Electrical, Plumbing)

MEP systems including:
- HVAC systems (heating, cooling, ventilation)
- Electrical power distribution
- Lighting systems
- Plumbing and drainage
- Fire protection systems
- Control systems

**See:** [MEP/00_ADMIN/README.md](MEP/00_ADMIN/README.md)

**Special considerations for H2ROOM:**
- H2 detection and ventilation
- Explosion-proof electrical
- Emergency shutdown systems

### IT/ (IT Infrastructure)

IT and communications infrastructure:
- Server racks and cabinets
- Cable trays and pathways
- Network equipment
- Patch panels
- Fiber optic routing
- Data cabling

**See:** [IT/00_ADMIN/README.md](IT/00_ADMIN/README.md)

**Focus areas:**
- OPSCTR: Console connectivity, control systems
- DATACENTER: High-density rack layouts, hot/cold aisles

### SAFE/ (Fire/Safety) - Optional

Fire and life safety systems (if separated from MEP):
- Fire alarm systems
- Emergency lighting
- Egress paths
- Fire suppression
- Safety signage

---

## File Naming Convention

Discipline models follow the pattern:

```
02-00-04-<DISC>-<LOCATION>-<PHASE>-LOD<nnn>-R<nn>.<ext>
```

Where:
- `02-00-04` = ATA chapter and design folder
- `DISC` = Discipline code (ARCH, STR, MEP, IT, SAFE)
- `LOCATION` = OPSCTR, DATACENTER, H2ROOM, GSE_AREA
- `PHASE` = Concept, Design, AsBuilt
- `LOD<nnn>` = Level of Development (LOD200-LOD400)
- `R<nn>` = Revision number
- `ext` = File extension (.rvt, .dwg, .ifc, etc.)

### Examples by Discipline

**Architecture:**
- `02-00-04-ARCH-OPSCTR-Design-LOD300-R02.rvt`
- `02-00-04-ARCH-DATACENTER-AsBuilt-LOD400-R00.rvt`

**Structural:**
- `02-00-04-STR-OPSCTR-Design-LOD300-R01.rvt`
- `02-00-04-STR-DATACENTER-Design-LOD300-R01.rvt`

**MEP:**
- `02-00-04-MEP-OPSCTR-Design-LOD300-R02.rvt`
- `02-00-04-MEP-H2ROOM-Design-LOD300-R01.rvt`

**IT:**
- `02-00-04-IT-OPSCTR-Design-LOD300-R01.rvt`
- `02-00-04-IT-DATACENTER-Design-LOD300-R01.rvt`

---

## Workflow

### Model Creation Workflow

1. **Start from template** (`05_TEMPLATES/`)
2. **Create discipline model** in appropriate location folder
3. **Follow naming convention** strictly
4. **Model to appropriate LOD** for current phase
5. **Export IFC** when ready for coordination
6. **Link into master model** (`10_MASTER_MODELS/`)
7. **Coordinate with other disciplines**
8. **Resolve clashes** identified in coordination
9. **Update model** and increment revision
10. **Document changes** in discipline CHANGELOG

### Coordination Cycle

```
Discipline Modeling (20_DISCIPLINE_MODELS/)
    ↓
Export to IFC
    ↓
Link into Master Model (10_MASTER_MODELS/)
    ↓
Clash Detection (30_COORDINATION_MODELS/)
    ↓
Identify Issues
    ↓
Resolve in Discipline Models
    ↓
[Repeat cycle]
```

### LOD Progression

**LOD200 → LOD300:**
- Concept to detailed design
- Major milestone, requires review
- Coordinate system must remain consistent

**LOD300 → LOD350:**
- Design to pre-construction
- Add fabrication details
- Resolve all clashes

**LOD350 → LOD400:**
- Pre-construction to as-built
- Verify field conditions
- Update with actual installation

---

## Coordination Requirements

### Inter-Discipline Coordination

Each discipline must coordinate with others:

**ARCH ↔ STR:** 
- Opening locations
- Structural penetrations
- Load-bearing requirements

**ARCH ↔ MEP:**
- Ceiling heights
- Equipment room sizes
- Service penetrations

**MEP ↔ IT:**
- Power requirements
- Cable pathways
- Cooling requirements

**All ↔ SAFE:**
- Egress paths
- Fire rating requirements
- Safety system locations

### Coordination Meetings

Regular coordination meetings should review:
- Clash detection results
- RFI status
- Design changes
- Schedule impacts

---

## Quality Standards

### Model Quality Checklist

Before publishing a discipline model for coordination:

✅ Model opens without errors or warnings  
✅ Coordinate system correct  
✅ Levels match project standard  
✅ Grids match project standard  
✅ LOD appropriate for phase  
✅ No unnecessary detail  
✅ File size optimized  
✅ Metadata complete  
✅ View templates configured  
✅ Export IFC successfully  

### Documentation Requirements

Each discipline model should have:
- **Change log** in discipline CHANGELOG.md
- **Known issues** documented
- **Assumptions** noted
- **Coordination items** tracked

---

## Best Practices

### File Management

- **One model per location** per discipline
- **Regular saves** and backups
- **Clear naming** following convention
- **Archive old versions** to 99_ARCHIVE/

### Modeling Standards

- **Follow BEP** (BIM Execution Plan)
- **Use templates** from 05_TEMPLATES/
- **Shared parameters** consistently
- **View organization** per standards
- **Layer/level naming** per standards

### Collaboration

- **Regular coordination** meetings
- **Clash detection** cycles
- **RFI tracking** and resolution
- **Design change** communication

---

## Related Documentation

- [BIM_CAD_MODELS 00_ADMIN README](../00_ADMIN/README.md)
- [05_TEMPLATES README](../05_TEMPLATES/README.md)
- [10_MASTER_MODELS README](../10_MASTER_MODELS/README.md)
- [ARCH/00_ADMIN/README.md](ARCH/00_ADMIN/README.md)
- [MEP/00_ADMIN/README.md](MEP/00_ADMIN/README.md)
- [IT/00_ADMIN/README.md](IT/00_ADMIN/README.md)
- [INSTALLATIONS README](../../README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)

---

**Last Updated:** 2025-11-15  
**Owner:** AMPEL360 BIM Coordination Team
