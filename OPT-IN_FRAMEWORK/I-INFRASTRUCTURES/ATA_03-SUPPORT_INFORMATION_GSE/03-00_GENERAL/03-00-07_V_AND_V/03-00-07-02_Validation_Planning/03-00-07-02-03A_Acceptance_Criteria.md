---
Title: "Acceptance Criteria — ATA 03 V&V"
Identifier: "AMPEL360-03-00-07-02-03A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 V&V Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Comprehensive acceptance criteria for ATA 03 GSE systems defining pass/fail thresholds and operational readiness standards."
Keywords: ["ATA 03","Acceptance Criteria","Validation","GSE","Standards"]
Compliance:
  - "ARP4754A"
  - "AS9100"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentValidationPlanning: "./"
  Siblings:
    - "./03-00-07-02-01A_Validation_Strategy.md"
    - "./03-00-07-02-02A_Validation_Matrix.md"
    - "./03-00-07-02-04A_Customer_Requirements_Trace.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 V&V Team", change: "Initial acceptance criteria" }
---

# 03-00-07-02-03A - Acceptance Criteria

## 1. Purpose

This document establishes comprehensive **Acceptance Criteria** for [ATA Chapter 03](https://www.ata.org/resources/specifications) — Support Information and Ground Support Equipment (GSE). It defines objective, measurable criteria that must be met for systems to be accepted for operational deployment.

## 2. Scope

### 2.1 Coverage

Acceptance criteria cover:

1. **Performance Criteria**: Quantitative performance thresholds
2. **Safety Criteria**: Safety system functionality and reliability
3. **Operational Criteria**: Operational suitability and usability
4. **Quality Criteria**: Quality and reliability standards
5. **Documentation Criteria**: Documentation completeness and accuracy

## 3. Applicable Documents

### 3.1 Standards

| Document | Application |
|----------|-------------|
| [ARP4754A](https://www.sae.org/standards/content/arp4754a/) | System acceptance standards |
| [AS9100](https://www.sae.org/standards/content/as9100d/) | Quality acceptance requirements |
| [ISO 19880-8](https://www.iso.org/standard/71940.html) | H₂ system acceptance criteria |

### 3.2 Internal References

- [03-00-07-02-01A Validation Strategy](./03-00-07-02-01A_Validation_Strategy.md)
- [03-00-07-02-02A Validation Matrix](./03-00-07-02-02A_Validation_Matrix.md)
- [03-00-03 Requirements](../../03-00-03_Requirements/)

## 4. Description

### 4.1 Overview

Acceptance criteria are:
- **Objective**: Measurable and unambiguous
- **Complete**: Cover all critical aspects
- **Traceable**: Linked to requirements
- **Agreed**: Approved by all stakeholders

### 4.2 Requirements

**AC-03-07-01**: All acceptance criteria shall be objective and measurable.

**AC-03-07-02**: Acceptance criteria shall be approved by customers before validation.

**AC-03-07-03**: All criteria must be met before operational acceptance.

**AC-03-07-04**: Deviations require formal waiver process with customer approval.

### 4.3 Methodology

Acceptance determined through:
- **Performance Testing**: Measurement against specifications
- **Operational Demonstrations**: Real-world scenario execution
- **Documentation Review**: Completeness and accuracy verification
- **Stakeholder Sign-Off**: Formal customer acceptance

## 5. Test/Verification Matrix

### 5.1 H₂ Refuelling System Acceptance Criteria

| Criterion | Specification | Measurement Method | Pass/Fail Threshold |
|-----------|--------------|-------------------|-------------------|
| Flow Rate | 100-500 kg/h | Flow meter | ±5% of target |
| Fill Time | < 20 minutes | Timing | < 20 min for full tank |
| Pressure Control | 350 bar ±10 bar | Pressure transducer | Within spec range |
| Leak Rate | < 1×10⁻⁴ mbar·L/s | Leak detector | Below threshold |
| Emergency Shutdown Time | < 2 seconds | Timer | < 2s from signal |
| Temperature Monitoring | -253°C to +50°C | Thermocouples | ±2°C accuracy |
| Safety System Response | Per ISO 19880-8 | Functional test | 100% functionality |
| Operator Training Time | < 8 hours | Training records | 100% pass rate |

### 5.2 Electrical Ground Power Unit Acceptance Criteria

| Criterion | Specification | Measurement Method | Pass/Fail Threshold |
|-----------|--------------|-------------------|-------------------|
| Output Voltage | 115V AC ±3% | Power analyzer | 111.6 - 118.5V |
| Frequency | 400 Hz ±0.5% | Frequency counter | 398 - 402 Hz |
| Power Capacity | 90 kVA continuous | Load bank test | ≥90 kVA for 2 hrs |
| Voltage Transient | < 10% deviation | Transient recorder | < 11.5V deviation |
| Ground Fault Protection | < 50ms trip time | Protection test | < 50ms |
| EMI/EMC | DO-160G Cat M | EMC chamber test | Pass per standard |
| Reliability | > 99.5% | MTBF calculation | > 99.5% availability |

### 5.3 Maintenance Platform Acceptance Criteria

| Criterion | Specification | Measurement Method | Pass/Fail Threshold |
|-----------|--------------|-------------------|-------------------|
| Load Capacity | 300 kg per platform | Load test | ≥300 kg with 1.5× factor |
| Stability | < 2° tilt under load | Inclinometer | < 2° at max load |
| Safety Rail Height | 1.1m minimum | Measurement | ≥1.1m all positions |
| Non-Slip Surface | Coefficient > 0.5 | Slip meter | > 0.5 wet and dry |
| Emergency Descent | < 30 seconds | Timing | < 30s to ground level |
| Access Coverage | All service panels | Physical verification | 100% panel access |
| Setup Time | < 10 minutes | Timing | < 10 min by single operator |

### 5.4 Digital Systems Acceptance Criteria

| Criterion | Specification | Measurement Method | Pass/Fail Threshold |
|-----------|--------------|-------------------|-------------------|
| Data Link Latency | < 100ms | Network analyzer | < 100ms 99th percentile |
| Data Integrity | CRC-32 validation | Test data transfers | 100% integrity |
| Cybersecurity | DO-326A compliance | Security audit | Pass all requirements |
| User Authentication | Required for all ops | Security test | 100% enforcement |
| Software Reliability | DO-178C DAL C | Code analysis + test | Pass all objectives |
| Interface Compatibility | ARINC 615A | Interface test | 100% message compliance |

### 5.5 Operational Acceptance Criteria

| Criterion | Specification | Measurement Method | Pass/Fail Threshold |
|-----------|--------------|-------------------|-------------------|
| Turnaround Time | < 45 minutes | Full operation timing | < 45 min average |
| Operator Training | < 8 hours initial | Training records | 100% pass < 8 hrs |
| Maintenance Task Time | < 4 hours/month | Task timing | < 4 hrs preventive |
| System Availability | > 99.5% | Reliability data | > 99.5% over trial period |
| Safety Incidents | Zero during trials | Incident reports | Zero incidents |
| User Satisfaction | > 80% satisfied | Survey | ≥80% positive feedback |

### 5.6 Documentation Acceptance Criteria

| Document Type | Completeness Standard | Review Method | Pass/Fail Threshold |
|--------------|---------------------|--------------|-------------------|
| Operations Manual | All procedures documented | Review + checklist | 100% procedures complete |
| Maintenance Manual | All tasks documented | Review + SME validation | 100% tasks complete |
| Training Materials | Complete curriculum | Review + pilot training | Effective training delivery |
| Safety Documentation | All hazards addressed | Safety review | 100% hazards mitigated |
| Certification Evidence | Complete per TCDS | Regulatory review | Authority acceptance |
| Interface Documentation | All interfaces defined | Review + test | 100% interfaces documented |

## 6. Acceptance Criteria

### 6.1 System Acceptance Gates

**Gate 1: Design Acceptance**
- ✓ All design reviews completed
- ✓ Design meets requirements
- ✓ Safety analysis approved
- ✓ Preliminary design validation complete

**Gate 2: Pre-Production Acceptance**
- ✓ Prototype testing complete
- ✓ All acceptance criteria met
- ✓ Production readiness verified
- ✓ Documentation 80% complete

**Gate 3: Operational Acceptance**
- ✓ Field trials successful
- ✓ All criteria met or waived
- ✓ Training program validated
- ✓ Customer acceptance obtained

**Gate 4: Final Acceptance**
- ✓ All documentation complete
- ✓ Certification obtained
- ✓ Customer sign-off received
- ✓ Operational readiness confirmed

### 6.2 Waiver Process

If acceptance criteria cannot be met:
1. **Document**: Detailed description of non-conformance
2. **Analyze**: Root cause and impact assessment
3. **Propose**: Corrective action or waiver justification
4. **Review**: Engineering and safety review
5. **Approve**: Customer and regulatory approval required

## 7. Cross-References

### 7.1 Related ATA Chapters

- [ATA 02](../../../ATA_02-OPERATIONS_INFORMATION/) — Operational acceptance
- [ATA 05](../../../ATA_05-TIME_LIMITS_MAINTENANCE_CHECKS/) — Maintenance acceptance

### 7.2 Parent Document

- [03-00-07-02 Validation Planning](./) — Validation Planning Overview

### 7.3 Related Engineering Documents

- [03-00-03 Requirements](../../03-00-03_Requirements/) — Requirements source
- [03-00-07-02-02A Validation Matrix](./03-00-07-02-02A_Validation_Matrix.md) — Validation traceability
- [03-00-10 Certification](../../03-00-10_Certification/) — Certification acceptance

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 V&V Team | Initial release |

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07.

---
