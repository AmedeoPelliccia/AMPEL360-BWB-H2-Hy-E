# BREX — Business Rules Exchange

## Overview

This directory contains **Business Rules Exchange (BREX)** files for the Illustrated Parts Catalog (IPC). BREX files define project-specific validation rules that extend and constrain the base S1000D specification.

## Purpose

BREX files provide:
- Project-specific validation rules beyond S1000D schema
- Consistency enforcement across all parts data modules
- Quality assurance automation
- Compliance verification
- Configuration management support
- Corporate standards enforcement

## What is BREX?

**Business Rules Exchange (BREX)** is an S1000D mechanism for defining and sharing:
- Allowed and required XML elements and attributes
- Valid value ranges and enumerations
- Mandatory metadata
- Naming conventions
- Structure rules
- Content constraints

BREX rules are **machine-readable**, enabling automated validation tools to verify compliance before publication.

## Naming Convention

BREX files follow a standard structure:

```
BREX-AMPEL360-{PROJECT}-{VERSION}.XML
```

### Components

- **Model ID**: `AMPEL360` (fixed)
- **Project**: Identifier for rule set scope
  - `GLOBAL` - Rules for all AMPEL360 publications
  - `IPC` - Rules specific to parts catalogs
  - `ATA23` - Rules specific to ATA 23 Communications
- **Version**: `v1-0`, `v1-1`, `v2-0` (version identifier)

### Examples

**Global AMPEL360 BREX**:
```
BREX-AMPEL360-GLOBAL-v1-0.XML
```
*Project-wide rules for all technical publications*

**IPC-Specific BREX**:
```
BREX-AMPEL360-IPC-v1-0.XML
```
*Rules specific to parts catalog format*

**ATA 23-Specific BREX**:
```
BREX-AMPEL360-ATA23-v1-0.XML
```
*Rules specific to communications system documentation*

## BREX Structure

Each BREX file contains:

1. **Identification Section**
   - BREX code and title
   - Responsible organization
   - Issue and version information

2. **Context Rules**
   - Specify where rules apply
   - Define scope (DM, PM, ICN, etc.)

3. **Structure Rules**
   - Required and allowed elements
   - Element nesting constraints
   - Attribute requirements

4. **Notation Rules**
   - Naming conventions
   - Part number formats
   - Code patterns

5. **Object Rules**
   - Whole-object constraints
   - Cross-element dependencies
   - Business logic validation

## Rule Categories

### Structure Rules

**Element Requirements**:
- Which elements are required
- Which elements are forbidden
- Valid child element combinations

### Notation Rules

**Naming Patterns**:
- Data Module Code format
- ICN numbering sequences
- Part number formats
- Publication Module codes

### Value Rules

**Allowed Values**:
- Restricted enumerations
- Value ranges
- Controlled vocabularies

## Common IPC BREX Rules

### Parts Data Requirements

- Part numbers must follow format standards
- Nomenclature must use approved terminology
- Quantities must be specified
- Units of measure must be standard

### Coding Conventions

- DMC must start with "AMPEL360"
- ATA chapter must match directory structure
- ICN must follow sequential numbering
- Part number format must be valid

### Quality Standards

- All parts must have nomenclature
- Part numbers must be complete
- Vendor codes must be valid
- Quantities must be positive integers

## Validation Process

### Authoring Time

- **Real-time validation**: Editors validate against BREX as you type
- **Save validation**: Check compliance before saving
- **Warnings/Errors**: Immediate feedback on violations

### Check-in Time

- **Repository validation**: Automatic check on content commit
- **Quality gate**: Prevent non-compliant content from entering CSDB
- **Reporting**: Log violations for correction

### Publication Time

- **Pre-publication validation**: Final compliance check
- **Publication blocking**: Prevent release of non-compliant content
- **Audit trail**: Record validation results

## Best Practices

- **Clear Rules**: Write unambiguous, testable rules
- **Documentation**: Document the purpose of each rule
- **Minimal Constraints**: Only add rules that add value
- **Testing**: Validate BREX files themselves for correctness
- **Communication**: Inform authors of rule changes

## Related Directories

- `../DM/` - Data Modules validated against BREX
- `../PM/` - Publication Modules validated against BREX
- `../ICN/` - Illustrations subject to BREX rules
- `../COMMON/` - Common content validated against BREX

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 23 (Communications)
- **Section**: 23-10-00 (Speech Communications)
- **Publication Type**: IPC (Illustrated Parts Catalog)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia

## References

- S1000D Issue 5.0 Specification - Chapter 3.3 (BREX)
- AMPEL360 BREX Development Guidelines
- S1000D User Guide - BREX Best Practices
