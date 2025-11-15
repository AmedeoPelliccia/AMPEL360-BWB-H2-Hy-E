# IT (IT Infrastructure) - Discipline Models

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / BIM_CAD_MODELS / 20_DISCIPLINE_MODELS / IT  
**Purpose:** IT infrastructure BIM models for all installation locations

---

## Contents

This folder contains IT infrastructure BIM models organized by location. IT models include server racks, network equipment, cable pathways, and data distribution systems.

---

## Structure

```
IT/
├── 00_ADMIN/                      # Administrative files (this folder)
│   ├── README.md                  # This file
│   ├── CHANGELOG.md               # Revision history
│   └── 02-00-04-IT_Index.csv     # Model inventory
├── OPSCTR/                        # Operations Center IT models
├── DATACENTER/                    # Data Center IT models
├── H2ROOM/                        # H2 Fuel Room IT models
├── GSE_AREA/                      # GSE Area IT models
└── 99_ARCHIVE/                    # Archived IT models
```

---

## IT Infrastructure Scope

### What IT Models Include

**Rack Infrastructure:**
- Server racks and cabinets
- Network equipment racks
- Rack PDUs (power distribution units)
- Rack elevations and layouts
- Equipment mounting positions

**Cable Infrastructure:**
- Cable trays and ladders
- Cable pathways (overhead and underfloor)
- Patch panels and termination points
- Fiber optic cable routes
- Copper cable routes
- Cable management systems

**Network Equipment:**
- Core switches and routers
- Edge switches
- Firewall appliances
- Load balancers
- Network storage devices

**Distribution Points:**
- Main distribution frame (MDF)
- Intermediate distribution frames (IDF)
- Telecommunications rooms (TR)
- Equipment distribution areas (EDA)

### What IT DOES NOT Include

- Power distribution to racks → See MEP/
- HVAC for equipment cooling → See MEP/
- Structural support for racks → See STR/
- Room architecture → See ARCH/

---

## Location-Specific Content

### OPSCTR/ (Operations Center)

**Typical files:**
- `02-00-04-IT-OPSCTR-Design-LOD300-R01.rvt`
- `02-00-04-IT-OPSCTR-Design-LOD350-R02.rvt`
- `02-00-04-IT-OPSCTR-AsBuilt-LOD400-R00.rvt`

**Key IT elements:**
- Console network connectivity
- Control system racks
- Display system network infrastructure
- Audio/video distribution equipment
- Operations network switches
- Redundant network paths
- UPS systems (IT-specific)
- Underfloor cable pathways

**Design considerations:**
- Low-latency network paths
- Redundancy for critical systems
- Console connectivity requirements
- Display wall connectivity
- Cable management under raised floor
- Electromagnetic interference (EMI) considerations

### DATACENTER/ (Data Center)

**Typical files:**
- `02-00-04-IT-DATACENTER-Design-LOD300-R01.rvt`
- `02-00-04-IT-DATACENTER-AsBuilt-LOD400-R00.rvt`

**Key IT elements:**
- Server rack rows (hot aisle/cold aisle)
- Network core equipment
- Storage area network (SAN) equipment
- Fiber optic distribution
- Copper distribution (structured cabling)
- Cable ladder systems (overhead)
- Underfloor cable trays
- Patch panel arrays
- Equipment distribution areas

**Design considerations:**
- High-density rack layouts
- Hot aisle/cold aisle configuration
- Cable pathway capacity
- Future expansion planning
- Fiber vs. copper distribution
- Cable management efficiency
- Power density per rack (coordinate with MEP)

### H2ROOM/ (Hydrogen Fuel Room)

**Typical files:**
- `02-00-04-IT-H2ROOM-Design-LOD300-R01.rvt`

**Key IT elements:**
- Monitoring and control racks
- Sensor networks
- Safety system network connectivity
- SCADA equipment
- Intrinsically safe cabling (if required)
- Control panels
- Remote monitoring connections

**Design considerations:**
- Explosion-proof or intrinsically safe equipment (if required)
- Environmental monitoring
- Emergency shutdown system integration
- Remote monitoring capability
- Redundant communication paths

### GSE_AREA/ (Ground Support Equipment Area)

**Typical files:**
- `02-00-04-IT-GSE_AREA-Design-LOD300-R01.rvt`

**Key IT elements:**
- Information kiosk network connections
- Equipment tracking systems
- Charging station network connectivity
- Wi-Fi access point locations
- Outdoor-rated cable pathways
- Security camera network

**Design considerations:**
- Weather-resistant equipment
- Wireless coverage
- Power over Ethernet (PoE) for devices
- Remote management capability

---

## File Naming Convention

```
02-00-04-IT-<LOCATION>-<PHASE>-LOD<nnn>-R<nn>.rvt
```

Where:
- `IT` = IT Infrastructure discipline
- `LOCATION` = OPSCTR, DATACENTER, H2ROOM, GSE_AREA
- `PHASE` = Design, AsBuilt
- `LOD<nnn>` = LOD300, LOD350, LOD400
- `R<nn>` = Revision number

---

## IT Modeling Standards

### LOD Requirements

**LOD300 - Design:**
- Rack locations and sizes
- Cable tray and ladder routes
- Equipment locations (generic)
- Pathway capacities
- Connection points

**LOD350 - Pre-Construction:**
- Specific equipment models
- Detailed rack elevations
- Cable routing detail
- Mounting details
- Connector types

**LOD400 - As-Built:**
- As-installed equipment
- Actual cable routes
- Port assignments
- Serial numbers (if required)
- Field modifications

### IT-Specific Modeling Guidelines

**Racks:**
- Model as 3D objects with correct dimensions
- Include front/rear doors
- Show internal equipment elevations
- Label with rack IDs
- Include weight data for structural coordination

**Cable Trays:**
- Model actual tray sizes and types
- Show fill capacity
- Indicate cable types (fiber, copper, power)
- Maintain proper separation from power cables
- Coordinate with ARCH for ceiling heights

**Equipment:**
- Use manufacturer families when available
- Include accurate dimensions and weights
- Show connection points
- Include heat output (for MEP coordination)
- Model airflow direction (for cooling coordination)

### Revit Standards (if using Revit)

**Worksets:**
- Racks and Cabinets
- Cable Trays and Pathways
- Network Equipment
- Terminations and Patch Panels
- Annotation
- Links

**Families:**
- Use standard IT equipment families from library
- Create new families for specialized equipment
- Include parameters for manufacturer, model, specifications
- Include electrical and thermal properties

---

## Coordination Points

**With MEP (Electrical):**
- Power requirements for racks
- Circuit assignments
- UPS systems
- Emergency power circuits
- Grounding and bonding

**With MEP (Mechanical):**
- Equipment heat loads
- Cooling requirements
- Hot aisle/cold aisle coordination
- Airflow requirements

**With ARCH:**
- Raised floor depths for cable routing
- Cable entry points
- Equipment room sizes
- Access requirements
- Equipment weight (for structural coordination)

**With MEP (Fire Protection):**
- Clean agent suppression coordination
- Pre-action sprinkler coordination

---

## Quality Checklist

Before publishing an IT model:

✅ All racks properly located and labeled  
✅ Cable tray routes complete and coordinated  
✅ Equipment clearances verified  
✅ Power requirements documented (for MEP)  
✅ Cooling requirements documented (for MEP)  
✅ Cable pathway capacities calculated  
✅ Redundant paths identified  
✅ Future expansion space allocated  
✅ Model opens without errors  
✅ Coordinate system matches other disciplines  

---

## Common Issues and Solutions

**Issue:** Insufficient cable tray capacity  
**Solution:** Calculate fill ratios early, oversize for future growth

**Issue:** Rack placement conflicts with structural columns  
**Solution:** Coordinate rack layout with structural grid early

**Issue:** Inadequate cooling for high-density racks  
**Solution:** Work with MEP team to model hot/cold aisle containment

**Issue:** Cable pathway conflicts with MEP systems  
**Solution:** Establish routing hierarchy (coordinate with MEP early)

**Issue:** Insufficient clearance for equipment access  
**Solution:** Model door swing clearances, service clearances

---

## Related Documentation

- [20_DISCIPLINE_MODELS README](../README.md)
- [BIM_CAD_MODELS 00_ADMIN README](../../00_ADMIN/README.md)
- [05_TEMPLATES README](../../05_TEMPLATES/README.md)
- [MEP/00_ADMIN/README.md](../MEP/00_ADMIN/README.md)
- [INSTALLATIONS README](../../../README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)

---

**Last Updated:** 2025-11-15  
**Owner:** AMPEL360 IT Infrastructure Team
