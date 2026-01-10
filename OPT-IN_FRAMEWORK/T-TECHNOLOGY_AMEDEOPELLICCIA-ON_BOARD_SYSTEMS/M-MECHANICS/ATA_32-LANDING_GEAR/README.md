# ATA 32 — LANDING GEAR

## Overview

This is ATA Chapter 32: LANDING GEAR, part of the T — TECHNOLOGY AMEDEOPELLICCIA — ON BOARD SYSTEMS axis.

> **Architecture Option B:** This landing gear system uses the **Distributed Electro-Hydraulic** architecture featuring:
> - **EHPU** (Electro-Hydraulic Power Units) — local hydraulic power generation
> - **EHA** (Electro-Hydrostatic Actuators) — self-contained actuation units
> - **EHB** (Electro-Hydraulic Brakes) — local braking with metering and accumulators
> - **Short hydraulic lines** — minimal central hydraulic dependency
> - **Explicit interfaces to ATA 24** (electrical power), **ATA 31** (indication), and **ATA 45** (CMS/BITE)

## Structure

This chapter follows the mandatory OPT-IN Framework structure:

### ATA-32-landing-gear (iSpec 2200 Structure)

The [ATA-32-landing-gear/](ATA-32-landing-gear/) directory contains the ATA iSpec 2200 structure for Option B (Distributed Electro-Hydraulic) architecture:

- **32-00-landing-gear-general/**: System overview, Option B philosophy, interfaces, safety
- **32-10-main-gear-and-doors/**: MLG structure, actuation, doors, locks, WOW
- **32-20-nose-gear-and-doors/**: NLG structure, steering-coupling, ground handling
- **32-30-extension-and-retraction/**: EHPU local power, sequencing, emergency extension
- **32-40-wheels-and-brakes/**: EHB braking, antiskid, autobrake, temperature monitoring
- **32-50-steering/**: EHA steering module, control laws, shimmy damping
- **32-60-position-indication-and-warning/**: Position sensing, health monitoring, BITE
- **32-70-supplementary-gear/**: Ground handling, servicing, LRU replacement

### 32-00_GENERAL (Lifecycle Folders)

The GENERAL layer contains 14 mandatory lifecycle folders covering the complete development cycle:

1. **32-00-01_Overview**: System overview and global architecture
2. **32-00-02_Safety**: Safety framework and analysis
3. **32-00-03_Requirements**: Requirements and traceability
4. **32-00-04_Design**: Design specifications and patterns
5. **32-00-05_Interfaces**: Interface control documents
6. **32-00-06_Engineering**: Analysis, models, and simulation
7. **32-00-07_V_AND_V**: Verification and validation
8. **32-00-08_Prototyping**: Prototype development
9. **32-00-09_Production_Planning**: Manufacturing planning
10. **32-00-10_Certification**: Certification evidence
11. **32-00-11_EIS_Versions_Tags**: Configuration management
12. **32-00-12_Services**: Maintenance and service
13. **32-00-13_Subsystems_Components**: Component breakdown
14. **32-00-14_Ops_Std_Sustain**: Operational standards

### Cross-ATA Root Buckets

The following buckets are mandatory in every ATA chapter:

- **32-10_Operations**: Operational procedures and use cases
- **32-20_Subsystems**: Functional subsystems (design-driven internal structure)
- **32-30_ANCHORS**: Sustainability, LCA, and circular economy
- **32-40_Software**: Software, control logic, and AI/ML
- **32-50_Structures**: Physical structures and frames
- **32-60_Storages**: Tanks, reservoirs, and storage
- **32-70_Propulsion**: Propulsion interfaces (if applicable)
- **32-80_Energy**: Energy management and distribution
- **32-90_Tables_Schemas_Diagrams**: Data tables and documentation

## Document Control

- **ATA Chapter**: 32
- **Status**: Active
- **Architecture**: Option B — Distributed Electro-Hydraulic (EHPU/EHA/EHB)
- **Owner**: AMPEL360 Documentation WG
- **Standard**: OPT-IN Framework v1.1 / ATA iSpec 2200 / S1000D 5.0
- **Last Updated**: 2026-01-10

## Cross-References

- [ATA 24 — Electrical Power](../../../E3-ELECTRONICS/ATA_24-ELECTRICAL_POWER/) — EHPU power source, peak loads, shedding
- [ATA 29 — Hydraulic Power](../ATA_29-HYDRAULIC_POWER/) — Minimal central hydraulic (Option B philosophy)
- [ATA 31 — Indicating/Recording Systems](../../../I-INFORMATION_INTELLIGENCE_INTERFACES/ATA_31-INDICATING_RECORDING/) — Gear position, warnings
- [ATA 45 — Central Maintenance System](../../../I-INFORMATION_INTELLIGENCE_INTERFACES/ATA_45-CENTRAL_MAINTENANCE/) — BITE export, diagnostics
