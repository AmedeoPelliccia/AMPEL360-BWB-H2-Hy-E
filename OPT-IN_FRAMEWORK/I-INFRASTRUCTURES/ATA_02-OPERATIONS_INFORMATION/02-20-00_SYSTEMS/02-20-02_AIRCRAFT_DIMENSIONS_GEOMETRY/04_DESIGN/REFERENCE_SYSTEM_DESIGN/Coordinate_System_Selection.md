# Coordinate System Selection

**Document ID:** AMPEL360-02-11-00-DES-RS-001  
**Version:** 1.0.0

## Reference System Overview

**Standard:** ATA 100 / ISO 1151-1 compatible

## Coordinate System Definition

### Body Axis System

**Origin:** Nose apex (Station 0, Buttline 0, Waterline 0)

**Axes:**
- X-axis: Positive aft (longitudinal)
- Y-axis: Positive right (lateral)
- Z-axis: Positive down (vertical)

**Right-hand rule:** Standard aircraft convention

### Station System (Fuselage/Body Stations - FS/BS)

**Definition:** Longitudinal measurement along X-axis

**Key Stations:**
- FS 0: Nose apex
- FS 2500: Forward pressure bulkhead
- FS 15000: Center body maximum width
- FS 27000: Aft pressure bulkhead
- FS 28500: Aft end (tail cone)

**Units:** Millimeters (mm)

### Buttline System (BL)

**Definition:** Lateral measurement along Y-axis from centerline

**Key Buttlines:**
- BL 0: Aircraft centerline
- BL ±19000: Maximum width (38m total)
- BL ±26000: Wingtip (52m span)

**Symmetry:** Aircraft symmetric about BL 0

### Waterline System (WL)

**Definition:** Vertical measurement along Z-axis

**Reference:** Ground level at static MTOW condition

**Key Waterlines:**
- WL 0: Ground reference (MTOW static)
- WL 3200: Landing gear extension
- WL 5000: Cabin floor level
- WL 8500: Upper deck (H₂ tanks)

## Datum Point

**Location:** FS 15000, BL 0, WL 5000

**Rationale:**
- Center of aircraft (geometric)
- Near center of gravity
- Convenient for calculations
- Digital twin origin point

## Measurement Convention

**Distance Measurements:**
- Along body axis: Stations (FS)
- Perpendicular to centerline: Buttlines (BL)
- Vertical: Waterlines (WL)

**All dimensions in millimeters for precision**

## Digital Twin Integration

**CAD Model:**
- Origin: Datum point (FS 15000, BL 0, WL 5000)
- Coordinate system: Right-hand rule
- Units: Millimeters
- Format: STEP AP242 (ISO 10303-242)

**Data Management:**
- Version control: PDM system
- Change tracking: Full traceability
- Configuration: Baseline frozen

## Certification Documentation

**Compliance:**
- ATA 100: Full compliance
- ISO 1151-1: Full compliance
- CS-25: Reference system approved

**Status:** Baseline frozen  
**Approved:** 2024-02-01
