# Contributing to 61-20-01_Electric_Motor

## Overview

This document provides guidelines for contributing to the Electric Motor (61-20-01) subsystem documentation within the AMPEL360 Q100 programme.

## Document Structure

All documents in this subsystem follow the OPT-IN Framework v1.2 structure.

### File Naming Convention

```
61-20-01_XX_YYY_Description.ext
```

Where:
- `61-20-01` = Subsystem ID
- `XX` = Category (01=Specs, 02=Performance, 03=Interfaces, etc.)
- `YYY` = Sequence number (001, 002, ...)
- `Description` = Brief description (PascalCase or snake_case)
- `ext` = File extension (.md, .yaml, .csv, .svg)

### Category Codes

| Code | Category |
|------|----------|
| 01 | Specifications |
| 02 | Performance Data |
| 03 | Interfaces |
| 04 | Thermal |
| 05 | Reliability & Maintenance |
| 06 | Certification |
| 07 | Models & Tables |
| 08 | Change Management |

## File Formats

| Format | Use Case |
|--------|----------|
| `.md` | Narrative documents, specifications, procedures |
| `.yaml` | Structured metadata, configuration, parameters |
| `.csv` | Tabular data, lookup tables |
| `.svg` | Diagrams, schematics (vector graphics only) |
| `.sysml` | SysML 1.6 textual models |

**Not permitted:** `.xlsx`, `.docx`, `.pdf` (generated outputs excepted)

## Document Headers

All Markdown documents shall include:

1. Title (H1)
2. Metadata table (Document ID, Subsystem, ATA, Programme, Version, Date, Owner, Standard)
3. Horizontal rule
4. Numbered sections

## Change Process

1. All changes require review by the subsystem owner
2. Update the CHANGELOG.md with each modification
3. Increment version numbers per semantic versioning
4. Submit via PR with clear description

## Quality Checks

Before submitting:

- [ ] File naming follows convention
- [ ] Metadata table is complete
- [ ] Cross-references are valid
- [ ] CHANGELOG is updated
- [ ] No binary files (except test reports in PDF)

## Contact

- **Subsystem Owner:** AMPEL360 Propulsion Team
- **Configuration Management:** See programme CC/CM procedures

---

*OPT-IN Framework v1.2 | AMPEL360 BWB H₂ Hy-E Q100*
