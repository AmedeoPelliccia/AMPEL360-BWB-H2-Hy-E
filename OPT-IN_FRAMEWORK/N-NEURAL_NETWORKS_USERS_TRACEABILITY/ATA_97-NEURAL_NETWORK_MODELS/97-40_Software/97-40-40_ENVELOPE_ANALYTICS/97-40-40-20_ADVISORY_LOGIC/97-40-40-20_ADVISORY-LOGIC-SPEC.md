# Advisory Logic Specification

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | OFEC-97-40-40-20-SPEC-001 |
| **Version** | 1.0 |
| **Status** | DRAFT |

---

## 1. Overview

The Advisory Logic module (97-40-40-20) processes margin data to generate advisories, detect trends, and identify exceedances.

---

## 2. Advisory Levels

| Level | Meaning | Trigger |
|-------|---------|---------|
| NORMAL | All margins adequate | All margins > 50% |
| CAUTION | Reduced margins | Any margin 25-50% |
| WARNING | Low margins | Any margin 10-25% |
| CRITICAL | At or beyond limit | Any margin < 10% |

---

## 3. Components

| Component | Purpose |
|-----------|---------|
| Advisory Engine | Generate and manage advisories |
| Trend Analyzer | Detect parameter trends |
| Exceedance Detector | Identify limit exceedances |
| Recovery Advisor | Suggest recovery actions |

---

## 4. Processing Flow

```
Margin Data → Trend Analysis → Exceedance Check → Advisory Generation → Output
                    ↓                  ↓
              Trend State        Event Logging
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.
