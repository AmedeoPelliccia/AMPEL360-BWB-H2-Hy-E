# [Product Name] — Product Definition

**Product ID:** [PRD-XXX-NNNN]  
**Product Family:** [INH / COTS / KIT / SVC]  
**ATA Chapter:** 02-00-04  
**Status:** [CONCEPT / DESIGN / ACTIVE / LEGACY / RETIRED]

---

## 1. Product Overview

### 1.1 Description

[Provide a clear, concise description of the product, its purpose, and primary functions]

### 1.2 Key Features

* Feature 1
* Feature 2
* Feature 3

### 1.3 Applications

[Describe where and how this product is intended to be used]

---

## 2. Technical Specifications

### 2.1 Physical Characteristics

* **Dimensions:** [L x W x H]
* **Weight:** [kg / lbs]
* **Mounting:** [floor-standing / rack-mount / wall-mount / etc.]
* **Color/Finish:** [description]

### 2.2 Electrical Specifications

* **Power Input:** [voltage, frequency, phases]
* **Power Consumption:** [watts / VA]
* **Backup Power:** [UPS compatible / battery backed / etc.]

### 2.3 Environmental Requirements

* **Operating Temperature:** [min - max °C]
* **Storage Temperature:** [min - max °C]
* **Humidity:** [min - max %RH non-condensing]
* **Altitude:** [max operating altitude]

### 2.4 Interfaces & Connectivity

* **Network:** [Ethernet, fiber, wireless, etc.]
* **Data Interfaces:** [USB, serial, etc.]
* **Power:** [connector types]
* **Other:** [any special interfaces]

---

## 3. Configuration Options

### 3.1 Standard Configuration

[Describe the base/standard configuration of this product]

### 3.2 Available Options

| Option Code | Description | Impact | Lead Time |
|-------------|-------------|--------|-----------|
| OPT-001     | [Option name] | [Price/weight/size impact] | [weeks] |
| OPT-002     | [Option name] | [Price/weight/size impact] | [weeks] |

### 3.3 Configuration Rules

* [List any configuration constraints or requirements]
* [e.g., "Option A requires Option B"]
* [e.g., "Options C and D are mutually exclusive"]

See: `CONFIG/[Product_ID]_ConfigMatrix-R01.xlsx` for detailed configuration matrix

---

## 4. Bill of Materials (BOM)

### 4.1 Major Components

| Part Number | Description | Quantity | Source |
|-------------|-------------|----------|--------|
| [Part ID]   | [Description] | [qty]  | [PARTS / COTS] |
| [Part ID]   | [Description] | [qty]  | [PARTS / COTS] |

**Complete BOM:** See `BOM/[Product_ID]_BOM-R01.xlsx`

### 4.2 Related Assemblies

* [Reference to ASSEMBLIES if applicable]

---

## 5. Models & Drawings

### 5.1 3D Models

* **BIM Model:** `MODELS/BIM/[filename].rvt`
* **CAD Model:** `MODELS/CAD/[filename].[ext]`

### 5.2 Functional Models

* **Logical Model:** `MODELS/LOGICAL/[filename].md`

### 5.3 Drawings

| Drawing Number | Sheet | Description | Revision |
|----------------|-------|-------------|----------|
| [DWG-ID]       | SHT01 | [Description] | R01    |
| [DWG-ID]       | SHT02 | [Description] | R01    |

**Location:** `DRAWINGS/`

---

## 6. Documentation

### 6.1 Manuals

* **Installation Manual:** `MANUALS/[Product_ID]_InstallationManual-R01.pdf`
* **User Guide:** `MANUALS/[Product_ID]_UserGuide-R01.pdf`
* **Maintenance Manual:** `MANUALS/[Product_ID]_MaintenanceManual-R01.pdf`

### 6.2 Datasheets

* **Product Sheet:** `MANUALS/[Product_ID]_ProductSheet-R01.pdf`
* **Technical Datasheet:** `MANUALS/[Product_ID]_TechnicalDatasheet-R01.pdf`

### 6.3 Certifications & Compliance

* [List any certifications, standards compliance, etc.]
* [e.g., CE marked, UL listed, etc.]

---

## 7. Requirements Traceability

### 7.1 Related Requirements

* [Requirement ID] - [Requirement description]
* [Requirement ID] - [Requirement description]

**Reference:** See `02-00-03_Requirements` folder

### 7.2 Related ATA Chapters

* ATA [XX-XX-XX]: [Description]

---

## 8. Lifecycle Information

### 8.1 Design Status

* **Design Phase:** [Concept / Preliminary / Detailed / Released]
* **Last Review Date:** [YYYY-MM-DD]
* **Next Review Date:** [YYYY-MM-DD]

### 8.2 Manufacturing

* **Lead Time:** [weeks]
* **MOQ (Minimum Order Quantity):** [quantity]
* **Expected Life:** [years / cycles]

### 8.3 Support & Maintenance

* **Warranty Period:** [duration]
* **Recommended Maintenance Interval:** [frequency]
* **Spare Parts Availability:** [duration after production ends]

---

## 9. Dependencies

### 9.1 Required Products

* [Product ID] - [Product name] - [Why required]

### 9.2 Compatible Products

* [Product ID] - [Product name] - [Compatibility notes]

### 9.3 Optional Accessories

* [Product ID] - [Product name] - [Enhancement provided]

---

## 10. Related Documentation

### 10.1 Internal References

* [AMPEL360 Assets Standard](../../../../../../AMPEL360_ASSETS_STANDARD.md)
* [AMPEL360 Documentation Standard](../../../../../../AMPEL360_DOCUMENTATION_STANDARD.md)
* [PRODUCTS Admin](../../00_ADMIN/README.md) - Product governance and naming conventions

### 10.2 Related Asset Directories

* [PARTS](../../../PARTS/) - Component parts library
* [ASSEMBLIES](../../../ASSEMBLIES/) - Assembly definitions
* [MODELS](../../../MODELS/) - System models
* [DRAWINGS](../../../DRAWINGS/) - Engineering drawings
* [INSTALLATIONS](../../../INSTALLATIONS/) - Installation procedures

### 10.3 Standards & Regulations

[Add relevant standards and regulations with hyperlinks, e.g.:]
* [ISO 9001](https://www.iso.org/iso-9001-quality-management.html) - Quality management systems
* [IEC Standards](https://www.iec.ch/) - International Electrotechnical Commission standards

---

## 11. Notes & Revision History

### 11.1 Special Notes

[Any special considerations, warnings, or important information]

### 11.2 Revision History

| Revision | Date | Description | Author | Approver |
|----------|------|-------------|--------|----------|
| R01      | YYYY-MM-DD | Initial release | [Name] | [Name] |

---

## 12. Contacts

* **Product Owner:** [Name / Role]
* **Technical Lead:** [Name / Role]
* **Project Manager:** [Name / Role]

---

**Document Control:**
* **Status:** [WORKING / FOR_REVIEW / APPROVED / RETIRED]
* **Last Updated:** [YYYY-MM-DD]
* **Next Review:** [YYYY-MM-DD]
