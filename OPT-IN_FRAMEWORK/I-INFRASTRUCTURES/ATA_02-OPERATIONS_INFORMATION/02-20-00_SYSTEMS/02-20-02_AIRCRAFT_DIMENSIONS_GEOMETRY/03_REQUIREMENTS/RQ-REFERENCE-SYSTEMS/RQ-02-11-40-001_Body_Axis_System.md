# RQ-02-11-40-001: Body Axis System

**Priority:** Critical  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

The aircraft shall use a right-hand orthogonal body axis system with origin at the nose apex (Station 0, Buttline 0, Waterline 0), following ATA 100 conventions and aerospace industry standards.

## Axis Definitions

**X-Axis (Longitudinal):**
- Direction: Aft (positive toward tail)
- Origin: Nose apex
- Reference: Aircraft centerline
- Units: Meters

**Y-Axis (Lateral):**
- Direction: Right (positive toward right wing)
- Origin: Aircraft centerline
- Reference: Perpendicular to XZ plane
- Units: Meters

**Z-Axis (Vertical):**
- Direction: Up (positive upward)
- Origin: Ground reference line
- Reference: Perpendicular to XY plane
- Units: Meters

## Right-Hand Rule

**Coordinate System:**
- X × Y = Z (right-hand rule)
- All rotations follow right-hand convention
- Positive angles: Counter-clockwise when viewed from positive axis
- Standard aerospace convention

**Angular Measurements:**
- Roll (φ): Rotation about X-axis
- Pitch (θ): Rotation about Y-axis
- Yaw (ψ): Rotation about Z-axis

## Rationale

**Standardization:**
- ATA 100 compliance
- Aerospace industry standard
- CAD/CAE software compatibility
- Documentation consistency

**BWB Application:**
- Origin at nose apex (forward-most point)
- Centerline through geometric center
- Vertical reference from ground line
- Integration with conventional systems

## Verification Method

**Documentation Review:**
- All drawings checked for compliance
- CAD models verified
- Digital twin validation
- Software interface confirmation

**Acceptance Criteria:**
- Right-hand system verified
- Origin at specified location
- All documentation consistent
- Software tools compatible

## Usage Requirements

**All Technical Documentation:**
- Use defined coordinate system
- Specify reference frame clearly
- Include orientation diagrams
- Maintain consistency throughout

**Component Location Format:**
- X: Station (STA)
- Y: Buttline (BL)
- Z: Waterline (WL)
- Example: STA 15.0, BL +8.5, WL 4.0

## Compliance

**Standards:**
- [ATA 100](https://www.ata.org/resources/specifications) (Coordinate Systems)
- [ATA iSpec 2200](https://www.ataebooks.org/product-category/ispec-2200/)
- [ISO 1151](https://www.iso.org/standard/5763.html) (Flight Dynamics)
- [SAE AS8015](https://www.sae.org/standards/content/as8015c/) (Axis Systems)

**Related Requirements:**
- [RQ-02-11-40-002](RQ-02-11-40-002_Station_System_Definition.md) (Station System)
- [RQ-02-11-40-003](RQ-02-11-40-003_Waterline_System_Definition.md) (Waterline System)
- [RQ-02-11-40-004](RQ-02-11-40-004_Buttline_System_Definition.md) (Buttline System)
- [RQ-02-11-40-005](RQ-02-11-40-005_Datum_Point_Definition.md) (Datum Point)
