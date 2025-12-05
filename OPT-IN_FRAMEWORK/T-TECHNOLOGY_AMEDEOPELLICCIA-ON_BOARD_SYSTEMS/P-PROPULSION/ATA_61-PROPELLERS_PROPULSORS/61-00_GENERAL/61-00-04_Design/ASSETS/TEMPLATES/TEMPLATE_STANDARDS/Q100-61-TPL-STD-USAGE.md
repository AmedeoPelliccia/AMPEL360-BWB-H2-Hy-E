# Template Usage Guidelines

<!-- Template ID: Q100-61-TPL-STD-USAGE -->

## 1. Purpose

This document provides guidelines for using templates in the ATA 61 propulsion system design.

---

## 2. Template Usage Process

### 2.1 Five-Step Process

```
1. FIND     → Locate appropriate template
2. COPY     → Copy to target directory
3. RENAME   → Apply proper naming convention
4. FILL     → Complete template content
5. COMMIT   → Version control the document
```

---

## 3. Finding Templates

### 3.1 Template Directory Structure

```
TEMPLATES/
├── CAD_TEMPLATES/          → CAD file templates
├── DRAWING_TEMPLATES/      → Drawing templates
├── DOCUMENT_TEMPLATES/     → Document templates
├── DATA_TEMPLATES/         → Data schema templates
├── ANALYSIS_TEMPLATES/     → Analysis templates
├── PROJECT_TEMPLATES/      → Project organization templates
├── CERTIFICATION_TEMPLATES/→ Certification templates
└── TEMPLATE_STANDARDS/     → Template standards
```

### 3.2 Selection Criteria

| Need | Template Location |
|------|-------------------|
| Part documentation | PROJECT_TEMPLATES/README_TEMPLATES/ |
| Test report | DOCUMENT_TEMPLATES/REPORTS/ |
| YAML data structure | DATA_TEMPLATES/YAML_SCHEMAS/ |
| Safety analysis | CERTIFICATION_TEMPLATES/SAFETY/ |

---

## 4. Copying and Renaming

### 4.1 Copy Rules

1. Copy entire template file
2. Do not modify original template
3. Place in appropriate target directory

### 4.2 Renaming

| Template | Becomes |
|----------|---------|
| Q100-61-TPL-YAML-PART-DEF.yaml | Q100-61-PRT-001.yaml |
| Q100-61-TPL-RPT-ANALYSIS.md | 61-10-04-RPT-001_FEA_Report.md |

---

## 5. Completing Templates

### 5.1 Field Types

| Marker | Meaning | Action |
|--------|---------|--------|
| [REQUIRED] | Mandatory field | Must complete |
| [Optional] | Optional field | Complete if applicable |
| [TBD] | To be determined | Mark for follow-up |

### 5.2 Instructions

1. Remove template instruction blocks after use
2. Complete all [REQUIRED] fields
3. Delete unused optional sections
4. Verify Document Control section

---

## 6. Common Mistakes to Avoid

- ❌ Modifying the original template
- ❌ Leaving [REQUIRED] placeholders unfilled
- ❌ Not updating Document Control section
- ❌ Using wrong template for document type

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
