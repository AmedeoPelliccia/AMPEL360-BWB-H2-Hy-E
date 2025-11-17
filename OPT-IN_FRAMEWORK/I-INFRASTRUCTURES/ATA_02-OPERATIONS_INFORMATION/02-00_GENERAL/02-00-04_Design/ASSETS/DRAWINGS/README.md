---
Title: "Drawings & Exports — ATA 02 / Design"
Identifier: "AMPEL360-02-00-04-ASSETS-DRAWINGS"
Version: "2.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Design Team"
CreatedAt: "2025-11-14"
ModifiedAt: "2025-11-17"
Abstract: "Conventions for storing 2D design drawings (sheet-type deliverables) and graphical exports for ATA 02 design."
Keywords: ["ATA 02","Design","Drawings","Exports","Views","GA","Equipment","Details"]
Links:
  ParentDesign: "../.."
  Assemblies: "../ASSEMBLIES/README.md"
  BIM_CAD_Models: "../INSTALLATIONS/BIM_CAD_MODELS/README.md"
  Requirements: "../../02-00-03_Requirements/02-00-03-002A_Master_Requirements.csv"
  Safety: "../../02-00-02_Safety/02-00-02_Safety.md"
ChangeLog:
  - { version: "2.0.0", date: "2025-11-17", author: "AMPEL360 Design Team", change: "Added comprehensive 2D drawings structure with subdirectories and governance" }
  - { version: "1.0.0", date: "2025-11-14", author: "AMPEL360 Design Team", change: "Initial drawings/exports rules" }
---

# DRAWINGS — 2D Design Drawings (ATA 02-00-04)

This folder holds **2D design drawings** (classical sheet-type deliverables) for 
**ATA 02-00-04_Design** (Operations Information infrastructures). 

## Overview

This directory now contains two types of drawing content:

1. **Formal 2D design drawings** (in organized subdirectories) — sheet-type deliverables
   including general arrangements, equipment assemblies, details, interfaces, and as-built drawings
2. **Assembly-derived exports** (loose files in root, legacy) — lightweight exports and views
   derived from assembly models

**See `00_ADMIN/README.md` for complete documentation of the 2D drawings structure.**

Source assets live in:

- BIM Models: `../INSTALLATIONS/BIM_CAD_MODELS/`
- Assembly Models & DETs: `../ASSEMBLIES/`
- BOMs: `../ASSEMBLIES/BOM/`

---

## 1. Directory Structure

```text
DRAWINGS/
├── 00_ADMIN/               # Governance, index, change log
├── 05_TEMPLATES/           # Title blocks, frames, standard drawing templates
├── 10_GENERAL_ARRANGEMENTS/# Overall layouts (GA)
├── 20_EQUIPMENT_AND_GSE/   # Equipment and GSE general assemblies
├── 30_SECTIONS_AND_DETAILS/# Sections and detailed construction drawings
├── 40_INTERFACE_DRAWINGS/  # Interface drawings (MEP/IT/structure/building)
├── 50_AS_BUILT/            # As-built drawings
└── 99_ARCHIVE/             # Superseded / archived drawings
```

**→ See `00_ADMIN/README.md` for complete documentation**

---

## 2. Scope

### 2.1 Formal 2D Design Drawings (in subdirectories)

- General arrangements (GA) — overall layouts and spatial organization
- Equipment drawings (EQP) — equipment and GSE assemblies
- Sections and details (DET) — construction details and sections
- Interface drawings (INT) — discipline coordination and interfaces
- As-built drawings (ASB) — final installed configuration
- Drawing templates and standards

### 2.2 Assembly-Derived Exports (legacy, may be in root)

- 2D mechanical drawings (e.g. PDF, DWG if needed as export, DXF)
- Lightweight viewables (e.g. PNG, JPG, SVG, JT, 3D PDF)
- Marked-up review snapshots or redlines **derived from** assemblies

Not allowed:

- Native CAD source models (`*.prt`, `*.sldprt`, `*.f3d`, etc.)
- Authoritative BOMs or DET YAMLs
- Lifecycle docs (safety, requirements, procedures)

---

## 2. Naming Pattern

Exports must be clearly tied to their **assembly asset_id**.

### 2.1 General form

```text
<AssetID>_EXPT_<ViewName>.<ext>
```

Where:

- `<AssetID>` → matches assembly ID (e.g. `02-00-04-A310`).
- `_EXPT_` → fixed marker for “export”.
- `<ViewName>` → short, stable name:
  - `Drawing`
  - `Overall_View`
  - `Section_A-A`
  - `Install_Guide`
- `<ext>` → `pdf`, `png`, `svg`, `jt`, etc.

### 2.2 Examples

- `02-00-04-A310_EXPT_Drawing.pdf`
- `02-00-04-A310_EXPT_Overall_View.png`
- `02-00-04-A311_EXPT_Drawing.pdf`
- `02-00-04-A311_EXPT_Section_A-A.svg`

If multiple revisions are exported, keep versioning either:

- In the document metadata (preferred), or
- As suffix: `…_v01`, `…_v02` only when necessary, e.g.:
  - `02-00-04-A310_EXPT_Drawing_v01.pdf`

---

## 3. Relationship to Assemblies & DET

Each export should be traceable back to:

- **Assembly model** in `../ASSEMBLIES/`
  - e.g. `02-00-04-A310_ASSY_GSE_Power_Cart.step`
- **BOM** in `../ASSEMBLIES/BOM/`
  - e.g. `02-00-04-A310_ASSY_GSE_Power_Cart_BOM.csv`
- **DET** in `../ASSEMBLIES/DET/`
  - e.g. `02-00-04-A310.det.yaml`

Recommended:

- Include `AssetID` inside the drawing title block or export metadata.
- Optionally list key requirement IDs (e.g. `REQ-02-001`) in the drawing notes.

---

## 4. Don’ts

- ❌ Do **not** store:
  - `*_ASSY_*.step` or any native CAD here.
  - `*_BOM.csv` or DET YAMLs.
- ❌ Do **not** invent new duplicate “source” folders under `ASSETS/DRAWINGS`.
- ❌ Do **not** use exports as the **only** location of design intent:
  - The source of truth remains in `ASSEMBLIES/` (models + BOM + DET).

---

## 5. How this ties into workflows

- **Design change**:
  - Update model/BOM/DET in `ASSEMBLIES/`.
  - Regenerate exports here as needed (drawing PDFs, views).
- **Safety / Requirements reviews**:
  - Reference exports for visualization, but bind arguments to:
    - Requirements (`REQ-02-###` in the master CSV).
    - Assembly IDs and DET trace fields.

---

## 6. What to do next / how to approach this

1. **Create subfolders if needed**
   - e.g.:
     - `DRAWINGS/MECH/`
     - `DRAWINGS/ELECT/`
     - `DRAWINGS/REVIEWS/`
   - Keep the same naming rules in all subfolders.

2. **Normalize existing exports**
   - Rename any existing files to match `<AssetID>_EXPT_<ViewName>.<ext>`.
   - Move any source models or BOMs found here back into `../ASSEMBLIES/`.

3. **Wire into PR/CI workflows**
   - In design PR templates:
     - “If exports changed, did the underlying assembly/BOM/DET also change?”
   - In CI (later):
     - Optionally verify that every `*_EXPT_*` file refers to an existing `<AssetID>` with a DET in `../ASSEMBLIES/DET/`.

4. **Extend later**
   - Add lightweight metadata (e.g. a small YAML index per asset) if you want to catalog exports for publications or operator manuals.
