---
Title: "GSE Subsystem Interfaces — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-13-01-03A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Interface definitions and specifications for Ground Support Equipment (GSE) subsystems interfacing with the AMPEL360 BWB H₂ Hy-E aircraft and ground infrastructure."
Keywords: ["ATA 03","GSE","Interfaces","Ground Support","Aircraft Interface","ICD"]
Compliance:
  - "ATA iSpec 2200"
  - "S1000D"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  Parent: "../"
  Siblings:
    - "03-00-13-01-01A_GSE_Subsystem_Overview.md"
    - "03-00-13-01-02A_GSE_Subsystem_Hierarchy.md"
    - "03-00-13-01-04A_GSE_Subsystem_Integration.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial GSE subsystem interfaces" }
---

# GSE Subsystem Interfaces — ATA 03 Support Information GSE

## 1. Purpose

This document defines the **interface specifications** for Ground Support Equipment (GSE) subsystems used with the AMPEL360 BWB H₂ Hy-E aircraft. It establishes physical, electrical, data, and procedural interfaces between GSE equipment, the aircraft, and ground infrastructure to ensure safe, efficient, and interoperable ground operations.

## 2. Scope

This document covers:

- Physical interfaces (mechanical connections, dimensions, tolerances)
- Electrical interfaces (power, grounding, signals)
- Fluid/gas interfaces (hydrogen, air, water, waste)
- Data/communication interfaces (digital protocols, data exchange)
- Procedural interfaces (operating sequences, safety interlocks)
- Environmental interfaces (temperature, pressure, safety zones)

## 3. Applicable Documents

### 3.1 Standards

| Standard | Application | Link |
|----------|-------------|------|
| **[ATA iSpec 2200](https://www.ata.org/resources/specifications)** | Technical documentation standards | Chapter 03 |
| **[SAE AS6968](https://www.sae.org/standards/content/as6968/)** | Hydrogen Aircraft Refueling | Interface requirements |
| **[MIL-STD-461](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35789)** | EMI/EMC Requirements | Electromagnetic compatibility |
| **[ISO 19880-8](https://www.iso.org/standard/71940.html)** | Gaseous Hydrogen Fueling | Interface protocols |
| **[SAE ARP5707](https://www.sae.org/standards/content/arp5707/)** | Aircraft Ground Support | Interface specifications |

### 3.2 Related Documents

- [03-00-13-01-01A_GSE_Subsystem_Overview.md](./03-00-13-01-01A_GSE_Subsystem_Overview.md)
- [03-00-13-01-02A_GSE_Subsystem_Hierarchy.md](./03-00-13-01-02A_GSE_Subsystem_Hierarchy.md)
- [03-00-05_Interfaces](../../03-00-05_Interfaces/) — Master interface control documents

## 4. Interface Categories

### 4.1 Interface Classification

| Interface Type | Code | Description | Example |
|----------------|------|-------------|---------|
| **Physical** | PHY | Mechanical connections, mounting | H₂ coupling interface |
| **Electrical** | ELE | Power, grounding, signals | GPU power connector |
| **Fluid/Gas** | FLU | Liquid, gas transfer | LH₂ transfer interface |
| **Data** | DAT | Digital communication, data exchange | Ethernet, CAN bus |
| **Environmental** | ENV | Safety zones, exclusion areas | H₂ hazard zone |
| **Procedural** | PRO | Operational sequences, interlocks | Refueling procedure steps |

## 5. Physical Interfaces

### 5.1 Hydrogen Refueling Interface

#### 5.1.1 LH₂ Quick-Connect Coupling

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| **Type** | Self-sealing quick-disconnect | SAE AS6968 |
| **Nominal Size** | DN 50 (2 inches) | ISO 6708 |
| **Material** | Stainless steel 316L | ASTM A240 |
| **Temperature Range** | -253°C to +50°C | Cryogenic rated |
| **Pressure Rating** | 10 bar (145 psi) | Working pressure |
| **Leak Rate** | < 1×10⁻⁶ mbar·L/s | Helium leak test |
| **Connection Force** | < 50 N (manual) | Ergonomic requirement |
| **Disconnection Force** | < 30 N (manual) | Ergonomic requirement |
| **Safety Features** | Dead-man switch, pressure relief | Built-in protection |

#### 5.1.2 Aircraft Receptacle Location

| Aircraft Station | Location | Access | Notes |
|------------------|----------|--------|-------|
| **Main H₂ Port 1** | Fwd fuselage, port side, Station 350 | Ground level | Primary refueling |
| **Main H₂ Port 2** | Aft fuselage, starboard side, Station 1250 | Ground level | Backup/simultaneous |
| **Emergency Vent** | Top fuselage, centerline, Station 800 | Roof access | Emergency defuel only |

### 5.2 Electrical Power Interface

#### 5.2.1 Ground Power Unit (GPU) Interface

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| **AC Power** | 115VAC, 3-phase, 400Hz | SAE ARP5707 |
| **DC Power** | 28VDC | SAE ARP5707 |
| **Connector Type** | MS3509 (AC), SAE AS50881 (DC) | Mil-Spec |
| **Maximum Current** | 150A (AC), 300A (DC) | Peak demand |
| **Cable Length** | 15 meters maximum | Standard GPU cart |
| **Grounding** | Separate ground connection, < 0.1 Ω | Safety requirement |
| **Voltage Tolerance** | ±5% nominal | Aircraft limits |
| **Frequency Tolerance** | ±1 Hz (400Hz) | Generator stability |

#### 5.2.2 GPU Receptacle Location

| Aircraft Station | Location | Access | Purpose |
|------------------|----------|--------|---------|
| **Main GPU Port** | Nose landing gear bay, port side | Ground level | Primary AC/DC power |
| **APU GPU Port** | Aft fuselage, APU compartment | Via access panel | APU starting only |

### 5.3 Environmental Control Interface

#### 5.3.1 Pre-Conditioned Air (PCA) Interface

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| **Duct Diameter** | 150 mm (6 inches) | Standard |
| **Flow Rate** | 0.5 - 2.0 kg/s | Variable demand |
| **Temperature Range** | -10°C to +30°C | Cabin conditioning |
| **Pressure** | 1.2 bar (max) | Cabin pressure limit |
| **Connection Type** | Quick-connect flexible duct | Cam-lock |
| **Filtration** | HEPA filter, 99.97% @ 0.3 μm | Air quality |

## 6. Electrical Interfaces

### 6.1 Control and Monitoring Interfaces

#### 6.1.1 Industrial Ethernet Interface

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| **Protocol** | Ethernet/IP, PROFINET, Modbus TCP | Industrial standards |
| **Physical Layer** | 100BASE-TX / 1000BASE-T | IEEE 802.3 |
| **Connector** | RJ45, IP67-rated | Rugged industrial |
| **Cable** | Cat6 shielded, outdoor-rated | UV and weather resistant |
| **Topology** | Star or ring | Redundancy capable |
| **IP Address Scheme** | 192.168.100.x (GSE subnet) | Isolated network |

#### 6.1.2 CAN Bus Interface

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| **Protocol** | CAN 2.0B (29-bit identifier) | ISO 11898 |
| **Bit Rate** | 250 kbps (standard), 500 kbps (high-speed) | Configurable |
| **Physical Layer** | High-speed CAN | ISO 11898-2 |
| **Connector** | 9-pin D-sub | DE-9 |
| **Termination** | 120 Ω at each end | Required |
| **Cable** | Twisted pair, shielded | CAN-compatible |
| **Max Bus Length** | 40 meters @ 1 Mbps | Per ISO 11898 |

### 6.2 Safety Interlock Interfaces

#### 6.2.1 Emergency Stop (E-Stop) Circuit

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Type** | Hardwired safety relay | Category 3 per ISO 13849-1 |
| **Voltage** | 24VDC safety-rated | PELV circuit |
| **Contact Configuration** | Force-guided contacts, 2 N.O. + 2 N.C. | Redundant monitoring |
| **Response Time** | < 50 ms | From button press to system halt |
| **Reset Type** | Manual reset only | Prevent auto-restart |
| **Indicator** | Red LED, audible alarm | Visual and audible feedback |

#### 6.2.2 Interlock Signals

| Signal Name | Type | Function | Voltage Level |
|-------------|------|----------|---------------|
| **H2_CONNECTED** | Digital input | H₂ coupling connected | 24VDC |
| **H2_FLOW_PERMIT** | Digital output | Enable H₂ flow | 24VDC |
| **AIRCRAFT_READY** | Digital input | Aircraft systems ready | 24VDC |
| **GSE_READY** | Digital output | GSE systems ready | 24VDC |
| **EMERGENCY_STOP** | Digital input | E-Stop activated | 0VDC (active low) |
| **LEAK_DETECTED** | Digital input | H₂ leak alarm | 24VDC (active high) |

## 7. Fluid and Gas Interfaces

### 7.1 Hydrogen Transfer Interface

#### 7.1.1 Transfer Specifications

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| **Transfer Rate** | 500 kg/hour nominal, 750 kg/hour max | Design capacity |
| **Supply Pressure** | 3-5 bar absolute | Pressure differential |
| **Aircraft Tank Pressure** | 1-2 bar absolute | Receiving pressure |
| **LH₂ Temperature** | -253°C (20 K) | Saturated liquid |
| **Purity Requirement** | 99.95% minimum | Fuel grade hydrogen |
| **Moisture Content** | < 5 ppm | Prevent ice formation |
| **Particulate Limit** | < 1 μm (filtered) | Fuel cleanliness |

#### 7.1.2 Vent and Relief Interface

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Vent Line Size** | DN 100 (4 inches) | Boil-off capacity |
| **Relief Pressure** | 6 bar (set pressure) | Overpressure protection |
| **Vent Rate** | 10 kg/hour (normal), 500 kg/hour (emergency) | Variable |
| **Discharge Location** | Vertical vent stack, 5m above ground | Dispersion height |
| **Flame Arrestor** | Integrated in vent stack | Fire protection |

### 7.2 Potable Water Interface

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| **Connection Type** | Quick-connect cam-lock, 1-inch | Standard service |
| **Flow Rate** | 50 liters/minute | Fill time optimization |
| **Pressure** | 2-4 bar | Service cart pressure |
| **Water Quality** | Potable water per WHO guidelines | Safe for consumption |
| **Hose Material** | Food-grade, FDA-approved | Safety |

## 8. Data and Communication Interfaces

### 8.1 Aircraft Data Interface

#### 8.1.1 Ground Data Link

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Physical Interface** | USB-C, Ethernet RJ45 | Dual option |
| **Protocol** | ARINC 615A (data loading), custom JSON/REST API | Software update and diagnostics |
| **Data Rate** | 100 Mbps minimum | Sufficient for logs and updates |
| **Security** | TLS 1.3, mutual authentication | Cybersecurity |
| **Location** | Avionics bay, access panel | Technician access |

### 8.2 GSE-to-GSE Communication

#### 8.2.1 Wireless Network

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| **Technology** | Wi-Fi 6 (802.11ax) or private LTE | Industrial-grade |
| **Frequency** | 5 GHz (Wi-Fi), licensed spectrum (LTE) | Reduced interference |
| **Range** | 100 meters minimum | Apron coverage |
| **Security** | WPA3-Enterprise / IPsec | Encrypted |
| **Latency** | < 50 ms | Real-time monitoring |

## 9. Environmental and Safety Interfaces

### 9.1 Hydrogen Hazard Zones

#### 9.1.1 Zone Definitions

| Zone | Radius | Description | Restrictions |
|------|--------|-------------|--------------|
| **Exclusion Zone** | 10 m from H₂ connections | No ignition sources, personnel with PPE only | Strictly enforced |
| **Restricted Zone** | 25 m from H₂ connections | Limited personnel, no vehicles | Controlled access |
| **Monitored Zone** | 50 m from H₂ connections | H₂ detectors, fire suppression available | Continuous monitoring |

### 9.2 Safety Equipment Interface

#### 9.2.1 Fire Suppression System

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Detection Type** | UV/IR flame detectors, H₂ concentration sensors | Multi-mode detection |
| **Suppression Agent** | Water mist, inert gas (N₂, CO₂) | H₂-compatible |
| **Activation Time** | < 5 seconds from detection | Automatic |
| **Coverage Area** | Entire refueling zone | 360° protection |
| **Manual Override** | Available from GSE control panel | Operator control |

## 10. Procedural Interfaces

### 10.1 Refueling Sequence Interlocks

#### 10.1.1 Pre-Refueling Checks

| Step | Interlock Condition | Status Signal |
|------|---------------------|---------------|
| 1. Aircraft parked and chocked | Weight-on-wheels sensor | AIRCRAFT_PARKED |
| 2. Engines off | Engine RPM = 0 | ENGINES_OFF |
| 3. APU off | APU RPM = 0 | APU_OFF |
| 4. Electrical bonding connected | Ground verified < 0.1 Ω | BONDING_OK |
| 5. Fire suppression armed | System status = READY | FIRE_SUPP_READY |
| 6. Personnel clear of exclusion zone | Zone sensors clear | ZONE_CLEAR |
| 7. GSE H₂ coupling connected | Coupling sensor = ENGAGED | H2_CONNECTED |

#### 10.1.2 Refueling Permit Logic

```
REFUELING_PERMIT = AIRCRAFT_PARKED AND 
                   ENGINES_OFF AND 
                   APU_OFF AND 
                   BONDING_OK AND 
                   FIRE_SUPP_READY AND 
                   ZONE_CLEAR AND 
                   H2_CONNECTED AND 
                   NOT EMERGENCY_STOP
```

Only when `REFUELING_PERMIT = TRUE` can hydrogen flow be enabled.

## 11. Cross-References

### 11.1 Related ATA Chapters

- [ATA 02 — Operations Information](../../../../../ATA_02-OPERATIONS_INFORMATION/) — Ground operations procedures
- [ATA 85 — Infrastructure Interface Standards](../../../../../ATA_85-INFRASTRUCTURE_INTERFACE_STANDARDS/) — Airport infrastructure interfaces

### 11.2 Related Documents

- [03-00-05_Interfaces](../../03-00-05_Interfaces/) — Master interface control documents
- [03-00-13-01-01A_GSE_Subsystem_Overview.md](./03-00-13-01-01A_GSE_Subsystem_Overview.md)
- [03-00-13-02_H2_GSE_Subsystems](../03-00-13-02_H2_GSE_Subsystems/) — Hydrogen GSE detailed specifications

### 11.3 Parent Document

- [03-00-13_Subsystems_Components](../) — Top-level subsystems directory

## 12. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-13-01-03A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 Ground Support Equipment WG

---
