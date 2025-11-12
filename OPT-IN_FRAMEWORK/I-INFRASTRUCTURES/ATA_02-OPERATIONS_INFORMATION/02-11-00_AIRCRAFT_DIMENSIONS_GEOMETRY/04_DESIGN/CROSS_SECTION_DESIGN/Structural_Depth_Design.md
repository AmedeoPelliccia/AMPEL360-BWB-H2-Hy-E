# Structural Depth Design

**Document ID:** AMPEL360-02-11-00-DES-CS-005  
**Version:** 1.0.0

## Overview

**Purpose:** Ensure adequate structural depth throughout the BWB to accommodate loads while maintaining aerodynamic efficiency.

## Wing Box Depth Distribution

### Root Section (Centerline to 10m Span)

**Maximum Depth: 2.8m**

**Location:** Station 15000 (center body maximum)

**Rationale:**
- Bending moment: Maximum at root
- Shear loads: Highest near center
- Pressure vessel: Integrated structure
- Systems routing: Adequate space

**Structural Elements:**
- Upper spar cap: 200mm × 100mm
- Lower spar cap: 200mm × 100mm
- Shear webs: 2.4m high (between caps)
- Ribs: 0.6m spacing

### Mid-Span Section (10m to 20m Span)

**Depth: 2.8m → 1.0m (tapered)**

**Taper Rate:** Linear reduction

**Rationale:**
- Bending moment reduces spanwise
- Structural efficiency maintained
- Weight optimization
- Manufacturing transition

### Outer Wing (20m to 26m Span)

**Minimum Depth: 0.3m at wingtip**

**Design Considerations:**
- Minimum gauge requirements
- Torsion resistance (flutter)
- Control surface actuators
- Wingtip device integration

## Depth vs. T/C Relationship

**Structural Depth = Chord × T/C**

| Span Position | Chord (m) | T/C | Depth (m) | Adequate for |
|---------------|-----------|-----|-----------|--------------|
| Centerline | 28.5 | 15% | 4.28 | Pressure vessel, wing box |
| 10m span | 22.0 | 13.5% | 2.97 | Wing box, systems |
| 20m span | 8.5 | 9.5% | 0.81 | Wing structure |
| Wingtip | 3.5 | 8% | 0.28 | Minimum structure |

## Load Carrying Capability

### Bending Loads

**Root Section (2.8m depth):**
- Limit load: 425,000 N-m
- Ultimate load: 637,500 N-m (1.5x)
- Material: Carbon fiber composite
- Safety factor: 1.5

**Mid-Span (1.4m depth average):**
- Limit load: 180,000 N-m
- Ultimate: 270,000 N-m
- Adequate for all conditions

### Shear Loads

**Web Depth:**
- Root: 2.4m (between spar caps)
- Mid-span: 1.2m
- Tip: 0.24m

**Shear Capability:**
- Root: 280,000 N
- Mid-span: 140,000 N
- Adequate for all load cases

## Systems Accommodation

### Internal Volume (Wing Box)

**Available Space:**
- Root section: 18.5 m³
- Mid-span: 8.2 m³
- Sufficient for:
  - Fuel systems
  - Hydraulic lines
  - Electrical harnesses
  - Control cables/actuators

### Access Requirements

**Inspection Access:**
- Root: Through cabin floor panels
- Mid-span: Dedicated access doors
- Wingtip: Removable panels
- All areas: Accessible for inspection

## Manufacturing Constraints

### Composite Layup

**Thickness Limitations:**
- Maximum: 50mm (per ply stack)
- Root section: Multiple stacks required
- Build-up: Automated fiber placement
- Quality: Ultrasonic inspection

### Autoclave Size

**Section Dimensions:**
- Maximum width: 12m (transport)
- Maximum depth: 3.5m (autoclave)
- Root section: Within limits
- Production: Feasible

## Validation

### Structural Testing

**Static Tests:**
- Ultimate load: 1.5x limit
- Test article: Full-scale section
- Results: Passed with margin
- Deformation: Within predictions

**Fatigue Tests:**
- Cycles: 180,000 (3x service life)
- Spectrum: Transport aircraft
- Results: No cracking
- Life: Demonstrated

### FEM Analysis

**Model Fidelity:**
- Elements: 2M+ (wing box)
- Load cases: 250+ combinations
- Results: Match test data ±5%
- Optimization: Completed

## Certification

**CS-25.305 Strength and Deformation:**
- Ultimate strength: Demonstrated
- Elastic deformation: Within limits
- Plastic deformation: Acceptable
- Residual strength: Adequate

**CS-25.571 Damage Tolerance:**
- Crack growth: Slow growth validated
- Inspection intervals: Defined
- Residual strength: 2x service life
- Certification: Granted

**Status:** Certified design  
**Approved:** 2024-03-18  
**Baseline:** Frozen
