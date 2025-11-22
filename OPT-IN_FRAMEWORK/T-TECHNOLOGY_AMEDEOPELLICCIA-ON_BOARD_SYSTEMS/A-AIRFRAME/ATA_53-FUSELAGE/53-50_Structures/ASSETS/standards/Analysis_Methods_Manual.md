# Analysis Methods Manual

## Purpose

This manual defines standard analysis methods for structural evaluation of AMPEL360 BWB fuselage components.

## Analysis Hierarchy

### Level 1: Hand Calculations
- Simple beam theory
- Pressure vessel equations
- Euler buckling
- Used for preliminary sizing and verification

### Level 2: Finite Element Analysis
- Detailed stress analysis
- Buckling stability
- Nonlinear analysis
- Primary certification method

### Level 3: Physical Testing
- Component tests
- Full-scale tests
- Ultimate verification method

## Static Strength Analysis

### Methodology
1. Define load cases per [CS-25.301](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
2. Apply loads to FEA model
3. Extract stresses (von Mises, principal)
4. Compare to allowables
5. Calculate margins of safety

### Acceptance Criteria
- Margin of Safety ≥ 0 for all load cases
- No yielding at limit load
- No failure at ultimate load (1.5 × limit)

## Buckling Analysis

### Linear Eigenvalue Analysis
- Used for initial stability assessment
- Provides critical buckling modes
- Conservative (neglects post-buckling strength)

### Nonlinear Post-Buckling Analysis
- Captures post-buckling behavior
- Required for thin panels and shells
- More accurate but computationally intensive

### Hand Methods
- Euler column buckling: P_cr = π²EI / L²
- Plate buckling: σ_cr = k × π²E / [12(1-ν²)] × (t/b)²

### Acceptance Criteria
- Buckling load factor > 1.0 at limit load
- Buckling load factor > 1.5 at ultimate load (or demonstrate post-buckling capability)

## Fatigue Analysis

### S-N Curve Method
- For high-cycle fatigue (N > 10⁴ cycles)
- Use material S-N curves
- Apply Miner's rule for cumulative damage

### Crack Growth Method
- For damage tolerance per [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- Use Paris law: da/dN = C(ΔK)ᵐ
- Define inspection intervals

## Damage Tolerance

### Initial Flaw Assumptions
- Manufacturing defects (e.g., 0.050" for aluminum)
- Impact damage (1" diameter for composites)
- Accidental damage scenarios

### Residual Strength
- Structure with damage must withstand limit load
- Demonstrate slow crack growth (detectable before critical)

## References

- [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) - Damage Tolerance and Fatigue
- [53-50-03 Fatigue and Damage Tolerance](../../53-50-03_Fatigue_and_Damage_Tolerance/README.md)

---

## Document Control
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Version: 1.0
- Last Update: 2025-11-22

---
