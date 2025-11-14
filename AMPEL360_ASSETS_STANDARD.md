# AMPEL360 ASSETS Standard

**Version:** 1.0  
**Date:** 2025-11-14  
**Status:** ACTIVE

---

## 1. Overview

The ASSETS subtree is a **standardized, reusable structure** for organizing design artifacts, models, drawings, and data across all `XX-..-.._Design` folders in the OPT-IN Framework. It provides:

- **Consistent organization** of design artifacts by category
- **Standardized file naming** for automation and traceability
- **Authoritative catalog** via `INDEX.meta.yaml`
- **CI validation** of asset integrity and references

---

## 2. Canonical ASSETS Subtree

Every `XX-..-.._Design/` folder SHALL include an ASSETS subtree with this structure:

```
ASSETS/
├── DIAGRAMS/        # architecture, sequence, context, data-flow (mmd, drawio, svg)
├── DRAWINGS/        # engineering drawings, dimensioned prints (dwg, dxf, pdf)
├── PRODUCTS/        # product-level models/docs (top-level items)
├── ASSEMBLIES/      # assemblies (BOM level > part)
├── PARTS/           # individual parts
├── INSTALLATIONS/   # installation layouts, mounting, routing
├── MODELS/          # logical/sysml models, json schemas, xmi, mdxml
├── DATA/            # lookup tables, csv/yaml configs used by design
├── TEMPLATES/       # authoring templates for this folder
├── EXPORTS/         # rendered pdf/png exported from sources (read-only)
├── INDEX.meta.yaml  # authoritative catalog of assets in this folder
└── README.md        # usage guide for this ASSETS folder
```

### 2.1 Category Definitions

| Category | Code | Purpose | Typical Formats |
|----------|------|---------|-----------------|
| DIAGRAMS | DIAG | Architecture, sequence, context diagrams | .mmd, .drawio, .svg, .puml |
| DRAWINGS | DRWG | Engineering drawings, dimensioned prints | .dwg, .dxf, .pdf |
| PRODUCTS | PROD | Product-level models and documentation | .step, .iges, .pdf |
| ASSEMBLIES | ASSY | Assembly models (BOM level > part) | .step, .iges, .pdf |
| PARTS | PART | Individual component models | .step, .iges, .ftpr, .sldprt |
| INSTALLATIONS | INST | Installation layouts, mounting, routing | .pdf, .dwg, .dxf |
| MODELS | MODL | Logical/SysML models, schemas | .mdxml, .xmi, .json, .yaml |
| DATA | DATA | Lookup tables, configuration data | .csv, .yaml, .json |
| TEMPLATES | TMPL | Authoring templates for this folder | .md, .docx, .pptx |
| EXPORTS | EXPT | Rendered outputs (PNG, PDF) from sources | .png, .pdf |

---

## 3. File Naming Convention

All assets MUST follow this standardized naming pattern:

```
<XX>-<YY>-<ZZ>-A<nnn>_<CATEGORY>_<ShortName>.<ext>
```

### 3.1 Naming Components

- **`XX-YY-ZZ`**: ATA chapter and folder identifier
  - Example: `02-00-04` for ATA 02, subfolder 00, lifecycle stage 04 (Design)
  
- **`A<nnn>`**: Asset ID number (3 digits, zero-padded)
  - Examples: `A001`, `A101`, `A999`
  - ID ranges by category (recommended):
    - `A001-A099`: Reserved for metadata/index
    - `A100-A199`: DIAGRAMS
    - `A200-A299`: DRAWINGS
    - `A300-A399`: PRODUCTS
    - `A400-A499`: ASSEMBLIES
    - `A500-A599`: PARTS
    - `A600-A699`: INSTALLATIONS
    - `A700-A799`: MODELS
    - `A800-A899`: DATA and TEMPLATES
    - `A900-A999`: EXPORTS

- **`CATEGORY`**: One of the category codes from Section 2.1
  
- **`ShortName`**: Descriptive name in PascalCase or Snake_Case
  - Use underscores for multi-word names
  - Keep concise but meaningful
  - Examples: `Context`, `Gate_Power_Layout`, `GSE_Power_Cart`

- **`ext`**: Appropriate file extension
  - Must match the file's actual format

### 3.2 Naming Examples

```
02-00-04-A101_DIAG_Context.mmd
02-00-04-A102_DIAG_Deployment.mmd
02-00-04-A201_DRWG_Gate_Power_Layout.pdf
02-00-04-A310_ASSY_GSE_Power_Cart.step
02-00-04-A401_PART_Coupler_A.step
02-00-04-A510_INST_Deicing_Stand_Install.pdf
02-00-04-A601_MODL_Ops_StateMachine.mdxml
02-00-04-A701_DATA_Turnaround_States.csv
02-00-04-A801_TMPL_Design_Review.md
02-00-04-A901_EXPT_Context.png
```

---

## 4. INDEX.meta.yaml Structure

The `INDEX.meta.yaml` file is the **authoritative catalog** for all assets in the folder. It MUST be located at `ASSETS/INDEX.meta.yaml`.

### 4.1 Schema

```yaml
# AMPEL360 ASSETS INDEX — applies to this XX-..-.. folder only
version: 1                           # Schema version
owner: "AMPEL360 Documentation Team" # Team responsible
folder: "XX-YY-ZZ_Design"           # Folder this index applies to

assets:
  - id: "XX-YY-ZZ-Annn"             # Unique asset identifier
    category: "CATG"                 # Category code (DIAG, DRWG, etc.)
    title: "Asset Title"             # Human-readable title
    source: "ASSETS/CATEGORY/filename.ext"  # Path to source file
    exports:                         # List of rendered outputs
      - "ASSETS/EXPORTS/filename.png"
      - "ASSETS/EXPORTS/filename.pdf"
    links:                           # References to other artifacts
      reqs: ["REQ-XX-nnn", ...]     # Requirements IDs
      odd: ["ODD-nn", ...]           # ODD (Operational Design Domain) IDs
      safety: ["HZ-XX-nnnn", ...]   # Safety/Hazard IDs
    status: "Draft|Review|Approved|Obsolete"  # Asset status
    version: "1.0.0"                 # Asset version (semantic)
    checksum: "<filled-by-CI>"       # File integrity hash
```

### 4.2 Validation Rules

1. **Uniqueness**: Each `id` MUST be unique within the index
2. **ID Format**: IDs MUST match pattern `^XX-YY-ZZ-A\d{3}$` where XX-YY-ZZ matches the folder
3. **Source Path**: 
   - MUST exist in the repository
   - MUST be under `ASSETS/<CATEGORY>/`
   - Category in path must match the `category` field
4. **Export Paths**: All exports MUST be under `ASSETS/EXPORTS/`
5. **References**: All IDs in `links` section must be resolvable in their respective systems

---

## 5. ASSETS README.md

Each ASSETS folder MUST include a `README.md` file that provides:

1. **Purpose**: Brief description of the ASSETS folder for this Design stage
2. **Categories**: List of category folders and their purposes
3. **File Naming**: Reference to the naming convention
4. **Examples**: Sample file names and locations
5. **Usage Guidelines**: How to add/update assets
6. **INDEX Reference**: Pointer to INDEX.meta.yaml as source of truth
7. **CI Validation**: Brief description of automated checks

See `/OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-00_GENERAL/02-00-04_Design/ASSETS/README.md` for a reference implementation.

---

## 6. Source vs. Export Policy

### 6.1 Sources

- **Keep source files** in their respective category folders (DIAGRAMS, DRAWINGS, etc.)
- Source files are **editable** and should be version-controlled
- Examples: `.mmd`, `.drawio`, `.dwg`, `.dxf`, `.step`

### 6.2 Exports

- **Place only rendered outputs** (PNG, PDF) in the EXPORTS/ folder
- Export files are **read-only** artifacts generated from sources
- Export filenames MUST use `_EXPT_` category code
- Exports should be **regenerated** whenever sources change

### 6.3 Workflow

```
Source File (DIAGRAMS/A101_DIAG_Context.mmd)
    ↓ [Render/Export]
Export File (EXPORTS/A901_EXPT_Context.png)
    ↓ [Reference in docs]
Documentation (README.md, SAD, etc.)
```

---

## 7. CI/CD Integration

### 7.1 Automated Checks

CI pipelines SHALL validate:

1. **INDEX Validity**:
   - INDEX.meta.yaml parses correctly
   - All required fields present
   - ID format matches folder pattern

2. **File Existence**:
   - All `source` paths exist
   - All `exports` paths exist or are flagged as pending

3. **Category Consistency**:
   - Source file location matches its category
   - Category code matches folder name

4. **Reference Resolution**:
   - All requirement IDs exist in requirements database
   - All ODD IDs exist in ODD registry
   - All safety IDs exist in safety/hazard logs

5. **Checksum Updates**:
   - Generate checksums for source files
   - Update INDEX.meta.yaml with computed values

### 7.2 Automated Actions

- **On Source Change**: Flag exports as stale, require regeneration
- **On INDEX Update**: Validate all fields, check for conflicts
- **On PR**: Generate diff showing added/modified/removed assets

---

## 8. Migration and Rollout

### 8.1 Existing Folders

For existing `XX-..-.._Design` folders without ASSETS structure:

1. Create ASSETS folder structure
2. Move existing assets to appropriate categories
3. Rename files to follow naming convention
4. Create INDEX.meta.yaml catalog
5. Add ASSETS README.md
6. Update references in documentation

### 8.2 New Folders

For new `XX-..-.._Design` folders:

1. Copy ASSETS structure from template
2. Customize INDEX.meta.yaml header (version, owner, folder name)
3. Update ASSETS README.md with folder-specific information
4. Begin adding assets following the standard

---

## 9. Usage Examples

### 9.1 Adding a New Diagram

1. Create source file: `ASSETS/DIAGRAMS/02-00-04-A103_DIAG_NewDiagram.mmd`
2. Add entry to INDEX.meta.yaml:
   ```yaml
   - id: "02-00-04-A103"
     category: "DIAG"
     title: "New Diagram"
     source: "ASSETS/DIAGRAMS/02-00-04-A103_DIAG_NewDiagram.mmd"
     exports:
       - "ASSETS/EXPORTS/02-00-04-A903_EXPT_NewDiagram.png"
     links:
       reqs: ["REQ-02-XXX"]
       odd: []
       safety: []
     status: "Draft"
     version: "1.0.0"
     checksum: "<filled-by-CI>"
   ```
3. Generate export: Convert .mmd to PNG and place in EXPORTS/
4. Commit changes

### 9.2 Referencing Assets in Documentation

In design documents, reference assets using relative paths:

```markdown
See the operational context diagram in [ASSETS/DIAGRAMS/02-00-04-A101_DIAG_Context.mmd](ASSETS/DIAGRAMS/02-00-04-A101_DIAG_Context.mmd).

![Context Diagram](ASSETS/EXPORTS/02-00-04-A901_EXPT_Context.png)
```

Or reference by ID:

```markdown
The deployment architecture (Asset ID: 02-00-04-A102) shows...
```

---

## 10. Benefits

1. **Consistency**: Same structure across all Design folders
2. **Discoverability**: Easy to find assets by category or ID
3. **Traceability**: Links to requirements and safety items
4. **Automation**: CI can validate and process assets
5. **Reusability**: Templates and standards can be shared
6. **Maintainability**: Clear ownership and version control
7. **Scalability**: Works for small and large projects

---

## 11. Related Standards

- [AMPEL360_DOCUMENTATION_STANDARD.md](AMPEL360_DOCUMENTATION_STANDARD.md) - Overall documentation structure
- [OPT-IN_FRAMEWORK_STANDARD.md](OPT-IN_FRAMEWORK_STANDARD.md) - OPT-IN Framework requirements
- [ATA_03_NUMBERING_GUIDE.md](ATA_03_NUMBERING_GUIDE.md) - ATA numbering conventions

---

## 12. Governance

### 12.1 Standard Owner

**AMPEL360 Documentation Working Group**

### 12.2 Change Control

Changes to this standard require:
- Review by Documentation WG
- Approval from Technical Lead
- Impact assessment for existing folders
- Migration plan if breaking changes

### 12.3 Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025-11-14 | Initial standard | AMPEL360 Team |

---

## Appendix A: JSON Schema for INDEX.meta.yaml

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AMPEL360 ASSETS Index",
  "type": "object",
  "required": ["version", "owner", "folder", "assets"],
  "properties": {
    "version": {
      "type": "integer",
      "minimum": 1,
      "description": "Schema version"
    },
    "owner": {
      "type": "string",
      "description": "Team or person responsible for these assets"
    },
    "folder": {
      "type": "string",
      "pattern": "^\\d{2}-\\d{2}-\\d{2}_Design$",
      "description": "Folder identifier (e.g., '02-00-04_Design')"
    },
    "assets": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "category", "title", "source", "status", "version"],
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^\\d{2}-\\d{2}-\\d{2}-A\\d{3}$",
            "description": "Unique asset identifier"
          },
          "category": {
            "type": "string",
            "enum": ["DIAG", "DRWG", "PROD", "ASSY", "PART", "INST", "MODL", "DATA", "TMPL", "EXPT"],
            "description": "Asset category code"
          },
          "title": {
            "type": "string",
            "minLength": 1,
            "description": "Human-readable asset title"
          },
          "source": {
            "type": "string",
            "pattern": "^ASSETS/[A-Z]+/.*",
            "description": "Relative path to source file"
          },
          "exports": {
            "type": "array",
            "items": {
              "type": "string",
              "pattern": "^ASSETS/EXPORTS/.*"
            },
            "description": "List of export file paths"
          },
          "links": {
            "type": "object",
            "properties": {
              "reqs": {
                "type": "array",
                "items": {"type": "string"}
              },
              "odd": {
                "type": "array",
                "items": {"type": "string"}
              },
              "safety": {
                "type": "array",
                "items": {"type": "string"}
              }
            }
          },
          "status": {
            "type": "string",
            "enum": ["Draft", "Review", "Approved", "Obsolete"],
            "description": "Current status of the asset"
          },
          "version": {
            "type": "string",
            "pattern": "^\\d+\\.\\d+\\.\\d+$",
            "description": "Semantic version"
          },
          "checksum": {
            "type": "string",
            "description": "File integrity hash (filled by CI)"
          }
        }
      }
    }
  }
}
```

---

## Appendix B: Quick Reference Card

### File Naming Pattern
```
XX-YY-ZZ-Annn_CATEGORY_ShortName.ext
```

### Category Codes
| Code | Folder |
|------|--------|
| DIAG | DIAGRAMS |
| DRWG | DRAWINGS |
| PROD | PRODUCTS |
| ASSY | ASSEMBLIES |
| PART | PARTS |
| INST | INSTALLATIONS |
| MODL | MODELS |
| DATA | DATA |
| TMPL | TEMPLATES |
| EXPT | EXPORTS |

### ID Ranges (Recommended)
- A100-199: Diagrams
- A200-299: Drawings
- A300-399: Products
- A400-499: Assemblies
- A500-599: Parts
- A600-699: Installations
- A700-799: Models
- A800-899: Data/Templates
- A900-999: Exports

---

**End of Standard**
