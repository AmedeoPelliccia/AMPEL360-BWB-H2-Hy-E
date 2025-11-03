# 12_ASSETS_MANAGEMENT - ATA 51: Standard Practices and Structures - General

## Purpose
This folder contains assets management documentation for ATA 51 structural systems, including spare parts inventory, tooling, ground support equipment, and logistics.

## Contents
- Spare parts catalog
- Tooling inventory
- Ground support equipment (GSE) specifications
- Logistics and supply chain management
- Asset tracking and control
- Calibration and maintenance of equipment
- Asset lifecycle management
- Provisioning analysis

## Key Assets Management Documents
- `Structural_Spare_Parts_Catalog.md` - Illustrated parts catalog (IPC)
- `Tooling_Inventory.md` - Production and maintenance tooling
- `GSE_Specifications.md` - Ground support equipment for structural maintenance
- `SHM_Sensor_Inventory.md` - Spare sensors, replacement schedule
- `NDT_Equipment_Calibration.md` - Inspection equipment maintenance and calibration
- `Logistics_Plan.md` - Supply chain management, warehousing, distribution

## Spare Parts Management

### Structural Components
- **Rotable Parts:** Landing gear attachments, door hinges, access panels
- **Expendable Parts:** Fasteners, sealants, adhesives, potting compounds
- **Repairable Parts:** Composite panels (damaged parts sent for repair)

### SHM System Components
- **FBG Sensors:** 50 spare sensors per aircraft (5% of installed base)
- **PZT Sensors:** 30 spare sensors per aircraft
- **Acoustic Emission Sensors:** 10 spare sensors per aircraft
- **Temperature Sensors:** 20 spare sensors per aircraft
- **Data Acquisition Units:** 2 spare DAU per 10 aircraft

### Repair Materials
- **Composite Materials:** Prepreg patches (shelf life: 12 months at -18°C)
- **Adhesives:** Structural adhesives (Cytec FM 300, Hysol EA 9396)
- **Honeycomb Core:** Nomex core blocks (various densities)
- **Fasteners:** Hi-Lok, Hi-Lite fasteners (multiple sizes)

## Tooling Assets

### Production Tooling
- Composite layup molds
- Autoclave tooling
- Assembly fixtures and jigs
- CNC machining fixtures

### Maintenance Tooling
- Composite repair tools (vacuum bagging, heat blankets)
- Fastener installation tools (torque wrenches, rivet guns)
- SHM sensor replacement tools
- Access and lifting equipment

### Calibration Requirements
- **Torque Wrenches:** Annual calibration (±4% accuracy)
- **Ultrasonic Flaw Detectors:** Annual calibration (reference block verification)
- **Thermographic Cameras:** Annual calibration (blackbody source)

## Ground Support Equipment (GSE)

### Structural Inspection Equipment
- **Ultrasonic NDT:** Olympus OmniScan, GE Phasor XS
- **Thermographic NDT:** FLIR T1030sc infrared camera
- **Shearography:** Dantec Dynamics Q-800 system
- **Borescopes:** Olympus IPLEX GX/GT industrial videoscopes

### Repair Equipment
- **Vacuum Bagging Equipment:** Vacuum pumps, leak detectors, consumables
- **Heat Application:** Heat blankets, thermocouples, controllers
- **Composite Cure Equipment:** Portable ovens for field repairs
- **Adhesive Mixing Equipment:** Dual-cartridge dispensers, static mixers

### SHM Equipment
- **Sensor Installation Kits:** Specialized tools for FBG, PZT sensor bonding
- **Data Acquisition Test Equipment:** Optical spectrum analyzer, function generator
- **Calibration Equipment:** Strain gauge simulator, temperature calibrator

## Provisioning Analysis

### Initial Provisioning
- Spare parts for first 5 years of operation
- Based on reliability data from similar composite aircraft
- Adjusted for AMPEL360 unique features (BWB, SHM, cryogenic)

### Provisioning Metrics
- **Mean Time Between Failure (MTBF):** Structural components (>100,000 FH)
- **Mean Time To Repair (MTTR):** Composite patch repair (8-24 hours)
- **Stock Levels:** 95% availability (parts available when needed)
- **Reorder Point:** Trigger restocking when inventory drops below safety level

### Fleet-Level Optimization
- Service Twin predicts spare parts demand across fleet
- Pre-position spare parts at major hubs (minimize AOG)
- Coordinate repairs across fleet (optimize hangar utilization)

## Asset Tracking and Control

### Inventory Management
- **Parts Tracking:** Barcodes, RFID tags for serialized parts
- **Lot Traceability:** Material lots tracked from manufacturing to installation
- **Shelf Life Management:** Prepreg and adhesive expiration tracking
- **Consumables Tracking:** Usage rates and reorder triggers

### Tooling Control
- **Tool Calibration:** Track calibration status and due dates
- **Tool Maintenance:** Preventive maintenance schedules
- **Tool Allocation:** Assign tools to specific maintenance tasks
- **Tool Retirement:** Remove tools at end of service life

## Asset Lifecycle Management

### Acquisition
- Procurement of spare parts, tooling, GSE
- Supplier selection and qualification
- Quality assurance and acceptance testing

### Utilization
- Issue parts/tools/equipment for maintenance tasks
- Track usage, remaining life, condition

### Maintenance
- Preventive maintenance of tooling and GSE
- Calibration of inspection equipment
- Repair or replacement of damaged assets

### Disposal
- Retire assets at end of service life
- Environmentally responsible disposal (composite waste recycling)
- Update inventory records

## Related Folders
- `09_PRODUCTION_PLANNING` - Production tooling requirements
- `11_OPERATIONS_AND_MAINTENANCE` - Spare parts usage and maintenance procedures
- `13_SUBSYSTEMS_AND_COMPONENTS` - Component specifications for spares

## Document Status
**Status:** Active Development  
**Last Updated:** 2025-11-03  
**Next Review:** 2025-12-01
