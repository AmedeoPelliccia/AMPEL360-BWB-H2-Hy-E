# 85-00-13-005: Configurable Packages and Kits

## Document Information

- **Document ID**: 85-00-13-005
- **Title**: Configurable Packages and Kits
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-21

---

## 1. Introduction

This document defines **configurable packages and kits** for ATA 85 Infrastructure Interface Standards. These packages group related subsystems and components into logical, manageable units that can be procured, installed, tested, and maintained as coherent sets.

### 1.1 Purpose

Configurable packages and kits:

- **Simplify procurement** by grouping related components
- **Standardize configurations** across aircraft variants and airport types
- **Reduce integration complexity** through pre-validated component combinations
- **Improve maintainability** with complete spare parts packages
- **Enable flexibility** for customer-specific or mission-specific configurations

### 1.2 Scope

This document covers:

- Standard infrastructure kits by airport category
- Aircraft variant-specific infrastructure configurations
- Service and maintenance kits
- Upgrade and retrofit packages
- Relationship to BOMs and DPP entries

---

## 2. Kit Taxonomy

### 2.1 Kit Categories

| Category | Purpose | Typical Contents |
|----------|---------|------------------|
| **Installation Kits** | New aircraft installation | Complete subsystem with all components, hardware, cables |
| **Airport Kits** | Airport-specific configurations | Interface hardware matching airport infrastructure type |
| **Service Kits** | Scheduled maintenance | Replacement seals, filters, consumables |
| **Spare Kits** | Unscheduled maintenance | Common failure-prone components |
| **Upgrade Kits** | Retrofit/modernization | New capability components + retrofit instructions |
| **Test Kits** | Verification and calibration | Test equipment, adapters, calibration standards |

### 2.2 Kit Identification

Kits use the following ID format:

```
85-KIT-<DOMAIN>-<PURPOSE>-<SEQUENCE>
```

**Examples**:
- `85-KIT-H2-INST-001` – H₂ Infrastructure Installation Kit (standard)
- `85-KIT-APT-CAT1-001` – Airport Interface Kit for Category 1 Airports
- `85-KIT-GSE-SERV-010` – GSE Service Kit (annual maintenance)
- `85-KIT-CO2-UPGR-002` – CO₂ Battery Interface Upgrade Kit

---

## 3. Installation Kits

### 3.1 H₂ Infrastructure Installation Kit

**Kit ID**: `85-KIT-H2-INST-001`

**Description**: Complete H₂ fueling and venting infrastructure for standard BWB configuration.

**Subsystems Included**:
- 85-H2-FUEL-001: H₂ Fueling Interface Subsystem
- 85-H2-VENT-001: H₂ Vent Interface Subsystem
- 85-H2-SFTY-001: H₂ Safety Monitoring Subsystem
- 85-H2-PURGE-001: H₂ Purge Interface Subsystem

**Components** (excerpt):
| Part Number | Description | Qty |
|-------------|-------------|-----|
| 85-RCPT-H2F-001-A | H₂ Fueling Receptacle Assembly | 2 |
| 85-CONN-H2V-001-A | H₂ Vent Coupling | 2 |
| 85-SENS-H2S-010 | H₂ Leak Detection Sensor | 8 |
| 85-VALVE-H2F-005 | H₂ Shutoff Valve | 2 |
| 85-CTRL-H2F-020 | H₂ Fueling Controller | 1 |
| 85-CABL-H2F-050 | H₂ System Wiring Harness | 1 |
| 85-MNTS-H2F-100 | Receptacle Mounting Bracket | 2 |

**Documentation**:
- Installation Manual: `85-H2-INST-001-IM`
- Interface Control Document: `85-H2-INST-001-ICD`
- Test Procedures: `85-H2-INST-001-TP`

**Total Kit Weight**: ~85 kg  
**Installation Time**: 40 man-hours  
**Lead Time**: 120 days

See: [ASSETS/BOMs/85-00-13-A-101_H2_Infrastructure_BOM.xlsx](./ASSETS/BOMs/)

### 3.2 CO₂ Battery Interface Installation Kit

**Kit ID**: `85-KIT-CO2-INST-001`

**Description**: Complete CO₂ battery charging and thermal management infrastructure.

**Subsystems Included**:
- 85-CO2-CHRG-001: CO₂ Battery Charging Interface
- 85-CO2-THRM-001: CO₂ Battery Thermal Interface
- 85-CO2-DATA-001: CO₂ Battery Data Interface
- 85-CO2-SFTY-001: CO₂ Battery Safety Interface

**Components** (excerpt):
| Part Number | Description | Qty |
|-------------|-------------|-----|
| 85-RCPT-CO2-001-A | High-Power DC Charging Receptacle | 2 |
| 85-CONN-CO2T-001-A | Thermal Management Coupling | 2 |
| 85-RCPT-APT-010-A | Data Interface Receptacle | 1 |
| 85-SENS-CO2S-015 | Battery Temperature Sensor Array | 1 |
| 85-CTRL-CO2-025 | Battery Interface Controller | 1 |

**Total Kit Weight**: ~120 kg  
**Installation Time**: 60 man-hours  
**Lead Time**: 150 days

See: [ASSETS/BOMs/85-00-13-A-102_CO2_Battery_Infrastructure_BOM.xlsx](./ASSETS/BOMs/)

### 3.3 Airport Interface Installation Kit (Base)

**Kit ID**: `85-KIT-APT-INST-001`

**Description**: Standard airport interface kit for typical gate infrastructure.

**Subsystems Included**:
- 85-APT-PWR-001: Airport Gate Power Interface
- 85-APT-DATA-001: Airport Data Interface
- 85-APT-BRDG-001: Boarding Bridge Interface
- 85-APT-UTIL-001: Airport Utilities Interface

**Components** (excerpt):
| Part Number | Description | Qty |
|-------------|-------------|-----|
| 85-RCPT-APT-001-A | 400Hz AC Ground Power Receptacle | 1 |
| 85-RCPT-APT-002-A | 28V DC Ground Power Receptacle | 1 |
| 85-RCPT-APT-010-A | Ethernet Data Receptacle | 2 |
| 85-RCPT-APT-011-A | Fiber Optic Data Receptacle | 2 |
| 85-CONN-PAX-001-A | Bridge Docking Adapter | 3 |

**Total Kit Weight**: ~65 kg  
**Installation Time**: 35 man-hours  
**Lead Time**: 90 days

See: [ASSETS/BOMs/85-00-13-A-103_Airport_Interface_BOM.xlsx](./ASSETS/BOMs/)

---

## 4. Airport-Specific Configuration Kits

### 4.1 Airport Categories

Infrastructure kits are tailored to airport infrastructure capabilities:

| Category | Description | Typical Airports | Kit Features |
|----------|-------------|------------------|--------------|
| **CAT-1** | Basic infrastructure | Regional airports | Standard power, basic data, no H₂ |
| **CAT-2** | Standard infrastructure | Major domestic hubs | Standard power, full data, H₂ capable |
| **CAT-3** | Advanced infrastructure | International hubs | High-power, advanced data, H₂ + CO₂ |
| **CAT-4** | Premium infrastructure | Future smart airports | All features + wireless, AI monitoring |

### 4.2 Category 1 Airport Kit

**Kit ID**: `85-KIT-APT-CAT1-001`

**Description**: Minimal interface kit for basic airport infrastructure.

**Includes**:
- 400Hz AC power interface (standard)
- Basic Ethernet data (1 Gbps)
- Manual boarding bridge adapter
- **Excludes**: H₂ fueling, CO₂ charging, advanced data

**Use Case**: Aircraft operating primarily from regional airports without H₂ infrastructure.

### 4.3 Category 2 Airport Kit

**Kit ID**: `85-KIT-APT-CAT2-001`

**Description**: Standard kit for typical major airport operations.

**Includes**:
- All CAT-1 features
- H₂ fueling interface (single receptacle)
- Enhanced data (10 Gbps Ethernet + fiber optic)
- Automated bridge docking

**Use Case**: Standard configuration for most aircraft in fleet.

### 4.3 Category 3 Airport Kit

**Kit ID**: `85-KIT-APT-CAT3-001`

**Description**: Full-featured kit for premium airport infrastructure.

**Includes**:
- All CAT-2 features
- Dual H₂ fueling receptacles (faster refueling)
- CO₂ battery charging interface (400 kW)
- High-speed data (100 Gbps fiber optic)
- Environmental control interface (gate HVAC)

**Use Case**: Aircraft based at major international hubs with full infrastructure.

### 4.4 Category 4 Airport Kit (Future)

**Kit ID**: `85-KIT-APT-CAT4-001`

**Description**: Next-generation smart airport interface kit.

**Includes**:
- All CAT-3 features
- Wireless power transfer (CO₂ battery inductive charging)
- Free-space optical data link (backup/supplemental)
- AI-driven predictive monitoring
- Blockchain-verified DPP integration

**Use Case**: Future deployment at next-generation smart airports (2030+).

---

## 5. Service and Maintenance Kits

### 5.1 Annual Service Kit – H₂ Infrastructure

**Kit ID**: `85-KIT-H2-SERV-010`

**Description**: Consumables and replacement items for annual H₂ system service.

**Contents**:
| Part Number | Description | Qty |
|-------------|-------------|-----|
| 85-SEAL-H2F-001 | H₂ Receptacle Seal Kit | 2 |
| 85-FLTR-H2F-010 | H₂ Particulate Filter | 2 |
| 85-SENS-H2S-010 | H₂ Leak Sensor (replacement) | 2 |
| 85-MISC-LUBE-001 | H₂-compatible Lubricant (50 mL) | 2 |
| 85-MISC-CLEAN-001 | H₂ System Cleaning Solution (1 L) | 1 |

**Service Interval**: 12 months or 500 flight hours  
**Installation Time**: 4 man-hours  
**Cost**: ~€1,500

### 5.2 Annual Service Kit – CO₂ Battery Interface

**Kit ID**: `85-KIT-CO2-SERV-010`

**Description**: Consumables for CO₂ battery interface maintenance.

**Contents**:
| Part Number | Description | Qty |
|-------------|-------------|-----|
| 85-SEAL-CO2-001 | Charging Receptacle Seal Kit | 2 |
| 85-SEAL-CO2T-001 | Thermal Coupling Seal Kit | 2 |
| 85-FLTR-CO2T-005 | Coolant Filter Cartridge | 2 |
| 85-FLUID-CO2T-010 | Water-Glycol Coolant (5 L) | 1 |

**Service Interval**: 12 months or 500 flight hours  
**Installation Time**: 3 man-hours  
**Cost**: ~€1,200

### 5.3 Spare Parts Kit – General Infrastructure

**Kit ID**: `85-KIT-INFR-SPAR-001`

**Description**: Common spare parts for unscheduled maintenance.

**Contents**:
| Part Number | Description | Qty |
|-------------|-------------|-----|
| 85-CONN-H2F-001-A | H₂ Fueling Connector (spare) | 1 |
| 85-SENS-H2S-010 | H₂ Leak Sensor | 2 |
| 85-RCPT-APT-010-A | Ethernet Receptacle | 1 |
| 85-SEAL-H2F-001 | H₂ Seal Kit | 2 |
| 85-SEAL-CO2-001 | CO₂ Seal Kit | 2 |
| 85-MISC-FAST-001 | Fastener Assortment | 1 |

**Recommended Stock**: 1 kit per 5 aircraft  
**Cost**: ~€5,000

---

## 6. Upgrade and Retrofit Kits

### 6.1 H₂ Infrastructure Upgrade Kit

**Kit ID**: `85-KIT-H2-UPGR-001`

**Description**: Retrofit existing aircraft with H₂ fueling capability.

**Includes**:
- All H₂ infrastructure components (as per Installation Kit)
- Structural reinforcement kit (if required)
- Retrofit wiring harness (adapts to existing electrical system)
- Software update package (interface controller firmware)
- Retrofit installation manual

**Prerequisites**:
- Aircraft must have ATA 28 fuel system provisions
- Structural mod allowance available
- Certification amendment (STC or EASA minor change)

**Installation Time**: 80 man-hours (includes structural work)  
**Certification**: STC required  
**Cost**: ~€150,000

### 6.2 CO₂ Battery Fast-Charging Upgrade

**Kit ID**: `85-KIT-CO2-UPGR-002`

**Description**: Upgrade from 200 kW to 400 kW fast charging capability.

**Includes**:
- Upgraded charging receptacle (85-RCPT-CO2-002-A)
- Enhanced cooling system components
- Higher-capacity wiring harness
- Updated interface controller firmware

**Prerequisites**:
- Existing CO₂ battery system installed
- Battery management system (BMS) version 2.0 or higher

**Installation Time**: 20 man-hours  
**Certification**: Minor change (EASA Form 1)  
**Cost**: ~€25,000

---

## 7. Test and Calibration Kits

### 7.1 H₂ System Test Kit

**Kit ID**: `85-KIT-H2-TEST-001`

**Description**: Portable test equipment for H₂ infrastructure verification.

**Contents**:
| Item | Description | Qty |
|------|-------------|-----|
| H₂ Leak Detector | Portable electrochemical detector (0-10,000 ppm) | 1 |
| Pressure Test Gauge | Digital gauge (0-1000 bar, ±0.1% accuracy) | 1 |
| Flow Meter | Thermal mass flow meter (0-20 kg/min H₂) | 1 |
| Test Hoses | H₂-compatible test hoses with fittings | 1 set |
| Calibration Gas | 1000 ppm H₂ in nitrogen (1 L cylinder) | 1 |
| Test Adapters | Mating connectors for aircraft receptacles | 1 set |

**Use Case**: Functional testing after installation, maintenance, or malfunction.

### 7.2 Electrical Interface Test Kit

**Kit ID**: `85-KIT-ELEC-TEST-001`

**Description**: Test equipment for power and data interfaces.

**Contents**:
| Item | Description | Qty |
|------|-------------|-----|
| Multimeter | True RMS multimeter (AC/DC, 1000V max) | 1 |
| Insulation Tester | Megohmmeter (1000V DC, 10 TΩ range) | 1 |
| Oscilloscope | 4-channel, 100 MHz, portable | 1 |
| Network Tester | Ethernet cable tester (Cat 6A, 10 Gbps) | 1 |
| Power Analyzer | 3-phase power quality analyzer (400Hz capable) | 1 |
| Test Leads | Assorted test leads and probes | 1 set |

**Use Case**: Electrical verification and troubleshooting.

---

## 8. Kit Configuration Management

### 8.1 Kit Bill of Materials (BOM)

Each kit has a master BOM maintained in:

**[MASTER/85-00-13-M-004_Subsystem_Configurable_Units.xlsx](./MASTER/)**

BOM includes:
- Part numbers and descriptions
- Quantities
- Unit weights and dimensions
- Lead times and costs
- Supplier information
- Revision history

### 8.2 Kit Versions

Kits use version control:

```
<KIT_ID>-V<MAJOR>.<MINOR>
```

**Example**: `85-KIT-H2-INST-001-V2.1`
- Version 2.1 = Major revision 2, minor update 1

Version changes:
- **Major**: Component change affecting function or interfaces
- **Minor**: Documentation update, alternative supplier, cost optimization

### 8.3 Configuration Baseline

Standard aircraft configurations defined by kit combinations:

**Example: AMPEL360-BWB-H2-STD (Standard Configuration)**:
- 85-KIT-H2-INST-001 (H₂ Infrastructure)
- 85-KIT-CO2-INST-001 (CO₂ Battery Interface)
- 85-KIT-APT-CAT2-001 (Category 2 Airport Interface)
- 85-KIT-GSE-INST-001 (GSE Interface)
- 85-KIT-PAX-INST-001 (Passenger Interface)

---

## 9. Procurement and Supply Chain

### 9.1 Kit Procurement

Kits can be procured as:

1. **Complete kits** – All components bundled, factory-tested
2. **Component kits** – Loose components, customer assembly/test
3. **Build-to-order** – Customized kit based on specific requirements

### 9.2 Lead Times

Typical procurement lead times:

| Kit Type | Lead Time | Notes |
|----------|-----------|-------|
| Standard installation kits | 90-150 days | High-volume production |
| Airport-specific kits | 60-120 days | Moderate customization |
| Service kits | 30-45 days | Stock items |
| Spare kits | 30-45 days | Stock items |
| Upgrade kits | 120-180 days | Low volume, long-lead items |
| Custom kits | 150-240 days | Engineering required |

### 9.3 Supplier Integration

Kit suppliers:
- Provide pre-assembled, tested kits where possible
- Include installation documentation and consumables
- Offer technical support during installation
- Maintain traceability to DPP requirements

---

## 10. DPP and Digital Twin Integration

### 10.1 Kit-Level DPP

Each kit instance has a DPP entry:

```
DPP-85-KIT-<KIT_ID>-SN-<SERIAL>
```

**Example**: `DPP-85-KIT-H2-INST-001-SN-202511-042`

Kit DPP includes:
- Kit BOM (all component part numbers and serial numbers)
- Assembly date and location
- Installation date and aircraft serial number
- Service history (when service kits used)
- Configuration changes (upgrades applied)

### 10.2 Component-Level Linkage

Kit DPP links to individual component DPPs:

```
Kit DPP (85-KIT-H2-INST-001-SN-202511-042)
├── Component DPP (85-RCPT-H2F-001-A-SN-202511-001-00042)
├── Component DPP (85-CONN-H2V-001-A-SN-202511-002-00015)
├── Component DPP (85-SENS-H2S-010-SN-202510-005-00234)
└── ... (all kit components)
```

This enables:
- Full traceability from kit to individual components
- Impact analysis when component issues discovered
- Lifecycle tracking at both kit and component level

See: [85-00-13-007_DPP_and_Digital_Twin_Links.md](./85-00-13-007_DPP_and_Digital_Twin_Links.md)

---

## 11. Maintenance and Lifecycle

### 11.1 Kit Inspection

Kits inspected:
- **Pre-installation**: Verify all components present, undamaged
- **Post-installation**: Functional test per test procedures
- **Periodic**: Per maintenance program (typically annual)

### 11.2 Kit Updates

Kits may be updated due to:
- Component obsolescence
- Supplier changes
- Design improvements
- Cost reduction initiatives
- Regulatory changes

Update process:
1. Engineering change proposal (ECP)
2. Impact assessment (form, fit, function, cost)
3. CCB approval
4. BOM and documentation update
5. Notification to customers (Service Bulletin)

### 11.3 End-of-Life

At aircraft retirement:
- Kits disassembled
- Components assessed for refurbishment or recycling
- DPP updated with disposition (reuse, recycle, scrap)
- Material recovery per ATA 99 circularity protocols

---

## 12. References

### 12.1 Internal References

- [85-00-13-001_Subsystems_Components_Overview.md](./85-00-13-001_Subsystems_Components_Overview.md)
- [85-00-13-003_Component_Taxonomy_and_Coding.md](./85-00-13-003_Component_Taxonomy_and_Coding.md)
- [85-00-13-004_Interface_Hardware_Catalog.md](./85-00-13-004_Interface_Hardware_Catalog.md)
- [85-00-13-007_DPP_and_Digital_Twin_Links.md](./85-00-13-007_DPP_and_Digital_Twin_Links.md)
- [ASSETS/BOMs/](./ASSETS/BOMs/)

### 12.2 External Standards

- **[ATA iSpec 2200](https://www.ata.org/)** – Provisioning and illustrated parts data
- **[S1000D](http://www.s1000d.org/)** – Technical publication specification
- **[EASA Part 21](https://www.easa.europa.eu/en/document-library/regulations/easa-part-21-regulation)** – Certification and approval of changes

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
