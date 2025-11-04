# Fault Tree Analysis for Neural Network Systems

**Document ID:** AMPEL360-95-00-00-SAF-FTA  
**Version:** 1.0  
**Date:** 2025-11-04  
**Classification:** Safety Critical

---

## 1. INTRODUCTION

### 1.1 Purpose

This document presents fault tree analyses for critical neural network failure scenarios in the AMPEL360 aircraft. Fault trees identify combinations of events that lead to unacceptable system states.

### 1.2 Scope

Covers top-level safety events for DAL A and B neural network systems.

### 1.3 Related Documents

- [Hazard_Analysis_Methodology.md](Hazard_Analysis_Methodology.md)
- [Functional_Hazard_Assessment.csv](Functional_Hazard_Assessment.csv)
- [Failure_Modes_Effects_Analysis.csv](Failure_Modes_Effects_Analysis.csv)
- [Common_Cause_Analysis.md](Common_Cause_Analysis.md)
- [Safety_Requirements.csv](Safety_Requirements.csv)
- [ARP4761](https://www.sae.org/standards/content/arp4761/) - Fault Tree Analysis Guidelines
- [ASSETS/FTA_Templates/](ASSETS/FTA_Templates/) - Fault Tree Templates

---

## 2. TOP EVENT 1: UNSAFE FLIGHT CONTROL COMMAND FROM NN

### 2.1 Fault Tree Structure

```
TOP: Unsafe Flight Control Command Results in Aircraft Upset
│
├─ AND Gate: NN Issues Unsafe Command AND Safety Barriers Fail
   │
   ├─ OR Gate: NN Issues Unsafe Command
   │  │
   │  ├─ NN receives OOD input AND OOD not detected
   │  │  ├─ Basic: Novel flight condition (P=10⁻⁴/FH)
   │  │  └─ Basic: OOD detector fails (P=10⁻²)
   │  │
   │  ├─ NN model degraded AND not detected
   │  │  ├─ Basic: Concept drift (P=10⁻³/FH)
   │  │  └─ Basic: Performance monitor fails (P=10⁻²)
   │  │
   │  ├─ GPU hardware fault AND not detected
   │  │  ├─ Basic: GPU computation error (P=10⁻⁵/FH)
   │  │  └─ Basic: BIT fails to detect (P=10⁻²)
   │  │
   │  ├─ Adversarial attack successful
   │  │  ├─ Basic: Malicious input crafted (P=10⁻⁶/FH)
   │  │  └─ Basic: Attack detector bypassed (P=10⁻¹)
   │  │
   │  └─ Training data bias manifests
   │     ├─ Basic: Rare scenario from biased training (P=10⁻⁴/FH)
   │     └─ Basic: Bias not caught in testing (P=10⁻²)
   │
   └─ AND Gate: Safety Barriers All Fail
      │
      ├─ Independent Safety Monitor Fails
      │  ├─ Basic: Monitor hardware fault (P=10⁻⁵/FH)
      │  └─ Basic: Monitor software fault (P=10⁻⁶/FH)
      │
      ├─ Crew Does Not Intervene
      │  ├─ Basic: Crew does not detect (P=10⁻¹)
      │  └─ Basic: Insufficient time to react (P=10⁻¹)
      │
      └─ Automatic Fallback Does Not Engage
         ├─ Basic: Fallback logic failure (P=10⁻⁶/FH)
         └─ Basic: Common cause with NN (P=10⁻⁴)
```

### 2.2 Quantitative Analysis

**Calculate Probability of Top Event**:

P(NN Unsafe Command) ≈ Sum of OR branches:
- OOD: 10⁻⁴ × 10⁻² = 10⁻⁶/FH
- Degradation: 10⁻³ × 10⁻² = 10⁻⁵/FH
- GPU fault: 10⁻⁵ × 10⁻² = 10⁻⁷/FH
- Adversarial: 10⁻⁶ × 10⁻¹ = 10⁻⁷/FH
- Bias: 10⁻⁴ × 10⁻² = 10⁻⁶/FH
- **Total: ≈ 1.2 × 10⁻⁵/FH**

P(All Barriers Fail) = P(Monitor Fails) × P(Crew No Intervene) × P(Fallback Fails)
- Monitor: 10⁻⁵ + 10⁻⁶ ≈ 1.1 × 10⁻⁵/FH
- Crew: 10⁻¹ × 10⁻¹ = 10⁻²
- Fallback: 10⁻⁶ + 10⁻⁴ ≈ 10⁻⁴
- **Total: 1.1 × 10⁻⁵ × 10⁻² × 10⁻⁴ = 1.1 × 10⁻¹¹/FH**

**P(Top Event) = 1.2 × 10⁻⁵ × 1.1 × 10⁻¹¹ = 1.32 × 10⁻¹⁶/FH**

**Result**: Meets catastrophic requirement (<10⁻⁹/FH) with large margin ✓

### 2.3 Sensitivity Analysis

**Most Critical Paths**:
1. Model degradation (10⁻⁵/FH contribution)
2. OOD inputs (10⁻⁶/FH contribution)

**Recommendations**:
- Enhance performance monitoring (reduce 10⁻² to 10⁻³)
- Improve OOD detection (reduce 10⁻² to 10⁻³)
- Both would reduce top path contributions by 10×

---

## 3. TOP EVENT 2: MISSED COLLISION THREAT

### 3.1 Fault Tree Structure

```
TOP: Collision Occurs Due to Missed Detection
│
├─ AND Gate: Threat Exists AND All Detection Systems Fail
   │
   ├─ Basic: Collision threat present (P=10⁻³/FH)
   │
   └─ AND Gate: All Detection Channels Fail
      │
      ├─ Vision NN fails to detect
      │  ├─ OR Gate:
      │     ├─ Poor visibility (P=10⁻²/FH)
      │     ├─ OOD traffic type (P=10⁻⁴/FH)
      │     ├─ NN model error (P=10⁻³/FH)
      │     └─ Camera failure (P=10⁻⁵/FH)
      │
      ├─ Radar fails to detect
      │  ├─ Basic: Radar clutter (P=10⁻²/FH)
      │  ├─ Basic: Small RCS target (P=10⁻³/FH)
      │  └─ Basic: Radar hardware fault (P=10⁻⁵/FH)
      │
      ├─ ADS-B fails (no transponder)
      │  └─ Basic: Traffic not equipped (P=10⁻¹/FH)
      │
      ├─ TCAS fails
      │  ├─ Basic: Below TCAS altitude (P=10⁻²/FH)
      │  └─ Basic: TCAS hardware fault (P=10⁻⁵/FH)
      │
      └─ Crew does not see traffic
         ├─ Basic: Traffic not visible (P=10⁻¹)
         └─ Basic: Crew task saturated (P=10⁻¹)
```

### 3.2 Quantitative Analysis

P(Vision NN Fails) ≈ 10⁻² + 10⁻⁴ + 10⁻³ + 10⁻⁵ ≈ 1.1 × 10⁻²/FH

P(All Channels Fail):
- Vision: 1.1 × 10⁻²
- Radar: 10⁻² + 10⁻³ + 10⁻⁵ ≈ 1.1 × 10⁻²
- ADS-B: 10⁻¹
- TCAS: 10⁻² + 10⁻⁵ ≈ 10⁻²
- Crew: 10⁻¹ × 10⁻¹ = 10⁻²

**P(All Fail) = 1.1×10⁻² × 1.1×10⁻² × 10⁻¹ × 10⁻² × 10⁻² = 1.21 × 10⁻⁸**

P(Top Event) = P(Threat) × P(All Fail) = 10⁻³ × 1.21 × 10⁻⁸ = 1.21 × 10⁻¹¹/FH

**Result**: Meets hazardous requirement (<10⁻⁷/FH) ✓

### 3.3 Critical Path Analysis

**Independence Verification**:
- Vision NN and Radar use different physics → Independent ✓
- ADS-B requires transponder → Independent ✓
- TCAS different frequency → Independent ✓
- Crew visual → Independent ✓

**Common Causes to Verify**:
- Weather (affects vision and crew visual) → Radar/ADS-B/TCAS still work
- Electrical failure → Redundant power buses required
- Software bug → Diverse implementations

---

## 4. TOP EVENT 3: FUEL CELL DAMAGE DUE TO NN OPTIMIZATION

### 4.1 Fault Tree Structure

```
TOP: Fuel Cell Damaged by NN Commands
│
└─ AND Gate: NN Commands Unsafe Parameters AND Protections Fail
   │
   ├─ OR Gate: NN Commands Outside Safe Envelope
   │  │
   │  ├─ NN trained with insufficient data
   │  │  └─ Basic: Edge conditions not in training (P=10⁻⁴/FH)
   │  │
   │  ├─ NN encounters novel operating mode
   │  │  └─ Basic: OOD operational state (P=10⁻⁴/FH)
   │  │
   │  ├─ NN optimization too aggressive
   │  │  └─ Basic: Reward function prioritizes efficiency over safety (P=10⁻⁵/FH)
   │  │
   │  └─ NN software bug
   │     └─ Basic: Inference error (P=10⁻⁶/FH)
   │
   └─ AND Gate: Safety Protections Fail
      │
      ├─ Independent limit monitor fails
      │  ├─ Basic: Monitor hardware fault (P=10⁻⁵/FH)
      │  └─ Basic: Limit thresholds wrong (P=10⁻⁷/FH)
      │
      ├─ Fuel cell controller doesn't reject command
      │  └─ Basic: Controller accepts out-of-range (P=10⁻⁴)
      │
      └─ Crew does not intervene
         └─ Basic: Parameters not displayed or checked (P=10⁻¹)
```

### 4.2 Quantitative Analysis

P(NN Unsafe Command) ≈ 10⁻⁴ + 10⁻⁴ + 10⁻⁵ + 10⁻⁶ ≈ 2.1 × 10⁻⁴/FH

P(All Protections Fail) = (10⁻⁵ + 10⁻⁷) × 10⁻⁴ × 10⁻¹ ≈ 1.0 × 10⁻⁹

P(Top Event) = 2.1 × 10⁻⁴ × 1.0 × 10⁻⁹ = 2.1 × 10⁻¹³/FH

**Result**: Meets hazardous requirement (<10⁻⁷/FH) ✓

---

## 5. COMMON CAUSE ANALYSIS IN FAULT TREES

### 5.1 Common Cause Factors

**Training Data Common Cause**:
- Same dataset → Same biases
- Same preprocessing → Same failure modes
- **Mitigation**: Use diverse training data for redundant channels

**Architecture Common Cause**:
- Same NN design → Same vulnerabilities
- Same hyperparameters → Same convergence issues
- **Mitigation**: Use diverse architectures (e.g., CNN + Transformer)

**Environmental Common Cause**:
- Novel scenario → All NNs fail
- Sensor degradation → All channels affected
- **Mitigation**: Conventional safety monitor independent of NNs

### 5.2 Beta Factor Model

For redundant NN channels, use beta factor for common cause:

P(Both Channels Fail) = P_independent × β + P_single²

Where:
- P_independent = probability of independent simultaneous failure
- β = common cause factor (typically 0.01 to 0.1 for diverse design)
- P_single = single channel failure probability

**Example**:
- P_single = 10⁻³/FH
- β = 0.05 (diverse training/architecture)
- P(Both) = 10⁻³ × 0.05 + (10⁻³)² = 5.0 × 10⁻⁵/FH + 10⁻⁶/FH ≈ 5.1 × 10⁻⁵/FH

**Insight**: Common cause dominates; diversity critical

---

## 6. MINIMAL CUT SETS

### 6.1 Definition

Minimal cut set = smallest combination of basic events that causes top event

### 6.2 Flight Control NN Top Event Minimal Cut Sets

**Critical Minimal Cut Sets** (highest probability):

1. {Model Degradation, Performance Monitor Failure, Safety Monitor Failure, Crew No Detect}
   - P = 10⁻³ × 10⁻² × 10⁻⁵ × 10⁻¹ = 10⁻¹¹/FH

2. {OOD Input, OOD Detector Failure, Safety Monitor Failure, Fallback Failure}
   - P = 10⁻⁴ × 10⁻² × 10⁻⁵ × 10⁻⁴ = 10⁻¹⁵/FH

3. {Training Bias, Rare Scenario, Safety Monitor Failure, Crew No Detect}
   - P = 10⁻² × 10⁻⁴ × 10⁻⁵ × 10⁻¹ = 10⁻¹²/FH

**Importance Ranking**:
1. Safety Monitor (appears in all critical cut sets)
2. Performance Monitoring
3. OOD Detection

**Recommendations**:
- Maximize safety monitor reliability (most critical)
- Improve performance monitoring
- Enhance OOD detection

---

## 7. ASSUMPTIONS AND LIMITATIONS

### 7.1 Assumptions

1. **Event Independence**: Assumed unless explicitly modeled as common cause
2. **Constant Failure Rates**: NN failure rates assumed constant (may increase with age/drift)
3. **Perfect Detection**: Some detectors assumed perfect (conservative)
4. **Crew Performance**: Based on generic human factors data
5. **Test Coverage**: Probabilities from testing assumed representative

### 7.2 Limitations

1. **Unknown Unknowns**: Cannot model scenarios not conceived
2. **Emergent Behavior**: NN interactions may produce unforeseen failures
3. **Data Limitations**: Limited operational data for validation
4. **Model Accuracy**: Probability estimates have uncertainty

### 7.3 Mitigation of Limitations

- **Conservative Assumptions**: Use pessimistic probabilities when uncertain
- **Defense in Depth**: Multiple independent barriers reduce sensitivity to modeling errors
- **Operational Monitoring**: Track actual failures to update model
- **Periodic Review**: Reassess as more data becomes available

---

## 8. FAULT TREE MAINTENANCE

### 8.1 Update Triggers

- Operational failure or anomaly
- Design change to NN system
- New failure mode identified
- Probability estimate refined
- Certification authority feedback

### 8.2 Review Schedule

- **Quarterly**: Review operational data, update probabilities if significant
- **Annually**: Full fault tree review and revalidation
- **Ad-hoc**: After any significant incident or design change

### 8.3 Version Control

All fault trees maintained in safety document repository with version control and change tracking.

---

**Document Control**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-04 | AMPEL360 Safety Team | Initial release |

**Classification**: Safety Critical  
**Next Review**: 2025-02-04 (Quarterly)
