# 95-80-00-006 Energy Balances and KPI Definitions

**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active  
**ATA Chapter:** 95-80 (Energy)

---

## 1. Purpose

This document defines the energy balance methodology and Key Performance Indicators (KPIs) for the AMPEL360 energy systems. It provides the basis for energy accounting, performance evaluation, and optimization.

---

## 2. Energy Balance Framework

### 2.1 Global Energy Balance Equation

```
E_input = E_useful + E_losses + E_stored
```

Where:
- **E_input**: Total energy input (primarily H₂)
- **E_useful**: Energy delivered to perform useful work
- **E_losses**: Energy dissipated as heat or other losses
- **E_stored**: Net change in stored energy (batteries, accumulators)

### 2.2 Power Balance Equation (Instantaneous)

```
P_gen = P_load + P_loss + P_storage
```

Where:
- **P_gen**: Instantaneous power generation (fuel cells + APU + battery discharge)
- **P_load**: Total instantaneous load
- **P_loss**: Instantaneous losses in distribution
- **P_storage**: Net power into storage (positive = charging, negative = discharging)

---

## 3. Energy Flow Accounting

### 3.1 Primary Energy Input

**H₂ Energy Content**:
```
E_H2 = m_H2 × LHV_H2
```
- m_H2: Mass of hydrogen consumed (kg)
- LHV_H2: Lower heating value = 33.3 kWh/kg

**Typical Mission Values**:
- Cruise: ~0.8 kg H₂ per 100 km
- 4000 km range: ~32 kg H₂
- Total energy: 32 × 33.3 = 1066 kWh

### 3.2 Electrical Generation

**Fuel Cell Output**:
```
P_elec_FC = m_H2 × LHV_H2 × η_FC
```
- η_FC: Fuel cell efficiency = 0.55-0.60

**APU Output**:
```
P_elec_APU = P_rated_APU × Load_Factor
```
- P_rated_APU: 350 kW maximum
- Load_Factor: 0-1.0 depending on demand

### 3.3 Distribution Efficiency

**Electrical Distribution**:
```
η_dist_elec = P_delivered / P_generated
```
- Target: η_dist_elec > 0.97 (3% losses maximum)

**Hydraulic Distribution**:
```
η_dist_hyd = P_actuator / P_pump_input
```
- Target: η_dist_hyd > 0.90 (10% losses maximum)

---

## 4. Key Performance Indicators (KPIs)

### 4.1 System-Level KPIs

#### KPI-E-001: Overall Energy Efficiency
**Definition**: Total useful output energy divided by total H₂ energy input
```
η_overall = (E_thrust + E_systems) / E_H2
```
**Target**: >45%  
**Current Status**: 47% (simulation)  
**Measurement**: Flight test data integration  
**Reporting Frequency**: Per flight cycle

#### KPI-E-002: Fuel Cell System Efficiency
**Definition**: Electrical energy output divided by H₂ chemical energy input
```
η_FC_sys = E_elec_out / (m_H2 × LHV_H2)
```
**Target**: >55%  
**Current Status**: 57% (vendor specification)  
**Measurement**: Fuel cell monitoring system  
**Reporting Frequency**: Real-time, aggregated per flight

#### KPI-E-003: Propulsion Energy Efficiency
**Definition**: Mechanical thrust power divided by electrical input power
```
η_propulsion = P_thrust / P_elec_motor
```
**Target**: >85%  
**Current Status**: 87% (motor vendor spec + propeller efficiency)  
**Measurement**: Motor controllers and thrust sensors  
**Reporting Frequency**: Real-time, averaged per flight phase

#### KPI-E-004: Electrical System Availability
**Definition**: Percentage of time primary electrical system is fully operational
```
Availability_elec = (T_operational / T_total) × 100%
```
**Target**: >99.5%  
**Current Status**: TBD (in development)  
**Measurement**: Fault logging system  
**Reporting Frequency**: Monthly fleet aggregate

---

### 4.2 Electrical Domain KPIs

#### KPI-E-005: Bus Voltage Regulation
**Definition**: Maximum deviation from nominal voltage
```
V_deviation = |V_measured - V_nominal| / V_nominal × 100%
```
**Target**: <5% for 270 VDC, <2% for 28 VDC  
**Measurement**: Bus voltage sensors  
**Reporting**: Continuous monitoring, alert on exceedance

#### KPI-E-006: Power Quality (THD)
**Definition**: Total harmonic distortion on AC buses
```
THD = √(Σ V_n²) / V_1 × 100%
```
Where V_n is nth harmonic voltage, V_1 is fundamental
**Target**: <5%  
**Measurement**: Power quality analyzers  
**Reporting**: Real-time monitoring, recorded per flight

#### KPI-E-007: Battery State of Charge (SoC)
**Definition**: Available charge as percentage of total capacity
```
SoC = Q_remaining / Q_total × 100%
```
**Target**: Maintain 30-90% for longevity  
**Measurement**: Battery management system  
**Reporting**: Real-time display, logged continuously

#### KPI-E-008: DC/DC Converter Efficiency
**Definition**: Output power divided by input power
```
η_converter = P_out / P_in × 100%
```
**Target**: >97%  
**Measurement**: Input/output power sensors  
**Reporting**: Aggregate per flight, trend analysis monthly

---

### 4.3 H₂ Domain KPIs

#### KPI-E-009: H₂ Consumption Rate
**Definition**: Mass of hydrogen consumed per unit distance
```
CR_H2 = m_H2 / distance (kg/100 km)
```
**Target**: <0.85 kg/100 km at cruise  
**Current Status**: 0.80 kg/100 km (design)  
**Measurement**: Flow meters and distance sensors  
**Reporting**: Per flight, averaged over cruise segment

#### KPI-E-010: H₂ Boil-Off Rate
**Definition**: Percentage of H₂ mass lost per day due to tank warming
```
BOR = (m_lost / m_total) / t_days × 100%
```
**Target**: <0.5% per day  
**Measurement**: Tank level sensors  
**Reporting**: Daily when parked, per flight when operating

#### KPI-E-011: H₂ Energy Conversion Efficiency
**Definition**: Electrical energy from fuel cells divided by H₂ chemical energy
```
η_H2_conv = E_elec_FC / (m_H2 × LHV_H2) × 100%
```
**Target**: >55%  
**Measurement**: Fuel cell stack monitors  
**Reporting**: Real-time, aggregated per flight phase

---

### 4.4 Hydraulic Domain KPIs

#### KPI-E-012: Hydraulic System Efficiency
**Definition**: Mechanical work output divided by electrical input to pumps
```
η_hydraulic = W_actuator / E_elec_pump × 100%
```
**Target**: >85%  
**Measurement**: Pump power and actuator position/force  
**Reporting**: Per actuator cycle, aggregated per flight

#### KPI-E-013: Accumulator Cycling
**Definition**: Number of charge/discharge cycles
```
Cycles_acc = count(pressure_rise_above_threshold)
```
**Target**: Monitor for maintenance planning  
**Measurement**: Pressure sensors  
**Reporting**: Cumulative, maintenance alert at threshold

---

### 4.5 Pneumatic Domain KPIs

#### KPI-E-014: Compressor Efficiency
**Definition**: Ideal compression work divided by actual electrical input
```
η_compressor = W_ideal / E_elec_compressor × 100%
```
**Target**: >75%  
**Measurement**: Pressure, temperature, flow, and electrical power  
**Reporting**: Per compressor run cycle, aggregated per flight

#### KPI-E-015: Pneumatic Pressure Stability
**Definition**: Standard deviation of delivery pressure
```
σ_pressure = stdev(P_delivered)
```
**Target**: <5 psi variation  
**Measurement**: Pressure sensors  
**Reporting**: Statistical analysis per flight segment

---

### 4.6 Energy Management KPIs

#### KPI-E-016: Load Shedding Events
**Definition**: Number of times non-essential loads are shed
```
Shedding_Events = count(load_shedding_activations)
```
**Target**: 0 in normal operations  
**Measurement**: Energy management system logs  
**Reporting**: Per flight, fleet aggregate monthly

#### KPI-E-017: Power Management Response Time
**Definition**: Time from fault detection to corrective action
```
t_response = t_action - t_detection
```
**Target**: <50 ms  
**Measurement**: EMS timestamps  
**Reporting**: Statistical analysis, alert on exceedance

#### KPI-E-018: Energy Optimization Savings
**Definition**: Energy saved through CAOS optimization vs. baseline
```
Savings = (E_baseline - E_optimized) / E_baseline × 100%
```
**Target**: 5-10% improvement  
**Measurement**: CAOS energy management algorithms  
**Reporting**: Per flight, trend analysis monthly

---

### 4.7 Digital Twin KPIs

#### KPI-E-019: Digital Twin Prediction Accuracy
**Definition**: Error between predicted and actual energy consumption
```
Error_DT = |E_predicted - E_actual| / E_actual × 100%
```
**Target**: <5%  
**Measurement**: Digital twin vs. actual telemetry  
**Reporting**: Per flight, model tuning updates quarterly

#### KPI-E-020: Energy Data Completeness
**Definition**: Percentage of required energy data successfully logged
```
Completeness = (n_logged / n_required) × 100%
```
**Target**: >99%  
**Measurement**: Data logging system health checks  
**Reporting**: Real-time monitoring, daily summary

---

## 5. Energy Balance by Mission Phase

### 5.1 Ground Operations
- **Primary Power**: Ground power cart or APU
- **H₂ Consumption**: Minimal (boil-off only)
- **Energy Balance**: P_ground = P_systems + P_HVAC
- **KPI Focus**: Boil-off rate, ground power quality

### 5.2 Taxi
- **Primary Power**: Fuel cells at low output
- **H₂ Consumption**: ~0.1 kg/min
- **Energy Balance**: P_FC = P_propulsion_taxi + P_systems
- **KPI Focus**: Fuel cell low-load efficiency, battery assist

### 5.3 Takeoff
- **Primary Power**: Fuel cells at maximum output + battery boost
- **H₂ Consumption**: ~0.3 kg/min
- **Energy Balance**: P_FC + P_battery = P_propulsion_max + P_systems
- **KPI Focus**: Peak power management, battery discharge rate

### 5.4 Climb
- **Primary Power**: Fuel cells at high continuous output
- **H₂ Consumption**: ~0.25 kg/min
- **Energy Balance**: P_FC = P_propulsion_climb + P_systems
- **KPI Focus**: Fuel cell efficiency at high load, thermal management

### 5.5 Cruise
- **Primary Power**: Fuel cells at optimal efficiency point
- **H₂ Consumption**: ~0.15 kg/min (~0.8 kg/100 km)
- **Energy Balance**: P_FC = P_propulsion_cruise + P_systems
- **KPI Focus**: Overall efficiency, fuel consumption rate per km

### 5.6 Descent
- **Primary Power**: Fuel cells at reduced output + regenerative braking
- **H₂ Consumption**: ~0.05 kg/min
- **Energy Balance**: P_FC + P_regen = P_propulsion_descent + P_systems + P_battery_charge
- **KPI Focus**: Regenerative energy capture, battery charging efficiency

### 5.7 Landing/Rollout
- **Primary Power**: Fuel cells + battery assist
- **H₂ Consumption**: ~0.1 kg/min
- **Energy Balance**: P_FC + P_battery = P_propulsion_brake + P_systems
- **KPI Focus**: Regenerative braking effectiveness

---

## 6. Energy Loss Budget

### 6.1 Identified Loss Mechanisms

| Loss Source | Estimated % of Input | Mitigation Strategy |
|-------------|---------------------|---------------------|
| Fuel cell stack losses | 40-45% | Optimize operating temperature, humidification |
| Power electronics losses | 2-3% | High-efficiency SiC devices |
| Electrical distribution losses | 1-2% | Minimize cable runs, optimize gauge |
| Motor losses | 4-6% | High-efficiency motors, optimal cooling |
| Propeller losses | 10-15% | Aerodynamic optimization |
| Hydraulic system losses | 8-10% | Minimize friction, optimize pump efficiency |
| Pneumatic system losses | 15-20% | Heat recovery, minimize leakage |
| Thermal management parasitic | 3-5% | Waste heat utilization |

### 6.2 Loss Allocation by System

```
Total Input Energy (H₂): 100%
├── Fuel Cell Electrical Output: 55-60%
│   ├── Propulsion (Motors): 45-50%
│   │   ├── Useful Thrust: 38-42%
│   │   └── Motor/Drive Losses: 2-4%
│   │   └── Propeller Losses: 5-7%
│   ├── Aircraft Systems: 10-12%
│   │   ├── Avionics: 1-2%
│   │   ├── ECS/Hydraulics: 5-7%
│   │   ├── Lighting/IFE: 2-3%
│   │   └── Distribution Losses: 1%
│   └── Distribution Losses: 1-2%
└── Fuel Cell Waste Heat: 40-45%
    ├── Useful Heat Recovery: 10-15%
    └── Rejected to Environment: 25-35%
```

---

## 7. KPI Dashboard and Reporting

### 7.1 Real-Time Cockpit Display

**Primary Indicators**:
- Total power generation (kW)
- H₂ consumption rate (kg/min)
- Battery SoC (%)
- System health status (green/amber/red)

**Secondary Indicators**:
- Bus voltages (VDC)
- Fuel cell current (A)
- Available energy remaining (kWh)
- Estimated range (km)

### 7.2 Post-Flight Report

**Energy Summary**:
- Total H₂ consumed (kg)
- Total energy generated (kWh)
- Average efficiency (%)
- Energy per distance (Wh/km)

**System Performance**:
- Fuel cell efficiency by phase
- Battery cycles and depth of discharge
- Abnormal events or deviations
- KPI compliance status

### 7.3 Fleet-Level Analytics

**Monthly Aggregates**:
- Average efficiency across fleet
- Energy consumption trends
- KPI compliance statistics
- Anomaly detection and predictive maintenance triggers

**Continuous Improvement**:
- Benchmarking best vs. worst performers
- Correlation analysis (e.g., efficiency vs. flight profile)
- Recommendations for operational optimization

---

## 8. Related Documents

| Document | Description |
|----------|-------------|
| [95-80-00-001](../95-80-00-001_Energy_Overview.md) | Energy module overview |
| [95-80-00-004](95-80-00-004_Energy_Taxonomy.md) | Energy terminology |
| [95-80-80](../95-80-80_Energy_Management_and_Optimization/) | Energy management details |
| [95-80-46](../95-80-46_Energy_Data_and_Digital_Twins/) | Digital twin implementation |

---

## 9. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 Energy WG | Initial version |

---

**Document Control**
- **Standard**: OPT-IN Framework v1.5
- **Owner**: AMPEL360 Documentation WG
- **Classification**: Technical Reference
