# RQ-02-11-40-002: Station System Definition

**Priority:** Critical  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

The aircraft station system (X-axis) shall be defined as longitudinal measurements in meters from the nose apex (Station 0), with positive values increasing aft (toward the tail), following the aircraft centerline.

## Rationale

**Standardization:**
- Consistent reference for all measurements
- Compatibility with ATA 100 standards
- Enables precise component location
- Facilitates maintenance documentation

**BWB Application:**
- Station 0 at nose apex (forward-most structural point)
- Follows centerline of pressurized center body
- Transitions to aerodynamic centerline in wing sections
- Station 38.2 at aft extremity (tail)

**Operational Use:**
- Weight and balance calculations
- Component location identification
- Maintenance access points
- CG determination (reference to MAC)

## Station System Definition

**Key Stations:**

| Station | Location | Significance |
|---------|----------|--------------|
| STA 0 | Nose apex | Datum point |
| STA 5 | Cockpit forward | Flight deck forward bulkhead |
| STA 10 | Cockpit aft | Flight deck aft bulkhead |
| STA 15 | Center body | Maximum width point |
| STA 20 | Forward tank | H₂ tank center (forward) |
| STA 25 | Wing box | Main spar carrythrough |
| STA 30 | Aft tank | H₂ tank center (aft) |
| STA 35 | Aft bulkhead | Pressurization boundary |
| STA 38.2 | Tail | Aft-most structural point |

## Verification Method

**Documentation Review:**
- Design drawings verification
- Station callouts on all drawings
- Consistency check across all ATA chapters
- Digital model validation

**Physical Verification:**
- Laser measurement from datum (nose apex)
- Key station markers on aircraft structure
- As-built verification at assembly
- Photogrammetry validation

**Acceptance Criteria:**
- Station markings accurate to ±10mm
- Consistent throughout documentation
- Physically marked on aircraft structure
- Digital twin synchronized

## Usage Requirements

**All Documentation Shall:**
- Reference station system for longitudinal position
- Use "STA XX.X" format (meters)
- Maintain consistency with datum
- Specify tolerance when critical

**Component Location:**
- Primary reference: Station (X)
- Secondary: Buttline (Y) and Waterline (Z)
- Format: STA 15.0, BL +8.5, WL 4.0

## Compliance

**Standards:**
- [ATA 100](https://www.ata.org/resources/specifications) (Coordinate systems)
- [ATA iSpec 2200](https://www.ataebooks.org/product-category/ispec-2200/) (Documentation)
- [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Reference systems)

**Related Requirements:**
- [RQ-02-11-40-001](RQ-02-11-40-001_Body_Axis_System.md) (Body Axis System)
- [RQ-02-11-40-003](RQ-02-11-40-003_Waterline_System_Definition.md) (Waterline System)
- [RQ-02-11-40-004](RQ-02-11-40-004_Buttline_System_Definition.md) (Buttline System)
- [RQ-02-11-40-005](RQ-02-11-40-005_Datum_Point_Definition.md) (Datum Point)
