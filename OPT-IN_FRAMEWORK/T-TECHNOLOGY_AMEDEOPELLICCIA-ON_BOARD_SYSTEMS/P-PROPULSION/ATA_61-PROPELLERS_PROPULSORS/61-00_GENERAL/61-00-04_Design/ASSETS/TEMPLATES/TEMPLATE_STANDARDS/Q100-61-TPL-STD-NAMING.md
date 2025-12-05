# Template Naming Convention

<!-- Template ID: Q100-61-TPL-STD-NAMING -->

## 1. Purpose

This document defines the naming convention for all templates in the ATA 61 TEMPLATES directory.

---

## 2. Naming Format

### 2.1 Standard Format

```
Q100-61-TPL-[CATEGORY]-[NAME].[ext]
```

**Components:**
- `Q100` — AMPEL360 program identifier
- `61` — ATA chapter
- `TPL` — Template designation
- `[CATEGORY]` — Template category code
- `[NAME]` — Descriptive name
- `[ext]` — File extension

---

## 3. Category Codes

| Code | Category | Description |
|------|----------|-------------|
| PRT | Part | Part CAD template |
| ASSY | Assembly | Assembly CAD template |
| START | Startup | Startup model template |
| DRW | Drawing | Drawing template |
| SYM | Symbol | Symbol library |
| SPEC | Specification | Specification template |
| RPT | Report | Report template |
| PROC | Procedure | Procedure template |
| CHK | Checklist | Checklist template |
| MTG | Meeting | Meeting notes template |
| YAML | YAML | YAML schema template |
| CSV | CSV | CSV format template |
| JSON | JSON | JSON schema template |
| FEA | FEA | FEA analysis template |
| CFD | CFD | CFD analysis template |
| SIM | Simulation | Simulation template |
| EM | Electromagnetic | EM analysis template |
| DIR | Directory | Directory structure |
| README | README | README template |
| WF | Workflow | Workflow template |
| CERT | Certification | Certification template |
| TEST | Test | Test template |
| SAF | Safety | Safety analysis template |
| STD | Standard | Template standard |

---

## 4. Naming Rules

### 4.1 General Rules

1. Use UPPERCASE for category codes
2. Use UPPERCASE with hyphens for names
3. No spaces in filenames
4. Use descriptive but concise names

### 4.2 Examples

| Template | Naming |
|----------|--------|
| Part definition YAML | Q100-61-TPL-YAML-PART-DEF.yaml |
| A3 landscape drawing | Q100-61-TPL-DRW-A3-LANDSCAPE.svg |
| Test report template | Q100-61-TPL-RPT-TEST.md |
| FMEA template | Q100-61-TPL-SAF-FMEA.yaml |

---

## 5. Extension Guidelines

| Format | Extension |
|--------|-----------|
| Markdown | .md |
| YAML | .yaml |
| JSON Schema | .schema.json |
| CSV | .csv |
| SVG | .svg |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
