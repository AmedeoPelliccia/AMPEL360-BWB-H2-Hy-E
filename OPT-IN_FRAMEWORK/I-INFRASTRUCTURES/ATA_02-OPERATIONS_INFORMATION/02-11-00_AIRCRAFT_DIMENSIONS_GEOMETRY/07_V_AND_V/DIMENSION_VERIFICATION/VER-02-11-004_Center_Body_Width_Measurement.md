# VER-02-11-004: Center Body Width Measurement Verification

**Verification ID:** VER-02-11-004  
**Component:** 02-11-00 Aircraft Dimensions Geometry  
**Dimension:** Center Body Width  
**Status:** Template Ready - Awaiting Test Execution

---

## 1. Objective

Verify that the center body width of the AMPEL360 BWB aircraft meets the design specification of **38.0 m ± 0.1 m**, measured at the maximum width location (STA 15.0).

---

## 2. Scope

This verification procedure covers:
- Measurement of maximum center body width at STA 15.0
- Verification against design value in `Principal_Dimensions_Table.csv`
- Tolerance compliance check (±0.1 m)
- Critical for passenger cabin width and structural analysis

---

## 3. Reference Documents

| Document ID | Title | Location |
|-------------|-------|----------|
| REQ-02-11-004 | Center Body Width Requirement | `03_REQUIREMENTS/BWB_Geometry_Requirements.csv` |
| — | Principal Dimensions Table | `01_OVERVIEW/PRINCIPAL_DIMENSIONS/Principal_Dimensions_Table.csv` |
| — | Center Body Design | `04_DESIGN/BWB_GEOMETRY/CENTER_BODY/` |
| — | Cross-Section Design | `04_DESIGN/BWB_GEOMETRY/CROSS_SECTION/` |

---

## 4. Design Specification

| Parameter | Value | Unit | Tolerance | Source |
|-----------|-------|------|-----------|--------|
| **Center Body Width** | 38.0 | m | ±0.1 | Principal_Dimensions_Table.csv |
| **Measurement Station** | STA 15.0 | m | — | Maximum width location |
| **Measurement Level** | WL (varies) | m | — | Widest cross-section |

---

## 5. Acceptance Criteria

### 5.1 Primary Criteria
- **Pass Condition:** Measured width = 38.0 m ± 0.1 m (37.9 m to 38.1 m)
- **Fail Condition:** Measured width < 37.9 m or > 38.1 m

### 5.2 Consistency Criteria
- Measurement repeatability: standard deviation < 0.02 m across 3 measurements
- Symmetry: port and starboard semi-widths differ by < 0.05 m

---

## 6. Measurement Method

### 6.1 Equipment Required
| Equipment | Model/Type | Accuracy | Calibration Status |
|-----------|------------|----------|-------------------|
| Photogrammetry System | GOM ATOS or equivalent | ±0.02 mm | Due: TBD |
| Laser Tracker | Leica AT960 or equivalent | ±0.015 mm + 5 μm/m | Due: TBD |
| Calibrated Targets | Coded targets + SMR | — | Due: TBD |

### 6.2 Measurement Procedure

**Step 1: Station Location Verification**
1. Verify STA 15.0 location on aircraft (15.0 m aft of nose datum)
2. Mark measurement plane perpendicular to aircraft centerline
3. Document precise station location

**Step 2: Measurement Setup**
1. Position photogrammetry system to capture full cross-section at STA 15.0
2. Apply coded targets to port and starboard edges at maximum width
3. Alternative: Use laser tracker to measure lateral extent

**Step 3: Width Measurement**
1. Capture 3D coordinates of port-most point at STA 15.0
2. Capture 3D coordinates of starboard-most point at STA 15.0
3. Calculate lateral distance (Buttline coordinate difference)
4. Repeat measurements 3 times with re-targeting for validation

---

## 7. Calculations

### 7.1 Center Body Width Calculation
```
Center_Body_Width = BL_starboard - BL_port = |Y_starboard - Y_port|
```

For symmetric aircraft:
```
Center_Body_Width = 2 × max(|BL_port|, |BL_starboard|)
```

### 7.2 Symmetry Check
```
Port Semi-Width = Distance from BL 0 to port edge
Starboard Semi-Width = Distance from BL 0 to starboard edge
Asymmetry = |Starboard Semi-Width - Port Semi-Width|
Pass if: Asymmetry < 0.05 m
```

---

## 8. Test Data Recording

### 8.1 Measurement Results

| Measurement # | Port Edge BL (m) | Starboard Edge BL (m) | Calculated Width (m) |
|---------------|-----------------|----------------------|---------------------|
| 1 | TBD | TBD | TBD |
| 2 | TBD | TBD | TBD |
| 3 | TBD | TBD | TBD |
| **Mean** | — | — | **TBD** |
| **Std Dev** | — | — | **TBD** |

### 8.2 Symmetry Check

| Semi-Width | Measurement 1 (m) | Measurement 2 (m) | Measurement 3 (m) | Mean (m) |
|-----------|------------------|------------------|------------------|----------|
| Port | TBD | TBD | TBD | TBD |
| Starboard | TBD | TBD | TBD | TBD |
| **Asymmetry** | — | — | — | **TBD** |

---

## 9. Results and Analysis

### 9.1 Summary

| Metric | Result | Status |
|--------|--------|--------|
| **Mean Center Body Width** | TBD m | TBD |
| **Design Target** | 38.0 m | — |
| **Deviation** | TBD m | TBD |
| **Within Tolerance (±0.1 m)?** | TBD | TBD |
| **Repeatability (Std Dev)** | TBD m | TBD |
| **Symmetry Check** | TBD m | TBD |

### 9.2 Disposition

**Verification Result:** [ ] PASS  [ ] FAIL  [ ] CONDITIONAL

**Justification:** TBD

---

## 10. Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Test Engineer** | TBD | | TBD |
| **Quality Inspector** | TBD | | TBD |
| **Structures Engineer** | TBD | | TBD |

---

## 11. Traceability

### 11.1 Requirements Satisfied
- REQ-02-11-004: Center Body Width = 38.0 m ± 0.1 m
- REQ-02-11-007: BWB center body geometry requirements

### 11.2 Related Verifications
- VER-02-11-005: Principal Dimensions Table Check
- VAL-02-11-104: Center Body Geometry Validation

---

## 12. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-11 | COPILOT Agent prompted by Amedeo Pelliccia | Initial template creation |
