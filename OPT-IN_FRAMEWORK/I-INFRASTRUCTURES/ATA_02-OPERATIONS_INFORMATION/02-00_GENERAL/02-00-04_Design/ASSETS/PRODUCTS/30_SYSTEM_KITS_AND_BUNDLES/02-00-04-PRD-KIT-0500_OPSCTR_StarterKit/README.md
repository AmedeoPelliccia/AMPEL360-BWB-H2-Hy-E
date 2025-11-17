# OPSCTR Starter Kit — System Bundle

**Product ID:** PRD-KIT-0500  
**Product Family:** KIT (System Kit / Bundle)  
**ATA Chapter:** 02-00-04  
**Status:** CONCEPT

---

## 1. Kit Overview

### 1.1 Description

The OPSCTR Starter Kit is a complete, pre-configured bundle of products and 
components designed to establish a basic operations control center for small to 
medium-sized operations. This kit includes all essential furniture, equipment, 
and accessories needed for a 2-operator control room.

### 1.2 Key Features

* Complete 2-operator setup
* Pre-selected compatible components
* Simplified procurement (single SKU)
* Reduced lead time vs. individual purchases
* Installation guide included
* Tested and validated configuration

### 1.3 Target Applications

Ideal for:
* New operations centers
* Satellite control rooms
* Emergency backup facilities
* Pilot installations
* Budget-constrained projects

---

## 2. Kit Contents

### 2.1 Included Products

| Product ID | Product Name | Quantity | Notes |
|------------|--------------|----------|-------|
| [PRD-INH-0010](../../10_INHOUSE_PRODUCTS/02-00-04-PRD-INH-0010_OPSCTR_ConsoleSystem/) | OPSCTR Console System | 2 | Standard configuration |
| PRD-COTS-1300 | Display Monitor 32" 4K | 4 | 2 per console |
| PRD-COTS-1100 | UPS 3kVA | 1 | Shared between consoles |
| PRD-COTS-1101 | Rack PDU | 2 | Power distribution |
| PRD-INH-0013 | Acoustic Privacy Screen | 1 | Between operators |
| PRD-COTS-1310 | Dual Monitor Arm | 2 | One per console |
| PRD-INH-0015 | Cable Management Kit | 1 | Complete set |

### 2.2 Included Accessories

* Network cables (Cat6, various lengths)
* Power cables (IEC, various lengths)
* Cable ties and labels
* Installation hardware kit
* Leveling shims

### 2.3 Included Documentation

* Installation guide (step-by-step)
* Configuration worksheet
* Wiring diagram
* Commissioning checklist
* Operations quick-start guide

---

## 3. Technical Specifications

### 3.1 Space Requirements

* **Minimum Room Size:** 5m x 4m
* **Recommended Room Size:** 6m x 5m
* **Ceiling Height:** 2.7m minimum
* **Layout:** See `DOCUMENTATION/02-00-04-PRD-KIT-0500_LayoutGuide.pdf`

### 3.2 Power Requirements

* **Total Power Draw:** 2.5 kW maximum
* **Input Required:** 230V AC, 16A circuit (single phase)
* **UPS Backup Time:** 15 minutes (full load)
* **Outlets Needed:** 2x dedicated circuits recommended

### 3.3 Network Requirements

* **Network Drops:** 4x Ethernet (1Gbps minimum)
* **Network Equipment:** Not included (customer provided)
* **Cabling:** 20m included, additional available separately

### 3.4 Environmental Requirements

* **Temperature:** 20 - 26°C (controlled environment)
* **Humidity:** 40 - 60% RH
* **Noise Level:** < 45 dBA with acoustic treatments
* **Lighting:** 300-500 lux recommended (not included in kit)

---

## 4. Configuration Options

### 4.1 Standard Kit (KIT-0500-STD)

* Base configuration as listed above
* Standard console finish (RAL 7035)
* Standard monitor arms

### 4.2 Kit Variants

| Variant Code | Description | Delta from Standard |
|--------------|-------------|---------------------|
| KIT-0500-PREM | Premium kit | Solid surface worktops, quad monitors |
| KIT-0500-COMP | Compact kit | Smaller footprint, single monitor per console |
| KIT-0500-EXT | Extended kit | 3 operators instead of 2 |

### 4.3 Add-On Options

* Additional operator positions
* Enhanced UPS capacity
* Upgraded monitors (larger/higher resolution)
* Sit-stand console upgrade
* Additional acoustic panels

---

## 5. Bill of Materials

### 5.1 Complete Kit BOM

See: `BOM/02-00-04-PRD-KIT-0500_BOM-R01.xlsx`

The BOM references all component products from:
* [`PRODUCTS/10_INHOUSE_PRODUCTS/`](../../10_INHOUSE_PRODUCTS/)
* [`PRODUCTS/20_COTS_EQUIPMENT/`](../../20_COTS_EQUIPMENT/)
* [`ASSETS/PARTS/`](../../../PARTS/) (for accessories)

### 5.2 BOM Structure

* Level 1: Kit assembly
* Level 2: Product references (PRD-xxx)
* Level 3: Component parts (from referenced products)

---

## 6. Pricing & Procurement

### 6.1 Kit Pricing

* **List Price:** [To be determined]
* **Volume Discount:** Available for 3+ kits
* **Bundle Savings:** ~15% vs. individual product purchase
* **Freight:** Calculated separately based on destination

### 6.2 Lead Time

* **Standard Kit:** 10 weeks from order
* **Custom Variants:** 12-14 weeks
* **Express Option:** 6-8 weeks (premium cost)

### 6.3 Ordering

* **Order Code:** PRD-KIT-0500 (+ variant suffix)
* **MOQ:** 1 kit
* **Delivery:** Consolidated shipment
* **Installation Services:** Available (quote separately)

---

## 7. Installation & Commissioning

### 7.1 Installation Requirements

* **Installation Time:** 2-3 days (2 technicians)
* **Tools Required:** Standard hand tools, power drill
* **Skills Required:** Basic electrical, network cabling
* **Prerequisites:** Room prepared, power/network available

### 7.2 Installation Services

* **Self-Install:** Instructions and support included
* **Supervised Install:** Technical advisor on-site
* **Full Install:** Complete turnkey installation
* **Training:** Operator training available

### 7.3 Commissioning

* Follow commissioning checklist provided
* System integration testing required
* Acceptance test procedure included
* Support available during commissioning

---

## 8. Documentation

### 8.1 Kit Documentation

* **Kit Overview:** `DOCUMENTATION/02-00-04-PRD-KIT-0500_Overview.pdf`
* **Installation Guide:** `DOCUMENTATION/02-00-04-PRD-KIT-0500_InstallGuide.pdf`
* **Layout Guide:** `DOCUMENTATION/02-00-04-PRD-KIT-0500_LayoutGuide.pdf`
* **Commissioning Checklist:** `DOCUMENTATION/02-00-04-PRD-KIT-0500_Commissioning.pdf`

### 8.2 Component Documentation

All individual product documentation is referenced:
* Console manuals (PRD-INH-0010)
* UPS manual (PRD-COTS-1100)
* Monitor specifications (PRD-COTS-1300)
* etc.

---

## 9. Requirements & Standards

### 9.1 Related Requirements

* REQ-OPS-010: Operations center minimum capabilities
* REQ-OPS-011: Operator workstation requirements
* REQ-OPS-012: Control room ergonomics

### 9.2 Standards Compliance

* [ISO 9241-5](https://www.iso.org/standard/77520.html): Ergonomic requirements for office work with visual display terminals
* [IEC 60950](https://webstore.iec.ch/publication/2089): Safety of information technology equipment (superseded by [IEC 62368-1](https://webstore.iec.ch/publication/26136))
* [NFPA 75](https://www.nfpa.org/): Standard for the Fire Protection of Information Technology Equipment
* [ANSI/HFES 100](https://www.hfes.org/): Human factors engineering of computer workstations

---

## 10. Support & Warranty

### 10.1 Warranty

* **Kit Warranty:** 2 years (entire kit)
* **Component Warranties:** Per individual product terms
* **Extended Warranty:** Available (quote separately)

### 10.2 Support

* **Technical Support:** Email and phone during business hours
* **On-Site Support:** Available (quote separately)
* **Spare Parts:** Available from component product listings
* **Upgrades:** Kit can be upgraded with additional products

---

## 11. Notes & Revision History

### 11.1 Special Notes

* This kit is designed for standard installations; custom requirements may need individual product selection
* All components are tested together for compatibility
* Kit pricing subject to change based on component costs
* Volume pricing available for multiple kit purchases
* Custom kits can be configured upon request

### 11.2 Revision History

| Revision | Date | Description | Author | Approver |
|----------|------|-------------|--------|----------|
| R01      | 2025-11-17 | Initial kit definition | AI Agent | Pending |

---

## 12. Contacts

* **Product Manager:** [To be assigned]
* **Sales Contact:** [To be assigned]
* **Technical Support:** [To be assigned]

---

**Document Control:**
* **Status:** WORKING
* **Last Updated:** 2025-11-17
* **Next Review:** 2026-01-17
