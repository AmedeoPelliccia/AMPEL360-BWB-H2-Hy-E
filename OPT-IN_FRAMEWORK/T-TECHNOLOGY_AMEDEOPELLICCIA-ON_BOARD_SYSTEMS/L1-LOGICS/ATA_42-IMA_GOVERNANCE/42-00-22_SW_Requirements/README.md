# 42-00-22_SW_Requirements

## Purpose

Software requirements repository for partitioned IMA software development.

## Scope

This folder contains software requirements organized by partition:

* High-Level Requirements (HLR)
* Low-Level Requirements (LLR)
* Derived Requirements
* Interface Requirements

## Structure

Requirements are organized by partition:

```text
42-00-22_SW_Requirements/
├── P-FCS/          # Flight Control System requirements
├── P-GNC/          # Guidance, Navigation, Control requirements
├── P-ADS/          # Air Data System requirements
├── P-MAINT/        # Maintenance Function requirements
└── P-DIAG/         # Diagnostics requirements
```

## Requirements Naming Convention

| Pattern | Example | Description |
|---------|---------|-------------|
| REQ-42-XXX-NNN | REQ-42-FCS-001 | Partition requirement |
| REQ-42-XXX-NNN-LLR | REQ-42-FCS-001-LLR | Low-level requirement |
| REQ-42-XXX-NNN-DER | REQ-42-FCS-001-DER | Derived requirement |

## Traceability

All requirements are traced in:

* [`42-00-20_GENCCC_SW_CONFIG/MATRICES/`](../42-00-20_GENCCC_SW_CONFIG/MATRICES/) — Traceability matrices

## Related Folders

* [`42-00-20_GENCCC_SW_CONFIG/`](../42-00-20_GENCCC_SW_CONFIG/) — GenCCC configuration
* [`42-00-21_Partition_Catalog/`](../42-00-21_Partition_Catalog/) — Partition registry
* [`42-00-23_SW_Code/`](../42-00-23_SW_Code/) — Source code
* [`42-00-24_SW_Tests/`](../42-00-24_SW_Tests/) — Test artifacts

## Document Control

- **Standard**: OPT-IN Framework v1.1
- **Status**: Active
- **Owner**: AMPEL360 SW WG
- **Last Updated**: 2025-12-04

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-04.

---
