# RQ-02-11-40-003: Waterline System Definition

**Priority:** Critical  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

The aircraft waterline system (Z-axis) shall be defined as vertical measurements in meters from the ground reference line (Waterline 0), positive upward direction, perpendicular to the XY plane.

## Rationale

**Vertical Reference:**
- Consistent height measurements
- Component vertical location
- Ground clearance determination
- Structural level references

**Ground Reference:**
- WL 0 at ground level (landing gear extended, level attitude)
- Facilitates ground clearance calculations
- Simplifies maintenance access planning
- Compatible with hangar/gate planning

**Operational Use:**
- Center of gravity height
- Equipment installation height
- Door threshold heights
- Service access points

## Waterline System Definition

**Key Waterlines:**

| Waterline | Location | Significance |
|-----------|----------|--------------|
| WL 0 | Ground level | Reference datum (gear extended) |
| WL 2.0 | Belly structure | Lowest center body point |
| WL 4.5 | Cabin floor | Passenger cabin main floor |
| WL 6.0 | Cabin ceiling | Passenger cabin ceiling |
| WL 7.5 | Upper deck | H₂ tank deck floor |
| WL 10.0 | Upper structure | H₂ tank top |
| WL 11.5 | Wing root | Wing-body intersection |
| WL 14.5 | Highest point | Top of vertical stabilizer |

## Verification Method

**Measurement:**
- Level aircraft on calibrated platform
- Laser measurement system
- Multiple reference points verified
- Photogrammetry validation

**Documentation:**
- All drawings show waterlines
- Consistent reference throughout
- Digital model correlation
- As-built documentation

**Acceptance Criteria:**
- Waterline markings accurate to ±10mm
- Consistent with ground reference
- Physically marked on structure
- Documentation complete

## Usage Requirements

**All Documentation Shall:**
- Reference waterline system for vertical position
- Use "WL X.X" format (meters)
- Maintain consistency with ground reference
- Specify tolerance when critical

**Height Measurements:**
- Ground clearances referenced to WL 0
- Component heights measured from WL 0
- Internal spaces referenced to cabin floor WL
- Format: WL 4.5 (4.5m above ground)

## Special Considerations

**Landing Gear States:**
- WL 0 with gear extended (level attitude)
- Different WL 0 with gear retracted
- Document both conditions when applicable
- Use "gear extended" as default

**BWB Configuration:**
- Wide variation in waterlines across span
- Center body vs. wing waterlines differ
- Reference to local vs. global WL
- Clarify reference in documentation

## Compliance

**Standards:**
- [ATA 100](https://www.ata.org/resources/specifications) (Coordinate systems)
- [ATA iSpec 2200](https://www.ataebooks.org/product-category/ispec-2200/)
- [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Reference systems)

**Related Requirements:**
- [RQ-02-11-40-001](RQ-02-11-40-001_Body_Axis_System.md) (Body Axis System)
- [RQ-02-11-40-002](RQ-02-11-40-002_Station_System_Definition.md) (Station System)
- [RQ-02-11-40-004](RQ-02-11-40-004_Buttline_System_Definition.md) (Buttline System)
- [RQ-02-11-10-003](../RQ-DIMENSIONS/RQ-02-11-10-003_Overall_Height_14.5m.md) (Overall Height)
