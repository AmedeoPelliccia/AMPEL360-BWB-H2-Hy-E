# 85-00-13-003: Component Taxonomy and Coding

## Document Information

- **Document ID**: 85-00-13-003
- **Title**: Component Taxonomy and Coding
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-21

---

## 1. Introduction

This document defines the **component taxonomy and coding system** for ATA 85 Infrastructure Interface Standards. It establishes consistent identification, classification, and tracking methods for all components within infrastructure interface subsystems.

### 1.1 Purpose

The component taxonomy serves to:

- Provide **unique identification** for every component
- Enable **lifecycle tracking** from manufacturing through disposal
- Support **configuration management** and change control
- Facilitate **supply chain management** and procurement
- Enable **digital product passport** (DPP) integration
- Support **maintenance** and **circularity** initiatives

### 1.2 Scope

This taxonomy covers:

- Physical hardware components (connectors, sensors, valves, receptacles)
- Embedded software/firmware components
- Interface cables and hoses
- Mounting hardware and brackets
- Safety and monitoring devices
- Configurable component kits and packages

---

## 2. Component Classification

### 2.1 Component Families

Components are organized into families based on function:

| Family Code | Family Name | Description | Examples |
|-------------|-------------|-------------|----------|
| CONN | Connectors | Electrical, fluid, data connectors | H₂ coupling, power plug, fiber optic |
| SENS | Sensors | Monitoring and measurement devices | Pressure, temperature, flow sensors |
| VALVE | Valves | Flow control and shutoff | H₂ shutoff valve, relief valve |
| RCPT | Receptacles | Fixed aircraft-side interfaces | Fueling receptacle, power inlet |
| CTRL | Controllers | Electronic control modules | Interface controller, safety interlock |
| CABL | Cables & Hoses | Flexible connections | Power cable, H₂ hose, data cable |
| MNTS | Mounting Hardware | Brackets, fasteners, supports | Receptacle bracket, cable clamps |
| SFTY | Safety Devices | Interlocks, fire suppression | Breakaway coupling, fire detector |
| SEAL | Seals & Gaskets | Fluid and environmental seals | O-ring, gasket, environmental seal |

### 2.2 Component Hierarchy

Components exist within a three-level hierarchy:

```
Subsystem (e.g., 85-H2-FUEL-001)
│
├── Assembly (e.g., H₂ Receptacle Assembly)
│   │
│   ├── Component (e.g., H₂ Coupling Body)
│   ├── Component (e.g., Seal Kit)
│   └── Component (e.g., Safety Sensor)
│
└── Assembly (e.g., H₂ Control Panel)
    │
    ├── Component (e.g., Controller Module)
    ├── Component (e.g., Display Unit)
    └── Component (e.g., Wiring Harness)
```

---

## 3. Component Identification System

### 3.1 Component Part Number Format

Each component has a unique part number following this pattern:

```
85-<FAMILY>-<SUBSYSTEM>-<SEQUENCE>-<VARIANT>
```

Where:
- **85** = ATA chapter
- **FAMILY** = Component family code (4 letters, see Section 2.1)
- **SUBSYSTEM** = Parent subsystem abbreviation (2-4 letters)
- **SEQUENCE** = Three-digit sequence number (001-999)
- **VARIANT** = Optional variant letter (A, B, C...) for similar components

**Examples**:
- `85-RCPT-H2F-001-A` – H₂ Fueling Receptacle, variant A
- `85-SENS-H2F-010` – H₂ Fueling Pressure Sensor
- `85-CONN-APT-005-B` – Airport Power Connector, variant B
- `85-CTRL-CO2-020` – CO₂ Battery Interface Controller

### 3.2 Serial Number System

Individual component instances (not types) are tracked with serial numbers:

```
<PART_NUMBER>-SN-<YEAR><MONTH><BATCH>-<SEQUENCE>
```

**Example**:
- `85-RCPT-H2F-001-A-SN-202511-001-00042`
  - Part number: 85-RCPT-H2F-001-A
  - Year: 2025
  - Month: 11
  - Batch: 001
  - Unit: 00042

Serial numbers enable:
- Individual component tracking throughout lifecycle
- Traceability to manufacturing batch and supplier
- Maintenance history recording
- Warranty and recall management

### 3.3 Digital Product Passport (DPP) ID

Each component serial number maps to a DPP ID following ATA 95 conventions:

```
DPP-85-<SERIAL_NUMBER>
```

**Example**:
- `DPP-85-RCPT-H2F-001-A-SN-202511-001-00042`

The DPP ID links to comprehensive lifecycle data (see [85-00-13-007_DPP_and_Digital_Twin_Links.md](./85-00-13-007_DPP_and_Digital_Twin_Links.md)).

---

## 4. Component Attributes

### 4.1 Master Component Record

Each component type is documented in:

**[MASTER/85-00-13-M-002_Master_Component_List.csv](./MASTER/85-00-13-M-002_Master_Component_List.csv)**

With the following attributes:

| Attribute | Description | Example |
|-----------|-------------|---------|
| Part_Number | Unique component identifier | 85-RCPT-H2F-001-A |
| Component_Name | Descriptive name | H₂ Fueling Receptacle Assembly |
| Family | Component family code | RCPT |
| Subsystem_ID | Parent subsystem | 85-H2-FUEL-001 |
| Description | Technical description | High-pressure H₂ receptacle with integrated safety interlock |
| Manufacturer | Supplier/manufacturer name | AeroConnect Systems |
| Manufacturer_PN | Manufacturer's part number | AC-H2R-350-001 |
| Material | Primary material(s) | Stainless steel 316L, PTFE seals |
| Weight | Component weight (kg) | 2.45 |
| Dimensions | Key dimensions (mm) | 150 x 100 x 80 |
| Interface_Type | Interface standard | SAE AS50881 H₂ Coupling |
| Lifecycle_Status | Current status | Active, Prototype, Obsolete |
| Criticality | Safety/mission criticality | Critical, Important, Standard |
| MTBF | Mean time between failures | 50,000 cycles |
| Price | Unit cost (EUR) | 1,250.00 |
| Lead_Time | Procurement lead time (days) | 90 |
| DPP_Required | DPP tracking required | Yes/No |
| Circular_Rating | Recyclability rating | A (High), B (Medium), C (Low) |

### 4.2 Interface Specifications

For interface components (connectors, receptacles), additional attributes:

| Attribute | Description | Example |
|-----------|-------------|---------|
| Electrical_Rating | Voltage, current, frequency | 28V DC, 200A continuous |
| Fluid_Rating | Pressure, temperature, flow | 700 bar, -40°C to +85°C |
| Data_Protocol | Communication standard | Ethernet 10GBASE-T, CAN-FD |
| Mating_Connector | Compatible mating component | 85-CONN-H2F-001-A |
| Sealing_Rating | Environmental protection | IP67, SAE AS50881 |

---

## 5. Component Labeling and Marking

### 5.1 Physical Labels

All components must have durable labels with:

- **Component part number** (as defined in Section 3.1)
- **Serial number** (for serialized components)
- **QR code** or **NFC tag** linking to DPP entry
- **Manufacturer name and logo**
- **Date of manufacture** (YYYY-MM)
- **Safety markings** (if applicable)

### 5.2 Label Placement

- Labels positioned on visible, accessible surfaces
- Labels must survive expected environmental conditions
- Backup labels on hidden surfaces for critical components
- Labels compatible with MRO inspection processes

### 5.3 Digital Marking

In addition to physical labels:

- **QR codes** encode: `https://dpp.ampel360.eu/<DPP_ID>`
- **NFC tags** (ISO 15693) contain: Part number, serial number, DPP link
- **RFID tags** (optional) for automated inventory tracking

---

## 6. Component Kits and Packages

### 6.1 Configurable Units

Components may be grouped into **configurable kits** for:

- Standard airport interface packages (e.g., "H₂ Gate Kit")
- Aircraft variant-specific configurations
- Service and maintenance kits
- Spare parts packages

### 6.2 Kit Numbering

Kits follow a similar pattern:

```
85-KIT-<DOMAIN>-<PURPOSE>-<SEQUENCE>
```

**Examples**:
- `85-KIT-H2-FUEL-001` – Standard H₂ Fueling Kit
- `85-KIT-APT-PWR-002` – Premium Airport Power Kit
- `85-KIT-GSE-SERV-010` – GSE Service Kit

### 6.3 Kit BOMs

Each kit has a Bill of Materials (BOM) listing:
- Component part numbers and quantities
- Assembly instructions reference
- Special tools or equipment required
- Installation time estimate

See [85-00-13-005_Configurable_Packages_and_Kits.md](./85-00-13-005_Configurable_Packages_and_Kits.md) for details.

---

## 7. Relationship to Standards

### 7.1 ATA iSpec 2200

Component identification follows ATA iSpec 2200 guidelines for:
- Part number structure
- Illustrated parts catalogs (IPC)
- Maintenance manual references

### 7.2 SAE Standards

Compliance with relevant SAE standards:
- **SAE AS50881** – H₂ connectors and couplings
- **SAE AS5498** – Prognostic health management
- **SAE ARP4761** – Safety assessment (for critical components)

### 7.3 ISO Standards

Alignment with ISO standards:
- **ISO 15926** – Data integration for process plants
- **ISO 29002-20** – Exchange of characteristic data (for DPP)
- **ISO 81346** – Structuring principles and reference designations

---

## 8. Lifecycle Tracking

### 8.1 Manufacturing to Installation

Component lifecycle stages:

| Stage | Data Captured | System |
|-------|---------------|--------|
| Manufacturing | Batch, date, supplier, test results | ERP, MES |
| Incoming Inspection | QC results, acceptance | QMS |
| Warehouse | Location, lot tracking | WMS |
| Installation | Aircraft serial number, location, installer | MRO system |
| As-Built | Actual configuration, torque values | Digital twin |

### 8.2 In-Service Tracking

During operational life:

| Event | Data Captured | System |
|-------|---------------|--------|
| Inspection | Condition, findings, inspector | MRO system |
| Maintenance | Actions, parts replaced, hours | CMMS |
| Failure | Failure mode, root cause, corrective action | Reliability database |
| Modification | Design change, retrofit kit, approval | Configuration management |

### 8.3 End-of-Life

At component removal or aircraft retirement:

| Action | Data Captured | System |
|--------|---------------|--------|
| Removal | Reason, condition, next destination | MRO system |
| Testing | Functionality, residual life | Test facility |
| Disposition | Recycle, refurbish, scrap | Asset management |
| Material Recovery | Material type, quantity, purity | Circularity system (ATA 99) |

---

## 9. Integration with DPP and Digital Twin

### 9.1 DPP Data Model

Each component's DPP includes:

- **Identity**: Part number, serial number, manufacturer
- **Provenance**: Manufacturing location, date, batch, supplier chain
- **Composition**: Materials, hazardous substances, recyclability
- **Performance**: Design specs, test data, certification
- **History**: Installation, maintenance, failures, modifications
- **Circularity**: Recycling instructions, material recovery potential

### 9.2 Digital Twin Integration

Component data feeds digital twin models:

- **Geometric model**: CAD representation, position in aircraft
- **Functional model**: Performance parameters, operational limits
- **Simulation model**: Stress, thermal, fluid flow analysis
- **Predictive model**: Remaining useful life, failure probability

See [85-00-13-007_DPP_and_Digital_Twin_Links.md](./85-00-13-007_DPP_and_Digital_Twin_Links.md) for integration details.

---

## 10. Governance and Maintenance

### 10.1 Change Control

Changes to component taxonomy or coding system require:

1. Engineering change proposal (ECP)
2. Impact assessment (existing components, systems, documentation)
3. Configuration Control Board (CCB) approval
4. Updated documentation and training
5. Migration plan for existing components

### 10.2 Master Data Stewardship

- **Data Owner**: Configuration Management Team
- **Review Frequency**: Quarterly
- **Audit Frequency**: Annual
- **Quality Metrics**: Data completeness, accuracy, consistency

---

## 11. References

### 11.1 Internal References

- [85-00-13-001_Subsystems_Components_Overview.md](./85-00-13-001_Subsystems_Components_Overview.md)
- [85-00-13-002_Subsystem_Master_Register.md](./85-00-13-002_Subsystem_Master_Register.md)
- [85-00-13-004_Interface_Hardware_Catalog.md](./85-00-13-004_Interface_Hardware_Catalog.md)
- [85-00-13-007_DPP_and_Digital_Twin_Links.md](./85-00-13-007_DPP_and_Digital_Twin_Links.md)

### 11.2 External Standards

- **[ATA iSpec 2200](https://www.ata.org/)** – Information Standards for Aviation Maintenance
- **[SAE AS50881](https://www.sae.org/)** – Wiring Aerospace Vehicle
- **[ISO 15926](https://www.iso.org/standard/29557.html)** – Industrial automation systems and integration
- **[ISO 29002-20](https://www.iso.org/standard/45031.html)** – Exchange of characteristic data

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
