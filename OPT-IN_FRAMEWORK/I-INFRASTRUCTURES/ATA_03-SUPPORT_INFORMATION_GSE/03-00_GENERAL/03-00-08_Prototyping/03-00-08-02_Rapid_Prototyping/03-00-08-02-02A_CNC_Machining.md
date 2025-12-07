# 03-00-08-02-02A - CNC Machining

## 1. Purpose

This document defines Computer Numerical Control (CNC) machining processes, standards, and practices for rapid prototyping within the AMPEL360-BWB-H2-Hy-E program.

## 2. Scope

This specification covers CNC milling, turning, and multi-axis machining for prototype fabrication, including materials, tooling, process planning, and quality assurance.

## 3. Applicable Documents

- ATA 03-00-08-01-01A_Prototyping_Strategy
- ATA 03-00-08-02-04A_Material_Selection
- ATA 03-00-06_Engineering
- ISO 2768 - General Tolerances
- AS9100 - Quality Management Systems

## 4. Description

### 4.1 Overview

CNC machining provides high-precision fabrication of metal and plastic prototype components with excellent dimensional control and surface finish. It is essential for functional prototypes, tooling, and production-representative parts.

### 4.2 Requirements

**CNC Machining Capabilities:**

**3-Axis Milling:**
- Applications: Plates, housings, brackets, simple geometries
- Work envelope: Up to 1000 x 500 x 500 mm
- Spindle speed: Up to 10,000 RPM
- Tolerance: ±0.05 mm

**4/5-Axis Milling:**
- Applications: Complex contours, aerospace components, impellers
- Work envelope: Up to 800 x 600 x 500 mm
- Spindle speed: Up to 15,000 RPM
- Tolerance: ±0.03 mm

**CNC Turning:**
- Applications: Shafts, bushings, rotational components
- Max diameter: Up to 300 mm
- Max length: Up to 500 mm
- Tolerance: ±0.02 mm

**Materials:**
- Aluminum alloys (6061, 7075, 2024)
- Titanium alloys (Ti-6Al-4V)
- Stainless steel (304, 316, 17-4 PH)
- Engineering plastics (PEEK, Delrin, Ultem)
- Composites (limited machining)

### 4.3 Methodology

**Process Workflow:**

1. **Design Review**
   - Manufacturability assessment
   - Tolerance analysis
   - Fixturing strategy
   - Tool path planning

2. **Programming**
   - CAM programming (Mastercam, Fusion 360, etc.)
   - Tool selection and optimization
   - Simulation and collision detection
   - G-code generation and verification

3. **Setup**
   - Material procurement and verification
   - Workholding and fixturing
   - Tool setup and offset measurement
   - First article setup

4. **Machining**
   - Rough machining operations
   - Semi-finish operations
   - Finish machining
   - In-process inspection

5. **Post-Machining**
   - Deburring and edge break
   - Surface treatment (if required)
   - Final inspection
   - Documentation

**Quality Assurance:**
- First article inspection (FAI)
- In-process dimensional checks
- CMM inspection for critical features
- Surface roughness verification
- Material certification

## 5. Deliverables

| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| CNC Process Plan | Document | Manufacturing Engineer | Per part, start - 1 week |
| CAM Program and G-code | Digital Files | CNC Programmer | Per part, start |
| Setup Sheet and Tooling List | Document | CNC Programmer | Per part, start |
| Inspection Report | Report | Quality Inspector | Per part, completion |

## 6. Quality Criteria

**Machining Quality Standards:**
- Dimensional tolerance: Per drawing or ISO 2768-m
- Surface finish: Ra 1.6 μm (standard), Ra 0.8 μm (precision)
- Edge condition: No sharp edges, 0.1-0.3 mm chamfer/radius
- Burr-free: Visual inspection, no tactile burrs

**Acceptance Criteria:**
- All critical dimensions within tolerance
- Surface finish meets specification
- No tool marks or chatter on finished surfaces
- Material certification on file
- Process documentation complete

## 7. Cross-References

- Related ATA Chapters: ATA 13 (Hardware and General Tools)
- Parent Document: 03-00-08_Prototyping
- Related Engineering Docs: 03-00-06_Engineering
- Related V&V Docs: 03-00-07_V_AND_V

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation WG | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-07.

---
