# 53-90-20-03 Parameter Management

| Field | Value |
|-------|-------|
| **Document ID** | 53-90-20-03 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | TECHNICAL / DATA |
| **ATA Chapter** | 53-90-20 |

---

## 1. Purpose

This document defines the management procedures for ANCHORS system parameters, including modification, version control, and deployment processes.

## 2. Parameter Categories

### 2.1 Category Definitions

| Category | Authority | When Modified | Example |
|----------|-----------|---------------|---------|
| **Fixed** | Factory Only | Manufacturing | Hardware limits |
| **Tunable** | Engineering | Development/Test | Control gains |
| **Configurable** | Maintenance | Per-aircraft | SOC limits |
| **Adaptive** | Automatic | Runtime | Learning rates |

### 2.2 Modification Rights Matrix

| Category | Design | Test | Maintenance | In-Service |
|----------|--------|------|-------------|------------|
| Fixed | ✓ | ✗ | ✗ | ✗ |
| Tunable | ✓ | ✓ | ✗ | ✗ |
| Configurable | ✓ | ✓ | ✓ | ✓* |
| Adaptive | Auto | Auto | Auto | Auto |

*With approved maintenance procedure

## 3. Parameter Change Process

### 3.1 Change Request Workflow

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ REQUEST  │───▶│  REVIEW  │───▶│ APPROVE  │───▶│  DEPLOY  │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
     │               │               │               │
     ▼               ▼               ▼               ▼
  Submit          Impact         Authority        Verify
  Justification   Analysis       Sign-off        Regression
```

### 3.2 Required Documentation

| Document | Fixed | Tunable | Configurable | Adaptive |
|----------|-------|---------|--------------|----------|
| Change Request | ✓ | ✓ | ✓ | N/A |
| Impact Analysis | ✓ | ✓ | ✓ | N/A |
| Safety Assessment | ✓ | ✓ | Optional | Auto |
| Test Evidence | ✓ | ✓ | ✓ | Monitor |
| Approval Record | ✓ | ✓ | ✓ | N/A |

### 3.3 Approval Authority

| Safety Impact | Fixed | Tunable | Configurable |
|---------------|-------|---------|--------------|
| Critical | DER + Chief Engineer | DER | Engineering Manager |
| High | Chief Engineer | Safety Engineer | Lead Engineer |
| Medium | Engineering Manager | Lead Engineer | Engineer |
| Low | Lead Engineer | Engineer | Technician |
| None | Engineer | Engineer | Technician |

## 4. Version Control

### 4.1 Parameter Set Versioning

```
Parameter Set Version: <Major>.<Minor>.<Patch>-<Build>

Example: 2.3.1-RC1
         │ │ │  │
         │ │ │  └── Build identifier (RC1, DEV, PROD)
         │ │ └───── Patch (bug fixes only)
         │ └─────── Minor (new parameters, compatible)
         └───────── Major (breaking changes)
```

### 4.2 Version History Template

| Version | Date | Author | Changes | Approval |
|---------|------|--------|---------|----------|
| 1.0.0 | 2025-01-15 | Team | Initial release | Approved |
| 1.1.0 | 2025-03-20 | Team | Added TH parameters | Approved |
| 1.1.1 | 2025-04-10 | Team | Fixed SOC limits | Approved |
| 2.0.0 | 2025-06-01 | Team | NN parameters added | Pending |

## 5. Deployment Procedures

### 5.1 Parameter Loading

| Method | Use Case | Verification |
|--------|----------|--------------|
| **Flash** | Factory initial load | Checksum + signature |
| **Data Load** | Software update | Version match |
| **MCDU Entry** | Field adjustment | Dual entry |
| **CMC Upload** | Batch configuration | Diff report |

### 5.2 Verification Checklist

- [ ] Parameter file checksum verified
- [ ] Version compatibility confirmed
- [ ] Previous values backed up
- [ ] Load completion confirmed
- [ ] BITE self-test passed
- [ ] Affected functions verified
- [ ] Log entry recorded

## 6. Safety Considerations

### 6.1 Safety-Critical Parameters

Parameters affecting safety functions require:

1. **Independent Verification** — Second engineer review
2. **Range Validation** — Values within safe bounds
3. **Dependency Check** — Related parameters consistent
4. **Reversion Plan** — Documented rollback procedure

### 6.2 Parameter Integrity

| Check | Method | Frequency |
|-------|--------|-----------|
| Checksum | CRC-32 | Every power-on |
| Range | Limit check | Continuous |
| Consistency | Cross-check | Every 10 sec |
| Signature | Cryptographic | On load |

## 7. Audit and Traceability

### 7.1 Change Log Format

| Timestamp | User | Parameter | Old Value | New Value | Reason |
|-----------|------|-----------|-----------|-----------|--------|
| 2025-06-15T10:30:00Z | ENG-001 | P_BAT_TMS_T_HIGH_LIM | 55 | 57 | Test optimization |

### 7.2 Retention Requirements

| Data Type | Active | Archive | Total |
|-----------|--------|---------|-------|
| Parameter Sets | 2 years | 20 years | 22 years |
| Change Logs | 3 years | 20 years | 23 years |
| Approval Records | 5 years | 25 years | 30 years |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-27_.

---
