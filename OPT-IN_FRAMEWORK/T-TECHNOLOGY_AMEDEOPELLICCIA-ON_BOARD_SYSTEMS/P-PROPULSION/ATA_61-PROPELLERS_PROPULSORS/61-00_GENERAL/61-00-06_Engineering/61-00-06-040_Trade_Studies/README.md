# 61-00-06-040_Trade_Studies

## Purpose

This folder contains **trade studies** and optimization work for ATA 61 Propellers/Propulsors, supporting design decision-making through comparative analysis and multi-objective optimization.

Trade studies provide:
- Systematic comparison of design alternatives
- Multi-objective optimization (performance, weight, cost, noise)
- Sensitivity analysis and design margin assessment
- Rationale documentation for certification

---

## Scope

Trade study types include:

### Design Alternative Trades
- Propeller diameter vs. efficiency vs. weight
- Blade count and chord distribution
- Motor type selection (PMSM vs. induction vs. switched reluctance)
- Cooling architecture (air-cooled vs. liquid-cooled vs. hybrid)
- Material selection (aluminum vs. carbon fiber vs. hybrid composites)

### Performance Trades
- Power loading vs. disk loading
- Cruise speed vs. propulsive efficiency
- Noise vs. efficiency (tip speed, blade count)
- Thrust capability vs. weight

### System Integration Trades
- Motor placement (nose-mounted vs. distributed)
- Voltage level selection (540V vs. 800V vs. 3000V)
- Redundancy architecture (single vs. dual-motor)
- Control authority vs. actuator weight

---

## Typical Contents

- **Trade study reports** (Markdown with objectives, alternatives, criteria, results)
- **Trade matrices** (CSV tables comparing alternatives)
- **Pareto front plots** (SVG showing multi-objective optimization results)
- **Decision rationale documents** (justification for selected baseline)
- **Sensitivity analysis results** (parameter impact on figures of merit)
- **Cost-benefit analyses** (where applicable)

---

## Workflow

### Conducting a New Trade Study:

1. **Define the trade study**:
   - Create document: `61-00-06-040-XXX_Trade_Name.md`
   - Example: `61-00-06-040-001_Propeller_Diameter_Trade.md`

2. **Identify alternatives and evaluation criteria**:
   - List design alternatives (A, B, C, ...)
   - Define figures of merit (FoMs) and weighting
   - Establish decision framework (e.g., weighted scoring, Pareto dominance)

3. **Gather data**:
   - Use analytical results from `../61-00-06-010_Analysis/`
   - Use simulation results from `../61-00-06-030_Simulation/`
   - Incorporate experimental data where available

4. **Perform comparison**:
   - Create trade matrix (CSV)
   - Generate Pareto plots or spider charts
   - Apply decision criteria

5. **Document decision**:
   - Summarize selected baseline and rationale
   - Document assumptions and sensitivities
   - Highlight residual risks or open items

6. **Link to requirements and design**:
   - Trace to requirements (`61-00-03_Requirements/`)
   - Update design documentation (`61-00-04_Design/`)
   - Create V&V linkage (`../61-00-06-070_V_AND_V_Linkage/`)

---

## Example Trade Study Document Structure

```markdown
# 61-00-06-040-001 — Propeller Diameter Trade Study

**Document ID:** 61-00-06-040-001  
**Title:** Trade Study: Propeller Diameter Selection  
**Date:** YYYY-MM-DD  
**Author:** [Name]  

## 1. Objective
Select optimal propeller diameter balancing efficiency, weight, and integration constraints.

## 2. Scope
- Aircraft: AMPEL360 BWB-H2-Hy-E
- Mission: Cruise at Mach 0.78, FL350
- Constraints: nacelle clearance, structural limits

## 3. Design Alternatives
| Alternative | Diameter (m) | Blade Count | Tip Speed (m/s) |
|:---|:---|:---|:---|
| A | 3.0 | 4 | 250 |
| B | 3.5 | 4 | 250 |
| C | 4.0 | 5 | 230 |

## 4. Evaluation Criteria (Figures of Merit)
| FoM | Weight | Target |
|:---|:---|:---|
| Cruise efficiency (%) | 40% | Maximize |
| Weight (kg) | 30% | Minimize |
| Noise (EPNdB) | 20% | Minimize |
| Cost (relative) | 10% | Minimize |

## 5. Data Sources
- Efficiency: CFD analysis (61-00-06-030-001)
- Weight: Structural sizing (61-00-06-010-002)
- Noise: Analytical model (61-00-06-010-003)
- Cost: Supplier quotes + scaling model

## 6. Trade Matrix
[Link to CSV file: `propeller_diameter_trade_matrix.csv`]

## 7. Results
- Pareto plot: `propeller_diameter_pareto.svg`
- Weighted score:
  - Alternative A: 72
  - Alternative B: 85 (SELECTED)
  - Alternative C: 78

## 8. Decision Rationale
Alternative B selected for:
- Best weighted score
- Acceptable structural margin
- Meets noise limits with margin
- Compatible with nacelle envelope

## 9. Sensitivity Analysis
- ±10% blade weight: ±3 points in score
- ±5% efficiency: ±7 points in score
- Most sensitive to efficiency assumption

## 10. Traceability
- Linked requirement: REQ-61-00-03-XXX (propeller efficiency)
- Design update: 61-00-04-YYY (propeller baseline)
- V&V linkage: 61-00-06-070-ZZZ

## 11. Files
- Trade matrix: `propeller_diameter_trade_matrix.csv`
- Pareto plot: `propeller_diameter_pareto.svg`
- Sensitivity data: `diameter_sensitivity.csv`
```

---

## Data Organization

Organize trade studies with supporting files:

```
61-00-06-040_Trade_Studies/
├── 61-00-06-040-001_Propeller_Diameter_Trade.md
├── 61-00-06-040-001_Data/
│   ├── propeller_diameter_trade_matrix.csv
│   ├── propeller_diameter_pareto.svg
│   └── diameter_sensitivity.csv
├── 61-00-06-040-002_Motor_Type_Trade.md
├── 61-00-06-040-002_Data/
│   └── ...
```

---

## File Naming Conventions

| Type | Convention | Example |
|:---|:---|:---|
| Trade doc | `61-00-06-040-XXX_Trade_Name.md` | `61-00-06-040-001_Propeller_Diameter_Trade.md` |
| Trade matrix | `trade_name_matrix.csv` | `propeller_diameter_trade_matrix.csv` |
| Pareto plot | `trade_name_pareto.svg` | `propeller_diameter_pareto.svg` |
| Sensitivity | `trade_name_sensitivity.csv` | `diameter_sensitivity.csv` |

---

## Standards and References

- **ATA iSpec 2200** — Propulsion system design documentation
- **Systems Engineering Best Practices** — Trade study frameworks
- **Multi-Objective Optimization** — Pareto analysis methods
- **EASA CS-25 / FAA FAR 25** — Certification requirements influencing trades

---

## Status

- **Lifecycle Stage**: 06 — Engineering
- **Subfolder**: 040 — Trade Studies
- **Content Status**: Scaffolded (ready for trade study work)
- **Last Updated**: 2025-12-11

---

## Related Folders

- **[../61-00-06-010_Analysis/](../61-00-06-010_Analysis/)** — Analytical data for trade studies
- **[../61-00-06-030_Simulation/](../61-00-06-030_Simulation/)** — Simulation data for trade comparisons
- **[../../61-00-03_Requirements/](../../61-00-03_Requirements/)** — Requirements traced to trade decisions
- **[../../61-00-04_Design/](../../61-00-04_Design/)** — Design baseline updated by trade studies
- **[../61-00-06-070_V_AND_V_Linkage/](../61-00-06-070_V_AND_V_Linkage/)** — Validation of trade study assumptions

---

## Document Control

- **Standard**: OPT-IN Framework v1.1 (Enhanced Engineering Template)
- **Owner**: AMPEL360 Engineering WG (Systems Engineering Team)
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

*Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.*
