# Test Procedure - Leak Rate Measurement

**Procedure:** PROC-003  
**Revision:** DRAFT  
**Date:** 2025-11-03

---

## 1. OBJECTIVE

Measure cabin pressure leak rate through door sealing system per CS-25.783 requirements.

---

## 2. EQUIPMENT

- Pressure controller (±0.01 psi accuracy)
- Leak detector (Inficon Protec or equivalent)
- Pressure sensors (2, redundant)
- Temperature sensors
- Data acquisition system

---

## 3. PROCEDURE

### 3.1 Setup
1. Install door in test fixture
2. Engage all latches
3. Inflate seals to 5 psi
4. Install pressure sensors
5. Seal all other openings

### 3.2 Pressurization
1. Close chamber
2. Pressurize to 8.5 psi @ 0.5 psi/min
3. Stabilize for 5 minutes
4. Note initial pressure (P₀) and time (t₀)

### 3.3 Hold and Measure
1. Isolate chamber (close valves)
2. Record pressure every 1 minute for 10 minutes
3. Monitor temperature (correct for thermal effects)
4. Calculate pressure decay rate (dP/dt)

### 3.4 Calculation
```
Leak Rate (CFM) = (V × dP/dt) / (Patm × 60)

Where:
V = chamber volume (cubic feet)
dP/dt = pressure decay rate (psi/min)
Patm = atmospheric pressure (psi)
```

---

## 4. ACCEPTANCE

**PASS:** Leak rate < 0.05 CFM @ 8.5 psi  
**FAIL:** Leak rate ≥ 0.05 CFM

---

## 5. TROUBLESHOOTING

If leak rate excessive:
1. Perform soap bubble test on seals
2. Check latch engagement
3. Inspect seal condition
4. Verify seal inflation pressure
5. Check for structural gaps

---

**Reference:** CS-25.783(c) - Doors must be reasonably airtight.
