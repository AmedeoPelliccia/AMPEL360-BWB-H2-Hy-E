# ATA 21-50 — Cooling

## Overview

This section covers: Cooling systems including air cycle machines, vapor cycle systems, and cooling controls

## Structure

This directory contains subject-level documentation following the ATA SNS format 21-50-yy:

```
21-50-cooling/
├── 21-50-00-cooling/     # General subject
└── 21-50-YY-<subject-name>/      # Additional subjects (as needed per SNS)
```

## Subject Organization

Each subject directory contains:
- **SSOT/**: Single Source of Truth — master content repository
- **PUB/**: Publication views (AMM, IPC, etc.) with S1000D CSDB structure

## Adding New Subjects

When adding new subjects to this section (per your ATA SNS extract):

1. Create directory: `21-50-YY-<descriptive-name>/`
2. Add `SSOT/` directory for master content
3. Add `PUB/<SUB_ID>/CSDB/` structure for each publication type
4. Include CSDB subdirectories: DM, PM, DML, ICN, BREX, COMMON, APPLICABILITY
5. Add `bindings.csv` and `csdb.profile.yaml` for each publication

## References

- ATA iSpec 2200 SNS Section 21-50
- S1000D Specification for CSDB structure

## Document Control

- **Section**: ATA 21-50
- **Status**: Active
- **Last Updated**: 2026-01-08
