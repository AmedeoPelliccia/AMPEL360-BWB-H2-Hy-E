# RQ-02-11-60-005: Measurement Accuracy

**Priority:** Critical  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

All dimensional measurements shall achieve specified accuracy levels using calibrated equipment and standardized procedures, with measurement uncertainty quantified and documented to ensure compliance with design specifications and regulatory requirements.

## Measurement Accuracy Requirements

**Primary Dimensions:**
- Wingspan, length, height: ±5mm accuracy
- Measurement uncertainty: ±2mm (95% confidence)
- Repeatability: ±1mm
- Equipment: Laser tracker or photogrammetry

**Secondary Dimensions:**
- Component locations: ±10mm accuracy
- Measurement uncertainty: ±5mm
- Repeatability: ±3mm
- Equipment: Laser scanner or CMM

**Critical Dimensions:**
- Control surface positions: ±1mm accuracy
- Measurement uncertainty: ±0.5mm
- Repeatability: ±0.2mm
- Equipment: CMM or precision optical

## Measurement Methods

**Laser Tracking:**
- Accuracy: ±0.010mm + 5µm/m (typical)
- Range: Up to 80m
- Applications: Large assembly, primary dimensions
- Requires optical targets on structure

**Photogrammetry:**
- Accuracy: ±0.1mm (close range) to ±1mm (full aircraft)
- Non-contact measurement
- Applications: Complex surfaces, large areas
- Requires coded/uncoded targets

**Coordinate Measuring Machine (CMM):**
- Accuracy: ±0.002mm to ±0.010mm (depending on size)
- Range: Limited to CMM table size
- Applications: Components, critical features
- Contact or optical probe

**Laser Scanning:**
- Accuracy: ±0.5mm to ±2mm (typical)
- Non-contact, high speed
- Applications: Surface verification, as-built
- Produces point cloud data

## Measurement Uncertainty

**Sources of Uncertainty:**
- Equipment calibration: ±0.001mm to ±1mm
- Environmental conditions: ±0.5mm to ±5mm
- Operator technique: ±0.1mm to ±1mm
- Datum establishment: ±1mm to ±5mm
- Data processing: ±0.1mm to ±0.5mm

**Uncertainty Budget:**
- Combined standard uncertainty calculated
- Expanded uncertainty (k=2, 95% confidence)
- Documented in measurement report
- Compared to tolerance requirements

## Environmental Control

**Standard Conditions:**
- Temperature: 20°C ±2°C (68°F ±4°F)
- Humidity: 40-60% RH
- Atmospheric pressure: 1013 ±10 hPa
- Vibration: Minimal (measurement lab)

**Temperature Compensation:**
- Material CTE applied to measurements
- Reference temperature: 20°C
- Thermal expansion calculated
- Correction documented

**Field Conditions:**
- Temperature: Recorded and compensated
- Expanded uncertainty for non-standard conditions
- Limits on acceptable conditions
- Correction factors validated

## Calibration Requirements

**Equipment Calibration:**
- Frequency: Annually or per manufacturer
- Traceability: National metrology institute (NIST, PTB, etc.)
- Calibration certificate current
- Calibration stickers on equipment

**Reference Standards:**
- Calibrated artifacts used
- Traceability chain documented
- Storage in controlled environment
- Periodic verification

**Calibration Records:**
- Equipment ID and serial number
- Calibration date and due date
- Calibration laboratory
- Certificate filed and accessible

## Verification Method

**Measurement System Analysis (MSA):**
- Gage Repeatability and Reproducibility (GR&R)
- %GR&R < 10% (acceptable)
- %GR&R 10-30% (marginal, acceptable with controls)
- %GR&R > 30% (unacceptable)

**Measurement Validation:**
- Independent measurements
- Cross-check with multiple methods
- Known standards measured
- Statistical analysis of results

**Acceptance Criteria:**
- Equipment within calibration
- MSA results acceptable
- Environmental conditions within limits
- Operator qualified

## Documentation Requirements

**Measurement Reports:**
- Date, time, location
- Equipment used (ID, calibration date)
- Environmental conditions
- Measurement results (raw and corrected)
- Uncertainty statement
- Comparison to specification
- Inspector name and signature

**Traceability:**
- Measurement plan reference
- Drawing/specification number
- Measurement procedure used
- Non-conformance linked (if applicable)

## Quality Assurance

**Audits:**
- Measurement process audits
- Calibration system audits
- Equipment verification checks
- Corrective action tracking

**Training:**
- Operator qualification
- Equipment-specific training
- Procedure training
- Refresher training annual

## Digital Twin Integration

**As-Built Data:**
- Measurement data imported
- Digital model updated
- Deviation analysis
- Historical record

**Configuration Management:**
- Version control
- Change tracking
- Baseline establishment
- Variance reporting

## Compliance

**Standards:**
- ISO 17025 (Testing and calibration laboratories)
- ISO 1101 (Geometrical tolerancing)
- ISO 10360 (CMM acceptance tests)
- VDI/VDE 2617 (Accuracy of CMMs)
- ASME B89 (Dimensional metrology)

**Related Requirements:**
- RQ-02-11-40-006 (Measurement Standards)
- RQ-02-11-60-001 (Manufacturing Tolerances)
- RQ-02-11-60-002 (Assembly Tolerances)
- All dimensional requirements
