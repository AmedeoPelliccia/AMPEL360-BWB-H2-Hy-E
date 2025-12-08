# 03-80-03-04A - Emergency Power Systems

## 1. Purpose
This document specifies emergency and backup power systems for Ground Support Equipment (GSE) operations to ensure continuity during grid outages and emergencies.

## 2. Scope
This specification covers:
- Standby generators (diesel, natural gas, H2)
- Uninterruptible Power Supply (UPS) systems
- Emergency power distribution
- Automatic transfer switching
- Critical load prioritization
- Testing and maintenance requirements

## 3. Applicable Documents
- ISO 8528 (Reciprocating Internal Combustion Engine Driven Alternating Current Generating Sets)
- NFPA 110 (Standard for Emergency and Standby Power Systems)
- IEC 62040 (Uninterruptible Power Systems)
- NFPA 111 (Standard on Stored Electrical Energy Emergency and Standby Power Systems)
- IEEE 446 (Recommended Practice for Emergency and Standby Power Systems)

## 4. Energy System Description

### 4.1 Overview
Emergency power systems provide backup electrical power to maintain critical GSE operations during utility grid failures, ensuring safety, security, and continuity of essential services.

### 4.2 Specifications
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Backup Generator Capacity | 500 kW - 5 MW | Based on critical load |
| UPS Capacity | 10 kW - 500 kW | For short-duration backup |
| Transfer Time | <10 seconds (generator), <1 ms (UPS) | Load dependent |
| Runtime | 24-72 hours (generator), 15-30 min (UPS) | With on-site fuel |
| Reliability | 99.9% availability | With proper maintenance |

### 4.3 Performance Requirements

#### 4.3.1 Standby Generators
- **Start-up Time**: <10 seconds from signal to rated power
- **Load Acceptance**: Full load in single step or multiple steps
- **Voltage Regulation**: ±5% steady-state, ±20% transient
- **Frequency Stability**: ±1 Hz steady-state, ±5% transient
- **Runtime**: Minimum 24 hours at full load with on-site fuel storage

#### 4.3.2 UPS Systems
- **Transfer Time**: <1 ms (no-break design)
- **Backup Time**: 15-30 minutes (bridging until generator starts)
- **Efficiency**: >95% in double-conversion mode
- **Battery Technology**: VRLA or Li-ion batteries
- **Scalability**: Modular design for capacity expansion

### 4.4 Emergency Power Technologies

#### 4.4.1 Diesel Generators
- Proven technology, high reliability
- Fast start-up and load acceptance
- Suitable for long-duration backup
- Emissions: Requires aftertreatment for compliance

#### 4.4.2 Natural Gas Generators
- Lower emissions than diesel
- Continuous fuel supply (if connected to gas grid)
- Slightly slower start-up than diesel
- Not dependent on on-site fuel storage

#### 4.4.3 H2 Generators (Emerging)
- Zero emissions (fuel cell or H2 combustion)
- Requires H2 infrastructure
- Higher initial cost
- Future technology for sustainable backup power

### 4.5 Critical Load Identification and Prioritization

**Priority 1 - Life Safety**:
- Emergency lighting and exit signs
- Fire detection and suppression systems
- Communication systems

**Priority 2 - Critical Operations**:
- Fuel/H2 pumping and refueling systems
- Essential GSE charging stations
- Control center and communications
- Security systems

**Priority 3 - Important Operations**:
- Non-essential GSE charging
- Office and facility lighting
- HVAC for control rooms

## 5. Safety and Environmental Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Generator Safety | ISO 8528, NFPA 110 | Design, installation, testing per standards |
| UPS Safety | IEC 62040, NFPA 111 | Electrical safety, battery management |
| Fuel Storage | NFPA 30, NFPA 110 | Diesel/gasoline storage safety |
| Emissions | EPA, EURO standards | Generator emissions compliance |
| Fire Protection | NFPA 110, local fire codes | Fire detection and suppression |

## 6. Cross-References
- Related ATA Chapters: ATA 03 (Support Information/GSE)
- Parent Document: 03-80_Energy
- Grid Power Supply: 03-80-03-01A_Grid_Power_Supply
- Power Distribution: 03-80-03-03A_Power_Distribution
- H2 Energy Systems: 03-80-02_H2_Energy_Systems

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 GSE Energy WG | Initial release |

---

## Document Control

- **Status**: DRAFT – Subject to review and approval
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Energy Working Group
- **Next Review**: 2026-03-08
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-08

---
