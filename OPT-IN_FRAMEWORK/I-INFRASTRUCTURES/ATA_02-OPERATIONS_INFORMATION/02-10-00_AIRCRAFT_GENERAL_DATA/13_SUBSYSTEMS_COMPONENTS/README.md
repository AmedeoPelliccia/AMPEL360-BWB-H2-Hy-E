# 13_SUBSYSTEMS_COMPONENTS - AIRCRAFT_GENERAL_DATA

**Component Code:** 02-10-00  
**Component Name:** AIRCRAFT_GENERAL_DATA  
**Folder:** 13_SUBSYSTEMS_COMPONENTS

## Purpose

This folder contains detailed subsystem components, part number registries, and configuration control documentation for aircraft general data systems including data plates, marking systems, measurement equipment, and configuration management.

## Directory Structure

```
13_SUBSYSTEMS_COMPONENTS/
├── README.md
├── Part_Number_Registry.csv
│
├── DATA_PLATES/
│   ├── PNR-02-10-001_Main_Data_Plate.md
│   │   ├── Component_List.csv
│   │   ├── PNR-02-10-001-01_Plate_Assembly.csv
│   │   └── PNR-02-10-001-02_Rivets_Kit.csv
│   │
│   └── PNR-02-10-002_Weight_Data_Plate.md
│
├── MARKING_SYSTEMS/
│   ├── PNR-02-10-101_Serial_Number_Marking.md
│   ├── PNR-02-10-102_Station_Marking_Set.md
│   └── PNR-02-10-103_CG_Reference_Markers.md
│
├── MEASUREMENT_EQUIPMENT/
│   ├── PNR-02-10-201_Weighing_Kit.md
│   ├── PNR-02-10-202_Dimension_Measurement_Tools.md
│   └── PNR-02-10-203_CG_Calculation_Tools.md
│
└── CONFIGURATION_CONTROL/
    ├── Configuration_Items_Registry.csv
    └── Interchangeability_Matrix.csv
```

## Part Number Registry

The `Part_Number_Registry.csv` contains the master list of all part numbers, descriptions, types, manufacturers, and status for components within this subsystem.

### Key Part Numbers

| Part Number | Description | Type | Manufacturer | Status |
|------------|-------------|------|--------------|--------|
| PNR-02-10-001 | Main Data Plate | Assembly | AMPEL360 | Active |
| PNR-02-10-001-01 | Aluminum Plate 200×150mm | Component | MetalCorp | Active |
| PNR-02-10-102 | Station Marking Decal Set | Consumable | AeroMark | Active |
| PNR-02-10-201 | Aircraft Weighing Kit 200t | GSE | Weightech | Active |

## Subsystem Categories

### 1. DATA_PLATES
Aircraft identification and certification data plates including:
- **Main Data Plate (PNR-02-10-001):** Primary aircraft identification with serial number, type certificate, and certification data
- **Weight Data Plate (PNR-02-10-002):** Empty weight, CG position, and weighing date information

### 2. MARKING_SYSTEMS
Permanent and semi-permanent marking systems for aircraft identification and maintenance reference:
- **Serial Number Marking (PNR-02-10-101):** Laser engraved serial numbers on primary structure
- **Station Marking Set (PNR-02-10-102):** Fuselage station, waterline, and buttock line reference decals
- **CG Reference Markers (PNR-02-10-103):** Center of gravity datum and limit indicators

### 3. MEASUREMENT_EQUIPMENT
Ground support equipment for dimensional verification and weight & balance operations:
- **Weighing Kit (PNR-02-10-201):** Complete aircraft weighing system with 200-ton capacity
- **Dimension Measurement Tools (PNR-02-10-202):** Precision measurement instruments for conformity inspections
- **CG Calculation Tools (PNR-02-10-203):** Software and hardware for weight & balance calculations

### 4. CONFIGURATION_CONTROL
Configuration management and interchangeability documentation:
- **Configuration_Items_Registry.csv:** Tracking of all configuration items, versions, and status
- **Interchangeability_Matrix.csv:** Part substitution rules and alternate part numbers

## Status

✅ **Complete** - Structure implemented with comprehensive documentation

This section includes:
- Complete part number registry
- Detailed specifications for all components
- Configuration control documentation
- Installation and operational procedures
- Cross-referenced with maintenance manuals

## BWB-Specific Considerations

The AMPEL360 BWB H2 Hy-E configuration requires specialized approaches for:
- **Datum Reference:** Forward datum at Station 0 (nose apex)
- **MAC Definition:** Modified for blended wing configuration (Station 450-750)
- **CG Range:** 15-35% MAC for normal operations
- **Station Marking:** Adapted for continuous wing-body blend surface
- **Weighing Points:** Three-point configuration optimized for BWB load distribution

## Related Documents

- Parent Component: 02-10-00_AIRCRAFT_GENERAL_DATA
- ATA Chapter: 02 - Operations Information
- AMPEL360 Platform: BWB H2 Hy-E Q100 INTEGRA
- Aircraft Maintenance Manual (AMM) Chapter 02-10
- Weight and Balance Manual
- Type Certificate Data Sheet

## Cross-References

- **ATA 05:** Time Limits/Maintenance Checks (weighing intervals)
- **ATA 06:** Dimensions and Areas (dimensional standards)
- **ATA 07:** Lifting and Shoring (jack point locations)
- **ATA 28:** Fuel (fuel system weights and moments)

---

**Document Control:**
- Version: 2.0
- Status: Complete
- Last Updated: 2025-11-05
- Change Summary: Complete subsystem implementation with part numbers, specifications, and configuration control
