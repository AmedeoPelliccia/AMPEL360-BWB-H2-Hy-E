# RQ-95-00-03-601 — DPP Changes SHALL Require CCB Approval

## 1. Requirement Statement

Changes to **approved DPP records** **SHALL** require **Configuration Control Board (CCB) approval** before implementation, ensuring proper change management and impact assessment.

## 2. Rationale

- **Safety assurance**: Uncontrolled changes to DPP data may impact safety assessments
- **Certification integrity**: Changes must be evaluated for certification impact
- **Traceability**: CCB process ensures all changes are documented and justified
- **Regulatory compliance**: Aviation authorities require formal change control
- **Quality management**: Prevents unauthorized or poorly considered changes

DPP changes may affect:
- Safety assessments (ODD, runtime monitoring)
- Certification evidence packages
- Regulatory compliance status
- Operational procedures

All such changes require formal review and approval.

## 3. Category

- **Requirement Type**: Governance & Audit
- **Domain**: Change Control & Configuration Management
- **ATA**: 95-00-03_Requirements

## 4. Source(s)

- **95-00-14_Ops_Std_Sustain/** — Change management framework
- **DO-178C** — Section 7 (Configuration management)
- **AS9100** — Quality management for aerospace
- **EASA Part 21** — Certification procedures for change management

## 5. Acceptance Criteria

- [x] CCB approval process is defined
- [ ] DPP change requests are submitted to CCB
- [ ] CCB reviews changes for safety/certification impact
- [ ] Approved changes are documented with rationale
- [ ] Rejected changes are documented with rationale
- [ ] DPP system enforces CCB approval before changes
- [ ] Audit trail captures all CCB decisions

## 6. Verification Method

- **Method**: Inspection + Analysis
- **Evidence**:
  - CCB meeting minutes showing DPP change reviews
  - DPP change request forms
  - System access controls preventing unauthorized changes
  - Audit trail showing CCB approval before implementation
  - Sample rejected change with documented rationale

## 7. Traceability

- **Design**: 95-00-04-601_CCB_Process_Design.md
- **Implementation**: 
  - DPP change request workflow
  - CCB review procedures
  - Access control enforcement
- **Test**: 
  - TC-95-00-03-601_CCB_Approval_Process
  - TC-95-00-03-601A_Unauthorized_Change_Prevention
- **Certification**: MoC-95-00-03-601

## 8. Status

- **Lifecycle State**: `APPROVED`
- **Owner**: Governance WG / Configuration Management
- **Approval Date**: 2025-11-17
- **Last Updated**: 2025-11-17
- **Comments**: Approved. CCB process is mandatory for all post-deployment DPP changes.

---

## Document Control

- **Document ID**: RQ-95-00-03-601
- **Version**: 1.0
- **Status**: APPROVED
