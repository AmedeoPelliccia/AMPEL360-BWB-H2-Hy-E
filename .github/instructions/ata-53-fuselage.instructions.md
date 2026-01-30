---
description: "ATA 53 Fuselage documentation and structure"
applyTo: "OPT-IN_FRAMEWORK/**/ATA_53-FUSELAGE/**/*.md"
---

## ATA 53 Specific Rules

- Keep the **CI numbering** and **drawing numbering** schemes intact:
  - CIs: `CI-53-...`
  - Assemblies: `ASM-53-...`
  - Drawings: `53-XX-YYYY_Description.svg`
- When adding new CIs or assemblies, also:
  - Update `CI_Database.csv`, `Drawing_Register_Zone_XXX.csv`, and any relevant dashboards.
- Do not reorganize zones (`Zone_100`, `Zone_200`, … `Zone_600`) or splice patterns without explicit instruction.
- Maintain **clear separation** between:
  - CI definition (YAML).
  - Design description (Markdown).
  - Data tables (CSV).
  - Drawings/diagrams (SVG).
