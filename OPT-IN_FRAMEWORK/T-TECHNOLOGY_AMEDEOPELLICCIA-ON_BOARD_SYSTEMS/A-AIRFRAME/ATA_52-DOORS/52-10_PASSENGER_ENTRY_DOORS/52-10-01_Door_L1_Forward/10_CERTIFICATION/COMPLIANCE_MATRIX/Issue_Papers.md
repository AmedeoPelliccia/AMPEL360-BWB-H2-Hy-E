# Issue Papers

**Document:** AMPEL360-52-10-01-ISSUE-PAPERS  
**Status:** DRAFT - READY FOR PRE-APPLICATION  
**Date:** 2025-11-03

## Overview

Issue papers are submitted to the certification authority early in the program to discuss novel or non-standard compliance approaches. They allow EASA to provide guidance before significant resources are committed.

Four issue papers have been drafted for Door L1 Forward certification.

---

## IP-01: Resonance with Propulsion System

### Issue Statement
Door L1 Forward Mode 1 natural frequency (~25-30 Hz based on AI estimate) may be close to engine operating frequency (25 Hz at max continuous power). This creates potential for resonance and flutter concerns per CS25.629.

### Background
- BWB configuration places door close to propulsion system
- Open-fan distributed propulsion generates periodic excitation
- Door is large, relatively flexible structure
- First bending mode predicted at 25-30 Hz (±30% uncertainty with AI analysis)
- Engine operates at up to 25 Hz at max continuous power

### Safety Concern
- Resonance could cause excessive vibration
- Fatigue cracking could develop
- Structural failure potential
- Flutter at high speed if damping insufficient

### Proposed Compliance Approach

**CS25.629 - Aeroelastic Stability**

#### Phase 1: FEA Modal Analysis (2026 Q1)
- Professional FEA software (NASTRAN/ANSYS)
- 3D model of door and surrounding structure
- Calculate natural frequencies and mode shapes
- Identify Mode 1 frequency (current AI estimate: 25-30 Hz)
- Estimate damping (conservative assumption: 2-3%)

#### Phase 2: GVT Validation (2027 Q1) - CRITICAL
- Ground Vibration Test of door on aircraft or representative structure
- Modal survey using accelerometers
- Impact or shaker excitation
- Extract frequencies, mode shapes, and damping ratios
- **Go/No-Go decision:** ζ ≥ 3% required for damping

#### Phase 3: Damping Enhancement (If Required)
If GVT shows inadequate damping:
- **Option 1:** Viscoelastic damping layers
- **Option 2:** Tuned mass dampers
- **Option 3:** Structural stiffening (frequency shift)
- Retest to validate improvement

#### Phase 4: Flutter Analysis
- Flutter analysis per CS25.629
- Show no flutter up to 1.2×VD (dive speed)
- Consider engine excitation in analysis
- Demonstrate adequate margins

### Success Criteria
- [ ] Mode 1 frequency characterized (FEA + GVT)
- [ ] Damping ratio ζ ≥ 3% demonstrated
- [ ] No resonance with engine frequency (>10% separation or adequate damping)
- [ ] No flutter up to 1.2×VD
- [ ] EASA acceptance of approach

### Schedule Impact
- FEA: 2026 Q1 (3 months)
- GVT: 2027 Q1 (1 month)
- If redesign needed: +6-12 months

### Cost Impact
- FEA: $50,000
- GVT: $30,000
- Damping enhancement (if needed): $75,000
- Retest (if needed): $30,000

### Authority Feedback Requested
1. Is GVT acceptable as primary validation method?
2. Is ζ ≥ 3% adequate damping criterion?
3. What separation from engine frequency is required if damping is marginal?
4. Is FEA prediction acceptable for initial design, with GVT validation?

**Status:** Draft ready for submission  
**Target Submission:** Pre-application meeting (2026 Q3)

---

## IP-02: Composite Damage Tolerance

### Issue Statement
Composite door skin as primary structure requires damage tolerance demonstration per CS25.571. Current AMC 20-29 provides guidance but composite doors have limited service experience.

### Background
- Door skin: Al-Li 2099-T83 with CFRP composite doubler
- Composite doublers act as primary load-carrying structure at critical locations
- Damage scenarios: Impact (tool drop, hail), manufacturing defects, service wear
- Limited service experience with composite primary structure on doors

### Safety Concern
- Composite damage may not be visible
- Damage growth could lead to catastrophic failure
- Inspection methods may miss internal damage
- Repair methods not fully validated

### Proposed Compliance Approach

**CS25.571 - Damage Tolerance and Fatigue Evaluation**

#### Building-Block Approach (AMC 20-29)

**Level 1: Coupon Tests**
- Material characterization
- Open-hole tension tests
- Compression after impact (CAI)
- Bearing strength
- Validate material allowables

**Level 2: Element Tests**
- Joint strength with damage
- Doubler bondline with defects
- Crack propagation in composite
- Environmental effects

**Level 3: Subcomponent Tests**
- Door section with 50mm damage
- Ultimate load with damage
- Residual strength validation
- Slow crack growth demonstration

**Level 4: Full-Scale Test**
- Fatigue test (120,000 cycles)
- Introduce damage at critical location
- Ultimate test with damage
- Validate analysis predictions

#### Damage Tolerance Analysis
- XFEM or similar for crack growth
- Residual strength analysis
- Inspection intervals determination
- No-growth approach for bonded doublers (with enhanced inspection)

#### Inspection Program
- **Initial:** Every 1,000 flights
- **Mature:** Every 3,000 flights (after service experience)
- Methods: Visual, tap test, ultrasonic
- Damage reporting and tracking program

### Success Criteria
- [ ] Building-block tests complete
- [ ] Residual strength ≥ ultimate with 50mm damage
- [ ] Inspection methods validated
- [ ] Service experience program in place
- [ ] EASA acceptance of approach

### Schedule Impact
- Coupon/element tests: 2026 Q3-Q4 (6 months)
- Subcomponent tests: 2027 Q1 (3 months)
- Full-scale test: 2027 Q2-Q3 (6 months)

### Cost Impact
- Coupon tests: $25,000
- Element tests: $30,000
- Subcomponent tests: $40,000
- Full-scale test: $150,000 (included in main program)

### Authority Feedback Requested
1. Is building-block approach acceptable for composite door?
2. Is 50mm damage size appropriate for residual strength?
3. Are proposed inspection intervals acceptable initially?
4. Is no-growth approach acceptable for bonded doublers?

**Status:** Draft ready for submission  
**Target Submission:** Pre-application meeting (2026 Q3)

---

## IP-03: Emergency Egress from BWB Configuration

### Issue Statement
BWB cabin configuration affects emergency egress per CS25.807, 25.809, 25.810. Non-traditional layout requires validation of egress capability.

### Background
- BWB has wide cabin (not cylindrical fuselage)
- Door locations optimized for BWB geometry
- Passenger flow patterns different from traditional aircraft
- Wider cabin may increase egress distance

### Safety Concern
- Passengers may take longer to reach exits
- Flight attendants may have reduced visibility
- Evacuation procedures may need modification
- 90-second evacuation requirement must be met

### Proposed Compliance Approach

**CS25.807 - Emergency Exits**
- Type A exit maintained: 42" × 72"
- Exit location per CS25.809 distribution requirements
- Dimensions verified by inspection

**CS25.809 - Emergency Exit Arrangement**
- Exit distribution analysis for BWB cabin
- Passenger loading analysis
- Show adequate exit distribution

**CS25.810 - Emergency Egress Assist Means**
- Escape slide Type A
- Slide deployment in BWB geometry validated
- Evacuation capability demonstration required

#### Evacuation Analysis (Pre-Test)
- Computational evacuation simulation
- Passenger flow modeling (Pathfinder or similar)
- Identify potential bottlenecks
- Optimize cabin layout if needed

#### Full-Scale Evacuation Demonstration
- Per CS25.803 requirements
- 90 seconds with 50% exits blocked
- Representative passenger mix (demographics, mobility)
- Realistic lighting conditions (emergency lighting only)
- Flight attendants using emergency procedures
- Independent observers and timing

#### Enhanced Procedures
- Flight attendant training for BWB cabin
- Evacuation procedures optimized for layout
- Passenger safety briefing updates
- Crew resource management for wide cabin

### Success Criteria
- [ ] Evacuation simulation shows <90 seconds
- [ ] Full-scale demo completes in ≤90 seconds
- [ ] All passengers egress successfully
- [ ] Flight attendants effectively manage evacuation
- [ ] EASA acceptance of BWB-specific procedures

### Schedule Impact
- Simulation: 2026 Q4 (2 months)
- Full-scale demo: 2027 Q3 (3 months planning + execution)

### Cost Impact
- Simulation: $25,000
- Full-scale demo: $100,000 (mockup, participants, observers)

### Authority Feedback Requested
1. Is evacuation simulation acceptable for initial validation?
2. Will standard CS25.803 demo suffice for BWB or are additional requirements needed?
3. Are BWB-specific procedures acceptable or is layout change required?

**Status:** Draft ready for submission  
**Target Submission:** Pre-application meeting (2026 Q3)

---

## IP-04: Lightning Strike Protection Validation

### Issue Statement
Composite door structure requires lightning strike protection per CS25.954. Zone 1A (likely direct strike) requires direct effects testing validation.

### Background
- Door is external surface, likely lightning strike point
- Composite structure requires enhanced protection
- Al-Li skin with CFRP doublers creates mixed materials
- Lightning protection must not compromise structure

### Safety Concern
- Direct strike could damage structure
- Burn-through could endanger passengers
- Fuel system proximity (H2) increases hazard
- Electromagnetic effects on systems

### Proposed Compliance Approach

**CS25.954 - Lightning Strike Protection**

#### Analysis Phase
- Lightning strike zone classification (expect Zone 1A)
- Current path analysis
- Structural effects analysis
- EMI/EMP effects on door systems

#### Protection Design
- **Option 1:** Conductive coating on composite areas
- **Option 2:** Expanded metal mesh embedded in composite
- **Option 3:** Copper mesh bonded to surface
- Ensure continuity to aircraft ground structure

#### Testing Phase
**Component-Level Tests:**
- Direct effects test per SAE ARP 5414
- Zone 1A waveform (Component A)
- Full current injection (200 kA peak)
- Inspect for damage after test

**Indirect Effects:**
- EMI/EMP analysis for door systems
- Bonding and grounding verification
- System-level testing if safety-critical functions

#### Validation
- Post-test inspection (visual, NDI)
- Residual strength test (if damage found)
- Electrical continuity verification
- Verify no safety-critical damage

### Success Criteria
- [ ] Lightning zones identified
- [ ] Protection system designed and installed
- [ ] Direct effects test passed (no safety-critical damage)
- [ ] Indirect effects acceptable
- [ ] EASA acceptance of approach

### Schedule Impact
- Protection design: 2026 Q4 (3 months)
- Component test: 2027 Q2 (2 months)
- Validation: 2027 Q3 (1 month)

### Cost Impact
- Protection design: $30,000
- Direct effects test: $50,000
- Indirect effects analysis: $20,000

### Authority Feedback Requested
1. Is Zone 1A classification expected for door?
2. Is component-level testing acceptable (vs. full aircraft)?
3. Which protection method is preferred for composite/metal hybrid?
4. Are there BWB-specific lightning concerns?

**Status:** Draft ready for submission  
**Target Submission:** Pre-application meeting (2026 Q3)

---

## Issue Paper Management

### Submission Process
1. **Preparation:** Draft complete with technical detail
2. **Internal review:** Engineering and certification team review
3. **DER review:** DER review for technical accuracy (if engaged)
4. **Submission:** Submit to EASA with pre-application package
5. **Discussion:** Present at pre-application meeting
6. **Authority feedback:** Receive EASA guidance
7. **Resolution:** Document agreed approach
8. **Execution:** Execute agreed compliance program
9. **Closure:** Demonstrate compliance and close

### Tracking
- Issue paper status tracked in certification database
- Authority feedback documented and distributed
- Agreed approach becomes part of certification basis
- Compliance demonstration tracked to closure

### Updates
Issue papers may be updated based on:
- Authority feedback
- Design changes
- Test results
- New information

---

## Summary Status

| IP | Title | Status | Target Submission | Priority |
|----|-------|--------|-------------------|----------|
| IP-01 | Resonance | Draft ready | 2026 Q3 | CRITICAL |
| IP-02 | Damage tolerance | Draft ready | 2026 Q3 | High |
| IP-03 | Emergency egress | Draft ready | 2026 Q3 | Medium |
| IP-04 | Lightning strike | Draft ready | 2026 Q3 | Medium |

---

**Document Control**

**Revision:** 1.0  
**Approved:** Pending  
**Next Review:** 2026-Q2  
**Owner:** AMPEL360 Certification Manager

---

**Part of:** AMPEL360 OPT-IN Framework - ATA 52-10-01 Certification Package
