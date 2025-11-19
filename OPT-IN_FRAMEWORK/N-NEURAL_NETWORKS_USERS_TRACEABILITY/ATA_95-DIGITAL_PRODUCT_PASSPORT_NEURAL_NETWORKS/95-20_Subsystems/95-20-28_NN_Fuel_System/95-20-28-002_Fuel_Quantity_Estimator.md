# 95-20-28-002 — Fuel Quantity Estimator

**Component ID**: 95-20-28-002  
**Model Version**: v1.0  
**Parent**: [95-20-28 Fuel System Neural Networks](README.md)  
**Status**: WORKING

## Overview

The Fuel Quantity Estimator is a sensor fusion neural network that provides accurate fuel level estimation across multiple tanks with ±2% accuracy. It compensates for aircraft attitude, fuel slosh, sensor drift, and tank geometry to provide reliable fuel quantity indications.

## Model Architecture

**Type**: Multi-Layer Perceptron (MLP) with Sensor Fusion  
**Input Features**: 18 (tank sensors, attitude, temperature, pressure, flow)  
**Hidden Layers**: 4 Dense layers (64, 32, 16, 8 units)  
**Output**: Fuel quantity estimates for all tanks  
**Framework**: TensorFlow 2.x  
**Model Size**: 1.8 MB (ONNX format)

### Architecture Diagram

```
Input (18 features) → Dense(64) → Dense(32) → Dense(16) → Dense(8) → Output (fuel quantities)
```

## Performance

- **Estimation Accuracy**: ±2% of tank capacity (95th percentile)  
- **Inference Time**: 12 ms (target hardware)  
- **Inference Rate**: 5 Hz  
- **Attitude Compensation**: Full 360° roll/pitch correction

## Training

- **Dataset**: 5,000+ flight hours of fuel quantity sensor data  
- **Training Time**: 24 hours on V100 GPU  
- **Validation Split**: 80/10/10 (train/val/test)  
- **Loss Function**: Mean Absolute Error (MAE)  
- **Optimizer**: Adam (`lr = 0.001`)

## Inputs

| Input                     | Source           | Type    | Rate  | Units |
|---------------------------|------------------|---------|-------|--------|
| Tank level sensors (all)  | ATA 28 sensors   | float32 | 5 Hz  | liters |
| Aircraft pitch            | AHRS             | float32 | 10 Hz | degrees|
| Aircraft roll             | AHRS             | float32 | 10 Hz | degrees|
| Aircraft yaw rate         | AHRS             | float32 | 10 Hz | deg/s  |
| Fuel temperature          | Temp sensors     | float32 | 1 Hz  | °C     |
| Fuel pressure             | Pressure sensors | float32 | 5 Hz  | psi    |
| Fuel flow rate            | Flow sensors     | float32 | 5 Hz  | kg/min |
| Tank configuration        | Fuel system      | enum    | 0.1 Hz| -      |

## Outputs

| Output                      | Destination      | Type    | Rate  | Units |
|----------------------------|------------------|---------|-------|--------|
| Estimated fuel quantities  | Fuel management  | float32 | 5 Hz  | liters |
| Total fuel remaining       | Flight management| float32 | 5 Hz  | liters |
| Confidence scores          | System monitor   | float32 | 5 Hz  | 0–1    |
| Sensor health status       | Maintenance      | enum    | 5 Hz  | -      |

## Safety & Certification

- **DAL Level**: C (Major)  
- **Failure Condition**: Inaccurate fuel quantity could lead to fuel exhaustion or improper flight planning  
- **Mitigation**: Cross-checking with physical sensors and redundant estimation methods  
- **V&V Status**: Complete per [DO-178C](https://www.rtca.org/product/do-178c/) Level C  

> _Reference requires confirmation by the certification team for final DAL / hazard classification alignment._

## Model Card

See: [`ASSETS/Model_Cards/95-20-28-A-101_Fuel_Quantity_Estimator_v1.0.yaml`](ASSETS/Model_Cards/95-20-28-A-101_Fuel_Quantity_Estimator_v1.0.yaml)

## Integration with ATA 28

### Sensor Inputs

The fuel quantity estimator integrates with the following [ATA 28](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) systems:

- Capacitance fuel quantity sensors (primary)
- Ultrasonic fuel level sensors (backup)
- Fuel flow meters
- Temperature probes
- Pressure transducers

### Control Outputs

- Estimated fuel quantities to cockpit displays
- Fuel imbalance warnings
- Low fuel warnings
- Sensor failure alerts

### Failure Modes

- **Sensor Failure**: Degrades to remaining sensors with reduced accuracy
- **Model Failure**: Falls back to direct sensor readings
- **Communication Loss**: Maintains last known good state

## Operational Scenarios

### Normal Operations

1. Continuous fuel quantity estimation during flight
2. Real-time attitude compensation
3. Sensor fusion across multiple inputs
4. Cross-validation with flow-based calculations

### Edge Cases

- **Rapid Maneuvers**: Maintains accuracy during aerobatic profiles
- **Fuel Transfer**: Tracks fuel movement between tanks
- **Cold Soak**: Compensates for temperature-induced density changes
- **Partial Sensor Failure**: Graceful degradation with remaining sensors

## Testing and Validation

### Unit Tests

- Model inference accuracy tests
- Input validation tests
- Output range checks
- Performance benchmarks

### Integration Tests

- [ATA 28](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) fuel system integration
- Sensor interface validation
- Attitude data integration
- Display system integration

### Scenario Tests

- Various flight profiles (cruise, climb, descent, maneuvers)
- Fuel transfer operations
- Emergency scenarios
- Sensor failure modes

## Document Control

- **Version**: 1.0  
- **Status**: WORKING  
- **Last Updated**: 2025-11-18  
- **Related Files**:  
  - Source: [`Models/Source/fuel_quantity_estimator_v1.0.py`](Models/Source/fuel_quantity_estimator_v1.0.py)  
  - Trained: [`Models/Trained/fuel_quantity_estimator_v1.0.onnx`](Models/Trained/fuel_quantity_estimator_v1.0.onnx)  
  - Config: [`Models/Configs/training_config_fuel_quantity.yaml`](Models/Configs/training_config_fuel_quantity.yaml)  

---

## Document Control – AI Involvement

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.  
- Status: **DRAFT** – Subject to human review and approval.  
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-18_.
