# Production Risk Assessment - Door L1 Forward

**Document:** AMPEL360-52-10-01-RISK  
**Date:** 2025-11-03  
**Status:** DRAFT

---

## Risk Assessment Matrix

| Risk ID | Risk Description | Category | Impact | Probability | Risk Score | Mitigation Strategy | Owner |
|---------|------------------|----------|--------|-------------|------------|---------------------|-------|
| PROD-001 | Design not validated (AI analysis only) | Technical | HIGH | High | 25 | Professional FEA, prototype testing | Engineering |
| PROD-002 | Autoclave service unavailable | Supply Chain | HIGH | Medium | 20 | Backup provider contract | Procurement |
| PROD-003 | Skilled labor shortage | Workforce | MEDIUM | High | 20 | Early recruitment, training program | HR |
| PROD-004 | Material supply disruption | Supply Chain | HIGH | Low | 15 | Safety stock, dual sourcing | Procurement |
| PROD-005 | Tooling delivery delays | Schedule | HIGH | Medium | 20 | Early procurement, expediting | Tooling |
| PROD-006 | Quality issues (high scrap) | Quality | MEDIUM | High | 20 | Rigorous process control, PFMEA | Quality |
| PROD-007 | Funding not secured | Financial | HIGH | Medium | 20 | Phased investment, business case | Finance |
| PROD-008 | Facility not available | Infrastructure | HIGH | Medium | 20 | Early site selection, negotiations | Facilities |
| PROD-009 | Design changes during production | Technical | HIGH | Medium | 20 | Design freeze discipline, ECO process | Engineering |
| PROD-010 | Certification delays | Regulatory | MEDIUM | Medium | 15 | Early EASA engagement, planning | Certification |
| PROD-011 | Supplier quality issues | Quality | MEDIUM | Medium | 15 | Supplier audits, quality agreements | Quality |
| PROD-012 | Tool damage/failure | Operations | HIGH | Low | 15 | Spare tooling, maintenance program | Manufacturing |
| PROD-013 | NDT capability inadequate | Quality | MEDIUM | Medium | 15 | Service provider qualification | Quality |
| PROD-014 | Environmental compliance | Regulatory | LOW | Low | 5 | Compliance assessment, permits | EHS |
| PROD-015 | Safety incidents | Safety | MEDIUM | Low | 10 | Safety training, PPE, procedures | Safety |

**Risk Scoring:**
- Impact: LOW=1, MEDIUM=2, HIGH=3, CRITICAL=4
- Probability: Low=1, Medium=2, High=3, Very High=4
- Risk Score = Impact × Probability × 2.5

---

## High Priority Risks (Score ≥20)

### PROD-001: Design Not Validated
**Current Status:** AI-based analysis only, no professional FEA  
**Impact:** HIGH - Could invalidate entire production plan  
**Probability:** High - Known gap in design validation

**Mitigation Plan:**
1. Commission professional structural FEA analysis
2. Validate material properties with physical testing
3. Build and test prototype articles
4. Conduct Ground Vibration Test (GVT) to verify damping ≥3%
5. Design freeze only after validation complete

**Timeline:** Q1-Q2 2026  
**Cost:** $150k (analysis + testing)  
**Residual Risk:** Medium (professional analysis reduces but doesn't eliminate)

---

### PROD-002: Autoclave Service Unavailable
**Current Status:** Negotiating with ACT Aerospace, no contract  
**Impact:** HIGH - Stops production completely  
**Probability:** Medium - Single source dependency

**Mitigation Plan:**
1. Execute service contract with ACT Aerospace (primary)
2. Identify and qualify backup autoclave provider
3. Maintain 2-week scheduling buffer
4. Consider mobile autoclave rental for emergencies
5. Long-term: Evaluate internal autoclave at higher rates

**Timeline:** Immediate  
**Cost:** Service contracts, qualification costs  
**Residual Risk:** Low (with backup provider)

---

### PROD-003: Skilled Labor Shortage
**Current Status:** Zero workforce, competitive market  
**Impact:** MEDIUM - Delays ramp-up, quality issues  
**Probability:** High - Composite skills scarce

**Mitigation Plan:**
1. Begin recruitment 6 months before production start
2. Offer competitive compensation packages
3. Develop comprehensive training program
4. Partner with technical schools
5. Cross-train workforce for flexibility
6. Retain experienced technicians with incentives

**Timeline:** Q3 2026 recruitment start  
**Cost:** Recruiting, training, retention bonuses  
**Residual Risk:** Medium (market remains competitive)

---

### PROD-005: Tooling Delivery Delays
**Current Status:** No tooling ordered, 16-week lead times  
**Impact:** HIGH - Delays production start  
**Probability:** Medium - Complex, specialized tooling

**Mitigation Plan:**
1. Finalize tooling designs by Q1 2026
2. Place orders immediately upon design approval
3. Weekly progress reviews with suppliers
4. Expediting fees in contracts if needed
5. Partial deliveries to accelerate validation
6. Backup suppliers identified for critical items

**Timeline:** Order Q2 2026 for Q4 delivery  
**Cost:** Tooling cost + expediting fees  
**Residual Risk:** Low (with early action and monitoring)

---

### PROD-006: Quality Issues
**Current Status:** No processes validated, conceptual only  
**Impact:** MEDIUM - High scrap, rework costs  
**Probability:** High - New processes, complex part

**Mitigation Plan:**
1. Develop comprehensive PFMEA (complete)
2. Implement robust control plans
3. Statistical Process Control (SPC) on critical parameters
4. First Article Inspection rigorous
5. Continuous process improvement
6. Supplier quality partnerships
7. Training and certification programs

**Timeline:** Ongoing from prototype phase  
**Cost:** Quality system implementation  
**Residual Risk:** Medium (inherent in new production)

---

### PROD-007: Funding Not Secured
**Current Status:** No budget approved, conceptual only  
**Impact:** HIGH - Cannot proceed with any activity  
**Probability:** Medium - Dependent on business case

**Mitigation Plan:**
1. Develop detailed business case with ROI analysis
2. Phased investment approach to reduce risk
3. Seek non-dilutive funding (grants, partnerships)
4. Milestone-based funding releases
5. Alternative funding sources identified

**Timeline:** Q4 2025 - Q1 2026  
**Cost:** $600k Phase 1, $1.1M total through FRP  
**Residual Risk:** High (external dependency)

---

### PROD-008: Facility Not Available
**Current Status:** No facility identified  
**Impact:** HIGH - Cannot start production  
**Probability:** Medium - Specific requirements (clean room)

**Mitigation Plan:**
1. Survey potential facilities immediately
2. Engage real estate brokers specializing in industrial
3. Consider build-to-suit if necessary
4. Negotiate lease with expansion options
5. Plan for 6-month lead time for clean room setup
6. Backup location identified

**Timeline:** Select by Q1 2026, ready Q3 2026  
**Cost:** Lease + tenant improvements  
**Residual Risk:** Low (with early action)

---

### PROD-009: Design Changes
**Current Status:** Design not frozen, likely changes  
**Impact:** HIGH - Tooling obsolescence, rework  
**Probability:** Medium - Early in development

**Mitigation Plan:**
1. Implement formal design freeze process
2. Engineering Change Order (ECO) discipline
3. Cost/schedule impact assessment for all changes
4. Change review board approval required
5. Modular tooling design where possible
6. Contractual change clauses with suppliers

**Timeline:** Design freeze target Q2 2026  
**Cost:** ECO process, potential rework  
**Residual Risk:** Medium (some changes inevitable)

---

## Medium Priority Risks (Score 10-19)

### PROD-010: Certification Delays
- Early engagement with EASA
- Parallel activities where possible
- Experienced certification team
- Documented compliance from design phase

### PROD-011: Supplier Quality
- Supplier audits and ratings
- Quality agreements and KPIs
- Regular performance reviews
- Corrective action processes

### PROD-012: Tool Damage
- Preventive maintenance program
- Spare critical tooling elements
- Tool usage tracking
- Repair vendor relationships

### PROD-013: NDT Capability
- Qualify multiple NDT service providers
- Capability studies on test articles
- Acceptance criteria validation
- Equipment calibration programs

### PROD-015: Safety Incidents
- Comprehensive safety training
- PPE enforcement
- Chemical handling procedures
- Ergonomic assessments

---

## Risk Monitoring and Review

### Monitoring Frequency
- **High risks (≥20):** Weekly review
- **Medium risks (10-19):** Monthly review
- **Low risks (<10):** Quarterly review

### Escalation Triggers
- Risk score increases by ≥5 points
- Mitigation plan not on track
- New information changes assessment
- Risk materializes

### Review Forums
- Production Planning Meetings (weekly)
- Program Review Boards (monthly)
- Executive Reviews (quarterly)

---

## Risk Contingency Budget

| Risk Category | Contingency ($k) | Basis |
|---------------|------------------|-------|
| Technical/Design | 100 | 15% of engineering costs |
| Schedule delays | 150 | 3-month operating costs |
| Quality/rework | 75 | 10% of first 10 units |
| Supplier issues | 50 | Alternate sourcing premium |
| **Total** | **375** | **~6% of Phase 1 investment** |

---

## Success Criteria

Production is considered low-risk when:
- [ ] Design validated by professional analysis
- [ ] Prototype successfully built and tested
- [ ] All critical suppliers qualified
- [ ] Tooling delivered and validated
- [ ] Facility operational with clean room certified
- [ ] Workforce recruited and trained
- [ ] First article passes all inspections
- [ ] Quality system established
- [ ] Funding secured for full ramp

**Target Date:** Q4 2027 (beginning of low-rate production)

---

**Document Control:**
- **Version:** Draft 1.0
- **Next Review:** Quarterly or upon significant change
- **Owner:** Production Planning Manager
