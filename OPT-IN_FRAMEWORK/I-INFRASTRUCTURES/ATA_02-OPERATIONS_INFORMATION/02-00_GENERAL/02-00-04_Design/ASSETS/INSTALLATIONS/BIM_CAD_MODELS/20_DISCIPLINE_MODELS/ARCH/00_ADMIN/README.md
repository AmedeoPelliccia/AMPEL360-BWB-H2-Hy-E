# ARCH (Architecture) - Discipline Models

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / BIM_CAD_MODELS / 20_DISCIPLINE_MODELS / ARCH  
**Purpose:** Architectural BIM models for all installation locations

---

## Contents

This folder contains architectural BIM models organized by location. Architecture provides the building shells, spaces, finishes, and context for all other disciplines.

---

## Structure

```
ARCH/
├── 00_ADMIN/                      # Administrative files (this folder)
│   ├── README.md                  # This file
│   ├── CHANGELOG.md               # Revision history
│   └── 02-00-04-ARCH_Index.csv   # Model inventory
├── OPSCTR/                        # Operations Center architectural models
├── DATACENTER/                    # Data Center architectural models
├── H2ROOM/                        # H2 Fuel Room architectural models
├── GSE_AREA/                      # GSE Area architectural models
└── 99_ARCHIVE/                    # Archived architectural models
```

---

## Architectural Scope

### What Architecture Models Include

**Building Elements:**
- Exterior walls and enclosures
- Interior partitions and walls
- Doors and door frames
- Windows and glazing
- Roof structures (if applicable)

**Interior Elements:**
- Floor finishes
- Wall finishes
- Ceiling systems
- Casework and millwork
- Built-in furniture

**Space Definition:**
- Room boundaries
- Functional zones
- Circulation paths
- Equipment clearances
- Access requirements

**Vertical Elements:**
- Stairs and ramps (if multi-level)
- Elevators/lifts (if applicable)
- Vertical shafts for services

### What Architecture DOES NOT Include

- Structural framing → See STR/
- MEP systems → See MEP/
- IT infrastructure → See IT/
- Movable furniture → See LAYOUTS/

---

## Location-Specific Content

### OPSCTR/ (Operations Center)

**Typical files:**
- `02-00-04-ARCH-OPSCTR-Concept-LOD200-R01.rvt`
- `02-00-04-ARCH-OPSCTR-Design-LOD300-R02.rvt`
- `02-00-04-ARCH-OPSCTR-AsBuilt-LOD400-R00.rvt`

**Key architectural elements:**
- Control room layouts
- Raised floor systems (architectural coordination)
- Acoustic treatments
- Wall systems (including glass partitions)
- Door and access control locations
- Ceiling systems
- Cable access floor boxes (architectural coordination)
- Equipment alcoves and niches

**Design considerations:**
- Sightlines for operators
- Acoustic performance
- Natural light vs. controlled lighting
- Security boundaries
- ADA accessibility

### DATACENTER/ (Data Center)

**Typical files:**
- `02-00-04-ARCH-DATACENTER-Design-LOD300-R01.rvt`
- `02-00-04-ARCH-DATACENTER-AsBuilt-LOD400-R00.rvt`

**Key architectural elements:**
- Server room enclosures
- Raised floor systems (typically 24" or 36" high)
- Hot aisle/cold aisle containment structures
- Access doors and mantrap systems
- Fire-rated walls and partitions
- Cable entry points
- Viewing windows
- Ceiling systems (plenum return)

**Design considerations:**
- Heavy floor loading (structural coordination)
- Controlled access
- Fire ratings
- Environmental separation
- Service access
- Future expansion

### H2ROOM/ (Hydrogen Fuel Room)

**Typical files:**
- `02-00-04-ARCH-H2ROOM-Design-LOD300-R01.rvt`

**Key architectural elements:**
- Blast-resistant enclosure (if required)
- Explosion-relief panels
- Separation walls (fire-rated)
- Special doors (pressure-relief, blast-rated)
- Ventilation openings (architectural coordination with MEP)
- Equipment platforms
- Emergency egress

**Design considerations:**
- Safety codes (NFPA, local codes)
- Explosion protection
- Separation distances
- Emergency egress
- Ventilation requirements (architectural coordination)

### GSE_AREA/ (Ground Support Equipment Area)

**Typical files:**
- `02-00-04-ARCH-GSE_AREA-Design-LOD300-R01.rvt`

**Key architectural elements:**
- Equipment storage shelters
- Information kiosk enclosures
- Weather protection
- Signage structures
- Access paths and ramps
- Service access doors

**Design considerations:**
- Weather resistance
- Vandalism resistance
- Visibility and wayfinding
- Accessibility

---

## File Naming Convention

```
02-00-04-ARCH-<LOCATION>-<PHASE>-LOD<nnn>-R<nn>.rvt
```

Where:
- `ARCH` = Architecture discipline
- `LOCATION` = OPSCTR, DATACENTER, H2ROOM, GSE_AREA
- `PHASE` = Concept, Design, AsBuilt
- `LOD<nnn>` = LOD200, LOD300, LOD350, LOD400
- `R<nn>` = Revision number

---

## Architectural Modeling Standards

### LOD Requirements

**LOD200 - Concept:**
- Generic walls, floors, roofs
- Generic doors and windows
- Room boundaries
- Approximate locations

**LOD300 - Design:**
- Specific wall assemblies
- Actual door and window types
- Finishes assigned
- Casework modeled
- Ceiling systems defined
- Sufficient for coordination

**LOD350 - Pre-Construction:**
- Fabrication details
- Mounting details
- Joint locations
- Installation sequences

**LOD400 - As-Built:**
- As-installed conditions
- Field-verified dimensions
- Actual products installed
- All modifications documented

### Revit Standards (if using Revit)

**Worksets:**
- Shell and Core
- Interiors
- Furniture and Casework
- Ceilings
- Annotation
- Links (for linked models)

**View Templates:**
- Floor plans (by LOD)
- Reflected ceiling plans
- Elevations and sections
- 3D coordination views

**Naming Conventions:**
- Levels: Per project standard
- Grids: Per project standard
- Views: Discipline prefix (A-)
- Sheets: A-series numbering

### Coordination Points

**With Structural (STR):**
- Wall/floor/ceiling attachment points
- Opening locations and sizes
- Load-bearing vs. non-load-bearing
- Raised floor support requirements

**With MEP:**
- Ceiling heights (clearances for ducts, pipes)
- Service penetrations
- Equipment room sizes
- Access panel locations
- Acoustic requirements affecting MEP routing

**With IT:**
- Raised floor depths
- Cable pathway locations
- Equipment mounting locations
- Access requirements

---

## Quality Checklist

Before publishing an architectural model:

✅ All walls on correct levels  
✅ Doors have correct swing direction  
✅ Room names and numbers assigned  
✅ Floor and ceiling finishes specified  
✅ Coordinate with structural grids  
✅ Service penetrations located  
✅ Access clearances verified  
✅ ADA compliance checked  
✅ Fire ratings assigned where required  
✅ Model opens without errors  

---

## Common Issues and Solutions

**Issue:** Walls not joining properly  
**Solution:** Check wall join settings, ensure walls are on same level

**Issue:** Doors missing or not visible  
**Solution:** Check view range, verify door family placement

**Issue:** Room boundaries not calculating  
**Solution:** Ensure room-bounding elements are properly set

**Issue:** Clash with structural elements  
**Solution:** Coordinate with structural team, adjust wall locations

**Issue:** Insufficient ceiling height for MEP  
**Solution:** Coordinate ceiling heights with MEP team early in design

---

## Related Documentation

- [20_DISCIPLINE_MODELS README](../README.md)
- [BIM_CAD_MODELS 00_ADMIN README](../../00_ADMIN/README.md)
- [05_TEMPLATES README](../../05_TEMPLATES/README.md)
- [10_MASTER_MODELS README](../../10_MASTER_MODELS/README.md)
- [INSTALLATIONS README](../../../README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)

---

**Last Updated:** 2025-11-15  
**Owner:** AMPEL360 Architecture Team
