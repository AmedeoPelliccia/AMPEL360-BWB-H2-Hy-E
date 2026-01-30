# CUSTOMER_CONFIGS — Customer-Specific Configurations

**Purpose**: This directory contains customer-specific configuration files that define the exact product configuration for each customer order.

## Naming Convention

```
Q100-61-CFG-[CUSTOMER_CODE]-[MSN].yaml
```

Example: `Q100-61-CFG-ACME-001.yaml`

## Configuration Contents

Each customer configuration file specifies:

- Customer identification
- Aircraft MSN (Manufacturer Serial Number)
- Selected baseline
- Selected options
- Selected variants
- Delivery configuration
- Customer-specific requirements

## Confidentiality

Customer configuration files may contain confidential information and should be handled according to the project's data classification policies.

## Related Documents

- [Master Configuration Index](../Q100-61-CFG-MASTER-INDEX.yaml)
- [Baselines](../BASELINE/README.md)
- [Options](../OPTIONS/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
