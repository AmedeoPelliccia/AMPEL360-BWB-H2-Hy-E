# 10-00-13 Subsystems & Components

## Purpose

This directory provides comprehensive documentation for subsystems, components, and product breakdown structures for **ATA 10 - Parking, Mooring, Storage & RTS** operations of the AMPEL360-BWB-H2-Hy-E aircraft.

It establishes the system architecture, subsystem decomposition, component specifications, and traceability for all parking, mooring, and storage systems with specific attention to:

- **H2/Cryogenic systems** - Liquid hydrogen (LH2) safety, detection, venting, and thermal management
- **BWB-specific subsystems** - Blended Wing Body configuration ground handling adaptations
- **Product Breakdown Structure (PBS)** - Hierarchical component organization aligned with ATA iSpec 2200

## Scope

This folder is part of the **10-00_GENERAL** layer, which provides governance and lifecycle management for ATA Chapter 10.

### In Scope

- System architecture definitions for parking, mooring, storage, and H2 safety systems
- Detailed subsystem specifications organized by functional area
- Component lists and Product Breakdown Structure (PBS)
- H2/LH2-specific subsystems (detection, venting, monitoring, emergency shutdown)
- Cryogenic subsystems (tank interfaces, insulation, valve systems, boiloff management)
- BWB-specific ground handling subsystems (tiedown, mooring, clearance adaptations)
- Interface definitions between subsystems
- Component-level traceability to requirements, hazards, and standards

### Out of Scope

- Detailed component manufacturing specifications (see 10-00-09_Production_Planning)
- Maintenance procedures (see 10-00-14_Ops_Std_Sustain)
- Certification evidence packages (see 10-00-10_Certification)
- Operational procedures (see 10-10_Operations)

## System Architecture Methodology

The subsystems are organized using a hierarchical decomposition approach aligned with **SAE ARP4754A** (Systems Development) and **MIL-STD-881** (Work Breakdown Structure):

### Level 1: System Architecture
High-level system architectures defining overall structure, boundaries, and major subsystem groupings:
- Parking System Architecture
- Mooring System Architecture  
- Storage System Architecture
- H2 Safety System Architecture
- BWB Ground System Architecture

### Level 2: Functional Subsystems
Mid-level subsystems organized by operational function:
- **Parking**: Tiedown, wheel chocks, parking brake, ground locks, guidance
- **Mooring**: Mooring points, equipment, storm mooring, wind monitoring
- **Storage**: Long-term storage, preservation, dehumidification, monitoring
- **H2 Safety**: Detection, venting, alarm, emergency shutdown, monitoring
- **Cryogenic**: Tank interfaces, insulation, valves, boiloff management, thermal protection
- **BWB-Specific**: BWB tiedown, mooring, ground handling, clearance

### Level 3: Components
Lowest-level items in the PBS with part numbers, specifications, and suppliers.

## Subsystem Decomposition Approach

Each subsystem document follows a standard structure:

1. **Subsystem Identification** - ID, title, parent system, revision
2. **Functional Description** - Purpose, operational modes, key functions
3. **Architecture** - Block diagrams, component hierarchy, interfaces
4. **Component List** - All constituent parts with IDs and part numbers
5. **Interfaces** - Mechanical, electrical, H2/LH2, data, thermal connections
6. **Requirements Traceability** - Links to parent requirements
7. **Safety & Hazards** - Safety-critical aspects, hazard mitigation
8. **Operational Domain** - Temperature, pressure, wind, humidity limits
9. **Applicable Standards** - Regulatory and industry standards
10. **Document Control** - Revision history, status, ownership

## H2/Cryo Subsystems Overview

### H2 Safety Subsystems (40-series)
Critical subsystems for hydrogen safety during ground operations:

- **10-00-13-40A H2 Detection** - H2 sensor arrays, LEL monitoring, detection zones
- **10-00-13-41A H2 Venting** - Controlled venting systems, safe dispersion
- **10-00-13-42A H2 Alarm** - Multi-stage alarm system, audio/visual indicators
- **10-00-13-43A H2 Emergency Shutdown (ESD)** - Emergency isolation and shutdown logic
- **10-00-13-44A H2 Monitoring** - Continuous monitoring, data logging, trending

### Cryogenic Subsystems (50-series)
LH2-specific cryogenic systems:

- **10-00-13-50A LH2 Tank Interface** - Fill/drain ports, vent connections, sensor interfaces
- **10-00-13-51A Cryo Insulation** - Multi-Layer Insulation (MLI), vacuum jackets, thermal protection
- **10-00-13-52A Cryo Valve** - Cryogenic-rated valves, actuators, control systems
- **10-00-13-53A Boiloff Management** - Pressure control, vent rate management, long-term storage
- **10-00-13-54A Thermal Protection** - Heat leak minimization, thermal bridges, insulation monitoring

**Key Standards:**
- SAE AS6968 - Hydrogen Aircraft Systems
- ISO 13984 - Liquid Hydrogen Land Vehicle Fuel Tanks
- ISO 20421-1 - Cryogenic vessels - Large transportable vacuum-insulated vessels
- NFPA 2 - Hydrogen Technologies Code

## BWB-Specific Subsystems

Adaptations required for the Blended Wing Body configuration:

- **10-00-13-60A BWB Tiedown** - Wide-body tiedown point distribution, load balancing
- **10-00-13-61A BWB Mooring** - Mooring point locations optimized for BWB aerodynamics
- **10-00-13-62A BWB Ground Handling** - Towing, jacking, lifting provisions for unconventional geometry
- **10-00-13-63A BWB Clearance** - Ground clearance management, tail strike prevention, wingtip protection

## Naming Conventions

All documents follow the standardized pattern: **10-00-13-NNA_DESCRIPTION.md**

Where:
- **10** = ATA Chapter (Parking, Mooring, Storage)
- **00** = Section (GENERAL)
- **13** = Subsection (Subsystems_Components)
- **NN** = Sequential number (01-99)
- **A** = Revision letter (A, B, C, ...)
- **_DESCRIPTION** = Descriptive title in PascalCase with underscores

### Numbering Ranges by Category

| Range | Category | Example |
|-------|----------|---------|
| 01-09 | System Architecture | 10-00-13-01A_System_Architecture_Overview.md |
| 10-19 | Parking Subsystems | 10-00-13-10A_Tiedown_Subsystem.md |
| 20-29 | Mooring Subsystems | 10-00-13-20A_Mooring_Points_Subsystem.md |
| 30-39 | Storage Subsystems | 10-00-13-30A_Long_Term_Storage_Subsystem.md |
| 40-49 | H2 Safety Subsystems | 10-00-13-40A_H2_Detection_Subsystem.md |
| 50-59 | Cryogenic Subsystems | 10-00-13-50A_LH2_Tank_Interface_Subsystem.md |
| 60-69 | BWB-Specific Subsystems | 10-00-13-60A_BWB_Tiedown_Subsystem.md |
| 70-79 | Component Breakdown | 10-00-13-70A_PBS_Product_Breakdown_Structure.md |

## Directory Structure

```
10-00-13_Subsystems_Components/
├── README.md (this file)
├── 00_INDEX.md
├── subsystems-metadata.schema.json
│
├── system-architecture/         # System architecture documents (01-09)
├── parking-subsystems/          # Parking subsystems (10-19)
├── mooring-subsystems/          # Mooring subsystems (20-29)
├── storage-subsystems/          # Storage subsystems (30-39)
├── h2-safety-subsystems/        # H2 safety subsystems (40-49)
├── cryo-subsystems/             # Cryogenic subsystems (50-59)
├── bwb-subsystems/              # BWB-specific subsystems (60-69)
├── component-breakdown/         # PBS and component lists (70-79)
└── subsystems-templates/        # Document templates
```

## Applicable Standards

### General Standards
- **ATA iSpec 2200** - ATA Specification 2200 Information Standards
- **ATA 100** - Chapter 10 Parking, Mooring, Storage
- **SAE ARP4754A** - Guidelines for Development of Civil Aircraft and Systems
- **SAE ARP4761** - Guidelines and Methods for Conducting the Safety Assessment Process
- **MIL-STD-881** - Work Breakdown Structures for Defense Materiel Items
- **S1000D** - International specification for technical publications

### H2/Cryogenic Standards
- **SAE AS6968** - Hydrogen Aircraft Ground Support Equipment and Storage
- **NFPA 2** - Hydrogen Technologies Code
- **ISO 11114-4** - Gas cylinders - Compatibility of cylinder and valve materials with gas contents - Part 4: Test methods for selecting metallic materials resistant to hydrogen embrittlement
- **ISO 13984** - Liquid hydrogen - Land vehicle fuel tanks
- **ISO 20421-1** - Cryogenic vessels - Large transportable vacuum-insulated vessels - Part 1: Design, fabrication, inspection and testing
- **ASTM E1450** - Standard Test Method for Tensile Testing of Structural Alloys in Liquid Helium

### Safety & Certification Standards
- **ATEX 2014/34/EU** - Equipment for potentially explosive atmospheres
- **IECEx** - International Electrotechnical Commission Explosive Atmospheres certification
- **DO-178C** - Software Considerations in Airborne Systems and Equipment Certification
- **DO-254** - Design Assurance Guidance for Airborne Electronic Hardware
- **IATA DGR** - Dangerous Goods Regulations
- **49 CFR** - Transportation of Hazardous Materials (USA)

## Metadata Schema

All subsystem documents include structured metadata compliant with `subsystems-metadata.schema.json`, capturing:

- Document identification and revision control
- Subsystem type and hierarchy
- Component lists and part numbers
- Interface definitions
- H2/Cryo/BWB classification flags
- Safety criticality and Design Assurance Level (DAL)
- Operational domain parameters
- Applicable standards
- Revision history

## Cross-References

### Internal References
- [10-00-02_Safety](../10-00-02_Safety/) - Safety requirements and hazard analysis
- [10-00-03_Requirements](../10-00-03_Requirements/) - System and subsystem requirements
- [10-00-04_Design](../10-00-04_Design/) - Detailed design specifications
- [10-00-05_Interfaces](../10-00-05_Interfaces/) - Interface control documents
- [10-00-10_Certification](../10-00-10_Certification/) - Certification evidence and compliance

### External ATA References
- **ATA 21** - Air Conditioning (for ECS interfaces)
- **ATA 28** - Fuel (for H2 fuel system interfaces)
- **ATA 49** - Airborne Auxiliary Power (for APU interfaces)
- **ATA 71** - Power Plant (for propulsion system interfaces)

## Status

- **Phase**: Subsystems Components
- **Lifecycle Position**: 13 of 14
- **Status**: Active
- **Last Updated**: 2025-12-11

## Related Folders

Part of the canonical 14-folder lifecycle:
1. Overview → 2. Safety → 3. Requirements → 4. Design → 5. Interfaces → 6. Engineering → 7. V&V → 8. Prototyping → 9. Production Planning → 10. Certification → 11. EIS/Versions/Tags → 12. Services → **13. Subsystems/Components** → 14. Ops/Std/Sustain

## Document Control

- **Standard**: OPT-IN Framework v1.1 (ATA 95 canonical template)
- **Owner**: AMPEL360 Documentation WG
- **Generated with assistance of**: AI (GitHub Copilot), prompted by Amedeo Pelliccia
- **Status**: DRAFT - Subject to human review and approval
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-11
