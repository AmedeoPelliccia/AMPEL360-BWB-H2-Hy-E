
# 02-40-11-010 — Testing Strategy

## Purpose

This document defines the **testing strategy** for the `02-40-11_EFB_Software` subsystem of AMPEL360.

It describes:

- The **test levels**, **test types** and **coverage expectations** for the EFB application.
- How testing activities support **DO-178C objectives** (for applicable software levels).
- The integration of EFB tests within the **global AMPEL360 CI/CD toolchain**.
- How tests, results and coverage are **traced back** to requirements and design artefacts.

This strategy is the EFB-specific view and complements the programme-wide guidance under:

- `02-40-42_Testing_QA/`
- `02-90-12_Certification_Documentation_Schemas/`

---

## Scope

### In Scope

- All software belonging to `02-40-11_EFB_Software`, including:

  - Core EFB app on iOS (Swift/SwiftUI).
  - Shared logic modules under `ASSETS/Source_Code/shared_logic/`.
  - Performance, Weight & Balance, Weather, and Document Viewer modules.
  - Data sync, caching and offline operations that affect operational outputs.

- Testing activities that:

  - Demonstrate conformance with software requirements allocated to 02-40-11.
  - Support DO-178C objectives for the selected software levels (e.g. Level C/D).
  - Are executed in automated pipelines and/or dedicated test rigs.

### Out of Scope

- Detailed test strategy for:

  - Backend services (covered in `02-40-12_Backend_Services/`).
  - Other airborne systems or avionics LRUs.

- Tool qualification details (covered by DO-178C evidence and tool-specific documents).

- NN/ML-specific test strategies beyond the EFB boundary (covered by ATA 95 / predictive services docs).

---

## 1. Testing Principles and Objectives

The EFB testing strategy is based on the following principles:

1. **Requirements-driven verification**

   - Every test case must be linked to at least one requirement (HLR and, where applicable, LLR).
   - No “orphan” tests without traceability.
   - No “orphan” requirements without at least one associated verification method.

2. **Risk-based depth**

   - Higher safety impact components (e.g. performance and W&B modules) receive:
     - Stricter coverage targets.
     - Deeper boundary, robustness and stress testing.
   - UI-only or informational features are tested primarily for correctness and usability.

3. **Early and continuous testing**

   - Testing starts at the unit level and runs continuously in CI.
   - Integration, system and regression suites are triggered on:
     - Feature branch merges.
     - Release candidates.
     - Hotfix branches for certified releases.

4. **Deterministic, reproducible results**

   - Test environments are defined and version-controlled.
   - Test data sets are stable, tagged and reproducible.
   - Deterministic seeds are used for stochastic or randomized tests.

5. **Traceability and auditability**

   - Tests, results and coverage reports are stored in a way that supports:
     - DO-178C audits.
     - Internal SQA audits.
     - Post-incident investigations.

---

## 2. Test Levels

### 2.1 Unit Testing

**Objective:** Verify the correct behaviour of individual functions, classes and small components in isolation.

- Scope:
  - Business logic in `shared_logic/` (e.g. performance calculations, W&B computations).
  - Core UI presentation logic where unit-testable (ViewModels, presenters).
- Characteristics:
  - Executed in memory, no external network calls.
  - Use mocks/stubs for external services and OS APIs.
- Expectations:
  - High coverage (statement/decision), especially for Level C code.
  - Strong focus on boundary conditions, error handling and numerical stability.

### 2.2 Component / Module Testing

**Objective:** Verify behaviour at the level of EFB modules.

- Modules include:
  - Performance module.
  - Weight & Balance module.
  - Weather display module.
  - Document viewer / technical publications integration.
- Characteristics:
  - Test the module through public interfaces or, for UI modules, through ViewModels and navigation flows.
  - Validate that each module conforms to its allocated HLR/LLR and design contracts.

### 2.3 Integration Testing

**Objective:** Validate interactions between EFB modules and external systems.

- Scenarios:
  - EFB ↔ backend API integration (performance data, weather, operational data).
  - EFB ↔ local data stores, caches and configuration.
- Characteristics:
  - Use test doubles for external systems when real services are unavailable.
  - Use “contract tests” to ensure conformance with API specifications defined under:
    - `02-40-12_Backend_Services/`
    - `02-90-02_API_Specifications/`.

### 2.4 System and End-to-End Testing

**Objective:** Validate full user workflows in realistic environments.

- Includes:
  - End-to-end flows for dispatch, performance computation, W&B, and documentation retrieval.
  - Combined online/offline scenarios (pre-flight sync, degraded connectivity).
- Test environments:
  - iOS simulator and physical iPad devices.
  - Representative network conditions (latency, loss, offline).

### 2.5 Non-Functional Testing

**Objective:** Ensure non-functional requirements are met.

- Types:
  - **Performance testing**:
    - Response time for key workflows (e.g. performance calculation).
    - Startup time.
  - **Usability and UX testing**:
    - Information clarity.
    - Error message clarity.
  - **Robustness and reliability**:
    - Behaviour under interruptions, low battery, app suspension/resume.
  - **Security-related testing**:
    - Basic checks for data at rest / in transit as per `02-40-43_Security_Compliance/`.

---

## 3. Test Types and Mapping to DO-178C

### 3.1 Requirements-Based Tests

- Derived directly from EFB HLR/LLR.
- For Level C software:
  - Required to cover all functional behaviour.
- Stored in:
  - `ASSETS/Source_Code/unit_tests/` (unit level).
  - `VERIFICATION/TESTS/` (higher levels, in DO-178C evidence structure).

### 3.2 Structural Coverage Analysis (Level C Components)

- Applied to code that is part of the DO-178C Level C boundary (e.g. performance calculations).
- Objectives:
  - Demonstrate that the requirements-based tests exercise:
    - Statements.
    - Decisions (and, where required, MC/DC).
- Results:
  - Tool reports aggregated into:
    - `ASSETS/Certification/02-40-11-A-502_Test_Coverage_Report.html`.

### 3.3 Boundary, Robustness and Error-Handling Tests

- Focus:
  - Max/min operational ranges (weight, runway length, temperatures, etc.).
  - Invalid inputs, missing data, and corrupted configuration.
- Objective:
  - Demonstrate safe behaviour and proper error messages/logging.

### 3.4 Regression Tests

- Maintain a growing suite of regression tests for:
  - Functionality previously found defective.
  - Critical workflows across releases.
- Trigger:
  - At every merge into main.
  - For every release candidate.

### 3.5 Exploratory and UX Tests

- Structured exploratory sessions for:
  - Edge scenarios not easily expressed as automated tests.
  - Usability / crew workload considerations.
- Evidence:
  - Session notes and defect reports stored under:
    - `VERIFICATION/REVIEWS/`.

---

## 4. Test Environments and Tooling

### 4.1 Environment Types

1. **Developer local environment**
   - Xcode, unit tests, and local simulators.
2. **CI environment**
   - Automated execution of unit, component and selected integration tests.
   - Generating artefacts for DO-178C evidence (test logs, coverage).
3. **Staging / pre-production**
   - Close to operational configuration.
   - Used for system, end-to-end and performance tests.
4. **Device test labs**
   - Physical iPad devices, different OS versions, form factors.

### 4.2 Tooling

- Build and test orchestrated via:
  - `.github/workflows/` under `02-40-41_DevOps_Infrastructure/`.
- Static analysis and coverage tools:
  - Defined and configured in:
    - `02-40-42_Testing_QA/` and DO-178C evidence tooling sections.
- Test results:
  - Persisted as versioned CI artefacts and synced to `VERIFICATION/RESULTS/` for baselined versions.

---

## 5. Test Data Strategy

### 5.1 Test Data Sources

- **Synthetic data**
  - Designed cases for coverage of:
    - Extreme weights and CG combinations.
    - Short/contaminated runway cases.
    - Edge weather conditions.
- **Derived operational scenarios**
  - Anonymised and aggregated from operational data sources where available.
  - Must respect privacy and data protection constraints (GDPR, etc.).

### 5.2 Test Data Management

- Test data stored under:
  - `VERIFICATION/TEST_DATA/` (EFB-specific).
  - Cross-referenced test datasets from:
    - `02-20_Subsystems/` (turnaround, FPL, predictive ops) when relevant.
- Each dataset:
  - Versioned and labelled.
  - Linked to:
    - Test cases using it.
    - Requirements it helps to verify.

### 5.3 DPP and Audit Trail

- For releases used in certification campaigns:
  - Test data hashes and provenance recorded under:
    - `DPP_Links/` and `TRACEABILITY/`.
- Supports:
  - Reproduction of test campaigns.
  - Long-term auditability.

---

## 6. CI/CD Integration and Automation

### 6.1 Pipeline Stages

Typical EFB CI pipeline stages:

1. **Build & static checks**
   - Compilation, linters, formatting, basic static analysis.
2. **Unit test stage**
   - Run unit tests with coverage collection.
3. **Component/integration tests**
   - Selected sets runnable in CI (API mocks, local databases).
4. **UI / snapshot tests (where applicable)**
   - Visual regression tests for critical screens.
5. **Packaging & signing**
   - For internal distribution, test flight or MDM.
6. **Publishing of reports**
   - Coverage, test results and quality gates.

### 6.2 Quality Gates

- Merge into main requires:
  - All mandatory tests passing.
  - Coverage thresholds met for Level C components.
  - No critical or high-severity static analysis findings outstanding (or formally justified).
- Release candidate requires:
  - Full regression suite executed.
  - Non-functional KPIs (performance, startup time) within defined limits.

---

## 7. Defect Management and Regression

### 7.1 Defect Lifecycle

- Defects identified via:
  - Automated tests.
  - Manual/exploratory testing.
  - Operational feedback.
- Lifecycle:
  - Log → triage → root cause analysis → fix → verification → closure.
- Metrics:
  - Open vs closed defects.
  - Mean time to resolution.
  - Defect density per module / release.

### 7.2 Regression Policy

- Every defect of Level C significance or above must:
  - Have at least one dedicated regression test.
  - Be added to the relevant regression test suite.
- Regression suites:
  - Executed automatically on main and for releases.

---

## 8. Traceability and Reporting

### 8.1 Requirements Traceability

- Each test case captures:
  - Requirement IDs (HLR and LLR).
  - Module / component under test.
  - Test data set identifier.

- The RTM (Requirements Traceability Matrix) under DO-178C evidence:
  - Includes EFB-specific test coverage mapping.

### 8.2 Test Reports and Dashboards

- Periodic and release-based reports include:
  - Test execution summary.
  - Pass/fail statistics.
  - Coverage metrics.
  - Outstanding defect list.

- Stored in:
  - `VERIFICATION/REPORTS/` and surfaced via:
    - `02-40-42_Testing_QA/` dashboards where applicable.

---

## 9. Open Items and Next Steps

The following items are intentionally left to be refined as the EFB programme matures:

1. Final definition of minimum coverage thresholds per module and software level.
2. Detailed linkage between:
   - `02-40-11-010_Testing_Strategy.md` and
   - `02-40-11-009_DO_178C_Evidence.md` objective coverage mapping.
3. Alignment of test case schemas with:
   - `02-90-12-A-002_Test_Case_Schema.json`.
4. Detailed performance and robustness KPI definitions (numeric thresholds, tolerances).
5. Formalisation of exploratory testing protocols and reporting templates.

---

## References

- [02-40-11 EFB Software README](README.md)  
- [02-40-00-001 Software Architecture Overview](../02-40-00-001_Software_Architecture_Overview.md)  
- [02-40-00-004 Software Development Standards](../02-40-00-004_Software_Development_Standards.md)  

Related:

- `../02-40-11-001_EFB_App_Architecture.md`  
- `../02-40-11-009_DO_178C_Evidence.md`  
- `../02-40-42_Testing_QA/README.md`  
- `../../02-90-12_Certification_Documentation_Schemas/README.md`  

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot / ChatGPT), prompted by Amedeo Pelliccia**.  
- **Status**: DRAFT – Initial EFB testing strategy definition.  
- **Human approver**: _[to be completed]_.  
- **Repository**: `AMPEL360-BWB-H2-Hy-E`  
- **Last AI update**: _2025-11-21_.  

---

**End of Document**
```

