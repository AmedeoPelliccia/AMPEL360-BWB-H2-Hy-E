# Means of Compliance (MOC) Summary

**Document:** AMPEL360-52-10-01-MOC-SUMMARY  
**Status:** PRELIMINARY  
**Date:** 2025-11-03

## Overview

This document summarizes the means of compliance (MOC) selected for each applicable CS-25 paragraph for Door L1 Forward certification.

---

## MOC Categories

### 1. Test (T)
Physical testing to demonstrate compliance directly

**Used for:**
- CS25.305 - Ultimate strength
- CS25.307 - Proof test
- CS25.571 - Fatigue and damage tolerance
- CS25.783 - Door operation and interlocks
- CS25.853 - Fire resistance
- CS25.954 - Lightning strike

**Percentage:** ~40% of compliance items

### 2. Analysis (A)
Engineering analysis, typically supported by test validation

**Used for:**
- CS25.301 - Loads
- CS25.365 - Pressurization (with test)
- CS25.571 - Damage tolerance (with test)
- CS25.629 - Flutter/resonance (with GVT)
- CS25.631 - Bird strike
- CS25.1309 - FMEA/system design

**Percentage:** ~30% of compliance items

### 3. Inspection (I)
Verification by physical inspection or measurement

**Used for:**
- CS25.603 - Materials (data review)
- CS25.807 - Emergency exit dimensions
- CS25.812 - Emergency lighting installation
- CS25.1316 - Electrical installation

**Percentage:** ~10% of compliance items

### 4. Demonstration (D)
Functional demonstration of capability

**Used for:**
- CS25.783 - Door operation
- CS25.810 - Emergency egress
- CS25.1301 - System function

**Percentage:** ~15% of compliance items

### 5. Design Feature (DF)
Inherent design characteristic

**Used for:**
- CS25.783(e) - Plug door (prevents opening in flight)

**Percentage:** ~5% of compliance items

---

## Detailed MOC Table

| CS25 Para | Requirement | Primary MOC | Secondary MOC | Rationale |
|-----------|-------------|-------------|---------------|-----------|
| 25.301 | Loads | Analysis | Test correlation | Standard practice |
| 25.305 | Strength/deformation | Test | - | Mandatory test |
| 25.307 | Proof of structure | Test | - | Mandatory proof test |
| 25.365 | Pressurization | Test | Analysis support | Critical safety item |
| 25.571 | Damage tolerance | Analysis | Test validation | Per AC 25.571-1D |
| 25.571 | Fatigue | Test | - | 2x service life demo |
| 25.603 | Materials | Inspection | Data review | Material certifications |
| 25.613 | Material properties | Test | - | Coupon tests required |
| 25.629 | Aeroelastic | Analysis | GVT validation | Modal survey mandatory |
| 25.631 | Bird strike | Analysis | - | Panel impact analysis |
| 25.783 | Doors | Test | Demonstration | Operation and interlocks |
| 25.807 | Emergency exits | Inspection | - | Dimensional check |
| 25.809 | Exit arrangement | Analysis | Inspection | Layout verification |
| 25.810 | Emergency egress | Demonstration | - | Evacuation capability |
| 25.812 | Emergency lighting | Inspection | - | Installation verification |
| 25.853 | Fire protection | Test | - | 15-minute burn test |
| 25.954 | Lightning strike | Test | - | Zone 1A direct effects |
| 25.1301 | Function | Demonstration | - | Operational demo |
| 25.1309 | System design | Analysis | FMEA/FTA | Safety assessment |
| 25.1316 | Electrical | Inspection | Test | If electrical systems |
| 25.1419 | Ice protection | Analysis | - | If ice protection required |
| 25.1435 | Hydraulics | Analysis | Test | If hydraulic actuation |

---

## MOC Selection Rationale

### Critical Safety Items (Test Required)
Items where failure could be catastrophic require physical test demonstration:
- **Structural ultimate** (CS25.305) - Verify structure withstands ultimate load
- **Fatigue life** (CS25.571) - Demonstrate crack-free life
- **Door operation** (CS25.783) - Prove interlock prevents inadvertent opening
- **Fire resistance** (CS25.853) - Validate fire barrier integrity

### Novel Configuration Items (Test + Analysis)
BWB configuration and composite construction require both analysis and test:
- **Aeroelastic** (CS25.629) - Novel geometry, GVT mandatory
- **Damage tolerance** (CS25.571) - Composite structure, test validation required
- **Pressurization** (CS25.365) - Complex load path, test verification needed

### Standard Practice Items (Analysis or Inspection)
Well-established methods can rely on analysis or inspection:
- **Loads** (CS25.301) - Standard FEA methods
- **Exit dimensions** (CS25.807) - Physical measurement
- **Materials** (CS25.603) - Certification review
- **Bird strike** (CS25.631) - Standard panel analysis

---

## MOC Documentation Requirements

### For Test-Based MOC
**Required documentation:**
1. Test plan (DER approved)
2. Test procedure
3. Test setup photos
4. Instrumentation plan
5. Data acquisition records
6. Test results and analysis
7. Test report (DER signed)
8. Test witnessing report (if applicable)

### For Analysis-Based MOC
**Required documentation:**
1. Analysis plan
2. Analysis methodology (DER approved if critical)
3. Assumptions and boundary conditions
4. Analysis results
5. Margins of safety
6. Sensitivity studies
7. Validation against test data (if available)
8. Analysis report (DER reviewed)

### For Inspection-Based MOC
**Required documentation:**
1. Inspection criteria
2. Inspection procedure
3. Inspection records
4. Photos or measurements
5. Certifications (for materials)
6. Conformity statement

### For Demonstration-Based MOC
**Required documentation:**
1. Demonstration plan
2. Acceptance criteria
3. Demonstration procedure
4. Video or photo evidence
5. Results documentation
6. Demonstration report

---

## Test vs. Analysis Decision Matrix

| Factor | Favor Test | Favor Analysis |
|--------|------------|----------------|
| Safety criticality | High | Low |
| Novel design | Yes | No |
| Composite structure | Yes | No (for simple cases) |
| Regulation requirement | Mandatory | Permitted |
| Cost | Can afford | Budget constrained |
| Schedule | Time available | Time constrained |
| Precedent | None | Well-established |
| Complexity | Can build test article | Too complex to test |

---

## Compliance Status Summary

### By MOC Type
| MOC Type | Count | Complete | In Progress | Not Started |
|----------|-------|----------|-------------|-------------|
| Test (T) | 9 | 0 | 0 | 9 |
| Analysis (A) | 7 | 0 | 2 | 5 |
| Inspection (I) | 4 | 0 | 1 | 3 |
| Demonstration (D) | 3 | 0 | 0 | 3 |
| Design Feature (DF) | 1 | 1 | 0 | 0 |
| **Total** | **24** | **1** | **3** | **20** |

**Overall Compliance:** 4% complete (1/24 items)

### Critical Path Items (Not Started)
1. GVT (CS25.629) - CRITICAL RISK
2. FEA validation (CS25.301, 365, 571) - BLOCKER
3. Ultimate test (CS25.305) - Required for certification
4. Fatigue test (CS25.571) - Longest duration item

---

## Next Steps

### Immediate (2026 Q1)
1. [ ] Contract professional FEA services
2. [ ] Engage DER for MOC review
3. [ ] Finalize test plan for all test-based MOC

### Short-term (2026 Q2-Q3)
1. [ ] Complete FEA analysis (MOC for CS25.301, 365, 571)
2. [ ] DER approval of test plans
3. [ ] Build prototype for testing

### Medium-term (2027)
1. [ ] Execute all test-based MOC
2. [ ] Complete all analysis-based MOC
3. [ ] Compile compliance documentation

### Long-term (2028)
1. [ ] DER sign-off on all MOC
2. [ ] Authority review and acceptance
3. [ ] TC issuance

---

**Document Control**

**Revision:** 1.0  
**Approved:** Pending  
**Next Review:** 2026-Q1  
**Owner:** AMPEL360 Certification Manager

---

**Part of:** AMPEL360 OPT-IN Framework - ATA 52-10-01 Certification Package
