# 61-00-06-010_Analysis

## Purpose

This folder contains **analytical models and studies** for ATA 61 Propellers/Propulsors, covering aerodynamic, structural, thermal, electromagnetic, and vibro-acoustic analyses.

Analytical work provides the foundation for:
- Initial design parameter estimation
- Feasibility validation
- Performance envelope definition
- Design limit calculations

---

## Scope

Analytical methods include:

### Aerodynamic Analysis
- Blade Element Momentum Theory (BEMT) models
- Actuator disk models
- Propeller efficiency and thrust calculations
- Tip speed and Mach number effects
- Slipstream and wake analysis

### Structural Analysis
- Blade stress and deflection (beam theory, hand calculations)
- Fatigue life estimation (S-N curves, Miner's rule)
- Modal analysis (natural frequencies, flutter assessment)
- Material property evaluation

### Thermal Analysis
- Motor thermal models (lumped-parameter networks)
- Cooling system heat transfer calculations
- Steady-state and transient thermal response
- Hot-spot identification

### Electromagnetic Analysis
- Motor torque-speed characteristics
- Efficiency maps
- Power electronics loss estimation
- EMI/EMC preliminary assessment

### Noise and Vibration Analysis
- Propeller tonal noise (blade-passing frequency)
- Broadband noise estimation
- Vibration transmission to airframe
- Resonance identification

---

## Analysis Documents

- **[61-00-06-010-001A — Methodology Overview](./61-00-06-010-001A_Methodology.md)**  
  Global analysis framework, workflows, toolchain, and QA for ATA 61-00-06-010.

- **[61-00-06-010-002A — Thrust & Altitude Performance Models](./61-00-06-010-002A_Thrust_Altitude_Performance_Models.md)**  
  Thrust/power vs. altitude & Mach, thrust decks, and envelope definition.

- **[61-00-06-010-003A — CFD & BLI Envelope Analysis](./61-00-06-010-003A_CFD_BLI_Envelope_Analysis.md)**  
  CFD methodology for BLI, mesh standards, and airframe–propulsor interaction.

- **61-00-06-010-004A — Structural Mounts FEM Methodology (Q100)**  
  FEM strategy for mounts and integration structure, loads, and margins.

- **[61-00-06-010-005A — Acoustic Signature Analysis (Q100)](./61-00-06-010-005A_Acoustic_Signature_Analysis_Q100.md)**  
  Acoustic methodology (external & cabin), source decomposition, metrics registry, case matrix, and acceptance criteria for the Q100 distributed BLI propulsion system.

---

## Typical Contents

- **Analytical reports** (Markdown documents with equations and results)
- **Calculation spreadsheets** (CSV tables, not Excel)
- **Performance curves** (CSV data + SVG plots)
- **Sensitivity studies** (parameter sweeps, uncertainty analysis)
- **Design limit calculations** (structural, thermal, aero)
- **References to analytical methods** (standards, textbooks, papers)

---

## Workflow

### Adding New Analysis Work:

1. **Create a descriptive Markdown document**: 
   - Format: `61-00-06-010-XXX_Descriptive_Analysis_Name.md`
   - Example: `61-00-06-010-001_Blade_Stress_Analysis.md`

2. **Document clearly**:
   - Objective and scope
   - Assumptions and limitations
   - Input parameters and sources
   - Analytical method and equations
   - Results and interpretation
   - References

3. **Store supporting data**:
   - CSV files for tabular data
   - SVG files for plots and diagrams
   - Link to external references

4. **Update traceability**:
   - Link to requirements in `61-00-03_Requirements/`
   - Link to design decisions in `61-00-04_Design/`
   - Create V&V linkage entry in `../61-00-06-070_V_AND_V_Linkage/`

---

## Example Document Structure

```markdown
# 61-00-06-010-001 — Blade Stress Analysis

**Document ID:** 61-00-06-010-001  
**Title:** Propeller Blade Stress Analysis  
**Date:** YYYY-MM-DD  
**Author:** [Name]  

## 1. Objective
Estimate maximum blade stress under cruise conditions.

## 2. Scope
- Blade geometry: [reference]
- Operating condition: cruise at [RPM], [altitude]
- Material: [carbon fiber composite]

## 3. Assumptions
- Beam theory valid (slender blade)
- Linear elastic material
- Quasi-steady loading

## 4. Method
[Equations, references to textbooks/standards]

## 5. Input Parameters
[Table with parameter values and sources]

## 6. Results
[Stress distribution, max stress value, margin]

## 7. Interpretation
[Discussion, comparison to allowables]

## 8. References
[Standards, textbooks, prior analyses]

## 9. Traceability
- Linked requirement: REQ-61-00-03-XXX
- Linked design doc: 61-00-04-YYY
- V&V linkage: 61-00-06-070-ZZZ
```

---

## Standards and References

- **ATA iSpec 2200** — Propulsion system documentation
- **ESDU Data Sheets** — Aerodynamic and structural methods
- **NASA Technical Reports** — Propeller design and analysis
- **EASA CS-25** — Structural and aero certification basis
- **Relevant textbooks** (e.g., Leishman "Principles of Helicopter Aerodynamics")

---

## Status

- **Lifecycle Stage**: 06 — Engineering
- **Subfolder**: 010 — Analysis
- **Content Status**: Scaffolded (ready for analytical work)
- **Last Updated**: 2025-12-12

---

## Related Folders

- **[../61-00-06-020_Models/](../61-00-06-020_Models/)** — Simulation models derived from analysis
- **[../61-00-06-030_Simulation/](../61-00-06-030_Simulation/)** — Higher-fidelity validation of analytical results
- **[../61-00-06-040_Trade_Studies/](../61-00-06-040_Trade_Studies/)** — Comparative analysis and optimization
- **[../61-00-06-070_V_AND_V_Linkage/](../61-00-06-070_V_AND_V_Linkage/)** — Traceability to V&V

---

## Document Control

- **Standard**: OPT-IN Framework v1.1 (Enhanced Engineering Template)
- **Owner**: AMPEL360 Engineering WG (Aero/Structures/Thermal Teams)
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

*Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.*
