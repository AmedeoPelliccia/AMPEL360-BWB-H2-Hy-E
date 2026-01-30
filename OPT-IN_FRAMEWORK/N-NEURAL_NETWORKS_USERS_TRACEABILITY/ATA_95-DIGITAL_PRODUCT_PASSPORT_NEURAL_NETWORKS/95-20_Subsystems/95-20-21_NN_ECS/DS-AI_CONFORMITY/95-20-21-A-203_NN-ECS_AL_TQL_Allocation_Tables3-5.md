# 95-20-21-A-203 — NN-ECS AL/TQL Allocation (DS.AI Tables 3-5)

**Document ID**: 95-20-21-A-203  
**Version**: 0.1  
**Status**: DRAFT  
**DS.AI Section**: DS.AI Tables 3, 4, 5

## 1. Objective

Document the Assurance Level (AL) and Test Quality Level (TQL) allocation for NN-ECS subsystem based on DS.AI Tables 3-5.

## 2. AI System Classification

Per AI Subsystems Register entry NN-ECS:
- **AI Level**: 2A or 2B (AI constituent)
- **Hazard Classification**: H2-H3
- **Safety Component**: YES
- **DS.AI Scope**: IN

## 3. AL/TQL Allocation

### 3.1 Per DS.AI Table 5 (AI Level 2A/2B)

| Hazard Level | AI Level | Assigned AL | Assigned TQL | Rationale |
|--------------|----------|-------------|--------------|-----------|
| H2 | 2A or 2B | AL2-AL3 | TQL2-TQL3 | Hazardous failure conditions require medium-high assurance |
| H3 | 2A | AL3 | TQL3 | Major failure conditions require medium assurance |

### 3.2 Allocation Decision
- **Selected AL**: AL2-AL3 (conservative approach covering both H2 and H3 hazards)
- **Selected TQL**: TQL2-TQL3
- **Justification**: Worst-case H2 hazards drive the allocation

## 4. Assurance Activities per AL2-AL3

TBD - Define specific assurance activities required for AL2-AL3

## 5. Test Quality Requirements per TQL2-TQL3

TBD - Define specific test quality requirements for TQL2-TQL3

## 6. Traceability

- **AI Subsystems Register**: Entry NN-ECS
- **Risk Assessment**: [95-20-21-A-103_NN-ECS_Risk_Assessment_DS-AI-130.md](./95-20-21-A-103_NN-ECS_Risk_Assessment_DS-AI-130.md)
- **Learning Assurance**: [95-20-21-A-106_NN-ECS_Learning_Assurance_DS-AI-150.md](./95-20-21-A-106_NN-ECS_Learning_Assurance_DS-AI-150.md)
- **Related Standards**: DS.AI Tables 3-5

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-23

---
