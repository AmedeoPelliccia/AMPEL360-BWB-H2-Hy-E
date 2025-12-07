# PRODUCT_DEFINITIONS — ATA 61 Propellers/Propulsors

**Purpose**: This directory contains the core product definitions for all deliverable propulsion system products in the Q100 program.

## Product Hierarchy

```
Q100-61-PROD-PROPULSOR-SYSTEM (Top Level)
├── Q100-61-PROD-OPEN-FAN-UNIT
├── Q100-61-PROD-ELECTRIC-DRIVE-UNIT
├── Q100-61-PROD-GEARBOX-UNIT
├── Q100-61-PROD-NACELLE-UNIT
└── Q100-61-PROD-CONTROLLER-UNIT
```

## Product Definition Structure

Each product directory contains:

| File | Purpose |
|------|---------|
| `README.md` | Product overview and key information |
| `product_definition.yaml` | Formal product definition metadata |
| `product_structure.yaml` | Product hierarchy and composition |
| `configuration/` | Configuration baselines specific to this product |
| `specifications/` | Product-specific specifications |
| `certification/` | Certification-related data (where applicable) |
| `documentation/` | Product-specific documentation (top-level only) |

## Products Summary

| Product ID | Name | Level | Description |
|------------|------|-------|-------------|
| Q100-61-PROD-PROPULSOR-SYSTEM | Propulsor System | Top-Level | Complete integrated propulsion unit |
| Q100-61-PROD-OPEN-FAN-UNIT | Open Fan Unit | Sub-Product | Open-fan rotor assembly |
| Q100-61-PROD-ELECTRIC-DRIVE-UNIT | Electric Drive Unit | Sub-Product | Motor and power electronics |
| Q100-61-PROD-GEARBOX-UNIT | Gearbox Unit | Sub-Product | Reduction gearbox assembly |
| Q100-61-PROD-NACELLE-UNIT | Nacelle Unit | Sub-Product | Nacelle structure and cowlings |
| Q100-61-PROD-CONTROLLER-UNIT | Controller Unit | Sub-Product | Propulsor control system |

## Usage

1. Navigate to the appropriate product directory
2. Review `README.md` for product overview
3. Consult `product_definition.yaml` for formal attributes
4. Use `product_structure.yaml` to understand composition

## Related Directories

- [Product Variants](../PRODUCT_VARIANTS/README.md) — Position and application variants
- [Product Configurations](../PRODUCT_CONFIGURATIONS/README.md) — Configuration baselines
- [Bill of Materials](../BILL_OF_MATERIALS/README.md) — Component lists
- [Product Specifications](../PRODUCT_SPECIFICATIONS/README.md) — Technical specifications

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
