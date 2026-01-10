# CSDB — Common Source Database

## Overview

The Common Source Database (CSDB) is the master repository for all S1000D content. It contains structured, reusable data modules that can be assembled into various publication types.

## Directory Structure

### DM — Data Modules

Contains all technical content as individual, self-contained data modules. Each data module has a unique Data Module Code (DMC) following S1000D conventions.

**Naming Convention**: `DMC-{ModelIdentCode}-{SystemDiffCode}-{SystemCode}-{SubSystemCode}-{SubSubSystemCode}-{AssyCode}-{DisassyCode}{DisassyCodeVariant}-{InfoCode}{InfoCodeVariant}-{ItemLocationCode}_{IssueNumber}-{InWork}_{LanguageIsoCode}-{CountryIsoCode}.XML`

**Example**: `DMC-AMPEL360AT-A-31-50-10-00A-040A-A_001-00_EN-US.XML`

**Common Info Codes**:
- **040A**: Description and Operation
- **520A**: Servicing
- **720A**: Removal/Installation
- **730A**: Testing and Fault Isolation
- **940A**: Illustrated Parts Data

### PM — Publication Modules

Defines the structure and content of publications (AMM, IPC, WDM, TSM). Publication Modules reference Data Modules to assemble complete manuals.

**Naming Convention**: `PMC-{ModelIdentCode}-{PubCode}-{IssueNumber}_{InWork}_{LanguageIsoCode}-{CountryIsoCode}.XML`

**Example**: `PMC-AMPEL360AT-31-50-AMM-00001_001-00_EN-US.XML`

### ICN — Illustrations

Contains all graphics and illustrations in SVG format (preferred) or other supported formats.

**Naming Convention**: `ICN-{ModelIdentCode}-{SystemCode}-{SubSystemCode}-{FigureNumber}-{Variant}_{IssueNumber}.SVG`

**Example**: `ICN-AMPEL360AT-31-50-0001-A_001.SVG`

### BREX — Business Rules Exchange

Defines project-specific validation rules and constraints for S1000D content. BREX files ensure consistency and compliance with organizational standards.

**Reference**: All data modules must reference the project BREX in their `<brexDmRef>` element.

### DML — Data Module Lists

Lists of data modules organized by function, system, or publication. Used for configuration management and publication assembly.

### COMMON — Common Information Elements

Reusable content snippets such as:
- Warning statements
- Caution statements
- Notes
- Standard procedures
- Common terminology

### APPLICABILITY — Applicability Statements

Defines applicability conditions for content (aircraft serial numbers, effectivity, optional equipment, etc.).

## Validation

All S1000D content should be validated against:

1. **S1000D XML Schema** (descript.xsd, procedu.xsd, etc.)
2. **Project BREX** (BREX-AMPEL360AT-AIR-T_001-00.XML)
3. **Cross-reference integrity** (all referenced data modules, ICNs, and entities exist)

## Tools

Recommended S1000D authoring and validation tools:
- Oxygen XML Editor (with S1000D framework)
- Arbortext Editor
- S1000D validation utilities
- CSDB management systems

## Document Control

- **Owner**: AMPEL360 Technical Publications
- **Standard**: S1000D Issue 5.0
- **Generated with AI assistance**: GitHub Copilot, prompted by **Amedeo Pelliccia**
- **Last Updated**: 2026-01-09
