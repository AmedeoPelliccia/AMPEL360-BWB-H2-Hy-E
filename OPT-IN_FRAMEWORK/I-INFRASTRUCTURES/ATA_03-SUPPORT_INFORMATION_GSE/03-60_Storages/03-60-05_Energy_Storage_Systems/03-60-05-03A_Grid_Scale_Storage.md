# 03-60-05-03A - Grid Scale Storage

## 1. Purpose
This document specifies requirements for grid-scale energy storage systems that support airport operations, renewable energy integration, and electrical grid stabilization.

## 2. Scope
This document covers:
- Large-scale battery energy storage systems (BESS)
- Hydrogen-based grid storage
- Integration with renewable energy sources
- Grid services and demand response
- Economic optimization and revenue streams

## 3. Applicable Documents
- NFPA 855 (Stationary Energy Storage Systems)
- UL 9540 (Energy Storage Systems)
- IEEE 1547 (Distributed Energy Resources)
- FERC Order 841 (Energy Storage Participation)
- IEC 61850 (Power System Communication)

## 4. Storage Description

### 4.1 Overview
Grid-scale energy storage provides large-capacity energy buffering for airport operations, enabling renewable energy integration, peak demand reduction, and grid services participation. These systems operate at MW scale with MWh of storage capacity.

### 4.2 Specifications

#### Storage Technology Comparison
| Technology | Power | Duration | Efficiency | Application |
|------------|-------|----------|------------|-------------|
| Li-ion BESS | 1-50 MW | 1-4 hours | 85-95% | Frequency regulation, peak shaving |
| Flow Battery | 1-10 MW | 4-10 hours | 70-80% | Long duration, high cycles |
| H2 Storage + FC | 1-5 MW | Days-weeks | 30-40% | Seasonal storage, backup |

#### System Sizing Example
For medium airport (50 MW peak demand):
- **BESS Capacity**: 10 MW / 40 MWh
- **Peak Shaving**: Reduce peak by 20% (10 MW)
- **Discharge Duration**: 4 hours at full power
- **Cycling**: 1-2 cycles per day (365-730 cycles/year)
- **Lifetime**: 10-15 years (7,000-10,000 cycles)

### 4.3 Capacity and Requirements

#### Electrical Integration
- **Grid Connection**: 13.8 kV or higher
- **Power Conditioning**: Bi-directional inverters
- **Transformer**: Isolated, pad-mounted
- **Protection**: IEEE C37 relay protection
- **SCADA**: Real-time monitoring and dispatch

#### Grid Services Revenue Streams
- **Frequency Regulation**: $10-50/kW-year
- **Demand Charge Reduction**: $5-15/kW-month
- **Energy Arbitrage**: $0.05-0.15/kWh spread
- **Renewable Firming**: Contract-based
- **Capacity Market**: Varies by region

## 5. Safety Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Fire Protection | NFPA 855 | Automatic suppression, 3-hour fire rating |
| Thermal Management | UL 9540, UL 9540A | Active cooling, thermal monitoring |
| Arc Flash Protection | NFPA 70E | PPE, working clearances |
| Emergency Shutdown | NFPA 855 | Remote and local E-stop |

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-60-05-01A (Battery Storage Systems) - Technology details
  - ATA 03-60-05-02A (H2 Energy Storage) - Long-duration storage
  - ATA 24 (Electrical Power) - Power system integration
- Parent Document: 03-60_Storages

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-08_.
