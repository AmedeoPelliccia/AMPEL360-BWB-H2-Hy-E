# 95-20-27-009 — Safety and Certification

**Document ID:** 95-20-27-009  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active

---

## 1. Purpose

This document describes the safety assessment and certification approach for the FCS_NN subsystem, ensuring compliance with airworthiness requirements for safety-critical neural network systems.

---

## 2. Safety Classification

### 2.1 Design Assurance Level

**DAL-A (Level A)** — Catastrophic Failure Condition

- **Rationale**: Loss of FCS_NN could result in loss of aircraft control
- **Failure Condition**: Catastrophic (probability <10⁻⁹ per flight hour)
- **Development Assurance**: DO-178C Level A
- **Hardware Assurance**: DO-254 Level A

### 2.2 Failure Condition Classification

| Failure Condition | Classification | Probability Requirement |
|-------------------|----------------|-------------------------|
| Complete loss of FCS_NN | Catastrophic | <10⁻⁹ /FH |
| Degraded FCS_NN performance | Hazardous | <10⁻⁷ /FH |
| Incorrect envelope protection | Catastrophic | <10⁻⁹ /FH |
| Gust load alleviation failure | Major | <10⁻⁵ /FH |
| Trim optimization failure | Minor | <10⁻³ /FH |

---

## 3. Applicable Standards and Regulations

### 3.1 Certification Standards

| Standard | Title | Applicability |
|----------|-------|---------------|
| **CS-25 / FAR 25** | Airworthiness Standards: Transport Category | All subsystems |
| **DO-178C** | Software Considerations in Airborne Systems | Software (Level A) |
| **DO-254** | Design Assurance for Airborne Electronic Hardware | Hardware (Level A) |
| **DO-333** | Formal Methods Supplement to DO-178C | NN verification |
| **EASA SC-AI** | Special Condition on Artificial Intelligence | ML-specific requirements |
| **ARP-4754A** | Guidelines for Development of Civil Aircraft | System development |
| **ARP-4761** | Guidelines and Methods for Safety Assessment | Safety assessment |

### 3.2 Relevant CS-25 Paragraphs

| Paragraph | Title | Requirement |
|-----------|-------|-------------|
| CS 25.143 | Controllability and maneuverability | General |
| CS 25.145 | Longitudinal control | Pitch control |
| CS 25.147 | Directional and lateral control | Roll/yaw control |
| CS 25.161 | Trim | Trim in all flight conditions |
| CS 25.203 | Stall characteristics | Stall warning and protection |
| CS 25.251 | Vibration and buffeting | Load alleviation |
| CS 25.335 | Design airspeeds | Speed envelope protection |
| CS 25.1309 | Equipment, systems, and installations | Safety analysis |
| CS 25.1322 | Flightcrew alerting | Crew alerts for failures |

---

## 4. Safety Assessment Process

### 4.1 Functional Hazard Assessment (FHA)

**Objective**: Identify all failure conditions and classify their severity.

**Method**:
1. Identify all functions provided by FCS_NN
2. For each function, identify failure modes
3. Assess effect on aircraft and occupants
4. Classify severity (Catastrophic, Hazardous, Major, Minor, No Safety Effect)

**Results**: See `ASSETS/Certification/95-20-27-A-504_Safety_Analysis_FTA_FMEA.pdf`

### 4.2 Fault Tree Analysis (FTA)

**Objective**: Demonstrate that catastrophic failure conditions have probability <10⁻⁹ /FH.

**Top Event**: "Loss of Aircraft Control due to FCS_NN Failure"

**Approach**:
- Decompose top event into contributing events
- Model redundancy, monitoring, and fault detection
- Quantify probability using component failure rates
- Verify total probability <10⁻⁹ /FH

**Key Results**:
- **Probability of Loss of Control**: 2.3 × 10⁻¹⁰ /FH (meets requirement)
- **Primary Contributors**: Dual sensor failures, dual partition failures
- **Mitigation**: Fallback to conventional FCS provides additional protection

### 4.3 Failure Modes and Effects Analysis (FMEA)

**Objective**: Identify all single-point failures and their effects.

**Scope**: All hardware, software, and sensor components of FCS_NN.

**Results**:
- **Single-Point Failures Identified**: 47
- **All Mitigated**: By redundancy, monitoring, or fallback
- **Residual Risk**: All within acceptable limits

**Full FMEA**: `ASSETS/Certification/95-20-27-A-504_Safety_Analysis_FTA_FMEA.pdf`

### 4.4 Common Cause Analysis (CCA)

**Objective**: Ensure independent redundant channels are truly independent.

**Analysis**:
- **Physical Separation**: Dual IMA cores in separate locations
- **Dissimilar Sensors**: Use ADC1/ADC2 from different manufacturers
- **Software Diversity**: Conventional FCS uses different algorithms
- **Independent Testing**: NN models validated separately
- **Power Supply**: Dual power sources

**Conclusion**: No credible common cause failure identified that could compromise both NN and conventional FCS.

---

## 5. Neural Network-Specific Certification

### 5.1 EASA SC-AI Compliance

The EASA Special Condition on AI/ML addresses unique challenges of certifying learning systems:

| SC-AI Requirement | Compliance Approach |
|-------------------|---------------------|
| **Training Data Quality** | Rigorous data curation, validation, traceability |
| **Model Verification** | Formal methods (DO-333), extensive testing |
| **Model Explainability** | SHAP values, sensitivity analysis, post-hoc analysis |
| **Robustness to Inputs** | Adversarial testing, input range validation |
| **Monitoring in Operation** | Real-time performance monitoring, anomaly detection |
| **Update and Retraining** | Change control, re-certification process defined |

### 5.2 Training Data Assurance

| Aspect | Approach |
|--------|----------|
| **Data Sources** | CFD (validated), Flight Test (certified aircraft), Wind Tunnel (NASA Ames) |
| **Data Quality** | Outlier detection, cross-validation, expert review |
| **Data Coverage** | Full flight envelope, all configurations, edge cases |
| **Data Traceability** | Every data point tagged with source, date, conditions |
| **Data Versioning** | Git LFS for datasets, immutable archives |

### 5.3 Model Verification and Validation (V&V)

| V&V Activity | Method | Coverage |
|--------------|--------|----------|
| **Unit Testing** | Known inputs → expected outputs | 10,000 test cases |
| **Integration Testing** | End-to-end FCS simulation | 5,000 scenarios |
| **Robustness Testing** | Adversarial inputs, noise injection | 50,000 trials |
| **Edge Case Testing** | Envelope boundaries, failures | 1,000 edge cases |
| **Flight Test Validation** | Real aircraft, instrumented flights | 100 hours |
| **Monte Carlo Analysis** | Randomized scenarios | 100,000 runs |

**Test Evidence**: `ASSETS/Certification/95-20-27-A-503_Verification_Matrix.xlsx`

### 5.4 Formal Verification (DO-333)

For critical properties, formal methods are used:

| Property | Verification Method | Tool |
|----------|---------------------|------|
| **Input Range Bounds** | Interval arithmetic | ACAS Xu Toolkit |
| **Lipschitz Continuity** | Gradient analysis | Custom |
| **Monotonicity** | Symbolic execution | Marabou |
| **Safety Constraints** | Constraint solving | Z3 SMT Solver |

**Results**: All critical properties formally verified for the Envelope Protection NN.

---

## 6. Redundancy and Fault Tolerance

### 6.1 Redundancy Architecture

```
┌────────────────────────────────────────────────┐
│        Pilot Commands / Autopilot              │
└────────────────┬───────────────────────────────┘
                 │
        ┌────────▼────────┐
        │  FCS_NN Channel A │
        └────────┬─────────┘
                 │
        ┌────────▼─────────┐
        │  FCS_NN Channel B │
        └────────┬──────────┘
                 │
        ┌────────▼──────────────┐
        │   Voting Logic        │
        │   (2-out-of-2)        │
        └────────┬──────────────┘
                 │
    ┌────────────▼────────────────┐
    │ Agreement?                  │
    │ YES: Use NN Output          │
    │ NO:  Fallback to Conv. FCS  │
    └────────────┬────────────────┘
                 │
    ┌────────────▼─────────────────┐
    │  ATA 27 Flight Control       │
    │  Computer (Triplex)          │
    └──────────────────────────────┘
```

### 6.2 Monitoring and Health Management

**Continuous Monitoring**:
- **Inference Latency**: Every cycle, alarm if >10ms
- **Output Reasonableness**: Range checks, rate limits
- **Cross-Channel Comparison**: Channels A/B must agree within 5%
- **Sensor Validity**: BIT checks on all inputs
- **Model Integrity**: Periodic CRC on model weights

**Health Score**:
Each NN model has a real-time health score (0-100%):
- **100%**: Nominal performance
- **80-99%**: Minor degradation, continue with caution
- **50-79%**: Significant degradation, crew alerted
- **<50%**: Failed, switch to fallback

### 6.3 Graceful Degradation

| Degradation Level | NN State | Conventional FCS State | Aircraft Impact |
|-------------------|----------|------------------------|-----------------|
| **Level 0** (Normal) | 100% active | Standby | Full performance |
| **Level 1** (Minor) | Optimization reduced | Monitor | -2% efficiency |
| **Level 2** (Major) | Envelope protection only | Active monitoring | -5% efficiency, reduced margins |
| **Level 3** (Critical) | NN disabled | Full control | -10% efficiency, conventional handling |
| **Level 4** (Emergency) | NN disabled | Full control + alerts | Conventional handling, land ASAP |

---

## 7. Testing and Validation

### 7.1 Development Testing

| Test Phase | Duration | Environment | Objectives |
|------------|----------|-------------|------------|
| **Model-in-the-Loop** | 10,000 hrs | MATLAB/Simulink | Algorithm validation |
| **Software-in-the-Loop** | 5,000 hrs | C++ on dev PC | Code validation |
| **Processor-in-the-Loop** | 2,000 hrs | IMA target HW | Timing validation |
| **Hardware-in-the-Loop** | 500 hrs | Iron Bird | Integration validation |

### 7.2 Certification Testing

| Test Type | Scenarios | Requirements Coverage |
|-----------|-----------|----------------------|
| **Functional Tests** | 1,000 | 100% requirements traced |
| **Failure Mode Tests** | 500 | All identified failures |
| **Environmental Tests** | 200 | Temp, vibration, EMI |
| **Limit Testing** | 100 | Envelope boundaries |

**Test Results**: `ASSETS/Test_Data/95-20-27-A-301_Ground_Rig_Test_Results.csv`

### 7.3 Flight Testing

| Phase | Flights | Hours | Objectives |
|-------|---------|-------|------------|
| **Phase 1** (Initial) | 20 | 50 | Basic functionality, safety checks |
| **Phase 2** (Envelope) | 30 | 100 | Full envelope exploration |
| **Phase 3** (Edge Cases) | 20 | 50 | Deliberate failures, edge cases |
| **Phase 4** (Validation) | 50 | 200 | Production representative testing |

**Flight Test Results**: `ASSETS/Test_Data/95-20-27-A-302_Flight_Test_Results.csv`

---

## 8. Operational Safety

### 8.1 Crew Training

**Training Modules**:
1. **FCS_NN Overview**: System capabilities and limitations
2. **Normal Operations**: How to use FCS_NN effectively
3. **Abnormal Procedures**: Responding to FCS_NN failures
4. **Emergency Procedures**: Manual reversion, direct law

**Training Materials**: `Documentation/Training_Materials/`

### 8.2 Operational Limitations

| Limitation | Rationale |
|------------|-----------|
| **Minimum Crew**: 2 pilots | Monitor NN performance |
| **Icing Conditions**: Reduced envelope margins | Degraded aerodynamics |
| **Turbulence**: GLA automatic, manual disable available | Crew may prefer conventional handling |
| **Low Visibility**: Autoland available, tested to CAT IIIb | Precision approach |

### 8.3 Maintenance Requirements

| Maintenance Action | Interval | Objective |
|--------------------|----------|-----------|
| **BIT Execution** | Pre-flight | Confirm system health |
| **Event Log Download** | Weekly | Trending, early failure detection |
| **Performance Trending** | Monthly | Detect gradual degradation |
| **Model Validation** | Annual | Confirm performance within limits |
| **Software Update** | As needed | Security patches, improvements |

**Maintenance Procedures**: `Documentation/95-20-27-802_FCS_NN_Maintenance_Procedures.md`

---

## 9. Continued Airworthiness

### 9.1 In-Service Monitoring

**Data Collection**:
- **Flight Data Recorder**: All FCS_NN inputs/outputs logged
- **Quick Access Recorder**: Key parameters for trending
- **ACMS Reports**: Automatic downloads to ground systems
- **Pilot Reports**: Crew feedback on NN performance

**Analysis**:
- **Performance Trending**: Detect gradual degradation
- **Anomaly Detection**: Identify unexpected behaviors
- **Fleet-Wide Comparison**: Compare aircraft-to-aircraft
- **Model Drift Detection**: Compare predictions to outcomes

### 9.2 Model Update Process

If model updates are required (e.g., for improved performance):

1. **Change Request**: Document reason for update
2. **Safety Assessment**: Impact on safety analysis
3. **Re-Verification**: Regression testing, new test cases
4. **Certification Authority Review**: EASA/FAA approval
5. **Service Bulletin**: Fleet-wide update procedure
6. **Validation**: Post-update flight test

**NOTE**: Any model update requires re-certification.

---

## 10. Certification Deliverables

### 10.1 Required Documents

| Document | Description | Location |
|----------|-------------|----------|
| **Plan for Software Aspects of Certification (PSAC)** | Overall certification approach | `ASSETS/Certification/` |
| **Software Requirements Standards** | How requirements are written | `ASSETS/Certification/` |
| **Software Design Standards** | Design rules and guidelines | `ASSETS/Certification/` |
| **Software Code Standards** | Coding standards (MISRA C++) | `ASSETS/Certification/` |
| **Software Verification Plan** | Test strategy and coverage | `ASSETS/Certification/` |
| **Software Verification Results** | Test reports, traceability matrix | `ASSETS/Certification/95-20-27-A-503_Verification_Matrix.xlsx` |
| **Software Configuration Management Plan** | Version control, change management | `ASSETS/Certification/` |
| **Software Quality Assurance Plan** | QA activities and records | `ASSETS/Certification/` |
| **Software Accomplishment Summary (SAS)** | Evidence of DO-178C compliance | `ASSETS/Certification/95-20-27-A-501_DO_178C_Evidence_Package.pdf` |

### 10.2 Safety Evidence Package

- **Functional Hazard Assessment**: `ASSETS/Certification/95-20-27-A-504_Safety_Analysis_FTA_FMEA.pdf`
- **Fault Tree Analysis**: `ASSETS/Certification/95-20-27-A-504_Safety_Analysis_FTA_FMEA.pdf`
- **FMEA**: `ASSETS/Certification/95-20-27-A-504_Safety_Analysis_FTA_FMEA.pdf`
- **Common Cause Analysis**: `ASSETS/Certification/95-20-27-A-504_Safety_Analysis_FTA_FMEA.pdf`
- **Verification Matrix**: `ASSETS/Certification/95-20-27-A-503_Verification_Matrix.xlsx`
- **EASA AI Compliance Report**: `ASSETS/Certification/95-20-27-A-502_EASA_AI_Compliance_Report.pdf`

---

## 11. Compliance Matrix

Full compliance matrix available in: `ASSETS/Certification/95-20-27-A-503_Verification_Matrix.xlsx`

Sample entries:

| Requirement ID | Requirement Text | Verification Method | Test Case(s) | Status |
|----------------|------------------|---------------------|--------------|--------|
| FR-FCS-001 | Aero prediction <10ms latency | Analysis + Test | TC-001, TC-002 | PASS |
| FR-FCS-003 | Gust load reduction ≥30% | Flight Test | TC-150, TC-151 | PASS |
| FR-FCS-004 | 100% envelope protection | Analysis + Test | TC-200-TC-250 | PASS |
| NFR-FCS-003 | Failover <10ms | HIL Test | TC-300 | PASS |

---

## 12. References

- [95-20-27-001_FCS_NN_Overview.md](95-20-27-001_FCS_NN_Overview.md)
- DO-178C: Software Considerations in Airborne Systems
- DO-254: Design Assurance for Airborne Electronic Hardware
- DO-333: Formal Methods Supplement to DO-178C
- ARP-4754A: Guidelines for Development of Civil Aircraft
- ARP-4761: Guidelines and Methods for Safety Assessment
- EASA Special Condition SC-AI: Artificial Intelligence
- CS-25 / FAR 25: Airworthiness Standards

---

## Document Control

- **Owner**: AMPEL360 FCS_NN Safety Team
- **Version**: 1.0
- **Status**: Active
- **Classification**: Certification Evidence
- **Last Updated**: 2025-11-17
