# 03-50-06-02A - Fatigue Analysis

## 1. Purpose
Specification for fatigue life assessment of Ground Support Equipment (GSE) structures subjected to cyclic loading, ensuring adequate service life under repeated operational loads.

## 2. Scope
- Fatigue analysis methods (S-N curves, crack growth)
- Load spectrum development
- Stress concentration factors
- Cumulative damage assessment
- Fatigue testing and validation

## 3. Applicable Documents
- AWS D1.1 Annex 4 (Fatigue Design)
- ASME VIII-2 Part 5 (Design by Analysis - Fatigue)
- BS 7608 (Code of Practice for Fatigue Design and Assessment of Steel Structures)
- EN 1993-1-9 (Eurocode 3: Fatigue)
- SAE J1099 (Technical Report on Fatigue Properties)

## 4. Structural Description

### 4.1 Fatigue Life Regimes
| Regime | Cycles | Application | Analysis Method |
|--------|--------|-------------|-----------------|
| Low-Cycle Fatigue (LCF) | <10,000 | Pressure cycling, overloads | Strain-life (ε-N) |
| High-Cycle Fatigue (HCF) | 10,000-10⁷ | Operational cycling | Stress-life (S-N) |
| Very High Cycle (VHCF) | >10⁷ | Vibration, resonance | S-N with endurance limit |
| Crack Growth | Any | Fracture mechanics approach | Paris Law (da/dN) |

### 4.2 S-N Curve Approach
| Detail Category | Description | Design Life (cycles @ σ_range) |
|-----------------|-------------|-------------------------------|
| A | Plain material, no welds | 2×10⁶ @ 180 MPa |
| B | Machined welds, ground flush | 2×10⁶ @ 140 MPa |
| C | As-welded, full-penetration | 2×10⁶ @ 100 MPa |
| D | Partial-penetration welds | 2×10⁶ @ 80 MPa |
| E | Fillet welds, attachments | 2×10⁶ @ 63 MPa |
| F | Rough welds, stress raisers | 2×10⁶ @ 50 MPa |

### 4.3 Load Spectrum
- **Constant Amplitude**: Single stress range repeated
- **Variable Amplitude**: Real service loads (load histogram)
- **Random**: Stochastic loading (vibration, wind)
- **Block Loading**: Simplified spectrum (high/medium/low blocks)

### 4.4 Damage Accumulation (Miner's Rule)
**Formula**: D = Σ(n_i / N_i)
- n_i = number of cycles at stress range i
- N_i = allowable cycles at stress range i (from S-N curve)
- **Failure criterion**: D ≥ 1.0

### 4.5 Stress Concentration Factors (SCF)
| Detail | SCF (K_t) | Notes |
|--------|-----------|-------|
| Smooth plate | 1.0 | Reference |
| Hole in plate | 2.0-3.0 | Depends on geometry |
| Sharp notch | 5-10 | Very detrimental |
| Weld toe | 2.0-4.0 | As-welded |
| Weld toe (ground) | 1.5-2.0 | Improved finish |

## 5. Structural Requirements

### 5.1 Design Criteria
| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Design Life | 20 years or 500,000 km (mobile) | Per specification |
| Cumulative Damage | D < 0.5 (design), D < 1.0 (ultimate) | Miner's Rule |
| Safety Factor | 2.0 on cycles or 1.5 on stress | AWS D1.1 |
| Stress Range | Below endurance limit preferred | Infinite life |

### 5.2 Analysis Procedure
1. Define load spectrum (measured or assumed)
2. Perform stress analysis (FEA or hand calculations)
3. Identify critical locations (high stress, welds)
4. Determine stress ranges (ΔσCycles)
5. Apply fatigue damage model (S-N or crack growth)
6. Calculate cumulative damage
7. Verify D < acceptance criterion

### 5.3 Fatigue Testing
- **Coupon Testing**: Validate S-N curve for specific detail
- **Component Testing**: Full-scale or sub-scale testing
- **Spectrum Loading**: Apply representative load history
- **Acceptance**: Achieve 2× design life without failure

## 6. Cross-References
- Parent Document: 03-50_Structures
- Related: 03-50-06-01A (FEA Structural Analysis), 03-50-06-03A (Vibration Analysis)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-06-02A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
