# ASSETS/models — 3D Model Exports

**Purpose**: This folder contains static exports of 3D CAD models for ATA 53 fuselage structure, suitable for documentation, visualization, and preliminary analysis.

---

## Contents

This folder should contain exports in various formats:

- **STEP files** (`.step`, `.stp`): Neutral CAD format for cross-platform compatibility
- **IGES files** (`.iges`, `.igs`): Legacy neutral CAD format (if needed)
- **STL files** (`.stl`): Mesh format for 3D printing, rapid prototyping
- **glTF/GLB files** (`.gltf`, `.glb`): Web-friendly 3D formats for online visualization
- **PNG/JPG views** (`.png`, `.jpg`): Static rendered views (isometric, front, side, top)
- **PDF 3D** (`.pdf`): 3D PDF for interactive viewing in Adobe Reader

---

## Example Files (to be created)

| File Name | Description | Format | Status |
|:----------|:------------|:-------|:-------|
| `53-00-01-M001_Full_Fuselage_OML.step` | Outer mold line of complete fuselage | STEP | Pending |
| `53-00-01-M002_Zone_400_Center_Wing_Box.step` | Center wing box structural assembly | STEP | Pending |
| `53-00-01-M003_Frame_FR400_Detail.step` | Main landing gear attachment frame | STEP | Pending |
| `53-00-01-M004_Fuselage_Cross_Section.png` | Cross-section view at FS 5000 | PNG | Pending |
| `53-00-01-M005_Fuselage_Exploded_View.glb` | Exploded view of modular assembly | GLB | Pending |

---

## Versioning

- Model exports are linked to specific CAD model versions in PLM system
- File naming convention: `53-00-01-Mxxx_Description_vYY.ext`
  - `Mxxx`: Model asset number
  - `Description`: Short descriptive name
  - `vYY`: Version number (optional, if multiple versions exist)
  - `.ext`: File extension

---

## Usage Guidelines

- **Design Reviews**: Use STEP or glTF files for interactive visualization during reviews
- **Documentation**: Embed PNG/JPG views in documentation (requirements, reports, manuals)
- **Analysis**: Import STEP files into FEA pre-processors for geometry extraction
- **Manufacturing**: Export STEP files to manufacturing CAM systems
- **Marketing/PR**: Use high-quality rendered views for presentations and publications

---

## Source of Truth

The **master CAD models** reside in the PLM system (CATIA/Siemens NX). Files in this folder are **static exports** for convenience. Always verify version and date when using these files for critical work.

---

## Document Control

- Folder created: 2025-11-22
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
