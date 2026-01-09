# 24-30 — DC Generation

## Overview

DC generation and conversion chain (rectifiers, DC/DC, HVDC buses, battery charging, fuel cell DC coupling).

This section is particularly critical for hydrogen-electric aircraft, as fuel cells produce DC power directly. Covers conversion stages, battery integration, and high-voltage DC distribution.

## Subjects

- **24-30-00**: DC generation overview — Introduction to DC power generation and conversion
- **24-30-01**: DC sources — Fuel cell stacks, rectified AC, and battery systems
- **24-30-02**: Conversion stages — Rectification, DC/DC conversion, and isolation
- **24-30-03**: Battery charging & energy buffering control — Battery management and power smoothing
- **24-30-04**: DC quality — Ripple, transients, and bus stability
- **24-30-05**: Protections — Over/under voltage/current, arc fault, insulation monitoring
- **24-30-07**: BITE & diagnostics — Built-in test for DC systems
- **24-30-10**: Verification — Bus stability, load steps, thermal, and EMC testing
- **24-30-90**: HVDC insulation monitoring & fault containment (Program Delta) — High-voltage DC safety systems


## Structure

Each subject in this section contains:

```
24-xx-yy-<subject-name>/
├── SSOT/                           # Single Source of Truth
│   └── README.md                   # SSOT documentation
└── PUB/                            # Publication views
    ├── AMM/                        # Aircraft Maintenance Manual
    │   ├── CSDB/                   # S1000D Common Source Database
    │   │   └── README.md
    │   ├── bindings.csv            # Publication bindings
    │   └── csdb.profile.yaml       # CSDB profile
    └── IPC/                        # Illustrated Parts Catalog
        ├── CSDB/
        │   └── README.md
        ├── bindings.csv
        └── csdb.profile.yaml
```

## SSOT Workflow

1. **Author**: Create/edit content in SSOT/
2. **Transform**: Apply publication-specific transformations
3. **Publish**: Generate S1000D data modules in PUB/CSDB
4. **Export**: Create final deliverables in PUB/EXPORT

## S1000D Compliance

All publication outputs follow:
- **S1000D Issue 5.0** specification
- **ATA iSpec 2200** chapter numbering
- **AMPEL360** project-specific BREX rules

## Related Sections

### Within ATA 24
- [24-00 General](../24-00-electrical-power-general/)
- [24-10 Generator Drive](../24-10-generator-drive/)
- [24-20 AC Generation](../24-20-ac-generation/)
- [24-30 DC Generation](../24-30-dc-generation/)
- [24-40 External Power](../24-40-external-power/)
- [24-50 AC Load Distribution](../24-50-ac-electrical-load-distribution/)
- [24-60 DC Load Distribution](../24-60-dc-electrical-load-distribution/)
- [24-70 Primary & Secondary Power](../24-70-primary-and-secondary-power/)

### OPT-IN Framework
- [24-00_GENERAL](../../24-00_GENERAL/) — Lifecycle documentation
- [24-20_Subsystems](../../24-20_Subsystems/) — Subsystem design
- [24-80_Energy](../../24-80_Energy/) — Energy management

## References

- [ATA 24 Index](../00_INDEX.md)
- [ATA 24 README](../README.md)
- [ATA iSpec 2200 SNS](https://publications.airlines.org/products/ispec-2200-extract-ata-standard-numbering-system-revision-2024-1)
- S1000D Issue 5.0 Specification

## Document Control

- **Section**: 24-30 — DC Generation
- **Standard**: ATA iSpec 2200 SNS / S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **Model**: BWB-H2-Hy-E
- **Status**: Active
- **Generated with**: AI assistance (GitHub Copilot), prompted by Amedeo Pelliccia
- **Last Updated**: 2026-01-09
