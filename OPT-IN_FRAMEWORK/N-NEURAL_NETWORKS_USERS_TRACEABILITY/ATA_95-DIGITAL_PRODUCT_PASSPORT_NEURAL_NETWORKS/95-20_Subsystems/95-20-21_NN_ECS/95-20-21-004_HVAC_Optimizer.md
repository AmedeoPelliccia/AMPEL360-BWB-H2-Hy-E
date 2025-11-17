# 95-20-21-004 — HVAC Optimizer

**Component ID**: 95-20-21-004  
**Model Version**: v2.1  
**Parent**: 95-20-21 ECS Neural Networks  
**Status**: WORKING

## Overview

The HVAC Optimizer is a deep reinforcement learning agent that dynamically adjusts heating, ventilation, and air conditioning parameters to maintain passenger comfort while minimizing energy consumption. It achieves a 15% reduction in HVAC energy usage compared to baseline control strategies.

## Model Architecture

**Type**: Deep Reinforcement Learning - Proximal Policy Optimization (PPO)  
**State Space**: 32 dimensions (temps, flows, power, comfort metrics)  
**Action Space**: 12 continuous actions (fan speeds, valve positions, compressor power)  
**Network**:
- Actor: MLP (256 → 128 → 64 → 12)
- Critic: MLP (256 → 128 → 64 → 1)

**Framework**: PyTorch + Stable-Baselines3  
**Model Size**: 3.1 MB (ONNX format)

### Architecture Diagram

```
State (32-dim) → Actor Network → Actions (12-dim) → HVAC Actuators
               ↘ Critic Network → Value Estimate
```

## Performance

- **Energy Reduction**: 15% vs. baseline PID control
- **Comfort Maintenance**: 99.2% within target ranges
- **Inference Time**: 12ms
- **Inference Rate**: 1 Hz
- **Convergence**: 5M training steps

## Training

- **Environment**: Custom OpenAI Gym environment with ECS dynamics
- **Training Time**: 72 hours on 8× A100 GPUs
- **Reward Function**: `R = -energy_cost + 10*comfort_score - 50*violation_penalty`
- **Hyperparameters**:
  - Learning rate: 3e-4
  - Clip range: 0.2
  - Batch size: 2048
  - n_epochs: 10

## Inputs

| Input | Source | Type | Rate | Units |
|-------|--------|------|------|-------|
| Current temps (zones 1-6) | Temp sensors | float32 | 1 Hz | °C |
| Target temps (zones 1-6) | Passenger input | float32 | 0.1 Hz | °C |
| Predicted temps | Temp Predictor | float32 | 1 Hz | °C |
| Air quality index | AQ Monitor | enum | 1 Hz | 1-5 |
| External conditions | Weather | float32 | 0.1 Hz | various |
| Power budget | Energy mgmt | float32 | 1 Hz | kW |

## Outputs

| Output | Destination | Type | Rate | Units |
|--------|-------------|------|------|-------|
| Fan speeds (zones 1-6) | HVAC actuators | float32 | 1 Hz | % |
| Heating valve positions | Heating valves | float32 | 1 Hz | 0-1 |
| Cooling valve positions | Cooling valves | float32 | 1 Hz | 0-1 |
| Compressor power | Compressor ctrl | float32 | 1 Hz | % |
| Fresh air damper | Ventilation | float32 | 1 Hz | 0-1 |

## Reward Structure

- **Comfort Score**: Weighted average of temperature accuracy, humidity in range, air quality
- **Energy Cost**: Power consumption normalized by flight phase
- **Violation Penalty**: Large penalty for exceeding safe operating limits

## Safety & Certification

- **DAL Level**: C (Hazardous)
- **Failure Condition**: Inefficient control or comfort degradation
- **Mitigation**: Safe action space limits + classical control fallback
- **Operational Limits**: Hard-coded constraints on all outputs
- **V&V Status**: Complete per DO-178C Level C

## Model Card

See: `ASSETS/Model_Cards/95-20-21-A-103_HVAC_Optimizer_v2.1.yaml`

## Document Control

- **Version**: 2.1
- **Status**: WORKING
- **Last Updated**: 2025-11-17
- **Related Files**: 
  - Source: `Models/Source/hvac_optimizer_v2.1.py`
  - Trained: `Models/Trained/hvac_optimizer_v2.1.onnx`
  - Config: `Models/Configs/deployment_config.yaml`
