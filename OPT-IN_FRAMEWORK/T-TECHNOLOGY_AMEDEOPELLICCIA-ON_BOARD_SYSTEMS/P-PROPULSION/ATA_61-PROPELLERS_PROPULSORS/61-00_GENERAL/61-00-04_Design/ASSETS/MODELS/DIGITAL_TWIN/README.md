# DIGITAL_TWIN Models

**Purpose**: Digital twin frameworks for real-time propulsor monitoring, health assessment, predictive maintenance, and model calibration.

---

## Overview

This directory contains digital twin models supporting:

- Real-time sensor data fusion
- Physics-based anomaly detection
- Remaining useful life (RUL) estimation
- Online model calibration and updating
- Predictive maintenance scheduling

---

## Models

### Q100-61-MDL-DT-PROPULSOR

Comprehensive propulsor digital twin:

| Subdirectory | Contents |
|--------------|----------|
| `sensor_mapping/` | Sensor locations and signal definitions |
| `data_interfaces/` | Data bus protocols and message formats |
| `physics_models/` | Reduced-order physics models |
| `health_monitoring/` | Degradation and anomaly detection |
| `calibration/` | Model tuning and validation procedures |

**Capabilities**:

- Real-time thrust and efficiency estimation
- Blade health monitoring (tip clearance, damage detection)
- Bearing wear tracking
- Thermal state estimation

### Q100-61-MDL-DT-MOTOR

Electric motor digital twin:

| Subdirectory | Contents |
|--------------|----------|
| `sensor_mapping/` | Motor-specific sensors |
| `health_monitoring/` | Insulation, bearing, magnet health |

**Capabilities**:

- Winding temperature estimation
- Insulation degradation tracking
- Bearing vibration monitoring
- Magnet flux monitoring

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    PHYSICAL PROPULSOR                        │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │ Sensors │  │ Sensors │  │ Sensors │  │ Sensors │        │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘        │
└───────┼────────────┼────────────┼────────────┼──────────────┘
        │            │            │            │
        └────────────┴────────────┴────────────┘
                          │
                    ┌─────▼─────┐
                    │ Data Bus  │ (ARINC 429/664, CAN)
                    └─────┬─────┘
                          │
        ┌─────────────────┼─────────────────┐
        │           DIGITAL TWIN            │
        │  ┌──────────────────────────────┐ │
        │  │    Data Acquisition Layer    │ │
        │  └──────────────┬───────────────┘ │
        │  ┌──────────────▼───────────────┐ │
        │  │   Physics Model Layer        │ │
        │  │  (Reduced-order models)      │ │
        │  └──────────────┬───────────────┘ │
        │  ┌──────────────▼───────────────┐ │
        │  │   Health Monitoring Layer    │ │
        │  │  (Anomaly, RUL, Prognosis)   │ │
        │  └──────────────┬───────────────┘ │
        │  ┌──────────────▼───────────────┐ │
        │  │   Decision Support Layer     │ │
        │  │  (Alerts, Recommendations)   │ │
        │  └──────────────────────────────┘ │
        └───────────────────────────────────┘
```

---

## Sensor Types

| Category | Sensors | Parameters |
|----------|---------|------------|
| **Mechanical** | Vibration, speed, position | Bearing health, imbalance, shaft speed |
| **Thermal** | Thermocouples, RTDs | Winding, bearing, coolant temperatures |
| **Electrical** | Current, voltage, power | Motor performance, insulation health |
| **Aerodynamic** | Pressure, flow | Thrust estimation, stall detection |
| **Structural** | Strain gauges, tip timing | Blade stress, tip clearance |

---

## Health Monitoring Algorithms

### Anomaly Detection

- **Residual Analysis**: Compare measured vs. predicted values
- **Statistical Process Control**: Control charts, CUSUM
- **Machine Learning**: Autoencoders, isolation forests

### Remaining Useful Life (RUL)

- **Physics-Based**: Degradation models with Bayesian updating
- **Data-Driven**: Recurrent neural networks, survival analysis
- **Hybrid**: Physics-informed machine learning

### Fault Diagnostics

- **Feature Extraction**: Frequency domain analysis, order tracking
- **Classification**: Support vector machines, random forests
- **Root Cause Analysis**: Fault signature matching

---

## Calibration Procedures

1. **Initial Calibration**: Factory test data → model parameters
2. **In-Service Calibration**: Flight data → model refinement
3. **Event-Based Update**: After maintenance → reset baselines
4. **Continuous Learning**: Streaming data → adaptive models

---

## Integration with Physical Systems

| Interface | Standard | Data Rate |
|-----------|----------|-----------|
| Flight Data | ARINC 429/664 | 12.5-100 kbps |
| Maintenance | AIDMS, MSG-3 | Event-based |
| Ground System | ACARS, Wi-Fi | Post-flight |
| Cloud Platform | MQTT, REST | Continuous |

---

## Traceability

- Requirements: See `61-00-03_Requirements/`
- Health Sensing: See `61-20-06_Health_Sensing/`
- Maintenance: See `61-00-12_Services/`
- Certification: CS-25.1309, ARP4761

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-05
