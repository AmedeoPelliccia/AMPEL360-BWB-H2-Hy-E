# 03-80-04-01A - Solar Power Systems

## 1. Purpose
This document specifies solar photovoltaic (PV) power systems for Ground Support Equipment (GSE) operations, including design, installation, and integration requirements.

## 2. Scope
This specification covers:
- Solar PV system design and sizing
- Panel selection and mounting
- Inverters and power conditioning
- Grid integration and net metering
- Performance monitoring and optimization
- Integration with GSE charging and energy storage

## 3. Applicable Documents
- IEC 61215 (Crystalline Silicon Terrestrial Photovoltaic (PV) Modules)
- IEC 61730 (Photovoltaic (PV) Module Safety Qualification)
- IEEE 1547 (Standard for Interconnection and Interoperability of Distributed Energy Resources)
- IEC 62446 (Photovoltaic (PV) Systems - Requirements for Testing, Documentation and Maintenance)
- NFPA 70 Article 690 (Solar Photovoltaic Systems)
- ISO 50001 (Energy Management Systems)

## 4. Energy System Description

### 4.1 Overview
Solar PV systems convert sunlight directly into electricity to power GSE operations, charge batteries, produce green hydrogen, and offset grid electricity consumption.

### 4.2 Specifications
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| System Capacity | 100 kW - 10 MW | Scalable based on available space |
| Panel Efficiency | 18-22% | Monocrystalline silicon |
| System Efficiency | 75-85% | DC to AC (inverter + losses) |
| Capacity Factor | 15-25% | Location and orientation dependent |
| Lifetime | 25-30 years | With >80% capacity retention |
| Grid Integration | IEEE 1547 compliant | Anti-islanding, power quality |

### 4.3 Performance Requirements

#### 4.3.1 Energy Generation
- **Annual Energy Production**: Match 20-50% of GSE facility electrical consumption
- **Peak Power**: Contribute to daytime peak demand reduction
- **Predictability**: Day-ahead and intraday production forecasting

#### 4.3.2 System Reliability
- **Availability**: >98% operational availability
- **Maintenance**: Scheduled cleaning and inspection semi-annually
- **Performance Monitoring**: Real-time monitoring of production, system health

### 4.4 Solar PV System Components

#### 4.4.1 Solar Panels
**Technology**: Monocrystalline silicon PV modules
- Efficiency: 18-22%
- Power rating: 300-500 W per panel
- Temperature coefficient: -0.35 to -0.40% per °C
- Warranty: 25 years for 80% capacity retention

**Mounting Options**:
- Ground-mounted: Fixed tilt or single-axis tracking
- Rooftop: Building roofs, carports, canopies
- Elevated structures: Over parking areas, equipment storage

#### 4.4.2 Inverters
**String Inverters**:
- Capacity: 5-100 kW per inverter
- Efficiency: 96-98%
- Suitable for smaller systems or distributed arrays

**Central Inverters**:
- Capacity: 100 kW - 1 MW per inverter
- Efficiency: 97-99%
- Suitable for large-scale ground-mounted systems

**Microinverters** (optional):
- Panel-level power optimization
- Enhanced system monitoring and diagnostics
- Higher cost, suitable for complex roof geometries

#### 4.4.3 Balance of System (BOS)
- **Mounting structures**: Aluminum or galvanized steel, wind-rated
- **DC wiring and combiner boxes**: Properly sized for current and voltage
- **AC disconnect and protection**: Circuit breakers, surge protection
- **Monitoring system**: Inverter monitoring + weather station

### 4.5 System Design Considerations

#### 4.5.1 Site Selection and Assessment
- **Solar resource**: Annual solar irradiation (kWh/m²/year)
- **Available area**: Ground space or roof area for panel installation
- **Shading analysis**: Avoid shading from buildings, trees, equipment
- **Structural capacity**: Roof load-bearing capacity (if rooftop installation)
- **Grid connection point**: Proximity to electrical infrastructure

#### 4.5.2 System Sizing
**Energy Demand Analysis**:
- Historical electricity consumption data
- Load profiles (hourly, daily, seasonal)
- Future growth projections

**Solar Resource Assessment**:
- Average daily solar irradiation
- Seasonal variations
- Weather patterns (cloudy days, monsoon seasons)

**Sizing Calculation**:
- PV array size = (Annual energy demand × Solar fraction) / (Solar irradiation × System efficiency)
- Example: 1 MW annual demand, 30% solar fraction, 1800 kWh/m²/year, 16% system efficiency
  - PV capacity = (1,000,000 kWh × 0.3) / (1800 × 0.16) = ~1,040 kW

#### 4.5.3 Grid Integration
**Grid-Tied Configuration**:
- PV generation directly offsets facility load
- Excess generation exported to grid (if net metering/feed-in tariff available)
- Anti-islanding protection per IEEE 1547
- Power quality compliance (THD, voltage regulation)

**Grid + Storage Configuration**:
- PV generation charges battery storage system
- Stored energy used during non-solar hours or peak demand periods
- Enhanced resilience and self-consumption

### 4.6 Integration with GSE Operations

**Direct EV Charging**:
- Solar canopies over charging stations
- PV generation offsets charging load during daytime
- Smart charging to maximize solar utilization

**Power-to-H2**:
- PV electricity powers electrolyzers for green H2 production
- Optimized operation during peak solar hours
- See 03-80-04-04A for detailed integration

**Building and Facility Power**:
- Offset facility electrical consumption (lighting, HVAC, equipment)
- Reduce utility demand charges

### 4.7 Performance Monitoring and Optimization

**Monitoring Parameters**:
- DC power output per string/array
- AC power output to grid/facility
- Solar irradiance and ambient temperature
- Inverter efficiency and status
- System performance ratio (PR)

**Optimization Strategies**:
- Predictive maintenance based on performance data
- Panel cleaning scheduling (if dust/soiling is significant)
- Inverter and system settings optimization
- Integration with energy management system

## 5. Safety and Environmental Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| PV Module Safety | IEC 61730, UL 1703 | Module certification and testing |
| Electrical Installation | NFPA 70 Article 690, IEC 60364 | Wiring, protection, grounding |
| Grid Interconnection | IEEE 1547 | Anti-islanding, power quality |
| Fire Safety | NFPA 70, local fire codes | DC arc-fault protection, rapid shutdown |
| Structural | IBC, local building codes | Wind and snow load design |
| Environmental | ISO 14001 | EMS, end-of-life recycling plans |

## 6. Cross-References
- Related ATA Chapters: ATA 03 (Support Information/GSE)
- Parent Document: 03-80_Energy
- Energy Strategy: 03-80-01-01A_GSE_Energy_Strategy
- Grid Power Supply: 03-80-03-01A_Grid_Power_Supply
- Renewable Microgrids: 03-80-04-03A_Renewable_Microgrids
- Power-to-H2: 03-80-04-04A_Power_To_H2_Systems
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
