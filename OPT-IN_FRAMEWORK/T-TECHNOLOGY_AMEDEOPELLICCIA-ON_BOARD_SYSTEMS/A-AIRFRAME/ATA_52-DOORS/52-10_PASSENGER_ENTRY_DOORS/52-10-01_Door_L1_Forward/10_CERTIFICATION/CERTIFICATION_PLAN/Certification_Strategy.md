# Certification Strategy - Door L1 Forward

**Document:** AMPEL360-52-10-01-CERT-STRATEGY  
**Status:** PRELIMINARY PLANNING  
**Date:** 2025-11-03

## 1. REGULATORY BASIS

### Primary Requirements
- **Europe:** EASA CS-25 Amendment 27
- **USA:** FAR Part 25 (harmonized)
- **Global:** Bilateral agreements

### Classification
- Primary structure (PSE)
- Emergency exit (Type A)
- Pressurized structure
- Safety-critical

## 2. CERTIFICATION APPROACH

### Overall Strategy
```
Design → Analysis → Test → Compliance → Approval
  ↓         ↓         ↓         ↓           ↓
(Now)    (Need)   (2027)    (2028)      (2028+)
```

### Key Principles
1. **Show compliance by test** where required
2. **Analysis supported by test** for damage tolerance
3. **Similarity** where applicable (limited for novel design)
4. **Conservative approach** due to BWB configuration

## 3. CRITICAL COMPLIANCE ITEMS

### High Priority (Safety Critical)

| Requirement | Concern | MOC | Status |
|------------|---------|-----|--------|
| CS25.783 | Door opening prevention | Test | Not started |
| CS25.365 | Ultimate pressure (17 psi) | Test | AI estimate only |
| CS25.571 | Damage tolerance | Analysis + Test | Conceptual |
| CS25.810 | Emergency egress | Demo | Not started |
| CS25.629 | Aeroelastic stability | Analysis + GVT | **CRITICAL RISK** |

### Resonance Risk (HIGHEST PRIORITY)
```
Mode 1: ~25-30 Hz (AI estimate)
Engine: 25 Hz max continuous

MANDATORY: GVT must show ζ ≥ 3%
Risk: May require redesign if damping insufficient
```

## 4. MEANS OF COMPLIANCE (MOC)

### MOC Selection
| Method | Usage | Percentage |
|--------|-------|------------|
| (1) Test | Ultimate, proof, fatigue | 40% |
| (2) Analysis | Supported by test data | 30% |
| (3) Inspection | Dimensions, mass | 10% |
| (4) Demonstration | Functional requirements | 15% |
| (5) Design feature | Plug door | 5% |

### Critical Tests Required
1. **GVT** - Modal survey (MANDATORY)
2. **Static ultimate** - 17 psi
3. **Fatigue** - 120,000 cycles
4. **Damage tolerance** - 50mm damage
5. **Functional** - Door operation

## 5. SPECIAL CONDITIONS

### Expected Special Conditions
1. **BWB configuration** - Novel door integration
2. **Composite structure** - Beyond current guidance
3. **H2 proximity** - Enhanced fire/explosion
4. **CAOS integration** - Software aspects

### Issue Papers Anticipated
- IP-01: Resonance with propulsion
- IP-02: Composite damage tolerance
- IP-03: Emergency egress from BWB
- IP-04: Lightning protection validation

## 6. CERTIFICATION TIMELINE

### Optimistic Schedule
```
2025 Q4: Current (AI conceptual only)
2026 Q1: FEA validation
2026 Q2: TC application preparation
2026 Q3: Initial authority meeting
2026 Q4: Prototype testing begins
2027 Q1: GVT (GO/NO-GO decision)
2027 Q2: Structural test campaign
2027 Q3: Test reports submission
2027 Q4: Compliance review
2028 Q1: Finding resolution
2028 Q2: TC approval (target)
```

### Realistic Timeline
Add 12-18 months for:
- FEA iterations
- Test failures and retest
- Authority findings
- Design changes from GVT

**Realistic TC: 2029-2030**

## 7. RISKS TO CERTIFICATION

| Risk | Impact | Mitigation |
|------|--------|-----------|
| No FEA capability | Cannot certify | Contract FEA services |
| Mode 1 resonance | Redesign required | Early GVT |
| AI analysis only | Authority rejection | Professional analysis |
| Novel configuration | Extended review | Early authority engagement |
| Funding gaps | Schedule delay | Phased approach |

## 8. DELEGATION STRATEGY

### DER (Designated Engineering Representative)
- **Structural DER** (primary) - Composite door structures
- **Systems DER** (secondary) - Door control systems
- **Software DER** (if required) - CAOS interface

### Authority Coordination
- **Pre-application meeting** - Q3 2026
- **Certification basis** - CS-25 Amendment 27
- **Special conditions** - BWB configuration
- **Issue papers** - Early submission

## 9. COMPLIANCE PHILOSOPHY

### Test vs. Analysis
```
Test-dominated areas:
- Ultimate strength (CS25.305)
- Fatigue life (CS25.571)
- Emergency operation (CS25.810)

Analysis-dominated areas:
- Detailed stress (supported by test)
- Damage tolerance (validated by test)
- Flutter/resonance (validated by GVT)
```

### Conservative Margins
- **Static ultimate:** 1.5 (limit load factor)
- **Fatigue:** 2.0 (service life)
- **Damage tolerance:** 1.15 (residual strength)

## 10. SUCCESS CRITERIA

### Go/No-Go Gates
1. **FEA Validation** (2026 Q1) - Margins positive
2. **GVT Results** (2027 Q1) - Damping adequate (ζ ≥ 3%)
3. **Ultimate Test** (2027 Q2) - No failure at ultimate
4. **Fatigue Test** (2027 Q3) - 120k cycles without failure
5. **Authority Review** (2028 Q1) - No major findings

### Certification Approval Criteria
- [ ] All compliance items closed
- [ ] All test evidence accepted
- [ ] All DER reports signed
- [ ] All authority findings resolved
- [ ] Production approval granted
- [ ] ICA approved

## Document Control

**Revision:** 1.0  
**Approved:** Pending  
**Next Review:** 2026-Q1  
**Owner:** AMPEL360 Certification Manager

---

**Part of:** AMPEL360 OPT-IN Framework - ATA 52-10-01 Certification Package
