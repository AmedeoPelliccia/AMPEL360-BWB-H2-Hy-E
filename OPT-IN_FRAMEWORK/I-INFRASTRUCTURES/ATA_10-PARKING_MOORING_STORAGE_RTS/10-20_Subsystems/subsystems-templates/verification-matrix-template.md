# Verification Matrix Template

## 1. Document Information

| Field | Value |
|-------|-------|
| Document Number | VM-10-20-NNA |
| Title | [Subsystem Name] Verification Matrix |
| Revision | A |
| Date | YYYY-MM-DD |
| Status | [DRAFT / ACTIVE] |
| Related Specification | 10-20-NNA |

## 2. Purpose

This verification matrix provides traceability between requirements and verification activities for the [Subsystem Name].

## 3. Verification Methods

| Code | Method | Description |
|------|--------|-------------|
| T | Test | Physical testing of component or system |
| A | Analysis | Engineering analysis (calculation, simulation, modeling) |
| I | Inspection | Visual or measurement inspection |
| D | Demonstration | Functional demonstration |
| S | Similarity | Verification by similarity to previously verified design |

## 4. Verification Status Codes

| Code | Status | Description |
|------|--------|-------------|
| P | Planned | Verification activity planned but not started |
| IP | In Progress | Verification activity in progress |
| C | Complete | Verification successfully completed |
| F | Failed | Verification failed, corrective action required |
| N/A | Not Applicable | Requirement not applicable for current configuration |

## 5. Functional Requirements Verification

| Req ID | Requirement Summary | Priority | Verification Method | Test/Analysis Reference | Status | Evidence | Notes |
|--------|-------------------|----------|---------------------|------------------------|--------|----------|-------|
| FR-10-20-NN-001 | [Requirement summary] | High | T | TEST-10-20-NN-001 | [P/IP/C/F] | [Evidence ref] | [Notes] |
| FR-10-20-NN-002 | [Requirement summary] | High | A | ANAL-10-20-NN-001 | [P/IP/C/F] | [Evidence ref] | [Notes] |
| FR-10-20-NN-003 | [Requirement summary] | Medium | I | INSP-10-20-NN-001 | [P/IP/C/F] | [Evidence ref] | [Notes] |
| FR-10-20-NN-004 | [Requirement summary] | Medium | D | DEMO-10-20-NN-001 | [P/IP/C/F] | [Evidence ref] | [Notes] |

## 6. Performance Requirements Verification

| Req ID | Parameter | Specification | Tolerance | Method | Test Reference | Status | Measured Value | Pass/Fail | Notes |
|--------|-----------|---------------|-----------|--------|----------------|--------|----------------|-----------|-------|
| PR-10-20-NN-001 | [Parameter] | [Value] [Unit] | ±[X]% | T | TEST-10-20-NN-002 | [Status] | [Value] | [P/F] | [Notes] |
| PR-10-20-NN-002 | [Parameter] | [Value] [Unit] | ±[X]% | T | TEST-10-20-NN-003 | [Status] | [Value] | [P/F] | [Notes] |

## 7. Safety Requirements Verification

| Req ID | Safety Requirement | DAL | Severity | Method | Test Reference | Status | Evidence | Notes |
|--------|-------------------|-----|----------|--------|----------------|--------|----------|-------|
| SR-10-20-NN-001 | [Safety requirement] | A | Catastrophic | T+A | TEST-10-20-NN-004, ANAL-10-20-NN-002 | [Status] | [Evidence] | [Notes] |
| SR-10-20-NN-002 | [Safety requirement] | B | Hazardous | T | TEST-10-20-NN-005 | [Status] | [Evidence] | [Notes] |

## 8. Interface Requirements Verification

| Req ID | Interface | Connected System | Method | Test Reference | Status | Evidence | Notes |
|--------|-----------|------------------|--------|----------------|--------|----------|-------|
| IR-10-20-NN-001 | [Interface] | [System] | T | TEST-10-20-NN-006 | [Status] | [Evidence] | [Notes] |
| IR-10-20-NN-002 | [Interface] | [System] | I | INSP-10-20-NN-002 | [Status] | [Evidence] | [Notes] |

## 9. Environmental Requirements Verification

| Req ID | Environmental Condition | Specification | Method | Test Reference | Status | Result | Pass/Fail | Notes |
|--------|------------------------|---------------|--------|----------------|--------|--------|-----------|-------|
| ER-10-20-NN-001 | Operating Temp Range | [Min to Max]°C | T | TEST-10-20-NN-007 | [Status] | [Result] | [P/F] | [Notes] |
| ER-10-20-NN-002 | Humidity | [Max]% RH | T | TEST-10-20-NN-008 | [Status] | [Result] | [P/F] | [Notes] |
| ER-10-20-NN-003 | Vibration | [Spec] | T | TEST-10-20-NN-009 | [Status] | [Result] | [P/F] | [Notes] |

## 10. H2/Cryogenic Requirements Verification (if applicable)

| Req ID | H2/Cryo Requirement | Method | Test Reference | Status | Evidence | Notes |
|--------|---------------------|--------|----------------|--------|----------|-------|
| H2-10-20-NN-001 | [H2 requirement] | T | TEST-10-20-NN-010 | [Status] | [Evidence] | [Notes] |
| CR-10-20-NN-001 | [Cryo requirement] | T | TEST-10-20-NN-011 | [Status] | [Evidence] | [Notes] |
| CR-10-20-NN-002 | LH2 compatibility at -253°C | T+A | TEST-10-20-NN-012, ANAL-10-20-NN-003 | [Status] | [Evidence] | [Notes] |

## 11. BWB-Specific Requirements Verification (if applicable)

| Req ID | BWB Requirement | Method | Test Reference | Status | Evidence | Notes |
|--------|-----------------|--------|----------------|--------|----------|-------|
| BWB-10-20-NN-001 | [BWB requirement] | T | TEST-10-20-NN-013 | [Status] | [Evidence] | [Notes] |
| BWB-10-20-NN-002 | [BWB requirement] | D | DEMO-10-20-NN-002 | [Status] | [Evidence] | [Notes] |

## 12. Test Campaign Summary

### 12.1 Planned Tests

| Test ID | Test Name | Type | Objective | Planned Date | Duration | Resources |
|---------|-----------|------|-----------|--------------|----------|-----------|
| TEST-10-20-NN-001 | [Test name] | [Type] | [Objective] | [Date] | [Duration] | [Resources] |

### 12.2 Analysis Activities

| Analysis ID | Analysis Name | Tool/Method | Objective | Planned Date | Analyst |
|-------------|---------------|-------------|-----------|--------------|---------|
| ANAL-10-20-NN-001 | [Analysis name] | [Tool] | [Objective] | [Date] | [Name] |

### 12.3 Inspection Activities

| Inspection ID | Inspection Name | Type | Objective | Planned Date | Inspector |
|---------------|----------------|------|-----------|--------------|-----------|
| INSP-10-20-NN-001 | [Inspection name] | [Type] | [Objective] | [Date] | [Name] |

## 13. Verification Completion Summary

### 13.1 Overall Status

| Category | Total Req | Planned | In Progress | Complete | Failed | N/A | % Complete |
|----------|-----------|---------|-------------|----------|--------|-----|------------|
| Functional | [N] | [N] | [N] | [N] | [N] | [N] | [X]% |
| Performance | [N] | [N] | [N] | [N] | [N] | [N] | [X]% |
| Safety | [N] | [N] | [N] | [N] | [N] | [N] | [X]% |
| Interface | [N] | [N] | [N] | [N] | [N] | [N] | [X]% |
| Environmental | [N] | [N] | [N] | [N] | [N] | [N] | [X]% |
| H2/Cryo | [N] | [N] | [N] | [N] | [N] | [N] | [X]% |
| BWB | [N] | [N] | [N] | [N] | [N] | [N] | [X]% |
| **TOTAL** | **[N]** | **[N]** | **[N]** | **[N]** | **[N]** | **[N]** | **[X]%** |

### 13.2 Method Distribution

| Method | Count | Percentage |
|--------|-------|------------|
| Test | [N] | [X]% |
| Analysis | [N] | [X]% |
| Inspection | [N] | [X]% |
| Demonstration | [N] | [X]% |
| Similarity | [N] | [X]% |

## 14. Open Items and Issues

| Issue ID | Description | Impact | Assigned To | Due Date | Status |
|----------|-------------|--------|-------------|----------|--------|
| ISSUE-001 | [Description] | [Impact] | [Name] | [Date] | [Open/Closed] |

## 15. Certification Evidence Package

### 15.1 Test Reports
- [TEST-10-20-NN-001-RPT]: [Test Name Report]
- [TEST-10-20-NN-002-RPT]: [Test Name Report]

### 15.2 Analysis Reports
- [ANAL-10-20-NN-001-RPT]: [Analysis Name Report]
- [ANAL-10-20-NN-002-RPT]: [Analysis Name Report]

### 15.3 Inspection Reports
- [INSP-10-20-NN-001-RPT]: [Inspection Name Report]

### 15.4 Compliance Documentation
- [Standard]: [Compliance Statement Document]

## 16. Traceability

### 16.1 Upstream Traceability
[Link to higher-level requirements or specifications]

### 16.2 Downstream Traceability
[Link to detailed design documents and test procedures]

## 17. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Verification Engineer | [Name] | [Signature] | [Date] |
| Systems Engineer | [Name] | [Signature] | [Date] |
| Safety Engineer | [Name] | [Signature] | [Date] |
| Certification Engineer | [Name] | [Signature] | [Date] |

## 18. Revision History

| Revision | Date | Author | Description |
|----------|------|--------|-------------|
| A | YYYY-MM-DD | [Author] | Initial release |

---

## Document Control

- **Status**: [DRAFT / ACTIVE]
- **Version**: Rev A
- **Generated with assistance from**: AI (GitHub Copilot), prompted by Amedeo Pelliccia
- **Approver**: [To be completed]
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Path**: `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_10-PARKING_MOORING_STORAGE_RTS/10-20_Subsystems/`

---

## Template Usage Instructions

1. Fill in all [bracketed] placeholders with actual project data
2. Update verification status as activities progress
3. Link to actual test procedures and reports
4. Maintain traceability to parent specification document
5. Update completion summary regularly
6. Track and resolve all open issues
7. Obtain required approvals before marking as ACTIVE
8. For H2 systems: Include hydrogen-specific test evidence (SAE AS6968 compliance)
9. For cryo systems: Include cryogenic qualification evidence
10. For BWB systems: Include BWB-specific verification evidence
