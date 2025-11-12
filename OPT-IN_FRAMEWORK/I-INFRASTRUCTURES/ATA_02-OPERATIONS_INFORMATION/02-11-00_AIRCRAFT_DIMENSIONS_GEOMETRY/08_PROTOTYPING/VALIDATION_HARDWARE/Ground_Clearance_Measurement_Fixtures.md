# Ground Clearance Measurement Fixtures

**Component:** ATA 02-11-00 - AIRCRAFT_DIMENSIONS_GEOMETRY  
**Document Type:** Hardware Specification  
**Platform:** AMPEL360 BWB H2 Hy-E Q100 INTEGRA  
**Version:** 1.0  
**Date:** 2025-11-11  
**Status:** Development

---

## Purpose

This document specifies the design and fabrication of precision measurement fixtures for validating ground clearance at critical points on the AMPEL360 Blended Wing Body aircraft. These fixtures enable accurate, repeatable measurements during various stages of aircraft development, from scale model validation to full-scale prototype testing.

---

## Fixture Overview

### Fixture Types

1. **Fixed-Height Reference Gauges** - Non-contact verification of minimum clearances
2. **Adjustable Contact Probes** - Direct measurement of clearance distances
3. **Laser Scanning Array** - Automated 3D clearance mapping
4. **Mobile Measurement Cart** - Portable fixture for field measurements

---

## Design Requirements

### Measurement Accuracy

| Fixture Type | Target Accuracy | Resolution | Repeatability |
|--------------|-----------------|------------|---------------|
| Reference Gauges | ±2 mm | 1 mm | ±1 mm |
| Contact Probes | ±1 mm | 0.5 mm | ±0.5 mm |
| Laser Array | ±0.5 mm | 0.1 mm | ±0.3 mm |
| Mobile Cart | ±2 mm | 1 mm | ±1 mm |

### Environmental Conditions

- **Operating Temperature:** -10°C to +50°C
- **Storage Temperature:** -20°C to +60°C
- **Humidity:** 10-90% RH (non-condensing)
- **Protection:** IP54 minimum (dust and splash resistant)

### Material Requirements

- **Structural:** Aluminum 6061-T6 or steel (corrosion-resistant)
- **Contact Surfaces:** Nylon or UHMW polyethylene (non-marring)
- **Hardware:** Stainless steel fasteners
- **Finish:** Anodized aluminum or powder coat paint

---

## Fixture Type 1: Fixed-Height Reference Gauges

### Description

Vertical posts with calibrated height markings that provide visual/physical reference for minimum clearance verification. Used for quick pass/fail checks without electronic instrumentation.

### Specifications

**Design:**
- Telescoping aluminum post
- Height range: 0.5m to 5.0m adjustable
- Graduated markings every 10mm
- High-visibility orange color
- Weighted base (15 kg) for stability

**Critical Height Gauges (Set of 13):**

| Gauge ID | Location | Nominal Height | Tolerance |
|----------|----------|----------------|-----------|
| RG-01 | Left Wingtip | 2.5 m | ±0.010 m |
| RG-02 | Right Wingtip | 2.5 m | ±0.010 m |
| RG-03 | Forward Belly | 1.8 m | ±0.010 m |
| RG-04 | Center Belly | 1.8 m | ±0.010 m |
| RG-05 | Aft Belly | 1.8 m | ±0.010 m |
| RG-06 | Left Engine Intake | 2.0 m | ±0.010 m |
| RG-07 | Right Engine Intake | 2.0 m | ±0.010 m |
| RG-08 | Aft Tail Tip | 3.2 m | ±0.010 m |
| RG-09 | Nose Gear Door | 1.5 m | ±0.010 m |
| RG-10 | Left Main Gear Door | 1.5 m | ±0.010 m |
| RG-11 | Right Main Gear Door | 1.5 m | ±0.010 m |
| RG-12 | Left TE Tip | 2.8 m | ±0.010 m |
| RG-13 | Right TE Tip | 2.8 m | ±0.010 m |

**Features:**
- Quick-release height adjustment with locking collar
- Bubble level integrated in base for vertical alignment
- Reflective tape for low-light visibility
- Carrying handle for portability
- Storage bag for protection

**Calibration:**
- Traceable to NIST standards
- Annual re-certification required
- Calibration certificate included

---

## Fixture Type 2: Adjustable Contact Probes

### Description

Precision measuring instruments with extendable probe tips that make direct contact with the aircraft surface. Provides accurate digital readout of clearance distance.

### Specifications

**Design:**
- Digital height gauge with telescoping probe
- Measurement range: 0-5000 mm
- Display: LCD, 10mm digit height
- Resolution: 0.01 mm
- Accuracy: ±0.05 mm (within 500mm), ±0.10 mm (up to 5000mm)

**Features:**
- Zero-set function at any position
- Data output: RS-232 serial, USB
- Data logging: 1000 measurement memory
- Battery life: >100 hours continuous use
- Water-resistant housing (IP65)

**Probe Tip Options:**
- **Standard Ball Tip:** 10mm diameter carbide sphere
- **Flat Tip:** 20mm diameter UHMW disc (for belly surfaces)
- **Pointed Tip:** 2mm carbide cone (for tight spaces)

**Base Configuration:**
- Magnetic base (switchable, 80 kg holding force)
- Articulating arm (5 degrees of freedom)
- Fine adjustment: ±50 mm in X, Y, Z
- Locking mechanism for all joints

**Applications:**
- Detailed clearance mapping
- Pre-flight/post-flight inspections
- Comparison measurements (left vs. right)
- Deflection measurements under load

---

## Fixture Type 3: Laser Scanning Array

### Description

Automated 3D laser scanning system for comprehensive clearance mapping. Provides full-field measurement data and generates 3D clearance maps.

### Specifications

**System Configuration:**
- 4× laser line scanners (2D profile)
- Scanner positioning: Gantry or tripod-mounted
- Scan width: 500mm per scanner, 2000mm total
- Scan rate: 100 profiles/second
- Point density: 0.5mm spacing

**Laser Specifications:**
- Type: Class 2 laser (eye-safe)
- Wavelength: 650 nm (red)
- Line width: 500mm @ 1m distance
- Standoff distance: 0.5-2.0m

**Measurement Performance:**
- Range accuracy: ±0.5mm
- Lateral resolution: 0.2mm
- Repeatability: ±0.3mm
- Scan time (full aircraft): 30 minutes

**Data Output:**
- Point cloud format: XYZ ASCII, PLY, STL
- Software: Proprietary control and processing suite
- Visualization: 3D false-color clearance map
- Report generation: Automated clearance analysis

**Positioning System:**
- Portable gantry (aluminum extrusion)
- Dimensions: 6m (L) × 4m (W) × 3m (H)
- Positioning accuracy: ±1mm in X-Y, ±0.5mm in Z
- Automated traverse: Stepper motor driven

**Applications:**
- Initial geometry validation
- Production quality control
- Deflection mapping under load
- Comparison with CAD model (digital twin)

---

## Fixture Type 4: Mobile Measurement Cart

### Description

Wheeled cart with integrated measurement systems for field use during flight testing, ground operations, and maintenance. Provides rapid clearance checks without dedicated facilities.

### Specifications

**Cart Design:**
- Dimensions: 1.2m (L) × 0.8m (W) × 1.5m (H)
- Weight: 80 kg (loaded)
- Wheels: 4× pneumatic, 200mm diameter, locking casters
- Handle: Ergonomic push handle with hand brake

**Measurement Systems Onboard:**
1. **Ultrasonic Distance Sensors (8×)**
   - Range: 0.3-5.0m
   - Accuracy: ±3mm or 1% of reading
   - Beam angle: 15°
   - Update rate: 10 Hz

2. **Laser Distance Meter (1×)**
   - Range: 0.05-80m
   - Accuracy: ±1.5mm
   - Beam divergence: <6mm @ 10m
   - Display: Backlit LCD

3. **Inclinometer (1×)**
   - Range: ±15° pitch/roll
   - Accuracy: ±0.1°
   - Digital display

4. **Digital Camera (1×)**
   - Resolution: 12 MP
   - Video: 1080p @ 60fps
   - Zoom: 10× optical
   - Mounting: Adjustable tripod head

**Power System:**
- Battery: 12V 100Ah lithium-ion
- Runtime: 8 hours continuous use
- Charging: 120/240V AC, 4-hour charge time
- Solar panel: Optional 100W panel for field use

**Data Management:**
- Tablet computer (ruggedized, 10" screen)
- Software: Custom clearance measurement app
- Data storage: 256GB SSD + cloud sync
- GPS: Integrated for location tagging

**Accessories:**
- Adjustable mast (extends to 4m height)
- Articulating arm for sensor positioning
- Tool tray for accessories
- Weather-resistant cover

---

## Calibration and Maintenance

### Calibration Schedule

| Fixture Type | Frequency | Method | Certifying Body |
|--------------|-----------|--------|-----------------|
| Reference Gauges | Annual | Height comparison to standards | ISO 17025 lab |
| Contact Probes | 6 months | Gauge block verification | ISO 17025 lab |
| Laser Array | 3 months | Artifact measurement | Manufacturer or lab |
| Mobile Cart Sensors | 6 months | Distance standard verification | In-house or lab |

### Calibration Procedure (Contact Probes)

1. **Pre-Calibration:**
   - Clean probe tip and surfaces
   - Allow thermal stabilization (2 hours at lab temp)
   - Record ambient temperature and humidity

2. **Calibration Points:**
   - 100mm gauge block: Measure 5×, record
   - 500mm gauge block: Measure 5×, record
   - 1000mm gauge block: Measure 5×, record
   - 2000mm master scale: Measure at 5 positions

3. **Acceptance Criteria:**
   - Mean deviation: <±0.05mm (100-500mm), <±0.10mm (>500mm)
   - Standard deviation: <0.02mm
   - Linearity: <0.05mm over full range

4. **Post-Calibration:**
   - Affix calibration sticker with expiration date
   - Update calibration database
   - Issue calibration certificate

### Maintenance Schedule

**Daily (Before Use):**
- Visual inspection for damage
- Battery charge check (mobile cart)
- Cleanliness check (sensors, probe tips)

**Weekly:**
- Clean all optical surfaces (laser scanners)
- Lubricate moving parts (probe arms)
- Tighten any loose fasteners

**Monthly:**
- Functional test all measurement systems
- Verify data logging and output
- Check base stability (weighted bases)

**Annually:**
- Comprehensive inspection by technician
- Replace wear parts (probe tips, wheels)
- Software updates
- Full calibration cycle

---

## Usage Guidelines

### Pre-Measurement Setup

1. **Aircraft Positioning:**
   - Level aircraft using jacks or leveling gear
   - Verify level attitude with digital inclinometers (±0.1°)
   - Record loading condition (empty, typical, MTOW)
   - Document fuel and ballast weights

2. **Fixture Setup:**
   - Position reference gauges per measurement plan
   - Verify gauge verticality (bubble level)
   - For laser array: Assemble gantry, align to aircraft datum
   - For mobile cart: Charge battery, initialize sensors

3. **Environmental Conditions:**
   - Record temperature, humidity, barometric pressure
   - Note any strong winds or vibrations
   - Ensure adequate lighting for visual inspection

### Measurement Procedure

**Reference Gauge Method:**
1. Position gauge at specified aircraft station
2. Verify gauge height matches requirement
3. Observe clearance (aircraft structure should not contact gauge)
4. Record pass/fail, photograph if clearance marginal
5. Repeat for all 13 critical points

**Contact Probe Method:**
1. Zero probe on ground plane adjacent to aircraft
2. Position probe tip in contact with lowest point of structure
3. Read clearance value from display
4. Record measurement with location tag
5. Repeat measurement 3× for verification
6. Move to next measurement point

**Laser Scanning Method:**
1. Start scanning software, verify sensor connectivity
2. Define scan area and resolution
3. Execute automated scan (30 min duration)
4. Process point cloud data
5. Generate 3D clearance map with color coding
6. Export data for analysis and archiving

### Data Recording

**Measurement Log Format:**

```
Date: YYYY-MM-DD
Time: HH:MM
Aircraft Serial: AMPEL-XXX
Loading Condition: [Empty/Typical/MTOW/MLW]
Pitch Attitude: ±X.X°
Roll Attitude: ±X.X°
Temperature: XX°C
Humidity: XX%
Measured by: [Name]

Clearance Measurements:
Point ID | Location | Target | Measured | Deviation | Status
---------|----------|--------|----------|-----------|-------
CP-01    | LH Wingtip | 2.50m | 2.48m | -0.02m | PASS
...
```

---

## Safety Considerations

### Personnel Safety

- **Laser Hazards:** Class 2 lasers used; avoid direct eye exposure
- **Mechanical Hazards:** Pinch points on adjustable fixtures; use care when adjusting
- **Electrical Hazards:** Battery-powered equipment; follow manufacturer guidelines
- **Lifting:** Mobile cart is 80kg; use proper lifting technique or two persons

### Aircraft Protection

- **Non-Marring Contact:** All fixtures use soft contact surfaces (nylon, UHMW)
- **Load Limits:** Do not apply excessive force with contact probes (max 5N)
- **Clearance:** Maintain 50mm safety margin when positioning fixtures near aircraft
- **Stability:** Ensure all fixtures are stable and will not tip onto aircraft

---

## Deliverables

### Hardware Deliverables

1. **13× Reference Gauges** (RG-01 through RG-13)
2. **4× Contact Probe Systems** (with articulating arms and magnetic bases)
3. **1× Laser Scanning Array** (4 scanners + gantry system)
4. **2× Mobile Measurement Carts** (fully equipped)
5. **Calibration Certificates** (for all traceable instruments)
6. **Storage Cases** (for all equipment)

### Documentation Deliverables

1. **Fixture Design Drawings** (CAD, PDF)
2. **User Manuals** (operation and maintenance)
3. **Calibration Procedures** (detailed step-by-step)
4. **Software User Guides** (laser scanner, mobile cart app)
5. **Safety Data Sheets** (materials, batteries)

---

## Budget and Schedule

### Cost Breakdown

| Item | Quantity | Unit Cost | Total Cost |
|------|----------|-----------|------------|
| Reference Gauges | 13 | $800 | $10,400 |
| Contact Probes | 4 | $3,500 | $14,000 |
| Laser Scanners | 4 | $15,000 | $60,000 |
| Gantry System | 1 | $25,000 | $25,000 |
| Mobile Carts | 2 | $12,000 | $24,000 |
| Tablet Computers | 2 | $1,500 | $3,000 |
| Accessories | — | — | $8,000 |
| Calibration (initial) | — | — | $5,000 |
| Software Development | — | — | $15,000 |
| Documentation | — | — | $5,000 |
| Contingency (10%) | — | — | $17,000 |
| **Total** | — | — | **$186,400** |

### Development Schedule

| Phase | Duration | Milestone |
|-------|----------|-----------|
| Design & Procurement | 6 weeks | Designs approved, orders placed |
| Fabrication | 10 weeks | Hardware delivered |
| Software Development | 8 weeks | Software tested and validated |
| Integration & Testing | 4 weeks | Systems operational |
| Calibration | 2 weeks | Calibration certificates issued |
| Training | 1 week | Personnel trained |
| **Total** | **31 weeks** | **Complete measurement capability** |

---

## Related Documents

- Ground_Clearance_Prototype_Tool_v1.py
- Coordinate_Reference_Fixture.md
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
| Metrology Engineer | TBD | ___________ | ______ |
| Quality Assurance Manager | TBD | ___________ | ______ |
| Project Manager | TBD | ___________ | ______ |

---

**Copyright © 2025 AMPEL360 Project. All Rights Reserved.**
