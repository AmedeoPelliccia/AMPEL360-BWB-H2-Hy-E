# Weight Tracking Tool

## 1. Purpose

This guide describes the weight tracking procedures for the ATA 53 Fuselage structure.

---

## 2. Weight Tracking Process

### 2.1 Data Sources

| Source | Data Type | Update Frequency |
|--------|-----------|------------------|
| CI_Definition.yaml | Target and actual weights | As updated |
| CAD models | Calculated weights | Weekly |
| Test articles | Measured weights | On weighing |

### 2.2 Tracking Files

| File | Description |
|------|-------------|
| `CI_Weight_Tracking.csv` | Detailed CI-level tracking |
| `Weight_Status_Dashboard.csv` | Summary dashboard |

---

## 3. Weight Status Categories

| Status | Criteria |
|--------|----------|
| Under Target | Actual ≤ Target |
| Within Tolerance | Actual < Target + 3% |
| Over Target | Actual ≥ Target + 3% |
| TBD | Actual not yet known |

---

## 4. Reporting

### 4.1 Weekly Report

- Zone-level weight summary
- Trend analysis
- Action items for over-target CIs

### 4.2 Milestone Reports

- PDR/CDR weight status
- Comparison to budget
- Recovery plans if needed

---

## 5. Document Control

- **Document ID**: 53-00-04-A-023
- **Version**: 1.0
- **Date**: 2025-11-24
- **Owner**: ATA 53 Weights Lead
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-24_.

---
