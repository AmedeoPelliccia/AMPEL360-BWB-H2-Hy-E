# 95-20-27-005 — Flight Envelope Protection NN

**Document ID:** 95-20-27-005  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active  
**Model Version:** v1.0

---

## 1. Purpose

The Flight Envelope Protection Neural Network provides real-time monitoring and prediction of flight envelope boundaries, preventing exceedances of critical parameters (α, speed, load factor, attitude) with predictive intervention.

---

## 2. Technical Specifications

### 2.1 Model Architecture

- **Type**: Ensemble of Feedforward Neural Networks
- **Framework**: PyTorch
- **Ensemble Size**: 5 models (voting mechanism)
- **Input Dimensions**: 20 (aircraft state + environmental)
- **Output Dimensions**: 12 (envelope boundaries + margins)
- **Hidden Layers**: 5 × 256 neurons per model
- **Activation**: Leaky ReLU
- **Model Size**: 6.2 MB total (ONNX)

### 2.2 Performance

| Metric | Specification | Achieved |
|--------|---------------|----------|
| Inference Latency | <5ms | 3.1ms (avg) |
| False Positive Rate | <0.1% | 0.04% |
| False Negative Rate | 0% (critical) | 0% (validated) |
| Prediction Horizon | 1000ms | 1200ms (typical) |
| Memory Footprint | <10 MB | 6.2 MB |

---

## 3. Protected Parameters

### 3.1 Aerodynamic Limits

| Parameter | Symbol | Soft Limit | Hard Limit | Units |
|-----------|--------|------------|------------|-------|
| Angle of Attack | α | 20° | 25° | deg |
| Sideslip Angle | β | 12° | 15° | deg |
| Bank Angle | φ | 60° | 67° | deg |
| Pitch Angle | θ | 25° | 30° | deg |

### 3.2 Speed Limits

| Limit | Symbol | Value | Units | Condition |
|-------|--------|-------|-------|-----------|
| Minimum Speed | V_min | V_stall + 20% | kt | All configs |
| Maximum Speed | V_max | 450 | kt | Structural |
| Maximum Mach | M_max | 0.85 | - | Aero |
| Maneuver Speed | V_a | 280 | kt | Full deflection |

### 3.3 Load Factor Limits

| Limit | Clean | Flaps Extended | Units |
|-------|-------|----------------|-------|
| Positive Limit | +2.5g | +2.0g | g |
| Negative Limit | -1.0g | 0.0g | g |

### 3.4 Angular Rate Limits

| Parameter | Limit | Units |
|-----------|-------|-------|
| Maximum Pitch Rate | 20 | deg/s |
| Maximum Roll Rate | 30 | deg/s |
| Maximum Yaw Rate | 15 | deg/s |

---

## 4. Inputs

### 4.1 Aircraft State

| Parameter | Source | Sampling Rate |
|-----------|--------|---------------|
| α, β, V, M, h | Air Data System | 100 Hz |
| φ, θ, ψ | AHRS | 100 Hz |
| p, q, r | IMU/IRU | 100 Hz |
| n_x, n_y, n_z | IMU | 100 Hz |
| Configuration | FCS (flaps, gear, spoilers) | 20 Hz |

### 4.2 Environmental Conditions

| Parameter | Source | Purpose |
|-----------|--------|---------|
| Wind Speed/Direction | Air Data | V_stall adjustment |
| Density Altitude | Air Data | Performance limits |
| Temperature | Air Data | Engine thrust available |
| Icing Conditions | Ice Detection | Stall margin adjustment |

### 4.3 Control State

| Parameter | Source | Purpose |
|-----------|--------|---------|
| Pilot Stick Inputs | FCS | Intent prediction |
| Autopilot Commands | FCS | Mode awareness |
| Control Surface Positions | FCS | Authority remaining |
| Throttle Position | FADEC | Energy state |

---

## 5. Outputs

### 5.1 Envelope Boundaries

For each protected parameter, the model outputs:

| Output | Description | Range |
|--------|-------------|-------|
| Current Value | Real-time parameter value | Actual units |
| Soft Limit | Warning threshold | Actual units |
| Hard Limit | Maximum allowed value | Actual units |
| Time to Limit | Predicted time until exceedance | 0-5 seconds |
| Margin | Distance from current to limit | % |

### 5.2 Protection Commands

| Output | Description | Authority |
|--------|-------------|-----------|
| Pitch Correction | δe adjustment to prevent α or n_z exceedance | ±15° |
| Roll Correction | δa adjustment to prevent φ exceedance | ±20° |
| Speed Correction | Thrust/drag adjustment for V limits | ±30% |
| Attitude Correction | Multi-axis correction for unusual attitudes | Full |

### 5.3 Crew Alerts

| Alert Level | Condition | Action |
|-------------|-----------|--------|
| Advisory | Margin <20% | Visual cue on PFD |
| Caution | Margin <10% | Amber alert + audio |
| Warning | Margin <5% | Red alert + stick shaker |
| Protection Active | Limit reached | Override pilot input |

---

## 6. Protection Modes

### 6.1 Normal Law

- **All protections active**
- Full envelope protection
- Predictive intervention
- Pilot can override with sustained force

### 6.2 Alternate Law

- **Reduced protections**
- Hard limits only (soft limits disabled)
- Increased margins (conservative)
- Easier pilot override

### 6.3 Direct Law

- **No NN protections**
- Fallback to conventional envelope protection
- Simple threshold-based limits
- Full pilot authority within hard limits

---

## 7. Predictive Logic

### 7.1 Trajectory Prediction

The system predicts aircraft trajectory using:

```
x(t+Δt) = f_NN(x(t), u(t), u_pilot(t))
```

Where:
- **x(t)**: Current state vector
- **u(t)**: Current control inputs
- **u_pilot(t)**: Pilot stick deflection (intent)
- **Δt**: Prediction horizon (up to 1.2s)

### 7.2 Intervention Criteria

Protection activates when:

```
IF (predicted_exceedance_time < threshold) AND (margin < margin_min):
    Apply protection commands
```

Thresholds vary by parameter:
- **α protection**: 1.0s ahead
- **Speed protection**: 2.0s ahead
- **Load factor**: 0.5s ahead
- **Attitude**: 1.5s ahead

---

## 8. Training

### 8.1 Training Data

- **Flight Test Data**: 5,000 hours with deliberate envelope probing
- **Simulator Data**: 100,000 hours covering all edge cases
- **Test Pilot Data**: 1,000 hours intentional limit approaches

Refer to: `Data/Training_Datasets/95-20-27-602_Control_Law_Flight_Data.parquet`

### 8.2 Edge Cases

Training specifically includes:
- Stall entry and recovery
- High-speed descents
- Unusual attitude recoveries
- Wind shear encounters
- Wake turbulence
- System failures (engine, control surface)

---

## 9. Validation

### 9.1 Validation Approach

- **Iron Bird**: 1,000 hours HIL testing with limit approaches
- **Flight Test**: 200 hours with test pilots deliberately probing limits
- **Monte Carlo**: 50,000 randomized scenarios

### 9.2 Validation Results

| Test Scenario | False Positives | False Negatives | Intervention Time |
|---------------|-----------------|-----------------|-------------------|
| Stall approach | 0.02% | 0% | 1.1s before stall |
| High-speed dive | 0.05% | 0% | 2.3s before V_max |
| Excessive bank | 0.03% | 0% | 1.5s before 67° |
| Load factor | 0.01% | 0% | 0.6s before 2.5g |

**Critical Result**: Zero false negatives (100% protection reliability)

Refer to: `ASSETS/Test_Data/95-20-27-A-303_IronBird_Validation_Results.xlsx`

---

## 10. Integration

### 10.1 FCS Integration

The envelope protection integrates with:
- **Control Surface Optimizer (95-20-27-003)**: Coordinate optimal and safe commands
- **Gust Load Alleviation (95-20-27-004)**: Ensure gust responses stay within envelope
- **Baseline FCS**: Override capability for protection

### 10.2 Interface Specs

- **Input**: `ASSETS/Interface_Specs/95-20-27-A-403_Sensor_and_Bus_Input_Specs.yaml`
- **Output**: `ASSETS/Interface_Specs/95-20-27-A-404_Actuator_Command_Output_Specs.yaml`

---

## 11. Pilot Interface

### 11.1 Primary Flight Display (PFD)

- **Envelope Indicators**: Visual display of margins on PFD scales
- **Color Coding**: Green (>20%), Amber (10-20%), Red (<10%)
- **Predictive Trend Vectors**: Show trajectory toward limits

### 11.2 EICAS/ECAM

- **Protection Status**: "PROT ACTIVE" when intervening
- **Mode Annunciation**: "NORM LAW", "ALT LAW", "DIRECT LAW"
- **Parameter Exceedance Warnings**: "OVERSPEED", "STALL", etc.

### 11.3 Override Capability

Pilots can override protection by:
- **Sustained Force**: >150 N stick force for >2 seconds
- **Override Button**: Dedicated "PROT OVRD" button (latching)
- **Alternate Law Selection**: Mode selector to ALT or DIRECT

---

## 12. Certification

### 12.1 Compliance

- **CS-25.143**: Stall protection
- **CS-25.253**: High-speed characteristics
- **CS-25.331**: Load factor limits
- **CS-25.341**: Gust load factors
- **CS-25.1581**: Safety equipment and markings

### 12.2 Validation Evidence

Refer to: `ASSETS/Certification/95-20-27-A-503_Verification_Matrix.xlsx`

---

## 13. Model Card

**Full Model Card**: `ASSETS/Model_Cards/95-20-27-A-104_Envelope_Protection_v1.0.yaml`

---

## 14. Source Code

**Location**: `Models/Source/envelope_protection_v1.0.py`

**Training Script**: `Models/Source/training_scripts/train_envelope_protection.py`

**Configuration**: `Models/Configs/training_config_envelope.yaml`

---

## 15. References

- [95-20-27-001_FCS_NN_Overview.md](95-20-27-001_FCS_NN_Overview.md)
- [95-20-27-003_Control_Surface_Optimizer.md](95-20-27-003_Control_Surface_Optimizer.md)
- CS-25 Certification Specifications
- AC 25-7D: Flight Test Guide

---

## Document Control

- **Owner**: AMPEL360 FCS_NN Team
- **Version**: 1.0
- **Status**: Active
- **Classification**: Technical Reference
- **Last Updated**: 2025-11-17
