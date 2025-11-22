# Assembly Standards — ATA 53 Fuselage

## Purpose

This document defines the assembly standards applicable to all AMPEL360 BWB-H2-Hy-E fuselage assemblies. These standards ensure consistency, quality, and regulatory compliance across all assembly operations.

---

## Applicable Standards and Regulations

### Certification Specifications

- **[CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)** — Certification Specifications for Large Aeroplanes
  - CS-25.305 — Strength and Deformation
  - CS-25.307 — Proof of Structure
  - CS-25.365 — Pressurization
  - CS-25.561 — Emergency Landing Conditions
  - CS-25.562 — Emergency Landing Dynamic Conditions
  - CS-25.721 — General (Landing Gear)
  - CS-25.783 — Doors
  - CS-25.787 — Cargo Compartment Doors
  - CS-25.789 — Retention of Items of Mass

### Industry Standards

- **RTCA DO-178C** — Software Considerations in Airborne Systems (for automated assembly processes)
- **RTCA DO-254** — Design Assurance Guidance for Airborne Electronic Hardware
- **SAE ARP4754A** — Guidelines for Development of Civil Aircraft and Systems
- **SAE ARP4761** — Guidelines and Methods for Conducting the Safety Assessment Process
- **ISO 9001:2015** — Quality Management Systems
- **AS9100D** — Quality Management Systems for Aviation, Space, and Defense

### Material Standards

- **ASTM D3039** — Standard Test Method for Tensile Properties of Polymer Matrix Composite Materials
- **ASTM D7264** — Standard Test Method for Flexural Properties of Polymer Matrix Composite Materials
- **ASTM E1444** — Standard Practice for Magnetic Particle Testing
- **ASTM E2001** — Standard Guide for Resonant Ultrasound Spectroscopy for Defect Detection

---

## Assembly Process Requirements

### General Requirements

1. **Work Environment**
   - Temperature: 20°C ±3°C
   - Relative Humidity: 40-60%
   - Cleanliness: Class 100,000 (ISO 8) or better for composite assemblies
   - Lighting: Minimum 1000 lux at work surface

2. **Personnel Qualifications**
   - Composite Technicians: Minimum 2 years experience or equivalent training
   - NDT Inspectors: Level II certification per EN 4179 / NAS 410
   - Quality Engineers: AS9100 Lead Auditor certification or equivalent
   - Assembly Leads: Minimum 5 years experience in aerospace assembly

3. **Documentation**
   - All assembly steps must be documented in assembly travelers
   - Non-conformances must be reported immediately per NCR procedure
   - Quality hold points must be signed off before proceeding
   - Traceability records maintained for all materials and components

### Tooling Requirements

1. **Assembly Fixtures and Jigs**
   - Calibrated to ±0.1 mm accuracy
   - Calibration certificate valid and current
   - Storage in controlled environment when not in use
   - Preventive maintenance per PM schedule

2. **Measurement Equipment**
   - Coordinate Measuring Machines (CMM): ±0.05 mm accuracy
   - Laser trackers: ±0.05 mm accuracy over 10 m
   - Torque wrenches: Calibrated every 90 days or 5000 cycles
   - Temperature sensors: ±0.5°C accuracy

3. **NDT Equipment**
   - Ultrasonic C-scan: Calibrated per manufacturer specification
   - X-ray equipment: Annual calibration and dose monitoring
   - Eddy current: Calibrated per ASTM E1444
   - Thermography: Calibrated per ISO 18434-1

---

## Material Handling and Storage

### Composite Materials

1. **Storage Conditions**
   - Prepreg materials: -18°C ±2°C (freezer storage)
   - Adhesives: Per manufacturer specification
   - Out-time tracking: Electronic system with automatic alerts
   - First-in-first-out (FIFO) inventory management

2. **Handling Requirements**
   - Warm prepreg to room temperature before use (minimum 12 hours)
   - Track out-time and cumulative exposure
   - Protect from contamination (use clean gloves, work surfaces)
   - Record lot numbers for traceability

### Metallic Materials

1. **Storage Conditions**
   - Titanium alloys: Clean, dry storage; protect from corrosion
   - Aluminum alloys: Segregate by alloy type; prevent galvanic contact
   - Steel: Protect from moisture; apply corrosion inhibitor if required
   - Verify material certificates before use

2. **Handling Requirements**
   - Use appropriate lifting equipment for heavy parts
   - Protect finished surfaces from damage
   - Maintain traceability tags on all materials
   - Inspect for damage before use

---

## Fastener Installation Standards

### Torque Specifications

All fasteners must be torqued per the following table unless otherwise specified in assembly YAML:

| Fastener Size | Material | Torque (Nm) | Tolerance |
|---------------|----------|-------------|-----------|
| M6 | Ti-6Al-4V | 30 | ±5% |
| M8 | Ti-6Al-4V | 45 | ±5% |
| M10 | Ti-6Al-4V | 65 | ±5% |
| M10 | Steel 300M | 80 | ±3% |
| M12 | Steel 300M | 85 | ±3% |
| M14 | Steel 300M | 95 | ±3% |
| M16 | Steel 300M | 120 | ±2% |

### Fastener Installation Procedure

1. **Preparation**
   - Verify correct fastener type, size, and material
   - Inspect holes for damage, burrs, contamination
   - Apply sealant or lubricant only if specified
   - Use correct installation tools

2. **Installation**
   - Install fasteners hand-tight first
   - Torque in specified sequence (typically inside-out, alternating)
   - Use calibrated torque wrench
   - Mark fasteners after torquing per QC procedure

3. **Verification**
   - 100% torque verification on critical fasteners
   - Sample inspection (typically 10%) on non-critical fasteners
   - Document torque values in assembly traveler
   - Report any out-of-specification torques immediately

---

## Adhesive Bonding Standards

### Surface Preparation

1. **Composite Surfaces**
   - Abrade with scotch-brite (medium grade)
   - Solvent wipe with MEK or IPA
   - Verify surface energy with water break test
   - Bond within 4 hours of preparation

2. **Metallic Surfaces**
   - Abrade or grit blast per specification
   - Degrease with approved solvent
   - Apply primer if required by bond specification
   - Bond within time limit specified for primer

### Adhesive Application

1. **Mixing**
   - Verify correct adhesive type and batch number
   - Mix per manufacturer specification
   - Use mixed adhesive within pot life
   - Record mixing time and batch information

2. **Application**
   - Apply uniform thickness per specification
   - Ensure complete coverage of bond area
   - Install within open time of adhesive
   - Apply pressure and temperature per cure cycle

3. **Curing**
   - Follow specified cure cycle (time, temperature, pressure)
   - Monitor and record cure parameters
   - Do not disturb assembly during cure
   - Allow cool-down before removing from tooling

---

## Non-Destructive Testing (NDT)

### Ultrasonic Inspection

- **Method**: C-scan or pulse-echo
- **Coverage**: 100% of critical bond lines and primary structure
- **Acceptance**: No indications greater than Level 2 per internal standard ST-53-NDT-001
- **Documentation**: Record C-scan images and inspection reports

### X-Ray Inspection

- **Method**: Film or digital radiography
- **Coverage**: 100% of critical fastener clusters, welds, and metallic joints
- **Acceptance**: Per ASTM E1742 and internal standard
- **Documentation**: Retain images for record

### Visual Inspection

- **Method**: Direct visual with minimum 1000 lux lighting
- **Coverage**: 100% of all assemblies
- **Acceptance**: No visible defects (cracks, voids, delaminations, contamination)
- **Documentation**: Photographic evidence for non-conformances

---

## Quality Control Checkpoints

### In-Process Inspections

1. **First Article Inspection**
   - Conduct dimensional inspection of first assembly
   - Verify all tooling and procedures
   - Document any deviations or issues
   - Obtain approval before proceeding with production

2. **In-Process Hold Points**
   - Adhesive mixing and application
   - Fastener installation before torquing
   - NDT before cure or final assembly
   - Dimensional verification at key stages

3. **Final Inspection**
   - Complete dimensional verification per drawing
   - NDT per inspection plan
   - Fastener torque verification
   - Visual inspection for workmanship

### Acceptance Criteria

- **Dimensional**: All critical dimensions within specified tolerances
- **NDT**: No rejectable indications per inspection standard
- **Fasteners**: 100% torqued and verified
- **Workmanship**: No visible defects or non-conformances

---

## Traceability Requirements

### Material Traceability

- All materials must have lot/batch numbers recorded
- Material certificates must be verified before use
- Maintain traceability throughout assembly process
- Record material information in assembly traveler

### Process Traceability

- Document all assembly steps in traveler
- Record date, time, operator, and inspector for each step
- Maintain photographic evidence at key stages
- Store records per document retention policy (minimum 20 years)

### Component Traceability

- All components must have unique serial numbers
- Link components to parent assemblies in database
- Maintain genealogy records for life of aircraft
- Support service bulletin and airworthiness directive implementation

---

## Environmental and Safety Requirements

### Environmental Controls

- **VOC Emissions**: Comply with local regulations for solvent use
- **Waste Disposal**: Proper disposal of composite scrap, adhesives, solvents per environmental regulations
- **Energy Conservation**: Use energy-efficient equipment and processes

### Safety Requirements

- **Personal Protective Equipment (PPE)**: Safety glasses, gloves, respirators as required by material SDS
- **Fire Safety**: Flammable materials stored in approved cabinets; fire extinguishers available
- **Ergonomics**: Lifting aids, adjustable workstations, rotation of personnel for repetitive tasks
- **Hazardous Materials**: SDS available for all materials; personnel trained in handling

---

## Continuous Improvement

### Lessons Learned

- Document assembly issues and resolutions
- Conduct root cause analysis for non-conformances
- Implement corrective actions to prevent recurrence
- Share lessons learned across assembly teams

### Process Optimization

- Review assembly processes periodically for efficiency
- Implement automation where feasible and cost-effective
- Solicit feedback from assembly technicians
- Benchmark against industry best practices

---

## References

- [CS-25 Certification Specifications](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)
- Internal Standard ST-53-ASM-001: Assembly Process Requirements
- Internal Standard ST-53-NDT-001: Non-Destructive Testing Requirements
- Internal Standard ST-53-QC-001: Quality Control Procedures

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status**: DRAFT – Subject to human review and approval
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22
