# 61-00-05-06-01A - Interface Control Document Template

**Document ID:** 61-00-05-06-01A  
**Title:** Interface Control Document (ICD) Template  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document provides a standard template for Interface Control Documents (ICDs) between the propulsion system (ATA 61) and other aircraft systems.

---

## 2. Scope

This template defines the structure and content requirements for all ATA 61 ICDs, ensuring consistency and completeness across system interfaces.

---

## 3. ICD Template Structure

### 3.1 Cover Page

- **Document Title**: ICD [System A] to [System B]
- **Document Number**: [e.g., ICD-61-XX]
- **Revision**: [Letter]
- **Date**: [YYYY-MM-DD]
- **Prepared by**: [Organization/Team]
- **Approved by**: [Name, Title]

### 3.2 Document Control

| Field | Content |
|-------|---------|
| Classification | Proprietary / Company Confidential |
| Distribution List | [Names/organizations authorized to receive] |
| Change Control | Configuration management board approval required |
| Related Documents | [List of parent/child/peer documents] |

### 3.3 Section 1: Introduction

#### 1.1 Purpose
- Brief statement of ICD purpose
- Scope of interfaces covered

#### 1.2 Scope
- Systems covered (both sides of interface)
- Lifecycle phases addressed (design, integration, test, operations)
- Exclusions (what is NOT covered)

#### 1.3 Applicable Documents
- Standards (industry, regulatory)
- System specifications
- Other ICDs
- Test plans

### 3.4 Section 2: System Overviews

#### 2.1 [System A] Overview
- Brief functional description
- Key components
- Interface responsibilities

#### 2.2 [System B] Overview
- Brief functional description
- Key components
- Interface responsibilities

#### 2.3 Interface Architecture
- Block diagram showing interface points
- Data flow diagrams
- Physical layout diagrams

### 3.5 Section 3: Interface Requirements

#### 3.1 Functional Requirements
| Req ID | Requirement | System A Responsibility | System B Responsibility | Verification |
|--------|-------------|-------------------------|-------------------------|--------------|
| IFR-XXX-001 | [Description] | [What A provides] | [What B provides] | [Method] |

#### 3.2 Performance Requirements
- Timing requirements
- Throughput requirements
- Accuracy requirements
- Reliability requirements

#### 3.3 Environmental Requirements
- Temperature, pressure, humidity
- Vibration, shock
- EMI/EMC

### 3.6 Section 4: Physical Interfaces

#### 4.1 Mechanical Interfaces
| Interface Point | Type | Connector/Fitting | Material | Dimensions | Torque |
|-----------------|------|-------------------|----------|------------|--------|
| [Name] | [Type] | [Spec] | [Material] | [Values] | [Nm] |

#### 4.2 Electrical Interfaces
| Signal/Power | Voltage/Current | Connector | Pin Assignment | Wire Spec |
|--------------|-----------------|-----------|----------------|-----------|
| [Name] | [Values] | [Type] | [Pinout] | [AWG, shield] |

#### 4.3 Fluid Interfaces
| Line | Fluid Type | Pressure | Flow Rate | Temperature | Fitting |
|------|------------|----------|-----------|-------------|---------|
| [Name] | [Type] | [bar] | [L/min] | [°C] | [Spec] |

### 3.7 Section 5: Data Interfaces

#### 5.1 Data Bus Interfaces
| Bus Type | Speed | Protocol | Messages | Update Rate |
|----------|-------|----------|----------|-------------|
| [AFDX/A429/CAN] | [bps] | [Standard] | [List] | [Hz] |

#### 5.2 Message Definitions
- Message ID
- Data fields
- Units and ranges
- Encoding
- Error handling

### 3.8 Section 6: Safety and Certification

#### 6.1 Safety Requirements
- Safety-critical interfaces
- Fault detection and handling
- Redundancy requirements
- Failure modes and effects

#### 6.2 Certification Requirements
- Applicable regulations (CS-25, FAR 25, etc.)
- Certification test requirements
- Documentation requirements

### 3.9 Section 7: Verification and Validation

#### 7.1 Interface Verification Matrix
| Requirement ID | Verification Method | Test Procedure | Acceptance Criteria | Status |
|----------------|---------------------|----------------|---------------------|--------|
| [ID] | [Test/Analysis/Inspection/Demo] | [Ref] | [Criteria] | [P/F] |

#### 7.2 Integration Test Plan
- Test setup
- Test sequence
- Success criteria
- Anomaly resolution process

### 3.10 Section 8: Operations and Maintenance

#### 8.1 Installation Procedures
- Step-by-step installation
- Torque specifications
- Alignment procedures
- Functional checks

#### 8.2 Inspection and Maintenance
- Inspection intervals
- Inspection criteria
- Maintenance procedures
- Troubleshooting guide

### 3.11 Section 9: Appendices

#### Appendix A: Interface Drawings
- Detailed interface drawings
- Cable routing diagrams
- Connector pinouts

#### Appendix B: Test Data
- Qualification test results
- First article inspection data

#### Appendix C: Acronyms and Definitions
- List of acronyms
- Definitions of key terms

---

## 4. ICD Development Process

### 4.1 Responsibilities

| Role | Responsibility |
|------|----------------|
| System A Lead | Define System A interface requirements and capabilities |
| System B Lead | Define System B interface requirements and capabilities |
| Integration Lead | Coordinate ICD development, resolve conflicts |
| Configuration Manager | Control ICD revisions, distribution |

### 4.2 Review and Approval Process

1. **Draft**: Initial ICD draft by integration team
2. **Review**: Technical review by both system teams
3. **Coordination**: Resolve comments and discrepancies
4. **Approval**: Sign-off by both system leads
5. **Baseline**: Configuration control board approval
6. **Distribution**: Controlled distribution to authorized users

### 4.3 Change Control

All changes to baselined ICDs must:
- Be documented in a change request
- Be technically reviewed by both system teams
- Be approved by configuration control board
- Be incorporated in a new ICD revision

---

## 5. Cross-References

### 5.1 Related ICDs
- 61-00-05-06-02A — ICD Propulsion to Avionics
- 61-00-05-06-03A — ICD Propulsion to Fuel System
- 61-00-05-06-04A — ICD Propulsion to Structure

### 5.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

---

## 6. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Parent: 61-00-05_Interfaces](../README.md) · [Next: 61-00-05-06-02A_ICD_Propulsion_to_Avionics](61-00-05-06-02A_ICD_Propulsion_to_Avionics.md) →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Interface Control Documents  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
