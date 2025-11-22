# 85-70-01-A-003: Battery Systems

## Document Information

- **Document ID**: 85-70-01-A-003
- **Title**: Battery Systems for Electric GSE
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

---

## 1. Purpose

This document provides detailed specifications for battery systems used in battery-electric Ground Support Equipment (GSE) for AMPEL360 BWB-H2-Hy-E operations.

---

## 2. Battery Chemistry Selection

### 2.1 Lithium-Ion Chemistry Comparison

| Chemistry | Energy Density (Wh/kg) | Cycle Life | Safety | Cost | Best Application |
|-----------|------------------------|------------|--------|------|------------------|
| **LFP** (LiFePO₄) | 120-160 | 3,000-6,000 | Excellent | Medium | Tugs, tractors, belt loaders |
| **NMC** (Ni-Mn-Co) | 200-260 | 1,500-3,000 | Good | Medium-High | Cargo loaders, high-power applications |
| **NCA** (Ni-Co-Al) | 220-270 | 1,000-2,000 | Moderate | High | Performance vehicles (less common in GSE) |
| **LTO** (Li₄Ti₅O₁₂) | 70-100 | 10,000-20,000 | Excellent | High | Fast-charging applications |

### 2.2 Recommended Chemistry by GSE Type

- **Battery Electric Tugs**: LFP (safety, longevity, cost)
- **Belt Loaders**: LFP (safety, moderate power)
- **Baggage Tractors**: LFP (cost-effective, long life)
- **Cargo Loaders**: NMC (high energy density for extended operation)
- **High-Performance Applications**: NMC or NCA (when weight is critical)

---

## 3. Battery Pack Architecture

### 3.1 Cell Configuration

#### Example: 400 kWh Battery Pack (Tug)

- **Cell Type**: LFP prismatic or pouch cells
- **Cell Capacity**: 280 Ah (3.2V nominal)
- **Cell Configuration**: 140S2P (140 series, 2 parallel)
- **Nominal Voltage**: 448 VDC (140 × 3.2V)
- **Total Energy**: 400 kWh
- **Pack Weight**: ~2,600 kg (specific energy ~154 Wh/kg)

#### Example: 150 kWh Battery Pack (Belt Loader)

- **Cell Type**: LFP prismatic cells
- **Cell Capacity**: 200 Ah (3.2V nominal)
- **Cell Configuration**: 120S2P (120 series, 2 parallel)
- **Nominal Voltage**: 384 VDC
- **Total Energy**: 154 kWh
- **Pack Weight**: ~1,050 kg (specific energy ~147 Wh/kg)

### 3.2 Module Design

- **Cells per Module**: 12-24 cells
- **Module Voltage**: 38.4-76.8 VDC (LFP)
- **Modules per Pack**: 8-16 modules
- **Cooling**: Liquid cooling plates between modules
- **Electrical Connection**: Busbar or flexible cables with fuses
- **Mechanical Support**: Aluminum or composite housing

### 3.3 Pack Enclosure

- **Material**: Aluminum alloy or steel (corrosion-resistant)
- **Protection Rating**: IP67 (dust-tight, water-resistant)
- **Impact Resistance**: Meets [UN 38.3](https://unece.org/transportdangerous-goods/un-manual-tests-and-criteria-rev6-2015) vibration and shock tests
- **Fire Protection**: Intumescent coating or fire-resistant materials
- **Mounting**: Vibration-isolated mounting to vehicle frame

---

## 4. Battery Management System (BMS)

### 4.1 BMS Architecture

- **Topology**: Distributed BMS with master-slave architecture
  - **Slave BMS**: One per module (cell monitoring)
  - **Master BMS**: Overall pack management and communication
- **Communication**: [CAN bus](https://www.can-cia.org/) or daisy-chain

### 4.2 Cell Monitoring

- **Voltage Monitoring**: ±5 mV accuracy per cell
- **Current Sensing**: Hall-effect or shunt resistor, ±0.5% accuracy
- **Temperature Monitoring**: NTC thermistors, ±2°C accuracy
- **Sampling Rate**: 1-10 Hz (configurable)

### 4.3 State Estimation Algorithms

- **State of Charge (SOC)**: 
  - Coulomb counting with voltage correction
  - Accuracy: ±3% over full SOC range
- **State of Health (SOH)**:
  - Capacity fade tracking
  - Internal resistance increase monitoring
- **State of Power (SOP)**:
  - Real-time charge/discharge power limits
  - Temperature and SOC dependent
- **Remaining Range**:
  - Based on SOC, historical consumption, and vehicle load

### 4.4 Cell Balancing

#### Passive Balancing

- **Method**: Dissipate excess energy through resistors
- **Balancing Current**: 100-200 mA per cell
- **Efficiency**: Energy lost as heat
- **Use Case**: Low-cost applications, maintenance charging

#### Active Balancing (Recommended)

- **Method**: Transfer energy from high-voltage cells to low-voltage cells
- **Balancing Current**: 5-10 A per cell
- **Efficiency**: >90%
- **Use Case**: High-capacity packs, fast charging

### 4.5 Thermal Management Control

- **Cooling System**: Liquid cooling with 50/50 water-glycol
- **Heating System**: PTC heaters or coolant heaters for cold climates
- **Target Temperature Range**: 20-35°C (optimal performance)
- **Control Strategy**:
  - Pre-conditioning before charging (warm battery in cold weather)
  - Active cooling during fast charging or heavy load
  - Thermal runaway detection and mitigation

---

## 5. Safety Features

### 5.1 Electrical Safety

- **High-Voltage Contactors**: Main positive and negative contactors
- **Pre-charge Circuit**: Limits inrush current to DC bus capacitors
- **Fuses**: Module-level and pack-level fusing
- **Insulation Monitoring**: Continuous monitoring of HV isolation to chassis
- **High-Voltage Interlock Loop (HVIL)**: Monitors integrity of HV connectors

### 5.2 Thermal Safety

- **Thermal Runaway Detection**: 
  - Rapid temperature rise detection (>5°C/min)
  - Voltage drop detection
  - Pressure sensors (in sealed cells)
- **Vent System**: Pressure relief valves to safely vent gases
- **Fire Suppression**: Automatic fire suppression in battery compartment
- **Thermal Barriers**: Fire-resistant materials between modules

### 5.3 Mechanical Safety

- **Crash Protection**: Reinforced enclosure per [UN ECE R100](https://unece.org/transport/vehicle-regulations-wp29/standards/addenda-1958-agreement-regulations-101-120)
- **Vibration Isolation**: Rubber or elastomeric mounts
- **Penetration Protection**: Reinforced bottom plate (for ground strikes)

### 5.4 Software Safety

- **Functional Safety**: [ISO 26262](https://www.iso.org/standard/68383.html) ASIL-C or ASIL-D
- **Fault Detection**: Comprehensive fault diagnostics
- **Safe State**: Defined actions on fault detection (e.g., open contactors)
- **Redundancy**: Dual-channel critical measurements

---

## 6. Charging Specifications

### 6.1 Charging Modes

#### Mode 1: Slow Charging (AC Level 1)

- **Power**: 3-7 kW (single-phase 230V, 16A)
- **Charging Time**: 10-16 hours (for 80-150 kWh pack)
- **Use Case**: Overnight charging, depot charging

#### Mode 2: Fast Charging (AC Level 2)

- **Power**: 7-22 kW (single-phase or three-phase)
- **Charging Time**: 4-8 hours (for 80-150 kWh pack)
- **Use Case**: Daytime charging, opportunity charging

#### Mode 3: DC Fast Charging (DCFC)

- **Power**: 50-150 kW
- **Charging Time**: 1-2 hours (to 80%)
- **Use Case**: Rapid turnaround, high-utilization vehicles
- **Standard**: CCS (Combined Charging System) or CHAdeMO

### 6.2 Charging Profile

- **Phase 1**: Constant Current (CC) at maximum safe current
- **Phase 2**: Constant Voltage (CV) at maximum cell voltage (3.65V for LFP, 4.2V for NMC)
- **Termination**: Current tapers to <C/20
- **Temperature Limits**: No charging below 0°C or above 45°C (without pre-conditioning)

### 6.3 Smart Charging Features

- **V2G Communication**: [ISO 15118](https://www.iso.org/standard/55366.html) for bidirectional communication
- **Load Management**: Coordinate charging to avoid grid overload
- **Time-of-Use (TOU) Optimization**: Charge during off-peak hours
- **State-Based Charging**: Adjust charge rate based on SOC, temperature, and grid conditions

---

## 7. Performance Specifications

### 7.1 Energy and Power Metrics

| Metric | LFP Chemistry | NMC Chemistry |
|--------|---------------|---------------|
| Specific Energy (Wh/kg) | 120-160 | 200-260 |
| Energy Density (Wh/L) | 250-350 | 500-700 |
| Specific Power (W/kg) | 300-500 | 800-1,200 |
| Cycle Life (80% DoD) | 3,000-6,000 | 1,500-3,000 |
| Calendar Life (years) | 10-15 | 8-12 |
| Operating Temp (°C) | -30 to +60 | -20 to +55 |
| Self-Discharge (%/month) | <3 | <5 |

### 7.2 Depth of Discharge (DoD) Strategy

- **Normal Operations**: 20-80% SOC (60% usable capacity)
  - Extends cycle life significantly
  - Provides buffer for regenerative braking
- **Emergency Use**: 10-90% SOC (80% usable capacity)
- **Storage**: 50% SOC (optimal for long-term storage)

---

## 8. Standards and Compliance

### 8.1 Battery Safety Standards

- [UN 38.3](https://unece.org/transportdangerous-goods/un-manual-tests-and-criteria-rev6-2015) – Lithium battery transportation testing
- [UL 2580](https://www.ul.com/resources/ul-2580-standard-safety) – Batteries for use in electric vehicles
- [IEC 62619](https://webstore.iec.ch/publication/7299) – Safety of secondary lithium cells and batteries for industrial applications
- [SAE J2929](https://www.sae.org/standards/content/j2929_201104/) – Safety standard for electric and hybrid vehicle propulsion battery systems

### 8.2 Functional Safety

- [ISO 26262](https://www.iso.org/standard/68383.html) – Road vehicles - Functional safety (ASIL-C or ASIL-D for BMS)

### 8.3 Environmental Standards

- [IEC 60068-2-6](https://webstore.iec.ch/publication/522) – Environmental testing (vibration)
- [IEC 60068-2-27](https://webstore.iec.ch/publication/534) – Environmental testing (shock)
- [ISO 12405-4](https://www.iso.org/standard/66451.html) – Electrically propelled road vehicles - Durability testing

---

## 9. Lifecycle Management

### 9.1 Battery Health Monitoring

- **SOH Tracking**: Capacity and resistance measurements
- **Predictive Maintenance**: Alert when SOH <80%
- **Data Logging**: Cloud-based battery analytics
- **Integration**: Link to [85-70-06-002_Battery_Health_Monitoring.md](../../85-70-06_Maintenance_and_Diagnostics/85-70-06-002_Battery_Health_Monitoring.md)

### 9.2 Second-Life Applications

- **Repurposing Criteria**: Batteries with SOH >70% suitable for stationary energy storage
- **Applications**: 
  - Airport energy storage (peak shaving)
  - Renewable energy integration
  - UPS (Uninterruptible Power Supply) systems
- **Testing and Certification**: Re-certify for second-life use

### 9.3 End-of-Life Recycling

- **Recycling Rate Target**: >95% of materials
- **Recycling Processes**:
  - Pyrometallurgy (high-temperature smelting)
  - Hydrometallurgy (chemical leaching)
  - Direct recycling (cathode restoration)
- **Circular Economy**: Integration with [85-30_Circularity](../../../85-30_Circularity/)

---

## 10. Cross-References

### 10.1 Internal (ATA 85)

- [85-70-01-005_Power_Electronics.md](../85-70-01-005_Power_Electronics.md) – BMS and power electronics
- [85-70-01-A-004_Charging_Integration.md](./85-70-01-A-004_Charging_Integration.md) – Charging system integration
- [85-70-04](../../85-70-04_Charging_Infrastructure/) – Charging infrastructure
- [85-70-06-002_Battery_Health_Monitoring.md](../../85-70-06_Maintenance_and_Diagnostics/85-70-06-002_Battery_Health_Monitoring.md) – Battery diagnostics
- [85-30_Circularity](../../../85-30_Circularity/) – Lifecycle and recycling

### 10.2 External (Other ATAs)

- [ATA 95 – Digital Product Passport](../../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/) – Battery traceability

---

## 11. Status and Next Steps

- **Current Phase**: Design specifications
- **Next Phase**: Supplier selection and testing
- **Dependencies**: GSE vehicle platforms, charging infrastructure deployment

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22.

---

**End of Document**
