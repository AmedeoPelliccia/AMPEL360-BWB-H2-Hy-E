# ASSETS Directory

**Purpose**: Design artifacts, diagrams, data files, and configurations for this energy subsystem.

## Structure

Per [AMPEL360_ASSETS_STANDARD.md](../../../../../../AMPEL360_ASSETS_STANDARD.md):

```
ASSETS/
├── DIAGRAMS/        # .drawio, .mmd, .svg
├── DRAWINGS/        # .dwg, .dxf, .pdf
├── MODELS/          # .json, .yaml schemas
├── DATA/            # .csv, .yaml data files
├── TEMPLATES/       # Document templates
└── EXPORTS/         # Rendered outputs
```

## Naming Convention

`<XX>-<YY>-<ZZ>-A<nnn>_<CATEGORY>_<Description>.<ext>`

Example: `95-80-24-A101_DIAG_Electrical_SingleLine.drawio`

## Asset Index

See individual `INDEX.meta.yaml` file (when created) for authoritative catalog of all assets in this folder.

## Placeholder Assets

The following assets are referenced in documentation but not yet created:
- Diagrams (.drawio files)
- Data tables (.csv files)
- Configuration schemas (.json, .yaml files)
- Specifications (.md files)

These should be created during detailed design phase.

---

**Document Control**
- **Standard**: AMPEL360_ASSETS_STANDARD v1.0
- **Owner**: AMPEL360 Energy WG
