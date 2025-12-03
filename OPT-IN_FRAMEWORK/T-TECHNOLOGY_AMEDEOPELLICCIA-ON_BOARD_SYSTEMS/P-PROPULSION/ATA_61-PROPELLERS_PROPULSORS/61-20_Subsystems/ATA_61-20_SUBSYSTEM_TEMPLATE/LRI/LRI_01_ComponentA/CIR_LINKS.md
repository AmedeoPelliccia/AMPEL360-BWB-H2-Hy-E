# CIR Links — LRI_01 ComponentA

## Document Information

- **Document ID**: 61-20-XX-LRI_01_CIR_LINKS
- **LRI ID**: LRI_01
- **Component**: ComponentA
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-12-01

---

## 1. Overview

This document provides references to all Configuration Item Reference (CIR) assets associated with **LRI_01 ComponentA**. All CIR assets are stored in the centralized CIR folder.

**CIR Folder Location**: `../../../../61-90_Tables_Schemas_Diagrams/ATA_61-90_CIR/`

---

## 2. Figure References (FIG)

### 2.1 Assembly Drawing

| Attribute | Value |
|-----------|-------|
| **CIR ID** | 61-90-20_61-02-FIG_001 |
| **Title** | ComponentA Assembly Drawing |
| **Format** | SVG |
| **Filename** | `61-90-20_61-02-FIG_001-ComponentA.svg` |
| **Path** | [61-90-20_61-02-FIG_001-ComponentA.svg](../../../../61-90_Tables_Schemas_Diagrams/ATA_61-90_CIR/61-90-20_61-02-FIG_001-ComponentA.svg) |
| **Description** | Isometric assembly view of ComponentA showing major subassemblies and mounting interfaces |
| **Revision** | Rev A |
| **Last Updated** | 2025-12-01 |

### 2.2 Additional Figures

*Add additional figure references as needed following the same format.*

| CIR ID | Title | Format | Description |
|--------|-------|--------|-------------|
| [61-90-20_61-02-FIG_002] | [Exploded View] | SVG | [Description] |
| [61-90-20_61-02-FIG_003] | [Installation Drawing] | SVG | [Description] |

---

## 3. Table References (TABLE)

### 3.1 Specifications Table

| Attribute | Value |
|-----------|-------|
| **CIR ID** | 61-90-20_61-02-TABLE_001 |
| **Title** | ComponentA Specifications |
| **Format** | CSV |
| **Filename** | `61-90-20_61-02-TABLE_001-ComponentA.csv` |
| **Path** | [61-90-20_61-02-TABLE_001-ComponentA.csv](../../../../61-90_Tables_Schemas_Diagrams/ATA_61-90_CIR/61-90-20_61-02-TABLE_001-ComponentA.csv) |
| **Description** | Complete specifications table including electrical, mechanical, and environmental parameters |
| **Revision** | Rev A |
| **Last Updated** | 2025-12-01 |

### 3.2 Additional Tables

*Add additional table references as needed following the same format.*

| CIR ID | Title | Format | Description |
|--------|-------|--------|-------------|
| [61-90-20_61-02-TABLE_002] | [Parts List] | CSV | [Description] |
| [61-90-20_61-02-TABLE_003] | [Test Data] | CSV | [Description] |

---

## 4. CIR Naming Convention

### 4.1 Figure Naming

```text
61-90-20_61-YY-FIG_NNN-[ComponentName].svg
│  │  │   │  │   │     └── Descriptive component name
│  │  │   │  │   └── Sequential figure number (001, 002, etc.)
│  │  │   │  └── Figure type identifier
│  │  │   └── LRI reference section (02=LRI_01, 03=LRI_02, 04=LRI_03)
│  │  └── Subsystem section (20)
│  └── CIR section (90)
└── ATA Chapter (61)
```

### 4.2 Table Naming

```text
61-90-20_61-YY-TABLE_NNN-[ComponentName].csv
│  │  │   │  │   │       └── Descriptive component name
│  │  │   │  │   └── Sequential table number (001, 002, etc.)
│  │  │   │  └── Table type identifier
│  │  │   └── LRI reference section
│  │  └── Subsystem section (20)
│  └── CIR section (90)
└── ATA Chapter (61)
```

---

## 5. Usage Guidelines

### 5.1 Linking in Documentation

When referencing CIR assets in other documents, use relative paths:

**Markdown**:
```markdown
See [ComponentA Assembly Drawing](../../../../61-90_Tables_Schemas_Diagrams/ATA_61-90_CIR/61-90-20_61-02-FIG_001-ComponentA.svg)
```

**YAML**:
```yaml
figure: "61-90-20_61-02-FIG_001-ComponentA.svg"
table: "61-90-20_61-02-TABLE_001-ComponentA.csv"
```

### 5.2 Version Control

- CIR assets follow the same version control as documentation
- Update revision indicators (Rev A, Rev B, etc.) when assets change
- Maintain change history in this document

---

## 6. Change History

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| 2025-12-01 | Rev A | Initial creation | AMPEL360 Documentation WG |

---

## 7. Related Documents

- [61-20-XX Design](./61-20-XX_Design.md)
- [BOM/LMP](./BOM_LMP.md)
- [LRU Overview](../../LRU_61-20-XX_Overview.md)
- [61-90 CIR Index](../../../../61-90_Tables_Schemas_Diagrams/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
