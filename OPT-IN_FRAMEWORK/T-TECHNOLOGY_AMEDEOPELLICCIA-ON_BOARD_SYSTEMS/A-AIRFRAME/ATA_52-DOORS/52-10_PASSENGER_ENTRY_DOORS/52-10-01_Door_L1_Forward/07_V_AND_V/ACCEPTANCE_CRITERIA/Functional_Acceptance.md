# Functional Acceptance Criteria
## Door L1 Forward

**Document:** ACCEPT-FUNC-001  
**Revision:** 1.0  
**Date:** 2025-11-03

---

## 1. NORMAL OPERATIONS

### 1.1 Powered Operation
**PASS:**
- ✓ Opening time <30 seconds
- ✓ Closing time <30 seconds
- ✓ Smooth operation (no binding)
- ✓ Position indicators accurate
- ✓ 50 cycles without failure

### 1.2 Manual Operation
**PASS:**
- ✓ Opening force ≤220 N
- ✓ Can be operated by 5th percentile female
- ✓ 10 cycles without excessive wear

### 1.3 Seal System
**PASS:**
- ✓ Inflation time <30 seconds
- ✓ Seal pressure 5 psi ±0.5 psi
- ✓ Leak rate <0.05 CFM @ 8.5 psi cabin pressure

### 1.4 Latch System
**PASS:**
- ✓ All 8 latches engage reliably
- ✓ Visual indicators show green when latched
- ✓ Latch release force within limits

---

## 2. EMERGENCY OPERATIONS

### 2.1 Emergency Opening - Inside
**PASS:**
- ✓ **Opening time ≤15 seconds** (CRITICAL)
- ✓ Handle operation <90 N force
- ✓ Slide deploys automatically
- ✓ Emergency lighting activates

### 2.2 Emergency Opening - Outside
**PASS:**
- ✓ External handle accessible
- ✓ Opens from outside when cabin unpressurized
- ✓ Opening time ≤15 seconds

### 2.3 Slide Deployment
**PASS:**
- ✓ **Deployment time ≤6 seconds** (CRITICAL)
- ✓ Slide inflates fully
- ✓ Girt bar attachment secure
- ✓ Slide detachment function works

---

## 3. SAFETY SYSTEMS

### 3.1 Pressure Interlock
**PASS:**
- ✓ Door cannot open when cabin pressure >1 psi
- ✓ Latches cannot disengage under pressure
- ✓ Override function works (if provided)
- ✓ Warning system activates

### 3.2 Warning Systems
**PASS:**
- ✓ "DOOR OPEN" warning <1 second delay
- ✓ Cockpit indication accurate
- ✓ Aural warning if configured
- ✓ Warning clears when door closed

### 3.3 Position Indicators
**PASS:**
- ✓ Accurate indication of door position
- ✓ Latched/unlatched indication
- ✓ Visible from cabin and cockpit

---

## 4. DURABILITY

### 4.1 Cyclic Operation
**PASS:**
- ✓ 50 cycles completed
- ✓ No degradation in performance
- ✓ No excessive wear
- ✓ Mechanisms remain within tolerance

---

## 5. OVERALL FUNCTIONAL ACCEPTANCE

**Door L1 Forward functionally acceptable if:**
- [  ] Normal operations meet requirements
- [  ] Emergency opening ≤15 seconds (CRITICAL)
- [  ] Slide deployment ≤6 seconds (CRITICAL)
- [  ] Safety systems function correctly
- [  ] 50-cycle durability passed
- [  ] All operator procedures validated

---

## 6. SIGNATURE

**Systems Engineer:** ____________________  
**Date:** ____________________

**Flight Test Engineer:** ____________________  
**Date:** ____________________

---

**Status:** Criteria established - Awaiting TP-010 execution
