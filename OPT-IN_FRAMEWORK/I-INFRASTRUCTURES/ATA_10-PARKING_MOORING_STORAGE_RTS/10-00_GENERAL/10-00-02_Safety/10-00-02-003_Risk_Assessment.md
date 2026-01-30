# 10-00-02-003 — Risk Assessment

## 1. Purpose

This document establishes the risk assessment methodology for evaluating hazards identified in ATA Chapter 10 operations, providing a systematic approach to prioritize safety efforts and allocate resources.

## 2. Scope

Risk assessment covers:

- Evaluation of hazard severity and likelihood
- Risk level determination
- Acceptability criteria
- Risk prioritization
- Residual risk evaluation

## 3. Risk Assessment Methodology

### 3.1 Risk Matrix

Risk is evaluated using a 5×5 matrix combining severity and likelihood:

```
                    LIKELIHOOD →
         ┌─────────────────────────────────────────────┐
         │         Extremely                           │
         │  Remote   Remote   Occasional  Probable  Frequent
    S    │
    E    │
    V  C │   HIGH     HIGH      HIGH      CRITICAL  CRITICAL
    E  a │
    R  t │
    I  a │  MEDIUM    HIGH      HIGH      HIGH     CRITICAL
    T  s │
    Y  t │
       r │   LOW     MEDIUM     HIGH      HIGH      HIGH
    ↓  o │
       p │   LOW      LOW      MEDIUM     HIGH      HIGH
       h │
       i │
       c │   LOW      LOW       LOW      MEDIUM    MEDIUM
         │
       N │
       e │
       g │
       l │
       i │
       g │
       i │
       b │
       l │
       e │
         └─────────────────────────────────────────────┘
```

### 3.2 Risk Levels

| Risk Level | Description | Action Required |
|------------|-------------|-----------------|
| **CRITICAL** | Unacceptable risk | Immediate action required; operations may not proceed |
| **HIGH** | Significant risk | Mitigation required before operations |
| **MEDIUM** | Moderate risk | Mitigation plan required within defined timeframe |
| **LOW** | Acceptable risk | Monitor; enhance controls as reasonably practicable |

## 4. Risk Assessment Process

### 4.1 Step 1: Hazard Review

For each hazard identified in [10-00-02-002_Hazard_Identification.md](./10-00-02-002_Hazard_Identification.md):

1. Review hazard description
2. Identify all potential consequences
3. Consider worst-case scenarios

### 4.2 Step 2: Severity Assessment

Determine severity based on the most severe credible consequence:

| Severity | Aircraft Effect | Personnel Effect | Environmental Effect |
|----------|----------------|------------------|---------------------|
| **Catastrophic** | Destruction | Multiple fatalities | Major environmental damage |
| **Hazardous** | Major damage | Fatality or serious injuries | Significant environmental impact |
| **Major** | Significant damage | Serious injury | Moderate environmental impact |
| **Minor** | Minor damage | Minor injury | Minor environmental impact |
| **Negligible** | No damage | No injury | No environmental impact |

### 4.3 Step 3: Likelihood Assessment

Determine likelihood based on:

- Historical data from similar operations
- Engineering analysis and modeling
- Subject matter expert judgment
- Industry experience

| Likelihood | Quantitative | Qualitative Description |
|------------|-------------|------------------------|
| **Frequent** | > 10⁻³ | Expected to occur regularly |
| **Probable** | 10⁻³ to 10⁻⁴ | Will probably occur several times |
| **Occasional** | 10⁻⁴ to 10⁻⁵ | May occur sometime |
| **Remote** | 10⁻⁵ to 10⁻⁶ | Unlikely, but possible |
| **Extremely Remote** | < 10⁻⁶ | Extremely unlikely to occur |

### 4.4 Step 4: Initial Risk Determination

Combine severity and likelihood using the risk matrix to determine initial risk level.

### 4.5 Step 5: Existing Controls Review

Document existing controls:

- Design features
- Procedural controls
- Training requirements
- PPE requirements
- Detection systems
- Administrative controls

### 4.6 Step 6: Mitigation Planning

For risks not meeting acceptability criteria:

1. Identify additional mitigation measures
2. Prioritize based on effectiveness and feasibility
3. Assign responsibility and timeline
4. Document in Mitigation Measures register

### 4.7 Step 7: Residual Risk Assessment

After implementing mitigations:

1. Re-evaluate severity (may be reduced by design changes)
2. Re-evaluate likelihood (reduced by controls)
3. Determine residual risk level
4. Verify acceptability

## 5. Risk Acceptability Criteria

### 5.1 ALARP Principle

Risks must be reduced to "As Low As Reasonably Practicable" (ALARP):

- **Critical/High Risk**: Must be reduced; significant effort justified
- **Medium Risk**: Reduce if reasonably practicable
- **Low Risk**: Generally acceptable; monitor for changes

### 5.2 Hydrogen-Specific Criteria

For hydrogen-related hazards:

- **Catastrophic + Occasional or worse**: Not acceptable
- **Hazardous + Probable or worse**: Requires engineering controls
- **Major + Frequent**: Requires multiple layers of protection

### 5.3 High Voltage Criteria

For HV electrical hazards:

- **Fatal electric shock + Remote or worse**: Requires isolation systems
- **Arc flash + Occasional or worse**: Requires PPE and procedures
- **Contact with live parts**: Must be Extremely Remote

## 6. Risk Assessment Documentation

### 6.1 Risk Register

All assessed risks are tracked in the Risk Register:

**Location**: [10-00-02-099-C_Risk_Register.md](./10-00-02-099_Index/10-00-02-099-C_Risk_Register.md)

**Schema**: [risk-assessment.schema.json](./10-00-02-090_Schemas/risk-assessment.schema.json)

### 6.2 Required Information

For each risk:

- Hazard ID (linkage to hazard register)
- Initial severity and likelihood
- Initial risk level
- Existing controls
- Additional mitigation measures
- Residual severity and likelihood
- Residual risk level
- Risk owner
- Status and review date

## 7. Specific Risk Assessments

### 7.1 Hydrogen Risk Assessment

Detailed assessment in: [10-00-02-005_H2_Specific_Safety/](./10-00-02-005_H2_Specific_Safety/)

Key considerations:

- LH₂ leak scenarios
- Ignition sources control
- Ventilation adequacy
- Emergency response capability
- Personnel exposure limits

### 7.2 High Voltage Risk Assessment

Detailed assessment in: [10-00-02-006_High_Voltage_Safety/](./10-00-02-006_High_Voltage_Safety/)

Key considerations:

- Electrical isolation effectiveness
- LOTO procedure compliance
- Arc flash hazard analysis
- PPE adequacy
- Qualified personnel requirements

### 7.3 Cryogenic Risk Assessment

Detailed assessment in: [10-00-02-007_Cryogenic_Safety/](./10-00-02-007_Cryogenic_Safety/)

Key considerations:

- Cold burn exposure scenarios
- Material compatibility
- Oxygen displacement in confined spaces
- Emergency response for cryogenic spills

### 7.4 Fire Risk Assessment

Detailed assessment in: [10-00-02-008_Fire_Protection/](./10-00-02-008_Fire_Protection/)

Key considerations:

- Fire detection system reliability
- Suppression system adequacy
- H₂ fire unique characteristics
- Evacuation time requirements
- Fire-resistant boundaries

## 8. Risk Review and Update

### 8.1 Regular Reviews

Risk assessments are reviewed:

- **Quarterly**: For operational risks
- **Annually**: Comprehensive review of all risks
- **After incidents**: Following any safety event
- **Design changes**: When systems or procedures change

### 8.2 Triggers for Re-assessment

- New hazard identified
- Change in operational environment
- New technology introduced
- Regulatory requirement changes
- Incident or near-miss occurs
- Mitigation effectiveness data available

## 9. Risk Communication

Risk information is communicated to:

- **Operations personnel**: Residual risks for their activities
- **Management**: High/critical risks requiring attention
- **Maintenance**: Risks during servicing activities
- **Emergency responders**: Risks for emergency planning
- **Regulatory authorities**: As required for certification

## 10. Cross-References

- **Hazard Identification**: [10-00-02-002_Hazard_Identification.md](./10-00-02-002_Hazard_Identification.md)
- **Mitigation Measures**: [10-00-02-004_Mitigation_Measures.md](./10-00-02-004_Mitigation_Measures.md)
- **Risk Register**: [10-00-02-099-C_Risk_Register.md](./10-00-02-099_Index/10-00-02-099-C_Risk_Register.md)

## 11. Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | 10-00-02-003 |
| **Version** | 1.0 |
| **Status** | 🔄 Draft — Preliminary Design |
| **Classification** | AMPEL360 Internal |
| **Owner** | Safety Engineering |
| **Last Updated** | 2025-12-09 |
| **Next Review** | 2026-03-09 |

---

**Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.**
