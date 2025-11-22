# 85-90 Tables, Schemas & Diagrams

## Overview

This directory contains comprehensive technical tables, data dictionaries, system diagrams, and reference documentation for ATA Chapter 85 - Infrastructure Interface Standards. These materials support the design, operation, and maintenance of ground infrastructure systems that interface with AMPEL360 BWB-H2-Hy-E aircraft.

## Purpose

Centralized repository for:
- **Master Equipment Tables**: Equipment inventory and specifications
- **System Interface Matrices**: Interface definitions and connectivity
- **Technical Diagrams**: Electrical, P&ID, and site layout drawings
- **Reference Tables**: Drawing indexes, data dictionaries, specifications
- **Performance Data**: Load schedules, specifications, safety distances

## Scope

This is a **cross-ATA root bucket** present in every ATA chapter. For ATA 85, it specifically covers:
- Hydrogen (H2) refueling and storage infrastructure
- Electrical ground power and distribution systems
- Ground support equipment interfaces
- Facility safety and monitoring systems
- Site planning and layout documentation

## Contents

### Primary Files

#### 1. **85-90-01_Master_Equipment_Tables.csv**
Complete inventory of ground infrastructure equipment including:
- H2 refueling dispensers and storage systems
- Electrical ground power units and substations
- Ground support equipment (GSE)
- Safety and monitoring systems
- Utility systems (air, water, etc.)

**Fields**: Equipment_ID, Equipment_Name, ATA_Chapter, System_Category, Manufacturer, Model, Capacity, Power_Rating, Location, Status, Certification_Ref

#### 2. **85-90-02_System_Interface_Matrix.csv**
Comprehensive interface definitions between infrastructure systems and aircraft:
- Physical connections (mechanical, electrical, fluid)
- Communication protocols and data interfaces
- Safety interlocks and control signals
- Performance specifications per interface

**Fields**: Interface_ID, From_System, To_System, Interface_Type, Protocol_Standard, Data_Rate, Physical_Connector, Criticality, Status

#### 3. **85-90-03_Electrical_Single_Line_Diagrams.svg**
Electrical power distribution single-line diagrams showing:
- Utility supply and main transformers
- Primary and emergency power distribution
- H2 facility electrical systems
- Ground power unit circuits
- Emergency generator and ATS

**Format**: SVG (Scalable Vector Graphics) - placeholder for professional CAD drawings

#### 4. **85-90-04_H2_PandID_Diagrams.svg**
Hydrogen system Piping & Instrumentation Diagrams (P&ID) including:
- LH2 storage and cryogenic systems
- Vaporization and pressure control
- Distribution piping and dispensing
- Safety systems (PSV, leak detection, fire suppression)
- Instrumentation and control loops

**Format**: SVG - placeholder for professional P&ID tools (AutoCAD P&ID, SmartPlant)
**Standards**: ISO 14687, ASME B31.12, NFPA 2, IEC 60079

#### 5. **85-90-05_Site_Layout_Master_Plan.svg**
Overall site layout and facility master plan showing:
- Terminal building and maintenance hangar
- Aircraft parking stands and apron area
- H2 production and storage facility
- Electrical substation and emergency generator
- Safety zones and perimeter security
- Access roads and service areas

**Format**: SVG - placeholder for professional civil/architectural CAD

#### 6. **85-90-06_Drawing_Index.csv**
Master index of all technical drawings with:
- Drawing numbers and titles
- Discipline (Civil, Electrical, Process, etc.)
- Revision status and dates
- Responsible parties (Drawn By, Checked By, Approved By)
- File paths and cross-references

**Total Drawings**: 30 indexed (conceptual and to-be-developed)

#### 7. **85-90-07_Data_Dictionary.csv**
Comprehensive data element definitions for all monitored parameters:
- H2 tank levels, pressures, temperatures
- Electrical voltage, current, power, frequency
- Flow rates and mass measurements
- Safety sensor data (leak detection, fire alarms)
- Environmental data (weather, wind, pressure)
- Operational data (stand occupancy, flight info, service status)

**Total Elements**: 40 data elements with metadata (type, units, valid ranges, quality rules)

#### 8. **85-90-08_Performance_Specifications.csv**
Detailed performance specifications for all infrastructure systems:
- H2 refueling and storage system parameters
- Electrical system specifications (voltage, frequency, power quality)
- Ground support equipment performance
- Safety system requirements (detection, response times)
- SCADA and control system specifications

**Total Specifications**: 50 performance parameters with min/max/nominal values and test methods

#### 9. **85-90-09_Load_Schedule.csv**
Electrical load schedule for all facility loads:
- Connected loads and demand factors
- Power factor and voltage levels
- Circuit breaker and feeder assignments
- Load categories and priorities
- Operating hours and duty cycles

**Total Loads**: 50 electrical loads across all facility systems

#### 10. **85-90-10_Safety_Distance_Tables.csv**
Safety separation distances per regulatory requirements:
- H2 facility to property lines, buildings, ignition sources
- Aircraft stand clearances and obstacle-free zones
- Fire protection equipment spacing
- Jet blast and propeller safety zones
- Environmental protection distances

**Total Safety Zones**: 50 separation requirements with regulatory basis (NFPA 2, ICAO, EPA, etc.)

### ASSETS Subdirectories

#### `ASSETS/Diagrams/`
Reserved for detailed technical diagrams:
- Full electrical single-line diagrams
- Complete H2 P&IDs (all sheets)
- Architectural and civil drawings
- Control system architecture diagrams
- Network topology diagrams

#### `ASSETS/Tables/`
Reserved for supplementary data tables:
- Equipment maintenance schedules
- Spare parts catalogs
- Material specifications
- Test and inspection records

#### `ASSETS/Schemas/`
Reserved for data schemas and formats:
- Database schemas
- API specifications
- Data exchange formats (XML, JSON)
- Configuration files

## Naming Convention

Files follow the pattern: **85-90-XX_DESCRIPTION**
- **85** = ATA Chapter (Infrastructure Interface Standards)
- **90** = Bucket number (Tables, Schemas, Diagrams)
- **XX** = Sequential number (01, 02, 03, etc.)
- **DESCRIPTION** = Descriptive file name

## Standards and Compliance

### Hydrogen Systems
- [ISO 14687:2019](https://www.iso.org/standard/69539.html) - Hydrogen fuel quality specifications
- [ASME B31.12](https://www.asme.org/codes-standards/find-codes-standards/b31-12-hydrogen-piping-pipelines) - Hydrogen piping and pipelines
- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) - Hydrogen technologies code
- [SAE AS 6858](https://www.sae.org/standards/content/as6858/) - H2 ground vehicle fueling connection devices

### Electrical Systems
- [IEEE C84.1](https://standards.ieee.org/ieee/C84.1/6700/) - Voltage ratings for electric power systems
- [IEEE 519](https://standards.ieee.org/ieee/519/6421/) - Harmonic control in electrical power systems
- [MIL-STD-704F](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35789) - Aircraft electric power characteristics
- [DO-160G](https://www.rtca.org/product/do-160g/) - Environmental conditions and test procedures for airborne equipment

### Safety and Fire Protection
- [NFPA 409](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=409) - Aircraft hangars
- [IEC 60079](https://webstore.iec.ch/publication/593) - Explosive atmospheres
- [IEC 62305](https://webstore.iec.ch/publication/20117) - Protection against lightning

### Aviation and Airport Standards
- [ICAO Annex 14](https://www.icao.int/safety/airnavigation/nationalitymarks/annexes_booklet_en.pdf) - Aerodromes
- [SAE AS 4073](https://www.sae.org/standards/content/as4073/) - Minimum performance standard for pre-conditioned air equipment

### Civil and Structural
- [ASME BPVC Section VIII](https://www.asme.org/codes-standards/find-codes-standards/bpvc-viii-1-bpvc-section-viii-rules-construction-pressure-vessels-division-1) - Pressure vessels
- [EN 13458](https://standards.iteh.ai/catalog/standards/cen/c3f2e6f8-8e8b-4f8a-8f4e-d1f9e9f5e8e8/en-13458-2-2016) - Cryogenic vessels

## Usage Guidelines

### For Engineers
1. **Equipment Selection**: Reference 85-90-01 for equipment inventory and 85-90-08 for performance specs
2. **Interface Design**: Use 85-90-02 for interface requirements and connection standards
3. **Electrical Design**: Review 85-90-03 (SLD), 85-90-09 (loads), and 85-90-08 (specs)
4. **H2 System Design**: Study 85-90-04 (P&ID) and safety distances in 85-90-10
5. **Site Planning**: Reference 85-90-05 for facility layout and 85-90-10 for clearances

### For Operations
1. **Data Monitoring**: Use 85-90-07 for parameter definitions and valid ranges
2. **Equipment Identification**: Reference 85-90-01 for equipment locations and specs
3. **Safety Compliance**: Follow separation distances in 85-90-10
4. **Interface Procedures**: Consult 85-90-02 for connection protocols

### For Maintenance
1. **Equipment Access**: Use 85-90-01 for equipment details and locations
2. **Drawing Retrieval**: Reference 85-90-06 drawing index for specific drawings
3. **Performance Verification**: Check 85-90-08 for test methods and acceptance criteria

### For Certification
1. **Compliance Evidence**: Tables link to applicable standards and regulations
2. **Safety Analysis**: Use 85-90-10 for hazard separation compliance
3. **Interface Control**: 85-90-02 documents interface specifications per standards
4. **Traceability**: All entries include certification references where applicable

## Important Notes

### Placeholder Status
Files **85-90-03** (Electrical SLD), **85-90-04** (H2 P&ID), and **85-90-05** (Site Layout) are **conceptual placeholders** created in SVG format. These diagrams:
- Provide high-level overview and structure
- Must be replaced with professional CAD drawings
- Require development by licensed engineers using:
  - **Electrical**: AutoCAD Electrical, EPLAN, or equivalent
  - **Process**: AutoCAD P&ID, SmartPlant P&ID, or equivalent
  - **Civil/Architectural**: AutoCAD Civil 3D, Revit, or equivalent

### Data Quality
All CSV files contain representative data structures with sample entries. Before operational use:
- Verify all equipment specifications with manufacturers
- Validate interface parameters through testing
- Confirm safety distances with site-specific risk assessments
- Update data dictionary with actual SCADA tag names
- Conduct electrical load studies for final load schedule

### Regulatory Compliance
This documentation references multiple standards and regulations. Users must:
- Obtain and review complete standard documents
- Ensure compliance with latest revisions
- Verify local code requirements
- Obtain necessary permits and approvals
- Conduct required inspections and testing

## Internal Structure

The structure is **design-driven** and flexible:
- Organized by technical discipline and system type
- No mandatory lifecycle folder duplication within this bucket
- Traceability to lifecycle phases maintained via metadata and cross-references
- Drawing index (85-90-06) provides comprehensive navigation

## Maintenance and Updates

### Version Control
- All files under Git version control
- Drawing revisions tracked in 85-90-06
- Data dictionaries versioned with SCADA system releases
- Safety distance tables updated with regulatory changes

### Update Frequency
- **Equipment Tables**: Update with additions/modifications to infrastructure
- **Interface Matrix**: Update with aircraft or ground equipment changes
- **Technical Diagrams**: As-built updates after construction/modifications
- **Data Dictionary**: Sync with SCADA system configuration changes
- **Performance Specs**: Update with equipment upgrades or new test data
- **Load Schedule**: Update after electrical system modifications
- **Safety Distances**: Review annually and with regulatory updates

### Responsible Parties
- **Infrastructure Engineering**: Equipment tables, specifications, load schedules
- **Process Engineering**: H2 P&IDs, safety distance tables
- **Electrical Engineering**: Electrical diagrams, load schedules
- **Control Systems**: Data dictionary, SCADA documentation
- **Safety Engineering**: Safety distance tables, hazard analysis
- **Civil Engineering**: Site layout, facility drawings

## Cross-References

### Related ATA 85 Documentation
- [85-00-03 Requirements](../../85-00_GENERAL/85-00-03_Requirements/) - System requirements traceability
- [85-00-04 Design](../../85-00_GENERAL/85-00-04_Design/) - Design specifications and rationale
- [85-00-05 Interfaces](../../85-00_GENERAL/85-00-05_Interfaces/) - Detailed interface control documents
- [85-00-06 Engineering](../../85-00_GENERAL/85-00-06_Engineering/) - Engineering analysis and models
- [85-00-10 Certification](../../85-00_GENERAL/85-00-10_Certification/) - Certification evidence packages
- [85-10 Operations](../../85-10_Operations/) - Operational procedures for ground infrastructure

### Related ATA Chapters
- [ATA 02 - Operations Information](/ATA_02-OPERATIONS_INFORMATION/) - Flight operations data
- [ATA 10 - Parking, Mooring, Storage](/ATA_10-PARKING_MOORING_STORAGE_RTS/) - Aircraft ground handling
- [ATA 13 - Hardware and General Tools](/ATA_13-HARDWARE_AND_GENERAL_TOOLS/) - GSE specifications

## Status

- **Bucket**: 90_Tables_Schemas_Diagrams
- **Status**: Active - Initial implementation complete
- **Applicability**: Universal (all ATA chapters)
- **Implementation Date**: 2025-11-22
- **Last Updated**: 2025-11-22

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status**: DRAFT - Subject to human review and approval
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22
- **Standard**: OPT-IN Framework v1.1
- **Owner**: AMPEL360 Infrastructure Documentation Team

---

**© 2025 AMPEL360. All rights reserved.**

*This documentation is part of the AMPEL360 BWB-H2-Hy-E program and is subject to the terms and conditions specified in the repository LICENSE file.*
