# OPSCTR Console System — Product Definition

**Product ID:** PRD-INH-0010  
**Product Family:** INH (In-House)  
**ATA Chapter:** 02-00-04  
**Status:** CONCEPT

---

## 1. Product Overview

### 1.1 Description

The OPSCTR Console System is a modular operations center console designed for 
aircraft operations control centers. It provides an integrated workstation for 
operations controllers with ergonomic design, equipment mounting capabilities, 
and integrated cable management.

### 1.2 Key Features

* Modular design allowing flexible configurations
* Integrated cable management system
* Adjustable monitor arms (supports up to 4 displays)
* Ergonomic sit-stand capability
* Built-in power distribution
* Acoustic panels for noise reduction
* Customizable work surface options

### 1.3 Applications

Primary use in:
* Aircraft operations control centers
* Ground operations coordination centers
* Maintenance control facilities
* Flight dispatch centers

---

## 2. Technical Specifications

### 2.1 Physical Characteristics

* **Dimensions:** 2400mm (L) x 900mm (W) x 750-1200mm (H adjustable)
* **Weight:** 180 kg (base configuration)
* **Mounting:** Floor-standing with leveling feet
* **Color/Finish:** RAL 7035 light grey, powder-coated steel frame
* **Work Surface:** Laminate or solid surface options

### 2.2 Electrical Specifications

* **Power Input:** 230V AC, 50/60Hz, single phase
* **Power Consumption:** 50W (console electronics only)
* **Integrated PDU:** 8x IEC C13 outlets, 2x USB charging ports
* **Circuit Protection:** Integrated circuit breakers

### 2.3 Environmental Requirements

* **Operating Temperature:** 15 - 30°C
* **Storage Temperature:** -10 - 50°C
* **Humidity:** 20 - 80% RH non-condensing
* **Altitude:** Up to 2000m

### 2.4 Interfaces & Connectivity

* **Network:** Integrated cable trays for Ethernet routing
* **Data Interfaces:** Cable pass-throughs for all standard connections
* **Power:** Integrated PDU with C14 input connector
* **Other:** Monitor arm mounting points (VESA compatible)

---

## 3. Configuration Options

### 3.1 Standard Configuration

Base console includes:
* Structural frame (2400mm width)
* Standard work surface
* Basic cable management
* Single monitor arm
* Integrated PDU

### 3.2 Available Options

| Option Code | Description | Impact | Lead Time |
|-------------|-------------|--------|-----------|
| OPT-001     | Premium solid surface worktop | +5kg, +cost | 4 weeks |
| OPT-002     | Dual monitor arm upgrade | +3kg | 2 weeks |
| OPT-003     | Quad monitor arm upgrade | +6kg | 2 weeks |
| OPT-004     | Sit-stand electric adjustment | +15kg, +cost | 4 weeks |
| OPT-005     | Enhanced acoustic panels | +8kg | 3 weeks |
| OPT-006     | Integrated task lighting | +2kg | 2 weeks |
| OPT-007     | Extended cable management | +4kg | 2 weeks |

### 3.3 Configuration Rules

* Options OPT-002 and OPT-003 are mutually exclusive (single OR dual OR quad monitors)
* Option OPT-004 (sit-stand) requires structural upgrade (automatic)
* Maximum 4 monitor arms per console
* Extended width (3000mm) available as custom configuration

See: `CONFIG/02-00-04-PRD-INH-0010_ConfigMatrix-R01.xlsx` for detailed configuration matrix

---

## 4. Bill of Materials (BOM)

### 4.1 Major Components

| Part Number | Description | Quantity | Source |
|-------------|-------------|----------|--------|
| To be defined | Console frame structure | 1 | [PARTS/STRUCTURAL](../../../PARTS/) |
| To be defined | Work surface panel | 1 | [PARTS/FURNITURE](../../../PARTS/) |
| To be defined | Monitor arm assembly | 1-4 | COTS |
| To be defined | Cable management system | 1 set | [PARTS/ACCESSORIES](../../../PARTS/) |
| To be defined | PDU 8-outlet | 1 | COTS |
| To be defined | Leveling feet set | 4 | COTS |

**Complete BOM:** See `BOM/02-00-04-PRD-INH-0010_BOM-R01.xlsx`

### 4.2 Related Assemblies

* Console Frame Assembly (to be defined in [ASSEMBLIES/](../../../ASSEMBLIES/))
* Cable Management Assembly (to be defined in [ASSEMBLIES/](../../../ASSEMBLIES/))

---

## 5. Models & Drawings

### 5.1 3D Models

* **BIM Model:** `MODELS/BIM/02-00-04-MDL-PRD-INH-0010_BIM_RefModel-R01.rvt`
* **CAD Model:** To be created

### 5.2 Functional Models

* **Logical Model:** `MODELS/LOGICAL/02-00-04-MDL-PRD-INH-0010_FunctionalModel-R01.md` (in this product folder)

### 5.3 Drawings

| Drawing Number | Sheet | Description | Revision |
|----------------|-------|-------------|----------|
| 02-00-04-DWG-EQP-PRD-INH-0010-ConsoleSystem-SHT01 | SHT01 | General arrangement | R01 |
| 02-00-04-DWG-EQP-PRD-INH-0010-ConsoleSystem-SHT02 | SHT02 | Detailed dimensions | R01 |
| 02-00-04-DWG-EQP-PRD-INH-0010-ConsoleSystem-SHT03 | SHT03 | Electrical schematic | R01 |

**Location:** [DRAWINGS/](../../../DRAWINGS/)

---

## 6. Documentation

### 6.1 Manuals

* **Installation Manual:** `MANUALS/02-00-04-PRD-INH-0010_InstallationManual-R01.pdf`
* **User Guide:** `MANUALS/02-00-04-PRD-INH-0010_UserGuide-R01.pdf`
* **Maintenance Manual:** `MANUALS/02-00-04-PRD-INH-0010_MaintenanceManual-R01.pdf`

### 6.2 Datasheets

* **Product Sheet:** `MANUALS/02-00-04-PRD-INH-0010_ProductSheet-R01.pdf`
* **Technical Datasheet:** `MANUALS/02-00-04-PRD-INH-0010_TechnicalDatasheet-R01.pdf`

### 6.3 Certifications & Compliance

* CE marked for European markets
* Ergonomic design per [ISO 9241-5](https://www.iso.org/standard/77520.html) (Ergonomic requirements for office work with visual display terminals)
* Fire rating: M1/B1 materials
* [BIFMA](https://www.bifma.org/) standards compliance (office furniture safety and performance)

---

## 7. Requirements Traceability

### 7.1 Related Requirements

* REQ-OPS-001: Operations center console ergonomics
* REQ-OPS-002: Multi-display support
* REQ-OPS-003: Cable management requirements
* REQ-OPS-004: Acoustic performance

**Reference:** See [02-00-03_Requirements](../../../../02-00-03_Requirements/) folder

### 7.2 Related ATA Chapters

* [ATA 02-00-04](../../../../02-00-04_Design/): Operations Information - Design
* [ATA 02-00-03](../../../../02-00-03_Requirements/): Operations Information - Requirements

---

## 8. Lifecycle Information

### 8.1 Design Status

* **Design Phase:** Concept
* **Last Review Date:** 2025-11-17
* **Next Review Date:** 2026-01-17

### 8.2 Manufacturing

* **Lead Time:** 8-12 weeks (standard configuration)
* **MOQ (Minimum Order Quantity):** 1 unit
* **Expected Life:** 15 years with proper maintenance

### 8.3 Support & Maintenance

* **Warranty Period:** 5 years (structural), 2 years (electrical components)
* **Recommended Maintenance Interval:** Annual inspection
* **Spare Parts Availability:** 20 years after production ends

---

## 9. Dependencies

### 9.1 Required Products

* None (standalone product)

### 9.2 Compatible Products

* PRD-COTS-1300: Display monitors (various sizes)
* PRD-INH-0011: Operator workstation (complementary)
* PRD-COTS-1100: UPS systems (for backup power)

### 9.3 Optional Accessories

* PRD-INH-0012: Console expansion module
* PRD-INH-0013: Acoustic privacy screen
* PRD-COTS-1310: Additional monitor arms

---

## 10. Notes & Revision History

### 10.1 Special Notes

* Custom colors available upon request (MOQ may apply)
* Can be integrated with building BIM models
* Designed for 24/7 operations environment
* Modular design allows for future upgrades

### 10.2 Revision History

| Revision | Date | Description | Author | Approver |
|----------|------|-------------|--------|----------|
| R01      | 2025-11-17 | Initial concept definition | AI Agent | Pending |

---

## 11. Contacts

* **Product Owner:** [To be assigned]
* **Technical Lead:** [To be assigned]
* **Project Manager:** [To be assigned]

---

**Document Control:**
* **Status:** WORKING
* **Last Updated:** 2025-11-17
* **Next Review:** 2026-01-17
