# 57-00-04_Design — ASSEMBLIES

## Purpose

This folder stores **wing-level CAD assemblies** for ATA 57, at the **chapter-general** level.

- Global wing assemblies (no subsystem-specific breakdown).
- Reference assemblies used for documentation, views, and exports.
- Source for DRAWINGS, EXPORTS, and INSTALLATIONS under `ASSETS/`.

## Scope

- **In scope**  
  - High-level wing CAD assemblies (e.g. full wing, wing + control surfaces as a whole).
  - Configurations used as references for design documentation.

- **Out of scope**  
  - Detailed FEM / CFD / analysis models (**must live in** `57-00-06_Engineering`).
  - Subsystem-specific assemblies for flaps, slats, etc.  
    (those belong under each `57-2X_*` lifecycle if needed).

## Usage Rules

- File naming pattern:  
  `57-00-04-A###_DESCRIPTION.ext`

  Examples:
  - `57-00-04-A001_Wing_Assembly.step`
  - `57-00-04-A010_Wing_Assembly_For_Drawing.step`

- Keep assemblies **versioned and tagged** via repo history and EIS tags under `57-00-11_EIS_Versions_Tags`.

## Document Control

- **Standard:** OPT-IN Framework v1.1  
- **Owner:** AMPEL360 Documentation WG  
- **Status:** DRAFT – Subject to human review and approval.
