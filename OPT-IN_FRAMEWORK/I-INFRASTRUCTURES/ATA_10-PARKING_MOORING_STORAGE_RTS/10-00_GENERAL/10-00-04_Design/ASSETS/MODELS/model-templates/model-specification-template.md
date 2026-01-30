# [Model Number] — [Model Title]

<!-- 
Template for documenting CAD models in ATA 10 Parking, Mooring, Storage & RTS
Replace all bracketed placeholders with actual information
Delete sections that are not applicable
-->

## 1. Purpose

[Brief description of what this model represents and why it exists]

## 2. Scope

This [component/assembly/simulation] applies to:

- **Aircraft Type**: AMPEL360-BWB-H2-Hy-E
- **System/Subsystem**: [Tiedown/Mooring/Parking/H2-Systems/Other]
- **Applicability**: [When/where this model is used]
- **Quantity**: [Number required per aircraft or installation]

## 3. Model Information

| Parameter | Value |
|-----------|-------|
| Model Number | [10-MDL-XXX-nnn or 10-SIM-XXX-nnn] |
| Model Type | [Assembly / Component / Simulation] |
| Component Category | [Tiedown / Mooring / Parking / H2-System] (if component) |
| CAD System | [CATIA / SolidWorks / NX / ANSYS / Other] |
| Version | [X.Y] |
| Status | [DRAFT / IN-REVIEW / ACTIVE / OBSOLETE] |
| Created | [YYYY-MM-DD] |
| Last Modified | [YYYY-MM-DD] |

## 4. Available Formats

| Format | Filename | Location | Checksum (SHA-256) |
|--------|----------|----------|---------------------|
| [Native CAD] | [filename.ext] | `cad-native/[system]/` | [checksum or TBD] |
| STEP | [filename.step] | `exchange-formats/step/` | [checksum or TBD] |
| [Visualization] | [filename.stl/glb] | `visualization/[format]/` | [checksum or TBD] |

## 5. Geometry Description

### 5.1 Overall Dimensions

[Describe the physical size and key dimensions]

| Dimension | Value (mm) | Notes |
|-----------|------------|-------|
| Length | [value] | [description] |
| Width | [value] | [description] |
| Height | [value] | [description] |
| Weight | [value] kg | [calculated/measured] |

### 5.2 Design Features

[List key geometric features, interfaces, mounting points, etc.]

- Feature 1: [description]
- Feature 2: [description]
- Feature 3: [description]

### 5.3 Assembly Structure (if applicable)

[For assemblies, describe the component breakdown]

```
[Model Number] — [Model Name]
├── Subassembly 1
│   ├── Component A
│   └── Component B
├── Subassembly 2
│   ├── Component C
│   └── Component D
└── Documentation Elements
```

## 6. Materials

| Part/Component | Material | Specification | Properties/Notes |
|----------------|----------|---------------|------------------|
| [Part name] | [Material name] | [Standard spec] | [Key properties] |
| [Part name] | [Material name] | [Standard spec] | [Key properties] |

**Material Properties (if applicable):**
- Tensile Strength: [value] MPa
- Yield Strength: [value] MPa
- Density: [value] kg/m³
- [Other relevant properties]

## 7. H2/BWB Considerations

### 7.1 BWB-Specific Design

[Describe how the BWB configuration impacts this model]

**Structural Integration:**
[How this integrates with BWB structure]

**Accessibility:**
[How ground crews access/install/maintain this]

**Design Adaptations:**
[Special features for BWB configuration]

### 7.2 H2 Safety Considerations (if applicable)

[Describe hydrogen safety features and considerations]

**Safety Features:**
- [Feature 1]
- [Feature 2]
- [Feature 3]

**H2 Compatibility:**
- Materials selected for H2 compatibility
- Non-sparking construction
- [Other H2-specific considerations]

## 8. Related Documentation

### Related Assemblies
- [Link to parent or related assembly documents]

### Related Components
- [Link to component or subassembly documents]

### Related Simulations
- [Link to FEA or CFD analysis documents]

### Related Drawings
- [Drawing number and reference]

### Related Specifications
- [Requirement IDs: REQ-10-XXX]

### Related Standards
- **[Standard name]** — [Description]
- **[Standard name]** — [Description]

## 9. Installation and Maintenance (if applicable)

### 9.1 Installation Procedure

[Brief installation steps or reference to procedure document]

1. Step 1
2. Step 2
3. Step 3

### 9.2 Maintenance Requirements

| Item | Inspection Interval | Procedure |
|------|---------------------|-----------|
| [Item] | [Interval] | [Brief description] |

## 10. Validation and Verification (if applicable)

### Design Validation
- [ ] [Validation criterion 1]
- [ ] [Validation criterion 2]
- [ ] [Validation criterion 3]

### Operational Validation
- [ ] [Operational test 1]
- [ ] [Operational test 2]
- [ ] [Operational test 3]

## 11. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| [X.Y] | [YYYY-MM-DD] | [Author name] | [Change description] |

## 12. Approvals

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Design Engineer | [TBD] | [TBD] | [TBD] |
| Lead Engineer | [TBD] | [TBD] | [TBD] |
| Safety Engineer | [TBD] | [TBD] | [TBD] |
| Configuration Manager | [TBD] | [TBD] | [TBD] |

---

## Document Control

- **Document ID**: [10-MDL/SIM-XXX-nnn]
- **Version**: [X.Y]
- **Status**: [Status]
- **Classification**: [Technical / Safety Critical]
- **Last Updated**: [YYYY-MM-DD]
- **Owner**: AMPEL360 ATA 10 [Team Name]
- **Repository**: AMPEL360-BWB-H2-Hy-E
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.

---

**See Also:**
- [MODELS README.md](../README.md)
- [MODELS Index](../00_INDEX.md)
- [model-metadata.schema.json](../model-metadata.schema.json)
