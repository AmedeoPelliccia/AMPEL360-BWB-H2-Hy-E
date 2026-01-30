# 03-00-02-002 — Hazard Identification and Risk Assessment for GSE

## 1. Purpose

This document defines the **methods and procedures for hazard identification (HAZID) and risk assessment** for Ground Support Equipment (GSE) operations under [ATA 03 – Support Information GSE](https://www.ata.org/resources/specifications/ispec2200).

It establishes:

- Hazard identification methodologies
- Risk assessment techniques (risk matrices, bow-tie analysis, FMEA)
- Risk control hierarchy
- Risk register management
- Periodic risk review processes

---

## 2. Hazard Identification (HAZID)

### 2.1 Definition

A **hazard** is any condition, event, or circumstance that could lead to or contribute to an unplanned or undesirable event, including injury, illness, equipment damage, or operational disruption.

### 2.2 Hazard Identification Methods

#### 2.2.1 Structured Workshops

- **HAZID Workshops**: Facilitated sessions with cross-functional teams (operations, maintenance, safety, engineering)
- **What-If Analysis**: Systematic questioning of GSE operations to identify potential hazards
- **Task-Based Analysis**: Breakdown of GSE tasks to identify hazards at each step

#### 2.2.2 Operational Observation

- **Safety Walk-Throughs**: Regular inspections of GSE operations to observe unsafe conditions or behaviors
- **Job Safety Analysis (JSA)**: Analysis of specific GSE tasks to identify hazards
- **Near-Miss Reporting**: Capturing events that could have resulted in harm

#### 2.2.3 Historical Data Review

- **Incident and Accident Analysis**: Review of past incidents to identify recurring hazards
- **Industry Benchmarking**: Review of [IATA Safety Report](https://www.iata.org/en/publications/safety-report/) and industry incidents
- **Manufacturer Safety Bulletins**: Review of GSE manufacturer safety notices

#### 2.2.4 Change Management

- **Pre-Change HAZID**: Identification of hazards introduced by changes to GSE equipment, procedures, or operations
- **New Equipment Introduction**: HAZID conducted before introducing new GSE types

### 2.3 Common GSE Hazards

| Hazard Category | Examples |
|---|---|
| **Collision/Impact** | GSE collision with aircraft, personnel, or other equipment |
| **Fire/Explosion** | H₂ leaks, fuel spills, electrical fires, battery fires |
| **Mechanical** | Equipment failure, moving parts, pinch points, hydraulic failure |
| **Slip/Trip/Fall** | Uneven surfaces, spills, poor lighting, working at height |
| **Ergonomic** | Manual handling, repetitive tasks, awkward postures |
| **Environmental** | Extreme weather, noise, exhaust fumes, cryogenic exposure (H₂) |
| **Human Factors** | Fatigue, distraction, inadequate training, communication errors |
| **Chemical** | H₂ asphyxiation, cryogenic burns, hydraulic fluid exposure |

---

## 3. Risk Assessment

### 3.1 Risk Definition

**Risk** = **Likelihood** × **Severity**

- **Likelihood**: Probability that a hazard will result in harm
- **Severity**: Potential consequences of harm (injury, damage, operational disruption)

### 3.2 Risk Matrix

The following **5×5 risk matrix** is used to assess and prioritize risks:

| Likelihood / Severity | **Negligible (1)** | **Minor (2)** | **Moderate (3)** | **Major (4)** | **Catastrophic (5)** |
|---|:---:|:---:|:---:|:---:|:---:|
| **Almost Certain (5)** | Medium | High | High | Extreme | Extreme |
| **Likely (4)** | Low | Medium | High | High | Extreme |
| **Possible (3)** | Low | Medium | Medium | High | High |
| **Unlikely (2)** | Low | Low | Medium | Medium | High |
| **Rare (1)** | Low | Low | Low | Medium | Medium |

#### Risk Rating Definitions

- **Extreme**: Unacceptable risk – immediate action required, stop operations if necessary
- **High**: Significant risk – priority action required, senior management approval needed to continue
- **Medium**: Moderate risk – action required within defined timeframe
- **Low**: Acceptable risk – manage through routine procedures

#### Likelihood Definitions

| Level | Description | Frequency |
|---|---|---|
| **Almost Certain (5)** | Expected to occur frequently | More than once per month |
| **Likely (4)** | Will probably occur | Once per month to once per year |
| **Possible (3)** | Might occur occasionally | Once per year to once per 5 years |
| **Unlikely (2)** | Could occur but unlikely | Once per 5 years to once per 20 years |
| **Rare (1)** | Very unlikely to occur | Less than once per 20 years |

#### Severity Definitions

| Level | Description | Injury | Equipment Damage | Operational Impact |
|---|---|---|---|---|
| **Catastrophic (5)** | Multiple fatalities or permanent total disabilities | Multiple fatalities | > $5M | Complete shutdown > 7 days |
| **Major (4)** | Single fatality or permanent partial disability | Fatality | $1M - $5M | Major disruption 3-7 days |
| **Moderate (3)** | Serious injury requiring hospitalization | Lost time injury | $100K - $1M | Moderate disruption 1-3 days |
| **Minor (2)** | Minor injury requiring first aid | Recordable injury | $10K - $100K | Minor disruption < 1 day |
| **Negligible (1)** | No injury or very minor injury | No injury | < $10K | No operational impact |

---

## 4. Risk Assessment Techniques

### 4.1 Bow-Tie Analysis

**Purpose**: Visualize the pathways from hazard causes to consequences, identifying barriers/controls at each stage.

**Structure**:
- **Hazard** (center): The source of potential harm (e.g., H₂ leak during refuelling)
- **Threats** (left): Causes that could trigger the hazard (e.g., connection failure, overpressure, equipment damage)
- **Preventive Barriers** (left): Controls to prevent hazard occurrence (e.g., leak detection, pressure relief valves, maintenance inspections)
- **Consequences** (right): Potential outcomes if hazard occurs (e.g., fire, explosion, asphyxiation)
- **Mitigative Barriers** (right): Controls to reduce consequences (e.g., fire suppression, emergency response, evacuation procedures)

**Example**: See [ASSETS/03-00-02-A-003_BowTie_Analysis_H2_Refuelling.svg](./ASSETS/03-00-02-A-003_BowTie_Analysis_H2_Refuelling.svg)

### 4.2 Failure Modes and Effects Analysis (FMEA)

**Purpose**: Systematic analysis of potential failure modes of GSE components/systems and their effects.

**Process**:
1. Identify GSE component or system
2. List potential failure modes (how it could fail)
3. Determine effects of each failure mode
4. Assess severity, occurrence, and detectability
5. Calculate Risk Priority Number (RPN) = Severity × Occurrence × Detectability
6. Prioritize and implement controls for high RPN items

**Template**: See [ASSETS/03-00-02-A-004_FMEA_Template.xlsx](./ASSETS/03-00-02-A-004_FMEA_Template.xlsx)

**Example FMEA Entry**:

| Component | Failure Mode | Effect | Severity (1-10) | Occurrence (1-10) | Detectability (1-10) | RPN | Control Measures |
|---|---|---|:---:|:---:|:---:|:---:|---|
| H₂ Refuelling Hose | Connection leak | H₂ release, fire risk | 9 | 4 | 3 | 108 | Leak detection sensors, breakaway coupling, maintenance inspections |

### 4.3 Risk Register

A **risk register** is a living document that tracks all identified risks, their assessments, and control measures.

**Template**: See [ASSETS/03-00-02-A-005_Risk_Register_Template.xlsx](./ASSETS/03-00-02-A-005_Risk_Register_Template.xlsx)

**Fields**:
- Risk ID
- Hazard description
- Risk scenario
- Likelihood rating
- Severity rating
- Initial risk level
- Control measures (existing)
- Residual risk level
- Additional actions required
- Action owner
- Target completion date
- Status

---

## 5. Risk Control Hierarchy

Risks shall be controlled using the following **hierarchy of controls** (in order of effectiveness):

### 5.1 Elimination

**Preferred**: Remove the hazard entirely
- **Example**: Replace manual GSE operations with automated systems

### 5.2 Substitution

Replace hazardous equipment, materials, or processes with less hazardous alternatives
- **Example**: Use electric GSE instead of diesel-powered equipment to reduce fire risk

### 5.3 Engineering Controls

Physical changes to equipment or environment to reduce risk
- **Example**: Install H₂ leak detection sensors, physical barriers around refuelling areas, automatic shutdown systems

### 5.4 Administrative Controls

Procedures, training, and policies to reduce risk
- **Example**: Speed limits, exclusion zones, work permits, safety briefings, scheduled maintenance

### 5.5 Personal Protective Equipment (PPE)

**Least Effective**: Equipment worn to protect against hazards
- **Example**: High-visibility vests, safety footwear, hearing protection, flame-resistant clothing, cryogenic gloves

---

## 6. Risk Register Management

### 6.1 Risk Register Ownership

- **GSE Safety Manager**: Overall ownership and maintenance of risk register
- **Risk Owners**: Designated individuals responsible for managing specific risks
- **Risk Review Board**: Quarterly review of risk register by cross-functional team

### 6.2 Risk Register Updates

The risk register shall be updated:
- **Immediately**: When new hazards are identified or significant incidents occur
- **After Changes**: When changes are made to GSE equipment, procedures, or operations
- **Quarterly**: Routine review of all open risks
- **Annually**: Comprehensive review and re-assessment of all risks

### 6.3 Risk Acceptance

Risks assessed as **Medium** or **Low** may be accepted with approval from:
- **Low**: Ground Operations Manager
- **Medium**: GSE Safety Manager

Risks assessed as **High** or **Extreme** require:
- **High**: Senior Management approval and documented justification
- **Extreme**: Not acceptable – operations must cease until risk is reduced

---

## 7. Hydrogen-Specific Risk Assessment

For H₂-related hazards, additional considerations apply:

### 7.1 H₂ Hazard Characteristics

- **Flammability**: Wide flammability range (4-75% in air), low ignition energy
- **Invisible Flame**: H₂ burns with nearly invisible flame in daylight
- **Rapid Dispersion**: H₂ disperses quickly due to low density
- **Cryogenic**: Liquid H₂ stored at -253°C, risk of cold burns and embrittlement
- **Asphyxiation**: H₂ can displace oxygen in confined spaces

### 7.2 H₂ Risk Assessment Requirements

- **Quantitative Risk Assessment (QRA)**: For high-volume H₂ storage and transfer operations
- **Explosion Modeling**: Simulation of potential H₂ vapor cloud explosions
- **Dispersion Modeling**: Analysis of H₂ leak dispersion and concentration levels
- **Fire Safety Analysis**: Assessment of H₂ fire scenarios and mitigation effectiveness

See [03-00-02-004_H2_Specific_Safety_Considerations.md](./03-00-02-004_H2_Specific_Safety_Considerations.md) for detailed H₂ safety requirements.

---

## 8. Integration with Other Processes

### 8.1 Safety Training

Risk assessments inform training content and competency requirements
See [03-00-02-005_Safety_Training_and_Competency.md](./03-00-02-005_Safety_Training_and_Competency.md)

### 8.2 Incident Investigation

Incidents trigger review and update of risk assessments
See [03-00-02-006_Safety_Incident_Reporting_and_Lessons_Learned.md](./03-00-02-006_Safety_Incident_Reporting_and_Lessons_Learned.md)

### 8.3 Audits and Inspections

Audits verify effectiveness of risk controls
See [03-00-02-008_Safety_Audits_and_Inspections.md](./03-00-02-008_Safety_Audits_and_Inspections.md)

---

## 9. Regulatory Alignment

This methodology aligns with:

- **[ISO 31000](https://www.iso.org/iso-31000-risk-management.html)** (Risk Management)
- **ISO 45001** (Occupational Health and Safety Management Systems)
- **[ICAO Safety Management Manual (Doc 9859)](https://www.icao.int/safety/SafetyManagement/Pages/Doc-9859.aspx)**
- **[IATA Safety Audit for Ground Operations (ISAGO)](https://www.iata.org/en/programs/safety/audit/isago/)**

---

## 10. References

- [03-00-02-001_Safety_Management_Framework.md](./03-00-02-001_Safety_Management_Framework.md)
- [03-00-02-003_Operational_Safety_Rules_GSE.md](./03-00-02-003_Operational_Safety_Rules_GSE.md)
- [03-00-02-004_H2_Specific_Safety_Considerations.md](./03-00-02-004_H2_Specific_Safety_Considerations.md)
- [ASSETS/03-00-02-A-003_BowTie_Analysis_H2_Refuelling.svg](./ASSETS/03-00-02-A-003_BowTie_Analysis_H2_Refuelling.svg)
- [ASSETS/03-00-02-A-004_FMEA_Template.xlsx](./ASSETS/03-00-02-A-004_FMEA_Template.xlsx)
- [ASSETS/03-00-02-A-005_Risk_Register_Template.xlsx](./ASSETS/03-00-02-A-005_Risk_Register_Template.xlsx)

---

## 11. Document Control

- **Status**: `DRAFT` – Subject to human review and approval
- **Owner**: GSE Safety Manager
- **Approver**: _[to be completed]_
- **Last Updated**: 2025-11-21
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`

---
