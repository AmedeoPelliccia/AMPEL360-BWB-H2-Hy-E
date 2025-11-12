# Dimension Data Accuracy Verification 02-11-00

**Component Code:** 02-11-00  
**Folder:** 09_PRODUCTION_PLANNING/QUALITY_CONTROL  
**Document:** Dimension_Data_Accuracy_Verification_02-11-00.md

## Purpose

This document establishes procedures for verifying the accuracy and consistency of dimensional data files (CSVs, JSON, tables) generated during production for the AMPEL360 BWB H₂ Hy-E aircraft. It ensures data integrity from measurement through final delivery to customers and certification authorities.

## Overview

Dimensional data accuracy verification ensures that:
- Data files correctly represent as-built aircraft geometry
- Data is free from transcription errors, format issues, and inconsistencies
- Data meets requirements of downstream users (certification, flight operations, maintenance)
- Data is traceable to source measurements and approved design
- Data integrity is maintained throughout production lifecycle

This document implements verification requirements defined in `07_V_AND_V/VER-02-11-402_Dimensional_Tolerance_Analysis.md`.

## Data Verification Methods

### Method 1: Source Document Verification

**Applies to:** Data extracted from design documents (CAD models, drawings, specifications)

**Procedure:**
1. Compare data file entries to source document (e.g., `01_OVERVIEW/baseline_dimensions.json` to CAD model dimensions)
2. Verify correct interpretation of dimensions:
   - Units (metric vs. imperial) correctly identified
   - Datum references correctly applied (FS, WL, BL)
   - Dimension definition matches intent (e.g., overall length includes all protrusions)
3. Check for transcription errors:
   - Decimal point placement
   - Digit transposition (e.g., 48.5 m vs. 45.8 m)
   - Sign errors (positive vs. negative coordinates)
4. Verify data completeness:
   - All required dimensions present
   - No placeholder or "TBD" values in production data

**Acceptance Criteria:**
- 100% match between data file and source document
- No transcription errors
- All required fields populated with valid data

**Responsible Party:** Engineering data analyst, QA review

**Frequency:** 100% for design baseline data, sample verification (10%) for production data generation

### Method 2: Measurement Data Verification

**Applies to:** Data derived from physical measurements (CMM, laser tracker, photogrammetry)

**Procedure:**
1. Trace data file entry back to raw measurement file:
   - Identify measurement file (CMM report, laser tracker session, photogrammetry project)
   - Verify extraction of correct dimension from measurement data
   - Check processing steps (e.g., best-fit calculation, coordinate transformation)
2. Verify measurement validity:
   - Measurement equipment calibration current
   - Measurement method appropriate for feature
   - Measurement uncertainty acceptable (< 10% of tolerance)
   - Operator qualified for measurement type
3. Check data processing accuracy:
   - Calculation of derived dimensions correct (e.g., wingspan from two point measurements)
   - Statistical analysis correct (mean, standard deviation of multiple measurements)
   - Coordinate transformations correctly applied (e.g., from tracker coordinates to aircraft body axes)
4. Verify as-built vs. nominal comparison:
   - Deviation correctly calculated (as-built minus nominal)
   - Tolerance check correct (deviation within tolerance = PASS)
   - Engineering disposition correctly captured for out-of-tolerance dimensions

**Acceptance Criteria:**
- Traceability from data file to raw measurement established
- Measurement validity confirmed (equipment, method, operator qualified)
- Data processing calculations verified correct
- Deviations and tolerance checks accurate

**Responsible Party:** QA inspector, independent verification by second inspector for critical dimensions

**Frequency:** 100% for prototype (MSN-P001), 20% sampling for pre-production, 10% sampling for serial production

### Method 3: Calculation Verification

**Applies to:** Dimensions calculated from other dimensions (e.g., aspect ratio from span and area, MAC from chord distribution)

**Procedure:**
1. Verify calculation formula:
   - Formula matches design standard or industry practice
   - Example: Aspect ratio AR = b²/S (wingspan squared divided by wing area)
2. Independent recalculation:
   - Second analyst performs calculation using same input data
   - Results compared to data file value
   - Acceptable tolerance: ≤0.1% difference (due to rounding)
3. Unit consistency check:
   - All inputs in consistent units before calculation
   - Output unit correctly labeled
4. Rounding and precision check:
   - Precision appropriate for dimension type (e.g., aspect ratio to 0.1, lengths to 0.01 m)
   - Rounding performed per standard rules (round half up)

**Acceptance Criteria:**
- Formula verified correct
- Independent calculation matches data file (within ≤0.1%)
- Units consistent and correctly labeled
- Precision appropriate

**Responsible Party:** Engineering analyst, QA review

**Frequency:** 100% for design baseline calculations, 10% sampling for production data

### Method 4: Cross-Reference Verification

**Applies to:** Dimensions appearing in multiple documents or data files

**Procedure:**
1. Identify dimensions that appear in multiple locations:
   - Example: Overall wingspan in baseline_dimensions.json, TCDS, AFM, as_built_geometry_MSN-XXX.json
2. Compare values across documents:
   - Exact match for same measurement (or within stated measurement uncertainty)
   - Consistent use of significant figures and units
3. Investigate discrepancies:
   - Determine if discrepancy is due to different measurement method, condition, or actual error
   - Resolve discrepancy: update incorrect value or document reason for difference
4. Document cross-reference matrix:
   - Table showing dimension, locations where it appears, values, and verification status

**Acceptance Criteria:**
- All cross-referenced dimensions consistent across documents (or discrepancies explained)
- No conflicting data in customer-facing documents (AFM, TCDS, delivery package)

**Responsible Party:** Quality engineer, certification engineer

**Frequency:** 100% for critical dimensions (overall dimensions, ground clearances), 20% sampling for other dimensions

### Method 5: Statistical Analysis

**Applies to:** Production data across multiple aircraft (serial production phase)

**Procedure:**
1. Compile dimensional data from multiple aircraft:
   - Extract specific dimensions (e.g., overall length) from all as_built_geometry_MSN-XXX.json files
   - Create data set for statistical analysis
2. Calculate statistical parameters:
   - Mean, standard deviation, min, max, range
   - Process capability indices: Cp, Cpk (if tolerance specified)
3. Identify outliers:
   - Data points >3 standard deviations from mean
   - Investigate outliers: measurement error, actual dimensional issue, or natural variation?
4. Trend analysis:
   - Plot dimension over time (by MSN sequence)
   - Identify shifts, trends, or patterns (e.g., tool wear causing dimensional drift)
5. Compare production average to design intent:
   - Is mean dimension significantly different from nominal design?
   - If yes, investigate root cause and consider design update or process adjustment

**Acceptance Criteria:**
- Process capability Cpk ≥ 1.33 for critical dimensions (4σ process)
- No significant outliers without valid explanation
- Production mean within design tolerance

**Responsible Party:** Quality engineering, statistical process control (SPC) analyst

**Frequency:** Ongoing after ≥10 aircraft produced, updated monthly

## Data File Types and Verification Requirements

### CSV Files (e.g., Principal_Dimensions.csv, Geometry_Parameters.csv)

**Verification Checklist:**
- [ ] File format valid: comma-separated, one header row, consistent number of columns
- [ ] Header row descriptive: column names clear, units specified
- [ ] Data types consistent: numeric data in numeric columns, no text in number fields
- [ ] No missing data: all cells populated (or explicitly marked "N/A" if not applicable)
- [ ] Numeric precision consistent: same number of decimal places for same dimension type
- [ ] Units consistent: all dimensions in same units (or clearly labeled if mixed)
- [ ] MSN or component ID correctly specified
- [ ] Date and version information included (metadata or in filename)

**Verification Method:**
- Automated script checks file format, data types, completeness
- Sample manual review (10 rows) for content accuracy
- Cross-reference to source data (design or measurement)

**Acceptance Criteria:**
- All checklist items passed
- Automated checks pass without errors
- Sample manual review shows 100% accuracy

### JSON Files (e.g., baseline_dimensions.json, as_built_geometry_MSN-XXX.json)

**Verification Checklist:**
- [ ] JSON syntax valid: properly formed (validated with JSON parser)
- [ ] Schema compliance: structure matches defined schema (if schema exists)
- [ ] Required fields present: all mandatory fields populated
- [ ] Data types correct: numbers as numbers (not strings), booleans as true/false, etc.
- [ ] Nested structures correct: arrays and objects properly formed
- [ ] Numeric precision appropriate: floating-point precision sufficient for dimension accuracy
- [ ] Units specified: either in field name or in separate "unit" field
- [ ] MSN or aircraft ID correctly specified
- [ ] Metadata complete: date, version, author, measurement method references

**Verification Method:**
- JSON validator tool checks syntax and schema compliance
- Automated script extracts key dimensions and compares to source
- Manual review of complex nested structures

**Acceptance Criteria:**
- JSON validator passes
- Schema compliance 100%
- Key dimensions match source data

### Technical Drawings (PDF)

**Verification Checklist:**
- [ ] Drawing number and revision correct
- [ ] Dimensions match CAD model (source of truth)
- [ ] Title block complete: aircraft model, MSN (if as-built drawing), date, approval signatures
- [ ] Dimension callouts clear and unambiguous
- [ ] Tolerance blocks correctly specify general and specific tolerances
- [ ] Units clearly labeled (metric preferred, imperial in parentheses if required)
- [ ] Datum references correctly specified per GD&T standard (ASME Y14.5 or ISO 1101)
- [ ] Scale correct and noted (or "DO NOT SCALE" if PDF is not to-scale)

**Verification Method:**
- Engineering review: compare drawing to CAD model
- QA review: check title block, tolerances, units
- Dimensional spot check: measure sample of dimensions on CAD model, compare to drawing callouts

**Acceptance Criteria:**
- Drawing dimensions accurate to CAD model
- Title block complete and correct
- Tolerances and units clearly specified

## Data Consistency Checks

### Internal Consistency

**Check 1: Dimensional Relationships**
- Wing area = span × average chord (approximately, exact depends on planform shape)
- Aspect ratio = span²/ wing area
- Overall length ≥ fuselage length
- Overall height ≥ maximum vertical stabilizer or winglet height

**Check 2: Coordinate System Consistency**
- All stations (FS), waterlines (WL), buttlines (BL) positive in defined directions
- Fuselage station FS0 at nose, increases aft
- Waterline WL0 at reference, increases up
- Buttline BL0 at centerline, increases right (starboard positive per SAE convention)

**Check 3: Tolerance Consistency**
- Tighter tolerance on component than on assembly containing it (e.g., wing component ±0.01 m, total span ±0.1 m)
- Tolerance stackup does not exceed assembly tolerance

### Cross-Document Consistency

**Check 1: Design vs. As-Built**
- As-built dimensions within design tolerances (or dispositioned if not)
- Deviations correctly calculated and documented

**Check 2: AFM vs. TCDS**
- Overall dimensions (length, span, height) identical in AFM and TCDS
- Ground clearances consistent
- ICAO code consistent with wingspan

**Check 3: Data Package Consistency**
- Customer delivery data package contains consistent dimensional data across all documents
- No conflicting values that could confuse customer or maintenance personnel

## Non-Conformance Management

### Data Non-Conformance Report (Data NCR)

**Triggers for Data NCR:**
- Transcription error discovered
- Data file format error
- Inconsistency between documents
- Data not traceable to source
- Out-of-tolerance dimension not properly dispositioned in data file

**Data NCR Process:**
1. Data quality analyst identifies issue and generates Data NCR
2. Data NCR includes:
   - Description of non-conformance
   - Affected data file(s) and document(s)
   - Impact assessment (e.g., affects AFM, customer delivery)
   - Proposed corrective action
3. Responsible engineer reviews Data NCR and approves corrective action
4. Data NCR disposition:
   - **Correct data:** Update data file, reissue document if necessary
   - **Correct source:** If source data was wrong, update source and propagate correction
   - **Accept deviation:** If impact is negligible and correction cost is high, document and accept
5. Data NCR closed by quality engineer after verification of corrective action

### Root Cause Analysis for Data Errors

**For recurring data errors (≥3 similar errors):**
1. Perform root cause analysis:
   - Human factors: transcription error, calculation mistake, lack of training
   - Process: inadequate verification, unclear procedures, manual data entry prone to error
   - Tools: software bugs, lack of automation, inadequate validation checks
2. Implement corrective action:
   - Improve training for data analysts
   - Automate data extraction and verification where possible
   - Enhance software validation checks
   - Update procedures and work instructions
3. Verify effectiveness: monitor data quality metrics, ensure error rate decreases

## Quality Metrics

### Data Accuracy Metrics

**Metric 1: Data NCR Rate**
- Definition: Number of Data NCRs per 100 data files produced
- Target: ≤1 Data NCR per 100 data files in serial production
- Tracking: Monthly report by quality engineering

**Metric 2: First-Time Data Quality**
- Definition: Percentage of data files passing verification on first submission
- Target: ≥95% for serial production
- Tracking: Real-time dashboard in CAOS system

**Metric 3: Traceability Compliance**
- Definition: Percentage of data dimensions with complete traceability to source
- Target: 100% for critical dimensions, ≥98% for all dimensions
- Tracking: Quarterly audit by quality engineering

### Data Verification Cycle Time

**Metric 4: Average Verification Time**
- Definition: Time from data file submission to verification approval
- Target: ≤2 business days for routine verification
- Tracking: CAOS workflow management system

**Metric 5: Data Revision Rate**
- Definition: Average number of revisions per data file before acceptance
- Target: ≤1.2 revisions per file (most files accepted on first or second submission)
- Tracking: Document management system

## Integration with CAOS Digital Twin

### Automated Data Validation

**CAOS Validation Checks:**
1. **Format validation:** Automatic syntax and schema checks for JSON, CSV files
2. **Range checks:** Dimensions within physically reasonable limits (e.g., wingspan 30-100 m, not 1000 m)
3. **Consistency checks:** Cross-reference dimensions across files, flag discrepancies
4. **Traceability checks:** Verify link from data file to source measurement or design document
5. **Tolerance checks:** Automatic comparison of as-built to nominal, flag out-of-tolerance conditions

**CAOS Alerts:**
- Real-time alerts to quality engineer if validation check fails
- Dashboard showing data quality status for each MSN
- Trend charts showing data quality metrics over time

### Data Integrity Assurance

**CAOS Data Management:**
- Version control: All data files versioned and archived, change history tracked
- Access control: Read/write permissions based on role (e.g., only quality engineers approve data)
- Audit trail: All data changes logged with user ID, timestamp, reason for change
- Backup and recovery: Daily backup of production database, disaster recovery procedures

## Related Documents

- `01_OVERVIEW/baseline_dimensions.json` – Design baseline geometry (source data)
- `07_V_AND_V/VER-02-11-402_Dimensional_Tolerance_Analysis.md` – Verification requirements
- `09_PRODUCTION_PLANNING/DATA_GENERATION/Dimension_Data_Production_02-11-00.md` – Data generation process
- `09_PRODUCTION_PLANNING/DATA_GENERATION/Geometry_Measurement_Data_Generation.md` – Measurement procedures
- `09_PRODUCTION_PLANNING/QUALITY_CONTROL/As_Built_Geometry_Inspection.md` – Physical inspection procedures
- `09_PRODUCTION_PLANNING/SERIAL_NUMBER_MANAGEMENT/MSN_Geometry_Data_Linkage.md` – MSN data linkage
- Company Quality Manual – Data quality standards and procedures
- AS9100 Standard – Aerospace quality management system requirements

---

**Document Control:**
- Version: 1.0
- Status: Template
- Last Updated: 2025-11-11
- Classification: Quality Critical
- Author: COPILOT agent prompted by Amedeo Pelliccia
