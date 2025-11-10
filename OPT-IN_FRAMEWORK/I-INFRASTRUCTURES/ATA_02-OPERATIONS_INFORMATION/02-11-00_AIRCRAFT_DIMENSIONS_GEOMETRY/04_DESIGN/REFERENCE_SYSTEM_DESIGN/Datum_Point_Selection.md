# Datum Point Selection

**Document ID:** AMPEL360-02-11-00-DES-RS-002  
**Version:** 1.0.0

## Datum Point Definition

**Location:** FS 15000, BL 0, WL 5000

**Coordinates:**
- Fuselage Station: 15.000 m (from nose apex)
- Butt Line: 0.000 m (centerline)
- Water Line: 5.000 m (from ground reference at MTOW)

## Selection Rationale

### Geometric Considerations

**Central Location:**
- Longitudinal: 15m (center of 28.5m length)
- Lateral: 0m (aircraft centerline)
- Vertical: 5m (cabin floor level)

**Benefits:**
- Convenient for measurements
- Minimizes coordinate magnitudes
- Intuitive for engineers
- Central to aircraft volume

### Center of Gravity Proximity

**CG Range:**
- Forward limit: FS 14200 (94.7% of datum)
- Aft limit: FS 15800 (105.3% of datum)
- Datum location: Near CG centroid

**Benefits:**
- Weight and balance calculations simplified
- Moment arms minimized
- CG tracking intuitive
- Fuel management optimization

### Manufacturing Reference

**Tooling Datum:**
- Assembly fixtures: Referenced to datum
- Measurement systems: Datum-based
- Quality control: Datum verification
- Traceability: Full documentation

**Digital Twin:**
- CAD model origin: Datum point
- FEM model origin: Datum point
- Simulation reference: Consistent
- Data integration: Simplified

## Reference Planes

### Fuselage Station (FS) Zero Plane

**Definition:** Vertical plane through nose apex, perpendicular to X-axis

**Location:** Aircraft nose (most forward point)

**Measurements:**
- Forward of datum: Negative FS
- Aft of datum: Positive FS
- Datum: FS 15000

### Butt Line (BL) Zero Plane

**Definition:** Vertical plane through aircraft centerline, perpendicular to Y-axis

**Symmetry Plane:** Aircraft symmetric about BL 0

**Measurements:**
- Left of centerline: Negative BL
- Right of centerline: Positive BL
- Centerline: BL 0

### Water Line (WL) Zero Plane

**Definition:** Horizontal plane at ground level (MTOW static)

**Reference:** Ground contact at MTOW

**Measurements:**
- Below reference: Negative WL
- Above reference: Positive WL
- Ground: WL 0 (MTOW)

## Usage in Documentation

### Drawing References

**Title Blocks:**
- Datum identified: FS 15000, BL 0, WL 5000
- Coordinate system: ATA 100 standard
- Units: Millimeters
- Projection: Standard orthographic

**Dimension Call-outs:**
- Station format: FS 12345
- Butt line format: BL ±1234
- Water line format: WL 1234
- Consistency: All drawings

### Part Identification

**Location Codes:**
- Forward of datum: F
- Aft of datum: A
- Left of centerline: L
- Right of centerline: R
- Above datum: U
- Below datum: D

**Example:** Part P-F3-L2-U1
- Forward 3m (FS 12000)
- Left 2m (BL -2000)
- Up 1m (WL 6000)

## Digital Twin Integration

### CAD Model

**Origin Point:** Datum (FS 15000, BL 0, WL 5000)

**Axis Orientation:**
- X-axis: Aft (positive)
- Y-axis: Right (positive)
- Z-axis: Down (positive)

**Model Structure:**
- Assembly: Datum-referenced
- Components: Local origins defined
- Traceability: Part number + location

### FEM Model

**Mesh Origin:** Datum point

**Node Numbering:**
- Convention: Coordinate-based
- Datum nodes: 1500000 series
- Forward: 1000000-1499999
- Aft: 1500001-2850000

### Configuration Management

**Baseline Control:**
- Datum: Frozen (unchangeable)
- Coordinates: Traceable to datum
- Changes: Impact analysis required
- Documentation: Full revision control

## Measurement Procedures

### Physical Measurements

**Tools:**
- Laser trackers: Referenced to datum
- Coordinate measuring machine (CMM): Datum setup
- Optical systems: Datum calibration
- Traditional: Tape measures, levels

**Accuracy:**
- Primary structure: ±1.0mm
- Secondary structure: ±2.0mm
- Non-critical: ±5.0mm

### Inspection

**Acceptance Criteria:**
- Critical features: ±0.5mm
- Important features: ±1.0mm
- Standard features: ±2.0mm
- Non-critical: ±5.0mm

**Documentation:**
- Measurement reports: Datum-referenced
- Deviation records: Coordinate-based
- As-built data: Digital format
- Archive: Permanent record

## Certification Documentation

**Type Certificate Data:**
- Datum point: Specified
- Coordinate system: Defined
- Reference planes: Documented
- Traceability: Required

**Approved:** 2024-02-01  
**Status:** Baseline frozen
