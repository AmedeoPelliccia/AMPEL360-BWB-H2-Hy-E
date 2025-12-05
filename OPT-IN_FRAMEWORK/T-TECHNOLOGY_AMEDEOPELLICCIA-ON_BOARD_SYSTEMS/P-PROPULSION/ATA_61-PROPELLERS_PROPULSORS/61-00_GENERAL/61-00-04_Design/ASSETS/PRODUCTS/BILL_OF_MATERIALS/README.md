# BILL_OF_MATERIALS — ATA 61 Propellers/Propulsors

**Purpose**: This directory contains Bill of Materials (BOM) data for all propulsion system products, in both YAML and CSV formats.

## Structure

Each product has a dedicated directory containing:

| File | Format | Purpose |
|------|--------|---------|
| `*.yaml` | YAML | Structured BOM with metadata |
| `*.csv` | CSV | Tabular BOM for ERP/PLM import |

## Products

| Product ID | BOM ID | Description |
|------------|--------|-------------|
| Q100-61-PROD-PROPULSOR-SYSTEM | Q100-61-BOM-PROPULSOR-SYSTEM | Complete propulsor BOM |
| Q100-61-PROD-OPEN-FAN-UNIT | Q100-61-BOM-OPEN-FAN-UNIT | Open fan unit BOM |
| Q100-61-PROD-ELECTRIC-DRIVE-UNIT | Q100-61-BOM-ELECTRIC-DRIVE-UNIT | Electric drive BOM |
| Q100-61-PROD-GEARBOX-UNIT | Q100-61-BOM-GEARBOX-UNIT | Gearbox BOM |
| Q100-61-PROD-NACELLE-UNIT | Q100-61-BOM-NACELLE-UNIT | Nacelle BOM |
| Q100-61-PROD-CONTROLLER-UNIT | Q100-61-BOM-CONTROLLER-UNIT | Controller BOM |

## BOM Levels

- **Level 0**: Top-level product
- **Level 1**: Major sub-products
- **Level 2**: Sub-assemblies
- **Level 3+**: Parts and components

## CSV Format

```csv
Level,Item_Number,Part_Number,Description,Quantity,Unit,Make_Buy,Reference
```

## Related Directories

- [Product Definitions](../PRODUCT_DEFINITIONS/README.md)
- [Product Specifications](../PRODUCT_SPECIFICATIONS/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
