# 95-60-00-007 Health Monitoring and Limits Overview

**Document ID:** 95-60-00-007  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** ACTIVE

---

## 1. Purpose

This document defines the health monitoring strategy, sensor requirements, and operational limits for all storage systems in the AMPEL360 BWB H₂ Hy-E aircraft.

---

## 2. Monitoring Strategy

### 2.1 Monitoring Tiers

| Tier | Frequency | Systems | Data Handling |
|------|-----------|---------|---------------|
| **Tier 1: Real-time** | Continuous (1-10 Hz) | Critical storages (H₂, batteries, FDR, hydraulic accumulators) | Real-time telemetry, immediate alerts |
| **Tier 2: Per-flight** | Pre/post flight, in-flight hourly | Essential storages (reservoirs, thermal buffers) | Flight data recording, trend analysis |
| **Tier 3: Daily** | Once per day or turnaround | Important storages (water/waste, data hubs) | Daily reports, scheduled checks |
| **Tier 4: Weekly/Monthly** | Scheduled intervals | Auxiliary storages (APU oil, backup systems) | Maintenance logs, periodic inspection |

---

## 3. Storage Health Metrics

### 3.1 Energy Storage Health

#### State of Charge (SOC)
- **Definition**: Current energy level relative to maximum capacity
- **Calculation**: `SOC = (Current Energy / Maximum Energy) × 100%`
- **Monitoring**: Real-time for all electrical and chemical storages
- **Alert Thresholds**:
  - Critical: SOC < 20%
  - Warning: SOC < 30%
  - Normal: SOC ≥ 30%

#### State of Health (SOH)
- **Definition**: Current capacity relative to design capacity (accounting for degradation)
- **Calculation**: `SOH = (Current Max Capacity / Design Capacity) × 100%`
- **Monitoring**: Weekly or per-charge cycle for batteries, monthly for other systems
- **Alert Thresholds**:
  - Critical: SOH < 70%
  - Warning: SOH < 80%
  - Normal: SOH ≥ 80%

#### State of Energy (SOE)
- **Definition**: Actual available energy considering current conditions
- **Calculation**: `SOE = SOC × SOH × Efficiency Factor`
- **Monitoring**: Real-time for mission-critical systems
- **Used for**: Range calculation, power management decisions

### 3.2 Fluid Storage Health

#### Level/Volume
- **Sensors**: Capacitive, ultrasonic, or float-based level sensors
- **Accuracy**: ±2% of full scale for critical systems, ±5% for non-critical
- **Alert Thresholds**:
  - Critical Low: < 10% capacity
  - Warning Low: < 20% capacity
  - Warning High: > 95% capacity (prevent overfill)

#### Pressure
- **Sensors**: Pressure transducers, strain gauges
- **Accuracy**: ±1% of full scale for accumulators, ±2% for tanks
- **Alert Thresholds**: System-specific (see individual storage specs)

#### Temperature
- **Sensors**: RTD (Pt100/Pt1000) for precision, thermocouples for high-temp
- **Accuracy**: ±0.5°C for cryogenic, ±2°C for others
- **Alert Thresholds**: Based on fluid properties and safety limits

#### Contamination (Hydraulic)
- **Monitoring**: Particle counters, water sensors
- **Standard**: ISO 4406 cleanliness code
- **Alert Thresholds**:
  - Target: ISO 18/16/13 or better
  - Warning: ISO 19/17/14
  - Critical: ISO 20/18/15 or worse

### 3.3 Data Storage Health

#### Utilization
- **Calculation**: `(Used Space / Total Space) × 100%`
- **Alert Thresholds**:
  - Critical: > 95% full
  - Warning: > 85% full
  - Normal: < 85% full

#### Write Cycle Count
- **Monitoring**: Track number of write cycles for flash/SSD storage
- **Limit**: Based on manufacturer specifications (typically 1000-10000 cycles)
- **Alert Thresholds**:
  - Critical: > 90% of rated cycles
  - Warning: > 75% of rated cycles

#### Data Integrity
- **Methods**: Checksums, ECC (Error Correction Codes), RAID redundancy
- **Monitoring**: Continuous background verification
- **Alert**: Any unrecoverable error triggers immediate alert

---

## 4. Safety Limits

### 4.1 Critical Safety Limits (Must Not Exceed)

| Storage Type | Parameter | Limit Type | Typical Value | Action on Exceed |
|--------------|-----------|------------|---------------|------------------|
| LH₂ Tanks | Pressure | Maximum | 5 bar | Auto vent, alert |
| LH₂ Tanks | Temperature | Minimum | -253°C | Insulation failure alert |
| LH₂ Tanks | Leak Rate | Maximum | 0.1% per hour | Emergency procedures |
| Batteries | Temperature | Maximum | 60°C | Reduce load, cooling |
| Batteries | Voltage | Maximum | 850 VDC | Open contactor, isolate |
| Batteries | Current | Maximum | 500 A | Load shedding |
| Hydraulic Accum. | Pressure | Maximum | 3200 psi | Relief valve activation |
| Hydraulic Accum. | Pressure | Minimum | 1500 psi | Low pressure warning |
| CO₂ Battery | Pressure | Maximum | 100 bar | Vent activation |
| CO₂ Battery | Temperature | Maximum | 80°C | Reduce power, cooling |

### 4.2 Operational Limits (Normal Operation)

- **Batteries**: 30-80% SOC for longevity
- **H₂ Tanks**: Maintain above 10% level for safe operation
- **Hydraulic**: Keep level above 20% to prevent pump cavitation
- **Data Recorders**: Ensure minimum 25 hours capacity at all times

---

## 5. Sensor Architecture

### 5.1 Sensor Redundancy

| Criticality | Redundancy Level | Configuration |
|-------------|------------------|---------------|
| **CRITICAL** | Triple redundant | 2-out-of-3 voting logic |
| **ESSENTIAL** | Dual redundant | Primary + backup with switchover |
| **IMPORTANT** | Single + monitoring | Single sensor with health monitoring |
| **AUXILIARY** | Single | Single sensor, periodic calibration |

### 5.2 Sensor Types by Storage

#### Energy Storage
- Voltage sensors (isolated, high-accuracy)
- Current sensors (Hall effect, Rogowski coil)
- Temperature sensors (RTD, thermocouple arrays)
- SOC estimators (Coulomb counting, impedance spectroscopy)

#### Fluid Storage
- Level sensors (capacitive, ultrasonic, radar)
- Pressure transducers (strain gauge, piezoelectric)
- Temperature sensors (RTD, thermistors)
- Flow meters (turbine, Coriolis, ultrasonic)
- Contamination sensors (particle counters, water detection)

#### Data Storage
- Utilization monitors (filesystem APIs)
- Write cycle counters (SSD/flash SMART data)
- Integrity checkers (continuous CRC verification)
- Performance monitors (latency, throughput)

---

## 6. Alert and Response Framework

### 6.1 Alert Levels

| Level | Description | Response Time | Action |
|-------|-------------|---------------|--------|
| **INFO** | Normal status update | N/A | Log only |
| **CAUTION** | Approaching limit | 1 hour | Crew awareness, trend monitoring |
| **WARNING** | Limit exceeded, degraded operation | 5 minutes | Crew action, operational adjustment |
| **ALERT** | Safety limit approached | 30 seconds | Immediate crew action, system reconfiguration |
| **EMERGENCY** | Safety limit exceeded | Immediate | Automatic safety actions, emergency procedures |

### 6.2 Automated Responses

- **Battery overtemp**: Reduce charge/discharge rate, activate cooling
- **H₂ overpressure**: Auto vent to safe level
- **Hydraulic low pressure**: Switch to backup accumulator
- **Data storage full**: Auto-purge non-critical data
- **CO₂ battery over-pressure**: Emergency vent, isolate system

---

## 7. Digital Twin Integration

All storage health data feeds into the CAOS (Cognitive Autonomous Operations System) digital twin:

- **Real-time mirroring**: Digital twin reflects current state
- **Predictive analytics**: Trend analysis, failure prediction
- **What-if scenarios**: Mission planning, load optimization
- **Historical analysis**: Performance tracking, degradation modeling

---

## 8. Maintenance Triggers

### 8.1 Condition-Based Maintenance

| Storage Type | Trigger Condition | Maintenance Action |
|--------------|-------------------|-------------------|
| Battery | SOH < 80% | Capacity test, possible replacement |
| Battery | Cycle count > 5000 | Detailed inspection, capacity verification |
| H₂ Tank | Boil-off rate > 0.5% | Insulation inspection, vacuum check |
| Hydraulic | Contamination > ISO 19/17/14 | Filter replacement, fluid analysis |
| Hydraulic Accum. | Pre-charge loss > 10% | Nitrogen recharge, seal inspection |
| Data Storage | Write cycles > 75% | Plan replacement, increase backup frequency |

### 8.2 Scheduled Maintenance

- **Daily**: Visual checks, data download (for QAR, data hubs)
- **Weekly**: Fluid sampling, pressure checks
- **Monthly**: Detailed inspections, calibration verification
- **Annual**: Full system tests, recertification

---

## 9. CAOS Integration Hooks

CAOS system discovers and monitors storages through:

- **Auto-discovery**: CAN bus, ARINC 429, Ethernet/IP protocols
- **Registration**: Storages register with CAOS on power-up
- **Health reporting**: Periodic telemetry via standard interfaces
- **Predictive models**: ML models for each storage type predict failures
- **Optimization**: CAOS optimizes storage usage across systems

---

## 10. Related Documents

- **[95-60-00-006](95-60-00-006_Storages_Registry.json)**: Complete storage registry with sensor specs
- **[95-60-00-008](95-60-00-008_CAOS_Storages_Hooks.md)**: CAOS discovery and monitoring integration
- **[95-40 Software](../../95-40_Software/)**: Monitoring software architecture

---

**Document Control**
- **Standard**: OPT-IN Framework v1.5
- **Classification**: Technical Documentation
- **Distribution**: Unrestricted (Open Source)
