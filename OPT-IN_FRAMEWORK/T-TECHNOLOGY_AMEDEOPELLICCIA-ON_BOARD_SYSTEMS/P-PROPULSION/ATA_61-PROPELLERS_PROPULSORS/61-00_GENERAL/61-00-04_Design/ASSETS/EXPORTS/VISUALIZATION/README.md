# VISUALIZATION — Visualization Export Formats

This directory contains visualization exports for design review, stakeholder communication, and web-based viewing of ATA 61 propulsion system components.

## Purpose

Visualization exports enable:

- Interactive 3D review without CAD software
- Web-based model viewing
- Technical presentations and reports
- Stakeholder communications
- Marketing and documentation imagery

## Directory Structure

```
VISUALIZATION/
├── README.md       # This file
├── 3DPDF/          # 3D PDF for interactive review
├── GLTF/           # glTF/GLB for web viewing
├── STL/            # STL mesh exports
│   ├── HIGH_RES/   # High resolution for visualization
│   └── LOW_RES/    # Low resolution for quick view
└── OBJ/            # OBJ for general 3D applications
```

## Format Specifications

### 3D PDF (3DPDF/)

**Interactive PDF for design review**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Standard             | PDF/A-3 with 3D artwork                  |
| 3D Format            | PRC (Product Representation Compact)     |
| Quality              | High (tessellation ≤ 0.05 mm chord)      |
| Views                | Include predefined views                 |
| Annotations          | Include PMI where available              |
| Naming               | `Q100-61-VIS-[COMPONENT]-[VARIANT].pdf`  |

**Use Cases:**

- Design review meetings
- Customer presentations
- Certification documentation
- Archival with interactive content

### glTF/GLB (GLTF/)

**Web-optimized 3D format**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Version              | glTF 2.0                                 |
| Container            | GLB (binary) preferred                   |
| Compression          | Draco mesh compression when appropriate  |
| Materials            | PBR metallic-roughness workflow          |
| Textures             | WebP or JPEG (quality ≥ 85%)             |
| Naming               | `Q100-61-VIS-[COMPONENT]-[VARIANT].glb`  |

**Use Cases:**

- Web-based 3D viewers
- Digital twin visualization
- AR/VR applications
- Technical documentation portals

### STL (STL/)

**Triangulated mesh exports**

#### High Resolution (STL/HIGH_RES/)

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Format               | Binary STL                               |
| Chord Deviation      | ≤ 0.01 mm                                |
| Angular Deviation    | ≤ 5°                                     |
| Units                | Millimeters                              |
| Naming               | `Q100-61-VIS-[COMPONENT]-HI.[ext]`       |

#### Low Resolution (STL/LOW_RES/)

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Format               | Binary STL                               |
| Chord Deviation      | ≤ 0.1 mm                                 |
| Angular Deviation    | ≤ 15°                                    |
| Units                | Millimeters                              |
| Naming               | `Q100-61-VIS-[COMPONENT]-LO.[ext]`       |

**Use Cases:**

- HIGH_RES: Detailed visualization, animation, rendering
- LOW_RES: Quick previews, large assemblies, web thumbnails

### OBJ (OBJ/)

**General purpose 3D format**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Format               | Wavefront OBJ with MTL                   |
| Tessellation         | Medium-high quality                      |
| Materials            | Include material library (.mtl)          |
| Textures             | Include texture maps where applicable    |
| Naming               | `Q100-61-VIS-[COMPONENT]-[VARIANT].obj`  |

**Use Cases:**

- 3D rendering applications (Blender, Maya, 3ds Max)
- Visualization tool import
- Cross-platform 3D sharing

## Naming Convention

All visualization exports follow:

```
Q100-61-VIS-[SYSTEM]-[COMPONENT]-[VARIANT].[ext]
```

### Examples

```
Q100-61-VIS-FPS-FULL-ASSY.pdf          → Full propulsor 3D PDF
Q100-61-VIS-EMD-MOTOR-ASSY.glb         → Motor assembly glTF
Q100-61-VIS-FAN-BLADE-HI.stl           → Fan blade high-res STL
Q100-61-VIS-FAN-BLADE-LO.stl           → Fan blade low-res STL
Q100-61-VIS-NAC-ASSEMBLY.obj           → Nacelle OBJ with materials
Q100-61-VIS-GBX-CUTAWAY.pdf            → Gearbox cutaway view PDF
```

## Export Procedures

1. **Source Selection**: Choose approved CAD model configuration
2. **View Setup**: Configure standard views and sections
3. **Material Assignment**: Apply visualization materials
4. **Export Settings**: Use settings from Q100-61-EXPORT-SETTINGS.yaml
5. **Quality Review**: Verify visual quality and file size
6. **Metadata**: Document version, date, and purpose

## Quality Guidelines

- Balance visual quality with file size
- Use appropriate resolution for intended use
- Verify colors and materials display correctly
- Test in target viewing applications
- Ensure proper orientation and scale

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
