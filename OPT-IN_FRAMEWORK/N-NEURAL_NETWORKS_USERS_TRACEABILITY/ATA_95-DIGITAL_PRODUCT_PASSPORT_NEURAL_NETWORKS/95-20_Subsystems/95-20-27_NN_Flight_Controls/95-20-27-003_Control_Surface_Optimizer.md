# 95-20-27-003 — Control Surface Optimizer

**Document ID:** 95-20-27-003  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active  
**Model Version:** v1.4

---

## 1. Purpose

The Control Surface Optimizer is a real-time neural network that determines optimal control surface deflections to achieve commanded aircraft state while minimizing drag, structural loads, and energy consumption.

---

## 2. Technical Specifications

### 2.1 Model Architecture

- **Type**: Deep Reinforcement Learning (Proximal Policy Optimization)
- **Framework**: PyTorch
- **Input Dimensions**: 18 (state vector + commands)
- **Output Dimensions**: 8 (control surface deflections)
- **Hidden Layers**: 6 × 512 neurons
- **Activation**: ReLU
- **Model Size**: 8.7 MB (ONNX)

### 2.2 Performance

| Metric | Specification | Achieved |
|--------|---------------|----------|
| Inference Latency | <10ms | 6.2ms (avg) |
| Drag Reduction | ≥5% | 6.8% (cruise) |
| Load Reduction | ≥15% | 18.3% (gust) |
| Convergence Time | <100ms | 78ms (typical) |
| Memory Footprint | <15 MB | 8.7 MB |

---

## 3. Inputs

### 3.1 Aircraft State

| Parameter | Symbol | Range | Units | Source |
|-----------|--------|-------|-------|--------|
| Angle of Attack | α | -10° to +25° | deg | Air Data |
| Sideslip Angle | β | -15° to +15° | deg | Air Data |
| Roll Angle | φ | -180° to +180° | deg | AHRS |
| Pitch Angle | θ | -30° to +30° | deg | AHRS |
| Heading | ψ | 0° to 360° | deg | AHRS |
| Altitude | h | 0 to 41,000 | ft | Air Data |
| Airspeed | V | 50 to 450 | kt | Air Data |

### 3.2 Pilot Commands

| Command | Symbol | Range | Units | Source |
|---------|--------|-------|-------|--------|
| Pitch Command | θ_cmd | -15° to +15° | deg | FCS |
| Roll Command | φ_cmd | -60° to +60° | deg | FCS |
| Yaw Command | ψ̇_cmd | -10° to +10° | deg/s | FCS |
| Thrust Command | T_cmd | 0 to 100 | % | FCS |

### 3.3 Aerodynamic Predictions

| Input | Source | Description |
|-------|--------|-------------|
| CL, CD, Cm, Cn, Cy, Cl | Aero Predictor (95-20-27-002) | Current aerodynamic coefficients |

### 3.4 Constraints

| Constraint | Range | Units |
|------------|-------|-------|
| Structural Load Limit | -2.5g to +2.5g | g |
| Flutter Margin | >20% | % |
| Actuator Rate Limit | 60°/s | deg/s |
| Power Available | Variable | kW |

---

## 4. Outputs

### 4.1 Control Surface Commands

| Surface | Symbol | Range | Units | Rate Limit |
|---------|--------|-------|-------|------------|
| Left Elevator | δe_L | -25° to +15° | deg | 60°/s |
| Right Elevator | δe_R | -25° to +15° | deg | 60°/s |
| Left Aileron | δa_L | -25° to +25° | deg | 60°/s |
| Right Aileron | δa_R | -25° to +25° | deg | 60°/s |
| Left Rudder | δr_L | -25° to +25° | deg | 60°/s |
| Right Rudder | δr_R | -25° to +25° | deg | 60°/s |
| Left Flap | δf_L | 0° to 40° | deg | 10°/s |
| Right Flap | δf_R | 0° to 40° | deg | 10°/s |

### 4.2 Optimization Metrics

| Metric | Output |
|--------|--------|
| Predicted Drag | CD_opt |
| Load Factor | n_z |
| Trim Efficiency | η_trim |
| Power Consumption | P_act |

---

## 5. Optimization Objective

### 5.1 Cost Function

The optimizer minimizes a weighted cost function:

```
J = w_track·||x - x_cmd||² + w_drag·CD + w_load·||F_struct||² + w_energy·P_act + w_smooth·||Δδ||²
```

Where:
- **w_track**: Tracking error weight (highest priority)
- **w_drag**: Drag penalty
- **w_load**: Structural load penalty
- **w_energy**: Energy consumption penalty
- **w_smooth**: Control surface smoothness penalty

### 5.2 Weight Tuning

Weights are dynamically adjusted based on flight phase:

| Phase | Tracking | Drag | Load | Energy | Smooth |
|-------|----------|------|------|--------|--------|
| Takeoff | 1.0 | 0.1 | 0.5 | 0.2 | 0.3 |
| Climb | 0.8 | 0.3 | 0.4 | 0.4 | 0.2 |
| Cruise | 0.7 | 0.8 | 0.2 | 0.5 | 0.1 |
| Descent | 0.8 | 0.5 | 0.3 | 0.6 | 0.2 |
| Approach | 0.9 | 0.1 | 0.4 | 0.2 | 0.4 |
| Landing | 1.0 | 0.0 | 0.5 | 0.1 | 0.5 |

---

## 6. Training

### 6.1 Training Environment

- **Simulator**: X-Plane 12 + Custom BWB Model
- **Episodes**: 50,000 flight hours
- **Scenarios**: All phases, weather, failures
- **Reward Signal**: Based on cost function J

### 6.2 Training Data

Refer to: `Data/Training_Datasets/95-20-27-602_Control_Law_Flight_Data.parquet`

---

## 7. Validation

### 7.1 Validation Approach

- **Digital Twin**: 10,000 hours in AMPEL360 digital twin
- **Iron Bird**: 500 hours HIL testing
- **Flight Test**: 100 hours in-flight validation

### 7.2 Validation Results

| Test Scenario | Drag Reduction | Tracking RMSE | Load Reduction |
|---------------|----------------|---------------|----------------|
| Cruise (steady) | 7.2% | 0.3° | 12% |
| Climb (transient) | 5.8% | 0.5° | 15% |
| Turbulence (moderate) | 6.3% | 0.8° | 22% |
| Wind shear | 4.9% | 1.1° | 18% |

Refer to: `ASSETS/Test_Data/95-20-27-A-303_IronBird_Validation_Results.xlsx`

---

## 8. Deployment

### 8.1 Runtime Environment

- **Platform**: IMA Partition (via 95-20-42)
- **Framework**: ONNX Runtime
- **Execution Frequency**: 100 Hz
- **Priority**: Critical (highest)

### 8.2 Integration

- **Input Interface**: `ASSETS/Interface_Specs/95-20-27-A-403_Sensor_and_Bus_Input_Specs.yaml`
- **Output Interface**: `ASSETS/Interface_Specs/95-20-27-A-404_Actuator_Command_Output_Specs.yaml`

---

## 9. Monitoring

### 9.1 Health Metrics

- **Inference latency**: Real-time tracking (<10ms)
- **Tracking error**: Deviation from commanded state
- **Control authority**: Remaining deflection margin
- **Actuator health**: Rate limiting and saturation

### 9.2 Performance Metrics

- **Drag coefficient**: Real-time CD monitoring
- **Fuel efficiency**: kg H₂ per km
- **Load factor**: Structural stress monitoring
- **Power consumption**: Actuator power draw

Refer to: `ASSETS/Performance_Data/95-20-27-A-204_Inference_Latency_Benchmarks.csv`

---

## 10. Failover

### 10.1 Degradation Criteria

- Inference latency >15ms (sustained)
- Tracking error >5° for >2 seconds
- Control saturation on multiple surfaces
- Actuator failures

### 10.2 Backup Strategy

- **Primary**: Switch to conventional control allocation
- **Secondary**: Direct law (pilot commands → surfaces)
- **Tertiary**: Mechanical reversion (if available)

---

## 11. Model Card

**Full Model Card**: `ASSETS/Model_Cards/95-20-27-A-102_Control_Surface_Optimizer_v1.4.yaml`

---

## 12. Source Code

**Location**: `Models/Source/control_surface_optimizer_v1.4.py`

**Training Script**: `Models/Source/training_scripts/train_control_optimizer.py`

**Configuration**: `Models/Configs/training_config_control_surface.yaml`

---

## 13. References

- [95-20-27-001_FCS_NN_Overview.md](95-20-27-001_FCS_NN_Overview.md)
- [95-20-27-002_Aerodynamic_Predictor.md](95-20-27-002_Aerodynamic_Predictor.md)
- [95-20-27-004_Gust_Load_Alleviation.md](95-20-27-004_Gust_Load_Alleviation.md)
- Sutton & Barto (2018): "Reinforcement Learning: An Introduction"

---

## Document Control

- **Owner**: AMPEL360 FCS_NN Team
- **Version**: 1.0
- **Status**: Active
- **Classification**: Technical Reference
- **Last Updated**: 2025-11-17
