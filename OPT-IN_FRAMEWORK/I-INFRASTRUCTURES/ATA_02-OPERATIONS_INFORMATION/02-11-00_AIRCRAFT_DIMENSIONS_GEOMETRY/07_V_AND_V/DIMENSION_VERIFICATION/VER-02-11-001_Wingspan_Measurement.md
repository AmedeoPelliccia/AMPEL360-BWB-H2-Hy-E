# [VER-02-11-001](VER-02-11-001_Wingspan_Measurement.md): Wingspan Measurement Verification

**Verification ID:** VER-02-11-001  
**Component:** 02-11-00 Aircraft Dimensions Geometry  
**Dimension:** Wingspan  
**Status:** Template Ready - Awaiting Test Execution

---

## 1. Objective

Verify that the physical wingspan of the AMPEL360 BWB aircraft meets the design specification of **52.0 m ± 0.1 m**, ensuring compliance with ICAO Code E airport compatibility requirements and design intent.

---

## 2. Scope

This verification procedure covers:
- Measurement of maximum wingspan from wingtip to wingtip
- Verification against design value in `Principal_Dimensions_Table.csv`
- Tolerance compliance check (±0.1 m)
- ICAO Code E requirement verification (wingspan between 52-65 m)

---

## 3. Reference Documents

| Document ID | Title | Location |
|-------------|-------|----------|
| REQ-02-11-001 | Wingspan Requirement | `03_REQUIREMENTS/Dimensional_Requirements.csv` |
| — | Principal Dimensions Table | `01_OVERVIEW/PRINCIPAL_DIMENSIONS/Principal_Dimensions_Table.csv` |
| — | Baseline Dimensions | `01_OVERVIEW/baseline_dimensions.json` |
| — | Dimension Summary | `01_OVERVIEW/TABLES/Dimension_Summary.csv` |
| ICAO Annex 14 | Aerodrome Design and Operations | Volume I, Chapter 2 |
| — | Airport Compatibility Table | `01_OVERVIEW/TABLES/Airport_Compatibility.csv` |

---

## 4. Design Specification

| Parameter | Value | Unit | Tolerance | Source |
|-----------|-------|------|-----------|--------|
| **Wingspan** | 52.0 | m | ±0.1 | Principal_Dimensions_Table.csv |
| **Measurement Point** | Wingtip to wingtip | — | — | Maximum span |
| **ICAO Code** | E | — | — | Airport_Compatibility.csv |
| **Code E Range** | 52-65 | m | — | ICAO Annex 14 |

**Design Value from baseline_dimensions.json:**
```json
"wingspan_m": 52.0
```

---

## 5. Acceptance Criteria

### 5.1 Primary Criteria
- **Pass Condition:** Measured wingspan = 52.0 m ± 0.1 m (51.9 m to 52.1 m)
- **Fail Condition:** Measured wingspan < 51.9 m or > 52.1 m

### 5.2 ICAO Code E Compliance
- **Pass Condition:** Measured wingspan ≥ 52.0 m and ≤ 65.0 m
- **Fail Condition:** Measured wingspan < 52.0 m or > 65.0 m

### 5.3 Consistency Criteria
- Measurement repeatability: standard deviation < 0.02 m across 3 measurements
- Left and right semi-spans differ by < 0.05 m (symmetry check)

---

## 6. Measurement Method

### 6.1 Equipment Required
| Equipment | Model/Type | Accuracy | Calibration Status |
|-----------|------------|----------|-------------------|
| Laser Tracker | Leica AT960 or equivalent | ±0.015 mm + 5 μm/m | Due: TBD |
| Calibrated Targets | SMR 1.5" | — | Due: TBD |
| Temperature Sensor | ±0.5°C | ±0.2°C | Due: TBD |
| Barometric Sensor | ±1 hPa | ±0.5 hPa | Due: TBD |

### 6.2 Environmental Conditions
- **Temperature:** 20°C ± 5°C (record actual)
- **Humidity:** 30-70% RH
- **Air Pressure:** Record for laser tracker compensation
- **Aircraft Configuration:** Level on landing gear, no external stores

### 6.3 Measurement Procedure

**Step 1: Aircraft Setup**
1. Position aircraft on level ground in assembly facility
2. Ensure landing gear properly extended and locked
3. Verify aircraft is level (pitch and roll within ±0.5°)
4. Remove any external attachments that affect span measurement
5. Allow thermal stabilization (minimum 4 hours after movement)

**Step 2: Equipment Setup**
1. Position laser tracker at optimal location (approximately midspan, 15 m from aircraft)
2. Perform laser tracker warm-up (minimum 30 minutes)
3. Verify calibration certificate validity
4. Attach SMR targets to both wingtips at the outermost structural points
5. Record environmental conditions (temperature, pressure, humidity)

**Step 3: Measurement Sequence**
1. Establish coordinate system using aircraft reference points (nose datum, BL 0)
2. Measure left wingtip position (X, Y, Z coordinates) - 3 readings
3. Measure right wingtip position (X, Y, Z coordinates) - 3 readings
4. Calculate wingspan as lateral distance between wingtip points
5. Repeat entire measurement sequence for statistical validation (minimum 3 complete sets)

**Step 4: Symmetry Check**
1. Measure left semi-span from aircraft centerline (BL 0) to left wingtip
2. Measure right semi-span from aircraft centerline (BL 0) to right wingtip
3. Verify semi-span difference < 0.05 m

**Step 5: Data Recording**
1. Record all raw measurement data in `[Dimension_Verification_Results.csv](Dimension_Verification_Results.csv)`
2. Calculate mean, standard deviation, and confidence interval
3. Document environmental conditions and any deviations from procedure
4. Photograph measurement setup and SMR target positions

---

## 7. Calculations

### 7.1 Wingspan Calculation
```
Wingspan = |Y_right - Y_left|

### 7.2 Statistical Analysis
```
Mean Wingspan = (Σ Wingspan_i) / n
Standard Deviation = sqrt(Σ(Wingspan_i - Mean)² / (n-1))
95% Confidence Interval = Mean ± (1.96 × SD / sqrt(n))
```

### 7.3 Semi-Span Check
```
Left Semi-Span = Distance from BL 0 to left wingtip
Right Semi-Span = Distance from BL 0 to right wingtip
Asymmetry = |Right Semi-Span - Left Semi-Span|
Pass if: Asymmetry < 0.05 m
```

---

## 8. Test Data Recording

### 8.1 Measurement Results Table

| Measurement # | Left Wingtip X (m) | Left Wingtip Y (m) | Left Wingtip Z (m) | Right Wingtip X (m) | Right Wingtip Y (m) | Right Wingtip Z (m) | Calculated Wingspan (m) |
|---------------|-------------------|-------------------|-------------------|---------------------|---------------------|---------------------|------------------------|
| 1 | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| 2 | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| 3 | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| **Mean** | — | — | — | — | — | — | **TBD** |
| **Std Dev** | — | — | — | — | — | — | **TBD** |

### 8.2 Environmental Conditions

| Parameter | Value | Unit |
|-----------|-------|------|
| Temperature | TBD | °C |
| Humidity | TBD | % RH |
| Barometric Pressure | TBD | hPa |
| Aircraft Attitude (Pitch) | TBD | deg |
| Aircraft Attitude (Roll) | TBD | deg |

### 8.3 Semi-Span Results

| Semi-Span | Measurement 1 (m) | Measurement 2 (m) | Measurement 3 (m) | Mean (m) |
|-----------|------------------|------------------|------------------|----------|
| Left | TBD | TBD | TBD | TBD |
| Right | TBD | TBD | TBD | TBD |
| **Asymmetry** | — | — | — | **TBD** |

---

## 9. Results and Analysis

### 9.1 Summary

| Metric | Result | Status |
|--------|--------|--------|
| **Mean Wingspan** | TBD m | TBD |
| **Design Target** | 52.0 m | — |
| **Deviation** | TBD m | TBD |
| **Within Tolerance (±0.1 m)?** | TBD | TBD |
| **ICAO Code E Compliant?** | TBD | TBD |
| **Repeatability (Std Dev)** | TBD m | TBD |
| **Symmetry Check** | TBD m | TBD |

### 9.2 Disposition

**Verification Result:** [ ] PASS  [ ] FAIL  [ ] CONDITIONAL

**Justification:** TBD

**Action Items (if any):**
1. TBD

---

## 10. Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Test Engineer** | TBD | | TBD |
| **Quality Inspector** | TBD | | TBD |
| **Design Engineer** | TBD | | TBD |
| **Program Manager** | TBD | | TBD |

---

## 11. Traceability

### 11.1 Requirements Satisfied
- REQ-02-11-001: Wingspan = 52.0 m ± 0.1 m (Dimensional Requirements)
- REQ-02-11-025: ICAO Code E compatibility (Airport Compatibility Requirements)

### 11.2 Related Verifications
- [VER-02-11-005](VER-02-11-005_Principal_Dimensions_Table_Check.md): Principal Dimensions Table Check
- [VAL-02-11-101](../GEOMETRY_VALIDATION/VAL-02-11-101_Planform_Geometry_Validation.md): Planform Geometry Validation
- COMP-401: CS-25 and ICAO compliance verification

---

## 12. Attachments

1. Laser tracker calibration certificate
2. SMR target placement photographs
3. Raw measurement data files (.txt or .csv from laser tracker software)
4. Environmental condition logs
5. Any non-conformance reports (if applicable)

---

## 13. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-11 | COPILOT Agent prompted by Amedeo Pelliccia | Initial template creation |

---

**Document Control:**
- **Template Status:** Ready for Test Execution
- **Next Review Date:** Upon test execution
- **Location:** `07_V_AND_V/DIMENSION_VERIFICATION/VER-02-11-001_Wingspan_Measurement.md`
