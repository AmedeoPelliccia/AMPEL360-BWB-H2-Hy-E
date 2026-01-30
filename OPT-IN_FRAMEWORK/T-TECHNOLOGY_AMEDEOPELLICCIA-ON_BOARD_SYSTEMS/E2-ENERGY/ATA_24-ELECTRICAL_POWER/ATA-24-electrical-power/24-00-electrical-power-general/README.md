# 24-00 — Electrical Power General

## Overview

Chapter-level scope, electrical architecture philosophy (including H₂ fuel cell + battery buffering), domains, redundancy, dispatch, and certification/verification framing.

This section establishes the foundation for the entire ATA 24 documentation set, defining the overall electrical power system architecture for the AMPEL360 hydrogen-electric aircraft.

## Subjects

- **24-00-00**: Chapter overview — High-level introduction to the electrical power system
- **24-00-01**: Scope & boundaries — Defines boundaries between ATA 24 and related chapters (21/28/45/46)
- **24-00-02**: Electrical architecture overview — AC/LVDC/HVDC architecture concept and philosophy
- **24-00-03**: Power quality & limits — Voltage, frequency, ripple, and THD specifications
- **24-00-04**: Load classification — Essential, sheddable, and non-essential load categories
- **24-00-05**: Redundancy & dispatch philosophy — Fail-operational and fail-safe design principles
- **24-00-06**: Interfaces & dependencies — Connections to fuel cells, batteries, converters, and propulsion
- **24-00-07**: Monitoring & BITE overview — Built-in test and health monitoring strategy
- **24-00-08**: Safety & compliance basis — Arc fault protection, HV hazards, and certification basis
- **24-00-10**: Verification strategy — Analysis, test, and inspection approach
- **24-00-90**: Fuel-cell transient constraints & buffering (Program Delta) — Unique constraints from hydrogen fuel cell power sources
- **24-00-91**: HV architecture & EMI environment (Program Delta) — High-voltage DC system considerations
- **24-00-92**: Thermal/power derating coordination (Program Delta) — Coordinated thermal and electrical management


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

- **Section**: 24-00 — Electrical Power General
- **Standard**: ATA iSpec 2200 SNS / S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **Model**: BWB-H2-Hy-E
- **Status**: Active
- **Generated with**: AI assistance (GitHub Copilot), prompted by Amedeo Pelliccia
- **Last Updated**: 2026-01-09
