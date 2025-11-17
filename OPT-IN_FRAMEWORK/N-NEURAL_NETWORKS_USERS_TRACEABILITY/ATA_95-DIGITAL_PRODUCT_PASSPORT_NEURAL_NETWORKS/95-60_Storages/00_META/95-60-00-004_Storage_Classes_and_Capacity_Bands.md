# 95-60-00-004 Storage Classes and Capacity Bands

**Document ID:** 95-60-00-004  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** ACTIVE

---

## 1. Purpose

This document provides detailed definitions of storage classes and capacity bands for the AMPEL360 BWB H₂ Hy-E aircraft, enabling consistent classification, sizing, and specification across all storage systems.

---

## 2. Storage Classes

### 2.1 Energy Storage Classes

#### Class E1: Primary Power Storage
- **Definition**: Main electrical energy storage for propulsion and systems
- **Typical Capacity**: 100-1000+ kWh
- **Duty Cycle**: Continuous
- **Examples**: Main battery packs (S-24-001, S-24-002), CO₂ battery (S-80-001)
- **Safety Requirements**: Crash-protected, fire-suppressed, thermal management
- **Monitoring**: Real-time SOC, SOH, temperature, voltage, current

#### Class E2: Backup Power Storage
- **Definition**: Emergency and backup power systems
- **Typical Capacity**: 1-50 kWh
- **Duty Cycle**: Standby, emergency activation
- **Examples**: Avionics backup (S-24-004), emergency lighting
- **Safety Requirements**: Independent power, rapid discharge capability
- **Monitoring**: Monthly health checks, charge maintenance

#### Class E3: Transient Power Storage
- **Definition**: High-power, short-duration energy buffering
- **Typical Capacity**: 1-20 kWh
- **Duty Cycle**: Intermittent, high-rate charge/discharge
- **Examples**: Supercapacitors (S-24-003), HVDC buffers (S-80-002)
- **Safety Requirements**: Overvoltage/overcurrent protection
- **Monitoring**: Real-time voltage, temperature

#### Class E4: Chemical Energy Storage
- **Definition**: Fuel and reactant storage for propulsion
- **Typical Capacity**: 500-2000+ kg H₂ equivalent
- **Duty Cycle**: Mission-based consumption
- **Examples**: LH₂ tanks (S-28-001, S-28-002)
- **Safety Requirements**: Cryogenic containment, leak detection, boil-off management
- **Monitoring**: Real-time level, pressure, temperature, boil-off rate

#### Class E5: Thermal Energy Storage
- **Definition**: Thermal buffering and temperature regulation
- **Typical Capacity**: 10-200 kW thermal
- **Duty Cycle**: Continuous or mission-based
- **Examples**: ECS thermal buffers (S-21-001), propulsion cooling (S-70-001)
- **Safety Requirements**: Pressure relief, thermal insulation
- **Monitoring**: Temperature, pressure, flow rate

---

### 2.2 Fluid Storage Classes

#### Class F1: Hydraulic Reservoirs
- **Definition**: Main hydraulic fluid supply
- **Typical Capacity**: 10-50 L
- **Operating Pressure**: Atmospheric to 50 psi (reservoir)
- **Examples**: Main reservoir (S-29-001)
- **Safety Requirements**: Contamination control, level monitoring
- **Monitoring**: Level, temperature, contamination sensors

#### Class F2: Hydraulic Accumulators
- **Definition**: Pressure buffering and emergency backup
- **Typical Capacity**: 5-20 L
- **Operating Pressure**: 1500-3000 psi
- **Examples**: Flight control accumulator (S-29-002), landing gear (S-29-003)
- **Safety Requirements**: Pressure relief, pre-charge nitrogen monitoring
- **Monitoring**: Pressure, pre-charge status

#### Class F3: Cryogenic Vessels
- **Definition**: Ultra-low temperature fluid storage
- **Typical Capacity**: 100-1000+ kg or L
- **Operating Temperature**: < -150°C
- **Examples**: LH₂ tanks (S-28-001, S-28-002)
- **Safety Requirements**: Multi-layer insulation, boil-off control, leak detection
- **Monitoring**: Level, pressure, temperature, boil-off rate, insulation integrity

#### Class F4: Service Fluid Tanks
- **Definition**: Water, waste, and service fluid storage
- **Typical Capacity**: 50-500 L
- **Operating Pressure**: Atmospheric to 50 psi
- **Examples**: Potable water (S-38-001), waste tanks (S-38-003, S-38-004)
- **Safety Requirements**: Contamination prevention, leak containment
- **Monitoring**: Level, quality sensors (for potable water)

---

### 2.3 Data Storage Classes

#### Class D1: Flight-Critical Recording
- **Definition**: Crash-protected flight data recording
- **Typical Capacity**: 25-100 hours of data
- **Retention**: Minimum regulatory requirement
- **Examples**: FDR (S-31-001), CVR (S-31-002)
- **Safety Requirements**: Crash-survivable, fire-resistant, underwater locatable
- **Monitoring**: Continuous recording verification, memory health

#### Class D2: Operational Data Buffering
- **Definition**: Mission data collection and buffering
- **Typical Capacity**: 1-10 TB
- **Retention**: Mission to mission (downloadable)
- **Examples**: QAR (S-31-003), data hubs (S-31-004, S-31-005)
- **Safety Requirements**: Redundancy, data integrity checks
- **Monitoring**: Storage utilization, write cycle count

#### Class D3: Digital Infrastructure Storage
- **Definition**: Ground-based data lakes, warehouses, registries
- **Typical Capacity**: 10 TB - 1 PB+
- **Retention**: Policy-based (years to decades)
- **Examples**: Data lake (S-46-001), model registry (S-46-002)
- **Safety Requirements**: Backup/recovery, access control, encryption
- **Monitoring**: Utilization, performance metrics, backup status

---

## 3. Capacity Bands

### 3.1 Energy Capacity Bands

| Band Code | Name | Capacity Range | Typical Applications |
|-----------|------|----------------|---------------------|
| **EC0** | Micro | < 100 Wh | Sensors, local buffers, embedded devices |
| **EC1** | Tiny | 100 Wh - 1 kWh | Backup batteries, small accumulators |
| **EC2** | Small | 1-10 kWh | Subsystem backup, supercapacitors |
| **EC3** | Medium | 10-100 kWh | System-level backup, APU start |
| **EC4** | Large | 100-500 kWh | Primary battery banks, thermal buffers |
| **EC5** | Mega | > 500 kWh | CO₂ battery, main power storage |
| **EF1** | Fuel-Small | < 100 kg H₂ | Buffer tanks, APU fuel |
| **EF2** | Fuel-Medium | 100-500 kg H₂ | Distribution buffers |
| **EF3** | Fuel-Large | > 500 kg H₂ | Main fuel tanks |

### 3.2 Fluid Volume Bands

| Band Code | Name | Volume Range | Typical Applications |
|-----------|------|-------------|---------------------|
| **FV0** | Micro | < 0.5 L | Sight glasses, sampling |
| **FV1** | Tiny | 0.5-2 L | Small accumulators, reservoirs |
| **FV2** | Small | 2-10 L | Component-level storage |
| **FV3** | Medium | 10-50 L | System reservoirs, accumulators |
| **FV4** | Large | 50-500 L | Service tanks, main reservoirs |
| **FV5** | Mega | > 500 L | Primary fuel tanks (when not cryogenic) |

### 3.3 Data Capacity Bands

| Band Code | Name | Capacity Range | Typical Applications |
|-----------|------|----------------|---------------------|
| **DC0** | Micro | < 100 MB | Real-time buffers, cache |
| **DC1** | Small | 100 MB - 10 GB | Logging, short-term buffers |
| **DC2** | Medium | 10-100 GB | Flight recorders, session data |
| **DC3** | Large | 100 GB - 1 TB | Mission data, video recording |
| **DC4** | Very Large | 1-10 TB | Data hubs, operational storage |
| **DC5** | Mega | 10-100 TB | Data lakes, model registries |
| **DC6** | Tera | > 100 TB | Enterprise archives, cold storage |

---

## 4. Classification Matrix

### 4.1 Energy Storage Classification

| Storage ID | Storage Name | Class | Capacity Band | Criticality |
|-----------|--------------|-------|---------------|-------------|
| S-24-001 | Main Battery Pack Forward | E1 | EC4 | CRITICAL |
| S-24-002 | Main Battery Pack Aft | E1 | EC4 | CRITICAL |
| S-24-003 | Supercapacitor Bank Start | E3 | EC2 | ESSENTIAL |
| S-24-004 | Avionics Backup Battery | E2 | EC2 | CRITICAL |
| S-28-001 | LH₂ Main Tank Starboard | E4 | EF3 | CRITICAL |
| S-28-002 | LH₂ Main Tank Port | E4 | EF3 | CRITICAL |
| S-28-003 | LH₂ Buffer Tank | E4 | EF1 | ESSENTIAL |
| S-80-001 | CO₂ Battery System | E1 | EC5 | CRITICAL |
| S-80-002 | HVDC Bus Buffer | E3 | EC3 | ESSENTIAL |

### 4.2 Fluid Storage Classification

| Storage ID | Storage Name | Class | Capacity Band | Criticality |
|-----------|--------------|-------|---------------|-------------|
| S-21-001 | ECS Primary Thermal Buffer | E5 | FV3 | ESSENTIAL |
| S-29-001 | Hydraulic Main Reservoir | F1 | FV3 | CRITICAL |
| S-29-002 | Hydraulic Accumulator FCS | F2 | FV2 | CRITICAL |
| S-29-003 | Hydraulic Accumulator LG | F2 | FV2 | CRITICAL |
| S-29-004 | Hydraulic Accumulator Brakes | F2 | FV2 | CRITICAL |
| S-38-001 | Potable Water Main Tank | F4 | FV4 | IMPORTANT |
| S-38-003 | Grey Water Tank | F4 | FV4 | IMPORTANT |
| S-38-004 | Black Water Tank | F4 | FV4 | IMPORTANT |

### 4.3 Data Storage Classification

| Storage ID | Storage Name | Class | Capacity Band | Criticality |
|-----------|--------------|-------|---------------|-------------|
| S-31-001 | Flight Data Recorder | D1 | DC2 | CRITICAL |
| S-31-002 | Cockpit Voice Recorder | D1 | DC1 | CRITICAL |
| S-31-003 | Quick Access Recorder | D2 | DC3 | ESSENTIAL |
| S-31-004 | Onboard Data Hub Primary | D2 | DC4 | ESSENTIAL |
| S-46-001 | Digital Data Lake | D3 | DC6 | ESSENTIAL |
| S-46-002 | Model Registry | D3 | DC5 | ESSENTIAL |

---

## 5. Related Documents

- **[95-60-00-002](../95-60-00-002_Storage_Taxonomy_and_Scope.md)**: Storage taxonomy
- **[95-60-00-005](95-60-00-005_Storages_Traceability_Matrix.csv)**: Traceability matrix
- **[95-60-00-006](95-60-00-006_Storages_Registry.json)**: Storage registry with full classification

---

**Document Control**
- **Standard**: OPT-IN Framework v1.5
- **Classification**: Technical Documentation
- **Distribution**: Unrestricted (Open Source)
