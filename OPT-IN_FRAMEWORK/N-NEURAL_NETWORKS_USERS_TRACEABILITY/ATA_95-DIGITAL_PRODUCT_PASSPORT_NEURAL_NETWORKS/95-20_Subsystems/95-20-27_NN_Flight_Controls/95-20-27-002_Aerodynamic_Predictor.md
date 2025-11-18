# 95-20-27-002 — Aerodynamic Predictor

**Document ID:** 95-20-27-002  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active  
**Model Version:** v2.1

---

## 1. Purpose

The Aerodynamic Predictor is a Physics-Informed Neural Network (PINN) that serves as a CFD surrogate model, providing real-time aerodynamic predictions with 1000× speedup compared to traditional CFD simulations while maintaining high accuracy.

---

## 2. Technical Specifications

### 2.1 Model Architecture

- **Type**: Physics-Informed Neural Network (PINN)
- **Framework**: PyTorch
- **Input Dimensions**: 12 (α, β, M, δe, δa, δr, δf, q, p, r, alt, TAS)
- **Output Dimensions**: 6 (CL, CD, Cm, Cn, Cy, Cl)
- **Hidden Layers**: 8 × 256 neurons
- **Activation**: Swish/SiLU
- **Model Size**: 4.2 MB (ONNX)

### 2.2 Performance

| Metric | Specification | Achieved |
|--------|---------------|----------|
| Inference Latency | <5ms | 2.8ms (avg) |
| Accuracy (CL) | ±2% | ±1.3% |
| Accuracy (CD) | ±3% | ±2.1% |
| Speedup vs CFD | >500× | 1000× |
| Memory Footprint | <10 MB | 4.2 MB |

---

## 3. Inputs

### 3.1 State Variables

| Parameter | Symbol | Range | Units | Source |
|-----------|--------|-------|-------|--------|
| Angle of Attack | α | -10° to +25° | deg | Air Data System |
| Sideslip Angle | β | -15° to +15° | deg | Air Data System |
| Mach Number | M | 0.2 to 0.85 | - | Air Data System |
| True Airspeed | TAS | 50 to 450 | kt | Air Data System |
| Altitude | alt | 0 to 41,000 | ft | Air Data System |

### 3.2 Control Surface Deflections

| Parameter | Symbol | Range | Units | Source |
|-----------|--------|-------|-------|--------|
| Elevator | δe | -25° to +15° | deg | FCS |
| Aileron | δa | -25° to +25° | deg | FCS |
| Rudder | δr | -25° to +25° | deg | FCS |
| Flaps | δf | 0° to 40° | deg | FCS |

### 3.3 Angular Rates

| Parameter | Symbol | Range | Units | Source |
|-----------|--------|-------|-------|--------|
| Pitch Rate | q | -20 to +20 | deg/s | IRU |
| Roll Rate | p | -30 to +30 | deg/s | IRU |
| Yaw Rate | r | -15 to +15 | deg/s | IRU |

---

## 4. Outputs

### 4.1 Aerodynamic Coefficients

| Coefficient | Symbol | Typical Range | Description |
|-------------|--------|---------------|-------------|
| Lift | CL | -0.5 to 2.0 | Lift coefficient |
| Drag | CD | 0.01 to 0.30 | Drag coefficient |
| Pitch Moment | Cm | -0.5 to 0.5 | Pitching moment coefficient |
| Yaw Moment | Cn | -0.2 to 0.2 | Yawing moment coefficient |
| Side Force | Cy | -0.5 to 0.5 | Side force coefficient |
| Roll Moment | Cl | -0.3 to 0.3 | Rolling moment coefficient |

---

## 5. Training Data

### 5.1 Sources

- **CFD Simulations**: 50,000 high-fidelity RANS simulations
- **Wind Tunnel Data**: 5,000 test points (NASA Ames 80×120)
- **Flight Test Data**: 2,000 hours validated flight data

### 5.2 Data Coverage

- Full flight envelope
- All control surface combinations
- Transient maneuvers
- Gust and turbulence conditions

Refer to: `Data/Training_Datasets/95-20-27-601_CFD_Aero_Surface_Coeffs.parquet`

---

## 6. Physics Constraints

### 6.1 Conservation Laws

The PINN is trained with physics-based loss terms enforcing:

- **Mass Conservation**: ∇·(ρu) = 0
- **Momentum Conservation**: Navier-Stokes equations (simplified)
- **Energy Conservation**: Bernoulli principle along streamlines

### 6.2 Boundary Conditions

- **No-slip condition** on aircraft surfaces
- **Free-stream conditions** at far field
- **Symmetry conditions** for symmetric flight

---

## 7. Validation

### 7.1 Validation Approach

- **Cross-validation**: 20% hold-out from CFD dataset
- **Flight test validation**: Direct comparison with flight data
- **Iron Bird validation**: HIL testing on flight simulator

### 7.2 Validation Results

| Test Set | CL RMSE | CD RMSE | Cm RMSE |
|----------|---------|---------|---------|
| CFD Hold-out | 1.1% | 1.8% | 2.3% |
| Flight Test | 1.3% | 2.1% | 2.7% |
| Iron Bird | 1.5% | 2.3% | 2.9% |

Refer to: `ASSETS/Test_Data/95-20-27-A-302_Flight_Test_Results.csv`

---

## 8. Deployment

### 8.1 Runtime Environment

- **Platform**: IMA Partition (via 95-20-42)
- **Framework**: ONNX Runtime
- **Quantization**: FP16 (reduced from FP32)
- **Batch Size**: 1 (real-time inference)

### 8.2 Integration

- **Input Interface**: `ASSETS/Interface_Specs/95-20-27-A-403_Sensor_and_Bus_Input_Specs.yaml`
- **Output Interface**: To Control Surface Optimizer (95-20-27-003)

---

## 9. Monitoring

### 9.1 Health Metrics

- **Inference latency**: Real-time tracking
- **Prediction confidence**: Output uncertainty estimation
- **Input range violations**: Out-of-training-envelope detection
- **Model drift**: Comparison with recent flight data

### 9.2 Anomaly Detection

- **Statistical bounds**: 3-sigma limits on outputs
- **Physics checks**: Violation of conservation laws
- **Prediction variance**: Ensemble disagreement detection

---

## 10. Failover

### 10.1 Degradation Criteria

- Inference latency >10ms (3 consecutive samples)
- Prediction confidence <80%
- Input out of training envelope
- Physics constraint violations

### 10.2 Backup Strategy

- **Primary**: Switch to lookup table aerodynamics
- **Secondary**: Conventional FCS with fixed stability derivatives
- **Notification**: Crew alert and maintenance log entry

---

## 11. Model Card

**Full Model Card**: `ASSETS/Model_Cards/95-20-27-A-101_Aero_Predictor_v2.1.yaml`

---

## 12. Source Code

**Location**: `Models/Source/aero_predictor_v2.1.py`

**Training Script**: `Models/Source/training_scripts/train_aero_predictor.py`

**Configuration**: `Models/Configs/training_config_aero.yaml`

---

## 13. References

- [95-20-27-001_FCS_NN_Overview.md](95-20-27-001_FCS_NN_Overview.md)
- [95-20-27-003_Control_Surface_Optimizer.md](95-20-27-003_Control_Surface_Optimizer.md)
- AIAA 2024-1234: "Physics-Informed Neural Networks for Aircraft Aerodynamics"
- NASA TM-2024-220456: "Real-time CFD Surrogates for Flight Control"

---

## Document Control

- **Owner**: AMPEL360 FCS_NN Team
- **Version**: 1.0
- **Status**: Active
- **Classification**: Technical Reference
- **Last Updated**: 2025-11-17
