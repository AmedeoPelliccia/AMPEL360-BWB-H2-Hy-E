# Contributing to ATA 61-20 Subsystem Documentation

## Overview

This folder contains the template structure for ATA Chapter 61 (Propellers/Propulsors) subsystem documentation following the **LRU/LRI/BOM/LMP/CIR** logic.

## Folder Structure

```text
ATA_61-20_SUBSYSTEM_TEMPLATE/
├── LRU_61-20-XX_Overview.md       # LRU overview document
├── meta/
│   ├── 61-20-XX_SUBSYSTEM.yaml    # Machine-readable metadata
│   └── CONTRIBUTING.md            # This file
└── LRI/
    ├── LRI_01_ComponentA/
    │   ├── 61-20-XX_Design.md     # Design specifications
    │   ├── CIR_LINKS.md           # References to CIR assets
    │   └── BOM_LMP.md             # Bill of Materials & Line Maintenance Parts
    ├── LRI_02_ComponentB/
    │   ├── 61-20-XX_Design.md
    │   ├── CIR_LINKS.md
    │   └── BOM_LMP.md
    └── LRI_03_ComponentC/
        ├── 61-20-XX_Design.md
        ├── CIR_LINKS.md
        └── BOM_LMP.md
```

## Terminology

| Term | Definition |
|------|------------|
| **LRU** | Line Replaceable Unit – A modular component designed to be replaced at the operational (line) level |
| **LRI** | Line Replaceable Item – A sub-component within an LRU that can be individually replaced |
| **BOM** | Bill of Materials – Hierarchical list of components and parts |
| **LMP** | Line Maintenance Parts – Parts required for line-level maintenance |
| **CIR** | Configuration Item Reference – Reference to figures, tables, and diagrams in the 90-series folder |

## How to Use This Template

### 1. Create a New Subsystem

1. Copy the entire `ATA_61-20_SUBSYSTEM_TEMPLATE/` folder
2. Rename to match your subsystem: `ATA_61-20-YY_[SUBSYSTEM_NAME]/`
3. Replace all `XX` placeholders with your actual sequence number `YY`
4. Update metadata in `meta/61-20-YY_SUBSYSTEM.yaml`

### 2. Update LRU Overview

Edit `LRU_61-20-YY_Overview.md`:

- Update subsystem identification
- Fill in physical characteristics
- Document functional description
- List all LRI components

### 3. Document Each LRI

For each component in the `LRI/` folder:

1. **Design Document** (`61-20-YY_Design.md`):
   - Functional description
   - Design specifications
   - Performance parameters
   - Interface details

2. **CIR Links** (`CIR_LINKS.md`):
   - References to figures (SVG) in CIR folder
   - References to tables (CSV) in CIR folder

3. **BOM/LMP** (`BOM_LMP.md`):
   - Complete Bill of Materials
   - Line Maintenance Parts list
   - Part numbers, quantities, criticality

### 4. Create CIR Assets

Add figures and tables to the CIR folder:

**Location**: `../../../61-90_Tables_Schemas_Diagrams/ATA_61-90_CIR/`

**Naming Convention**:

```text
61-90-20_61-YY-FIG_NNN-[ComponentName].svg     # Figures
61-90-20_61-YY-TABLE_NNN-[ComponentName].csv   # Tables
```

Where:

- `61-90-20` = ATA chapter 61, section 90, subsection 20
- `61-YY` = Reference to subsystem section (e.g., 61-02 for LRI_01)
- `FIG_NNN` / `TABLE_NNN` = Sequential figure/table number
- `[ComponentName]` = Descriptive name

## File Format Standards

### Markdown (.md)

- Use GitHub Flavored Markdown
- Include Document Control section
- Maintain consistent heading hierarchy
- Use tables for structured data

### YAML (.yaml)

- UTF-8 encoding
- 2-space indentation
- Use quotes for strings with special characters
- Include schema version

### SVG (.svg)

- Vector graphics for diagrams
- Include title and description metadata
- Optimize for web viewing

### CSV (.csv)

- UTF-8 encoding
- Comma-separated values
- Header row required
- Quote fields containing commas

## Quality Checklist

Before submitting documentation:

- [ ] All `XX` placeholders replaced with actual values
- [ ] LRU Overview complete with all sections
- [ ] Each LRI has Design, CIR_LINKS, and BOM_LMP documents
- [ ] CIR assets created and properly linked
- [ ] YAML metadata validates against schema
- [ ] Document Control section complete
- [ ] Internal links verified
- [ ] Traceability to requirements documented

## Related Documents

- [AMPEL360 Documentation Standard](../../../../../../../../AMPEL360_DOCUMENTATION_STANDARD.md)
- [OPT-IN Framework Standard](../../../../../../../../OPT-IN_FRAMEWORK_STANDARD.md)
- [ATA 61 README](../../../README.md)
- [61-20 Subsystems README](../../README.md)

## Support

For questions or issues:

1. Check the AMPEL360 documentation standards
2. Review existing subsystem implementations
3. Contact the AMPEL360 Documentation Working Group

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
