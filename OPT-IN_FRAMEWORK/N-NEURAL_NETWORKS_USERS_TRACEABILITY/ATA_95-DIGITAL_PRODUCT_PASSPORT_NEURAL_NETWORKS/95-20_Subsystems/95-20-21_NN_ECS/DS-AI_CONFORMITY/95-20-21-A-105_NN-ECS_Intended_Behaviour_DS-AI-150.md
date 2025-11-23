# 95-20-21-A-105 — NN-ECS Intended Behaviour (DS-AI-150)

**Document ID**: 95-20-21-A-105  
**Version**: 0.1  
**Status**: DRAFT  
**DS.AI Section**: DS-AI.150

## 1. Objective

Define the intended behaviour of each NN component in the ECS subsystem in accordance with DS.AI.150 requirements.

## 2. Cabin Temperature Predictor - Intended Behaviour

### 2.1 Primary Function
Predict cabin temperature 5-15 minutes ahead based on current conditions, external environment, passenger load, and HVAC settings.

### 2.2 Inputs
- Current cabin temperature (°C)
- External ambient temperature (°C)
- Passenger load (% occupancy)
- Current HVAC power setting (%)
- Altitude (m)
- Vertical speed (ft/min)
- Time of day
- Flight phase

### 2.3 Outputs
- Predicted cabin temperature at t+5min, t+10min, t+15min (°C)
- Prediction confidence bounds (±°C)

### 2.4 Performance Requirements
- **Accuracy**: ±0.5°C (95% confidence interval)
- **Update Rate**: 10 Hz
- **Latency**: <100ms
- **Availability**: >99.9%

### 2.5 Boundary Conditions
- Input validation: Reject inputs outside sensor ranges
- ODD compliance: Flag predictions when inputs are outside trained domain
- Graceful degradation: Provide last valid prediction with increasing uncertainty bounds

## 3. Air Quality Monitor - Intended Behaviour

### 3.1 Primary Function
Fuse multi-sensor data to provide comprehensive air quality assessment and detect anomalies.

### 3.2 Inputs
- CO₂ concentration (ppm)
- Humidity (%RH)
- VOC levels (ppb)
- Particulate matter PM2.5 (μg/m³)
- Temperature (°C)
- Pressure (hPa)

### 3.3 Outputs
- Air Quality Index (0-100 scale)
- Individual contaminant levels
- Anomaly alerts (boolean flags)
- Trend predictions

### 3.4 Performance Requirements
- **Detection Accuracy**: >95% for known contaminants
- **False Positive Rate**: <5%
- **Update Rate**: 5 Hz
- **Latency**: <200ms

## 4. HVAC Optimizer - Intended Behaviour

### 4.1 Primary Function
Optimize HVAC control settings to minimize energy consumption while maintaining passenger comfort within specified bounds.

### 4.2 Inputs
- Current environmental conditions (temp, humidity, CO₂, etc.)
- Temperature predictions (from Cabin Temp Predictor)
- Air quality status (from Air Quality Monitor)
- Comfort bounds (temperature and humidity ranges)
- Energy cost function
- Current power availability

### 4.3 Outputs
- Optimal HVAC power settings (%)
- Predicted energy consumption (kW)
- Estimated comfort level (0-100 scale)
- Optimization confidence

### 4.4 Performance Requirements
- **Energy Reduction**: 15% target vs. baseline control
- **Comfort Maintenance**: 95% of time within comfort bounds
- **Update Rate**: 1 Hz
- **Optimization Horizon**: 15 minutes

### 4.5 Constraints
- Temperature must remain within 18-26°C
- Humidity must remain within 40-60% RH
- CO₂ must remain below 1000 ppm
- Minimum fresh air exchange rate must be maintained

## 5. Pressure Control NN - Intended Behaviour

TBD - To be completed with detailed specifications

## 6. Humidity Management - Intended Behaviour

TBD - To be completed with detailed specifications

## 7. CO₂ Scrubbing Optimizer - Intended Behaviour

TBD - To be completed with detailed specifications

## 8. Unintended Behaviour and Limitations

### 8.1 Known Limitations
- **Out-of-ODD Performance**: Degraded accuracy outside trained parameter ranges
- **Sensor Failures**: Requires fallback to traditional control when sensor data is unavailable
- **Extreme Scenarios**: May not optimize effectively in extreme environmental conditions
- **Rapid Transients**: Prediction accuracy degrades during rapid cabin condition changes

### 8.2 Prohibited Uses
- **Safety-Critical Control**: NN outputs are advisory; final control authority rests with certified control laws
- **Medical Applications**: Not designed for medical air quality requirements
- **Standalone Operation**: Requires human oversight and monitoring

### 8.3 Failure Modes
- **Prediction Failure**: Revert to last valid prediction with degrading confidence
- **Sensor Failure**: Switch to sensor fusion from remaining sensors
- **Complete NN Failure**: Revert to traditional ECS control laws

## 9. Verification Approach

### 9.1 Requirements-Based Testing
- Test each specified behaviour against requirements
- Boundary condition testing for all input parameters
- Performance validation across operational envelope

### 9.2 ML-Specific Verification
- Out-of-distribution detection validation
- Adversarial robustness testing
- Uncertainty quantification validation
- Model interpretability assessment

### 9.3 System Integration Testing
- End-to-end system testing with all NN components
- Hardware-in-the-loop (HIL) testing
- Iron bird testing
- Flight test validation

## 10. Traceability

- **Parent Document**: [95-20-21-001_ECS_NN_Overview.md](../95-20-21-001_ECS_NN_Overview.md)
- **OD/ODD**: [95-20-21-A-102_NN-ECS_Operational_Domain_ODD_DS-AI-120.md](./95-20-21-A-102_NN-ECS_Operational_Domain_ODD_DS-AI-120.md)
- **Learning Assurance**: [95-20-21-A-106_NN-ECS_Learning_Assurance_DS-AI-150.md](./95-20-21-A-106_NN-ECS_Learning_Assurance_DS-AI-150.md)
- **Requirements**: REQ-95-20-21-XXX (TBD)
- **Test Cases**: To be linked from [10_CERTIFICATION/ASSETS/Reports/](../10_CERTIFICATION/ASSETS/Reports/)
- **Related Standards**: DS.AI.150, DO-178C

## 11. Open Issues

- [ ] Complete specifications for Pressure Control NN
- [ ] Complete specifications for Humidity Management
- [ ] Complete specifications for CO₂ Scrubbing Optimizer
- [ ] Define detailed failure modes and recovery procedures
- [ ] Validate performance requirements through testing
- [ ] Document model interpretability approaches

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval by ECS Domain Lead and V&V Engineer.
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-23

---
