# Uncertainty Quantification
## Door L1 Forward Analysis

**Document:** UQ-001  
**Revision:** 1.0  
**Date:** 2025-11-03

---

## 1. PURPOSE

Quantify uncertainty in analytical predictions to establish confidence bounds for certification.

---

## 2. UNCERTAINTY SOURCES

### 2.1 Material Properties
| Property | Nominal | Uncertainty | Distribution |
|----------|---------|-------------|--------------|
| CFRP E1 | 135 GPa | ±8 GPa | Normal |
| CFRP E2 | 8.5 GPa | ±0.8 GPa | Normal |
| Core modulus | 95 MPa | ±15 MPa | Normal |
| Core density | 48 kg/m³ | ±3 kg/m³ | Normal |
| Face sheet thickness | 4.0 mm | ±0.2 mm | Uniform |

### 2.2 Geometric Tolerances
| Parameter | Nominal | Tolerance |
|-----------|---------|-----------|
| Panel dimensions | 2100×1200 mm | ±2 mm |
| Core thickness | 25 mm | ±0.5 mm |
| Skin-core bond | 100% | -5% |

### 2.3 Boundary Conditions
| Condition | Nominal | Uncertainty |
|-----------|---------|-------------|
| Latch stiffness | 500 kN/mm | ±20% |
| Hinge stiffness | 50 Nm/rad | ±30% |
| Seal pressure | 5 psi | ±10% |

### 2.4 Loading
| Load | Nominal | Uncertainty |
|------|---------|-------------|
| Cabin pressure | 8.5 psi | ±0.1 psi |
| Temperature | 20°C | ±10°C |

---

## 3. UNCERTAINTY PROPAGATION

### 3.1 Method: Monte Carlo Simulation

**Approach:**
1. Define probability distributions for all uncertain inputs
2. Sample 1000 combinations using Latin Hypercube
3. Run FEA for each combination
4. Calculate statistics on outputs

**Outputs to Quantify:**
- Mode 1 frequency
- Mode 1 damping
- Panel deflection @ 8.5 psi
- Peak stress @ ultimate
- Margin of safety

### 3.2 Expected Results

**Mode 1 Frequency:**
```
Mean: 25 Hz
Standard deviation: 2.5 Hz (10%)
95% confidence interval: 20-30 Hz
```

**Peak Stress:**
```
Mean: 450 MPa
Standard deviation: 90 MPa (20%)
95% confidence interval: 280-620 MPa
```

---

## 4. CONFIDENCE LEVELS

### 4.1 Current Status (AI-Based)
- Confidence in predictions: **LOW**
- Uncertainty: **±30-50%**
- Basis: AI-assisted conceptual analysis

### 4.2 After Professional FEA
- Confidence: **MEDIUM**
- Uncertainty: **±15-25%**
- Basis: Validated FEA with uncertainty quantification

### 4.3 After Testing
- Confidence: **HIGH**
- Uncertainty: **±5-10%**
- Basis: Test-validated models

---

## 5. SAFETY FACTORS

### 5.1 Required Margins

**Structural:**
- Limit load: Factor of Safety = 1.0 (no yield)
- Ultimate load: Factor of Safety = 1.5 (no failure)

**With Uncertainty:**
```
If prediction uncertainty = ±25%
Then required analytical margin = 1.5 × 1.25 = 1.875
```

**Current Design:**
- Predicted ultimate capability: 17 psi
- Required ultimate: 17 psi
- Margin of safety: 0% (MARGINAL)

**Conclusion:** Design is marginal with current uncertainty. Testing critical to confirm capability.

---

## 6. RISK ASSESSMENT

### 6.1 Mode 1 Resonance Risk

**Predicted frequency:** 25 Hz ± 7.5 Hz (30% uncertainty)
**Engine frequency:** 25 Hz (fixed)

**Probability analysis:**
```
P(f < 23 Hz) ≈ 15% (too close to engine)
P(23 Hz < f < 27 Hz) ≈ 70% (marginal separation)
P(f > 27 Hz) ≈ 15% (adequate separation)
```

**Mitigation:** GVT testing MANDATORY to measure actual frequency and damping.

---

## 7. DELIVERABLES

### 7.1 UQ Report
- Uncertainty analysis methodology
- Input distributions
- Monte Carlo results
- Sensitivity analysis (which inputs matter most)
- Confidence intervals on all predictions
- Risk assessment

### 7.2 Design Recommendations
Based on uncertainty analysis:
- Identify design sensitivities
- Recommend testing priorities
- Suggest design robustness improvements

---

## 8. REFERENCES

- ASME V&V 20 Standard for Verification and Validation in Computational Fluid Dynamics and Heat Transfer
- NASA-STD-7009A Standard for Models and Simulations
- AIAA Guide for Verification and Validation of Computational Fluid Dynamics Simulations

---

**Status:** To be performed in Phase 2 (Q1 2026) after professional FEA completion
