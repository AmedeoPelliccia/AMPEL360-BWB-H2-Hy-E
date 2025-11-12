# Material Coupon Test Plan
## Property Validation for AI Predictions

**Document:** DEM-001-TEST-PLAN  
**Priority:** HIGH - Validates Material Assumptions  
**Status:** Awaiting Funding

### 1. OBJECTIVE

Validate material properties used in AI analysis:
- CFRP face sheet properties
- Core shear properties
- Face/core bond strength
- Actual vs. theoretical density

### 2. COUPON MATRIX

| Test | Specimen | Quantity | Standard |
|------|----------|----------|----------|
| Tensile 0° | 250×25×2mm | 5 | ASTM D3039 |
| Tensile 90° | 250×25×2mm | 5 | ASTM D3039 |
| Compression | 150×100×2mm | 5 | ASTM D6641 |
| In-plane shear | 250×25×2mm | 5 | ASTM D5379 |
| Core shear L | 50×50×40mm | 5 | ASTM C273 |
| Core shear W | 50×50×40mm | 5 | ASTM C273 |
| Core compression | 50×50×40mm | 5 | ASTM C365 |
| Flatwise tension | 50×50×48mm | 5 | ASTM C297 |
| Climbing drum peel | 75×300×48mm | 3 | ASTM D1781 |

**Total Specimens:** 43

### 3. MANUFACTURING

#### Small Autoclave Run
- 600×600mm panel
- Same cure cycle as full door
- Cut specimens after cure
- Document process parameters

#### Layup Configuration
```
Face sheets (both sides):
[0/+45/90/-45]s = 8 plies total

Core:
Nomex HRH10-1/8-3.0
Thickness: 38mm (1.5 inches)

Adhesive:
EA9396 film adhesive
```

#### Process Parameters
- Cure temperature: 180°C
- Cure pressure: 7 bar (100 psi)
- Ramp rate: 2°C/min
- Hold time: 120 minutes
- Vacuum: Throughout cure

### 4. CRITICAL VALIDATIONS

#### AI Prediction vs. Test

| Property | AI Estimate | Uncertainty | Test Target | Action if Failed |
|----------|-------------|-------------|-------------|------------------|
| E₁ (GPa) | 148 | ±30% | 104-192 GPa | Update FEA |
| E₂ (GPa) | 9.65 | ±30% | 6.8-12.5 GPa | Update FEA |
| Strength (MPa) | 2724 | ±30% | >2000 min | Redesign if <1800 |
| G₁₂ (GPa) | 5.24 | ±30% | 3.7-6.8 GPa | Update FEA |
| Core shear (MPa) | 1.17 | ±40% | >0.8 min | Thicker core |
| Core E (MPa) | 137 | ±40% | 82-192 MPa | Update FEA |
| Bond (MPa) | 35 | ±40% | >25 min | Change adhesive |
| Density (kg/m³) | 1580 | ±10% | 1420-1740 | Update mass |

### 5. TEST PROCEDURES

#### 5.1 Tensile Testing (ASTM D3039)
**Equipment:** Universal test machine, 50 kN capacity

**Procedure:**
1. Mount specimen in grips
2. Install strain gauges (0° and 90°)
3. Load at 2 mm/min
4. Record load-displacement
5. Calculate E, ν, σ_ult

**Data Required:**
- Stress-strain curve
- Modulus of elasticity
- Poisson's ratio
- Ultimate tensile strength
- Failure mode

#### 5.2 Compression Testing (ASTM D6641)
**Equipment:** CLC fixture, 100 kN capacity

**Procedure:**
1. Mount specimen in CLC fixture
2. Install strain gauges
3. Load at 1 mm/min
4. Record load-displacement
5. Note buckling or crushing failure

**Data Required:**
- Compression modulus
- Ultimate compression strength
- Failure mode

#### 5.3 In-Plane Shear (ASTM D5379)
**Equipment:** V-notched beam fixture

**Procedure:**
1. Mount notched specimen
2. Install ±45° strain gauges
3. Load at 2 mm/min
4. Record shear stress-strain

**Data Required:**
- Shear modulus G₁₂
- Ultimate shear strength
- Nonlinear behavior

#### 5.4 Core Shear Testing (ASTM C273)
**Equipment:** Sandwich beam fixture

**Procedure:**
1. Bond specimens to loading blocks
2. Apply 3-point bending
3. Load at 0.5 mm/min
4. Calculate core shear from beam theory

**Data Required:**
- Core shear modulus
- Core shear strength
- Face/core bond integrity

#### 5.5 Flatwise Tension (ASTM C297)
**Equipment:** Tensile machine with bonded blocks

**Procedure:**
1. Bond loading blocks to faces
2. Pull perpendicular to faces
3. Record load at failure
4. Inspect failure surface

**Data Required:**
- Flatwise tensile strength
- Failure mode (core or bond)

#### 5.6 Climbing Drum Peel (ASTM D1781)
**Equipment:** Peel test drum fixture

**Procedure:**
1. Debond one face partially
2. Peel face over 3-inch drum
3. Record peel force
4. Calculate peel strength

**Data Required:**
- Peel strength (N/m)
- Failure mode
- Consistency along length

### 6. DATA ANALYSIS

#### Statistical Analysis
- Calculate mean and standard deviation
- Identify outliers (>2σ)
- Determine A-basis and B-basis values
- Compare to AI predictions

#### Correlation with AI
- Plot AI predictions vs. test results
- Calculate % difference
- Update uncertainty bands
- Identify need for FEA updates

#### Property Database
- Document all results
- Include failure modes
- Photo documentation
- Environmental conditions

### 7. COST & SCHEDULE

**Budget Breakdown:**
| Item | Cost |
|------|------|
| Materials (prepreg, core, adhesive) | $3,000 |
| Autoclave time (8 hours) | $1,000 |
| Specimen preparation (machining) | $2,000 |
| Testing services | $3,000 |
| Analysis and reporting | $2,000 |
| **Total** | **$11,000** |

**Schedule:**
- Week 1: Material procurement
- Week 2: Panel layup and cure
- Week 3: Specimen preparation
- Week 4: Testing
- Week 5: Analysis and report

**Total Duration:** 5 weeks

### 8. GO/NO-GO CRITERIA

**PROCEED if:**
- ✓ Properties within AI uncertainty bands (±30-40%)
- ✓ Minimum strengths achieved:
  - Face tensile >2000 MPa
  - Core shear >0.8 MPa
  - Bond strength >25 MPa
- ✓ Manufacturing quality acceptable (<5% void content by C-scan)
- ✓ No unexpected failure modes

**STOP if:**
- ✗ Properties <50% of AI predictions
- ✗ Manufacturing defects >5% void content
- ✗ Bond strength inadequate (<20 MPa)
- ✗ Inconsistent results (CV >15%)

**REDESIGN REQUIRED if:**
- Properties significantly different from predictions
- Structural analysis no longer valid
- Weight budget exceeded
- Manufacturing quality issues

### 9. REPORTING

#### Test Report Contents
1. Executive summary
2. Test matrix and procedures
3. Results tables and plots
4. Statistical analysis
5. Comparison to AI predictions
6. Failure mode analysis
7. Recommendations
8. Updated material database

#### Deliverables
- [ ] Certified test report
- [ ] Material property database
- [ ] Failure mode photos
- [ ] Recommendation memo
- [ ] Updated FEA inputs (if needed)

### 10. SUCCESS METRICS

**Technical Success:**
- Properties validated within uncertainty
- Manufacturing process proven
- Quality standards achieved

**Program Success:**
- On schedule (5 weeks)
- On budget ($13k)
- Clear GO/NO-GO decision
- FEA inputs updated

---

**Document Control:** DEM-001-TEST-PLAN-001  
**Revision:** A  
**Date:** 2025-11-03  
**Status:** READY FOR EXECUTION (pending funding)

**Prepared by:** Materials Engineer  
**Reviewed by:** Chief Engineer  
**Approved by:** Program Manager
