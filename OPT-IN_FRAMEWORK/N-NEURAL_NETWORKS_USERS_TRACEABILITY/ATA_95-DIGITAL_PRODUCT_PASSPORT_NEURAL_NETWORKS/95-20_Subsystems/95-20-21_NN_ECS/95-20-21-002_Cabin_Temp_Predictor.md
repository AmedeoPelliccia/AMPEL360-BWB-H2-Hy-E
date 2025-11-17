# 95-20-21-002 — Cabin Temperature Predictor

**Component ID**: 95-20-21-002  
**Model Version**: v1.2  
**Parent**: 95-20-21 ECS Neural Networks  
**Status**: WORKING

## Overview

The Cabin Temperature Predictor is a time-series forecasting neural network that predicts cabin temperature across multiple zones with ±0.5°C accuracy. It enables proactive climate control adjustments and improves passenger comfort while reducing energy consumption.

## Model Architecture

**Type**: LSTM (Long Short-Term Memory) with Dense Layers  
**Input Features**: 24 (temperature sensors, flight phase, passenger load, external conditions)  
**Hidden Layers**: 3 LSTM layers (128, 64, 32 units) + 2 Dense layers (16, 8 units)  
**Output**: Temperature prediction for 6 cabin zones, 5-minute horizon  
**Framework**: TensorFlow 2.x  
**Model Size**: 2.3 MB (ONNX format)

### Architecture Diagram

```
Input (24 features) → LSTM(128) → LSTM(64) → LSTM(32) → Dense(16) → Dense(8) → Output (6 zones)
```

## Performance

- **Prediction Accuracy**: ±0.5°C (95th percentile)
- **Inference Time**: 8ms (target hardware)
- **Inference Rate**: 10 Hz
- **Energy Savings**: Contributes to 15% overall HVAC reduction

## Training

- **Dataset**: 10,000+ flight hours of cabin temperature data
- **Training Time**: 48 hours on V100 GPU
- **Validation Split**: 80/10/10 (train/val/test)
- **Loss Function**: Mean Squared Error (MSE)
- **Optimizer**: Adam (lr=0.001)

## Inputs

| Input | Source | Type | Rate | Units |
|-------|--------|------|------|-------|
| Cabin temp (zones 1-6) | ATA 21 sensors | float32 | 10 Hz | °C |
| External temp | Weather sensors | float32 | 1 Hz | °C |
| Passenger count | Cabin management | int16 | 0.1 Hz | count |
| Flight phase | FMS | enum | 0.5 Hz | - |
| HVAC power | ECS controller | float32 | 10 Hz | kW |
| Airflow rate | Vent sensors | float32 | 10 Hz | m³/min |

## Outputs

| Output | Destination | Type | Rate | Units |
|--------|-------------|------|------|-------|
| Predicted temp (zones 1-6) | HVAC Optimizer | float32 | 10 Hz | °C |
| Confidence | HVAC Optimizer | float32 | 10 Hz | 0-1 |
| Anomaly flag | System monitor | bool | 10 Hz | - |

## Safety & Certification

- **DAL Level**: C (Hazardous)
- **Failure Condition**: Temperature prediction error could lead to passenger discomfort but not safety hazard
- **Mitigation**: Fallback to sensor-based reactive control
- **V&V Status**: Complete per DO-178C Level C

## Model Card

See: `ASSETS/Model_Cards/95-20-21-A-101_Temp_Predictor_v1.2.yaml`

## Document Control

- **Version**: 1.2
- **Status**: WORKING
- **Last Updated**: 2025-11-17
- **Related Files**: 
  - Source: `Models/Source/temp_predictor_v1.2.py`
  - Trained: `Models/Trained/temp_predictor_v1.2.onnx`
  - Config: `Models/Configs/training_config_temp.yaml`
