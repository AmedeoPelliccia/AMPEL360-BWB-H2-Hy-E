# As-Built Geometry Inspection

**Component Code:** 02-11-00  
**Folder:** 09_PRODUCTION_PLANNING/QUALITY_CONTROL  
**Document:** As_Built_Geometry_Inspection.md

## Purpose

This document establishes the comprehensive inspection plan for verifying as-built dimensional and geometric conformance of the AMPEL360 BWB H₂ Hy-E aircraft throughout production. It defines inspection stages, methods, frequencies, acceptance criteria, and non-conformance management procedures.

## Overview

As-built geometry inspection ensures that manufactured aircraft components and assemblies conform to design specifications within approved tolerances. This is critical for:
- Airworthiness and safety compliance
- Aerodynamic performance validation
- Structural integrity verification
- Interchangeability of components across fleet
- Certification authority conformity demonstration

## Inspection Stages

### Stage 1: Component Level Inspection

**Scope:** Individual components before assembly (e.g., wing panels, center body sections, landing gear)

**Timing:** At component manufacturing completion, before release to final assembly

**Inspection Activities:**
1. **Critical Dimensions Verification:**
   - CMM measurement of machined features (holes, surfaces, interfaces)
   - Laser scanning of complex surfaces (BWB center body sections, wing panels)
   - Comparison to component design drawings and CAD models
   - Documentation in component inspection report

2. **Interface Verification:**
   - Measurement of mating surfaces (e.g., wing-to-center body junction)
   - Hole pattern verification for fastener installations
   - Surface finish and contour checks at interfaces
   - Fit-check with master tooling or adjacent components

3. **Structural Frame Geometry:**
   - Frame station locations per design (FS, WL, BL coordinates)
   - Frame perpendicularity and alignment
   - Critical load path dimensions
   - CMM verification against design model

**Acceptance Criteria:**
- All dimensions within design tolerances per `03_REQUIREMENTS/RQ-TOLERANCES-*`
- No deviations exceeding Class II (requiring engineering disposition)
- Component inspection report signed off by QA inspector and responsible engineer

**Frequency:** 100% for prototype and pre-production aircraft, sampling plan (e.g., AQL 1.0) for serial production

### Stage 2: Major Assembly Inspection

**Scope:** Wing assembly, center body assembly, empennage assembly

**Timing:** At major assembly completion, before integration into final assembly

**Inspection Activities:**
1. **Global Assembly Geometry:**
   - Laser tracker measurement of assembly coordinate system
   - Verification of overall assembly dimensions (span, chord distribution, sweep)
   - Twist and dihedral measurement along wing span
   - Comparison to assembly CAD model

2. **Junction and Interface Alignment:**
   - Wing panel splice alignment (gap, step, flush)
   - Skin-to-frame joint verification
   - Control surface hinge line alignment
   - Fastener pattern and hole quality at critical joints

3. **BWB-Specific Geometry:**
   - Center body cross-section verification at key stations
   - Blended section contour measurement (transition from center body to outer wing)
   - Surface continuity across blended region (G2 curvature continuity check)
   - Comparison to aerodynamic surface CAD

**Acceptance Criteria:**
- Assembly dimensions within design tolerances
- Junction alignment within specified gap/step limits (e.g., ±0.5 mm)
- Surface continuity meeting aerodynamic quality requirements
- No adverse deviations affecting structural load paths or aerodynamics

**Frequency:** 100% for all aircraft

### Stage 3: Final Assembly Inspection

**Scope:** Complete aircraft after final assembly, all systems installed

**Timing:** At final assembly completion, before ground testing and delivery

**Inspection Activities:**
1. **Overall Aircraft Dimensions:**
   - Photogrammetry of complete aircraft (360° coverage)
   - Overall length, wingspan, height measurement
   - Ground clearance verification (wingtip, belly, tail, engine)
   - Comparison to `01_OVERVIEW/baseline_dimensions.json`

2. **Control Surface Installation:**
   - Control surface gap and step measurements (trailing edge flaps, elevons, rudder)
   - Deflection range verification (maximum up/down, left/right)
   - Hinge line alignment and actuation mechanism geometry
   - Clearance verification at maximum deflections

3. **Landing Gear Geometry:**
   - Main gear track and wheelbase measurement
   - Landing gear extension and retraction clearances
   - Wheel alignment (camber, toe-in/toe-out)
   - Ground stance attitude (pitch and roll at OEW)

4. **Reference System Verification:**
   - Body axis coordinate system establishment (FS0, WL0, BL0 datum)
   - Station, waterline, and buttline marker verification
   - CG measurement location verification (for weight and balance)
   - Alignment with design reference system

5. **H₂ System Geometry (BWB-Specific):**
   - H₂ tank bay envelope verification (clearances to structure, insulation)
   - Fuel line routing geometry (clearances, support locations)
   - Fuel cell installation geometry (alignment, interfaces)
   - Cross-reference with ATA 28 (Fuel System) inspection requirements

**Acceptance Criteria:**
- Overall dimensions within ±0.1 m (±4 in) of design
- Ground clearances meeting minimum requirements per `03_REQUIREMENTS/RQ-CLEAR-*`
- Control surface gaps and steps within ±1 mm (±0.04 in)
- Reference system markers within ±5 mm (±0.2 in) of design location

**Frequency:** 100% for all aircraft

### Stage 4: Pre-Delivery Inspection

**Scope:** Final verification before aircraft delivery to customer

**Timing:** After all ground and flight testing, immediately before delivery

**Inspection Activities:**
1. **Geometry Re-Verification:**
   - Spot-check critical dimensions (sample of 10-20 key dimensions)
   - Visual inspection for any damage or deformation during testing
   - Photogrammetry comparison to post-final-assembly baseline (optional)
   - Verification that no unauthorized modifications have occurred

2. **Ground Clearance Confirmation:**
   - Ground clearance measurement at delivery weight condition (typically OEW)
   - Verification of tire pressures and landing gear servicing
   - Confirmation of ground stance attitude (pitch, roll)

3. **As-Built Configuration Freeze:**
   - Finalize as_built_geometry_MSN-XXX.json for aircraft
   - Generate final as-built dimensional report
   - Upload to customer delivery data package and CAOS digital twin
   - Archive in production database for lifecycle traceability

**Acceptance Criteria:**
- No changes from final assembly inspection beyond acceptable limits
- All damage or deformation documented and dispositioned
- As-built configuration record complete and accurate

**Frequency:** 100% for all aircraft

## BWB-Specific Inspection Procedures

### Center Body Internal Geometry
**Inspection:**
- Internal cabin dimensions (length, width, height at key sections)
- Floor plan layout verification (seat track locations, galley positions)
- Cargo hold dimensions and access door clearances
- Emergency exit locations and dimensions per CS-25.807

**Method:** Laser tracker or tape measure for internal dimensions, cross-check with passenger cabin layout drawing

**Frequency:** 100% on MSN-P001 (prototype), 10% sampling in production

### Blended Wing-Body Surface Quality
**Inspection:**
- Surface waviness and smoothness across blended region
- Filler and fairing application quality (if used to achieve surface continuity)
- Gaps at skin panel joints (maximum gap specification, typically ≤3 mm)
- Surface discontinuities (steps, dents, scratches exceeding limits)

**Method:** Optical scanning (structured light or laser), visual inspection with surface quality gauges

**Acceptance Criteria:** 
- Surface waviness ≤0.5 mm over 300 mm span (typical aerodynamic quality requirement)
- No steps or gaps exceeding 0.5 mm at joints within aerodynamic critical regions

**Frequency:** 100% on MSN-P001, sampling based on process capability in production

### Wing-Center Body Junction Inspection
**Inspection:**
- Junction line geometry (position, alignment with design)
- Structural joint integrity (fastener installation, edge distance, joint fit)
- Fillet or fairing contour (smooth transition, no discontinuities)
- Load transfer verification (indirect, through joint inspection and structural test)

**Method:** Laser tracker measurement of junction line, CMM or manual measurement of joint features, visual and tactile inspection of fairing

**Acceptance Criteria:** 
- Junction line within ±5 mm (±0.2 in) of design position
- All fasteners installed per specification, no gaps at joint exceeding 0.2 mm
- Fillet/fairing smooth with no abrupt transitions

**Frequency:** 100% for all aircraft (critical structural and aerodynamic feature)

## Inspection Methods and Equipment

### Coordinate Measuring Machine (CMM)
- **Application:** Precision measurement of components, small assemblies
- **Accuracy:** ±0.01 mm + 3 µm/m
- **Calibration:** Annual by ISO/IEC 17025 accredited lab
- **Operator qualification:** Certified CMM operator (Level II per company standard)

### Laser Tracker
- **Application:** Large-scale assembly measurement, final assembly inspection
- **Accuracy:** ±0.015 mm + 6 µm/m (up to 80 m range)
- **Calibration:** Annual by ISO/IEC 17025 accredited lab, daily self-compensation
- **Operator qualification:** Certified laser tracker operator (Level II)

### Photogrammetry
- **Application:** Full aircraft dimensional inspection, ground clearance measurement
- **Accuracy:** ±0.1 mm to ±1 mm depending on setup
- **Calibration:** Camera and lens calibration every 6 months, scale bars annual
- **Operator qualification:** Certified photogrammetry operator (Level II)

### Optical Scanning
- **Application:** Complex surface geometry capture (BWB contours)
- **Accuracy:** ±0.05 mm to ±0.2 mm
- **Calibration:** Quarterly calibration with reference artifacts
- **Operator qualification:** Certified scanner operator (Level II)

### Manual Measurement Tools
- **Application:** Spot checks, field measurements, simple dimensions
- **Tools:** Tape measures, calipers, height gauges, protractors
- **Accuracy:** Varies, typically ±1 mm (tape), ±0.01 mm (calipers)
- **Calibration:** Annual for precision tools
- **Operator qualification:** General inspector training

## Inspection Frequency Matrix

| Feature/Component | Prototype (MSN-P001) | Pre-Production (MSN-PP001-PP010) | Serial Production (MSN-001+) |
|---|---|---|---|
| Critical structural dimensions (component) | 100% | 100% | 100% (or AQL 1.0 sampling) |
| Non-critical component dimensions | 100% | 50% | AQL 2.5 sampling |
| Major assembly overall dimensions | 100% | 100% | 100% |
| Wing-center body junction | 100% | 100% | 100% |
| BWB surface quality (optical scan) | 100% | 100% | 10% sampling |
| Final assembly overall dimensions | 100% | 100% | 100% |
| Ground clearances | 100% | 100% | 100% |
| Control surface gaps/steps | 100% | 100% | 100% |
| Internal cabin dimensions | 100% | 20% | 5% (audit sample) |
| H₂ system geometry | 100% | 100% | 100% (safety critical) |
| Pre-delivery spot check | 100% | 100% | 100% |

## Acceptance Criteria and Tolerancing

### Tolerance Classification
- **Class I Deviation:** Within design tolerance, no action required
  - Example: Overall length 48.5 m ±0.1 m, measured 48.52 m → Class I
- **Class II Deviation:** Outside design tolerance but within acceptance limit (engineering disposition required)
  - Example: Wing station 10 m chord 3.00 m ±0.01 m, measured 3.012 m → Class II, accepted per engineering review
- **Class III Deviation:** Outside acceptance limit, requires rework or repair
  - Example: Ground clearance 0.8 m minimum, measured 0.78 m → Class III, rework required

### Acceptance Limits
- **Overall dimensions:** Typically ±0.1 m (±4 in) from nominal
- **Wing geometry:** Chord ±0.02 m (±0.8 in), twist ±0.2°, dihedral ±0.5°
- **Ground clearances:** No negative deviation from minimum required
- **Junction gaps/steps:** ±0.5 mm (±0.02 in) from flush in aerodynamic critical regions
- **Reference system markers:** ±5 mm (±0.2 in) from design location

### Engineering Disposition Process
1. Inspector identifies dimension outside tolerance → generates non-conformance report (NCR)
2. Responsible engineer reviews NCR, compares to design intent and functional requirements
3. Engineer dispositions NCR:
   - **Accept as-is:** Dimension acceptable for form, fit, function
   - **Rework:** Return to production for correction
   - **Repair:** Implement approved repair procedure
   - **Scrap:** Component unusable (rare, high cost)
4. Quality engineer reviews and approves disposition
5. For significant deviations, certification authority is informed (may require concession)
6. Disposition documented in production record and linked to MSN

## Non-Conformance Management

### Non-Conformance Report (NCR) Generation
- **Trigger:** Any dimension or geometry outside acceptance criteria
- **NCR contents:**
  - MSN or component serial number
  - Feature or dimension out of tolerance
  - Nominal value, actual value, tolerance, deviation
  - Measurement method and equipment used
  - Inspector name and date
  - Supporting data (photos, measurement reports)

### Root Cause Analysis
- For recurring non-conformances (≥3 occurrences of same issue):
  - Perform root cause analysis (5 Whys, Fishbone diagram)
  - Identify systemic issue (tooling, process, training, design)
  - Implement corrective action
  - Verify effectiveness through follow-up inspection

### Trend Analysis
- Quality engineering monitors non-conformance trends:
  - Plot dimensional deviations over time (control charts)
  - Identify shifts or patterns indicating process drift
  - Proactive intervention before out-of-tolerance condition occurs

## Quality Metrics and Reporting

### Key Performance Indicators (KPIs)
- **First-time inspection pass rate:** Target ≥95% for serial production
- **Class II deviation rate:** Target ≤5% of inspected dimensions
- **Class III deviation rate (rework):** Target ≤1% of inspected dimensions
- **Average inspection cycle time:** Tracked to optimize efficiency

### Reporting
- **Daily:** Inspection results logged in production database
- **Weekly:** Summary of non-conformances and dispositions to production management
- **Monthly:** Dimensional trend analysis report to engineering and quality leadership
- **Quarterly:** Comprehensive quality review including geometry conformance, presented to senior management

## Integration with CAOS Digital Twin

### Automated Inspection Data Flow
- Inspection measurement files automatically uploaded to CAOS system
- CAOS ingests data and updates digital twin with as-built geometry
- Deviations color-coded in digital twin 3D visualization (green = conforming, yellow = Class II, red = Class III)
- Non-conformances automatically flagged for engineering review

### Predictive Quality Analytics
- CAOS analyzes historical inspection data across fleet
- Machine learning predicts potential quality issues (e.g., tool wear leading to dimensional drift)
- Recommends preventive maintenance on tooling or process adjustments
- Optimizes inspection plans based on process capability (reduce inspection on stable processes)

## Inspector Qualification and Training

### Inspector Certification Levels
- **Level I:** Supervised inspector, performs routine inspections under oversight
- **Level II:** Independent inspector, performs all inspections, signs off inspection reports
- **Level III:** Lead inspector, performs complex inspections, trains and audits Level I/II inspectors

### Training Requirements
- **Initial training:** 40 hours classroom + 80 hours on-the-job training (OJT)
- **Measurement technology specific:** CMM (40 hrs), laser tracker (24 hrs), photogrammetry (16 hrs), optical scanning (16 hrs)
- **Annual recurrent training:** 8 hours refresher, covers process changes and lessons learned
- **Practical exam:** Demonstration of measurement competency on test artifacts

### Qualification Maintenance
- Perform inspection activities continuously (no gap >12 months)
- Pass annual practical proficiency test
- Comply with company quality manual and work instructions

## Related Documents

- `01_OVERVIEW/baseline_dimensions.json` – Design baseline geometry
- `03_REQUIREMENTS/RQ-TOLERANCES-*` – Dimensional tolerances
- `04_DESIGN/` – CAD models and inspection drawings
- `07_V_AND_V/VER-02-11-402_Dimensional_Tolerance_Analysis.md` – Tolerance analysis
- `09_PRODUCTION_PLANNING/DATA_GENERATION/Geometry_Measurement_Data_Generation.md` – Measurement methods
- `09_PRODUCTION_PLANNING/QUALITY_CONTROL/Dimension_Data_Accuracy_Verification_02-11-00.md` – Data validation
- `09_PRODUCTION_PLANNING/QUALITY_CONTROL/Geometry_Production_Acceptance_Tests.csv` – Acceptance test matrix
- Company Quality Manual – General QA procedures and standards
- AS9100 Standard – Aerospace quality management system requirements

---

**Document Control:**
- Version: 1.0
- Status: Template
- Last Updated: 2025-11-11
- Classification: Production Critical
