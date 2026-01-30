# 61-00-06-030_Simulation

## Purpose

This folder contains **simulation campaigns** and their outputs for ATA 61 Propellers/Propulsors, including performance validation, failure mode analysis, and multi-physics coupling studies.

Simulation work provides:
- Performance validation across operating envelope
- Failure mode and effects analysis (FMEA) support
- Digital twin scenario testing
- Evidence for V&V and certification

---

## Scope

Simulation types include:

### Performance Simulations
- Steady-state cruise/climb/descent
- Transient maneuvers (acceleration, windmilling)
- Off-design conditions (icing, degraded performance)
- Multi-point optimization validation

### Failure Mode Simulations
- Motor winding failure (single/multiple phase loss)
- Blade damage or loss scenarios
- Controller failure modes
- Sensor failures and FDI validation
- Icing accumulation and performance degradation

### Multi-Physics Coupling
- Aero-structural (blade deflection effects on aero)
- Aero-thermal (motor cooling with airflow)
- Electro-thermal-mechanical (motor performance + thermal + vibration)

### Sensitivity and Uncertainty Analysis
- Monte Carlo sampling of input uncertainties
- Parameter sweep studies
- Surrogate model validation

---

## Typical Contents

- **Simulation campaign reports** (Markdown with objectives, setup, results)
- **Output datasets** (CSV, HDF5, NetCDF)
- **Plots and visualizations** (SVG, PNG from scripts)
- **Failure mode logs** (timestamped event sequences)
- **Campaign configuration files** (YAML, JSON describing run matrix)
- **Post-processing scripts** (Python, MATLAB)

---

## Workflow

### Running a New Simulation Campaign:

1. **Define campaign objectives and scope**:
   - Create a campaign document: `61-00-06-030-XXX_Campaign_Name.md`
   - Example: `61-00-06-030-001_Cruise_Performance_Campaign.md`

2. **Set up the run matrix**:
   - Define parameter sweep (RPM, altitude, velocity, etc.)
   - Specify failure modes to test
   - Document random seeds for reproducibility

3. **Execute simulations**:
   - Use models from `../61-00-06-020_Models/`
   - Follow tool configurations from `../61-00-06-050_Tools_Config/`
   - Log all runs with timestamps and Git commit hashes

4. **Store outputs**:
   - Raw output files in organized subdirectories
   - Processed datasets (CSV) for traceability
   - Metadata files describing each run

5. **Post-process and visualize**:
   - Generate performance curves
   - Create failure mode timelines
   - Produce comparison plots (analytical vs. simulation)

6. **Document and link**:
   - Write campaign report summarizing results
   - Link to requirements and V&V (`../61-00-06-070_V_AND_V_Linkage/`)
   - Archive raw data to `../61-00-06-060_Data_Artifacts/` if very large

---

## Example Campaign Document Structure

```markdown
# 61-00-06-030-001 — Cruise Performance Campaign

**Document ID:** 61-00-06-030-001  
**Title:** Propeller Cruise Performance Validation Campaign  
**Date:** YYYY-MM-DD  
**Author:** [Name]  

## 1. Objective
Validate propeller performance across cruise envelope using CFD.

## 2. Scope
- Flight conditions: cruise at FL350, Mach 0.78
- RPM range: [X to Y]
- Blade geometry: [version reference]
- Model: 61-00-06-020-001 (CFD Propeller Model)

## 3. Run Matrix
| Run ID | RPM | Altitude (ft) | Mach | Random Seed |
|:---|:---|:---|:---|:---|
| R001 | 2000 | 35000 | 0.78 | 1234 |
| R002 | 2200 | 35000 | 0.78 | 1234 |
| ... | ... | ... | ... | ... |

## 4. Execution
- Solver: [OpenFOAM 9]
- Tool config: `../61-00-06-050_Tools_Config/openfoam_env.yml`
- Execution date: [YYYY-MM-DD]
- Compute resource: [HPC cluster, node count]

## 5. Results
- Performance curves: `cruise_performance_curves.svg`
- Output dataset: `cruise_campaign_results.csv`
- Comparison to analytical: ±X% agreement

## 6. Analysis
[Interpretation, trends, validation against requirements]

## 7. Traceability
- Linked requirement: REQ-61-00-03-XXX
- V&V linkage: 61-00-06-070-YYY

## 8. Files
- Campaign config: `cruise_campaign_config.yaml`
- Post-processing script: `postprocess_cruise.py`
- Output dataset: `cruise_campaign_results.csv`
- Plots: `cruise_performance_curves.svg`
```

---

## Data Organization

Organize simulation outputs by campaign:

```
61-00-06-030_Simulation/
├── 61-00-06-030-001_Cruise_Performance_Campaign.md
├── 61-00-06-030-001_Campaign_Data/
│   ├── cruise_campaign_config.yaml
│   ├── cruise_campaign_results.csv
│   ├── cruise_performance_curves.svg
│   ├── postprocess_cruise.py
│   └── raw_outputs/
│       ├── R001/
│       ├── R002/
│       └── ...
├── 61-00-06-030-002_Motor_Failure_Campaign.md
├── 61-00-06-030-002_Campaign_Data/
│   └── ...
```

---

## File Naming Conventions

| Type | Convention | Example |
|:---|:---|:---|
| Campaign doc | `61-00-06-030-XXX_Campaign_Name.md` | `61-00-06-030-001_Cruise_Performance_Campaign.md` |
| Config file | `campaign_name_config.yaml` | `cruise_campaign_config.yaml` |
| Dataset | `campaign_name_results.csv` | `cruise_campaign_results.csv` |
| Plots | `descriptive_name.svg` | `cruise_performance_curves.svg` |
| Run folders | `RXXX/` | `R001/`, `R002/`, ... |

---

## Standards and References

- **ATA iSpec 2200** — Propulsion system simulation and validation
- **V&V Planning** — Simulation validation against test data
- **DO-178C / DO-254** — Simulation evidence for certification (where applicable)
- **Model-Based Systems Engineering (MBSE)** — Traceability to requirements

---

## Status

- **Lifecycle Stage**: 06 — Engineering
- **Subfolder**: 030 — Simulation
- **Content Status**: Scaffolded (ready for simulation campaigns)
- **Last Updated**: 2025-12-11

---

## Related Folders

- **[../61-00-06-020_Models/](../61-00-06-020_Models/)** — Simulation models used in campaigns
- **[../61-00-06-040_Trade_Studies/](../61-00-06-040_Trade_Studies/)** — Optimization based on simulation results
- **[../61-00-06-050_Tools_Config/](../61-00-06-050_Tools_Config/)** — Tool versions and environment
- **[../61-00-06-060_Data_Artifacts/](../61-00-06-060_Data_Artifacts/)** — Archival of large raw datasets
- **[../61-00-06-070_V_AND_V_Linkage/](../61-00-06-070_V_AND_V_Linkage/)** — Validation traceability

---

## Document Control

- **Standard**: OPT-IN Framework v1.1 (Enhanced Engineering Template)
- **Owner**: AMPEL360 Engineering WG (Simulation Team)
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

*Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.*
