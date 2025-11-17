# Template Naming Convention (ATA 02-00-04)

## Overview

All templates in the TEMPLATES library follow a standardized naming pattern to ensure:
- Consistent identification across the project
- Easy automation and scripting
- Clear versioning and revision control
- Traceability to source domain and intended use

---

## Naming Pattern

```text
[ATA]-TPL-[Domain]-[TemplateName]-R[rev].[ext]
```

### Components

| Component | Description | Example Values |
|-----------|-------------|----------------|
| **[ATA]** | ATA chapter reference | `02-00-04` |
| **TPL** | Template artifact identifier (fixed) | `TPL` |
| **[Domain]** | Template domain category | `DOC`, `PRES`, `XLS`, `SCR`, `TD` |
| **[TemplateName]** | Descriptive template name | `Requirement`, `BOM`, `DesignReview` |
| **R[rev]** | Revision number | `R01`, `R02`, `R03`, ... |
| **[ext]** | File extension | `md`, `docx`, `pptx`, `xlsx`, `py`, `xml` |

---

## Domain Codes

| Code | Domain | Purpose | Typical Extensions |
|------|--------|---------|-------------------|
| **DOC** | Documents | Requirements, specifications, reports, procedures | `.md`, `.docx`, `.pdf` |
| **PRES** | Presentations | Design reviews, briefings, summaries | `.pptx`, `.pdf` |
| **XLS** | Spreadsheets | BOMs, registers, matrices, logs | `.xlsx`, `.csv` |
| **SCR** | Scripts | Automation, data extraction, validation | `.py`, `.sh`, `.js` |
| **TD** | Technical Publications | S1000D data modules, manuals, tasks | `.xml`, `.md`, `.sgml` |

---

## Template Name Guidelines

Template names should be:
- **Descriptive**: Clearly indicate the template's purpose
- **Concise**: Use abbreviations where widely understood (e.g., BOM, ICD)
- **PascalCase or snake_case**: Consistent with project standards
- **No spaces**: Use underscores or hyphens if needed

### Examples of Good Template Names

| Domain | Template Name | Full Filename |
|--------|--------------|---------------|
| DOC | `Requirement` | `02-00-04-TPL-DOC-Requirement-R01.md` |
| DOC | `RequirementsSet` | `02-00-04-TPL-DOC-RequirementsSet-R01.md` |
| DOC | `SystemSpecification` | `02-00-04-TPL-DOC-SystemSpecification-R01.md` |
| DOC | `InstallationProcedure` | `02-00-04-TPL-DOC-InstallationProcedure-R01.md` |
| PRES | `DesignReview` | `02-00-04-TPL-PRES-DesignReview-R01.pptx` |
| PRES | `ManagementSummary` | `02-00-04-TPL-PRES-ManagementSummary-R01.pptx` |
| XLS | `BOM` | `02-00-04-TPL-XLS-BOM-R01.xlsx` |
| XLS | `RiskRegister` | `02-00-04-TPL-XLS-RiskRegister-R01.xlsx` |
| SCR | `DataExtraction` | `02-00-04-TPL-SCR-DataExtraction-R01.py` |
| SCR | `ModelCheck` | `02-00-04-TPL-SCR-ModelCheck-R01.py` |
| TD | `S1000D_DataModule` | `02-00-04-TPL-TD-S1000D_DataModule-R01.xml` |
| TD | `OPS_ManualSection` | `02-00-04-TPL-TD-OPS_ManualSection-R01.md` |

---

## Revision Numbering

- Start with **R01** for the initial version
- Increment sequentially for each major revision: **R02**, **R03**, etc.
- Minor updates within a revision can be tracked in the Change Log
- When creating a new major revision:
  1. Increment the revision number
  2. Update the Global Index
  3. Archive the previous revision to `99_ARCHIVE/`

---

## Archive Naming

When archiving superseded templates, use:

```text
99_ARCHIVE/02-00-04-TPL-ARCHIVE_YYYY-MM-DD_<tag>/
```

Example:
```text
99_ARCHIVE/02-00-04-TPL-ARCHIVE_2025-11-17_pre-v2-update/
```

---

## Validation Rules

Templates must follow these rules:

1. ✅ Always start with `02-00-04-TPL-`
2. ✅ Include a valid domain code (DOC, PRES, XLS, SCR, TD)
3. ✅ Use a descriptive template name without spaces
4. ✅ Include revision number in format `-Rxx`
5. ✅ End with appropriate file extension
6. ✅ Be registered in `02-00-04-TPL_Global_Index.csv`

---

## Document Control

* **Version:** 1.0
* **Date:** 2025-11-17
* **Status:** WORKING
* **Originator:** AI (prompted by Amedeo Pelliccia)
* **Checker:** [Pending]
* **Approver:** [Pending]
