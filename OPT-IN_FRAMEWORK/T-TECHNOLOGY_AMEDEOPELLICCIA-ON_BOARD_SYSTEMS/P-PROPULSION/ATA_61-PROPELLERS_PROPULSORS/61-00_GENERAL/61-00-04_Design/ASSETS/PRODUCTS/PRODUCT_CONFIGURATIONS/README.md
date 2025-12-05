# PRODUCT_CONFIGURATIONS — ATA 61 Propellers/Propulsors

**Purpose**: This directory contains configuration management data for the propulsion system products, including baselines, options, and customer-specific configurations.

## Structure

```
PRODUCT_CONFIGURATIONS/
├── README.md                           # This file
├── Q100-61-CFG-MASTER-INDEX.yaml      # Master configuration index
├── BASELINE/                           # Baseline configurations
│   ├── README.md
│   ├── Q100-61-CFG-BASELINE-R01.yaml  # Initial baseline
│   └── effectivity/                    # Effectivity data
├── OPTIONS/                            # Optional features
│   ├── README.md
│   ├── Q100-61-OPT-HIGH-POWER.yaml
│   ├── Q100-61-OPT-EXTENDED-RANGE.yaml
│   ├── Q100-61-OPT-REDUCED-NOISE.yaml
│   └── Q100-61-OPT-SAF-OPTIMIZED.yaml
└── CUSTOMER_CONFIGS/                   # Customer-specific
    └── README.md
```

## Configuration Management Process

1. **Baseline Definition**: Establish initial configuration baseline
2. **Option Selection**: Customer selects applicable options
3. **Configuration Build**: Generate specific configuration
4. **Effectivity Assignment**: Assign MSN/tail number effectivity
5. **Configuration Control**: Track changes and maintain traceability

## Related Directories

- [Product Definitions](../PRODUCT_DEFINITIONS/README.md)
- [Product Variants](../PRODUCT_VARIANTS/README.md)
- [Bill of Materials](../BILL_OF_MATERIALS/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
