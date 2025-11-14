# TEMPLATES — Administration

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / TEMPLATES / 00_ADMIN  
**Purpose:** Administrative files, metadata, and change tracking for installation templates

---

## Contents

This folder contains:

- **README.md** - This file, describing the TEMPLATES structure
- **CHANGELOG.md** - Revision history of all templates in this folder tree
- **02-00-04-TPL_Index.csv** - Master index of all templates with metadata

---

## TEMPLATES Structure

```
TEMPLATES/
├── 00_ADMIN/                      # Administrative files (this folder)
├── 10_BIM_CAD/                    # BIM/CAD model templates
├── 20_DIAGRAMS/                   # Diagram templates
├── 30_LAYOUTS/                    # Layout presentation templates
├── 40_PROCEDURES/                 # Procedure document templates
├── 50_CHECKLISTS_FORMS/           # Checklist and form templates
├── 60_LEGENDS_AND_STANDARDS/      # Legends, symbols, naming standards
└── 99_ARCHIVE/                    # Archived/superseded templates
```

---

## Purpose of TEMPLATES/

**TEMPLATES/** serves as the **central template library** for all INSTALLATIONS assets. It provides:

- **Consistency** - Standardized starting points for all asset creation
- **Efficiency** - Reduces setup time for new assets
- **Quality** - Ensures best practices are baked into templates
- **Standards compliance** - Enforces naming, formatting, and content standards

Think of this as the "master mold" that feeds all other INSTALLATIONS folders:
- **BIM_CAD_MODELS/** uses templates from `10_BIM_CAD/`
- **DIAGRAMS/** uses templates from `20_DIAGRAMS/`
- **LAYOUTS/** uses templates from `30_LAYOUTS/`
- **PROCEDURES/** uses templates from `40_PROCEDURES/`

---

## Template Categories

### 10_BIM_CAD

BIM/CAD modeling templates:
- Generic room/space templates
- Operations center console module templates
- Data center rack row templates
- Shared parameter files (Revit)
- Family templates (Revit)
- Block libraries (AutoCAD)

**Purpose:** Consistent BIM/CAD modeling across all disciplines

**Formats:** `.rvt`, `.rft`, `.dwt`, `.dwg`

**Examples:**
- `02-00-04-TPL-BIM-GenericRoom-LOD200-R01.rvt`
- `02-00-04-TPL-BIM-OPSCTR-ConsoleModule-R01.rvt`
- `02-00-04-TPL-BIM-DATACENTER-RackRow-R01.rvt`

### 20_DIAGRAMS

Diagram drawing templates:
- Installation layout template (AutoCAD)
- Power single-line diagram template
- Network topology template (Visio)
- P&ID template
- Information flow diagram template

**Purpose:** Consistent diagram formatting and symbols

**Formats:** `.dwt`, `.dwg`, `.vsdx`, `.drawio`

**Examples:**
- `02-00-04-TPL-DGM-InstallationLayout-R01.dwg`
- `02-00-04-TPL-DGM-PowerSingleLine-R01.dwg`
- `02-00-04-TPL-DGM-NetworkTopology-R01.vsdx`

### 30_LAYOUTS

Layout presentation templates:
- Baseline layout template (PowerPoint)
- Option comparison template (Excel)
- Review package template (Word)
- Zoning diagram template
- Equipment layout template

**Purpose:** Consistent presentation of layout options

**Formats:** `.pptx`, `.xlsx`, `.docx`, `.vsdx`

**Examples:**
- `02-00-04-TPL-LYT-BaselineLayout-R01.pptx`
- `02-00-04-TPL-LYT-OptionComparison-R01.xlsx`
- `02-00-04-TPL-LYT-ReviewPackage-R01.docx`

### 40_PROCEDURES

Procedure document templates:
- Installation procedure template
- Commissioning procedure template
- Operation procedure template
- Maintenance procedure template
- Emergency procedure template

**Purpose:** Standardized procedure structure and format

**Formats:** `.md`, `.docx`, `.pdf`

**Examples:**
- `02-00-04-TPL-PRC-Installation-R01.md`
- `02-00-04-TPL-PRC-Commissioning-R01.md`
- `02-00-04-TPL-PRC-Operation-R01.md`
- `02-00-04-TPL-PRC-Maintenance-R01.md`

### 50_CHECKLISTS_FORMS

Checklist and form templates:
- Commissioning checklist template
- Maintenance log template
- Pre-startup checklist template
- Inspection form template
- Test record template

**Purpose:** Standardized data collection and verification

**Formats:** `.xlsx`, `.docx`, `.pdf`

**Examples:**
- `02-00-04-TPL-CHK-CommissioningChecklist-R01.xlsx`
- `02-00-04-TPL-CHK-MaintenanceLog-R01.xlsx`
- `02-00-04-TPL-CHK-PreStartupChecklist-R01.xlsx`

### 60_LEGENDS_AND_STANDARDS

Legends, symbols, and naming standards:
- Symbol legend for diagrams
- BIM naming rules and conventions
- Layer naming standard (DWG)
- Color coding standards
- Line weight standards
- Font standards

**Purpose:** Ensure consistent use of symbols, names, and conventions

**Formats:** `.pdf`, `.md`, `.dwg`, `.xlsx`

**Examples:**
- `02-00-04-TPL-STD-SymbolLegend-Diagrams-R01.pdf`
- `02-00-04-TPL-STD-BIM_NamingRules-R01.md`
- `02-00-04-TPL-STD-LayerNaming-DWG-R01.md`

---

## File Naming Convention

All templates follow the pattern:

```
02-00-04-TPL-<TYPE>-<DESCRIPTION>-R<nn>.<ext>
```

Where:
- `02-00-04` = ATA chapter and design folder
- `TPL` = Template category code
- `TYPE` = BIM (BIM/CAD), DGM (Diagram), LYT (Layout), PRC (Procedure), CHK (Checklist), STD (Standard)
- `DESCRIPTION` = Descriptive name of template
- `R<nn>` = Revision number (R01, R02, etc.)
- `ext` = File extension (native format of the template)

---

## Usage Guidelines

### Using a Template

1. **Locate appropriate template** in category folders (10-60)
2. **Copy template** to your working folder (BIM_CAD_MODELS, DIAGRAMS, LAYOUTS, or PROCEDURES)
3. **Rename** following the target folder's naming convention
4. **Customize** content for your specific use case
5. **Do NOT modify** the original template file

### Creating a New Template

1. **Identify need** - Recurring asset type that would benefit from standardization
2. **Create template** with best practices and standards embedded
3. **Select appropriate category** folder (10-60)
4. **Follow naming convention** for templates
5. **Document usage** in template (embedded instructions or readme)
6. **Review with team** - Ensure template meets standards
7. **Test template** - Have someone else use it to verify clarity
8. **Update index** in `00_ADMIN/02-00-04-TPL_Index.csv`
9. **Update CHANGELOG.md** with new template entry

### Template Standards

Templates should include:

**BIM/CAD Templates:**
- Correct units and scales
- Standard layers/levels defined
- Shared parameters loaded (if Revit)
- View templates configured
- Title block with metadata fields

**Diagram Templates:**
- Standard title block
- Symbol library loaded
- Layers configured with standard names/colors
- Viewport/layout configured
- Standard text styles

**Layout Templates:**
- Company/project branding
- Standard slide layouts (PowerPoint)
- Placeholder text and images
- Consistent fonts and colors
- Metadata fields (title, date, revision, etc.)

**Procedure Templates:**
- Standard sections (Purpose, Scope, Prerequisites, etc.)
- Safety warning formatting examples
- Step numbering style
- Table of contents structure
- Revision history table

**Checklist Templates:**
- Standard header with metadata
- Checkbox/status column
- Comments/notes column
- Sign-off section
- Conditional formatting (if Excel)

**Legend/Standards:**
- Clear symbol definitions
- Examples of correct usage
- Notes on when to use each element
- Cross-references to related standards

---

## Template Maintenance

### Version Control

- Templates are **versioned** (R01, R02, etc.)
- Major changes increment revision number
- Document all changes in CHANGELOG.md
- Archive previous versions to `99_ARCHIVE/`

### Review Cycle

Templates should be reviewed:
- **Annually** - Regular scheduled review
- **After major project** - Incorporate lessons learned
- **When standards change** - Update to match new standards
- **When users request** - Address user feedback

### Deprecation

When a template is superseded:
1. Move old template to `99_ARCHIVE/`
2. Add deprecation notice in CHANGELOG.md
3. Update index to note deprecation
4. Communicate change to users
5. Provide migration guide if needed

---

## Template Library Management

### Centralized Control

- **Single source of truth** - This folder is the authoritative source
- **No local copies** - Users should always pull from this folder
- **Change control** - Template updates go through review process
- **Communication** - Notify users of template updates

### Template Discovery

Templates are discoverable through:
1. **This README** - Overview of available templates
2. **Index file** - `00_ADMIN/02-00-04-TPL_Index.csv` with searchable metadata
3. **Folder structure** - Organized by type for easy browsing
4. **Naming convention** - Self-describing file names

---

## Quality Standards

Templates must meet these quality standards:

✅ **Complete** - Contains all necessary elements and instructions
✅ **Correct** - Follows all applicable standards and best practices
✅ **Clear** - Easy to understand and use without extensive training
✅ **Consistent** - Matches other templates in style and structure
✅ **Current** - Up-to-date with latest standards and requirements
✅ **Tested** - Verified to work as intended

---

## Related Documentation

- [INSTALLATIONS README](../README.md)
- [BIM_CAD_MODELS README](../BIM_CAD_MODELS/00_ADMIN/README.md)
- [DIAGRAMS README](../DIAGRAMS/00_ADMIN/README.md)
- [LAYOUTS README](../LAYOUTS/00_ADMIN/README.md)
- [PROCEDURES README](../PROCEDURES/00_ADMIN/README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)
- Company CAD Standards - see project documentation
- Company BIM Standards - see project documentation

---

**Last Updated:** 2025-11-14  
**Owner:** AMPEL360 Standards & Templates Team
