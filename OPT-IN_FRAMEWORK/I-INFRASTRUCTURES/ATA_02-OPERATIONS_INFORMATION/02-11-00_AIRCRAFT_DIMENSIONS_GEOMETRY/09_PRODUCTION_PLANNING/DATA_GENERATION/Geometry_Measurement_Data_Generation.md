# Geometry Measurement Data Generation

**Component Code:** 02-11-00  
**Folder:** 09_PRODUCTION_PLANNING/DATA_GENERATION  
**Document:** Geometry_Measurement_Data_Generation.md

## Purpose

This document defines the processes for capturing dimensional and geometric data from physical aircraft using various measurement technologies, including Coordinate Measuring Machines (CMM), laser trackers, and photogrammetry. It establishes procedures for data acquisition, processing, and integration into production data repositories.

## Overview

Geometry measurement data generation is the process of capturing the as-built physical dimensions and geometry of manufactured aircraft components and assemblies. This data is essential for:
- Verifying conformance to design specifications
- Creating as-built configuration records
- Supporting certification activities
- Enabling digital twin population
- Facilitating maintenance and modification planning

## Measurement Technologies

### Coordinate Measuring Machine (CMM)

#### Applications
- Precision measurement of machined components
- Critical junction verification
- Structural frame geometry
- Landing gear component dimensions

#### Equipment Specifications
- **Type:** Bridge-type or gantry CMM
- **Working volume:** Minimum 5m × 3m × 2m for fuselage sections
- **Accuracy:** ±0.01 mm + 3 µm/m (ISO 10360-2)
- **Probe:** Touch-trigger or scanning probe
- **Software:** Calypso, PC-DMIS, or equivalent

#### Measurement Procedure
1. **Setup:**
   - Clean and prepare part surface
   - Establish temperature-controlled environment (20°C ±1°C)
   - Secure component on CMM table or fixture
   - Define coordinate system per design datum structure

2. **Calibration:**
   - Verify CMM calibration certificate (valid within 12 months)
   - Perform daily artifact check (reference sphere or gauge block)
   - Document ambient temperature and humidity

3. **Data Acquisition:**
   - Follow CMM program or manual inspection plan
   - Capture critical dimensions per inspection drawing
   - Minimum 3 points per feature for planes, 5 for cylinders
   - Scan complex surfaces with ≤1 mm point spacing

4. **Data Processing:**
   - Best-fit analysis of measured points to nominal geometry
   - Calculate deviations from design dimensions
   - Generate inspection report with pass/fail status
   - Export data to CSV and native CMM format

5. **Data Storage:**
   - Save raw CMM measurement file with MSN identifier
   - Upload processed data to production database
   - Link to component serial number and inspection record

### Laser Tracker

#### Applications
- Large-scale aircraft assembly verification
- Wing-to-fuselage junction alignment
- Control surface installation and rigging
- Global aircraft coordinate system establishment
- Final assembly as-built measurements

#### Equipment Specifications
- **Type:** Absolute Distance Meter (ADM) laser tracker
- **Range:** Minimum 80 m
- **Accuracy:** ±0.015 mm + 6 µm/m (ISO 10360-10)
- **Measurement rate:** ≥1000 Hz for dynamic measurements
- **Targets:** Spherically mounted retroreflectors (SMRs), 1.5" diameter

#### Measurement Procedure
1. **Setup:**
   - Position laser tracker with clear line of sight to measurement area
   - Establish reference coordinate system using master tooling balls
   - Verify tracker-to-aircraft coordinate transformation

2. **Calibration:**
   - Verify tracker calibration certificate (valid within 12 months)
   - Perform daily self-compensation routine
   - Validate with length bar or scale bar artifact (1-10 m)

3. **Data Acquisition:**
   - Attach SMR targets to key measurement points (tooling holes, reference marks)
   - Measure target positions with SMR in tracker capture
   - Probe surface features using SMR on fixed probe or handheld arm
   - Scan continuous surfaces by moving SMR along profiles

4. **Data Processing:**
   - Import point cloud into analysis software (SpatialAnalyzer, PolyWorks)
   - Best-fit to CAD model or reference geometry
   - Calculate deviations and generate color-coded deviation maps
   - Identify out-of-tolerance features for engineering review

5. **Data Storage:**
   - Save raw laser tracker session file (.xit, .mea formats)
   - Export processed point cloud to ASCII or binary format
   - Archive deviation analysis report with screenshots
   - Upload summary dimensions to production database

### Photogrammetry

#### Applications
- Full-aircraft as-built geometry capture
- Complex BWB surface verification
- Large component alignment (e.g., wing assembly)
- Rapid inspection of assembled aircraft
- Ground clearance and stance measurement

#### Equipment Specifications
- **Cameras:** Industrial digital cameras, ≥12 megapixels
- **Lenses:** Calibrated fixed focal length (25-50 mm typical)
- **Targets:** Coded and non-coded retroreflective targets
- **Scale bars:** Certified reference length, ≥2 per setup
- **Software:** TRITOP, V-STARS, Aicon, or equivalent

#### Measurement Procedure
1. **Setup:**
   - Apply retroreflective targets to aircraft surface
   - Target spacing: 0.5-1.0 m typical, denser in areas of high curvature
   - Place coded targets for automatic image orientation
   - Position scale bars to define measurement scale and orientation

2. **Calibration:**
   - Verify camera calibration certificate (valid within 6 months)
   - Calibrate scale bars (annual certification)
   - Perform camera self-calibration during bundle adjustment if required

3. **Data Acquisition:**
   - Capture images from multiple angles around aircraft
   - Minimum 3 images per target for triangulation
   - Maintain ≥30° convergence angle between cameras
   - Ensure ≥60% image overlap
   - Typical image count: 200-500 for full aircraft

4. **Data Processing:**
   - Import images into photogrammetry software
   - Automatic target recognition and matching
   - Bundle adjustment to calculate 3D target coordinates
   - Quality check: target point precision ≤0.1 mm RMS
   - Export target coordinates and fit to CAD reference geometry

5. **Derived Measurements:**
   - Use target coordinates to calculate:
     - Overall dimensions (length, wingspan, height)
     - Ground clearances at specified load conditions
     - Control surface gap and step measurements
     - Alignment of major assemblies

6. **Data Storage:**
   - Archive all images with camera calibration data
   - Save photogrammetry project file with processed target coordinates
   - Export dimensional report with comparison to design
   - Upload to production database linked to MSN

### Optical Scanning (Structured Light, Laser)

#### Applications
- High-resolution surface capture for BWB contours
- Blended section geometry verification
- Surface finish and waviness inspection
- Composite part quality control
- Reverse engineering for tooling verification

#### Equipment Specifications
- **Type:** Structured light scanner or laser line scanner
- **Accuracy:** ±0.05 mm to ±0.2 mm depending on volume
- **Resolution:** 0.1 mm point spacing typical
- **Working volume:** 0.5m to 2m cube per scan position
- **Software:** GOM Inspect, Geomagic, Polyworks, or equivalent

#### Measurement Procedure
1. **Setup:**
   - Clean and prepare surface (remove dust, grease)
   - Apply anti-reflective coating if surface is too shiny
   - Position reference markers (coded targets) around scan area
   - Define scan strategy to cover all required surfaces

2. **Calibration:**
   - Verify scanner calibration certificate (valid within 3 months)
   - Perform warm-up and calibration with reference artifact

3. **Data Acquisition:**
   - Scan from multiple positions to cover entire surface
   - Overlap scans by ≥30% for accurate alignment
   - Capture reference markers in each scan for global registration
   - Typical scan count: 20-100 depending on component size

4. **Data Processing:**
   - Align individual scans using common reference markers
   - Merge scans into single point cloud or mesh
   - Noise filtering and outlier removal
   - Generate continuous surface (NURBS or mesh)
   - Compare to CAD model and generate deviation color map

5. **Data Storage:**
   - Archive raw scan files and processing project
   - Export point cloud (ASCII, PLY, STL)
   - Export inspection report with deviation histograms
   - Upload summary data to production database

## Measurement Planning

### Feature-Based Measurement Plan
For each critical dimension or geometry:
1. Identify feature type (plane, cylinder, cone, sphere, freeform surface)
2. Select appropriate measurement method based on:
   - Required accuracy vs. method capability
   - Feature size and accessibility
   - Available equipment and operator skill
   - Time and cost constraints
3. Specify measurement frequency:
   - 100% for critical safety features
   - Sampling plan for non-critical features (e.g., AQL 2.5)

### BWB-Specific Measurement Strategy

#### Center Body Cross-Sections
- **Method:** Laser tracker or photogrammetry
- **Locations:** Fuselage stations per design (e.g., FS500, FS1000, FS1500)
- **Points:** Profile cross-section with ≥50 points per section
- **Frequency:** 100% at final assembly

#### Blended Wing-Body Surface
- **Method:** Optical scanning (structured light or laser)
- **Coverage:** Complete OML surface, upper and lower
- **Resolution:** ≤0.1 mm point spacing
- **Comparison:** Deviation analysis vs. aerodynamic surface CAD (tolerance ±2 mm)
- **Frequency:** 100% on MSN-P001 (prototype), 10% sampling in production

#### Wing Geometry
- **Method:** Photogrammetry supplemented by laser tracker
- **Features:** Leading edge profile, trailing edge, chord lengths, twist distribution
- **Stations:** Wing stations per design (e.g., every 1 m along span)
- **Frequency:** 100% at wing build, verification at final assembly

#### Ground Clearances
- **Method:** Photogrammetry or manual measurement
- **Locations:** Wingtip, belly, tail, engine nacelle (as defined in 03_REQUIREMENTS)
- **Load condition:** Static ground attitude with OEW
- **Frequency:** 100% at final assembly and pre-delivery

## Data Processing and Reporting

### Data Flow
1. **Capture:** Raw measurement data acquired on shop floor
2. **Transfer:** Data uploaded to secure server or directly to analysis workstation
3. **Processing:** Point clouds, CMM data, or photogrammetry processed to extract dimensions
4. **Comparison:** As-built geometry compared to nominal design (CAD model)
5. **Reporting:** Dimensional report generated with deviations and pass/fail status
6. **Storage:** Processed data and reports archived in production database
7. **Integration:** Summary dimensions populate digital twin and MSN configuration record

### Deviation Analysis
- **Color-coded maps:** Visual representation of deviations (e.g., green = within tolerance, red = out of tolerance)
- **Histograms:** Distribution of deviations across entire surface
- **Statistical summary:** Mean deviation, standard deviation, min/max, RMS
- **Out-of-tolerance list:** Table of features exceeding design tolerances for engineering review

### Inspection Report Contents
- MSN and component identification
- Measurement date, operator, equipment used
- Measurement method and procedure reference
- List of dimensions inspected with nominal, actual, deviation, tolerance, and pass/fail
- Overall inspection result (Accept, Conditional Accept, Reject)
- Engineering disposition for out-of-tolerance features
- Approval signatures (inspector, QA, responsible engineer)

## Quality Assurance

### Measurement System Analysis (MSA)
- **Gauge R&R study:** Perform for each measurement method and critical feature type
- **Acceptance criteria:** Gauge R&R ≤10% of tolerance for critical dimensions
- **Frequency:** Annually or when process changes

### Operator Qualification
- **Training:** Formal training on each measurement technology
- **Certification:** Practical exam demonstrating measurement competency
- **Recertification:** Every 2 years or after 12 months without performing measurements

### Equipment Calibration
- **Calibration interval:** Per equipment specifications (typically 6-12 months)
- **Calibration laboratory:** ISO/IEC 17025 accredited
- **Traceability:** Calibration certificates traceable to national standards (NIST, PTB)
- **Out-of-tolerance:** If equipment found out-of-tolerance, review and re-inspect parts measured since last calibration

### Measurement Audit
- **Internal audit:** Quarterly audit of measurement processes and data quality
- **External audit:** Annual third-party audit for AS9100 compliance
- **Findings:** Corrective actions for non-conformances, process improvements

## Integration with CAOS Digital Twin

### Automated Data Flow
- CAOS system monitors production database for new measurement data
- Automatically ingests as-built geometry and populates digital twin model
- Updates digital twin 3D visualization with as-built surfaces
- Flags deviations exceeding thresholds for engineering review

### Predictive Analytics
- CAOS analyzes measurement trends across multiple aircraft
- Predicts potential quality issues before they occur
- Recommends process adjustments (e.g., tooling compensation)
- Optimizes inspection plans based on historical data

### Lifecycle Data Retention
- Measurement data retained for life of aircraft
- Supports maintenance, modification, and repair planning
- Enables comparison of in-service geometry changes (e.g., after heavy maintenance)

## Deliverables by Production Phase

### Prototype Phase (MSN-P001)
- Comprehensive measurement data for complete aircraft
- Measurement method validation reports
- Process capability studies (Cpk analysis)
- Lessons learned and process improvements

### Pre-Production Phase (MSN-PP001 to MSN-PP010)
- Refined measurement plans and procedures
- Reduced measurement scope based on process capability
- Automated data processing workflows
- CAOS integration validation

### Serial Production Phase (MSN-001 onwards)
- Standardized measurement procedures
- Sampling plans for non-critical features
- Automated data acquisition and processing where feasible
- Continuous improvement based on statistical process control

## Safety Considerations

### Personnel Safety
- Laser safety: Class 2 or 1M lasers for CMM and trackers (eye-safe)
- Working at height: Fall protection when measuring on scaffolding or lifts
- Moving equipment: Lockout/tagout procedures when measuring on aircraft with installed systems
- Hazardous materials: PPE for cleaning agents or coatings applied before measurement

### Data Security
- Protect proprietary geometry data from unauthorized access
- Encrypted data transfer and storage
- Access control based on need-to-know principle
- Compliance with customer data sharing agreements

## Related Documents

- `01_OVERVIEW/baseline_dimensions.json` – Nominal design geometry reference
- `04_DESIGN/` – CAD models and inspection drawings
- `07_V_AND_V/VER-02-11-402_Dimensional_Tolerance_Analysis.md` – Tolerance specifications
- `09_PRODUCTION_PLANNING/DATA_GENERATION/As_Built_Geometry_Configuration.md` – As-built data management
- `09_PRODUCTION_PLANNING/DATA_GENERATION/Dimension_Data_Production_02-11-00.md` – Data file generation
- `09_PRODUCTION_PLANNING/QUALITY_CONTROL/As_Built_Geometry_Inspection.md` – Inspection procedures
- `09_PRODUCTION_PLANNING/QUALITY_CONTROL/Dimension_Data_Accuracy_Verification_02-11-00.md` – Data validation

---

**Document Control:**
- Version: 1.0
- Status: Template
- Last Updated: 2025-11-11
- Classification: Production Critical
- Author: COPILOT agent prompted by Amedeo Pelliccia
