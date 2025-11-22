# 85-70-01-A-004: Charging Integration

## Document Information

- **Document ID**: 85-70-01-A-004
- **Title**: Charging Integration for Electric GSE
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

---

## 1. Purpose

This document defines the requirements and guidelines for integrating battery-electric Ground Support Equipment (GSE) with airport charging infrastructure for AMPEL360 BWB-H2-Hy-E operations.

---

## 2. Charging Infrastructure Overview

### 2.1 Charging Levels

| Level | Type | Power | Voltage | Current | Charging Time (150 kWh) | Use Case |
|-------|------|-------|---------|---------|-------------------------|----------|
| **Level 1** | AC | 3-7 kW | 230V 1φ | 16A | 20-50 hours | Emergency, overnight |
| **Level 2** | AC | 7-22 kW | 230-400V 1φ/3φ | 32A | 7-21 hours | Depot charging, overnight |
| **Level 3** | DC Fast | 50-150 kW | 400-800 VDC | 125-200A | 1-3 hours | Opportunity charging |
| **Level 4** | DC Ultra-Fast | 150-350 kW | 400-800 VDC | 300-500A | 0.5-1 hour | High-turnover vehicles |

### 2.2 Charging Standards

#### AC Charging

- **Type 2 (IEC 62196-2)**: European standard, 3-phase AC
  - Single-phase: Up to 7.4 kW (230V, 32A)
  - Three-phase: Up to 22 kW (400V, 32A)
  - Communication: Control Pilot signal per [IEC 61851-1](https://webstore.iec.ch/publication/6035)

#### DC Charging

- **CCS (Combined Charging System) Combo 2**: Preferred standard
  - DC power up to 350 kW
  - Communication: [ISO 15118](https://www.iso.org/standard/55366.html) (PLC - Power Line Communication)
  - Backward compatible with Type 2 AC charging
  
- **CHAdeMO**: Alternative DC standard
  - Power up to 62.5 kW (CHAdeMO 1.0) or 400 kW (CHAdeMO 3.0)
  - Communication: CAN bus

---

## 3. Charging Station Design

### 3.1 Depot Charging Stations

#### Fixed Charging Pedestals

- **Quantity**: 1 charger per 2-3 vehicles (optimized for depot layout)
- **Power**: 22 kW AC (Type 2) or 50 kW DC (CCS)
- **Mounting**: Bollard-style or wall-mounted
- **Cable Length**: 5-7 meters (sufficient reach)
- **Weatherproofing**: IP54 minimum, outdoor-rated
- **Access Control**: RFID card or app-based authentication
- **Payment**: Fleet account or credit card (optional)

#### Overhead Pantograph Charging (Optional)

- **Power**: 50-150 kW DC
- **Mechanism**: Automated pantograph drops onto vehicle roof connector
- **Use Case**: High-throughput depot with limited space
- **Advantages**: No cable handling, faster connection
- **Disadvantages**: Higher capital cost, requires vehicle roof connector

### 3.2 Opportunity Charging Stations

#### On-Apron Charging

- **Location**: Strategic locations on apron (near aircraft stands)
- **Power**: 50-150 kW DC fast charging
- **Cable Management**: Retractable cable reels
- **Safety**: Conspicuous markings, FOD prevention
- **Weather Protection**: All-weather operation, heated cables for cold climates

#### Charging While Working (CWW)

- **Concept**: Charge during idle periods (e.g., belt loader waiting for aircraft)
- **Power**: 22-50 kW
- **Connector**: Magnetic or automated connection
- **Implementation**: Pilot program for high-utilization equipment

---

## 4. Electrical Infrastructure

### 4.1 Grid Connection

- **Voltage**: Medium voltage (e.g., 11 kV, 20 kV) or low voltage (400V)
- **Transformer**: Dedicated substation for GSE charging
- **Capacity**: Design for peak demand (e.g., 50 chargers × 50 kW = 2.5 MW)
- **Power Factor Correction**: PFC to maintain unity power factor
- **Harmonic Filtering**: Active filters to meet [IEC 61000-3-2](https://webstore.iec.ch/publication/4149)

### 4.2 Load Management

#### Smart Load Balancing

- **Dynamic Load Allocation**: Distribute available power among active chargers
- **Priority System**: 
  - High priority: Cargo loaders, tugs (critical for operations)
  - Medium priority: Belt loaders
  - Low priority: Tractors (long idle times)
- **Peak Shaving**: Reduce charging power during grid peak demand
- **Grid Services**: Participate in demand response programs

#### Energy Storage Integration

- **Battery Energy Storage System (BESS)**: 
  - Capacity: 500 kWh - 2 MWh (depending on depot size)
  - Purpose: Peak shaving, renewable integration, grid backup
- **Solar Integration**: On-site solar PV to offset charging energy
- **V2G (Vehicle-to-Grid)**: Bidirectional charging for grid support (future)

### 4.3 Renewable Energy Integration

- **On-Site Solar**: Rooftop or carport solar PV
- **Wind Energy**: Small wind turbines (if location suitable)
- **Renewable Energy Certificates (RECs)**: Purchase RECs to offset grid energy
- **Target**: 50% renewable energy by 2030, 100% by 2040

---

## 5. Communication and Software

### 5.1 Charging Communication Protocols

#### ISO 15118 (Plug & Charge)

- **Function**: Automated authentication and billing
- **Features**:
  - Automatic vehicle identification
  - Encrypted communication
  - Dynamic pricing and load management
- **Implementation**: CCS Combo 2 with PLC modem

#### OCPP (Open Charge Point Protocol)

- **Version**: OCPP 1.6J or OCPP 2.0.1
- **Function**: Communication between chargers and management system
- **Features**:
  - Remote monitoring and control
  - Firmware updates
  - Transaction management
  - Smart charging profiles

### 5.2 Fleet Management System Integration

- **Real-Time Monitoring**:
  - Vehicle location and SOC
  - Charger availability and status
  - Energy consumption and costs
- **Automated Dispatch**:
  - Assign vehicles based on SOC and operational needs
  - Route vehicles to available chargers
- **Predictive Charging**:
  - Predict charging needs based on schedule
  - Optimize charging times for cost and grid load

### 5.3 Data Analytics

- **Energy Consumption**: Track kWh per vehicle, per day, per operation
- **Charging Efficiency**: Monitor charger and vehicle efficiency
- **Battery Health**: SOH tracking across fleet (see [85-70-06-002](../../85-70-06_Maintenance_and_Diagnostics/85-70-06-002_Battery_Health_Monitoring.md))
- **Cost Analysis**: Energy costs, demand charges, time-of-use optimization
- **Carbon Footprint**: Lifecycle emissions tracking

---

## 6. Safety and Standards

### 6.1 Electrical Safety

- **Ground Fault Protection**: Residual Current Device (RCD) per [IEC 60364-4-41](https://webstore.iec.ch/publication/1862)
- **Overcurrent Protection**: Circuit breakers and fuses
- **Arc Fault Detection**: [IEC 62606](https://webstore.iec.ch/publication/7267)
- **Insulation Monitoring**: For DC charging systems
- **Emergency Stop**: E-stop buttons on chargers and vehicles

### 6.2 Physical Safety

- **Conspicuous Markings**: High-visibility paint for charging areas
- **Lighting**: Adequate lighting for night operations
- **Fire Suppression**: Fire extinguishers and automatic systems in charging depot
- **Ventilation**: Adequate ventilation for battery off-gassing (rare but required)
- **FOD Prevention**: Cable management to prevent Foreign Object Debris on apron

### 6.3 Cybersecurity

- **Encrypted Communication**: TLS/SSL for all network traffic
- **Authentication**: Strong passwords and certificate-based auth
- **Firmware Security**: Signed firmware updates
- **Network Segmentation**: Isolate charging network from airport IT network
- **Compliance**: [IEC 62443](https://webstore.iec.ch/publication/7030) - Industrial communication networks security

### 6.4 Standards Compliance

- [IEC 61851-1](https://webstore.iec.ch/publication/6035) – Electric vehicle conductive charging system
- [IEC 62196](https://webstore.iec.ch/publication/6614) – Plugs, socket-outlets, vehicle connectors
- [ISO 15118](https://www.iso.org/standard/55366.html) – Vehicle-to-grid communication
- [SAE J1772](https://www.sae.org/standards/content/j1772_201710/) – Electric vehicle conductive charge coupler
- [UL 2202](https://www.ul.com/resources/ul-2202-outline-investigation-electric-vehicle-ev-charging-system-equipment) – EV charging system equipment

---

## 7. Operational Procedures

### 7.1 Charging Protocols

#### Standard Charging Procedure

1. **Park Vehicle**: Align vehicle with charging station
2. **Connect Cable**: Plug in charging connector (or automated pantograph)
3. **Authentication**: Tap RFID card or app authentication
4. **Initiate Charging**: Charger performs safety checks and starts charging
5. **Monitor**: Driver or system monitors charging status
6. **Complete Charging**: Charger stops at target SOC or time limit
7. **Disconnect**: Unplug connector and stow cable
8. **Return to Service**: Vehicle ready for operation

#### Opportunity Charging Procedure

1. **Identify Idle Time**: Detect vehicle idle >15 minutes
2. **Dispatch to Charger**: Fleet management system sends vehicle to nearest available charger
3. **Quick Charge**: 10-15 minute top-up (add 20-30% SOC)
4. **Return to Service**: Vehicle returns to operational area

### 7.2 Maintenance and Inspection

- **Daily**: Visual inspection of cables and connectors
- **Weekly**: Test charging stations, verify communication
- **Monthly**: Clean connectors, inspect cable wear
- **Quarterly**: Thermal imaging of electrical connections
- **Annually**: Full electrical safety inspection and testing

---

## 8. Performance Metrics

### 8.1 Key Performance Indicators

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Charger Uptime | >98% | Availability tracking |
| Charging Efficiency (AC to Battery) | >92% | Energy metering |
| Average Charging Time (to 80%) | <2 hours (DC), <8 hours (AC) | Transaction logs |
| Energy Cost per kWh | <0.12 EUR/kWh | Utility billing data |
| Renewable Energy Fraction | >50% by 2030 | REC tracking |
| Fleet SOC (minimum) | >30% at all times | Real-time monitoring |
| Charger Utilization | 40-60% (optimal) | Transaction data |

### 8.2 Data Collection and Reporting

- **Real-Time Dashboard**: Display for depot managers
- **Daily Reports**: Energy consumption, costs, vehicle SOC
- **Monthly Reports**: Trends, anomalies, maintenance needs
- **Annual Reports**: ROI analysis, carbon footprint, performance vs. targets

---

## 9. Cost Analysis

### 9.1 Capital Expenditure (CapEx)

| Item | Unit Cost (EUR) | Quantity (Example) | Total Cost (EUR) |
|------|-----------------|-------------------|------------------|
| Level 2 AC Charger (22 kW) | 5,000 | 30 | 150,000 |
| DC Fast Charger (50 kW) | 30,000 | 15 | 450,000 |
| DC Ultra-Fast Charger (150 kW) | 75,000 | 5 | 375,000 |
| Electrical Infrastructure | 200,000 | 1 | 200,000 |
| Network and Software | 50,000 | 1 | 50,000 |
| Installation and Commissioning | 100,000 | 1 | 100,000 |
| **Total CapEx** | | | **1,325,000** |

### 9.2 Operational Expenditure (OpEx)

| Item | Annual Cost (EUR) |
|------|-------------------|
| Electricity (2 GWh @ 0.12 EUR/kWh) | 240,000 |
| Maintenance and Repairs | 30,000 |
| Network and Software Subscriptions | 10,000 |
| Personnel (part-time charging coordinator) | 20,000 |
| **Total Annual OpEx** | **300,000** |

### 9.3 Return on Investment (ROI)

- **Diesel GSE Annual Fuel Cost**: ~600,000 EUR (for equivalent fleet)
- **Annual Savings**: 600,000 - 300,000 = **300,000 EUR**
- **Payback Period**: 1,325,000 / 300,000 = **4.4 years**
- **Additional Benefits**: Reduced maintenance, zero emissions, regulatory compliance

---

## 10. Future Developments

### 10.1 Wireless Charging

- **Technology**: Inductive charging pads
- **Power**: 20-100 kW
- **Advantages**: No cable handling, automated
- **Challenges**: Lower efficiency (~85-90%), higher cost
- **Timeline**: Pilot projects 2026-2027

### 10.2 Battery Swapping

- **Concept**: Replace depleted battery with charged battery
- **Swap Time**: 5-10 minutes
- **Use Case**: High-utilization vehicles (tugs, cargo loaders)
- **Challenges**: Standardization, logistics, capital cost
- **Timeline**: Feasibility study 2025-2026

### 10.3 Vehicle-to-Grid (V2G)

- **Function**: Bidirectional charging (discharge battery to grid)
- **Applications**: Grid stabilization, peak shaving, renewable integration
- **Requirements**: Bidirectional inverters, grid operator agreements
- **Timeline**: Pilot projects 2027-2028

---

## 11. Cross-References

### 11.1 Internal (ATA 85)

- [85-70-01-A-003_Battery_Systems.md](./85-70-01-A-003_Battery_Systems.md) – Battery specifications
- [85-70-01-005_Power_Electronics.md](../85-70-01-005_Power_Electronics.md) – On-board charger design
- [85-70-04](../../85-70-04_Charging_Infrastructure/) – Charging infrastructure design
- [85-70-06](../../85-70-06_Maintenance_and_Diagnostics/) – Maintenance procedures
- [85-40_Software](../../../85-40_Software/) – Fleet management software
- [85-80_Energy](../../../85-80_Energy/) – Energy management systems

### 11.2 External (Other ATAs)

- [ATA 95 – Digital Product Passport](../../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/) – Energy traceability

---

## 12. Status and Next Steps

- **Current Phase**: Requirements definition and RFP preparation
- **Next Phase**: Vendor selection and pilot deployment
- **Dependencies**: Airport electrical infrastructure upgrades, fleet procurement

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22.

---

**End of Document**
