# CAD Directory — FAN_ASSEMBLY

**Parent Assembly**: 61-00-04-A410 (FAN_ASSEMBLY)

## Directory Structure

```
CAD/
├── PRODUCTS/          # Native CAD assembly files
│   ├── CATIA/        # .CATProduct files
│   ├── SOLIDWORKS/   # .sldasm files
│   └── NX/           # .prt assembly files
├── NEUTRAL/          # Exchange formats
├── VISUALIZATION/    # Lightweight viewing formats
└── RENDERS/          # Visual documentation
```

## File Formats by Directory

| Directory | Formats | Purpose |
|-----------|---------|---------|
| PRODUCTS/CATIA | .CATProduct, .CATPart | Native CATIA V5/V6 files |
| PRODUCTS/SOLIDWORKS | .sldasm, .sldprt | Native SolidWorks files |
| PRODUCTS/NX | .prt | Native Siemens NX files |
| NEUTRAL | .step, .stp, .jt | Vendor-neutral exchange |
| VISUALIZATION | .stl, .3dpdf | Lightweight viewing |
| RENDERS | .png, .gif, .jpg | Visual documentation |

## Naming Convention

```
FAN_[COMPONENT]_ASSY.[extension]
```

### Expected Files

| File Name | Description |
|-----------|-------------|
| FAN_ASSY.* | Complete fan assembly |
| FAN_HUB_ASSY.* | Hub subassembly |
| FAN_BLADE_ASSY.* | Single blade assembly |
| FAN_SPINNER_ASSY.* | Spinner assembly |

## Export Settings

### STEP Export

- **Format**: AP242 (preferred) or AP214
- **Include**: Assembly structure, colors
- **Naming**: Same base name as source

### STL Export

- **Resolution**: Fine (chord deviation ≤ 0.01mm)
- **Format**: Binary
- **Units**: Millimeters

### 3D PDF Export

- **Include**: Assembly tree, annotations
- **Template**: AMPEL360 standard template

## Part References

Parts are linked from:

```
../../../../PARTS/
```

Ensure CAD system search paths include the PARTS directory.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
