# RQ-02-11-40-006: Measurement Standards

**Priority:** Critical  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

All aircraft dimensional measurements shall be performed using calibrated equipment and standardized procedures, ensuring accuracy, repeatability, and traceability per international metrology standards.

## Measurement Requirements

**Accuracy Standards:**
- Primary dimensions: ±5mm (wingspan, length, height)
- Secondary dimensions: ±10mm (component locations)
- Critical dimensions: ±1mm (control surface positions)
- Manufacturing tolerances: Per specification

**Measurement Methods:**
- Laser scanning: ±2mm accuracy
- Photogrammetry: ±1mm accuracy for primary structure
- Coordinate Measuring Machine (CMM): ±0.1mm
- Tape measure: ±10mm (preliminary only)

## Environmental Conditions

**Standard Conditions:**
- Temperature: 15°C ±5°C (59°F ±9°F)
- Pressure: Standard atmospheric (1013.25 hPa)
- Humidity: 30-70% RH
- Lighting: Adequate for measurement method

**Corrections:**
- Thermal expansion coefficients applied
- Temperature compensation documented
- Non-standard conditions recorded
- Adjustments clearly stated

## Equipment Requirements

**Calibration:**
- All measurement equipment calibrated
- Calibration certificates current
- Traceability to national standards
- Calibration interval: Per manufacturer or annually

**Approved Equipment:**
- Laser trackers: Leica, FARO, or equivalent
- Photogrammetry: GOM, ATOS, or equivalent
- CMM: Zeiss, Hexagon, or equivalent
- Optical systems: Per specification

## Measurement Procedures

**Dimensional Inspection:**
1. Verify equipment calibration current
2. Establish environmental conditions acceptable
3. Identify reference datum points
4. Perform measurement per procedure
5. Record raw data and conditions
6. Apply corrections as necessary
7. Document results with uncertainty
8. Compare to specification requirements

**Repeatability:**
- Multiple measurements required for critical dimensions
- Statistical analysis of measurement variation
- Measurement uncertainty calculated
- Acceptance criteria: 95% confidence interval

## Documentation Requirements

**Measurement Reports:**
- Equipment used (model, serial, calibration date)
- Environmental conditions during measurement
- Raw measurement data recorded
- Corrections applied (with justification)
- Final values with uncertainty
- Comparison to specification
- Inspector signature and date

**Traceability:**
- Measurement linked to drawing/specification
- As-built vs. design comparison
- Non-conformances documented
- Corrective actions tracked

## Verification Method

**Quality Assurance:**
- Independent verification of critical dimensions
- Cross-check with multiple methods
- Audit of measurement procedures
- Calibration system audit

**Acceptance Criteria:**
- All measurements within specification
- Measurement uncertainty acceptable
- Documentation complete
- Traceability established

## Digital Model Integration

**As-Built Model:**
- Measurement data imported to digital twin
- CAD model updated with actual dimensions
- Deviation analysis performed
- Historical record maintained

**Configuration Control:**
- As-built configuration documented
- Changes from design captured
- Approved deviations recorded
- Configuration baseline established

## Compliance

**Standards:**
- [ISO 1101](https://www.iso.org/standard/66777.html) (Geometric tolerancing)
- [ISO 17025](https://www.iso.org/standard/66912.html) (Calibration laboratories)
- [ATA iSpec 2200](https://www.ataebooks.org/product-category/ispec-2200/) (Documentation)
- [ASME Y14.5](https://www.asme.org/codes-standards/find-codes-standards/y14-5-dimensioning-tolerancing) (Dimensioning and tolerancing)
- [VDI/VDE 2617](https://www.vdi.de/en/home/vdi-standards/details/vdivde-2617-blatt-4-accuracy-of-coordinate-measuring-machines-characteristics-and-their-testing-application-of-coordinate-measuring-machines-for-measuring-workpieces) (Accuracy of CMMs)

**Related Requirements:**
- [RQ-02-11-40-001](RQ-02-11-40-001_Body_Axis_System.md) through [RQ-02-11-40-005](RQ-02-11-40-005_Datum_Point_Definition.md) (Reference systems)
- [RQ-02-11-60-001](../RQ-TOLERANCES/RQ-02-11-60-001_Manufacturing_Tolerances.md) (Manufacturing Tolerances)
- [RQ-02-11-60-005](../RQ-TOLERANCES/RQ-02-11-60-005_Measurement_Accuracy.md) (Measurement Accuracy)
- All dimensional requirements
