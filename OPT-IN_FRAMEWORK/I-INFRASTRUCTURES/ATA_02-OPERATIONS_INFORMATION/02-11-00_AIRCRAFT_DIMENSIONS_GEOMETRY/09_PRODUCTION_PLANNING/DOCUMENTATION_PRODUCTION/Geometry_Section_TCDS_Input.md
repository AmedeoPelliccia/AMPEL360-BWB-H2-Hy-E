# Geometry Section TCDS Input

**Component Code:** 02-11-00  
**Folder:** 09_PRODUCTION_PLANNING/DOCUMENTATION_PRODUCTION  
**Document:** Geometry_Section_TCDS_Input.md

## Purpose

This document defines the dimensional and geometric content from 02-11-00 Aircraft Dimensions Geometry that is included in the Type Certificate Data Sheet (TCDS), which is the official regulatory document specifying the approved configuration of the AMPEL360 BWB H₂ Hy-E aircraft.

## TCDS Overview

The Type Certificate Data Sheet (TCDS) is issued by the certification authority (EASA, FAA) upon completion of the type certification process. It contains the minimum essential information necessary to:
- Identify the aircraft type
- Define the certified configuration
- Specify operational limitations
- Support airworthiness determination of individual aircraft

**Regulatory Basis:**
- EASA: CS-21 Subpart B (Type Certificates and Restricted Type Certificates)
- FAA: 14 CFR Part 21 Subpart B (Type Certificates)

## TCDS Structure and Dimensional Content

The TCDS typically consists of:
1. **Data Sheet Header:** Aircraft model designation, type certificate number, certification basis
2. **Section I - Model:** Model variations and applicable data sheets
3. **Section II - Certification Basis:** Certification specifications and special conditions
4. **Section III - Description:** Physical description including dimensions
5. **Section IV - Operating Limitations:** Speeds, weights, CG limits
6. **Section V - Data Pertinent to All Models:** Fuel, oil, systems common to all variants

**Dimensional data primarily appears in Section III - Description.**

## Dimensional Parameters for TCDS

### Principal Dimensions (TCDS Section III)

**Overall Dimensions:**
- **Length overall:** [Value] m ([Value] ft [Value] in)
  - Source: `01_OVERVIEW/baseline_dimensions.json`, verified by as-built measurements
  - Definition: From nose tip to rearmost point (typically tail cone or rear fuselage)
  - Measurement method: Photogrammetry or laser tracker, static ground attitude
- **Wingspan:** [Value] m ([Value] ft [Value] in)
  - Source: `01_OVERVIEW/baseline_dimensions.json`, verified by as-built measurements
  - Definition: Wingtip to wingtip at maximum span location
  - Measurement method: Photogrammetry or laser tracker, OML (Outer Mold Line)
- **Height overall:** [Value] m ([Value] ft [Value] in)
  - Source: `01_OVERVIEW/baseline_dimensions.json`, verified by as-built measurements
  - Definition: Ground to highest point, static ground attitude, empty weight condition
  - Measurement method: Photogrammetry or laser tracker, vertical stabilizer/winglet tip

**Wing Geometry:**
- **Wing area (reference):** [Value] m² ([Value] ft²)
  - Source: `03_REQUIREMENTS/RQ-DIM-002_Wingspan.md` (design value), CAD computation
  - Definition: Projected wing planform area, used for performance calculations
  - Note: Includes area integrated into BWB center body per industry standard methods
- **Aspect ratio:** [Value] (dimensionless)
  - Calculated: AR = b²/S (wingspan squared divided by wing area)
  - Used for aerodynamic performance characterization

**BWB Configuration Description:**
- **Configuration type:** Blended Wing-Body (BWB)
- **Center body width (maximum):** [Value] m ([Value] ft [Value] in)
  - Source: `01_OVERVIEW/baseline_dimensions.json`
  - Definition: Maximum width of center body section containing passenger cabin
  - Significance: Distinguishing feature of BWB design, affects gate compatibility
- **Blended section:** Description of transition from center body to outer wing
  - Typically a qualitative description rather than specific dimensions
  - Example: "Blended wing-body configuration with gradual transition over [Value] m span"

### Ground Clearances (TCDS Section III or IV)

**Static Ground Clearances (Empty Weight, Static Attitude):**
- **Minimum ground clearance - wingtip:** ≥ [Value] m ([Value] ft [Value] in)
  - Source: `03_REQUIREMENTS/RQ-CLEAR-001_Wingtip_Clearance.md`, as-built verification
  - Condition: OEW (Operating Empty Weight), static attitude, level ground
- **Minimum ground clearance - belly/center body:** ≥ [Value] m ([Value] ft [Value] in)
  - Source: `03_REQUIREMENTS/RQ-CLEAR-002_Belly_Clearance.md`, as-built verification
  - Condition: OEW, static attitude, measured at lowest center body point
- **Minimum ground clearance - tail/rear fuselage:** ≥ [Value] m ([Value] ft [Value] in)
  - Source: `03_REQUIREMENTS/RQ-CLEAR-003_Tail_Clearance.md`, as-built verification
  - Condition: OEW, static attitude, measured at rearmost lower point
- **Minimum ground clearance - engine/propulsion pods:** ≥ [Value] m ([Value] ft [Value] in)
  - Source: Ground clearance analysis, as-built verification
  - Condition: OEW, static attitude, measured at lowest propulsion system point

**Operational Ground Clearance Limits (TCDS Section IV - Operating Limitations):**
- **Maximum pitch attitude on ground:** [Value]° nose-up
  - Limitation to prevent tail strike during rotation
  - Derived from tail clearance at MTOW and aft CG limit
- **Minimum ground clearance at MTOW:** [Value] m ([Value] ft [Value] in)
  - Accounts for landing gear deflection under maximum weight
  - May be specified at critical location (e.g., belly, engine intake)

### ICAO Aerodrome Reference Code (TCDS Section III)

**Code Classification:**
- **ICAO Code:** [Letter][Number] (e.g., 4E)
  - **Code number (4):** Aerodrome reference field length ≥ 1800 m
  - **Code letter (E):** Wingspan 52 m to < 65 m, outer main gear wheel span < 9 m
  - Source: `03_REQUIREMENTS/RQ-AIRPORT-005_ICAO_Code_E.md`
  - Significance: Defines compatible airports and infrastructure requirements

**Implications for TCDS:**
- Specifies minimum runway length, width, and strength requirements
- Defines taxiway and apron width requirements
- Affects gate and stand compatibility at airports

### Control Surface Geometry (TCDS Section III)

**Control Surface Descriptions:**
- **Trailing edge flaps:** Type (e.g., plain, slotted, Fowler), number of segments
  - Maximum deflection angles: [Value]° takeoff, [Value]° landing
  - Source: `04_DESIGN/CONTROL_SURFACES_DESIGN/`, flight test validation
- **Elevons/Elevators:** Type and control authority
  - Maximum deflection angles: [Value]° up, [Value]° down
- **Rudder/Yaw control:** Type (may be split rudder on winglets for BWB)
  - Maximum deflection angles: [Value]° left, [Value]° right

**Note:** Detailed control surface geometry typically not in TCDS unless critical for certification or unusual configuration (BWB may require more detail due to unconventional control surfaces).

### Landing Gear Geometry (TCDS Section III)

**Gear Configuration:**
- **Type:** Tricycle, retractable (or specific BWB gear arrangement if unique)
- **Main gear track:** [Value] m ([Value] ft [Value] in)
  - Distance between main landing gear centerlines
  - Source: Landing gear design, as-built verification
  - Affects ICAO code letter and pavement load classification
- **Wheelbase:** [Value] m ([Value] ft [Value] in)
  - Distance from nose gear to main gear (longitudinally)
  - Affects ground handling and turning radius

**Tire Sizes:**
- **Nose gear:** [Size] (e.g., 900 × 300 mm)
- **Main gear:** [Size] (e.g., 1400 × 530 mm)
- Source: Landing gear design, tire manufacturer specifications

**Note:** Landing gear geometry primarily from ATA 32, but included in TCDS for aircraft identification and operational limits.

## Data Flow from 02-11-00 to TCDS

### Stage 1: Design Data (Preliminary TCDS)
1. Preliminary TCDS drafted during design phase with nominal dimensions
2. Dimensions extracted from `01_OVERVIEW/baseline_dimensions.json`
3. Design tolerances considered for TCDS value ranges
4. Preliminary TCDS submitted to authority with certification plan

### Stage 2: Prototype Verification (Interim TCDS)
1. MSN-P001 (prototype) measured per `09_PRODUCTION_PLANNING/DATA_GENERATION/Geometry_Measurement_Data_Generation.md`
2. As-built dimensions compared to design values
3. TCDS updated with verified dimensions from physical aircraft
4. Interim TCDS issued if prototype aircraft enters service before type certification

### Stage 3: Flight Test and Certification (Final TCDS)
1. Flight test program validates dimensional assumptions (e.g., ground clearances at various weights)
2. Certification authority inspects aircraft to verify TCDS data
3. Any deviations from design intent are documented and approved
4. Final TCDS issued upon type certification

### Stage 4: Production (Production TCDS)
1. Statistical analysis of as-built dimensions across production aircraft
2. TCDS amended if production average differs from certified prototype
3. TCDS revision for aircraft modifications affecting dimensions

## TCDS Production Process

### TCDS Dimensional Content Development
1. **Responsible party:** Certification Engineering team
2. **Input sources:**
   - `01_OVERVIEW/baseline_dimensions.json` (design baseline)
   - `09_PRODUCTION_PLANNING/DATA_GENERATION/As_Built_Geometry_Configuration.md` (as-built MSN-P001)
   - `03_REQUIREMENTS/RQ-CLEAR-*`, `RQ-AIRPORT-*` (clearances, airport compatibility)
   - `10_CERTIFICATION/` (certified dimension data package)
   - Flight test reports validating ground clearances and operational limits
3. **Format:** EASA Form 45 or FAA equivalent TCDS format
4. **Approval:** Issued by certification authority (EASA, FAA) upon type certification

### TCDS Dimensional Content Checklist
- [ ] Length overall (metric and imperial units)
- [ ] Wingspan (metric and imperial units)
- [ ] Height overall (metric and imperial units)
- [ ] Wing area (reference, metric and imperial)
- [ ] Aspect ratio (dimensionless)
- [ ] BWB configuration description (center body width, blended section description)
- [ ] Ground clearances (wingtip, belly, tail, engine - static and operational limits)
- [ ] ICAO aerodrome reference code (code number and letter)
- [ ] Landing gear geometry (track, wheelbase, tire sizes)
- [ ] Control surface descriptions and deflection limits
- [ ] Any special conditions related to BWB geometry

### Unit Conventions
- Primary units: Metric (meters, square meters) per EASA preference
- Secondary units: Imperial (feet, inches, square feet) in parentheses per FAA preference
- Example: "Length overall: 48.5 m (159 ft 1 in)"

### Precision and Tolerances
- TCDS dimensions typically rounded to practical precision:
  - Overall dimensions: ±0.1 m (±0.5 ft)
  - Wing area: ±1 m² (±10 ft²)
  - Ground clearances: ±0.01 m (±0.5 in)
- Tolerances not explicitly stated in TCDS; compliance demonstrated by conformity inspection

## BWB-Specific TCDS Considerations

### Special Conditions for BWB Configuration
- BWB configuration may require special conditions or interpretations of CS-25/Part 25
- TCDS references special conditions related to:
  - Novel aircraft configuration (non-conventional fuselage-wing arrangement)
  - Ground clearance requirements unique to BWB (wide, flat lower surface)
  - Emergency egress from wide center body cabin
  - Control surface arrangement (e.g., distributed flaperons, split rudders on winglets)

### Comparison to Conventional Aircraft
- TCDS may include note distinguishing BWB from conventional aircraft
- Example: "This aircraft is certified as a Blended Wing-Body configuration per Special Condition SC-XXX, with continuous lifting surface from center body to wingtip."

### H₂ Propulsion Impact on TCDS Geometry
- H₂ fuel cell propulsion may affect TCDS dimensional content:
  - Propulsion system envelope and ground clearances
  - H₂ tank bay dimensions (if unusual or safety-critical)
  - Fuel system dimensional constraints (clearances, routing)
- TCDS cross-references ATA 28 (Fuel System) and ATA 71 (Power Plant) for detailed H₂ system data

## Integration with Other Certification Documents

### TCDS and Type Design Definition
- TCDS provides summary; full detail in Type Design documentation
- Type Design includes:
  - Complete CAD models from `04_DESIGN/`
  - Detailed drawings with GD&T
  - As-built configuration records from production
- Certification authority retains Type Design for conformity inspections

### TCDS and Aircraft Flight Manual (AFM)
- TCDS and AFM must be consistent in dimensional data
- AFM may include more detail (e.g., cargo hold dimensions, detailed ground clearance tables)
- Any discrepancies resolved before TCDS issuance
- Reference: `09_PRODUCTION_PLANNING/DOCUMENTATION_PRODUCTION/Geometry_Section_AFM_Input.md`

### TCDS and Weight and Balance Manual (WBM)
- TCDS specifies CG limits; WBM provides MAC location
- MAC location defined by wing geometry from 02-11-00
- Dimensional consistency required for CG calculation

## Quality Assurance and Data Validation

### TCDS Data Accuracy Verification
- All TCDS dimensions cross-checked against:
  - Design CAD models from `04_DESIGN/`
  - As-built measurement reports from MSN-P001
  - Independent measurement by certification authority inspector
- Discrepancies investigated and resolved before TCDS approval

### Conformity Inspection
- Certification authority performs conformity inspection of MSN-P001
- Verifies key TCDS dimensions on physical aircraft
- Measurement methods: Tape measure, laser tracker, photogrammetry as appropriate
- Conformity statement signed by authority inspector

### TCDS Revision Control
- **Revision:** For changes affecting type design (e.g., wing extension, fuselage stretch)
  - Requires amended type certificate or supplemental type certificate
  - New TCDS revision issued
- **Administrative change:** For corrections or clarifications not affecting type design
  - Updated TCDS issued with change history noted

## Related Documents

- `01_OVERVIEW/baseline_dimensions.json` – Design baseline dimensions
- `03_REQUIREMENTS/RQ-CLEAR-*` – Ground clearance requirements
- `03_REQUIREMENTS/RQ-AIRPORT-*` – Airport compatibility requirements
- `09_PRODUCTION_PLANNING/DATA_GENERATION/As_Built_Geometry_Configuration.md` – As-built prototype data
- `09_PRODUCTION_PLANNING/DOCUMENTATION_PRODUCTION/Geometry_Section_AFM_Input.md` – AFM geometry content
- `10_CERTIFICATION/` – Complete certification data package
- `11_OPERATIONS_MAINTENANCE/` – Operational manuals (AFM, WBM)
- ATA 02-20-00 Weight and Balance – CG limits and MAC location
- ATA 32-00-00 Landing Gear – Gear geometry and loads

---

**Document Control:**
- Version: 1.0
- Status: Template
- Last Updated: 2025-11-11
- Classification: Certification Critical
