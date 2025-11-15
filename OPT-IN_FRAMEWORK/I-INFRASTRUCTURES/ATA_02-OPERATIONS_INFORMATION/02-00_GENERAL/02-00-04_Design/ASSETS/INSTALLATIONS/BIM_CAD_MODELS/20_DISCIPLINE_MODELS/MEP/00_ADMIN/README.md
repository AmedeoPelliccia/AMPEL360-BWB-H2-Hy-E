# MEP (Mechanical, Electrical, Plumbing) - Discipline Models

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / BIM_CAD_MODELS / 20_DISCIPLINE_MODELS / MEP  
**Purpose:** MEP systems BIM models for all installation locations

---

## Contents

This folder contains MEP (Mechanical, Electrical, Plumbing) systems BIM models organized by location. MEP encompasses HVAC, electrical power distribution, lighting, plumbing, and fire protection systems.

---

## Structure

```
MEP/
├── 00_ADMIN/                      # Administrative files (this folder)
│   ├── README.md                  # This file
│   ├── CHANGELOG.md               # Revision history
│   └── 02-00-04-MEP_Index.csv    # Model inventory
├── OPSCTR/                        # Operations Center MEP models
├── DATACENTER/                    # Data Center MEP models
├── H2ROOM/                        # H2 Fuel Room MEP models
├── GSE_AREA/                      # GSE Area MEP models
└── 99_ARCHIVE/                    # Archived MEP models
```

---

## MEP Systems Scope

### What MEP Models Include

**Mechanical (HVAC):**
- Air handling units (AHU)
- Variable air volume (VAV) boxes
- Ductwork (supply, return, exhaust)
- Diffusers and grilles
- Cooling equipment (chillers, CRAC units)
- Heating equipment
- Ventilation systems
- Smoke control systems

**Electrical:**
- Power distribution panels
- Transformers
- UPS systems
- Emergency generators
- Circuit routing
- Lighting fixtures
- Lighting controls
- Emergency lighting
- Power outlets and receptacles
- Equipment circuits

**Plumbing:**
- Domestic water supply
- Drainage and waste
- Fire protection water supply
- Backflow preventers
- Water heaters
- Specialty plumbing (lab equipment, safety showers if applicable)

**Fire Protection:**
- Sprinkler systems (wet, dry, pre-action)
- Fire alarm systems
- Smoke detection
- Clean agent suppression (for data centers)
- Emergency shutdown systems

### What MEP DOES NOT Include

- IT network equipment → See IT/
- Building structure → See STR/
- Architectural finishes → See ARCH/

---

## Location-Specific Content

### OPSCTR/ (Operations Center)

**Typical files:**
- `02-00-04-MEP-OPSCTR-Concept-LOD200-R01.rvt`
- `02-00-04-MEP-OPSCTR-Design-LOD300-R02.rvt`
- `02-00-04-MEP-OPSCTR-AsBuilt-LOD400-R00.rvt`

**Key MEP systems:**

**Mechanical:**
- Precision air conditioning for equipment
- Underfloor air distribution (if raised floor)
- Overhead supply and return ductwork
- Temperature and humidity control
- Noise control (acoustic considerations)

**Electrical:**
- Dedicated power for consoles and displays
- Emergency power circuits
- UPS-backed circuits for critical systems
- Lighting systems (task, ambient, emergency)
- Lighting controls (dimming for display viewing)

**Plumbing:**
- Minimal plumbing (break room, restrooms nearby)

**Fire Protection:**
- Sprinkler systems (coordinated with equipment)
- Fire alarm system
- Smoke detection

**Design considerations:**
- 24/7 operation reliability
- Redundant systems for critical equipment
- Low noise levels
- Precise temperature and humidity control
- Emergency power for critical systems

### DATACENTER/ (Data Center)

**Typical files:**
- `02-00-04-MEP-DATACENTER-Design-LOD300-R01.rvt`
- `02-00-04-MEP-DATACENTER-AsBuilt-LOD400-R00.rvt`

**Key MEP systems:**

**Mechanical:**
- Computer room air conditioning (CRAC/CRAH units)
- Hot aisle/cold aisle containment
- Underfloor plenum air distribution
- Overhead return air
- High cooling capacity (30-50 BTU/sq ft or higher)
- Redundant cooling (N+1 or 2N)

**Electrical:**
- High-capacity power distribution (PDUs)
- UPS systems (redundant)
- Emergency generators
- Rack-level power distribution
- Power monitoring systems
- Busway distribution
- Redundant power feeds

**Plumbing:**
- Minimal (usually none in server areas)
- Chilled water piping (if water-cooled)

**Fire Protection:**
- Pre-action sprinkler systems
- Clean agent suppression (FM-200, Novec)
- VESDA (very early smoke detection)
- Emergency power off (EPO) systems

**Design considerations:**
- High availability (Tier III or Tier IV)
- Redundancy in all systems
- Hot aisle/cold aisle efficiency
- Power usage effectiveness (PUE)
- Scalability for future growth
- Cooling efficiency

### H2ROOM/ (Hydrogen Fuel Room)

**Typical files:**
- `02-00-04-MEP-H2ROOM-Design-LOD300-R01.rvt`
- `02-00-04-MEP-H2ROOM-AsBuilt-LOD400-R00.rvt`

**Key MEP systems:**

**Mechanical:**
- High-capacity ventilation (continuous air changes)
- Explosion-proof fans and ductwork
- H2 detection and alarm system
- Emergency ventilation
- Temperature control

**Electrical:**
- Explosion-proof electrical equipment (Class I, Division 1/2)
- Emergency lighting
- Intrinsically safe circuits
- Ground fault protection
- Bonding and grounding

**Plumbing:**
- Safety showers and eyewash stations
- Drainage for safety equipment
- Pressure relief drainage

**Fire Protection:**
- H2 detection systems
- Explosion venting
- Fire suppression (special systems)
- Emergency shutdown systems

**Design considerations:**
- NFPA 2 Hydrogen Technologies Code
- Explosion-proof equipment
- Continuous ventilation
- H2 detection and alarming
- Emergency response systems
- Separation from ignition sources

### GSE_AREA/ (Ground Support Equipment Area)

**Typical files:**
- `02-00-04-MEP-GSE_AREA-Design-LOD300-R01.rvt`

**Key MEP systems:**

**Mechanical:**
- Outdoor air quality considerations
- Shelter ventilation (if enclosed)

**Electrical:**
- Outdoor lighting
- Equipment charging stations
- Power outlets for maintenance
- Outdoor-rated equipment
- Lightning protection

**Plumbing:**
- Drainage

**Fire Protection:**
- Fire extinguishers
- Fire alarm notification

---

## File Naming Convention

```
02-00-04-MEP-<LOCATION>-<PHASE>-LOD<nnn>-R<nn>.rvt
```

Where:
- `MEP` = MEP discipline
- `LOCATION` = OPSCTR, DATACENTER, H2ROOM, GSE_AREA
- `PHASE` = Concept, Design, AsBuilt
- `LOD<nnn>` = LOD200, LOD300, LOD350, LOD400
- `R<nn>` = Revision number

---

## MEP Modeling Standards

### LOD Requirements

**LOD200 - Concept:**
- Schematic system layouts
- Equipment sizes (approximate)
- Major distribution routes
- Space allocations

**LOD300 - Design:**
- Specific equipment selections
- Detailed routing
- Sizes and capacities
- Connection points
- Sufficient for coordination

**LOD350 - Pre-Construction:**
- Fabrication details
- Hanger locations
- Access panels
- Installation sequences

**LOD400 - As-Built:**
- As-installed conditions
- Final equipment
- Actual routing
- Control sequences
- Commissioning data

### MEP-Specific Modeling Guidelines

**Ductwork:**
- Model centerlines for coordination
- Include fittings and transitions
- Show access panels
- Coordinate with structural for hangers

**Piping:**
- Model centerlines for coordination
- Include valves and specialties
- Show pipe supports
- Coordinate slope requirements

**Electrical:**
- Model conduit routes for major circuits
- Show panel locations and sizes
- Model lighting fixtures
- Include emergency power routing

**Equipment:**
- Use manufacturer families
- Include clearances for service
- Show connection points
- Model vibration isolation

---

## Coordination Points

**With ARCH:**
- Ceiling heights for ductwork and piping
- Equipment room sizes
- Service penetrations
- Access panel locations

**With STR:**
- Equipment loads and vibration isolation
- Hanger locations
- Roof penetrations for equipment
- Floor penetrations

**With IT:**
- Power requirements for IT racks
- Cooling requirements for IT equipment
- UPS systems sizing
- Cable tray coordination

**With Fire Protection:**
- Sprinkler coordination with ductwork
- Fire alarm coordination
- Clean agent system design

---

## Quality Checklist

Before publishing an MEP model:

✅ Equipment properly sized and located  
✅ Ductwork and piping routes coordinated  
✅ Clearances for service access verified  
✅ Electrical loads calculated  
✅ Cooling loads calculated  
✅ System capacities documented  
✅ Clash detection run with other disciplines  
✅ Energy analysis performed (if required)  
✅ Code compliance verified  
✅ Model opens without errors  

---

## Related Documentation

- [20_DISCIPLINE_MODELS README](../README.md)
- [BIM_CAD_MODELS 00_ADMIN README](../../00_ADMIN/README.md)
- [IT/00_ADMIN/README.md](../IT/00_ADMIN/README.md)
- [ARCH/00_ADMIN/README.md](../ARCH/00_ADMIN/README.md)
- [INSTALLATIONS README](../../../README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)

---

**Last Updated:** 2025-11-15  
**Owner:** AMPEL360 MEP Engineering Team
