# Margin of Safety Calculator Guide

## Overview

This guide provides instructions for calculating and reporting Margin of Safety (MS) for structural components per certification requirements.

## Formula

**MS = (Allowable / Applied) × (1 / SF) - 1**

Where:
- **Allowable**: Material or structural allowable (strength, stress, load)
- **Applied**: Actual applied value (stress, load)
- **SF**: Safety Factor (typically 1.0 for ultimate loads, as 1.5 factor already in ultimate load definition)

## Interpretation

- **MS ≥ 0**: PASS - Adequate margin
- **MS < 0**: FAIL - Negative margin, redesign required

## Typical Margin Ranges

| Range | Interpretation | Action |
|-------|----------------|--------|
| MS < 0 | Unacceptable | Redesign required |
| 0 ≤ MS < 0.05 | Marginal | Monitor closely |
| 0.05 ≤ MS < 0.15 | Adequate | Acceptable |
| MS ≥ 0.15 | Conservative | Consider optimization |

## Examples

### Example 1: Tension Member
- Applied stress: 400 MPa
- Allowable stress (A-basis, ETW): 500 MPa
- Safety factor: 1.0 (for ultimate load)

**MS = (500 / 400) × (1 / 1.0) - 1 = 0.25**

Result: PASS with 25% margin

### Example 2: Compression Panel
- Applied stress: 620 MPa
- Allowable stress: 600 MPa
- Safety factor: 1.0

**MS = (600 / 620) × (1 / 1.0) - 1 = -0.032**

Result: FAIL with -3.2% margin (redesign required)

## Documentation

All margin calculations must be documented with:
- Component identification
- Load case
- Material and allowables reference
- Analysis method
- Calculated margin
- Pass/fail status

---

## Document Control
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Version: 1.0
- Last Update: 2025-11-22

---
