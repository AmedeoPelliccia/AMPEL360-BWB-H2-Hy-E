# Structural Acceptance Criteria
## Door L1 Forward

**Document:** ACCEPT-STRUCT-001  
**Revision:** 1.0  
**Date:** 2025-11-03

---

## 1. STRUCTURAL TESTS

### 1.1 Static Ultimate Strength (TP-001)

**PASS Criteria:**
- ✓ No rupture at 17.0 psi (3 seconds minimum hold)
- ✓ No visible cracks or delamination
- ✓ Peak strain <10,000 με at all locations
- ✓ Displacement within analytical predictions (±30%)

**FAIL Criteria:**
- ✗ Panel rupture or catastrophic failure
- ✗ Face sheet delamination >25 mm diameter
- ✗ Core crushing or permanent damage
- ✗ Latch or hinge failure

---

### 1.2 Proof Pressure (TP-002)

**PASS Criteria:**
- ✓ No permanent deformation (residual <0.5 mm)
- ✓ Residual strain <100 με
- ✓ Leak rate <0.05 CFM @ 8.5 psi
- ✓ No visible damage

**FAIL Criteria:**
- ✗ Permanent set >0.5 mm
- ✗ Residual strain >100 με  
- ✗ Excessive leak rate
- ✗ Any structural damage

---

### 1.3 Fatigue (TP-003)

**PASS Criteria:**
- ✓ 120,000 cycles completed
- ✓ No crack initiation
- ✓ No delamination growth
- ✓ Residual strength >ultimate load

**FAIL Criteria:**
- ✗ Crack initiation before 120,000 cycles
- ✗ Delamination growth
- ✗ Loss of structural capability

---

### 1.4 Damage Tolerance (TP-004)

**PASS Criteria:**
- ✓ Sustains limit load (11.33 psi) with 50 mm hole
- ✓ No catastrophic failure
- ✓ Controlled crack growth only

**FAIL Criteria:**
- ✗ Catastrophic failure with damage
- ✗ Inability to sustain limit load

---

### 1.5 GVT Modal (TP-005) - CRITICAL

**PASS Criteria:**
- ✓ **Mode 1 damping ζ ≥ 3.0%** (PRIMARY)
- ✓ Natural frequencies within ±15% of predictions
- ✓ Mode shapes match FEA (MAC >0.80)
- ✓ No unexpected resonances <100 Hz

**FAIL Criteria:**
- ✗ **Mode 1 damping <3.0%** (MANDATORY REDESIGN)
- ✗ Mode 1 frequency 23-27 Hz range (resonance risk)
- ✗ Unexpected low-frequency modes
- ✗ Poor correlation with predictions (>30%)

**Contingency:** If fail, implement Option A (thicker face sheets) or Option B (add CLD damping)

---

## 2. ENVIRONMENTAL TESTS

### 2.1 Temperature Extremes (TP-009)

**PASS Criteria:**
- ✓ Door operates at -40°C and +55°C
- ✓ Seals remain effective
- ✓ Mechanisms function normally
- ✓ No material degradation

---

### 2.2 Lightning Strike (TP-006)

**PASS Criteria:**
- ✓ No burn-through of pressure boundary
- ✓ Damage repairable
- ✓ Safe current path established
- ✓ No system failures

---

### 2.3 Bird Strike (TP-007)

**PASS Criteria:**
- ✓ No penetration of pressure boundary
- ✓ Damage localized (<300 mm)
- ✓ Door remains attached
- ✓ Latches remain engaged

---

### 2.4 Fire Resistance (TP-008)

**PASS Criteria:**
- ✓ No burn-through for 15 minutes
- ✓ Back face temp <300°C average
- ✓ Smoke within limits
- ✓ Structural integrity maintained

---

## 3. OVERALL STRUCTURAL ACCEPTANCE

**Door L1 Forward structurally acceptable if:**
- [  ] ALL structural tests passed
- [  ] GVT shows ζ ≥ 3.0% at Mode 1 (CRITICAL)
- [  ] Analysis-test correlation acceptable
- [  ] No unexpected failure modes
- [  ] Margins of safety verified

---

## 4. SIGNATURE

**Structures Lead:** ____________________  
**Date:** ____________________

**Chief Engineer:** ____________________  
**Date:** ____________________

---

**Status:** Criteria established - Awaiting test execution
