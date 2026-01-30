# 85-00-08-002 Prototype Planning and Prioritization

## 1. Purpose

This document establishes the planning and prioritization framework for prototyping activities within [ATA 85 – Infrastructure Interface Standards](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes).

## 2. Planning Process

### 2.1 Prototype Identification
Sources for prototype candidates:
- High-risk items from [FMEA/FHA](../85-00-02_Safety/README.md)
- Novel technologies with limited heritage
- Critical interfaces requiring regulatory approval
- Stakeholder-requested validation items

### 2.2 Prototype Definition
Each prototype shall have:
- **Objectives**: Clear success criteria and learning goals
- **Scope**: What will be tested vs. what is out-of-scope
- **Resources**: Budget, personnel, facilities, timeline
- **Dependencies**: Prerequisite work, external partnerships
- **Exit criteria**: Conditions for prototype completion or termination

### 2.3 Risk Assessment
Evaluate each prototype on:
- **Technical risk**: Likelihood of failure and impact
- **Schedule risk**: Critical path implications
- **Cost risk**: Budget overrun probability
- **Opportunity cost**: Value of alternative investments

## 3. Prioritization Framework

### 3.1 Scoring Matrix

| Category                      | Score 1-5 | Weight |
|-------------------------------|-----------|--------|
| **Safety Impact**             |           | 40%    |
| - Catastrophic failure mode   | 5         |        |
| - Hazardous failure mode      | 4         |        |
| - Major failure mode          | 3         |        |
| - Minor failure mode          | 2         |        |
| - No significant safety impact| 1         |        |
| **Technical Novelty**         |           | 30%    |
| - No heritage, high uncertainty| 5        |        |
| - Limited heritage            | 4         |        |
| - Some heritage, new application| 3       |        |
| - Proven technology, new context| 2       |        |
| - Mature, proven technology   | 1         |        |
| **Regulatory Criticality**    |           | 20%    |
| - Certification prerequisite  | 5         |        |
| - Major certification evidence| 4         |        |
| - Supporting evidence         | 3         |        |
| - Informational only          | 2         |        |
| - Non-regulatory              | 1         |        |
| **Schedule Criticality**      |           | 10%    |
| - On critical path            | 5         |        |
| - Near critical path          | 4         |        |
| - Important milestone         | 3         |        |
| - Flexible timing             | 2         |        |
| - Non-time-sensitive          | 1         |        |

**Total Priority Score** = Σ (Category Score × Weight)

### 3.2 Decision Thresholds
- **Score ≥ 4.0**: Must-do, highest priority
- **Score 3.0-3.9**: Should-do, schedule as resources allow
- **Score 2.0-2.9**: Could-do, opportunistic
- **Score < 2.0**: Defer or cancel

## 4. Prototype Roadmap

### 4.1 Near-Term (0-12 months)
Focus on:
- Safety-critical interfaces (H2 refueling, CO₂ battery)
- Regulatory prerequisite validations
- Long-lead prototypes (e.g., cryogenic test rigs)

### 4.2 Mid-Term (12-24 months)
- Pilot deployments at partner airports
- Integrated interface testing (multiple GSE types)
- Digital twin HIL validation

### 4.3 Long-Term (24+ months)
- Pre-production validation
- Certification readiness demonstrations
- Scalability and cost-reduction prototypes

## 5. Resource Allocation

### 5.1 Budget
- **High-priority prototypes**: 70% of budget
- **Medium-priority prototypes**: 20% of budget
- **Exploratory/opportunistic**: 10% of budget

### 5.2 Personnel
- Assign dedicated prototype leads for high-priority items
- Cross-functional teams (engineering, safety, operations)
- External partners (airports, suppliers, academia)

### 5.3 Facilities
- On-site testbeds and labs
- Partner airport facilities for field trials
- Digital twin compute infrastructure

## 6. Approval and Review

### 6.1 Initial Approval
- **Low-risk prototypes (score < 3.0)**: Department manager approval
- **Medium-risk prototypes (score 3.0-3.9)**: Prototype Review Board approval
- **High-risk prototypes (score ≥ 4.0)**: Executive review and approval

### 6.2 Ongoing Reviews
- **Monthly**: Progress review for active prototypes
- **Quarterly**: Roadmap refresh and re-prioritization
- **Stage gates**: Go/No-Go decision at each TRL transition

## 7. Lessons Learned Process

After prototype completion:
1. **Debrief**: What worked, what didn't, unexpected findings
2. **Documentation**: Update [Lessons Learned](./85-00-08-005_Lessons_Learned_and_Feedback_Loop.md)
3. **Traceability**: Feed findings back to [Requirements](../85-00-03_Requirements/README.md) and [Design](../85-00-04_Design/README.md)
4. **Knowledge sharing**: Presentations, reports, and best practices dissemination

## 8. Example: H2 Refueling Prototype Prioritization

| Criterion                | Score | Justification                                              |
|--------------------------|-------|------------------------------------------------------------|
| Safety Impact            | 5     | Catastrophic failure mode (fire/explosion)                 |
| Technical Novelty        | 5     | No heritage in commercial aviation LH2 refueling           |
| Regulatory Criticality   | 5     | Certification prerequisite per [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) |
| Schedule Criticality     | 4     | Near critical path (EIS dependency)                        |
| **Weighted Total**       | **4.8** | **Must-do, highest priority**                            |

## 9. Traceability

Links to:
- [85-00-08-001 Prototyping Strategy](./85-00-08-001_Prototyping_Strategy.md) – Overall strategy
- [85-00-08-MASTER-002 Prototyping Roadmap](./MASTER/85-00-08-MASTER-002_Prototyping_Roadmap.md) – Consolidated roadmap
- [85-00-02 Safety](../85-00-02_Safety/README.md) – Safety-driven prototype needs

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---
