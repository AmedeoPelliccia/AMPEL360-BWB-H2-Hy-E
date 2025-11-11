# VER-02-11-401: CS-25 and ICAO Geometric Compliance Verification

**Verification ID:** VER-02-11-401  
**Component:** 02-11-00 Aircraft Dimensions Geometry  
**Standards:** CS-25, ICAO Annex 14  
**Status:** Template Ready - Awaiting Verification

---

## 1. Objective

Verify compliance of aircraft dimensions and geometry with:
- **CS-25:** Certification Specifications for Large Aeroplanes
- **ICAO Annex 14:** Aerodrome Design and Operations (Code E)
- **Airport Compatibility:** Taxiway, gate, and parking requirements

---

## 2. Regulatory Requirements

### 2.1 CS-25 Geometric Requirements

| Regulation | Title | Requirement | Compliance Method | Evidence |
|-----------|-------|-------------|------------------|----------|
| CS-25.771 | Pilot Compartment View | View angles, geometry | Analysis + Test | TBD |
| CS-25.783 | Doors | Door positioning, dimensions | Design Review | TBD |
| CS-25.807 | Emergency Exit Access | Sill height, accessibility | Mockup Test | TBD |
| CS-25.1541 | Markings/Placards | Dimension markings | Documentation | TBD |
| CS-25.1583 | Operating Limitations | Geometric limits in AFM | AFM Documentation | TBD |

### 2.2 ICAO Annex 14 - Aerodrome Code E

| Parameter | Code E Requirement | AMPEL360 Design | Status |
|-----------|-------------------|-----------------|--------|
| **Wingspan** | 52 m to < 65 m | 52.0 m | TBD |
| **Outer Main Gear Wheel Span** | 9 m to < 15 m | 15.5 m (wheelbase) | TBD (*) |
| **Taxiway Width** | 23 m minimum | 52 m span + clearance | TBD |
| **Runway Width** | 45 m minimum | Compatible | TBD |
| **Taxiway Center Line to Object** | 21.5 m | Requires analysis | TBD |
| **Aircraft Stand Width** | 44 m typical | 52 m + clearance = ~60 m | TBD |

**Note (*):** Code E specifies outer main gear wheel span 9-15 m. AMPEL360 wheelbase is 15.5 m. Clarification needed on whether this refers to wheelbase or track.

---

## 3. Airport Compatibility Analysis

### 3.1 Taxiway Requirements

**ICAO Code E Taxiway:**
- Width: 23 m minimum
- Clearance required: Each side = (Wingspan / 2) + safety margin
- AMPEL360: (52 / 2) + 4.0 m safety = 30 m required from centerline
- **Total envelope needed: 60 m**
- **Status:** Exceeds Code E standard taxiway width. **Requires Code F taxiway (30 m width) or operational restrictions.**

### 3.2 Gate Compatibility

**Standard Code E Gate:**
- Width: ~44 m
- AMPEL360 requirement: 52 m + 2×4 m clearance = 60 m
- **Status:** Requires wider than standard Code E gate. Compatible with Code F gates (60 m).

### 3.3 Turning Radius

**ICAO Requirement:**
- Adequate maneuvering area on taxiways
- AMPEL360 turning radius: 42 m
- **Status:** Analysis required for Code E/F taxiway compatibility.

---

## 4. Compliance Verification Matrix

### 4.1 CS-25 Compliance

| Item | Requirement | Evidence Document | Verification Method | Result | Status |
|------|------------|------------------|-------------------|--------|--------|
| Pilot View | CS-25.771 | 06_ENGINEERING/Analysis | FEA + Test | TBD | TBD |
| Door Position | CS-25.783 | 04_DESIGN/Door_Design | Design Review | TBD | TBD |
| Exit Access | CS-25.807 | VER-02-11-003, VER-02-11-203 | Measurement | TBD | TBD |
| Markings | CS-25.1541 | 11_OPERATIONS_MAINTENANCE/ | Documentation | TBD | TBD |
| Limitations | CS-25.1583 | 11_OPERATIONS_MAINTENANCE/AFM | Documentation | TBD | TBD |

### 4.2 ICAO Annex 14 Compliance

| Item | Requirement | AMPEL360 Value | Compliant? | Notes |
|------|------------|---------------|-----------|-------|
| Wingspan | 52-65 m (Code E) | 52.0 m | TBD | At lower limit |
| Main Gear Span | 9-15 m (Code E) | 15.5 m wheelbase | TBD | Needs clarification |
| Taxiway Width | 23 m (Code E) | 60 m required | **NO** | Exceeds Code E, needs Code F |
| Runway Width | 45 m (Code E) | Compatible | TBD | OK |
| Gate Width | 44 m (Code E) | 60 m required | **NO** | Needs Code F gate |

---

## 5. Findings and Recommendations

### 5.1 Critical Findings

**Finding 1: Airport Code Classification**
- **Issue:** Aircraft dimensions compatible with Code E wingspan (52 m), but operational envelope (60 m with clearance) exceeds Code E taxiway and gate dimensions.
- **Impact:** Limits airport compatibility to facilities with Code F infrastructure.
- **Recommendation:** 
  - Document operational restrictions for Code E-only airports.
  - Identify Code F-capable airports for route planning.
  - Consider operational procedures to reduce required clearance where safe.

**Finding 2: Wheelbase vs. Track Clarification**
- **Issue:** ICAO Code E specifies "outer main gear wheel span" 9-15 m. AMPEL360 wheelbase is 15.5 m, track is 30.0 m.
- **Clarification Needed:** Determine if specification refers to wheelbase (longitudinal) or track (lateral).
- **Recommendation:** Engage EASA/ICAO for clarification. If track is specified, aircraft may exceed Code E.

### 5.2 CS-25 Compliance Status

All CS-25 geometric requirements appear addressable through standard compliance methods. No show-stoppers identified, but verification testing required.

---

## 6. Compliance Summary

| Standard | Section | Compliant? | Conditional Items | Action Required |
|----------|---------|-----------|------------------|----------------|
| CS-25 | Geometric | TBD | Testing required | Execute test plans |
| ICAO Annex 14 | Code E Wingspan | YES | — | None |
| ICAO Annex 14 | Code E Operations | **CONDITIONAL** | Taxiway/gate compatibility | Document restrictions |

---

## 7. Results

**Overall Compliance Result:** [ ] COMPLIANT  [ ] CONDITIONALLY COMPLIANT  [ ] NON-COMPLIANT

**Justification:** TBD

**Recommended Actions:**
1. TBD

---

## 8. Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Certification Engineer** | TBD | | TBD |
| **Regulatory Affairs** | TBD | | TBD |
| **Program Manager** | TBD | | TBD |

---

## 9. Traceability

- All REQ-02-11-XXX requirements
- CS-25 applicable paragraphs
- ICAO Annex 14, Volume I, Chapter 2
- Airport_Compatibility.csv

---

**Revision:** 1.0 | **Date:** 2025-11-11 | **Author:** COPILOT Agent prompted by Amedeo Pelliccia
