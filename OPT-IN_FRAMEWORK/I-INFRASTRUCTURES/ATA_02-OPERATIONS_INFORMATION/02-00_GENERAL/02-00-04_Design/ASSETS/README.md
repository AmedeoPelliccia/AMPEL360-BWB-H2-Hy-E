# ASSETS — Design (ATA 02)

This subtree stores **sources** by category and **rendered** files in `EXPORTS/`.
Authoritative list is `INDEX.meta.yaml`.

## Categories

- **DIAGRAMS** - Architecture, sequence, context, data-flow diagrams (mmd, drawio, svg)
- **DRAWINGS** - Engineering drawings, dimensioned prints (dwg, dxf, pdf)
- **PRODUCTS** - Product-level models/docs (top-level items)
- **ASSEMBLIES** - Assemblies (BOM level > part)
- **PARTS** - Individual parts
- **INSTALLATIONS** - Installation layouts, mounting, routing
- **MODELS** - Logical/SysML models, JSON schemas, xmi, mdxml
- **DATA** - Lookup tables, csv/yaml configs used by design
- **TEMPLATES** - Authoring templates for this folder
- **EXPORTS** - Rendered png/pdf only (read-only outputs)

## File Naming Convention

All assets follow this standardized naming pattern:

```
<XX>-<YY>-<ZZ>-A<nnn>_<CATEGORY>_<ShortName>.<ext>
```

Where:
- `XX-YY-ZZ` = ATA chapter and folder numbers (e.g., `02-00-04`)
- `A<nnn>` = Asset ID number (e.g., `A101`, `A201`)
- `CATEGORY` = One of: `DIAG`, `DRWG`, `PROD`, `ASSY`, `PART`, `INST`, `MODL`, `DATA`, `TMPL`, `EXPT`
- `ShortName` = Descriptive name (e.g., `Context`, `Gate_Power_Layout`)
- `ext` = Appropriate file extension

### Examples

- `02-00-04-A101_DIAG_Context.mmd` → ASSETS/DIAGRAMS/
- `02-00-04-A201_DRWG_Gate_Power_Layout.pdf` → ASSETS/DRAWINGS/
- `02-00-04-A310_ASSY_GSE_Power_Cart.step` → ASSETS/ASSEMBLIES/
- `02-00-04-A401_PART_Coupler_A.step` → ASSETS/PARTS/
- `02-00-04-A510_INST_Deicing_Stand_Install.pdf` → ASSETS/INSTALLATIONS/
- `02-00-04-A601_MODL_Ops_StateMachine.mdxml` → ASSETS/MODELS/
- `02-00-04-A701_DATA_Turnaround_States.csv` → ASSETS/DATA/
- `02-00-04-A901_EXPT_Context.png` → ASSETS/EXPORTS/

## Usage Guidelines

1. **Keep sources** in their respective category folders (DIAGRAMS, DRAWINGS, etc.)
2. **Place only rendered outputs** (PDF/PNG) in EXPORTS/
3. **Update INDEX.meta.yaml** when adding new assets
4. **Link to requirements** and safety items in INDEX.meta.yaml
5. **Follow the naming convention** strictly for CI validation

## INDEX.meta.yaml

The `INDEX.meta.yaml` file is the single source of truth for all assets in this folder. Each asset entry includes:

- `id`: Unique asset identifier
- `category`: Asset category code
- `title`: Human-readable title
- `source`: Path to source file
- `exports`: List of rendered output files
- `links`: References to requirements, ODDs, safety items
- `status`: Current status (Draft, Review, Approved, etc.)
- `version`: Asset version
- `checksum`: File integrity check (filled by CI)

## CI Validation

The following rules are enforced by CI:

- Asset IDs must be unique and match pattern `^02-00-04-A\d{3}$`
- Source paths must exist and match their category folder
- Export paths must be under `ASSETS/EXPORTS/`
- All referenced requirement, ODD, and safety IDs must resolve
