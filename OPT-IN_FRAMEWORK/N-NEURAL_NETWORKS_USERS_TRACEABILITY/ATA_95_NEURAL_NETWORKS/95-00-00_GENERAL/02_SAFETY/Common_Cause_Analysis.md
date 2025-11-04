# Common Cause Analysis for Neural Network Systems

**Document ID:** AMPEL360-95-00-00-SAF-CCA  
**Version:** 1.0  
**Date:** 2025-11-04  
**Classification:** Safety Critical

---

## 1. INTRODUCTION

### 1.1 Purpose

This document identifies and analyzes common causes that could simultaneously affect multiple neural network channels, defeating redundancy and independence assumptions.

### 1.2 Scope

Covers all redundant and diverse neural network systems in the AMPEL360 aircraft, with focus on DAL A and B systems where redundancy is required for safety.

### 1.3 Definition

**Common Cause Failure**: A single event or condition that causes multiple systems/channels to fail simultaneously, defeating redundancy.

### 1.4 Related Documents

- [Safety_Framework_Overview.md](Safety_Framework_Overview.md)
- [Fault_Tree_Analysis.md](Fault_Tree_Analysis.md)
- [Failure_Modes_Effects_Analysis.csv](Failure_Modes_Effects_Analysis.csv)
- [Runtime_Safety_Monitoring.md](Runtime_Safety_Monitoring.md)
- [ARP4761](https://www.sae.org/standards/content/arp4761/) - Common Cause Analysis Guidelines
- [ARP4754A](https://www.sae.org/standards/content/arp4754a/) - Development Guidelines

---

## 2. NN-SPECIFIC COMMON CAUSE CATEGORIES

### 2.1 Training Data Common Causes

#### 2.1.1 Same Dataset

**Description**: All redundant NN channels trained on identical data

**Risk**:
- Same biases propagate to all channels
- Same gaps in coverage affect all channels
- Same label errors learned by all

**Manifestation**:
- All channels fail in scenarios underrepresented in training data
- All channels exhibit same systematic bias

**Examples**:
- Training data contains only daytime images → All vision NNs fail at night
- Training data biased to normal weather → All NNs fail in severe weather
- Training data from single geographic region → All NNs fail in other regions

**Mitigation Strategies**:

1. **Diverse Datasets** (Preferred):
   - Train Channel A on Dataset 1
   - Train Channel B on Dataset 2 (overlapping but different sources)
   - Ensures independent failure modes

2. **Augmentation Diversity**:
   - Use different augmentation strategies for each channel
   - One channel: geometric transforms
   - Another channel: photometric transforms

3. **Temporal Diversity**:
   - Train channels on data from different time periods
   - Reduces temporal bias common cause

**Verification**:
- Dataset overlap analysis (<80% overlap)
- Independent bias testing per channel
- Cross-validation on disjoint test sets

**Residual Risk**: β_data = 0.05 to 0.20 depending on diversity

#### 2.1.2 Same Preprocessing

**Description**: Identical data preprocessing applied to all channels

**Risk**:
- Preprocessing bug affects all channels
- Normalization errors common to all
- Feature engineering flaws universal

**Mitigation**:
- Use diverse preprocessing pipelines
- One channel: manual feature engineering
- Another channel: learned features (end-to-end)

**Residual Risk**: β_preprocess = 0.02 to 0.10

#### 2.1.3 Data Collection Common Cause

**Description**: Same sensors/collection process for all training data

**Risk**:
- Sensor biases common to all data
- Collection methodology affects all samples
- Environmental biases during collection

**Mitigation**:
- Collect data from diverse sources (different aircraft, locations, time periods)
- Use simulated data to fill gaps
- Independent data quality validation

**Residual Risk**: β_collection = 0.05 to 0.15

---

### 2.2 Model Architecture Common Causes

#### 2.2.1 Same Architecture

**Description**: Redundant channels use identical NN architecture

**Risk**:
- Same architectural vulnerabilities in all channels
- Same convergence issues
- Same adversarial vulnerabilities

**Manifestation**:
- All channels fail on same input patterns
- All channels exhibit same numerical instabilities

**Examples**:
- All channels use ResNet → Common adversarial vulnerabilities
- All channels use LSTM → Common vanishing gradient issues
- All channels use specific activation → Common saturation problems

**Mitigation Strategies**:

1. **Architectural Diversity** (Strongly Recommended):
   - Channel A: Convolutional Neural Network (CNN)
   - Channel B: Transformer
   - Channel C: Classical algorithm (safety monitor)

2. **Design Diversity Within Same Paradigm**:
   - Channel A: ResNet architecture
   - Channel B: EfficientNet architecture
   - Different depth, width, skip connections

3. **Hybrid Approaches**:
   - Channel A: Deep learning
   - Channel B: Ensemble of shallow models
   - Different failure modes

**Verification**:
- Architectural dissimilarity analysis
- Adversarial testing (one channel fails, other succeeds)
- Cross-channel failure correlation measurement

**Residual Risk**: 
- Same architecture: β_arch = 0.30 to 0.50
- Diverse architectures: β_arch = 0.05 to 0.15

#### 2.2.2 Same Hyperparameters

**Description**: Redundant channels trained with identical hyperparameters

**Risk**:
- Same overfitting/underfitting issues
- Same convergence problems
- Same regularization effects

**Mitigation**:
- Use different hyperparameters (learning rate, batch size, regularization)
- Train to different convergence criteria
- Use different optimization algorithms

**Residual Risk**: β_hyper = 0.05 to 0.15

#### 2.2.3 Same Training Algorithm

**Description**: All channels trained with same optimization algorithm

**Risk**:
- Same local minima attraction
- Same training instabilities
- Same initialization sensitivities

**Mitigation**:
- Channel A: SGD with momentum
- Channel B: Adam optimizer
- Different random seeds

**Residual Risk**: β_training = 0.05 to 0.10

---

### 2.3 Environmental Common Causes

#### 2.3.1 Novel Operational Scenario

**Description**: All NNs encounter scenario outside training distribution

**Risk**: Most critical NN common cause

**Manifestation**:
- All NN channels produce poor predictions
- OOD detection may trigger in all channels simultaneously

**Examples**:
- Never-before-seen weather phenomenon
- Novel aircraft configuration not in training
- Unprecedented system failure combination
- New obstacle/traffic type

**Mitigation Strategies**:

1. **Broad ODD Coverage**:
   - Extensive training data covering wide operational range
   - Synthetic data for rare scenarios
   - Adversarial testing

2. **OOD Detection** (Critical):
   - Independent OOD detector for each channel
   - If detected, switch to conventional safety monitor

3. **Conventional Safety Monitor** (Essential):
   - Independent algorithm not affected by training data
   - Physics-based or rule-based system
   - Acts as ultimate fallback

**Verification**:
- Stress testing with beyond-ODD scenarios
- Verify conventional monitor independence
- OOD detection coverage testing

**Residual Risk**: 
- With OOD detection + conventional monitor: β_OOD = 0.01 to 0.05
- Without: β_OOD = 0.50 to 0.80 (unacceptable)

#### 2.3.2 Sensor Degradation

**Description**: Input sensors degrade, affecting all NN channels

**Risk**:
- All channels receive poor quality inputs
- Degradation may be outside training experience

**Examples**:
- Camera lens fouling (dirt, ice, moisture)
- Sensor drift/aging
- Interference affecting all sensors

**Mitigation**:
- Sensor diversity (different sensor types for redundant channels)
- Sensor health monitoring
- Input quality checking before NN
- Sensor redundancy (3x)

**Residual Risk**: β_sensor = 0.10 to 0.30 (depending on diversity)

#### 2.3.3 Adversarial Attack

**Description**: Deliberately crafted input to fool NNs

**Risk**:
- Attacker may target common vulnerabilities
- All NN channels potentially affected

**Mitigation**:
- Adversarial training for all channels
- Input sanitization and validation
- Architectural diversity reduces attack transferability
- Anomaly detection

**Residual Risk**: β_adv = 0.10 to 0.40 (depends on diversity)

---

### 2.4 Software/Hardware Common Causes

#### 2.4.1 Common Software Framework

**Description**: All NN channels use same ML framework (TensorFlow, PyTorch)

**Risk**:
- Framework bug affects all channels
- Compiler optimization errors
- Library vulnerabilities

**Mitigation**:
- Use different framework versions (if compatible)
- Diverse implementations (one in TensorFlow, one in PyTorch)
- Extensive verification testing
- Safety monitor in different language/framework

**Residual Risk**: β_framework = 0.05 to 0.15

#### 2.4.2 Common Hardware Platform

**Description**: All NN channels on same GPU/hardware

**Risk**:
- Hardware failure affects all channels
- Thermal event impacts all
- SEU/radiation affects all

**Mitigation**:
- Physically separate GPU cards
- Different GPU vendors/models if possible
- Conventional monitor on different hardware (CPU)
- ECC memory, radiation hardening

**Residual Risk**: β_hardware = 0.10 to 0.30

#### 2.4.3 Common Power Source

**Description**: All NN channels powered by same bus

**Risk**:
- Power failure disables all channels

**Mitigation**:
- Redundant power buses
- Conventional monitor on independent power
- Battery backup for safety monitor

**Residual Risk**: β_power = 0.01 to 0.05 (with bus diversity)

---

## 3. QUANTITATIVE COMMON CAUSE ANALYSIS

### 3.1 Beta Factor Model

For redundant NN system with common cause:

**P(Both Channels Fail) = P_independent + P_common**

Where:
- P_independent = (P_single)² (if truly independent)
- P_common = β × P_single (common cause contribution)
- β = common cause factor (0 to 1)

**Total: P(Both) = (P_single)² + β × P_single**

**For small P_single, common cause dominates!**

### 3.2 Beta Factor Estimation

**Overall System Beta**:

β_system = β_data × β_arch × β_env × β_sw × β_hw

**Example Calculation** (Dual Redundant Flight Control NN):

Assumptions:
- Diverse datasets: β_data = 0.10
- Diverse architectures: β_arch = 0.10
- OOD detection + conventional monitor: β_env = 0.02
- Same framework: β_sw = 0.10
- Separate GPUs: β_hw = 0.20

β_system = 0.10 × 0.10 × 0.02 × 0.10 × 0.20 = 4 × 10⁻⁶

**With P_single = 10⁻³/FH**:

P(Both) = (10⁻³)² + 4×10⁻⁶ × 10⁻³ = 10⁻⁶ + 4×10⁻⁹ ≈ 10⁻⁶/FH

**Common cause adds negligible contribution** ✓

### 3.3 Sensitivity Analysis

**Impact of Beta Factors**:

| Scenario | β_data | β_arch | β_env | P(Both) | Acceptable? |
|----------|--------|--------|-------|---------|-------------|
| Baseline (diverse) | 0.10 | 0.10 | 0.02 | 10⁻⁶ | ✓ (DAL B) |
| Same dataset | 0.50 | 0.10 | 0.02 | 5×10⁻⁶ | ✓ (DAL B marginal) |
| Same architecture | 0.10 | 0.50 | 0.02 | 5×10⁻⁶ | ✓ (DAL B marginal) |
| No OOD detection | 0.10 | 0.10 | 0.50 | 5×10⁻⁵ | ✗ (DAL B fail) |
| Worst case (all same) | 0.50 | 0.50 | 0.50 | 1.25×10⁻⁴ | ✗ (unacceptable) |

**Critical Insight**: Environmental common cause (OOD) is most important

---

## 4. MITIGATION STRATEGIES SUMMARY

### 4.1 Mandatory Mitigations (DAL A/B)

1. **Conventional Safety Monitor**
   - Independent of all NN channels
   - Physics-based or rule-based
   - Different hardware/software
   - → Breaks all NN common causes

2. **OOD Detection**
   - Required on all NN channels
   - Triggers fallback to conventional
   - → Mitigates environmental common cause

3. **Sensor Diversity**
   - Different sensor types for redundant channels
   - → Mitigates sensor common cause

4. **Hardware Separation**
   - Physically separate processors
   - → Mitigates hardware common cause

### 4.2 Recommended Mitigations

1. **Dataset Diversity**
   - Distinct data sources for channels
   - → Reduces β_data from 0.50 to 0.10

2. **Architectural Diversity**
   - Different NN architectures
   - → Reduces β_arch from 0.50 to 0.10

3. **Software Diversity**
   - Different ML frameworks if practical
   - → Reduces β_sw from 0.15 to 0.05

### 4.3 Effectiveness Hierarchy

**Most Effective** (breaks common cause completely):
1. Conventional safety monitor
2. Diverse sensor modalities

**Highly Effective** (reduces β by 5-10×):
3. Architectural diversity
4. Dataset diversity
5. OOD detection

**Moderately Effective** (reduces β by 2-3×):
6. Software framework diversity
7. Hardware diversity

---

## 5. VERIFICATION OF INDEPENDENCE

### 5.1 Test Methods

#### 5.1.1 Correlation Testing

**Method**: Measure failure correlation between channels

**Test**:
- Inject faults into test scenarios
- Record which channels fail
- Calculate correlation coefficient

**Acceptance**:
- Correlation < 0.20 for diverse channels
- If higher, investigate common cause

#### 5.1.2 Common Mode Failure Testing

**Method**: Specifically test for common failure scenarios

**Tests**:
- Present OOD inputs to all channels
- Inject common sensor degradation
- Apply adversarial attacks

**Verification**:
- At least one channel or safety monitor detects issue
- Fallback mechanism engages

#### 5.1.3 Dissimilarity Metrics

**Dataset Dissimilarity**:
- Measure overlap percentage
- Target: <80% overlap

**Architectural Dissimilarity**:
- Compare layer structures
- Different paradigms preferred

**Software Dissimilarity**:
- Different frameworks/versions
- Different compilation options

---

## 6. DOCUMENTATION REQUIREMENTS

### 6.1 Common Cause Analysis Report

Required sections:

1. **Identification of Common Causes**
   - List all potential common causes
   - Categorize by type

2. **Quantitative Assessment**
   - Estimate beta factors
   - Calculate combined failure probability
   - Compare to safety objectives

3. **Mitigation Strategies**
   - For each common cause
   - Implementation description
   - Effectiveness assessment

4. **Verification Evidence**
   - Test results
   - Independence metrics
   - Correlation measurements

5. **Residual Risk**
   - Remaining common cause sensitivity
   - Justification of acceptability

---

## 7. OPERATIONAL MONITORING

### 7.1 In-Service Tracking

**Monitor for Common Cause Indicators**:

- Multiple NN channels failing in same scenario (track frequency)
- OOD detection rate (should be low, <1% of operations)
- Conventional monitor activation rate
- Sensor degradation affecting all channels

**Action Triggers**:
- Common cause rate >10⁻³/FH → Investigate
- Multiple channels fail in specific scenario → Retrain/update
- Systematic bias detected → Dataset augmentation

### 7.2 Continuous Improvement

**Feedback Loop**:
1. Operational data reveals common cause
2. Root cause analysis
3. Update training data / modify architecture
4. Revalidate independence
5. Deploy update

---

**Document Control**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-04 | AMPEL360 Safety Team | Initial release |

**Classification**: Safety Critical  
**Next Review**: 2025-02-04 (Quarterly)
