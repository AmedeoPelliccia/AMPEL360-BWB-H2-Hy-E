# 95-20-21-A-102 — NN-ECS Operational Domain & ODD (DS-AI-120)

**Document ID**: 95-20-21-A-102  
**Version**: 0.1  
**Status**: DRAFT  
**DS.AI Section**: DS-AI.120

## 1. Objective

Define the Operational Domain (OD) of the ECS system and the Operational Design Domain (ODD) of the AI constituents in accordance with DS.AI.120 requirements.

## 2. System Operational Domain (OD)

### 2.1 Aircraft Domain
- **Aircraft Type**: AMPEL360 BWB H₂ Hy-E
- **Variants**: Q80, Q100, Q120
- **Certification Basis**: CS-25 (Large Aeroplanes)
- **Service Entry**: TBD

### 2.2 Environmental Domain
- **Altitude Range**: Ground level to FL450
- **Temperature Range**: ISA -40°C to ISA +35°C
- **Pressure Range**: Sea level to maximum certified altitude
- **Humidity Range**: 0% to 95% RH (external)

### 2.3 Operational Domain
- **Flight Phases**: All phases (ground through landing)
- **Day/Night**: All conditions
- **Weather**: All weather conditions (VMC and IMC)
- **Geographic**: Worldwide operations

## 3. AI Constituent Operational Design Domain (ODD)

### 3.1 Cabin Temperature Predictor ODD

#### Input Parameter Ranges
| Parameter | Minimum | Maximum | Units | Notes |
|-----------|---------|---------|-------|-------|
| Current cabin temp | 15.0 | 30.0 | °C | Training data range |
| External temp | -60.0 | 50.0 | °C | ISA envelope |
| Passenger load | 0 | 100 | % | Occupancy |
| HVAC power setting | 0 | 100 | % | Control input |
| Altitude | 0 | 14000 | m | FL0-FL450 |
| Climb/descent rate | -1500 | 1500 | ft/min | Vertical speed |

#### Operational Conditions
- **Training Data**: 10,000 flight hours across Q100 operations
- **Validation Data**: 2,000 flight hours from flight test program
- **Out-of-Distribution Detection**: TBD

### 3.2 Air Quality Monitor ODD

#### Sensor Inputs
| Sensor | Range | Resolution | Accuracy |
|--------|-------|------------|----------|
| CO₂ | 300-5000 ppm | 1 ppm | ±50 ppm |
| Humidity | 0-100% RH | 0.1% | ±2% |
| VOC | 0-500 ppb | 1 ppb | ±10% |
| Particulates (PM2.5) | 0-500 μg/m³ | 1 μg/m³ | ±10% |
| Temperature | -40 to +85 °C | 0.1°C | ±0.5°C |

#### Operational Conditions
TBD - To be completed with validated sensor ranges

### 3.3 HVAC Optimizer ODD

#### Control Parameters
- **Optimization Objective**: Minimize energy while maintaining comfort
- **Constraints**: Temperature bounds, humidity bounds, air quality thresholds
- **Update Rate**: 1 Hz
- **Prediction Horizon**: 15 minutes

#### Training Environment
TBD - To be completed with training environment specification

### 3.4 Pressure Control NN ODD

TBD - To be completed

### 3.5 Humidity Management ODD

TBD - To be completed

### 3.6 CO₂ Scrubbing Optimizer ODD

TBD - To be completed

## 4. ODD Boundary Conditions

### 4.1 Normal Operating Conditions
TBD - Define nominal operating envelope

### 4.2 Edge Cases
TBD - Define boundary conditions requiring special handling

### 4.3 Out-of-ODD Detection
TBD - Define methods for detecting operation outside trained domain

## 5. ODD Validation

### 5.1 Coverage Analysis
TBD - Demonstrate training data covers operational domain

### 5.2 Gap Analysis
TBD - Identify any gaps between OD and ODD

### 5.3 Mitigation for Gaps
TBD - Define approach for handling OD-ODD gaps

## 6. Traceability

- **Parent Document**: [95-20-21-001_ECS_NN_Overview.md](../95-20-21-001_ECS_NN_Overview.md)
- **ConOps**: [95-20-21-A-101_NN-ECS_ConOps_DS-AI-100.md](./95-20-21-A-101_NN-ECS_ConOps_DS-AI-100.md)
- **Related Dataset Cards**: To be created in [ASSETS/DATASETS/](../ASSETS/DATASETS/)
- **Related Standards**: DS.AI.120, ATA 21

## 7. Open Issues

- [ ] Complete ODD specifications for all six NN components
- [ ] Validate input parameter ranges against actual sensor specifications
- [ ] Define out-of-ODD detection mechanisms
- [ ] Complete ODD coverage analysis
- [ ] Identify and document OD-ODD gaps

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval by ECS Domain Lead and Certification Manager.
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-23

---
