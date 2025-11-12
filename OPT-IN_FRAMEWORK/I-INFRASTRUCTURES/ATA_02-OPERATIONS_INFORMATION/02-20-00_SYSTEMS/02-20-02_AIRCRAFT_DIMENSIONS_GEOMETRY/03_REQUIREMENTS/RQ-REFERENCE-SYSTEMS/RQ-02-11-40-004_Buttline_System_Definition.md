# RQ-02-11-40-004: Buttline System Definition

**Priority:** Critical  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

The aircraft buttline system (Y-axis) shall be defined as lateral measurements in meters from the aircraft centerline (Buttline 0), positive toward the right side, negative toward the left side.

## Rationale

**Lateral Reference:**
- Component lateral positioning
- Symmetry verification
- Left/right identification
- Load distribution analysis

**Centerline Reference:**
- BL 0 at aircraft centerline (vertical plane through nose and tail)
- Positive values: Right side (+)
- Negative values: Left side (-)
- Symmetric about centerline for most components

**Operational Use:**
- Weight and balance calculations
- Equipment installation location
- Door identification (L/R)
- Structural load paths

## Buttline System Definition

**Key Buttlines:**

| Buttline | Location | Significance |
|----------|----------|--------------|
| BL 0 | Centerline | Reference datum |
| BL ±2.5 | Cockpit sides | Flight deck width |
| BL ±10.0 | Cabin sides (typical) | Passenger cabin width varies |
| BL ±19.0 | Center body edge | Body-to-wing transition |
| BL ±22.5 | Mid semi-span | Mid-wing location |
| BL ±26.0 | Wingtip | Wing extremity |

## Symmetry Requirements

**Symmetric Components:**
- Most structural components: ±0.1mm symmetry
- Wing structure: ±50mm left-right
- Control surfaces: ±20mm position
- Landing gear: ±100mm track

**Asymmetric Components:**
- Documented exceptions
- Reason for asymmetry stated
- Impact on operations analyzed
- Approved by design authority

## Verification Method

**Measurement:**
- Centerline established from nose/tail alignment
- Laser measurement system
- Left-right symmetry verification
- Photogrammetry validation

**Documentation:**
- All drawings show buttlines
- Left/right clearly indicated
- Sign convention consistent (+/-)
- Digital model correlation

**Acceptance Criteria:**
- Buttline markings accurate to ±10mm
- Centerline defined and marked
- Symmetry requirements met
- Documentation complete

## Usage Requirements

**All Documentation Shall:**
- Reference buttline system for lateral position
- Use "BL ±X.X" format (meters)
- Positive for right, negative for left
- Specify tolerance when critical

**Component Identification:**
- Use "L" or "BL -X" for left side
- Use "R" or "BL +X" for right side
- Format examples:
  - Door L1: BL -15.0
  - Door R1: BL +15.0
  - Centerline equipment: BL 0

## Special Considerations

**BWB Configuration:**
- Very wide center body (38m)
- Buttlines extend to ±19m at center body
- Buttlines to ±26m at wingtip
- Clear differentiation of body vs. wing BL

**Cabin Layout:**
- Cabin width varies with station
- Buttline reference for seat rows
- Aisle centerline typically BL 0
- Emergency exits at specific BL locations

## Compliance

**Standards:**
- [ATA 100](https://www.ata.org/resources/specifications) (Coordinate systems)
- [ATA iSpec 2200](https://www.ataebooks.org/product-category/ispec-2200/)
- [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Reference systems)
- [ISO 1151](https://www.iso.org/standard/5763.html) (Axis conventions)

**Related Requirements:**
- [RQ-02-11-40-001](RQ-02-11-40-001_Body_Axis_System.md) (Body Axis System)
- [RQ-02-11-40-002](RQ-02-11-40-002_Station_System_Definition.md) (Station System)
- [RQ-02-11-40-003](RQ-02-11-40-003_Waterline_System_Definition.md) (Waterline System)
- [RQ-02-11-20-001](../RQ-BWB-GEOMETRY/RQ-02-11-20-001_Center_Body_Width_38m.md) (Center Body Width)
