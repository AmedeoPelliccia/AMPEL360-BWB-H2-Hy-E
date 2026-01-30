# Assembly Directory Structure Template

<!-- Template ID: Q100-61-TPL-DIR-ASSEMBLY -->

## Standard Assembly Directory Layout

```
[ASSEMBLY_NUMBER]/
├── README.md                    # Assembly documentation
├── DEFINITION/
│   ├── [Assy].yaml             # Assembly definition
│   └── BOM.yaml                # Bill of Materials
├── CAD/
│   ├── [Assy].sldasm           # CAD assembly
│   ├── [Assy].step             # STEP export
│   └── COMPONENTS/             # Component references
├── DRAWINGS/
│   ├── [Assy]-DRW-001.svg      # Assembly drawing
│   └── [Assy]-DRW-001.pdf      # PDF export
├── PARTS/
│   ├── [Part1]/                # Subpart directories
│   └── [Part2]/
├── SUBASSEMBLIES/
│   └── [SubAssy]/              # Subassembly directories
├── ANALYSIS/
│   └── REPORTS/
├── INTERFACES/
│   └── ICD/                    # Interface control docs
└── EXPORTS/
    └── RELEASED/
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
