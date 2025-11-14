---
Title: "Assemblies — ATA 02 / Design"
Identifier: "AMPEL360-02-00-04-ASSEMBLIES-README"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Design Team"
CreatedAt: "2025-11-14"
ModifiedAt: "2025-11-14"
Abstract: "Rules and conventions for storing ATA 02 assemblies (CAD models, BOMs, DETs) and keeping exports separate."
Keywords: ["ATA 02","Design","Assemblies","BOM","STEP","DET"]
Links:
  ParentDesign: "../"
  Exports: "../EXPORTS/"
  Requirements: "../02-00-03_Requirements/02-00-03-002A_Master_Requirements.csv"
  Safety: "../02-00-02_Safety/02-00-02_Safety.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-11-14", author: "AMPEL360 Design Team", change: "Initial assembly rules and structure" }
---

# ASSEMBLIES — ATA 02 / Design

**Rule:** Keep **source models and BOMs here**. Put **renders/exports** (PNG/PDF/JT snapshots) only in `../EXPORTS/`.

This folder is the **design source** for ATA 02 assemblies (e.g. GSE, gate boxes). It is intended to be CI‑friendly: CSV for BOMs, STEP (or similar) for CAD, and small YAML DETs for meta.

---

## 1. Naming Rules

### 1.1 Assembly model files

Pattern:

```text
<XX>-<YY>-<ZZ>-A<nnn>_ASSY_<ShortName>.<ext>
```

- `XX-YY-ZZ` → lifecycle path (here: `02-00-04` for ATA 02 Design).
- `A<nnn>` → assembly index (e.g. `A310`, `A311`).
- `<ShortName>` → concise, stable English identifier.
- `<ext>` → CAD or source model extension (e.g. `step`, `prt`, `asm`, `f3d`), but **stored** here as exported neutral formats (STEP preferred).

**Examples**

- `02-00-04-A310_ASSY_GSE_Power_Cart.step`
- `02-00-04-A311_ASSY_Gate_Power_Box.step`

### 1.2 BOM files

BOMs live in:

```text
ASSEMBLIES/BOM/
```

Pattern:

```text
<AssetID>_BOM.csv
```

Where `<AssetID>` matches the assembly prefix:

- `02-00-04-A310_ASSY_GSE_Power_Cart_BOM.csv`
- `02-00-04-A311_ASSY_Gate_Power_Box_BOM.csv`

---

## 2. Minimal DET (Design Engineering Tag)

Every assembly must have a **DET block**, either:

- Appended at the **end of the BOM file** (as a YAML fenced block), or
- Stored as a separate YAML asset: `<AssetID>.det.yaml`.

### 2.1 DET schema (minimal)

```yaml
det_version: 1
asset_id: 02-00-04-A310
category: ASSY
mass_properties:
  mass_kg: null
  cg: [null, null, null]   # x,y,z (m)
  inertia_tensor: [null, null, null, null, null, null]
trace:
  reqs: ["REQ-02-001"]
  odd:  ["ODD-01"]
  safety: ["HZ-02-0007"]
checksum: "<filled-by-CI>"
status: Draft
```

**Notes**

- `asset_id` → `<XX>-<YY>-<ZZ>-A<nnn>` (no suffix).
- `category` → `ASSY` for assemblies (can later extend to `SUBASSY`, `KIT`).
- `mass_properties`:
  - Start with `null`; update from CAD or physical measurement when available.
- `trace`:
  - `reqs` → IDs from `02-00-03-002A_Master_Requirements.csv`.
  - `odd` → IDs from `02-00-01-002A_Applicability_Matrix.md`.
  - `safety` → hazard IDs (e.g. `HZ-02-0007`), consistent with the hazard log.
- `checksum`:
  - Filled by CI (e.g. hash of CAD + BOM).
- `status`: e.g. `Draft` → `Reviewed` → `Released`.

---

## 3. Structure (Recommended)

```text
02-00-04_Design/
  ASSEMBLIES/
    02-00-04-A310_ASSY_GSE_Power_Cart.step
    02-00-04-A311_ASSY_Gate_Power_Box.step
    BOM/
      02-00-04-A310_ASSY_GSE_Power_Cart_BOM.csv
      02-00-04-A311_ASSY_Gate_Power_Box_BOM.csv
    DET/
      02-00-04-A310.det.yaml
      02-00-04-A311.det.yaml
  EXPORTS/
    02-00-04-A310_ASSY_GSE_Power_Cart_EXPT_View-01.png
    02-00-04-A311_ASSY_Gate_Power_Box_EXPT_Drawing.pdf
```

- `ASSEMBLIES/` → source CAD + BOMs + DETs.
- `EXPORTS/` → **derived** artefacts only (renders, drawings, JT, PDFs).

---

## 4. Don’ts

- ❌ **Do not** store `…_EXPT_*.pdf/png/jt` in `ASSEMBLIES/`  
  → Use `../EXPORTS/` for any render, drawing, or publication export.

- ❌ **Do not** duplicate lifecycle docs inside `ASSEMBLIES/`  
  → No copies of safety/requirements/V&V documents here. Link to:
  - `../02-00-02_Safety/`
  - `../02-00-03_Requirements/`
  - `../02-00-07_V_AND_V/`

- ❌ **Do not** invent new naming patterns under `ASSEMBLIES/`  
  → Stick to `<AssetID>_ASSY_<ShortName>.<ext>` for models and `<AssetID>_BOM.csv` for BOMs.

---

## 5. Integration and Traceability

- From **requirements**:
  - Use `trace.reqs` in DET to indicate which requirements the assembly supports (e.g. `REQ-02-001` for nominal ops envelope).
- From **ODD/Applicability**:
  - Use `trace.odd` to bind the assembly to relevant ODD slice(s) (e.g. `ODD-01` for nominal Cat C/D ops).
- From **safety**:
  - Use `trace.safety` to record the hazards that this assembly addresses or contributes to (e.g. `HZ-02-0007` for GSE connection hazards).

CI can use these to:

- Check that every assembly used in a safety‑relevant context:
  - Maps to at least one requirement.
  - Has an ODD tag.
  - Appears in hazard/FMEA entries when relevant.

---

## 6. What to do next / how to approach this

1. **Normalize existing assets**
   - Rename any existing STEP/BOM files to follow:
     - `02-00-04-A3xx_ASSY_<ShortName>.*`
     - `<AssetID>_BOM.csv` under `ASSEMBLIES/BOM/`.
   - Move any renders/drawings out to `../EXPORTS/`.

2. **Add DETs for current assemblies**
   - For `02-00-04-A310` and `02-00-04-A311`:
     - Create `DET/02-00-04-A310.det.yaml` and `DET/02-00-04-A311.det.yaml` using the minimal DET template.
     - Populate `trace.reqs`, `trace.odd`, and `trace.safety` with what you already know (e.g. `REQ-02-001`, `ODD-01`).

3. **Wire to requirements & safety**
   - In `02-00-03-002A_Master_Requirements.csv`, ensure any GSE/gate‑power requirements list:
     - This assembly ID in `CrossATARefs` or `Links`.
   - In FMEA/hazard logs, reference the assembly (by `asset_id`) where relevant.

4. **Optimize the workflow**
   - Add a quick check to your design PR template:
     - “Does this PR add/change an assembly under `ASSEMBLIES/`?”
       - If yes:
         - “BOM updated?”  
         - “DET present and `trace.*` filled?”  
         - “No exports stored in `ASSEMBLIES/`?”

5. **Plan CI enhancements**
   - Simple CI steps:
     - Verify file naming patterns.
     - Validate DET YAML schema (keys + types).
     - Ensure `checksum` is present for `status: Released`.
   - Later, consider auto‑updating `checksum` based on the hash of the STEP + BOM files.
