# ATA 22-00-00 — Auto Flight General

## Overview

This is the general subject for ATA 22-00, containing common information applicable across all Auto Flight systems.

## Directory Structure

```
22-00-00-auto-flight-general/
├── SSOT/                           # Single Source of Truth
│   └── (Master content goes here)
└── PUB/                            # Publication views
    ├── AMM/                        # Aircraft Maintenance Manual
    │   ├── CSDB/                   # S1000D Common Source Database
    │   │   ├── DM/                 # Data Modules
    │   │   ├── PM/                 # Publication Modules
    │   │   ├── DML/                # Data Module Lists
    │   │   ├── ICN/                # Illustrations/Graphics
    │   │   ├── BREX/               # Business Rules Exchange
    │   │   ├── COMMON/             # Common information sets
    │   │   └── APPLICABILITY/      # Applicability statements
    │   ├── EXPORT/                 # Export outputs (PDF, HTML, etc.)
    │   ├── bindings.csv            # Publication bindings configuration
    │   └── csdb.profile.yaml       # CSDB profile settings
    └── IPC/                        # Illustrated Parts Catalog
        └── (same structure as AMM)
```

## SSOT (Single Source of Truth)

The SSOT directory contains:
- Master source files
- Unprocessed content
- Source data before publication transformation
- Lifecycle documentation references

## PUB (Publication Views)

The PUB directory contains publication-specific views:

### AMM (Aircraft Maintenance Manual)
Documentation for maintenance, inspection, troubleshooting procedures, and operational guidelines.

### IPC (Illustrated Parts Catalog)
Illustrated parts breakdown and identification for Auto Flight components.

### Adding More Publications
Additional publication types can be added as needed:
- **WDM**: Wiring Diagram Manual
- **CMM**: Component Maintenance Manual
- **FIM**: Fault Isolation Manual
- **SRM**: Structural Repair Manual

## S1000D CSDB Organization

Each publication's CSDB follows the S1000D standard:

- **DM**: Data modules containing specific maintenance tasks or descriptions
- **PM**: Publication modules defining the structure of publications
- **DML**: Data module lists organizing groups of data modules
- **ICN**: Illustrations, graphics, and multimedia content
- **BREX**: Business rules for content validation
- **COMMON**: Reusable content snippets and information sets
- **APPLICABILITY**: Product variant and configuration applicability

## Configuration Files

### bindings.csv
Defines the relationship between data modules and publication structure.

Example format:
```csv
publication_module,data_module,sequence,applicability
PM-22-00-00-001,DM-22-00-00-001,1,ALL
PM-22-00-00-001,DM-22-00-00-002,2,ALL
```

### csdb.profile.yaml
CSDB profile configuration for this subject.

Example format:
```yaml
profile:
  ata_chapter: "22-00"
  subject: "00"
  publication_type: "AMM"
  language: "en-US"
  issue_date: "2026-01-08"
  
validation:
  s1000d_version: "5.0"
  schema_location: "schemas/S1000D_5-0"
  
processing:
  output_formats: ["pdf", "html5", "xml"]
  stylesheet: "default"
```

## Document Control

- **Subject**: ATA 22-00-00
- **Status**: Active
- **Standard**: ATA iSpec 2200 SNS / S1000D
- **Last Updated**: 2026-01-08
