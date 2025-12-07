# ROUTING — Electrical, Fluid, and Data Routing

## Purpose

This directory contains routing specifications for all electrical, fluid, and data connections between propulsion system components. Proper routing is critical for:

- System reliability and safety
- Thermal management
- EMI protection
- Maintenance access
- Weight optimization

## Structure

```
ROUTING/
├── ELECTRICAL/     # Power, control, sensor routing
├── FLUID/          # Cooling, lubrication, hydraulic routing
└── DATA/           # FADEC, health monitoring, ARINC-429 routing
```

## Hybrid-Electric Architecture

The Q100 hybrid-electric propulsion system has unique routing requirements:

### Power System

- **H2-FC-LINK**: H₂ PEM fuel cell to DC bus (650-800 VDC)
- **CO2-BATT-LINK**: CO₂ battery buffer to DC bus (peak power support)
- **POWER-MAIN**: DC bus to motor controller
- **CONTROL-BUS**: Controller to motor phases (3-phase AC)

### Thermal Management

- **COOLING-SUPPLY/RETURN**: Closed-loop cooling for motor and controller
- **LUBE-SUPPLY/SCAVENGE**: Gearbox lubrication system

### Data Systems

- **FADEC-BUS**: Full Authority Digital Engine Control
- **HEALTH-MON**: Predictive maintenance and health monitoring
- **ARINC-429**: Aircraft system integration

## Routing Standards

### Separation Requirements

| Category | Power | Control | Data | Fluid |
|----------|-------|---------|------|-------|
| Power | — | 100mm | 100mm | 50mm |
| Control | 100mm | — | 25mm | 50mm |
| Data | 100mm | 25mm | — | 50mm |
| Fluid | 50mm | 50mm | 50mm | — |

### Bend Radius (Minimum)

| Type | Radius |
|------|--------|
| High-voltage power cable | 10× diameter |
| Control cable | 6× diameter |
| Data cable | 4× diameter |
| Cooling hose | 5× diameter |
| Lube line | 5× diameter |

### Thermal Clearances

| Zone | Max Temp | Clearance |
|------|----------|-----------|
| Hot (motor housing) | 120°C | 50mm from cables |
| Warm (cooling lines) | 80°C | 25mm from cables |
| Exhaust | 150°C | 100mm from cables |

## Related Documents

- [ELECTRICAL/README.md](ELECTRICAL/README.md)
- [FLUID/README.md](FLUID/README.md)
- [DATA/README.md](DATA/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
