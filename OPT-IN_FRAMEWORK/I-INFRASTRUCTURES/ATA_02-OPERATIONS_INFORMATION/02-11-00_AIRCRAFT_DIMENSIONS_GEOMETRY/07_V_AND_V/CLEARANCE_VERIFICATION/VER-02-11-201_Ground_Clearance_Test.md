# [VER-02-11-201](VER-02-11-201_Ground_Clearance_Test.md): Ground Clearance Test

**Verification ID:** VER-02-11-201  
**Component:** 02-11-00 Aircraft Dimensions Geometry  
**Test:** Ground Clearance Verification  
**Status:** Template Ready - Awaiting Test Execution

---

## 1. Objective

Verify that all aircraft ground clearances meet minimum requirements as specified in `Critical_Clearances.csv` under various operational conditions including:
- Level ground (MTOW and empty weight)
- Maximum rotation angle (12°)
- Various loading conditions

---

## 2. Critical Clearance Points

| Location | Station | Buttline | Min Required (m) | Design Value (m) | Condition |
|----------|---------|----------|-----------------|------------------|-----------|
| Belly (minimum) | STA 18 | BL 0 | 1.5 | 1.8 | MTOW level |
| Nose (lowest) | STA 3 | BL 0 | 1.5 | 2.1 | Rotation |
| Tail (aft body) | STA 36 | BL 0 | 2.0 | 2.5 | Level |
| Engine intake L | STA 25 | BL -12 | 2.5 | 2.8 | Ground ops |
| Engine intake R | STA 25 | BL +12 | 2.5 | 2.8 | Ground ops |
| Nose at 12° rot | STA 3 | BL 0 | 0.3 | 0.5 | Max rotation |
| Tail at 12° rot | STA 36 | BL 0 | 0.2 | 0.3 | Tail strike limit |

---

## 3. Test Methods

### 3.1 Static Measurements
- Aircraft on level ground, landing gear extended
- Measure clearances at specified locations
- Test at multiple weight conditions (empty, MTOW)

### 3.2 Rotation Test
- Simulate rotation using jacks or test rig
- Gradually increase pitch angle to 12° limit
- Monitor clearances at nose and tail
- Document tail strike angle

### 3.3 Load Deflection Test
- Measure clearances with varying fuel/payload
- Document relationship between loading and clearance
- Verify minimum clearance maintained at MTOW

---

## 4. Acceptance Criteria

All clearances must exceed minimum required values with appropriate safety margin (typically 20% of design value above minimum).

---

## 5. Data Recording

| Location | Min Req (m) | Test Condition | Measured (m) | Margin (m) | Result |
|----------|------------|----------------|-------------|-----------|--------|
| Belly @ MTOW | 1.5 | Level, MTOW | TBD | TBD | TBD |
| Nose @ Level | 1.5 | Level, MTOW | TBD | TBD | TBD |
| Tail @ Level | 2.0 | Level, MTOW | TBD | TBD | TBD |
| Nose @ 12° | 0.3 | 12° rotation | TBD | TBD | TBD |
| Tail @ 12° | 0.2 | 12° rotation | TBD | TBD | TBD |
| Engine Intakes | 2.5 | Level | TBD | TBD | TBD |

---

## 6. Results Summary

**Verification Result:** [ ] PASS  [ ] FAIL  [ ] CONDITIONAL

**Critical Findings:** TBD

**Justification:** TBD

---

## 7. Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Test Engineer** | TBD | | TBD |
| **Safety Engineer** | TBD | | TBD |
| **Flight Operations** | TBD | | TBD |

---

## 8. Traceability

- REQ-02-11-013: Ground clearance requirements
- REQ-02-11-014: Tail strike angle limits
- Critical_Clearances.csv: All clearance specifications

---

**Revision:** 1.0 | **Date:** 2025-11-11 | **Author:** COPILOT Agent prompted by Amedeo Pelliccia
