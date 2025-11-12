# Landing Gear Height Trade Study

**Trade Study ID:** 02-11-00-TS-001  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Status:** Draft  
**Date:** 2025-11-10

---

## 1. Objective

Determine optimal landing gear height balancing:
- Ground clearance requirements
- Gear structural weight
- Gear bay volume and integration
- Rotation angle capability

---

## 2. Requirements and Constraints

### 2.1 Ground Clearance Requirements (CS-25.477)
- **Tail-down angle:** ≥ 10° at MLW with aft CG
- **Tip-over angle:** ≥ 25° lateral
- **Belly clearance:** ≥ 0.5 m static level
- **Rotation clearance:** ≥ 0.3 m during take-off rotation

### 2.2 Constraints
- **Wheelbase:** 18.0 m (NLG to MLG)
- **Center body depth:** 4.2 m
- **Wing box depth at root:** 1.8 m

---

## 3. Options Evaluated

| Option | MLG Height (m) | NLG Height (m) | Belly Clearance (m) | Tail-Down Angle (°) | Est. Gear Weight (kg) |
|--------|----------------|----------------|---------------------|---------------------|----------------------|
| A | 2.8 | 2.4 | 0.55 | 8.5 | 4,200 |
| B | 3.0 | 2.6 | 0.65 | 9.2 | 4,450 |
| C | 3.2 | 2.8 | 0.85 | 10.1 | 4,750 |
| D | 3.5 | 3.0 | 1.05 | 11.2 | 5,200 |

---

## 4. Evaluation Criteria

### 4.1 Ground Clearance (Weight: 40%)

| Option | Static Clearance | Rotation Clearance | Tail-Down Angle | Score (1-10) |
|--------|------------------|-------------------|----------------|--------------|
| A | Marginal (0.55 m) | Marginal (0.25 m) | Below req (8.5°) | 4 |
| B | Acceptable (0.65 m) | Acceptable (0.32 m) | Marginal (9.2°) | 6 |
| C | Good (0.85 m) | Good (0.42 m) | Meets req (10.1°) | 9 |
| D | Excellent (1.05 m) | Excellent (0.58 m) | Exceeds req (11.2°) | 10 |

### 4.2 Structural Weight (Weight: 30%)

| Option | Gear Weight (kg) | % of OEW | Score (1-10) |
|--------|------------------|----------|--------------|
| A | 4,200 | 3.5% | 10 |
| B | 4,450 | 3.7% | 8 |
| C | 4,750 | 4.0% | 6 |
| D | 5,200 | 4.3% | 4 |

**Note:** Gear weight increases approximately as height^2.5 due to increased bending moments.

### 4.3 Integration and Complexity (Weight: 20%)

| Option | Bay Volume Impact | Wing Box Integration | Retraction Kinematics | Score (1-10) |
|--------|-------------------|----------------------|-----------------------|--------------|
| A | Minimal | Easy fit | Simple | 10 |
| B | Low | Good fit | Simple | 9 |
| C | Moderate | Acceptable | Moderate complexity | 7 |
| D | High | Challenging | Complex kinematics | 5 |

### 4.4 Operational Flexibility (Weight: 10%)

| Option | Rough Field Ops | Service/Maintenance Access | Score (1-10) |
|--------|-----------------|----------------------------|--------------|
| A | Limited | Good | 6 |
| B | Acceptable | Good | 7 |
| C | Good | Excellent | 9 |
| D | Excellent | Excellent | 10 |

---

## 5. Scoring Summary

| Option | Ground Clearance (40%) | Weight (30%) | Integration (20%) | Operational (10%) | **Total Score** |
|--------|------------------------|--------------|-------------------|-------------------|-----------------|
| A | 1.6 | 3.0 | 2.0 | 0.6 | **7.2** |
| B | 2.4 | 2.4 | 1.8 | 0.7 | **7.3** |
| C | 3.6 | 1.8 | 1.4 | 0.9 | **7.7** ✓ |
| D | 4.0 | 1.2 | 1.0 | 1.0 | **7.2** |

---

## 6. Sensitivity Analysis

### 6.1 Weight Penalty Sensitivity

If gear weight impact is increased to 40% (equal to ground clearance):
- Option C still scores highest (7.3)
- Option B becomes closer competitor (7.1)

### 6.2 Clearance Requirement Sensitivity

If tail-down angle requirement reduced to 9° (less conservative):
- Option B becomes acceptable
- However, Option C still preferred for margin

---

## 7. Risk Assessment

| Option | Technical Risk | Programmatic Risk | Overall Risk |
|--------|----------------|-------------------|--------------|
| A | High (marginal clearance) | Low (minimal weight) | High |
| B | Medium (low margin) | Low | Medium |
| C | Low (adequate margin) | Low | **Low** ✓ |
| D | Low (excessive margin) | Medium (weight/integration) | Medium |

---

## 8. Recommendation

**Selected Option: C (MLG 3.2 m, NLG 2.8 m)**

### 8.1 Rationale

- **Meets all CS-25.477 requirements** with adequate margin (tail-down angle 10.1°)
- **Acceptable weight penalty** (4,750 kg, 4.0% of OEW)
- **Good ground clearance** (0.85 m belly clearance, 0.42 m rotation clearance)
- **Manageable integration** into wing box and center body
- **Lowest overall risk** profile

### 8.2 Trade-Off Justification

Option C provides the best balance between:
- Safety (adequate clearances)
- Weight efficiency (reasonable gear weight)
- Technical maturity (proven gear design)
- Operational flexibility (good rough field capability)

### 8.3 Design Margin

- Tail-down angle: 10.1° (1% margin above 10° requirement)
- Belly clearance: 0.85 m (70% margin above 0.5 m requirement)
- Rotation clearance: 0.42 m (40% margin above 0.3 m requirement)

---

## 9. Next Steps

- [ ] Detailed landing gear design (strut sizing, wheel selection)
- [ ] Gear bay integration study (doors, hydraulics, routing)
- [ ] Landing gear loads analysis (CS-25.471 through CS-25.511)
- [ ] Ground clearance verification with dynamic simulation
- [ ] Kinematic analysis of retraction/extension sequence

---

## 10. References

- CS-25.477 – Landing Gear Arrangement
- `ANALYSIS_REPORTS/CLEARANCE/Ground_Clearance_Calculations.md`
- `ANALYSIS_REPORTS/STRUCTURAL/Landing_Gear_Loads.md`
- `04_DESIGN/STRUCTURAL_DESIGN/Landing_Gear_Design.md`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Author:** Landing Gear Design Team
- **Reviewed by:** Chief Structural Engineer, Chief Aerodynamicist
- **Approved by:** Program Chief Engineer
- **Date:** 2025-11-10
