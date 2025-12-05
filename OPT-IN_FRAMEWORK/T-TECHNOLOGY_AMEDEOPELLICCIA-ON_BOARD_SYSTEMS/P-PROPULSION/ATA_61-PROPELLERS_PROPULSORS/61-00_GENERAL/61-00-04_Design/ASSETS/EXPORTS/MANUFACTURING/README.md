# MANUFACTURING — Manufacturing Export Formats

This directory contains manufacturing-ready exports for production of ATA 61 propulsion system components, including CNC machining, additive manufacturing, sheet metal, and composite layup data.

## Purpose

Manufacturing exports enable:

- Direct machine programming from CAD data
- Prototype fabrication via 3D printing
- Sheet metal fabrication with flat patterns
- Composite ply layup and manufacturing
- Quality control and inspection reference

## Directory Structure

```
MANUFACTURING/
├── README.md       # This file
├── CNC/            # CNC machining data
├── 3D_PRINT/       # Additive manufacturing exports
├── SHEET_METAL/    # Sheet metal flat patterns
└── COMPOSITES/     # Composite layup data
```

## Format Specifications

### CNC (CNC/)

**Computer Numerical Control machining data**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Format               | STEP AP242 (geometry) + G-Code           |
| Tolerance            | Per drawing requirements                 |
| Coordinate System    | WCS per machining setup                  |
| Stock Definition     | Include bounding box and material        |
| Tool Paths           | Optional (machine-specific)              |
| Naming               | `Q100-61-MFG-CNC-[COMPONENT].[ext]`      |

**Included Files:**

- `*.step` - Clean machining geometry
- `*.dxf` - 2D profiles for wire EDM/laser
- `*.nc` / `*.gcode` - Machine programs (when applicable)
- `*_SETUP.pdf` - Machining setup sheet

**Use Cases:**

- Milling operations (3/5 axis)
- Turning operations
- Wire EDM
- Laser cutting

### 3D Print (3D_PRINT/)

**Additive manufacturing exports**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Format               | STL (binary), 3MF preferred              |
| Resolution           | Chord deviation ≤ 0.05 mm                |
| Units                | Millimeters                              |
| Orientation          | Optimized for build                      |
| Supports             | None (added by slicer)                   |
| Naming               | `Q100-61-MFG-3DP-[COMPONENT].[ext]`      |

**Included Files:**

- `*.stl` - Print geometry
- `*.3mf` - 3D Manufacturing Format (with metadata)
- `*_PRINT-SPEC.yaml` - Print specifications

**Print Specification Example:**

```yaml
material: AlSi10Mg
process: DMLS
layer_thickness: 0.030 mm
orientation: [0, 0, 1]
supports_required: true
post_processing:
  - stress_relief
  - machining_critical_features
```

**Use Cases:**

- Rapid prototyping
- Complex geometry production
- Tooling and fixtures
- Low-volume production parts

### Sheet Metal (SHEET_METAL/)

**Flat pattern and sheet metal fabrication data**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Format               | DXF (2D), STEP (3D folded)               |
| Bend Allowance       | Per material specification               |
| K-Factor             | Material-specific                        |
| Grain Direction      | Indicated where critical                 |
| Naming               | `Q100-61-MFG-SM-[COMPONENT].[ext]`       |

**Included Files:**

- `*_FLAT.dxf` - Flat pattern for cutting
- `*_FOLDED.step` - 3D folded geometry
- `*_BEND-TABLE.csv` - Bend sequence and angles
- `*_SPEC.yaml` - Material and process specifications

**Use Cases:**

- Brackets and mounting hardware
- Enclosures and covers
- Heat shields
- Ducting components

### Composites (COMPOSITES/)

**Composite layup and manufacturing data**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Format               | STEP (tool surface) + Layup data         |
| Ply Definition       | Material, orientation, boundaries        |
| Core Definition      | Material, thickness, locations           |
| Fiber Orientation    | Per ply, referenced to 0° datum          |
| Naming               | `Q100-61-MFG-COMP-[COMPONENT].[ext]`     |

**Included Files:**

- `*_TOOL.step` - Layup tool surface
- `*_LAYUP.csv` - Ply schedule
- `*_PLY-[nn].dxf` - Individual ply flat patterns
- `*_CORE.step` - Core geometry
- `*_SPEC.yaml` - Material and process specifications

**Ply Schedule Format:**

```csv
ply_number,material,orientation_deg,start_point,end_point,area_m2
1,UD-CFRP-T700,0,0.000,1.200,0.85
2,UD-CFRP-T700,45,0.050,1.150,0.78
3,UD-CFRP-T700,-45,0.050,1.150,0.78
4,UD-CFRP-T700,90,0.100,1.100,0.72
```

**Use Cases:**

- Fan blades
- Nacelle structures
- Inlet components
- Fairings and covers

## Naming Convention

All manufacturing exports follow:

```
Q100-61-MFG-[PROCESS]-[COMPONENT]-[VARIANT].[ext]
```

### Process Codes

| Code   | Process                |
|--------|------------------------|
| CNC    | CNC machining          |
| 3DP    | 3D printing            |
| SM     | Sheet metal            |
| COMP   | Composites             |

### Examples

```
Q100-61-MFG-CNC-GBX-HOUSING.step         → Gearbox housing machining geometry
Q100-61-MFG-3DP-FAN-BLADE-PROTO.stl      → Fan blade prototype print
Q100-61-MFG-SM-BRACKET-MNT-FLAT.dxf      → Mounting bracket flat pattern
Q100-61-MFG-COMP-FAN-BLADE-LAYUP.csv     → Fan blade ply schedule
Q100-61-MFG-COMP-FAN-BLADE-PLY-01.dxf    → Fan blade ply 1 flat pattern
```

## Export Procedures

1. **Design Freeze**: Confirm design is released for manufacturing
2. **Configuration Check**: Verify correct variant/configuration
3. **Process Selection**: Choose appropriate manufacturing process
4. **Export Generation**: Create format-specific outputs
5. **Quality Review**: Verify geometry and specifications
6. **Package Creation**: Bundle related files with manifest

## Quality Requirements

- Geometry verified against source model
- Tolerances specified per manufacturing capability
- Material specifications complete
- Process parameters documented
- Traceability to design release maintained

## Related Documentation

- [Q100-61-EXPORT-SETTINGS.yaml](../Q100-61-EXPORT-SETTINGS.yaml) - Detailed export settings
- [../README.md](../README.md) - EXPORTS overview

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
