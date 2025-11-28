# 53-90-10-03 Signal Validation

| Field | Value |
|-------|-------|
| **Document ID** | 53-90-10-03 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | TECHNICAL / DATA |
| **ATA Chapter** | 53-90-10 |

---

## 1. Purpose

This document defines the validation rules and procedures for ANCHORS signals in the 53-90-10 Signal Dictionary.

## 2. Validation Rules

### 2.1 Signal ID Validation

| Rule ID | Rule Description | Severity |
|---------|------------------|----------|
| SIG-001 | Signal ID must match pattern `ANCH_[A-Z0-9]+_[TPFLVIWSDACX]_[A-Z0-9_]+` | ERROR |
| SIG-002 | Signal ID must be unique across all catalogs | ERROR |
| SIG-003 | Signal ID length must not exceed 32 characters | WARNING |
| SIG-004 | Subsystem code must be registered in naming conventions | ERROR |

### 2.2 Range Validation

| Rule ID | Rule Description | Severity |
|---------|------------------|----------|
| RNG-001 | Range min must be less than range max | ERROR |
| RNG-002 | Default value must be within range | ERROR |
| RNG-003 | Range must be appropriate for signal type | WARNING |
| RNG-004 | Physical limits must be realistic | WARNING |

### 2.3 Rate Validation

| Rule ID | Rule Description | Severity |
|---------|------------------|----------|
| RAT-001 | Rate must be positive and non-zero | ERROR |
| RAT-002 | DAL B signals must have rate ≥ 10 Hz | ERROR |
| RAT-003 | Safety signals must have rate ≥ 100 Hz | ERROR |
| RAT-004 | Rate must not exceed bus capacity | WARNING |

### 2.4 DAL Validation

| Rule ID | Rule Description | Severity |
|---------|------------------|----------|
| DAL-001 | DAL must be A, B, C, D, or E | ERROR |
| DAL-002 | Safety-critical signals must be DAL B or higher | ERROR |
| DAL-003 | Fault flags must have same DAL as monitored signal | WARNING |
| DAL-004 | Commands must have same DAL as controlled function | WARNING |

## 3. Validation Process

### 3.1 Automated Validation

```python
# Example validation pseudocode
def validate_signal(signal):
    errors = []
    warnings = []
    
    # SIG-001: Pattern match
    if not re.match(r'^ANCH_[A-Z0-9]+_[TPFLVIWSDACX]_[A-Z0-9_]+$', signal.id):
        errors.append('SIG-001: Invalid signal ID pattern')
    
    # RNG-001: Range check
    if signal.range_min >= signal.range_max:
        errors.append('RNG-001: Range min must be less than max')
    
    # DAL-002: Safety check
    if signal.is_safety_critical and signal.dal not in ['A', 'B']:
        errors.append('DAL-002: Safety signals require DAL B or higher')
    
    return {'errors': errors, 'warnings': warnings}
```

### 3.2 CI/CD Integration

| Stage | Validation Type | Action on Failure |
|-------|-----------------|-------------------|
| Pre-commit | Schema syntax | Block commit |
| PR Review | Full validation | Request changes |
| Merge | Complete regression | Block merge |
| Release | Certification evidence | Block release |

## 4. Validation Results Template

### 4.1 Summary Report

| Category | Total | Errors | Warnings | Pass Rate |
|----------|-------|--------|----------|-----------|
| Signal ID | 175 | 0 | 2 | 98.9% |
| Range | 175 | 0 | 5 | 97.1% |
| Rate | 175 | 0 | 0 | 100% |
| DAL | 175 | 0 | 3 | 98.3% |
| **Total** | **175** | **0** | **10** | **94.3%** |

### 4.2 Issue Log

| Signal ID | Rule | Severity | Description | Status |
|-----------|------|----------|-------------|--------|
| ANCH_H2O_D_QUALITY | RNG-003 | WARNING | Boolean range should be 0-1 | Open |
| ANCH_NN_V_CONFIDENCE | SIG-003 | WARNING | Consider shorter ID | Accepted |

## 5. Traceability Requirements

### 5.1 Required Traceability

Each signal must have documented links to:

- **Requirements**: At least one functional requirement
- **Design**: Source and destination components
- **Test Cases**: At least one verification test

### 5.2 Coverage Matrix

| DAL | Req Coverage | Test Coverage | Min Coverage |
|-----|--------------|---------------|--------------|
| A | 100% | 100% | 100% |
| B | 100% | 100% | 100% |
| C | 100% | 95% | 95% |
| D | 90% | 80% | 80% |
| E | 80% | 50% | 50% |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-27_.

---
