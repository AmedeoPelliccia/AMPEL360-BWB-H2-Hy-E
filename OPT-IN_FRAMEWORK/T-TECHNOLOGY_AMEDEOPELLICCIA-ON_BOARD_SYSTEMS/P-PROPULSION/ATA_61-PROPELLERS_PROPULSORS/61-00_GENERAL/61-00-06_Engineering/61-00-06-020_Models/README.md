# 61-00-06-020_Models

## Purpose

This folder contains **simulation-ready models** and computational frameworks for ATA 61 Propellers/Propulsors, including CFD meshes, FEM models, control algorithms, and I/O schemas.

Models serve as the foundation for:
- High-fidelity simulation campaigns
- Multi-physics coupling analyses
- Digital twin development
- Hardware-in-the-loop (HIL) testing

---

## Scope

Model types include:

### Computational Fluid Dynamics (CFD) Models
- Propeller blade geometry (CAD-derived)
- Mesh generation (structured/unstructured)
- Boundary condition definitions
- Turbulence model selection
- Moving reference frame setup

### Finite Element Method (FEM) Models
- Blade structural mesh
- Motor housing and mounting structure
- Material property definitions
- Boundary conditions and loads
- Contact definitions

### Control System Models
- Motor control algorithms (Python, Simulink, etc.)
- Propeller governor logic
- Fault detection and isolation (FDI)
- Sensor fusion and estimation

### I/O Schemas and Data Contracts
- Model input/output definitions (JSON, YAML)
- Interface Control Documents (ICDs)
- Data validation schemas
- Unit and coordinate system conventions

---

## Typical Contents

- **CFD model files** (`.msh`, `.cgns`, setup scripts)
- **FEM model files** (`.inp`, `.bdf`, material libraries)
- **Control code** (`.py`, `.m`, `.slx`)
- **I/O schemas** (`.json`, `.yaml`, `.xml`)
- **Model documentation** (Markdown with equations, assumptions, validation)
- **Model version logs** (Git-tracked)

---

## Workflow

### Adding New Models:

1. **Create a descriptive Markdown document**:
   - Format: `61-00-06-020-XXX_Model_Name.md`
   - Example: `61-00-06-020-001_CFD_Propeller_Model.md`

2. **Document the model**:
   - Purpose and scope
   - Geometry and mesh details
   - Boundary conditions and physics
   - Solver settings and convergence criteria
   - Validation against analytical/experimental data
   - Known limitations

3. **Store model files**:
   - Use version control (Git LFS for large files if needed)
   - Follow naming conventions: `model_name_vX.Y.ext`
   - Include setup/run scripts alongside model files

4. **Define I/O schemas**:
   - Document input parameters (units, ranges, defaults)
   - Document output quantities (units, accuracy, post-processing)
   - Provide example input/output files

5. **Update traceability**:
   - Link to requirements (`61-00-03_Requirements/`)
   - Link to design (`61-00-04_Design/`)
   - Link to analytical basis (`../61-00-06-010_Analysis/`)
   - Create simulation campaign references (`../61-00-06-030_Simulation/`)

---

## Example Document Structure

```markdown
# 61-00-06-020-001 — CFD Propeller Model

**Document ID:** 61-00-06-020-001  
**Title:** CFD Model of ATA 61 Propeller  
**Date:** YYYY-MM-DD  
**Author:** [Name]  

## 1. Purpose
High-fidelity aerodynamic simulation of propeller performance.

## 2. Scope
- Blade geometry: [reference to CAD]
- Operating conditions: [cruise, climb, etc.]
- Solver: [OpenFOAM / ANSYS Fluent / etc.]

## 3. Geometry and Mesh
- Blade geometry: [source, version]
- Domain extent: [X × Y × Z meters]
- Mesh size: [N cells, refinement zones]
- Mesh quality: [orthogonality, skewness metrics]

## 4. Physics and Boundary Conditions
- Turbulence model: [k-ω SST, LES, etc.]
- Moving reference frame: [RPM, axis]
- Inlet: [velocity, turbulence intensity]
- Outlet: [pressure]
- Walls: [no-slip, roughness]

## 5. Solver Settings
- Solver: [steady-state / transient]
- Discretization: [2nd order upwind, etc.]
- Convergence criteria: [residuals < 1e-5]

## 6. Validation
- Comparison to analytical BEMT model: [±X%]
- Comparison to wind tunnel data: [±Y%]

## 7. I/O Schema
- Inputs: [RPM, freestream velocity, altitude]
- Outputs: [thrust, torque, efficiency, flow field]

## 8. Files
- Mesh: `propeller_mesh_v1.0.msh`
- Setup script: `setup_cfd_run.py`
- Post-processing: `postprocess_results.py`

## 9. Traceability
- Linked requirement: REQ-61-00-03-XXX
- Linked design doc: 61-00-04-YYY
- Analytical basis: 61-00-06-010-ZZZ
- Simulation campaigns: 61-00-06-030-AAA
```

---

## File Naming Conventions

| Type | Convention | Example |
|:---|:---|:---|
| Python code | `snake_case.py` | `propeller_control.py` |
| MATLAB/Simulink | `CamelCase.m` / `.slx` | `MotorController.m` |
| CFD mesh | `descriptive_name_vX.Y.ext` | `propeller_mesh_v1.0.msh` |
| FEM model | `descriptive_name_vX.Y.ext` | `blade_structure_v2.1.inp` |
| I/O schema | `schema_name.json` | `propeller_io_schema.json` |

---

## Standards and References

- **ATA iSpec 2200** — Propulsion system models
- **AIAA Turbulence Model Best Practices** — CFD turbulence modeling
- **NAFEMS FEM Benchmarks** — Structural model validation
- **Model-Based Systems Engineering (MBSE)** — Traceability and version control
- **DO-178C / DO-254** — Software/hardware model verification (where applicable)

---

## Status

- **Lifecycle Stage**: 06 — Engineering
- **Subfolder**: 020 — Models
- **Content Status**: Scaffolded (ready for model development)
- **Last Updated**: 2025-12-11

---

## Related Folders

- **[../61-00-06-010_Analysis/](../61-00-06-010_Analysis/)** — Analytical foundation for models
- **[../61-00-06-030_Simulation/](../61-00-06-030_Simulation/)** — Simulation campaigns using these models
- **[../61-00-06-050_Tools_Config/](../61-00-06-050_Tools_Config/)** — Tool versions and environment setup
- **[../61-00-06-060_Data_Artifacts/](../61-00-06-060_Data_Artifacts/)** — CAD geometry and raw data sources

---

## Document Control

- **Standard**: OPT-IN Framework v1.1 (Enhanced Engineering Template)
- **Owner**: AMPEL360 Engineering WG (CFD/FEM/Controls Teams)
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

*Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.*
