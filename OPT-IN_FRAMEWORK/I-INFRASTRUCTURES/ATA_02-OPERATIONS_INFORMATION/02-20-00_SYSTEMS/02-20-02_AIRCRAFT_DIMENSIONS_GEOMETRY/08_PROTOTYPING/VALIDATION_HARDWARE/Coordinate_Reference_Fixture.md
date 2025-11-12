# Coordinate Reference Fixture

**Component:** ATA 02-11-00 - AIRCRAFT_DIMENSIONS_GEOMETRY  
**Document Type:** Hardware Specification  
**Platform:** AMPEL360 BWB H2 Hy-E Q100 INTEGRA  
**Version:** 1.0  
**Date:** 2025-11-11  
**Status:** Development

---

## Purpose

This document specifies the design and fabrication of a precision coordinate reference fixture system for the AMPEL360 Blended Wing Body aircraft. The fixture establishes and maintains the aircraft reference coordinate system (Station, Buttline, Waterline) throughout development, manufacturing, assembly, and testing phases.

---

## Overview

### Coordinate System Definition

**Aircraft Reference System:**
- **Station (FS):** Fuselage Station, longitudinal axis, positive forward from datum
- **Buttline (BL):** Lateral axis, positive to the right (looking forward)
- **Waterline (WL):** Vertical axis, positive upward from ground reference

**Datum Locations:**
- **FS 0:** Forward perpendicular at nose reference point
- **BL 0:** Aircraft centerline (plane of symmetry)
- **WL 0:** Ground plane when aircraft is in level flight attitude

### Fixture System Components

1. **Primary Datum Fixture** - Establishes FS 0, BL 0, WL 0
2. **Secondary Reference Fixtures** - Key structural interface points (4 locations)
3. **Portable Reference Probes** - Field measurement tools (set of 10)
4. **Laser Theodolite Targets** - Optical alignment targets (20 locations)
5. **Digital Coordinate Measurement System** - Electronic measurement network

---

## Design Requirements

### Accuracy Requirements

| Measurement | Target Accuracy | Tolerance Class |
|-------------|-----------------|-----------------|
| Position (X, Y, Z) | ±0.5 mm | Precision |
| Angle (Pitch, Roll, Yaw) | ±0.05° | High precision |
| Distance (point-to-point) | ±0.3 mm | Precision |
| Datum plane flatness | ±0.1 mm | High precision |
| Repeatability | ±0.2 mm | Precision |

### Material Requirements

- **Primary Structure:** Invar 36 (low thermal expansion coefficient)
- **Secondary Structure:** Aluminum 7075-T6
- **Target Spheres:** Ceramic (zirconia), 25.4mm diameter
- **Mounting Hardware:** Stainless steel 316
- **Surface Finish:** Ground and lapped to Ra ≤ 0.8 μm

### Environmental Stability

- **Thermal Expansion:** <1 ppm/°C (Invar components)
- **Temperature Range:** 15-25°C (operating), -20 to +60°C (storage)
- **Humidity Range:** 30-70% RH (non-condensing)
- **Vibration Resistance:** No permanent deformation under 0.5g
- **Corrosion Resistance:** 500-hour salt spray test per ASTM B117

---

## Component 1: Primary Datum Fixture

### Description

The primary datum fixture is a precision-machined monument that physically defines the aircraft's origin and three-axis coordinate system. It serves as the master reference for all measurements.

### Design Specifications

**Physical Configuration:**
- **Base Platform:** 1000mm (L) × 800mm (W) × 100mm (H)
- **Material:** Invar 36 plate, stress-relieved
- **Top Surface:** Ground flat and parallel to ±0.05mm
- **Mounting:** 4× anchor bolts to facility floor (grouted)

**Datum Features:**

1. **FS 0 Plane (Vertical)**
   - Precision ground surface, 500mm (H) × 600mm (W)
   - Perpendicularity to base: ±0.05mm over 500mm height
   - Reference marks: Laser-engraved cross hairs (center)

2. **BL 0 Plane (Vertical, perpendicular to FS 0)**
   - Precision ground surface, 500mm (H) × 800mm (W)
   - Perpendicularity to FS 0: ±0.05mm over 500mm height
   - Reference marks: Laser-engraved centerline

3. **WL 0 Plane (Horizontal)**
   - Top surface of base platform
   - Flatness: ±0.05mm over 1000mm × 800mm area
   - Reference grid: Laser-engraved 100mm × 100mm grid

**Target Spheres (3× ceramic, 25.4mm diameter):**
- Sphere #1: FS 0, BL 0, WL 500mm (defines Z-axis)
- Sphere #2: FS 500mm, BL 0, WL 0 (defines X-axis)
- Sphere #3: FS 0, BL 400mm, WL 0 (defines Y-axis)

**Installation:**
- Leveling: ±0.01° using precision spirit levels
- Alignment: Theodolite-based, referenced to facility grid
- Grouting: Non-shrink epoxy grout, 7-day cure
- Verification: CMM measurement of all features

---

## Component 2: Secondary Reference Fixtures

### Description

Four secondary fixtures located at key structural interfaces provide intermediate reference points and facilitate distributed measurements across the large BWB airframe.

### Fixture Locations

| Fixture ID | Location (FS, BL, WL) | Purpose |
|------------|-----------------------|---------|
| SRF-1 | FS 15.0, BL 0, WL 2.5 | Forward center body |
| SRF-2 | FS 25.0, BL 0, WL 8.0 | Main gear bulkhead |
| SRF-3 | FS 40.0, BL 0, WL 5.0 | Aft center body |
| SRF-4 | FS 20.0, BL ±15.0, WL 6.0 | Wing-body junction (2 fixtures) |

### Design (Per Fixture)

**Structure:**
- **Base Plate:** 300mm × 300mm × 20mm aluminum
- **Vertical Post:** 50mm × 50mm × 500mm aluminum extrusion
- **Target Sphere Mount:** Precision 3-jaw chuck, ceramic sphere

**Mounting:**
- Attached to aircraft structure via 4× M8 cap screws
- Interface: Precision-machined mounting holes (Ø8.0 +0.01/-0.00 mm)
- Torque: 20 Nm, thread-locked
- Shims: Stainless steel, 0.1mm thick, for leveling

**Adjustability:**
- X, Y adjustment: ±10mm via slotted holes
- Z adjustment: Shim stack under base plate
- Angular: ±2° tilt adjustment

**Features:**
- Target sphere: 25.4mm diameter ceramic (zirconia)
- Reflective targets: 3M retroreflective tape discs (50mm diameter)
- Engraved ID: Laser-marked fixture ID and nominal coordinates
- Protective cover: Removable polycarbonate dome

---

## Component 3: Portable Reference Probes

### Description

Handheld precision probes for field measurements and verification of local geometry relative to the established coordinate system.

### Specifications

**Design:**
- **Type:** Spring-loaded contact probe with ceramic ball tip
- **Body:** Anodized aluminum, Ø25mm × 200mm
- **Tip:** Ceramic sphere, Ø6mm, spring force 2-5N
- **Interface:** Magnetic base with 3-2-1 kinematic mount

**Measurement Capability:**
- Contact point repeatability: ±0.05mm
- Magnetic base holding force: 40kg
- Base flatness: ±0.01mm
- Weight: 0.5kg (manageable for overhead work)

**Set Contents (10 probes):**
- 6× Standard probes (200mm length)
- 2× Extended probes (400mm length)
- 2× Right-angle probes (for tight spaces)

**Accessories:**
- Calibration fixture (cone socket, 3-point)
- Storage case (foam-lined, hard shell)
- Cleaning kit (lint-free wipes, isopropyl alcohol)

**Applications:**
- Door frame measurements
- Panel alignment checks
- Skin contour verification
- Fastener hole positions

---

## Component 4: Laser Theodolite Targets

### Description

Optical targets for theodolite-based measurements, providing non-contact coordinate determination across large distances.

### Target Specifications

**Target Design:**
- **Type:** Precision sphere with reflector mount
- **Sphere Material:** Ceramic (zirconia), ultra-smooth surface
- **Sphere Diameter:** 38.1mm (1.5 inches) per ISO 10360
- **Sphere Grade:** Grade 5 (sphericity ≤1.25 μm)
- **Reflector:** 3M™ retroreflective prismatic film (50mm disc on top)

**Mount Design:**
- **Stem:** Stainless steel, Ø12mm × 50mm
- **Thread:** M8 × 1.25mm for attachment to aircraft
- **Base:** Magnetic or bolt-on, depending on location
- **Adjustment:** ±5° tilt for optimal reflector orientation

**Target Network (20 locations):**

| Target ID | Location (FS, BL, WL) | Mount Type |
|-----------|-----------------------|------------|
| TGT-01 | FS 0, BL 0, WL 2.0 | Magnetic |
| TGT-02 | FS 10, BL 0, WL 5.0 | Bolt-on |
| TGT-03 | FS 20, BL 0, WL 8.0 | Bolt-on |
| TGT-04 | FS 30, BL 0, WL 7.0 | Bolt-on |
| TGT-05 | FS 40, BL 0, WL 5.0 | Bolt-on |
| TGT-06 | FS 50, BL 0, WL 3.0 | Magnetic |
| TGT-07 | FS 15, BL ±10, WL 6.0 | Bolt-on (2) |
| TGT-08 | FS 25, BL ±15, WL 7.0 | Bolt-on (2) |
| TGT-09 | FS 35, BL ±20, WL 7.0 | Bolt-on (2) |
| TGT-10 | FS 15, BL ±30, WL 6.5 | Magnetic (2) - Wingtips |

**Calibration:**
- Each sphere measured on CMM (diameter, sphericity)
- Calibration certificate with traceability to NIST
- Recalibration interval: 2 years or after impact/damage

---

## Component 5: Digital Coordinate Measurement System

### Description

Electronic measurement network using iGPS (indoor GPS) or laser tracker technology for real-time, distributed coordinate measurement.

### System Specifications

**Technology:** Nikon iGPS or Leica Absolute Tracker AT960

**Performance:**
- **Measurement Volume:** 60m × 60m × 20m (sufficient for BWB)
- **Accuracy:** ±0.2mm (within 20m range)
- **Resolution:** 0.01mm
- **Update Rate:** 40 Hz (real-time)
- **Measurement Range:** 1-60m

**Transmitter/Sensor Configuration:**

**For iGPS:**
- 4× transmitters mounted on gantry or ceiling
- Transmitter spacing: 15-20m
- Calibration: Factory-calibrated, verified on-site

**For Laser Tracker:**
- 1× laser tracker on precision tripod
- Automated positioning: Motorized pan/tilt head
- Reflector targets: Spherically mounted retroreflectors (SMR), 38.1mm

**Measurement Probes:**
- Wireless handheld probes (battery, 8-hour life)
- Integrated reflector or iGPS sensor
- Trigger button for point capture
- LED indicators (status, GPS lock)

**Software:**
- **Data Acquisition:** Proprietary measurement software
- **Data Processing:** Polyworks or Spatial Analyzer
- **CAD Comparison:** Import CATIA model, best-fit alignment
- **Reporting:** Automated deviation reports with color maps

**Applications:**
- Major assembly alignment (wing-to-body join)
- Jig and fixture verification
- Production quality control
- As-built documentation

---

## Calibration and Traceability

### Calibration Hierarchy

**Primary Reference:**
- NIST-traceable gauge blocks and length standards
- Certified CMM at ISO 17025 accredited laboratory

**Secondary Reference:**
- Primary Datum Fixture (measured on certified CMM)
- Annual verification required

**Working Standards:**
- Secondary Reference Fixtures (measured against Primary Datum)
- Semi-annual verification

**Field Instruments:**
- Portable Probes, Laser Targets (measured against Working Standards)
- Quarterly verification

### Calibration Procedures

**Primary Datum Fixture (Annual):**
1. Remove from aircraft environment
2. Transport to CMM laboratory (climate-controlled)
3. Full 3D scan of all datum features
4. Measure target sphere positions (X, Y, Z)
5. Verify flatness, perpendicularity, parallelism
6. Issue calibration certificate
7. Reinstall and re-level at facility

**Secondary Reference Fixtures (Semi-Annual):**
1. Measurement in-situ using laser tracker
2. Compare to nominal positions (from Primary Datum)
3. Check deviations: ±0.5mm acceptable, ±1.0mm action limit
4. Re-adjust if necessary, re-measure
5. Document in calibration log

**Portable Probes (Quarterly):**
1. Contact repeatability test (cone socket)
2. 10 measurements, calculate standard deviation
3. Acceptance: σ < 0.03mm
4. Clean and inspect for wear
5. Replace worn tips if needed

---

## Usage Guidelines

### Initial Setup

**Facility Preparation:**
1. Designate measurement area (climate-controlled)
2. Install primary datum fixture (level, aligned to facility grid)
3. Allow 48-hour stabilization period
4. Verify datum fixture using CMM or laser tracker

**Aircraft Installation:**
1. Position aircraft on jacks or support fixtures
2. Level aircraft (pitch ±0.05°, roll ±0.05°)
3. Install secondary reference fixtures at designated locations
4. Measure SRFs relative to primary datum
5. Install laser targets across airframe

**System Verification:**
1. Perform closed-loop measurement (traverse all targets)
2. Calculate network residuals (should be <±0.3mm)
3. Generate reference coordinate file
4. Archive baseline data

### Routine Measurements

**Daily Start-Up:**
1. Verify primary datum (visual inspection, no disturbance)
2. Power on digital measurement system
3. Warm-up period: 30 minutes
4. Check temperature (18-24°C), humidity (40-60%)

**Measurement Session:**
1. Measure known reference targets (verification)
2. If verification passes, proceed with measurements
3. Capture points of interest, tag with descriptive names
4. Export data at end of session

**Measurement Recording:**
- All measurements logged with timestamp, operator ID
- Ambient conditions recorded (temperature, humidity)
- Data files backed up to secure server

---

## Acceptance Testing

### Primary Datum Fixture Acceptance

**Flatness Test:**
- Measure WL 0 plane with 25-point grid (5×5)
- Calculate flatness deviation
- Requirement: ≤0.05mm over 1000mm × 800mm area

**Perpendicularity Test:**
- Measure FS 0 and BL 0 planes with laser square
- Measure deviation from 90° at 5 heights
- Requirement: ≤0.05mm over 500mm height

**Target Sphere Position Test:**
- Measure 3 target sphere centers with CMM
- Compare to nominal positions (FS/BL/WL)
- Requirement: ≤0.2mm deviation

### Secondary Fixture Acceptance

**Positional Accuracy:**
- Measure installed SRF positions with laser tracker
- Compare to nominal (from aircraft datum)
- Requirement: ≤0.5mm deviation (X, Y, Z)

**Stability Test:**
- Measure SRF position, apply 50N load, re-measure
- Calculate position shift
- Requirement: ≤0.1mm shift

---

## Maintenance

### Routine Maintenance

**Weekly:**
- Clean all optical surfaces (alcohol wipes)
- Check for physical damage or corrosion
- Verify target spheres are secure

**Monthly:**
- Lubricate adjustment mechanisms (light oil)
- Tighten mounting hardware (torque check)
- Inspect protective covers

**Quarterly:**
- Verify calibration of field instruments
- Clean and inspect all fixtures
- Update maintenance log

**Annually:**
- Full calibration cycle (all components)
- Replace wear parts (probe tips, covers)
- Comprehensive inspection by metrology engineer

---

## Safety and Handling

**Laser Safety:**
- Class 2 lasers: Avoid direct eye exposure
- Laser tracker: Automatic shut-off if beam interrupted
- Signage: "Laser in Use" when operating

**Mechanical Safety:**
- Fixtures are heavy (up to 50kg): Use proper lifting or two persons
- Magnetic bases: Ensure secure attachment before releasing
- Overhead work: Use safety glasses, hard hat in assembly areas

**Handling Procedures:**
- Always handle ceramic spheres with clean gloves
- Store fixtures in protective cases when not in use
- Transport in shock-resistant packaging

---

## Deliverables

### Hardware Deliverables

1. **1× Primary Datum Fixture** with installation kit
2. **4× Secondary Reference Fixtures** with mounting hardware
3. **10× Portable Reference Probes** with accessories
4. **20× Laser Theodolite Targets** with mounts
5. **1× Digital Coordinate Measurement System** (iGPS or Laser Tracker)
6. **Calibration Certificates** for all precision components
7. **Storage and Transport Cases** for all equipment

### Documentation Deliverables

1. **Fixture Design Drawings** (CAD, PDF)
2. **Installation Manual** (step-by-step procedures)
3. **User Manual** (operation and measurement)
4. **Calibration Procedures** (detailed methods)
5. **Maintenance Manual** (schedule and procedures)
6. **Acceptance Test Report** (as-built verification)

---

## Budget and Schedule

### Cost Breakdown

| Item | Cost (USD) |
|------|-----------|
| Primary Datum Fixture | $65,000 |
| Secondary Reference Fixtures (4×) | $40,000 |
| Portable Probes (10×) | $15,000 |
| Laser Targets (20×) | $12,000 |
| iGPS or Laser Tracker System | $150,000 |
| Calibration (initial) | $20,000 |
| Documentation | $8,000 |
| Contingency (10%) | $31,000 |
| **Total** | **$341,000** |

### Development Schedule

| Phase | Duration | Completion |
|-------|----------|------------|
| Design | 6 weeks | Week 6 |
| Procurement | 8 weeks | Week 14 |
| Fabrication | 12 weeks | Week 26 |
| Initial Calibration | 3 weeks | Week 29 |
| Installation & Testing | 2 weeks | Week 31 |
| Training | 1 week | Week 32 |
| **Total** | **32 weeks** | **Complete** |

---

## Related Documents

- Station_BL_WL_Visualizer_v1.py
- Ground_Clearance_Measurement_Fixtures.md
- Dimension_Test_Results_Log.csv
- ATA 02-11-00 Requirements Document

---

## Document Control

**Revision History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-11 | AMPEL360 Engineering | Initial release |

**Approval:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Chief Metrology Engineer | TBD | ___________ | ______ |
| Manufacturing Engineer | TBD | ___________ | ______ |
| Quality Assurance Manager | TBD | ___________ | ______ |
| Project Manager | TBD | ___________ | ______ |

---

**Copyright © 2025 AMPEL360 Project. All Rights Reserved.**
