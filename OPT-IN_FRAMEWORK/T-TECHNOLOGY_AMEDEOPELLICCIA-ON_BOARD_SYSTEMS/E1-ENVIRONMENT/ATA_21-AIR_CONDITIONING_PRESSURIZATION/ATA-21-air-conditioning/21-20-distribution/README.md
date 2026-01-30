# ATA 21-20 — Distribution

## Overview

This section covers: Air distribution systems, ducts, manifolds, and distribution controls

## Structure

This directory contains subject-level documentation following the ATA SNS format 21-20-yy:

```
21-20-distribution/
├── 21-20-00-distribution/     # General subject
└── 21-20-YY-<subject-name>/      # Additional subjects (as needed per SNS)
```

## Subject Organization

Each subject directory contains:
- **SSOT/**: Single Source of Truth — master content repository
- **PUB/**: Publication views (AMM, IPC, etc.) with S1000D CSDB structure

## Adding New Subjects

When adding new subjects to this section (per your ATA SNS extract):

1. Create directory: `21-20-YY-<descriptive-name>/`
2. Add `SSOT/` directory for master content
3. Add `PUB/<SUB_ID>/CSDB/` structure for each publication type
4. Include CSDB subdirectories: DM, PM, DML, ICN, BREX, COMMON, APPLICABILITY
5. Add `bindings.csv` and `csdb.profile.yaml` for each publication

## References

- ATA iSpec 2200 SNS Section 21-20
- S1000D Specification for CSDB structure

## Document Control

- **Section**: ATA 21-20
- **Status**: Active
- **Last Updated**: 2026-01-08
