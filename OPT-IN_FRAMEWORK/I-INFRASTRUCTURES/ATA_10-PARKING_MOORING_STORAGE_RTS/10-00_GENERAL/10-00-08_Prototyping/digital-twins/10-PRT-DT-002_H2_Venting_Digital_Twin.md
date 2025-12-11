# 10-PRT-DT-002 - H2 Venting Digital Twin

## 1. Digital Twin Identification

| Parameter | Value |
|-----------|-------|
| Document Number | 10-PRT-DT-002 |
| Digital Twin Type | H2 Dispersion Simulation |
| TRL Target | 3→5 |
| Status | In Development |
| Version | A |
| Date | 2025-12-10 |
| Author | AMPEL360 CFD/Simulation Team |

## 2. Purpose

Develop a computational fluid dynamics (CFD) digital twin to simulate hydrogen (H2) dispersion from venting operations during parking, mooring, and storage of the AMPEL360 BWB aircraft. The digital twin will predict H2 concentration fields, validate vent system design, optimize sensor placement, and support safety analysis for certification.

### 2.1 Background
Safe H2 venting requires understanding dispersion behavior under various environmental conditions (wind speed, temperature, obstacles). Physical testing is expensive and time-consuming. A validated digital twin enables:
- Rapid evaluation of vent stack designs
- Optimization of H2 sensor placement
- Prediction of hazard zones
- Training and emergency response planning
- Certification evidence generation

### 2.2 Objectives
- Create CFD model of H2 venting from aircraft LH2 system
- Validate model against experimental data (10-PRT-POC-003, 10-PRT-PHY-004 testing)
- Simulate various scenarios (wind directions, vent rates, ambient conditions)
- Predict H2 concentration contours (identify ≥4% LEL zones)
- Optimize vent stack height and direction
- Determine minimum safe distances for personnel and equipment
- Support sensor placement strategy

## 3. Scope

### 3.1 What the Digital Twin Represents
- 3D CFD model of AMPEL360 BWB aircraft on ground with surrounding environment
- H2 vent source (vent valve outlet, vent stack)
- Atmospheric boundary layer (wind profiles, turbulence)
- Buoyancy-driven dispersion (H2 lighter than air)
- Transient dispersion (time-dependent H2 concentration)

### 3.2 Limitations
- Model represents single aircraft in open parking area (not hangar, not multi-aircraft)
- Simplified aircraft geometry (focus on vent area, not full detail)
- Steady-state wind conditions (not gusts or rapidly changing wind)
- Isothermal or simplified temperature gradients (not full thermal model of H2 boil-off cooling)
- Assumes ideal gas behavior (reasonable for low-pressure venting)

### 3.3 Use Cases
- Vent system design optimization
- Safety analysis for certification (hazard zones)
- H2 sensor placement optimization
- Emergency response planning (evacuation zones)
- Training tool (visualize H2 dispersion)
- What-if scenarios (equipment failures, adverse conditions)

## 4. Design Basis

### 4.1 Related Documents
- ATA_10-00-02_Safety: H2 hazard analysis, safety zones
- ATA_10-00-04_Design: H2 venting system design
- 10-PRT-PLN-004: H2 System Prototype Plan
- 10-PRT-POC-003: H2 Venting POC (experimental data for validation)
- 10-PRT-PHY-004: H2 Vent Valve Prototype (vent flow rate data)

### 4.2 Requirements Addressed
| Requirement ID | Description | Verification Method |
|----------------|-------------|---------------------|
| REQ-10-00-H2-002 | Safe H2 dispersion (no accumulation) | Digital twin simulation |
| REQ-10-00-H2-006 | H2 concentration < 4% LEL outside hazard zone | CFD prediction |
| REQ-10-00-H2-007 | Vent stack height and direction | CFD optimization |
| REQ-10-00-H2-008 | Sensor placement strategy | CFD-based sensor optimization |

### 4.3 Physics and Modeling Approach
- **Governing Equations**: Navier-Stokes (RANS or LES), species transport (H2-air mixture)
- **Turbulence Model**: k-ε or k-ω SST for RANS, Smagorinsky for LES
- **Buoyancy**: Boussinesq approximation or full density variation
- **Boundary Conditions**: 
  - Inlet: Atmospheric boundary layer velocity profile
  - Outlet: Pressure outlet (far-field)
  - Ground: No-slip wall
  - Aircraft surface: Simplified as walls
  - Vent source: Mass flow inlet (H2 at specified rate)

## 5. Digital Twin Specifications

### 5.1 Software and Tools
| Tool | Purpose | Version |
|------|---------|---------|
| OpenFOAM or ANSYS Fluent | CFD solver | OpenFOAM v11 or Fluent 2023 |
| Gmsh or ANSYS Mesher | Mesh generation | Gmsh 4.x |
| ParaView | Post-processing, visualization | ParaView 5.x |
| Python (NumPy, SciPy, Matplotlib) | Scripting, analysis, plotting | Python 3.10+ |
| Git | Version control for model files | Git 2.x |

### 5.2 Model Geometry
- **Domain Size**: 200m (L) x 100m (W) x 50m (H) - large enough to avoid boundary effects
- **Aircraft**: Simplified BWB geometry, focus on vent area (reduce mesh size)
- **Vent Stack**: Cylindrical vent stack, variable height (2-10m), variable orientation
- **Ground**: Flat ground plane (or slight slope if applicable to test site)

### 5.3 Mesh Specifications
- **Mesh Type**: Structured hex-dominant or unstructured tetrahedral/polyhedral
- **Mesh Refinement**: 
  - Fine mesh near vent source (cell size 0.05-0.1 m)
  - Refinement region along expected plume path (cell size 0.2-0.5 m)
  - Coarser mesh in far-field (cell size 1-2 m)
- **Total Cell Count**: Target 2-5 million cells (balance accuracy and computation time)
- **Mesh Quality**: Skewness < 0.85, aspect ratio < 100

### 5.4 Simulation Parameters
| Parameter | Value | Notes |
|-----------|-------|-------|
| H2 Vent Rate | 1-10 kg/min | Range based on design (10-PRT-PHY-004) |
| Wind Speed | 0.5-10 m/s | Range from calm to moderate wind |
| Wind Direction | 0°-360° | Multiple scenarios |
| Ambient Temperature | -20°C to +40°C | Environmental range |
| Ambient Pressure | 1 atm (101,325 Pa) | Sea level (adjust for altitude if needed) |
| H2 Temperature at Vent | -200°C to +20°C | Cold from LH2 or warmed in vent line |
| Turbulence Intensity | 5-15% | Typical outdoor |

### 5.5 Scenarios to Simulate
| Scenario | Wind Speed | Wind Direction | Vent Rate | Purpose |
|----------|-----------|----------------|-----------|---------|
| 1. Calm Air | 0.5 m/s | 0° (reference) | 5 kg/min | Worst case (minimal dispersion) |
| 2. Light Breeze | 2 m/s | 0°, 90°, 180°, 270° | 5 kg/min | Typical conditions |
| 3. Moderate Wind | 5 m/s | 0°, 90°, 180°, 270° | 5 kg/min | Good dispersion |
| 4. High Vent Rate | 2 m/s | 0° | 10 kg/min | Emergency venting |
| 5. Low Vent Rate | 2 m/s | 0° | 1 kg/min | Normal boil-off |
| 6. Temperature Effects | 2 m/s | 0° | 5 kg/min | -20°C vs +40°C ambient |

## 6. H2/BWB/Cryo Considerations

### 6.1 System Classification
| Parameter | Value | Details |
|-----------|-------|---------|
| H2 Related | Yes | Core focus: H2 dispersion |
| Cryo Related | Partial | H2 may be cold from LH2 |
| BWB Specific | Yes | BWB aircraft geometry affects flow |

### 6.2 H2 Dispersion Physics
- **H2 Density**: ρ(H2) = 0.0899 kg/m³ at STP (air: 1.225 kg/m³) → H2 rises due to buoyancy
- **Molecular Weight**: M(H2) = 2.016 g/mol (air: 28.97 g/mol)
- **Buoyancy Velocity**: V_buoyant ≈ √(g * Δρ/ρ * H) where g = gravity, Δρ = density difference, H = vent height
- **Turbulent Diffusion**: H2 mixes with air via turbulent eddies
- **Cold H2 Effects**: Initially, cold H2 (-200°C) is denser than ambient air → initially may descend, then warm and rise

### 6.3 BWB Aircraft Effects
- **Wide Fuselage**: BWB has wide, flat upper surface → may affect near-field dispersion
- **Vent Location**: Vent stack on top center of BWB → far from ground, good for dispersion
- **Wake Effects**: Aircraft body creates recirculation zones → potential H2 trapping (model must capture this)

### 6.4 Safety Zones
Digital twin will predict:
- **4% LEL (0.16% H2) Contour**: Inner boundary of hazard zone (ignition possible)
- **25% LEL (1% H2) Contour**: More conservative safety zone
- **Time to Reach LEL**: Transient simulation → how quickly H2 accumulates

## 7. Development Plan

### 7.1 Phase 1: Model Setup (Weeks 1-3)
- Define geometry (simplified BWB aircraft, vent stack)
- Generate mesh (2-5M cells)
- Set up physics models (species transport, buoyancy, turbulence)
- Define boundary conditions
- Initial simulation (baseline case: 2 m/s wind, 5 kg/min vent rate)

### 7.2 Phase 2: Model Validation (Weeks 4-6)
- Compare CFD predictions to experimental data from 10-PRT-POC-003 (if available) or literature
- Adjust turbulence model, mesh refinement if needed
- Convergence study (mesh independence, time step independence)

### 7.3 Phase 3: Parametric Study (Weeks 7-10)
- Run scenarios (wind speed, direction, vent rate variations)
- Post-process results (H2 concentration contours, hazard zones)
- Document results

### 7.4 Phase 4: Optimization (Weeks 11-12)
- Optimize vent stack height (trade-off: height vs. structural/aerodynamic impact)
- Optimize vent direction (if directional vent possible)
- Optimize sensor placement (place sensors at predicted H2 accumulation zones)

### 7.5 Phase 5: Reporting (Weeks 13-14)
- Generate final report with visualizations (contour plots, animations)
- Document assumptions, limitations, validation
- Deliver model files and documentation to project team

## 8. Validation Strategy

### 8.1 Validation Data Sources
- **10-PRT-POC-003**: H2 Venting POC - small-scale venting test with H2 concentration measurements
- **Literature**: Published CFD validation cases for H2 dispersion (e.g., HySafe database)
- **Benchmark**: Simple cases with analytical solutions (e.g., Gaussian plume model for point source)

### 8.2 Validation Metrics
| Metric | Acceptance Criteria |
|--------|---------------------|
| H2 Concentration at Measurement Points | Within ±30% of experimental data |
| Plume Centerline Trajectory | Within ±20° of experimental observation |
| Plume Width (at given downwind distance) | Within ±40% of experimental data |

### 8.3 Uncertainty Quantification
- Sensitivity analysis: vary key parameters (turbulence model constants, mesh size)
- Document uncertainty in predictions (e.g., ±50% for far-field concentration)

## 9. Results and Deliverables

[To be completed after simulation - Q2-Q3 2026]

### 9.1 Key Outputs
- [ ] H2 concentration contour plots (3D and 2D slices)
- [ ] 4% LEL and 25% LEL isosurfaces (hazard zones)
- [ ] Time history of H2 concentration at specific points
- [ ] Recommended vent stack height and orientation
- [ ] Recommended H2 sensor placement locations
- [ ] Minimum safe distances for personnel and equipment
- [ ] Animation of H2 dispersion (for training)

### 9.2 Sensitivity Analysis Results
- [To be completed]

### 9.3 Validation Results
- [To be completed]

## 10. Lessons Learned

[To be completed after digital twin development]

### 10.1 Modeling Lessons
- TBD

### 10.2 Validation Lessons
- TBD

### 10.3 Computational Lessons
- TBD

## 11. Recommendations

### 11.1 Vent System Design
- [To be determined from simulation results]

### 11.2 Sensor Placement
- [To be determined from simulation results]

### 11.3 Future Model Enhancements
- Add multiple aircraft (parking configuration)
- Add hangar geometry (enclosed space dispersion)
- Add full thermal model (LH2 boil-off cooling, heat transfer)
- Couple with structural analysis (wind loads on vent stack)

## 12. Attachments and References

### 12.1 Model Files
- [Git repository]: AMPEL360-BWB-H2-Venting-CFD (OpenFOAM cases, scripts)

### 12.2 Visualization
- [ParaView state files for visualization]
- [Animations of H2 dispersion]

### 12.3 Related Documents
- 10-PRT-PLN-004: H2 System Prototype Plan
- 10-PRT-POC-003: H2 Venting POC
- 10-PRT-PHY-004: H2 Vent Valve Prototype
- ATA_10-00-02_Safety: H2 hazard analysis

## 13. References

### 13.1 Standards and Literature
- **NFPA 2**: Hydrogen Technologies Code (dispersion and safety zone guidance)
- **ISO/TR 15916**: Basic considerations for the safety of hydrogen systems
- **HySafe**: International hydrogen safety database (validation cases)
- **Journals**: Int. J. Hydrogen Energy (CFD modeling papers)
- **OpenFOAM Documentation**: www.openfoam.org
- **ANSYS Fluent Theory Guide**: (if using Fluent)

### 13.2 CFD Validation References
- [Specific papers on H2 dispersion CFD validation - TBD]

## 14. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| CFD Lead Engineer | TBD | | YYYY-MM-DD |
| H2 Systems Lead | TBD | | YYYY-MM-DD |
| Safety Engineer | TBD | | YYYY-MM-DD |
| Prototyping Program Manager | TBD | | YYYY-MM-DD |

## 15. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-10 | AMPEL360 CFD/Simulation Team | Initial release |

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last Update**: 2025-12-10
