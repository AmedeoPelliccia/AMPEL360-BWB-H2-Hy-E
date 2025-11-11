# VER-02-11-003: Overall Height Measurement Verification

**Verification ID:** VER-02-11-003  
**Component:** 02-11-00 Aircraft Dimensions Geometry  
**Dimension:** Overall Height  
**Status:** Template Ready - Awaiting Test Execution

---

## 1. Objective

Verify that the overall height of the AMPEL360 BWB aircraft meets the design specification of **14.5 m ± 0.05 m**, measured from the ground to the highest point with landing gear extended.

---

## 2. Scope

This verification procedure covers:
- Measurement of overall aircraft height (ground to highest point)
- Verification against design value in `Principal_Dimensions_Table.csv`
- Tolerance compliance check (±0.05 m - tighter tolerance for hangar clearance)
- Landing gear extended configuration

---

## 3. Reference Documents

| Document ID | Title | Location |
|-------------|-------|----------|
| REQ-02-11-003 | Overall Height Requirement | `03_REQUIREMENTS/Dimensional_Requirements.csv` |
| — | Principal Dimensions Table | `01_OVERVIEW/PRINCIPAL_DIMENSIONS/Principal_Dimensions_Table.csv` |
| — | Critical Clearances | `01_OVERVIEW/TABLES/Critical_Clearances.csv` |
| — | Height Specifications | `04_DESIGN/GROUND_CLEARANCE_DESIGN/` |

---

## 4. Design Specification

| Parameter | Value | Unit | Tolerance | Source |
|-----------|-------|------|-----------|--------|
| **Overall Height** | 14.5 | m | ±0.05 | Principal_Dimensions_Table.csv |
| **Measurement Point** | Ground to highest point | — | — | Gear extended |
| **Hangar Clearance Required** | 2.0 | m | — | Critical_Clearances.csv |

---

## 5. Acceptance Criteria

### 5.1 Primary Criteria
- **Pass Condition:** Measured height = 14.5 m ± 0.05 m (14.45 m to 14.55 m)
- **Fail Condition:** Measured height < 14.45 m or > 14.55 m

### 5.2 Operational Criteria
- **Hangar Compatibility:** Overall height + 2.0 m clearance ≤ typical hangar door height
- Critical for airport facility planning

---

## 6. Measurement Method

### 6.1 Equipment Required
| Equipment | Model/Type | Accuracy | Calibration Status |
|-----------|------------|----------|-------------------|
| Laser Tracker | Leica AT960 or equivalent | ±0.015 mm + 5 μm/m | Due: TBD |
| Level Reference | Optical level | ±1 mm | Due: TBD |
| Calibrated Targets | SMR 1.5" | — | Due: TBD |

### 6.2 Measurement Procedure

**Step 1: Aircraft Setup**
1. Position aircraft on level, surveyed ground surface
2. Verify landing gear properly extended and locked
3. Aircraft at specified weight condition (document actual)
4. All antennas and protrusions in operational configuration

**Step 2: Ground Reference Establishment**
1. Establish ground reference plane using multiple points under aircraft
2. Verify level reference (pitch and roll < ±0.5°)
3. Record ground reference elevation

**Step 3: Height Measurement**
1. Identify highest point on aircraft (typically top of vertical surface at STA 15, WL 14.5)
2. Measure Z-coordinate of highest point relative to ground reference
3. Repeat measurements at 3 different times for validation

---

## 7. Calculations

### 7.1 Height Calculation
```
Overall_Height = Z_highest_point - Z_ground_reference
```

### 7.2 Statistical Analysis
```
Mean Height = (Σ Height_i) / n
Standard Deviation = sqrt(Σ(Height_i - Mean)² / (n-1))
```

---

## 8. Test Data Recording

### 8.1 Measurement Results

| Measurement # | Ground Ref Z (m) | Highest Point Z (m) | Calculated Height (m) |
|---------------|-----------------|---------------------|----------------------|
| 1 | TBD | TBD | TBD |
| 2 | TBD | TBD | TBD |
| 3 | TBD | TBD | TBD |
| **Mean** | — | — | **TBD** |
| **Std Dev** | — | — | **TBD** |

### 8.2 Aircraft Configuration

| Parameter | Value | Unit |
|-----------|-------|------|
| Aircraft Weight | TBD | kg |
| Fuel Load | TBD | kg |
| Landing Gear Status | Extended/Locked | — |
| Highest Point Location | STA 15, BL 0, WL 14.5 (nominal) | — |

---

## 9. Results and Analysis

### 9.1 Summary

| Metric | Result | Status |
|--------|--------|--------|
| **Mean Overall Height** | TBD m | TBD |
| **Design Target** | 14.5 m | — |
| **Deviation** | TBD m | TBD |
| **Within Tolerance (±0.05 m)?** | TBD | TBD |
| **Hangar Clearance (Height + 2.0m)** | TBD m | TBD |

### 9.2 Disposition

**Verification Result:** [ ] PASS  [ ] FAIL  [ ] CONDITIONAL

**Justification:** TBD

---

## 10. Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Test Engineer** | TBD | | TBD |
| **Quality Inspector** | TBD | | TBD |
| **Facilities Planner** | TBD | | TBD |

---

## 11. Traceability

### 11.1 Requirements Satisfied
- REQ-02-11-003: Overall Height = 14.5 m ± 0.05 m
- REQ-02-11-013: Overhead clearance requirements

### 11.2 Related Verifications
- VER-02-11-005: Principal Dimensions Table Check
- VER-02-11-201: Ground Clearance Test

---

## 12. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-11 | COPILOT Agent prompted by Amedeo Pelliccia | Initial template creation |
