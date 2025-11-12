# RQ-02-11-60-001: Manufacturing Tolerances

**Priority:** Critical  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

Manufacturing tolerances for aircraft structural components shall be maintained within specified limits to ensure aerodynamic performance, structural integrity, and assembly fit-up, with critical dimensions held to ±0.1 meter or tighter as specified.

## Tolerance Classification

**Critical Dimensions (±0.05m or ±50mm):**
- Control surface hinge lines
- Landing gear attachment points
- Wing-body junction contours
- Pressurization boundary locations
- Engine mount interfaces

**Primary Dimensions (±0.1m or ±100mm):**
- Overall wingspan
- Overall length
- Center body width
- Major structural interfaces
- Door frame locations

**Secondary Dimensions (±0.2m or ±200mm):**
- Equipment bay dimensions
- Non-structural fairings
- Interior panel locations
- Service access panels

**Form Tolerances:**
- Surface profile: ±5mm for Class A surfaces
- Surface waviness: 0.5mm over 300mm
- Edge straightness: ±2mm per meter

## Rationale

**Aerodynamic Performance:**
- Maintains designed flow characteristics
- Preserves laminar flow regions
- Controls drag penalties
- Ensures performance targets achieved

**Structural Integrity:**
- Load path alignment critical
- Joint fit-up requirements
- Fastener hole alignment
- Stress concentration control

**Assembly Requirements:**
- Component interchangeability
- Reduced shimming requirements
- Assembly time optimization
- Quality control simplification

## Verification Method

**In-Process Inspection:**
- CMM (Coordinate Measuring Machine) inspection
- Laser scanning of major components
- Photogrammetry for large assemblies
- Statistical process control (SPC)

**Final Inspection:**
- 100% inspection of critical dimensions
- Sample inspection of primary dimensions
- Visual inspection of secondary dimensions
- As-built documentation

**Acceptance Criteria:**
- All dimensions within specified tolerances
- Critical features: Zero defects
- Primary features: Cpk ≥ 1.67
- Secondary features: Cpk ≥ 1.33

## Manufacturing Process Control

**Tooling Requirements:**
- Tool accuracy: 50% of part tolerance
- Tool calibration: Monthly or per schedule
- Tool wear monitoring
- Temperature compensation

**Process Monitoring:**
- In-process measurements
- SPC charts for critical dimensions
- Trend analysis and corrective action
- Capability studies (Cp, Cpk)

## Material Considerations

**Composite Materials:**
- Cure cycle control critical
- Thermal expansion during cure
- Resin shrinkage allowance
- Fiber orientation tolerance: ±5°

**Metallic Materials:**
- Machining tolerances: ISO 2768-m
- Heat treatment effects
- Surface finish requirements
- Hardness uniformity

## Non-Conformance Handling

**Disposition Options:**
- Use as-is: Engineering analysis required
- Rework: Within process capability
- Repair: Approved repair procedures
- Scrap: Outside repair limits

**Documentation:**
- Non-conformance report (NCR)
- Engineering disposition
- Corrective action
- Rework/repair records

## Compliance

**Standards:**
- [ISO 2768](https://www.iso.org/standard/79442.html) (General tolerances)
- [ASME Y14.5](https://www.asme.org/codes-standards/find-codes-standards/y14-5-dimensioning-tolerancing) (GD&T)
- [AS9100](https://www.sae.org/standards/content/as9100d/) (Quality management - aerospace)
- [ATA iSpec 2200](https://www.ataebooks.org/product-category/ispec-2200/) (Tolerancing practices)
- Composite-specific: Industry standards

**Related Requirements:**
- [RQ-02-11-10-006](../RQ-DIMENSIONS/RQ-02-11-10-006_Dimensional_Tolerances.md) (Dimensional Tolerances)
- [RQ-02-11-60-002](RQ-02-11-60-002_Assembly_Tolerances.md) (Assembly Tolerances)
- [RQ-02-11-60-005](RQ-02-11-60-005_Measurement_Accuracy.md) (Measurement Accuracy)
- All dimensional requirements
