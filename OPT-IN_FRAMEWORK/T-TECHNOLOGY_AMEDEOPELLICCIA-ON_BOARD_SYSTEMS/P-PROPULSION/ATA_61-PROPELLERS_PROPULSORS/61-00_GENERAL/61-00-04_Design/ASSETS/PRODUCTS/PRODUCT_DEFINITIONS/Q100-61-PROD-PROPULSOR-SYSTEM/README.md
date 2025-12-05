# Q100-61-PROD-PROPULSOR-SYSTEM — Integrated Propulsion System

**Product ID**: Q100-61-PROD-PROPULSOR-SYSTEM  
**Version**: 1.0  
**Status**: DRAFT  
**Level**: Top-Level Product

## Purpose

The Q100-61-PROD-PROPULSOR-SYSTEM is the top-level integrated propulsion system product for the AMPEL360 BWB H2 Hy-E hybrid-electric aircraft. It represents the complete, flight-ready propulsor unit including all sub-products, configured for aircraft integration.

## System Architecture

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                     Q100-61-PROD-PROPULSOR-SYSTEM                            │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────┐                 ┌─────────────────────┐            │
│  │  Q100-61-PROD-      │                 │  Q100-61-PROD-      │            │
│  │  OPEN-FAN-UNIT      │◄───Mechanical───┤  GEARBOX-UNIT       │            │
│  │                     │    Coupling     │                     │            │
│  │  • Fan blades       │                 │  • Reduction gear   │            │
│  │  • Hub/spinner      │                 │  • Bearings         │            │
│  │  • Pitch control    │                 │  • Lubrication      │            │
│  └─────────────────────┘                 └─────────┬───────────┘            │
│                                                    │                         │
│  ┌─────────────────────┐                 ┌────────▼────────────┐            │
│  │  Q100-61-PROD-      │                 │  Q100-61-PROD-      │            │
│  │  NACELLE-UNIT       │                 │  ELECTRIC-DRIVE-UNIT│            │
│  │                     │                 │                     │            │
│  │  • Inlet cowl       │                 │  • Electric motor   │            │
│  │  • Fan cowl         │                 │  • Inverter/rectifier│            │
│  │  • Thrust reverser  │                 │  • Cooling system   │            │
│  │  • Acoustic liners  │                 │  • HV distribution  │            │
│  └─────────────────────┘                 └─────────┬───────────┘            │
│                                                    │                         │
│  ┌─────────────────────────────────────────────────▼───────────────────────┐│
│  │  Q100-61-PROD-CONTROLLER-UNIT                                           ││
│  │  • FADEC (Full Authority Digital Engine Control)                        ││
│  │  • Motor control algorithms                                              ││
│  │  • Power management                                                      ││
│  │  • Health monitoring                                                     ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Power Architecture

The propulsor system receives power from the aircraft's hybrid-electric power system:

- **Primary Source**: H₂ PEM Fuel Cells (2× 250 kW nominal)
- **Peak Power Buffer**: Closed-loop CO₂ Battery
- **Distribution**: 800 VDC high-voltage bus
- **SAF Backup**: Sustainable Aviation Fuel capability (APU mode)

## Key Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Maximum Thrust | 85 | kN | Sea level, ISA |
| Cruise Thrust | 35 | kN | FL350, M0.78 |
| Motor Power (Continuous) | 1,000 | kW | 2× 500 kW motors |
| Motor Power (Peak) | 1,200 | kW | 30-second rating |
| Fan Diameter | 2.8 | m | Open-fan configuration |
| Effective Bypass Ratio | 25:1 | — | Open-fan equivalent |
| Propulsor Efficiency | 92 | % | At cruise condition |
| System Weight (Dry) | 1,850 | kg | Including nacelle |
| Noise Level | TBD | EPNdB | Per ICAO Chapter 14 |

## Sub-Products

| Product ID | Name | Quantity | Description |
|------------|------|----------|-------------|
| Q100-61-PROD-OPEN-FAN-UNIT | Open Fan Unit | 1 | Open-fan rotor assembly |
| Q100-61-PROD-ELECTRIC-DRIVE-UNIT | Electric Drive Unit | 1 | Dual motor system |
| Q100-61-PROD-GEARBOX-UNIT | Gearbox Unit | 1 | Reduction gearbox |
| Q100-61-PROD-NACELLE-UNIT | Nacelle Unit | 1 | Nacelle structure |
| Q100-61-PROD-CONTROLLER-UNIT | Controller Unit | 1 | FADEC and controls |

## Interfaces

### Aircraft Interfaces (ATA 71 — Power Plant)

| Interface | Type | Description |
|-----------|------|-------------|
| IF-61-001 | Mechanical | Pylon/mounting attachment |
| IF-61-002 | Electrical | 800 VDC power input |
| IF-61-003 | Data | ARINC 429 / CAN-FD control bus |
| IF-61-004 | Fluid | Cooling loop connection |
| IF-61-005 | Fluid | Fire suppression (ATA 26) |

### Related ATA Chapters

| ATA | System | Interface |
|-----|--------|-----------|
| ATA 24 | Electrical Power | HV power distribution |
| ATA 26 | Fire Protection | Fire suppression |
| ATA 45 | Health Monitoring | Vibration and performance data |
| ATA 71 | Power Plant | Physical integration |
| ATA 76 | Engine Controls | FADEC interface |

## Certification Targets

- **EASA CS-E** — Engine certification specifications
- **FAA FAR Part 33** — Airworthiness standards for engines
- **EASA CS-25.1309** — Equipment, systems, and installations
- **ICAO Annex 16, Vol. I** — Aircraft noise
- **ICAO Annex 16, Vol. II** — Aircraft engine emissions

## Configuration Baseline

- **Baseline Configuration**: [Q100-61-CFG-PROPULSOR-BASELINE.yaml](configuration/Q100-61-CFG-PROPULSOR-BASELINE.yaml)
- **Master Configuration Index**: [Q100-61-CFG-MASTER-INDEX.yaml](../../PRODUCT_CONFIGURATIONS/Q100-61-CFG-MASTER-INDEX.yaml)

## Bill of Materials

- **Product BOM**: [Q100-61-BOM-PROPULSOR-SYSTEM](../../BILL_OF_MATERIALS/Q100-61-BOM-PROPULSOR-SYSTEM/)

## Traceability

- **Requirements**: `../../../61-00-03_Requirements/`
- **Safety Analysis**: `../../../61-00-02_Safety/`
- **Verification**: `../../../61-00-07_V_AND_V/`
- **Interfaces**: `../../../61-00-05_Interfaces/`

## Related Documents

- [Product Definition YAML](product_definition.yaml)
- [Product Structure YAML](product_structure.yaml)
- [Product Specifications](../../PRODUCT_SPECIFICATIONS/README.md)
- [Certification Evidence](../../CERTIFICATION/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
