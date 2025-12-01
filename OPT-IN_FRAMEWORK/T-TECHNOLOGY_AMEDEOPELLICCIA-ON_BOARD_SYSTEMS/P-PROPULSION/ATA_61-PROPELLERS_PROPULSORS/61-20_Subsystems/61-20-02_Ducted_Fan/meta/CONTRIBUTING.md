# Contributing to 61-20-02_Ducted_Fan

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Subsystem ID**   | 61-20-02_Ducted_Fan                    |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Last Updated**   | 2025-12-01                             |

---

## 1. Purpose

This document provides guidelines for contributing to the **Ducted Fan** subsystem documentation and data.

---

## 2. File Structure

```
61-20-02_Ducted_Fan/
├── README.md                      # Subsystem overview
├── LRU_61-20-02_DuctedFan.md      # LRU description
├── LRI/                           # Line Replaceable Items
│   ├── 61-20-02_LRI_01_Rotor/
│   │   ├── 61-20-02_01_001_AerodynamicDesign.md
│   │   ├── CIR_LINKS.md
│   │   └── BOM_LMP.md
│   ├── 61-20-02_LRI_02_Stator/
│   │   ├── 61-20-02_02_001_StatorDesign.md
│   │   ├── CIR_LINKS.md
│   │   └── BOM_LMP.md
│   └── 61-20-02_LRI_03_Nacelle/
│       ├── 61-20-02_03_001_NacelleIntegration.md
│       ├── CIR_LINKS.md
│       └── BOM_LMP.md
├── SysML/                         # System models
├── meta/
│   ├── 61-20-02_SUBSYSTEM.yaml
│   └── CONTRIBUTING.md
└── ...
```

---

## 3. Naming Conventions

### 3.1 Document IDs

Format: `61-20-02_XX_YYY_Description.md`

- `XX` = LRI sequence (01, 02, 03, ...)
- `YYY` = Document sequence within LRI (001, 002, ...)
- `Description` = PascalCase descriptive name

Examples:
- `61-20-02_01_001_AerodynamicDesign.md`
- `61-20-02_02_001_StatorDesign.md`

### 3.2 Part Numbers

| Prefix       | Component Type      | Example            |
|--------------|---------------------|---------------------|
| PN-DF-ROT-   | Rotor components    | PN-DF-ROT-001       |
| PN-DF-STA-   | Stator components   | PN-DF-STA-001       |
| PN-DF-NAC-   | Nacelle components  | PN-DF-NAC-001       |
| PN-DF-BLD-   | Blades              | PN-DF-BLD-001       |
| PN-DF-VAN-   | Vanes               | PN-DF-VAN-001       |

### 3.3 CIR References

Format: `61-90-20_02-XX-TYPE_YYY`

- `XX` = LRI sequence
- `TYPE` = FIG / TABLE / CHART
- `YYY` = Asset sequence

---

## 4. Data Formats

| Type               | Format   | Location                        |
|--------------------|----------|----------------------------------|
| **Narrative docs** | Markdown | LRI folders                      |
| **BOM / LMP**      | Markdown | `BOM_LMP.md` in each LRI folder  |
| **Coordinates**    | CSV      | `61-90_Tables_Schemas_Diagrams/` |
| **Diagrams**       | SVG      | `61-90_Tables_Schemas_Diagrams/` |
| **Metadata**       | YAML     | `meta/` folder                   |

---

## 5. BOM + LMP Integration

When adding new components:

1. Update the relevant `BOM_LMP.md` with:
   - Part number
   - Description
   - Material
   - Quantity
   - Illustrated (Y/N)
   - Maintenance marking (Y/N)

2. Add corresponding CIR references in `CIR_LINKS.md`

3. Update `61-90_Tables_Schemas_Diagrams/` with:
   - Coordinate tables (include BOM columns)
   - Technical drawings (SVG)

---

## 6. Review Process

1. **Self-review** — Verify all links and cross-references
2. **Technical review** — Domain expert validation
3. **CM approval** — Configuration management check
4. **Merge** — Per `61-00-11_EIS_Versions_Tags` rules

---

## 7. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Last AI Update:** 2025-12-01
