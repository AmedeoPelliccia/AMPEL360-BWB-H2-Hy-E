# Baseline Document Template

## Document Information
- **Document ID**: 10-00-11-[NN]A
- **Title**: [Baseline Title]
- **Version**: [MAJOR.MINOR.PATCH]
- **Date**: [YYYY-MM-DD]
- **Status**: [DRAFT | IN_REVIEW | APPROVED | RELEASED]
- **Document Type**: baseline
- **Baseline Type**: [FBL | ABL | PBL | H2BL | BWBBL | EISBL]
- **Milestone**: [PDR | CDR | TRR | FAI | EIS]
- **H2 Related**: [true | false]
- **Cryo Related**: [true | false]
- **BWB Specific**: [true | false]

## Purpose

[State the purpose of this baseline document. What configuration snapshot does it represent?]

## Scope

This baseline covers:
- [List primary scope items]
- [Systems included]
- [Subsystems included]
- [Interfaces included]

## Baseline Establishment

### Baseline Criteria

The baseline is established when:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]
- [CCB approval obtained]

### Baseline Date

- **Target [Milestone] Date**: [YYYY-MM-DD or TBD]
- **Baseline Freeze Date**: [YYYY-MM-DD or TBD]
- **CCB Approval**: [Date or Pending]

## Configuration Items

The following Configuration Items are included in this baseline:

| CI ID | Description | Version | Status | Notes |
|-------|-------------|---------|--------|-------|
| CI-10-XXX-001 | [Description] | [X.Y.Z] | [Status] | [Notes] |
| CI-10-XXX-002 | [Description] | [X.Y.Z] | [Status] | [Notes] |

## Requirements Baseline

[List or reference the requirements that are baselined]

### Requirements Summary

- Total Requirements: [Number]
- Functional: [Number]
- Performance: [Number]
- Interface: [Number]
- Safety: [Number]

### Requirements Traceability

Traceability matrix maintained in: `[Path to traceability matrix]`

## Interface Baseline

### External Interfaces

- **ATA [XX]**: [Interface description] - ICD-10-ATA[XX] v[X.Y.Z]
- **ATA [YY]**: [Interface description] - ICD-10-ATA[YY] v[X.Y.Z]

### Ground System Interfaces

- [Interface 1]: [Description] - [Document reference]
- [Interface 2]: [Description] - [Document reference]

## Design Baseline

[For ABL and PBL: Include design configuration details]

### Architecture

[Brief architecture description or reference]

### Key Design Parameters

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| [Parameter 1] | [Value] | [Unit] | [Notes] |
| [Parameter 2] | [Value] | [Unit] | [Notes] |

## Safety Baseline

### Safety Assessment Status

- **FHA**: [Complete | In Progress | Not Started]
- **PSSA/SSA**: [Complete | In Progress | Not Started]
- **FMEA**: [Complete | In Progress | Not Started]

### Identified Hazards

| Hazard ID | Description | Severity | Status |
|-----------|-------------|----------|--------|
| H-10-[XXX] | [Description] | [Severity] | [Status] |

Safety assessment document: `[Path to safety document]`

## Verification Baseline

### Verification Methods

| Method | Count | Notes |
|--------|-------|-------|
| Analysis | [N] | [Notes] |
| Test | [N] | [Notes] |
| Inspection | [N] | [Notes] |
| Demonstration | [N] | [Notes] |

Verification Plan: `[Path to verification plan]`

## H2 System Considerations

[If H2 Related = true]

### H2 Configuration

- [H2 system element 1]
- [H2 system element 2]

### H2 Safety Notes

- [Safety note 1]
- [Safety note 2]

### H2 Certification Status

- [Status note]

## BWB Configuration Considerations

[If BWB Specific = true]

### BWB Design Elements

- [Design element 1]
- [Design element 2]

### BWB-Specific Requirements

- [Requirement 1]
- [Requirement 2]

## Baseline Change Control

### Change Authority

- **Pre-Baseline Freeze**: [Role/authority]
- **Post-Baseline Freeze**: CCB approval required

### Change Impact Assessment

All changes after baseline freeze require:
- [Impact type 1] analysis
- [Impact type 2] assessment
- CCB review and approval

### Emergency Changes

Emergency changes for safety issues:
- Immediate implementation permitted with [authority] approval
- Post-implementation CCB review within [N] working days
- Documentation update within [N] working days

## Compatibility and Effectivity

### Version Compatibility

| Aircraft Version | Baseline Version | Notes |
|------------------|------------------|-------|
| v[X.Y.Z] | [Baseline] v[X.Y.Z] | [Notes] |

### Effectivity

This baseline applies to:
- [Effectivity item 1]
- [Effectivity item 2]

## Known Limitations and Open Issues

### Open Issues

1. **[ID]**: [Description] - [Status]
2. **[ID]**: [Description] - [Status]

### Assumptions

- [Assumption 1]
- [Assumption 2]

### Constraints

- [Constraint 1]
- [Constraint 2]

## Standards and References

### Applicable Standards

- **[Standard 1]**: [Title/description]
- **[Standard 2]**: [Title/description]

### Related Documents

- [Document ID]: [Title]
- [Document ID]: [Title]

## Approval Record

- **Prepared By**: [Name/role]
- **Technical Review**: [Name/role and date or Pending]
- **Safety Review**: [Name/role and date or Pending]
- **CCB Approval**: [Date or Pending]
- **[Milestone] Approval**: [Date or Pending]

## Document Control

- **Author**: [Author name/team]
- **Reviewer**: [To be assigned or name]
- **Approver**: [To be assigned or name]
- **Next Review**: [Date or milestone]
- **Revision History**:
  - Rev A (v1.0.0) - [YYYY-MM-DD] - Initial release
  - Rev B (v1.1.0) - [YYYY-MM-DD] - [Change description]

---

**END OF DOCUMENT**

---

## Template Usage Instructions

1. **Copy this template** to create a new baseline document
2. **Replace all [placeholders]** with actual values
3. **Delete unused sections** (e.g., if not H2 related, remove H2 section)
4. **Follow naming convention**: 10-00-11-[NN]A_[Description].md
5. **Update metadata** in eis-metadata.schema.json format if using JSON metadata
6. **Obtain approvals** before changing status from DRAFT to RELEASED
7. **Update cross-references** in related documents
8. **Add to 00_INDEX.md** in the parent directory

## Baseline Numbering Guide

| Range | Baseline Type |
|-------|---------------|
| 10-19 | Configuration Baselines |
| 20-29 | Milestone Baselines |

## Status Workflow

DRAFT → IN_REVIEW → APPROVED → RELEASED → [SUPERSEDED] → [OBSOLETE]
