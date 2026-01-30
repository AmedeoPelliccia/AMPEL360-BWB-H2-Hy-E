# Part Directory Structure Template

<!-- Template ID: Q100-61-TPL-DIR-PART -->

## Standard Part Directory Layout

```
[PART_NUMBER]/
├── README.md                    # Part documentation (use README-PART template)
├── DEFINITION/
│   ├── [Part].yaml             # Part definition (use YAML-PART-DEF template)
│   └── [Part].json             # Optional JSON format
├── CAD/
│   ├── [Part].sldprt           # CAD model
│   ├── [Part].step             # STEP export
│   └── [Part].iges             # IGES export (if needed)
├── DRAWINGS/
│   ├── [Part]-DRW-001.svg      # Engineering drawing
│   └── [Part]-DRW-001.pdf      # PDF export
├── ANALYSIS/
│   ├── FEA/                    # Finite Element Analysis
│   ├── THERMAL/                # Thermal analysis
│   └── REPORTS/                # Analysis reports
├── SPECIFICATIONS/
│   └── [Part]-SPEC.md          # Part specifications
└── EXPORTS/
    └── RELEASED/               # Released outputs
```

---

## Usage

1. Create directory with part number as name
2. Copy this structure
3. Add files using appropriate templates
4. Update README with part information

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
