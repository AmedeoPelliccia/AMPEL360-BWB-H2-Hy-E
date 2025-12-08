# 03-50-07-04A - Corrosion Inspection

## 1. Purpose
Specification for corrosion inspection and assessment of Ground Support Equipment (GSE) structures to detect, quantify, and evaluate corrosion damage for continued safe operation.

## 2. Scope
- Corrosion types and identification
- Corrosion inspection methods
- Corrosion measurement and quantification
- Corrosion rate assessment
- Remaining life estimation
- Corrosion control and prevention

## 3. Applicable Documents
- NACE SP0169 (Control of External Corrosion on Underground or Submerged Metallic Piping Systems)
- ASTM G1 (Preparing, Cleaning, and Evaluating Corrosion Test Specimens)
- ISO 8501-1 (Preparation of Steel Substrates Before Application of Paints and Related Products)
- API 571 (Damage Mechanisms Affecting Fixed Equipment in the Refining Industry)
- SSPC-VIS 1 (Visual Standard for Abrasive Blast Cleaned Steel)

## 4. Structural Description

### 4.1 Corrosion Types
| Type | Appearance | Typical Location | Severity |
|------|-----------|------------------|----------|
| General (Uniform) | Even metal loss across surface | Exterior surfaces, unprotected steel | Moderate |
| Pitting | Localized deep holes | Stainless steel, aluminum, under deposits | High (stress concentration) |
| Crevice | Corrosion in tight spaces | Lap joints, gaskets, under fasteners | High |
| Galvanic | Accelerated at dissimilar metal contact | SS-steel joints, Al-steel | Moderate to High |
| Stress Corrosion Cracking (SCC) | Cracks in corrosive environment + stress | Welds, cold-worked areas (SS, Al) | Critical |
| Corrosion Fatigue | Cracks from cyclic loading + corrosion | High-stress areas, corrosive environment | Critical |
| Corrosion Under Insulation (CUI) | Hidden under insulation | Piping, vessels with insulation | High (hidden) |

### 4.2 Inspection Methods
| Method | Application | Measurement | Notes |
|--------|-------------|-------------|-------|
| Visual Inspection | General corrosion, pitting | Qualitative (rust grade) | First step |
| Ultrasonic Thickness (UT) | Wall thickness measurement | Quantitative (mm) | Remaining thickness |
| Pit Depth Gauge | Pitting corrosion | Depth (mm) | Direct measurement |
| Corrosion Coupon | Corrosion rate monitoring | Weight loss (g/m²/yr) | Requires installation |
| Electrochemical (LPR) | Real-time corrosion rate | Corrosion rate (mm/yr) | Requires probe |
| Coating Thickness Gauge | Coating integrity | Thickness (µm) | Prevent corrosion |

### 4.3 Corrosion Quantification
- **General Corrosion**: Measure average thickness loss (t_original - t_remaining)
- **Pitting**: Measure pit depth and diameter; pit density (pits/cm²)
- **Crevice**: Measure depth of attack, extent of affected area
- **SCC**: Crack detection methods (PT, MT), crack length/depth
- **Corrosion Rate**: Calculate from thickness measurements over time:
  **CR = (t₁ - t₂) / Δt** (mm/year)

### 4.4 Acceptance Criteria
| Corrosion Type | Acceptance | Action |
|----------------|------------|--------|
| General, loss < corrosion allowance (3 mm) | Acceptable | Monitor |
| General, loss > corrosion allowance | Engineering evaluation | Assess remaining life |
| Pitting, depth < 2× corrosion allowance | Acceptable | Monitor |
| Pitting, depth > 2× corrosion allowance | Engineering evaluation | Repair or replace |
| SCC, any crack | Reject | Immediate action |
| Coating damage < 5% area | Acceptable | Repair coating |
| Coating damage > 5% area | Repair required | Prevent further corrosion |

### 4.5 Remaining Life Assessment
**Formula**: Remaining Life (years) = t_remaining / CR
- t_remaining = t_current - t_minimum (corrosion allowance)
- CR = corrosion rate (mm/year)
- **Example**: Current thickness 10 mm, minimum 7 mm, CR = 0.2 mm/yr
  → Remaining Life = (10-7)/0.2 = 15 years

## 5. Structural Requirements

### 5.1 Inspection Frequency
| Environment | Corrosion Rate | Inspection Interval |
|-------------|---------------|---------------------|
| Indoor, dry | Very low (<0.01 mm/yr) | 10 years |
| Outdoor, temperate | Low (0.01-0.1 mm/yr) | 5 years |
| Marine/coastal | Moderate (0.1-0.5 mm/yr) | 2 years |
| Aggressive (chemical, CUI) | High (>0.5 mm/yr) | Annual |
| H2 Service (SCC risk) | Variable | Annual |

### 5.2 Inspection Procedure
1. **Visual Examination**: Overall condition, rust grading (per ISO 8501-1)
2. **Thickness Measurement**: UT at predefined locations (grid pattern)
3. **Pit/Crevice Inspection**: Identify and measure localized corrosion
4. **Coating Inspection**: Check for damage, blistering, delamination
5. **Documentation**: Record findings, photos, thickness data
6. **Evaluation**: Compare to previous inspections, calculate corrosion rate
7. **Recommendation**: Accept, monitor, repair coating, or structural repair

### 5.3 Corrosion Control
| Method | Application | Effectiveness | Cost |
|--------|-------------|---------------|------|
| Protective Coatings | All exposed surfaces | High (if maintained) | Moderate |
| Cathodic Protection | Buried/submerged structures | Very high | Moderate to High |
| Corrosion Inhibitors | Internal piping, closed systems | Moderate | Low to Moderate |
| Material Selection | Design phase (SS, Al, galvanized) | Very high | High (initial) |
| Drainage/Ventilation | Prevent moisture accumulation | Moderate | Low |
| Regular Cleaning | Remove deposits, salts | Moderate | Low |

### 5.4 H2-Specific Corrosion Considerations
- Stainless steel and aluminum generally resistant to H2 corrosion
- Concern: Stress Corrosion Cracking (SCC) in austenitic SS under stress
- Inspection focus: Welds, cold-worked areas, high-stress regions
- Prevention: Proper material selection, stress relief, corrosion-resistant coatings

## 6. Cross-References
- Parent Document: 03-50_Structures
- Related: 03-50-07-01A (Visual Inspection), 03-50-07-02A (NDT Methods), 03-50-08 (GSE Structural Repair)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-07-04A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
