# Dimensioning Standards

**Document ID**: ATA53-DES-STD-DIM-001  
**Version**: 2.0 | **Date**: 2025-11-24 | **Status**: Active  
**Reference**: ISO 129-1, ISO 1101, ISO 1302, ISO 2553, ISO 2768, ASME Y14.5

---

## 1. General Rules

1. **Units**: All dimensions in millimeters (mm) unless otherwise noted
2. **Tolerance**: Per ISO 2768-mK unless otherwise specified
3. **Arrow style**: Solid filled triangles (ISO 129-1 compliant)
4. **Text height**: 3.5mm minimum (2.5mm for confined spaces)
5. **Text position**: Above dimension line, centered
6. **Font**: ISO 3098-compliant technical lettering (Arial or similar sans-serif)

---

## 2. Dimension Placement

- Place dimensions outside the object when possible
- Chain dimensions for related features
- Use baseline dimensioning for multiple features from common datum
- Avoid crossing dimension lines
- Group related dimensions logically
- Dimension to visible outlines, not hidden lines
- Place dimensions between views where practical

---

## 3. Tolerance Notation

### 3.1 General Tolerances (ISO 2768-mK)

| Dimension Range (mm) | Tolerance Class m | Tolerance Class K (angular) |
|----------------------|-------------------|----------------------------|
| 0.5 – 3              | ±0.1              | ±1°                        |
| 3 – 6                | ±0.1              | ±0°30'                     |
| 6 – 30               | ±0.2              | ±0°20'                     |
| 30 – 120             | ±0.3              | ±0°10'                     |
| 120 – 400            | ±0.5              | ±0°5'                      |
| 400 – 1000           | ±0.8              | ±0°5'                      |
| 1000 – 2000          | ±1.2              | —                          |
| 2000 – 4000          | ±2.0              | —                          |

### 3.2 Specific Tolerances
- **Symmetric**: 100.0 ±0.1
- **Asymmetric**: 100.0 +0.2/-0.1
- **Limit dimensions**: 99.9 / 100.1

---

## 4. Datum Reference

- **Primary datum**: A (typically major mounting surface)
- **Secondary datum**: B (secondary constraint)
- **Tertiary datum**: C (rotational constraint)

Use geometric dimensioning and tolerancing (GD&T) symbols per **ISO 1101** / **ASME Y14.5**.

### 4.1 Common GD&T Symbols

| Symbol | Characteristic | Zone Type |
|--------|---------------|-----------|
| ⌖      | Position      | Cylindrical/Spherical |
| ⏥      | Flatness      | Planar |
| ⌓      | Circularity   | Circular |
| ⌒      | Profile of a line | Linear |
| ⌓      | Cylindricity  | Cylindrical |
| ∥      | Parallelism   | Planar/Linear |
| ⊥      | Perpendicularity | Planar/Linear |
| ◎      | Concentricity | Cylindrical |
| ⟁      | Circular Runout | Circular |
| ↗      | Total Runout  | Cylindrical |

---

## 5. Surface Finish Notation (ISO 1302)

### 5.1 Surface Roughness Parameters

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Ra        | —      | Arithmetical mean roughness |
| Rz        | —      | Maximum height of profile |
| Rmax      | —      | Maximum peak-to-valley height |

### 5.2 Standard Ra Values (µm)

| Finish Class | Ra (µm) | Application |
|--------------|---------|-------------|
| N12          | 50      | Rough machined |
| N10          | 25      | Standard machined |
| N9           | 12.5    | Fine machined |
| N8           | 6.3     | Ground |
| N7           | 3.2     | Fine ground |
| N6           | 1.6     | Lapped |
| N5           | 0.8     | Polished |
| N4           | 0.4     | Super-finished |

### 5.3 Surface Finish Symbol Format

```
     Ra 3.2
    ╱
   ╱ MRR (Material Removal Required)
  ╱
 ╱   Lay direction: = (parallel), ⊥ (perpendicular), X (crossed), M (multi-directional)
```

### 5.4 Typical Aerospace Surface Requirements

| Component | Ra (µm) | Notes |
|-----------|---------|-------|
| Faying surfaces | 3.2 max | Sealant application |
| Fatigue-critical | 1.6 max | Shot-peened after machining |
| Bearing seats | 0.8 max | Ground finish |
| Hydraulic sealing | 0.4 max | Lapped |

---

## 6. Weld Symbols (ISO 2553)

### 6.1 Basic Weld Symbol Structure

```
         ┌─── Finish symbol
         │ ┌─ Contour symbol
         │ │
    ─────┼─┼────── Reference line
         │ │
    Arrow│ └─ Weld symbol (arrow side)
         │
         └─── Tail (supplementary info)
```

### 6.2 Common Weld Types

| Symbol | Weld Type | Application |
|--------|-----------|-------------|
| ∨      | Single-V butt | Skin splices |
| ╲      | Fillet | Bracket attachments |
| ║      | Square butt | Thin material joints |
| ⫽      | Double-V butt | Heavy structure |
| ⌒      | Plug/Slot | Panel attachments |

### 6.3 Weld Specification Format

```
[Process]-[Filler material]-[Position]-[Size]
Example: GTAW-ER4043-F-6 (Gas Tungsten Arc, 4043 filler, Flat, 6mm leg)
```

### 6.4 Aerospace Weld Standards Reference
- AWS D17.1 – Fusion Welding for Aerospace Applications
- AMS 2680 – Electron Beam Welding
- AMS 2681 – Laser Beam Welding

---

## 7. Section and Detail View Conventions

### 7.1 Section Views

| Type | Symbol | Usage |
|------|--------|-------|
| Full section | A-A | Complete cut through object |
| Half section | A-A | Symmetric parts, one half cut |
| Offset section | A-A | Multiple planes, staggered cut |
| Revolved section | — | In-line cross-section |
| Removed section | B-B | Separate cross-section view |
| Broken-out section | — | Partial cut for internal detail |

### 7.2 Section Line Standards
- **Cutting plane line**: Thick dash-dot (0.5mm)
- **Arrow direction**: Points away from section view
- **Letters**: 6mm height minimum, placed at arrow ends
- **Hatching**: 45° at 3mm spacing (ISO 128-50)

### 7.3 Detail Views

| Element | Standard |
|---------|----------|
| Circle diameter | 20mm minimum |
| Letter designation | Sequential (X, Y, Z) |
| Scale notation | DETAIL X (SCALE 2:1) |
| Location | Adjacent to parent view |

### 7.4 Auxiliary Views
- Project perpendicular to inclined surface
- Label: "VIEW A-A" or "AUXILIARY VIEW A"
- Include projection symbol if ambiguous

---

## 8. Scale Notation Standards

### 8.1 Standard Scales (ISO 5455)

| Category | Scales |
|----------|--------|
| Enlargement | 50:1, 20:1, 10:1, 5:1, 2:1 |
| Full size | 1:1 |
| Reduction | 1:2, 1:5, 1:10, 1:20, 1:50, 1:100, 1:200, 1:500, 1:1000 |

### 8.2 Scale Notation Format
- **Title block**: SCALE 1:10 or SCALE 1/10
- **Detail views**: DETAIL A (SCALE 5:1)
- **Multiple scales**: Primary in title block, others at each view

### 8.3 Scale Selection Guidelines

| Drawing Type | Recommended Scale |
|--------------|-------------------|
| General Arrangement | 1:20, 1:50, 1:100 |
| Assembly drawings | 1:5, 1:10, 1:20 |
| Detail drawings | 1:1, 1:2, 2:1 |
| Large structures | 1:50, 1:100, 1:200 |
| Small components | 2:1, 5:1, 10:1 |

---

## 9. Thread Callout Conventions

### 9.1 ISO Metric Threads (ISO 261/262)

**Format**: `M[Diameter] x [Pitch] - [Tolerance class] - [Length]`

**Examples**:
- `M8 x 1.25 - 6H` (internal thread, medium fit)
- `M10 x 1.5 - 6g` (external thread, medium fit)
- `M6 x 1 - 6H/6g` (thread pair specification)

### 9.2 Unified Threads (ASME B1.1)

**Format**: `[Diameter]-[TPI] [Series] - [Class]`

**Examples**:
- `1/4-20 UNC-2A` (external, Class 2 fit)
- `#10-32 UNF-2B` (internal, Class 2 fit)
- `.250-28 UNEF-3A` (extra-fine, Class 3 fit)

### 9.3 Thread Representation

| View | Convention |
|------|------------|
| External (side) | Crest = thick solid, root = thin solid |
| Internal (section) | Crest = thin solid, root = thick solid |
| End view | Full circle (crest), 3/4 circle (root) |

### 9.4 Aerospace Thread Standards
- AS8879 – Metric threads for aerospace
- MIL-S-8879 – Screw threads, controlled radius root
- NAS1352 – Machine screws, pan head

---

## 10. Digital Native Requirements

### 10.1 CAD Layer Standards
Reference: `CAD_Layer_Standards.csv` (ATA53-DES-STD-LAY-001)

### 10.2 File Naming Convention

**Format**: `[ATA]-[Zone]-[Sequence]_[Title]_[Rev].[ext]`

**Examples**:
- `53-10-1000_Forward_Bulkhead_Assembly_A.svg`
- `53-40-3000_MLG_Bay_Left_Assembly_B.dwg`

### 10.3 Export Formats

| Format | Usage | Notes |
|--------|-------|-------|
| DWG | Native CAD | Master files |
| DXF | CAD exchange | Compatibility |
| PDF | Review/Print | ISO 32000 compliant |
| SVG | Web/Version control | Scalable, text-searchable |
| STEP | 3D geometry | AP203/AP214 |
| JT | Lightweight 3D | Visualization |

### 10.4 Model-Based Definition (MBD) Requirements
- Embed PMI (Product Manufacturing Information) in 3D models
- Use semantic GD&T per ASME Y14.41 / ISO 16792
- Include saved views for inspection and manufacturing

---

## 11. Revision Block and Change Marking

### 11.1 Revision Block Format

| Rev | Date | Description | Approved |
|-----|------|-------------|----------|
| A   | 2025-01-15 | Initial release | [Initials] |
| B   | 2025-03-20 | Updated per ECN-1234 | [Initials] |
| C   | 2025-06-10 | Added detail view X | [Initials] |

### 11.2 Change Marking Standards

| Element | Standard |
|---------|----------|
| Revision cloud | Freehand wavy enclosure around changed area |
| Revision triangle | △ with revision letter inside, adjacent to change |
| Zone indication | Drawing zone (e.g., "A3") in revision block |
| Color | Red for current revision, black for previous |

### 11.3 ECO/ECN Reference
- Include ECO/ECN number in revision description
- Cross-reference to Change Management System
- Maintain revision history in Master_Drawing_Register.csv

### 11.4 Superseded Drawing Handling
- Mark "SUPERSEDED BY [New Dwg No.]" diagonally across drawing
- Archive per document retention policy
- Update all referencing documents

---

## 12. Special Notations

### 12.1 Material Removal Indicators
- **MRR** (Material Removal Required): Machining mandatory
- **MRP** (Material Removal Prohibited): Cast/forged surface maintained
- **NMR** (No Material Removal): As-manufactured surface acceptable

### 12.2 Critical Dimensions
- **CTQ** (Critical to Quality): Flag with ⬥ symbol
- **Safety Critical**: Flag with △ and note "SAFETY CRITICAL"
- **Interchangeability**: Note "INTERCHANGEABLE" where applicable

### 12.3 Notes Hierarchy
1. General notes (apply to entire drawing)
2. Local notes (apply to specific features)
3. Flag notes (warnings and critical items)

---

## Document Control

- **Document ID**: ATA53-DES-STD-DIM-001
- **Version**: 2.0
- **Date**: 2025-11-24
- **Status**: Active
- **Owner**: ATA 53 Drawing Authority
- **References**: ISO 129-1, ISO 1101, ISO 1302, ISO 2553, ISO 2768, ASME Y14.5
- **AI Assistance**: Generated with GitHub Copilot, prompted by Amedeo Pelliccia
- **Human Approver**: _[to be completed]_
