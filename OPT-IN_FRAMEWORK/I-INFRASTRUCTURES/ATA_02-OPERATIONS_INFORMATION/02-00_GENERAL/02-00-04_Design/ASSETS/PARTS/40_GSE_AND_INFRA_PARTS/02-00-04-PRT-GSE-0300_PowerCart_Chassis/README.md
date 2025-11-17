# Part: PowerCart_Chassis (02-00-04-PRT-GSE-0300)

## 1. Part Identification

* **Part ID:** `02-00-04-PRT-GSE-0300`
* **Part Code:** `0300`
* **Category:** `GSE`
* **Short Name:** `PowerCart_Chassis`
* **Full Name:** `Power Cart Chassis Frame`

---

## 2. Classification

* **Type:** `CUSTOM`
* **Supplier:** `[To be determined - fabrication shop]`
* **Manufacturer:** `[To be determined - fabrication shop]`
* **Manufacturer P/N:** `N/A (Custom design)`
* **Standard Reference:** `N/A`

---

## 3. Physical Properties

### 3.1 Material

* **Primary Material:** `Structural steel A36`
* **Secondary Materials:** `Caster mounts - steel plate`
* **Material Standard:** `ASTM A36 / ASME SA-36`

### 3.2 Surface Finish

* **Finish Type:** `Painted`
* **Finish Specification:** `RAL 7035 (Light Grey) powder coat or industrial enamel`
* **Protective Coating:** `Zinc-rich primer before topcoat for corrosion resistance`

### 3.3 Mass Properties

* **Mass:** `45.0 kg` (chassis only, estimated)
* **Center of Gravity:** `Centered horizontally, low vertical position (to be calculated from CAD)`
* **Moment of Inertia:** `To be calculated if dynamic analysis required`

### 3.4 Dimensions

* **Bounding Box:** `800 x 600 x 900 mm` (L x W x H, estimated)
* **Critical Dimensions:** 
  - Caster mounting hole pattern per caster specification
  - Equipment mounting surface flatness ±2mm
  - Ground clearance: 150mm minimum with casters
* **Mounting Points:** 
  - Four corner caster mounts
  - Top surface equipment mounting grid (M8 threaded inserts or tapped holes)

---

## 4. Manufacturing & Procurement

### 4.1 Manufacturing Process

* **Process:** `Structural steel welded fabrication`
* **Special Operations:** 
  - MIG/TIG welding per AWS D1.1
  - Grinding and finishing of welds
  - Surface preparation and painting
  - Installation of threaded inserts/hardware

### 4.2 Tolerances

* **General Tolerances:** `±3mm for structural dimensions`
* **Critical Tolerances:** 
  - Top surface flatness: ±2mm over full area
  - Caster mount hole pattern: ±0.5mm
  - Equipment mounting holes/inserts: ±1mm location
  - Overall squareness: ±2mm diagonal difference

### 4.3 Procurement

* **Lead Time:** `4-6 weeks` (estimated for custom fabrication)
* **Minimum Order Quantity:** `1 unit` (custom fabrication)
* **Cost Category:** `Medium-High` (custom welded steel structure)

---

## 5. Files & Documentation

### 5.1 3D CAD Files

* `3D/02-00-04-PRT-GSE-0300_PowerCart_Chassis.step` - Neutral STEP format (to be created)
* `3D/02-00-04-PRT-GSE-0300_PowerCart_Chassis.prt` - Native CAD format (to be created)

### 5.2 2D Drawings

* `2D/02-00-04-DWG-DET-PRT-GSE-0300-PowerCart_Chassis-SHT01-R01.dwg` - Fabrication drawing sheet 1 (to be created)
* `2D/02-00-04-DWG-DET-PRT-GSE-0300-PowerCart_Chassis-SHT02-R01.dwg` - Fabrication drawing sheet 2 (to be created)
* `2D/02-00-04-DWG-DET-PRT-GSE-0300-PowerCart_Chassis-SHT01-R01.pdf` - PDF drawings (to be created)

### 5.3 Datasheets & Specifications

* `DATASHEETS/02-00-04-PRT-GSE-0300_PowerCart_Chassis-Specification-R01.pdf` - Fabrication specification (to be created)
* Welding procedure specifications (WPS) if required

### 5.4 Certifications & Test Reports

* `CERTS/` - Material certifications (mill certs for steel)
* Weld inspection reports if required by specification
* Load testing report if required

---

## 6. Usage & Integration

### 6.1 Design Intent

* Mobile power cart chassis for ground support equipment
* Supports electrical panels, battery packs, or power distribution equipment
* Designed for industrial/airport ramp environment

### 6.2 Related Assemblies

* `02-00-04-ASSY-A310` - Complete GSE Power Cart Assembly
* Electrical panel assemblies mounted to chassis

### 6.3 Related BoMs

* GSE Power Cart complete BoM
* Includes casters, handles, electrical components

### 6.4 Related BIM Models

* To be included in GSE equipment layout models

### 6.5 Related Drawings

* Assembly drawings showing installed equipment
* Installation and mounting detail drawings

---

## 7. Requirements Traceability

### 7.1 Design Requirements

* **Load Capacity:** `500 kg` equipment load (to be verified by structural analysis)
* **Mobility:** `4-wheel caster system, 2 swivel + 2 fixed with brakes`
* **Environmental:** `Outdoor storage capable, corrosion resistant finish`
* **Safety:** `Stable under load, low center of gravity, no tip hazard`

### 7.2 Traceability

* **Requirements:** `REQ-02-001` (GSE infrastructure requirements - to be confirmed)
* **ODD References:** `ODD-01` (Ground operations - to be confirmed)
* **Safety/Hazards:** `HZ-02-0007` (GSE handling and stability hazards - to be confirmed)

---

## 8. Maintenance & Notes

### 8.1 Special Handling

* Use appropriate lifting equipment for assembly and positioning
* Do not drag - use casters for movement
* Ensure brakes are engaged when stationary
* Avoid impacts to structural members and painted surfaces

### 8.2 Inspection Points

* Verify structural welds for quality and completeness
* Check paint/coating for coverage and adhesion
* Verify flatness of mounting surfaces
* Check caster installation and operation
* Verify all mounting hardware is installed and secure

### 8.3 Maintenance Requirements

* Periodic inspection of welds and structural integrity (annually)
* Touch up paint as needed to prevent corrosion
* Lubricate and inspect casters (quarterly)
* Verify mounting hardware tightness (semi-annually)
* Check for deformation or damage after any impact

### 8.4 Design Notes

* Structure designed for static loads - not for dynamic/impact loads
* Paint system selected for outdoor industrial environment
* Caster selection must consider load capacity and floor surface
* Consider electrical bonding/grounding provisions for equipment
* Design allows for future modifications/additions
* Ergonomic considerations for push/pull handles and access

---

## 9. Change History

| Revision | Date | Author | Description |
|----------|------|--------|-------------|
| R01 | 2025-11-17 | AMPEL360 Design Team | Initial creation - example GSE custom part |

---

## 10. Document Control

* **Status:** `WORKING` (Example part for structure demonstration)
* **Originator:** `AMPEL360 Design Team`
* **Checker:** `[To be assigned - Structural Engineer]`
* **Approver:** `[To be assigned]`
* **Last Updated:** `2025-11-17`

**Notes:**
* This is an example GSE custom part created to demonstrate the PARTS directory structure
* Structural design must be verified by qualified structural engineer
* Welding must be performed by certified welders per AWS standards
* All specifications are illustrative - final design requires detailed engineering
* Consider local regulations for GSE equipment in operational environment
* AI-generated content requires human review and approval by qualified engineers
