# 61-20-01 Electric Motor — Models and Tables Directory

This directory contains lookup tables, data schemas, and diagrams for the Electric Motor (61-20-01) subsystem.

## Directory Structure

```
61-20-01_07_001_Models_Tables/
├── README.md (this file)
├── tables/
│   ├── lookup-table-torque-speed.csv
│   ├── lookup-table-efficiency.csv
│   └── lookup-table-thermal.csv
└── diagrams/
    ├── schema-electrical.svg
    └── schema-thermal.svg
```

## Tables

| Table | Description | Format |
|-------|-------------|--------|
| `lookup-table-torque-speed.csv` | Torque vs. speed characteristic | CSV |
| `lookup-table-efficiency.csv` | Efficiency map | CSV |
| `lookup-table-thermal.csv` | Thermal resistance network | CSV |

## Diagrams

| Diagram | Description | Format |
|---------|-------------|--------|
| `schema-electrical.svg` | Electrical equivalent circuit | SVG |
| `schema-thermal.svg` | Thermal network schematic | SVG |

## Data Sources

Primary data derived from:
- `61-20-01_02_001_TorqueSpeed.csv`
- `61-20-01_02_002_EfficiencyMap.csv`
- Engineering analysis models

## Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Last Updated:** 2025-12-01
