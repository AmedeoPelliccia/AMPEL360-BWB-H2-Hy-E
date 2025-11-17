# Part: ServerChassis_2U (02-00-04-PRT-IT-0200)

## 1. Part Identification

* **Part ID:** `02-00-04-PRT-IT-0200`
* **Part Code:** `0200`
* **Category:** `IT`
* **Short Name:** `ServerChassis_2U`
* **Full Name:** `Server Chassis - 2U Rack Mount`

---

## 2. Classification

* **Type:** `COTS`
* **Supplier:** `ITSupplier Inc.`
* **Manufacturer:** `Dell Technologies`
* **Manufacturer P/N:** `PowerEdge R750` (example)
* **Standard Reference:** `EIA-310-D (19" rack standard)`

---

## 3. Physical Properties

### 3.1 Material

* **Primary Material:** `Steel chassis with aluminum front bezel`
* **Secondary Materials:** `Plastic cable management components`
* **Material Standard:** `Per manufacturer specifications`

### 3.2 Surface Finish

* **Finish Type:** `Powder coated steel`
* **Finish Specification:** `Black powder coat finish`
* **Protective Coating:** `Corrosion-resistant coating`

### 3.3 Mass Properties

* **Mass:** `12.5 kg` (empty chassis, per manufacturer)
* **Center of Gravity:** `Per manufacturer data (typically mid-depth, centered width)`
* **Moment of Inertia:** `Not typically critical for rack-mounted equipment`

### 3.4 Dimensions

* **Bounding Box:** `482.6 x 708.0 x 88.9 mm` (W x D x H, typical 2U server)
* **Rack Units:** `2U` (88.9mm height)
* **Critical Dimensions:** `Standard 19" rack mounting (465mm hole spacing)`
* **Mounting Points:** `Front and rear rack ears with standard EIA-310-D hole pattern`

---

## 4. Manufacturing & Procurement

### 4.1 Manufacturing Process

* **Process:** `Commercial off-the-shelf (COTS) product`
* **Special Operations:** `Factory integration of compute components`

### 4.2 Tolerances

* **General Tolerances:** `Per EIA-310-D rack standard`
* **Critical Tolerances:** `Rack mounting holes per standard`

### 4.3 Procurement

* **Lead Time:** `4-8 weeks` (typical for configured server hardware)
* **Minimum Order Quantity:** `1 unit` (standard catalog item)
* **Cost Category:** `High` (enterprise server equipment)

---

## 5. Files & Documentation

### 5.1 3D CAD Files

* Simplified envelope model can be created from manufacturer specifications
* Full detailed CAD typically not provided by manufacturer

### 5.2 2D Drawings

* `2D/02-00-04-DWG-DET-PRT-IT-0200-ServerChassis_2U-SHT01-R01.dwg` - Rack integration drawing (to be created)
* `2D/02-00-04-DWG-DET-PRT-IT-0200-ServerChassis_2U-SHT01-R01.pdf` - Integration drawing PDF (to be created)

### 5.3 Datasheets & Specifications

* `DATASHEETS/02-00-04-PRT-IT-0200_ServerChassis_2U-Datasheet-R01.pdf` - Manufacturer datasheet (to be added)
* `DATASHEETS/02-00-04-PRT-IT-0200_ServerChassis_2U-Specification-R01.pdf` - Technical specification (to be added)
* Configuration specification document detailing CPU, RAM, storage, networking

### 5.4 Certifications & Test Reports

* `CERTS/` - FCC/CE certifications from manufacturer
* Thermal and acoustic test reports if applicable

---

## 6. Usage & Integration

### 6.1 Technical Specifications (Example)

* **Form Factor:** `2U rack mount server`
* **Processor:** `Dual Intel Xeon (to be specified)`
* **Memory:** `64GB DDR4 ECC (to be specified)`
* **Storage:** `SSD configuration (to be specified)`
* **Networking:** `Dual 10GbE (to be specified)`
* **Power Supply:** `Dual redundant PSU, 1100W (to be specified)`
* **Management:** `iDRAC9 Enterprise (example)`

### 6.2 Related Assemblies

* Server rack assembly
* Data center infrastructure assemblies

### 6.3 Related BoMs

* To be determined as assemblies are developed
* Include all server configuration components

### 6.4 Related BIM Models

* To be included in data center/IT infrastructure BIM models

### 6.5 Related Drawings

* Rack elevation drawings
* Power and network connectivity diagrams
* Thermal and airflow management drawings

---

## 7. Requirements Traceability

### 7.1 Performance Requirements

* **Compute Performance:** Per application requirements
* **Storage Capacity:** Per data requirements
* **Network Throughput:** Per connectivity requirements
* **Power Consumption:** Per power budget
* **Thermal Output:** Per cooling capacity

### 7.2 Traceability

* **Requirements:** `REQ-02-001` (IT infrastructure requirements - to be confirmed)
* **ODD References:** `ODD-01` (Operational data domain - to be confirmed)
* **Safety/Hazards:** `HZ-02-0008` (IT equipment hazards - to be confirmed)

---

## 8. Maintenance & Notes

### 8.1 Special Handling

* Equipment is heavy - use proper lifting techniques or mechanical assistance
* Handle by chassis frame, not by bezel or removable components
* Ensure proper grounding before installation
* Follow manufacturer ESD precautions

### 8.2 Inspection Points

* Verify part number and configuration upon receipt
* Check for shipping damage
* Verify all ordered components are present
* Test power-on and POST before rack installation

### 8.3 Maintenance Requirements

* Regular firmware updates per manufacturer security bulletins
* Monitor system health logs via management interface
* Clean air filters per manufacturer schedule (typically quarterly)
* Verify redundant components (PSU, fans) operational
* Replace components per manufacturer recommended service life

### 8.4 Design Notes

* Ensure adequate power supply (consider redundant PSU power requirements)
* Verify thermal management - front-to-back or back-to-front airflow
* Plan cable management for power, network, and management connections
* Consider vibration isolation if mounted in mobile or industrial environment
* Verify compatibility with rack PDU and network infrastructure
* Plan for future expansion/upgrade capacity

---

## 9. Change History

| Revision | Date | Author | Description |
|----------|------|--------|-------------|
| R01 | 2025-11-17 | AMPEL360 Design Team | Initial creation - example COTS IT part |

---

## 10. Document Control

* **Status:** `WORKING` (Example part for structure demonstration)
* **Originator:** `AMPEL360 Design Team`
* **Checker:** `[To be assigned]`
* **Approver:** `[To be assigned]`
* **Last Updated:** `2025-11-17`

**Notes:**
* This is an example COTS IT hardware part created to demonstrate the PARTS directory structure
* Actual server specification must be based on detailed application and workload requirements
* Configuration details are illustrative - final specification requires IT architecture review
* Consider cybersecurity requirements and compliance needs
* AI-generated content requires human review and approval by qualified IT/systems engineer
