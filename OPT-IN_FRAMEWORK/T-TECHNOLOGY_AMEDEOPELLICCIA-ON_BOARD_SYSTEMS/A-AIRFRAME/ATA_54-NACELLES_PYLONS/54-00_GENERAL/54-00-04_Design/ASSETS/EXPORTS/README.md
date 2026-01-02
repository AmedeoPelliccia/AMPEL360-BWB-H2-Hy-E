# EXPORTS — Read-Only Rendered Outputs

**Folder Purpose:** Distribution-ready rendered files (PDF/PNG) derived from source assets  
**Status:** Active  
**Last Updated:** 2026-01-02

---

## Overview

The `EXPORTS/` folder contains **rendered outputs only** — files generated from authoritative sources in the ASSETS category folders (ASSEMBLIES, DRAWINGS, MODELS, DIAGRAMS). These exports serve as:

- **Distribution packages** for design reviews and approvals
- **Archive-quality documentation** for certification and compliance
- **Presentation materials** for stakeholder communication
- **Manufacturing data packages** ready for downstream use

### Critical Principles

1. **Read-Only**: Never edit files in EXPORTS directly
2. **Source-Derived**: All exports are generated from source files
3. **Traceable**: Each export links to its authoritative source
4. **Quality-Controlled**: Strict format and resolution requirements apply

---

## Folder Structure

```
EXPORTS/
├── 00_INDEX.md                  # This comprehensive index and register
├── README.md                     # This file - usage guidelines
├── ASSEMBLIES/                   # Assembly BOMs and structure visualizations (PDF)
├── DRAWINGS/
│   ├── PDF/                     # Engineering drawings in PDF/A-1b format
│   └── PNG/                     # High-resolution raster drawings (300+ DPI)
├── MODELS/                       # Model analysis reports and visualizations
└── DIAGRAMS/                     # System diagrams and workflow exports
```

---

## Export Generation Guidelines

### Workflow Overview

1. **Update source file** in appropriate category folder (ASSEMBLIES/, DRAWINGS/, etc.)
2. **Generate export** using approved tool/script with quality settings
3. **Place export** in correct EXPORTS subfolder following naming conventions
4. **Update 00_INDEX.md** with export metadata (file, source, status, date)
5. **Track with Git LFS** if file size exceeds 1 MB
6. **Commit and push** with descriptive commit message

### Approved Export Tools

| Source Format | Tool/Method | Output Format | Notes |
|---------------|-------------|---------------|-------|
| YAML (Assembly) | `tools/render_assembly_report.py` | PDF | Generates BOM tables and metadata |
| YAML (Drawing) | CAD tool export or `tools/render_drawing.py` | PDF/A-1b, PNG | Requires drawing renderer |
| DrawIO (.drawio) | Draw.io CLI or desktop export | PDF, PNG | Use 300 DPI for PNG |
| SVG | Inkscape CLI or `svg2pdf` | PDF, PNG | Preserve dimensions |
| SysML/UML models | Model export plugin | PDF, PNG | Include diagrams and specifications |

### Manual Export Process

If automated tools are not available:

1. Open source file in appropriate authoring tool
2. Configure export settings per quality standards (see below)
3. Export to temporary location
4. Validate format and quality
5. Move to EXPORTS/ subfolder
6. Update index

---

## File Naming Conventions

### Requirement: Exact Match with Source

Export filenames **must match** the source filename exactly, differing only in:
- Extension (e.g., `.yaml` → `.pdf`, `.drawio` → `.png`)
- Optional resolution suffix for rasters (e.g., `_300dpi.png`)

### Examples

| Source File | Valid Export Name | Invalid Export Name |
|-------------|-------------------|---------------------|
| `54-00-04-D001_DRWG_Nacelle_GA.yaml` | `54-00-04-D001_DRWG_Nacelle_GA.pdf` | `Nacelle_GA.pdf` ❌ |
| `ASM-54-NAC-001_Primary_Nacelle_Structure.yaml` | `54-00-04-A001_ASSY_Nacelle_Primary_Structure.pdf` | `Primary_Nacelle.pdf` ❌ |
| `54-00-04-DG001_System_Context.drawio` | `54-00-04-DG001_System_Context.png` | `context_diagram.png` ❌ |

### Assembly Export Naming

Assemblies use the pattern `54-00-04-A###_ASSY_<Description>.pdf` where:
- `54-00-04` = ATA chapter and lifecycle folder
- `A###` = Assembly sequence number
- `ASSY` = Category identifier
- `<Description>` = Short descriptive name matching source

### Drawing Export Naming

Drawings use the pattern `54-00-04-D###_DRWG_<Description>.pdf` where:
- `D###` = Drawing number from source metadata
- `DRWG` = Category identifier
- Subfolder determines drawing type (GA, DETAIL, INTERFACE, etc.)

---

## Quality Requirements

### PDF Exports

#### PDF/A-1b Standard (ISO 19005-1)

**Required for:**
- Engineering drawings
- Assembly reports
- Certification documentation

**Settings:**
```
Format: PDF/A-1b
Color Space: sRGB (preferred) or CMYK
Fonts: All fonts embedded
Compression: Lossless for line art; JPEG quality ≥85% for images
Metadata: Include title, author, creation date
```

**Validation:**
```bash
# Verify PDF/A-1b compliance
pdfinfo <filename.pdf> | grep "PDF subtype"
# Expected output: PDF subtype:         PDF/A-1b

# Or use veraPDF for comprehensive validation
verapdf --format text <filename.pdf>
```

#### Standard PDF

Acceptable for non-archival outputs:
- Presentation materials
- Interim review packages

### PNG Exports

#### Resolution Standards

| Use Case | Minimum Resolution | Recommended Resolution | Color Depth |
|----------|-------------------|------------------------|-------------|
| Printing / Manufacturing | 300 DPI | 300-600 DPI | 24-bit RGB |
| Screen / Presentations | 150 DPI | 150-300 DPI | 24-bit RGB |
| Web / Documentation | 96 DPI | 150 DPI | 24-bit RGB |

#### Naming with Resolution

Include resolution in filename:
```
54-00-04-D001_DRWG_Nacelle_GA_300dpi.png    # For printing
54-00-04-D001_DRWG_Nacelle_GA_150dpi.png    # For screen
```

#### Validation

```bash
# Check PNG resolution
identify -format "%f: %wx%h pixels, %[resolution.x]x%[resolution.y] DPI\n" <filename.png>
```

### Assembly Reports

**Required Content:**
1. Cover page with assembly ID, title, version, status
2. Table of contents with bookmarks
3. BOM table (part numbers, descriptions, quantities, materials)
4. Assembly sequence/procedure
5. Tooling requirements
6. Quality control specifications
7. Traceability footer with source YAML path

**Format:** PDF with internal hyperlinks and navigation

---

## Git LFS Configuration

### When to Use Git LFS

Track files in EXPORTS/ with Git LFS if:
- File size > 1 MB
- Binary format (PDF, PNG)
- Frequently updated

### Setup

1. **Install Git LFS** (if not already installed):
   ```bash
   git lfs install
   ```

2. **Apply LFS tracking rules** from `.gitattributes-EXPORTS-TEMPLATE`:
   ```bash
   # In repository root
   cat OPT-IN_FRAMEWORK/.../54-00-04_Design/ASSETS/EXPORTS/.gitattributes-EXPORTS-TEMPLATE >> .gitattributes
   ```

3. **Track existing files**:
   ```bash
   git lfs track "OPT-IN_FRAMEWORK/**/ASSETS/EXPORTS/**/*.pdf"
   git lfs track "OPT-IN_FRAMEWORK/**/ASSETS/EXPORTS/**/*.png"
   ```

4. **Verify tracking**:
   ```bash
   git lfs ls-files
   ```

### Manual Override

For specific large files:
```bash
git lfs track "EXPORTS/ASSEMBLIES/54-00-04-A001_ASSY_Nacelle_Primary_Structure.pdf"
git add .gitattributes
git commit -m "Track large assembly export with LFS"
```

---

## CI/CD Integration

### Automated Export Generation

**Trigger Conditions:**
- Source file commit in ASSEMBLIES/, DRAWINGS/, MODELS/, DIAGRAMS/
- Manual workflow dispatch with export targets
- Scheduled regeneration (weekly/monthly)

**CI Workflow Steps:**
```yaml
name: Generate Exports

on:
  push:
    paths:
      - 'OPT-IN_FRAMEWORK/**/ASSETS/ASSEMBLIES/**'
      - 'OPT-IN_FRAMEWORK/**/ASSETS/DRAWINGS/**'
      - 'OPT-IN_FRAMEWORK/**/ASSETS/MODELS/**'
      - 'OPT-IN_FRAMEWORK/**/ASSETS/DIAGRAMS/**'

jobs:
  generate-exports:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          lfs: true
      
      - name: Setup Export Tools
        run: |
          pip install pyyaml jinja2 reportlab
          # Install additional tools as needed
      
      - name: Generate Assembly Exports
        run: |
          python tools/render_assembly_report.py \
            --input ASSEMBLIES/ \
            --output EXPORTS/ASSEMBLIES/
      
      - name: Generate Drawing Exports
        run: |
          python tools/render_drawings.py \
            --input DRAWINGS/ \
            --output EXPORTS/DRAWINGS/
      
      - name: Validate Export Quality
        run: |
          python tools/validate_exports.py \
            --exports EXPORTS/
      
      - name: Update Index
        run: |
          python tools/update_export_index.py \
            --index EXPORTS/00_INDEX.md
      
      - name: Commit Exports
        run: |
          git config user.name "CI Export Bot"
          git config user.email "ci@ampel360.local"
          git add EXPORTS/
          git commit -m "Auto-generated exports from source updates"
          git push
```

### Validation Checks

**Format Validation:**
```bash
# PDF/A-1b compliance
find EXPORTS/ -name "*.pdf" -exec verapdf --format text {} \;

# PNG resolution check
find EXPORTS/ -name "*.png" -exec identify -format "%f: %[resolution.x]x%[resolution.y]\n" {} \;
```

**Traceability Validation:**
```python
# Pseudo-code for traceability check
for export_file in EXPORTS:
    source_file = derive_source_path(export_file)
    if not exists(source_file):
        raise Error(f"Orphaned export: {export_file} has no source")
    if export_version != source_version:
        raise Warning(f"Version mismatch: {export_file}")
```

**Naming Convention Check:**
```bash
# Verify all exports follow naming conventions
python tools/validate_naming.py --folder EXPORTS/
```

---

## Common Operations

### Regenerate Single Export

```bash
# Example: Regenerate assembly export from updated YAML
python tools/render_assembly_report.py \
  --input ASSEMBLIES/NACELLE_ASSEMBLIES/ASM-54-NAC-001_Primary_Nacelle_Structure.yaml \
  --output EXPORTS/ASSEMBLIES/54-00-04-A001_ASSY_Nacelle_Primary_Structure.pdf \
  --format pdf
```

### Batch Regenerate All Exports

```bash
# Regenerate all exports in category
./tools/batch_export.sh --category ASSEMBLIES --format pdf
./tools/batch_export.sh --category DRAWINGS --format pdf --resolution 300
```

### Add New Export

1. Generate export from source with correct naming
2. Place in appropriate subfolder
3. Update `00_INDEX.md`:
   ```markdown
   | 54-00-04-DXXX_DRWG_NewDrawing.pdf | ../DRAWINGS/.../source.yaml | Active | 2026-01-02 |
   ```
4. Track with LFS if >1 MB
5. Commit:
   ```bash
   git add EXPORTS/DRAWINGS/PDF/54-00-04-DXXX_DRWG_NewDrawing.pdf
   git add EXPORTS/00_INDEX.md
   git commit -m "Add export for drawing DXXX"
   git push
   ```

### Remove Obsolete Export

1. Mark as "Obsolete" in `00_INDEX.md` (do not delete row)
2. Move file to archive location or delete:
   ```bash
   git rm EXPORTS/DRAWINGS/PDF/54-00-04-DXXX_DRWG_ObsoleteDrawing.pdf
   git commit -m "Remove obsolete export DXXX per ECN-####"
   git push
   ```

---

## Troubleshooting

### Export Quality Issues

**Problem:** PDF not PDF/A-1b compliant  
**Solution:** Re-export with proper settings; use veraPDF to diagnose issues

**Problem:** PNG resolution too low  
**Solution:** Re-export with `--dpi 300` flag or equivalent CAD tool setting

**Problem:** Missing fonts in PDF  
**Solution:** Ensure fonts are embedded; use PDF/A-1b profile in export tool

### Naming Mismatches

**Problem:** Export filename doesn't match source  
**Solution:** Rename export to match source exactly (except extension)

**Problem:** Multiple exports for same source  
**Solution:** Consolidate; keep only current version; update index

### Git LFS Issues

**Problem:** Large file not tracked by LFS  
**Solution:**
```bash
git lfs track "EXPORTS/**/*.pdf"
git add .gitattributes
git rm --cached <large-file>
git add <large-file>
git commit -m "Track large file with LFS"
```

**Problem:** LFS bandwidth quota exceeded  
**Solution:** Contact repo admin; consider compression or selective export

---

## Maintenance Guidelines

### Regular Review Cycle

**Quarterly:**
- Verify all exports are current with sources
- Regenerate outdated exports
- Check format compliance (PDF/A-1b, PNG resolution)
- Update `00_INDEX.md` with accurate statuses

**After Major Design Changes:**
- Regenerate affected exports immediately
- Update version numbers in index
- Notify downstream stakeholders

### Obsolescence Management

When source is marked obsolete:
1. Mark corresponding export as "Obsolete" in index
2. Add obsolescence date and reason
3. Keep export for historical reference (do not delete immediately)
4. After retention period, archive or remove per document control procedure

---

## Related Documentation

- [00_INDEX.md](./00_INDEX.md) — Comprehensive export register and traceability
- [../README.md](../README.md) — ASSETS folder overview and guidelines
- [../INDEX.meta.yaml](../INDEX.meta.yaml) — Authoritative asset catalog
- [.gitattributes-EXPORTS-TEMPLATE](./.gitattributes-EXPORTS-TEMPLATE) — Git LFS configuration
- [AMPEL360 ASSETS Standard](../../../../../../../AMPEL360_ASSETS_STANDARD.md) — Naming and structure standards

---

## Document Control

- **Version:** 1.0.0
- **Status:** Active
- **Owner:** AMPEL360 Design Documentation Team
- **Last Updated:** 2026-01-02
- **Review Cycle:** Quarterly
- **Contact:** documentation@ampel360.local

---

## Quick Reference Card

| Task | Command/Action |
|------|----------------|
| Generate assembly export | `python tools/render_assembly_report.py --input <yaml> --output <pdf>` |
| Validate PDF/A-1b | `verapdf --format text <pdf>` |
| Check PNG resolution | `identify -format "%[resolution.x]x%[resolution.y]" <png>` |
| Track with LFS | `git lfs track "EXPORTS/**/*.pdf"` |
| Update index | Edit `00_INDEX.md` with new entry |
| Verify traceability | `python tools/validate_export_traceability.py` |

---

**Remember:** EXPORTS/ is read-only. Always regenerate from source, never edit directly.
