# AMPEL360 Q100 (AMPEL360-AIR-T) — Hydrogen-Hybrid Electric BWB Aircraft

<p align="center">
  <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Active%20Development-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/ATA%20Chapters-79-orange" alt="ATA Chapters">
  <img src="https://img.shields.io/badge/Framework-OPT--IN-purple" alt="Framework">
  <img src="https://img.shields.io/badge/Publications-S1000D-teal" alt="S1000D">
</p>

<p align="center">
  <strong>Digital engineering baseline and publication-grade CSDB for a next-generation hydrogen-electric BWB aircraft.</strong>
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#how-this-repo-is-organized">Repo Organization</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#publishing-model-csdb--ietp">Publishing Model</a> •
  <a href="#standards--compliance">Standards</a> •
  <a href="#contributing">Contributing</a>
</p>

---

## Overview

**AMPEL360 Q100** is a next-generation **~100 passenger regional aircraft concept** featuring: 

| Technology | Description |
|------------|-------------|
| **Blended Wing Body (BWB)** | High aerodynamic efficiency and integrated volume |
| **H₂ PEM Fuel Cells** | Primary electrical power generation from hydrogen |
| **Distributed / Open-Fan Propulsors** | Distributed propulsion architecture for efficiency and noise reduction |
| **Peak-Power Buffering** | Buffer strategy for transients (energy management and load leveling) |
| **Circularity + DPP** | Digital Product Passport foundations for lifecycle traceability |

This repository contains a **certification-grade digital baseline** organized under the **OPT-IN Framework** and structured for **SSOT + PUB** workflows.

**Live Spec (demo):** [v0-ampel-360-aircraft-specification.vercel.app](https://v0-ampel-360-aircraft-specification.vercel.app)

---

## How This Repo Is Organized

At a high level, the repo separates **engineering truth** from **publishable deliverables**:

```
┌─────────────────────────────────────────────────────────────────┐
│                         AMPEL360-AIR-T                          │
├─────────────────────────────┬───────────────────────────────────┤
│          SSOT (Back)        │           PUB (Front)             │
│   Lifecycle Engineering     │    Controlled Deliverables        │
│   • Requirements            │    • CSDB (S1000D)                │
│   • Safety Evidence         │    • EXPORT (PDF/HTML)            │
│   • Design/ICDs             │    • IETP (Runtime)               │
│   • V&V Artifacts           │                                   │
└─────────────────────────────┴───────────────────────────────────┘
```

### SSOT (Single Source of Truth)

**SSOT** is the *system of record* for lifecycle engineering artifacts (LC01–LC14):

| Folder | Content |
|--------|---------|
| `LC01_PROBLEM_STATEMENT` | Problem definition, scope, constraints |
| `LC02_SYSTEM_REQUIREMENTS` | Requirements and traceability |
| `LC03_SAFETY_RELIABILITY` | Safety analysis, hazard logs, FMEA |
| `LC04_DESIGN_DEFINITION` | Design specs, ICDs, architecture |
| `LC05_ANALYSIS_MODELS` | FEA, CFD, thermal, performance models |
| `LC06_VERIFICATION` | Test procedures, evidence, compliance |
| `LC07_VALIDATION` | Integration and validation artifacts |
| `LC08_CONFIGURATION` | Baselines, effectivity, change control |
| `LC09_PRODUCTION` | Manufacturing specs, tooling |
| `LC10_OPERATIONS` | Operational documentation sources |
| `LC11_MAINTENANCE` | Maintenance program sources |
| `LC12_CUSTOMER_CARE` | Customer support, technical services, post-delivery care |
| `LC13_TRAINING` | Training content sources |
| `LC14_RETIREMENT_CIRCULARITY` | End-of-life, recycling, DPP |

### PUB (Publications)

**PUB** is the controlled *delivery surface*:

| Component | Purpose |
|-----------|---------|
| **CSDB** | S1000D Common Source Database (DM/PM/DML/BREX/ICN/APPLICABILITY) |
| **EXPORT** | Rendered deliverables (PDF, HTML, other outputs) per publication |
| **IETP** | Runtime "image" (viewer/config/index + packaging) for interactive delivery |

### Rule of Thumb

| If artifact is... | Place in... |
|-------------------|-------------|
| Authoritative engineering evidence | `SSOT/` |
| Publishable or deliverable | `PUB/` |

---

## OPT-IN Framework (5-Axis Topology)

The OPT-IN Framework organizes all 79 ATA chapters across five axes:

```
OPT-IN_FRAMEWORK/
├── O-ORGANIZATION/                        # Governance, policy, operational rules (ATA 00-05)
├── P-PROGRAM/                             # Program baselines, geometry, handling (ATA 06-12)
├── T-TECHNOLOGY/                          # On-board systems by domain
│   ├── A-AIRFRAME/                        # Structures (ATA 50-57)
│   ├── P-PROPULSION/                      # Powerplant (ATA 60-79)
│   ├── E2-ENERGY/                         # Electrical/thermal (ATA 24, 47, 49, 80)
│   ├── C2-CIRCULAR_CRYOGENICS_SYSTEMS/    # H₂ systems (ATA 28, 99, 100)
│   └── ...                                 # (11 more subsystem domains)
├── I-INFRASTRUCTURES/                     # Ground support, H₂ logistics, facilities (ATA 02, 03, 10, 13, 85)
└── N-NEURAL_NETWORKS/                     # AI/ML, DPP, traceability (ATA 95-98)
```

---

## Canonical ATA Content Pattern (Sub-Subject Level)

**CSDB lives at sub-subject (subproduct) level.** Each sub-subject carries both SSOT and PUB: 

```
ATA_XX-<SYSTEM>/
└── xx-yy-zz-<sub-subject>/
    ├── SSOT/
    │   ├── LC01_PROBLEM_STATEMENT/
    │   ├── LC02_SYSTEM_REQUIREMENTS/
    │   ├── LC03_SAFETY_RELIABILITY/
    │   ├── ... 
    │   └── LC14_RETIREMENT_CIRCULARITY/
    │
    └── PUB/
        └── <SUB_ID>/                    # AMM / IPC / WDM / TSM / etc.
            ├── CSDB/
            │   ├── DM/                  # Data Modules
            │   ├── PM/                  # Publication Modules
            │   ├── DML/                 # Data Module Lists
            │   ├── BREX/                # Business Rules Exchange
            │   ├── ICN/                 # Illustrations (SVG preferred)
            │   ├── COMMON/              # Reusable primitives
            │   └── APPLICABILITY/       # ACT/PCT/CCT filtering
            ├── EXPORT/                  # Rendered outputs
            └── IETP/
                ├── RUNTIME/             # Viewer application
                ├── PKG/                 # Package manifests
                └── DEPLOY/              # Deployment artifacts
```

---

## Quick Start

### Prerequisites
- Python 3.9+
- Git

### Clone and Setup

```bash
git clone https://github.com/AmedeoPelliccia/AMPEL360-AIR-T.git
cd AMPEL360-AIR-T

pip install -r requirements. txt
bash . github/hooks/setup-hooks. sh
```

### Validate Structure

```bash
python tools/ci/optin_structure_validator. py --check
python tools/ci/optin_structure_validator.py --check --chapter 31
```

### Navigate

```bash
cd OPT-IN_FRAMEWORK/
ls
```

### Entry Points by Role

| Role | Start Here |
|------|------------|
| **Engineers** | [`OPT-IN_FRAMEWORK/README.md`](./OPT-IN_FRAMEWORK/README.md) |
| **Publication Authors** | Example: `.../PUB/AMM/CSDB/README.md` (pattern at each sub-subject) |
| **Program Managers** | [`IMPLEMENTATION_SUMMARY.md`](./IMPLEMENTATION_SUMMARY.md) |
| **CAOS / Airworthiness** | [`CAOS/CAOS_INDEX. md`](./CAOS/CAOS_INDEX.md) |
| **Certification** | `XX-00-10_Certification/` folders |

---

## CAOS — Continuous Airworthiness for Operational Sustainment

**CAOS** is the framework for maintaining airworthiness throughout the operational lifecycle: 

| Domain | Scope |
|--------|-------|
| **Continued Airworthiness** | AD compliance, SB tracking, modification status |
| **Reliability Programs** | MSG-3, condition monitoring, fleet trends |
| **Operational Feedback** | In-service data, SDR/MOR analysis, operator liaison |
| **Technical Services** | Field support, AOG response, technical bulletins |
| **Configuration Control** | As-maintained vs. as-designed reconciliation |

CAOS artifacts reside primarily in: 
- `LC11_MAINTENANCE` — maintenance program sources
- `LC12_CUSTOMER_CARE` — technical services and post-delivery support
- `CAOS/` — cross-cutting CAOS documentation and dashboards

See:  [`CAOS/CAOS_INDEX. md`](./CAOS/CAOS_INDEX.md) • [`CAOS/CAOS_ARCHITECTURE.md`](./CAOS/CAOS_ARCHITECTURE.md) • [`CAOS/CAOS_OPERATIONS_FRAMEWORK. md`](./CAOS/CAOS_OPERATIONS_FRAMEWORK.md)

---

## Publishing Model (CSDB + IETP)

### CSDB (S1000D Common Source Database)

The CSDB is the **single source for modular publications**:

| Component | Purpose |
|-----------|---------|
| **DM** | Atomic content modules (descriptive, procedural, fault isolation, IPD, etc.) |
| **PM** | Publication structures that assemble DMs into deliverables |
| **DML** | Controlled lists of DMs with status and applicability |
| **BREX** | Business rules for validation and compliance checking |
| **ICN** | Graphics (SVG preferred) referenced by DMs |
| **APPLICABILITY** | ACT/PCT/CCT for product/condition filtering |
| **COMMON** | Reusable content primitives (warnings, cautions, notes) |

### IETP (Interactive Electronic Technical Publication)

HTML/PDF are outputs; the **IETP runtime** is the deliverable software "image" that: 
- Consumes PM/DM sets from CSDB
- Applies applicability rules (ACT/PCT/CCT)
- Provides interactive navigation, search, and filtering
- Is packaged and versioned in `PUB/<SUB_ID>/IETP/`

---

## KNOT → KNU (Controlled Uncertainty Handling)

Work in this repository is managed through **KNOTs** and **KNUs**:

| Concept | Definition |
|---------|------------|
| **KNOT** | A *known unknown* — an identified uncertainty or problem node requiring resolution |
| **KNU** | A *Knowledge Unit* — a concrete artifact that addresses a KNOT |

### How It Works

1. **KNOT Identification**: An uncertainty is logged (e.g., "H₂ tank thermal cycling limits undefined")
2. **KNU Production**: Work produces artifacts in SSOT and/or PUB (requirements, ICDs, analyses, DMs, ICNs, etc.)
3. **KNOT Closure**: The KNOT is "done" when required KNUs exist, are linked, and reduce residual uncertainty to acceptable levels

This provides **traceability from uncertainty to evidence** across the engineering and publication lifecycle.

---

## Standards & Compliance

| Standard | Application |
|----------|-------------|
| **EASA CS-25 / FAA Part 25** | Airworthiness requirements framing |
| **ATA iSpec 2200** | Chapter/section/subject scaffolding for system breakdown |
| **S1000D (+ project BREX)** | Technical publications CSDB (DM/PM/DML/ICN/APPLICABILITY) |
| **DO-178C** | Software considerations in airborne systems |
| **DO-254** | Hardware design assurance |
| **DO-160** | Environmental qualification |
| **ISO 15926** | Industrial data standards |

---

## Key Documentation

| Document | Description |
|----------|-------------|
| [OPT-IN Framework Standard](./OPT-IN_FRAMEWORK_STANDARD.md) | Complete framework specification |
| [Documentation Standard](./AMPEL360_DOCUMENTATION_STANDARD.md) | Formatting and structure guidelines |
| [AI→ASI Transition Proposal](./AI-ASI-TP.md) | AI→ASI transition roadmap:  governance, assurance, and certification-grade adoption across SSOT+PUB |
| [Digital Twin Control Loop](./DIGITAL_TWIN_CONTROL_LOOP. md) | Digital twin architecture and data flows |
| [CAOS Index](./CAOS/CAOS_INDEX.md) | Continuous Airworthiness for Operational Sustainment |
| [CAOS Architecture](./CAOS/CAOS_ARCHITECTURE.md) | CAOS system architecture |
| [CAOS Operations Framework](./CAOS/CAOS_OPERATIONS_FRAMEWORK.md) | CAOS operational playbook |

---

## Contributing

1. **Fork** the repository
2. **Setup hooks**:  `bash .github/hooks/setup-hooks.sh`
3. **Follow** the SSOT + PUB pattern and OPT-IN structure
4. **Validate**: `python tools/ci/optin_structure_validator.py --check`
5. **Submit** a pull request

### Contribution Rules

| Rule | Guidance |
|------|----------|
| **Narrative docs** | Use Markdown (`.md`) — not `.pdf`, `.docx` |
| **Matrices/logs** | Use CSV (`.csv`) — not `.xlsx` |
| **Graphics** | Prefer SVG for illustrations (ICN) |
| **S1000D content** | Keep XML/BREX compliant under `PUB/**/CSDB/**` |
| **References** | Ensure DM ↔ ICN ↔ PM ↔ DML ↔ APPLICABILITY resolve correctly |
| **Safety-critical** | Include DO-178C compliance tags where applicable |

---

## License

Apache 2.0 — see [LICENSE](./LICENSE).

---

## Acknowledgments

- **Concept & Direction**:  Amedeo Pelliccia
- **AI Assistance**: GitHub Copilot (documentation generation)
- **Framework Design**: OPT-IN Framework

---

<p align="center">
  <strong>AMPEL360 Q100</strong> — Digital engineering, traceability, and publication-grade CSDB for sustainable aviation. 
</p>

<p align="center">
  <em>By Amedeo Pelliccia • AI-Assisted Development</em>
</p>


  <i>Last AI update: Added S1000D DML breakdown for ATA 31-00-00 - 2026-01-10</i>
</p>


