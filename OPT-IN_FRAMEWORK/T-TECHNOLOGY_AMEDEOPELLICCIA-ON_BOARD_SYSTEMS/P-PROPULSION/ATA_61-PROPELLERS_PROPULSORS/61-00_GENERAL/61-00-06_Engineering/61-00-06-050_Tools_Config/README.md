# 61-00-06-050_Tools_Config

## Purpose

This folder contains **tool configurations and environment management** for ATA 61 Propellers/Propulsors engineering work, ensuring reproducible analyses, simulations, and model development.

Tool configuration management provides:
- Reproducible computational environments
- Version-controlled dependencies
- Solver configuration templates
- Random seed and initialization management
- Tool installation and setup guides

---

## Scope

Tool and configuration types include:

### Computational Environment Management
- Python virtual environments (`requirements.txt`, `environment.yml`)
- MATLAB/Simulink version specifications
- Compiler and library dependencies
- Operating system requirements

### Solver Configurations
- CFD solver settings (convergence criteria, discretization schemes)
- FEM solver options (element types, solution methods)
- Optimization algorithm settings (tolerances, iteration limits)
- Random number generator seeds

### Tool Installation Guides
- Step-by-step setup instructions
- License configuration (where applicable)
- Verification/validation of installation
- Troubleshooting common issues

### Configuration Templates
- Reusable solver input decks
- Baseline configurations for common cases
- Pre-configured job scripts (HPC clusters)

---

## Typical Contents

- **`requirements.txt`** — Python package dependencies
- **`environment.yml`** — Conda environment specification
- **Tool version logs** — Record of tool versions used in analyses
- **Solver configuration files** (`.cfg`, `.json`, `.yaml`)
- **Installation guides** (Markdown documents)
- **Job submission scripts** (`.sh`, `.pbs`, `.slurm`)
- **Random seed registry** — Centralized random seed management

---

## Workflow

### Setting Up a New Tool Environment:

1. **Document tool requirements**:
   - Create: `61-00-06-050-XXX_Tool_Setup_Guide.md`
   - Example: `61-00-06-050-001_OpenFOAM_Setup.md`

2. **Specify dependencies**:
   - For Python: create `requirements.txt` or `environment.yml`
   - For other tools: document version and dependencies in Markdown

3. **Provide installation instructions**:
   - OS-specific steps (Linux, Windows, macOS)
   - Verification commands
   - Known issues and workarounds

4. **Create baseline configurations**:
   - Template solver input files
   - Document key parameters and their effects
   - Provide examples for common use cases

5. **Version control**:
   - Track all configuration files in Git
   - Use semantic versioning for major changes
   - Document changes in tool version log

---

## Example Tool Setup Document Structure

```markdown
# 61-00-06-050-001 — OpenFOAM Setup Guide

**Document ID:** 61-00-06-050-001  
**Title:** OpenFOAM Installation and Configuration for ATA 61  
**Date:** YYYY-MM-DD  
**Author:** [Name]  

## 1. Purpose
Provide reproducible OpenFOAM environment for propeller CFD simulations.

## 2. Tool Information
- Tool: OpenFOAM
- Version: 9 (or OpenFOAM-v2206)
- License: GPL / ESI
- Platform: Linux (Ubuntu 20.04 LTS or later)

## 3. Installation Steps

### 3.1 System Requirements
- OS: Ubuntu 20.04 LTS
- RAM: 16+ GB
- Disk: 50+ GB free

### 3.2 Install Dependencies
```bash
sudo apt-get update
sudo apt-get install build-essential flex bison cmake git-core
```

### 3.3 Install OpenFOAM
[Detailed steps or reference to official docs]

### 3.4 Verify Installation
```bash
source /opt/openfoam9/etc/bashrc
foamVersion
```

Expected output: `OpenFOAM-9`

## 4. Configuration Files

### 4.1 Baseline Solver Configuration
File: `baseline_steady_simpleFoam.cfg`

Key parameters:
- Turbulence model: `kOmegaSST`
- Discretization: `Gauss linear` (gradients), `upwind` (convection)
- Convergence: Residuals < 1e-5

### 4.2 HPC Job Script
File: `run_openfoam_hpc.sh`
```bash
#!/bin/bash
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=32
#SBATCH --time=24:00:00
source /opt/openfoam9/etc/bashrc
mpirun -np 128 simpleFoam -parallel
```

## 5. Random Seed Management
Not applicable for steady-state RANS simulations.
For LES/DES: see `random_seed_registry.csv`

## 6. Troubleshooting
[Common issues and solutions]

## 7. Traceability
- Used in: 61-00-06-020-001 (CFD Propeller Model)
- Used in: 61-00-06-030-001 (Cruise Performance Campaign)
```

---

## Python Environment Example

**File: `requirements.txt`**
```
# Python dependencies for ATA 61 engineering work
numpy==1.24.3
scipy==1.10.1
matplotlib==3.7.1
pandas==2.0.2
pyyaml==6.0
h5py==3.8.0
```

**File: `environment.yml`**
```yaml
name: ata61-engineering
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy=1.24
  - scipy=1.10
  - matplotlib=3.7
  - pandas=2.0
  - pyyaml=6.0
  - h5py=3.8
  - pytest=7.3
```

---

## Random Seed Registry

**File: `random_seed_registry.csv`**
```csv
Study_ID,Purpose,Seed_Value,Date,Notes
61-00-06-030-001,Cruise performance Monte Carlo,1234,2025-12-11,Baseline seed
61-00-06-030-002,Motor failure simulation,5678,2025-12-15,Different from baseline
```

---

## File Naming Conventions

| Type | Convention | Example |
|:---|:---|:---|
| Setup guide | `61-00-06-050-XXX_Tool_Setup_Guide.md` | `61-00-06-050-001_OpenFOAM_Setup.md` |
| Python deps | `requirements.txt` or `environment.yml` | `requirements.txt` |
| Solver config | `descriptive_name.cfg` | `baseline_steady_simpleFoam.cfg` |
| HPC script | `run_toolname_hpc.sh` | `run_openfoam_hpc.sh` |
| Seed registry | `random_seed_registry.csv` | `random_seed_registry.csv` |

---

## Standards and References

- **Python Packaging** — PEP 440 (version specifiers)
- **Conda Environments** — Reproducible scientific computing
- **HPC Best Practices** — Job submission and resource management
- **Model-Based Systems Engineering (MBSE)** — Configuration management and traceability

---

## Status

- **Lifecycle Stage**: 06 — Engineering
- **Subfolder**: 050 — Tools & Configuration
- **Content Status**: Scaffolded (ready for tool configuration documentation)
- **Last Updated**: 2025-12-11

---

## Related Folders

- **[../61-00-06-020_Models/](../61-00-06-020_Models/)** — Models requiring these tool configurations
- **[../61-00-06-030_Simulation/](../61-00-06-030_Simulation/)** — Simulations using these tools
- **[../61-00-06-060_Data_Artifacts/](../61-00-06-060_Data_Artifacts/)** — Tool output data storage

---

## Document Control

- **Standard**: OPT-IN Framework v1.1 (Enhanced Engineering Template)
- **Owner**: AMPEL360 Engineering WG (Computational Team)
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

*Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.*
