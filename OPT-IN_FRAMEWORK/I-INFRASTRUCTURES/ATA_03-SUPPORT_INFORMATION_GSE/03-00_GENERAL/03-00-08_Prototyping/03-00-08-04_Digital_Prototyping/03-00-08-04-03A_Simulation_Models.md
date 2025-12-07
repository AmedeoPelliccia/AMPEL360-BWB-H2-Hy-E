# 03-00-08-04-03A - Simulation Models

## 1. Purpose

This document defines standards and processes for developing and validating simulation models within the AMPEL360-BWB-H2-Hy-E program to support design analysis and virtual testing.

## 2. Scope

This specification covers various simulation disciplines including structural (FEA), fluid dynamics (CFD), multi-body dynamics (MBD), thermal analysis, and system simulation.

## 3. Applicable Documents

- ATA 03-00-08-01-01A_Prototyping_Strategy
- ATA 03-00-06_Engineering
- ATA 03-00-07_V_AND_V
- AIAA Standards for CFD/FEA Validation
- ASME V&V Standards

## 4. Description

### 4.1 Overview

Simulation models enable virtual prototyping, reducing the need for physical tests while providing insights into complex phenomena. High-fidelity simulations support design optimization, failure prediction, and certification compliance.

### 4.2 Requirements

**Simulation Disciplines:**

**Structural Analysis (FEA):**
- Linear and nonlinear stress analysis
- Buckling and stability analysis
- Fatigue and damage tolerance
- Composite failure analysis
- Software: Abaqus, Nastran, Ansys

**Fluid Dynamics (CFD):**
- External aerodynamics (BWB performance)
- Internal flows (cooling, ventilation)
- Propulsion integration
- Icing and environmental effects
- Software: Fluent, Star-CCM+, OpenFOAM

**Multi-Body Dynamics (MBD):**
- Landing gear dynamics
- Flight control kinematics
- Mechanisms and actuators
- Software: Adams, Simpack, RecurDyn

**Thermal Analysis:**
- Steady-state and transient heat transfer
- Cryogenic system thermal performance
- Avionics cooling
- Environmental control systems
- Software: Ansys Thermal, Fluent, Sinda

**System Simulation:**
- Electrical power distribution
- Hydraulic systems
- Flight control systems
- H2 fuel system
- Software: Matlab/Simulink, AMESim, Modelica

### 4.3 Methodology

**Simulation Process:**

1. **Model Definition**
   - Define simulation objectives
   - Specify required accuracy and fidelity
   - Identify boundary conditions and loads
   - Define mesh/discretization requirements

2. **Geometry Preparation**
   - Import CAD geometry
   - Simplify/idealize as appropriate
   - Create mid-surfaces (for shells)
   - Clean and repair geometry

3. **Meshing/Discretization**
   - Generate mesh (FEA) or grid (CFD)
   - Verify mesh quality metrics
   - Perform mesh sensitivity study
   - Document mesh statistics

4. **Material and Property Assignment**
   - Assign material properties
   - Define loads and boundary conditions
   - Specify initial conditions
   - Set solver parameters

5. **Solution Execution**
   - Run simulation
   - Monitor convergence
   - Check for errors/warnings
   - Document solution time and resources

6. **Post-Processing**
   - Extract results of interest
   - Visualize stress, displacement, flow fields, etc.
   - Compare to acceptance criteria
   - Generate plots and animations

7. **Validation**
   - Compare to analytical solutions (where available)
   - Compare to test data
   - Assess uncertainty
   - Document validation basis

**Simulation Quality Standards:**

**Mesh Quality (FEA):**
- Element aspect ratio < 5:1 (10:1 for coarse mesh)
- Jacobian > 0.6
- Warping < 10 degrees
- Minimum 3 elements through thickness

**Grid Quality (CFD):**
- y+ < 1 for viscous wall-resolved
- Skewness < 0.85
- Orthogonal quality > 0.3
- Growth rate < 1.2

**Convergence Criteria:**
- Residuals < 1e-4 (FEA), 1e-6 (CFD)
- Monitored quantities stabilized
- Energy balance within 1%

**Validation Requirements:**
- Model validation against test data
- Error quantification
- Uncertainty analysis
- Documented limitations

## 5. Deliverables

| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Simulation Plan | Document | Analysis Engineer | Pre-simulation |
| Model Description | Document | Analysis Engineer | With results |
| Mesh/Grid Quality Report | Report | Analysis Engineer | With results |
| Results Report | Document | Analysis Engineer | Post-simulation |
| Validation Report | Document | Analysis Engineer | Post-simulation |
| Model Files | Native format | Analysis Engineer | Archive |

## 6. Quality Criteria

**Model Quality:**
- Geometry accurately represents intent
- Mesh/grid quality criteria met
- Material properties verified
- Boundary conditions appropriate
- Convergence achieved

**Results Quality:**
- Results physically reasonable
- Sensitivity to mesh/grid demonstrated
- Uncertainty quantified
- Validation documented
- Peer review completed

**Documentation Quality:**
- Assumptions clearly stated
- Limitations identified
- Traceability to requirements
- Results reproducible

## 7. Cross-References

- Related ATA Chapters: ATA 03-00-06 (Engineering), ATA 03-00-07 (V&V)
- Parent Document: 03-00-08_Prototyping
- Related Engineering Docs: 03-00-06_Engineering
- Related V&V Docs: 03-00-07_V_AND_V

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation WG | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-07.

---
