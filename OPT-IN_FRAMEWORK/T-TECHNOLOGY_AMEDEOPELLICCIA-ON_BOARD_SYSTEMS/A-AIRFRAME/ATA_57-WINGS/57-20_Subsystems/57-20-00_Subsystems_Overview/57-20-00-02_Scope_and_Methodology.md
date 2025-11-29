# 57-20-00-02_Scope_and_Methodology

**Version:** 1.0  
**Date:** 2025-11-28  
**Status:** Draft

---

## Purpose

This document defines the scope and methodology for structuring and maintaining documentation within the 57-20_Subsystems layer of ATA 57 (Wings).

---

## Scope

### In Scope

- Physical wing subsystems that require dedicated lifecycle documentation
- Each subsystem's 14-step lifecycle content from Overview through Ops/Std/Sustain
- Traceability to global wing documentation (57-00_GENERAL)
- Cross-references to operational procedures (57-10_Operations)
- Interface specifications between wing subsystems
- Certification evidence specific to each subsystem

### Out of Scope

- Global wing-level governance (covered in 57-00_GENERAL)
- Operational procedures not specific to a subsystem (covered in 57-10_Operations)
- Avionics and software logic (covered in 57-40_Software)
- Structural analysis at wing level (covered in 57-50_Structures)

---

## Methodology

### Subsystem Identification

Each physical subsystem is assigned a unique identifier following the pattern:

```
57-2x_<SUBSYSTEM_NAME>
```

Where `x` is a sequential digit (1-9) and `<SUBSYSTEM_NAME>` is an uppercase descriptive name.

### Lifecycle Folder Structure

Each subsystem contains a GENERAL folder following the pattern:

```
57-2x_<SUBSYSTEM_NAME>/
├── 57-2x_GENERAL-<SUBSYSTEM_NAME>/
│   ├── 57-2x-01_Overview.md
│   ├── 57-2x-02_Safety.md
│   ├── 57-2x-03_Requirements.md
│   ├── 57-2x-04_Design.md
│   ├── 57-2x-05_Interfaces.md
│   ├── 57-2x-06_Engineering.md
│   ├── 57-2x-07_V_AND_V.md
│   ├── 57-2x-08_Prototyping.md
│   ├── 57-2x-09_Production_Planning.md
│   ├── 57-2x-10_Certification.md
│   ├── 57-2x-11_EIS_Versions_Tags.md
│   ├── 57-2x-12_Services.md
│   ├── 57-2x-13_Subsystems_Components.md
│   └── 57-2x-14_Ops_Std_Sustain.md
│
└── ASSETS/
    ├── DIAGRAMS/
    ├── INSTALLATIONS/
    └── EXPORTS/
```

### Naming Conventions

| Element | Pattern | Example |
|---------|---------|---------|
| Subsystem folder | `57-2x_<NAME>` | `57-21_FLAPS` |
| GENERAL folder | `57-2x_GENERAL-<NAME>` | `57-21_GENERAL-FLAPS` |
| Lifecycle file | `57-2x-YY_<Phase>.md` | `57-21-01_Overview.md` |
| Diagram asset | `57-2x-AXXX_<Description>.mermaid` | `57-21-A001_Flaps_Architecture.mermaid` |

### Traceability

Each lifecycle document must:

1. Reference relevant requirements from 57-00-03_Requirements
2. Link to related safety analyses in 57-00-02_Safety
3. Cross-reference interface specifications
4. Maintain consistency with certification evidence

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
