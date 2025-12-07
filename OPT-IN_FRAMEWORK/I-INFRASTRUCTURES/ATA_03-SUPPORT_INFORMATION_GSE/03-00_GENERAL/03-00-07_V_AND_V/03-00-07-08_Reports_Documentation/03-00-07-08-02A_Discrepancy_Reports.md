---
Title: "Discrepancy Reports — ATA 03 V&V"
Identifier: "AMPEL360-03-00-07-08-02A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 V&V Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Discrepancy reporting procedures for ATA 03 GSE verification and validation non-conformances."
Keywords: ["ATA 03","Discrepancy","Non-Conformance","V&V","GSE","Quality"]
Compliance:
  - "AS9100"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentReportsDocumentation: "./"
---

# 03-00-07-08-02A - Discrepancy Reports

## 1. Purpose

This document defines **Discrepancy Reporting** procedures for ATA Chapter 03 GSE verification and validation activities when test results do not meet requirements.

## 2. Scope

Discrepancy reports document:
- Test failures
- Non-conformances
- Anomalies and deviations
- Root cause analysis
- Corrective actions

## 3. Applicable Documents

| Document | Application |
|----------|-------------|
| [AS9100](https://www.sae.org/standards/content/as9100d/) | Non-conformance management |

## 4. Description

### 4.1 Discrepancy Classification

**Class 1 - Critical**: Safety-critical failure or major non-conformance
**Class 2 - Major**: Significant performance deviation
**Class 3 - Minor**: Minor deviation from specification
**Class 4 - Observation**: Item for attention but not failure

### 4.2 Reporting Process

1. **Identification**: Discrepancy discovered and documented
2. **Classification**: Severity determined
3. **Investigation**: Root cause analysis performed
4. **Disposition**: Corrective action defined
5. **Verification**: Fix verified effective
6. **Closure**: Discrepancy closed with approval

### 4.3 Requirements

**DR-03-07-01**: All discrepancies shall be documented immediately.

**DR-03-07-02**: Critical discrepancies require immediate notification.

**DR-03-07-03**: Root cause analysis required for all Class 1 and 2 discrepancies.

**DR-03-07-04**: Corrective actions shall be verified before closure.

## 5. Test/Verification Matrix

| Discrepancy Type | Response Time | Investigation Level | Approval Level |
|-----------------|---------------|-------------------|---------------|
| Class 1 - Critical | Immediate | Full RCA | Program manager |
| Class 2 - Major | 24 hours | Detailed analysis | Lead engineer |
| Class 3 - Minor | 1 week | Basic analysis | Test lead |
| Class 4 - Observation | As scheduled | Review | Test engineer |

## 6. Acceptance Criteria

- ✓ All discrepancies documented
- ✓ Root cause identified
- ✓ Corrective action implemented
- ✓ Verification completed
- ✓ Formal closure approved

## 7. Cross-References

- [03-00-07-08-01A Test Report Template](./03-00-07-08-01A_Test_Report_Template.md)
- [03-00-07-08-03A Verification Closure](./03-00-07-08-03A_Verification_Closure.md)

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
