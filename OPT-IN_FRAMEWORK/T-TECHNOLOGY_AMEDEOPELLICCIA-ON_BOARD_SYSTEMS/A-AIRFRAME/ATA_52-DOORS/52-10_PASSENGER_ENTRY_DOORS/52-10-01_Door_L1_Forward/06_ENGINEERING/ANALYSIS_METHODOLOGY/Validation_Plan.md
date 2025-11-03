# Validation Plan

**Document:** AMPEL360-52-10-01-ENG-VAL  
**Date:** 2025-11-03  
**Status:** Draft

## Overview

This document outlines the validation strategy for all AI-assisted engineering analyses of the Door L1 Forward.

## VALIDATION PHILOSOPHY

**Principle:** "Trust but verify—everything"

All AI-generated calculations must be validated through multiple independent methods before hardware fabrication or certification.

## VALIDATION LEVELS

### Level 1: Sanity Checks (Immediate)
**Performed by:** Engineering team  
**Timeline:** During analysis development

**Methods:**
- Order-of-magnitude verification
- Comparison with similar structures
- Units and dimensional analysis
- Limiting case checks (e.g., zero load → zero stress)

**Status:** ✅ Completed for all calculations

### Level 2: Professional Review (Short Term)
**Performed by:** Licensed professional engineers  
**Timeline:** Before detailed design freeze

**Methods:**
- Independent calculation review
- Alternative method comparison
- Assumption validation
- Standards compliance check

**Status:** ⏳ Planned

### Level 3: FEA Validation (Medium Term)
**Performed by:** FEA specialists using commercial software  
**Timeline:** Detailed design phase

**Methods:**
- NASTRAN/ANSYS/Abaqus analysis
- Mesh convergence studies
- Sensitivity analysis
- Correlation with AI estimates

**Status:** ⏳ Planned

### Level 4: Physical Testing (Long Term)
**Performed by:** Test laboratories  
**Timeline:** Prototype and certification phases

**Methods:**
- Component testing
- Full-scale testing
- Environmental testing
- Fatigue testing

**Status:** ⏳ Planned

## VALIDATION BY DISCIPLINE

### Structural Analysis Validation

#### Static Stress (CALC-52-10-01-STR-001 through STR-007)

**FEA Validation:**
```
Tool: NASTRAN or Abaqus
Model: 3D solid/shell elements
Mesh: Min 4 elements through thickness
Loads: CS-25.365 pressure cases
BC: Elastic restraint at hinges/latches
```

**Test Validation:**
```
Test: Full-scale pressure test
Instrumentation: 
  - 20+ strain gauges on panel
  - 6 LVDTs for deflection
  - Load cells at hinges/latches
Load levels:
  - Limit: 8.5 psi
  - Proof: 12.75 psi (1.5×)
  - Ultimate: 17.0 psi (2.0×)
Success criteria: No permanent deformation at proof
```

**Correlation Target:** FEA within ±10% of test

#### Composite Laminate (CALC-52-10-01-STR-005)

**FEA Validation:**
```
Tool: Abaqus Composite Modeler
Model: Ply-by-ply layup
Analysis: First ply failure + progressive
Output: Tsai-Wu failure index
```

**Test Validation:**
```
Test: Coupon testing per ASTM D3039/D3518
Specimens: 
  - [0]8 unidirectional
  - [±45]2s shear
  - [0/90]2s cross-ply
  - [0/±45/90]s quasi-isotropic
Properties measured:
  - E11, E22, G12
  - ν12
  - σ_tu, σ_cu
  - τ_u
```

**Correlation Target:** Properties within CMH-17 basis values

### Dynamic Analysis Validation

#### Natural Frequency (CALC-52-10-01-DYN-001 through DYN-004)

**FEA Validation:**
```
Tool: NASTRAN SOL 103 (normal modes)
Model: Same as static with mass
Output: First 10 natural frequencies and mode shapes
Damping: Not predicted (must measure)
```

**Test Validation (CRITICAL):**
```
Test: Ground Vibration Test (GVT)
Method: Impact hammer or shaker excitation
Instrumentation:
  - 15+ accelerometers on panel
  - 3-axis measurements at key points
Frequency range: 5-200 Hz
Output:
  - Natural frequencies (±1 Hz accuracy)
  - Mode shapes (animation)
  - Damping ratios (half-power method)
```

**Correlation Target:**
- Frequency: FEA within ±5% of GVT
- Mode shapes: MAC > 0.9

**Risk:** If Mode 1 < 27 Hz, REDESIGN REQUIRED

### Fatigue & Damage Tolerance Validation

#### Fatigue Life (CALC-52-10-01-FAT-001 through FAT-005)

**Analysis Validation:**
```
Tool: fe-safe or MSC Fatigue
Input: FEA stress results + load spectrum
Method: Rainflow counting + Miner's rule
Material data: Test-derived S-N curves
```

**Test Validation (MANDATORY FOR CERTIFICATION):**
```
Test: Full-scale fatigue test
Spectrum: ASTERIX or similar (60,000 flights)
Duration: 2× design life (120,000 flights equivalent)
Instrumentation:
  - Crack detection (eddy current/ultrasonic)
  - Strain monitoring at critical locations
Inspections: Every 10,000 flight equivalents
Success criteria: No cracks > 2mm after 120k flights
```

**Teardown Inspection:**
- Disassemble after testing
- Microscopic examination of all critical areas
- Correlate with predictions

### Weight & Balance Validation

#### Mass Properties (CALC-52-10-01-WGT-001 through WGT-003)

**Test Validation:**
```
Test: Precision weighing and MOI measurement
Equipment:
  - Calibrated scale (±0.1 kg accuracy)
  - Trifilar pendulum or bifilar suspension
Measurements:
  - Total mass
  - CG location (x, y, z)
  - Moments of inertia (Ixx, Iyy, Izz, Ixy, Ixz, Iyz)
```

**Correlation Target:** Mass within ±3% of prediction

### Thermal Analysis Validation

#### Thermal Effects (CALC-52-10-01-THM-001 through THM-003)

**Test Validation:**
```
Test: Environmental chamber testing
Temperature range: -55°C to +85°C
Cycles: 10× expected life
Measurements:
  - Thermal expansion (LVDT)
  - Seal compression set
  - Leak rate vs. temperature
  - Operation force vs. temperature
```

### Mechanism Validation

#### Kinematics & Actuation (CALC-52-10-01-MEC-001 through MEC-003)

**Test Validation:**
```
Test: Full-scale mechanism testing
Setup: Door mounted in test fixture
Measurements:
  - Operation force vs. position
  - Operation time
  - Clearances (min/max)
  - Manual override force
Cycles: 10,000 operations
Success criteria:
  - Force < 60 N (per CS-25.783)
  - Operation time < 5 seconds
  - No binding or jamming
```

## VALIDATION SCHEDULE

### Phase 1: Analysis Completion (Weeks 1-2)
- [x] AI calculations completed
- [ ] Engineering review
- [ ] Preliminary design review (PDR)

### Phase 2: FEA Validation (Weeks 3-8)
- [ ] Contract FEA specialist
- [ ] Develop detailed FEA models
- [ ] Run analyses and correlate
- [ ] Update design if needed

### Phase 3: Material Testing (Weeks 4-12)
- [ ] Procure composite materials
- [ ] Fabricate test coupons
- [ ] Conduct ASTM testing
- [ ] Update material properties

### Phase 4: Component Testing (Weeks 10-16)
- [ ] Fabricate prototype components
- [ ] Static strength testing
- [ ] GVT testing
- [ ] Mechanism testing

### Phase 5: Full-Scale Testing (Weeks 18-30)
- [ ] Fabricate full door assembly
- [ ] Pressure testing
- [ ] Environmental testing
- [ ] Fatigue testing (long duration)

### Phase 6: Certification (Weeks 30-40)
- [ ] DER review of all data
- [ ] Compliance demonstration
- [ ] Type certificate data sheet update

## SUCCESS CRITERIA

### Minimum Requirements for Manufacturing Release

**Structural:**
- [ ] FEA shows MS > 0 for all load cases
- [ ] Static test to ultimate with no failure
- [ ] Fatigue test to 2× life with inspection plan

**Dynamic:**
- [ ] GVT confirms no resonance < 1.2× engine frequency
- [ ] Damping > 2% of critical in Mode 1
- [ ] No flutter or vibration issues

**Weight:**
- [ ] Actual weight < 140 kg (target)
- [ ] CG within ±50 mm of predicted

**Performance:**
- [ ] Leak rate < 0.1 CFM at 8.5 psi
- [ ] Operation force < 60 N
- [ ] Passes all CS-25.783 requirements

## DOCUMENTATION REQUIREMENTS

For each validation activity:
1. Test plan (before testing)
2. Test procedure (step-by-step)
3. Raw data (calibrated instruments)
4. Data reduction and analysis
5. Correlation with predictions
6. Test report (summary and conclusions)

## CONTINGENCY PLANS

### If Validation Fails

**Stress too high:**
- Increase face sheet to 5mm
- Add local reinforcement
- Reduce pressure (if possible)

**Resonance detected:**
- Add constrained layer damping
- Modify structure (add ribs)
- Change boundary conditions

**Fatigue life too short:**
- Reduce stress (see above)
- Change material
- Establish inspection program

**Weight too high:**
- Reduce core density
- Optimize non-critical areas
- Review design for excess material

## APPROVAL GATES

| Gate | Requirements | Approver |
|------|------------|----------|
| PDR | AI calcs reviewed | Lead Engineer |
| CDR | FEA complete, test plan approved | Chief Engineer |
| Manufacturing Release | All testing complete, MS > 0 | DER |
| Certification | All compliance shown | Certification Authority |

## RISK MANAGEMENT

**High-Risk Items (Require Extra Validation):**
1. Natural frequency (resonance risk) → GVT mandatory
2. Fatigue life (safety critical) → Full-scale testing mandatory
3. Damage tolerance (certification critical) → Damage scenarios tested

**Medium-Risk Items:**
- Ultimate strength (covered by safety factors)
- Weight (margin available)
- Thermal effects (standard materials)

## COST ESTIMATE

| Activity | Cost (USD) | Duration |
|----------|-----------|----------|
| FEA Analysis | $30,000 | 6 weeks |
| Material Testing | $15,000 | 8 weeks |
| GVT | $25,000 | 2 weeks |
| Static Testing | $20,000 | 4 weeks |
| Fatigue Testing | $80,000 | 12 weeks |
| DER Review | $10,000 | 4 weeks |
| **TOTAL** | **$180,000** | **~30 weeks** |

## CONCLUSION

This validation plan ensures that all AI-assisted calculations are verified through professional analysis and physical testing before the door is certified for flight.

**Key Principle:** AI provides fast preliminary estimates. Validation provides confidence for certification.

---

*"In God we trust. All others must bring data." — W. Edwards Deming*
