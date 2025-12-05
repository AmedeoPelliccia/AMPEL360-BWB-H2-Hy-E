# POWER_DISTRIBUTION_ASSEMBLY

**Assembly ID**: 61-00-04-A453  
**Version**: 1.0  
**Status**: DRAFT

## Purpose

High-voltage and low-voltage power distribution assembly for the AMPEL360 BWB H2 Hy-E electric propulsion system. Manages power routing from fuel cells and batteries to the motor controller.

## Components

| Component | Description |
|-----------|-------------|
| HV Bus Bars | High-current copper/aluminum conductors |
| HV Connectors | High-voltage rated connectors (>500V) |
| Contactors | Main power switching devices |
| Pre-charge Circuit | Inrush current limiting for DC link |
| Current Sensors | Hall-effect or shunt-based measurement |
| Fuses/Breakers | Overcurrent protection devices |

## Key Specifications

| Parameter | Value |
|-----------|-------|
| System Voltage | TBD VDC (nominal) |
| Max Current | TBD A |
| Isolation Rating | >2kV AC for 1 minute |
| Protection Class | IP67 (for exposed components) |

## Part References

```
../../../../../PARTS/
```

## CAD Structure

```
CAD/
├── PRODUCTS/          # Native CAD assembly files
│   ├── CATIA/        # POWER_DIST_ASSY.CATProduct
│   ├── SOLIDWORKS/   # POWER_DIST_ASSY.sldasm
│   └── NX/           # POWER_DIST_ASSY.prt
├── NEUTRAL/          # POWER_DIST_ASSY.step, .jt
├── VISUALIZATION/    # Lightweight viewing files
└── RENDERS/          # Visual documentation
```

## CAD Naming Convention

```
POWER_DIST_[COMPONENT]_ASSY.[extension]
```

Examples:

- `POWER_DIST_ASSY.CATProduct` — Complete power distribution assembly
- `POWER_DIST_BUSBAR_ASSY.sldasm` — Bus bar subassembly
- `POWER_DIST_PRECHARGE_ASSY.step` — Pre-charge circuit (neutral)

## Interface Points

- **Input (Fuel Cell)**: HV DC from fuel cell system (ATA 28)
- **Input (Battery)**: HV DC from CO₂ battery pack (ATA 24)
- **Output**: HV DC to motor controller
- **Control**: Contactor control signals, status feedback
- **Sensing**: Voltage, current, temperature monitoring

## Safety Considerations

- **High Voltage** — All work requires HV-trained personnel
- **Arc Flash** — Proper PPE and arc flash analysis required
- **Lockout/Tagout** — Strict isolation procedures

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
