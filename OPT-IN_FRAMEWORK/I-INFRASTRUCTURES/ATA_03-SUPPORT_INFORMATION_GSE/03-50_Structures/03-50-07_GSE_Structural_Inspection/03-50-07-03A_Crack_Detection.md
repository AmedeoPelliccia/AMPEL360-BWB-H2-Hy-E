# 03-50-07-03A - Crack Detection

## 1. Purpose
Specification for crack detection methods in Ground Support Equipment (GSE) structures, including identification, characterization, and evaluation of cracks for fitness-for-service assessment.

## 2. Scope
- Crack detection methods
- Crack characterization (location, size, orientation)
- Crack growth monitoring
- Fitness-for-service evaluation
- Critical crack size determination

## 3. Applicable Documents
- ASTM E1820 (Fracture Toughness Testing)
- BS 7910 (Guide to Methods for Assessing the Acceptability of Flaws in Metallic Structures)
- API 579-1/ASME FFS-1 (Fitness-For-Service)
- ASTM E647 (Fatigue Crack Growth Rate Testing)
- ASME BPVC Section V (Nondestructive Examination)

## 4. Structural Description

### 4.1 Crack Types and Causes
| Crack Type | Typical Cause | Location |
|------------|--------------|----------|
| Fatigue Crack | Cyclic loading | Welds, stress concentrations, notches |
| Stress Corrosion Cracking (SCC) | Tensile stress + corrosive environment | Welds, cold-worked areas (SS, Al) |
| Hydrogen-Induced Cracking | H2 absorption + tensile stress | H2-exposed areas, welds |
| Weld Solidification Crack | Welding thermal stress | Weld centerline, crater |
| Weld Cold Crack (HAZ) | Hydrogen, residual stress | Heat-affected zone |
| Overload Crack | Single excessive load | High-stress areas, notches |
| Thermal Fatigue Crack | Thermal cycling | Cryogenic systems, thermal gradients |

### 4.2 Crack Detection Methods
| Method | Detectability | Application | Notes |
|--------|--------------|-------------|-------|
| Visual Inspection | >1 mm (unaided), >0.1 mm (magnified) | Surface cracks | Economical, first step |
| Dye Penetrant (PT) | >0.1 mm (surface-breaking) | All materials, surface | Simple, effective |
| Magnetic Particle (MT) | >0.01 mm (ferromagnetic) | Ferromagnetic, surface/near-surface | Very sensitive |
| Eddy Current (ET) | >0.05 mm | Conductive, surface/near-surface | Fast scanning |
| Ultrasonic (UT) | >1 mm (internal) | All materials, volumetric | Internal cracks |
| Radiography (RT) | >2% thickness | All materials, planar defects difficult | Porosity, inclusions |
| Acoustic Emission (AE) | Active cracks during loading | Real-time monitoring | Crack growth detection |

### 4.3 Crack Characterization
- **Location**: Component, distance from edges/welds
- **Orientation**: Longitudinal, transverse, oblique
- **Length (a)**: Surface length or through-thickness length
- **Depth (c)**: Depth below surface
- **Shape**: Semi-elliptical, through-thickness, corner
- **Surface Condition**: Tight, open, corroded

### 4.4 Critical Crack Size (Fracture Mechanics)
**Formula (simplified)**: a_crit = (K_Ic / (Y×σ))²/π
- K_Ic = fracture toughness (material property)
- Y = geometry factor (~1.0-1.2)
- σ = applied stress
- a_crit = critical crack size (half-length for through-crack)

**Example**: SS 304L, K_Ic = 200 MPa√m, σ = 100 MPa, Y = 1.12
→ a_crit = (200/(1.12×100))² / π ≈ 1.0 m (very large, ductile material)

### 4.5 Crack Growth Monitoring
- **Frequency**: Depends on growth rate (weekly to annually)
- **Method**: Same NDT as initial detection, measure length
- **Acceptance**: Growth rate < critical rate (fracture mechanics analysis)
- **Action**: If approaching critical size, repair or replace

## 5. Structural Requirements

### 5.1 Inspection Frequency
| Risk Level | Initial Detection Method | Re-Inspection Interval |
|------------|-------------------------|----------------------|
| Critical (H2 pressure systems) | PT + UT | Annually |
| High (structural welds, high stress) | PT or MT | Every 2-3 years |
| Medium (general structure) | Visual + PT (sample) | Every 5 years |
| Low (non-critical) | Visual | Every 10 years |

### 5.2 Acceptance Criteria
| Crack Type | Acceptance | Action |
|------------|------------|--------|
| Surface Crack, a < 3 mm | Monitor | Re-inspect in 6-12 months |
| Surface Crack, 3 mm ≤ a < a_crit | Engineering evaluation | Repair or monitor closely |
| Surface Crack, a ≥ a_crit | Reject | Immediate repair or replace |
| Through-Thickness Crack | Reject | Immediate repair or replace |

### 5.3 Fitness-For-Service Evaluation
- Perform when crack detected and a > acceptance limit
- Methods: Fracture mechanics (linear elastic or elastic-plastic)
- Standards: API 579-1/ASME FFS-1, BS 7910
- Input: Crack size, applied stress, material toughness
- Output: Remaining life, critical crack size, repair/replace decision

### 5.4 H2-Specific Considerations
- Hydrogen embrittlement lowers fracture toughness
- Fatigue crack growth rate may be accelerated in H2 environment
- Special attention to welds and cold-worked areas
- Conservative assumptions in fitness-for-service analysis

## 6. Cross-References
- Parent Document: 03-50_Structures
- Related: 03-50-07-01A (Visual Inspection), 03-50-07-02A (NDT Methods), 03-50-08 (GSE Structural Repair)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-07-03A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
