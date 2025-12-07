# 03-00-08-02-01A - 3D Printing Processes

## 1. Purpose

This document defines 3D printing (additive manufacturing) processes, standards, and best practices for rapid prototyping activities within the AMPEL360-BWB-H2-Hy-E program.

## 2. Scope

This specification covers various additive manufacturing technologies, materials, process parameters, quality control, and applications for prototype development.

## 3. Applicable Documents

- ATA 03-00-08-01-01A_Prototyping_Strategy
- ATA 03-00-08-02-04A_Material_Selection
- ATA 03-00-06_Engineering
- ISO/ASTM 52900 - Additive Manufacturing General Principles
- AS9100 - Quality Management Systems

## 4. Description

### 4.1 Overview

3D printing enables rapid fabrication of complex geometries for concept validation, fit checks, functional testing, and tooling. Multiple additive manufacturing technologies are employed based on part requirements and intended use.

### 4.2 Requirements

**3D Printing Technologies:**

**Fused Deposition Modeling (FDM/FFF):**
- Applications: Concept models, fit checks, non-structural prototypes
- Materials: PLA, ABS, PETG, Nylon, Carbon fiber filled
- Layer resolution: 0.1 - 0.4 mm
- Build volume: Up to 300 x 300 x 400 mm

**Stereolithography (SLA):**
- Applications: High-detail models, form validation, master patterns
- Materials: Standard, tough, flexible, high-temp resins
- Layer resolution: 0.025 - 0.1 mm
- Build volume: Up to 145 x 145 x 175 mm

**Selective Laser Sintering (SLS):**
- Applications: Functional prototypes, end-use parts, complex geometries
- Materials: Nylon (PA11, PA12), TPU, Glass-filled nylon
- Layer resolution: 0.1 - 0.15 mm
- Build volume: Up to 300 x 300 x 300 mm

**Metal 3D Printing (DMLS/SLM):**
- Applications: Metal functional prototypes, tooling, production parts
- Materials: Aluminum alloys, Titanium alloys, Stainless steel, Inconel
- Layer resolution: 0.02 - 0.1 mm
- Build volume: Up to 250 x 250 x 325 mm

### 4.3 Methodology

**Process Workflow:**

1. **Design Preparation**
   - CAD model optimization for additive manufacturing
   - Design for AM (DfAM) considerations
   - Support structure planning
   - Orientation optimization

2. **Pre-Processing**
   - STL file generation and validation
   - Slicing and path planning
   - Support generation
   - Build setup and nesting

3. **Printing**
   - Material loading and verification
   - Build initiation and monitoring
   - Environmental control (temperature, humidity)
   - Process documentation

4. **Post-Processing**
   - Support removal
   - Surface finishing (sanding, polishing, coating)
   - Heat treatment (if required)
   - Dimensional inspection

**Quality Control:**
- Material certification and traceability
- Process parameter verification
- In-process monitoring
- Dimensional inspection
- Material property testing (as required)

## 5. Deliverables

| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| 3D Printing Process Plan | Document | Manufacturing Engineer | Per prototype, start - 1 week |
| Build File Package (STL, G-code) | Digital Files | Design Engineer | Per prototype, start |
| As-Built Inspection Report | Report | Quality Inspector | Per prototype, completion |
| Material Certification | Certificate | Supplier / Material Manager | Before printing |

## 6. Quality Criteria

**Print Quality Standards:**
- Dimensional accuracy: ±0.1 mm or ±0.5% (whichever is greater)
- Surface finish: Ra 6.3 μm (with post-processing)
- Porosity: < 2% for functional parts
- Layer adhesion: No visible delamination

**Acceptance Criteria:**
- Dimensional inspection passed
- Visual inspection passed (no critical defects)
- Material certification on file
- Build documentation complete

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
