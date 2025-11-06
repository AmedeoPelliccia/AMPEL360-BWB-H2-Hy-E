# RQ-02-11-40-005: Datum Point Definition

**Priority:** Critical  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

The aircraft reference datum point shall be defined at the nose apex (STA 0, BL 0, WL reference), serving as the origin for all dimensional measurements and coordinate transformations.

## Datum Point Location

**Coordinates:**
- Station (X): 0.0m (nose apex - forward-most structural point)
- Buttline (Y): 0.0m (aircraft centerline)
- Waterline (Z): Reference based on ground line with gear extended

**Physical Location:**
- Forward-most structural point of nose
- On aircraft centerline (vertical plane of symmetry)
- Permanent reference mark on structure
- Accessible for measurement verification

## Rationale

**Measurement Reference:**
- Single point origin for all measurements
- Simplifies coordinate transformations
- Enables precise component location
- Standardizes documentation

**Manufacturing Use:**
- Assembly fixture reference
- Tooling alignment
- Quality control measurements
- As-built verification

**Operational Use:**
- Weight and balance calculations
- CG location determination
- Loading computations
- Moment arm calculations

## Physical Marking

**Datum Mark:**
- Permanent physical mark on structure
- Inscribed or stamped identification
- "DATUM" label clearly visible
- Protected from damage/wear

**Verification Points:**
- Multiple reference points for verification
- Optical targets for photogrammetry
- Laser tracker reference points
- Survey monuments established

## Verification Method

**Establishment:**
- Surveyed during initial assembly
- Photogrammetry system verification
- Multiple measurement confirmations
- Documented in assembly records

**Maintenance:**
- Periodic verification (annually)
- After major structural work
- Post-incident inspection
- Digital twin synchronization

**Acceptance Criteria:**
- Datum location verified to ±5mm
- Physical mark clearly visible
- Documentation complete
- Digital model synchronized

## Related Reference Points

**Secondary Datums:**
- Main landing gear datum: For loading calculations
- CG reference point: For weight and balance
- MAC reference point: For aerodynamic calculations
- Engine thrust line: For propulsion analysis

**Transformations:**
- All secondary datums referenced to primary datum
- Transformation matrices documented
- Software tools use consistent datum
- Clear documentation of any alternate datums

## Usage Requirements

**All Measurements:**
- Reference primary datum unless stated otherwise
- State reference datum in all documents
- Include coordinate system definition
- Specify measurement accuracy

**Documentation Format:**
- "Distance from datum (STA 0)"
- "Referenced to nose apex datum"
- Coordinate format: (X, Y, Z) from datum
- Example: Component at (15.0, +8.5, 4.0)

## Compliance

**Standards:**
- ATA 100 (Reference systems)
- ATA iSpec 2200
- ISO 1151 (Reference systems)
- Quality management standards

**Related Requirements:**
- RQ-02-11-40-001 (Body Axis System)
- RQ-02-11-40-002 (Station System)
- RQ-02-11-40-003 (Waterline System)
- RQ-02-11-40-004 (Buttline System)
- RQ-02-11-40-006 (Measurement Standards)
