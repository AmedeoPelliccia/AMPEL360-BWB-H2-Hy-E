# MSN Geometry Data Linkage

**Component Code:** 02-11-00  
**Folder:** 09_PRODUCTION_PLANNING/SERIAL_NUMBER_MANAGEMENT  
**Document:** MSN_Geometry_Data_Linkage.md

## Purpose

This document defines how dimensional and geometric datasets (measurement files, as-built records, CAD models) are linked to each Manufacturer Serial Number (MSN) for the AMPEL360 BWB H₂ Hy-E aircraft, ensuring complete traceability throughout the aircraft lifecycle.

## Overview

MSN geometry data linkage establishes a comprehensive digital thread connecting:
- Design geometry (CAD models, baseline_dimensions.json)
- Manufacturing measurements (CMM, laser tracker, photogrammetry)
- As-built configuration records (as_built_geometry_MSN-XXX.json)
- Certification data (TCDS, AFM dimensional sections)
- Operational data (maintenance, modifications)
- CAOS digital twin (real-time geometry model)

This linkage enables:
- Traceability: Any dimension traceable to source measurement and design intent
- Configuration management: Geometry changes tracked through aircraft life
- Quality assurance: Dimensional conformance verified at each lifecycle stage
- Maintenance planning: As-built geometry informs spare parts, clearances, repairs
- Fleet analytics: Dimensional trends analyzed across multiple aircraft

## Data Linkage Architecture

### Primary MSN Identifier

**MSN Format:** MSN-[Type][Number]
- **Type:**
  - P: Prototype (MSN-P001)
  - PP: Pre-Production (MSN-PP001 to MSN-PP010)
  - [Numeric]: Serial Production (MSN-001, MSN-002, ...)
- **Number:** Sequential within type

**MSN as Key:** All geometry datasets tagged with MSN as primary key for database linking

### Geometry Data Hierarchy

```
MSN-XXX (Aircraft)
├── Build Standard (BS-XXX)
│   ├── baseline_dimensions.json (vX.X)
│   └── CAD Model (Release RX.X)
├── As-Built Measurements
│   ├── Component Measurements
│   │   ├── CMM Reports (Component SN → MSN linkage)
│   │   ├── Laser Tracker Sessions
│   │   └── Optical Scans
│   ├── Assembly Measurements
│   │   ├── Photogrammetry Projects
│   │   └── Laser Tracker Global Verification
│   └── Final Assembly Measurements
│       ├── Overall Dimensions (Photogrammetry)
│       └── Ground Clearances (Manual + Photogrammetry)
├── As-Built Configuration
│   ├── as_built_geometry_MSN-XXX.json
│   ├── Principal_Dimensions_MSN-XXX.csv
│   ├── Geometry_Parameters_MSN-XXX.csv
│   └── Deviation_Analysis_Report_MSN-XXX.pdf
├── Certification Data
│   ├── TCDS_Dimension_Data_MSN-XXX.xlsx
│   └── AFM_Dimension_Data_MSN-XXX.xlsx
└── Operational Data
    ├── Maintenance_Geometry_Records
    ├── Modification_Geometry_Updates
    └── CAOS_Digital_Twin_Geometry
```

## Data Linking Methods

### Method 1: Database Relational Linkage

**Production Database Schema:**

**Table: MSN_Master**
- MSN (Primary Key)
- Build_Standard
- Manufacturing_Start_Date
- Delivery_Date
- Customer
- Status

**Table: Geometry_Datasets**
- Dataset_ID (Primary Key)
- MSN (Foreign Key → MSN_Master)
- Dataset_Type (Design, Measurement, As-Built, Certification, Operational)
- Dataset_Name (e.g., "as_built_geometry_MSN-P001.json")
- File_Path (location in file system or document management system)
- Date_Created
- Created_By
- Version
- Status (Draft, Approved, Archived)

**Table: Measurements**
- Measurement_ID (Primary Key)
- MSN (Foreign Key → MSN_Master)
- Dataset_ID (Foreign Key → Geometry_Datasets)
- Measurement_Type (CMM, Laser_Tracker, Photogrammetry, Optical_Scan, Manual)
- Measurement_Date
- Equipment_ID
- Operator
- Measurement_File_Path
- Status (Valid, Superseded, Rejected)

**Table: Dimensions**
- Dimension_ID (Primary Key)
- MSN (Foreign Key → MSN_Master)
- Dimension_Name (e.g., "Overall_Length", "Wingspan")
- Nominal_Value (from baseline_dimensions.json)
- As_Built_Value (from measurement)
- Tolerance
- Deviation
- Unit
- Measurement_ID (Foreign Key → Measurements, traceability to source)
- Status (Within_Tolerance, Accepted_Deviation, Out_of_Tolerance)

**Queries for Linkage:**
- Get all geometry datasets for MSN: `SELECT * FROM Geometry_Datasets WHERE MSN = 'MSN-P001'`
- Get as-built dimensions for MSN: `SELECT * FROM Dimensions WHERE MSN = 'MSN-P001'`
- Trace dimension to measurement: `SELECT * FROM Measurements WHERE Measurement_ID = (SELECT Measurement_ID FROM Dimensions WHERE Dimension_Name = 'Wingspan' AND MSN = 'MSN-P001')`

### Method 2: File Naming Convention

**Standardized File Names:**
- **As-built geometry:** `as_built_geometry_MSN-XXX.json`
- **Measurement files:** `[MeasurementType]_MSN-XXX_[Component]_[Date].ext`
  - Example: `PhotogrammetrySession_MSN-P001_FinalAssembly_20270630.vstar`
  - Example: `CMM_Report_MSN-P001_CenterBodySection1_20270315.pdf`
- **Dimensional data:** `[DataType]_MSN-XXX_[Version].csv`
  - Example: `Principal_Dimensions_MSN-P001_v1.0.csv`

**Directory Structure:**
```
/Production_Data/
  /MSN-P001/
    /Measurements/
      /CMM/
      /Laser_Tracker/
      /Photogrammetry/
      /Optical_Scan/
    /As_Built_Configuration/
    /Certification/
    /Delivery_Package/
  /MSN-PP001/
    ...
```

**Advantage:** File system organization mirrors MSN structure, easy manual navigation

### Method 3: Metadata Embedding

**Within Data Files:**

**JSON Files (as_built_geometry_MSN-XXX.json):**
```json
{
  "metadata": {
    "MSN": "MSN-P001",
    "Build_Standard": "BS-001",
    "Baseline_Dimensions_Version": "v1.0",
    "CAD_Model_Release": "R1.0",
    "Date_Created": "2027-06-30",
    "Created_By": "J. Smith (QA Inspector)",
    "Status": "Approved"
  },
  "dimensions": {
    "overall_length_m": {
      "nominal": 48.50,
      "as_built": 48.52,
      "tolerance": 0.10,
      "deviation": 0.02,
      "measurement_id": "MEAS-2027-0450",
      "measurement_file": "PhotogrammetrySession_MSN-P001_FinalAssembly_20270630.vstar"
    },
    ...
  }
}
```

**CSV Files (header metadata):**
```csv
# MSN: MSN-P001
# Build Standard: BS-001
# Date Created: 2027-06-30
# Created By: J. Smith
Dimension_Name,Nominal_Value,As_Built_Value,Tolerance,Deviation,Unit,Status
Overall_Length,48.50,48.52,0.10,0.02,m,Within_Tolerance
...
```

**Advantage:** Metadata travels with file, linkage preserved if file moved

### Method 4: Digital Twin Linkage (CAOS System)

**CAOS Digital Twin Architecture:**
- Each MSN has dedicated digital twin instance in CAOS system
- Digital twin geometry model initially populated from build standard baseline
- As measurements captured, digital twin updated with as-built geometry
- All geometry datasets linked to digital twin via database

**CAOS Geometry Data Model:**
- **Digital Twin ID:** Unique identifier for each aircraft digital twin (maps to MSN)
- **Geometry Layer:** 3D model representing as-built geometry
- **Metadata Layer:** Links to source data (measurements, as-built files, CAD models)
- **History Layer:** Tracks geometry changes over time (baseline → as-built → post-modification)

**CAOS Linkage Workflow:**
1. MSN created in CAOS at manufacturing start → Digital twin instantiated
2. Build standard geometry loaded into digital twin (nominal dimensions)
3. Measurements uploaded to CAOS → Linked to MSN → Digital twin updated
4. As-built configuration finalized → Locked in digital twin (baseline for operations)
5. Modifications during life → Geometry updates → Digital twin revised

**Advantage:** Single source of truth for aircraft geometry, real-time access, automated updates

## Data Linkage Lifecycle

### Phase 1: Design (Before Manufacturing)

**Data Created:**
- Build standard definition (BS-XXX)
- baseline_dimensions.json (version for build standard)
- CAD model release (RX.X)

**Linkage:**
- MSN assigned to build standard in configuration management system
- MSN record created in production database
- CAOS digital twin instantiated for MSN with build standard geometry

**Traceability:** MSN → Build Standard → Baseline Dimensions → CAD Model

### Phase 2: Manufacturing (Component and Assembly)

**Data Created:**
- Component CMM reports (component SN linked to MSN via bill of materials)
- Assembly laser tracker sessions
- Optical scans of critical surfaces

**Linkage:**
- Measurement files named with MSN identifier
- Measurement records created in database with MSN foreign key
- CAOS ingests measurement data and associates with MSN digital twin

**Traceability:** MSN → Measurement Files → Component SN → Assembly Records

### Phase 3: Final Assembly

**Data Created:**
- Overall dimensions (photogrammetry)
- Ground clearances (photogrammetry + manual)
- Control surface geometry
- Reference system verification

**Linkage:**
- Final assembly measurement files stored in MSN directory
- Database records created for each dimension measured
- CAOS digital twin updated with final as-built geometry

**Traceability:** MSN → Final Assembly Measurements → As-Built Geometry

### Phase 4: As-Built Configuration Freeze

**Data Created:**
- as_built_geometry_MSN-XXX.json (comprehensive as-built record)
- Principal_Dimensions_MSN-XXX.csv
- Geometry_Parameters_MSN-XXX.csv
- Deviation_Analysis_Report_MSN-XXX.pdf

**Linkage:**
- As-built files linked to MSN in database
- As-built configuration locked in CAOS (cannot be changed without formal modification)
- Certification data generated from as-built configuration

**Traceability:** MSN → As-Built Configuration → Measurement Sources → Build Standard Baseline

### Phase 5: Certification and Delivery

**Data Created:**
- TCDS_Dimension_Data_MSN-XXX.xlsx
- AFM_Dimension_Data_MSN-XXX.xlsx
- Customer delivery data package

**Linkage:**
- Certification data linked to MSN and as-built configuration
- Customer delivery package contains complete dimensional traceability
- CAOS digital twin includes certification-approved geometry

**Traceability:** MSN → Certification Data → As-Built Configuration → Customer Delivery Package

### Phase 6: Operations and Maintenance

**Data Created:**
- Maintenance geometry records (wear, damage, repairs affecting dimensions)
- Modification geometry updates (service bulletins, alterations)
- In-service measurement data (if dimensional inspection required)

**Linkage:**
- Maintenance records linked to MSN in CAOS
- Modification geometry updates revise CAOS digital twin
- Historical geometry data preserved for lifecycle analysis

**Traceability:** MSN → Operational Geometry History → Maintenance Records → Modification Records

## Quality Assurance of Data Linkage

### Linkage Verification Checks

**Check 1: MSN Identifier Consistency**
- Verify MSN identifier is consistent across all datasets for an aircraft
- No typos or variations (e.g., "MSN-P001" vs. "MSN-P-001" vs. "P001")
- Automated script checks MSN format compliance

**Check 2: Database Referential Integrity**
- Verify all foreign key relationships valid (no orphaned records)
- Verify each measurement linked to valid MSN
- Verify each dimension traced to valid measurement

**Check 3: File Naming Compliance**
- Verify all measurement files follow naming convention
- Verify MSN in filename matches MSN in file metadata (if applicable)
- Verify files stored in correct MSN directory

**Check 4: Metadata Completeness**
- Verify all geometry datasets have complete metadata (MSN, date, author, version)
- Verify traceability fields populated (measurement_id, measurement_file)
- Verify no missing or "TBD" values in production data

**Check 5: CAOS Digital Twin Synchronization**
- Verify CAOS digital twin geometry matches as-built configuration
- Verify all measurements uploaded to CAOS and linked to correct MSN
- Verify no discrepancies between CAOS and production database

### Linkage Audit

**Frequency:** Quarterly for active MSNs, at delivery for completed aircraft

**Audit Procedure:**
1. Select sample MSN (prototype, pre-production, or production aircraft)
2. Retrieve all geometry datasets for sample MSN from database
3. Verify each dataset accessible and correctly named
4. Verify traceability chain: Design → Measurement → As-Built → Certification → Delivery
5. Verify CAOS digital twin matches as-built configuration
6. Document findings and corrective actions

**Responsible Party:** Quality Engineering, Configuration Management

## Integration with Configuration Management

### MSN Configuration Baseline

**Dimensional Baseline Established:**
- At as-built configuration freeze (post-final assembly)
- Includes: as_built_geometry_MSN-XXX.json, Principal_Dimensions_MSN-XXX.csv
- Approved by: Responsible Engineer, QA Manager, Configuration Manager
- Stored in: Configuration management system, CAOS digital twin

**Baseline Change Control:**
- Any change to MSN dimensional configuration requires formal change process
- Engineering Change Request (ECR) or Service Bulletin (SB) documents change
- Change linked to MSN in database and CAOS
- Revised geometry data generated with version control

### Fleet Configuration Management

**Fleet-Wide Geometry Analysis:**
- Configuration manager can query database for dimensional data across fleet
- Identify aircraft with specific dimensional characteristics (e.g., all aircraft with wingspan ≥65.5 m)
- Support fleet-wide modifications or service bulletins
- Analyze dimensional trends (e.g., manufacturing drift over time)

**Configuration Status Accounting:**
- Generate configuration reports showing dimensional status of each MSN
- Track which MSNs have incorporated specific dimensional changes
- Support customer queries about specific aircraft geometry

## Related Documents

- `09_PRODUCTION_PLANNING/DATA_GENERATION/As_Built_Geometry_Configuration.md` – As-built data capture
- `09_PRODUCTION_PLANNING/DATA_GENERATION/Dimension_Data_Production_02-11-00.md` – Data file generation
- `09_PRODUCTION_PLANNING/SERIAL_NUMBER_MANAGEMENT/Dimensional_Build_Standard_Control.md` – Build standard management
- `09_PRODUCTION_PLANNING/SERIAL_NUMBER_MANAGEMENT/Dimensional_Configuration_Tracking.csv` – MSN configuration tracking table
- `14_META_GOVERNANCE/` – Configuration management procedures
- CAOS Digital Twin User Guide
- Production Database Schema Documentation

---

**Document Control:**
- Version: 1.0
- Status: Template
- Last Updated: 2025-11-11
- Classification: Configuration Critical
