# CONTROLLER_ASSEMBLY

**Assembly ID**: 61-00-04-A452  
**Version**: 1.0  
**Status**: DRAFT

## Purpose

Motor controller and inverter assembly for the AMPEL360 BWB H2 Hy-E electric propulsion system. Converts DC power from the fuel cell/battery system to 3-phase AC for motor operation.

## Components

| Component | Description |
|-----------|-------------|
| Inverter Module | Power electronics (SiC or GaN devices) |
| Gate Drivers | IGBT/MOSFET gate drive circuits |
| Control Board | DSP/FPGA-based motor control logic |
| DC Link Capacitors | High-voltage DC bus filtering |
| Cooling System | Liquid-cooled cold plate |
| EMI Filters | Electromagnetic interference suppression |

## Key Specifications

| Parameter | Value |
|-----------|-------|
| Input Voltage | TBD VDC (High Voltage) |
| Output Power | TBD kW |
| Efficiency | > 98% |
| Switching Frequency | TBD kHz |
| Control Method | Field Oriented Control (FOC) |
| Protection | Over-current, over-temp, short-circuit |

## Part References

```
../../../../../PARTS/
```

## CAD Structure

```
CAD/
├── PRODUCTS/          # Native CAD assembly files
│   ├── CATIA/        # CONTROLLER_ASSY.CATProduct
│   ├── SOLIDWORKS/   # CONTROLLER_ASSY.sldasm
│   └── NX/           # CONTROLLER_ASSY.prt
├── NEUTRAL/          # CONTROLLER_ASSY.step, .jt
├── VISUALIZATION/    # Lightweight viewing files
└── RENDERS/          # Visual documentation
```

## CAD Naming Convention

```
CONTROLLER_[COMPONENT]_ASSY.[extension]
```

Examples:

- `CONTROLLER_ASSY.CATProduct` — Complete controller assembly
- `CONTROLLER_INVERTER_ASSY.sldasm` — Power stage subassembly
- `CONTROLLER_COOLING_ASSY.step` — Cooling plate (neutral)

## Interface Points

- **DC Input**: HV DC bus connection from power distribution
- **AC Output**: 3-phase power to motor
- **Control**: CAN/ARINC interface to FADEC
- **Cooling**: Coolant inlet/outlet
- **Sensors**: Motor feedback signals

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
