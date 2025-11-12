# 1:20 Scale BWB Geometry Model

**Component:** ATA 02-11-00 - AIRCRAFT_DIMENSIONS_GEOMETRY  
**Document Type:** Scale Model Specification  
**Platform:** AMPEL360 BWB H2 Hy-E Q100 INTEGRA  
**Version:** 1.0  
**Date:** 2025-11-11  
**Status:** Development

---

## Purpose

This document specifies the 1:20 scale model of the AMPEL360 Blended Wing Body aircraft for geometry validation, wind tunnel testing, and dimensional verification. The scale model serves as a critical tool for validating the aircraft's external dimensions, aerodynamic shape, and ground clearance characteristics.

---

## Model Overview

### Scale Factor: 1:20

**Full-Scale Aircraft Dimensions:**
- Wingspan: 65.0 m
- Overall Length: 52.0 m
- Overall Height: 15.5 m
- Wing Area: 850.0 m²
- Center Body Width: 28.0 m

**Scale Model Dimensions:**
- Wingspan: 3.250 m (3250 mm)
- Overall Length: 2.600 m (2600 mm)
- Overall Height: 0.775 m (775 mm)
- Wing Area: 2.125 m²
- Center Body Width: 1.400 m (1400 mm)

### Model Classification

- **Type:** High-fidelity geometry validation model
- **Primary Purpose:** Dimensional verification and wind tunnel testing
- **Secondary Purpose:** Visual mockup for stakeholder presentations
- **Construction Method:** CNC machined from tooling board, with carbon fiber reinforcement
- **Finish:** High-quality surface finish (Ra < 1.6 μm) for accurate aerodynamic testing

---

## Design Specifications

### Geometric Accuracy

**Tolerance Class:** Precision model
- **Primary Surfaces:** ±0.5 mm (±10 mm full-scale equivalent)
- **Secondary Surfaces:** ±1.0 mm (±20 mm full-scale equivalent)
- **Control Surfaces:** ±0.3 mm (±6 mm full-scale equivalent)
- **Panel Lines:** ±0.1 mm (±2 mm full-scale equivalent)

**Critical Dimensions to Verify:**
1. Wingspan (tip-to-tip)
2. Overall length (nose to tail)
3. Overall height (ground to highest point)
4. Center body width and profile
5. Wingtip clearance from ground
6. Landing gear geometry
7. Control surface deflection ranges
8. Door and access panel locations

### Aerodynamic Fidelity

**Surface Quality:**
- All aerodynamic surfaces CNC machined
- Surface roughness: Ra ≤ 1.6 μm (equivalent to polished metal)
- Minimal panel lines and joints on upper surface
- Smooth transitions between body and wing sections

**Features Included:**
- ✓ Blended wing-body contour (full fidelity)
- ✓ Wingtip devices (winglets)
- ✓ Control surfaces (elevons, rudders)
- ✓ Engine nacelles/propulsor fairings
- ✓ Landing gear bays (simplified)
- ✓ Passenger door outlines
- ✓ Sensor apertures (pitot, static ports)
- ✗ Rivets and fasteners (omitted for wind tunnel)
- ✗ Antennas (removable for testing)

---

## Material Specifications

### Primary Structure

**Material:** High-density polyurethane tooling board (RenShape® 5166 or equivalent)
- **Density:** 480 kg/m³
- **Compressive Strength:** 12.4 MPa
- **Thermal Stability:** -30°C to +80°C
- **Machinability:** Excellent (CNC compatible)
- **Moisture Resistance:** Good

**Reinforcement:** Carbon fiber (selective areas)
- **Location:** Wing tips, tail surfaces, mounting points
- **Layup:** 2-ply, plain weave, 200 g/m²
- **Resin:** Epoxy (low-viscosity for infusion)

### Surface Coating

**Primer:**
- 2K polyurethane primer-surfacer
- 3 coats, 100 μm total thickness
- Wet-sanded to final surface finish

**Topcoat:**
- 2K polyurethane paint (AMPEL360 livery)
- High-gloss finish (>85 gloss units)
- UV-resistant formulation
- Color: White base with blue/green accents

---

## Construction Method

### Phase 1: Digital Model Preparation (2 weeks)

**CAD Model Processing:**
1. Export full-scale CATIA model
2. Scale to 1:20 in CAD software
3. Verify all critical dimensions at scale
4. Generate sectioned geometry for assembly
5. Create CNC toolpaths

**Sections for Manufacturing:**
- Section A: Nose (FS 0-10 → 0-500mm scale)
- Section B: Forward center body (FS 10-25 → 500-1250mm)
- Section C: Aft center body (FS 25-40 → 1250-2000mm)
- Section D: Tail section (FS 40-52 → 2000-2600mm)
- Section E: Left wing panel (BL 0 to -32.5 → 0 to -1625mm)
- Section F: Right wing panel (BL 0 to +32.5 → 0 to +1625mm)

### Phase 2: CNC Machining (6 weeks)

**Equipment:**
- 5-axis CNC mill (minimum 2m × 2m working envelope)
- Tooling: Ball-end mills (6mm, 12mm, 20mm)
- Workholding: Vacuum table with soft jaws

**Process per Section:**
1. Rough machining (0.5mm stepover, 2mm depth)
2. Finish machining (0.1mm stepover, 0.5mm depth)
3. Manual finishing (sanding, filling)
4. Quality inspection (CMM scan)

**Acceptance Criteria:**
- Dimensional accuracy: ±0.5mm
- Surface roughness: Ra ≤ 3.2 μm (pre-coating)
- No visible tool marks or gouges

### Phase 3: Assembly (3 weeks)

**Alignment and Bonding:**
1. Dry-fit all sections using alignment pins
2. Check fit and finish at all joints
3. Bond sections using epoxy adhesive
4. Reinforce joints with carbon fiber tape
5. Fill and fair seams

**Internal Structure:**
- Central spar (aluminum tube, 40mm OD)
- Mounting hard points (threaded inserts)
- Balance weights (lead shot in bags)
- Instrumentation cavities (pressure taps)

### Phase 4: Surface Finishing (2 weeks)

**Filling and Fairing:**
1. Apply lightweight filler to all seams
2. Sand smooth (progression: 80, 120, 220, 400 grit)
3. Apply primer-surfacer (3 coats)
4. Wet-sand to final surface (600, 1000, 1500 grit)
5. Inspect for imperfections

**Painting:**
1. Clean surface (solvent wipe)
2. Mask off specific areas
3. Apply topcoat (3 coats, 50 μm each)
4. Cure per manufacturer spec
5. Unmask and touch-up
6. Apply decals (AMPEL360 livery)
7. Clear coat (2 coats, 25 μm each)

### Phase 5: Instrumentation (1 week)

**Pressure Taps:**
- 50× static pressure ports
- Locations per wind tunnel test plan
- Tubing routed internally to balance cavity

**Mounting Points:**
- Sting mount (underside, FS 22 location)
- Ground support stand sockets (3 locations)
- Lifting eyes (4 locations)

---

## Landing Gear

### Configuration

**Type:** Retractable tricycle, partially functional
- **Nose Gear:** Single wheel, steerable
- **Main Gear:** Dual-wheel bogies (left and right)
- **Retraction:** Manual or motorized (optional)

**Scale Dimensions:**

| Parameter | Full Scale | 1:20 Scale |
|-----------|------------|------------|
| Nose Gear Height | 3.2 m | 160 mm |
| Main Gear Height | 3.8 m | 190 mm |
| Nose Gear Position | FS 10.0 | 500 mm |
| Main Gear Position | FS 15.0 | 750 mm |
| Track (main gear) | 12.0 m | 600 mm |

**Construction:**
- **Struts:** Aluminum tube, 8mm OD
- **Wheels:** Rubber, 40mm diameter (nose), 50mm diameter (main)
- **Retraction Mechanism:** Servo-driven (optional feature)
- **Doors:** Removable panels

---

## Instrumentation and Test Capability

### Wind Tunnel Instrumentation

**Force Balance Interface:**
- 6-component strain gauge balance (sting-mounted)
- Load ranges: 
  - Lift: ±500 N
  - Drag: ±100 N
  - Side Force: ±100 N
  - Moments: ±50 Nm each axis

**Pressure Measurement:**
- 50× static pressure taps
- 1mm diameter holes, flush with surface
- Connected to Scanivalve system (0-10 psid)
- Sample rate: 100 Hz

**Flow Visualization:**
- Tufts: 100× wool tufts (20mm long)
- Smoke: Smoke wire or rake capability
- Oil flow: Surface oil application
- PSP: Pressure-sensitive paint compatible surface

### Ground Testing Instrumentation

**Position Measurement:**
- 4× laser distance sensors (ground clearance)
- Digital inclinometer (pitch/roll)
- GPS tracker (for transport)

**Photo Documentation:**
- Fiducial markers (20 locations)
- Photogrammetry compatible
- 3D scanning reference points

---

## Validation and Acceptance Testing

### Dimensional Verification

**Method:** Coordinate Measuring Machine (CMM)
- **Equipment:** FARO Edge or equivalent arm
- **Accuracy:** ±0.025mm
- **Measurement Points:** 500+ locations
- **Comparison:** CAD model vs. as-built

**Critical Dimensions Checklist:**

| Dimension | Target (mm) | Tolerance (mm) | Method |
|-----------|-------------|----------------|--------|
| Wingspan | 3250.0 | ±1.0 | CMM |
| Overall Length | 2600.0 | ±1.0 | CMM |
| Overall Height | 775.0 | ±1.0 | CMM |
| Center Body Width | 1400.0 | ±1.0 | CMM |
| Wing Root Chord | 1450.0 | ±2.0 | CMM |
| Wing Tip Chord | 140.0 | ±1.0 | CMM |
| Sweep Angle (25% chord) | 35.0° | ±0.5° | CAD comp |
| Dihedral | 2° | ±0.3° | Inclinometer |

**Documentation:**
- CMM scan data (IGES format)
- Deviation map (color-coded)
- As-built drawings (annotated CAD)
- Non-conformance report (if applicable)

### Surface Quality Inspection

**Visual Inspection:**
- No visible tool marks, gouges, or defects
- Smooth transitions at all joints
- Paint finish uniform and glossy

**Tactile Inspection:**
- Run hand along surface (no snags or bumps)
- Check for voids or soft spots

**Quantitative Measurement:**
- Surface roughness: Ra ≤ 1.6 μm (10 locations)
- Paint thickness: 150-200 μm (20 locations)
- Gloss: ≥85 GU @ 60° (20 locations)

---

## Handling and Transport

### Support Stand

**Design:** Three-point support stand
- Supports under nose and main gear locations
- Adjustable height (±50mm)
- Non-marring contact surfaces (rubber pads)
- Lockable casters for mobility

**Storage Position:**
- Nose slightly elevated (3° pitch-up attitude)
- Protects tail from contact
- Accessible for inspection

### Transport Case

**Construction:**
- Rigid foam-lined shipping case
- Aluminum frame with latches
- Internal dimensions: 3500mm × 2000mm × 900mm
- Weight capacity: 150 kg
- Shock-mounted interior

**Accessories:**
- Dust cover (breathable fabric)
- Desiccant packs (humidity control)
- Handling gloves (white cotton)
- Inspection mirror

---

## Testing Applications

### Wind Tunnel Testing

**Suitable Facilities:**
- Low-speed wind tunnel (M < 0.3)
- Test section ≥ 4m × 3m
- Reynolds number: Re = 1-3 × 10⁶ (based on mean chord)

**Test Objectives:**
1. Validate aerodynamic coefficients (CL, CD, Cm)
2. Measure lift distribution across span
3. Characterize stall behavior
4. Assess control surface effectiveness
5. Flow visualization studies

**Expected Test Duration:** 40 hours tunnel time

### Geometry Validation

**Purpose:** Verify as-designed dimensions translate to physical model
- Cross-sections at 10 stations (FS 0, 5, 10, ... 50)
- Profile accuracy check
- Comparison with full-scale intent

### Photography and Marketing

**Visual Communication:**
- High-resolution photography for presentations
- 3D turntable video (360° rotation)
- Trade show display
- Investor briefings

---

## Maintenance and Care

### Routine Maintenance

**After Each Use:**
- Inspect for damage (nicks, scratches)
- Clean surface (mild soap and water)
- Dry thoroughly
- Return to storage stand

**Monthly:**
- Check for loose parts or degradation
- Touch-up paint if needed
- Verify alignment pins secure

### Long-Term Storage

**Environment:**
- Temperature: 15-25°C
- Humidity: 40-60% RH
- Covered with dust cover
- Avoid direct sunlight

**Inspection Schedule:**
- Quarterly visual inspection
- Annual dimensional check (key dimensions)

---

## Cost and Schedule Summary

### Budget Breakdown

| Item | Cost (USD) |
|------|-----------|
| Materials (tooling board, carbon fiber) | $8,000 |
| CNC Machining (6 weeks) | $25,000 |
| Surface finishing (primer, paint) | $3,000 |
| Landing gear fabrication | $2,000 |
| Instrumentation (pressure taps, wiring) | $4,000 |
| Transport case | $2,500 |
| Support stand | $1,000 |
| Quality inspection (CMM) | $2,000 |
| Labor (assembly, finishing) | $8,500 |
| Contingency (10%) | $5,600 |
| **Total** | **$61,600** |

### Schedule

| Phase | Duration | Completion |
|-------|----------|------------|
| CAD Preparation | 2 weeks | Week 2 |
| CNC Machining | 6 weeks | Week 8 |
| Assembly | 3 weeks | Week 11 |
| Surface Finishing | 2 weeks | Week 13 |
| Instrumentation | 1 week | Week 14 |
| Inspection & Acceptance | 1 week | Week 15 |
| **Total** | **15 weeks** | **Complete** |

---

## Deliverables

1. **Physical Model:** Fully finished 1:20 scale BWB aircraft
2. **Support Stand:** Three-point adjustable stand
3. **Transport Case:** Foam-lined shipping case
4. **Documentation Package:**
   - As-built drawings
   - CMM inspection report
   - Deviation analysis
   - Handling procedures
   - Maintenance manual
5. **Digital Assets:**
   - High-resolution photos (50+ images)
   - 3D scan data (point cloud)
   - CAD model (as-built, STEP format)

---

## Related Documents

- Geometry_Envelope_Tool_v1.py
- Wind_Tunnel_Geometry_Model_Specs.md
- Geometry_Model_Test_Results.csv
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
| Chief Engineer | TBD | ___________ | ______ |
| Aerodynamics Lead | TBD | ___________ | ______ |
| Manufacturing Manager | TBD | ___________ | ______ |
| Quality Assurance | TBD | ___________ | ______ |

---

**Copyright © 2025 AMPEL360 Project. All Rights Reserved.**
