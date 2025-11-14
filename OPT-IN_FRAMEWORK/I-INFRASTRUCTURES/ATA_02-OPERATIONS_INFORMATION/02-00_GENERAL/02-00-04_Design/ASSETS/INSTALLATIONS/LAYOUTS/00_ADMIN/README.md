# LAYOUTS — Administration

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / LAYOUTS / 00_ADMIN  
**Purpose:** Administrative files, metadata, and change tracking for installation layouts

---

## Contents

This folder contains:

- **README.md** - This file, describing the LAYOUTS structure
- **CHANGELOG.md** - Revision history of all layouts in this folder tree
- **02-00-04-LYT_Index.csv** - Master index of all layouts with metadata

---

## LAYOUTS Structure

```
LAYOUTS/
├── 00_ADMIN/                      # Administrative files (this folder)
├── 10_BASELINE_LAYOUTS/           # Baseline/reference layouts
├── 20_VARIANT_LAYOUTS/            # Design variants and options
├── 30_ZONING_AND_USE/             # Functional and security zoning
├── 40_EQUIPMENT_AND_FURNITURE/    # Equipment and furniture placement
├── 50_FLOW_LAYOUTS/               # People flow, material flow diagrams
└── 99_ARCHIVE/                    # Archived/superseded layouts
```

---

## Purpose of LAYOUTS/

**LAYOUTS/** differs from **DIAGRAMS/** and **BIM_CAD_MODELS/** in that it contains:

- **Human-readable spatial configurations** (options, zoning, seating)
- **Presentation-quality** layouts for stakeholder review
- **Conceptual arrangements** before detailed CAD/BIM work
- **Comparison studies** of different layout options
- **Non-technical formats** (PDF, PNG, PowerPoint)

Think of LAYOUTS as the **spatial planning and option study** layer, while:
- **DIAGRAMS/** = Technical system diagrams (electrical, network, P&ID)
- **BIM_CAD_MODELS/** = Detailed 3D engineering models

---

## Layout Categories

### 10_BASELINE_LAYOUTS

Reference layouts establishing the baseline design:
- Initial approved layouts
- Current operational configurations
- Standard space allocations
- Default equipment arrangements

**Use:** Starting point for all design work, basis for variants

**Formats:** `.pdf`, `.png`, `.pptx`

### 20_VARIANT_LAYOUTS

Alternative design options and variants:
- Option A, B, C comparisons
- High-density vs. resilient configurations
- Expandability options
- Cost-optimized variants

**Use:** Design option studies, stakeholder reviews, trade-off analysis

**Formats:** `.pdf`, `.png`, `.pptx`, `.xlsx` (comparison matrices)

### 30_ZONING_AND_USE

Functional and security zoning diagrams:
- Functional zones (operations, admin, support)
- Security zones (public, restricted, secure)
- Access control areas
- Work/rest area delineation
- Circulation zones

**Use:** Space planning, security design, access control planning

**Formats:** `.pdf`, `.png`, `.svg`

### 40_EQUIPMENT_AND_FURNITURE

Equipment and furniture placement layouts:
- Console arrangements
- Workstation layouts
- Server rack layouts
- Storage configurations
- Support equipment

**Use:** Detailed space planning, furniture procurement, installation planning

**Formats:** `.pdf`, `.png`, `.dwg` (if from CAD)

### 50_FLOW_LAYOUTS

People flow and material flow diagrams:
- Personnel circulation patterns
- Emergency egress routes
- Material delivery paths
- Equipment movement paths
- Visitor flow

**Use:** Ergonomics analysis, safety planning, efficiency studies

**Formats:** `.pdf`, `.png`, `.svg`

---

## File Naming Convention

All layouts follow the pattern:

```
02-00-04-LYT-<FACILITY>-<TYPE>-<DETAIL>-R<nn>.<ext>
```

Where:
- `02-00-04` = ATA chapter and design folder
- `LYT` = Layout category code
- `FACILITY` = OPSCTR (Operations Center), DATACENTER, etc.
- `TYPE` = Baseline, OptionA, FunctionalZones, ConsolesLayout, etc.
- `DETAIL` = Specific detail or level (L1, HighDensity, etc.)
- `R<nn>` = Revision number (R01, R02, etc.)
- `ext` = File extension (.pdf, .png, .pptx, etc.)

### Examples

- `02-00-04-LYT-OPSCTR-Baseline-L1-R01.pdf`
- `02-00-04-LYT-DATACENTER-Baseline-R01.pdf`
- `02-00-04-LYT-OPSCTR-OptionA-HighDensity-R01.pdf`
- `02-00-04-LYT-OPSCTR-OptionB-Resilient-R01.pdf`
- `02-00-04-LYT-OPSCTR-FunctionalZones-L1-R01.png`
- `02-00-04-LYT-OPSCTR-SecurityZones-R01.pdf`
- `02-00-04-LYT-OPSCTR-ConsolesLayout-L1-R01.pdf`
- `02-00-04-LYT-DATACENTER-RacksLayout-R01.pdf`
- `02-00-04-LYT-OPSCTR-PeopleFlow-L1-R01.png`
- `02-00-04-LYT-OPSCTR-MaterialFlow-R01.svg`

---

## Usage Guidelines

### Creating a New Layout

1. **Determine category** (baseline, variant, zoning, equipment, flow)
2. **Select appropriate folder** (10-50)
3. **Create layout** using appropriate tool (PowerPoint, Visio, CAD export, etc.)
4. **Follow naming convention** strictly
5. **Export to presentation format** (PDF or PNG for review)
6. **Update CHANGELOG.md** with revision entry
7. **Update index** in `00_ADMIN/02-00-04-LYT_Index.csv`

### Layout Standards

- **Scale:** Include graphic scale bar (not text scale)
- **North arrow:** Show orientation on all floor plan layouts
- **Legend:** Include clear legend for colors, symbols, zones
- **Title block:** Use consistent title block with facility name, date, revision
- **Annotations:** Use clear, readable annotations
- **Color coding:** Use consistent color scheme across all layouts
- **Resolution:** Minimum 150 DPI for raster images

### Variant Comparison

When creating design variants:
1. Use **consistent visual style** across all options
2. Create **side-by-side comparison** sheets
3. Document **key differences** in each variant
4. Include **pros/cons matrix** or comparison table
5. Highlight **cost implications** if known
6. Note **schedule implications** if different

### Coordination with Other Assets

Layouts must coordinate with:
- **BIM_CAD_MODELS/** - Derived from or inform 3D models
- **DIAGRAMS/** - Support and inform technical diagrams
- **Requirements/** - `02-00-03_Requirements` (space requirements)
- **Interfaces/** - `02-00-05_Interfaces` (physical interfaces)

---

## Layout Review Process

1. **Draft layout** created in appropriate category folder
2. **Internal review** by design team
3. **Revise** based on feedback (increment revision)
4. **Stakeholder review** using PDF/PNG exports
5. **Incorporate feedback** (new revision)
6. **Approval** - document in CHANGELOG.md
7. **Archive superseded** layouts to `99_ARCHIVE/`

---

## Presentation Guidelines

When preparing layouts for stakeholder presentation:

- Use **PDF format** for formal reviews
- Use **PNG format** for embedding in documents/reports
- Use **PowerPoint** for presentation packages with multiple layouts
- Include **title slide** with project context
- Add **notes pages** explaining key features of each layout
- Prepare **comparison slides** for variant options
- Include **decision matrix** if presenting multiple options

---

## Related Documentation

- [INSTALLATIONS README](../README.md)
- [BIM_CAD_MODELS README](../BIM_CAD_MODELS/00_ADMIN/README.md)
- [DIAGRAMS README](../DIAGRAMS/00_ADMIN/README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)
- Space Programming Standards - see project documentation
- Design Standards Manual - see project documentation

---

**Last Updated:** 2025-11-14  
**Owner:** AMPEL360 Space Planning Team
