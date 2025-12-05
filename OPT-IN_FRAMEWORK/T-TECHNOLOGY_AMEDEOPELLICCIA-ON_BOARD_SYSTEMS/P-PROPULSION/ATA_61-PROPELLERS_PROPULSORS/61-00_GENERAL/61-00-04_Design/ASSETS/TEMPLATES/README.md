# TEMPLATES — ATA 61 Propellers/Propulsors

## Overview

This directory contains standardized templates, boilerplates, and reusable patterns for creating consistent documentation, CAD files, and data structures for the AMPEL360-BWB-H2-Hy-E Q100 program.

Templates ensure consistency across:
- **PARTS** — Component definitions
- **ASSEMBLIES** — CAD products
- **PRODUCTS** — Configured products
- **MODELS** — Analysis models
- **INSTALLATIONS** — Integration data
- **DRAWINGS** — Engineering drawings
- **EXPORTS** — Released outputs

---

## Template Categories

| Category | Directory | Purpose |
|----------|-----------|---------|
| CAD | `CAD_TEMPLATES/` | Part, assembly, and startup model templates |
| Drawing | `DRAWING_TEMPLATES/` | Sheet formats, title blocks, symbol libraries |
| Document | `DOCUMENT_TEMPLATES/` | Specifications, reports, procedures, checklists |
| Data | `DATA_TEMPLATES/` | YAML schemas, CSV formats, JSON schemas |
| Analysis | `ANALYSIS_TEMPLATES/` | FEA, CFD, system simulation templates |
| Project | `PROJECT_TEMPLATES/` | Directory structures, READMEs, workflows |
| Certification | `CERTIFICATION_TEMPLATES/` | Compliance, test plans, safety |
| Standards | `TEMPLATE_STANDARDS/` | Template naming, usage, versioning rules |

---

## Naming Convention

All templates follow the Q100-61 naming pattern:

```
Q100-61-TPL-[CATEGORY]-[NAME].[ext]
```

### Template Category Codes

| Code | Description | Example |
|------|-------------|---------|
| PRT | Part CAD template | Q100-61-TPL-PRT-BLADE.sldprt |
| ASSY | Assembly CAD template | Q100-61-TPL-ASSY-PROPULSOR.sldasm |
| START | Startup model | Q100-61-TPL-START-MM.sldprt |
| DRW | Drawing template | Q100-61-TPL-DRW-A3-LANDSCAPE.svg |
| SYM | Symbol library | Q100-61-TPL-SYM-GDT.svg |
| SPEC | Specification template | Q100-61-TPL-SPEC-PERFORMANCE.md |
| RPT | Report template | Q100-61-TPL-RPT-ANALYSIS.md |
| PROC | Procedure template | Q100-61-TPL-PROC-INSTALLATION.md |
| CHK | Checklist template | Q100-61-TPL-CHK-DESIGN-REVIEW.md |
| MTG | Meeting template | Q100-61-TPL-MTG-TECHNICAL.md |
| YAML | YAML schema template | Q100-61-TPL-YAML-PART-DEF.yaml |
| CSV | CSV format template | Q100-61-TPL-CSV-BOM.csv |
| JSON | JSON schema template | Q100-61-TPL-JSON-PART.schema.json |
| FEA | FEA analysis template | Q100-61-TPL-FEA-STATIC.inp |
| CFD | CFD analysis template | Q100-61-TPL-CFD-FLOW.cfg |
| SIM | Simulation template | Q100-61-TPL-SIM-THERMAL.sim |
| EM | Electromagnetic template | Q100-61-TPL-EM-COMPAT.cfg |
| DIR | Directory structure template | Q100-61-TPL-DIR-PART.md |
| README | README template | Q100-61-TPL-README-PART.md |
| WF | Workflow template | Q100-61-TPL-WF-DESIGN-RELEASE.md |
| CERT | Certification template | Q100-61-TPL-CERT-MOC.md |
| TEST | Test template | Q100-61-TPL-TEST-PLAN.md |
| SAF | Safety template | Q100-61-TPL-SAF-FMEA.yaml |
| STD | Template standard | Q100-61-TPL-STD-NAMING.md |

---

## How to Use Templates

### 1. Find the Right Template

Navigate to the appropriate subdirectory based on what you need to create:

```
TEMPLATES/
├── CAD_TEMPLATES/          → For part/assembly models
├── DRAWING_TEMPLATES/      → For engineering drawings
├── DOCUMENT_TEMPLATES/     → For specifications, reports, procedures
├── DATA_TEMPLATES/         → For data structures (YAML, CSV, JSON)
├── ANALYSIS_TEMPLATES/     → For FEA, CFD, simulations
├── PROJECT_TEMPLATES/      → For directory structures and workflows
├── CERTIFICATION_TEMPLATES/→ For compliance and certification
└── TEMPLATE_STANDARDS/     → For template standards and guidelines
```

### 2. Copy the Template

Copy the template file to your target location:

```bash
cp TEMPLATES/DOCUMENT_TEMPLATES/SPECIFICATIONS/Q100-61-TPL-SPEC-PERFORMANCE.md \
   ../PARTS/MyComponent/SPEC-PERFORMANCE.md
```

### 3. Rename Following Standards

Rename the file following the AMPEL360 Assets naming convention:

```
61-00-04-A501_SPEC_Component_Performance.md
```

### 4. Fill in the Template

1. Remove the `<!-- TEMPLATE INSTRUCTIONS -->` sections
2. Replace all `[PLACEHOLDER]` text with actual content
3. Fill in required fields (marked with `*`)
4. Remove or customize optional sections

### 5. Validate and Commit

1. Ensure all required fields are completed
2. Run any applicable validation checks
3. Update the INDEX.meta.yaml if adding a new asset
4. Commit with a descriptive message

---

## Template Structure

Each template includes:

1. **Header** — Template ID, version, and description
2. **Instructions** — How to use (remove when applying)
3. **Required Fields** — Marked with `*` or `[REQUIRED]`
4. **Optional Fields** — With sensible defaults
5. **Examples** — Sample content where helpful
6. **Document Control** — Version tracking

---

## Directory Structure

```
TEMPLATES/
├── README.md                       # This file
│
├── CAD_TEMPLATES/
│   ├── PART_TEMPLATES/             # Individual part templates
│   ├── ASSEMBLY_TEMPLATES/         # Assembly templates
│   └── STARTUP_MODELS/             # Clean startup models
│
├── DRAWING_TEMPLATES/
│   ├── SHEET_FORMATS/              # A0-A4 sheet formats
│   ├── TITLE_BLOCKS/               # Standard title blocks
│   ├── SYMBOL_LIBRARIES/           # GDT, weld, electrical symbols
│   └── DRAWING_TYPES/              # Drawing type templates
│
├── DOCUMENT_TEMPLATES/
│   ├── SPECIFICATIONS/             # Spec templates
│   ├── REPORTS/                    # Report templates
│   ├── PROCEDURES/                 # Procedure templates
│   ├── CHECKLISTS/                 # Checklist templates
│   └── MEETING_NOTES/              # Meeting note templates
│
├── DATA_TEMPLATES/
│   ├── YAML_SCHEMAS/               # YAML schema templates
│   ├── CSV_FORMATS/                # CSV format templates
│   └── JSON_SCHEMAS/               # JSON schema templates
│
├── ANALYSIS_TEMPLATES/
│   ├── FEA/                        # Finite Element Analysis
│   ├── CFD/                        # Computational Fluid Dynamics
│   ├── SYSTEM_SIMULATION/          # System-level simulation
│   └── ELECTROMAGNETIC/            # EM analysis templates
│
├── PROJECT_TEMPLATES/
│   ├── DIRECTORY_STRUCTURES/       # Directory layout templates
│   ├── README_TEMPLATES/           # README templates
│   └── WORKFLOW_TEMPLATES/         # Workflow templates
│
├── CERTIFICATION_TEMPLATES/
│   ├── COMPLIANCE/                 # Compliance matrix templates
│   ├── TEST_PLANS/                 # Test plan templates
│   └── SAFETY/                     # Safety analysis templates
│
└── TEMPLATE_STANDARDS/             # Standards for templates
```

---

## Related Standards

- [AMPEL360_ASSETS_STANDARD.md](../../../../../../../AMPEL360_ASSETS_STANDARD.md) — Asset management standard
- [AMPEL360_DOCUMENTATION_STANDARD.md](../../../../../../../AMPEL360_DOCUMENTATION_STANDARD.md) — Documentation standard
- [OPT-IN_FRAMEWORK_STANDARD.md](../../../../../../../OPT-IN_FRAMEWORK_STANDARD.md) — Framework requirements

---

## Document Control

- **Template ID**: Q100-61-TPL-README-TEMPLATES
- **Version**: 1.0
- **Status**: DRAFT
- **Owner**: AMPEL360 Documentation WG
- **Last Updated**: 2025-12-05
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`

---
