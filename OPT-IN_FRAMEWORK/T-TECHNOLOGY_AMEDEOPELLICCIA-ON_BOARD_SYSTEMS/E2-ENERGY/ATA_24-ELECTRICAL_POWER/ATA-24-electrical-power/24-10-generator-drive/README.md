# 24-10 — Generator Drive

## Overview

Mechanical/electromechanical drive chain that produces generator shaft power (or equivalent power takeoff) and its control/monitoring.

For the hydrogen-electric AMPEL360, this often maps to motor-generator coupling, gearboxes, or dedicated turbogenerators/APU-equivalent, depending on the specific architecture implementation.

## Subjects

- **24-10-00**: Generator drive overview — Introduction to drive systems
- **24-10-01**: Drive architecture & variants — IDG/CSD, starter-generator, and motor-generator sets
- **24-10-02**: Mechanical interfaces — Mounts, shafts, and gear train connections
- **24-10-03**: Control & regulation interface — Speed control and enable/inhibit logic
- **24-10-04**: Cooling/lubrication interfaces — Thermal management for drive components
- **24-10-05**: Monitoring & protections — Overspeed, overtemp, and vibration monitoring
- **24-10-06**: Maintenance & inspection tasks — Service limits and wear indicators
- **24-10-10**: Verification & qualification — Environmental, endurance, and fault injection testing
- **24-10-90**: Electric MG transient torque limits (Program Delta) — Regenerative braking and transient constraints


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

- **Section**: 24-10 — Generator Drive
- **Standard**: ATA iSpec 2200 SNS / S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **Model**: BWB-H2-Hy-E
- **Status**: Active
- **Generated with**: AI assistance (GitHub Copilot), prompted by Amedeo Pelliccia
- **Last Updated**: 2026-01-09
