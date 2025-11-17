# 95-50 Structures

**ATA Chapter:** 95-50  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active

---

## Overview

The **95-50_Structures** module defines all **hardware carriers, mounting structures, and physical integration points** for Neural Network (NN) hardware and sensors across the AMPEL360 BWB-H2-Hy-E aircraft. This includes:

- Equipment racks, chassis, and mounting brackets
- Cable trays, conduits, and routing structures
- Sensor mounts, antenna fairings, and access panels
- Structural reinforcements for heavy equipment
- Cross-ATA traceability to system components

---

## Purpose

This chapter ensures that **all NN-related hardware has defined physical homes** on the aircraft, with:

- ✅ **Structural integration** coordinated with airframe (ATA 53, 57, etc.)
- ✅ **Installation standards** for consistent mounting and maintenance access
- ✅ **Traceability** linking hardware structures to subsystems in 95-20 and components in 95-00-13
- ✅ **Safety and certification** compliance with mounting, bonding, and separation requirements

---

## Directory Structure

```
95-50_Structures/
├── README.md (this file)
├── 95-50-00-001_Structures_and_Hardware_Overview.md
├── 95-50-00-002_Structural_Integration_Strategy.md
├── 95-50-00-003_Cross_ATA_Structural_Map.csv
│
├── 00_META/                                           # Taxonomy & Traceability
│   ├── 95-50-00-004_Structural_Taxonomy.md
│   ├── 95-50-00-005_Hardware_Carrier_Taxonomy.md
│   ├── 95-50-00-006_Structural_Traceability_Matrix.csv
│   ├── 95-50-00-007_Installation_Standards_and_Rules.md
│   └── 95-50-00-008_CAOS_Structures_Hooks.md
│
├── 95-50-21_ECS_Hardware_and_Installations/          # ATA 21 – Environmental Control
├── 95-50-24_Electrical_Cabinets_and_Routing/        # ATA 24 – Electrical Power
├── 95-50-28_H2_Tanks_and_Fuel_Hardware/             # ATA 28 – Hydrogen Fuel
├── 95-50-31_Recording_and_Data_HW_Structures/       # ATA 31 – Recording Systems
├── 95-50-42_IMA_and_Avionics_Hardware/              # ATA 42 – Integrated Modular Avionics
├── 95-50-46_Information_Systems_Hardware/           # ATA 46 – Information Systems
├── 95-50-49_APU_and_Aux_Hardware_Structures/        # ATA 49 – APU
├── 95-50-53_Fuselage_and_Bay_Structures_for_NN_HW/ # ATA 53 – Fuselage
├── 95-50-57_Wing_Structures_for_Sensors_and_Antennas/ # ATA 57 – Wings
└── 95-50-70_Propulsion_and_Pylon_Structures_for_NN_HW/ # ATA 70-79 – Propulsion
```

---

## Key Features

### 1. **Hardware Carrier Taxonomy**
A standardized classification system for all mounting structures, ensuring consistent identification and maintenance procedures.

### 2. **Cross-ATA Mapping**
Every structure is traceable to:
- **Parent ATA systems** (21, 24, 28, 31, 42, 46, 49, 53, 57, 70-79)
- **95-20 Subsystems** (functional neural network systems)
- **95-00-13 Components** (hardware parts and assemblies)

### 3. **ASSETS Standard**
Each ATA-specific subfolder includes an `ASSETS/` directory following the [AMPEL360_ASSETS_STANDARD.md](../../../../../AMPEL360_ASSETS_STANDARD.md):
- **ASSEMBLIES/** – Assembly models (ASM.json, STEP)
- **INSTALLATIONS/** – Installation layouts (INS.json, PDF)
- **DRAWINGS/** – Engineering drawings (drawio, SVG, DXF)

### 4. **CAOS Integration**
Structures include digital hooks for the Computer Aided Operations & Services (CAOS) system to track:
- Sensor positions for predictive maintenance
- Thermal management zones
- Access panel schedules
- Structural health monitoring points

---

## Cross-References

### Within ATA 95
- **[95-00-13 Subsystems & Components](../95-00_GENERAL/95-00-13_Subsystems_Components/)** – Hardware component library
- **[95-20 Subsystems](../95-20_Subsystems/)** – Functional neural network systems
- **[95-30 Circularity](../95-30_Circularity/)** – End-of-life disassembly and recycling

### To Other ATA Chapters
- **[ATA 21 - Air Conditioning](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E1-ENVIRONMENT/ATA_21-AIR_CONDITIONING_AND_PRESSURIZATION/)** – ECS system details
- **[ATA 24 - Electrical Power](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E2-ENERGY/ATA_24-ELECTRICAL_POWER/)** – Electrical system details
- **[ATA 28 - Fuel (H₂)](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENIC_SYSTEMS/ATA_28-FUEL_SAF_AND_CRYOGENIC/)** – H₂ fuel system details
- **[ATA 42 - IMA](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E3-ELECTRONICS/ATA_42-INTEGRATED_MODULAR_AVIONICS_HARDWARE_MODULES/)** – Avionics hardware details
- **[ATA 53 - Fuselage](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/A-AIRFRAME/ATA_53-FUSELAGE/)** – Fuselage structure details
- **[ATA 57 - Wings](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/A-AIRFRAME/ATA_57-WINGS/)** – Wing structure details

---

## Usage Guidelines

### Adding a New Structure
1. Identify the parent ATA chapter (21, 24, 28, etc.)
2. Navigate to the appropriate `95-50-XX/` subfolder
3. Create documentation in markdown format
4. Add CAD models and drawings to the `ASSETS/` subtree
5. Update the `95-50-00-006_Structural_Traceability_Matrix.csv`
6. Link to parent systems in 95-20 and components in 95-00-13

### Installation Standards
All structures must comply with:
- **Mounting:** Load paths, fastener types, torque specifications
- **Bonding:** Electrical bonding and grounding requirements
- **Separation:** Physical separation for EMI, fire protection, and redundancy
- **Access:** Maintenance access requirements and panel design
- **Thermal:** Heat dissipation paths and cooling interfaces

See `00_META/95-50-00-007_Installation_Standards_and_Rules.md` for complete guidelines.

---

## Compliance & Standards

- **ATA iSpec 2200** – Air Transport Association specification for technical documentation
- **S1000D** – International specification for technical publications
- **EASA CS-25** – Certification Specifications for Large Aeroplanes
- **RTCA DO-160** – Environmental Conditions and Test Procedures for Airborne Equipment
- **SAE AS50881** – Wiring Aerospace Vehicle (for electrical routing)
- **ISO 19881** – Gaseous hydrogen - Land vehicle fuel containers (for H₂ structures)

---

## Document Control

| Version | Date       | Author                     | Changes                          |
|---------|------------|----------------------------|----------------------------------|
| 1.0     | 2025-11-17 | AMPEL360 Documentation Team | Initial creation of 95-50 structure |

---

## Related Documents

- [AMPEL360_DOCUMENTATION_STANDARD.md](../../../../../AMPEL360_DOCUMENTATION_STANDARD.md)
- [AMPEL360_ASSETS_STANDARD.md](../../../../../AMPEL360_ASSETS_STANDARD.md)
- [OPT-IN_FRAMEWORK_STANDARD.md](../../../../../OPT-IN_FRAMEWORK_STANDARD.md)

---

**Maintained by:** AMPEL360 Structures Team  
**Contact:** structures@ampel360.aero
