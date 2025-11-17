# SIMULATIONS - Virtual Testing and Validation

**Purpose**: This directory contains simulation models and configurations for virtual testing of the DPP+NN system.

## Contents

### Digital_Twin/
Digital twin models for virtual aircraft representation:
- Physics-based models (aerodynamics, propulsion)
- Neural network behavior models
- Sensor simulation and synthetic data generation
- Operational scenario playback

Tools: MATLAB/Simulink, GAIA-AIR platform, custom Python simulators

### Shadow_Mode_Testing/
Shadow mode testing infrastructure:
- Parallel execution framework
- Performance comparison tools
- Validation data collection
- Ground truth labeling

Purpose: Run new models alongside production models without affecting operations

## Simulation Objectives

1. **Functional Validation**: Verify correct behavior before hardware deployment
2. **Performance Testing**: Measure latency, throughput, resource usage
3. **Safety Analysis**: Inject faults and test failure modes
4. **Regression Testing**: Ensure new models don't degrade performance
5. **Training Data Generation**: Create synthetic datasets for edge cases

## Simulation Environments

- **Desktop**: Local development and debugging
- **Cloud**: Scalable batch simulation on GPU clusters
- **Hardware-in-the-Loop (HIL)**: IMA simulator with real NPU hardware
- **Iron Bird**: Full aircraft systems integration simulator
- **Flight Test**: Shadow mode on actual aircraft

## Document Control

- **Owner**: AMPEL360 V&V WG
- **Status**: Active development
