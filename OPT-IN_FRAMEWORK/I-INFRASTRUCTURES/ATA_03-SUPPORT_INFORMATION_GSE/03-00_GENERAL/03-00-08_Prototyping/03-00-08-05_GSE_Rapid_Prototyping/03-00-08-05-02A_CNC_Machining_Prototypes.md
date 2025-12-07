# 03-00-08-05-02A - CNC Machining Prototypes

## 1. Purpose
This document defines the prototype development using CNC (Computer Numerical Control) machining technologies for precision manufacturing of GSE components, providing high-accuracy parts with excellent surface finish and mechanical properties.

## 2. Scope
This prototype covers CNC machining capabilities including multi-axis milling, turning, Swiss-type machining, material selection, tooling strategies, quality control, and applications for GSE component manufacturing requiring tight tolerances.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- SAE ARP1796 (GSE Design Requirements)
- ISO 2768 (General Tolerances for Machined Parts)
- ASME Y14.5 (Geometric Dimensioning and Tolerancing)
- ISO 9001 (Quality Management Systems)
- [Reference to 03-00-06_Engineering]
- [Reference to 03-00-07_V_AND_V]

## 4. Prototype Description

### 4.1 Overview
The CNC Machining Prototypes initiative provides precision manufacturing capabilities for GSE components requiring tight tolerances, excellent surface finish, and superior mechanical properties. CNC machining is essential for critical structural parts, precision fittings, and high-performance components.

### 4.2 Design Specifications

| Parameter | Specification | Target |
|-----------|---------------|--------|
| Machine Types | Multi-axis CNC capabilities | 3, 4, and 5-axis milling/turning |
| Work Envelope | Maximum part size | 1000mm x 600mm x 500mm |
| Position Accuracy | Machine precision | ±0.005mm (±0.0002") |
| Surface Finish | Achievable Ra | 0.4-3.2 μm (Ra) |
| Material Options | Machinable materials | Metals, plastics, composites |
| Production Lead Time | Part delivery | 2-7 days typical |
| Tolerance Capability | Precision level | IT6-IT8 (ISO 286) |
| Material Properties | Strength | 100% of base material |

### 4.3 Materials and Components
- **CNC Mills**: 3, 4, and 5-axis vertical/horizontal mills
- **CNC Lathes**: Turning centers with live tooling
- **Swiss Machines**: Precision small parts production
- **Tooling**: Carbide, HSS, and diamond tools
- **Workholding**: Vises, chucks, fixtures, custom workholding
- **CAM Software**: Mastercam, Fusion 360, or equivalent
- **Measuring Equipment**: CMM, optical comparators, micrometers
- **Materials**: Aluminum alloys, stainless steel, titanium, engineering plastics

## 5. Prototype Build Plan

| Phase | Activities | Duration | Deliverables |
|-------|------------|----------|--------------|
| Design | CAD modeling, DFM analysis | 1-2 weeks | Manufacturing drawings |
| Programming | CAM programming, toolpath generation | 1 week | CNC programs |
| Setup | Fixturing, tool selection, first article | 1-2 days | Setup documentation |
| Machining | Part production, in-process inspection | 1-3 days | Machined parts |
| Inspection | Final dimensional inspection, documentation | 1 day | Inspection reports |

## 6. Testing Requirements

### 6.1 Dimensional Inspection
- **CMM Measurement**: Critical dimensions verification
- **Geometric Tolerancing**: GD&T compliance per ASME Y14.5
- **Surface Finish**: Ra/Rz measurement
- **Roundness**: For turned features
- **Flatness/Straightness**: For mating surfaces
- **Thread Inspection**: Gauge or optical inspection

### 6.2 Material Verification
- **Material Certification**: Verify material specifications
- **Hardness Testing**: Rockwell or Brinell hardness
- **Non-destructive Testing**: Dye penetrant, ultrasonic (if required)
- **Mechanical Testing**: Tensile, yield strength (sample basis)

### 6.3 Process Validation
- **First Article Inspection**: Complete dimensional verification
- **In-process Monitoring**: SPC for critical dimensions
- **Tool Life**: Monitor tool wear and replacement
- **Repeatability**: Process capability studies (Cpk)
- **Traceability**: Part serialization and records

### 6.4 Applications
- **Structural Components**: Load-bearing brackets and frames
- **Precision Fittings**: Hydraulic and pneumatic fittings
- **Couplings and Adapters**: Interface components
- **Shafts and Axles**: Rotating components
- **Valve Bodies**: Complex internal passages
- **Mounting Hardware**: Precision fasteners and bushings
- **Tooling**: Fixtures, gauges, and inspection tools

### 6.5 Materials Commonly Machined
- **Aluminum Alloys**: 6061-T6, 7075-T6 for lightweight parts
- **Stainless Steel**: 304, 316 for corrosion resistance
- **Titanium**: Ti-6Al-4V for high strength-to-weight ratio
- **Engineering Plastics**: Delrin, PEEK, UHMW for wear resistance
- **Brass/Bronze**: For electrical and bearing applications

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 03-00-06 (Engineering)
  - ATA 03-00-07 (V&V)
- Parent Document: 03-00-08_Prototyping
- Related 3D Printing: 03-00-08-05-01A_3D_Printing_GSE_Parts
- Related Composite: 03-00-08-05-03A_Composite_Prototyping
- Related Digital Twin: 03-00-08-05-04A_Digital_Twin_GSE

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation WG | Initial release |
