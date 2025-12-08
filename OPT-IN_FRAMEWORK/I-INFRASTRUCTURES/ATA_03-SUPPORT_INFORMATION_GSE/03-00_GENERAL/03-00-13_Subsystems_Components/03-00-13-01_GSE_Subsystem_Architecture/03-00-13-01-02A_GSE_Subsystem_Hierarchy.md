---
Title: "GSE Subsystem Hierarchy — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-13-01-02A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Detailed hierarchical structure of Ground Support Equipment (GSE) subsystems for the AMPEL360 BWB H₂ Hy-E aircraft."
Keywords: ["ATA 03","GSE","Subsystem Hierarchy","Ground Support","Architecture"]
Compliance:
  - "ATA iSpec 2200"
  - "S1000D"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  Parent: "../"
  Siblings:
    - "03-00-13-01-01A_GSE_Subsystem_Overview.md"
    - "03-00-13-01-03A_GSE_Subsystem_Interfaces.md"
    - "03-00-13-01-04A_GSE_Subsystem_Integration.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial GSE subsystem hierarchy" }
---

# GSE Subsystem Hierarchy — ATA 03 Support Information GSE

## 1. Purpose

This document defines the **hierarchical structure** of Ground Support Equipment (GSE) subsystems for the AMPEL360 BWB H₂ Hy-E aircraft. It establishes the breakdown structure from top-level systems down to individual components, enabling clear organization, configuration management, and traceability throughout the GSE lifecycle.

## 2. Scope

This document covers:

- Complete GSE hierarchical breakdown structure (HBS)
- System-subsystem-component relationships
- Hierarchical numbering and identification scheme
- Parent-child dependencies and relationships
- Integration with Part Number Registry (PNR)

## 3. Applicable Documents

- [ATA iSpec 2200](https://www.ata.org/resources/specifications) — Information Standards for Aviation Maintenance
- [ATA Spec 2000](https://www.ata.org/resources/specifications) — E-Business Specification
- [ISO 10007](https://www.iso.org/standard/70400.html) — Configuration Management
- [03-00-13-01-01A_GSE_Subsystem_Overview.md](./03-00-13-01-01A_GSE_Subsystem_Overview.md) — Parent overview document

## 4. GSE Hierarchical Breakdown Structure

### 4.1 Level 0: GSE System (Top Level)

```
Level 0: Ground Support Equipment System
└── Supports: AMPEL360 BWB H₂ Hy-E Aircraft Ground Operations
```

### 4.2 Level 1: Major GSE Categories

| L1 Code | Category Name | Description |
|---------|---------------|-------------|
| **GSE-H2** | Hydrogen Service Equipment | All hydrogen-related GSE |
| **GSE-EL** | Electrical Service Equipment | Ground electrical power and charging |
| **GSE-MX** | Maintenance Equipment | Maintenance stands, tooling, diagnostics |
| **GSE-EN** | Environmental Control Equipment | Pre-conditioned air, climate control |
| **GSE-GH** | Ground Handling Equipment | Towing, positioning, jacking |
| **GSE-SF** | Safety Equipment | Fire suppression, emergency response |
| **GSE-CT** | Control & Monitoring Systems | Automated control, sensors, HMI |

### 4.3 Level 2: GSE Subsystems

#### 4.3.1 GSE-H2: Hydrogen Service Equipment

```
GSE-H2: Hydrogen Service Equipment
├── GSE-H2-01: LH₂ Storage Subsystem
│   ├── GSE-H2-01-001: Primary Storage Tank
│   ├── GSE-H2-01-002: Backup Storage Tank
│   ├── GSE-H2-01-003: Vacuum Insulation System
│   ├── GSE-H2-01-004: Pressure Relief System
│   └── GSE-H2-01-005: Tank Monitoring System
│
├── GSE-H2-02: LH₂ Transfer Subsystem
│   ├── GSE-H2-02-001: Transfer Pump Assembly
│   ├── GSE-H2-02-002: Cryogenic Transfer Hoses
│   ├── GSE-H2-02-003: Quick-Connect Couplings
│   ├── GSE-H2-02-004: Flow Control Valves
│   └── GSE-H2-02-005: Flow Metering System
│
├── GSE-H2-03: H₂ Safety Subsystem
│   ├── GSE-H2-03-001: Hydrogen Leak Detectors
│   ├── GSE-H2-03-002: Emergency Vent System
│   ├── GSE-H2-03-003: Grounding Equipment
│   ├── GSE-H2-03-004: Safety Interlock System
│   └── GSE-H2-03-005: Fire Detection System
│
└── GSE-H2-04: Cryogenic Control Subsystem
    ├── GSE-H2-04-001: Temperature Control Unit
    ├── GSE-H2-04-002: Pressure Control Unit
    ├── GSE-H2-04-003: Boil-Off Gas Recovery
    ├── GSE-H2-04-004: Cryogenic Sensors Array
    └── GSE-H2-04-005: Control System PLC
```

#### 4.3.2 GSE-EL: Electrical Service Equipment

```
GSE-EL: Electrical Service Equipment
├── GSE-EL-01: Ground Power Unit (GPU)
│   ├── GSE-EL-01-001: 400Hz AC Generator
│   ├── GSE-EL-01-002: DC Power Converter
│   ├── GSE-EL-01-003: Power Distribution Panel
│   ├── GSE-EL-01-004: Cable Reels and Connectors
│   └── GSE-EL-01-005: Power Quality Monitoring
│
├── GSE-EL-02: Battery Charging System
│   ├── GSE-EL-02-001: Main Battery Charger
│   ├── GSE-EL-02-002: APU Battery Charger
│   ├── GSE-EL-02-003: Emergency Battery Pack
│   └── GSE-EL-02-004: Charge Monitoring System
│
└── GSE-EL-03: Emergency Power Backup
    ├── GSE-EL-03-001: Backup Generator
    ├── GSE-EL-03-002: UPS System
    ├── GSE-EL-03-003: Transfer Switch
    └── GSE-EL-03-004: Battery Bank
```

#### 4.3.3 GSE-MX: Maintenance Equipment

```
GSE-MX: Maintenance Equipment
├── GSE-MX-01: Access Equipment
│   ├── GSE-MX-01-001: Fuselage Access Stand
│   ├── GSE-MX-01-002: Wing Access Platform
│   ├── GSE-MX-01-003: Engine Access Stand
│   ├── GSE-MX-01-004: Tail Access Platform
│   └── GSE-MX-01-005: Adjustable Work Platform
│
├── GSE-MX-02: Specialized Tooling
│   ├── GSE-MX-02-001: H₂ Tank Inspection Tools
│   ├── GSE-MX-02-002: Cryogenic Torque Tools
│   ├── GSE-MX-02-003: Pressure Test Equipment
│   └── GSE-MX-02-004: Leak Detection Tools
│
└── GSE-MX-03: Diagnostic Equipment
    ├── GSE-MX-03-001: Portable Diagnostic Unit
    ├── GSE-MX-03-002: Data Download System
    ├── GSE-MX-03-003: Built-In Test Equipment (BITE) Interface
    └── GSE-MX-03-004: Non-Destructive Testing (NDT) Equipment
```

#### 4.3.4 GSE-EN: Environmental Control Equipment

```
GSE-EN: Environmental Control Equipment
├── GSE-EN-01: Pre-Conditioned Air (PCA) Unit
│   ├── GSE-EN-01-001: Air Conditioning Unit
│   ├── GSE-EN-01-002: Heating Unit
│   ├── GSE-EN-01-003: Distribution Ducting
│   ├── GSE-EN-01-004: Temperature Control System
│   └── GSE-EN-01-005: Air Quality Sensors
│
└── GSE-EN-02: Cabin Service Equipment
    ├── GSE-EN-02-001: Potable Water Service Cart
    ├── GSE-EN-02-002: Waste Water Service Cart
    ├── GSE-EN-02-003: Lavatory Service Equipment
    └── GSE-EN-02-004: Galley Service Cart
```

#### 4.3.5 GSE-GH: Ground Handling Equipment

```
GSE-GH: Ground Handling Equipment
├── GSE-GH-01: Towing and Positioning
│   ├── GSE-GH-01-001: Aircraft Tow Tractor
│   ├── GSE-GH-01-002: Tow Bar
│   ├── GSE-GH-01-003: Pushback Tug
│   └── GSE-GH-01-004: Positioning System
│
├── GSE-GH-02: Jacking Equipment
│   ├── GSE-GH-02-001: Main Jacks (Set of 4)
│   ├── GSE-GH-02-002: Auxiliary Jacks (Set of 2)
│   ├── GSE-GH-02-003: Jack Control Panel
│   └── GSE-GH-02-004: Safety Stands
│
└── GSE-GH-03: Loading Equipment
    ├── GSE-GH-03-001: Cargo Loader
    ├── GSE-GH-03-002: Container Dolly
    ├── GSE-GH-03-003: Belt Loader
    └── GSE-GH-03-004: Baggage Tractor and Carts
```

#### 4.3.6 GSE-SF: Safety Equipment

```
GSE-SF: Safety Equipment
├── GSE-SF-01: Fire Suppression
│   ├── GSE-SF-01-001: Aircraft Rescue and Firefighting (ARFF) Vehicle
│   ├── GSE-SF-01-002: Portable Fire Extinguishers (H₂-rated)
│   ├── GSE-SF-01-003: Fire Suppression System for H₂ GSE
│   └── GSE-SF-01-004: Fire Blankets and Covers
│
├── GSE-SF-02: Emergency Response
│   ├── GSE-SF-02-001: Emergency Response Kit
│   ├── GSE-SF-02-002: Spill Containment Equipment
│   ├── GSE-SF-02-003: Personal Protective Equipment (PPE)
│   └── GSE-SF-02-004: First Aid Station
│
└── GSE-SF-03: Safety Barriers and Signage
    ├── GSE-SF-03-001: Safety Barrier System
    ├── GSE-SF-03-002: Safety Cones and Signs
    ├── GSE-SF-03-003: Ground Marking Equipment
    └── GSE-SF-03-004: Warning Light System
```

#### 4.3.7 GSE-CT: Control & Monitoring Systems

```
GSE-CT: Control & Monitoring Systems
├── GSE-CT-01: PLC Control System
│   ├── GSE-CT-01-001: Primary PLC Controller
│   ├── GSE-CT-01-002: Backup PLC Controller
│   ├── GSE-CT-01-003: I/O Modules
│   └── GSE-CT-01-004: Control Logic Software
│
├── GSE-CT-02: HMI System
│   ├── GSE-CT-02-001: Operator Console
│   ├── GSE-CT-02-002: Touchscreen Display
│   ├── GSE-CT-02-003: HMI Software
│   └── GSE-CT-02-004: Alarm Annunciation System
│
├── GSE-CT-03: Sensor Network
│   ├── GSE-CT-03-001: Temperature Sensors
│   ├── GSE-CT-03-002: Pressure Sensors
│   ├── GSE-CT-03-003: Flow Sensors
│   ├── GSE-CT-03-004: Level Sensors
│   └── GSE-CT-03-005: H₂ Concentration Sensors
│
└── GSE-CT-04: Communication System
    ├── GSE-CT-04-001: Industrial Ethernet Switch
    ├── GSE-CT-04-002: Wireless Communication Module
    ├── GSE-CT-04-003: Data Logger
    └── GSE-CT-04-004: Remote Monitoring Interface
```

## 5. Hierarchical Numbering Scheme

### 5.1 Numbering Convention

The GSE hierarchical numbering follows this structure:

```
GSE-[L1]-[L2]-[L3]-[Variant]
│   │    │    │    │
│   │    │    │    └─ Variant code (A, B, C...) for alternate configurations
│   │    │    └────── Level 3: Component (001-999)
│   │    └─────────── Level 2: Subsystem (01-99)
│   └──────────────── Level 1: Category (H2, EL, MX, EN, GH, SF, CT)
└──────────────────── GSE prefix
```

**Examples**:
- `GSE-H2-01-001-A`: Hydrogen GSE, LH₂ Storage Subsystem, Primary Storage Tank, Variant A
- `GSE-EL-01-001-B`: Electrical GSE, GPU, 400Hz AC Generator, Variant B
- `GSE-CT-03-005-A`: Control GSE, Sensor Network, H₂ Concentration Sensors, Variant A

### 5.2 Hierarchical Relationships

Each component inherits properties from its parent:

| Level | Inherits From | Example |
|-------|---------------|---------|
| L1 (Category) | GSE System | GSE-H2 inherits system-wide requirements |
| L2 (Subsystem) | L1 Category | GSE-H2-01 inherits H₂ GSE requirements |
| L3 (Component) | L2 Subsystem | GSE-H2-01-001 inherits storage subsystem requirements |

## 6. Part Number Information

Each component in the hierarchy is assigned a unique Part Number from the Part Number Registry (PNR):

| Hierarchy Level | PNR Assignment | Example |
|-----------------|----------------|---------|
| L1 (Category) | No PNR (logical grouping) | N/A |
| L2 (Subsystem) | Assembly-level PNR | PN-GSE-H2-01-ASM |
| L3 (Component) | Component-level PNR | PN-GSE-H2-01-001 |

See [03-00-13-03_GSE_Part_Number_Registry](../03-00-13-03_GSE_Part_Number_Registry/) for complete PNR documentation.

## 7. Spare Parts Information

Critical spare parts are identified at the L3 (Component) level and tracked in the Spare Parts Management system:

| Criticality | Hierarchy Level | Spare Strategy |
|-------------|-----------------|----------------|
| Critical | L3 Component | 100% redundancy, immediate availability |
| Essential | L3 Component | 1-2 units in stock, < 7 days lead time |
| Standard | L3 Component | On-demand, < 30 days lead time |

See [03-00-13-04_GSE_Spare_Parts_Management](../03-00-13-04_GSE_Spare_Parts_Management/) for spare parts strategy.

## 8. Cross-References

### 8.1 Related ATA Chapters

- [ATA 02 — Operations Information](../../../../../ATA_02-OPERATIONS_INFORMATION/) — Ground operations
- [ATA 85 — Infrastructure Interface Standards](../../../../../ATA_85-INFRASTRUCTURE_INTERFACE_STANDARDS/) — Airport infrastructure

### 8.2 Related Documents

- [03-00-13-01-01A_GSE_Subsystem_Overview.md](./03-00-13-01-01A_GSE_Subsystem_Overview.md) — Parent overview
- [03-00-13-01-03A_GSE_Subsystem_Interfaces.md](./03-00-13-01-03A_GSE_Subsystem_Interfaces.md) — Interface definitions
- [03-00-13-03_GSE_Part_Number_Registry](../03-00-13-03_GSE_Part_Number_Registry/) — PNR system
- [03-00-13-04_GSE_Spare_Parts_Management](../03-00-13-04_GSE_Spare_Parts_Management/) — Spare parts management

### 8.3 Parent Document

- [03-00-13_Subsystems_Components](../) — Top-level subsystems directory

## 9. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-13-01-02A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 Ground Support Equipment WG

---
