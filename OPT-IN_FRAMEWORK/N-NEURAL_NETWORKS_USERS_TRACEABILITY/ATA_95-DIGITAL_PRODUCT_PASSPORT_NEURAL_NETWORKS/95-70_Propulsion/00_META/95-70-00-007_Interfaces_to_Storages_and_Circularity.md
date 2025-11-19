# 95-70-00-007: Interfaces to Storages and Circularity

## 1. Introduction

This document describes the interfaces between the Propulsion systems (ATA 70-79) and the Storage/Circularity systems within the AMPEL360 BWB H₂ Hy-E Q100 aircraft. It focuses on physical, data, and energy flows that enable the circular economy features and cryogenic storage integration.

## 2. H₂ Storage Interfaces (ATA 28)

### 2.1 Physical Interface

**Connection**: H₂ Storage Tanks → Engine Fuel Feed

| Parameter | Specification |
|-----------|--------------|
| **Fluid** | Liquid Hydrogen (LH₂) |
| **Temperature** | -253°C ± 3°C |
| **Pressure Range** | 3-6 bar (storage) → 12-15 bar (engine inlet) |
| **Flow Rate** | 0-10 kg/min per engine |
| **Line Material** | Stainless steel 316L, vacuum-insulated |
| **Connection Type** | Quick-disconnect cryogenic coupling |
| **Leak Detection** | H₂ sensors, pressure monitoring |

**Documents**:
- Storage Side: `95-60-28` (Storage DPP)
- Propulsion Side: `95-70-73-004` (Fuel Supply Interfaces)
- Interface Control: `ICD-28-73-H2-Supply`

### 2.2 Control Interface

| Signal | Direction | Protocol | Description |
|--------|-----------|----------|-------------|
| Fuel Demand | Propulsion → Storage | CAN Bus | Requested fuel flow rate |
| Tank Pressure | Storage → Propulsion | ARINC 429 | Current tank pressure |
| Tank Temperature | Storage → Propulsion | ARINC 429 | LH₂ temperature |
| Tank Quantity | Storage → Propulsion | ARINC 429 | Remaining fuel mass |
| Valve Commands | Propulsion → Storage | Discrete | Fuel shutoff valves |
| Emergency Shutoff | Either → Both | Discrete | Immediate fuel cutoff |

### 2.3 Safety Interface

- **Firewall Penetration**: Fuel lines pass through firewall with isolation valves
- **Emergency Venting**: H₂ vent system isolated from propulsion exhaust
- **Leak Detection Zone**: Continuous H₂ monitoring in nacelle and pylon
- **Automatic Shutoff**: Triggered by fire, leak detection, or crash sensor

---

## 3. CO₂ Capture System Interfaces (ATA 21-80)

### 3.1 Thermal Energy Interface

**Purpose**: Use propulsion exhaust waste heat to power CO₂ capture solid-state battery system

| Parameter | Specification |
|-----------|--------------|
| **Heat Source** | Exhaust gas heat exchanger |
| **Temperature Range** | 150-400°C (exhaust side) |
| **Heat Transfer Rate** | 50-200 kW per engine |
| **Working Fluid** | Thermal oil or glycol loop |
| **Interface Location** | Exhaust duct, 1-2 meters aft of nozzle |
| **Control** | Variable flow rate based on CO₂ capture demand |

**Documents**:
- Propulsion Side: `95-70-78-004` (Exhaust Heat Recovery)
- CO₂ Capture Side: `95-30-21-80` (CO₂ Circularity)
- Interface Control: `ICD-78-21-80-Heat`

### 3.2 Data Interface

| Signal | Direction | Protocol | Description |
|--------|-----------|----------|-------------|
| Exhaust Temperature | Propulsion → CO₂ | ARINC 429 | Available thermal energy |
| CO₂ Demand | CO₂ → Propulsion | CAN Bus | Requested heat flow rate |
| Heat Exchanger Status | Propulsion → CO₂ | Discrete | HX operational status |
| Valve Position | Propulsion → CO₂ | Analog | Thermal loop flow control |

### 3.3 CO₂ Emissions Monitoring

| Parameter | Specification |
|-----------|--------------|
| **Emissions Sensors** | NOx, CO, particulates (if combustion engine) |
| **Sampling Location** | Exhaust duct, 0.5 meters aft of nozzle |
| **Data Rate** | 1 Hz continuous |
| **Data Destination** | CAOS, ESG Reporting, CO₂ Capture Controller |
| **Compliance** | ICAO Annex 16 Chapter 14 |

**Note**: Pure electric propulsion produces zero direct emissions; monitoring applies only if hybrid combustion is used.

---

## 4. Bleed Air Circularity (ATA 75 → ATA 21, 30, 36)

### 4.1 Energy Recovery from Bleed Air

**Purpose**: Minimize energy waste by recovering bleed air thermal energy

| Parameter | Specification |
|-----------|--------------|
| **Bleed Source** | Compressor stage (if turbine engine) or electric compressor |
| **Pressure** | 30-45 psi |
| **Temperature** | 200-400°C |
| **Mass Flow** | 0.5-2.0 kg/s |
| **Applications** | ECS, ice protection, cabin pressurization |
| **Heat Recovery** | Preconditioner for CO₂ capture or cabin heating |

**Documents**:
- Propulsion: `95-70-75-004` (Energy Recovery and Circularity Links)
- ECS: `95-30-21` (Air Conditioning)
- Ice Protection: `95-30-30` (Ice and Rain Protection)

### 4.2 Circularity Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Bleed Air Energy Recovery Efficiency | >60% | TBD |
| Exhaust Heat Recovery for CO₂ | >40% | TBD |
| Waste Heat Utilization | >50% | TBD |

---

## 5. Lubrication Oil Circularity (ATA 79)

### 5.1 Oil Lifecycle Management

**Purpose**: Extend oil life, monitor quality, and enable recycling/reuse

| Parameter | Specification |
|-----------|--------------|
| **Oil Type** | Synthetic aviation oil (MIL-PRF-23699) |
| **Oil Capacity** | 15-20 liters per engine |
| **Change Interval** | 2000 flight hours or condition-based |
| **Quality Monitoring** | Metal particle detection, viscosity, acidity |
| **Recycling** | Off-wing filtration and reconditioning |

**Documents**:
- Propulsion: `95-70-79-004` (Maintenance Intervals and Circularity Links)
- Circularity: `95-30` (Circularity and ESG Reporting)

### 5.2 Predictive Oil Changes

- **Neural Network Model**: Predicts oil degradation based on temperature, pressure, contamination
- **Benefit**: Avoid premature oil changes, reduce waste
- **Data Source**: ATA 77 health monitoring sensors
- **Model**: `oil_quality_predictor_v1.0`

---

## 6. Component End-of-Life and Circularity

### 6.1 Propulsion Component Recycling

| Component | Material | Recycling Method | Recovery Rate |
|-----------|----------|------------------|---------------|
| **Propulsor Blades** | CFRP | Pyrolysis or chemical recycling | 70-80% |
| **Nacelle Structure** | Aluminum, CFRP | Material separation, melting/reprocessing | 85-95% |
| **FADEC Units** | Electronics, aluminum housing | E-waste recycling, precious metal recovery | 60-70% |
| **Fuel Lines** | Stainless steel | Melting and reprocessing | 95-99% |
| **Oil Coolers** | Aluminum, copper | Material separation, melting | 90-95% |

**Documents**:
- Circularity Plan: `95-30-Circularity`
- Component Decommissioning: `95-70-XX-005` (each subsystem)

### 6.2 Material Passport

Each propulsion component includes a **Material Passport** with:
- Material composition (bill of materials)
- Hazardous substances declaration (REACH, RoHS)
- Recycling instructions
- Supplier information
- End-of-life handling requirements

**Storage**: `95-70-00-006_Propulsion_Assets_Registry.json` (extended fields)

---

## 7. Interface Control Documents (ICDs)

### 7.1 Active ICDs

| ICD Number | Title | Rev | Date | Parties |
|------------|-------|-----|------|---------|
| ICD-28-73-H2 | H₂ Storage to Engine Fuel Supply | A | 2025-11-10 | ATA 28 / ATA 73 |
| ICD-78-21-80 | Exhaust Heat to CO₂ Capture | A | 2025-11-12 | ATA 78 / ATA 21-80 |
| ICD-75-21 | Bleed Air to ECS | A | 2025-10-15 | ATA 75 / ATA 21 |
| ICD-75-30 | Bleed Air to Ice Protection | A | 2025-10-20 | ATA 75 / ATA 30 |
| ICD-76-24 | Generator Interface | A | 2025-09-25 | ATA 76 / ATA 24 |

### 7.2 ICD Management

- **Owner**: Systems Integration Team
- **Review Cycle**: Quarterly
- **Change Control**: Configuration Control Board (CCB)
- **Distribution**: All interface stakeholders

---

## 8. Circularity Metrics and Reporting

### 8.1 Key Performance Indicators (KPIs)

| KPI | Target | Current | Measurement Method |
|-----|--------|---------|-------------------|
| **Energy Recovery Efficiency** | >55% | TBD | (Recovered Energy) / (Waste Energy Available) |
| **Material Recycling Rate** | >80% | TBD | (Recycled Mass) / (Total Decommissioned Mass) |
| **Component Reuse Rate** | >30% | TBD | (Reused Components) / (Total Components EOL) |
| **CO₂ Capture Enhancement** | +5 kg/flight | TBD | Net CO₂ removed per flight |
| **Oil Life Extension** | +20% | TBD | (Actual Hours) / (Baseline Hours) |

### 8.2 Reporting Cadence

- **Monthly**: Internal circularity dashboard (CAOS)
- **Quarterly**: Executive summary to leadership
- **Annually**: Public ESG report (if applicable)
- **Regulatory**: As required by EU DPP Regulation

---

## 9. Neural Network Integration

### 9.1 CAOS Circularity Module

**Purpose**: Optimize energy recovery and predict component end-of-life

**Functions**:
- **Real-Time Optimization**: Adjust bleed air extraction, heat exchanger flow rates
- **Predictive EOL**: Forecast component retirement based on usage patterns
- **Recycling Advisor**: Recommend optimal recycling pathways
- **Fleet Learning**: Share best practices across aircraft fleet

**Model**: `caos_circularity_optimizer_v1.0`

**Documents**: `95-20-70-NN-Circularity` (CAOS Modules)

---

## 10. Future Enhancements

### 10.1 Advanced Circularity Features

- **On-Wing Oil Reconditioning**: Real-time filtration and additive replenishment
- **Hydrogen Recirculation**: Capture boil-off gas for reuse
- **3D Printed Spare Parts**: On-demand manufacturing of replacement parts
- **Blockchain Traceability**: Immutable record of component lifecycle

### 10.2 Technology Roadmap

| Year | Enhancement | Expected Benefit |
|------|-------------|------------------|
| 2026 | Predictive oil quality NN model | +15% oil life extension |
| 2027 | Advanced heat recovery system | +10% energy recovery |
| 2028 | Component refurbishment program | +25% reuse rate |
| 2029 | Digital material passport | 100% traceability |

---

## 11. Related Documents

- [95-70-00-001: Propulsion DPP Overview](../95-70-00-001_Propulsion_DPP_Overview.md)
- [95-70-73-004: H₂ Storage Interfaces](../95-70-73_Engine_Fuel_and_Supply/95-70-73-004_Interfaces_to_LH2_Storages_95-60-28_and_28_Fuel.md)
- [95-70-78-004: CO₂ Capture Interfaces](../95-70-78_Exhaust_and_Emissions/95-70-78-004_Interfaces_to_CO2_Capture_or_PostProcessing_Systems.md)
- [95-30: Circularity and ESG Reporting](../../95-30_Circularity/)

---

## 12. Version History

| Version | Date       | Author               | Changes                    |
|---------|------------|----------------------|----------------------------|
| 1.0     | 2025-11-17 | AMPEL360 Doc Team    | Initial creation           |

---

**Document ID**: 95-70-00-007  
**Status**: Active  
**Classification**: Internal Use  
**Next Review**: 2026-02-17
