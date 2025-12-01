# ATA 61-90 CIR — Configuration Item References

## Overview

This folder contains **Configuration Item Reference (CIR)** assets for ATA Chapter 61 (Propellers/Propulsors) subsystems. CIR assets include figures (SVG) and tables (CSV) that support the technical documentation.

## Folder Structure

```text
ATA_61-90_CIR/
├── README.md                                    # This file
├── 61-90-20_61-02-FIG_001-ComponentA.svg       # LRI_01 assembly figure
├── 61-90-20_61-02-TABLE_001-ComponentA.csv     # LRI_01 specifications table
├── 61-90-20_61-03-FIG_002-ComponentB.svg       # LRI_02 assembly figure
├── 61-90-20_61-03-TABLE_002-ComponentB.csv     # LRI_02 specifications table
├── 61-90-20_61-04-FIG_003-ComponentC.svg       # LRI_03 assembly figure
└── 61-90-20_61-04-TABLE_003-ComponentC.csv     # LRI_03 specifications table
```

## Naming Convention

### Figures (FIG)

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

### Tables (TABLE)

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

## Asset Index

### Figures

| CIR ID | LRI | Description | Status |
|--------|-----|-------------|--------|
| 61-90-20_61-02-FIG_001 | LRI_01 | ComponentA Assembly Drawing | Placeholder |
| 61-90-20_61-03-FIG_002 | LRI_02 | ComponentB Assembly Drawing | Placeholder |
| 61-90-20_61-04-FIG_003 | LRI_03 | ComponentC Assembly Drawing | Placeholder |

### Tables

| CIR ID | LRI | Description | Status |
|--------|-----|-------------|--------|
| 61-90-20_61-02-TABLE_001 | LRI_01 | ComponentA Specifications | Template |
| 61-90-20_61-03-TABLE_002 | LRI_02 | ComponentB Specifications | Template |
| 61-90-20_61-04-TABLE_003 | LRI_03 | ComponentC Specifications | Template |

## Usage

### Referencing CIR Assets

From LRI documentation, reference CIR assets using relative paths:

**Markdown**:
```markdown
![ComponentA Assembly](../../../../61-90_Tables_Schemas_Diagrams/ATA_61-90_CIR/61-90-20_61-02-FIG_001-ComponentA.svg)
```

**YAML**:
```yaml
figure: "61-90-20_61-02-FIG_001-ComponentA.svg"
table: "61-90-20_61-02-TABLE_001-ComponentA.csv"
```

### Adding New Assets

1. Follow the naming convention above
2. Place figures in SVG format
3. Place tables in CSV format with header row
4. Update this README index
5. Update corresponding CIR_LINKS.md in the LRI folder

## File Format Requirements

### SVG Files

- Vector graphics format
- Include `<title>` and `<desc>` metadata
- Standard A4/A3 drawing format with title block
- Optimize for web viewing

### CSV Files

- UTF-8 encoding
- Comma-separated values
- Header row required
- Quote fields containing commas

## Related Documents

- [61-20 Subsystems Template](../../../61-20_Subsystems/ATA_61-20_SUBSYSTEM_TEMPLATE/)
- [61-90 Tables/Schemas/Diagrams README](../README.md)
- [AMPEL360 Documentation Standard](../../../../../../AMPEL360_DOCUMENTATION_STANDARD.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
