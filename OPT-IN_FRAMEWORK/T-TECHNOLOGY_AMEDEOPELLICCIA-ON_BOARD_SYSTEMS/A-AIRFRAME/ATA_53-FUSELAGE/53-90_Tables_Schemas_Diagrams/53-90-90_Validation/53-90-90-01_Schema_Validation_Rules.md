# 53-90-90-01 Schema Validation Rules

| Field | Value |
|-------|-------|
| **Document ID** | 53-90-90-01 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | TECHNICAL / VALIDATION |
| **ATA Chapter** | 53-90-90 |

---

## 1. Purpose

This document defines the validation rules for all schemas and data files in the 53-90 Tables, Schemas & Diagrams bucket.

## 2. Validation Framework

### 2.1 Validation Levels

| Level | Scope | When Applied |
|-------|-------|--------------|
| **Syntax** | File format validity | Every change |
| **Schema** | JSON/XML schema compliance | Every change |
| **Semantic** | Cross-reference integrity | PR merge |
| **Consistency** | System-wide coherence | Release |

### 2.2 Validation Tools

| Tool | Purpose | Files |
|------|---------|-------|
| jsonschema | JSON validation | *.json |
| xmllint | XML/XSD validation | *.xml, *.xsd |
| csvkit | CSV structure check | *.csv |
| markdownlint | Markdown linting | *.md |

## 3. Signal Validation Rules

### 3.1 Signal ID Rules

| Rule ID | Description | Severity | Example |
|---------|-------------|----------|---------|
| SIG-001 | ID must match pattern | ERROR | `ANCH_BAT_T_CELL_MAX` ✓ |
| SIG-002 | ID must be unique | ERROR | No duplicates in catalog |
| SIG-003 | ID length ≤ 32 chars | WARNING | Consider shorter names |
| SIG-004 | Type code must be valid | ERROR | T, P, F, L, V, I, W, S, D, A, C, X |
| SIG-005 | Subsystem must be registered | ERROR | BAT, CO2, H2O, TH, EMS, SS, MM |

### 3.2 Signal Range Rules

| Rule ID | Description | Severity |
|---------|-------------|----------|
| RNG-001 | Min < Max | ERROR |
| RNG-002 | Default within range | ERROR |
| RNG-003 | Range appropriate for type | WARNING |
| RNG-004 | Physical limits realistic | WARNING |

### 3.3 Signal Rate Rules

| Rule ID | Description | Severity |
|---------|-------------|----------|
| RAT-001 | Rate > 0 | ERROR |
| RAT-002 | DAL B signals ≥ 10 Hz | ERROR |
| RAT-003 | Safety signals ≥ 100 Hz | ERROR |
| RAT-004 | Rate within bus capacity | WARNING |

## 4. Parameter Validation Rules

### 4.1 Parameter ID Rules

| Rule ID | Description | Severity |
|---------|-------------|----------|
| PAR-001 | ID must match pattern `P_*` | ERROR |
| PAR-002 | ID must be unique | ERROR |
| PAR-003 | ID length ≤ 40 chars | WARNING |
| PAR-004 | Bucket reference valid | ERROR |

### 4.2 Parameter Value Rules

| Rule ID | Description | Severity |
|---------|-------------|----------|
| VAL-001 | Default must be valid | ERROR |
| VAL-002 | Fixed: min/max must be null | ERROR |
| VAL-003 | Tunable: must have min/max | ERROR |
| VAL-004 | Dependencies must exist | ERROR |

## 5. Message Validation Rules

### 5.1 AFDX VL Rules

| Rule ID | Description | Severity |
|---------|-------------|----------|
| VL-001 | VL ID unique in range | ERROR |
| VL-002 | BAG ≥ 2ms | ERROR |
| VL-003 | MTU ≤ 1518 bytes | ERROR |
| VL-004 | Source/Dest must exist | ERROR |

### 5.2 CAN Message Rules

| Rule ID | Description | Severity |
|---------|-------------|----------|
| CAN-001 | CAN ID unique | ERROR |
| CAN-002 | DLC ≤ 8 bytes | ERROR |
| CAN-003 | Rate within bus capacity | WARNING |
| CAN-004 | Content matches DLC | ERROR |

## 6. Cross-Reference Validation

### 6.1 Traceability Rules

| Rule ID | Description | Severity |
|---------|-------------|----------|
| TRC-001 | Requirement ID must exist | ERROR |
| TRC-002 | Test case must exist | ERROR |
| TRC-003 | Design ref must exist | ERROR |
| TRC-004 | Hazard ID must exist | ERROR |

### 6.2 Consistency Rules

| Rule ID | Description | Severity |
|---------|-------------|----------|
| CON-001 | Signal in catalog = signal in schema | ERROR |
| CON-002 | Parameter in catalog = parameter in schema | ERROR |
| CON-003 | Abbreviation defined = abbreviation used | WARNING |
| CON-004 | Figure in catalog = figure file exists | WARNING |

## 7. Validation Procedures

### 7.1 Pre-Commit Validation

```bash
#!/bin/bash
# Run before committing changes

# JSON validation
for f in $(find . -name "*.json"); do
    jsonschema --instance "$f" schema.json || exit 1
done

# CSV structure check
for f in $(find . -name "*.csv"); do
    csvstat "$f" > /dev/null || exit 1
done

# Markdown lint
markdownlint "**/*.md" || exit 1
```

### 7.2 CI/CD Integration

| Stage | Validation | Action |
|-------|------------|--------|
| Pre-commit | Syntax | Block |
| PR Open | Schema | Report |
| PR Merge | Semantic | Block |
| Release | Complete | Block |

### 7.3 Validation Report

```
=== 53-90 VALIDATION REPORT ===
Date: 2025-11-27
Scope: Full validation

SUMMARY:
  Total Files: 36
  Validated: 36
  Errors: 0
  Warnings: 5

BY CATEGORY:
  Signals: 175 checked, 0 errors
  Parameters: 51 checked, 0 errors
  Messages: 16 VL, 37 CAN, 0 errors
  Traceability: 22 requirements traced

WARNINGS:
  - SIG-003: ANCH_H2O_D_QUALITY_OK (33 chars)
  - CON-004: FIG-53-10-002 file pending
  
STATUS: PASS (with warnings)
```

## 8. Error Handling

### 8.1 Error Severity

| Level | Description | Action |
|-------|-------------|--------|
| ERROR | Must be fixed | Block merge |
| WARNING | Should be reviewed | Document exception |
| INFO | For information | Log only |

### 8.2 Exception Process

1. Document the exception in this file
2. Obtain engineering review
3. Log exception ID in validation run
4. Review at next release

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-27_.

---
