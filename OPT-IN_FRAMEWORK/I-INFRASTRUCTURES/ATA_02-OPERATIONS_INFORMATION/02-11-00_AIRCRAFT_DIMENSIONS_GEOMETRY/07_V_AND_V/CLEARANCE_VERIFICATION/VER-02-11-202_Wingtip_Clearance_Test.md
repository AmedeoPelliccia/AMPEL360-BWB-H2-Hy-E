# VER-02-11-202: Wingtip Clearance Test

**Verification ID:** VER-02-11-202  
**Component:** 02-11-00 Aircraft Dimensions Geometry  
**Test:** Wingtip Clearance and Deflection Verification  
**Status:** Template Ready - Awaiting Test Execution

---

## 1. Objective

Verify wingtip ground clearances under maximum deflection conditions including:
- Static clearance at MTOW with full fuel load
- Maximum wingtip droop measurement (0.15 m design)
- Taxiway lateral clearance verification (4.0 m minimum)

---

## 2. Design Specifications

| Parameter | Design Value | Min Required | Condition |
|-----------|--------------|--------------|-----------|
| Wingtip Height (static) | 1.2 m | 0.8 m | MTOW, fueled |
| Maximum Droop | 0.15 m | — | Fuel load effect |
| Lateral Clearance | 4.0 m | 3.5 m | Taxiing envelope |
| Wingtip Location | BL ±26 m | — | From centerline |

---

## 3. Test Methods

### 3.1 Static Height Measurement
- Aircraft at MTOW with maximum fuel
- Measure height from ground to lowest point of each wingtip
- Record port and starboard values

### 3.2 Deflection Test
- Measure wingtip height at empty weight
- Progressively load fuel to maximum capacity
- Record height at each fuel increment
- Calculate maximum droop (empty height - full height)

### 3.3 Lateral Clearance Verification
- Measure wingspan at ground level (accounting for droop)
- Add required lateral clearance (4.0 m each side)
- Verify total envelope ≤ Code E taxiway width (23 m)

---

## 4. Acceptance Criteria

| Criterion | Target | Tolerance | Result |
|-----------|--------|-----------|--------|
| Wingtip Height @ MTOW | 1.2 m | Min 0.8 m | TBD |
| Maximum Droop | 0.15 m | Max 0.20 m | TBD |
| Port-Starboard Symmetry | < 0.05 m | — | TBD |
| Lateral Clearance Met | Yes | ≥ 3.5 m | TBD |

---

## 5. Data Recording

### 5.1 Deflection Measurements

| Fuel Load (%) | Fuel Mass (kg) | Left Tip Height (m) | Right Tip Height (m) | Mean Height (m) | Droop from Empty (m) |
|--------------|---------------|-------------------|---------------------|----------------|---------------------|
| 0 (Empty) | 0 | TBD | TBD | TBD | 0.00 |
| 25 | TBD | TBD | TBD | TBD | TBD |
| 50 | TBD | TBD | TBD | TBD | TBD |
| 75 | TBD | TBD | TBD | TBD | TBD |
| 100 (Full) | TBD | TBD | TBD | TBD | **TBD** |

### 5.2 Clearance Summary

| Parameter | Measured | Required | Status |
|-----------|----------|----------|--------|
| Min Wingtip Height | TBD m | 0.8 m | TBD |
| Max Droop | TBD m | ≤ 0.20 m | TBD |
| Lateral Clearance | TBD m | ≥ 3.5 m | TBD |
| Symmetry | TBD m | < 0.05 m | TBD |

---

## 6. Results Summary

**Verification Result:** [ ] PASS  [ ] FAIL  [ ] CONDITIONAL

**Justification:** TBD

---

## 7. Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Test Engineer** | TBD | | TBD |
| **Structures Engineer** | TBD | | TBD |
| **Airport Planning** | TBD | | TBD |

---

## 8. Traceability

- REQ-02-11-015: Wingtip clearance requirements
- REQ-02-11-016: Deflection limits
- Critical_Clearances.csv: Wingtip specifications

---

**Revision:** 1.0 | **Date:** 2025-11-11 | **Author:** V&V Team
