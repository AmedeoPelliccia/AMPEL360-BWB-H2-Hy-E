# ASSETS — Requirements Supporting Materials

## Purpose

This folder contains supporting materials for the **95-00-03 Requirements**, including:
- Diagrams illustrating requirements taxonomy and relationships
- Visual aids for requirements traceability
- Reference materials and templates
- Exported views and reports

## Contents

### Planned Assets

| Asset ID | Filename | Type | Description | Status |
|----------|----------|------|-------------|--------|
| 95-00-03-OVW-001 | Requirements_Taxonomy_Diagram.png | Diagram | Visual representation of requirements categories and ID ranges | Planned |
| 95-00-03-OVW-002 | Requirements_to_Lifecycle_Map.svg | Diagram | Mapping of requirements to 14-folder lifecycle stages | Planned |
| 95-00-03-OVW-003 | Requirements_Traceability_Graph.svg | Diagram | Graph showing requirement dependencies and traceability links | Planned |
| 95-00-03-REF-001 | Requirement_Template.md | Template | Blank requirement template for new requirements | Planned |
| 95-00-03-REF-002 | EU_AI_Act_Mapping.xlsx | Reference | Mapping of DPP requirements to EU AI Act articles | Planned |
| 95-00-03-REF-003 | EU_DPP_Mapping.xlsx | Reference | Mapping of DPP requirements to EU DPP regulation | Planned |

---

## Asset Naming Convention

Assets follow the naming pattern:
```
95-00-03-[TYPE]-[NNN]_Descriptive_Name.[ext]
│         │      │
│         │      └─ Sequential number within type
│         └──────── Asset type (OVW=Overview, REF=Reference, etc.)
└────────────────── ATA Chapter + Section + Folder
```

### Asset Types

| Type | Description | Examples |
|------|-------------|----------|
| **OVW** | Overview diagrams | Taxonomy, architecture, process flows |
| **REF** | Reference materials | Standards mapping, templates, checklists |
| **RPT** | Reports | Coverage reports, gap analysis, metrics |
| **TMP** | Templates | Blank forms, requirement templates |

---

## Usage Guidelines

### Adding New Assets

1. Determine the appropriate **asset type** (OVW, REF, RPT, TMP)
2. Assign the next available **sequential number** within that type
3. Create the asset file with the standard naming convention
4. Update this README with the asset metadata

### Linking Assets from Requirements

Requirements should reference assets using relative paths:
```markdown
See [Requirements Taxonomy Diagram](../ASSETS/95-00-03-OVW-001_Requirements_Taxonomy_Diagram.png)
```

### Version Control

- Assets are version-controlled in git alongside requirements
- For binary files (PNG, XLSX), include source files when possible (e.g., draw.io, ODS)
- Large binary files (> 5 MB) should be stored in Git LFS or external storage

---

## Document Control

- **Folder ID**: 95-00-03-ASSETS
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-11-17
- **Owner**: Requirements WG
- **Standard**: OPT-IN Framework v1.4

---

**For questions about requirements assets, contact: requirements@ampel360.aero**
