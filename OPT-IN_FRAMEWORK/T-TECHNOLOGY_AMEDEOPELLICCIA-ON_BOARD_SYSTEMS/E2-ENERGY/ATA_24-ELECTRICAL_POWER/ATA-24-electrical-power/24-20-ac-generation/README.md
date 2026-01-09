# 24-20 — AC Generation

## Overview

AC generation sources and conditioning (variable frequency vs constant frequency, inverter-based AC, regulation, paralleling rules).

This section covers the generation, regulation, and distribution of alternating current power throughout the aircraft, with particular attention to inverter-based systems common in hydrogen-electric architectures.

## Subjects

- **24-20-00**: AC generation overview — Introduction to AC power generation systems
- **24-20-01**: AC sources — Main generators, APU/auxiliary, and emergency sources
- **24-20-02**: Regulation & control — Voltage and frequency regulation strategies
- **24-20-03**: Paralleling / transfer logic — Multiple source synchronization and transfer
- **24-20-04**: AC power quality — Harmonics, transients, and ride-through requirements
- **24-20-05**: Protections — Over/under voltage/frequency, differential, ground fault
- **24-20-07**: BITE & fault isolation — Built-in test and fault detection systems
- **24-20-10**: Verification — Power quality, load step, and EMC testing
- **24-20-90**: Inverter-dominated grid stability (Program Delta) — AC microgrid behavior and grid-forming control


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

- **Section**: 24-20 — AC Generation
- **Standard**: ATA iSpec 2200 SNS / S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **Model**: BWB-H2-Hy-E
- **Status**: Active
- **Generated with**: AI assistance (GitHub Copilot), prompted by Amedeo Pelliccia
- **Last Updated**: 2026-01-09
