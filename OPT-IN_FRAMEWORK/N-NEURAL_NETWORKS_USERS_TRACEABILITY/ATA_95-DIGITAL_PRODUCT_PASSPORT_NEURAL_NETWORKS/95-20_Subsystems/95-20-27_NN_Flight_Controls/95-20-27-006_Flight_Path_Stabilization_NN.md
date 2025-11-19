# 95-20-27-006 — Flight Path Stabilization NN

**Document ID:** 95-20-27-006  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active  
**Model Version:** v1.1

---

## 1. Purpose

The Flight Path Stabilization Neural Network provides advanced trajectory tracking and disturbance rejection, maintaining commanded flight path with high precision in varying atmospheric conditions.

---

## 2. Technical Specifications

### 2.1 Model Architecture

- **Type**: Model Predictive Control with Neural Network Dynamics
- **Framework**: PyTorch
- **Input Dimensions**: 16 (state + commands + disturbances)
- **Output Dimensions**: 4 (rate commands: p_cmd, q_cmd, r_cmd, T_cmd)
- **Hidden Layers**: 6 × 384 neurons
- **Activation**: Swish/SiLU
- **MPC Horizon**: 2.0 seconds (20 steps @ 10Hz)
- **Model Size**: 7.1 MB (ONNX)

### 2.2 Performance

| Metric | Specification | Achieved |
|--------|---------------|----------|
| Inference Latency | <15ms | 9.8ms (avg) |
| Path Tracking Error | ±0.5° | ±0.3° (avg) |
| Settling Time | <3s | 2.1s (typical) |
| Overshoot | <5% | 2.8% |
| Memory Footprint | <12 MB | 7.1 MB |

---

## 3. Inputs

### 3.1 Aircraft State

| Parameter | Symbol | Range | Units | Source |
|-----------|--------|-------|-------|--------|
| Position (NED) | x, y, z | - | m | INS |
| Velocity (NED) | u, v, w | 0-250 | m/s | INS |
| Euler Angles | φ, θ, ψ | - | deg | AHRS |
| Angular Rates | p, q, r | -30 to +30 | deg/s | IMU |
| Airspeed | V_TAS | 50-450 | kt | Air Data |
| Altitude | h | 0-41,000 | ft | Air Data |

### 3.2 Flight Path Commands

| Command | Symbol | Range | Units | Source |
|---------|--------|-------|-------|--------|
| Desired Track | χ_cmd | 0-360° | deg | FMS/Autopilot |
| Desired Altitude | h_cmd | 0-41,000 | ft | FMS/Autopilot |
| Desired Speed | V_cmd | 50-450 | kt | FMS/Autopilot |
| Vertical Speed | VS_cmd | -3000 to +3000 | ft/min | FMS/Autopilot |

### 3.3 Disturbance Estimates

| Disturbance | Symbol | Range | Units | Source |
|-------------|--------|-------|-------|--------|
| Wind (N-E-D) | w_N, w_E, w_D | ±50 | m/s | Air Data |
| Gust Velocity | w_gust | ±20 | m/s | Aero Predictor |
| Atmospheric Density Error | Δρ | ±10% | % | Air Data |

---

## 4. Outputs

### 4.1 Rate Commands

| Output | Symbol | Range | Units | Description |
|--------|--------|-------|-------|-------------|
| Roll Rate Command | p_cmd | -30 to +30 | deg/s | To inner loop (Control Surface Optimizer) |
| Pitch Rate Command | q_cmd | -20 to +20 | deg/s | To inner loop |
| Yaw Rate Command | r_cmd | -15 to +15 | deg/s | To inner loop |
| Thrust Command | T_cmd | 0-100 | % | To FADEC |

### 4.2 Predicted Trajectory

| Output | Description | Horizon |
|--------|-------------|---------|
| Position Trajectory | x(t), y(t), z(t) | 2.0s |
| Velocity Trajectory | u(t), v(t), w(t) | 2.0s |
| Attitude Trajectory | φ(t), θ(t), ψ(t) | 2.0s |

### 4.3 Performance Metrics

| Metric | Output |
|--------|--------|
| Cross-Track Error | CTE |
| Altitude Error | AE |
| Speed Error | SE |
| Control Effort | CE |

---

## 5. Control Architecture

### 5.1 Cascaded Control Structure

```
Flight Path Stabilization NN (Outer Loop)
    ↓ Rate commands (p_cmd, q_cmd, r_cmd, T_cmd)
Control Surface Optimizer (Inner Loop)
    ↓ Surface deflections (δe, δa, δr, δf)
Aircraft Dynamics
    ↓ Aircraft state
Flight Path Stabilization NN (feedback)
```

### 5.2 Model Predictive Control

The NN implements MPC with cost function:

```
J = Σ [||e_path||²_Q + ||u||²_R + ||Δu||²_S]
```

Where:
- **e_path**: Path tracking error (position, velocity, attitude)
- **u**: Control inputs (rate commands, thrust)
- **Δu**: Control rate (smoothness penalty)
- **Q, R, S**: Weighting matrices (tuned per flight phase)

---

## 6. Operating Modes

### 6.1 Lateral-Directional Modes

| Mode | Description | Inputs | Outputs |
|------|-------------|--------|---------|
| Heading Hold | Maintain constant heading | ψ_cmd | r_cmd |
| Track Hold | Follow ground track | χ_cmd, w_N, w_E | r_cmd, p_cmd |
| Localizer Capture | Follow ILS localizer | LOC deviation | r_cmd, p_cmd |
| LNAV | Follow FMS lateral path | FMS lat path | r_cmd, p_cmd |

### 6.2 Longitudinal Modes

| Mode | Description | Inputs | Outputs |
|------|-------------|--------|---------|
| Altitude Hold | Maintain altitude | h_cmd | q_cmd, T_cmd |
| Vertical Speed | Climb/descend at VS | VS_cmd | q_cmd, T_cmd |
| Glideslope Capture | Follow ILS glideslope | GS deviation | q_cmd, T_cmd |
| VNAV | Follow FMS vertical path | FMS vert path | q_cmd, T_cmd |

### 6.3 Combined Modes

| Mode | Description |
|------|-------------|
| NAV (LNAV+VNAV) | Full 4D trajectory tracking |
| Approach | Precision approach (LOC+GS) |
| Go-Around | Automated go-around sequence |

---

## 7. Training

### 7.1 Training Approach

The NN is trained using:
- **Supervised Learning**: From optimal MPC solutions (10,000 flight hours)
- **Reinforcement Learning**: Fine-tuning in simulator (50,000 flight hours)
- **Imitation Learning**: From expert test pilot data (500 hours)

### 7.2 Training Data

Refer to: `Data/Training_Datasets/95-20-27-602_Control_Law_Flight_Data.parquet`

### 7.3 Training Scenarios

- All flight phases (taxi to landing)
- Variable winds and turbulence
- System failures (engine, control surface)
- Non-standard configurations
- Abnormal procedures

---

## 8. Validation

### 8.1 Validation Approach

- **Digital Twin**: 20,000 hours in AMPEL360 digital twin
- **Iron Bird**: 1,000 hours HIL testing
- **Flight Test**: 300 hours in-flight validation

### 8.2 Validation Results

| Scenario | Cross-Track Error (RMS) | Altitude Error (RMS) | Speed Error (RMS) |
|----------|-------------------------|----------------------|-------------------|
| Straight & Level | 8 m | 12 ft | 1.2 kt |
| Turns (30° bank) | 15 m | 18 ft | 1.8 kt |
| Approach (ILS) | 3 m (lat), 5 ft (vert) | - | 2.1 kt |
| Wind Shear | 25 m | 35 ft | 3.5 kt |
| Turbulence (moderate) | 18 m | 28 ft | 2.4 kt |

Refer to: `ASSETS/Performance_Data/95-20-27-A-201_Tracking_Performance_Results.xlsx`

---

## 9. Disturbance Rejection

### 9.1 Wind Compensation

The system actively compensates for:
- **Steady Winds**: Full compensation using wind estimates
- **Wind Gusts**: Predictive compensation using Gust Load Alleviation data
- **Wind Shear**: Rapid thrust response to maintain energy state
- **Crosswinds**: Coordinated roll-yaw to maintain track

### 9.2 Turbulence Handling

In turbulence:
- **Reduce control gains**: Prevent over-correction
- **Increase smoothness penalty**: Minimize passenger discomfort
- **Widen deadbands**: Tolerate larger tracking errors
- **Coordinate with GLA**: Share disturbance predictions

---

## 10. Integration

### 10.1 Autopilot Integration

The Flight Path Stabilization NN serves as the core of the autopilot:
- **FMS Interface**: Receives lateral and vertical path commands
- **Mode Control Panel**: Pilot selects modes (HDG, ALT, NAV, etc.)
- **Autoland**: Provides precision guidance for CAT III approaches

### 10.2 Flight Management System

- **4D Trajectory**: Tracks time-based waypoints
- **RNP Operations**: Enables RNP 0.1 navigation
- **VNAV Speed Control**: Maintains speed schedule in climb/descent

### 10.3 Interface Specs

- **Input**: `ASSETS/Interface_Specs/95-20-27-A-403_Sensor_and_Bus_Input_Specs.yaml`
- **Output**: Internal to FCS (rate commands)

---

## 11. Performance Monitoring

### 11.1 Real-Time Metrics

Continuously monitored:
- **Tracking Errors**: Cross-track, altitude, speed
- **Control Activity**: Rate command frequency content
- **Model Predictions**: Comparison with actual outcomes
- **Inference Latency**: Timing performance

### 11.2 Post-Flight Analysis

Logged for maintenance analysis:
- **Navigation Performance**: RNP compliance
- **Approach Performance**: Localizer/glideslope tracking
- **Autopilot Disconnects**: Frequency and reasons
- **Model Anomalies**: Out-of-envelope or degraded performance

Refer to: `ASSETS/Performance_Data/95-20-27-A-201_Tracking_Performance_Results.xlsx`

---

## 12. Certification

### 12.1 Compliance

- **CS-25.1329**: Automatic pilot
- **CS-AWO**: All Weather Operations (CAT III autoland)
- **RNP 0.1**: Required Navigation Performance
- **DO-178C**: Software Level A

### 12.2 Validation Evidence

Refer to: `ASSETS/Certification/95-20-27-A-503_Verification_Matrix.xlsx`

---

## 13. Model Card

**Full Model Card**: `ASSETS/Model_Cards/95-20-27-A-105_Flight_Path_Stabilization_v1.1.yaml`

---

## 14. Source Code

**Location**: `Models/Source/flight_path_stabilization_v1.1.py`

**Training Script**: `Models/Source/training_scripts/train_flight_path_stab.py`

**Configuration**: `Models/Configs/training_config_flight_path.yaml`

---

## 15. References

- [95-20-27-001_FCS_NN_Overview.md](95-20-27-001_FCS_NN_Overview.md)
- [95-20-27-003_Control_Surface_Optimizer.md](95-20-27-003_Control_Surface_Optimizer.md)
- [95-20-27-004_Gust_Load_Alleviation.md](95-20-27-004_Gust_Load_Alleviation.md)
- Maciejowski (2002): "Predictive Control with Constraints"

---

## Document Control

- **Owner**: AMPEL360 FCS_NN Team
- **Version**: 1.0
- **Status**: Active
- **Classification**: Technical Reference
- **Last Updated**: 2025-11-17
