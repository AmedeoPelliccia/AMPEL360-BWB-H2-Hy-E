# Prototype Development Strategy
## Door L1 Forward

**Document:** AMPEL360-52-10-01-PROTO-PLAN  
**Status:** CONCEPTUAL  
**Date:** 2025-11-03

### 1. OBJECTIVES

#### Primary Goals
1. **Validate AI predictions** (±30-50% uncertainty)
2. **Measure damping ratio** (Mode 1 resonance risk)
3. **Prove structural capability** (17 psi ultimate)
4. **Demonstrate manufacturability**
5. **Verify interfaces**

#### Critical Unknowns
- Actual stress vs. AI predictions
- Natural frequency and damping
- Manufacturing defects impact
- Assembly tolerance buildup

### 2. BUILD APPROACH

#### 2.1 Progressive Complexity
```
Coupons → Subcomponents → Full Panel → Complete Door

Risk: LOW ───────────────────────→ HIGH
Cost: $5k ───────────────────────→ $500k
Time: 1 week ────────────────────→ 6 months
```

#### 2.2 Test-Fail-Fix Philosophy
- Expect failures in early articles
- Learn from each iteration
- Document all findings
- Update analysis models

### 3. PROTOTYPE DEFINITIONS

#### PROTO-001: Engineering Development Unit (EDU)

**Purpose:** Structural and dynamic validation

**Configuration:**
- Full-size door panel (1120 × 1880mm)
- Composite sandwich construction
- Simplified frame (aluminum angles)
- Manual latches (non-flight)
- No slide or interior finish

**Key Tests:**
- **GVT (CRITICAL)** - Damping measurement
- Static ultimate (17 psi)
- Proof pressure (12.75 psi)
- Initial fatigue (1000 cycles)

**Success Criteria:**
- Mode 1 damping ≥3% → Proceed
- Mode 1 damping <3% → REDESIGN
- Ultimate strength demonstrated
- Correlation with AI predictions

**Cost Estimate:** $350,000

#### PROTO-002: Qualification Unit

**Purpose:** Certification compliance

**Configuration:**
- Flight-representative design
- Full mechanism integration
- Production tooling
- All interfaces verified

**Test Campaign:**
- Full fatigue (120,000 cycles)
- Environmental testing
- Lightning strike
- Fire resistance
- All certification tests

**Cost Estimate:** $500,000

#### PROTO-003: Flight Article

**Purpose:** First flight-worthy door

**Configuration:**
- Production design
- Flight systems integration
- Full certification
- Flight test instrumentation

**Cost Estimate:** $600,000

### 4. MANUFACTURING DEVELOPMENT

#### Tooling Requirements

**Cure Mold:**
- Material: Invar or steel
- Surface: 400mm × 2000mm × 1200mm
- Tolerance: ±0.5mm profile
- Cost: $250,000
- Lead time: 16 weeks

**Assembly Fixtures:**
- Frame alignment jig
- Latch drilling template
- Hinge installation fixture
- Cost: $75,000

#### Process Development

**Hand Layup (Initial):**
- Lower cost for prototype
- Higher labor hours
- More variability
- Suitable for 1-5 units

**AFP (Production):**
- Requires equipment access
- Better quality control
- Lower unit cost >10 units
- Not available initially

### 5. CRITICAL PATH SCHEDULE

```
2025 Q4: Funding pursuit (ACTIVE)
2026 Q1: FEA validation + Design freeze
2026 Q2: Tooling fabrication
        Material procurement
        Coupon testing
2026 Q3: PROTO-001 manufacture
        GVT testing (GO/NO-GO)
2026 Q4: Structural testing
        PROTO-002 start
2027 Q1: Qualification testing
2027 Q2: PROTO-003 flight article
2027 Q3: Ground tests complete
2027 Q4: First flight
```

### 6. RISK MITIGATION

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Mode 1 resonance | HIGH | Redesign | Early GVT on coupons |
| Material properties | MEDIUM | Reanalysis | Coupon testing first |
| Manufacturing defects | MEDIUM | Scrap part | Process trials |
| Interface mismatch | LOW | Rework | 3D scanning |
| Cost overrun | HIGH | Delay | Phased approach |

### 7. DECISION GATES

**Gate 1: Post-FEA** (Q1 2026)
- Confirm design feasible
- Release for prototype

**Gate 2: Post-GVT** (Q3 2026) **CRITICAL**
- Damping acceptable?
- Proceed or redesign

**Gate 3: Post-Static** (Q4 2026)
- Structure adequate?
- Release for qualification

**Gate 4: Post-Qual** (Q2 2027)
- All requirements met?
- Release for flight

### 8. SUCCESS METRICS

**Technical:**
- Mode 1 damping ≥3%
- Ultimate strength ≥17 psi
- Fatigue life >120,000 cycles
- Weight <45 kg

**Schedule:**
- First flight Q4 2027
- No more than 2 major redesigns
- Decision gates met on schedule

**Cost:**
- Total prototype cost <$2.5M
- No cost overrun >20%

---

**Approvals Required:**
- Chief Engineer: [ ]
- Program Manager: [ ]
- Manufacturing Lead: [ ]

**Document Control:** AMPEL360-52-10-01-PROTO-STRAT-001  
**Revision:** A  
**Date:** 2025-11-03
