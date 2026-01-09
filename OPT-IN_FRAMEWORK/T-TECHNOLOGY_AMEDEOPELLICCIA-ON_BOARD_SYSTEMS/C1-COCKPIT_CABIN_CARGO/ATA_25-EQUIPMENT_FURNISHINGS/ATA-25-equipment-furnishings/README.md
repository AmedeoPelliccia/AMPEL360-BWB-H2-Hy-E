# ATA 25 — EQUIPMENT/FURNISHINGS

## Overview

This directory contains the complete **ATA 25 Equipment/Furnishings** system documentation following the **AMPEL360 SBJ (Subject) Code Assignment** structure. The organization maps each Table of Contents (TOC) bullet to a specific **25-xx-yy** subject code for complete traceability and navigability.

**Definition:** ATA 25 covers removable equipment and furnishings in flight and passenger compartments, including emergency, galley, and lavatory equipment, excluding structures and systems assigned elsewhere.

## Structure

The ATA 25 Equipment/Furnishings chapter is organized into the following major sections:

### 25-00 — Equipment/Furnishings General
Foundation and cross-cutting concerns for equipment and furnishings systems.

**Subject Codes (yy):** 00-10
- Chapter overview and scope boundaries
- Architecture and zoning (flight deck / cabin / cargo / crew rest)
- Interfaces to owner systems (ATA 21/23/24/33/35/38/44/50/52/26)
- Attachment standards, materials, and flammability constraints
- Maintainability philosophy and inspection concepts
- Safety and human factors considerations
- Verification strategy

### 25-10 — Flight Compartment
Flight deck furnishings and removable equipment.

**Subject Codes (yy):** 00-10
- Flight crew seats (installation, adjustment, restraints)
- Observer/jump seats
- Stowage, wardrobes, and manual storage
- Tables, partitions, sunshades
- Equipment racks and enclosures
- Floor coverings and anti-skid provisions
- Flight deck escape provisions
- Verification (static loads, endurance, ergonomics)

### 25-20 — Passenger Compartment
Cabin interior architecture: seats, bins, lining, partitions, attendant stations.

**Subject Codes (yy):** 00-10, 90
- Passenger seats (tracks, retention, IFE provisions boundary)
- Cabin attendant seats and stations
- Overhead stowage bins and latches
- Lining, sidewalls, ceiling panels, monuments
- Curtains, partitions, class dividers
- Floor coverings, carpets, liners
- Accessibility provisions (PRM considerations)
- Verification (loads, abuse, latch integrity, evacuation clearances)
- BWB cabin layout modularity program delta

### 25-30 — Galley
Galley monuments and removable equipment integration.

**Subject Codes (yy):** 00-10, 90
- Galley structures/monuments and attach points
- Inserts integration (ovens, chillers, coffee makers)
- Trolleys, carts, and retention systems
- Interfaces (24 power, 38 water/waste, 21 ventilation, 26 fire protection)
- Safety and operational constraints
- Cleaning and maintenance access
- Verification (restraint loads, abuse, thermal adjacency)
- Galley load-shedding compatibility with electric energy management

### 25-40 — Lavatories
Lavatory monuments and removable fittings.

**Subject Codes (yy):** 00-10
- Lavatory monument/module installation and attach points
- Furnishings (mirrors, cabinets, dispensers, seats)
- Interfaces (38 water/waste, 24 power, 21 ventilation)
- Accessibility and safety constraints
- Cleaning and maintenance access
- Verification (fit, door clearances, latch integrity, abuse checks)

### 25-50 — Additional Compartments
Crew rest modules, underfloor equipment spaces, and extra compartments treated as furnishings.

**Subject Codes (yy):** 00-10
- Crew rest compartments (modules, bunks, privacy partitions)
- Wardrobes/stowage monuments outside cabin core
- Cargo accessory equipment treated as furnishings
- Lifts/stairs (if applicable in multi-deck concepts)
- Verification (loads, restraint integrity, access/egress)

### 25-60 — Emergency
Emergency equipment stowage, accessibility, and inspection.

**Subject Codes (yy):** 00-10
- Evacuation equipment (slides/rafts integration and stowage)
- Life vests / flotation devices (stowage, access, inspections)
- ELT/locator devices stowage provisions
- First-aid and medical kits
- Emergency tools (crash axe, flashlights, megaphones, etc.)
- Inspection intervals and servicing checks
- Verification (access time, retention loads, inspection repeatability)

**Note:** Oxygen systems belong to their own chapter, and fire extinguishers belong to fire protection (ATA 26).

### 25-70 — Available
Controlled placeholder for airline/customer options.

**Subject Codes (yy):** 00-10
- Allocation policy (what qualifies to live in 25-70)
- Airline option packages (placeholders + governance)
- Customer configuration deltas (CSDB applicability linkage)
- Verification (configuration control checks)

### 25-80 — Insulation
Thermal/acoustic insulation as a furnishings-managed topic.

**Subject Codes (yy):** 00-10
- Thermal insulation (coverage, thickness classes, installation rules)
- Acoustic insulation (noise reduction targets and placement logic)
- Condensation control and moisture barriers
- Materials & flammability constraints
- Installation workmanship and sealing rules
- Inspection/repair/replace rules
- Verification (thermal performance, moisture tests, durability)

## Directory Structure

Each subject code folder (25-xx-yy) contains:

```
25-xx-yy-descriptive-name/
├── SSOT/                              # Single Source of Truth
│   ├── LC01_Requirements/
│   ├── LC02_System_Requirements/
│   ├── LC03_Design/
│   ├── LC04_Analysis/
│   ├── LC05_VnV/
│   ├── LC06_Quality/
│   ├── LC07_Safety/
│   └── LC08_Certification/
└── PUB/                               # Publications
    ├── AMM/                           # Aircraft Maintenance Manual
    │   ├── CSDB/                      # Common Source Database
    │   │   ├── DM/                    # Data Modules
    │   │   ├── PM/                    # Publication Modules
    │   │   ├── DML/                   # Data Module Lists
    │   │   ├── ICN/                   # Illustrations
    │   │   ├── BREX/                  # Business Rules
    │   │   ├── COMMON/                # Common information
    │   │   └── APPLICABILITY/         # Applicability statements
    │   ├── EXPORT/                    # Export/publication outputs
    │   ├── bindings.csv
    │   └── csdb.profile.yaml
    └── IPC/                           # Illustrated Parts Catalog
        ├── CSDB/                      # (same structure as AMM)
        ├── EXPORT/
        ├── bindings.csv
        └── csdb.profile.yaml
```

## Governance Note

This is an **AMPEL360 internal SBJ allocation for scaffolding**. If your licensed **SNS (System Numbering Standard) extract** already assigns official 5th–6th digit subjects for ATA 25, reconcile or rename to match it.

**Reserved codes:** yy=90–99 are reserved for **program-specific deltas** (e.g., BWB cabin layout modularity, galley load-shedding compatibility with electric propulsion).

## Key Features

### BWB-Specific Considerations
- **25-00-02**: Architecture & zoning with BWB cabin layout considerations
- **25-20-90**: BWB cabin layout modularity program delta (monument zoning constraints)
- Accommodation of blended wing body configuration constraints

### Electric Propulsion Environment
- **25-30-90**: Galley load-shedding compatibility with electric energy management
- Integration with advanced electrical power distribution systems
- Coordination with ATA 24 for power interfaces

### Safety and Accessibility
- **25-00-08**: Safety & human factors (evacuation, accessibility, injury prevention)
- **25-20-07**: Accessibility provisions (PRM considerations, handholds, signage)
- **25-40-04**: Lavatory accessibility and safety constraints
- **25-60**: Complete emergency equipment coverage
- Compliance with evacuation and emergency access requirements

### Materials and Flammability
- **25-00-05**: Materials, flammability & toxicity constraints (project policy)
- **25-80-04**: Insulation materials & flammability constraints
- Adherence to fire safety standards across all furnishings

## Standards and Compliance

Equipment and furnishings systems must comply with:
- **CS-25**: Certification Specifications for Large Aeroplanes
  - CS-25.853: Compartment interiors
  - CS-25.855: Cargo and baggage compartments
  - CS-25.1309: Equipment, systems, and installations
- **CS-25.561**: Emergency landing conditions (seat and restraint systems)
- **CS-25.789**: Retention of items of mass in passenger and crew compartments
- **CS-25.810**: Emergency egress (interfaces)
- **CS-25.812**: Emergency lighting (interfaces)
- **FAA regulations** (equivalent to CS-25 for US certification)
- **ATA iSpec 2200**: Maintenance information standards
- **S1000D**: Technical publication specification
- **DO-160**: Environmental conditions (for electronic equipment in furnishings)

Refer to **25-00-01** (Scope & boundaries) and individual verification subjects for complete regulatory mapping.

## Cross-References

### Related ATA Chapters
- **ATA 21**: Air Conditioning (ventilation interfaces for galleys/lavatories)
- **ATA 23**: Communications (PA system interfaces, IFE boundaries)
- **ATA 24**: Electrical Power (power distribution to galleys, lighting)
- **ATA 26**: Fire Protection (fire extinguisher stowage, smoke detection interfaces)
- **ATA 33**: Lights (cabin lighting, emergency lighting interfaces)
- **ATA 35**: Oxygen (crew oxygen interfaces, passenger oxygen boundaries)
- **ATA 38**: Water/Waste (galley and lavatory water/waste interfaces)
- **ATA 44**: Cabin Systems (environmental control interfaces)
- **ATA 50**: Cargo and Accessory Compartments (cargo restraint boundaries)
- **ATA 52**: Doors (emergency exit interfaces)

### Internal Cross-References
- **25-00-03** → Interfaces matrix (comprehensive cross-ATA mapping)
- **25-20-01** → **25-30**: Seat track/monument attachment standards
- **25-30-04** → **ATA 24/38/21/26**: Galley system interfaces
- **25-40-03** → **ATA 38/24/21**: Lavatory system interfaces

## Document Control

- **ATA Chapter**: 25 — Equipment/Furnishings
- **Structure Standard**: AMPEL360 SBJ Code Assignment
- **Status**: Active
- **Owner**: AMPEL360 Equipment/Furnishings System WG
- **Version**: 1.0
- **Date**: 2026-01-09
- **Repository**: AMPEL360-AIR-T

## Usage

1. **For Requirements**: Navigate to `25-xx-yy-*/SSOT/LC01_Requirements/`
2. **For Design**: Navigate to `25-xx-yy-*/SSOT/LC03_Design/`
3. **For Maintenance**: Navigate to `25-xx-yy-*/PUB/AMM/`
4. **For Parts**: Navigate to `25-xx-yy-*/PUB/IPC/`
5. **For Verification**: Navigate to `25-xx-yy-*/SSOT/LC05_VnV/`

## Contributing

When adding documentation:
1. Use the correct **25-xx-yy** subject code
2. Place content in the appropriate lifecycle folder (LC01-LC08) or publication folder (AMM/IPC)
3. Maintain traceability with clear cross-references
4. Update this index when adding new subjects
5. Follow materials and flammability standards for all equipment and furnishings
6. Ensure compliance with accessibility and safety requirements

## Implementation Status

**Status:** Scaffold Complete  
**Date:** 2026-01-09

All section and subject folders have been created with the complete SSOT/PUB structure. Individual subject documentation is ready for population with:
- Requirements (LC01/LC02)
- Design documentation (LC03)
- Analysis results (LC04)
- Verification and validation plans/results (LC05)
- Quality records (LC06)
- Safety assessments (LC07)
- Certification evidence (LC08)
- Maintenance procedures (AMM)
- Parts catalogs (IPC)

---

**For detailed subject code mapping, see:** [00_INDEX.md](./00_INDEX.md)
