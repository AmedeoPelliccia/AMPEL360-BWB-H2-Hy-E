# 02-80-00-002: Cross-ATA Energy Data Map

## Purpose

This document maps energy-related data objects across ATA chapters, identifying data origins, consumers, governance requirements, and traceability links within the AMPEL360 BWB-H2-Hy-E energy ecosystem.

## Scope

The data map covers:

- **Data objects** related to electrical power, batteries, fuel cells, and renewable energy
- **Origins** (source systems and ATA chapters)
- **Consumers** (users of the data within operations, maintenance, and analytics)
- **Governance** (ownership, quality, security, retention)
- **Traceability** (links to requirements, certifications, and standards)

## Energy Data Architecture

### High-Level Data Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    ENERGY DATA ECOSYSTEM                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  [ATA 24] ──> Generator/Distribution Data ──┐                   │
│  [ATA 28] ──> Fuel Cell/H2 Data ────────────┤                   │
│  [ATA 31] ──> Recording/Telemetry ──────────┤                   │
│  [ATA 49] ──> APU Power Data ───────────────┤                   │
│  [ATA 80] ──> Starting/Ground Power ────────┤                   │
│  [ATA 95] ──> AI/ML Analytics ──────────────┤                   │
│                                              │                   │
│                                              ▼                   │
│                                    ┌─────────────────┐           │
│                                    │  ATA 02-80      │           │
│                                    │  Energy Ops     │           │
│                                    │  Integration    │           │
│                                    └─────────────────┘           │
│                                              │                   │
│                    ┌─────────────────────────┼──────────────┐   │
│                    ▼                         ▼              ▼   │
│              Flight Crew                  OCC          Maintenance│
│              Displays                  Dashboards      Analytics │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

## Data Object Catalog

### 1. Electrical Power Generation Data

#### ATA 24-01: Generator Status

**Origin**: [ATA 24 – Electrical Power](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes) Systems

**Data Objects**:
- `Generator_Voltage` (V_ac, V_dc per bus)
- `Generator_Current` (A per phase)
- `Generator_Frequency` (Hz)
- `Generator_Power_Output` (kW)
- `Generator_Temperature` (°C per bearing, winding)
- `Generator_Status` (online, offline, fault)
- `Generator_Runtime_Hours` (cumulative)

**Consumers**:
- Flight deck displays (real-time status)
- Central Maintenance Computer (fault logging)
- OCC dashboards (fleet monitoring)
- Energy optimization algorithms ([02-80-05](./02-80-05_Energy_Optimization/))

**Governance**:
- **Owner**: Electrical Power Systems Engineering
- **Update Frequency**: 1 Hz (status), 0.1 Hz (detailed metrics)
- **Retention**: 30 days hot, 7 years archived
- **Quality**: Per [DO-178C](https://www.rtca.org/) DAL-A for flight-critical data

**Traceability**: [CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes) – Electrical power generation requirements

#### ATA 24-02: Power Distribution

**Origin**: Power Distribution Units (PDU)

**Data Objects**:
- `Bus_Voltage` (per AC/DC bus)
- `Bus_Frequency` (per AC bus)
- `Load_Current` (per feeder)
- `Circuit_Breaker_Status` (per breaker)
- `Power_Quality_THD` (Total Harmonic Distortion)
- `Bus_Tie_Status` (open/closed)

**Consumers**:
- Load management systems ([02-80-02](./02-80-02_Energy_Budget_Management/))
- Real-time monitoring ([02-80-07](./02-80-07_Real_Time_Energy_Monitoring/))
- Anomaly detection algorithms
- Maintenance diagnostics

**Governance**:
- **Owner**: Electrical Power Systems Engineering
- **Update Frequency**: 10 Hz
- **Retention**: 7 days hot, 1 year archived
- **Quality**: High precision (±0.5% voltage, ±1% current)

**Traceability**: [CS-25.1309(b)](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes) – Power distribution integrity

### 2. Battery Energy Storage Data

#### Battery Management System (BMS)

**Origin**: Battery packs with integrated BMS

**Data Objects**:
- `Battery_SOC` (State of Charge, %)
- `Battery_SOH` (State of Health, %)
- `Battery_Voltage` (pack and per-cell, V)
- `Battery_Current` (charge/discharge, A)
- `Battery_Temperature` (per module, °C)
- `Battery_Cycle_Count` (cumulative)
- `Battery_Capacity_Actual` (Ah)
- `Battery_Capacity_Nominal` (Ah)
- `Battery_Internal_Resistance` (mΩ)
- `Battery_Thermal_Runaway_Risk` (boolean flag)

**Consumers**:
- Flight crew displays (SOC, range estimation)
- Battery energy management ([02-80-03](./02-80-03_Battery_Energy_Management/))
- Thermal management systems ([ATA 21](#))
- Predictive maintenance ([02-80-09](./02-80-09_Energy_Systems_Health/))
- Range anxiety mitigation algorithms

**Governance**:
- **Owner**: Energy Storage Systems Engineering
- **Update Frequency**: 1 Hz (SOC/SOH), 10 Hz (voltages/currents)
- **Retention**: 30 days hot, lifetime archived (health data)
- **Security**: Encrypted transmission for safety-critical alarms
- **Quality**: Per [DO-254](https://www.rtca.org/) for BMS hardware

**Traceability**: [CS-25.1309(c)](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes) – Battery system safety and monitoring

### 3. Fuel Cell Power Data

#### ATA 28: Fuel Cell Systems

**Origin**: Fuel cell stack controllers

**Data Objects**:
- `FC_Stack_Voltage` (V per stack)
- `FC_Stack_Current` (A per stack)
- `FC_Power_Output` (kW per stack)
- `FC_Efficiency` (%)
- `FC_H2_Flow_Rate` (kg/h)
- `FC_Coolant_Temperature` (°C)
- `FC_Stack_Temperature` (°C per cell)
- `FC_Membrane_Humidity` (%)
- `FC_Stack_Degradation_Index` (%)
- `FC_Fault_Codes` (enumerated)

**Consumers**:
- Fuel cell interface monitoring ([02-80-04](./02-80-04_Fuel_Cell_Energy_Interface/))
- Power management and load balancing
- Efficiency tracking and optimization
- Prognostics for degradation

**Governance**:
- **Owner**: Propulsion and Energy Systems Engineering
- **Update Frequency**: 1 Hz
- **Retention**: 30 days hot, 7 years archived
- **Quality**: ±2% accuracy on power/efficiency

**Traceability**: Hydrogen fuel system requirements (ATA 28 specific)

### 4. Ground Power Operations Data

#### ATA 80: Ground Power Unit (GPU) Interface

**Origin**: GPU interface unit, APU controller

**Data Objects**:
- `GPU_Connected` (boolean)
- `GPU_Voltage` (V)
- `GPU_Frequency` (Hz)
- `GPU_Power_Supplied` (kW)
- `GPU_Energy_Total` (kWh per session)
- `APU_Running` (boolean)
- `APU_Load` (%)
- `Charging_Active` (boolean)
- `Charging_Power` (kW)
- `Ground_Energy_Cost` (USD per kWh)

**Consumers**:
- Ground operations ([02-80-06](./02-80-06_Ground_Power_Operations/))
- Energy cost tracking ([02-80-12](./02-80-12_Energy_Cost_Optimization/))
- Pre-flight readiness checks
- OCC fleet management

**Governance**:
- **Owner**: Ground Operations and Facilities
- **Update Frequency**: 0.1 Hz
- **Retention**: 90 days hot, 7 years archived (cost data)
- **Security**: Secure for billing and financial data

**Traceability**: Ground support equipment standards, airport interface specifications

### 5. Telemetry and Recording Data

#### ATA 31: Energy Telemetry Recording

**Origin**: Flight Data Recorder (FDR), Quick Access Recorder (QAR)

**Data Objects**:
- Subset of all above energy parameters
- Time-synchronized to aircraft state (flight phase, altitude, airspeed)
- Aggregated energy consumption by system
- Cumulative energy usage per flight

**Consumers**:
- Post-flight analysis ([02-80-08](./02-80-08_Post_Flight_Energy_Analysis/))
- Regulatory reporting
- Fleet performance benchmarking
- AI model training datasets

**Governance**:
- **Owner**: Flight Operations and Safety
- **Update Frequency**: Per [CS-25 Appendix M](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes) FDR requirements
- **Retention**: Regulatory minimum (25 hours FDR), extended QAR retention
- **Security**: Tamper-proof recording, chain-of-custody for investigations

**Traceability**: [CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes), FDR/CVR regulations

### 6. AI/ML Analytics Data

#### ATA 95: Predictive Energy Management

**Origin**: AI/ML models processing energy telemetry

**Data Objects**:
- `Predicted_Load_Profile` (kW over time horizon)
- `Optimized_Power_Allocation` (per system)
- `Anomaly_Score` (per data stream)
- `RUL_Generator` (Remaining Useful Life, hours)
- `RUL_Battery` (cycles or years)
- `Efficiency_Recommendations` (actionable suggestions)
- `Range_Prediction` (nm with confidence intervals)

**Consumers**:
- Energy optimization ([02-80-05](./02-80-05_Energy_Optimization/))
- Predictive maintenance ([02-80-09](./02-80-09_Energy_Systems_Health/))
- Flight crew decision support
- OCC operational planning

**Governance**:
- **Owner**: AI/ML Engineering and Data Science
- **Update Frequency**: Variable (real-time to daily)
- **Retention**: Model outputs 30 days, training data per [EU AI Act](https://eur-lex.europa.eu/homepage.html)
- **Quality**: Model validation per ATA 95 standards
- **Transparency**: Model cards, explainability logs

**Traceability**: [EU AI Act](https://eur-lex.europa.eu/homepage.html) compliance, [DO-178C](https://www.rtca.org/) for embedded AI

## Data Sharing and Interfaces

### Internal Data Sharing (Within Aircraft Systems)

| Source System | Target System | Protocol | Frequency | Security |
|---------------|---------------|----------|-----------|----------|
| Generator ECU | PDU | ARINC 429 | 10 Hz | Integrity-checked |
| BMS | Flight Control Computer | ARINC 664 (AFDX) | 1 Hz | Encrypted |
| Fuel Cell Controller | Power Management Unit | CAN Bus | 1 Hz | Authenticated |
| PDU | Central Maintenance Computer | ARINC 629 | 1 Hz | Signed messages |

### External Data Sharing (Off-Aircraft)

| Source | Destination | Protocol | Frequency | Governance |
|--------|-------------|----------|-----------|------------|
| Aircraft Energy Telemetry | OCC Ground Station | ACARS/FANS | 0.01 Hz (periodic) | Encrypted link |
| FDR/QAR Data | Maintenance Data Lake | Secure File Transfer | Post-flight | Chain of custody |
| Battery Health Data | Manufacturer Cloud | HTTPS/REST | Daily | Anonymized, consent-based |
| Fuel Cell Diagnostics | OEM Support Portal | HTTPS/REST | On-demand | NDA-protected |

## Data Governance Framework

### Data Ownership

- **Flight-Critical Data**: Owned by Flight Operations, delegated read to Maintenance and Engineering
- **Maintenance Data**: Owned by Maintenance, shared with Engineering and OEMs
- **Performance Data**: Owned by Engineering, shared with Sustainability and Finance
- **Cost Data**: Owned by Finance, shared with Operations for optimization

### Data Quality Standards

- **Accuracy**: Per sensor specifications and calibration schedules
- **Completeness**: 99.9% uptime for flight-critical telemetry
- **Timeliness**: Real-time data latency < 100 ms
- **Consistency**: Cross-validation between redundant sensors

### Data Retention and Archival

| Data Type | Hot Storage | Warm Storage | Cold Archive | Deletion |
|-----------|-------------|--------------|--------------|----------|
| Real-time Telemetry | 7 days | 30 days | 1 year | After 1 year (unless incident) |
| Flight Data (QAR) | 90 days | 1 year | 7 years | Per regulatory requirements |
| Battery Health History | Lifetime | Lifetime | Lifetime | Never (lifecycle tracking) |
| Cost and Billing | 1 year | 7 years | 10 years | Per tax/audit requirements |
| AI Model Training Data | 6 months | 2 years | 5 years | Per [EU AI Act](https://eur-lex.europa.eu/homepage.html) |

### Data Security and Privacy

- **Encryption**: AES-256 for data at rest, TLS 1.3 for data in transit
- **Access Control**: Role-based access control (RBAC) with audit logging
- **Anonymization**: PII removed from datasets shared externally
- **Compliance**: GDPR for personal data, export control for sensitive technologies

## Traceability Matrix

### Certification Requirements to Data Objects

| Requirement | Data Objects | Justification |
|-------------|--------------|---------------|
| [CS-25.1309(b)](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes) – Power sources | Generator_Status, Bus_Voltage | Demonstrate adequate power for all flight phases |
| [CS-25.1309(c)](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes) – Battery safety | Battery_SOC, Battery_Temperature, Thermal_Runaway_Risk | Monitor battery within safe operating envelope |
| [CS-25.1309(d)](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes) – Load shedding | Load_Current, Circuit_Breaker_Status | Verify load shedding logic in degraded modes |
| [DO-178C](https://www.rtca.org/) – Software assurance | All control algorithms | Trace software requirements to data inputs/outputs |
| [EU AI Act](https://eur-lex.europa.eu/homepage.html) – AI transparency | Predicted_Load_Profile, Anomaly_Score | Document AI model inputs, outputs, and decisions |

### Data Objects to ATA Chapters

| Data Object | Primary ATA | Secondary ATAs | Notes |
|-------------|-------------|----------------|-------|
| Generator_Voltage | ATA 24 | ATA 02-80-01 | Monitored in 02-80 for operations |
| Battery_SOC | ATA 24 | ATA 02-80-03 | Battery management in operations context |
| FC_Power_Output | ATA 28 | ATA 02-80-04 | Fuel cell operational data |
| GPU_Power_Supplied | ATA 80 | ATA 02-80-06 | Ground power interface |
| Predicted_Load_Profile | ATA 95 | ATA 02-80-05 | AI/ML optimization outputs |

## Data Lineage Example: Battery SOC

To illustrate end-to-end data lineage:

1. **Origin**: Battery cell voltage sensors (hardware)
2. **Collection**: Battery Management System (BMS) microcontroller samples at 100 Hz
3. **Processing**: BMS computes SOC using Coulomb counting + Kalman filter
4. **Transmission**: BMS sends SOC via ARINC 664 to Flight Control Computer (1 Hz)
5. **Display**: Flight deck MFD shows battery gauge and range estimate
6. **Recording**: FDR logs SOC at 1 Hz per [CS-25 Appendix M](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes)
7. **Downlink**: ACARS sends SOC snapshot to OCC every 5 minutes
8. **Storage**: OCC stores in time-series database for analytics
9. **Analytics**: AI model ingests historical SOC for range prediction
10. **Archival**: SOC data archived for battery lifecycle tracking

**Governance**: Each step has defined ownership, quality checks, and traceability to [CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes).

## Integration Points with Other Documents

- **Energy Operations Overview**: [02-80-00-001](./02-80-00-001_Energy_Operations_Overview.md) – High-level context for this data map
- **Energy Management Strategy**: [02-80-00-003](./02-80-00-003_Energy_Management_Strategy.md) – How data informs strategy
- **Power Budget Tracking**: [02-80-00-004](./02-80-00-004_Power_Budget_Tracking.md) – Data used for budget calculations
- **Electrical Power Monitoring**: [02-80-01](./02-80-01_Electrical_Power_Monitoring/) – Detailed monitoring architecture
- **Battery Energy Management**: [02-80-03](./02-80-03_Battery_Energy_Management/) – Battery-specific data flows

## References

### Standards and Regulations

- [CS-25 – Certification Specifications for Large Aeroplanes](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes)
- [CS-25.1309 – Equipment, Systems, and Installations](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes)
- [DO-178C – Software Considerations in Airborne Systems](https://www.rtca.org/)
- [DO-254 – Design Assurance Guidance for Airborne Electronic Hardware](https://www.rtca.org/)
- [EU AI Act – Artificial Intelligence Act](https://eur-lex.europa.eu/homepage.html)
- [GDPR – General Data Protection Regulation](https://eur-lex.europa.eu/homepage.html)

### Related ATA Chapters

- [ATA 24 – Electrical Power](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes)
- [ATA 28 – Fuel (Hydrogen)](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes)
- [ATA 31 – Indicating/Recording](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes)
- [ATA 80 – Starting](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-11-21*.

---
