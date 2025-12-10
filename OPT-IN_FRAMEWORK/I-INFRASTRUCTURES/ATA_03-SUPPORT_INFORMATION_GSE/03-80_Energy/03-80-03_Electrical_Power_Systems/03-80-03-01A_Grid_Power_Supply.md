# 03-80-03-01A - Grid Power Supply

## 1. Purpose
This document specifies grid electrical power supply systems for Ground Support Equipment (GSE) operations, including utility connections, power distribution, and reliability requirements.

## 2. Scope
This specification covers:
- Utility grid connections and service levels
- Primary and secondary distribution systems
- Power quality requirements
- Backup and redundancy provisions
- Integration with renewable energy and microgrids
- Grid-connected energy storage

## 3. Applicable Documents
- IEC 61850 (Communication Networks and Systems for Power Utility Automation)
- IEEE 1547 (Standard for Interconnection and Interoperability of Distributed Energy Resources)
- IEC 60364 (Low-Voltage Electrical Installations)
- NFPA 70 (National Electrical Code)
- ISO 50001 (Energy Management Systems)
- IEEE 519 (Harmonic Control in Electrical Power Systems)

## 4. Energy System Description

### 4.1 Overview
Grid power supply provides the primary electrical energy source for GSE operations, including battery charging, facility operations, H2 production via electrolysis, and direct equipment operation. The system ensures reliable, high-quality power delivery while integrating with on-site renewable generation and energy storage.

### 4.2 Specifications
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Primary Voltage | 10-35 kV (Medium Voltage) | Utility grid connection |
| Secondary Voltage | 400V AC, 230V AC | Low-voltage distribution |
| Frequency | 50 Hz / 60 Hz | Regional standard |
| Power Capacity | 2-20 MVA | Scalable per facility size |
| Reliability | 99.95% availability | With redundancy |
| Power Quality | IEEE 519, IEC 61000 | Harmonics, voltage stability |

### 4.3 Performance Requirements

#### 4.3.1 Reliability and Availability
- **Service Level**: Utility supply with N+1 redundancy for critical loads
- **Availability Target**: 99.95% (equivalent to <4.5 hours downtime per year)
- **Restoration Time**: <15 minutes for planned outages, <4 hours for unplanned
- **Load Transfer**: Automatic transfer to backup sources within 10 seconds

#### 4.3.2 Power Quality
- **Voltage Regulation**: ±5% of nominal voltage
- **Frequency Stability**: ±0.5 Hz of nominal frequency
- **Total Harmonic Distortion (THD)**: <5% for voltage, <8% for current
- **Power Factor**: >0.95 at point of common coupling (PCC)
- **Voltage Unbalance**: <2% under normal conditions

### 4.4 Grid Connection Architecture

#### 4.4.1 Utility Service Entry
**Primary Service**:
- Voltage level: 10-35 kV (medium voltage)
- Service type: Dedicated substation or shared airport substation
- Protection: Circuit breakers, relays, surge arresters
- Metering: Revenue-grade metering at PCC
- Communication: SCADA integration with utility dispatch

**Secondary Service** (optional redundancy):
- Independent feed from different utility substation or distribution line
- Automatic or manual transfer capability
- Load sharing or hot standby configuration

#### 4.4.2 On-Site Substation
**Main Transformer(s)**:
- Capacity: 2-20 MVA depending on facility load
- Type: Oil-filled or dry-type, depending on location and regulations
- Configuration: Single transformer or N+1 redundant transformers
- Voltage ratio: MV primary to 400V secondary (three-phase)
- Cooling: ONAN (oil natural, air natural) or ONAF (oil natural, air forced)

**Protection and Switchgear**:
- MV switchgear: Circuit breakers, disconnect switches, protection relays
- LV switchgear: Main circuit breaker, feeder breakers, metering
- Arc flash protection: Arc-resistant switchgear, incident energy labels
- Ground fault protection: Sensitive earth fault protection

#### 4.4.3 Low-Voltage Distribution
**Distribution Panels**:
- Main distribution board (MDB) at substation
- Sub-distribution boards (SDB) at key locations (charging stations, buildings, etc.)
- Voltage: 400V three-phase, 230V single-phase
- Protection: Molded case circuit breakers (MCCBs), miniature circuit breakers (MCBs)

**Distribution Topology**:
- Radial: Simple, lower cost, suitable for non-critical loads
- Ring/Loop: Higher reliability, automatic fault isolation
- Selective coordination: Circuit breaker settings coordinated to minimize outage impact

### 4.5 Integration with Renewable Energy

#### 4.5.1 Grid-Tied Renewable Generation
**On-Site Solar PV**:
- Capacity: 100 kW - 10 MW
- Interconnection: Grid-tied inverters per IEEE 1547
- Net metering or feed-in tariff arrangements
- Anti-islanding protection
- Power quality compliance (THD, power factor)

**On-Site Wind Turbines** (if applicable):
- Capacity: 1-5 MW per turbine
- Interconnection: Similar to solar PV
- Grid integration studies for stability

**Benefits**:
- Reduced grid electricity consumption and cost
- Lower carbon footprint
- On-site generation for resilience
- Potential revenue from excess generation

#### 4.5.2 Grid-Interactive Microgrids
**Microgrid Architecture**:
- Grid-connected mode: Normal operation, drawing from utility + on-site generation
- Island mode: Disconnect from grid during outage, operate autonomously
- Seamless transition: <100 ms transfer time
- Control system: Microgrid controller coordinates sources and loads

**Components**:
- Renewable generation (solar, wind)
- Energy storage (batteries)
- Backup generators (diesel, natural gas, or H2)
- Critical load identification and prioritization
- Smart switching and protection devices

### 4.6 Grid-Connected Energy Storage

**Purpose**:
- Load leveling: Shift electricity consumption from peak to off-peak hours
- Peak shaving: Reduce maximum demand charge
- Frequency regulation: Support grid stability (if participating in utility programs)
- Backup power: Short-duration backup during grid outages or transfer to backup generators

**Technology**:
- Lithium-ion batteries: 1-10 MWh capacity, 0.5-2 MW power
- Power conversion system (PCS): Bidirectional inverter, battery management system (BMS)
- Control strategy: Economic dispatch, demand charge management, resilience

### 4.7 Power Quality Management

#### 4.7.1 Harmonic Mitigation
**Sources of Harmonics**:
- Variable frequency drives (VFDs) for motors
- Battery chargers and power electronics
- LED lighting, computer equipment

**Mitigation Strategies**:
- Passive harmonic filters: Tuned LC filters for specific harmonics
- Active harmonic filters: Real-time harmonic cancellation
- Transformer design: K-rated transformers for non-linear loads
- 12-pulse or 18-pulse rectifiers: Reduce characteristic harmonics

#### 4.7.2 Power Factor Correction
**Reactive Power Compensation**:
- Capacitor banks: Switched or fixed capacitors for power factor correction
- Active power factor correction: Power electronics-based compensation
- Target: Power factor >0.95 at PCC to avoid utility penalties

#### 4.7.3 Voltage Regulation
**Strategies**:
- On-load tap changers (OLTC) on transformers
- Voltage regulators on distribution feeders
- Distributed generation voltage support
- Reactive power management (Q control)

### 4.8 Monitoring and Control

**Energy Management System (EMS)**:
- Real-time monitoring: Voltage, current, power, energy, power factor, harmonics
- Historical data: Energy consumption trends, demand profiles
- Alarming: Abnormal conditions, equipment faults
- Optimization: Load scheduling, demand response participation
- Reporting: Energy reports, compliance documentation

**Communication Protocols**:
- IEC 61850 for substation automation
- Modbus for equipment integration
- BACnet for building management systems
- DNP3 for utility SCADA integration

## 5. Safety and Environmental Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Electrical Installation | IEC 60364, NFPA 70 | Design, installation, inspection per codes |
| Substation Safety | IEEE 80 (Grounding), IEEE 1584 (Arc Flash) | Safety design and labeling |
| Power Quality | IEEE 519, IEC 61000 | Harmonic limits, compatibility |
| Grid Interconnection | IEEE 1547 | DER interconnection requirements |
| Energy Management | ISO 50001 | EnMS certification |
| Environmental Protection | ISO 14001 | EMS, pollution prevention |

## 6. Cross-References
- Related ATA Chapters: ATA 03 (Support Information/GSE)
- Parent Document: 03-80_Energy
- Related GSE ANCHORS: 03-30_ANCHORS
- Related GSE Propulsion: 03-70_Propulsion
- Energy Strategy: 03-80-01-01A_GSE_Energy_Strategy
- Energy Requirements: 03-80-01-02A_GSE_Energy_Requirements
- Ground Power Units: 03-80-03-02A_Ground_Power_Units
- Power Distribution: 03-80-03-03A_Power_Distribution
- Emergency Power: 03-80-03-04A_Emergency_Power_Systems
- Renewable Energy: 03-80-04_Renewable_Energy_GSE
- Battery Energy Systems: 03-80-05_Battery_Energy_Systems
- Energy Management Systems: 03-80-06_Energy_Management_Systems

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
