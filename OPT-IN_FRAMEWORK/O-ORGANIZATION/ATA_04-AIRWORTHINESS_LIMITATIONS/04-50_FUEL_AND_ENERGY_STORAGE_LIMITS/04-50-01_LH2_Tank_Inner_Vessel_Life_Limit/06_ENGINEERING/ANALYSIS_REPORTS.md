# Engineering: 04-50-01 - LH₂ Tank Inner Vessel Life Limit

## 1.0 Engineering Analysis Overview

This folder contains the engineering analyses that substantiate the life limit for the LH₂ tank inner vessel. All analyses support the 50,000 flight cycle and 20 calendar year retirement criteria.

## 2.0 Structural Analysis

### 2.1 Finite Element Analysis (FEA)
**Document:** AMPEL-STRESS-H2-TANK-001 Rev D

**Model Characteristics:**
- Software: ANSYS Mechanical 2024 R1
- Element Type: SOLID186 (20-node hexahedral elements)
- Total Elements: 2.3 million
- Total Nodes: 8.7 million
- Mesh Convergence: < 3% stress variation with 50% mesh refinement

**Loading Conditions:**
1. Internal pressure (5.5 bar operating, 8.25 bar design)
2. Thermal gradient (-253°C to +70°C)
3. Inertial loads (9g ultimate per CS-25.561)
4. Support reactions

**Critical Results:**
- Max von Mises stress: 285 MPa at dome-cylinder weld
- Max principal stress: 310 MPa at support lug
- Margin of Safety (yield): +0.47 (adequate)
- Margin of Safety (ultimate): +0.79 (adequate)

### 2.2 Fatigue Life Prediction
**Method:** Linear Elastic Fracture Mechanics (LEFM)

**Crack Growth Analysis:**
- Paris Law constants for Al-Li 2195 at -253°C:
  - C = 1.2×10⁻¹¹ (m/cycle)/(MPa√m)^m
  - m = 3.1 (dimensionless)
- Initial crack size: a₀ = 0.5 mm (NDT detection limit)
- Critical crack size: aᴄ = 45 mm (K_IC = 45 MPa√m)
- Stress intensity factor: K = σ√(πa) × Y (geometry factor Y = 1.12)

**Integration Results:**
- Crack initiation life: 50,000 cycles (0.5 → 1.0 mm)
- Crack propagation life: 97,000 cycles (1.0 → 45 mm)
- Total fatigue life: 147,000 cycles
- Design service goal: 50,000 cycles (safety factor = 2.94 ≈ 3.0)

### 2.3 Damage Tolerance Evaluation
**Approach:** CS-25.571(b) safe-life demonstration

**No Inspection Intervals Required:**
- Component classified as safe-life (retirement at limit)
- Crack propagation life (97,000 cycles) exceeds 2× design life
- Manufacturing NDT ensures initial quality
- No in-service inspections can extend life

**Fail-Safe Considerations:**
- Leak-before-burst verified by analysis
- Leak detection system provides early warning
- Dual-wall construction prevents immediate loss of H₂

## 3.0 Thermal Analysis

### 3.1 Thermal-Structural Coupling
**Document:** AMPEL-THERM-H2-TANK-001 Rev B

**Thermal Conditions:**
- LH₂ temperature: -253°C (20K)
- Ambient temperature: -55°C to +70°C (flight envelope)
- Fill rate: 150 kg/min (thermal shock consideration)
- Boil-off rate: 0.3% per hour (normal operations)

**Thermal Stress Results:**
- Maximum thermal stress: 200 MPa during cool-down
- Dome radius location: High stress concentration
- Support lug thermal expansion: 18 mm radial contraction
- Weld joint thermal strain: 0.12% (within elastic range)

### 3.2 Cryogenic Material Behavior
**Testing:** AMPEL-MAT-CRYO-001

**Al-Li 2195 Properties at -253°C:**
- Yield strength increase: +22% vs. room temperature
- Toughness: No ductile-brittle transition (excellent)
- Thermal conductivity: 120 W/m·K (high, beneficial for cool-down)
- Specific heat: 0.88 kJ/kg·K

**Weld Properties:**
- Heat affected zone (HAZ): Slight strength reduction (-5%)
- Fusion zone: Properties match base material
- Post-weld heat treatment: Restores 98% of base strength

## 4.0 Environmental Degradation Analysis

### 4.1 Hydrogen Embrittlement Study
**Document:** AMPEL-ENV-H2-TANK-002 Rev A

**Test Program:**
- Specimen exposure: 5,000 hours in LH₂ environment
- Accelerated aging: 85°C, 100% RH (equivalent to 20 years)
- Fracture toughness testing: ASTM E1820 standard

**Results:**
- Initial K_IC: 45 MPa√m
- Post-exposure K_IC: 41 MPa√m (9% reduction)
- Critical threshold: K_IC > 32 MPa√m for design loads
- Time to critical: 28.9 years (extrapolated)
- **Calendar limit (÷1.5 SF): 19.3 years → 20 years**

### 4.2 Corrosion Assessment
**Environment:** Coastal operation (salt spray exposure)

**Analysis:**
- Corrosion rate: 0.004 mm/year (based on ASTM B117 testing)
- Protective coating: MIL-A-8625 Type II anodizing (50 μm)
- Coating life: 10 years minimum
- Wall thickness margin: 1.5 mm (23% of nominal thickness)
- **Conclusion:** Corrosion not life-limiting

### 4.3 Vacuum System Degradation
**Multi-Layer Insulation (MLI) Aging:**
- Initial vacuum: 1×10⁻⁶ torr
- Degradation rate: 2.1×10⁻⁴ torr/year
- 20-year vacuum pressure: 5×10⁻³ torr
- Performance threshold: 1×10⁻³ torr (boil-off rate doubles)
- **Conclusion:** Vacuum monitoring required, but not life-limiting

## 5.0 Low-Cycle Fatigue (Thermal Cycling)

### 5.1 Thermal Cycle Damage Assessment
**Document:** AMPEL-LCF-H2-TANK-001

**Thermal Cycle Definition:**
- Cool-down: +20°C → -253°C (45 minutes)
- Hold: -253°C (flight duration, 2-6 hours)
- Warm-up: -253°C → +20°C (60 minutes)

**Strain Analysis:**
- Plastic strain per cycle: εₚ = 0.08%
- Location: Dome radius transition (stress concentration)
- Cumulative damage: Palmgren-Miner rule

**LCF Life Calculation:**
- Coffin-Manson relationship: Nf = (Δε/2ε'f)^(1/c)
- Material constants: ε'f = 0.35, c = -0.55
- LCF life: 112,000 thermal cycles
- **Limit (÷1.5 SF): 75,000 thermal cycles**

### 5.2 Thermal-Mechanical Interaction
**Combined HCF + LCF Damage:**
- Thermal cycle equivalent: 0.67 flight cycles (Palmgren-Miner)
- 75,000 TC × 0.67 = 50,250 equivalent FC
- **Validates 50,000 FC limit with margin**

## 6.0 Probabilistic Analysis

### 6.1 Reliability Assessment
**Method:** Monte Carlo simulation (10,000 runs)

**Input Distributions:**
- Stress intensity factor: Normal (μ = 285 MPa, σ = 15 MPa)
- Material toughness: Lognormal (μ = 45 MPa√m, σ = 3 MPa√m)
- Initial flaw size: Exponential (λ = 2 mm⁻¹)

**Results:**
- Probability of failure at 50,000 FC: 1.2×10⁻⁹
- Reliability: 99.9999999% (9-nines)
- **Meets CS-25.1309 catastrophic failure rate requirement**

### 6.2 Sensitivity Analysis
**Most Influential Parameters:**
1. Initial flaw size (62% of variance)
2. Stress intensity factor (25% of variance)
3. Material toughness (10% of variance)
4. Paris Law constants (3% of variance)

**Mitigation:**
- Improved NDT (reduce a₀ from 0.5 mm to 0.3 mm): +18% life extension
- Weld process improvement (reduce stress 10%): +35% life extension
- Combined improvements: Could support 65,000 FC limit (future)

## 7.0 Special Considerations

### 7.1 Manufacturing Variability
**Quality Control:**
- 100% radiographic inspection of welds
- Ultrasonic testing for subsurface defects
- Dye penetrant for surface cracks
- Acceptance criteria per AWS D17.1

**First Article Testing:**
- 5 prototype tanks subjected to proof test
- 1 prototype subjected to burst test (verified 2.4× design pressure)
- 1 prototype subjected to full-scale fatigue test (147,350 cycles)

### 7.2 Service Life Monitoring
**Fleet Leader Program:**
- 10 instrumented aircraft with strain gauges on tanks
- Data collected: Every flight for first 2 years
- Early teardown: 1 tank at 25,000 FC for lessons learned
- Life extension potential: Based on actual vs. predicted degradation

## 8.0 Engineering Reports Summary

| Document ID | Title | Rev | Date |
|-------------|-------|-----|------|
| AMPEL-STRESS-H2-TANK-001 | Structural Analysis Report | D | 2024-06-30 |
| AMPEL-THERM-H2-TANK-001 | Thermal Analysis Report | B | 2024-05-15 |
| AMPEL-LCF-H2-TANK-001 | Low-Cycle Fatigue Assessment | A | 2024-06-22 |
| AMPEL-ENV-H2-TANK-002 | Environmental Qualification | A | 2024-07-10 |
| AMPEL-MAT-CRYO-001 | Material Characterization | C | 2024-04-08 |
| AMPEL-PROB-H2-TANK-001 | Probabilistic Analysis | A | 2024-08-01 |

## 9.0 Software Tools and Versions

**Analysis Software:**
- ANSYS Mechanical 2024 R1 (FEA)
- NASGRO 9.4 (fracture mechanics)
- MATLAB R2024a (probabilistic analysis)
- Python 3.11 (post-processing scripts)

**Verification:**
- All software validated per AMPEL-PROC-SW-VAL-001
- Benchmark problems solved for each analysis type
- Results within 5% of handbook solutions

## 10.0 Uncertainty and Conservatism

**Conservative Assumptions:**
- Initial flaw size: 0.5 mm (actual NDT capability: 0.3 mm)
- Safety factor: 3.0 on test life (regulatory minimum: 2.5)
- Stress analysis: 95th percentile of load spectrum used
- Material properties: Lower bound (B-basis) used

**Total Conservatism:** Approximately 5× margin between actual capability and certified limit
