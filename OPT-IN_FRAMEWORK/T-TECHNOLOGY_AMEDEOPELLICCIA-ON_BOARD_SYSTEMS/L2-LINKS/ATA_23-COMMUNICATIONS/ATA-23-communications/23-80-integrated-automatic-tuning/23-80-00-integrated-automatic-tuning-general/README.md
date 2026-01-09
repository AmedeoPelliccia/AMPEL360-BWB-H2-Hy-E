# 23-80-00

## Overview

This directory contains the publication-ready content for integrated automatic tuning system technical documentation.

## Purpose

This level organizes content by publication type following S1000D standards:
- **SSOT/**: Single Source of Truth (lifecycle content)
- **PUB/**: Publication content organized by manual type

## Structure

```
23-80-00/
├── SSOT/                           # Single Source of Truth
│   ├── LC01_Requirements/
│   ├── LC02_System_Requirements/
│   ├── LC03_Design/
│   ├── LC04_Analysis/
│   ├── LC05_VnV/
│   ├── LC06_Quality/
│   ├── LC07_Safety/
│   └── LC08_Certification/
└── PUB/                            # Publications
    ├── AMM/                        # Aircraft Maintenance Manual
    └── IPC/                        # Illustrated Parts Catalog
```

## SSOT — Single Source of Truth

The SSOT directory contains lifecycle-organized content:

- **LC01_Requirements**: System and functional requirements
- **LC02_System_Requirements**: Detailed system-level requirements
- **LC03_Design**: Design specifications and architecture
- **LC04_Analysis**: Engineering analysis and modeling
- **LC05_VnV**: Verification and validation evidence
- **LC06_Quality**: Quality assurance documentation
- **LC07_Safety**: Safety analysis and evidence
- **LC08_Certification**: Certification artifacts and compliance

## Publication Types

### AMM - Aircraft Maintenance Manual

Complete maintenance documentation including:
- System descriptions
- Maintenance procedures
- Troubleshooting guides
- Test procedures
- Component maintenance

### IPC - Illustrated Parts Catalog

Complete parts documentation including:
- Illustrated parts breakdowns
- Parts lists with nomenclature
- Part numbers and quantities
- Vendor information
- Applicability data

## CSDB Structure

Each publication type contains a **Common Source Database (CSDB)** with:
- **DM/**: Data Modules (content units)
- **PM/**: Publication Modules (structure definitions)
- **DML/**: Data Module Lists (content groupings)
- **ICN/**: Illustrations and graphics
- **BREX/**: Business rules (validation)
- **COMMON/**: Reusable content
- **APPLICABILITY/**: Product variant applicability

## Navigation

Access publication content:
- `PUB/AMM/CSDB/` - Maintenance manual content
- `PUB/IPC/CSDB/` - Parts catalog content

Each CSDB directory contains a comprehensive README explaining its structure and purpose.

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 23 (Communications)
- **Section**: 23-80-00 (Integrated Automatic Tuning)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
