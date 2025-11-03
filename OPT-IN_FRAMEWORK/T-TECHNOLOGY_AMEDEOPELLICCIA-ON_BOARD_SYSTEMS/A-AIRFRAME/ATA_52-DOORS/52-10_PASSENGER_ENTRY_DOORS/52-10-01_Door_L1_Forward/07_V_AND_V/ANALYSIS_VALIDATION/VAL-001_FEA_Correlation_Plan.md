# FEA Correlation Plan
## Door L1 Forward

**Document:** VAL-001  
**Revision:** 1.0  
**Date:** 2025-11-03

---

## 1. OBJECTIVE

Establish correlation between Finite Element Analysis (FEA) predictions and physical test results to validate analytical models.

---

## 2. SCOPE

### 2.1 Analysis to Correlate
- Static stress analysis (CALC-STR-001)
- Modal analysis (CALC-DYN-001)
- Pressure load distribution
- Strain field predictions

### 2.2 Test Data for Correlation
- Static ultimate test (TP-001)
- Proof pressure test (TP-002)
- Ground vibration test (TP-005)

---

## 3. CORRELATION METRICS

### 3.1 Stress/Strain Correlation

**Metric:** Strain comparison at 24 gauge locations

**Acceptance Criteria:**
```
Good correlation: <10% difference
Acceptable: 10-20% difference
Poor: >20% difference (requires model update)
```

**Method:**
1. Extract FEA strain at gauge locations
2. Compare with test data at same load
3. Calculate % difference
4. Generate correlation plots

### 3.2 Displacement Correlation

**Metric:** Panel center displacement

**Acceptance Criteria:**
```
Good: <15% difference
Acceptable: 15-25% difference
Poor: >25% difference
```

### 3.3 Natural Frequency Correlation

**Metric:** First 5 mode frequencies

**Acceptance Criteria:**
```
Excellent: <5% difference
Good: 5-10% difference
Acceptable: 10-15% difference
Poor: >15% difference
```

### 3.4 Mode Shape Correlation

**Metric:** Modal Assurance Criterion (MAC)

**Acceptance Criteria:**
```
Excellent: MAC > 0.95
Good: MAC 0.90-0.95
Acceptable: MAC 0.80-0.90
Poor: MAC < 0.80
```

**MAC Formula:**
```
MAC = |φ_test^T × φ_FEA|² / (|φ_test|² × |φ_FEA|²)

Where:
φ_test = measured mode shape vector
φ_FEA = predicted mode shape vector
```

---

## 4. CORRELATION PROCESS

### 4.1 Phase 1: Pre-Test Predictions
1. Complete FEA analysis
2. Extract predictions at test measurement points
3. Document assumptions and boundary conditions
4. Issue prediction report before testing

### 4.2 Phase 2: Test Execution
1. Perform tests per test plans
2. Collect data at same locations as FEA
3. Process raw data to engineering units
4. Archive test data

### 4.3 Phase 3: Correlation Analysis
1. Import test data
2. Extract FEA data at same locations
3. Calculate correlation metrics
4. Generate correlation plots
5. Identify discrepancies

### 4.4 Phase 4: Model Update
If correlation poor:
1. Review FEA assumptions
2. Check material properties
3. Verify boundary conditions
4. Update mesh if needed
5. Re-run analysis
6. Document changes

---

## 5. REPORTING

### 5.1 Correlation Report Contents
1. Executive summary (pass/fail)
2. Comparison tables (predicted vs. measured)
3. Correlation plots
4. Statistical analysis
5. Discrepancy investigation
6. Model update recommendations
7. Updated predictions

### 5.2 Plots Required
- Strain distribution (FEA vs. test)
- Displacement contours
- Mode shapes (side-by-side)
- Frequency comparison bar chart
- MAC matrix
- Error distribution

---

## 6. MODEL VALIDATION

### 6.1 Validated Uses
If correlation good:
- Predict production hardware performance
- Support design changes
- Analyze what-if scenarios
- Certification by analysis

### 6.2 Limitations
Document limitations:
- Valid load range
- Configuration dependencies
- Material variability
- Uncertainty bounds

---

## 7. UNCERTAINTY QUANTIFICATION

### 7.1 Sources of Uncertainty

**Material Properties:**
- E-modulus: ±10%
- Poisson's ratio: ±5%
- Thickness: ±0.2mm

**Boundary Conditions:**
- Latch stiffness: ±20%
- Hinge rotation resistance: ±30%
- Seal pressure distribution: ±15%

**Measurement:**
- Strain gauge: ±2%
- LVDT: ±1%
- Natural frequency: ±0.5 Hz

### 7.2 Combined Uncertainty

**Monte Carlo Analysis:**
1. Define probability distributions for inputs
2. Run 1000 FEA simulations
3. Calculate output statistics
4. Report confidence intervals

**Target:** 95% confidence that actual response within ±25% of prediction

---

## 8. SUCCESS CRITERIA

**Validation Successful if:**
- ✓ All strain correlations <20% error
- ✓ Displacement correlation <25% error
- ✓ Mode 1 frequency <10% error
- ✓ Mode 1 MAC > 0.85
- ✓ No unexpected failure modes in test

**Validation Failed if:**
- ✗ Any metric outside acceptable range
- ✗ Test reveals unanticipated behavior
- ✗ Failure mode not predicted by FEA

---

## 9. SCHEDULE

- Pre-test predictions: 2 weeks before test
- Correlation analysis: 1 week after test
- Model update (if needed): 2 weeks
- Final report: 1 week after correlation

---

## 10. REFERENCES

- NAFEMS Quality Assurance Guidelines
- ASME V&V 10 Guide for Verification and Validation in Computational Solid Mechanics
- NASA-STD-7009A Standard for Models and Simulations
- Door L1 Forward FEA Model Documentation

---

**Status:** Ready for execution after FEA completion
