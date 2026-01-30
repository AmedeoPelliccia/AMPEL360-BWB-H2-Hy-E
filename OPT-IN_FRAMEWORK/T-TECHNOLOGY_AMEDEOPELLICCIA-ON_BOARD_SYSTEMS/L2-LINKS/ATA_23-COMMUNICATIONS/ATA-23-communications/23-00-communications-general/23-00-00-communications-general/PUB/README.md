# PUB — Publication Views

## Purpose

This directory contains publication-specific views of the content, organized by manual type and formatted according to S1000D standards.

## Structure

```
PUB/
├── AMM/                    # Aircraft Maintenance Manual
│   ├── CSDB/              # Common Source Database
│   ├── EXPORT/            # Export outputs
│   ├── bindings.csv       # Publication bindings
│   └── csdb.profile.yaml  # CSDB profile configuration
└── IPC/                    # Illustrated Parts Catalog
    ├── CSDB/              # Common Source Database
    ├── EXPORT/            # Export outputs
    ├── bindings.csv       # Publication bindings
    └── csdb.profile.yaml  # CSDB profile configuration
```

## Publication Types

### AMM - Aircraft Maintenance Manual

The Aircraft Maintenance Manual provides complete maintenance documentation:
- System descriptions and operation
- Maintenance procedures
- Troubleshooting procedures
- Inspection requirements
- Test and adjustment procedures
- Removal and installation procedures

**Target Audience**: Maintenance technicians, engineers

### IPC - Illustrated Parts Catalog

The Illustrated Parts Catalog provides complete parts information:
- Illustrated parts breakdowns
- Parts lists with nomenclature
- Part numbers and quantities
- Vendor/supplier information
- Applicability and effectivity data

**Target Audience**: Parts planning, supply chain, maintenance planners

## CSDB — Common Source Database

Each publication type has its own **Common Source Database** (CSDB) containing S1000D-compliant data modules and support files.

See the CSDB directory README for detailed information about:
- Data module structure
- Publication module organization
- Illustration management
- Business rules
- Applicability management

## Configuration Files

### bindings.csv

Defines the bindings between SSOT content and S1000D data modules:
- SSOT file paths
- Corresponding data module codes
- Transformation rules
- Metadata mappings

### csdb.profile.yaml

CSDB configuration profile defining:
- Project-specific S1000D settings
- Data module code schema
- Publication module structure
- Validation rules
- Export settings

## Export Directory

The EXPORT directory contains final deliverable outputs:
- PDF documents
- Interactive Electronic Technical Publications (IETP)
- Web-based publications
- Other delivery formats as required

## Workflow

1. **Author**: Content is authored in SSOT
2. **Transform**: SSOT content is transformed into S1000D data modules in CSDB
3. **Validate**: Data modules are validated against BREX rules
4. **Publish**: Publication modules assemble data modules into publications
5. **Export**: Final outputs are generated in EXPORT directory

## Navigation

- `AMM/CSDB/` - Aircraft Maintenance Manual data modules
- `IPC/CSDB/` - Illustrated Parts Catalog data modules
- `AMM/EXPORT/` - AMM deliverable outputs
- `IPC/EXPORT/` - IPC deliverable outputs

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
