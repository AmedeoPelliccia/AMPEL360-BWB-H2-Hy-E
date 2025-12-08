# 03-50-06-01A - FEA Structural Analysis

## 1. Purpose
Specification for Finite Element Analysis (FEA) methods and practices for Ground Support Equipment (GSE) structural design, validation, and optimization.

## 2. Scope
- FEA modeling best practices
- Element selection and meshing
- Boundary conditions and loads
- Analysis types (linear, nonlinear, dynamic)
- Results interpretation and validation
- Software and quality assurance

## 3. Applicable Documents
- ASME V&V 10 (Verification and Validation in Computational Solid Mechanics)
- NAFEMS (National Agency for Finite Element Methods and Standards) Guidelines
- AWS D1.1 (Structural Welding Code)
- AISC 360 (Structural Steel Design)
- ISO 16269 (Statistical Interpretation of Data)

## 4. Structural Description

### 4.1 FEA Applications in GSE
| Application | Analysis Type | Purpose |
|-------------|--------------|---------|
| Structural Design | Linear static | Verify stress, deflection criteria |
| Load Optimization | Topology optimization | Minimize weight while meeting constraints |
| Fatigue Assessment | Dynamic + fatigue | Predict service life |
| Failure Analysis | Nonlinear (plasticity, contact) | Understand failure modes |
| Vibration Analysis | Modal, harmonic | Avoid resonance, reduce noise |
| Crash/Impact | Explicit dynamics | Safety assessment |
| Thermal-Structural | Coupled thermal-structural | Cryogenic systems, thermal stress |

### 4.2 Element Types
| Element Type | Application | Typical GSE Use |
|--------------|-------------|-----------------|
| Shell (2D) | Thin-walled structures | Chassis frames, panels, vessels |
| Solid (3D) | Complex geometries, contact | Brackets, joints, thick sections |
| Beam | Frame structures | Trusses, space frames |
| Spring/Damper | Suspension, isolators | Mobile GSE, vibration isolation |
| Contact | Interface behavior | Bolted joints, sliding surfaces |
| Rigid | Kinematic constraints | Load application, symmetry |

### 4.3 Mesh Quality Criteria
| Parameter | Target | Notes |
|-----------|--------|-------|
| Element Aspect Ratio | < 3:1 (shell), < 5:1 (solid) | Avoid distorted elements |
| Warpage (shell) | < 5° | Flat elements preferred |
| Jacobian | > 0.6 | Element validity check |
| Nodes per Wavelength | > 20 (dynamics) | Capture dynamic response |
| Refinement at Stress Concentrations | h-refinement or p-refinement | Accurate local stress |
| Mesh Independence | <5% change with 2× refinement | Convergence verification |

### 4.4 Analysis Types
#### 4.4.1 Linear Static Analysis
- **Assumptions**: Small deformations, linear material, static loads
- **Output**: Stress, strain, deflection
- **Acceptance**: σ_von_Mises ≤ 0.5×Fy (service), ≤ Fy (ultimate)

#### 4.4.2 Nonlinear Analysis
- **Material Nonlinearity**: Plasticity, large strain
- **Geometric Nonlinearity**: Large deformation, buckling
- **Contact Nonlinearity**: Friction, gap elements
- **Acceptance**: Plastic strain < 5% for ductile behavior

#### 4.4.3 Dynamic Analysis
- **Modal**: Natural frequencies and mode shapes
- **Harmonic**: Frequency response (steady-state vibration)
- **Transient**: Time-history response (impact, seismic)
- **Acceptance**: Avoid resonance (f_excitation < 0.5×f_natural)

### 4.5 Software Tools
| Software | Strengths | Typical Use |
|----------|-----------|-------------|
| ANSYS Mechanical | General-purpose, robust | Static, dynamic, thermal-structural |
| ABAQUS | Nonlinear, contact | Crash, advanced nonlinear |
| LS-DYNA | Explicit dynamics | Impact, blast, crash |
| NASTRAN | Linear analysis, optimization | Aircraft-heritage structures |
| SolidWorks Simulation | Integrated CAD | Preliminary design, quick checks |
| COMSOL Multiphysics | Coupled physics | H2 diffusion, thermal-fluid-structural |

## 5. Structural Requirements

### 5.1 Modeling Best Practices
- Use CAD geometry cleanup (remove fillets <5 mm unless critical)
- Model symmetry to reduce model size (1/2 or 1/4 models)
- Apply loads and constraints at nodes or element faces (not geometry)
- Use remote load/displacement for accurate force/moment application
- Include contact where appropriate (bonded, frictional, or frictionless)

### 5.2 Load Application
| Load Type | Modeling Method | Notes |
|-----------|----------------|-------|
| Distributed Load | Pressure on surface | Accurate representation |
| Concentrated Load | Force at node | Use remote point for moment |
| Gravity | Body force (acceleration) | -9.81 m/s² |
| Thermal Load | Temperature field | From thermal analysis |
| Inertial | Acceleration field | Braking, cornering |
| Bolt Preload | Pretension element | Accurate bolt behavior |

### 5.3 Boundary Conditions
- **Fixed Support**: All DOFs constrained (0 displacement, 0 rotation)
- **Pinned**: Translations fixed, rotations free
- **Slider**: One translation free (sliding surface)
- **Symmetry**: Normal displacement = 0, tangential shear = 0
- **Spring**: Elastic constraint (suspension mounts)

### 5.4 Results Validation
| Method | Purpose | Acceptance |
|--------|---------|------------|
| Hand Calculations | Verify global behavior | ±20% agreement |
| Mesh Convergence Study | Ensure mesh independence | <5% change |
| Comparison to Test Data | Validate model | ±15% agreement |
| Comparison to Similar Designs | Sanity check | Reasonable agreement |
| Peer Review | Quality assurance | Independent check |

### 5.5 Reporting Requirements
- Model description (geometry, elements, mesh statistics)
- Material properties used
- Boundary conditions and loads (with diagrams)
- Analysis type and solver settings
- Results (stress contours, deflection plots, safety factors)
- Mesh convergence study
- Validation against hand calculations or test data
- Conclusions and recommendations

## 6. Cross-References
- Parent Document: 03-50_Structures
- Related: 03-50-01-04A (GSE Load Analysis), 03-50-06-02A (Fatigue Analysis), 03-50-06-04A (Cryogenic Stress Analysis)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-06-01A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
