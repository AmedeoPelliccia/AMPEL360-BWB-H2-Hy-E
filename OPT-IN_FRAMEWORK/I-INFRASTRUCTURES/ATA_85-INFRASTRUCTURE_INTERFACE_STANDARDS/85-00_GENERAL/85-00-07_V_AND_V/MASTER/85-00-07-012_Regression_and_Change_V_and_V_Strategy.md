# 85-00-07-012: Regression and Change V&V Strategy

## 1. Purpose
Establishes the approach for re-verification and re-validation following design changes, ensuring that modifications do not introduce new failures or degrade existing functionality.

## 2. Change Classification
Per [Part 21](https://www.easa.europa.eu/document-library/regulations/commission-regulation-eu-no-7482012) and [AC 21.101-1](https://www.faa.gov/regulations_policies/advisory_circulars):

### 2.1 Minor Change
**Definition**: No appreciable effect on weight, balance, structural strength, reliability, operational characteristics, or other safety-related factors.

**V&V Scope**: Focused regression testing of affected interfaces only.

### 2.2 Major Change
**Definition**: Significant impact on aircraft systems, requiring re-approval by certification authority.

**V&V Scope**: Full regression suite + additional tests for new functionality.

### 2.3 Emergency Change
**Definition**: Immediate safety fix (e.g., airworthiness directive compliance).

**V&V Scope**: Rapid targeted testing with abbreviated documentation (full documentation post-facto).

## 3. Impact Assessment
Before executing regression tests, perform:

### 3.1 Change Impact Analysis (CIA)
- Identify affected requirements ([85-00-03](../../85-00-03_Requirements/README.md))
- Determine impacted interfaces ([85-00-05](../../85-00-05_Interfaces/README.md))
- List modified components and subsystems

### 3.2 Regression Test Selection
- **Risk-Based**: Prioritize tests for high-criticality interfaces
- **Dependency-Driven**: Include tests for downstream dependencies
- **Historical**: Analyze previous defect patterns

## 4. Regression Test Automation
### 4.1 Automated Test Suite
Maintained in CI/CD pipeline (Jenkins, GitLab CI):
- **Unit Tests**: Nightly execution
- **Integration Tests**: Weekly execution
- **Smoke Tests**: Pre-release execution

### 4.2 Test Coverage Monitoring
Track regression test coverage against baseline:
- **Baseline**: Test suite from previous certification milestone
- **Delta**: New tests added for changed functionality
- **Obsolete**: Tests retired due to design evolution

## 5. Retest Criteria
Re-execute tests when:
- Source code or design documents change
- Test procedures updated
- Test environment modified (hardware, software, calibration)
- Defect fix implemented

## 6. Configuration Management
### 6.1 Baseline Management
- **Frozen Baseline**: Reference configuration for regression comparisons
- **Working Baseline**: Current development configuration
- **Released Baseline**: Certified configuration per [85-00-11 EIS Versions](../../85-00-11_EIS_Versions_Tags/README.md)

### 6.2 Traceability
Link each change to:
- Change request (CR) / Engineering change order (ECO)
- Updated requirements
- Regression test results
- Certification authority concurrence (if major change)

## 7. Regression Test Reporting
For each regression cycle, produce:
- **Regression Test Report**: Summary of tests executed, pass/fail status
- **Defect Log**: New defects discovered, root cause analysis
- **Compliance Statement**: Confirmation that changes do not invalidate previous certification

## 8. Tools and Infrastructure
- **Version Control**: Git (this repository)
- **Test Automation**: Jenkins, GitLab CI, Selenium (for digital interfaces)
- **Defect Tracking**: Jira, Azure DevOps, or equivalent
- **Traceability**: IBM DOORS, Jama Connect

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---
