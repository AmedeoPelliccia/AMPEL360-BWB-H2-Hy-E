# 22-00-00-auto-flight-general

## Overview

This directory contains the publication-ready content for general autoflight system technical documentation.

## Purpose

This level organizes content by publication type following S1000D standards:
- **PUB/**: Publication content organized by manual type

## Structure

```
22-00-00-auto-flight-general/
└── PUB/
    ├── AMM/    # Aircraft Maintenance Manual
    └── IPC/    # Illustrated Parts Catalog
```

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
- **ATA Chapter**: 22 (Autoflight)
- **Section**: 00-00 (General)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
