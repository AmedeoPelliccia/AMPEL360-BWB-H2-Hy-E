# Critical Path Items for Certification

**Document:** AMPEL360-52-10-01-CRITICAL-PATH  
**Status:** ACTIVE MONITORING  
**Date:** 2025-11-03

## Overview

This document identifies the critical path items that gate certification progress for Door L1 Forward. These items have **zero float** in the schedule and any delay directly impacts the certification target date.

---

## 1. GVT - HIGHEST PRIORITY ⚠️

### Issue
Mode 1 resonance with engine frequency

### Current Status
- **Predicted Mode 1:** ~25-30 Hz (AI estimate, ±30% uncertainty)
- **Engine frequency:** 25 Hz at max continuous power
- **Required damping:** ζ ≥ 3% critical
- **Current damping:** Unknown (no test data)

### Risk Assessment
**CRITICAL RISK - GO/NO-GO FOR ENTIRE PROGRAM**

If GVT shows:
- ζ < 1%: **Major redesign required** (add damping, stiffen structure)
- ζ = 1-3%: **Minor modifications needed** (damping patches, tuned mass dampers)
- ζ ≥ 3%: **Proceed to certification** (acceptable damping)

### Timeline
- **Must complete:** 2027 Q1
- **Decision gate:** 2027-03-22
- **Cost:** $30,000
- **Duration:** 4 weeks (setup + execution + analysis)

### Dependencies
- Prototype fabrication complete
- Test instrumentation ready
- Modal analysis software validated
- DER witness arranged

### Mitigation Actions
1. **Early GVT:** Schedule as soon as prototype ready
2. **Backup plan:** Identify damping enhancement options now
3. **Modal analysis:** Improve FEA prediction to reduce uncertainty
4. **Expert review:** Engage aeroelastic specialist early

### Success Criteria
- [ ] Mode 1 identified and measured
- [ ] Damping ratio ζ ≥ 3%
- [ ] No coupling with engine frequency
- [ ] DER acceptance of results

---

## 2. FEA VALIDATION

### Issue
Currently AI-based analysis only; must be replaced with professional FEA

### Current Status
- **Analysis method:** AI predictions + hand calculations
- **Uncertainty:** ±30-50%
- **Authority acceptance:** NO - will be rejected
- **DER acceptance:** NO - cannot sign off

### Risk Assessment
**CRITICAL BLOCKER - CANNOT PROCEED WITHOUT**

### Timeline
- **Must complete:** 2026 Q1
- **Cost:** $150,000
- **Duration:** 3-5 months

### Required Actions
1. **Software acquisition:**
   - NASTRAN, ANSYS, or ABAQUS license
   - Hardware capable of large models
   - Training for engineers

2. **Model development:**
   - 3D FEM model of door assembly
   - Material properties validation
   - Boundary conditions definition
   - Mesh convergence study

3. **Analysis execution:**
   - Static stress analysis
   - Fatigue analysis
   - Damage tolerance analysis
   - Modal analysis (pre-GVT prediction)

4. **Validation:**
   - Compare with test data (when available)
   - DER review and approval
   - Documentation per AMC requirements

### Success Criteria
- [ ] Professional FEA software operational
- [ ] Model validated and approved
- [ ] All margins positive (MS > 0)
- [ ] DER acceptance of methodology

---

## 3. ULTIMATE STRENGTH TEST

### Requirement
CS25.305 - Strength and Deformation

### Load Condition
- **Ultimate pressure:** 17.0 psi (2.0 × relief pressure)
- **Test article:** Full-scale door assembly
- **Acceptance:** No failure or permanent deformation

### Current Status
- **Prediction:** AI estimate shows MS = +0.12 to +0.25
- **Uncertainty:** ±50%
- **Risk:** Marginal margins may not hold in test

### Timeline
- **Must complete:** 2027 Q2
- **Cost:** $25,000
- **Duration:** 2 weeks

### Dependencies
- Prototype fabrication complete
- FEA analysis validated and approved
- Test fixture designed and built
- DER witness scheduled

### Risk Mitigation
1. **Conservative design:** Ensure FEA margins > +0.25
2. **Proof test first:** Test at 1.5× limit (12.75 psi) before ultimate
3. **Instrumentation:** Extensive strain gages to validate FEA
4. **DER presence:** Mandatory for witness

### Success Criteria
- [ ] Withstand 17.0 psi without failure
- [ ] Strain measurements validate FEA
- [ ] No permanent deformation
- [ ] DER sign-off on test report

---

## 4. FATIGUE DEMONSTRATION

### Requirement
CS25.571 - Damage Tolerance and Fatigue Evaluation

### Test Parameters
- **Cycles:** 120,000 (2× service life of 60,000 flights)
- **Spectrum:** Pressurization + ground-air-ground + door operations
- **Duration:** 6 months continuous testing
- **Acceptance:** No cracking or failure

### Current Status
- **Analysis:** S-N curve based on literature (not validated)
- **Risk:** Long duration test, expensive, no room for retest

### Timeline
- **Must complete:** 2027 Q3
- **Cost:** $150,000
- **Duration:** 6 months

### Dependencies
- Fatigue test article fabricated
- Test rig designed and commissioned
- Load spectrum validated
- Inspection intervals defined

### Risk Mitigation
1. **Phased approach:** Inspect every 20,000 cycles
2. **NDI capability:** Ready to detect cracks early
3. **Backup article:** Consider second test article
4. **Expert review:** Fatigue specialist to validate spectrum

### Success Criteria
- [ ] Complete 120,000 cycles without failure
- [ ] No cracks > 0.05 inches at final inspection
- [ ] Inspection data supports damage tolerance analysis
- [ ] DER acceptance of results

---

## 5. DAMAGE TOLERANCE

### Requirement
CS25.571 - Damage Tolerance and Fatigue Evaluation

### Test Scenario
- **Damage:** 50mm (2-inch) through-thickness hole
- **Location:** Critical stress location from FEA
- **Load:** Ultimate pressure (17.0 psi)
- **Acceptance:** Withstand ultimate with damage (residual strength)

### Current Status
- **Prediction:** AI estimate shows MS = +0.05 (MARGINAL)
- **Uncertainty:** ±50%
- **Risk:** May fail damage tolerance requirement

### Timeline
- **Must complete:** 2027 Q3
- **Cost:** $30,000
- **Duration:** 1 month

### Dependencies
- Fatigue test complete (to establish inspection intervals)
- FEA damage tolerance analysis validated
- Test article prepared with simulated damage

### Risk Mitigation
1. **Design improvement:** Consider crack stoppers or thicker skin
2. **Repair analysis:** Validate repair capability
3. **Multiple damage scenarios:** Test additional critical locations
4. **Conservative approach:** Use measured material properties (not handbook)

### Success Criteria
- [ ] Withstand ultimate with 50mm damage
- [ ] Validate slow crack growth prediction
- [ ] Establish inspection thresholds
- [ ] DER acceptance of approach

---

## 6. DER ENGAGEMENT

### Issue
No DER currently engaged; required for all certification activities

### Current Status
- **DER identified:** NO
- **DER engaged:** NO
- **Contract in place:** NO
- **Risk:** Cannot proceed to testing without DER plan approval

### Timeline
- **Must complete:** 2026 Q2
- **Cost:** $75,000
- **Duration:** Ongoing through TC

### Required Actions
1. **Selection:**
   - Identify structural DER with composite experience
   - Verify CS-25 authorization
   - Check availability for 2026-2028
   - Prefer BWB or novel configuration experience

2. **Engagement:**
   - Initial consultation on FEA and test plans
   - Formal contract for certification support
   - Schedule witness events
   - Define deliverables (8110-3 forms)

3. **Coordination:**
   - Review FEA methodology
   - Approve test plans
   - Witness critical tests (GVT, ultimate)
   - Review and sign reports

### Success Criteria
- [ ] DER selected and under contract by 2026 Q2
- [ ] Test plans approved by DER
- [ ] DER witness schedule confirmed
- [ ] 8110-3 forms signed by 2028 Q1

---

## 7. AUTHORITY COORDINATION

### Issue
No formal coordination with EASA established

### Current Status
- **Pre-application meeting:** Not scheduled
- **Certification basis:** Not agreed
- **Special conditions:** Not defined
- **Risk:** Late engagement may extend schedule

### Timeline
- **Pre-application meeting:** 2026 Q3
- **Certification basis agreement:** 2026 Q4
- **Ongoing coordination:** Through TC issuance

### Required Actions
1. **Pre-application meeting:**
   - Present BWB door concept
   - Discuss certification basis (CS-25 Amendment 27)
   - Identify potential special conditions
   - Agree on MOC for critical items

2. **Issue papers:**
   - Prepare issue papers for:
     - IP-01: Resonance with propulsion
     - IP-02: Composite damage tolerance
     - IP-03: Emergency egress from BWB
     - IP-04: Lightning protection validation

3. **Regular updates:**
   - Quarterly progress meetings
   - Test planning reviews
   - Test result presentations
   - Compliance documentation reviews

### Success Criteria
- [ ] Pre-application meeting complete by 2026 Q3
- [ ] Certification basis agreed
- [ ] Special conditions defined
- [ ] Authority engagement plan in place

---

## Critical Path Summary

```
FEA Validation (2026 Q1)
    ↓
Design Freeze (2026 Q3)
    ↓
Prototype Build (2026 Q4 - 2027 Q1)
    ↓
GVT - GO/NO-GO (2027 Q1) ← CRITICAL DECISION GATE
    ↓
Static Ultimate Test (2027 Q2)
    ↓
Fatigue Test (2027 Q2-Q3)
    ↓
Documentation (2027 Q4)
    ↓
TC Submission (2028 Q1)
    ↓
TC Approval (2028 Q2 - optimistic)
```

### Float Analysis
| Item | Float (weeks) | Impact if delayed |
|------|---------------|-------------------|
| FEA Validation | 0 | Delays everything |
| GVT | 0 | GO/NO-GO gate |
| Ultimate Test | 2 | Delays fatigue test |
| Fatigue Test | 0 | Longest duration item |
| DER Engagement | 4 | Can parallel with FEA |
| Authority Meeting | 8 | Can delay if needed |

---

## Monitoring and Control

### Weekly Reviews
- Critical path item status
- Risk register updates
- Schedule adherence
- Budget tracking

### Monthly Reports
- Progress to stakeholders
- Risk mitigation status
- Decision gate preparation
- Authority coordination

### Decision Gates
1. **FEA Validation** (2026 Q1) - Proceed to prototype?
2. **GVT Results** (2027 Q1) - Proceed to certification?
3. **Ultimate Test** (2027 Q2) - Design adequate?
4. **Fatigue Complete** (2027 Q3) - Submit for TC?

---

**Document Control**

**Revision:** 1.0  
**Approved:** Pending  
**Next Review:** Monthly  
**Owner:** AMPEL360 Program Manager

---

**Part of:** AMPEL360 OPT-IN Framework - ATA 52-10-01 Certification Package
