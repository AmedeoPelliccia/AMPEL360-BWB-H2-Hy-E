# ASSETS — Design

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

See [AMPEL360_ASSETS_STANDARD.md](../../../../../../../AMPEL360_ASSETS_STANDARD.md) for complete specification.

## Usage Guidelines

1. **Keep sources** in their respective category folders (DIAGRAMS, DRAWINGS, etc.)
2. **Place only rendered outputs** (PDF/PNG) in EXPORTS/
3. **Update INDEX.meta.yaml** when adding new assets
4. **Link to requirements** and safety items in INDEX.meta.yaml
5. **Follow the naming convention** strictly for CI validation
