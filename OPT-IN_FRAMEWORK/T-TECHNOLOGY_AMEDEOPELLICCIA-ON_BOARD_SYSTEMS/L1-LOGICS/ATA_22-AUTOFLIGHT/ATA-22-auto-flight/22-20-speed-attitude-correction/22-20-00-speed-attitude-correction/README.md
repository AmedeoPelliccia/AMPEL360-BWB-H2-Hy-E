# ATA 22-20-00 — Speed–Attitude Correction

## Overview

This is the general subject for ATA 22-20, containing common information applicable across all Speed-Attitude Correction systems.

## Directory Structure

```
22-20-00-speed-attitude-correction/
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
- Master source files for speed-attitude correction
- Control algorithms and logic
- Energy state management specifications
- Integration with propulsion systems

## PUB (Publication Views)

The PUB directory contains publication-specific views:

### AMM (Aircraft Maintenance Manual)
Documentation for speed-attitude correction maintenance, testing, and troubleshooting.

### IPC (Illustrated Parts Catalog)
Illustrated parts breakdown for speed-attitude correction components.

## Configuration Files

### bindings.csv
Example format:
```csv
publication_module,data_module,sequence,applicability
PM-22-20-00-001,DM-22-20-00-001,1,ALL
PM-22-20-00-001,DM-22-20-00-002,2,ALL
```

### csdb.profile.yaml
Example format:
```yaml
profile:
  ata_chapter: "22-20"
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

- **Subject**: ATA 22-20-00
- **Status**: Active
- **Standard**: ATA iSpec 2200 SNS / S1000D
- **Last Updated**: 2026-01-08
