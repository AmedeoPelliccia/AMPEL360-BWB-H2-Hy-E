# Build Phases
## Door L1 Forward Prototype Development

**Document:** AMPEL360-52-10-01-BUILD-PHASES  
**Status:** PLANNING  
**Date:** 2025-11-03

## Overview

The prototype development is divided into four distinct build phases, each with specific objectives, deliverables, and success criteria.

---

## PHASE 1: RISK REDUCTION (Q4 2025 - Q2 2026)

### Objectives
- Validate material properties against AI predictions
- Prove manufacturing processes
- Reduce technical uncertainty before major investment

### Activities

#### 1.1 Material Coupon Testing (DEM-001)
**Timeline:** 4 weeks  
**Budget:** $11,000

- CFRP mechanical property testing
- Core shear and compression testing
- Face/core bond strength validation
- Process parameter verification

**Success Criteria:**
- Properties within ±30% of AI predictions
- No manufacturing defects >5% voids
- Adequate bond strength (>25 MPa)

#### 1.2 Corner Section Trial (DEM-002)
**Timeline:** 6 weeks  
**Budget:** $15,000

- Complex geometry layup
- Corner radius forming
- Edge band integration
- Tool pulling verification

**Success Criteria:**
- No wrinkles or bridging
- Dimensional tolerance ±2mm
- Clean corner radius

#### 1.3 Latch Mechanism Demo (DEM-003)
**Timeline:** 8 weeks  
**Budget:** $25,000

- Latch kinematics validation
- Load path verification
- Actuation force measurement
- Emergency release function

**Success Criteria:**
- Latch engagement verified
- Forces within human capability
- Emergency release <5 seconds

#### 1.4 Seal Section Test (DEM-004)
**Timeline:** 6 weeks  
**Budget:** $10,000

- Seal compression testing
- Leak rate measurement
- Durability cycling (1000 cycles)
- Temperature effects

**Success Criteria:**
- Leak rate <0.1 CFM at 8.6 psi
- No permanent seal set
- Function -40°C to +70°C

### Phase 1 Deliverables
- [ ] Coupon test report with validated properties
- [ ] Corner manufacturing procedure
- [ ] Latch mechanism function demonstration
- [ ] Seal qualification data
- [ ] Lessons learned log

### Phase 1 Decision Gate
**GO Criteria:**
- All demonstrators meet success criteria
- No showstopper technical issues identified
- Funding for Phase 2 secured

**NO-GO Actions:**
- Redesign required elements
- Re-run failed demonstrations
- Escalate to program management

---

## PHASE 2: ENGINEERING PROTOTYPE (Q2 2026 - Q3 2026)

### Objectives
- Build full-scale engineering development unit
- Validate structural analysis through testing
- **CRITICAL: Measure modal damping ratio**

### Activities

#### 2.1 Tooling Fabrication
**Timeline:** 16 weeks  
**Budget:** $325,000

- Cure mold design and fabrication
- Assembly fixture design
- Trim templates
- Quality inspection tools

#### 2.2 PROTO-001 Manufacturing
**Timeline:** 12 weeks  
**Budget:** $150,000

- Face sheet layup (2 panels)
- Core bonding and assembly
- Frame fabrication and integration
- Simplified latch installation
- NDT inspection (C-scan)

#### 2.3 Ground Vibration Test (GVT)
**Timeline:** 2 weeks  
**Budget:** $30,000

- Modal survey (0-100 Hz)
- Frequency response functions
- **Mode 1 damping measurement**
- Mode shape visualization

**CRITICAL GO/NO-GO:**
- If damping ≥3% → Proceed
- If damping <3% → Redesign required

#### 2.4 Static Ultimate Test
**Timeline:** 1 week  
**Budget:** $25,000

- 17 psi ultimate pressure load
- Strain gauge instrumentation
- Failure mode identification
- Correlation with FEA

### Phase 2 Deliverables
- [ ] PROTO-001 engineering unit
- [ ] GVT test report with damping data
- [ ] Static test report
- [ ] Updated FEA correlation
- [ ] Manufacturing lessons learned
- [ ] GO/NO-GO decision for Phase 3

### Phase 2 Decision Gate
**GO Criteria:**
- Mode 1 damping ≥3%
- Ultimate strength achieved
- Good FEA correlation (±20%)
- Manufacturing feasible

**NO-GO Actions:**
- Major redesign if damping <3%
- Structural redesign if strength inadequate
- Process improvement if manufacturing issues

---

## PHASE 3: QUALIFICATION ARTICLE (Q4 2026 - Q2 2027)

### Objectives
- Build flight-representative qualification unit
- Complete certification test campaign
- Demonstrate compliance with requirements

### Activities

#### 3.1 PROTO-002 Manufacturing
**Timeline:** 16 weeks  
**Budget:** $300,000

- Production-representative build
- Full mechanism integration
- All interfaces verified
- Complete systems integration

#### 3.2 Certification Testing
**Timeline:** 20 weeks  
**Budget:** $200,000

**Test Campaign:**
- Proof pressure (12.75 psi)
- Fatigue (120,000 cycles)
- Ultimate pressure (17 psi)
- Environmental (-55°C to +70°C)
- Lightning strike
- Fire resistance
- Impact damage tolerance

### Phase 3 Deliverables
- [ ] PROTO-002 qualification unit
- [ ] Complete certification test reports
- [ ] Type Certificate Data Sheet (TCDS) support data
- [ ] Manufacturing process specifications
- [ ] Quality control procedures

### Phase 3 Decision Gate
**GO Criteria:**
- All certification tests passed
- No open non-conformances
- Manufacturing released to production
- FAA DER approval (if required)

---

## PHASE 4: FLIGHT ARTICLE (Q2 2027 - Q4 2027)

### Objectives
- Build first flight-worthy door
- Integrate with aircraft systems
- Complete ground and flight testing

### Activities

#### 4.1 PROTO-003 Manufacturing
**Timeline:** 14 weeks  
**Budget:** $400,000

- Flight production build
- Complete systems integration
- Flight test instrumentation
- Final acceptance testing

#### 4.2 Ground Integration
**Timeline:** 8 weeks  
**Budget:** $100,000

- Aircraft installation
- Systems checkout
- Ground functional tests
- Safety of flight release

#### 4.3 Flight Test
**Timeline:** 8 weeks  
**Budget:** $100,000

- Flight envelope expansion
- Performance validation
- Vibration and loads measurement
- Certification flight tests

### Phase 4 Deliverables
- [ ] PROTO-003 flight article
- [ ] Installation instructions
- [ ] Ground test reports
- [ ] Flight test reports
- [ ] Final certification data package

### Phase 4 Decision Gate
**GO Criteria:**
- Successful first flight
- All flight test objectives met
- Production design released
- Type certificate issued (if required)

---

## Build Phase Summary

| Phase | Duration | Cost | Key Milestone |
|-------|----------|------|---------------|
| Phase 1 | 6 months | $61k | Risk reduction |
| Phase 2 | 6 months | $530k | GVT GO/NO-GO |
| Phase 3 | 8 months | $500k | Certification |
| Phase 4 | 6 months | $600k | First flight |
| **TOTAL** | **26 months** | **$1.69M** | **Flight test complete** |

**Additional costs (not in phases):**
- FEA analysis: $30k
- Program management: $200k
- Contingency (20%): $340k
- **TOTAL PROJECT: $2.26M**

---

**Document Control:** AMPEL360-52-10-01-BUILD-PHASES-001  
**Revision:** A  
**Date:** 2025-11-03
