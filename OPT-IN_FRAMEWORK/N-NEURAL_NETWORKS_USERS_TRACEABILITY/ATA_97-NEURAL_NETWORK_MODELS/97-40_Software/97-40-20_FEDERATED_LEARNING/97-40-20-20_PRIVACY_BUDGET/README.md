# 97-40-20-20 — Privacy Budget

## Purpose

Per-model, per-aircraft privacy budget (ε, δ) tracking and enforcement.

## Budget Limits

| Model Type | Max ε per Round | Max ε Lifetime | δ |
|------------|-----------------|----------------|---|
| Non-safety | 1.0 | 10.0 | 10⁻⁵ |
| Advisory | 0.5 | 5.0 | 10⁻⁶ |
| Safety-related | N/A (no FL) | N/A | N/A |

## Accounting Method

- **Moments Accountant** for tight composition
- Per-aircraft, per-model tracking
- Automatic blocking when exhausted

## Document Control

- Standard: OPT-IN Framework v1.2
- Status: Active
- Last Updated: 2025-11-27
