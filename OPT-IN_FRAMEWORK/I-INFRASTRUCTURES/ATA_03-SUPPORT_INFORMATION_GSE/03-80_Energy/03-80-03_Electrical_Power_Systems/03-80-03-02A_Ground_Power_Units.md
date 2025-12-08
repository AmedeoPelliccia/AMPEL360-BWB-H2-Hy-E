# 03-80-03-02A - Ground Power Units

## 1. Purpose
This document specifies Ground Power Units (GPUs) used to provide electrical power to aircraft during ground operations, including both conventional and advanced power generation technologies.

## 2. Scope
This specification covers:
- Fixed and mobile GPUs
- Power generation technologies (diesel, H2, fuel cell, battery)
- Power output specifications
- Aircraft interface requirements
- Environmental and noise considerations
- Integration with airport energy systems

## 3. Applicable Documents
- SAE AS6858 (400 Hz Electrical Ground Support Equipment)
- ISO 6858 (Aircraft Ground Support Equipment - Electrical Supplies)
- MIL-STD-704 (Aircraft Electric Power Characteristics)
- ISO 8528 (Reciprocating Internal Combustion Engine Driven Alternating Current Generating Sets)
- IEC 60204-1 (Safety of Machinery - Electrical Equipment)

## 4. Energy System Description

### 4.1 Overview
Ground Power Units provide 400 Hz AC electrical power to parked aircraft, replacing aircraft APU operation and reducing fuel consumption, emissions, and noise during ground operations.

### 4.2 Specifications
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Output Voltage | 115V AC (single-phase), 115/200V AC (three-phase) | Per MIL-STD-704 |
| Output Frequency | 400 Hz ±1 Hz | Aircraft standard |
| Power Rating | 30-180 kVA | Varies by aircraft type |
| Voltage Regulation | ±1% of nominal | Tight regulation for avionics |
| Frequency Stability | ±0.5 Hz | Critical for aircraft systems |
| THD | <3% | Low distortion requirement |

### 4.3 Performance Requirements

#### 4.3.1 Electrical Performance
- **Power Quality**: Meet MIL-STD-704 requirements for aircraft power
- **Load Response**: <3 cycles transient for 50-100% load step
- **Parallel Operation**: Multiple GPUs can be synchronized (for large aircraft)
- **Soft Start**: Gradual voltage ramp-up to protect aircraft systems

#### 4.3.2 Operational Performance
- **Start-up Time**: <60 seconds from off to ready for connection
- **Runtime**: Continuous operation for typical turnaround (1-3 hours)
- **Fuel/Energy Efficiency**: Optimize for low consumption and emissions
- **Noise Level**: <65 dB(A) at 7m distance (for conventional GPUs)
- **Availability**: >98% operational availability

### 4.4 GPU Technologies

#### 4.4.1 Conventional Diesel GPUs
**Technology**: Diesel engine driving 400 Hz alternator

**Characteristics**:
- Power: 30-180 kVA
- Fuel consumption: 6-20 L/hour depending on load
- Emissions: CO2, NOx, PM per diesel engine standards
- Noise: 60-75 dB(A) at 7m

**Applications**: Legacy fleet, locations without advanced infrastructure

#### 4.4.2 Hybrid Diesel-Battery GPUs
**Technology**: Diesel engine + battery energy storage

**Benefits**:
- Reduced fuel consumption (up to 50%)
- Lower emissions and noise
- Battery provides peak power, diesel charges battery

#### 4.4.3 Battery-Electric GPUs
**Technology**: Battery energy storage + inverter

**Characteristics**:
- Power: 30-90 kVA (typical for narrowbody aircraft)
- Battery capacity: 100-200 kWh
- Runtime: 1-3 hours per charge
- Charging time: 1-2 hours (fast charging)
- Emissions: Zero local emissions
- Noise: <50 dB(A) (very quiet)

**Advantages**:
- Zero emissions at point of use
- Very low noise
- Low operating cost
- Simplified maintenance

**Limitations**:
- Limited runtime per charge
- Requires charging infrastructure
- Higher initial cost

#### 4.4.4 Fuel Cell GPUs
**Technology**: H2 fuel cell + power conditioning

**Characteristics**:
- Power: 30-180 kVA
- Fuel: Compressed H2 (350-700 bar)
- Efficiency: 40-50% (electrical)
- Emissions: Zero (only water vapor)
- Noise: <55 dB(A)

**Advantages**:
- Zero emissions
- Low noise
- Fast refueling (similar to diesel)
- No runtime limitation (with adequate H2 supply)

**Limitations**:
- Requires H2 infrastructure
- Higher initial cost
- Developing technology (early commercialization)

#### 4.4.5 Fixed GPUs (Pre-Conditioned Air + Ground Power)
**Technology**: Centralized ground power system at gate

**Description**:
- 400 Hz power supplied from substation via pit or overhead
- Combined with pre-conditioned air (PCA)
- Eliminates need for mobile GPUs

**Benefits**:
- No on-apron equipment
- Lowest operating cost and emissions
- Highest reliability

**Limitations**:
- Requires infrastructure at each gate (high capital cost)
- Less flexible for aircraft positioning

### 4.5 Aircraft Interface

**Connection Types**:
- 115V single-phase (small aircraft, general aviation)
- 115/200V three-phase (commercial aircraft, most common)
- Connectors: MS3106A, MS3108B series or equivalent

**Safety Features**:
- Ground fault protection
- Overcurrent protection
- Reverse power protection (prevent backfeed)
- Emergency disconnect (both GPU and aircraft side)

**Operational Procedures**:
- Pre-connection checks (voltage, frequency, phase rotation)
- Soft connection (GPU running, then connect to aircraft)
- Monitoring during operation (voltage, current, frequency)
- Soft disconnection (reduce load, then disconnect)

### 4.6 Environmental Considerations

**Emissions Reduction**:
- Transition from diesel to electric or H2 fuel cell GPUs
- Target: 50% emission reduction by 2030, 100% by 2050

**Noise Reduction**:
- Electric and fuel cell GPUs significantly quieter than diesel
- Important for airport noise abatement and community relations

**Energy Efficiency**:
- Right-sizing GPU to aircraft needs (avoid oversized units)
- Load monitoring and optimization
- Integration with airport energy management system

## 5. Safety and Environmental Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Electrical Safety | IEC 60204-1, NFPA 70 | Design, grounding, protection |
| Aircraft Power Quality | MIL-STD-704, SAE AS6858 | Testing and certification |
| Fuel Cell Safety | IEC 62282, ISO 23273 | H2 safety, ventilation |
| Battery Safety | IEC 62619, UL 2580 | Battery management, fire protection |
| Emissions | EPA Tier standards, EURO Stage | Diesel engine compliance (if applicable) |
| Environmental Management | ISO 14001 | EMS, pollution prevention |

## 6. Cross-References
- Related ATA Chapters: ATA 03 (Support Information/GSE)
- Parent Document: 03-80_Energy
- Related GSE ANCHORS: 03-30_ANCHORS
- Related GSE Propulsion: 03-70_Propulsion
- Grid Power Supply: 03-80-03-01A_Grid_Power_Supply
- Power Distribution: 03-80-03-03A_Power_Distribution
- H2 Energy Systems: 03-80-02_H2_Energy_Systems
- Battery Energy Systems: 03-80-05_Battery_Energy_Systems

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
