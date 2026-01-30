# ANALYSIS — Analysis Model Exports

This directory contains analysis model exports for FEA, CFD, thermal, and electromagnetic simulations of ATA 61 propulsion system components.

## Purpose

Analysis exports enable:

- Structural finite element analysis (FEA)
- Computational fluid dynamics (CFD) simulations
- Thermal analysis for heat management
- Electromagnetic analysis for motor design
- Multi-physics coupled simulations

## Directory Structure

```
ANALYSIS/
├── README.md           # This file
├── FEA_MESH/           # FEA mesh exports
├── CFD_GEOMETRY/       # CFD surface geometry
├── THERMAL/            # Thermal analysis models
└── ELECTROMAGNETIC/    # EM analysis exports
```

## Format Specifications

### FEA Mesh (FEA_MESH/)

**Finite Element Analysis mesh exports**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Formats              | Nastran (.bdf, .nas), Abaqus (.inp), ANSYS (.cdb) |
| Element Types        | Per analysis requirements                |
| Mesh Quality         | Jacobian ≥ 0.3, aspect ratio ≤ 10        |
| Units                | SI (mm, N, MPa, s)                       |
| Coordinate System    | Global or component-specific             |
| Naming               | `Q100-61-FEA-[COMPONENT].[ext]`          |

**Included Files:**

- `*.bdf` / `*.nas` - Nastran bulk data file
- `*.inp` - Abaqus input file
- `*.cdb` - ANSYS component database
- `*_MESH-REPORT.md` - Mesh quality report

**Mesh Quality Requirements:**

| Parameter           | Requirement                              |
|---------------------|------------------------------------------|
| Min Jacobian        | ≥ 0.3                                    |
| Max Aspect Ratio    | ≤ 10 (≤ 5 for critical areas)            |
| Warpage             | ≤ 15°                                    |
| Skewness            | ≤ 60°                                    |
| Element Size        | Per stress gradient requirements         |

**Use Cases:**

- Static structural analysis
- Modal analysis (natural frequencies)
- Dynamic/transient analysis
- Fatigue and damage tolerance
- Buckling analysis

### CFD Geometry (CFD_GEOMETRY/)

**Computational Fluid Dynamics surface geometry**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Format               | STL (binary), STEP, CGNS                 |
| Surface Quality      | Watertight, manifold                     |
| Tessellation         | Chord deviation ≤ 0.05 mm                |
| Feature Capture      | All aerodynamic features preserved       |
| Naming               | `Q100-61-CFD-[COMPONENT].[ext]`          |

**Included Files:**

- `*.stl` - Surface mesh for CFD preprocessing
- `*.step` - Clean CAD geometry
- `*.cgns` - CFD General Notation System format
- `*_BOUNDARY-DEF.yaml` - Boundary condition definitions

**Boundary Definition Example:**

```yaml
boundaries:
  inlet:
    type: velocity_inlet
    surfaces: [surface_001, surface_002]
  outlet:
    type: pressure_outlet
    surfaces: [surface_003]
  wall:
    type: no_slip_wall
    surfaces: [surface_004, surface_005]
  symmetry:
    type: symmetry_plane
    surfaces: [surface_006]
```

**Use Cases:**

- External aerodynamic analysis
- Internal flow (cooling, air systems)
- Aeroacoustic analysis
- Performance optimization

### Thermal (THERMAL/)

**Thermal analysis model exports**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Format               | Nastran thermal, ANSYS, STEP             |
| Mesh Type            | Volume mesh with thermal properties      |
| Material Properties  | Conductivity, specific heat, density     |
| Boundary Conditions  | Heat sources, convection, radiation      |
| Naming               | `Q100-61-THM-[COMPONENT].[ext]`          |

**Included Files:**

- `*.bdf` - Nastran thermal model
- `*.step` - Geometry for thermal analysis
- `*_THERMAL-PROP.yaml` - Material thermal properties
- `*_HEAT-SOURCES.csv` - Heat source definitions

**Thermal Properties Example:**

```yaml
materials:
  AL7075-T6:
    conductivity: 130  # W/(m·K)
    specific_heat: 960  # J/(kg·K)
    density: 2810  # kg/m³
  CFRP-UD:
    conductivity_fiber: 5.0  # W/(m·K)
    conductivity_transverse: 0.5  # W/(m·K)
    specific_heat: 800  # J/(kg·K)
    density: 1550  # kg/m³
```

**Use Cases:**

- Motor thermal management
- Gearbox heat dissipation
- Nacelle thermal protection
- Transient thermal analysis

### Electromagnetic (ELECTROMAGNETIC/)

**Electromagnetic analysis exports**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Format               | STEP, IGES, native EM tool formats       |
| Geometry Type        | 2D axisymmetric or 3D solid              |
| Material Properties  | Magnetic permeability, conductivity      |
| Winding Definition   | Coil geometry and turns                  |
| Naming               | `Q100-61-EM-[COMPONENT].[ext]`           |

**Included Files:**

- `*.step` - Clean EM geometry
- `*_EM-PROP.yaml` - Electromagnetic material properties
- `*_WINDING.csv` - Motor winding definition
- `*_MAGNET.csv` - Permanent magnet definitions

**EM Properties Example:**

```yaml
materials:
  M19-29G:  # Silicon steel laminations
    type: nonlinear
    bh_curve: M19_29G_BH.csv
    conductivity: 2.0e6  # S/m
    lamination_factor: 0.95
  NdFeB-N42:  # Permanent magnet
    type: permanent_magnet
    remanence: 1.32  # T
    coercivity: 955000  # A/m
    conductivity: 0.67e6  # S/m
```

**Use Cases:**

- Electric motor electromagnetic design
- Power electronics EMI analysis
- Magnetic bearing analysis
- Generator performance

## Naming Convention

All analysis exports follow:

```
Q100-61-[TYPE]-[COMPONENT]-[VARIANT].[ext]
```

### Analysis Type Codes

| Code | Analysis Type            |
|------|--------------------------|
| FEA  | Finite Element Analysis  |
| CFD  | Computational Fluid Dynamics |
| THM  | Thermal Analysis         |
| EM   | Electromagnetic Analysis |

### Examples

```
Q100-61-FEA-GBX-HOUSING.bdf            → Gearbox housing Nastran mesh
Q100-61-FEA-FAN-BLADE-S01.inp          → Fan blade stage 1 Abaqus input
Q100-61-CFD-NAC-EXTERNAL.stl           → Nacelle external flow surface
Q100-61-CFD-CLG-CHANNEL.cgns           → Cooling channel CFD geometry
Q100-61-THM-EMD-MOTOR.bdf              → Motor thermal model
Q100-61-EM-EMD-ROTOR.step              → Motor rotor EM geometry
```

## Export Procedures

1. **Geometry Preparation**: Clean and simplify CAD for analysis
2. **Mesh Generation**: Create analysis-appropriate mesh
3. **Quality Check**: Verify mesh quality metrics
4. **Material Assignment**: Apply material properties
5. **Export Generation**: Create solver-specific files
6. **Validation**: Run basic sanity checks

## Quality Requirements

- Mesh quality metrics within specified limits
- Geometry watertight and manifold
- Material properties complete and traceable
- Boundary conditions documented
- Units consistent and specified

## Related Documentation

- [Q100-61-EXPORT-SETTINGS.yaml](../Q100-61-EXPORT-SETTINGS.yaml) - Detailed export settings
- [../README.md](../README.md) - EXPORTS overview

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
