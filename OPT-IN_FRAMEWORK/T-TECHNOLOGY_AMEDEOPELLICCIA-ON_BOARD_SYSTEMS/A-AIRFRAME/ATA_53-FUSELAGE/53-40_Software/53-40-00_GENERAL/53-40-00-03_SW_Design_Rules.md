# 53-40-00-03 — Software Design Rules

| Field | Value |
|-------|-------|
| **Document ID** | 53-40-00-03 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | SOFTWARE / DESIGN RULES |

---

## 1. Purpose

This document establishes mandatory software design rules for all 53-40 Software components, ensuring consistency, safety, and certification compliance across the ATA 53 Fuselage embedded software domain.

## 2. Scope

These rules apply to:

- All software developed under 53-40 bands (00-95)
- Auto-generated code from model-based tools
- Configuration files and parameter sets
- Test code and verification artifacts

## 3. General Design Rules

### 3.1 Code Structure

| Rule ID | Rule | Rationale |
|---------|------|-----------|
| DR-001 | Each function SHALL have a single, well-defined purpose | Maintainability |
| DR-002 | Cyclomatic complexity SHALL NOT exceed 15 per function | Testability |
| DR-003 | Function length SHALL NOT exceed 100 lines | Readability |
| DR-004 | Nesting depth SHALL NOT exceed 4 levels | Comprehension |
| DR-005 | All functions SHALL return a status/error code | Error handling |

### 3.2 Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Functions | `<Module>_<Action><Object>` | `CO2Ctrl_SetCapturerate` |
| Variables | `<type>_<descriptiveName>` | `f32_targetTemperature` |
| Constants | `<MODULE>_<NAME>` | `BATTMS_MAX_TEMP` |
| Types | `<Module><Type>_t` | `CO2CtrlState_t` |
| Files | `53-40-XX-YY_<Name>.c/h` | `53-40-10-02_CO2_Controller.c` |

### 3.3 Documentation Requirements

| Rule ID | Rule |
|---------|------|
| DR-010 | Every source file SHALL have a file header with Document ID, version, and description |
| DR-011 | Every function SHALL have a doxygen-style comment describing purpose, parameters, return values |
| DR-012 | Complex algorithms SHALL include inline comments explaining the logic |
| DR-013 | All magic numbers SHALL be replaced with named constants |

## 4. Safety-Critical Design Rules

### 4.1 Memory Management

| Rule ID | Rule | DAL Applicability |
|---------|------|-------------------|
| DR-100 | Dynamic memory allocation SHALL NOT be used after initialization | A, B, C |
| DR-101 | Stack usage SHALL be bounded and verified | A, B, C |
| DR-102 | All arrays SHALL have bounds checking | A, B, C, D |
| DR-103 | Pointer arithmetic SHALL be minimized and documented | A, B |

### 4.2 Timing and Determinism

| Rule ID | Rule | DAL Applicability |
|---------|------|-------------------|
| DR-110 | All loops SHALL be bounded | A, B, C |
| DR-111 | Worst-case execution time (WCET) SHALL be analyzed | A, B |
| DR-112 | Blocking operations SHALL have timeouts | A, B, C |
| DR-113 | Recursive calls SHALL NOT be used | A, B |
| DR-114 | Interrupt handlers SHALL complete within specified time budget | A, B, C |

### 4.3 Data Integrity

| Rule ID | Rule | DAL Applicability |
|---------|------|-------------------|
| DR-120 | Safety-critical data SHALL use defensive copies | A, B |
| DR-121 | Critical parameters SHALL include range validation | A, B, C |
| DR-122 | State variables SHALL be protected against corruption | A, B |
| DR-123 | CRC/checksum SHALL be used for data in transmission | A, B, C |

## 5. Interface Design Rules

### 5.1 API Design

| Rule ID | Rule |
|---------|------|
| DR-200 | All APIs SHALL use consistent parameter ordering: inputs, outputs, status |
| DR-201 | APIs SHALL validate all input parameters |
| DR-202 | APIs SHALL be idempotent where possible |
| DR-203 | APIs SHALL use versioned interfaces |

### 5.2 Bus Communication

| Rule ID | Rule |
|---------|------|
| DR-210 | All bus messages SHALL include message ID and sequence number |
| DR-211 | Messages SHALL have defined timeout and retry behavior |
| DR-212 | Message rates SHALL be explicitly specified and enforced |
| DR-213 | All signals SHALL have defined validity criteria |

## 6. Testing Design Rules

### 6.1 Testability

| Rule ID | Rule |
|---------|------|
| DR-300 | All modules SHALL be unit-testable in isolation |
| DR-301 | Dependencies SHALL be injectable for testing |
| DR-302 | Observable points SHALL be provided for key internal states |
| DR-303 | BITE interfaces SHALL be provided for all testable functions |

### 6.2 Coverage Requirements

| DAL | Statement | Branch | MC/DC |
|-----|-----------|--------|-------|
| A | 100% | 100% | 100% |
| B | 100% | 100% | — |
| C | 100% | — | — |
| D | Objective | — | — |

## 7. NN Integration Design Rules

### 7.1 Neural Network Wrappers

| Rule ID | Rule |
|---------|------|
| DR-400 | NN inference SHALL be isolated in dedicated functions |
| DR-401 | NN outputs SHALL be validated against safety envelope |
| DR-402 | Fallback deterministic logic SHALL be available when NN fails |
| DR-403 | NN execution time SHALL be bounded and monitored |
| DR-404 | NN model version SHALL be traceable at runtime |

### 7.2 Safety Envelope

| Rule ID | Rule |
|---------|------|
| DR-410 | NN outputs SHALL be rate-limited |
| DR-411 | NN outputs SHALL be range-checked before use |
| DR-412 | NN confidence scores SHALL be evaluated before accepting output |
| DR-413 | NN degradation SHALL trigger automatic fallback |

## 8. Configuration and Data Rules

### 8.1 Parameters

| Rule ID | Rule |
|---------|------|
| DR-500 | All tunable parameters SHALL be in configuration files, not code |
| DR-501 | Parameters SHALL have defined valid ranges |
| DR-502 | Parameter sets SHALL be versioned |
| DR-503 | Default values SHALL be defined for all parameters |

### 8.2 Logging

| Rule ID | Rule |
|---------|------|
| DR-510 | All log entries SHALL include timestamp and source |
| DR-511 | Log levels SHALL be used consistently: ERROR, WARN, INFO, DEBUG |
| DR-512 | Safety-critical events SHALL always be logged |
| DR-513 | Log messages SHALL NOT expose sensitive data |

## 9. Compliance Matrix

| Standard | Applicable Rules |
|----------|------------------|
| DO-178C | DR-001 to DR-123, DR-300 to DR-303 |
| MISRA C:2012 | DR-001 to DR-013, DR-100 to DR-103 |
| CERT C | DR-100 to DR-123, DR-200 to DR-213 |
| IEC 61508 | DR-100 to DR-123 |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-40-00-03 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Author** | AMPEL360 SW Quality Team |
| **Reviewer** | _[To be assigned]_ |
| **Approver** | _[To be assigned]_ |

### AI Disclosure

- **Generated with assistance of:** AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status:** DRAFT — Subject to human review and approval
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-27

---

*END OF DOCUMENT*
