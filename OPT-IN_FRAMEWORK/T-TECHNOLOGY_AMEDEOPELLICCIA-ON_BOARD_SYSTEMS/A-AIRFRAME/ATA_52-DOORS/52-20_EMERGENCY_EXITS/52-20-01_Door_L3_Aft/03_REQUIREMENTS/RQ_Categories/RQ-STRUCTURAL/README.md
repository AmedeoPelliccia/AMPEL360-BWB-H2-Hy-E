# RQ-STRUCTURAL - Structural Requirements

**Category:** RQ-STRUCTURAL  
**ID Range:** RQ-52-20-01-001 to RQ-52-20-01-019  
**Total Requirements:** 19  
**Priority:** High

## Overview

This category contains all structural requirements for the Door L3 Aft Emergency Exit, including ultimate strength, fatigue life, damage tolerance, and environmental resistance.

## Structural Design Philosophy

The emergency exit door structure must:
- Withstand 150% of ultimate design loads
- Tolerate visible damage without catastrophic failure
- Survive 20,000 operational cycles minimum
- Operate in extreme environmental conditions (-55°C to +70°C)

## Key Requirements Summary

### Primary Structure (RQ-001 to RQ-005)
- **RQ-52-20-01-001**: Ultimate strength @ 150% design load limit
- **RQ-52-20-01-002**: Fatigue life 20,000 cycles minimum
- **RQ-52-20-01-003**: Damage tolerance per CS 25.571
- **RQ-52-20-01-004**: Static strength verification by test
- **RQ-52-20-01-005**: Frame interface load transfer capability

### Material Requirements (RQ-006 to RQ-010)
- **RQ-52-20-01-006**: Aluminum alloy 7075-T6 or equivalent
- **RQ-52-20-01-007**: Corrosion resistance treatment required
- **RQ-52-20-01-008**: Material certifications per AMS specifications
- **RQ-52-20-01-009**: Non-metallic materials flame resistance
- **RQ-52-20-01-010**: Composite material environmental qualification

### Structural Interfaces (RQ-011 to RQ-015)
- **RQ-52-20-01-011**: 12 attachment points minimum to fuselage
- **RQ-52-20-01-012**: Load distribution uniformity requirements
- **RQ-52-20-01-013**: Hinge fitting ultimate strength
- **RQ-52-20-01-014**: Latch striker plate strength requirements
- **RQ-52-20-01-015**: Floor beam interface load capability

### Damage Tolerance (RQ-016 to RQ-019)
- **RQ-52-20-01-016**: Detectable damage threshold definition
- **RQ-52-20-01-017**: Crack growth analysis requirements
- **RQ-52-20-01-018**: Inspection interval determination
- **RQ-52-20-01-019**: Residual strength after damage

## Verification Methods

| Method | Requirements | Percentage |
|--------|--------------|------------|
| Test | 10 | 53% |
| Analysis (FEA) | 7 | 37% |
| Inspection | 2 | 10% |

## Critical Load Cases

1. **Pressurization Loads**: 9.5 psi differential pressure
2. **Emergency Opening Loads**: Manual force + inertia loads
3. **Slide Deployment Loads**: Girt bar attachment forces
4. **Crowd Surge Loads**: 250 lbf/ft² panic loading
5. **Impact Loads**: Bird strike, hail, maintenance damage

## Material Specifications

| Component | Material | Specification |
|-----------|----------|---------------|
| Door Frame | AL 7075-T6 | AMS 4045 |
| Skin Panels | AL 2024-T3 | AMS 4037 |
| Hinges | Ti-6Al-4V | AMS 4928 |
| Fasteners | A286 CRES | MS20426 |

## Structural Analysis Requirements

### Finite Element Analysis
- **Mesh Density**: Max element size 10mm in critical areas
- **Load Cases**: 15 critical load combinations
- **Safety Factors**: 1.5 ultimate, 1.0 limit
- **Validation**: Correlation with physical test data

### Test Requirements
- Static ultimate test to 150% design load limit
- Fatigue test spectrum (20,000 cycles + scatter factor)
- Damage tolerance test with artificial flaws
- Environmental conditioning + retest

## Compliance Matrix

| Requirement | CS25 Reference | Verification | Status |
|-------------|----------------|--------------|--------|
| RQ-001 | 25.305(a) | Test | Defined |
| RQ-002 | 25.571 | Analysis | Defined |
| RQ-003 | 25.571(a) | Analysis | Defined |
| RQ-004 | 25.305(b) | Test | Defined |
| RQ-005 | 25.365 | Analysis | Defined |

## Design Constraints

- **Weight Budget**: 142 kg maximum (including mechanisms)
- **Center of Gravity**: Within ±50mm of design point
- **Stiffness**: Natural frequency > 15 Hz (avoid flutter)
- **Thermal Expansion**: Accommodate ±5mm differential growth

## Related Documents

- **04_DESIGN**: Structural design drawings and calculations
- **06_ENGINEERING**: FEA reports and analysis documentation
- **07_V_AND_V**: Test plans and test reports
- **10_CERTIFICATION**: CS 25.305/571 compliance evidence

## Change Control

All structural requirements are configuration-controlled. Changes require:
1. Structural Engineering review and approval
2. Updated stress analysis
3. Impact assessment on weight and CG
4. Re-verification if design changes

---

**Document Control**  
**Version:** 1.0  
**Date:** 2025-11-04  
**Status:** Released  
**Approved by:** Chief Structural Engineer
