# Geometry Section AFM Input

**Component Code:** 02-11-00  
**Folder:** 09_PRODUCTION_PLANNING/DOCUMENTATION_PRODUCTION  
**Document:** Geometry_Section_AFM_Input.md

## Purpose

This document defines which geometric and dimensional parameters from 02-11-00 Aircraft Dimensions Geometry feed into the Aircraft Flight Manual (AFM), including dimensional envelopes, ground clearances, and operational dimension constraints for the AMPEL360 BWB H₂ Hy-E aircraft.

## AFM Section Structure

The AFM geometry-related content is distributed across multiple sections per EASA CS-25 and FAA Part 25 requirements:

### Section 1: General (AFM-1)
- Aircraft description and principal dimensions
- Three-view drawing with overall dimensions
- BWB configuration unique characteristics

### Section 2: Limitations (AFM-2)
- Ground clearance limitations
- Maximum operating dimensions (e.g., control surface deflections)
- Airport compatibility constraints

### Section 5: Performance (AFM-5)
- Reference dimensions for performance calculations
- Wing area, aspect ratio for lift calculations
- Envelope dimensions affecting drag

## Dimensional Parameters for AFM

### Overall Dimensions (AFM-1)

**Aircraft Envelope:**
- **Overall length:** From `01_OVERVIEW/baseline_dimensions.json` → AFM-1
  - Nominal design value
  - Measurement method reference (photogrammetry, ±0.1 m)
- **Wingspan:** From `01_OVERVIEW/baseline_dimensions.json` → AFM-1
  - Nominal design value
  - Wingtip to wingtip, measured at OML
- **Overall height:** From `01_OVERVIEW/baseline_dimensions.json` → AFM-1
  - Ground to highest point (vertical stabilizer or winglet tip)
  - Static ground attitude, OEW condition

**Wing Geometry:**
- **Wing area (reference):** From `03_REQUIREMENTS/RQ-DIM-002_Wingspan.md` → AFM-5
  - Used for lift coefficient and performance calculations
  - S_ref = 850 m² (nominal)
- **Aspect ratio:** Derived from wingspan and area → AFM-5
  - AR = b²/S = (65.0 m)² / 850 m² = 8.5
- **Mean aerodynamic chord (MAC):** From `04_DESIGN/` CAD analysis → AFM-5
  - Location and length of MAC for CG reference

**BWB-Specific Dimensions:**
- **Center body width:** From `01_OVERVIEW/baseline_dimensions.json` → AFM-1
  - Maximum width of passenger compartment section
  - Relevant for ground handling and gate compatibility
- **Blended section length:** From BWB geometry parameters → AFM-1
  - Transition region from center body to outer wing
  - Characteristic of BWB design for aircraft description

### Ground Clearances (AFM-2)

**Static Ground Clearances (OEW, No Load):**
- **Wingtip clearance:** From `03_REQUIREMENTS/RQ-CLEAR-001_Wingtip_Clearance.md` → AFM-2
  - Minimum clearance to ground: ≥1.0 m
  - Measured at wingtip lowest point in static attitude
- **Belly clearance:** From `03_REQUIREMENTS/RQ-CLEAR-002_Belly_Clearance.md` → AFM-2
  - Minimum clearance under center body: ≥0.8 m
  - Critical for ground handling on uneven surfaces
- **Tail clearance:** From `03_REQUIREMENTS/RQ-CLEAR-003_Tail_Clearance.md` → AFM-2
  - Minimum clearance at rear fuselage/empennage: ≥0.6 m
  - Relevant for tail strike avoidance on takeoff/landing
- **Engine/Nacelle clearance:** From ground clearance data → AFM-2
  - Minimum clearance under propulsion system pods
  - Foreign object debris (FOD) ingestion prevention

**Ground Clearance Limitations (AFM-2 Operational Limits):**
- Maximum pitch attitude on ground: Derived from tail clearance at MTOW
- Minimum ground clearance at MTOW: Calculated based on tire deflection and load
- Turning radius limits: Related to wingtip ground clearance during taxi

### Dimensional Envelopes (AFM-2 Airport Compatibility)

**ICAO Aerodrome Reference Code:**
- **Code letter:** "E" per `03_REQUIREMENTS/RQ-AIRPORT-005_ICAO_Code_E.md` → AFM-2
  - Wingspan: 52 m to < 65 m (AMPEL360 at 65 m borderline, treated as Code E)
  - Outer main gear wheel span: Typically <9 m for Code E
- **Code number:** "4" (Runway length ≥1800 m required)

**Gate and Stand Dimensions:**
- **Wingtip-to-wingtip parking envelope:** Wingspan + safety margin → AFM-2
  - Required parking stand width: 70 m minimum (65 m + 5 m clearance)
- **Nose-to-tail parking length:** Overall length + towing tractor clearance → AFM-2
  - Required parking stand length: 55 m minimum (48.5 m + 6.5 m)

### Dimensional Data for Performance Calculations (AFM-5)

**Aerodynamic Reference Dimensions:**
- **Reference wing area (S_ref):** 850 m² → AFM-5 performance tables
  - Used in lift and drag coefficient calculations
  - C_L = Lift / (0.5 × ρ × V² × S_ref)
- **Reference span (b_ref):** 65.0 m → AFM-5
  - Used in induced drag calculations
  - C_Di = C_L² / (π × AR × e)
- **Reference chord (c_ref or MAC):** From CAD → AFM-5
  - Used in pitching moment coefficient
  - C_M = Moment / (0.5 × ρ × V² × S_ref × c_ref)

**Wetted Area:**
- **Total wetted area:** From CAD surface analysis → AFM-5 drag analysis
  - Includes all external surfaces (OML)
  - Used in skin friction drag estimation

**Volume Coefficients:**
- **Horizontal tail volume coefficient:** If applicable (BWB may not have conventional tail) → AFM-5 stability
- **Vertical tail volume coefficient:** From vertical stabilizer/winglet geometry → AFM-5 stability

### Cargo and Cabin Dimensions (AFM-1 General Description)

**Passenger Compartment:**
- **Cabin length:** Internal dimension from CAD → AFM-1
  - Affects passenger capacity and emergency egress calculations
- **Cabin width (maximum):** BWB center body internal width → AFM-1
  - Seating configuration determination (e.g., 2-3-2, 2-4-2)
- **Cabin height:** Ceiling clearance at aisle centerline → AFM-1
  - Typically 2.0-2.1 m for passenger comfort

**Cargo Holds:**
- **Cargo volume:** From `01_OVERVIEW/` or `04_DESIGN/` → AFM-1
  - Forward and aft cargo hold volumes
  - May include belly cargo in BWB center body
- **Cargo compartment dimensions:** Length × width × height for each hold → AFM-1
  - Container/pallet compatibility (e.g., LD3, LD6)

### Control Surface Geometry (AFM-2 Limitations)

**Maximum Deflections:**
- **Trailing edge flaps:** Maximum deflection angles → AFM-2
  - Takeoff, landing, and intermediate settings
  - Affected by flap geometry from `04_DESIGN/CONTROL_SURFACES_DESIGN`
- **Elevons/Elevators:** Maximum deflection angles (up/down) → AFM-2
  - Pitch control authority limits
- **Rudder:** Maximum deflection angles (left/right) → AFM-2
  - Yaw control authority limits

**Control Surface Positions:**
- **Dimensional limits:** Trailing edge flap extension affects ground clearance → AFM-2
  - Maximum flap extension on ground may be limited by ground strike risk

## Data Flow from 02-11-00 to AFM

### Stage 1: Design Data (Pre-Production)
1. Nominal dimensions extracted from `01_OVERVIEW/baseline_dimensions.json`
2. Design tolerances from `03_REQUIREMENTS/RQ-TOLERANCES-*` reviewed
3. Preliminary AFM dimensional content drafted based on design intent
4. Engineering review and validation against CAD models

### Stage 2: As-Built Data (Prototype and Pre-Production)
1. As-built dimensions measured per `09_PRODUCTION_PLANNING/DATA_GENERATION/Geometry_Measurement_Data_Generation.md`
2. As-built data compared to nominal design
3. AFM dimensional content updated with actual values from MSN-P001 (prototype)
4. Ground clearances verified with physical aircraft on scales and jacks

### Stage 3: Flight Test Validation (Certification)
1. Flight test program validates dimensional assumptions for performance
2. Wing twist and deflection under load measured in flight (if applicable)
3. AFM performance data correlated with actual aircraft geometry
4. Final AFM issued with certified dimensional data

### Stage 4: Production Updates (Serial Production)
1. Statistical analysis of as-built dimensions across production run
2. AFM updated if production average differs significantly from design
3. Service bulletins issued if dimensional changes affect operations

## AFM Production Process

### AFM Geometry Section Development
1. **Responsible party:** Flight Operations / Technical Publications team
2. **Input sources:**
   - `01_OVERVIEW/baseline_dimensions.json` (design baseline)
   - `09_PRODUCTION_PLANNING/DATA_GENERATION/As_Built_Geometry_Configuration.md` (as-built data)
   - `03_REQUIREMENTS/` (clearance and airport compatibility requirements)
   - `10_CERTIFICATION/` (certified dimension data)
3. **Format:** Per ATA iSpec 2200 and S1000D standards
4. **Approval:** Requires certification authority approval (EASA, FAA)

### AFM Dimensional Content Checklist
- [ ] Three-view drawing with overall dimensions (length, span, height)
- [ ] Principal dimensions table with tolerances
- [ ] Wing geometry (area, aspect ratio, MAC location)
- [ ] Ground clearances (static and operational limits)
- [ ] ICAO aerodrome code and gate/stand requirements
- [ ] Cargo and cabin dimensions (volume, access dimensions)
- [ ] Control surface deflection limits
- [ ] BWB-specific geometry description

### AFM Revision Management
- **Temporary Revision (TR):** For minor dimensional corrections or clarifications
- **Revision:** For significant changes affecting operations (e.g., revised ground clearances)
- **Amendment:** For regulatory-mandated changes or airworthiness directives
- **Version control:** Tracked in CAOS document management system

## BWB-Specific AFM Considerations

### Unique Geometry Description
- AFM Section 1 includes detailed description of blended wing-body configuration
- Comparison to conventional aircraft highlighting differences:
  - No distinct fuselage-wing junction
  - Entire center body generates lift
  - Wide, flat lower surface for ground clearance considerations

### Ground Handling Special Notes
- AFM Section 2 includes special notes on:
  - Wide wingspan requiring Code E airports
  - Wide center body requiring special towing and pushback equipment
  - Ground clearance margin considerations for uneven apron surfaces

### Performance Impact of Geometry
- AFM Section 5 correlates BWB aerodynamic efficiency to geometry:
  - High aspect ratio (8.5) reduces induced drag
  - Blended wing-body reduces interference drag
  - Large wing area provides low wing loading for short takeoff

## Integration with CAOS System

### Automated AFM Data Population
- CAOS extracts dimensional data from production database
- Automatically populates AFM templates with as-built dimensions
- Flags discrepancies between design and as-built for engineering review
- Generates AFM geometry sections in S1000D format for publication

### Digital AFM (Electronic Flight Bag)
- Dimensional data linked to interactive 3D model in EFB
- Pilots can visualize aircraft envelope and ground clearances
- Real-time updates if aircraft configuration changes (e.g., after modification)

## Quality Assurance

### Data Accuracy Verification
- Cross-check AFM dimensions against multiple sources:
  - Design CAD models
  - As-built measurement reports
  - Type Certificate Data Sheet (TCDS)
  - Weight and Balance Manual (WBM)
- Independent review by certification engineer
- Approval by chief engineer and certification authority

### Consistency Checks
- AFM dimensions consistent with TCDS and other operational documents
- Ground clearances consistent with maximum pitch attitudes
- Wing area and aspect ratio mathematically consistent with span
- ICAO code consistent with wingspan and main gear span

## Related Documents

- `01_OVERVIEW/baseline_dimensions.json` – Design baseline dimensions
- `03_REQUIREMENTS/RQ-CLEAR-*` – Ground clearance requirements
- `03_REQUIREMENTS/RQ-AIRPORT-*` – Airport compatibility requirements
- `09_PRODUCTION_PLANNING/DATA_GENERATION/As_Built_Geometry_Configuration.md` – As-built geometry data
- `09_PRODUCTION_PLANNING/DOCUMENTATION_PRODUCTION/Geometry_Section_TCDS_Input.md` – TCDS geometry content
- `10_CERTIFICATION/` – Certified dimensional data package
- `11_OPERATIONS_MAINTENANCE/` – Operational manuals (AFM, WBM)
- ATA 02-20-00 Weight and Balance – CG position relative to MAC
- ATA 02-40-00 Performance Data – Performance calculations using geometry

---

**Document Control:**
- Version: 1.0
- Status: Template
- Last Updated: 2025-11-11
- Classification: Flight Operations Critical
- Author: COPILOT agent prompted by Amedeo Pelliccia
