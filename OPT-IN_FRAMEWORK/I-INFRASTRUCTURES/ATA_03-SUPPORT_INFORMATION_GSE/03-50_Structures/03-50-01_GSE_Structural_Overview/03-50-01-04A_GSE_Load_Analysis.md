# 03-50-01-04A - GSE Load Analysis

## 1. Purpose
This document defines the load cases, analysis methods, and acceptance criteria for structural analysis of Ground Support Equipment (GSE). It establishes the framework for ensuring structural adequacy under all anticipated operating and environmental conditions.

## 2. Scope
This specification covers:
- Load case definitions for all GSE types
- Static and dynamic load analysis
- Fatigue and fracture mechanics analysis
- Finite element analysis (FEA) requirements
- Load testing requirements
- Special considerations for H2/LH2 systems

## 3. Applicable Documents
- AISC 360 (Load and Resistance Factor Design)
- ASME BPVC Section VIII (Pressure Vessel Design)
- AWS D1.1 (Structural Welding Code)
- ASCE 7 (Minimum Design Loads for Buildings and Other Structures)
- EN 1991 (Eurocode 1: Actions on Structures)
- ISO 21009 (Cryogenic Vessels Design Criteria)
- Reference: 03-50-01-01A (GSE Structural Design)

## 4. Structural Description

### 4.1 Overview
GSE load analysis encompasses the systematic evaluation of all forces, moments, and environmental effects acting on GSE structures. The analysis ensures structural integrity throughout the design life under normal, abnormal, and emergency conditions.

### 4.2 Load Categories

#### 4.2.1 Dead Loads (DL)
| Component | Description | Typical Values |
|-----------|-------------|----------------|
| Structural Self-Weight | Weight of GSE structure | Per material density |
| Fixed Equipment | Permanently installed components | Per equipment specs |
| Insulation | Cryogenic insulation systems | 50-200 kg/m² for LH2 vessels |

#### 4.2.2 Live Loads (LL)
| Load Type | Description | Typical Values |
|-----------|-------------|----------------|
| Service Personnel | Workers on platforms/walkways | 2.4 kPa (50 psf) minimum |
| Stored Materials | Tools, parts, consumables | Per operational analysis |
| Aircraft Loads | Weight of supported aircraft | Per aircraft MTOW data |
| Fluid Loads | LH2, hydraulic fluids, water | Per vessel/tank capacity |

#### 4.2.3 Environmental Loads

##### 4.2.3.1 Wind Loads (W)
| Condition | Basic Wind Speed | Exposure Category | Importance Factor |
|-----------|------------------|-------------------|-------------------|
| Normal Operations | Per local code (e.g., 160 km/h) | C (open terrain) | 1.0 |
| Survival (non-operating) | 1.5× normal or 200 km/h | C | 1.15 |
| Hurricane-prone regions | As per ASCE 7 | Per site | 1.15 |

##### 4.2.3.2 Seismic Loads (E)
| Seismic Zone | Design Category | Response Modification Factor (R) |
|--------------|-----------------|-----------------------------------|
| Low (Ss < 0.25g) | B or C | 3.0 (ordinary steel) |
| Moderate (0.25g ≤ Ss < 0.5g) | C or D | 3.0-4.0 |
| High (Ss ≥ 0.5g) | D | 4.0-5.0 (special design) |

##### 4.2.3.3 Thermal Loads (T)
| Condition | Temperature Range | Application |
|-----------|------------------|-------------|
| Solar Heating | +70°C surface | Exposed steel structures |
| Cryogenic (LH2) | -253°C | LH2 vessels and piping |
| Diurnal Cycling | ±30°C | Thermal stress analysis |
| Thermal Shock | 200°C/hour max rate | Emergency venting scenarios |

#### 4.2.4 Operational Loads

##### 4.2.4.1 Pressure Loads (P)
| System | Design Pressure | Test Pressure |
|--------|----------------|---------------|
| LH2 Storage Vessels | MAWP + 10% | 1.5× MAWP |
| H2 Transfer Piping | 100-350 bar (typical) | 1.5× design |
| Pneumatic Systems | 6-10 bar | 1.5× design |
| Vacuum Insulation | Full vacuum (0 bar abs) | Leak test |

##### 4.2.4.2 Impact Loads (I)
| Scenario | Load Factor | Application |
|----------|-------------|-------------|
| Vehicle Collision | 2.0× static equivalent | Protective barriers |
| Dropped Objects | Per OSHA 1910.176 | Platform canopies |
| Aircraft Contact | 1.5× static contact force | Docking equipment |
| Accidental Impact | 50 kN lateral force | Critical supports |

##### 4.2.4.3 Dynamic Loads (D)
| Source | Amplification Factor | Notes |
|--------|---------------------|-------|
| Mobile GSE Motion | 1.5-2.0 | Acceleration/braking |
| Vibrating Equipment | Per resonance analysis | Pumps, compressors |
| Fluid Hammer | Per hydraulic analysis | Rapid valve closure |
| Earthquake | Per response spectrum | Site-specific analysis |

### 4.3 Load Combinations

#### 4.3.1 Service Load Combinations (LRFD)
1. **1.4 DL** (dead load only)
2. **1.2 DL + 1.6 LL** (normal operations)
3. **1.2 DL + 1.6 LL + 0.5 W** (operations with wind)
4. **1.2 DL + 1.0 LL + 1.0 W** (reduced live load with full wind)
5. **1.2 DL + 1.0 LL + 1.0 E** (seismic)
6. **0.9 DL + 1.0 W** (uplift/overturning check)
7. **0.9 DL + 1.0 E** (seismic uplift check)

#### 4.3.2 Pressure Vessel Load Combinations
1. **DL + P + T** (normal operation)
2. **DL + 1.5P + T** (hydrostatic test)
3. **DL + P + T + E** (seismic event during operation)
4. **DL + P + T + W** (wind during operation)

#### 4.3.3 Cryogenic System Load Combinations
1. **DL + LL + P + T(cryo)** (normal LH2 operations)
2. **DL + P + T(thermal shock)** (emergency warm-up)
3. **DL + LL + P + T(cryo) + E** (seismic during LH2 service)

## 5. Structural Requirements

### 5.1 Analysis Methods
| Method | Application | Acceptance Criteria |
|--------|-------------|---------------------|
| Hand Calculations | Simple structures, preliminary design | Safety factor ≥ 2.0 |
| Finite Element Analysis | Complex geometries, critical structures | Von Mises stress ≤ 0.5×Fy (service) |
| Fatigue Analysis | Cyclic loading, mobile GSE | Life > 50,000 cycles |
| Buckling Analysis | Compression members, thin shells | Load factor ≥ 2.0 |
| Fracture Mechanics | Cryogenic, high-consequence systems | Crack growth rate acceptable |

### 5.2 Acceptance Criteria

#### 5.2.1 Strength Criteria
| Limit State | Allowable Stress (ASD) | Strength Reduction (LRFD) |
|-------------|------------------------|---------------------------|
| Tension Yielding | 0.6 Fy | φ = 0.90 |
| Compression Yielding | 0.6 Fy | φ = 0.90 |
| Bending | 0.66 Fy | φ = 0.90 |
| Shear | 0.4 Fy | φ = 0.90 |
| Combined Stress | Unity check ≤ 1.0 | Unity check ≤ 1.0 |

#### 5.2.2 Deflection Criteria
| Component | Limit | Notes |
|-----------|-------|-------|
| General Beams | L/500 (service), L/240 (ultimate) | L = span length |
| Cantilevered Members | L/250 (service) | L = cantilever length |
| Platforms/Walkways | L/360 minimum | Avoid ponding and user discomfort |
| Crane Runways | L/600 (vertical), L/400 (lateral) | Precision equipment |

### 5.3 Fatigue Analysis Requirements
| GSE Type | Design Life (cycles) | Analysis Method |
|----------|---------------------|-----------------|
| Mobile GSE (daily use) | 50,000 minimum | S-N curves per AWS D1.1 |
| Pressure Cycling (LH2) | 10,000 fill/empty cycles | ASME VIII-2 FEA |
| Vibrating Equipment Supports | 10⁸ cycles | High-cycle fatigue analysis |

### 5.4 Load Testing Requirements
| Test Type | Test Load | Acceptance |
|-----------|-----------|------------|
| Proof Load Test | 1.25× design load | No permanent deformation |
| Hydrostatic Test (vessels) | 1.5× MAWP | No leakage, no deformation |
| Platform Load Test | 1.5× design live load | Deflection within limits |

### 5.5 H2-Specific Load Considerations
- **Pressure relief sizing**: Per API 520, ASME Section VIII
- **Thermal cycling**: LH2 thermal contraction/expansion (~1% linear)
- **Hydrogen fire loads**: Radiant heat flux up to 250 kW/m²
- **Deflagration pressure**: Design for 8× static pressure in confined spaces
- **Seismic + simultaneous pressure**: Required for high-consequence systems

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-00-06 (GSE Engineering)
  - ATA 03-30 (Anchors and Tie-downs)
- Parent Document: 03-50_Structures
- Related Documents:
  - 03-50-01-01A (GSE Structural Design)
  - 03-50-01-03A (GSE Materials Selection)
  - 03-50-02 (H2 GSE Structures)
  - 03-50-06 (GSE Structural Analysis - detailed FEA)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-01-04A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
