# ATA 06: Dimensions and Areas

**PROGRAM CHAPTER STATUS:** ATA 06 is a foundational chapter within P-PROGRAM that establishes the official dimensional data for the AMPEL360 aircraft. This data is critical for ground handling, hangar planning, maintenance access, regulatory compliance, and operational procedures.

## Scope and Structure
This chapter documents all physical dimensions, surface areas, volumes, and geometric characteristics of the aircraft, including:
- **Overall Dimensions:** Length, width, height, wingspan
- **Surface Areas:** Wing, control surfaces, wetted area
- **Volumes:** Fuel tanks, cargo holds, equipment bays
- **Access Dimensions:** Doors, hatches, panels
- **Clearance Requirements:** Ground equipment, maintenance access
- **Zonal Definitions:** Maintenance zones and access coordinates

## The 14-Folder Skeleton
Every 6-digit component within this chapter represents a formal dimensional specification or geometric dataset. Each component is managed through the full lifecycle skeleton to ensure requirements traceability, design verification, measurement validation, and configuration control.

## Regulatory Framework

### Certification Requirements
- **CS-25.783:** Doors (minimum dimensions, emergency egress)
- **CS-25.1359:** Electrical System Fire Protection (compartment dimensions)
- **FAA AC 150/5300-13B:** Airport Design (aircraft parking envelope)
- **ICAO Annex 14:** Aerodromes (aircraft reference code dimensions)
- **AHM 560:** Airplane Characteristics for Airport Planning

### Industry Standards
- **ATA iSpec 2200 Chapter 06:** Standard dimensional data format
- **SAE ARP6116:** Aircraft Ground Support Equipment Clearances
- **ISO 3977:** Aircraft Dimensions and Masses
- **IATA Airport Handling Manual (AHM):** Standard dimensional data exchange

## AMPEL360 Unique Characteristics

### 1. **Blended Wing Body (BWB) Geometry**
The AMPEL360 has no conventional fuselage-wing distinction, presenting unique dimensional challenges:

**Dimensional Definition Challenges:**
- **Wingspan:** Measured at maximum lateral extent (includes winglets/endplates)
- **Length:** Nose to aft-most point (no tail cone reference)
- **Height:** Ground to highest point (propulsor nacelle top)
- **Reference Datum:** Established at nose apex (not conventional firewall)

**Solution Approach:**
- Define **BWB Reference System (BRS):** X-axis (longitudinal), Y-axis (lateral), Z-axis (vertical)
- Origin at nose apex, X+ aft, Y+ right, Z+ up
- All dimensions referenced to BRS per SAE AS8015 (Aircraft Coordinate System)

### 2. **Cryogenic Hydrogen Tanks**
LH₂ storage tanks occupy significant internal volume requiring precise documentation:

**Tank Dimensional Data:**
- **Inner Vessel Volume:** 12,500 liters (usable) + 500 liters (ullage) = 13,000 L total
- **Outer Vessel Dimensions:** 6.2m length × 3.8m diameter (including vacuum jacket)
- **Insulation Thickness:** 150mm multi-layer insulation (MLI) in annular vacuum space
- **Clearance Envelope:** 500mm minimum clearance from structure (thermal protection)

**Special Considerations:**
- Tank dimensions include thermal contraction allowance (-253°C to +20°C)
- Access envelope for tank removal (requires belly fairing removal)
- Safety zone demarcation (no hot work within 5m of tank)

### 3. **Upper-Surface Propulsor Installation**
Twin propulsors mounted above BWB center body create unique dimensional requirements:

**Propulsor Dimensional Data:**
- **Propulsor Diameter:** 5.2m (blade tip to tip)
- **Ground Clearance:** 3.8m (blade tip to ground at static condition)
- **Nacelle Length:** 4.5m (inlet to exhaust)
- **Lateral Spacing:** 18m (centerline to centerline)

**Ground Handling Implications:**
- **Tail Stand Required:** Aircraft tips aft if CG >65% MAC (propulsor strike risk)
- **Tow Bar Clearance:** Special low-profile tow bar (<1.2m height)
- **Maintenance Platforms:** Elevated platforms required for propulsor access

### 4. **Distributed Cabin Architecture**
BWB cabin spans entire center body width (no aisle constraints):

**Cabin Dimensional Data:**
- **Cabin Width (Max):** 22.5m at widest point (BWB center section)
- **Cabin Width (Min):** 8.2m at nose/tail sections
- **Cabin Height:** 2.3m (constant across width, no crown curvature)
- **Floor Area:** 485 m² (total pressurized area)
- **Seating Capacity:** 300 passengers (3-class config), 350 passengers (high-density)

**Special Considerations:**
- Emergency egress requires distributed door locations (8 Type-A exits)
- Cabin width creates unique interior design opportunities (10-abreast center section)
- HVAC distribution requires zonal analysis (ATA 21 interface)

## Integration with Other Chapters

### Data Flows
```
ATA 06 (Dimensions/Areas)
    ↓ Aircraft Envelope → ATA 07 (Lifting/Shoring), ATA 09 (Towing/Taxiing)
    ↓ Zone Definitions → ATA 05 (Maintenance Checks), ATA 12 (Servicing)
    ↓ Volume Data → ATA 28 (Fuel), ATA 50 (Cargo), ATA 25 (Equipment)
    ↓ Access Data → ATA 52-57 (Structures - Doors/Panels)
    ↓ Airport Planning → ATA 02 (Operations Information)
```

### Cross-References
- **ATA 00-10:** Aircraft General Information (summary dimensions)
- **ATA 02-30:** Airport Facilities (ground handling envelope)
- **ATA 05-30:** Zonal Inspection (zone boundary definitions)
- **ATA 07:** Lifting and Shoring (jack point locations)
- **ATA 08:** Leveling and Weighing (datum and station references)
- **ATA 09:** Towing and Taxiing (tow bar attachment dimensions)
- **ATA 12:** Servicing (service panel locations and access)
- **ATA 28:** Fuel System (tank volume and capacity)
- **ATA 50:** Cargo Compartments (cargo hold dimensions)
- **ATA 51-57:** Structures (structural component dimensions)

## Dimensional Data Categories

### 1. **Principal Dimensions**
Overall aircraft geometry for airport planning and hangar requirements:
- Wingspan, length, height
- Wheelbase, track width
- Ground angles (pitch, bank limits)
- Turning radius

### 2. **Surface Areas**
Aerodynamic and structural reference areas:
- Wing reference area (S_ref)
- Wetted area (total external surface)
- Control surface areas (elevons, rudders)
- Exposed vs. theoretical areas

### 3. **Internal Volumes**
Capacity data for fuel, cargo, equipment:
- Fuel tank volumes (usable/unusable)
- Cargo hold volumes (lower holds)
- Equipment bay volumes (avionics, ECS)
- Cabin volume (pressurized)

### 4. **Access Dimensions**
Maintenance and servicing access requirements:
- Door dimensions (passenger, cargo, service)
- Access panel dimensions and quantities
- Hatch openings (fuel, oil, hydraulic)
- Walkway clearances

### 5. **Zonal Definitions**
Maintenance zone boundaries per ATA 100 standard:
- Zone numbering system (100-900)
- Zone access requirements
- Zone environmental conditions (temp, hazards)
- Zone servicing points

### 6. **Clearance Envelopes**
Safe operating and maintenance clearances:
- Ground equipment clearances
- Maintenance platform requirements
- Propeller/jet blast zones
- Hydrogen safety zones

## Measurement Standards

### Precision Requirements
- **Overall Dimensions:** ±25mm (±1 inch)
- **Critical Interfaces:** ±5mm (±0.2 inch) (e.g., door seals, attachment points)
- **Tank Volumes:** ±0.5% of nominal capacity
- **Surface Areas:** ±1% of calculated value

### Measurement Methods
- **Laser Scanning:** Full aircraft 3D scan (±2mm accuracy) for as-built documentation
- **Photogrammetry:** Large dimension verification (wingspan, length)
- **Coordinate Measuring Machine (CMM):** Critical interface dimensions
- **Tank Calibration:** Volumetric flow measurement with certified flowmeter

### As-Built Documentation
- All production aircraft measured at final assembly
- Deviations from nominal dimensions tracked in quality database
- Statistical analysis for manufacturing process control
- Configuration control for Service Bulletin compliance

## Data Management

### CAD Model Integration
- **Master Geometry:** CATIA V6 digital mockup (DMU)
- **Dimensional Drawings:** 2D engineering drawings per ASME Y14.5 (GD&T)
- **3D PDF:** Interactive 3D models for maintenance documentation
- **Model-Based Definition (MBD):** Full 3D annotations (no 2D drawings required)

### Revision Control
- Dimensional data controlled via Product Lifecycle Management (PLM) system
- Changes require Engineering Change Order (ECO) approval
- Impact analysis for dependent documents (AMM, IPC, CMM)
- Operator notification via Service Bulletin (if affects operations)

### Data Exchange Formats
- **STEP AP242:** 3D CAD exchange (ISO 10303-242)
- **IGES:** Legacy format for older systems
- **ATA iSpec 2200 XML:** Standard dimensional data exchange
- **Airport Planning Database:** Standardized format for airport design tools

## Document Hierarchy
```
ATA 06 (This Chapter)
├── Aircraft General Arrangement Drawing
├── Principal Dimensions Drawing
├── Surface Areas Calculation Report
├── Volume Capacity Report
├── Zonal Layout Drawing
├── Access Panel Index
├── Ground Handling Envelope Drawing
├── Airport Characteristics Document
└── Dimensional Inspection Procedures
```

## Revision Control
Changes to ATA 06 data require:
1. **Design Change Approval:** Engineering review and authorization
2. **Impact Analysis:** Assess effects on operations, maintenance, certification
3. **Configuration Control:** Update all dependent documents (AMM, IPC, FCOM)
4. **Operator Notification:** Service Bulletin if affects aircraft handling
5. **Regulatory Notification:** EASA/FAA if affects type design (major change)

## Future Enhancements
- **Digital Twin Integration:** Real-time dimensional monitoring via embedded sensors
- **Augmented Reality (AR):** Dimensional data overlay for maintenance technicians
- **Blockchain Verification:** Immutable dimensional records for certification evidence
- **AI-Driven Optimization:** Machine learning for manufacturing tolerance optimization

---

## **Complete Directory Structure for ATA 06**

```
/P-PROGRAM
└── /ATA_06-DIMENSIONS_AND_AREAS
    ├── 06_README.md
    ├── INDEX.meta.yaml
    │
    ├── /06-10_PRINCIPAL_DIMENSIONS
    │   ├── /06-10-01_Overall_Dimensions
    │   │   ├── 01_OVERVIEW
    │   │   ├── 02_SAFETY
    │   │   ├── 03_REQUIREMENTS
    │   │   ├── 04_DESIGN
    │   │   ├── 05_INTERFACES
    │   │   ├── 06_ENGINEERING
    │   │   ├── 07_V_AND_V
    │   │   ├── 08_PROTOTYPING
    │   │   ├── 09_PRODUCTION_PLANNING
    │   │   ├── 10_CERTIFICATION
    │   │   ├── 11_OPERATIONS_AND_MAINTENANCE
    │   │   ├── 12_ASSETS_MANAGEMENT
    │   │   ├── 13_SUBSYSTEMS_AND_COMPONENTS
    │   │   └── 14_META_GOVERNANCE
    │   ├── /06-10-02_Wingspan_and_Wing_Geometry
    │   │   └── (14-folder skeleton)
    │   ├── /06-10-03_Aircraft_Length
    │   │   └── (14-folder skeleton)
    │   ├── /06-10-04_Aircraft_Height
    │   │   └── (14-folder skeleton)
    │   ├── /06-10-05_Ground_Clearances
    │   │   └── (14-folder skeleton)
    │   ├── /06-10-06_Wheelbase_and_Track
    │   │   └── (14-folder skeleton)
    │   └── /06-10-07_Reference_Datum_System
    │       └── (14-folder skeleton)
    │
    ├── /06-20_SURFACE_AREAS
    │   ├── /06-20-01_Wing_Reference_Area
    │   │   └── (14-folder skeleton)
    │   ├── /06-20-02_Wetted_Area_Total
    │   │   └── (14-folder skeleton)
    │   ├── /06-20-03_Control_Surface_Areas
    │   │   └── (14-folder skeleton)
    │   ├── /06-20-04_BWB_Planform_Area
    │   │   └── (14-folder skeleton)
    │   ├── /06-20-05_Composite_Panel_Areas
    │   │   └── (14-folder skeleton)
    │   └── /06-20-06_Aerodynamic_Reference_Areas
    │       └── (14-folder skeleton)
    │
    ├── /06-30_INTERNAL_VOLUMES
    │   ├── /06-30-01_Fuel_Tank_Volumes_LH2
    │   │   └── (14-folder skeleton)
    │   ├── /06-30-02_Cargo_Hold_Volumes
    │   │   └── (14-folder skeleton)
    │   ├── /06-30-03_Cabin_Pressurized_Volume
    │   │   └── (14-folder skeleton)
    │   ├── /06-30-04_Equipment_Bay_Volumes
    │   │   └── (14-folder skeleton)
    │   ├── /06-30-05_Battery_Compartment_Volumes
    │   │   └── (14-folder skeleton)
    │   └── /06-30-06_Fuel_Cell_Compartment_Volume
    │       └── (14-folder skeleton)
    │
    ├── /06-40_CABIN_DIMENSIONS
    │   ├── /06-40-01_Cabin_Length_and_Width
    │   │   └── (14-folder skeleton)
    │   ├── /06-40-02_Cabin_Height_and_Floor_Area
    │   │   └── (14-folder skeleton)
    │   ├── /06-40-03_Seating_Arrangement_Dimensions
    │   │   └── (14-folder skeleton)
    │   ├── /06-40-04_Aisle_Width_and_Configuration
    │   │   └── (14-folder skeleton)
    │   ├── /06-40-05_Emergency_Exit_Dimensions
    │   │   └── (14-folder skeleton)
    │   └── /06-40-06_Galley_and_Lavatory_Dimensions
    │       └── (14-folder skeleton)
    │
    ├── /06-50_CARGO_COMPARTMENT_DIMENSIONS
    │   ├── /06-50-01_Forward_Cargo_Hold
    │   │   └── (14-folder skeleton)
    │   ├── /06-50-02_Aft_Cargo_Hold
    │   │   └── (14-folder skeleton)
    │   ├── /06-50-03_Bulk_Cargo_Compartment
    │   │   └── (14-folder skeleton)
    │   ├── /06-50-04_Cargo_Door_Dimensions
    │   │   └── (14-folder skeleton)
    │   ├── /06-50-05_Container_and_Pallet_Positions
    │   │   └── (14-folder skeleton)
    │   └── /06-50-06_Cargo_Loading_System_Dimensions
    │       └── (14-folder skeleton)
    │
    ├── /06-60_ACCESS_DIMENSIONS
    │   ├── /06-60-01_Passenger_Door_Dimensions
    │   │   └── (14-folder skeleton)
    │   ├── /06-60-02_Service_Door_Dimensions
    │   │   └── (14-folder skeleton)
    │   ├── /06-60-03_Access_Panel_Index
    │   │   └── (14-folder skeleton)
    │   ├── /06-60-04_Maintenance_Hatch_Dimensions
    │   │   └── (14-folder skeleton)
    │   ├── /06-60-05_Equipment_Bay_Access
    │   │   └── (14-folder skeleton)
    │   └── /06-60-06_H2_Tank_Access_Envelope
    │       └── (14-folder skeleton)
    │
    ├── /06-70_ZONAL_DEFINITIONS
    │   ├── /06-70-01_Zone_Numbering_System
    │   │   └── (14-folder skeleton)
    │   ├── /06-70-02_Nose_Section_Zones_100_200
    │   │   └── (14-folder skeleton)
    │   ├── /06-70-03_Center_Body_Zones_300_600
    │   │   └── (14-folder skeleton)
    │   ├── /06-70-04_Wing_Zones_700_800
    │   │   └── (14-folder skeleton)
    │   ├── /06-70-05_Aft_Section_Zones_900
    │   │   └── (14-folder skeleton)
    │   ├── /06-70-06_Propulsor_Zones_400
    │   │   └── (14-folder skeleton)
    │   └── /06-70-07_H2_System_Safety_Zones
    │       └── (14-folder skeleton)
    │
    ├── /06-80_GROUND_HANDLING_ENVELOPE
    │   ├── /06-80-01_Aircraft_Parking_Envelope
    │   │   └── (14-folder skeleton)
    │   ├── /06-80-02_Wingtip_Clearance_Requirements
    │   │   └── (14-folder skeleton)
    │   ├── /06-80-03_Towing_Clearance_Envelope
    │   │   └── (14-folder skeleton)
    │   ├── /06-80-04_Turning_Radius_Data
    │   │   └── (14-folder skeleton)
    │   ├── /06-80-05_Jetway_Compatibility_Dimensions
    │   │   └── (14-folder skeleton)
    │   ├── /06-80-06_Ground_Support_Equipment_Clearances
    │   │   └── (14-folder skeleton)
    │   └── /06-80-07_Propulsor_Safety_Zone
    │       └── (14-folder skeleton)
    │
    └── /06-90_AIRPORT_CHARACTERISTICS_DATA
        ├── /06-90-01_ICAO_Aerodrome_Reference_Code
        │   └── (14-folder skeleton)
        ├── /06-90-02_Airport_Planning_Document
        │   └── (14-folder skeleton)
        ├── /06-90-03_Gate_Compatibility_Matrix
        │   └── (14-folder skeleton)
        ├── /06-90-04_Pavement_Classification_Number_PCN
        │   └── (14-folder skeleton)
        ├── /06-90-05_Special_Handling_Requirements_H2
        │   └── (14-folder skeleton)
        └── /06-90-06_AHM_560_Data_Package
            └── (14-folder skeleton)
```
