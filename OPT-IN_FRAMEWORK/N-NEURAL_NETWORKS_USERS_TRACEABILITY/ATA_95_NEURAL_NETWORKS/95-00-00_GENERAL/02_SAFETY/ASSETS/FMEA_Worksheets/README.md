# FMEA Worksheets

**Purpose:** Failure Modes and Effects Analysis worksheets for neural network components

---

## Worksheets

### 1. FMEA Template - Neural Network Components
**File:** `FMEA_Template_NN_Components.xlsx` (Placeholder)

**Columns:**
- Component
- Failure Mode
- NN-Specific Cause
- Local Effect
- System Effect
- Aircraft Effect
- Detection Method
- Compensation
- Mitigation
- Severity
- Probability
- DAL

**Components Covered:**
- Input preprocessing
- Feature extraction
- Neural network core
- Output processing
- Confidence estimation
- Explainability module
- Safety monitor
- Hardware (GPU, memory)

### 2. FMEA Template - Training Phase
**File:** `FMEA_Template_Training_Phase.xlsx` (Placeholder)

**Focus:** Failures during model development

**Failure Modes:**
- Insufficient training data
- Data bias
- Label errors
- Overfitting
- Training instability
- Architecture selection errors

### 3. FMEA Template - Deployment Phase
**File:** `FMEA_Template_Deployment_Phase.xlsx` (Placeholder)

**Focus:** Operational failures

**Failure Modes:**
- OOD inputs
- Concept drift
- Adversarial attacks
- Hardware degradation
- Software bugs
- Configuration errors

---

## FMEA Process

### Step 1: Identify Components
- List all components of NN system
- Include hardware, software, data, processes

### Step 2: Identify Failure Modes
- For each component, list ways it could fail
- Consider NN-specific modes (OOD, drift, bias, etc.)
- Review industry lessons learned

### Step 3: Analyze Effects
- Local effect (on component itself)
- System effect (on NN system)
- Aircraft effect (on aircraft/crew/safety)

### Step 4: Severity Classification
- Catastrophic: Prevents safe flight/landing
- Hazardous: Large reduction in safety margins
- Major: Significant operational limitations
- Minor: Slight reduction in safety
- No Effect: No impact

### Step 5: Detection and Mitigation
- How is failure detected?
- What compensates for failure?
- What prevents or mitigates failure?

### Step 6: Probability Assessment
- Estimate failure probability
- Based on testing, analysis, or conservative assumption
- Consider detection and mitigation effectiveness

### Step 7: DAL Assignment
- Based on severity of worst-case effect
- Determines development assurance level

---

## Severity Assessment Guidelines

### For Neural Networks

**Catastrophic (DAL A)**:
- Primary flight control NN commands unsafe maneuver
- NN prevents safe landing
- NN causes loss of aircraft control

**Hazardous (DAL B)**:
- Collision avoidance NN misses traffic
- Navigation NN causes position loss
- Propulsion NN damages fuel cells

**Major (DAL C)**:
- Fuel optimization NN causes early landing
- Structural health NN misses crack
- Route planning NN adds significant delay

**Minor (DAL D)**:
- Performance optimization NN suboptimal
- Comfort systems NN fails
- Non-essential advisory NN errors

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-04 | AMPEL360 Safety Team | Initial worksheets |

**Classification**: Safety Critical
