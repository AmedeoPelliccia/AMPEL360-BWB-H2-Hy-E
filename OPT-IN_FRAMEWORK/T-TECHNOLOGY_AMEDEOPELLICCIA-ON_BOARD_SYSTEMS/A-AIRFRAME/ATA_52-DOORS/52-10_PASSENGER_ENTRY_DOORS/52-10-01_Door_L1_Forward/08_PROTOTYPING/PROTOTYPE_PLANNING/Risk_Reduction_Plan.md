# Risk Reduction Plan
## Door L1 Forward Prototype Program

**Document:** AMPEL360-52-10-01-RISK-PLAN  
**Status:** ACTIVE  
**Date:** 2025-11-03

## Executive Summary

This plan identifies technical risks in the Door L1 Forward prototype development and defines mitigation strategies. The highest priority risk is **Mode 1 resonance**, which could require a complete redesign if not properly addressed.

---

## RISK MATRIX

### Risk Severity Scale
- **CRITICAL:** Program showstopper, requires major redesign
- **HIGH:** Significant impact, may cause delays >3 months
- **MEDIUM:** Moderate impact, manageable with replanning
- **LOW:** Minor impact, can be resolved with local fixes

### Probability Scale
- **VERY HIGH:** >70% likelihood
- **HIGH:** 40-70% likelihood
- **MEDIUM:** 20-40% likelihood
- **LOW:** <20% likelihood

---

## TOP RISKS (Priority Order)

### RISK 001: Mode 1 Resonance at 25 Hz
**Category:** Structural Dynamics  
**Probability:** HIGH (60%)  
**Impact:** CRITICAL  
**Risk Score:** 10/10

**Description:**
AI analysis predicts Mode 1 at 25.13 Hz with only 0.8% damping. This frequency is within the engine excitation range and could cause:
- Structural fatigue
- Passenger discomfort
- Certification failure

**Root Cause:**
- Large, flat composite panel
- Limited inherent damping in CFRP
- No damping features in current design

**Mitigation Strategy:**

**PROACTIVE (Before PROTO-001):**
1. FEA modal analysis to confirm AI predictions
2. Damping material investigation (VEM, constrained layer)
3. Design modifications:
   - Internal stiffeners
   - Damping patches
   - Honeycomb core optimization

**REACTIVE (During GVT):**
1. Measure actual damping ratio
2. If <3%:
   - Add damping treatments
   - Redesign internal structure
   - Consider active damping
3. Retest before proceeding

**Success Metric:** Mode 1 damping ≥3%

**Budget Reserve:** $100,000 for redesign

---

### RISK 002: Material Property Uncertainty
**Category:** Materials  
**Probability:** MEDIUM (40%)  
**Impact:** HIGH  
**Risk Score:** 7/10

**Description:**
AI predictions have ±30-50% uncertainty. Actual material properties may differ, causing:
- Structural inadequacy
- Weight increase
- Cost overrun

**Root Cause:**
- No physical testing yet
- AI trained on generic data
- Specific layup/cure not validated

**Mitigation Strategy:**

**PROACTIVE:**
1. **DEM-001 coupon testing (MANDATORY)**
   - Test before PROTO-001
   - Budget: $11,000
   - Duration: 4 weeks

2. Material selection review
   - Compare alternatives (M21E vs. M21)
   - Supplier qualification

3. Conservative design factors
   - Use AI lower bounds
   - Safety factor 1.5 until validated

**REACTIVE:**
1. If properties <50% of AI predictions:
   - Structural redesign
   - Thicker laminates
   - Different material system

**Success Metric:** Properties within ±30% of AI predictions

**Budget Reserve:** $50,000 for material changes

---

### RISK 003: Manufacturing Defects
**Category:** Manufacturing  
**Probability:** MEDIUM (50%)  
**Impact:** MEDIUM  
**Risk Score:** 6/10

**Description:**
Hand layup process may introduce:
- Wrinkles and bridging
- Void content >5%
- Dimensional tolerance issues
- Bond line porosity

**Root Cause:**
- Manual process variability
- No AFP equipment available
- Complex geometry
- Tight tolerances

**Mitigation Strategy:**

**PROACTIVE:**
1. **DEM-002 corner section trial**
   - Prove process before full door
   - Develop layup procedures
   - Train technicians

2. Process development
   - Detailed layup procedures
   - Photo documentation at each step
   - Debulking schedule optimization

3. Quality controls
   - In-process inspections
   - NDT after cure (C-scan)
   - Dimensional CMM checks

**REACTIVE:**
1. If defects found:
   - Scrap and rebuild (budget 1 extra unit)
   - Revise procedures
   - Additional training

**Success Metric:** <5% void content, no wrinkles

**Budget Reserve:** $75,000 for scrap/rework

---

### RISK 004: Tooling Lead Time
**Category:** Schedule  
**Probability:** MEDIUM (40%)  
**Impact:** MEDIUM  
**Risk Score:** 5/10

**Description:**
Cure mold fabrication is on critical path:
- 16-week lead time
- Single source supplier
- Payment terms may delay start
- Changes require remachining

**Root Cause:**
- Complex mold geometry
- Tight tolerance requirements
- Long lead time tooling steel

**Mitigation Strategy:**

**PROACTIVE:**
1. Early mold design (Q1 2026)
2. Supplier pre-qualification
3. Split mold into sections
4. Consider interim foam tools for DEM units

**REACTIVE:**
1. If delayed:
   - Fast-track foam tool for initial tests
   - Parallel path development
   - Adjust schedule (accept delay)

**Success Metric:** Mold delivered on schedule

**Budget Reserve:** $25,000 for expedited delivery

---

### RISK 005: Interface Mismatches
**Category:** Integration  
**Probability:** LOW (20%)  
**Impact:** MEDIUM  
**Risk Score:** 3/10

**Description:**
Door interfaces with:
- Fuselage structure
- Slide/raft system
- Electrical/pneumatic systems
- Interior trim

Mismatches could cause:
- Installation delays
- Rework costs
- Performance issues

**Root Cause:**
- Parallel development of systems
- Tolerance stackup
- Design changes in other areas

**Mitigation Strategy:**

**PROACTIVE:**
1. Interface control documents (ICDs)
2. 3D CAD assembly verification
3. Early mockup (SM-002)
4. Coordination meetings with other teams

**REACTIVE:**
1. If mismatch found:
   - Engineering change order
   - Rework affected parts
   - Update ICDs

**Success Metric:** First-time fit on aircraft

**Budget Reserve:** $30,000 for interface fixes

---

### RISK 006: Funding Delays
**Category:** Program  
**Probability:** MEDIUM (50%)  
**Impact:** HIGH  
**Risk Score:** 7/10

**Description:**
$2M funding requirement may be delayed:
- Budget approval process
- Priority conflicts
- Economic conditions

**Root Cause:**
- Large upfront investment
- Uncertain return timeline
- Competing programs

**Mitigation Strategy:**

**PROACTIVE:**
1. Phased funding approach
   - Phase 1: $61k (demonstrators)
   - Phase 2: $530k (engineering unit)
   - Phase 3+: $1.4M (qual and flight)

2. Multiple funding sources
   - Internal R&D budget
   - Government grants (SBIR/STTR)
   - Industry partnerships

3. Strong business case
   - ROI analysis
   - Technology value
   - Competitive advantage

**REACTIVE:**
1. If funding delayed:
   - Pause program at phase boundaries
   - Maintain design team (core only)
   - Re-baseline schedule

**Success Metric:** Funding secured by Q1 2026

**Budget Reserve:** N/A (external issue)

---

## RISK REDUCTION SCHEDULE

### Q4 2025 - Funding Phase
- [ ] Secure Phase 1 funding ($61k minimum)
- [ ] Begin FEA analysis
- [ ] Supplier qualification

### Q1 2026 - Analysis Phase
- [ ] Complete FEA modal analysis
- [ ] Finalize damping strategy
- [ ] Design freeze with risk mitigations

### Q2 2026 - Demonstrator Phase
- [ ] DEM-001: Material validation (RISK 002)
- [ ] DEM-002: Manufacturing trial (RISK 003)
- [ ] DEM-003: Latch function
- [ ] DEM-004: Seal testing

### Q3 2026 - Critical Test Phase
- [ ] PROTO-001 manufacture
- [ ] **GVT damping test (RISK 001 - GO/NO-GO)**
- [ ] Static ultimate test

### Q4 2026 - Qualification Phase
- [ ] Proceed if risks retired
- [ ] PROTO-002 start
- [ ] Monitor for new risks

---

## RISK RETIREMENT CRITERIA

| Risk ID | Retirement Event | Target Date |
|---------|------------------|-------------|
| 001 | GVT shows damping ≥3% | Q3 2026 |
| 002 | Coupon tests validate properties | Q2 2026 |
| 003 | DEM-002 shows quality manufacturing | Q2 2026 |
| 004 | Mold delivered on time | Q2 2026 |
| 005 | Mockup fits aircraft | Q3 2026 |
| 006 | Funding secured | Q1 2026 |

---

## CONTINGENCY BUDGET

| Risk Category | Reserve | Rationale |
|---------------|---------|-----------|
| Redesign (001) | $100,000 | Major structural changes |
| Materials (002) | $50,000 | Material system change |
| Scrap/Rework (003) | $75,000 | 1 additional unit |
| Tooling (004) | $25,000 | Expedited delivery |
| Interfaces (005) | $30,000 | Rework and modifications |
| **TOTAL** | **$280,000** | **14% of base budget** |

**Recommended Total Contingency:** 20% = $400,000

---

## MONITORING AND CONTROL

### Weekly Risk Reviews
- Program manager and chief engineer
- Update risk scores
- Track mitigation actions

### Monthly Risk Reports
- Status to stakeholders
- Trigger points for escalation
- Budget and schedule impacts

### Decision Gates
- Gate reviews include risk assessment
- GO/NO-GO based on risk levels
- Document lessons learned

---

**Document Control:** AMPEL360-52-10-01-RISK-PLAN-001  
**Revision:** A  
**Date:** 2025-11-03  
**Next Review:** 2026-01-01
