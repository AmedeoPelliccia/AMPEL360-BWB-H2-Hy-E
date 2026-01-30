# PRODUCT_VARIANTS — ATA 61 Propellers/Propulsors

**Purpose**: This directory contains the product variant definitions for position-specific and application-specific variants of the propulsion system products.

## Variants Overview

| Variant ID | Name | Position | Description |
|------------|------|----------|-------------|
| Q100-61-VAR-PROPULSOR-LH | Left Hand Propulsor | Left wing | Mirrored mounting configuration |
| Q100-61-VAR-PROPULSOR-RH | Right Hand Propulsor | Right wing | Baseline mounting configuration |
| Q100-61-VAR-PROPULSOR-CENTER | Center Propulsor | Tail | Centerline with thrust vectoring |
| Q100-61-VAR-PROPULSOR-EXTENDED-RANGE | Extended Range Propulsor | Any | Enhanced efficiency mode |

## Variant Structure

Each variant directory contains:

| File | Purpose |
|------|---------|
| `README.md` | Variant overview |
| `variant_definition.yaml` | Formal variant definition |
| `delta_from_baseline.yaml` | Differences from baseline product |

## BWB Configuration

The AMPEL360 BWB aircraft can be configured with:

- **Twin Configuration**: LH + RH propulsors (wing-mounted)
- **Tri Configuration**: LH + RH + CENTER propulsors
- **Extended Range**: Any position with efficiency optimization

## Related Directories

- [Product Definitions](../PRODUCT_DEFINITIONS/README.md) — Base product definitions
- [Product Configurations](../PRODUCT_CONFIGURATIONS/README.md) — Configuration baselines

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
