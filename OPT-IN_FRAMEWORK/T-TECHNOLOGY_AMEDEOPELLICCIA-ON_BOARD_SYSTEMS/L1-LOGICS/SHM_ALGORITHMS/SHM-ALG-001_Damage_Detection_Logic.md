# SHM-ALG-001: Damage Detection Logic

## Document ID
**SHM-ALG-001**

## Title
Damage Detection Algorithm Specification

## Purpose
Specify the damage detection algorithms used in the SHM system for identifying structural anomalies based on sensor data.

## Algorithm Overview

### Detection Framework
```
Raw Sensor Data
      │
      ▼
┌─────────────────┐
│  Preprocessing  │ ← Band-pass filtering, windowing
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Baseline        │ ← Temperature-indexed baseline selection
│ Subtraction     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Feature         │ ← Energy, amplitude, ToF, correlation
│ Extraction      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Damage          │ ← Threshold comparison, pattern recognition
│ Detection       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Localization    │ ← TDoA, ellipse intersection
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Severity        │ ← ML classification
│ Classification  │
└─────────────────┘
```

## Algorithm 1: Baseline Subtraction

### Method
Subtract temperature-compensated reference signal from current measurement to isolate damage-related changes.

### Equation
```
ΔS(t) = S_current(t) - α(T) × S_baseline(t, T_ref)
```

Where:
- ΔS(t) = Residual signal (damage indicator)
- S_current(t) = Current measurement
- S_baseline(t, T_ref) = Temperature-indexed baseline
- α(T) = Temperature compensation factor

### Parameters
| Parameter | Value | Units |
|-----------|-------|-------|
| Temperature bins | 5°C intervals | °C |
| Baseline library size | 50 baselines | per sensor pair |
| Compensation accuracy | ±2% | amplitude |

## Algorithm 2: Damage Index Calculation

### Root Mean Square Deviation (RMSD)
```
DI_RMSD = √(Σ[ΔS(t)]² / N)
```

### Correlation Coefficient Complement
```
DI_CC = 1 - ρ(S_current, S_baseline)
```

Where ρ is Pearson correlation coefficient.

### Energy Ratio
```
DI_E = E_current / E_baseline
```

### Combined Damage Index
```
DI_combined = w₁×DI_RMSD + w₂×DI_CC + w₃×log(DI_E)
```

Default weights: w₁=0.4, w₂=0.4, w₃=0.2

## Algorithm 3: Threshold-Based Detection

### Fixed Threshold
```
DAMAGE_DETECTED = (DI_combined > Th_fixed)
```

### Adaptive Threshold
```
Th_adaptive = μ_baseline + k × σ_baseline
```

Where:
- μ_baseline = Mean DI over baseline period
- σ_baseline = Standard deviation of baseline DI
- k = Sensitivity factor (default k=3)

### Detection Criteria
| Level | Threshold | Action |
|-------|-----------|--------|
| Normal | DI < Th_low | Continue monitoring |
| Watch | Th_low ≤ DI < Th_high | Increase monitoring frequency |
| Alert | DI ≥ Th_high | Generate maintenance alert |

## Algorithm 4: Machine Learning Classification

### Random Forest Classifier
| Parameter | Value |
|-----------|-------|
| Trees | 100 |
| Max depth | 10 |
| Min samples split | 5 |
| Features | DI_RMSD, DI_CC, DI_E, ToF change |

### Training Data
| Category | Samples | Source |
|----------|---------|--------|
| Pristine | 10,000 | Baseline flights |
| Fatigue crack | 500 | Coupon tests |
| Delamination | 500 | Element tests |
| Disbond | 300 | Element tests |
| Impact (BVID) | 400 | Drop tests |

### Classification Output
| Class | Probability Threshold |
|-------|----------------------|
| No damage | P > 0.7 |
| Possible damage | 0.3 ≤ P ≤ 0.7 |
| Damage confirmed | P < 0.3 for pristine |

## Algorithm 5: Localization

### Time Difference of Arrival (TDoA)
```
d₁ - d₂ = c × (t₁ - t₂)
```

Where:
- d₁, d₂ = Distances to sensors 1 and 2
- c = Wave velocity (temperature compensated)
- t₁, t₂ = Arrival times at sensors 1 and 2

### Ellipse Intersection
For each sensor pair, damage lies on ellipse with foci at sensor locations. Intersection of multiple ellipses localizes damage.

### Localization Accuracy
| Configuration | Accuracy |
|---------------|----------|
| 3 sensors | ±30 mm |
| 4 sensors | ±20 mm |
| 6 sensors | ±15 mm |

## Performance Requirements

| Metric | Requirement |
|--------|-------------|
| True positive rate | ≥90% at a90/95 |
| False positive rate | ≤5% |
| Processing time | ≤500 ms per zone |
| Memory usage | ≤128 MB per zone |

## Traceability
- Parent Requirement: [53-00-03-01-005](../../A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md)

---

## Document Control

| Field | Value |
|-------|-------|
| Generated with | AI assistance (GitHub Copilot) |
| Prompted by | **Amedeo Pelliccia** |
| Status | **DRAFT** |
| Repository | `AMPEL360-BWB-H2-Hy-E` |
| Last AI Update | 2025-11-27 |

---
