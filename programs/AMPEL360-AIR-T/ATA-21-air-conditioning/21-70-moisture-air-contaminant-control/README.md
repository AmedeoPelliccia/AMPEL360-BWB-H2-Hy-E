# ATA 21-70 — Moisture Air Contaminant Control

## Overview

This section covers: Moisture control, dehumidification, air filtration, and contaminant removal systems

## Structure

This directory contains subject-level documentation following the ATA SNS format 21-70-yy:

```
21-70-moisture-air-contaminant-control/
├── 21-70-00-moisture-air-contaminant-control/     # General subject
└── 21-70-YY-<subject-name>/      # Additional subjects (as needed per SNS)
```

## Subject Organization

Each subject directory contains:
- **SSOT/**: Single Source of Truth — master content repository
- **PUB/**: Publication views (AMM, IPC, etc.) with S1000D CSDB structure

## Adding New Subjects

When adding new subjects to this section (per your ATA SNS extract):

1. Create directory: `21-70-YY-<descriptive-name>/`
2. Add `SSOT/` directory for master content
3. Add `PUB/<SUB_ID>/CSDB/` structure for each publication type
4. Include CSDB subdirectories: DM, PM, DML, ICN, BREX, COMMON, APPLICABILITY
5. Add `bindings.csv` and `csdb.profile.yaml` for each publication

## References

- ATA iSpec 2200 SNS Section 21-70
- S1000D Specification for CSDB structure

## Document Control

- **Section**: ATA 21-70
- **Status**: Active
- **Last Updated**: 2026-01-08
