# FTA Templates

**Purpose:** Fault Tree Analysis templates for neural network safety assessment

---

## Related Documents

- [../../Fault_Tree_Analysis.md](../../Fault_Tree_Analysis.md) - FTA Methodology
- [../../Hazard_Analysis_Methodology.md](../../Hazard_Analysis_Methodology.md)
- [../../Common_Cause_Analysis.md](../../Common_Cause_Analysis.md)
- [ARP4761](https://www.sae.org/standards/content/arp4761/) - FTA Guidelines

---

## Templates

### 1. Generic NN Fault Tree Template
**File:** `FTA_Template_Generic_NN.xlsx` (Placeholder)

**Structure:**
- Top Event: Unacceptable NN behavior
- Level 1: NN failures, safety barrier failures
- Level 2: Root causes (training, deployment, operational)
- Quantitative analysis worksheet
- Minimal cut sets calculation

**Usage:** Starting point for any NN system FTA

### 2. Flight Control NN Template
**File:** `FTA_Template_Flight_Control_NN.xlsx` (Placeholder)

**Specific to:** Primary flight control neural networks (DAL A)

**Includes:**
- Catastrophic event: Unsafe flight control command
- Control law failure modes
- Envelope protection failures
- Sensor failure combinations

### 3. Collision Avoidance NN Template
**File:** `FTA_Template_Collision_Avoidance_NN.xlsx` (Placeholder)

**Specific to:** Traffic separation neural networks (DAL B)

**Includes:**
- Hazardous event: Missed traffic collision threat
- Detection failure modes
- Multi-sensor fusion failures
- Alert generation failures

### 4. Propulsion NN Template
**File:** `FTA_Template_Propulsion_NN.xlsx` (Placeholder)

**Specific to:** Fuel cell optimization neural networks (DAL C)

**Includes:**
- Major event: Fuel cell damage
- Optimization algorithm failures
- Parameter limit violations
- Monitoring system failures

---

## Instructions

### Creating a New Fault Tree

1. **Select Template:** Choose appropriate template based on NN system DAL and function
2. **Customize Top Event:** Define specific unacceptable outcome
3. **Identify Failure Paths:** Brainstorm ways top event could occur
4. **Add Basic Events:** Define root causes with probabilities
5. **Connect Gates:** Use AND/OR logic to connect events
6. **Quantify:** Calculate probability of top event
7. **Analyze:** Identify minimal cut sets and critical paths
8. **Document:** Complete all worksheets and save

### Probability Estimation

**Sources:**
- Test-based: From extensive testing (>1M cases)
- Historical: From similar systems if available
- Conservative: When data insufficient, assume higher probability
- Expert judgment: For novel scenarios

**Validation:**
- Independent review required
- Sensitivity analysis performed
- Compare to safety objectives
- Document assumptions

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-04 | AMPEL360 Safety Team | Initial templates |

**Classification**: Safety Critical
