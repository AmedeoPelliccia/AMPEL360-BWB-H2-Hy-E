# Contributing to ATA 74-20 Subsystem Documentation

## Overview

This folder contains the template structure for ATA Chapter 74 (Ignition) subsystem documentation following the **LRU/LRI/BOM/LMP/CIR** logic.

## Folder Structure

```text
ATA_74-20_SUBSYSTEM_TEMPLATE/
├── LRU_74-20-XX_Overview.md       # LRU overview document
├── meta/
│   ├── 74-20-XX_SUBSYSTEM.yaml    # Machine-readable metadata
│   └── CONTRIBUTING.md                    # This file
└── LRI/
    ├── LRI_01_ComponentA/
    │   ├── 74-20-XX_Design.md     # Design specifications
    │   ├── CIR_LINKS.md                   # References to CIR assets
    │   └── BOM_LMP.md                     # Bill of Materials & Line Maintenance Parts
    ├── LRI_02_ComponentB/
    │   └── ...
    └── LRI_03_ComponentC/
        └── ...
```

## Terminology

| Term | Definition |
|------|------------|
| **LRU** | Line Replaceable Unit |
| **LRI** | Line Replaceable Item |
| **BOM** | Bill of Materials |
| **LMP** | Line Maintenance Parts |
| **CIR** | Configuration Item Reference |

## How to Use

1. Copy the entire `ATA_74-20_SUBSYSTEM_TEMPLATE/` folder
2. Rename to match your subsystem: `ATA_74-20-YY_[SUBSYSTEM_NAME]/`
3. Replace all `XX` placeholders with actual sequence number `YY`
4. Update metadata in `meta/74-20-YY_SUBSYSTEM.yaml`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
