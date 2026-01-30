# 85-00-13-004: Interface Hardware Catalog

## Document Information

- **Document ID**: 85-00-13-004
- **Title**: Interface Hardware Catalog
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-21

---

## 1. Introduction

This document provides a **comprehensive catalog of physical interface hardware** used in ATA 85 Infrastructure Interface Standards. It serves as the reference for all connectors, receptacles, couplers, manifolds, sensors, and other hardware components at the aircraft-ground interface boundary.

### 1.1 Purpose

The Interface Hardware Catalog:

- Documents all **standard interface hardware** used across ATA 85 subsystems
- Defines **specifications and ratings** for each hardware type
- Establishes **interoperability requirements** between aircraft and ground systems
- Supports **procurement** and **supply chain management**
- Enables **standardization** across fleet and airport facilities

### 1.2 Scope

This catalog covers:

- H₂ and CO₂ fuel/energy interface hardware
- Electrical power connectors and receptacles
- Data and communication interface hardware
- Fluid and pneumatic connectors
- Passenger boarding interface hardware
- Safety and monitoring devices

---

## 2. H₂ Infrastructure Interface Hardware

### 2.1 H₂ Fueling Connectors

#### 2.1.1 High-Pressure H₂ Receptacle

**Part Number**: `85-RCPT-H2F-001-A`

| Specification | Value |
|---------------|-------|
| **Type** | SAE AS50881-compliant H₂ receptacle |
| **Pressure Rating** | 700 bar (10,150 psi) max |
| **Temperature Range** | -40°C to +85°C |
| **Flow Rate** | Up to 10 kg/min H₂ |
| **Material** | Stainless steel 316L body, PTFE seals |
| **Sealing** | Metal-to-metal primary seal, elastomer backup |
| **Safety Features** | Integrated pressure relief, breakaway coupling |
| **Leak Rate** | < 1 × 10⁻⁶ mbar·L/s |
| **Coupling Mechanism** | Quarter-turn bayonet with safety lock |
| **Mating Connector** | 85-CONN-H2F-001-A (ground-side) |
| **Certification** | EASA CS-25, SAE AS50881, ISO 19881 |
| **Weight** | 2.45 kg |
| **Dimensions** | 150 mm × 100 mm × 80 mm |

**Interfaces**:
- H₂ fuel system (ATA 28)
- Safety monitoring system (leak detection, fire suppression)
- Grounding system for static discharge

#### 2.1.2 H₂ Vent Coupling

**Part Number**: `85-CONN-H2V-001-A`

| Specification | Value |
|---------------|-------|
| **Type** | Low-pressure H₂ vent coupling |
| **Pressure Rating** | 10 bar (145 psi) max |
| **Temperature Range** | -40°C to +85°C |
| **Flow Rate** | Up to 50 L/min H₂ vapor |
| **Material** | Aluminum alloy 6061-T6, Viton seals |
| **Sealing** | Cam-lock with captive seal |
| **Safety Features** | Flame arrestor, static bonding |
| **Coupling Mechanism** | Cam-lock quick-disconnect |
| **Certification** | EASA CS-25, SAE ARP5433 |

### 2.2 H₂ Safety Interface Hardware

#### 2.2.1 H₂ Leak Detection Sensor

**Part Number**: `85-SENS-H2S-010`

| Specification | Value |
|---------------|-------|
| **Type** | Electrochemical H₂ sensor |
| **Detection Range** | 0-4% H₂ by volume |
| **Response Time** | < 2 seconds to 50% LEL |
| **Accuracy** | ±5% of reading |
| **Output** | 4-20 mA analog + CAN-FD digital |
| **Power** | 12-28V DC, < 500 mA |
| **Environmental** | IP67, -40°C to +85°C |
| **Certification** | ATEX Zone 1, IECEx, EASA CS-25.1309 |

---

## 3. CO₂ Battery Interface Hardware

### 3.1 CO₂ Battery Charging Connectors

#### 3.1.1 High-Power DC Charging Receptacle

**Part Number**: `85-RCPT-CO2-001-A`

| Specification | Value |
|---------------|-------|
| **Type** | High-power DC fast charging inlet |
| **Voltage Rating** | 800V DC nominal (400-900V range) |
| **Current Rating** | 500A continuous, 600A peak (30 min) |
| **Power Rating** | 400 kW max |
| **Connector Standard** | CCS (Combined Charging System) Type 2 |
| **Temperature Range** | -40°C to +50°C |
| **Cooling** | Liquid-cooled (integrated cooling channels) |
| **Material** | Copper alloy contacts, thermoplastic housing |
| **Safety Features** | Pre-charge circuit, isolation monitoring, temperature sensors |
| **Communication** | CAN-FD (charging control protocol) |
| **Mating Connector** | CCS Type 2 charging plug |
| **Certification** | IEC 62196-3, SAE J1772, EASA CS-25 |

#### 3.1.2 CO₂ Battery Thermal Interface

**Part Number**: `85-CONN-CO2T-001-A`

| Specification | Value |
|---------------|-------|
| **Type** | Thermal management quick-disconnect |
| **Fluid** | Water-glycol coolant (50/50 mix) |
| **Pressure Rating** | 5 bar (73 psi) |
| **Flow Rate** | 50-200 L/min variable |
| **Temperature Range** | -20°C to +80°C |
| **Material** | Stainless steel, EPDM seals |
| **Coupling** | Flat-face quick-disconnect (no-spill) |
| **Certification** | SAE J2044, ISO 9001 |

---

## 4. Airport Infrastructure Interface Hardware

### 4.1 Ground Power Connectors

#### 4.1.1 400Hz AC Ground Power Receptacle

**Part Number**: `85-RCPT-APT-001-A`

| Specification | Value |
|---------------|-------|
| **Type** | 400Hz aircraft ground power receptacle |
| **Voltage** | 115/200V AC, 3-phase, 400Hz |
| **Current Rating** | 400A continuous |
| **Power Rating** | 138 kVA |
| **Connector Standard** | MIL-DTL-38999 Series III |
| **Contact Arrangement** | 4-pin (3 phase + neutral) + ground shell |
| **Temperature Range** | -55°C to +125°C |
| **Material** | Aluminum alloy, silver-plated copper contacts |
| **Safety Features** | Ground-first/break-last design, arc suppression |
| **Mating Connector** | MIL-DTL-38999 plug |
| **Certification** | EASA CS-25, MIL-DTL-38999 |

#### 4.1.2 28V DC Ground Power Receptacle

**Part Number**: `85-RCPT-APT-002-A`

| Specification | Value |
|---------------|-------|
| **Type** | 28V DC ground power inlet |
| **Voltage** | 28V DC nominal (18-32V range) |
| **Current Rating** | 600A continuous |
| **Power Rating** | 16.8 kW |
| **Connector Standard** | AS50181 DC power connector |
| **Contact Arrangement** | 2-pin (+ / -) + ground shell |
| **Temperature Range** | -55°C to +125°C |
| **Material** | Aluminum alloy housing, copper contacts |
| **Safety Features** | Reverse polarity protection, overcurrent disconnect |
| **Certification** | SAE AS50181, EASA CS-25 |

### 4.2 Airport Data Interface Hardware

#### 4.2.1 Ethernet Data Receptacle

**Part Number**: `85-RCPT-APT-010-A`

| Specification | Value |
|---------------|-------|
| **Type** | Ruggedized Ethernet receptacle |
| **Data Rate** | 10 Gbps (10GBASE-T) |
| **Connector Standard** | RJ45 (8P8C) with EMI shielding |
| **Cable Type** | Cat 6A or Cat 7 |
| **Temperature Range** | -40°C to +85°C |
| **Environmental** | IP67 sealed (when mated) |
| **Material** | Die-cast zinc alloy, gold-plated contacts |
| **Safety Features** | ESD protection, EMI filtering |
| **Certification** | IEC 60512, ARINC 664 Part 7 |

#### 4.2.2 Fiber Optic Data Receptacle

**Part Number**: `85-RCPT-APT-011-A`

| Specification | Value |
|---------------|-------|
| **Type** | Multi-mode fiber optic receptacle |
| **Connector Standard** | LC duplex (ARINC 801) |
| **Fiber Type** | OM4 multi-mode (50/125 µm) |
| **Data Rate** | Up to 100 Gbps |
| **Wavelength** | 850 nm (short-range) |
| **Temperature Range** | -40°C to +85°C |
| **Environmental** | IP67 sealed with protective cap |
| **Insertion Loss** | < 0.5 dB |
| **Certification** | ARINC 801, IEC 61754-20 |

---

## 5. Ground Services Equipment (GSE) Interface Hardware

### 5.1 GSE Power Interface

#### 5.1.1 GSE External Power Receptacle

**Part Number**: `85-RCPT-GSE-001-A`

| Specification | Value |
|---------------|-------|
| **Type** | Mobile GPU power inlet |
| **Voltage** | 115/200V AC, 400Hz or 28V DC selectable |
| **Current Rating** | 200A (AC) or 400A (DC) |
| **Connector Standard** | SAE AS50001 universal power connector |
| **Temperature Range** | -40°C to +70°C |
| **Safety Features** | Interlocked cover, voltage detection |
| **Certification** | SAE AS50001, EASA CS-25 |

### 5.2 GSE Data Interface

#### 5.2.1 Maintenance Data Port

**Part Number**: `85-CONN-GSE-010-A`

| Specification | Value |
|---------------|-------|
| **Type** | Aircraft maintenance data port |
| **Data Protocol** | CAN-FD, Ethernet (switchable) |
| **Connector Standard** | D-sub 9-pin (CAN) or RJ45 (Ethernet) |
| **Data Rate** | CAN-FD: 5 Mbps; Ethernet: 1 Gbps |
| **Temperature Range** | -40°C to +85°C |
| **Environmental** | IP54 (dustproof, splash-resistant) |
| **Certification** | ARINC 825 (CAN), ARINC 664 (Ethernet) |

---

## 6. Passenger Boarding/Evacuation Interface Hardware

### 6.1 Boarding Bridge Interface

#### 6.1.1 Bridge Docking Adapter

**Part Number**: `85-CONN-PAX-001-A`

| Specification | Value |
|---------------|-------|
| **Type** | Passenger boarding bridge docking adapter |
| **Interface** | Aircraft door frame to bridge |
| **Material** | Aluminum alloy frame, rubber seal |
| **Sealing** | Inflatable environmental seal (pressure: 0.5 bar) |
| **Load Capacity** | 500 kg distributed load |
| **Temperature Range** | -40°C to +50°C |
| **Safety Features** | Proximity sensors, alignment guides, interlock |
| **Certification** | ISO 16029 (Passenger Boarding Bridges) |

### 6.2 Emergency Evacuation Interface

#### 6.2.1 Evacuation Slide Interface

**Part Number**: `85-CONN-PAX-010-A`

| Specification | Value |
|---------------|-------|
| **Type** | Emergency slide deployment interface |
| **Function** | Automatic slide deployment trigger |
| **Actuation** | Pneumatic (door opening) or manual override |
| **Response Time** | < 6 seconds (per CS-25.810) |
| **Environmental** | Sealed, corrosion-resistant |
| **Certification** | EASA CS-25.810, CS-25.812 |

---

## 7. Safety and Monitoring Interface Hardware

### 7.1 Fire Detection Interface

#### 7.1.1 Fire/Smoke Detector Port

**Part Number**: `85-SENS-SFTY-001`

| Specification | Value |
|---------------|-------|
| **Type** | Optical smoke and heat detector |
| **Detection Method** | Dual-spectrum optical + thermal |
| **Response Time** | < 30 seconds (smoke), < 10 seconds (heat) |
| **Output** | Discrete alarm + analog 4-20 mA |
| **Power** | 12-28V DC, < 100 mA |
| **Environmental** | IP65, -40°C to +85°C |
| **Certification** | EASA CS-25.858, CS-25.1309 |

### 7.2 Environmental Monitoring

#### 7.2.1 Temperature Sensor Interface

**Part Number**: `85-SENS-ENV-010`

| Specification | Value |
|---------------|-------|
| **Type** | RTD temperature sensor (PT1000) |
| **Range** | -55°C to +150°C |
| **Accuracy** | ±0.3°C |
| **Output** | 4-20 mA analog + RS-485 digital |
| **Response Time** | < 5 seconds (in air) |
| **Environmental** | IP67 |
| **Certification** | IEC 60751 Class A |

---

## 8. Material and Construction Standards

### 8.1 Material Selection

All interface hardware materials selected based on:

- **Corrosion resistance**: Marine/airport environment exposure
- **Temperature stability**: Wide operational range (-55°C to +150°C)
- **Electrical conductivity**: Low resistance for power contacts
- **Flammability**: FAR 25.853 (or equivalent) compliance
- **Recyclability**: High-grade materials for circularity (ATA 99)

### 8.2 Common Materials

| Material | Applications | Properties |
|----------|--------------|------------|
| Stainless Steel 316L | H₂ components, fluid connectors | Corrosion resistant, high strength |
| Aluminum Alloy 6061-T6 | Housings, brackets | Lightweight, corrosion resistant |
| Copper Alloy (C18000) | Electrical contacts | High conductivity, wear resistant |
| PTFE (Teflon) | H₂ seals, insulators | Chemical resistant, low friction |
| Viton (FKM) | Fuel/fluid seals | Temperature stable, fuel resistant |
| EPDM | Water/coolant seals | Weather resistant, flexible |

### 8.3 Surface Treatments

- **Anodizing**: Aluminum components (Type II or Type III)
- **Passivation**: Stainless steel (ASTM A967)
- **Electroplating**: Contacts (gold, silver, nickel per MIL-DTL-45204)
- **Powder coating**: Housings (polyester or epoxy)

---

## 9. Testing and Qualification

### 9.1 Environmental Testing

All interface hardware undergoes:

| Test | Standard | Criteria |
|------|----------|----------|
| Temperature cycling | MIL-STD-810, Method 503 | -55°C to +85°C, 10 cycles |
| Humidity | MIL-STD-810, Method 507 | 95% RH, 240 hours |
| Salt spray | ASTM B117 | 500 hours (no corrosion) |
| Vibration | RTCA DO-160, Section 8 | Aircraft operational profile |
| Shock | MIL-STD-810, Method 516 | 40g, 11 ms half-sine |
| EMI/EMC | RTCA DO-160, Section 20-21 | Category M (aircraft) |

### 9.2 Performance Testing

Specific to component type:

- **Electrical connectors**: Contact resistance, insulation resistance, dielectric withstand
- **Fluid connectors**: Proof pressure, burst pressure, leak test, flow test
- **Sensors**: Accuracy, repeatability, response time, drift
- **Safety devices**: Functional test, fault insertion, fail-safe verification

### 9.3 Lifecycle Testing

- **Durability**: 10,000 mating cycles (connectors)
- **Fatigue**: Per expected operational life
- **Wear**: Periodic inspection after extended use

---

## 10. Procurement and Supply Chain

### 10.1 Approved Suppliers

Qualified suppliers maintained in:

**Approved Vendor List (AVL)** – Configuration Management Database

Qualification criteria:
- AS9100 or ISO 9001 certification
- EASA Part 21 approval (where applicable)
- Quality history and performance metrics
- Supply chain transparency (for DPP compliance)

### 10.2 Bill of Materials (BOM) Links

Interface hardware BOMs available in:

- [ASSETS/BOMs/85-00-13-A-101_H2_Infrastructure_BOM.xlsx](./ASSETS/BOMs/)
- [ASSETS/BOMs/85-00-13-A-102_CO2_Battery_Infrastructure_BOM.xlsx](./ASSETS/BOMs/)
- [ASSETS/BOMs/85-00-13-A-103_Airport_Interface_BOM.xlsx](./ASSETS/BOMs/)
- [ASSETS/BOMs/85-00-13-A-104_GSE_Interface_BOM.xlsx](./ASSETS/BOMs/)
- [ASSETS/BOMs/85-00-13-A-105_Pax_Boarding_Evac_BOM.xlsx](./ASSETS/BOMs/)

---

## 11. Maintenance and Inspection

### 11.1 Inspection Intervals

| Component Type | Visual Inspection | Functional Test | Replacement Interval |
|----------------|-------------------|-----------------|----------------------|
| H₂ connectors | Every flight | Monthly | 5 years or 10,000 cycles |
| Power connectors | Weekly | Quarterly | 10 years or 20,000 cycles |
| Data connectors | Monthly | Semi-annually | 7 years or 15,000 cycles |
| Sensors | Monthly | Quarterly | 3-5 years (calibration-dependent) |

### 11.2 Inspection Criteria

- **Visual**: Corrosion, cracks, deformation, contamination
- **Functional**: Continuity, leak test, actuation force, signal integrity
- **Dimensional**: Wear measurements, thread inspection

### 11.3 Maintenance Actions

- **Cleaning**: Approved solvents per maintenance manual
- **Lubrication**: Specified lubricants (compatible with H₂, fuels, fluids)
- **Torque check**: Fasteners per installation specifications
- **Seal replacement**: At prescribed intervals or if damaged

---

## 12. Future Developments

### 12.1 Next-Generation Interfaces

- **Wireless power transfer**: Inductive charging for CO₂ batteries
- **Optical data links**: Free-space optical communication (10+ Gbps)
- **Smart connectors**: Embedded health monitoring, self-diagnostics
- **Modular interfaces**: Quick-change interface modules for flexibility

### 12.2 Standardization Initiatives

- Harmonization with SAE and ISO hydrogen fueling standards
- Participation in EASA/FAA rulemaking for infrastructure interfaces
- Collaboration with airport authorities on standard ground equipment

---

## 13. References

### 13.1 Internal References

- [85-00-13-001_Subsystems_Components_Overview.md](./85-00-13-001_Subsystems_Components_Overview.md)
- [85-00-13-003_Component_Taxonomy_and_Coding.md](./85-00-13-003_Component_Taxonomy_and_Coding.md)
- [85-00-13-005_Configurable_Packages_and_Kits.md](./85-00-13-005_Configurable_Packages_and_Kits.md)

### 13.2 External Standards

- **[SAE AS50881](https://www.sae.org/)** – Hydrogen fuel system components
- **[MIL-DTL-38999](https://quicksearch.dla.mil/)** – Electrical connectors
- **[RTCA DO-160](https://www.rtca.org/)** – Environmental conditions and test procedures for airborne equipment
- **[IEC 62196](https://www.iec.ch/)** – Plugs, socket-outlets, vehicle connectors and vehicle inlets for EV charging
- **[ISO 16029](https://www.iso.org/standard/55485.html)** – Passenger boarding bridges

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
