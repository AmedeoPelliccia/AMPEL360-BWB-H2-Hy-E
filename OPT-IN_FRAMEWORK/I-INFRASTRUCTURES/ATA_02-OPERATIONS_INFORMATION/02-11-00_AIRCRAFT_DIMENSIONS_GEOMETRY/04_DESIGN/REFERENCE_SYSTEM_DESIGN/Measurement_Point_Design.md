# Measurement Point Design

**Document ID:** AMPEL360-02-11-00-DES-RS-004  
**Version:** 1.0.0

## Overview

**Purpose:** Define standard measurement points for aircraft dimensional verification and quality control.

## Primary Measurement Points

### Overall Dimensions

**Wingspan (BL ±26000):**
- Left tip: BL -26000
- Right tip: BL +26000
- Measurement: Tip to tip = 52,000mm
- Tolerance: ±10mm
- Method: Laser tracker

**Length (FS 0 to FS 28500):**
- Nose: FS 0
- Tail: FS 28500
- Measurement: 28,500mm
- Tolerance: ±10mm
- Method: Laser tracker

**Maximum Width (BL ±19000 at FS 15000):**
- Left: BL -19000
- Right: BL +19000
- Measurement: 38,000mm
- Tolerance: ±5mm
- Method: Laser tracker

**Maximum Height (WL 8500 at FS 15000):**
- Ground: WL 0
- Top: WL 8500
- Measurement: 8,500mm (static MTOW)
- Tolerance: ±10mm (gear compression variation)
- Method: Vertical measurement

## Structural Measurement Points

### Wing Box

**Spar Locations:**
- Front spar: Various stations
- Rear spar: Various stations
- Measurement: 3D coordinates
- Tolerance: ±1.0mm
- Method: CMM or laser tracker

### Pressure Bulkheads

**Forward Bulkhead (FS 2500):**
- Location: FS 2500 ±0.5mm
- Shape: Dome profile
- Measurement: Radial dimensions
- Tolerance: ±0.5mm (critical)

**Aft Bulkhead (FS 27000):**
- Location: FS 27000 ±0.5mm
- Shape: Dome profile
- Measurement: Radial dimensions
- Tolerance: ±0.5mm (critical)

## Critical Interface Points

### Landing Gear Attachment

**Main Gear (FS 10000 and FS 20000):**
- Location: Exactly defined
- Tolerance: ±0.5mm (load path)
- Measurement: 3D coordinates
- Method: CMM (precision required)

**Nose Gear (FS 5000):**
- Location: Centerline
- Tolerance: ±0.5mm
- Measurement: 3D coordinates
- Method: CMM

### H₂ Tank Mounting

**Tank Support Points:**
- Locations: 16 points (4 per tank)
- Tolerance: ±1.0mm
- Measurement: Coordinate verification
- Method: Laser tracker

## Assembly Measurement Points

### Tooling Balls

**Quantity:** 48 primary points

**Distribution:**
- Nose section: 8 points
- Center section: 24 points
- Aft section: 8 points
- Wings: 8 points (4 per side)

**Specification:**
- Diameter: 38.1mm (1.5")
- Material: Stainless steel
- Tolerance: ±0.025mm (sphere)
- Calibration: Annual

### Measurement Protocol

**Frequency:**
- Assembly: Each major join
- Final assembly: Complete verification
- Pre-flight (first flight): Full dimensional
- Production: Sample (1 in 10)

**Documentation:**
- Measurement report: Required
- Deviation report: If out-of-tolerance
- Engineering disposition: For deviations
- Archive: Permanent record (serial number)

## Ground Clearance Measurement

**Critical Points:**
- Wingtip height: WL measurement at BL ±26000
- Belly clearance: Minimum WL (various stations)
- Tail clearance: WL at FS 28500 (15° attitude)

**Conditions:**
- Static MTOW: Reference condition
- Empty weight: Documented
- CG variations: Measured

## Flight Test Measurement

**Flight Test Instrumentation:**
- Nose boom: FS 0 (pressure measurements)
- Tufts: Surface flow visualization (multiple stations)
- Strain gauges: Structural verification (key stations)

**Post-Flight:**
- Dimensional check: Key points
- Deformation check: If anomaly detected
- Documentation: Test report

## Digital Twin Verification

**CAD Model Validation:**
- Physical measurements: Compared to CAD
- Tolerance verification: Accept/reject criteria
- Model update: If deviations significant
- Traceability: Version control

**As-Built Data:**
- Measurement data: Imported to digital twin
- Deviation tracking: Documented
- Configuration: Actual aircraft state
- Maintenance planning: Uses as-built data

## Certification Measurements

**Type Certification:**
- Conformity inspection: Key points measured
- Regulatory witness: Present for critical measurements
- Documentation: Part of type certificate data
- Traceability: Full chain of custody

**Status:** Measurement plan approved  
**Baseline:** Frozen  
**Approved:** 2024-02-08
